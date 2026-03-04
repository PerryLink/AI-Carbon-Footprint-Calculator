"""Tests for comparison functionality."""

from ai_carbon_footprint.comparisons import get_comparisons


def test_get_comparisons_large_value():
    """Test comparisons for large CO2 values."""
    comparisons = get_comparisons(5000)

    assert len(comparisons) <= 3
    assert all("name" in c and "emoji" in c and "equivalent" in c for c in comparisons)

    # Should include car_year comparison (5000 / 4600 ≈ 1.09)
    car_comp = next((c for c in comparisons if "车" in c["name"]), None)
    assert car_comp is not None
    assert 0.5 < car_comp["equivalent"] < 2


def test_get_comparisons_medium_value():
    """Test comparisons for medium CO2 values."""
    comparisons = get_comparisons(400)

    assert len(comparisons) <= 3

    # Should include home electricity comparison (400 / 400 = 1.0)
    home_comp = next((c for c in comparisons if "家庭" in c["name"]), None)
    assert home_comp is not None
    assert 0.5 < home_comp["equivalent"] < 2


def test_get_comparisons_small_value():
    """Test comparisons for small CO2 values."""
    comparisons = get_comparisons(20)

    assert len(comparisons) <= 3

    # Should include tree comparison (20 / 21 ≈ 0.95)
    tree_comp = next((c for c in comparisons if "树" in c["name"]), None)
    assert tree_comp is not None


def test_comparisons_sorted_by_relevance():
    """Test that comparisons are sorted by relevance."""
    comparisons = get_comparisons(1000)

    if len(comparisons) > 1:
        # First comparison should be closest to 1.0 ratio
        first_ratio = abs(1 - comparisons[0]["equivalent"])
        second_ratio = abs(1 - comparisons[1]["equivalent"])
        assert first_ratio <= second_ratio
