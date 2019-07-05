#include"itensor/all.h"
using namespace itensor;

int main(int argc, char *argv[])
{
  using Holstein = MixedSiteSet<FermionSite,BosonSite>;
  // want a chain of lenght L, choosen small to compare with ED values
  auto L=4;
  auto N=2*L;
  auto t0=1.0;
  auto omega=1.0;
  auto gamma=1.0;

  // generating the mixed site set with conserved fermion number, but not bosons
  auto sites = Holstein(N,{"ConserveNf=",true,
			   "ConserveNb=",false, "MaxOcc=",2});

  auto ampo = AutoMPO(sites);

 // generating the Hamiltonian, making sure fermionic operators only act on site
 // 1, 3, 5 etc
 // and bosonic on 2, 4 ..

   for(int j=1;j  <= N-2; j+=2)
    {
    ampo += -t0,"Cdag",j,"C",j+2;
	  ampo+= -t0, "C",j,"Cdag",j+2 ;
    }
   for(int j=1;j < N; j += 2)
    {
	   ampo += gamma,"N",j,"A",j+1;
	   ampo += gamma,"N",j,"Adag",j+1;
    }
   for(int j = 1; j <= N; j += 2)
    {
	   ampo += omega,"N",j+1;
    }
    auto H=toMPO(ampo);

    auto sweeps = Sweeps(100);
    // noise terms are very important to get the correct results
    sweeps.noise() = 1E-6,1E-6,1E-8, 1E-10,  1E-12;
    sweeps.maxdim() = 10,20,100,100,800;
    sweeps.cutoff() = 1E-14;

    auto state = InitState(sites);

    // fixing one fermion in the initial state
    state.set(5,"Occ");

    auto psi = randomMPS(state);

    auto [energy,psi0] = dmrg(H,psi,sweeps,{"Quiet=",true});

    printfln("Ground State Energy = %.12f",energy);

  return 0;
}
