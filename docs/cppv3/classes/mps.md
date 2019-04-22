# MPS

The MPS class is a matrix product state of ITensors. 

The main benefit of using the MPS class is that it can provide strong guarantees about the 
orthogonality properties of the matrix product state it represents. Calling `A.position(n)`
on an MPS `A` makes site n the orthogonality center (OC). Calling `A.position(m)` moves
the OC in an intelligent way using the fewest steps possible. If an arbitrary tensor of
the MPS is modified, and `A.position(n)` is again called, the MPS class knows how
to restore the OC in the fewest number of steps.

ITensor library functions assume an Index structure that each MPS tensor has one site index 
(an index unique to that tensor) as well as one or two link indices, each of which is shared by 
one of the neighboring MPS tensors. They also generally assume open boundary conditions, such
that the end MPS tensors have only one link and one site index.
However, these constraints are not enforced when constructing an MPS or modifying the tensors
of an MPS.

Some ITensor library functions accepting MPS objects assume the convention that indices 
connecting neighboring tensors have the tag "Link" and physical indices carry the "Site" tag,
for example the `dmrg` function (but these requirements may be lifted in the future).

MPS objects can be constructed from either a [[SiteSet|classes/siteset]] or 
an [[InitState|classes/initstate]].

## Synopsis ##

    int N = 100;
    auto sites = SpinHalf(N);

    auto A = MPS(sites); //create random product MPS

    // Shift MPS gauge such that site 1 is
    // the orthogonality center
    A.position(1);
    //Shift orthogonality center to site k
    auto k = 10;
    A.position(k);

    // Read-only access of tensor at site j
    auto j = 15;
    auto Aj = A(j);

    // Replace tensor at site j with
    // a modified tensor.
    A.set(j,2*Aj);

    // Directly modify tensor at site j; "ref"
    // signified that a reference to A_j tensor is returned
    A.ref(j) *= -1;

    // Initialize an MPS to a specific product state
    auto state = InitState(sites);
    for(int i = 1; i <= N; ++i)
        {
        if(i%2 == 0) state.set(i,"Up");
        else         state.set(i,"Dn");
        }
    auto B = MPS(state);

## Constructors ##

* `MPS()`

  Default constructor. A default constructed state `A` evaluates to false in a boolean context.

  <div class="example_clicker">Show Example</div>

      auto A = MPS();
      if(!A) println("A is default constructed");

* `MPS(SiteSet sites)`

  Construct an `MPS` with physical sites given by a [[SiteSet|classes/siteset]]. The `MPS` will be initialized to a random product state with real entries.

* `MPS(InitState state)` <br/>

  Construct an `MPS` and set its site tensors to be in the product state 
  specified by an [[InitState|classes/initstate]] object.

## Retrieving Basic Information about MPS

* `length(MPS A) -> int`

  Returns the number of sites (number of tensors) of the MPS.

* `operator()(int i) -> ITensor const&`

  Returns a const reference (read-only access) to the MPS tensor at site `i`.

* `rightLim(MPS A) -> int`

  Return the right orthogonality limit. If `rightLim()==j`, all tensors
  at sites `i >= j` are guaranteed to be right orthogonal.

* `leftLim(MPS A) -> int`

  Return the left orthogonality limit. If `leftLim()==j`, all tensors
  at sites `i <= j` are guaranteed to be left orthogonal.

* `isOrtho(MPS A) -> bool`

  Return `true` if the MPS has a well-defined orthogonality center that is a single site. 
  This is equivalent to
  the condition that `leftLim()+1 == rightLim()-1`, 
  in which case the center site is `leftLim()+1`.

* `orthoCenter(MPS A) -> int`

  Return the location of the center site (unique site which is the orthogonality center of the MPS).
  Throws an `ITError` exception if the orthogonality center is not well defined i.e. if `isOrtho()==false`.

## Index Methods

* `siteInds(MPS A) -> IndexSet`

  Return an ordered IndexSet of all of the site indices of the MPS.

* `siteIndex(MPS A, int j) -> Index`

  Return the site index of MPS `A` (the index not shared by the neighboring MPS tensors).

  For now, this function assumes open boundary conditions (the first and last MPS tensors only
  have one neighboring tensor each, the ones after and before them respectively).

* `hasSiteInds(MPS A, IndexSet is) -> bool`

  Returns true if, for all sites `j`, `siteIndex(A,j)==is(j)`.

* `linkInds(MPS A) -> IndexSet`

  Return an IndexSet containing the link indices of the MPS `A`. For an MPS with `N` sites, this returns
  `N-1` indices (for now, this function assumes open boundary conditions).

* `leftLinkIndex(MPS A, int j) -> Index`

  Return the left link index of the `j`th tensor of MPS `A` (the index on MPS tensor `A(j)` shared
  with MPS tensor `A(j-1)`).

* `rightLinkIndex(MPS A, int j) -> Index`

  `linkIndex(MPS A, int j) -> Index`

  Return the right link index of the `j`th tensor of MPS `A` (the index on MPS tensor `A(j)` shared
  with MPS tensor `A(j+1)`).

* `linkInds(MPS A, int j) -> IndexSet`

  Return an IndexSet containing the left and right link indices of the MPS tensor `A(j)`.

* `.replaceSiteInds(IndexSet is)`

  `replaceSiteInds(MPS A, IndexSet is) -> MPS`

  Replace all of the site indices of the MPS `A` with those specified in the IndexSet `is`.

* `.replaceLinkInds(IndexSet is)`

  `replaceLinkInds(MPS A, IndexSet is) -> MPS`

  Replace all of the link indices of the MPS `A` with those specified in the IndexSet `is` (`is`
  must have `N-1` indices for MPS `A` with `N` tensors).


## Modifying MPS Tensors

* `.set(int i, ITensor T)`

  Set the MPS tensor on site i to be the tensor T.

  If site `i` is not the orthogonality center, calling `set(i,T)` will set `leftLim()`
  to `i-1` or `rightLim()` to `i+1` depending on whether `i` comes before or after 
  the center site&mdash;this can lead to additional overhead later when calling `position(j)`
  to gauge the MPS to a different site.

* `.ref(int i) -> ITensor&`

  Returns a non-const reference (read-write access) to the MPS tensor at site `i`.

  If read-only access is sufficient, use the `A(i)` method instead of this one
  because `A.ref(i)` may be less efficient.

  If site `i` is not the orthogonality center, calling `ref(i)` will set `leftLim()`
  to `i-1` or `rightLim()` to `i+1` depending on whether `i` comes before or after 
  the center site&mdash;this can lead to additional overhead later when calling `position(j)`
  to gauge the MPS to a different site.


## Modifying and Re-gauging MPS

* `.position(int j, Args args = Args::global())`

  Sets the orthogonality center to site `j` by performing singular value decompositions of tensors
  between `leftLim()` and `rightLim()`. After calling `position(j)`, tensors at sites `i < j` are
  guaranteed left-orthogonal and tensors at sites `i > j` are guaranteed right-orthogonal. Left
  and right orthogonal site tensors can be omitted from operator expectation values for sites not 
  in the support of the operator.

  Note: calling `position(j)` may in general change the "virtual" or `"Link"` indices between 
  some or all of the MPS tensors, but the new indices will have the same tags as the
  original indices.

  By default, the .position method only changes the position of the orthogonality center,
  and does not truncate the MPS. However, it will truncate if the "Cutoff" or "MaxDim"
  named arguments are provided.

  Optional named arguments recognized:

  * "Cutoff" &mdash; truncation error cutoff to use to truncate MPS

  * "MaxDim" &mdash; maximum bond dimension to use when truncating MPS


<a name="orthogonalize"></a>
* `.orthogonalize(Args args = Args::global())`

  Fully re-gauge and compress the MPS, regardless of what its gauge properties might be. 
  
  Afterward the position (orthogonality center) will be at site 1.

  Named arguments recognized:

  * "Cutoff" &mdash; truncation error cutoff to use

  * "MaxDim" &mdash; maximum bond dimension of MPS to allow

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

## MPS Tag Methods

MPS have the same tagging methods that are defined for
ITensors and IndexSets. See the __Tag Methods__ section of the
[[IndexSet documentation|classes/indexset]] for a complete list of methods.

When applied to an MPS, the method is applied to every MPS tensor.

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
  pass truncation accuracy parameters such as "Cutoff" and "MaxDim" through
  the named arguments `args`. Internally these parameters will be passed
  to the svd algorithm; for more information on the available parameters
  and their meaning see the [[svd documentation|classes/decomp]].

  <div class="example_clicker">Show Example</div>

      auto sites = SpinHalf(N);
      auto state = InitState(sites);
      
      // Make an all-up MPS
      for(auto j : range1(N)) state.set(j,"Up");
      auto A1 = MPS(state);

      // Make a "Neel state" MPS
      for(auto j : range1(N)) state.set(j,j%2==1 ? "Up" : "Dn");
      auto A2 = MPS(state);

      A1.plusEq(A2,{"MaxDim",500,"Cutoff",1E-9});


## Functions for Analyzing MPS

* `norm(MPS A) -> Real`
  
  Compute the norm of A (square root of overlap of A with itself).

  If MPS has a well-defined orthogonality center (`isOrtho(A)==true`),
  the norm is computed very efficiently using only a single tensor.

  If the MPS does not have a well-defined orthogonality center, the
  norm is computed using the full overlap of `A` with itself.

  Caution: if the MPS does not have a well-defined orthogonality center then the cost of 
  `norm` is linear in the system size. If the MPS does have a well-defined ortho center
  the cost of `norm` is only proportional to the bond dimension m.

* `isOrtho(MPS A) -> bool`
  
  Return `true` if the MPS has a well defined orthogonality center.

* `orthoCenter(MPS A) -> int`
  
  Return the position of the site tensor which is the orthogonality center of the MPS A.
  If the MPS does not have a well-defined orthogonality center, throws at ITError exception.

* `isComplex(MPS A) -> bool`
  
  Return `true` if any tensor of the MPS is complex (has complex number storage).

* `averageLinkDim(MPS A) -> Real`

  Return the average dimension of the link or virtual degrees of freedom of the MPS A.

* `maxLinkDim(MPS A) -> int`

  Return the maximum dimension of the link or virtual degrees of freedom of the MPS A.
  This means the actual maximum of all of the current link indices, not any theoretical maximum.
  


## Functions for Modifying MPS

* `.normalize() -> Real`
  
  Multiply the MPS by a factor such that it is normalized.
  Afterward calling `norm(A)` or `inner(A,A)`
  for the MPS `A` will give the value 1.0.

  For convenience, returns the previous norm of the MPS as computed by `norm(A)`.

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
_This page current as of version 3.0.0_
