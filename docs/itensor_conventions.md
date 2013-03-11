#Tensor and Index Conventions#

##Arrows##

* IQIndex Arrows (represented by the Arrow enum) have the values In or Out and should not be thought of
as pointing in an absolute direction such as up/down/left/right.

* Conceptually Arrows represent the flow or flux of quantum numbers out of a tensor. Equivalently, they
specify whether a particular index transforms as a ket (a vector, or raised index in classic tensor notation) 
or a bra (a covector, dual vector, or lowered index). 

* An Out Arrow means the index transforms as a ket (for example, a site of an MPS), an In Arrow means an index transforms as a bra.

* Conjugating a tensor (applying conj(T)) reverses Arrow directions in addition to taking the complex conjugate.

##Index Types##

* The two primary index types (represented by the IndexType enum) are `Site` and `Link`.

* `Site` indices are physical, or real, indices such as the sites of a lattice model.

* `Link` indices (sometimes called virtual indices) label internal, or gauge, degrees of freedom of a tensor network.
For example, the bonds of a matrix product state are `Link` indices.

* The real and imaginary parts of a complex ITensor or IQTensor are indexed by a special Index or IQIndex
of type `ReIm`.

* There is a special IndexType `All` which can be used to specify that a certain function or transformation 
should be applied to all indices regardless of type.

##Matrix Product States##

* An orthogonality center of a matrix product state or MPS is any tensor whose indices all label 
orthonormal states. For example, every site tensor of a canonical MPS is an orthogonality center.
During a conventional DMRG calculation, where an MPS is in the so-called mixed canonical gauge, 
only one tensor (the left or right of the two "center" sites depending on sweep direction) is an ortho center.

* All Arrows (including both Link and Site indices) flow Out from the orthogonality center of an MPS.
For a normalized MPS in a well-defined gauge, therefore, a tensor is an ortho. center if and only if 
all its indices point Out.

##Operators##

* Single-site operator tensors have one unprimed Site index `S` and one primed Site Index `S'`.
  For IQTensor operators, IQIndex `S` has an In Arrow and `S'` an Out Arrow.

* Each tensor of a matrix product operator (MPO) follows the same convention as a single-site operator above.

* Unless an MPO is in a definite gauge (typically not the case), Link arrows should flow out from the first site tensor.



</br>

[[Back to Main|main]]
