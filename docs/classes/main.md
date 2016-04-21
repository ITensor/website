# <img src="docs/classes/icon.png" class="largeicon"> ITensor Library Classes and Methods #

Detailed information about every method and function in the ITensor library.


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

## ITensor

* [[ITensor|classes/itensor]]. The elementary tensor type. <br/>

* Sparse ITensors:

    - [[Single Element ITensor|classes/single_itensor]]
    - [[Combiner|classes/combiner]]
    - [[Delta and Diagonal ITensor|classes/diag_itensor]]

<br/>
<br/>
<span style="color:red;font-style:italic;">Note: the remainder of these links refer to code prior to version 2.0</span>

## Methods for working with tensors

* [[SVD Algorithms|classes/svdalgs]]. Singular value decomposition, density matrix diagonalization, etc.
* [[Spectrum|classes/spectrum]]. Class for storing & analyzing density matrix eigenvalue spectrum.

## Matrix product states and DMRG

* [[MPS and IQMPS|classes/mps]]. Matrix product state class. <br/>
  [[MPS Functions|classes/mps_functions]]. Functions for working with MPS. <br/>
  [[InitState|classes/initstate]]. Class for initializing matrix product states.
* [[SiteSet|classes/siteset]]. Class handling the site space.
    * [[SpinHalf|classes/spinhalf]]. Set of S=1/2 degrees of freedom.
    * [[SpinOne|classes/spinone]]. Set of S=1 degrees of freedom.
* [[Sweeps|classes/sweeps]]. Class for specifying DMRG sweep parameters.


* [[Options|classes/options]]. Class for specifying various options.

The above documentation may omit minor details that do not change method semantics, 
for example, describing a particular function signature as `f(ITensor T)` even though
for efficiency reasons its actual signature is `f(const ITensor& T)`. 
Also the return type is often omitted for functions returning `void`.

