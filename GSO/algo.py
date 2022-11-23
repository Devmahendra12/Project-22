# Inputs:
# Initial luciferin value = l_0,
# Initial dynamic decision domain value = r0, i.e., r_i
# d(0) = r_0,
# Maximum iteration number = iter_max,
# Initial time, t = 1.
# Outputs: Identify the most appropriate sensors to move at the centroids of the
# Voronoi cell structure.
# Algorithm:

1. Repeat

2. for each glowworm i do:

3. li(t) = (1 – ρ) li(t – 1) + γ J (xi (t)) // luciferin update phase


4. for each glowworm i do: // glowworm movement phase
5. {// set neighborhood glowworm
Ni (t)= {j: dij(t) < ri
d(t); li(t) ˂ lj(t)}; for each neighborhood glowworm, j ∈ Ni (t)



6. Calculate the probability of movement using the following equation,
Pij(t) = lj(t) 􀀀 li(t)
Σ
k∈Ni(t)(lk(t) 􀀀 li(t))


7. Select glowworm with the maximum probability of movement.


8. // Update location of glowworm by the following equation,
xi (t + 1) = xi (t) + s
( xj(t) 􀀀 xi(t)
‖ xj(t) 􀀀 xi(t) ‖
)
Where, s =| dik 􀀀 √3r| belongs to step-size, || || appears as the Euclidian norm
Operator.


9. // Update neighborhood range of each glowworm
ri
d(t + 1) = min {rs, max{0, ri
d(t) + β (nt 􀀀 􀀀 | Ni (t)|)}};
Where β is a constant parameter and n represents a controlling parameter that
manages the neighboring nodes.
10.}


11. Move on to the next iteration.
12.} until (t ≤ maximum iteration number).