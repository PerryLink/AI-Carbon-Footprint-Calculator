"""Concrete comparisons for carbon emissions."""

from typing import List, Dict

COMPARISONS = {
    "car_year": {"name": "燃油车行驶一年", "co2_kg": 4600, "emoji": "🚗"},
    "flight_nyc_london": {"name": "纽约-伦敦往返航班", "co2_kg": 1100, "emoji": "✈️"},
    "tree_year": {"name": "树木一年吸收的CO2", "co2_kg": 21, "emoji": "🌳"},
    "smartphone_charge": {"name": "智能手机充电", "co2_kg": 0.008, "emoji": "📱"},
    "home_electricity_month": {"name": "家庭一个月用电", "co2_kg": 400, "emoji": "🏠"},
}


def get_comparisons(co2_kg: float) -> List[Dict]:
    """Get relevant comparisons for the given CO2 amount.

    Args:
        co2_kg: CO2 emissions in kilograms

    Returns:
        List of comparison dictionaries with calculated equivalents
    """
    results = []

    for key, comp in COMPARISONS.items():
        ratio = co2_kg / comp["co2_kg"]

        # Select comparisons in reasonable range (0.1x to 10x)
        if 0.1 <= ratio <= 10:
            results.append({
                "name": comp["name"],
                "emoji": comp["emoji"],
                "equivalent": ratio,
                "unit_co2": comp["co2_kg"],
            })

    # Sort by how close to 1.0 the ratio is
    results.sort(key=lambda x: abs(1 - x["equivalent"]))

    # Return top 3 most relevant
    return results[:3]
