"""Data models used by the Polynomial Alien Life Qualifier."""

from dataclasses import dataclass, field
from typing import Callable, Dict, List


@dataclass
class AlienCandidate:
    """Represents a hypothetical alien-life candidate."""

    name: str
    parameters: Dict[str, float]

    def get(self, parameter: str) -> float:
        """Return a parameter value.

        Raises:
            KeyError: If the requested parameter does not exist.
        """
        return self.parameters[parameter]


@dataclass
class PolynomialConstraint:
    """A polynomial constraint used to qualify a candidate.

    The function should return a numerical value. A candidate satisfies
    the constraint when the absolute value of that result is within
    the specified tolerance.
    """

    name: str
    function: Callable[[Dict[str, float]], float]
    tolerance: float = 1e-6
    description: str = ""

    def evaluate(self, parameters: Dict[str, float]) -> float:
        """Evaluate the polynomial against a set of parameters."""
        return float(self.function(parameters))

    def satisfied(self, parameters: Dict[str, float]) -> bool:
        """Return True if the polynomial constraint is satisfied."""
        value = self.evaluate(parameters)
        return abs(value) <= self.tolerance


@dataclass
class QualificationResult:
    """Stores the result of qualifying an alien candidate."""

    candidate_name: str
    qualified: bool
    passed_constraints: List[str] = field(default_factory=list)
    failed_constraints: List[str] = field(default_factory=list)
    values: Dict[str, float] = field(default_factory=dict)

    @property
    def total_constraints(self) -> int:
        """Return the number of evaluated constraints."""
        return len(self.passed_constraints) + len(self.failed_constraints)

    @property
    def score(self) -> float:
        """Return the percentage of constraints that passed."""
        if self.total_constraints == 0:
            return 0.0

        return len(self.passed_constraints) / self.total_constraints

    def summary(self) -> str:
        """Return a human-readable summary."""
        status = "QUALIFIED" if self.qualified else "NOT QUALIFIED"

        lines = [
            f"Candidate: {self.candidate_name}",
            f"Status: {status}",
            (
                f"Constraints: "
                f"{len(self.passed_constraints)}/{self.total_constraints} passed"
            ),
            f"Score: {self.score:.1%}",
        ]

        if self.failed_constraints:
            lines.append("Failed constraints:")
            for constraint in self.failed_constraints:
                lines.append(f"  - {constraint}")

        return "\n".join(lines)
