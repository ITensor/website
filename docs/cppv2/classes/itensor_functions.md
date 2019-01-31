# ITensor Functions #

<span style="color:red;font-style:italic;">Note: this documentation page refers to code prior to version 2.0</span>

Standalone methods for manipulating objects implementing the [[ITensor|classes/itensor]] interface. 

The following methods are templates, so they work not only for [[ITensor|classes/itensor]] objects
but for other object supporting the relevant methods such as [[IQTensor|classes/iqtensor]].

## Complex / Hermitian Conjugation

* `ITensor conj(ITensor T)`

   Returns the complex conjugate of `T`.

* `ITensor dag(ITensor T)`

   Returns the Hermitian conjugate of `T`. Equivalent to `conj(ITensor)`
   but defined to support generic code acting on either ITensors or IQTensors.


## Prime Level Methods

* `ITensor prime(ITensor T, int inc = 1)` <br/>
  `IQTensor prime(IQTensor T, int inc = 1)` <br/>
  `Tensor prime(Tensor T, int inc = 1)` <br/>

   Return a copy of `T` with prime level of each index of `T` incremented by 1 (or by optional amount `inc`).
   Works for any type `Tensor` supporting the `.prime` method.

* `ITensor noprime(ITensor T)` <br/>
  `IQTensor noprime(IQTensor T)` <br/>
  `Tensor noprime(Tensor T)` <br/>

   Return a copy of `T` with prime level of each index set to zero.
   Works for any type `Tensor` supporting the `.noprime` method.

* `ITensor swapPrime(ITensor T, int plev1, int plev2)` <br/>
  `IQTensor swapPrime(IQTensor T, int plev1, int plev2)` <br/>
  `Tensor swapPrime(Tensor T, int plev1, int plev2)` <br/>

   Return a copy of `T` with all indices having prime level `plev1` set to prime level `plev2`
   and all indices with prime level `plev2` set to `plev1`.
   Works for any type `Tensor` supporting the `.mapprime` method.

## Index Inspection Methods

* `Index commonIndex(ITensor A, ITensor B, IndexType type = All)`  <br/>
  `IQIndex commonIndex(IQTensor A, IQTensor B, IndexType t = All)` <br/>
  `TensorA::IndexT commonIndex(TensorA A, TensorB B, IndexType t = All)` 

   Return the index shared by tensors A and B. Optionally, only return the common index if it is of type `t`.
   If A and B have more than one index in common, the return value will be an arbitrary one of these (depending
   on how A was constructed). If A and B have no indices in common, throws an ITError exception. (On develop branch
   now returns a Null index in this case.)

   See also `uniqueIndex`.

   Works for any types `TensorA` and `TensorB` defining `TensorA::IndexT` and exposing an IndexSet through the .indices() accessor.

* `Index findtype(ITensor T, IndexType t)` <br/>
  `IQIndex findtype(IQTensor T, IndexType t)` <br/>
  `Tensor::IndexT findtype(Tensor T, IndexType t)`

   Return the index of tensor T having type `t`. If T has more than one index of type `t`, returns an arbitrary one of these
   depending on how T was constructed.

   Works for any type `Tensor` defining `Tensor::IndexT` and exposing an IndexSet through the `.indices()` accessor.

* `bool hasindex(ITensor T, Index i)` <br/>
  `bool hasindex(IQTensor T, IQIndex i)` <br/>
  `bool hasindex(Tensor T, Tensor::IndexT i)`

   Return `true` if T has the index i.

   Works for any type `Tensor` defining `Tensor::IndexT` and exposing an IndexSet through the `.indices()` accessor.

* `Index uniqueIndex(ITensor A, ITensor B, IndexType type = All)`  <br/>
  `IQIndex uniqueIndex(IQTensor A, IQTensor B, IndexType t = All)` <br/>
  `TensorA::IndexT uniqueIndex(TensorA A, TensorB B, IndexType t = All)` 

   Return the index belonging to A but not to B. Optionally, only return the unique index of type `t`.
   If A has more than one index not belonging to B, the return value will be an arbitrary one of these (depending
   on how A was constructed). If A has no unique indices relative to B, returns a Null index.

   See also `commonIndex`.

   Works for any types `TensorA` and `TensorB` defining `TensorA::IndexT` and exposing an IndexSet through the .indices() accessor.

## Other Methods

* `Real Dot(ITensor x, ITensor y)`

   Compute `x*y` and return the real scalar resulting from this contraction. 
   Throws an `ITError` if the contraction does not yield a real, scalar ITensor.

* `Complex BraKet(ITensor x, ITensor y)`

   Compute `dag(x)*y` and return the complex scalar resulting from this contraction.
   Throws an `ITError` if the contraction does not yield a scalar ITensor.


* `ITensor multSiteOps(ITensor A, ITensor B)` <br/>
  `IQTensor multSiteOps(IQTensor A, IQTensor B)` <br/>
  `Tensor multSiteOps(Tensor A, Tensor B)`

   Compute the product of two operator-like tensors `A` and `B`. An operator-like tensor 
   is a tensor having some number of `Site` type indices `s1`, `s2`, ... with prime level zero and also
   these same indices with prime level one. (An example would be an ITensor declared as `ITensor Op(s,prime(s))`.)

   The return value `R` produced by this function could be equivalently produced by the following code:

       Tensor R = prime(A,Site)*B;
       R.mapprime(2,1,Site);

   Works for any type `Tensor` supporting the methods `.prime` and `.mapprime`.

* `ITensor imagPart(ITensor T)` <br/>
  `IQTensor imagPart(IQTensor T)` <br/>
  `Tensor imagPart(Tensor T)`

   Return the imaginary part of tensor `T`. Works for any type `Tensor` providing the `.takeImagPart()` method.

* `ITensor realPart(ITensor T)` <br/>
  `IQTensor realPart(IQTensor T)` <br/>
  `Tensor realPart(Tensor T)`

   Return the real part of tensor `T`. Works for any type `Tensor` providing the `.takeRealPart()` method.

* `Real sumels(ITensor T)`

   Returns the sum of all elements of T.


[[Back to Classes|classes]]

[[Back to Main|main]]

