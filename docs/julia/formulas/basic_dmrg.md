# Perform a basic DMRG calculation #

Because tensor indices in ITensor have unique identities, before we can make a Hamiltonian
or a wavefunction we need to construct a "site set" which will hold the site indices defining
the physical Hilbert space:

    N = 100
    sites = siteinds("S=1",N)

Here we have chosen to create a Hilbert space of N spin 1 sites. The string "S=1"
denotes a special Index tag which hooks into a system that knows "S=1" indices have
a dimension of 3 and how to create common physics operators like "Sz" for them.

Next we'll make our Hamiltonian matrix product operator (MPO). A very 
convenient way to do this is to use the AutoMPO helper type which lets 
us input a Hamiltonian (or any sum of local operators) in similar notation
to pencil-and-paper notation:

    ampo = AutoMPO()
    for j=1:N-1
      ampo += (0.5,"S+",j,"S-",j+1)
      ampo += (0.5,"S-",j,"S+",j+1)
      ampo += ("Sz",j,"Sz",j+1)
    end
    H = MPO(ampo,sites)

In the last line above we convert the AutoMPO helper object to an actual MPO.

Before beginning the calculation, we need to specify how many DMRG sweeps to do and
what schedule we would like for the parameters controlling the accuracy.
These parameters are stored within a sweeps object:

    sweeps = Sweeps(5) # number of sweeps is 5
    maxdim!(sweeps,10,20,100,100,200) # gradually increase states kept
    cutoff!(sweeps,1E-10) # desired truncation error

The random starting wavefunction `psi0` must be defined in the same Hilbert space
as the Hamiltonian, so we construct it using the same collection of site indices:

    psi0 = randomMPS(sites,2)

Here we have made a random MPS of bond dimension 2. We could have used a random product
state instead, but choosing a slightly larger bond dimension can help DMRG avoid getting
stuck in local minima. We could also set psi to some specific initial state using the 
function `productMPS`, which is actually required if we were conserving QNs.

Finally, we are ready to call DMRG:

    energy,psi = dmrg(H,psi0,sweeps)

When the algorithm is done, it returns the ground state energy as the variable `energy` and an MPS 
approximation to the ground state as the variable `psi`.

Below you can find a complete working code that includes all of these steps:

    include:docs/VERSION/formulas/basic_dmrg.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/basic_dmrg.jl">Download the full example code</a>
