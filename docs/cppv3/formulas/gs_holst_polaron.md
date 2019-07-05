# Ground state of the 1d Holstein Polaron
Itensor also allows you to generate mixed SiteSets so that you can simulate systems with different particle types on each site. This examples demonstrates how to generate the ground state with DMRG for the Holstein polaron, with one spinless fermion. The Hamiltonian is defined as:
$$
H = -t_0 \sum\_i (c^{\dagger}_{i}c_{i+1} + h.c.) + \omega_0 \sum\_i (b^{\dagger}_i b_i) + \gamma \sum_i c^{\dagger}_i c_i (b^{\dagger}_i + b_i)
$$
To calculate the ground state of this system one first defines a MixedSiteSet type, which taking the two particle types as template parameters
```c++
  using Holstein = MixedSiteSet<FermionSite,BosonSite>;
```
The resulting site set of type `Holstein` will have spinless fermion degrees of freedom on the odd-numbered sites and boson degrees of freedom on the even-numbered sites.

To create an instance of a `Holstein` site set, we call:
```c++
    auto sites = Holstein(N,{"ConserveNf=",true,
               "ConserveNb=",false, "MaxOcc=",2});
```
where the named arguments
```c++
  {"ConserveNf=",true,"ConserveNb=",false,"MaxOcc=",2}
```
mean that we conserve the number of fermions in the system, that the bosons number is not conserved, and that each site can have a maximum of 2 bosons per site.

When one implements the Hamiltonian, one has to make sure that the right operators are assigned to the correct sites, so that the fermionic operators only act on site 1, 3 etc.
```c++
for(int j = 1; j <= N-2; j+=2)
   {
  ampo += -t0,"Cdag",j,"C",j+2;
  ampo+=  -t0,"C",j,"Cdag",j+2 ;
   }
 for(int j = 1; j < N; j += 2)
   {
   ampo += gamma,"N",j,"A",j+1;
   ampo += gamma,"N",j,"Adag",j+1;
   }
 for(int j = 1; j <= N; j += 2)
   {
   ampo += omega,"N",j+1;
   }
 auto H = toMPO(ampo);
```
We then generate an initial state which only contains one fermion and compute:
```c++
 auto state = InitState(sites);
 state.set(5,"Occ");
 auto psi0 = randomMPS(state);
    ```
We then compute the ground state by calling `dmrg`.

### Full example code:

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/gs_holst_polaron.cc">Download the full example code</a>

```c++
include:docs/VERSION/formulas/gs_holst_polaron.cc
```

