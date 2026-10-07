"""
    AlienCandidate

Represents a hypothetical alien-life candidate.

# Fields

- `name`: Name or identifier of the candidate.
- `parameters`: Dictionary containing the candidate's numerical parameters.
"""
struct AlienCandidate{T<:Real}
    name::String
    parameters::Dict{Symbol,T}
end


"""
    PolynomialConstraint

A polynomial constraint used by the qualification engine.

The constraint is satisfied when:

    abs(f(parameters)) <= tolerance
"""
struct PolynomialConstraint{F,T<:Real}
    name::String
    function_::F
    tolerance::T
    description::String
end


function PolynomialConstraint(
    name::String,
    function_::F;
    tolerance::T = 1e-6,
    description::String = ""
) where {F,T<:Real}

    return PolynomialConstraint(
        name,
        function_,
        tolerance,
        description
    )
end


"""
    QualificationResult

Stores the result of evaluating an alien candidate.
"""
struct QualificationResult
    candidate_name::String
    qualified::Bool
    passed_constraints::Vector{String}
    failed_constraints::Vector{String}
    values::Dict{String,Float64}
end


"""
    score(result)

Return the fraction of constraints that passed.
"""
function score(result::QualificationResult)
    total = length(result.passed_constraints) +
            length(result.failed_constraints)

    total == 0 && return 0.0

    return length(result.passed_constraints) / total
end


"""
    summary(result)

Return a human-readable summary of the qualification.
"""
function summary(result::QualificationResult)

    status = result.qualified ? "QUALIFIED" : "NOT QUALIFIED"

    total = length(result.passed_constraints) +
            length(result.failed_constraints)

    percentage = round(score(result) * 100; digits=1)

    lines = String[
        "Candidate: $(result.candidate_name)",
        "Status: $status",
        "Constraints: $(length(result.passed_constraints))/$total passed",
        "Score: $percentage%"
    ]

    if !isempty(result.failed_constraints)
        push!(lines, "Failed constraints:")

        for constraint in result.failed_constraints
            push!(lines, "  - $constraint")
        end
    end

    return join(lines, "\n")
end
