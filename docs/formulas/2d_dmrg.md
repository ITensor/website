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

### Full Sample code:

    #include "itensor/mps/dmrg.h"
    #include "itensor/mps/sites/spinhalf.h"
    #include "itensor/mps/autompo.h"
    #include "itensor/mps/lattice/square.h"
    #include "itensor/mps/lattice/triangular.h"

    using namespace itensor;

    int 
    main()
        {
        int Nx = 8;
        int Ny = 8;
        int N = Nx*Ny;
        auto yperiodic = false;

        //
        // Initialize the site degrees of freedom.
        //
        auto sites = SpinHalf(N);

        //
        // Use the AutoMPO feature to create the 
        // next-neighbor Heisenberg model.
        //
        auto ampo = AutoMPO(sites);
        auto lattice = triangularLattice(Nx,Ny,{"YPeriodic=",yperiodic});
        //square lattice also available:
        //auto lattice = squareLattice(Nx,Ny,{"YPeriodic=",yperiodic});
        for(auto bnd : lattice)
            {
            ampo += 0.5,"S+",bnd.s1,"S-",bnd.s2;
            ampo += 0.5,"S-",bnd.s1,"S+",bnd.s2;
            ampo +=     "Sz",bnd.s1,"Sz",bnd.s2;
            }
        auto H = IQMPO(ampo);

        // Set the initial wavefunction matrix product state
        // to be a Neel state.
        //
        // This choice implicitly sets the global Sz quantum number
        // of the wavefunction to zero. Since it is an IQMPS
        // it will remain in this quantum number sector.
        //
        auto state = InitState(sites);
        for(int i = 1; i <= N; ++i) 
            {
            if(i%2 == 1)
                state.set(i,"Up");
            else
                state.set(i,"Dn");
            }

        auto psi = IQMPS(state);

        //
        // overlap calculates matrix elements of MPO's with respect to MPS's
        // overlap(psi,H,psi) = <psi|H|psi>
        //
        printfln("Initial energy = %.5f", overlap(psi,H,psi) );

        //
        // Set the parameters controlling the accuracy of the DMRG
        // calculation for each DMRG sweep. 
        // Here less than 5 cutoff values are provided, for example,
        // so all remaining sweeps will use the last one given (= 1E-10).
        //
        auto sweeps = Sweeps(5);
        sweeps.maxm() = 10,20,100,100,200;
        sweeps.cutoff() = 1E-10;
        sweeps.niter() = 2;
        sweeps.noise() = 1E-7,1E-8,0.0;
        println(sweeps);

        //
        // Begin the DMRG calculation
        //
        auto energy = dmrg(psi,H,sweeps,"Quiet");

        //
        // Print the final energy reported by DMRG
        //
        printfln("\nGround State Energy = %.10f",energy);
        printfln("\nUsing overlap = %.10f", overlap(psi,H,psi) );

        println("\nTotal QN of Ground State = ",totalQN(psi));

        return 0;
        }
