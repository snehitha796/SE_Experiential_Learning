import pytest

from bus_transit_fare import (
    process_commute_manifest,
    inspect_smartcard_turnstiles
)


# 1. Invalid input tests
def test_invalid_manifests():
    with pytest.raises(ValueError):
        process_commute_manifest("invalid", 2.0)


def test_negative_booking_fee():
    with pytest.raises(ValueError):
        process_commute_manifest([], -1.0)


# 2. Route types, passenger categories and fare calculation
def test_route_types_and_passenger_categories():
    manifests = [
        {
            "route_active": True,
            "route_type": "local",
            "priority_boarding": True,
            "commuters": [
                {"zones": 2, "type": "regular"},
                {"zones": 2, "type": "student"},
                {"zones": 1, "type": "senior"},
                {"zones": 1, "blacklisted": True},
                {"zones": 0, "type": "regular"}
            ]
        },
        {
            "route_active": True,
            "route_type": "express",
            "priority_boarding": True,
            "commuters": [
                {"zones": 1, "type": "regular"},
                {"zones": 1, "blacklisted": True},
                {"zones": 2, "type": "student"}
            ]
        },
        {
            "route_active": True,
            "route_type": "shuttle",
            "commuters": [
                {"zones": 1, "type": "regular"}
            ]
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

    assert result["total_fare"] == 17.35
    assert result["status"] == "COMPLETED"


# 3. Default values and empty commuters
def test_empty_commuters_and_default_route():
    manifests = [
        {
            "route_active": True,
            "commuters": []
        },
        {
            "route_active": True,
            "commuters": [
                {}
            ]
        }
    ]

    result = process_commute_manifest(manifests, 0)

    assert result["total_fare"] == 3.5
    assert result["status"] == "COMPLETED"


# 4. Audit rejection
def test_audit_rejected():
    manifests = [
        {"route_active": True, "route_type": "unknown"}
        for _ in range(5)
    ]

    result = process_commute_manifest(manifests, 2.0)

    assert result["total_fare"] == 0.0
    assert result["status"] == "AUDIT_REJECTED"


# 5. Zero ridership
def test_zero_ridership():
    result = process_commute_manifest([], 2.0)

    assert result["total_fare"] == 0.0
    assert result["status"] == "ZERO_RIDERSHIP"


# 6. Smartcard turnstile tests
def test_empty_turnstile_matrix():
    assert inspect_smartcard_turnstiles([]) == "NO_DATA"


def test_operational_turnstile():
    matrix = [
        [4, 2, 4],
        []
    ]

    assert inspect_smartcard_turnstiles(matrix) == "OPERATIONAL"


def test_turnstile_jam():
    matrix = [
        [4, 5, 1]
    ]

    assert inspect_smartcard_turnstiles(matrix) == "TURNSTILE_JAM"