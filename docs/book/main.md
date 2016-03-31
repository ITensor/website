# <img src="docs/book/icon.png" class="largeicon">  The ITensor Book

ITensor is designed to simplify tensor
calculations through an "Einstein summation" interface for tensor contractions.
ITensor indices are objects which "remember" their identities, so that nothing about the interface
depends on the index ordering; this makes ITensor code easy to write and maintain.
Despite these higher level features, ITensor is very efficient.

The goal of this book is to first familiarize users with the 
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

<br/>
<span style="float:right;"><img src="docs/arrowright.png" class="icon"> 
[[ITensor Library Overview|book/intro]]
</span>
