# Measure Local Properties of an MPS

For matrix product states (MPS) representing the wavefunction of a quantum
system, a common task is to measure local observables defined for each
site or physical degree of freedom. To see how to do this in ITensor,
let's start from the following example of measuring the `"Sz"` operator
for each site of an MPS `psi`:

    include:docs/VERSION/formulas/measure_mps/measure_mps.jl
