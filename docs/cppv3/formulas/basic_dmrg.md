# Perform a basic DMRG calculation #

Because tensor indices in ITensor have unique identities, before we can make a Hamiltonian
or a wavefunction we need to construct a "site set" which will hold the site indices defining
the physical Hilbert space:

    auto sites = SpinOne(N,{"ConserveQNs=",false});

Here we have chosen to use the SpinOne site set to create a Hilbert space of N 
spin 1 sites. We use set the arg "ConserveQNs" to false to indicate the we don't
want to conserve any quantum numbers.

Next we'll make our Hamiltonian matrix product operator (MPO). A very 
convenient way to do this is to use the AutoMPO helper class which lets 
us input a Hamiltonian (or any sum of local operators) in similar notation
to pencil-and-paper notation:

    auto ampo = AutoMPO(sites);
    for(int j = 1; j < N; ++j)
        {
        ampo += 0.5,"S+",j,"S-",j+1;
        ampo += 0.5,"S-",j,"S+",j+1;
        ampo +=     "Sz",j,"Sz",j+1;
        }
    auto H = toMPO(ampo);

In the last line above we convert the AutoMPO helper object to an actual MPO.

Before beginning the calculation, we need to specify how many DMRG sweeps to do and
what schedule we would like for the parameters controlling the accuracy.
These parameters are stored within a sweeps object:

    auto sweeps = Sweeps(5); //number of sweeps is 5
    sweeps.maxdim() = 10,20,100,100,200; //gradually increase states kept
    sweeps.cutoff() = 1E-10; //desired truncation error

The random starting wavefunction `psi0` must be defined in the same Hilbert space
as the Hamiltonian, so we construct it using the same site set object as before:

    auto psi0 = randomMPS(sites);

We could also set psi to some specific initial state using an [[InitState|classes/initstate]] object,
which is required if we were conserving QNs.

Finally, we are ready to call DMRG:

    auto [energy,psi] = dmrg(H,psi0,sweeps);

When the algorithm is done, it returns the ground state energy as the variable `energy` and an MPS 
approximation to the ground state as the variable `psi`.

Below you can find a complete working code that includes all of these steps,
along with the headers you need to include to obtain all of the necessary library code.

    #include "itensor/all.h"

    using namespace itensor;

    int 
    main()
        {
        int N = 100;

        auto sites = SpinOne(N,{"ConserveQNs=",false});

        auto ampo = AutoMPO(sites);
        for(int j = 1; j < N; ++j)
            {
            ampo += 0.5,"S+",j,"S-",j+1;
            ampo += 0.5,"S-",j,"S+",j+1;
            ampo +=     "Sz",j,"Sz",j+1;
            }
        auto H = toMPO(ampo);

        auto sweeps = Sweeps(5); //number of sweeps is 5
        sweeps.maxdim() = 10,20,100,100,200;
        sweeps.cutoff() = 1E-10;

        auto psi0 = randomMPS(sites);

        auto [energy,psi] = dmrg(H,psi0,sweeps);

        println("Ground State Energy = ",energy);

        return 0;
        }

