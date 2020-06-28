# Change Log (Julia)

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

