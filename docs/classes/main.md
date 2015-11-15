# <img src="docs/classes/icon.png" class="largeicon"> ITensor Library Classes and Methods #

The classes and methods below are ordered starting from most fundamental. (For example, an ITensor stores its indices in an
IndexSet containing Index objects.)

## ITensor: dense tensor class

* [[Index|classes/index]]. Single tensor index. <br/>
  [[Index Functions|classes/index_functions]] for working with Index and similar classes. <br/>
  [[IndexVal|classes/indexval]]. Index set to a particular value. 
* [[IndexSet|classes/indexset]]. Container for storing indices. <br/>
  [[IndexSet functions|classes/indexset_functions]].
* [[ITensor|classes/itensor]]. The elementary tensor type. <br/>
  [[ITensor Functions|classes/itensor_functions]] for working with ITensor and similar classes. <br/>

## IQTensor: quantum number block-sparse tensors

* [[QN|classes/qn]]. Abelian quantum number class.
* [[IQIndex|classes/iqindex]]. Index split into quantum number blocks. <br/>
  [[IQIndexVal|classes/iqindexval]]. IQIndex set to a particular value.
* [[IQTensor|classes/iqtensor]]. Tensor with quantum number block structure.

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

