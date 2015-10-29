# TABLE OF CONTENTS (WORKING DRAFT)

* ITensor Library Overview

## ITENSOR FUNDAMENTALS 

* Index Objects

* ITensor Basics

* Contracting ITensors

* Factorizing ITensors
  - SVD
  - diagHermitian

* Adjusting Prime Levels (Advanced Contraction?)
   - prime by Index
   - prime by IndexType
   - mapprime
   - swapPrime
   - primeExcept (v2-only currently)

* Case Study: Tensor Renormalization Group Algorithm
  "We have already assembled enough tools to write a very
   powerful algorithm: tensor renormalization group (TRG)."

* Sparse ITensors
  - combiners
  - diagonal ITensors

* Reading and writing to disk


## IQTENSOR - SYMMETRY PRESERVING TENSORS

* Introduction to IQTensors

* IQIndex Objects

* IQTensor Basics

## MATRIX PRODUCT STATES (MPS) AND DMRG

* MPS/DMRG Overview

* SiteSets

* Constructing MPS

* Making Hamiltonians with AutoMPO

* The DMRG Algorithm

* DMRG Observers

## ADVANCED TOPICS

*  Advanced ITensor/IQTensor Usage
   - realPart, imagPart; takeRealPart, takeImagPart
   - commonIndex,uniqueIndex,
   - making random tensors
   - apply/generate/fill/visit functions; 
     a lot more useful with C++14 auto lambdas but can emulate with a templated function object
   - Contracting ITensor with IndexVal: effectively like contracting with kronecker delta tensor
   - Sparse ITensors (how to create and use cases)
     Generally can be used for "eager slicing" operations which make a copy of the data.
     * Combiners.
     * Identity/projector like tensors.
       Use cases include replacing indices; "tying" indices.
     * Diagonal tensors ("all same" and general)
       Use cases include singular values tensor; tracing other tensors.

## DESIGN OF ITENSOR LIBRARY AND INTERNALS

*  ITensor Internals
   - scale factors
   - Copy-on-write mechanism
   - ITData system (v2)
