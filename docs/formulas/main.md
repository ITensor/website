# <img src="docs/formulas/icon.png" class="largeicon">  Code Formulas #

Below are code "formulas" for common tasks that come up when using ITensor. 
Please email Miles (emiles -at- pitp.ca) to suggest a formula you would
like to see.

## General Formulas 

* [[Creating your own "driver" code that builds against ITensor|formulas/driver]]
* [[Running your program in debug mode|formulas/debug_mode]]
* [[Reading input from a file|formulas/input]]

## ITensor Formulas
Formulas about working with ITensors, Index, etc.

* [[Create a set of Site indices to use as a lattice|formulas/index_sites]]
* [[Make a single-site operator (no quantum numbers)|formulas/itensor_single_site_op]]
* [[Extract the Storage of a Dense ITensor|formulas/extractdense]]

## IQTensor Formulas
Formulas involving quantum number tensors and indices (objects such as IQIndex, IQTensor).

(None yet - please suggest one!)

## MPS and DMRG Formulas
Formulas involving matrix product states and DMRG.

* <h3>Running DMRG</h3>
    - [[Perform a basic DMRG calculation|formulas/basic_dmrg]]
    - [[Make a Ladder Hamiltonian for DMRG|formulas/ladder]]
    - [[Make a 2D Hamiltonian for DMRG|formulas/2d_dmrg]]
    - [[Compute excited states using DMRG|formulas/excited_dmrg]]
    - [[Read and write an MPS or MPO to and from disk|formulas/readwrite_mps]]
    - [[Stopping a DMRG Run "Gracefully"|formulas/stopping_dmrg]]

* <h3>Measuring MPS</h3>
    - [[Measure local properties of an MPS wavefunction|formulas/measure_mps]]
    - [[Measure two-point correlator from an MPS wavefunction|formulas/correlator_mps]]
    - [[Compute entanglement entropy|formulas/entanglement_mps]]
    - [[Measure spinless fermion two-point correlator|formulas/spinless_correlator_mps]]

* <h3>Time Evolution</h3>
    - [[Time-evolving an MPS with an MPO (matrix product operator)|formulas/tevol_mps_mpo]]
