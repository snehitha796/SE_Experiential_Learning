import pytest
from hypothesis import given, strategies as st
from processor import process_age, process_fare, process_passenger_name

@given(st.one_of(st.integers(), st.floats(), st.text(), st.none()))
def test_process_age_no_crash(val):
    try:
        res = process_age(val)
        if res is not None:
            assert isinstance(res, int)
            assert 0 <= res <= 120
    except (ValueError, TypeError):
        pass
    except Exception as e:
        pytest.fail(f"process_age crashed with {type(e).__name__}: {e}")

@given(st.one_of(st.integers(), st.floats(), st.text(), st.none()))
def test_process_fare_no_crash(val):
    try:
        res = process_fare(val)
        if res is not None:
            assert isinstance(res, (int, float))
            assert res >= 0
    except (ValueError, TypeError):
        pass
    except Exception as e:
        pytest.fail(f"process_fare crashed with {type(e).__name__}: {e}")

@given(st.one_of(st.text(), st.integers(), st.none()))
def test_process_passenger_name_no_crash(val):
    try:
        res = process_passenger_name(val)
        if res is not None:
            assert isinstance(res, str)
            assert len(res) > 0
    except (ValueError, TypeError):
        pass
    except Exception as e:
        pytest.fail(f"process_passenger_name crashed with {type(e).__name__}: {e}")