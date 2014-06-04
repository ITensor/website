# ITensor Functions #

Standalone methods for manipulating objects implementing the [[ITensor|classes/itensor]] interface. 

The following methods are templates, so they work not only for [[ITensor|classes/itensor]] objects
but for other object supporting the relevant methods such as [[IQTensor|classes/iqtensor]].

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

   Works for any type `Tensor` defining `Tensor::IndexT` and exposing an IndexSet through the .indices() accessor.

* `bool hasindex(ITensor T, Index i)` <br/>
  `bool hasindex(IQTensor T, IQIndex i)` <br/>
  `bool hasindex(Tensor T, Tensor::IndexT i)`

   Return `true` if T has the index i.

   Works for any type `Tensor` defining `Tensor::IndexT` and exposing an IndexSet through the .indices() accessor.

* `Index uniqueIndex(ITensor A, ITensor B, IndexType type = All)`  <br/>
  `IQIndex uniqueIndex(IQTensor A, IQTensor B, IndexType t = All)` <br/>
  `TensorA::IndexT uniqueIndex(TensorA A, TensorB B, IndexType t = All)` 

   Return the index belonging to A but not to B. Optionally, only return the unique index of type `t`.
   If A has more than one index not belonging to B, the return value will be an arbitrary one of these (depending
   on how A was constructed). If A has no unique indices relative to B, returns a Null index.

   See also `commonIndex`.

   Works for any types `TensorA` and `TensorB` defining `TensorA::IndexT` and exposing an IndexSet through the .indices() accessor.


[[Back to Classes|classes]]

[[Back to Main|main]]

