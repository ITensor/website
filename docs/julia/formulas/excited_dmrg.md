# Compute excited states with DMRG 

ITensor DMRG accepts additional MPS wavefunctions as a optional, extra argument.
These additional 'penalty states' are provided as an array of MPS just 
after the Hamiltonian, like this:

    energy,psi3 = dmrg(H,[psi0,psi1,psi2],psi3_init,sweeps)

Here the penalty states are `[psi0,psi1,psi2]`. 
When these are provided, the DMRG code minimizes the
energy of the current MPS while also reducing its overlap 
(inner product) with the previously provided MPS. If these overlaps become sufficiently small,
then the computed MPS is an excited state. So by finding the ground
state, then providing it to DMRG as a "penalty state" or previous state
one can compute the first excited state. Then providing both of these, one can
get the second excited state, etc.

A  keyword argument called `weight` can also be provided to
the `dmrg` function when penalizing overlaps to previous states. The 
`weight` parameter is multiplied by the overlap with the previous states,
so sets the size of the penalty. It should be chosen at least as large
as the (estimated) gap between the ground and first excited states.
Otherwise the optimal value of the weight parameter is not so obvious,
and it is best to try various weights during initial test calculations.

Note that when the system has conserved quantum numbers, a superior way
to find excited states can be to find ground states of quantum number (or symmetry)
sectors other than the one containing the absolute ground state. In that
context, the penalty method used below is a way to find higher excited states
within the same quantum number sector.
  
### Example code:

    include:docs/VERSION/formulas/excited_dmrg.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/excited_dmrg.jl">Download the example code</a>
