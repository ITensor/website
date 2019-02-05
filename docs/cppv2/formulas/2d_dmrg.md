# Make a 2D Hamiltonian for DMRG

You can use the AutoMPO helper class to make 2D Hamiltonians
much in the same way you make 1D Hamiltonians: by looping over
all of the bonds and adding the interactions on these bonds to
the AutoMPO. 

To help with the logic of 2D lattices, we have included some 
code in the itensor/mps/lattice/ folder definining functions
which return an array of bonds. Each bond object has an
"s1" field and an "s2" field which are the integers numbering
the two sites the bond connects.

Each lattice function takes an optional named argument
"YPeriodic" which lets you request that the lattice should
have periodic boundary conditions around the y direction, making
the geometry a cylinder.

### Full example code:

    include:docs/VERSION/formulas/2d_dmrg.cc

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/2d_dmrg.cc">Download the full example code</a>
