# <img src="docs/book/icon.png" class="largeicon">  The ITensor Book

Tensor methods are a powerful approach for problems in physics and
applied mathematics, but keeping track of tensor indices can be tedious
and error-prone.

Inspired by tensor diagram notation, ITensor automatically handles
low-level details of index ordering and data permutation, freeing the user
to think about the structure of tensor networks. Indices in ITensor
carry extra information and "multiplying" two ITensors contracts all
matching indices, similar to Einstein summation.
Despite these higher level features ITensor is very efficient.

The goal of this book is to quickly familiarize users with the 
main features of ITensor. Later chapters turn to advanced features and
customizing higher-level parts of the library.

# Table of Contents

- [[ITensor Library Overview|book/intro]]

### ITensor Fundamentals

- [[Index Objects|book/index]]

- [[ITensor Basics|book/itensor_basics]]

- [[Contracting ITensors|book/itensor_contraction]]

- [[Factorizing ITensors (SVD Example)|book/itensor_factorizing]]

- [[Case Study: TRG Algorithm|book/trg]]

<!--
- [[Sparse ITensors (combiners, diagonal,...)|book/itensor_sparse]]
-->

### IQTensor: Block Sparse, Symmetry Preserving Tensors

<!--
- [[IQTensor Overview|book/iqtensor_overview]]
- [[IQIndex Objects|book/iqindex]]
- [[IQTensor Basics|book/iqtensor_basics]]
-->

### Matrix Product States and DMRG

### Design of ITensor Library and Internals

<!--
- [[Dynamic Storage System|book/dynamic_storage]]
- [[Scale Factors (LogNum)|book/scale_factors]]
- [[TensorRef Layer|book/tensorref]]
-->

_The ITensor Book is written and maintained by Miles Stoudenmire_

<br/>
<span style="float:right;"><img src="docs/arrowright.png" class="icon"> 
[[ITensor Library Overview|book/intro]]
</span>
