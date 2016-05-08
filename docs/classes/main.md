# <img src="docs/classes/icon.png" class="largeicon"> ITensor Library Classes and Methods #

Detailed information about every method and function in the ITensor library.

The documentation may omit minor details that do not change how you use a method,
like describing a particular function as `f(ITensor T)` even though
its actual signature is `f(ITensor const& T)`.

## Index: named tensor index

* [[Index|classes/index]]. Tensor index.

* [[IndexVal|classes/indexval]]. Index-value pair.

* [[IndexType|classes/indextype]]. Lightweight label for Index objects.

* [[IndexSet|classes/indexset]]. Container for storing indices.

## IQIndex: Index with quantum number sectors

* [[QN|classes/qn]]. Abelian quantum numbers.

* [[IQIndex|classes/iqindex]]. Index with quantum number sectors.

* [[IndexQN|classes/indexqn]]. Index-QN pair.

* [[IQIndexVal|classes/iqindexval]]. IQIndex-value pair.

## ITensor and IQTensor

* [[ITensor|classes/itensor]]. The elementary tensor type. <br/>

* Sparse ITensors:

    - [[Single Element ITensor|classes/single_itensor]]
    - [[Combiner|classes/combiner]]
    - [[Delta and Diagonal ITensor|classes/diag_itensor]]

* [[IQTensor|classes/iqtensor]]. Quantum number block sparse tensor.

* [[Tensor Decompositions|classes/decomp]]. Singular value decomposition, density matrix diagonalization, etc.

## Matrix product states and DMRG

* [[MPS and IQMPS|classes/mps]]. Matrix product state class. <br/>

<!--

## Methods for working with tensors

* [[Spectrum|classes/spectrum]]. Class for storing & analyzing density matrix eigenvalue spectrum.

## Matrix product states and DMRG

* [[MPS Functions|classes/mps_functions]]. Functions for working with MPS. <br/>
  [[InitState|classes/initstate]]. Class for initializing matrix product states.
* [[SiteSet|classes/siteset]]. Class handling the site space.
    * [[SpinHalf|classes/spinhalf]]. Set of S=1/2 degrees of freedom.
    * [[SpinOne|classes/spinone]]. Set of S=1 degrees of freedom.
* [[Sweeps|classes/sweeps]]. Class for specifying DMRG sweep parameters.

To Do:
- Spectrum
- InitState
- MPS functions & algorithms
- MPO
- MPO functions & algorithms
- SiteSet
  * SpinHalf
  * SpinOne
  * Spinless
  * Hubbard
  * tJ
  * Z3
- BondGate
- dmrg functions
- idmrg
- Sweeps
- Observer / DMRGObserver
- AutoMPO
- HamBuilder
- Args
- LocalOp, LocalMPO, etc.
-->

