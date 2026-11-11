import pytest

from bus_transit_fare import (
    process_commute_manifest,
    inspect_smartcard_turnstiles
)


# 1. Input validation branches
def test_validation_branches():
    with pytest.raises(ValueError):
        process_commute_manifest("invalid", 2.0)

    with pytest.raises(ValueError):
        process_commute_manifest([], -1.0)

    assert process_commute_manifest([], 2.0)["status"] == "ZERO_RIDERSHIP"


# 2. All route type branches
def test_all_route_types():
    manifests = [
        {
            "route_active": True,
            "route_type": "express",
            "commuters": [{"zones": 1}]
        },
        {
            "route_active": True,
            "route_type": "shuttle",
            "commuters": [{"zones": 1}]
        },
        {
            "route_active": True,
            "route_type": "local",
            "commuters": [{"zones": 1}]
        },
        {
            "route_active": True,
            "route_type": "unknown",
            "commuters": []
        },
        {
            "route_active": False,
            "route_type": "local",
            "commuters": [{"zones": 2}]
        }
    ]

    result = process_commute_manifest(manifests, 2.0)

    assert result["total_fare"] == 15.5
    assert result["status"] == "COMPLETED"


# 3. Passenger category and zone branches
def test_passenger_and_zone_branches():
    manifests = [
        {
            "route_active": True,
            "route_type": "local",
            "priority_boarding": True,
            "commuters": [
                {"zones": 2, "type": "student"},
                {"zones": 1, "type": "senior"},
                {"zones": 1, "type": "regular"},
                {"zones": 0, "type": "regular"},
                {"zones": -1, "type": "regular"},
                {"zones": 1, "blacklisted": True}
            ]
        }
    ]

    result = process_commute_manifest(manifests, 2.0)

    assert result["total_fare"] == 9.35
    assert result["status"] == "COMPLETED"


# 4. Express blacklisted-card branch
def test_blacklisted_express_branch():
    manifests = [
        {
            "route_active": True,
            "route_type": "express",
            "priority_boarding": True,
            "commuters": [
                {"zones": 1, "type": "regular"},
                {"zones": 1, "blacklisted": True},
                {"zones": 2, "type": "student"}
            ]
        }
    ]

    result = process_commute_manifest(manifests, 2.0)

    assert result["total_fare"] == 2.0
    assert result["status"] == "COMPLETED"


# 5. Default values and empty commuter branch
def test_default_values_and_empty_commuters():
    manifests = [
        {
            "route_active": True,
            "commuters": [{}]
        },
        {
            "route_active": True,
            "route_type": "local",
            "commuters": []
        },
        {}
    ]

    result = process_commute_manifest(manifests, 0)

    assert result["total_fare"] == 3.5
    assert result["status"] == "COMPLETED"


# 6. Audit rejection branch
def test_audit_rejection_branch():
    manifests = [
        {"route_active": True, "route_type": "invalid"}
        for _ in range(5)
    ]

    result = process_commute_manifest(manifests, 0)

    assert result["status"] == "AUDIT_REJECTED"


# 7. Turnstile empty matrix branch
def test_no_turnstile_data():
    assert inspect_smartcard_turnstiles([]) == "NO_DATA"


# 8. Operational turnstile branches
def test_operational_turnstile_branches():
    matrix = [
        [],
        [4, 1, 4],
        [2, 3, 1]
    ]

    assert inspect_smartcard_turnstiles(matrix) == "OPERATIONAL"


# 9. Turnstile jam branch
def test_turnstile_jam_branch():
    matrix = [
        [2, 4, 5]
    ]

    assert inspect_smartcard_turnstiles(matrix) == "TURNSTILE_JAM"