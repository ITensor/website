# Algorithms for MPS and MPO (also IQMPS and IQMPO)


## Summing MPS

* `sum(MPS A1, MPS A2, Args args = Args::global()) -> MPS` <br/>

  Return the sum of the MPS `A1` and `A2`. The returned MPS will have 
  an orthogonality center on site 1. Before being returned, the MPS 
  representing the sum will be compressed using truncation parameters
  provided in the named arguments `args`.

  The input MPS must have the same site indices. The link indices of
  the output MPS will have the same tags as the first input MPS.

  <div class="example_clicker">Show Example</div>

      auto A3 = sum(A1,A2,{"MaxDim",500,"Cutoff",1E-8});
  
* `sum(vector<MPS> terms, Args args = Args::global()) -> MPS`

  Returns the sum of all the MPS provided in the vector `terms` as a single MPS,
  using the truncation accuracy parameters (such as "Cutoff" or "MaxDim")
  provided in the named arguments `args` to control the accuracy of the sum.

  This function uses a hierarchical, tree-like algorithm which first sums pairs of MPS, 
  then pairs of pairs, etc. so that the largest bond dimensions are only
  reached toward the end of the process for maximum efficiency. Therefore using
  this algorithm can be much faster than calling the above two-argument 
  `sum` function to sum the terms one at a time.

  <div class="example_clicker">Show Example</div>

      auto terms = vector<MPS>(4);
      terms.at(0) = A0;
      terms.at(1) = A1;
      terms.at(2) = A2;
      terms.at(3) = A3;

      auto res = sum(terms,{"Cutoff",1E-8});


## Inner Products and Expectation Values

* `inner(MPS y, MPS x) -> Real` <br/>
  `innerC(MPS y, MPS x) -> Cplx`

  Compute the exact inner product @@\langle y|x \rangle@@ of two
  MPS (the tensors of `y` will get conjugated). 
  If the inner product is expected to be a complex number
  use `innerC`. 

  The algorithm used scales as @@m^3 d@@ where @@m@@ is a typical link
  dimension of the MPS and @@d@@ is the site dimension.

  Note that if `x` and `y` don't have the same site indices,
  this function will attempt to make them match.

* `inner(MPS y, MPO A, MPS x) -> Real` <br/>
  `innerC(MPS y, MPO A, MPS x) -> Cplx`

  Compute the exact inner product @@\langle y|A|x \rangle@@
  of two MPS `y` and `x` with respect to an MPO `A` (the tensors
  of `y` will get conjugated).

  The algorithm used scales as @@m^3\, k\,d + m^2\, k^2\, d^2@@ where @@m@@ is typical link
  dimension of the MPS, @@k@@ is the typical MPO dimension, and @@d@@ is the site dimension.

  Note that `A` and `x` must share a set of site indices. If the remaining site indices of `A` are
  not shared with `y`, this function will attempt to match them (i.e. it has the same behavior
  as `inner(y,Ax)` if `Ax` was the exact application of MPO `A` to MPS `x`).

* `inner(MPS y, MPO B, MPO A, MPS x) -> Real` <br/>
  `innerC(MPS y, MPO B, MPO A, MPS x) -> Cplx`

  Compute the exact inner product @@\langle y|BA|x \rangle@@
  of two MPS `y` and `x` with respect to two MPOs `B` and `A` (MPS `y` will get conjugated).

  MPO `A` must share a set of site indices with MPS `x`, and the other set of site indices with
  MPO `B`. If the remaining set of site indices of `B` are not shared with `y`, with function
  will attempt to make them match.

  The algorithm used scales as @@m^3\, k^2\,d + m^2\, k^3\, d^2@@ where @@m@@ is typical bond
  dimension of the MPS, @@k@@ is the typical MPO dimension, and @@d@@ is the site dimension.

* `inner(MPO B, MPS y, MPO A, MPS x) -> Real` <br/>
  `innerC(MPO B, MPS y, MPO A, MPS x) -> Cplx`

  Compute the exact inner product @@\langle By|A|x \rangle@@ (i.e. the inner product of
  of @@B|y \rangle@@ and @@A|x \rangle@@). MPO `B` and MPS `y` will get conjugated.

  MPO `A` must share a set of site indices with MPS `x`, and MPO `B` must share a set of site indices
  with MPS `y`. If the remaining site indices of `A` and `B` do not match with each other,
  the function will attempt to make them match.

  The algorithm used scales as @@m^3\, k^2\,d + m^2\, k^3\, d^2@@ where @@m@@ is typical bond
  dimension of the MPS, @@k@@ is the typical MPO dimension, and @@d@@ is the site dimension.

## Tracing an MPO

* `trace(MPO A) -> Real`

  `traceC(MPO A) -> Cplx`

  Trace over the site indices of the MPO.

* `trace(MPO A, MPO B) -> Real`

  `traceC(MPO A, MPO B) -> Cplx`

  Return the trace of the operator that would result from performing the exact contraction of MPO `A`
  with MPO `B`. For each `j`, `A(j)` and `B(j)` must share one or two site indices.

  Note that neither `A` or `B` will get conjugated by this function.

## Multiplying MPOs

* `nmultMPO(MPO A, MPO B, Args args = Args::global()) -> MPO`

  Multiply MPOs `A` and `B`, returning the results MPO.
  MPO tensors are multiplied one at 
  a time from left to right and the resulting tensors are compressed using
  the truncation parameters (such as "Cutoff" and "MaxDim") provided through
  the named arguments `args`.

  For each `j`, MPO tensors `A(j)` and `B(j)` must share a single site index.
  MPO `C` will contain the site indices not shared by MPOs `A` and `B`.
  In addition, the link indices of MPO `C` will have the same tags as the link
  indices of the MPO `A`.

  <div class="example_clicker">Show Example</div>
      
      auto sites = SiteSet(10,2);

      // Make trivial MPOs
      auto A = MPO(sites);
      auto B = MPO(sites);

      // Prime MPO A to ensure only one set of site indices are shared
      auto C = nmultMPO(prime(A),B,{"MaxDim",500,"Cutoff",1E-8});

      auto s3 = sites(3);
      Print(hasInds(C(3),{s3,prime(s3,2)})); //print: true


## Applying MPO to MPS

* `applyMPO(MPO A, MPS x, Args args = Args::global()) -> MPS`

  Apply an MPO `A` to an MPS `x`, resulting in an approximation to the MPS `y`:  
  @@|y\rangle = A |x\rangle@@. <br/>
  The resulting MPS is returned. The algorithm used is chosen with the parameter "Method" 
  in the named arguments `args`.

  MPO `A` and MPS `x` must share a set of site indices.
  The links of the output MPS will have the same tags as the links of the input MPS `x`. The site indices
  of the output MPS will be the site indices of `A` that are not shared with `x`.

  The default algorithm used is the <a href="https://tensornetwork.org/mps/algorithms/denmat_mpo_mps">"density matrix" algorithm</a>,
  chosen by setting the parameter "Method" to "DensityMatrix".
  If the input MPS has a typical bond dimension of @@m@@ and the MPO has typical bond 
  dimension @@k@@, this algorithm scales as @@m^3 k^2 + m^2 k^3@@.

  No approximation is made when applying the MPO, but after applying it the resulting
  MPS is compressed using the truncation parameters provided in the named arguments `args`.

  An alternative algorithm can be chosen by setting the parameter "Method" to "Fit". 
  This is a sweeping algorithm that iteratively optimizes the resulting MPS 
  @@|y\rangle@@ (analogous to DMRG). This algorithm has better scaling in the MPO bond 
  dimension @@k@@ compared to the "DensityMatrix" method, but is not guaranteed to converge 
  (depending on the input MPO and MPS). The number of sweeps can be chosen with the parameter "Nsweep".

  It is recommended to try the default "DensityMatrix" first because it is more reliable. 
  Then, the "Fit" method can be tried if higher performance is required.

  Named arguments recognized:

  * `"Method"` &mdash; (default: "DensityMatrix") algorithm used for applying the MPO to the MPS. Currently available options are 
    - "DensityMatrix" 
    - "Fit"

  * `"Cutoff"` &mdash; (default: 1E-13) truncation error cutoff for compressing resulting MPS

  * `"MaxDim"` &mdash; maximum bond dimension of resulting compressed MPS

  * `"Verbose"` &mdash; (default: false) if true, prints extra output
  
  * `"Normalize"` &mdash; (default: false) choose whether or not to normalize the output wavefunction

  * `"Nsweep"` &mdash; (default: 1) sets the number of sweeps of the "Fit" algorithm

  <div class="example_clicker">Show Example</div>

      //Use the method "DensityMatrix"
      auto y1 = applyMPO(A,x,{"Method=","DensityMatrix","MaxDim=",100,"Cutoff=",1E-8});

      //Use the method "Fit" with 5 sweeps
      auto y2 = applyMPO(A,x,{"Method=","Fit","MaxDim=",100,"Cutoff=",1E-8,"Nsweep=",5});

* `applyMPO(MPO A, MPS x, MPS x0, Args args = Args::global()) -> MPS` <br/>

  Similar to `applyMPO` above, but accepts a guess for the output wavefunction (the guess wavefunction `x0` 
  is not overwritten).

  MPO `A` and MPS `x` must share a set of site indices. The site indices of `x0` will be made to match
  the site indices of `A` that are not shared by `x`.
  The links of the output MPS will have the same tags as the links of the guess MPS `x0`.

  Currently, this version of `applyMPO` only accepts "Fit" for the parameter "Method". Choosing a good guess 
  state `x0` can improve the convergence of the "Fit" method.

  <div class="example_clicker">Show Example</div>

      auto sites = SiteSet(10,2);

      // Make trivial MPO and random MPS
      auto A = MPO(sites);
      auto x = randomMPS(sites);

      // Some other random starting state
      auto x0 = randomMPS(sites);

      //Use the method "Fit" with 5 sweeps and a guess state x0
      auto y = applyMPO(A,x,x0,{"Method=","Fit","MaxDim=",100,"Cutoff=",1E-8,"Nsweep=",2});

* `errorMPOProd(MPS y, MPO A, MPS x) -> Real`

  Computes, without approximation, the difference @@||\, |y\rangle - A |x\rangle ||^2@@,
  where `A` is an MPO that shares a set of site indices with MPS `x`.
  This is especially useful for testing methods for applying an MPO to an MPS.

  `A` and `x` need to share a set of site indices. The function will attempt to match
  the remaining site indices of `A` with the site indices of `y`.

  <div class="example_clicker">Show Example</div>

      auto sites = SiteSet(10,2);

      // Make trivial MPO and random MPS
      auto A = MPO(sites);
      auto x = randomMPS(sites);

      //Approximate A|x>
      auto y = applyMPO(A,x,{"MaxDim=",200,"Cutoff=",1E-12});

      //Check 
      Print(errorMPOProd(y,A,x)); //should be close to zero

<!--

To do:

* exactApplyMPO
* fitApplyMPO
* zipUpApplyMPO

-->

<br/>
_This page current as of version 2.0.7_
