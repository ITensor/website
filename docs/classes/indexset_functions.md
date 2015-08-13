# IndexSet Functions #

Free functions for working with [[IndexSet|classes/indexset]] objects. All methods below are templated over the index type IndexT.

* `bool hasindex(IndexSet<IndexT> is, IndexT I)`

   Return `true` if index `I` is contained the in the IndexSet `is`, otherwise `false`.

* `bool hastype(IndexSet<IndexT> is, IndexType t)`

   Return `true` if the IndexSet `is` contains an index of IndexType `t`, otherwise `false`.

* `int findindex(IndexSet<IndexT> is, IndexT I)` 

   Return the integer j such that `is[j]==I`. If I is not found, throws an ITError exception.

* `IndexT findtype(IndexSet<IndexT> is, IndexType t)`

   Return the first index in the IndexSet `is` having type `t`. If no indices have type `t`, throws an ITError exception.

* `Arrow dir(IndexSet<IndexT> is, IndexT I)` 

   Return the Arrow direction of the index I contained in the IndexSet `is`. If index I is not found, throws an ITError exception.

* `IndexT finddir(IndexSet<IndexT> is, Arrow dir)` 

   Return the first index in the IndexSet `is` having the direction dir. If no indices have direction dir, throws an ITError exception.

* `int minM(IndexSet<IndexT> is)`

   Return the smallest bond dimension of the indices contained in IndexSet `is`.

* `int maxM(IndexSet<IndexT> is)`

   Return the largest bond dimension of the indices contained in IndexSet `is`.

