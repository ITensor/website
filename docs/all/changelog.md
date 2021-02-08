# Change Log (C++)

<a name="v3.1.7"></a>
## [Version 3.1.7](https://github.com/ITensor/ITensor/tree/v3.1.7) (Feb 8, 2021)

- Throw error if requested QN not satisfied in randomITensor (PR #384 @emstoudenmire)
- Fix subscript out of range in autovector.h (PR #379 @shencebebetterme)
- Make gesdd the default SVD algorithm (PR #376 @mtfishman)
- Restore mixed fermionic and non-fermionic AutoMPO support (PR #374 @emstoudenmire)

<a name="v3.1.6"></a>
## [Version 3.1.6](https://github.com/ITensor/ITensor/tree/v3.1.6) (Nov 6, 2020)

- Fix issue #311 regarding wrong fermion sign when no QNs conserved (PR #373)
- Add sample code for 2D Hubbard model with ky conservation
- Add citation info to README


<a name="v3.1.5"></a>
## [Version 3.1.5](https://github.com/ITensor/ITensor/tree/v3.1.5) (Oct 17, 2020)

- Add CTMRG sample code.
- Update lapack wrapper functions to use LAPACK_INT (PR #369)
- Fix potential integer overflow in getContractedOffsets (PR #368)
- Reorganize and simplify TRG sample code

<a name="v3.1.4"></a>
## [Version 3.1.4](https://github.com/ITensor/ITensor/tree/v3.1.4) (Oct 12, 2020)

- Switch headers to use pragma once (PR #356)
- Fix issue with colliding SVD indices (PR 357)
- More comprehensive README for sample codes
- Fix bug where LocalOp constructor errors if optional NumCenter variable left unspecified (PR #359)
- Fix issue with range function in case start > end (PR #362)


<a name="v3.1.3"></a>
## [Version 3.1.3](https://github.com/ITensor/ITensor/tree/v3.1.3) (May 11, 2020) ##

Bug fixes and improvements:
- Remove util/print_macro.h from all.h (PR #352)
- Fix faulty QN MPS error check (PR #349)
- Improve LocalOp operator bool (PRs #351, #354 )
- Fix totalQN function to always succeed if lims set (PR #355)

<a name="v3.1.2"></a>
## [Version 3.1.2](https://github.com/ITensor/ITensor/tree/v3.1.2) (Apr 28, 2020) ##

New features:
- randomMPS now allows bond dimension > 1 (without QNs) (PR #339)
- LAPACK SVD routines now supported (thanks Jack Kemp) (PR #333)
- OpenMP multi-core paralellism for QN ITensor contractions (PR #325)
- QR factorization for ITensors (thanks Jack Kemp) (PR #285)

Bug fixes and improvements:
- fix bug in QN version of excited-state DMRG (PR #341)
- improvements to nmultMPO (PR #347)
- generalize setElt to allow a value other than 1 (PR #344)
- update finite T tutorial codes for v3 and improvements to them (PR #343)
- ITensor default SVD now uses QR to get V (PR #334)
- QN combiner can now be printed
- optimizations related to not initializing data with zeros (PR #323 and others)
- printing Index objects puts "dim=" in front of the dimension

<a name="v3.1.1"></a>
## [Version 3.1.1](https://github.com/ITensor/ITensor/tree/v3.1.1) (Dec 13, 2019) ##

- Fixes a bug in the removeQNs(ITensor) function
- svd no longer truncates by default
- better handling of singular values which are exactly zero when setting Cutoff=0

<a name="v3.1.0"></a>
## [Version 3.1.0](https://github.com/ITensor/ITensor/tree/v3.1.0) (Nov 20, 2019) ##

This update to ITensor speeds up calculations involving block sparse ITensors 
by a considerable amount, especially when the number of different blocks is large
(or equivalently the block sizes are small compared to the over index dimensions).

This version also introduces an optimization where ITensor data is not initialized
to all zero when it is about to be immediately overwritten, say as the result of
a contraction operation.

New features added since v3.0.0:
- itertools for range-based iteration (e.g. enumerate)
- arnoldi function for finding dominant eigenvector of a large matrix
- applyExp function (Krylov method for applying the exponential of a matrix/operator)
- polar decomposition
- directSum: partial direct sum of ITensors


<a name="v3.0.0"></a>
## [Version 3.0.0](https://github.com/ITensor/ITensor/tree/v3.0.0) (May 15, 2019) ##

This major update to ITensor features a number of changes to the design.


Index objects now carry up to four "tag" strings instead of a name or
IndexType as in version 2. These tags are useful for many tasks, including
selecting a particular Index from a set, or preventing two Index objects
with the same ID from being contracted.

The IQIndex and IQTensor classes have been removed, and are now just
Index or ITensor objects which carry extra quantum number block information.
Similarly IQMPS and IQMPO have been removed, and one can use just MPS and MPO
instead. This change streamlines much of the design, letting us turn many
template functions into regular functions. Importantly, it fixes a number
of issues and awkward design aspects of site set objects.

QN objects now carry small strings naming each of their sectors, allowing
QNs with different sectors to still be sensibly combined. This allows
one to define different QNs locally and still use them together globally
within the same algorithm or code.

Finally, the move to version 3.0.0 brings a raft of many other small redesigns,
such as deprecating many class methods in favor of free functions; better
and more general names for various functions; more consistent interfaces across similar functions;
improvements to MPO and MPS algorithms to make them work for a broader range of inputs;
and many other similar improvements.

For help upgrading an existing code to version 3, see the [[upgrade guide|upgrade2to3]].

To move to version 3 if you have already cloned ITensor, 
you have to switch to the `v3` branch. To do so, use the commands<br/>
`git pull`<br/>
`git checkout v3`<br/>

### Major Breaking Changes

- C++17 is required to compile ITensor version 3. To upgrade your options.mk file, either
  create a new one from options.mk.sample, or replace `-std=c++11` with `-std=c++17`.

- Index objects now only require a dimension to be constructed. They optionally accept
  up to four "tag" strings. Two Index objects must have the same tags (regardless of ordering)
  to compare equal.

- The IQIndex, IQTensor, IQMPS, and IMPO types have been removed, in favor of adding
  the same functionality as special storage types of Index, ITensor, MPS, and MPO.

- QN objects now store string labels, or names, for each of their sectors. A missing
  or undefined sector is treated as having a value of zero for the purpose of combining
  two QNs with different sector definitions.

- Getting a tensor element as a real number immediately throws an error if the tensor
  has complex storage, even if that element has zero imaginary part.

### General changes

- Changed license to Apache 2.0 per Flatiron Institute policy

- In general, the user interface is more consistant that member functions called with `A.f(...)`
modify `A` in-place and free functions do not perform modifications of the inputs

- `str(int) -> string` helper function added to make it easier to make tags, i.e. `"n="+str(n)` to make the tag `"n=2"` if `int n = 2`

### Changes to Index class

- Changes to Index constructors:
    - `Index(2)` for Index of size 2
    - `Index(2,"Site,n=2")` for Index of size 2 and tags "Site" and "n=2"
    - `Index(QN({"Sz",0}),2,QN({"Sz",1"}),3)` for Index with QNs

- New QN design:
    - No seperate IQIndex class. Instead, Index either has or does not have QN data.
    - Store a smallstring along with QN value and mod fac. Storage is an array (fixed-size) of triples name-val-modfac.
    - `removeQNs(i)` to remove the QNs from Index `i`

- In general, `dim` is now preferred to `m` to refer to the dimension of the Index

- New tagging and priming functions:
    - `setTags`, `noTags`, `addTags`, `removeTags`, `replaceTags`, `prime`, `setPrime`, `noPrime`
        - See the C++v3 version of the [[IndexSet docs|classes/indexset]] for more details.
        - NOTE: the `prime` function, when using Indices for matching, now match the exact Index without ignoring the prime level. For example: `auto i = Index(2,"i"); auto is = IndexSet(i,prime(i),prime(i,2)); prime(is,3,i);` only primes Index `i` in the IndexSet. To prime all of the indices, use `prime(is,3,"i")`.
        - V2 method `i.noprime()` is replaced by `i.noPrime()`
        - V2 method `i.mapprime(0,1)` is replaced by `i.replaceTags("0","1")`
        - V2 method `i.noprimeEquals(j)` is replaced by `noPrime(i)==noPrime(j)`
    - All functions have in-place versions and free versions:
        - `i.addTags("a")` adds the Tag "a" in-place
        - `addTags(i,"a")` creates a copy of `i` with the Tag "a" added
    - The same tagging and priming functions also work on IndexVal, IndexSet, ITensor, MPS and MPO

- `sim(i)` creates a new Index with the same properties as `i` except with a new `id` (in V2, it set the prime level to zero)

- New accessor methods for properties of an Index:
    - `dim(i)` to get dimension of Index `i` (instead of `i.m()` in V2)
    - `tags(i)` to get the TagSet of Index `i` (supercedes the IndexType and Index name of V2)
    - `primeLevel(i)` for prime level of an Index `i` (instead of `i.primeLevel()` in V2)
        - NOTE: the prime level is included in the TagSet as a special "integer tag"
    - `id(i)` to get the id (instead of `i.id()` in V2)
    - `dir(i)` to get the arrow directions (instead of `i.dir()` in V2)
    - `hasTags(i,"a,b")` checks if Index `i` has the tags "a" and "b"
    - `nblock(i)` to get the number of QN blocks of Index `i` (previously `i.nblock()` in V2)
    - `qn(i,b)` to get the QN of block `b` of Index `i` (previously `i.qn(b)`)
    - `blocksize(i,b)` to get the size of block `b` of Index `i` (previously `i.blocksize(b)` in V2)

- New arrow manipulation functions:
    - `i.dag()` and `dag(i)` to reverse the arrow direction, either in-place or by making a copy
    - `i.setDir(In)` to set the direction of an Index `i` to `In`

### Changes to IndexSet class

- Added `order(is)` and `length(is)` as preferred methods for getting the number if Indices in IndexSet `is` (previously `is.r()` in V2)

- Add conversion of the following to IndexSet:
    - `std::initializer_list<Index>`
    - `std::array<Index,N>`
    - `std::vector<Index>`
    - `IndexSet`,`IndexSet`
    - `Index`,`IndexSet`
    - `IndexSet`,`Index`
    - Functions accepting `IndexSet` as an input will accept the above as well. Functions accepting lists of indices (such as special ITensor constructors) are more consistent about accepting IndexSets.

- Add `sim(IndexSet)`, `sim(IndexSet,IndexSet)`, `sim(IndexSet,TagSet)` to create a new IndexSet with indices replaced by similar indices (or optionally, only the specified indices)

- IndexSet set operations:
    - Add `hasSameInds(is1,is2)` for set equality of IndexSet `is1` and `is2`
    - Add `hasInds(is1,is2)` to check if IndexSet `is2` is a subset of IndexSet `is1`
    - Add `unionInds(IndexSet,IndexSet)->IndexSet` and `unionInds({IndexSet,IndexSet,...})` to get set union
    - Add `uniqueInds(IndexSet,IndexSet)` and `uniqueInds(IndexSet,{IndexSet,...})` to get set difference
    - Add `commonInds(IndexSet,IndexSet)` to get set intersection
    - Add `noncommonInds(IndexSet,IndexSet)` to get set symmetric difference
    - These functions respect the ordering of the input Indices

- Finding Indices in an IndexSet:
    - Add `findInds(IndexSet,TagSet)` to get a subset containing tags in the tagset
    - Add `findIndsExcept(IndexSet,TagSet)` to get a subset not containing tags in the tagset
    - `findIndex(IndexSet,TagSet)` finds the Index containing the tags of the specified TagSet. Returns a null Index `Index()` of none are found, and errors if more than one are found (this replaces `findType` in V2, where the first Index found was returned).
    - `findIndex(IndexSet,Arrow)` of V2 removed

- Added `equals(IndexSet,IndexSet)` to check if IndexSets are exactly equal (same indices in the same order)

- IndexSet tagging and priming functions:
  - Removed `mapPrime(1,2,...)`, use `replaceTags("1","2",...)` instead
  - Prime level can be accessed through TagSet, i.e. `findIndex(A,"Site,1")` means Index with tag "Site" and prime level 1

- IndexSet properties:
    - `maxDim(is)` and `minDim(is)` to get the maximum and minimum Index dimensions in the IndexSet (replaces `maxM(is)` and `minM(is)`)

### Changes to ITensor functions

- Accessing values of an ITensor:
    - Make `elt(T,i=1,j=2)` for complex storage throw an error, require using `eltC(T,i=1,j=2)` (use `real(eltC(T,i=1,j=2))` to get the old behavior).
    - Replace `T.real(i=2,j=2) and `T.cplx(i=2,j=2)` to `elt(T,i=2,j=2)` and `eltC(T,i=2,j=2)` (kept .real and .cplx just for backwards compatibility).
    - Added `elt(T,vector<IndexVal>)` and `eltC(T,vector<IndexVal>)`
    - Added `elt(T,vector<int>)` and `eltC(T,vector<int>)`

- Changes to ITensor constructors:
    - Deprecate `randomTensor`, `matrixTensor`, `diagTensor` in favor of `randomITensor`, `matrixITensor`, `diagITensor` (deprecation warnings)
    - All ITensor constructors like `ITensor(...)`, `randomITensor(...)`, `diagITensor(...)`, etc. now accept Index collections convertible to IndexSet (see IndexSet changes).
    - `Combiner(IndexSet) -> tuple<ITensor,Index>` now returns a tuple of the combiner ITensor and the new combined Index.

- `removeQNs(ITensor A) -> ITensor` makes a new ITensor with QNs removed.

- Changes to ITensor decompositions:
    - `diagHermitian` now does no truncation, use `diagPosSemiDef` if the ITensor is approximately positive semi-definite to perform truncations
    - Add versions of ITensor decompositions that return tuples of outputs:
       - `svd(ITensor,IndexSet[,IndexSet]) -> tuple<ITensor,ITensor,ITensor>`
       - `factor(ITensor,IndexSet[,IndexSet]) -> tuple<ITensor,ITensor>`
       - `denmatDecomp(ITensor,IndexSet[,IndexSet]) -> tuple<ITensor,ITensor>`
       - `diagPosSemiDef(ITensor) -> tuple<ITensor,ITensor>`
       - `diagHermitian(ITensor) -> tuple<ITensor,ITensor>`
       - `eigen(ITensor) -> tuple<ITensor,ITensor>`
    - Deprecate "Maxm", "Minm" args in favor of "MaxDim", "MinDim" in svd(), diagPosSemiDef(), factorize(), dmrg(), idmrg(), etc.
    - Add "RespectDegenerate" arg to `svd()` and `diagPosSemiDef()` function to switch on and off whether degenerate subspaces will be truncated. False by default. Defaults to true for MPS functions.

- Replacing Indices in ITensors:
    - Optimize `A*delta(i,j)` contraction so that if `A` has Index `i` or `j` (but not both), no contraction occurs and the Index is just replaced in the IndexSet
    - Deprecate reindex(ITensor,Index,Index,...), replace with replaceInds(ITensor,IndexSet,IndexSet) that does not ignore prime levels and internally calls delta() (deprecation error)
    - Add `swapInds(A,{i,j,k},{a,b,c})` to swap the Indices i<->a, j<->b, etc. a certain tag constraint

- More Index operations:
    - `findIndex(ITensor,TagSet)` to get the index that has tags in a TagSet (throws error if there are more than one)
    - `findInds(ITensor,TagSet)` to get all indices that have the tags in a TagSet
    - `hasInds(ITensor,IndexSet)` to see if the ITensor has the specified Indices
    - Added `uniqueInds(A,{B,C})` and `uniqueIndex(A,{B,C}[,ts])` notation for getting the unique indices/index under
    - Add `inds(ITensor)` as preferred alternative to `ITensor.inds()`
    - Add `index(ITensor,int)` as preferred alternative to `ITensor.index(int)`
    - `indexPosition(ITensor,Index) -> int` to get the position of the Index in the IndexSet of the ITensor (in V2, was `findIndex(ITensor,Index) -> int`)

- Tagging and priming functions:
    - Same as tagging/priming functions of IndexSet
    - Allow tag and prime functions to accept multiple indices for matching, also allow IndexSet for matching
    - Add deprecation warning for prime(ITensor,Index,int) pointing towards prime(ITensor,int,Index)

- Add `maxDim(ITensor)` and `minDim(ITensor)`

- `permute(A,{i,j,k})` to fix the ordering of the Indices and permute the data of an ITensor (in V2, was called `order(A,i,j,k)`)

- Deprecate `randomize(ITensor& T)` in favor of `T.randomize()`

### Changes to MPS and MPO functions

- Change default behavior of `MPS(sites,m)` constructor to be uninitialized MPS of size m
    - m>1 only allowed with no QNs

- New `randomMPS(SiteSet)` and `randomMPS(InitState)` constructor

- New functions for getting inner products of MPS/MPO:
    - Deprecate overlap(MPS x, MPS y) in favor of `inner(MPS x, MPS y)` (overlap is deprecated with a warning)
        - `inner(MPS x, MPS y)` conjugates x and then matches the indices of `dag(x)` and `y`
    - Deprecate `overlap(MPO A, MPO B)` in favor of `trace(MPO A, MPO B)` (overlap is deprecated with a warning)
        - The MPOs must share one or two sets of indices. Neither of them get conjugated.
    - Added `trace(A)` to get the trace of an MPO
    - Deprecate `overlap(MPS x, MPO A[, MPO B], MPS y)` in favor of `inner(x,A[,B],y)` (overlap is deprecated with a warning)
        - `inner(x,A,y)` = <x|A|y>, where the site indices of A|y> are matched to the site indices of <x|
        - `inner(x,A,B,y)` = <x|AB|y>, where the site indices of AB|y> are matched to the site indices of <x|
    - Also added `inner(MPO A, MPS x, MPO B, MPS y)` which does <Ax|By> (this helps to get the norm of A|x> with sqrt(inner(A,x,A,x))

- New accessor methods for MPS/MPO:
    - `psi.A(i) -> psi(i)`
    - `psi.Aref(i) -> psi.ref(i)`
    - `psi.setA(i,T) -> psi.set(i,T)`
    - `psi.N() -> length(psi)`

- New methods for getting indices of MPS/MPO:
    - Remove SiteSet from MPS class (no more `psi.site()`), use `siteInds(MPS)` to get the indices of an MPS as an IndexSet and `SiteSet(siteInds(MPS))` to get the siteset
    - Add `siteInds(MPS) -> IndexSet` to get an ordered IndexSet of the site indices
    - Add `linkInds(MPS) -> IndexSet` to get an ordered IndexSet of the link indices
    - Add `linkInds(MPS/MPO,int) -> IndexSet` to get the link indices of an MPS/MPO tensor
    - Add `leftLinkIndex(MPS/MPO,int) -> Index` and `rightLinkIndex(MPS/MPO,int)` to get the left/right link index of an MPS/MPO
        - Add `linkIndex(MPS/MPO,int) -> Index` is a shorthand for `rightLinkIndex`
    - `siteIndex(MPS,int)` to get the site index of an MPS
    - `siteIndex(MPO,int[,TagSet])` to get a site index of an MPO
        - Since there are two site indices, one can use a TagSet like "0" or "1" to decide which site index to grab, by default it is "0"

- New methods for replacing indices of MPS/MPO:
    - Add `replaceSiteInds(MPS,IndexSet) -> MPS` to make a new MPS with site indices replaces by those in the IndexSet
    - Add `replaceLinkInds(MPS,IndexSet) -> MPS` to make a new MPS with link indices replaces by those in the IndexSet
    - Add `replaceSiteInds(MPO,IndexSet,IndexSet) -> MPO` to make a new MPO with specified site indices replaces by those in the IndexSet
    - Add `swapSiteInds(MPO) -> MPO` to "transpose" an MPO (swap the site indices, site by site)

- Tagging/priming methods for MPS/MPO:
    - Added `addTags(MPS/MPO,...)`, `replaceTags(MPS/MPO,...)`, `prime(MPS/MPO,...)`, etc. (all the same functions as for IndexSet and ITensor, applied to every tensor in the MPS/MPO)
    - `.position(int)`, `.orthogonalize()`, and `.svdBond()` accept inputs with any tag convention and keep the proper tags of the input MPS/MPO
    - Deprecate `MPO.primeall()` in favor of `MPO.prime()`

- Replace `maxM(MPS)` and `averageM(MPS)` with `maxLinkDim(MPS)` and `averageLinkDim(MPS)`

- Deprecate `normalize(MPS& psi)` in favor of `psi.normalize()`

- Deprecate "Maxm", "Minm" args in favor of "MaxDim", "MinDim" in dmrg(), idmrg(), etc.

- Site and link indices now have a tag convention:
    - Site indices have tags "Site,n=1" and then a tag for the SiteSet
        - For MPOs, sites have tags "Site,n=1,0" and "Site,n=1,1"
    - Link indices have tags "Link,l=1"
    - Site and Link IndexTypes removed in favor of tags

- `toMPO(AutoMPO)` is the preferred way to construct an MPO from an AutoMPO

- Add `hasQNs(MPS/MPO)` to check if an MPS/MPO has QNs conserved

### Changes to applyMPO, nmultMPO and DMRG

- Add "Silent" arg in DMRG to suppress all output

- Make DMRG return the optimized MPS: `auto [E,psi] = dmrg(H,psi0,args)`

- Changes to applyMPO:
    - `applyMPO(A,x) -> y`, y now has the exact site indices of A|x> and the link tags of x (to allow more general tag conventions)
    - Remove support for `zipUpApplyMPO`, `exactApplyMPO`, `fitApplyMPO` interfaces

- Added `errMPOProd(MPS y, MPO A, MPS x)` to measure the error ||y> - A|x>|
    - Deprecated `checkMPOProd`

- Changes to nmultMPO:
    - `nmultMPO(A,B) -> C`, C now has the exact site indices of AB and the link tags of A (to allow more general tag conventions)

- DMRG operations:
    - `idmrg()` function moved to it's own repo (https://github.com/ITensor/iDMRG)
    - Deprecate "Maxm", "Minm" args in favor of "MaxDim", "MinDim" in dmrg()
    - In Sweeps object, added deprecation warning for .maxm() and .minm(), saying to use .maxdim() and .mindim()

### Changes to SiteType and SiteSets

- SiteType changes:
    - Default constructors `SpinHalfSite()`, `SpinOneSite()`, etc. now make a site, but without an `"n="+str(n)` tag (before made an empty Index)
    - Specify the site number with `{"SiteNumber=",n}` arg, instead of `SpinHalf(int n, Args args)` (old version kept for backwards compatibility)
    - `index(SiteType) -> Index`, `op(SiteType,string) -> ITensor, `state(SiteType,string) -> IndexVal` now have free function versions (in V2, they were only member functions)

- SiteSet changes:
    - Use `Electron(10,{"ConserveQNs=",false})` to get spinful electrons with no QNs
        - SiteSets except for the default one default to `{"ConserveQNs=",true}`
    - New `Boson` SiteType and `BosonSite` SiteSet
    - Rename `HubbardSite` -> `ElectronSite` (deprecated with a typedef)
    - Rename `SpinlessSite` -> `FermionSite` (deprecated with a typedef)
    - Make `op(sites,i,"Up")` a free function
    - Add `SiteSet(IndexSet)` constructor
    - Add `inds(SiteSet) -> IndexSet` function to get the indices of a SiteSet as an IndexSet


<a name="v2.1.1"></a>
## [Version 2.1.1](https://github.com/ITensor/ITensor/tree/v2.1.1) (Aug 8, 2017) ##

### Feature improvements

* Completely new implementation of exactApplyMPO which scales much better
  than previous version and uses a globally optimal approximation
  for compressing the resulting MPS.

* New interface for fitApplyMPO that returns the resulting MPS.

* Added `combinedIndex` function which fetches the combined index of a
  combiner (both ITensor and IQTensor versions)

* New version of `.set` method of ITensor and IQTensor that
  accepts a vector of IndexVals (thanks Mengsu Chen for suggesting)

* Added "IndexName" option to diagHermitian.

* Added operator[] element access to Ten, TenRef, TenRefc classes

* Added itensor::read and itensor::write for std::array

* Added read/write methods for Args (thanks Lars-Hendrik Frahm)

* Added read/write methods for for Ten class

### Bug Fixes

* Added missing `defined` macro keyword in lapack\_wrap.h (thanks Jahan Claes)

* Enclosed error.h functions in itensor namespace (thanks Mengsu Chen)

* Added a macro directive to undefine the `I` macro defined by complex.h

* Added missing setA method for MPO template class (thanks Martin Richter)

<a name="v2.1.0"></a>
## [Version 2.1.0](https://github.com/ITensor/ITensor/tree/v2.1.0) (Jun 1, 2017) ##

* New default [[AutoMPO|classes/autompo]] backend that supports terms with operators acting on more than two sites. This backend also performs a series of SVDs to compress the resulting MPO to as small a bond dimension as possible, which can be extremely useful for MPOs representing long-range interactions, for example. (Thanks to Anna Keselman for a lot of hard work on this new system.)

* Changed Index (and IQIndex) internal ID numbers to be 64 bit. Fixes random crash bug during long time evolution runs reported by multiple users. <span style="color:red;">Note:</span> this change is backwards incompatible with tensors or other objects such as MPS saved to disk in previous version of ITensor.

* New [[SiteSet|classes/siteset]] system. New design makes it easier to create SiteSets with a mixture of different local degrees of freedom (such as spin chains with alternating spin sizes). It is also now very cheap to copy a SiteSet as all copies point to the same underlying storage.

* New ScalarReal and ScalarCplx storage types. Leads to cleaner handling of scalar ITensors and IQTensors. (Thanks Chia-Min Chung for suggestions leading to this design.)

* Build system now optionally builds dynamic libraries. (Thanks Kyungmin Lee for contributing this.)

* New [[MPS::orthogonalize|classes/mps#orthogonalize]] algorithm. Orthogonalizes MPS in a single pass without using a more heuristic two-pass approach like the older routine did.

* Fixed a faulty optimization of IQTensor combiners for the case of combining a single IQIndex. (Thanks Chia-Min Chung for reporting this.)

* Changed logic for deducing the arrow direction of the IQIndex produced by a combiner when the combined indices have different arrow directions. (Thanks Lars-Hendrick Frahm for bringing this to my attention.)

* New SpinTwo SiteSet. (Thanks Samuel Gozel for contributing.)

* New parallel.h tools for sending tensors and other data via MPI. (Thanks Lars Frahm for improvements to this also.)

* More efficient implementation of gateTEvol template routine.


<a name="v2.0.11"></a>
## [Version 2.0.11](https://github.com/ITensor/ITensor/tree/v2.0.11) (Sep 8, 2016) ##

* Fixed poor convergence of idmrg, which was due to a poorly chosen value for a pseudo-inverse cutoff

* Fixed a declaration of an overload of the "overlap" functions

* Added "S+" and "S-" operator names to tJ SiteSet (thanks Mingru Yang for this suggestion)

* Merged pull #108 from user ybarlev, improving lattice generating functions

* Merged pull #107 from user kyungminlee, improving OpenBLAS compatibility

* Updated Davidson code to support multiple targeting

* Merge pull #106 from using mingpu, improving reading of Sweeps from a table in a file

* Fixed bug in printing of SiteSets

* Some improvements to tutorial codes

<a name="v2.0.10"></a>
## [Version 2.0.10](https://github.com/ITensor/ITensor/tree/v2.0.10) (Jun 19, 2016) ##

* Fixed bug where denmatDecomp and diagHermitian were passing wrong scale factor to showEigs method (did not affect results, only printing of density matrix eigenvalues)

* factor decomposition now returns a Spectrum object computing by the svd

* Added optional method to MPS/IQMPS: you can use Aref(int i) as an alternative to Anc(int i)

* Added -lpthread to suggested flags for PLATFORM=lapack in options.mk.sample

<a name="v2.0.9"></a>
## [Version 2.0.9](https://github.com/ITensor/ITensor/tree/v2.0.9) (Jun 8, 2016) ##

* Reorganized library code for big speedup of driver-code compile times.

* Restored computation of quantum numbers of entanglement spectrum. It is now only done if requested
  by passing the (boolean) named arg "ComputeQNs".

* Fixed bug where AutoMPO was not working for non-QN conserving operators (thanks Yifan Tian).

* Fixed bug where Truncate=false was getting set back to true if other truncation args (Cutoff, Maxm) were set
  (thanks Bill Huggins).

* Fixed autovector to allow types with non-constexpr default constructor.

* Changed averageM(MPS) to return a Real instead of an int.

* Broke up some big source files to aid compilation on Windows using cygwin.


<a name="v2.0.8"></a>
## [Version 2.0.8](https://github.com/ITensor/ITensor/tree/v2.0.8) (May 24, 2016) ##

* Fixed major bug in davidson algorithm where Gram-Schmidt was not being repeated after orthog failure.

* Improved behavior of Truncate argument to svd and diagHermitian. Now gets set to true automatically if a truncation parameter (such as Cutoff or Maxm) is set.

* Split tensor decomposition and MPS code into separate .cc files to help with linker limitations on Windows.

* Removed static vectors from lapack_wrap.cc to make calls to these wrappers thread safe.

* Fixed compilation errors and an off-by-one bug in stats.h

* Fixed issue with using exactApplyMPO with same input and output MPS

* Added sweepnext1 for single site sweeping algorithms

* nmultMPO now uses a small default cutoff if none is provided

<a name="v2.0.7"></a>
## [Version 2.0.7](https://github.com/ITensor/ITensor/tree/v2.0.7) (May 2, 2016) ##

* Product of IndexVal and scalar now works for complex scalars too

* Combined prime function taking Index objects and function taking IndexType arguments 
  into single function which can take combinations of both.

* Function findIQInd now returns default-constructed IQIndex if not found; previously would throw an exception.

* orderedC function now switches ITensor storage to complex if it was real instead of throwing an exception.


<a name="v2.0.6"></a>
## [Version 2.0.6](https://github.com/ITensor/ITensor/tree/v2.0.6) (Apr 27, 2016) ##

* Fixed some cases which failed to compile when using the .apply method on ITensor and IQTensor with diagonal storage.

* Fixed addition of Diag ITensors to work in all real or complex combinations.

* Added second argument to expHermitian function, which is necessary for including a complex factor in the exponential.

* Merged pull request #104 from Kyungmin Lee, which includes cstdlib header in error.h

<a name="v2.0.5"></a>
## [Version 2.0.5](https://github.com/ITensor/ITensor/tree/v2.0.5) (Apr 25, 2016) ##

* Added `expHermitian` function for exponentiating Hermitian tensors

* Added new `eigen` function for computing eigenvectors and eigenvalues of a general tensor

* Fixed `ordered` and `orderedC` to make sure ITensor is allocated

* Building library now updates timestamp of `all.h`, `all_basic.h`, and `all_mps.h` files

<a name="v2.0.4"></a>
## [Version 2.0.4](https://github.com/ITensor/ITensor/tree/v2.0.4) (Apr 18, 2016) ##

* Introduced convenience headers all.h, all_basic.h, and all_mps.h. Thanks for Siva Swaminathan for emphasizing the need for these.

* Merge pull requests by Kyungmin Lee which fix various issues when using ITensor on Windows.

* Updated tutorial/project_template/ code.

<a name="v2.0.3"></a>
## [Version 2.0.3](https://github.com/ITensor/ITensor/tree/v2.0.3) (Apr 11, 2016) ##

* Fixed LocalOp::diag method to correctly use new `delta` function to tie indices.
  Thanks to Xiongjie Yu for the bug report (bug #96).

* Merged pull request #94 (by Github user xich) which fixes incorrect definition of
  operator+ for IndexSetIter.

* Merged pull request #83 from Kyungmin Lee which fixes cputime.cc when using MSVC compiler.

* Changed how ITensor write-to-disk system works. Fixed some subtle compilation issues
  where write methods weren't being called. Now each storage type implements a 
      write(ostream& s, StorageType const& s) 
  free function.

* Better error messages when doTask overloads are not implemented.

* Passing a complex number with exactly zero imaginary part to `.set` no longer switches storage to complex.

* Fixed `.set` method when arguments include a mix of IndexVals and IQIndexVals.

* Merged pull request #93 from Mingru Yang which fixes out-of-date code in `tutorial/project_template` folder.

<a name="v2.0.2"></a>
## [Version 2.0.2](https://github.com/ITensor/ITensor/tree/v2.0.2) (Apr 2, 2016) ##

* Added the factor decomposition, which uses the SVD to factorize a tensor into just two factors by multiplying the square root of the singular values into the U and V matrices.

* Added helpful functions which return vectors of "bonds" for common two-dimensional lattices. These are extremely useful for making 2D Hamiltonians as MPOs using AutoMPO. See the [[code formula example|formulas/2d_dmrg]].

<a name="v2.0.1"></a>
## [Version 2.0.1](https://github.com/ITensor/ITensor/tree/v2.0.1) (Mar 30, 2016) ##

This version fixes a few bugs:

* Fixed issue where AutoMPO was failing when operators were not provided in order. Also fixes issue with fermions and periodic boundary conditions. Thanks to Jordan Venderley for reporting this.

* Fixed out-of-date interface of LocalMPO_MPS and LocalMPOSet which was preventing excited state DMRG code from compiling.

* Fixed some places where a divide-by-zero error could occur.

This version also includes a new mapprime function which takes an arbitrary number of arguments of the form Index,plevold,plevnew (meaning replace the Index with prime level plevold with prime level plevnew) or of the form IndexType,plevold,plevnew (same but for any Index of that IndexType).
For example, 

    auto T = ITensor(i,prime(j,2),k);
    T.mapprime(i,0,3,j,2,1);

Now T's index i will have prime level 3 and index j will have prime level 1.


<a name="v2.0.0"></a>
## [Version 2.0.0](https://github.com/ITensor/ITensor/tree/v2.0.0) (Mar 25, 2016) ##

<span style="color:red;">Warning:</span> this version contains many breaking changes;
see the [[version 2 transition guide|v2transition_guide]].

Version 2.0 of ITensor is a major update to the internals of the ITensor and IQTensor 
classes. Tensors now store their data in "storage objects" which can have arbitrary
data layouts. The code to manipulate tensor storage deals with the different storage
types through a dynamic multiple dispatch design, revolving around overloads
of the function doTask(TaskType,...) where TaskType is a "task object" saying
which task should be carried out (contraction, addition, mutiplication by a scalar, etc.).

Major changes:

* [[New storage system|articles/storage]] for tensors with "dynamic overloading" a.k.a. multiple dispatch
  for doTask functions carrying out operations on storage types.

* ITensor and IQTensor now share exactly the same interface (they are instantiations
  of the same template class). ITensors and IQTensors are distinguished by what
  type of indices they have (Index versus IQIndex) and what storage types they have.

* New "TensorRef" library for basic tensor operations, such as tensor slicing and 
  permutation. Matrix and vector operations are implemented as a special case of 
  tensor operations.

* Fixed "long run crash" bug that was plauging version 1.x. Most likely fixed
  by better memory safety of TensorRef library.

* No longer any limit on the number of indices ITensors can have.
  This makes ITensor even more useful for two-dimensional
  algorithms such as TRG, PEPS, MERA etc.

* New QN (quantum number) system. To create a quantum number using the
  standard recognized fields (spin "Sz", boson number "Nb", fermion number "Nf",
  or fermion parity "Pf") call the QN constructor as

      auto q = QN("Sz=",-1,"Nf=",1);

  More advanced QNs can be created by provided a list of value-modulus pairs.
  The modulus is an integer saying how addition is defined for that particular
  "slot" of the QN. For example, a QN constructed as `QN({a,1},{b,3})`
  will have the value "a", modulus 1 in slot one and value "b", modulus 3 in slot two. 
  When adding QNs of this type, the first slot will obey regular integer
  addition (@@Z_1@@ in an abuse of notation) while the second slot will obey
  @@Z_3@@ addition rules.

Other changes:

* The Combiner and IQCombiner types no longer exist. Instead, a combiner is
  just a special type of ITensor or IQTensor. To obtain a combiner which
  combines the indices i,j,k, call the function

      auto C = combiner(i,j,k);

  The tensor C will have a fourth index whose size is the product of the sizes
  of i,j, and k.

* It is now mandatory to prefix header file names with their path inside
  the ITensor folder. For example, 

      #include "itensor/iqtensor.h" 
      #include "itensor/mps/dmrg.h"

* User-created IndexTypes are now supported. Internally, an IndexType is now
  just a fixed-size string of up to 7 characters. To make an IndexType
  called "MyType" just do 

      auto MyType = IndexType("MyType");
      auto i = Index("i",5,MyType);





<a name="v1.3.0"></a>
## [Version 1.3.0](https://github.com/ITensor/ITensor/tree/v1.3.0) (Oct 29, 2015) ##

For better compatibility with the upcoming version 2.0 release, this version introduces a new file layout so that users have the option of including header files such as dmrg.h using the code:
`#include "itensor/mps/dmrg.h"`
The itensor/mps/ prefix in this include will become mandatory in version 2.0. This new layout improves readability, and moves away from a more complex build system where header files were copied to the include/ folder (which is still done but only for backwards compatibility).

Other changes:
* Introduced randomTensor(Index...) function for better compatibility with upcoming version 2.0.
* Fixed bug #89: missing scale_.real() reported by @BapRoyer
* Added external rank(T) methods as alternative to T.r()
* Added experimental operator[] to Index which returns a copy with primelevel set to specified value.
* Updated Index printing format to `(name,size,type)'plev`


<a name="v1.2.4"></a>
## [Version 1.2.4](https://github.com/ITensor/library/tree/v1.2.4) (Sep 30, 2015) ##

Both ITensor and IQTensor now support the following element access methods, where I1, I2, ... are Index objects (or IQIndex objects in the case of IQTensor):

    T.set(I1(n1),I2(n2),..., x); //set element to x,
                                 //can be a Real or Cplx scalar

    T.real(I1(n1),I2(n2),...) //return element as real number
                              //throws if non-zero imag part

    T.cplx(I1(n1),I2(n2),...) //return element as complex number

<a name="v1.2.3"></a>
## [Version 1.2.3](https://github.com/ITensor/library/tree/v1.2.3) (Sep 23, 2015) ##

- Fixed major bug where svd of a complex ITensor with a negative scale could fail because the sign of the scale was only being included in the real part of the result. Thanks to Benoit Vermersch for pointing out this bug.

- Introduced fabs(LogNumber) function.

- Some tweaks to how Index, IndexSet, and ITensor are printed.

<a name="v1.2.2"></a>
## [Version 1.2.2](https://github.com/ITensor/library/tree/v1.2.2) (Sep 17, 2015) ##

- Fixed a bug in IQTensor const element access, thanks Shenghan Jiang

- Added stdx utility library which adds convenient extensions to the std library

- Added timers utility for profiling

<a name="v1.2.1"></a>
## [Version 1.2.1](https://github.com/ITensor/library/tree/1.2.1) (Aug 20, 2015) ##

- Created `setA` method for MPS/IQMPS. More self-documenting name and usage than 
  current `Anc` method.

  <div class="example_clicker">Show Example</div>

      auto psi = MPS(sites);
      auto T = ITensor(sites(j));
      T(j(1)) = 1./sqrt(2.);
      T(j(2)) = 1./sqrt(2.);
      psi.setA(j,T);

- `svd` functions now support setting `IndexType` and names of left and right 
  indices of singular value tensor.

  <div class="example_clicker">Show Example</div>

      auto T = ITensor(s1,s2,j);
      ITensor U(s1),D,V;
      svd(T,U,D,V,{"LeftIndexName","L",
                   "RightIndexName","R",
                   "IndexType",Xtype});
      //can also specify "LeftIndexType" and "RightIndexType" separately

- Added `count.h` mini-library. Allows range based iteration over integer ranges.

  <div class="example_clicker">Show Example</div>

      #include "count.h"

      auto v = std::vector<int>(10);
      for(auto n : count(v.size()))
          v[n] = n+n;

      //go from 2,...,v.size()-1
      for(auto n : count(2,v.size()))
          v[n] = n+n;

      //index(v) does count(v.size())
      for(auto n : index(v))
          v[n] = n+n;

      //count1 does 1-indexed counting
      auto T = ITensor(J);
      for(auto j : count1(J.m()))
          T(J(j)) = sqr(j);

- Added external `norm(T)` functions for ITensor and IQTensor.

- Fixed bug where truncation error was not properly reported by ITensor svd function.


<a name="v1.2.0"></a>
## [Version 1.2.0](https://github.com/ITensor/library/tree/v1.2.0) (Aug 13, 2015) ##

<b>New features:</b>

- IndexType now a class instead of an enum; this makes IndexType's user extensible, see commit github:a92c17a

  <div class="example_clicker">Show Example</div>

      auto MyType = IndexType("MyType");
      auto i = Index("i",10,MyType);
      auto j = Index("j",10,Link);

      auto T = ITensor(i,j);

      Print(prime(T,MyType)); //only i will be primed

- Makefiles now hide most compiler output for a nicer installation experience

<b>Bug fixes:</b>

- AutoMPO now works correctly independently of order of operators passed
- Updates to CMakeLists.txt files for cmake users (thanks Andrey Antipov)
- Added MSVC version of mkdtemp for Windows users (thanks Kyungmin Lee)
- Fixed bug in hams/TriHeisenberg.h (thanks Hitesh Changlani)

<a name="v1.1.1"></a>
## [Version 1.1.1](https://github.com/ITensor/library/tree/v1.1.1) (May 18, 2015) ##

<b>Bug fixes:</b>

- Fixed a compilation error due to a typo in lapack_wrap.h (thanks user lukyluket)
- Fixed a compilation error due to missing include in error.h
- Removed use of non-standard variable sized array in utility.cc (thanks user kyungminlee)

<a name="v1.1.0"></a>
## [Version 1.1.0](https://github.com/ITensor/library/tree/v1.1.0) (May 16, 2015) ##


<b>Major design changes:</b>
- Requires C++11. No more boost dependence.
- Removed uniqueReal system from Index due to occasional comparison failures. Now Index comparisons are exact integer comparisons.
- Changed ITensor storage from ref-counted Vector to just std::vector
- Major redesign of IQTensor storage to store ITensor blocks in an ordered array

<b>Major new features:</b>
- AutoMPO: helper class for constructing MPOs with a pencil-and-paper type interface

<b>Bug fixes:</b>
- Fixed invalid memory access in matrix/storelink.h (contributed by Steve White)
- New version of lapack_wrap.h. Previous version had been mistakenly using C99 variable-sized arrays which are not standard C++ (thanks Kyungmin Lee)
- Fixed improper handling of negative scale factors in svd algorithm (thanks to Hitesh Changlani and Bryan Clark)
- Fixes to MatrixRef: moved unsafe iterators from VectorRef to Vector and updated usage of these in ITensor
- Fixed bug in Args::add where const char* was converting to bool
- Removed incorrect usage of delete in Index::read. Replaced with std::unique_ptr.
- Fixed bug in psiHKphi where conj should be replaced by dag (thanks to Ori Alberton).

<b>Other improvements:</b>
- Index no longer uses ref-counted heap storage. Data is directly stored in Index object.
- Improvements to input.h utility library for reading input files
- Added explicit bool conversions to many objects to check if default constructed or not
- Reimplemented ITensor contraction using lightweight SimpleMatrixRef wrapper
- Renamed Opt and OptSet to Args and folded Opt class into private class Args::Val to simplify interface

<a name="v1.0.5"></a>
## [Version 1.0.5](https://github.com/ITensor/library/tree/v1.0.5) (Oct 7, 2014) ##

<b>Bug fixes:</b>

- Fixed incorrect use of `delete` (should have been `delete[]`) in `Index::read`.

<a name="v1.0.4"></a>
## [Version 1.0.4](https://github.com/ITensor/library/tree/v1.0.4) (Oct 2, 2014) ##

<b>Bug fixes:</b>

- Fixed off-by-one memory bug in `MatrixRef::Last()` function.

- Fixed bug where if ITensor scale was negative, ordering of eigenvalues in svd methods could get reversed.

- Fixed bug where ITensor scale not included in eigenvalues returned from diag_hermitian.


<a name="v1.0.0"></a>
## [Version 1.0.0](https://github.com/ITensor/library/tree/v1.0.0) (May 28, 2014) ##

<span style="color:red;">Warning:</span> this version contains many breaking changes.

<b>Major breaking changes:</b>

- Put all code into `namespace itensor`. In your code, put `using namespace itensor;` at the top
  or explicitly qualify types with the itensor:: prefix. (Or wrap header code in `namespace itensor {...};`.)

- Removed ITSparse and IQTSparse classes. Now ITensor class carries an internal flag specifying whether it is
  diagonal (type()==ITensor::Diag) or dense (type()==ITensor::Dense). Diagonal ITensors are created by using
  certain constructors such as the constructor taking a Vector of components.

- Changed name of Hermitian conjugate method `conj` to `dag` (for "dagger"). Added `conj` methods for ITensor and IQTensor
  which take complex conjugate only, without reversing any index arrows.

- Removed minm,maxm,cutoff parameters from MPS. Instead these are passed to various methods which work with MPS
  using the OptSet named argument system.

- MPS class no longer stores a vector of Spectrum objects.

- Addition + operator and += operator no longer defined for MPS/MPO. Instead use the `sum` and `plusEq` functions.

- Spectrum class no longer used to pass accuracy parameters to `svd` and related methods. Instead use the OptSet system.

- Renamed "model" folder to "sites". Renamed `Model` class to `SiteSet`.

- New design for HamBuilder class. Now models an MPO initialized to the identity after which one can modify any 
  number of site operators using the `set` method. Supports multiplication by Real scalars as well. 
  After one sets all desired site operators, a HamBuilder instance can be automatically converted to an MPO or IQMPO.

  <div class="example_clicker">Show Example</div>

        SpinHalf model(100);

        vector<MPO> terms;

        //Can set operators using "set" method
        HamBuilder pm23(model);
        pm23.set("Sp",2,"Sm",3);
        pm23 *= 0.5;
        terms.push_back(pm23);

        //Or using constructor
        terms.push_back(0.5*HamBuilder(model,"Sp",2,"Sm",3));

- Replaced automatic MPO to IQMPO conversion with a named method toIQMPO().

- Made certain MPS/MPO methods external (linkInd, applyGate, averageM, checkOrtho, etc).

<b>Major new features:</b>

- Removed all dependence on boost C++ library when compiling with USE_CPP11=yes in options.mk.

- Included `boost_minimal` folder so that downloading boost is not required when using C++98 (USE_CPP11=no).

- Can now construct OptSet objects from a string such as 

   `"UseSVD=false,Cutoff=1E-8,IndexName=newind"`.

  Writing only the name of an 
  Opt such as "Quiet" is equivalent to "Quiet=true". Can also combine Opts and strings with '&' operator, for example:

  `Opt("Cutoff",1E-8) & Opt("Quiet") & "UseSVD=false,IndexName=newind"`.

- If ITensor is compiled with USE_CPP11, can initialize OptSet arguments using a bracketed list of Opt names and values.

  `some_function(arg1,arg2,{"UseSVD",false,"Cutoff",1E-8});`

  where some_function is a function accepting an OptSet as its last argument.

- Improved printing methods based on the Tinyformat library. Defined print, println, printf, and printfln. These are
  type safe methods with an interface similar to the std C library printf function. The printf methods take a formatting
  string as their first argument. The functions ending in "ln" print a newline at the end.

- Added improved idmrg functions.

- MPS/MPO A(int) and Anc(int) accessors now take negative arguments. For i < 0, A(i) = A(N-i+1).
  For example, use psi.A(-1) to access last site tensor of an MPS psi.

<b>Other major changes:</b>

- Deprecated the functions `primed` and `deprimed` in favor of just `prime` and `noprime` for consistency with Index and
  ITensor class interface.

- Opt names limited to 20 characters for efficiency (this limit can be modified by editing `utilities/options.h` and recompiling).

- Unit test library now based on [Catch](https://github.com/philsquared/Catch) unit test framework.

- Removed sandbox folder.

- Added idmrg sample code.

<b>Other breaking changes:</b>

- Removed deprecated Model named virtual function interface.

- Removed deprecated InitState class method pointer interface.

- Simplified InputFile, InputGroup interface.

- Removed IQTensor::iten_size() method. For an IQTensor T, just use T.blocks().size() instead.

- Renamed IQTensor::iten_empty() to just IQTensor::empty().

- Changed behavior of commonIndex when no common index found: used to throw an exception, now returns a default-constructed ("Null")
  index.

<a name="v0.2.4"></a>
## [Version 0.2.4](https://github.com/ITensor/library/tree/v0.2.4) (April 24, 2014) ##

- Updated license to v1.1, adding suggested wording for citing ITensor and clarifying when it should be cited.

<b>New features:</b>

- More convenient interface to InputGroup class defined in utilities/input.h. Returns parameters instead of pass-by-reference, allowing
  single-line syntax. Also allows specifying default arguments; parameters without defaults are mandatory. github:58dfc538

- Can store edge tensors in MPS or MPO classes by assigning to Anc(0) or Anc(N+1). Useful for infinite DMRG, for example.

<b>Bug fixes and maintenance:</b>

- Fixed some cases where local includes were using angle brackets <...> instead of quotes "..."

- Removed .ih files from MatrixRef library. Non-standard extension was causing issues with certain compiler.

- Fixed some friend declarations that were declaring default arguments (causing breakage under cerain compilers).

- Removed deprecated 'register' keyword from MatrixRef code.

- Fixed a typo: S+ and S- were swapped in the SpinHalf class

- Added missing inline declaration to BondGate<IQTensor>::makeSwapGate.


<a name="v0.2.3"></a>
## [Version 0.2.3](https://github.com/ITensor/library/tree/v0.2.3) (January 21, 2014) ##

<b>New features:</b>

- Model class "op" method now allows operator strings of the form "Op1*Op2" where "Op1" and "Op2" are
  valid operators. The method returns the on-site product of these two operators, similar to calling multSiteOps.

- Can now combine two OptSets using the & operator.

<b>Bug fixes and maintenance:</b>

- Updated tutorial codes to compile with latest library.

- Fixed some namespace/naming conflicts with boost and the std lib (especially involving std::array).

- Updated sample and sandbox codes to use newer interface conventions.

- Fixed BondGate swap operator for the IQTensor case.

- Cleanup of unit tests.

- Added acml lapack wrapper for zgeev.


<a name="v0.2.2"></a>
## [Version 0.2.2](https://github.com/ITensor/library/tree/v0.2.2) (November 11, 2013) ##

- Changed gateTEvol function to be templated over the gate container type.

- Added typedefs Gate and IQGate for BondGate<ITensor> and BondGate<IQTensor>, respectively.

<a name="v0.2.1"></a>
## [Version 0.2.1](https://github.com/ITensor/library/tree/v0.2.1) (November 6, 2013) ##

<b>New features:</b>

- ITensor::randomize and IQTensor::randomize can now generate a random complex tensor if passed the "Complex" Opt.

<b>Internal improvements:</b>

- New simplified implementation of Condenser.


<b>Bug fixes:</b>

- Fixed possible compiler errors when using C++11 standard libraries.

- Fixed error where svd (ITensor case) could sometimes return incorrect singular values (by not including scale factor).

- MPSt::applygate now correctly passes opts to svdBond.

<a name="v0.2.0"></a>
## [Version 0.2.0](https://github.com/ITensor/library/tree/v0.2.0) (October 22, 2013) ##

<b>Interface improvements:</b>

- Model classes now use strings for retrieving operators and site states (the latter are objects of type IQIndexVal).
  The older model class interfaces (e.g. model.sz(5) for a SpinHalf or SpinOne model) are still supported but the new style is preferred&mdash;see 
  the example below.

  <div class="example_clicker">Show Example</div>

        int N = 100;
        SpinHalf model(N);

        //Retrieving site indices
        model(5); //returns an IQIndex
        model.si(5); //this form still works too
        model.siP(5); //primed version of same index
        
        //Retrieving site operators
        model.op("Sz",3);
        model.op("Sp",10);
        model.op("Id",11); //identity operator
        model.op("Sp*Sz",11); //on-site product of two operators
                              //any string of the form A*B works
                              //if A and B are defined operator names

        //Retrieving a site state (of type IQIndexVal)
        model(5,"Up");
        model(5,"Dn");


- InitState class for initializing MPS now uses strings too. Related MPS/IQMPS constructor no
  longer requires redundant Model argument.

  <div class="example_clicker">Show Example</div>

        int N = 100;
        SpinHalf model(N);

        //Initialize an IQMPS to a Neel state
        InitState initState(model);
        for(int i = 1; i <= N; ++i)
            {
            initState.set(i,(i%2==1 ? "Up" : "Dn"));
            }

        IQMPS psi(initState);

<b>Internal improvements:</b>

- IQTensor storage (class IQTDat) no longer holds a separate map of iterators to the ITensor blocks. Instead blocks are
  stored in a std::vector and found using linear search. 
  * Much simpler IQTensor code.
  * No measured loss in speed.
  * Allows removing `mutable` modifier from IQTDat storage.
  * Now possible to set separate tolerance for Index uniqueReals and the ApproxReal class.

<b>Bug fixes:</b>

- Fixed major bug (#45) where ITensor addition was incorrect when adding certain complex ITensors.

- Fixed major bug (#46) where tieIndices was failing for complex tensors.

- Fixed lapack_wrap.h to compile with ACML library.

- Fixed Combiner to automatically init when copied to avoid confusing situations where copies could have a different right() Index.

- Fixed bug in IndexSet constructor when 8 indices provided.

- Updated sample codes.

- Fixed MPO constructor taking a Model class and ifstream to read from disk.



<a name="v0.1.1"></a>
## [Version 0.1.1](https://github.com/ITensor/library/tree/v0.1.1) (August 17, 2013) ##

<b>Major bug fixes:</b>

- IQCombiner now auto-initializes (constructs its "right" IQIndex) when copied. For an IQCombiner "c", this prevents, for example, 
  situations where conj(c) and c could have completely different right IQIndices.

- The error/Error functions now abort instead of throwing an ITError exception. To throw an ITError just use `throw ITError("Message");`
  explicitly.

- Fixed incorrect/buggy constructor for Spectrum objects where an explicit cutoff, maxm, etc. specified.

- Fixed an overflow bug in the ExpM helper class for sweeps where doing a large number of sweeps could cause the maxm to become negative.

<b>Internal improvements:</b>

- Major work on imagTEvol method. More stable to larger time steps and a wider variety of starting states.

<a name="v0.1.0"></a>
## [Version 0.1.0](https://github.com/ITensor/library/tree/v0.1.0) (July 16, 2013) ##

- First numbered version.

- Recently improved handling of complex ITensors and IQTensors. 
ITensors store an (initially null) pointer to their
imaginary part. The imaginary part is allocated only if it is non-zero.

</br>

<!--## [Development Version](https://github.com/ITensor/library/tree/develop) (in progress) ##-->
