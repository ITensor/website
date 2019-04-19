#include "itensor/all.h"

using namespace itensor;

int 
main()
    {
    int Nx = 50;
    auto N = 2*Nx;
    auto Jx = 1.0;
    auto Jy = 1.0;

    auto sites = SpinHalf(N);

    auto ampo = AutoMPO(sites);
    for(int j = 1; j <= N-3; j += 2)
        {
        ampo +=   Jx,"Sz",j,"Sz",j+2;
        ampo += Jx/2,"S+",j,"S-",j+2;
        ampo += Jx/2,"S-",j,"S+",j+2;

        ampo +=   Jx,"Sz",j+1,"Sz",j+3;
        ampo += Jx/2,"S+",j+1,"S-",j+3;
        ampo += Jx/2,"S-",j+1,"S+",j+3;
        }
    for(int j = 1; j <= N-1; j += 2)
        {
        ampo +=   Jy,"Sz",j,"Sz",j+1;
        ampo += Jy/2,"S+",j,"S-",j+1;
        ampo += Jy/2,"S-",j,"S+",j+1;
        }
    auto H = toMPO(ampo);

    auto state = InitState(sites);
    for(int i = 1; i <= N; ++i) 
        {
        if(i%2 == 1) state.set(i,"Up");
        else         state.set(i,"Dn");
        }
    auto psi = MPS(state);

    auto sweeps = Sweeps(10);
    sweeps.maxdim() = 50,100,200,300,400;
    sweeps.cutoff() = 1E-10;
    println(sweeps);

    auto energy = dmrg(psi,H,sweeps,{"Quiet",true});

    return 0;
    }

