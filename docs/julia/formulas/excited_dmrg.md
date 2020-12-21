# Compute excited states with DMRG 

ITensor DMRG accepts additional MPS wavefunctions as an extra argument.
When these are provided, the DMRG code minimizes the
energy while also reducing the overlap (inner product) of the current MPS
 with the previously provided MPS. If these overlaps become sufficiently small,
then the computed MPS is an excited state. So by finding the ground
state, then providing it to DMRG as a "penalty state" or previous state
one can compute the first excited state. Then providing this one can
get the second excited state, etc.

Note that when the system has conserved quantum numbers, a superior way
to find excited states can be to find ground states of quantum number (or symmetry)
sectors other than the one containing the absolute ground state. In that
context, the penalty method used below is a way to find higher excited states
within the same quantum number sector.
  
### Example code:

    include:docs/VERSION/formulas/excited_dmrg.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/excited_dmrg.jl">Download the example code</a>
