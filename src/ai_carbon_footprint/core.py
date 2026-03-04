"""Core carbon footprint calculation logic."""

from typing import Dict
from ai_carbon_footprint.data import GPU_SPECS, CARBON_INTENSITY, DEFAULT_PUE


def calculate_carbon_footprint(
    gpu_model: str,
    hours: float,
    num_gpus: int = 1,
    pue: float = DEFAULT_PUE,
    region: str = "global",
    utilization: float = 1.0,
) -> Dict:
    """Calculate carbon footprint for AI compute workload.

    Args:
        gpu_model: GPU model identifier (e.g., "A100")
        hours: Runtime in hours
        num_gpus: Number of GPUs
        pue: Power Usage Effectiveness coefficient
        region: Geographic region for carbon intensity
        utilization: GPU utilization rate (0-1)

    Returns:
        Dictionary with calculation results
    """
    if gpu_model not in GPU_SPECS:
        raise ValueError(f"Unknown GPU model: {gpu_model}")

    if region not in CARBON_INTENSITY:
        raise ValueError(f"Unknown region: {region}")

    if not 0 < utilization <= 1:
        raise ValueError("Utilization must be between 0 and 1")

    gpu_spec = GPU_SPECS[gpu_model]
    tdp_watts = gpu_spec["tdp"]

    # Calculate energy consumption
    gpu_energy_kwh = (tdp_watts * hours * num_gpus * utilization) / 1000
    total_energy_kwh = gpu_energy_kwh * pue

    # Calculate CO2 emissions
    carbon_intensity = CARBON_INTENSITY[region]
    co2_kg = total_energy_kwh * carbon_intensity

    return {
        "gpu_name": gpu_spec["name"],
        "gpu_model": gpu_model,
        "num_gpus": num_gpus,
        "hours": hours,
        "utilization": utilization,
        "pue": pue,
        "region": region,
        "energy_kwh": gpu_energy_kwh,
        "total_energy_kwh": total_energy_kwh,
        "co2_kg": co2_kg,
        "carbon_intensity": carbon_intensity,
    }
