# MPS and IQMPS #

MPS is matrix product state of ITensors. IQMPS nearly identical but uses IQTensors.
In the documentation below, MPS refers to both MPS and IQMPS unless explicitly
specified. The type ITensor should be replaced with IQTensor for the case of an IQMPS.

The main benefit of using the MPS class is that it can provide strong guarantees about the 
orthogonality properties of the matrix product state it represents. Calling `psi.position(n)`
on an MPS `psi` makes site n the orthogonality center (OC). Calling `psi.position(m)` moves
the OC in an intelligent way using the fewest steps possible. If an arbitrary tensor of
the MPS is modified, and `psi.position(n)` is again called, the MPS class knows how
to restore the OC in the fewest number of steps.

MPS tensors follow the convention that indices connecting neighboring tensors have the IndexType
`Link`. Physical indices have the IndexType `Site`.

MPS objects can be constructed from either a [[SiteSet|classes/siteset]] or an [[InitState|classes/initstate]].

## Synopsis ##

    int N = 100;
    auto sites = SpinHalf(N);

    auto psi = MPS(sites); //create random product MPS

    // Shift MPS gauge such that site 1 is
    // the orthogonality center
    psi.position(1);
    //Shift orthogonality center to site k
    psi.position(k);

    // Read-only access of tensor at site j
    auto A = psi.A(j);

    // Replace tensor at site j with
    // a modified tensor
    psi.setA(j,2*A);

    // Directly modify tensor at site j
    //"nc" stands for "non-const"
    psi.Anc(j) *= -1;

    // Initialize an IQMPS to a specific product state
    auto state = InitState(sites);
    for(int i = 1; i <= N; ++i)
        {
        if(i%2 == 0) state.set(i,"Up");
        else         state.set(i,"Dn");
        }
    auto qpsi = IQMPS(state);


## Constructors ##

* `MPS()` <br/>
  `IQMPS()`

  Default constructor. A default constructed state `psi` evaluates to false in a boolean context.

  <div class="example_clicker">Show Example</div>

      MPS psi;
      if(!psi) println("psi is default constructed");

* `MPS(SiteSet sites)`

  Construct an `MPS` with physical sites given by a [[SiteSet|classes/siteset]]. The `MPS` will be initialized to a random product state.

* `IQMPS(SiteSet sites)`

  Construct an `IQMPS` with physical sites given by a [[SiteSet|classes/siteset]]. 
  The `IQMPS` site tensors will _not_ be initialized (to construct an initialized IQMPS see next function).

* `MPS(InitState state)` <br/>
  `IQMPS(InitState state)`

  Construct an `MPS` or `IQMPS` and set its site tensors to be in the product state 
  specified by an [[InitState|classes/initstate]] object.

## Retrieving Basic Information about MPS

* `.N() -> int`

  Returns the number of sites (number of tensors) of the MPS.

* `.A(int i) -> ITensor const&`

  Returns a const reference (read-only access) to the MPS tensor at site `i`.

* `.rightLim() -> int`

  Return the right orthogonality limit. If `rightLim()==j`, all tensors
  at sites `i >= j` are guaranteed to be right orthogonal.

* `.leftLim() -> int`

  Return the left orthogonality limit. If `leftLim()==j`, all tensors
  at sites `i <= j` are guaranteed to be left orthogonal.

* `.isOrtho() -> bool`

  Return `true` if the MPS has a well-defined orthogonality center that is a single site. 
  This is equivalent to
  the condition that `leftLim()+1 == rightLim()-1`, 
  in which case the center site is `leftLim()+1`.

* `.orthoCenter() -> int`

  Return the location of the center site (unique site which is the orthogonality center of the MPS).
  Throws an `ITError` exception if the orthogonality center is not well defined i.e. if `isOrtho()==false`.

* `.sites() -> SiteSet const&`

  Return a read-only reference to the `SiteSet` associated with the lattice sites of this MPS.

## Modifying MPS Tensors

* `.setA(int i, ITensor T)`

  Set the MPS tensor on site i to be the tensor T.

  If site `i` is not the orthogonality center, calling `setA(i,T)` will set `leftLim()`
  to `i-1` or `rightLim()` to `i+1` depending on whether `i` comes before or after 
  the center site&mdash;this can lead to additional overhead later when calling `position(j)`
  to gauge the MPS to a different site.

* `.Anc(int i) -> ITensor&`

  Returns a non-const reference (read-write access) to the MPS tensor at site `i`.

  If read-only access is sufficient, use the `A(i)` method instead of this one
  because `Anc` may be less efficient.

  If site `i` is not the orthogonality center, calling `Anc(i)` will set `leftLim()`
  to `i-1` or `rightLim()` to `i+1` depending on whether `i` comes before or after 
  the center site&mdash;this can lead to additional overhead later when calling `position(j)`
  to gauge the MPS to a different site.


## Modifying and Re-gauging MPS

* `.position(int j)`

  Sets the orthogonality center to site `j` by performing singular value decompositions of tensors
  between `leftLim()` and `rightLim()`. After calling `position(j)`, tensors at sites `i < j` are
  guaranteed left-orthogonal and tensors at sites `i > j` are guaranteed right-orthogonal. Left
  and right orthogonal site tensors can be omitted from operator expectation values for sites not 
  in the support of the operator.

  Note: calling `position(j)` may in general change the "virtual" or `Link` indices between 
  some or all of the MPS tensors.

* `.orthogonalize(Args args = Args::global())`

  Fully re-gauge and compress the MPS by performing two passes: one to make all of the 
  tensors orthogonal with minimal truncation, and another to truncate the MPS to the requested accuracy.

  Named arguments recognized:

  * "Cutoff" &mdash; truncation error cutoff to use

  * "Maxm" &mdash; maximum bond dimension of MPS to allow

* ```
  .svdBond(int b, ITensor AA, Direction dir, 
           Args args = Args::global()) -> Spectrum
  ```

  Replace the tensors at sites `b` and `b+1` (i.e. on bond `b`) with the tensor `AA`, which will be decomposed
  using a factorization equivalent to an SVD. If the `Direction` argument `dir==Fromleft`, then after the call
  to `svdBond`, site `b+1` will be the orthogonality center of the MPS. Similarly, if `dir==Fromright` then `b`
  will be the orthogonality center.

  Returns a [[Spectrum|classes/spectrum]] object with information about the truncation and density
  matrix eigenvalues.

* ```
  .svdBond(int b, ITensor AA, Direction dir, BigMatrixT PH, 
           Args args = Args::global()) -> Spectrum
  ```

  Equivalent to `svdBond` above but with an additional argument `PH` which
  is used to compute the "noise term" which will be added to the density matrix used to decompose `AA`.
  For more information see the docs on [[denmatDecomp|classes/decomp]].


* `.swap(MPS & phi)`

  Efficiently replace all tensors of this MPS with the corresponding tensors
  of another MPS `phi`, which must have the same number of sites.

## MPS Prime Level Methods

* `.mapprime(int plevold, int plevnew, IndexType type = All)`

  For each tensor of the MPS, any index having prime level `plevold`
  will have its prime level changed to `plevnew`.

  Optionally the mapping will only be applied to indices with IndexType `type`.

* `.primelinks(int plevold, int plevnew)`

  For each tensor of the MPS, any index having type `Link` and prime level `plevold`
  will have its prime level changed to `plevnew`.

* `.noprimelink()`

  Reset the `Link` indices of the MPS back to prime level zero.

## Operations on MPS

* `MPS * Real -> MPS` <br/>
  `Real * MPS -> MPS` <br/>
  `MPS * Cplx -> MPS` <br/>
  `Cplx * MPS -> MPS` <br/>
  `MPS *= Real` <br/> <!--*-->
  `MPS *= Cplx`

  Multiply an MPS by a real or complex scalar. 
  The factor is put into the orthogonality center
  tensor, if well defined. Otherwise it is put into an arbitrary tensor.

* `MPS /= Real` <br/>
  `MPS /= Cplx`

  Divide an MPS by a real or complex scalar. 
  The divisor is put into the orthogonality center
  tensor, if well defined. Otherwise it is put into an arbitrary tensor.

* `.plusEq(MPS R, Args args = Args::global())`

  Add an MPS `R` to this MPS. When using this algorithm it is recommended to
  pass truncation accuracy parameters such as "Cutoff" and "Maxm" through
  the named arguments `args`. Internally these parameters will be passed
  to the svd algorithm; for more information on the available parameters
  and their meaning see the [[svd documentation|classes/decomp]].

  <div class="example_clicker">Show Example</div>

      auto sites = SpinHalf(N);
      auto state = InitState(sites);
      
      // Make an all-up MPS
      for(auto j : range1(N)) state.set(j,"Up");
      auto psi1 = MPS(state);

      // Make a "Neel state" MPS
      for(auto j : range1(N)) state.set(j,j%2==1 ? "Up" : "Dn");
      auto psi2 = MPS(state);

      psi1.plusEq(psi2,{"Maxm",500,"Cutoff",1E-9});


## Functions for Analyzing MPS

* `norm(MPS psi) -> Real`
  
  Compute the norm of psi (square root of overlap of psi with itself).

  If MPS has a well-defined orthogonality center (`psi.isOrtho()==true`),
  the norm is computed very efficiently using only a single tensor.

  If the MPS does not have a well-defined orthogonality center, the
  norm is computed using the full overlap of `psi` with itself.

  Caution: if the MPS does not have a well-defined orthogonality center then the cost of 
  `norm` is linear in the system size. If the MPS does have a well-defined ortho center
  the cost of `norm` is only proportional to the bond dimension m.

* `linkInd(MPS psi, int b) -> Index`

  Return the Index connecting the MPS tensor at site b to the tensor at site b+1.

* `rightLinkInd(MPS psi, int s) -> Index`

  Return the Index connecting the MPS tensor at site s to the tensor at site s+1.

* `leftLinkInd(MPS psi, int s) -> Index`

  Return the Index connecting the MPS tensor at site s-1 to the tensor at site s.

* `isOrtho(MPS psi) -> bool`
  
  Return `true` if the MPS has a well defined orthogonality center.

* `orthoCenter(MPS psi) -> int`
  
  Return the position of the site tensor which is the orthogonality center of the MPS psi.
  If the MPS does not have a well-defined orthogonality center, throws at ITError exception.

* `isComplex(MPS psi) -> bool`
  
  Return `true` if any tensor of the MPS is complex (has complex number storage).

* `averageM(MPS psi) -> Real`

  Return the average bond dimension of the MPS psi.

* `maxM(MPS psi) -> int`

  Return the maximum bond dimension of the MPS psi. This means the actual maximum of 
  all of the current bond (Link) indices, not any theoretical maximum.
  


## Functions for Modifying MPS

* `normalize(MPS & psi) -> Real`
  
  Multiply the MPS by a factor such that it is normalized. Afterward calling `psi.norm()` or `overlap(psi,psi)`
  for the MPS `psi` will give the value 1.0.

  For convenience, returns the previous norm of the MPS as computed by `norm(psi)`.

  Caution: if the MPS does not have a well-defined orthogonality center then the cost of 
  normalize is linear in the system size. If the MPS does have a well-defined ortho center
  the cost of normalize is only proportional to the bond dimension m.


## Developer / Advanced Methods

* `.leftLim(int j)` <br/>
  `.rightLim(int j)`

  Forcibly set the left or right orthogonality limits (see documentation 
  for `leftLim()` and `rightLim()` above).

  Only use these methods after modifying MPS tensors using `.setA` or `.Anc` 
  when you know that the replaced tensors obey left or right orthogonality
  constraints.

  Setting these incorrectly could lead to an improperly gauged MPS even
  after calling the `.position` method.

<!--

Still need to add:

* Args for 
  - position
  - orthogonalize
  - svdBond
* doWrite
* writeDir
* applyGate
* checkQNs
* totalQN

-->

<br/>
_This page current as of version 2.0.7_
