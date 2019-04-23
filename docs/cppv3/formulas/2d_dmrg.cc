#include "itensor/all.h"

using namespace itensor;

int 
main()
    {
    int Nx = 8;
    int Ny = 8;
    auto N = Nx*Ny;
    auto yperiodic = false;

    //
    // Initialize the site degrees of freedom.
    //
    auto sites = SpinHalf(N,{"ConserveQNs=",true});

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
    auto H = toMPO(ampo);

    // Set the initial wavefunction matrix product state
    // to be a Neel state.
    //
    // This choice implicitly sets the global Sz quantum number
    // of the wavefunction to zero. Since it is an MPS
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

    auto psi0 = MPS(state);

    //
    // overlap calculates matrix elements of MPO's with respect to MPS's
    // inner(psi0,H,psi0) = <psi0|H|psi0>
    //
    printfln("Initial energy = %.5f", inner(psi0,H,psi0) );

    //
    // Set the parameters controlling the accuracy of the DMRG
    // calculation for each DMRG sweep. 
    // Here less than 5 cutoff values are provided, for example,
    // so all remaining sweeps will use the last one given (= 1E-10).
    //
    auto sweeps = Sweeps(5);
    sweeps.maxdim() = 10,20,100,100,200;
    sweeps.cutoff() = 1E-10;
    sweeps.niter() = 2;
    sweeps.noise() = 1E-7,1E-8,0.0;
    println(sweeps);

    //
    // Begin the DMRG calculation
    //
    auto [energy,psi] = dmrg(H,psi0,sweeps,"Quiet");

    //
    // Print the final energy reported by DMRG
    //
    printfln("\nGround State Energy = %.10f",energy);
    printfln("\nUsing overlap = %.10f", inner(psi,H,psi) );

    println("\nTotal QN of Ground State = ",totalQN(psi));

    return 0;
    }

