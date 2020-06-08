# Change Log (Julia)

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

