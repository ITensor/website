# Algorithms for MPS and MPO (also IQMPS and IQMPO)


## Summing MPS

* `sum(MPS psi1, MPS psi2, Args args = Args::global()) -> MPS` <br/>
  `sum(IQMPS psi1, IQMPS psi2, Args args = Args::global()) -> IQMPS`

  Return the sum of the MPS psi1 and ps2. The returned MPS will have 
  an orthogonality center on site 1. Before being returned, the MPS 
  representing the sum will be compressed using truncation parameters
  provided in the named arguments `args`.

  <div class="example_clicker">Show Example</div>

      auto psi3 = sum(psi1,psi2,{"Maxm",500,"Cutoff",1E-8});
  
* `sum(vector<MPS> terms, Args args = Args::global()) -> MPS` <br/>
  `sum(vector<IQMPS> terms, Args args = Args::global()) -> IQMPS`

  Returns the sum of all the MPS provided in the vector `terms` as a single MPS,
  using the truncation accuracy parameters (such as "Cutoff" or "Maxm")
  provided in the named arguments `args` to control the accuracy of the sum.

  This function uses a hierarchical, tree-like algorithm which first sums pairs of MPS, 
  then pairs of pairs, etc. so that the largest bond dimensions are only
  reached toward the end of the process for maximum efficiency. Therefore using
  this algorithm can be much faster than calling the above two-argument 
  `sum` function to sum the terms one at a time.

  <div class="example_clicker">Show Example</div>

      auto terms = vector<MPS>(4);
      terms.at(0) = psi0;
      terms.at(1) = psi1;
      terms.at(2) = psi2;
      terms.at(3) = psi3;

      auto res = sum(terms,{"Cutoff",1E-8});


## Overlaps, Matrix Elements, and Expectation Values

* `overlap(MPS psi1, MPS psi2) -> Real` <br/>
  `overlap(IQMPS psi1, IQMPS psi2) -> Real` <br/>
  <br/>
  `overlapC(MPS psi1, MPS psi2) -> Cplx` <br/>
  `overlapC(IQMPS psi1, IQMPS psi2) -> Cplx` <br/>

  Compute the exact overlap @@\langle \psi\_1|\psi\_2 \rangle@@ of two
  MPS or IQMPS. If the overlap value is expected to be a complex number
  use `overlapC`. 

  The algorithm used scales as @@m^3 d@@ where @@m@@ is typical bond
  dimension of the MPS and @@d@@ is the site dimension.

  (In ITensor version 1.x this function was called `psiphi`. This name is still supported
  for backwards compatibility.)

* `overlap(MPS psi1, MPO W, MPS psi2) -> Real` <br/>
  `overlap(IQMPS psi1, IQMPO W, IQMPS psi2) -> Real` <br/>
  <br/>
  `overlapC(MPS psi1, MPO W, MPS psi2) -> Cplx` <br/>
  `overlapC(IQMPS psi1, IQMPO W, IQMPS psi2) -> Cplx` <br/>

  Compute the exact overlap (or matrix element) @@\langle \psi\_1|W|\psi\_2 \rangle@@
  of two MPS psi1 and psi2 with respect to an MPO W.

  The algorithm used scales as @@m^3\, k\,d + m^2\, k^2\, d^2@@ where @@m@@ is typical bond
  dimension of the MPS, @@k@@ is the typical MPO dimension, and @@d@@ is the site dimension.

  (In ITensor version 1.x this function was called `psiHphi`. This name is still supported
  for backwards compatibility.)

* `overlap(MPS psi1, MPO W1, MPO W2, MPS psi2) -> Real` <br/>
  `overlap(IQMPS psi1, IQMPO W1, IQMPO W2, IQMPS psi2) -> Real` <br/>
  <br/>
  `overlapC(MPS psi1, MPO W1, MPO W2, MPS psi2) -> Cplx` <br/>
  `overlapC(IQMPS psi1, IQMPO W1, IQMPO W2, IQMPS psi2) -> Cplx`

  Compute the exact overlap (or matrix element) @@\langle \psi\_1|W\_1 W\_2 |\psi\_2 \rangle@@
  of two MPS psi1 and psi2 with respect to two MPOs W1 and W2.

  The algorithm used scales as @@m^3\, k^2\,d + m^2\, k^3\, d^2@@ where @@m@@ is typical bond
  dimension of the MPS, @@k@@ is the typical MPO dimension, and @@d@@ is the site dimension.

  (In ITensor version 1.x this function was called `psiHKphi`. This name is still supported
  for backwards compatibility.)

## Multiplying MPOs

* `nmultMPO(MPO A, MPO B, MPO & C, Args args = Args::global())` <br/>
  `nmultMPO(IQMPO A, IQMPO B, IQMPO & C, Args args = Args::global())`

  Multiply MPOs A and B. On return, the result is stored in C. 
  MPO tensors are multiplied one at 
  a time from left to right and the resulting tensors are compressed using
  the truncation parameters (such as "Cutoff" and "Maxm") provided through
  the named arguments `args`.

  <div class="example_clicker">Show Example</div>

      MPO C;
      nmultMPO(A,B,C,{"Maxm",500,"Cutoff",1E-8});


## Applying MPO to MPS

* `applyMPO(MPO K, MPS psi, Args args = Args::global()) -> MPS` <br/>
  `applyMPO(IQMPO K, IQMPS psi, Args args = Args::global()) -> IQMPS`

  Apply an MPO K to an MPS psi, resulting in an approximation to the MPS phi:  @@|\phi\rangle = K |\psi\rangle@@. <br/>
  The resulting MPS is returned. The algorithm used is chosen with the parameter "Method" in the named arguments `args`.

  The default algorithm used is the <a href="https://tensornetwork.org/mps/algorithms/denmat_mpo_mps">"density matrix" algorithm</a>,
  chosen by setting the parameter "Method" to "DensityMatrix".
  If the input MPS has a typical bond dimension of @@m@@ and the MPO has typical bond dimension @@k@@,
  this algorithm scales as @@m^3 k^2 + m^2 k^3@@.

  No approximation is made when applying the MPO, but after applying it the resulting
  MPS is compressed using the truncation parameters provided in the named arguments `args`.

  An alternative algorithm can be chosen by setting the parameter "Method" to "Fit". This is a sweeping algorithm that iteratively
  optimizes the resulting MPS @@|\phi\rangle@@ (analogous to DMRG). This algorithm has better scaling in the MPO bond dimension @@k@@ 
  compared to the "DensityMatrix" method, but is not guaranteed to converge (depending on the input MPO and MPS). 
  The number of sweeps can be chosen with the parameter "Sweeps" and whether or not the resulting MPS is normalized can be set with the 
  parameter "Normalize".

  It is recommended to try the default "DensityMatrix" first because it is more reliable. Then, the "Fit" method can be tried if 
  higher performance is required.

  Named arguments recognized:

  * `"Method"` &mdash; (default: "DensityMatrix") algorithm used for applying the MPO to the MPS. Currently available options are "DensityMatrix"
                        and "Fit"

  * `"Cutoff"` &mdash; (default: 1E-13) truncation error cutoff for compressing resulting MPS

  * `"Maxm"` &mdash; maximum bond dimension of resulting compressed MPS

  * `"Verbose"` &mdash; (default: false) if true, prints extra output
  
  * `"Sweeps"` &mdash; (default: 1) sets the number of sweeps of the "Fit" algorithm

  * `"Normalize"` &mdash; (default: true) choose whether to normalize the output wavefunction, only used by the method "Fit"

  <div class="example_clicker">Show Example</div>

      //Use the method "DensityMatrix"
      auto phi = applyMPO(K,psi,{"Method=","DensityMatrix","Maxm=",100,"Cutoff=",1E-8});

      //Use the method "Fit" with 5 sweeps
      auto phi2 = applyMPO(K,psi,{"Method=","Fit","Maxm=",100,"Cutoff=",1E-8,"Sweeps=",5,"Normalize=",false});


* `checkMPOProd(MPS psi2, MPO K, MPS psi1) -> Real` <br/>
  `checkMPOProd(IQMPS psi2, IQMPO K, IQMPS psi1) -> Real`

  Computes, without approximation, the difference @@||\, |\psi\_2\rangle - K |\psi\_1\rangle ||^2@@,
  where K is an arbitrary MPO.
  This is especially useful for testing methods for applying an MPO to an MPS.

  <div class="example_clicker">Show Example</div>

      //Approximate K*psi
      auto phi = applyMPO(K,psi,{"Maxm=",200,"Cutoff=",1E-12});

      //Check 
      Print(checkMPOProd(phi,K,psi)); //should be close to zero

<!--

To do:

* overlap functions taking boundary tensors
* psiHKphi where you pass re and im by reference

* exactApplyMPO
* fitApplyMPO
* zipUpApplyMPO

-->

<br/>
_This page current as of version 2.0.7_
