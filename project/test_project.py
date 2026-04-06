import pytest
from project import get_military_minutes
from project import is_valid_time
from project import is_valid_event, event_list

def setup():
    for i in event_list:
        event_list[i] = [""] * 7

def test_get_military_minutes():
    assert get_military_minutes(5, 0, "AM") == 300
    assert get_military_minutes(6, 0, "AM") == 360
    assert get_military_minutes(1, 30, "AM") == 90
    assert get_military_minutes(3, 56, "AM") == 236
    assert get_military_minutes(12, 0, "AM") == 0
    assert get_military_minutes(5, 0, "PM") == 1020
    assert get_military_minutes(6, 0, "PM") == 1080
    assert get_military_minutes(1, 30, "PM") == 810
    assert get_military_minutes(3, 56, "PM") == 956
    assert get_military_minutes(12, 0, "PM") == 720



def test_is_valid_time():
    assert is_valid_time("9:00 AM to 11:00 AM") == (540, 660)
    assert is_valid_time("9 AM - 11 AM") is None
    assert is_valid_time("5:00 PM to 4:00 PM") is None
    assert is_valid_time("3:00 PM to 3:00 PM") is None
    assert is_valid_time("12:00 AM to 1:00 AM") == (0, 60)
    assert is_valid_time("12:00 PM to 1:00 PM") == (720, 780)

def test_is_valid_event():
    assert is_valid_event(540, 600, "Monday") == True
    setup()
    event_list[9][0] = "Busy"
    assert is_valid_event(540, 600, "Monday") == False
    setup()
    event_list[9][1] = "Busy"
    assert is_valid_event(540, 600, "Monday")
    setup()
    event_list[9][0] = "Busy"
    event_list[10][0] = "Busy"
    assert is_valid_event(540, 660, "Monday") == False