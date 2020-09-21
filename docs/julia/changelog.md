# Change Log (Julia)

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

