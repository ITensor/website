
# <img src="docs/tutorials/icon.png" class="largeicon"> Tutorials


### Basics of ITensor

* [[ITensor Quick Start|tutorials/quickstart]]

  Simplest non-trivial program (similar to "hello world") based on the ITensor library.

* [[Citing the ITensor Library|tutorials/citing]]

  How to cite the ITensor Library in a paper or published work.

### Tensor Network Fundamentals

* [[Understanding Tensor Diagrams|tutorials/diagrams]]

  Tensor network diagrams are a powerful way to express 
  contractions of many tensors.
  Learn to understand tensor diagrams and translate them 
  into ITensor code.

* [[Estimating the Cost of Evaluating a Tensor Network|tutorials/cost]]

  We discuss how to determine the cost of evaluating a tensor network and best practices for 
  computing properties of matrix product states.

* [[Singular Value Decomposition|tutorials/SVD]]
  
  The singular value decomposition (SVD) provides a way to separate large degrees 
  of freedom from irrelevant ones.  ITensors allows for the easy SVD of tensors.

* [[Fermions and Jordan-Wigner String|tutorials/fermions]]

  Learn how to map fermionic operators to bosonic operators with non-local "string" operators.


### ITensor Library Tutorials

* [[Priming Indices in ITensor|tutorials/primes]]

  ITensor uses a flexible priming system to prevent indices from automatically 
  contracting.  We discuss best practices and give examples.

<!-- Commented out for the time being
* [[The Matrix Product State (MPS)|tutorials/MPS]]

  ITensor includes a full-featured matrix product state class that can be used
  with or without quantum number conservation.
  -->

* [[Choosing DMRG Parameters|tutorials/dmrg_params]]

  Learn how to choose optimal parameters (number of sweeps; cutoff; etc)
  for DMRG calculations of ground states.

* [[Matrix Product States (MPS)|tutorials/MPS]]

  A matrix product state (MPS) is a tensor network often used to
  represent ground states and low-lying excited states of one-dimensional
  quantum systems. Learn about some basics of using MPS with ITensor.


* [[Matrix Product Operators (MPO)|tutorials/MPO]]

  Hamiltonians and other sums of local operators can be represented as a tensor 
  network called an MPO. This tutorial introduces the idea of an MPO with an 
  example, and gives a taste of some advanced concepts.


* [[Introduction to AutoMPO|tutorials/AutoMPO]]

  Instead of making MPOs by hand, ITensor has a facility to create MPOs using a
  simple interface resembling hand-written mathematical notation.


* [[Calculating a Two-Site Correlation Function|tutorials/correlations]]

  Contracting a tensor network to measure a two-operator correlation
  function from an MPS is shown in diagrammatic form with ITensor code.

### C++ Utilities

* [[ITensor Input Parameter System|tutorials/input]]

  ITensor comes with an optional input parameter system you can
  use to read simulation parameters from an external file.

* [[The "Args" Named Arguments System|tutorials/args]]

  Args is a system used in ITensor to pass named parameters to functions,
  and can be a useful addition to your own code.
  Examples of named arguments include SVD accuracy parameters ("Maxm", "Cutoff")
  and parameters controlling the amount of information printed by an algorithm. 

* [[Git Quickstart Guide|tutorials/git]]

  Git is the version control system used to maintain ITensor.
  Learn the basic git workflow and how to contribute to the ITensor code base.


<br/>
