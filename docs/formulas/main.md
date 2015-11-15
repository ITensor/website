# <img src="docs/formulas/icon.png" class="largeicon">  Code Formulas #

Below are code "formulas" for common tasks that come up when using ITensor. 
Please email Miles (emiles -at- pitp.ca) to suggest a formula you would
like to see.

## General Formulas 

* [[Creating your own "driver" code that builds against ITensor|formulas/driver]]

## ITensor Formulas
Formulas about working with individual tensors and indices (objects like Index, ITensor).

* [[Create a set of Site indices to use as a lattice|formulas/index_sites]]
* [[Make a single-site operator (no quantum numbers)|formulas/itensor_single_site_op]]

## IQTensor Formulas
Formulas involving quantum number tensors and indices (objects such as IQIndex, IQTensor).

(None yet - please suggest one!)

## MPS and DMRG Formulas
Formulas involving matrix product states and DMRG.

<div style="margin-left:30px;margin-top:-50px;"> <!--Begin Indent-->
### Running DMRG
* [[Perform a basic DMRG calculation|formulas/basic_dmrg]]
* [[Compute excited states using DMRG|formulas/excited_dmrg]]
* [[Read and write an MPS or MPO to and from disk|formulas/readwrite_mps]]
* [[Stopping a DMRG Run "Gracefully"|formulas/stopping_dmrg]]

### Measuring MPS
* [[Measure local properties of an MPS wavefunction|formulas/measure_mps]]
* [[Measure two-point correlator from an MPS wavefunction|formulas/correlator_mps]]
* [[Compute entanglement entropy|formulas/entanglement_mps]]

### Time Evolution
* [[Time-evolving an MPS with an MPO (matrix product operator)|formulas/tevol_mps_mpo]]


</div> <!--End Indent-->
