#Perform a basic DMRG calculation#

To do any DMRG calculation you first need a Hamiltonian. 
The simplest way to obtain one is to 
use a pre-defined Hamiltonian provided with the library. 
The sites used by the Hamiltonian are provided by a model object:

`SpinOne::Model model(N);`

Here we have chosen to use spin 1 sites and our lattice size is `N`.
Now instantiate the Hamiltonian, which is a matrix product operator (MPO):

`MPO H = SpinOne::Heisenberg(model)();`

(Note the second set of () at the end of the line.)

Before beginning the calculation, we need to specify how many DMRG sweeps to do and
what schedule we would like to follow as we change the parameters controlling the accuracy.
These parameters are stored within a sweeps object:

<code>
Sweeps sweeps(Sweeps::ramp_m);
sweeps.setNsweep(5);
sweeps.setMaxm(100);
sweeps.setCutoff(1E-5);
</code>

The argument `Sweeps::ramp_m` in the first line tells the sweeps object to gradually
increase the maximum number of states kept in each sweep until it reaches the Maxm (=100).

The wavefunction must have the same number of sites
as the Hamiltonian, so we can declare it as

`MPS psi(model);`

By default the components of an MPS are set to random values; we could also set `psi`
to some initial state in order to accelerate the DMRG convergence time.

Finally, we are ready to call DMRG:

`Real energy = dmrg(psi,H,sweeps);`

When the algorithm is done, it returns the ground state energy. The optimized ground state
wavefunction is stored back into `psi` on return.



<br>
[[Back to Recipes|recipes]]
