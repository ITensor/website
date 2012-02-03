#Perform a basic DMRG calculation#

To do any DMRG calculation you first need a Hamiltonian. 
The simplest way to obtain one is to 
use a pre-defined Hamiltonian provided with the library. 
The site indices used by the Hamiltonian are provided by a model object:

`SpinOne model(N);`

Here we have chosen to use spin 1 sites and our lattice size is `N`.
Next we instantiate the Hamiltonian, which is a matrix product operator (MPO):

`MPO H = Heisenberg(model);`

Before beginning the calculation, we need to specify how many DMRG sweeps to do and
what schedule we would like for the parameters controlling the accuracy.
These parameters are stored within a sweeps object:

<code>
Sweeps sweeps(Sweeps::exp_m);
sweeps.setNsweep(5);
sweeps.setMaxm(100);
sweeps.setCutoff(1E-5);
</code>

The argument `Sweeps::exp_m` in the first line tells the sweeps object to exponentially
increase the maximum number of states kept in each sweep until it reaches the `Maxm` (which is 100 here).

The wavefunction must use the same sites
as the Hamiltonian, so we construct it using the same model object as before

`MPS psi(model);`

By default an MPS is initialized to a random product state; we could also set `psi`
to some specific initial state in order to accelerate the DMRG convergence time.

Finally, we are ready to call DMRG:

`Real energy = dmrg(psi,H,sweeps);`

When the algorithm is done, it returns the ground state energy. The optimized ground state
wavefunction is stored back into `psi` on return.



<br>
[[Back to Recipes|recipes]]
