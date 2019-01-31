<span class='article_title'>Converging DMRG</span>

<span class='article_sig'>Thomas E. Baker&mdash;April 28, 2016</span>

Now that you've set up a basic DMRG or other tensor network calculation (perhaps with our [[quickstart|tutorials/quickstart]] guide), you're ready to get the best answer possible.

This tutorial contains some in-house information we like to use to converge our calculations.  The following covers options in the `Args` class and general considerations when running a calculation.

### What we are calculating

DMRG is often hailed as the "gold-standard" of one-dimensional calculations.  It is true that DMRG is wonderfully powerful both in speed and accuracy.  But the question is not how accurate and how fast we can obtain the answer.

The question is: for what system did we obtain a fast and accurate answer?

Consider a basic example of a free particle:

$$
\mathcal{H}=-\frac12\partial_x^2\phi
$$

The problem must be phrased in some basis.  For the sake of example, let's express the derivatives as a finite difference

$$
\frac{\partial\phi}{\partial x}=\underset{\Delta x\rightarrow0}{\lim}\frac{\Delta\phi}{\Delta x}\Rightarrow\frac{\partial^2\phi}{\partial x^2}=\underset{\Delta x\rightarrow0}{\lim}\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{\Delta x^2}
$$

Although for realistic calculation, we need to keep @@\Delta x@@ at some finite value (called a grid spacing, @@a@@).  Note that @@i@@ is an index over all grid points.

The second quantized Hamiltonian for this problem is written as

$$
\mathcal{H} = t \hat c^\dagger_{i+1}\hat c_i-2t\hat n_i+t \hat c^\dagger_i\hat c_{i+1}
$$

where @@t=-1/(2a^2)@@ and a sum over spins has been ignored (recovered below).  This can be implemented in ITensor through [[AutoMPO|tutorials/AutoMPO]] as

    auto a = 0.01; //grid spacing
    auto t = -1/(2*pow(a,2));
    AutoMPO ampo;
    for(int i = 1;i < Ns; ++i) //Ns = number of sites
    {
      ampo += t,"Cdagup",i,"Cup",i+1; //must be ordered i->i+1
      ampo += t,"Cdagdn",i,"Cdn",i+1; //for Fermion phases
      ampo += -t,"Cup",i,"Cdagup",i+1;
      ampo += -t,"Cdn",i,"Cdagdn",i+1; 
      ampo += -2*t,"Ntot",i;          //density term
    }
    auto H = IQMPO(ampo);//generates MPO

DMRG can then calculate the ground state energy.  But does so for the **finite size** Hamiltonian.  Not the continuum!

The main point of this section is that to get the continuum answer, one must calculate several grid spacings @@a@@ and then extrapolate the continuum answer. 

In the same way that we might need to tune parameters of our system (grid spacing, etc.), the parameters specific to the DMRG algorithm also need to be considered.  We continue with those in the next section.

### Convergence parameters in DMRG

The basic parameters that need consideration for any DMRG calculation are `maxm`, `minm`, `cutoff`, `niter`, `nsweeps`, the truncation error, and `noise`.  Each is covered in a separate section below.

When implementing the parameters into the `dmrg` function, the syntax

    dmrg(psi,H,{"cutoff",1E-4,"maxm",40},"Quiet"); //optional: "Quiet" reduces output

can be used.  Alternatively, the `Args` class can store all the desired parameters.

    Args args;
    args.nsweeps() = 20;
    args.maxm() = 20,40,80,160,400;//repeats 400 for all other sweeps
    args.minm() = 20;
    args.noise() = 1E-3,1E-4,1E-4,1E-8,1E-10,1E-12;

    dmrg(psi,H,args);

For each different system and each different user, the values needed are different.  Consider playing around with a few practice runs to see how the values you wish (such as ground state energy or entanglement) behave under different parameters.

The choice to make is always between accuracy and speed.

#### Maximum states kept: `maxm`

When performing an [[SVD//tutorials/SVD]], the maximum number of singular values kept (in other words the size of the diagonal @@D@@ matrix), can be truncated to a number `maxm`.

If the size of @@D@@ is lower than `maxm`, then that size is kept.

The use of `maxm` is "dumb" in contrast to `cutoff` (see below).  Typically, one can grow the size of `maxm` over the number of sweeps.  We typically grow this parameter exponentially (see above example).  Obviously, if your computer can not handle a certain matrix size, `maxm` can be used to keep the size lower.

Note that keeping `maxm` large can keep a lot of singular values that have a very low weight.  This is inefficient if the small singular values do not contribute to the overall answer.

#### Minimum number of states: `minm`

`minm` has two primary uses that are only necessary for some specific calculations.

The first is testing speed.  If one wishes to know how fast a sweep of DMRG performs with bond dimension (effectively `maxm`), it may be useful to fix this quantity by settig `minm` = `maxm`.  This ensures the size of the tensors at each site in the MPS are identical.

The other use of `minm` is to ensure the wavefunction has enough size to grow from the first (random) guess state.  Setting `minm` to be 20 on the first sweep is sufficient in most cases of our interest.  This also does not run too slowly, though we point out that smaller values of `minm` also perform well.

#### Magnitude of singular values: `cutoff`

The `cutoff` is a "smart" way to truncate the size of the singular values (in contrast with `maxm` which was "dumb").

Effectively, so long as the inequality

$$
\lamda^2_n\geq \mathrm{cutoff}
$$

the singular value will be kept.

Let's pretend we identify an accuracy we wish to achieve with our DMRG run as @@10^{-3}@@.  Setting `cutoff=1E-4` would then be a suitable starting point.

#### Number of iterations in Davidson: `niter`

This is the number of steps in the Davidson algorithm used at each step of the [[DMRG|tutorials/DMRG]] algorithm.

The choice for the size of the basis set is up to the user, but we recommend `niter=2`.  Why?  Increasing the number of kyrlov vectors kept decreases the runtime of `dmrg`.  Further, the extra accuracy given by a larger `niter` doesn't help converge `dmrg` to any higher accuracy.  The reason for this second remark is that we want a small change of the state vector for a given block.  Changing the vector by a larger amount may overshoot the actual answer.

The key difference is that converging a local block in DMRG, for example, doesn't necessarily help converge the entire system globally.

#### Number of sweeps: `nsweeps`

This is simply the number of sweeps (left to right or right to left) that DMRG will perform.

For simple systems, DMRG converges in a few tens of sweeps.  However, it might be desirable to increase this number if the difference in the energy is not small from sweep to sweep.

#### Avoiding local minima: `noise`

It is possible for DMRG to get stuck in a local minimum.  This implies the method does not always reach the ground state despite having a good truncation error or other seemingly converged indicator.

Adding some noise to a a calculation can "shake" it out of local minima and help converge to the true ground state.

Reference [1] details how noise can be added to a DMRG calculation without destroying the [[quantum number flux|tutorials/IQTensor]].  

### Additional notes

Some aspects of converging DMRG above demand extra consideration.

#### Two-dimensional systems

The bond dimension for a two-dimensional system [[increases substantially|tutorials/MPO]].  This makes DMRG harder to converge.

Note that the entanglement in a given system is typically the last parameter to converge.

Truncation error is something we like to look for in 2D calculations.  If the value is below @@10^{-5}@@, this tends to signal the ground state has been reached.

For reference, the truncation error is defined as the sum of the discarded singular values.  One may find it useful to extrapolate in the truncation error by increasing `maxm` or decreasing `cutoff`.

#### Pinning fields

In order to isolate some behaviors in a system, a pinning field can be applied to certain sites.  Because this depends so strongly on the system considered, we refer the interested reader to a comprehensive article [2].

### Infinite DMRG calculations

The [[`idmrg` function|tutorials/iDMRG]] has special convergence parameters. 

when calling `idmrg`, some useful flags are

    idmrg(psi,infH,infsweeps,{"OutputLevel",2,"NUCSweeps",nsubsweeps});

`infsweeps` is a `Sweeps` class parameter.  

The default number of sweeps over the unit cell is 1 (`nsubsweeps`=1).  Any other number of subsweeps must be odd to avoid an error.  The reason for this is the placement of the orthogonality center for the next sweep.

The number of sweeps (`infsweeps`) for the whole algorithm (number of unit cells inserted) must be even for similar reasons.

### References

[1] S.R. White

[2] E. Miles Stoudenmire and Steven R. White. "Studying Two-Dimensional Systems with the Density Matrix Renormalization Group." Annu. Rev. Condens. Matter Phys. 3.1 (2012): 111-128.

