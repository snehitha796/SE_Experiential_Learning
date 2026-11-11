import pytest
from hypothesis import given, strategies as st
from processor import parse_transit_corridor, lookup_concession_discount, compute_passenger_density

# Fuzz Test 1: Transit Corridor Code Parsing
@given(st.one_of(st.text(), st.integers(), st.none()))
def test_parse_transit_corridor_no_crash(val):
    try:
        res = parse_transit_corridor(val)
        if res is not None:
            assert isinstance(res, str)
    except (ValueError, TypeError, KeyError):
        pass  # Expected handled defensive exceptions
    except Exception as e:
        pytest.fail(f"parse_transit_corridor crashed unexpectedly with {type(e).__name__}: {e}")

# Fuzz Test 2: Concession Discount Lookup
@given(st.one_of(st.text(), st.integers(), st.none()))
def test_lookup_concession_discount_no_crash(val):
    try:
        res = lookup_concession_discount(val)
        if res is not None:
            assert isinstance(res, (int, float))
    except (ValueError, TypeError, KeyError):
        pass
    except Exception as e:
        pytest.fail(f"lookup_concession_discount crashed unexpectedly with {type(e).__name__}: {e}")

# Fuzz Test 3: Passenger Density Computation
@given(st.one_of(st.text(), st.integers(), st.none()))
def test_compute_passenger_density_no_crash(val):
    try:
        res = compute_passenger_density(val)
        if res is not None:
            assert isinstance(res, (int, float))
    except (ValueError, TypeError, ZeroDivisionError):
        pass
    except Exception as e:
        pytest.fail(f"compute_passenger_density crashed unexpectedly with {type(e).__name__}: {e}")