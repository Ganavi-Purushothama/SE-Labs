
from hypothesis import given, strategies as st
from elevator_dispatch import (
    parse_request,
    total_travel,
    load_percent
)


# TEST 1: parse_request
@given(st.one_of(st.text(), st.none()))
def test_parse_request_no_crash(s):
    result = parse_request(s)
    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
    )


@given(st.integers(min_value=0), st.integers(min_value=0))
def test_parse_request_valid(start, end):
    assert parse_request(f"{start}->{end}") == (start, end)


# TEST 2: total_travel
@given(st.one_of(st.text(), st.none()))
def test_total_travel_no_crash(s):
    result = total_travel(s)
    assert result is None or (
        isinstance(result, int) and result >= 0
    )


@given(st.lists(st.integers(min_value=0), min_size=1))
def test_total_travel_valid(floors):
    csv = ",".join(map(str, floors))

    expected = sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )

    assert total_travel(csv) == expected


# TEST 3: load_percent
@given(st.one_of(st.text(), st.none()))
def test_load_percent_no_crash(s):
    result = load_percent(s)
    assert result is None or (
        isinstance(result, int) and result >= 0
    )


@given(
    st.integers(min_value=0),
    st.integers(min_value=1)
)
def test_load_percent_valid(load, capacity):
    result = load_percent(f"{load} of {capacity}")
    assert result == load * 100 // capacity
