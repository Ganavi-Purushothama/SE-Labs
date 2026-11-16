"""Branch coverage tests, including boundaries, precedence, and ties."""

import pytest

from elevator_dispatch import door_action, next_direction, pick_elevator


@pytest.mark.parametrize("direction", ["up", "down", "idle"])
@pytest.mark.parametrize("requests", [[], [3], [3, 3]])
def test_no_other_floor_requests(direction, requests):
    assert next_direction(3, direction, requests) == "idle"


@pytest.mark.parametrize(
    "direction, requests, expected",
    [
        ("up", [7], "up"),
        ("up", [1], "down"),
        ("up", [1, 3, 7], "up"),
        ("down", [1], "down"),
        ("down", [7], "up"),
        ("down", [1, 3, 7], "down"),
        ("idle", [7], "up"),
        ("idle", [1], "down"),
        ("idle", [1, 3, 7], "up"),
    ],
)
def test_direction_decisions(direction, requests, expected):
    assert next_direction(3, direction, requests) == expected


@pytest.mark.parametrize(
    "load, blocked, emergency, expected",
    [
        (100, False, True, "hold_open"),
        (631, True, True, "hold_open"),
        (631, False, False, "overload"),
        (631, True, False, "overload"),
        (629, False, False, "close"),
        (630, False, False, "close"),
        (630, True, False, "reopen"),
    ],
)
def test_door_boundaries_and_priority(load, blocked, emergency, expected):
    assert door_action(load, blocked, emergency) == expected


@pytest.mark.parametrize(
    "cars, floor, expected",
    [
        ([], 5, None),
        ([("A", 5, True)], 5, "A"),
        ([("A", 5, False)], 5, "A"),
        ([("A", 1, True), ("B", 4, True)], 5, "B"),
        ([("A", 4, True), ("B", 1, True)], 5, "A"),
        ([("A", 3, True), ("B", 7, True)], 5, "A"),
        ([("A", 5, False), ("B", 9, True)], 5, "B"),
        ([("A", 5, False), ("B", 10, True)], 5, "A"),
        ([("A", 4, True), ("B", 5, False)], 5, "A"),
        ([("A", 1, False), ("B", 4, False)], 5, "B"),
    ],
)
def test_car_selection(cars, floor, expected):
    assert pick_elevator(cars, floor) == expected
