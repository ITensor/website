# Perform a basic DMRG calculation #

To do any DMRG calculation you first need a Hamiltonian. 
The library provides some common Hamiltonians for convenience.
The site indices used by the Hamiltonian are provided by an instance of the SpinOne class:

    SpinOne sites(N);

Here we have chosen to use spin 1 sites and our lattice size is N.
Next we instantiate the Hamiltonian, which is a matrix product operator (MPO):

    MPO H = Heisenberg(sites);

Before beginning the calculation, we need to specify how many DMRG sweeps to do and
what schedule we would like for the parameters controlling the accuracy.
These parameters are stored within a sweeps object:

    Sweeps sweeps(5); //number of sweeps is 5
    sweeps.maxm() = 10,20,100,100,200; //gradually increase states kept
    sweeps.cutoff() = 1E-10; //desired truncation error

The wavefunction must use the same sites
as the Hamiltonian, so we construct it using the same sites object as before

    MPS psi(sites);

By default an MPS is initialized to a random product state; we could also set psi
to some specific initial state using an [[InitState|classes/initstate]] object.

Finally, we are ready to call DMRG:

    Real energy = dmrg(psi,H,sweeps);

When the algorithm is done, it returns the ground state energy. The optimized ground state
wavefunction is stored back into `psi` on return.

Below you can find a complete working code that includes all of these steps.


    #include "core.h"
    #include "model/spinone.h"
    #include "hams/Heisenberg.h"
    using namespace std;

    int 
    main(int argc, char* argv[])
        {
        int N = 100;

        SpinOne sites(N);

        MPO H = Heisenberg(sites);

        Sweeps sweeps(5); //number of sweeps is 5
        sweeps.maxm() = 10,20,100,100,200;
        sweeps.cutoff() = 1E-10;

        MPS psi(sites);

        Real energy = dmrg(psi,H,sweeps);

        cout << "Ground State Energy = " << energy << endl;

        return 0;
        }

<br>
[[Back to Recipes|recipes]]
