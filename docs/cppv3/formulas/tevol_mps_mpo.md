# Time Evolving an MPS with an MPO

First set up the MPS you would like to time evolve. An easy way to do this is to make
a product state using the InitState helper class:

    #include "itensor/all.h"
    //...
    int N = 100;
    auto sites = SpinHalf(N,{"ConserveQNs=",true});
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
    auto H = toMPO(ampo);
    auto tau = 0.1;
    auto expH = toExpH(ampo,tau);

In the above example, expH will be approximately equal to @@exp(-\tau H)@@ up to terms of order @@\tau^2@@.
For more details on this construction, see the following article: <a href="http://journals.aps.org/prb/abstract/10.1103/PhysRevB.91.165112" target="_blank">Phys. Rev. B 91, 165112</a>. (Alternatively arxiv:1407.1832.) As mentioned in the article, you can also combine two complex time steps to further reduce the scaling of the errors with @@\tau@@.

To do real-time evolution instead, change the time step to be imaginary:

    auto expH = toExpH(ampo,tau*Cplx_i);

which gives @@exp(-i\tau H)@@. Fully complex time steps @@\tau=a+ib@@ are fine too.

To carry out the actual time evolution, repeatedly apply the MPO to the MPS using one of the following methods:

* `psib = exactApplyMPO(K,psia[,args])` &mdash; exactly compute @@\hat{K} |\psi\_a\rangle@@ then recompress the result as an MPS @@|\psi\_b\rangle@@. Not the fastest method, but is fully controlled and does not have any risk of getting stuck (versus fitApply, which in contrast can have different output based on the initial state provided). Providing the named args "Cutoff" and "Maxm" control the amount of truncation of the resulting MPS.

* `fitApplyMPO(psia,K,psib[,args])` &mdash; compute @@|\psi\_b\rangle = \hat{K} |\psi\_a\rangle@@ using a DMRG-style "fitting" algorithm. Very efficient but can fail if @@|\psi\_b\rangle@@ is too different from @@\hat{K}|\psi\_b\rangle@@ (this failure isn't a concern for time evolution with a small time step). Of the optional args recognized by this function, two key ones are "Cutoff" which specifies the truncation-error cutoff used to truncate the resulting MPS and "Maxm" which sets an upper limit on the bond dimension of the resulting MPS.

The recommended practice is to use exactApplyMPO to make sure your code is working. Then consider switching to fitApplyMPO if you need more efficiency, especially if the MPO you are applying has a large bond dimension. But verify that the results you obtain with fitApplyMPO are very similar to the ones you obtain with exactApplyMPO.

Here is some sample time evolution code using exactApplyMPO:

    auto args = Args("Cutoff=",1E-9,"Maxm=",3000);
    auto ttotal = 3.0;
    auto nt = int(ttotal/tau+(1e-9*(ttotal/tau)));

    for(int n = 1; n <= nt; ++n)
        {
        psi = exactApplyMPO(expH,psi,args);
        normalize(psi);
        }


