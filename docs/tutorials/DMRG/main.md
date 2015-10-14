<span class='article_title'>Density Matrix Renormalization Group</span>

<span class='article_sig'>Thomas E. Baker and Benedikt Bruognolo&mdash;September 15, 2015</span>

One of the most successful methods to calculate low dimensional systems is known as the density matrix renormalization group (DMRG).  DMRG uses the [[MPS|tutorials/MPS]] and [[MPO|tutorials/MPO]] representation to calculate the ground state of a low dimensional quantum system.  The algorithm DMRG is the combination of three other methods that we covered elsewhere:  

  1.  The optimization problem is constructed as a two-site object from the full tensor network
  2.  This reduced operator is solved by an eigensolver such as the [[Lanczos||tutorials/Lanczos]] or [[Davidson algorithm|tutorials/davidson]]
  3.  We apply an [[SVDs|tutorials/SVD]] and move to the next two sites

There are various permutations of the above algorithm (for example, single site DMRG is a possibility), but this article will discuss the current implementation in ITensor.

This article will cover how and why DMRG works.  We will end with a section describing the use of ITensor's `dmrg` function.

## How DMRG works

DMRG seeks to reduce the full Hamiltonian, which grows exponentially (for a spin-half chain this grows like @@2^L@@ for @@L@@ spins) in the system size, to a smaller eigenvalue problem to solve for the ground state.  So, we could solve something like

<p align="center"><img src="docs/tutorials/DMRG/schrodinger.png" alt="Schrodinger's equation" style="width: 600px;"/></p>

which is simply Schrodinger's equation,

$$
\mathcal{H}|\psi\rangle=E|\psi\rangle
$$


Quickly counting, there are five physical indices that are open on our five site system.  This implies that we are working with a rank five tensor to solve the entire system.  We could solve this with an exact diagonalization calculation (or similar), but for a larger systems, the computational cost grows exponentially with system size (this is bad!) implying that larger systems are inaccessible.  We want to reformulate the problem to search over a reduced number of degrees of freedom. 

We can variationally optimize for some of the components of the MPS instead of all of them at the same time. The equation to search for two components in the MPS is

<p align="center"><img src="docs/tutorials/DMRG/dmrg_eig0.png" alt="DMRG eigenvalue equation" style="width: 600px;"/></p>

The MPS has now been gauged so its orthogonality center is located on the tensor we wish to minimize. Note that we have chosen to vary two tensors in the network.  This allows for full control of the bond dimension in the SVD; there are single site updates, but ITensor currently uses a two site update.  No matter how many tensors are chosen to variationally minimize, truncating the network like this incurs a large savings in that the network. 

The tensor multiplying @@E@@ can be contracted down to a single tensor:

<p align="center"><img src="docs/tutorials/DMRG/dmrg_eig.png" alt="DMRG eigenvalue equation" style="width: 600px;"/></p>

Mathematically varying tensor is equivalent to taking the partial derivative of the expectation value of the normalized Hamiltonian,

$$
\frac{\partial}{\partial A_i^*}\frac{\langle\psi|\mathcal{H}|\psi\rangle}{\langle\psi|\psi\rangle}\overset!=0
$$ 

Varying both (as shown above) is

$$
\frac{\partial}{\partial [A\_{i}^\ast{}A\_{i+1}^{\ast}]}\frac{\langle\psi|\mathcal{H}|\psi\rangle}{\langle\psi|\psi\rangle}\overset!=0
$$ 

and require the solution to find the variational minimum in energy.  We will always place the orthogonality center on the tensor we want to obtain.  This form of the eigenvalue problem is handling a tensor that is rank four (which is reduced to rank two, see below).  In order to find the tensor, we may use a sparse eigenvalue solver like the Lanczos or Davidson algorithms in the reduced Hilbert space and solve the equation 

$$
\mathcal{H}[A^{\sigma\_i}\_{a\_ia\_{i+1}}A^{\sigma\_{i+1}}\_{a\_{i+1}a\_{i+2}}]-E[A^{\sigma\_i}\_{a\_ia\_{i+1}}A^{\sigma\_{i+1}}\_{a\_{i+1}a\_{i+2}}]\overset!=0
$$

While the mathematical expression for this eigenvalue problem on the local tensor is cumbersome (we have hidden a complicated sum by simply writing @@\mathcal{H}@@ in the above), the ITensor code is not.  We will cover how the [[Lanczos and Davidson|]] algorithms work in the library in another article; however,  ITensor provides a function `davidson` that will evaluate this for us

    auto H;//define an operator
    auto psi;//define a wavefunction
    auto args;//arguments
    davidson(H,psi,args);//returns the scalar energy

The output of the `davidson` algorithm undergoes a SVD in order to restore the form of the MPS. There is one more step that must be taken to ensure the algorithm is fast and can solve larger systems than exact diagonalization.  Keeping all states in the SVD is not necessary to obtain the correct ground state at an acceptable accuracy. Truncating the MPS in the SVD keeps only the most relevant degrees of freedom for the ground state and eliminates extraneous degrees of freedom.  Sweeping back and forth in the system eventually approaches the ground state.   

The [[Mini-Course|course]] contains a DMRG tutorails and shows how the ITensor codes works in full.

### Why DMRG works:  Information Theory and Entanglement

When receiving a message that is known to have some characters distorted, it is necessary to determine what the uncertainty of a particular character @@x@@ might be.  For, how sure are we that this was the original character sent?  We therefore search for a mathematically rigorous way of defining the uncertainty of @@x@@ and connecting this to the the probability of choosing the correct @@x@@. The quantity we are searching for is most critical to the understanding of how much information can be sent though the communication channel is known as the information entropy (also known as the entanglement entropy).  The first step is to quantify how much uncertainty there is in the message (especially, say, if some of the message is garbled).

Beginning from the most general statements, there are four conditions we can expect on any measure of information passing through a channel [1].

 * The probability, @@\rho@@, should increase with more possibilities, @@M@@ available to sample (i.e., @@\rho(M)<\rho(M')@@ if @@M<M'@@)

Consider the task of finding one star in the universe in comparison with predicting the roll of a six sided die.  The former should have a much higher uncertainty in the choice.

 *  The probabilities for two objects should be additive as @@\rho(ML)=\rho(M)+\rho(L)@@

If we have two objects we want to find from two different sets, then we expect that picking the first object will not affect the uncertainty of choosing the second.

 * Assume the grouping axiom:  the uncertainty of picking an object from the set of @@r@@ elements @@x\_1, x\_2, x\_3, x\_4,\ldots@@ with probabilities @@\rho\_1, \rho\_2, \rho\_3, \rho\_4,\ldots@@ is

$$
H\left(\frac{\rho\_1}{\sum\_{\rho=1}^r \rho\_i},\frac{\rho\_2}{\sum\_{\rho=1}^r \rho\_i},\frac{\rho\_3}{\sum\_{\rho=1}^r \rho\_i},\ldots\right)
$$

and the uncertainty of picking an object,  from the second group is @@x\_{r+1}, x\_{r+2}, x\_{r+3}, x\_{r+4},\ldots@@ is then 

$$
H\left(\frac{\rho\_{r+1}}{\sum\_{\rho=1}^M \rho\_i},\frac{\rho\_{r+2}}{\sum\_{\rho=1}^M \rho\_i},\frac{\rho\_{r+3}}{\sum\_{\rho=1}^M \rho_i},\ldots\right)
$$

the sum of these two equations is the uncertainty in each of the two groups plus a term 

$$
H(\rho\_1+\rho\_2+\rho\_3+\ldots+\rho\_r,\rho\_{r+1}+\ldots+\rho\_M),
$$

signifying the uncertainty for picking either group, are the total uncertainty.

 * Small changes in the probability should produce small changes in the uncertainty so that @@H(p,1-p)@@ is continuous.

With these four assumptions, it can be shown that an entropy  function

$$
S=-C\sum_i\rho\_i\ln\rho\_i
$$

where @@C@@ is a constant and @@\rho_i@@ are the probabilities of the @@i^\mathrm{th}@@ possibility (later, this will be the eigenvalue), is the only function that can satisfy the four statements above.  The special case of @@C=1@@ is the von Neumann entropy.

The meaning of the information entropy is many-fold, but one of the more transparent meanings is that it is the minimum number of questions you must ask to get the answer (on average). For example, consider many variables that could be the answer.  We can search for the correct answer by asking for a yes or no on each variable ("Is it @@x_1@@? @@x_2@@?...").  The minimum of the average number of these questions is the information entropy.  

By calculating the reduced density matrix correctly, DMRG is automatically maximizing the von Neumann entropy.  This is the fundamental reason why DMRG obtains the correct ground state, it gets the correct information entropy.  One can visualize this as passing information from block to block.

A point worth mentioning here is the area law.  Ground states and low lying excited states tend to follow the area law. The area law states that entanglement scales with system size and dimension for two partitions of a system--in effect, with the area.  In one dimension, the "area" between two blocks is zero-dimensional (it is just a point).  Since entanglement doesn't increase with system size in this case, attacking the problem by maximizing the entropy is efficient.  

DMRG still works in higher dimensions, but the area law says that entanglement will increase with system size (in 2D, the area between partitions is a line while 3D has a sheet between partitions).  This can be seen by recognizing that [[higher dimensional lattices can be mapped to lower dimensional lattices with longer range interactions|tutorials/MPO]].  Increasing entanglement is harder to calculate through DMRG, seen by increasing matrix sizes for the MPO (making individual steps in DMRG slower), hence it is known as a minimally entangled algorithm.

## How to use ITensor's `dmrg` function 

To run a DMRG calculation, we can use the `dmrg` function as

    MPO H;//or IQMPO
    MPS psi;//or IQMPS
    
    //add sweeps and opts here

    auto energy = dmrg(psi,H,sweeps,opts);

Several options are available for the `dmrg` function in the `sweeps` and `opts` options.  We survey the possible options here briefly.

### Sweeps

The `Sweeps` class specifies accuracy parameters during a sweep.  An example programming code for each parameter is given below.  The values may require change based on the application.

 * `sweeps`

Controls the number of sweeps used to optimize the ground state wavefunction.

    Sweeps sweeps(10);//initializes the sweeps class

 * `maxm`

Controls the maximum number of many body states kept in the [[singular value decomposition|tutorials/SVD]].  The default value is 500.

    sweeps.maxm() = 10,20,100,100,200;//the maximum bond dimension
                                      //ITensor repeats the last entry if 
                                      //more sweeps are called for

 * `minm`

Controls the minimum number of many body states kept in the [[singular value decomposition|tutorials/SVD]].  The default value is 1.

    sweeps.minm() = 1,2,10,10,20;//the minimum bond dimension
                                      //ITensor repeats the last entry if 
                                      //more sweeps are called for

 * `cutoff`

Eigenvalues (equivalently, singlar values squared) greater than the defined `cutoff` are kept in the matrix @@D@@ of the singular value decomposition.  If the number of eigenvalues larger than the `cutoff` is bigger than `maxm`, only the `maxm` number of largest eigenvalues are kept.  The default is @@10^{-8}@@

    sweeps.cutoff() = 1E-10;

 * `niter`

Number of `davidson` iterations for each variational optimization.  The default is ???.

    sweeps.niter() = 2;

Note that there is a tradeoff between accuracy (larger `niter`) and speed (smaller `niter`).

 * `noise`

Includes a small noise term in the MPS at each step to help convergence and avoid getting stuck in a local minimum.  The default is zero.

    sweeps.noise() = 1E-3,1E-4,1E-8,1E-12,0;

### args

To initialize `args`, we use the `Args` (formerly `OptSet`) as

    Args args;

 * `Quiet`

Minimizes output of `dmrg`.  Default is `true`.

    args.add("Quiet",false);

 * `energy_errgoal`

Stops `dmrg` once the energy difference between consecutive sweeps is below the given value of `energy_errgoal`. Default is -1 (will carry out all sweeps no matter the `energy_errgoal`).

    args.add("energy_errgoal",1E-3);

MILES:  What is the correct default and syntax here?

## References

[1] Robert B. Ash and Catherine Doleans-Dade, Probability and measure theory (Academic Press, 2000).
