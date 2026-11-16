"""Line coverage tests: exercise every return and executable statement."""

import pytest

from elevator_dispatch import door_action, next_direction, pick_elevator


@pytest.mark.parametrize(
    "direction, requests, expected",
    [
        ("up", [7], "up"),
        ("up", [1], "down"),
        ("up", [], "idle"),
        ("down", [1], "down"),
        ("down", [7], "up"),
        ("down", [], "idle"),
        ("idle", [7], "up"),
        ("idle", [1], "down"),
        ("idle", [], "idle"),
    ],
)
def test_direction_returns(direction, requests, expected):
    assert next_direction(3, direction, requests) == expected


@pytest.mark.parametrize(
    "load, blocked, emergency, expected",
    [
        (100, False, True, "hold_open"),
        (631, False, False, "overload"),
        (100, True, False, "reopen"),
        (100, False, False, "close"),
    ],
)
def test_door_returns(load, blocked, emergency, expected):
    assert door_action(load, blocked, emergency) == expected


def test_closer_car_replaces_first_car():
    # A's score is abs(1 - 5) + 5 = 9; B's score is abs(4 - 5) = 1.
    assert pick_elevator([("A", 1, False), ("B", 4, True)], 5) == "B"
