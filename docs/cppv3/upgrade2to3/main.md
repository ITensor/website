# <img src="docs/VERSION/upgrade2to3/icon.png" class="largeicon"> Version 2 to 3 Upgrade Guide

Here we list some of the largest and most important changes to know about
when switching from ITensor version 2 to version 3. 
We also discuss some upgrades for specific tasks you 
may have, such as a DMRG calculation.

## Major Changes

* **C++17 is required to compile the ITensor Library.** Switching to C++17
  allows us to make significant interface improvements, such as using 
  multiple return values, and also make internal, developer-level code
  easier to read and maintain. To upgrade, change your
  compiler flags <br/>from `-std=c++11` to `-std=c++17`.

* **Changes to Index objects:** 
  - only the dimension is required to construct an Index (no name string)
  - you can optionally provide a string which is a comma-separated list of "tags"
    Index objects must have the same set of tags to compare equal. Tags can be 
    added, removed, and replaced.
  - the dimension of an Index i is now accessed as `dim(i)`, versus `i.m()` in version 2.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(3);
      println("i is an Index of dimension ",dim(i));
      //prints: i is an Index of dimension 3

      auto j = Index(5,"j,Site,Top");
      println("j has the tags ",tags(j));
      //prints: j has the tags j,Top,Site

* **Tensor decompositions provide multiple return values.** The new, preferred
  interfaces for tensor decompositions such as `svd` and `diagHermitian` no
  longer takes the factored results by reference, but returns them using the
  new "structured binding" or multiple-return-value feature of C++17.
  For more details, see the [[tensor decomposition docs|classes/decomp]].

  <div class="example_clicker">Click to Show Example</div>

      auto l1 = Index(8,"l1");
      auto l2 = Index(4,"l2");
      auto s = Index(2,"s1");

      auto T = randomITensor(l1,s,l2);

      auto [U,S,V,u,v] = svd(T,{l1,s});

* **To access individual MPS tensors**, say of an MPS object `psi`, just
  call `psi(j)`. To replace the tensor at site j with a tensor `T`, call
  `psi.set(j,T)`. Or to modify the tensor in-place, do `psi.ref(j) = T`.

* **The `IQTensor`, `IQIndex`, `IQMPS`, and `IQMPO` types have been removed.**
  An IQIndex is now just an Index which carries extra quantum number (QN) information.
  An IQTensor is now just an ITensor with block-sparse storage internally and whose
  indices carry quantum numbers. You can use the `hasQNs` function to inspect
  whether an Index or ITensor has QN block structure.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(QN({"Sz",-1}),4,
                     QN({"Sz", 0}),8,
                     QN({"Sz",+1}),4);
      Print(hasQNs(i));
      //prints: hasQNs(i) = true
      println("i is an Index of dimension ",dim(i));
      //prints: i in an Index of dimension 16

      auto T = ITensor(i,prime(i));
      T.set(i=1,prime(i)=1,-0.234);
      PrintData(T); //view the storage of T to see it's block-sparse

      Print(hasQNs(T));
      //print: hasQNs(T) = true

* **Quantum number QN objects use strings to label each of their values.** 

## Task-Specific Upgrades

* **Upgrading a DMRG Calculation**
