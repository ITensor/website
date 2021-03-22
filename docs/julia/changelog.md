# Change Log (Julia)

<!-- ## Link to [Development Version](https://github.com/ITensor/ITensors.jl) (master branch) -->

<a name="v0.1.41"></a>
[ITensors v0.1.41](https://github.com/ITensor/ITensors.jl/tree/v0.1.41) Release Notes
==============================

- Fixed: doc link is broken (Issue #599)
- Add documentation for space function for built-in site types (PR #590) (@mtfishman)
- Remove size type parameter from ITensor and IndexSet [WIP] (PR #591) (@kshyatt)
- Add Qubit sites and operators (PR #592) (@emstoudenmire)

<a name="v0.1.40"></a>
[ITensors v0.1.40](https://github.com/ITensor/ITensors.jl/tree/v0.1.40) Release Notes
==============================

- Remove eigen QN fix code (simplify ITensors eigen code by handling QNs better in NDTensors eigen) (PR #587) (@emstoudenmire).
- More general polar decomposition that works with QNs (PR #588) (@mtfishman).
- Bump to v0.1.28 of NDTensors, which includes some bug fixes for BlockDiag storage and makes ArrayInterface setindex compatiblity more general (NDTensors PR #68) (@mtfishman).

<a name="v0.1.39"></a>
[ITensors v0.1.39](https://github.com/ITensor/ITensors.jl/tree/v0.1.39) Release Notes
==============================

- Add Pauli X,Y,Z to S=1/2 site type (PR #576) (@emstoudenmire).
- Add truncation error output to DMRG (PR #577) (@emstoudenmire).
- Bump StaticArrays version to v1.0 (PR #578) (@mtfishman).
- Fix orthogonalize when there are missing MPS link indices (PR #579) (@mtfishman).
- Simplify MPO * MPO contraction and make more robust for MPOs with multiple site indices per tensor (PR #585) (@mtfishman).

<a name="v0.1.38"></a>
[ITensors v0.1.38](https://github.com/ITensor/ITensors.jl/tree/v0.1.38) Release Notes
==============================

Closed issues:

- MPO-MPO multiplication for chain length N=1,2 not working (Issue #544)
- Scalar ITensor for QN or BlockSparse Case (Issue #564)

Merged pull requests:

- Fix bug in BlockSparse-DiagBlockSparse contraction (PR #567) (@mtfishman)
- Add tests for printing QN diag ITensor (PR #568) (@mtfishman)
- Add generic support for scalar ITensor contraction (PR #569) (@mtfishman)
- Fix MPOMPS, MPOMPO for system sizes 1 and 2 (PR #572) (@mtfishman)
- Add support for inner(::MPS, ::MPO, ::MPS) with multiple siteinds per tensor (PR #573) (@mtfishman)
- New MPS/MPO index manipulation interface (PR #575) (@mtfishman)

<a name="v0.1.37"></a>
ITensors v0.1.37 Release Notes
==============================

- Add tests for threaded contraction with no output blocks (PR #565)


<a name="v0.1.36"></a>
ITensors v0.1.36 Release Notes
==============================
- Bump to v0.1.22 of NDTensors which introduces block sparse multithreading. Add documentation and examples for using block sparse multithreading (PR #561) (@mtfishman).
- Make dmrg set ortho center to 1 before starting (PR #562) (@emstoudenmire).

ITensors v0.1.35 Release Notes
==============================
Closed issues:

- Should we define iterate for TagSet? (#542)
- AutoMPO slower than expected (#555)

Merged pull requests:

- Implement iterate for TagSet (#553) (@tomohiro-soejima)
- Add check for Index arrows for map! (includes sum and difference etc) (#554) (@emstoudenmire)
- Optimize AutoMPO (#556) (@mtfishman)
- Add checks for common site indices in DMRG, dot, and inner (#557) (@mtfishman)
- Fix and Improve DMRGObserver Constructor (#558) (@emstoudenmire)
- Update HDF5 to versions 0.14, 0.15 (#559) (@emstoudenmire)

ITensors v0.1.34 Release Notes
==============================
* Allow operator names in the `op` system that are longer than 8 characters (PR #551).

ITensors v0.1.33 Release Notes
==============================
* Fix bug introduced in v0.1.32 involving inner(::MPS, ::MPS) if the MPS have more than one site Index per tensor (PR #549).

ITensors v0.1.32 Release Notes
==============================
* Update to NDTensors v0.1.21, which includes a bug fix for scalar-like tensor contractions involving mixed element types (NDTensors PR #58).
* Docs for observer system and DMRGObserver (PR #546).
* Add `ITensors.@debug_check`, `ITensors.enable_debug_checks()`, and `ITensors.disable_debug_checks()` for denoting that a block of code is a debug check, and turning on and off debug checks (off by default). Use to check for repeated indices in IndexSet construction and other checks (PR #547).
* Add `index_id_rng()`, an RNG specifically for generating Index IDs. Set the seed with `Random.seed!(index_id_rng(), 1234)`. This makes the random stream of number seperate for Index IDs and random elements, and helps avoid Index ID clashes with reading and writing (PR #547).
* Add back checking for proper QN Index directions in contraction (PR #547).

ITensors v0.1.31 Release Notes
==============================
* Update to NDTensors v0.1.20, which includes some more general block sparse slicing operations as well as optimizations for contracting scalar-like (length 1) tensors (NDTensors PR #57).
* Add flux of IndexVal functionality which returns the QN multiplied by the direction of the Index. Make `qn` consistently return the bare QN. Might be breaking for people who were calling `qn(::IndexVal)` and related functions, since now it consistently returns the QN not modified by the Index direction (PR #543).
* Introduce `splitblocks` function for Index, ITensor and MPS/MPO. This splits the QNs of the specified indices into blocks of size 1 and drops nonzero blocks, which can make certain tensors more sparse and improve efficiency. This is particularly useful for Hamiltonian MPOs. Thanks to Johannes Hauschild for pointing out this strategy (PR #540).
* Add Ising YY and ZZ gates to qubits examples (PR #539).

ITensors v0.1.30 Release Notes
==============================
* Update to NDTensors v0.1.19, which includes various block sparse optimizations. The primary change is switching the block-offset storage from a sorted vector to a dictionary for O(1) lookup of the offsets. Note this may be a slightly breaking change for users that were doing block operations of block sparse tensors since now blocks have a special type Block that stores a tuple of the block location and the hash (NDTensors PR #54 and ITensors PR #538).

<a name="v0.1.29"></a>
ITensors v0.1.29 Release Notes
==============================
* Add global flag for combining before contracting QN ITensors, control with enable/disable_combine_contract!(). This can speed up the contractions of high order QN ITensors (PR #536).
* Fix bug when using "end" syntax when indexing ITensors where the Index ordering doesn't match the internal ITensor Index order (PR #537).
* Increase NDTensors to v0.1.18, which includes a variety of dense and sparse contraction optimizations.


<a name="v0.1.28"></a>
## [Version 0.1.28](https://github.com/itensor/itensors.jl/tree/v0.1.28) (Dec 3, 2020)

Closed issues:

* Non-Hermitian bug coming from eigsolve with complex MPO (#517)

Merged pull requests:

* Add DMRG and contraction examples of using TBLIS (#533) (@mtfishman)
* Add support for setting slices of an ITensor (#535) (@mtfishman)

<a name="v0.1.27"></a>
## [Version 0.1.27](https://github.com/itensor/itensors.jl/tree/v0.1.27) (Nov 23, 2020)

* Use LAPACK's gesdd by default in SVD (PR #531).

<a name="v0.1.26"></a>
## [Version 0.1.26](https://github.com/itensor/itensors.jl/tree/v0.1.26) (Nov 20, 2020)

* Introduce a density matrix algorithm for summing arbitrary numbers of MPS/MPO (non-QN and QN) (PR #528).
* Introduce @preserve_ortho macro, which indicates that a block of code preserves the orthogonality limits of a specified MPS/MPO or set of MPS/MPO (PR #528).
* Introduce the ortho_lims(::MPS/MPO) function, that returns the orthogonality limits as a range (PR #528).
* Improves the (::Number * ::MPS/MPO) function by ensuring the number scales an MPS/MPO tensor within the orthogonality limits (PR #528).
* Improve functionality for making an MPO that is a product of operators. In particular, MPO(s, "Id") now works for QN sites, and it adds notation like: MPO(s, n -> isodd(n) ? "S+" : "S-") (PR #528).
* Add SiteType and op documentation.
* Add unexported function ITensors.examples_dir to get examples directory.

<a name="v0.1.25"></a>
## [Version 0.1.25](https://github.com/itensor/itensors.jl/tree/v0.1.25) (Nov 3, 2020)

* Introduce imports.jl to organize import statements (PR #511).
* Add TRG and isotropic CTMRG examples (PR #511).
* Add example for 2D Hubbard model with momentum conservation around the cylinder (PR #511).
* Fix fermion string issue (PR #519)

<a name="v0.1.24"></a>
## [Version 0.1.24](https://github.com/itensor/itensors.jl/tree/v0.1.24) (October 8, 2020) 

Pull requests:

* Add stacktrace output to warn tensor order (#498) (@mtfishman)
* Generalize tr(::MPO) (#509) (@mtfishman)


<a name="v0.1.23"></a>
## [Version 0.1.23](https://github.com/itensor/itensors.jl/tree/v0.1.23) (September 21, 2020) 

Pull requests:

* Add tr(::MPO) (PR #492) (@mtfishman)
* Fix broadcast bug and add new broadcast operations (PR #495) (@mtfishman)

Issues closed:

* Add tr(::MPO) (Issue #487)
* Define lastindex(::ITensor) and lastindex(::ITensor,::Int) (Issue #489)
* Add anyhastags(::ITensor, ::String) and allhastags(::ITensor, ::String) (Issue #491)
* Add 1 ./ A broadcasting operation for ITensor (Issue #493)
* Bug in broadcasting ITensors (Issue #494)

<a name="v0.1.22"></a>
## [Version 0.1.22](https://github.com/itensor/itensors.jl/tree/v0.1.22) (September 11, 2020) 

* Add generic version of "F" operator for non-fermion sites in AutoMPO (PR #469) (@emstoudenmire)
* Introduce Order value type (PR #475) (@mtfishman)
* Add movesites function (PR #477) (@mtfishman)
* Add MPS/MPO circuit evolution (PR #480) (@mtfishman)
* Add docstrings for siteinds methods (PR #481) (@orialb)
* Allow conserving Sz up or down in Fermion type (PR #482) (@mtfishman)
* Add dense function for MPS and MPO (PR #483) (@emstoudenmire)
* Add MPDO sampling (PR #486) (@mtfishman)
* Improve MPS and MPO docs (PR #488) (@emstoudenmire)
* Fix logic of outer has_fermion_string function for products of operators (PR #490) (@emstoudenmire)

<a name="v0.1.21"></a>
## [Version 0.1.21](https://github.com/itensor/itensors.jl/tree/v0.1.21) (July 23, 2020) 

* Add parity conservation to S=1/2 sitetype (PR #467)
  * Add "ProjUp" and "ProjDn" operator definitions to S=1/2 site type.
  * Change QN name "Pf" to "NfParity"
  * Add keyword arguments to choose the QN names when making siteinds.
* Add ! as not syntax (PR #471)
  * Add @ts_str macro for TagSet construction
* Add Sweeps constructor from matrix of parameters (PR #472)
* Add examples of input files (PR #473)
  * Add native ITensors argument parsing with the argsdict() function.
  * Add examples of using ITensors with input files and ArgParse.jl and argsdict().

<a name="v0.1.20"></a>
## [Version 0.1.20](https://github.com/itensor/itensors.jl/tree/v0.1.20) (July 16, 2020) 

* Make ITensors compatible with Julia v1.3 (#468)
* New function filterinds, alias for inds (#466)
* Add QN ITensor from Array constructor (#464)


<a name="v0.1.19"></a>
## [Version 0.1.19](https://github.com/itensor/itensors.jl/tree/v0.1.19) (July 14, 2020) 

* Add setindex!(::MPS, _, ::Colon) (PR #463)
  * Set new limits to limits of input MPS
* Add macros for warn ITensor order (PR #461)
  * Add macros for warn ITensor order
  * Shorten warn ITensor order function name (breaking for anyone who
  managed to use them in the short time they existed).
* Make map for MPS reset the orthogonality limits (PR #460)
  * Makes map and map! reset the orthogonality limits by default.
  * Add keyword argument set_limits to map and map! to let users turn
on and off setting the orthogonality limits (so it can be turned
off for cases like priming).
  * Add orthogonalize, an out-of-place version of orthogonalize!.
  * Add SiteType"S=\1/2" as an alias for SiteType"S=1/2".

<a name="v0.1.18"></a>
## [Version 0.1.18](https://github.com/ITensor/ITensors.jl/tree/v0.1.18) (July 14, 2020) 

* Add functions for controlling warn itensor order (PR #458)
* Add pair syntax to mapprime, replacetags, and replaceinds (PR #459)

<a name="v0.1.17"></a>
## [Version 0.1.17](https://github.com/ITensor/ITensors.jl/tree/v0.1.17) (July 13, 2020) 

* Miscellaneous new ITensor and MPS/MPO functionality (PR #457):
  * Add `eachindex(T::ITensor)` to return an iterator over each cartesian
index of an ITensor (i.e. for an `d x d` ITensor, either `1:d^2` or
`(1,1), (1,2), ..., (d, d)`). For sparse ITensors, this includes
structurally zero and nonzero entries.
  * Add `iterate(A::ITensor, args...)`, which allows using `for a in A
@show a end` to print all elements (zero and nonzero, for sparse
tensors).
  * Add `setindex!(T::ITensor, x::Number, I::CartesianIndex)` to allow
indexing with a `CartesianIndex`, which is naturally returned by
functions like `eachindex`.
  * Add `hasplev(pl::Int)` that returns a function `x -> hasplev(x, pl)`
(useful in functions like `map`).
  * Add `hasind[s](i::Index)` that returns a function `x -> hasind[s](x, i)`
(useful in functions like `map`).
  * Add `hascommoninds(A, B; kwargs...)` which returns true if `A` and `B`
have common indices.
  * Add `findfirstsiteind(M::MPS/MPO, s::Index)` that returns which site
of the MPS/MPO has the site index `s`.
  * Add `findfirstsiteinds(M::MPS/MPO, is)` that returns which site
of the MPS/MPO has the site indices `is`.
  * Add `linkinds(::MPS/MPO)` that returns a vector of the link indices.
  * Add `linkdim(::MPS/MPO, ::Int)` that returns the dimension of the
specified link, and nothing if there is no link found.
  * Add `linkdims(::MPS/MPO)` that returns a vector of the link
dimensions.
  * Fix a bug in `+(::MPST, ::MPST)` that the inputs were getting modified
(the inputs were getting orthogonalized and the prime levels were beging
modified).
  * Add `productMPS(sites, state::Union{String, Int})` to create a uniform
MPS (for example, `productMPS(sites, "Up")` makes a state with all Up
spins).
* Add QR option for factorize (only Dense tensors so far). Used by default
if not truncation is requested (PR #427)


<a name="v0.1.16"></a>
## [Version 0.1.16](https://github.com/ITensor/ITensors.jl/tree/v0.1.16) (July 9, 2020) 

* Update physics site definitions to user newer overload style (PR #453)
* Fix some issues with precompile_itensors.jl code and automatically test it (PR #452)

<a name="v0.1.15"></a>
## [Version 0.1.15](https://github.com/ITensor/ITensors.jl/tree/v0.1.15) (July 7, 2020) 

* Add multi-site op support (PR #444)
* Update state system to be user-extensible using StateName (PR #449)
* Update siteinds system to be more easily extensible using `space` and `siteind` functions (PR #446)
* Remove parenthesis from AutoMPO syntax from tests and examples (PR #448)

<a name="v0.1.14"></a>
## [Version 0.1.14](https://github.com/ITensor/ITensors.jl/tree/v0.1.14) (June 27, 2020) 

* Fix AutoMPO issue #440 (PR #445)
* Have ITensors.compile() compile QN DMRG (PR #442)
* Make linkind return nothing for all links outside the boundary of the MPS (PR #441)

<a name="v0.1.13"></a>
## [Version 0.1.13](https://github.com/ITensor/ITensors.jl/tree/v0.1.13) (June 24, 2020) 

* New ITensors.compile() routine (PR #436, PR #439)
* Propagate keyword args through orthogonalize! (PR #438)
* Speed improvement to op (PR #435)
* Major improvements to op function system (PR #406)

<a name="v0.1.12"></a>
## [Version 0.1.12](https://github.com/ITensor/ITensors.jl/tree/v0.1.12) (June 21, 2020) 

* HDF5 Support for QNITensors, QNIndex (PR #433) 
* Add ProjMPO_MPS to exports

<a name="v0.1.11"></a>
## [Version 0.1.11](https://github.com/ITensor/ITensors.jl/tree/v0.1.11) (June 18, 2020) 

* Add tests for contraction bug. Add tests for extended Spectrum definition (PR #432)

<a name="v0.1.10"></a>
## [Version 0.1.10](https://github.com/ITensor/ITensors.jl/tree/v0.1.10) (June 17, 2020) 

* Fix missing return statement in QNVal constructor (PR #431)

* Fix bug with AutoMPO dimension in certain cases (PR #426)

<a name="v0.1.9"></a>
## [Version 0.1.9](https://github.com/ITensor/ITensors.jl/tree/v0.1.9) (June 12, 2020) 

* Fix bug with AutoMPO dimension in certain cases (PR #426)


<a name="v0.1.8"></a>
## [Version 0.1.8](https://github.com/ITensor/ITensors.jl/tree/v0.1.8) (June 11, 2020) 

* Fix a bug in broadcast and in-place contraction (PR #425)

<a name="v0.1.7"></a>
## [Version 0.1.7](https://github.com/ITensor/ITensors.jl/tree/v0.1.7) (June 10, 2020) 

* Add Unicode support for SmallStrings/Tags (PR #413)
* Speed up small ITensor contractions (PR #423)
* Add swapsites keyword argument to `replacebond` (PR #420)
* Change `flux(::AbstractMPS)` to return nothing in non-QN case (PR #419)


<a name="v0.1.6"></a>
## [Version 0.1.6](https://github.com/ITensor/ITensors.jl/tree/v0.1.6) (June 4, 2020) 

* Allow user to control Arrow direction of combined Index in combiner (PR #417)
* Fix eigen for case when left/right indices had mixed Arrow directions (PR #417)
* Add exp for QN ITensor (PR #402)
* Add Advanced Usage Guide to docs (PR #387)

<a name="v0.1.5"></a>
## [Version 0.1.5](https://github.com/ITensor/ITensors.jl/tree/v0.1.5) (May 28, 2020) 


- Fix bug with combiner (uncombining step) when combined Index is not the first one (PR #401)
- Add check to ProjMPO to ensure result of product is same order as input tensor (PR #390)

<a name="v0.1.4"></a>
## [Version 0.1.4](https://github.com/ITensor/ITensors.jl/tree/v0.1.4) (May 27, 2020) 

* Add note to docs about requiring Julia 1.4 currently
* Improve error message for non-scalar input to `scalar` (PR #396)
* Export @TagType_str macro (PR #393)
* Fix `productMPS` for complex element type (PR #392)

<a name="v0.1.3"></a>
## [Version 0.1.3](https://github.com/ITensor/ITensors.jl/tree/v0.1.3) (May 22, 2020) 

Use NDTensors v0.1.3

Bug fixes:
- fix issue with propagation of type in complex SVD (inside NDTensors) and add unit tests (PR #388)


<a name="v0.1.2"></a>
## [Version 0.1.2](https://github.com/ITensor/ITensors.jl/tree/v0.1.2) (May 21, 2020) ##

New features:
- Add norm, lognorm, loginner for MPS/MPO (PR #384)

Bug fixes and improvements:
- Add docs for Array conversion. Add installation instructions. Reorganize DMRG/ProjMPO docs. (PR #385)
- Remove pre-release install languge from docs/index.md (PR #383)

<a name="v0.1.1"></a>
## [Version 0.1.1](https://github.com/ITensor/ITensors.jl/tree/v0.1.1) (May 20, 2020) ##

Bug fixes and improvements:
- correct QNs for indices introduced in eigen (PR #382)
- fixes for N=1 cases of MPS functions (PR #380)
- remove pre-release language from README 
- improvements to MPS docs (PR #372)
- add compat information and CompatHelper (PR #373)
 
<a name="v0.1.0"></a>
## [Version 0.1.0](https://github.com/ITensor/ITensors.jl/tree/v0.1.0) (May 19, 2020) ##

Initial release of Julia version of ITensor

