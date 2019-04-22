# <img src="docs/VERSION/upgrade2to3/icon.png" class="largeicon"> Version 2 to 3 Upgrade Guide

Here we list some of the largest and most important changes to know about
when switching from ITensor version 2 to version 3. 
We also discuss some smaller changes or changes to specific tasks you 
may have, like setting up a DMRG calculation.

## Major Changes

* **C++17 is required to compile the ITensor Library.** Switching to C++17
  allows us to make significant interface improvements, such as using 
  multiple return values, and also make internal, developer-level code
  easier to read and maintain. To upgrade, change your
  compiler flags from `-std=c++11` to `-std=c++17`.

* **When constructing  Index objects,** you only have to provide the dimension.
  You can optionally provide a string which is a comma-separated list of "tags".
  Index objects must have the same set of tags to compare equal. Tags can be 
  added, removed, and replaced.

* **The `IQTensor`, `IQIndex`, `IQMPS`, and `IQMPO` types have been removed.**
  Instead of IQTensor being a separate type, it is just a type of ITensor
  with block-sparse storage internally. Similarly, an IQIndex is now just
  an Index which carries extra quantum number (QN) information.

* **Tensor decompositions provide multiple return values.** The new, preferred
  interfaces for tensor decompositions such as `svd` and `diagHermitian` no
  longer takes the factored results by reference, but returns them using the
  new "structured binding" feature of C++17.

* **Quantum number QN objects use strings to label each of their values.** 

* **To access individual MPS tensors**, say of an MPS object `psi`, just
  call `psi(j)`. To replace the tensor at site j with a tensor `T`, call
  `psi.set(j,T)`. Or to modify the tensor in-place, do `psi.ref(j) = T`.

## Task-Specific Upgrades

* **Upgrading a DMRG Calculation**
