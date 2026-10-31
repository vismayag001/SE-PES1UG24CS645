
import pytest

from irrigation_scheduler import should_irrigate, water_volume, schedule


# ==========================================
# 1. TEST should_irrigate()
# ==========================================

def test_moisture_above_limit():
    assert should_irrigate(70, 0, "seedling") is False


def test_high_rainfall():
    assert should_irrigate(30, 10, "seedling") is False


def test_seedling_needs_water():
    assert should_irrigate(40, 0, "seedling") is True


def test_seedling_does_not_need_water():
    assert should_irrigate(50, 0, "seedling") is False


def test_flowering_needs_water():
    assert should_irrigate(50, 0, "flowering") is True


def test_flowering_does_not_need_water():
    assert should_irrigate(55, 0, "flowering") is False


def test_other_stage_rainfall_limit():
    assert should_irrigate(30, 5, "mature") is False


def test_other_stage_needs_water():
    assert should_irrigate(30, 0, "mature") is True


def test_other_stage_does_not_need_water():
    assert should_irrigate(45, 0, "mature") is False


# ==========================================
# 2. TEST water_volume()
# ==========================================

def test_invalid_area():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)


def test_flowering_volume():
    assert water_volume(10, "flowering", 20) == 50


def test_other_stage_volume():
    assert water_volume(10, "mature", 20) == 40


def test_high_temperature():
    assert water_volume(10, "seedling", 40) == 30


def test_low_temperature():
    assert water_volume(10, "seedling", 5) == 10


# ==========================================
# 3. TEST schedule()
# ==========================================

def test_schedule_with_multiple_zones():
    zones = [
        ("Zone1", 10, 70, 0, "seedling", 20),
        ("Zone2", 10, 30, 0, "seedling", 20),
        ("Zone3", 10, 30, 0, "flowering", 20),
        ("Zone4", 10, 30, 0, "seedling", 20)
    ]

    result = schedule(zones, 25)

    assert result == ["Zone2"]


def test_empty_schedule():
    assert schedule([], 100) == []
