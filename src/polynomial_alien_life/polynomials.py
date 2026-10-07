"""Polynomial functions used by the default alien-life model."""

from typing import Dict


def metabolic_balance(p: Dict[str, float]) -> float:
    """Model metabolic balance.

    A simple hypothetical relationship between available energy,
    temperature, and metabolic activity.

    P = energy - temperature * metabolic_rate
    """
    return p["energy"] - p["temperature"] * p["metabolic_rate"]


def environmental_pressure(p: Dict[str, float]) -> float:
    """Model environmental pressure compatibility.

    P = pressure * tolerance - 1
    """
    return p["pressure"] * p["pressure_tolerance"] - 1.0


def resource_balance(p: Dict[str, float]) -> float:
    """Model resource availability.

    P = resources - population * consumption
    """
    return p["resources"] - (
        p["population"] * p["resource_consumption"]
    )


def thermal_stability(p: Dict[str, float]) -> float:
    """Model thermal stability.

    P = temperature^2 - optimal_temperature^2

    This represents a simplified symmetric thermal relationship.
    """
    return (
        p["temperature"] ** 2
        - p["optimal_temperature"] ** 2
    )


def biological_complexity(p: Dict[str, float]) -> float:
    """Model biological complexity.

    P = complexity * energy - minimum_complexity_energy
    """
    return (
        p["complexity"] * p["energy"]
        - p["minimum_complexity_energy"]
    )
