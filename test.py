"""Tests for the alien-life qualification engine."""

from polynomial_alien_life import (
    AlienCandidate,
    AlienLifeQualifier,
    PolynomialConstraint,
)


def test_candidate_passes_constraint() -> None:
    """A candidate should pass a satisfied constraint."""

    constraint = PolynomialConstraint(
        name="test",
        function=lambda p: p["x"] - 10,
    )

    qualifier = AlienLifeQualifier([constraint])

    candidate = AlienCandidate(
        name="Test Candidate",
        parameters={"x": 10},
    )

    result = qualifier.qualify(candidate)

    assert result.qualified is True
    assert result.passed_constraints == ["test"]
    assert result.failed_constraints == []


def test_candidate_fails_constraint() -> None:
    """A candidate should fail an unsatisfied constraint."""

    constraint = PolynomialConstraint(
        name="test",
        function=lambda p: p["x"] - 10,
    )

    qualifier = AlienLifeQualifier([constraint])

    candidate = AlienCandidate(
        name="Test Candidate",
        parameters={"x": 20},
    )

    result = qualifier.qualify(candidate)

    assert result.qualified is False
    assert result.passed_constraints == []
    assert result.failed_constraints == ["test"]


def test_multiple_constraints() -> None:
    """All constraints should be evaluated."""

    constraints = [
        PolynomialConstraint(
            name="first",
            function=lambda p: p["x"] - 10,
        ),
        PolynomialConstraint(
            name="second",
            function=lambda p: p["y"] - 20,
        ),
    ]

    qualifier = AlienLifeQualifier(constraints)

    candidate = AlienCandidate(
        name="Test Candidate",
        parameters={
            "x": 10,
            "y": 20,
        },
    )

    result = qualifier.qualify(candidate)

    assert result.qualified is True
    assert result.score == 1.0


def test_partial_qualification() -> None:
    """A candidate can be evaluated without requiring every constraint."""

    constraints = [
        PolynomialConstraint(
            name="passing",
            function=lambda p: p["x"] - 10,
        ),
        PolynomialConstraint(
            name="failing",
            function=lambda p: p["y"] - 20,
        ),
    ]

    qualifier = AlienLifeQualifier(
        constraints,
        require_all=False,
    )

    candidate = AlienCandidate(
        name="Test Candidate",
        parameters={
            "x": 10,
            "y": 50,
        },
    )

    result = qualifier.qualify(candidate)

    assert result.qualified is True
    assert result.score == 0.5


def test_missing_parameter() -> None:
    """Missing parameters should cause a constraint to fail."""

    constraint = PolynomialConstraint(
        name="requires_y",
        function=lambda p: p["y"] - 10,
    )

    qualifier = AlienLifeQualifier([constraint])

    candidate = AlienCandidate(
        name="Incomplete Candidate",
        parameters={"x": 10},
    )

    result = qualifier.qualify(candidate)

    assert result.qualified is False
    assert len(result.failed_constraints) == 1
