# <img src="docs/VERSION/upgrade2to3/icon.png" class="largeicon"> Version 2 to 3 Upgrade Guide

Here we list some of the largest and most important changes to know about
when switching from ITensor version 2 to version 3. 
We also discuss some upgrades for specific tasks you 
may have, such as a DMRG calculation.

For much more detailed info about the changes made in version 3, see the [[changelog|changelog]].

To move to version 3 if you have already cloned ITensor, 
you have to switch to the `v3` branch. To do so, use the commands<br/>
`git pull`<br/>
`git checkout v3`<br/>

## Major or Required Changes

* **C++17 is required to compile the ITensor Library.** Switching to C++17
  allows us to make significant interface improvements, such as using 
  multiple return values, and also make internal, developer-level code
  easier to read and maintain. To upgrade, change your
  compiler flags <br/>from `-std=c++11` to `-std=c++17`.
  (For C++ aficionados, here is a [website](https://github.com/AnthonyCalandra/modern-cpp-features) 
   with the new C++17 features.)

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
  Each sector of a QN object is specified by a string and an integer value.
  You can optionally specify a "mod factor" N if the sector follows a @@\mathbb{Z}_N@@
  addition rule. For efficiency, the name string of the sector must be seven characters
  or less. Sectors are sorted by their name and you must use the name to access the value.
  Having strings in QN objects allows sensible addition between QNs which do not all
  carry the same sectors; a missing sector is treated as having the value zero.
  For more information see the [[QN docs|classes/qn]].

  <div class="example_clicker">Click to Show Example</div>

      auto q1 = QN({"Sz",+1});
      Print(q1.val("Sz"));
      //prints: q1.val("Sz") = 1

      auto q2 = QN({"N",3},{"T",-2});
      Print(q2.val("T"));
      //prints: q2.val("T") = -2
      Print(q2.val("N"));
      //prints: q2.val("N") = 3

      //Make a QN with a Z2 addition rule:
      auto q3 = QN({"P",1,2});
      Print(q3.val("P"));
      //prints: q3.val("P") = 1
      Print(q3.mod("P"));
      //prints: q3.mod("P") = 2
      Print(q3+q3);
      //prints: q3+q3 = QN({"P",0});

## Recommended, Optional Changes

These are changes we recommend to follow the standards of version 3, or to avoid
using now-deprecated features, but which are not required to make your code compile:

* **To retrieve elements of tensors** use the free function `elt` if 
  the ITensor is real, or `eltC` if the ITensor could be complex.

  <div class="example_clicker">Click to Show Example</div>

      auto T = randomITensor(i,j,k);

      auto x = elt(T,i=1,j=1,k=1);

      auto V = randomITensorC(m,n);

      auto z = eltC(V,n=2,m=3);

* **Physics-specific Site Sets Carry QNs by Default**. If you use
  a site set such as `SpinHalf` or `Electron` (formerly called "Hubbard"),
  the indices and operators produced from these will be QN-block-sparse.
  If you wish to omit or not have the QN sparsity, pass a named argument
  `{"ConserveQNs=",false}` to the site set constructor, for example <br/>
  `auto sites = SpinHalf(N,{"ConserveQNs=",false});`.

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

      auto [U,S,V] = svd(T,{l1,s});

* **To access individual MPS tensors**, say of an MPS object `psi`, just
  call `psi(j)`. To replace the tensor at site j with a tensor `T`, call
  `psi.set(j,T)`. Or to modify the tensor in-place, do `psi.ref(j) = T`.

## Task-Specific Upgrades

* **Upgrading a DMRG Calculation**
  The following steps should be sufficient for upgrading an existing DMRG code
  from version 2. Also we suggest you look at the sample DMRG codes in the sample/
  folder distributed with the ITensor source.

  - if using AutoMPO to construct your Hamiltonian MPO, replace the line
    `auto H = MPO(ampo);` with `auto H = toMPO(ampo);`
  - if using IQMPO and IQMPS, just replace these with `MPO` and `MPS` instead
    and make sure the indices or site set you use to construct these 
    carry QN block structure (you can print out these objects to see the QNs
    and ITensor storage type). 
  - make sure to initialize the MPS you pass as an initial state to the `dmrg`
    function. In version 2, a non-QN MPS would be randomly initialized, but
    now you must initialize all MPS. See the sample/dmrg.cc code for an example
    of initializing an MPS to a particular product state.
  - when constructing a Sweeps object, replace the line `sweeps.maxm() = 10,20,40;`
    with `sweeps.maxdim() = 10,20,40;`
  - prefer to call dmrg as `auto [energy,psi] = dmrg(H,psi0,sweeps,"Quiet");`

* **Changes to priming functions**
  To accommodate the new tags interface, some priming functions have been superceded by tag
  functions (since the prime level can be accessed through the new tag interface). Please see
  the __Tag and Prime Methods__ section of the [[IndexSet docs|classes/indexset]] for more 
  details on the new interface. This interface works for ITensor, MPS and MPO objects. For example:

  - instead of `mapprime(T,0,1)`, use `replaceTags(T,"0","1")` (note that tags that are just 
    integer numbers are interpreted as prime levels).
  - instead of `swapPrime(T,0,1)`, use `swapTags(T,"0","1")`.
  - for all tagging and priming methods, optional matching tags and indices are the last
    input of the function (for example, use `prime(T,2,i)` to increase the prime level of 
    Index `i` of ITensor `T` by two).
  - indices used for matching are now always matched exactly, without ignoring the prime level. 
    For example, if ITensor `auto T = ITensor(i,prime(i),j)` where Index `i` is 
    `auto i = Index(2,"i")` and Index `j` is `Index(3,"j")`, to prime indices `i` and 
    `prime(i)` use either `prime(T,{i,prime(i)})` or `prime(T,"i")` since `prime(T,i)` 
    will only prime Index `i`).

* **Changes to MPS and MPO Functions**
  Some conventions and names have changed for common MPS and MPO functions, such as `applyMPO`
  and `nmultMPO`. For more details, please see the [[MPS and MPO docs|classes/mps_mpo_algs]].

  - Use `removeQNs` to remove the QNs of an MPS or MPO, instead of converting from IQMPS to MPS 
    or IQMPO to MPO.
  - use `inner` and `innerC` instead of `overlap` and `overlapC` to get inner products of MPSs 
    (and inner products of MPSs contracted with MPOs).
  - use `trace` and `traceC` to get the trace of an MPO or the trace of the product of two
    MPOs (superceding some use cases of `overlap`).
  - the interfaces `exactApplyMPO` and `fitApplyMPO` have been removed in favor
    of the single `applyMPO` function.
  - when calling `auto y = applyMPO(A,x)`, for MPS `x` with unprimed site indices and MPO `A` with
    pairs of prime and unprimed site indices, the resulting MPS `y` will have primed indices 
    (or in general, the site indices that are not shared by MPO `A` and `x`). 
    Use `y.replaceTags("1","0")` or `y.noPrime()` to get back an MPS with unprimed site indices.
  - for MPOs `A` and `B` with pairs of primed and unprimed site indices, contract them together
    with `auto C = nmultMPO(prime(A),B)`. The inputs must share one site index per tensor, and
    the output MPO `C` will have the remaining unshared site indices (so one unprimed site index
    and one site index of prime level 2). One can use `C.setPrime(1,"2")` or 
    `C.replaceTags("2","1")` to get an MPO `C` with pairs of unprimed and single-primed indices.

