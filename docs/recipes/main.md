# 🍴  Code Recipes #

Below are code "recipes" (code segments) for common tasks that come up when using ITensor. 
Please email Miles (emiles -at- pitp.ca) to suggest a recipe you would
like to see.

## General Recipes 

* [[Creating your own "driver" code that builds against ITensor|recipes/driver]]

## ITensor Recipes
Recipes about working with individual tensors and indices (objects like Index, ITensor).

* [[Create a set of Site indices to use as a lattice|recipes/index_sites]]
* [[Make a single-site operator (no quantum numbers)|recipes/itensor_single_site_op]]

## IQTensor Recipes
Recipes involving quantum number tensors and indices (objects such as IQIndex, IQTensor).

(None yet - please suggest one!)

## MPS and DMRG Recipes
Recipes involving matrix product states and DMRG.

<div style="margin-left:30px;margin-top:-50px;"> <!--Begin Indent-->
### Running DMRG
* [[Perform a basic DMRG calculation|recipes/basic_dmrg]]
* [[Compute excited states using DMRG|recipes/excited_dmrg]]
* [[Read and write an MPS or MPO to and from disk|recipes/readwrite_mps]]
* [[Stopping a DMRG Run "Gracefully"|recipes/stopping_dmrg]]

### Measuring MPS
* [[Measure local properties of an MPS wavefunction|recipes/measure_mps]]
* [[Measure two-point correlator from an MPS wavefunction|recipes/correlator_mps]]
* [[Compute entanglement entropy|recipes/entanglement_mps]]

### Time Evolution
* [[Time-evolving an MPS with an MPO (matrix product operator)|recipes/tevol_mps_mpo]]


</div> <!--End Indent-->
