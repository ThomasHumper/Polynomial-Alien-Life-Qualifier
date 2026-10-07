"""
    metabolic_balance(p)

Energy required to maintain the candidate's metabolism.

P = energy - temperature * metabolic_rate
"""
function metabolic_balance(p::Dict{Symbol,T}) where {T<:Real}

    return p[:energy] -
           p[:temperature] * p[:metabolic_rate]
end


"""
    environmental_pressure(p)

Measures compatibility between environmental pressure
and the organism's pressure tolerance.

P = pressure * pressure_tolerance - 1
"""
function environmental_pressure(
    p::Dict{Symbol,T}
) where {T<:Real}

    return p[:pressure] *
           p[:pressure_tolerance] - 1
end


"""
    resource_balance(p)

Determines whether available resources can support
the population.

P = resources - population * resource_consumption
"""
function resource_balance(
    p::Dict{Symbol,T}
) where {T<:Real}

    return p[:resources] -
           p[:population] *
           p[:resource_consumption]
end


"""
    thermal_stability(p)

Simple thermal stability polynomial.

P = temperature² - optimal_temperature²
"""
function thermal_stability(
    p::Dict{Symbol,T}
) where {T<:Real}

    return p[:temperature]^2 -
           p[:optimal_temperature]^2
end


"""
    biological_complexity(p)

Measures whether enough energy exists to support
the specified biological complexity.

P = complexity * energy - minimum_complexity_energy
"""
function biological_complexity(
    p::Dict{Symbol,T}
) where {T<:Real}

    return p[:complexity] *
           p[:energy] -
           p[:minimum_complexity_energy]
end
