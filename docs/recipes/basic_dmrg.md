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
int nsweep = 5;
int minm = 1;
int maxm = 100;
Real cutoff = 1E-5;

Sweeps sweeps(Sweeps::exp_m,nsweep,minm,maxm,cutoff);
</code>

The argument `Sweeps::exp_m` in the last line tells the sweeps object to exponentially
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

Below you can find a complete working code that includes all of these steps.


<code>
\#include "core.h"
\#include "model/spinone.h"
\#include "hams/heisenberg.h"
using boost::format;
using namespace std;

int main(int argc, char\* argv[])
{
    int N = 100;
    int nsweep = 5;
    int minm = 1;
    int maxm = 100;
    Real cutoff = 1E-5;

    SpinOne model(N);

    MPO H = Heisenberg(model);

    Sweeps sweeps(Sweeps::exp_m,nsweep,minm,maxm,cutoff);

    MPS psi(model);

    Real energy = dmrg(psi,H,sweeps);

    cout << format("Ground State Energy = %.10f") % energy << endl;

    return 0;
}

</code>

<br>
[[Back to Recipes|recipes]]
