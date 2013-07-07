# ITensor Library Classes and Methods #

The classes and methods below are ordered starting from most fundamental. For example, an ITensor stores its indices in an
IndexSet, which contains Index objects.

* [[Index|classes/index]]. Single tensor index. <br/>
  [[Index functions|classes/index_functions]] for manipulating [[Index|classes/index]] instances.
* [[IndexVal|classes/indexval]]. Index set to a particular value.
* [[IndexSet|classes/indexset]]. Container template for storing indices. <br/>
  [[IndexSet functions|classes/indexset_functions]].
* [[ITensor|classes/itensor]]. The elementary tensor type.
* [[QN|classes/qn]]. Abelian quantum number class.
* [[IQIndex|classes/iqindex]]. Represents an Index split into quantum number blocks.
* [[SVD Algorithms|classes/svdalgs]]. Singular value decomposition, density matrix diagonalization, etc.
* [[InitState|classes/initstate]]. Class for initializing matrix product states.
* [[Sweeps|classes/sweeps]]. Class for specifying DMRG sweep parameters.

Some commonly occurring methods are not explicitly documented. For instance, nearly all classes in the ITensor Library
support printing using the stream (`<<`) operator. Also, nearly all major classes provide the methods `void read(std::istream& s)`
and `void write(std::ostream& s)` which facilitate reading and writing objects to disk as binary streams.

Also, the above documentation may omit minor details that do not change method semantics, 
for example, describing a particular function signature as `f(ITensor T)` even though
its actual signature is `f(const ITensor& T)` for efficiency reasons.


[[Back to Main|main]]
