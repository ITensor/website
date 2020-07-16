# DMRG Calculation with Mixed Local Hilbert Space Types

The following fully-working example shows how to set up a calculation
mixing S=1/2 and S=1 spins on every other site of a 1D system. The 
Hamiltonian involves Heisenberg spin interactions with adjustable
couplings between sites of the same spin or different spin.

Note that the only difference from a regular ITensor DMRG calculation
is that the `sites` array has Index objects which alternate in dimension
and in which physical tag type they carry, whether `"S=1/2"` or `"S=1"`.
(Try printing out the sites array to see!)
These tags tell the AutoMPO system which local operators to use for these
sites when building the Hamiltonian MPO.

    include:docs/VERSION/formulas/mixed_sites_dmrg/mixed_sites_dmrg.jl
