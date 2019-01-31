
# Choosing DMRG Parameters

<span class='article_sig'>Miles Stoudenmire&mdash; Jan 4, 2017</span>

When using the density matrix renormalization group (DMRG) algorithm,
a common question is how to choose the best algorithm parameters, 
such as the number of sweeps or truncation error cutoff for each sweep.
There are no perfect choices for these parameters, but this tutorial 
attempts to provide a basic starting point for understanding.
Fortunately DMRG is quite a robust algorithm, so you do not have to
worry excessively about getting the wrong answer; the more common
concern is about minimizing the calculation time. When in doubt, perform
your own experiments: do additional sweeps or vary the cutoff or bond 
dimension parameters to see if your results change significantly.

This tutorial only discusses the basic, ground-state DMRG algorithm.
ITensor also supports more advanced algorithms such as infinite DMRG
which may have additional parameters. For more information on these
algorithms see the [[in-depth documentation|classes]].

# Table of Contents

* <a href="#basic">Basic DMRG Parameters</a>
* <a href="#basic_sample">Basic Sample Parameter Schedules</a>
* <a href="#advanced">Advanced DMRG Parameters</a>
* <a href="#adv_sample">Advanced Sample Parameter Schedules</a>

<a name="basic"></a>
# Basic DMRG Parameters

The most basic parameters controlling a DMRG calculation are

* Number of sweeps
* Maximum MPS bond dimension (`maxm`)
* Truncation error cutoff (`cutoff`)

For slightly more advanced parameters see further below.

These parameters are set by creating a [[Sweeps|classes/sweeps]] object.
See the [[Sweeps class documentation|classes/sweeps]] for more information 
on creating a [[Sweeps|classes/sweeps]] object and for very precise
definitions of what each parameter does.

## Number of Sweeps

For an easy-to-converge system such as a one-dimensional (1D) spin chain,
DMRG can give excellent results in as few as 4-5 sweeps.

For more challenging lattice models, such as quasi-two-dimensional (2D) systems or
systems with widely varying energy scales such as the 2D Hubbard model,
you may find as many as 10 sweeps are needed. One reason is simply because DMRG
can take longer to converge properties related to small energy scales or
longer-ranged interactions. Another reason is that you may want to extrapolate
your results as a function of the truncation error; in this case more sweeps
are needed to get a reliable extrapolation.

In short, the number of sweeps can in principle be small, but it never hurts
to do one more sweep to check. Try to find a good number by doing a less accurate
calculation for your system before trying more accurate and expensive runs.

## Maximum Bond Dimension

The `maxm` parameter sets the maximum bond dimension "m" the MPS is allowed
to have on each sweep, and can be different for each sweep. Below some
sample sweeping schedules are provided with different strategies for choosing
`maxm`. 

The most important thing about choosing `maxm` is to make it small
in the first 1-3 sweeps. MPS wavefunctions with bond dimensions as small as m=10
can be surprisingly good at capturing the essential physics, while being extremely
cheap for DMRG, so the first sweep should have a `maxm` in the 10-50 range, followed
by slightly larger `maxm` values until going to a high, or very high `maxm` in the 
last few sweeps.

For 1D systems, bond dimensions in the hundreds are often sufficient for high accuracy.
For ladder or quasi-2D systems, the bond dimension must be raised exponentially as
a function of the transverse system size, and can reach many thousands for large 2D calculations.

## Truncation Error Cutoff

The `cutoff` parameter is very useful because it controls the bond dimension
of the MPS in a "smart" and adaptive way. Setting the cutoff to a modestly small
value such as 1E-8 guarantees accuracy, assuming `maxm` is sufficiently large. But in regions
where the bond dimension could be smaller, setting a 
cutoff will let the bond dimension shrink as much as possible without sacrificing accuracy.

Very roughly speaking, a cutoff of 1E-5 gives sensible accuracy; a cutoff of 1E-8 is high accuracy;
and a cutoff of 1E-12 is near exact accuracy.

<a name="basic_sample"></a>
# Basic Sample DMRG Parameter Schedules

Below are some sample parameter schedules which 
use different strategies to converge a DMRG calculation.
Which strategy to use depends on your resource constraints 
and your research goals. 

In the schedule tables below, each row is a different sweep.

## Maxm Dominated Schedule

If your goal is to reach an accurate ground state
while ensuring an efficient calculation, 
then controlling the accuracy primarily through the `maxm` parameter is 
a good approach.
Often you may know in advance that a certain final `maxm` will give sufficient accuracy,
for example m=200 is quite good for the S=1 Heisenberg spin chain.

```
nsweeps = 5
maxm  minm  cutoff  niter  noise
10    1     1E-5    2      0
20    1     1E-8    2      0
80    1     1E-12   2      0
200   1     1E-12   2      0
200   1     1E-12   2      0
```

## Cutoff Dominated Schedule

If your main priority is finding an accurate ground state, and
you are willing to spend the resources necessary to do this or 
do not have a good idea up-front of what final `maxm` to choose,
then you can quickly increase `maxm` to a very high value 
and let the truncation error cutoff set the actual bond dimension 
DMRG will choose, which could be much less than the `maxm` specified. 
It is still smart to keep `maxm` low initially, 
though, so as not to waste time during the initial few sweeps.

```
nsweeps = 6
maxm  minm  cutoff  niter  noise
20    1     1E-5    2      0
80    1     1E-6    2      0
200   1     1E-7    2      0
400   1     1E-8    2      0
800   1     1E-8    2      0
800   1     1E-8    2      0
```


<a name="advanced"></a>
# Advanced DMRG Parameters

* Number of Davidson algorithm interations (`niter`)
* Noise term strength (`noise`)
* Minimum MPS bond dimension (`minm`)

## Number of Davidson Iterations

The core of DMRG is the Davidson algorithm, which is type of iterative exact diagonalization
algorithm, somewhat similar to Lanczos. The parameter setting the maximum number of Davidson 
iterations at each step of DMRG is `niter`. Due to the way the ITensor Davidson code is defined,
the minimum value of `niter` you should use is 2 (two vectors in the basis built by the algorithm).

Often just keeping `niter` equal to 2 is sufficient and fast for most systems. But for tough
systems, such as Hubbard models or long-range models, increasing `niter` can help. 

It is essentially never a good idea to fully converge the inner Davidson loop of a DMRG calculation, 
since the MPS environment defining the projected Hamiltonian used in the Davidson calculation
is only approximate anyway. DMRG can still perfectly converge with the minimum number of Davidson
steps since it does multiple sweeps over the system.

## Noise Term

The noise term is a technique originally developed for the single-site DMRG method, but which
is also useful for two-site DMRG (the algorithm provided with ITensor). It can be especially
useful for ensuring convergence of calculations which conserve quantum numbers or calculations
of quasi-2D systems.

To read about the definition of the noise term, see 
the [original paper by White](https://doi.org/10.1103/PhysRevB.72.180403).

The noise term is basically an ad-hoc perturbation that is added to the density matrix at 
each step before diagonalizing it to get the new MPS basis. It can improve MPS which
are deficient in some way (e.g. lacking certain "quantum fluctuations" which are present
in the true ground state). But taking the noise term too large can prevent DMRG from
finding an optimal MPS, so it should be reduced to a small value or turned off in the 
last few sweeps.

Roughly speaking, 1E-5 is a lot of noise and 1E-12 is a minimal amount of noise that
can still be considered non-zero.


<a name="adv_sample"></a>
# Advanced Sample DMRG Parameter Schedules

## Schedule with Noise Term

The schedule below could be for a Hubbard chain or ladder, or
some other model where we want to conserve quantum numbers
and can find the system difficult to converge.

```
nsweeps = 7
maxm  minm  cutoff  niter  noise
10    1     1E-5    4      1E-5
20    1     1E-6    3      1E-5
80    1     1E-7    3      1E-8
200   1     1E-8    2      1E-9
300   1     1E-8    2      1E-10
400   1     1E-8    2      1E-10
400   1     1E-8    2      1E-10
```
