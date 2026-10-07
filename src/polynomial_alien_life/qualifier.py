"""Alien-life qualification engine."""

from typing import Iterable, List

from .models import (
    AlienCandidate,
    PolynomialConstraint,
    QualificationResult,
)


class AlienLifeQualifier:
    """Evaluates candidates against polynomial constraints."""

    def __init__(
        self,
        constraints: Iterable[PolynomialConstraint],
        require_all: bool = True,
    ) -> None:
        self.constraints: List[PolynomialConstraint] = list(constraints)
        self.require_all = require_all

    def qualify(
        self,
        candidate: AlienCandidate,
    ) -> QualificationResult:
        """Evaluate an alien candidate.

        Args:
            candidate: Candidate to evaluate.

        Returns:
            QualificationResult containing the evaluation details.
        """
        passed = []
        failed = []
        values = {}

        for constraint in self.constraints:
            try:
                value = constraint.evaluate(candidate.parameters)
                values[constraint.name] = value

                if constraint.satisfied(candidate.parameters):
                    passed.append(constraint.name)
                else:
                    failed.append(constraint.name)

            except KeyError as exc:
                failed.append(
                    f"{constraint.name} (missing parameter: {exc.args[0]})"
                )

        if self.require_all:
            qualified = len(failed) == 0
        else:
            qualified = len(passed) > 0

        return QualificationResult(
            candidate_name=candidate.name,
            qualified=qualified,
            passed_constraints=passed,
            failed_constraints=failed,
            values=values,
        )

    def qualify_many(
        self,
        candidates: Iterable[AlienCandidate],
    ) -> List[QualificationResult]:
        """Qualify multiple candidates."""
        return [self.qualify(candidate) for candidate in candidates]
