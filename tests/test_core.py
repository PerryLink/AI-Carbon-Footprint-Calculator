"""Tests for core carbon footprint calculation."""

import pytest
from ai_carbon_footprint.core import calculate_carbon_footprint


def test_basic_calculation():
    """Test basic carbon footprint calculation."""
    result = calculate_carbon_footprint("A100", 1000, num_gpus=1)

    assert result["gpu_model"] == "A100"
    assert result["gpu_name"] == "NVIDIA A100"
    assert result["hours"] == 1000
    assert result["num_gpus"] == 1
    assert result["energy_kwh"] == 400.0  # 400W * 1000h / 1000
    assert result["total_energy_kwh"] == 632.0  # 400 * 1.58
    assert result["co2_kg"] == pytest.approx(300.2, rel=0.01)  # 632 * 0.475


def test_multiple_gpus():
    """Test calculation with multiple GPUs."""
    result = calculate_carbon_footprint("A100", 100, num_gpus=8)

    assert result["num_gpus"] == 8
    assert result["energy_kwh"] == 320.0  # 400W * 100h * 8 / 1000


def test_custom_pue():
    """Test calculation with custom PUE."""
    result = calculate_carbon_footprint("A100", 100, pue=1.2)

    assert result["pue"] == 1.2
    assert result["total_energy_kwh"] == 48.0  # 40 * 1.2


def test_different_region():
    """Test calculation with different carbon intensity."""
    result = calculate_carbon_footprint("A100", 100, region="france")

    assert result["region"] == "france"
    assert result["carbon_intensity"] == 0.056


def test_gpu_utilization():
    """Test calculation with GPU utilization."""
    result = calculate_carbon_footprint("A100", 100, utilization=0.5)

    assert result["utilization"] == 0.5
    assert result["energy_kwh"] == 20.0  # 400W * 100h * 0.5 / 1000


def test_invalid_gpu():
    """Test error handling for invalid GPU model."""
    with pytest.raises(ValueError, match="Unknown GPU model"):
        calculate_carbon_footprint("INVALID_GPU", 100)


def test_invalid_region():
    """Test error handling for invalid region."""
    with pytest.raises(ValueError, match="Unknown region"):
        calculate_carbon_footprint("A100", 100, region="invalid")


def test_invalid_utilization():
    """Test error handling for invalid utilization."""
    with pytest.raises(ValueError, match="Utilization must be between 0 and 1"):
        calculate_carbon_footprint("A100", 100, utilization=1.5)
