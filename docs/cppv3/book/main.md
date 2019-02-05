# <img src="docs/VERSION/book/icon.png" class="largeicon">  The ITensor Book

Tensor methods are a powerful approach for problems in physics and
applied math, but keeping track of tensor indices by hand
can be tedious and make your code fragile and prone to bugs.

Inspired by diagrammatic notation for tensor networks, ITensor lets you
focus on the connectivity of tensor networks without thinking about
low-level details like index ordering and data permutation.
Indices in ITensor carry extra information so that "multiplying" 
two ITensors contracts all matching indices, similar to Einstein summation.
ITensor is very efficient despite these high level features.

The goal of this book is to quickly familiarize you with the 
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

### IQTensor: Block-Sparse, Quantum Number Conserving Tensors

- [[IQTensor Overview|book/iqtensor_overview]]
- [[Block-Sparse Tensors|book/block_sparse]]
- [[IQIndex|book/iqindex]]

<!--
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
<span style="float:right;"><img src="docs/VERSION/arrowright.png" class="icon"> 
[[ITensor Library Overview|book/intro]]
</span>
