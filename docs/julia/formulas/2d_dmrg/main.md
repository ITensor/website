# Make a 2D Hamiltonian for DMRG

You can use the AutoMPO system to make 2D Hamiltonians
much in the same way you make 1D Hamiltonians: by looping over
all of the bonds and adding the interactions on these bonds to
the AutoMPO. 

To help with the logic of 2D lattices, ITensor pre-defines
some helper functions which
return an array of bonds. Each bond object has an
"s1" field and an "s2" field which are the integers numbering
the two sites the bond connects.
(You can view the source for these functions at [this link](https://github.com/ITensor/ITensors.jl/blob/master/src/physics/lattices.jl).)

The two provided functions currently are `square_lattice` and 
`triangular_lattice`. It is not hard to write your own similar lattice
functions as all they have to do is define an array of `ITensors.LatticeBond`
structs or even a custom struct type you wish to define. We welcome any
user contributions of other lattices that ITensor does not currently offer.

Each lattice function takes an optional named argument
"yperiodic" which lets you request that the lattice should
have periodic boundary conditions around the y direction, making
the geometry a cylinder.

### Full example code:

    include:docs/VERSION/formulas/2d_dmrg/2d_dmrg.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/2d_dmrg.cc">Download the full example code</a>
