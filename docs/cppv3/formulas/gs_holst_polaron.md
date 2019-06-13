# Ground state of the 1d Holstein Polaron
Itensor also allows you to generate mixed SiteSets so that you can simulate systems with different particle types on each site. This examples demonstrates how to generate the ground state with DMRG for the Holstein polaron, with one spinless fermion. The Hamiltonian is defined as:
$$
H = t_0 \sum\_i (c^{\dagger}_{i+1}c_{i} + h.c.) + \omega_0 \sum\_i (b^{\dagger}_i b_i) + \gamma \sum_i c^{\dagger}_i c_i (b^{\dagger}_i + b_i)
$$
To calculate the ground state of this system one first defines a MixedSiteSet, which taking the two particle types as template parameters
```c++
  using Holstein = MixedSiteSet<FermionSite,BosonSite>;
```
The "site set" is now of length N and has spinless fermionic degrees of freedom on every uneven site and bosonic degrees of freedom on ever even site. The arguments:
```c++
  {"ConserveNf=",true,"ConserveNb=",false,"MaxOcc=",2}
```
means that we conserve the number of fermions in the system, that the bosons number is not conserved and that each site can have a maximum of 2 bosons per site.
When one implements the Hamiltonian, one has to make sure that the right operators are assigned to the correct sites, so that the fermionic operators only act on site 1, 3 etc.
```c++
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
```
We then generate an initial state which only contains one fermion and compute:
```c++
 auto state = InitState(sites);
 state.set(5,"Occ");
 auto psi0 = randomMPS(state);
    ```
We then compute the ground state.
### Full example code:

```c++
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



```


    include:docs/VERSION/formulas/gs_holst_polaron.cc

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/gs_holst_polaron.cc">Download the full example code</a>
