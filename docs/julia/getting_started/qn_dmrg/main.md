# Conserving Quantum Numbers in DMRG

An important technique in DMRG calculations of quantum Hamiltonians
is the conservation of _quantum numbers_. Examples of these are the
total number of particles of a model of fermions, or the total of all
@@S^z@@ components of a system of spins. Not only can conserving quantum
numbers make DMRG calculations run more quickly and use less memory, but
it can be important for simulating physical systems with conservation
laws and for obtaining ground states in different symmetry sectors.
Note that ITensor currently only supports Abelian quantum numbers.

## Necessary Changes

Setting up a quantum-number conserving DMRG calculation in ITensor requires
only very small changes to a DMRG code. The main changes are:

1. using tensor indices (`Index` objects)
which carry quantum number (QN) information to build your Hamiltonian and 
initial state
2. initializing your MPS to have well-defined total quantum numbers

Importantly, _the total QN of your state throughout the calculation will 
remain the same as the initial state passed to DMRG_.
The total QN of your state is not set separately, but determined 
implicitly from the initial QN of the state when it is first constructed.

Of course, your Hamiltonian should conserve all of the QN's that you would
like to use. If it doesn't, you will get an error when you try to construct
it out of the QN-enabled tensor indices.

## Making the Changes

Let's see how to make these two changes to the DMRG code from the 
[[Getting Started with DMRG|getting_started/dmrg]] page. At the end,
we will put together these changes for a complete, working code.

### Change 1: QN site indices

To make change (1), we will change the line

    sites = siteinds("S=1",N)

by setting the `conserve_qns` keyword argument to `true`:

    sites = siteinds("S=1",N; conserve_qns=true)

Setting `conserve_qns=true` tells the `siteinds` function to conserve
every possible quantum number associated to the site
type (which is `"S=1"` in this example). For @@S=1@@ spins, this will turn on
total-@@S^z@@ conservation.
(For other site types that conserve multiple QNs, there are specific keyword 
arguments available to track just a subset of conservable QNs.)
We can check this by printing out some of the site indices, and seeing that the
subspaces of each `Index` are labeled by QN values:

    @show sites[1]
    @show sites[2]

    # Sample output:
    #
    # sites[1] = (dim=3|id=794|"S=1,Site,n=1") <Out>
    # 1: QN("Sz",2) => 1
    # 2: QN("Sz",0) => 1
    # 3: QN("Sz",-2) => 1
    # sites[2] = (dim=3|id=806|"S=1,Site,n=2") <Out>
    # 1: QN("Sz",2) => 1
    # 2: QN("Sz",0) => 1
    # 3: QN("Sz",-2) => 1

In the sample output above, note than in addition to the dimension of these indices being 3, each of the three settings of the Index have a unique QN associated to them. The number after the QN on each line is the dimension of that subspace, which is 1 for each subspace of the Index objects above. Note also that `"Sz"` quantum numbers in ITensor are measured in units of @@1/2@@, so `QN("Sz",2)` corresponds to @@S^z=1@@ in conventional physics units.

### Change 2: initial state

To make change (2), instead of constructing the initial MPS `psi0` to be an arbitrary, random MPS, we will make it a specific state with a well-defined total @@S^z@@. 
So we will replace the line

    psi0 = randomMPS(sites,10)

by the lines

    state = [isodd(n) ? "Up" : "Dn" for n=1:N]
    psi0 = productMPS(sites,state)

The first line of the new code above makes an array of strings which 
alternate between `"Up"` and `"Dn"` on odd and even numbered sites.
These names `"Up"` and `"Dn"` are special values associated to the `"S=1"` 
site type which indicate up and down spin values. The second line takes
the array of site Index objects `sites` and the array of strings `state`
and returns an MPS which is a product state (classical, unentangled state)
with each site's state given by the strings in the `state` array.
In this example, `psi0` will be a Neel state with alternating up and down 
spins, so it will have a total @@S^z@@ of zero. We could check this by
computing the quantum-number flux of `psi0`

    @show flux(psi0)
    # Output: flux(psi0) = QN("Sz",0)

## Putting it All Together

Let's take the DMRG code from the [[Getting Started with DMRG|getting_started/dmrg]]
tutorial and make the changes above to it, to turn it into a code which conserves 
the total @@S^z@@ quantum number throughout the DMRG calculation. The resulting code is:


    include:docs/VERSION/getting_started/qn_dmrg/qn_dmrg.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/getting_started/qn_dmrg/qn_dmrg.jl">Download this example code</a>


