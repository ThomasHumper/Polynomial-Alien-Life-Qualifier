"""Tests for the alien-life qualification engine."""

from polynomial_alien_life import (
    AlienCandidate,
    AlienLifeQualifier,
    PolynomialConstraint,
)


def test_candidate_passes_constraint() -> using Test
using PolynomialAlienLife


@testset "Polynomial Alien Life Qualifier" begin

    @testset "Passing constraint" begin

        constraint = PolynomialConstraint(
            "test",
            p -> p[:x] - 10
        )

        engine = AlienLifeQualifier([constraint])

        candidate = AlienCandidate(
            "Test",
            Dict(:x => 10.0)
        )

        result = qualify(engine, candidate)

        @test result.qualified
        @test result.passed_constraints == ["test"]
        @test isempty(result.failed_constraints)
    end


    @testset "Failing constraint" begin

        constraint = PolynomialConstraint(
            "test",
            p -> p[:x] - 10
        )

        engine = AlienLifeQualifier([constraint])

        candidate = AlienCandidate(
            "Test",
            Dict(:x => 20.0)
        )

        result = qualify(engine, candidate)

        @test !result.qualified
        @test isempty(result.passed_constraints)
        @test result.failed_constraints == ["test"]
    end


    @testset "Multiple constraints" begin

        constraints = [
            PolynomialConstraint(
                "x constraint",
                p -> p[:x] - 10
            ),

            PolynomialConstraint(
                "y constraint",
                p -> p[:y] - 20
            )
        ]

        engine = AlienLifeQualifier(constraints)

        candidate = AlienCandidate(
            "Test",
            Dict(
                :x => 10.0,
                :y => 20.0
            )
        )

        result = qualify(engine, candidate)

        @test result.qualified
        @test score(result) == 1.0
    end


    @testset "Partial qualification" begin

        constraints = [
            PolynomialConstraint(
                "passing",
                p -> p[:x] - 10
            ),

            PolynomialConstraint(
                "failing",
                p -> p[:y] - 20
            )
        ]

        engine = AlienLifeQualifier(
            constraints;
            require_all = false
        )

        candidate = AlienCandidate(
            "Test",
            Dict(
                :x => 10.0,
                :y => 50.0
            )
        )

        result = qualify(engine, candidate)

        @test result.qualified
        @test score(result) == 0.5
    end


    @testset "Missing parameter" begin

        constraint = PolynomialConstraint(
            "requires y",
            p -> p[:y] - 10
        )

        engine = AlienLifeQualifier([constraint])

        candidate = AlienCandidate(
            "Incomplete",
            Dict(:x => 10.0)
        )

        result = qualify(engine, candidate)

        @test !result.qualified
        @test length(result.failed_constraints) == 1
    end


    @testset "Polynomial models" begin

        candidate = Dict(
            :temperature => 10.0,
            :optimal_temperature => 10.0,
            :pressure => 1.0,
            :pressure_tolerance => 1.0,
            :energy => 100.0,
            :metabolic_rate => 10.0,
            :resources => 100.0,
            :population => 10.0,
            :resource_consumption => 10.0,
            :complexity => 1.0,
            :minimum_complexity_energy => 100.0
        )

        @test metabolic_balance(candidate) ≈ 0.0
        @test environmental_pressure(candidate) ≈ 0.0
        @test resource_balance(candidate) ≈ 0.0
        @test thermal_stability(candidate) ≈ 0.0
        @test biological_complexity(candidate) ≈ 0.0
    end

endNone:
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
