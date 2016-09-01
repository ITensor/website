# DMRG Interface

The density matrix renormalization group (DMRG) is a very powerful algorithm
for optimizing matrix product states (MPS) for ground states and low-lying 
excited states of one-dimensional (and quasi-one-dimensional) Hamiltonians.

The ITensor DMRG code works with Hamiltonians in matrix product
operator (MPO) form so that a single DMRG code can work for a very wide 
range of different Hamiltonians and local Hilbert spaces.

ITensor also offers DMRG routines for more general optimization tasks, including
- Hamiltonians which are an (implicit) sum of multiple MPOs
- minimizing the energy of an MPS, while constraining it to remain orthogonal
  to a collection of other MPS (for targeting excited states)
- "restricted" sweeping over a sub-region of a system (such as a unit cell)
  within an environment defined by a "frozen" MPS basis for the rest of the system


## Synopsis

    int N = 100;
    auto sites = SpinOne(N);

    auto psi = MPS(sites);

    auto ampo = AutoMPO(sites);
    for(int j = 1; j < N; ++j)
        {
        ampo += "Sz",j,"Sz",j+1;
        ampo += 0.5,"S+",j,"S-",j+1;
        ampo += 0.5,"S-",j,"S+",j+1;
        }
    auto H = MPO(ampo);

    auto sweeps = Sweeps(5);
    sweeps.maxm() = 10,40,100,200,200;
    sweeps.cutoff() = 1E-8;

    auto energy = dmrg(psi,H,sweeps,{"Quiet",true});
    //                  ^ psi passed by reference,
    //                    can measure properties afterwards

    printfln("Ground state energy = %.20f",energy);


## Basic DMRG interface







