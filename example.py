"""Basic usage example."""

from polynomial_alien_life import (
    AlienCandidate,
    AlienLifeQualifier,
    PolynomialConstraint,using PolynomialAlienLife

constraints = [
    PolynomialConstraint(
        "metabolic balance",
        metabolic_balance;
        tolerance = 0.5,
        description = "Energy must support metabolic activity."
    ),

    PolynomialConstraint(
        "environmental pressure",
        environmental_pressure;
        tolerance = 0.1,
        description = "Pressure must be compatible with the organism."
    ),

    PolynomialConstraint(
        "resource balance",
        resource_balance;
        tolerance = 1.0,
        description = "Resources must support the population."
    ),

    PolynomialConstraint(
        "thermal stability",
        thermal_stability;
        tolerance = 1.0,
        description = "Temperature must be compatible with the organism."
    ),

    PolynomialConstraint(
        "biological complexity",
        biological_complexity;
        tolerance = 1.0,
        description = "Energy must support biological complexity."
    )
]


engine = AlienLifeQualifier(
    constraints;
    require_all = true
)


candidate = AlienCandidate(
    "A-001",
    Dict(
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
)


result = qualify(engine, candidate)

println(summary(result))

println()
println("Polynomial values:")

for (name, value) in result.values
    println("  $name = $(round(value; digits=4))")
end
)

from polynomial_alien_life.polynomials import (
    biological_complexity,
    environmental_pressure,
    metabolic_balance,
    resource_balance,
)


def main() -> None:
    """Run the example."""

    constraints = [
        PolynomialConstraint(
            name="metabolic balance",
            function=metabolic_balance,
            tolerance=0.5,
            description="Energy must support metabolic activity.",
        ),
        PolynomialConstraint(
            name="environmental pressure",
            function=environmental_pressure,
            tolerance=0.1,
            description="Pressure must be compatible with the organism.",
        ),
        PolynomialConstraint(
            name="resource balance",
            function=resource_balance,
            tolerance=1.0,
            description="Resources must support the population.",
        ),
        PolynomialConstraint(
            name="biological complexity",
            function=biological_complexity,
            tolerance=1.0,
            description="Energy must support biological complexity.",
        ),
    ]

    qualifier = AlienLifeQualifier(
        constraints=constraints,
        require_all=True,
    )

    candidate = AlienCandidate(
        name="A-001",
        parameters={
            "temperature": 10.0,
            "pressure": 1.0,
            "energy": 100.0,
            "metabolic_rate": 10.0,
            "pressure_tolerance": 1.0,
            "resources": 100.0,
            "population": 10.0,
            "resource_consumption": 10.0,
            "complexity": 1.0,
            "minimum_complexity_energy": 100.0,
        },
    )

    result = qualifier.qualify(candidate)

    print(result.summary())
    print()
    print("Polynomial values:")

    for name, value in result.values.items():
        print(f"  {name}: {value:.4f}")


if __name__ == "__main__":
    main()
