# DMRG of the 1d Holstein Polaron
Itensor also allows you to generate mixed SiteSets so that you can simulate systems with mixed with more than one particle type on each site. This examples demonstrates how to generate the ground state for the Holstein polaron, with one spinless electron. The Hamiltonian we will demonstrate looks as follows:
$$
H = t_0 \sum\_j (c^{\dagger}_i c_{i+1} + h.c. ) + \omega_0 \sum\_j (b^{\dagger}_i b_i) + \sum_i n_i (b^{\dagger}_i + b)
$$
One defines a MixedSiteSet taking the two partice types as template paramters

       auto sites = Holstein(N,{"ConserveNf=",true,"ConserveNb=",false,"MaxOcc=",2});

The "site set" is of lenght N and has spinless fermionic degrees of freedom on every second site, with a conserved number of fermions, and  bosonic degrees of freedom on the even sites with a maximum occupancy of 2 and without conservation of the bosons.
It is important to assigne the correct operators to the corresponding sites, so that the fermionic operators only act on site 1, 3 etc. in the Hamiltonian.

        auto ampo = AutoMPO(sites);
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
	    auto H = toMPO(ampo);
    
We then generate an initial state which only contains one fermion and compute: 

	auto state = InitState(sites);
	state.set(5,"Occ");
    auto psi0 = randomMPS(state);
We then compute the ground state.
### Full example code:

    include:docs/VERSION/formulas/2d_dmrg.cc

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/2d_dmrg.cc">Download the full example code</a>
