# Time Evolving an MPS with an MPO

(Throughout this formula I will use the ITensor, MPS, and MPO classes. To take advantage
of quantum numbers automatically for symmetric Hamiltonians, 
use the IQTensor, IQMPS, and IQMPO classes instead but otherwise leave the code the same.)

First set up the MPS you would like to time evolve. An easy way to do this is to make
a product state using the InitState helper class:

    #include "itensor/mps/sites/spinhalf.h"
    #include "itensor/mps/autompo.h"
    //...
    int N = 100;
    auto sites = SpinHalf(N);
    auto state = InitState(sites);
    for(int i = 1; i <= N; ++i)
        {
        //Neel state
        state.set(i,i%2==1 ? "Up" : "Dn");
        }
    auto psi = MPS(state);

Next we can use AutoMPO to specify a Hamiltonian, and use the "toExpH" function to exponentiate this
Hamiltonian:

    auto ampo = AutoMPO(sites);
    //Make the Heisenberg Hamiltonian
    for(int b = 1; b < N; ++b)
        {
        ampo += 0.5,"S+",b,"S-",b+1;
        ampo += 0.5,"S-",b,"S+",b+1;
        ampo +=     "Sz",b,"Sz",b+1;
        }
    auto H = MPO(ampo);
    auto tau = 0.1;
    auto expH = toExpH<ITensor>(ampo,tau);

In the above example, expH will be approximately equal to @@exp(-\tau H)@@ up to terms of order @@\tau^2@@.
For more details on this construction, see the following article: <a href="http://journals.aps.org/prb/abstract/10.1103/PhysRevB.91.165112" target="_blank">Phys. Rev. B 91, 165112</a>. (Alternatively arxiv:1407.1832.) As mentioned in the article, you can also combine two complex time steps to further reduce the scaling of the errors with @@\tau@@.

To do real-time evolution instead, change the time step to be imaginary:

    auto expH = toExpH<ITensor>(ampo,tau*Cplx_i);

which gives @@exp(-i\tau H)@@. Fully complex time steps @@\tau=a+ib@@ are fine too.

To carry out the actual time evolution, repeatedly apply the MPO to the MPS using one of the following methods:

* `exactApplyMPO(psia,K,psib)` &mdash; exactly computes @@|\psi\_b\rangle = \hat{K} |\psi\_a\rangle@@. Only use this for very small MPS!

* `fitApplyMPO(psia,K,psib[,args])` &mdash; compute @@|\psi\_b\rangle = \hat{K} |\psi\_a\rangle@@ using a DMRG-style "fitting" algorithm. Very efficient but can fail if @@|\psi\_b\rangle@@ is too different from @@\hat{K}|\psi\_b\rangle@@ (this failure isn't a concern for time evolution with a small time step). Of the optional args recognized by this function, two key ones are "Cutoff" which specifies the truncation-error cutoff used to truncate the resulting MPS and "Maxm" which sets an upper limit on the bond dimension of the resulting MPS.

* `zipUpApplyMPO(psia,K,psib)` &mdash; computes @@|\psi\_b\rangle = \hat{K} |\psi\_a\rangle@@ using the "zip up" algorithm described in  New. J. Phys. 12, 055026. 


Here is some sample code using one step of exactApplyMPO (since we started from a product state) followed by fitApplyMPO
for the rest of the steps:

    auto args = Args("Cutoff=",1E-9,"Maxm=",3000);
    auto ttotal = 3.0;
    auto nt = int(ttotal/tau+(1e-9*(ttotal/tau)));

    exactApplyMPO(psi,expH,psi);

    for(int n = 2; n <= nt; ++n)
        {
        fitApplyMPO(psi,expH,psi,args);
        }


