## IndexSet

Container for storing indices. 

IndexSet is defined in "itensor/indexset.h". Also see "itensor/indexset_impl.h".
An IndexSet is a subclass of Range which is defined in "itensor/tensor/range.h".

## Synopsis ##

    //Make some indices
    auto b1 = Index(5);
    auto b3 = Index(8);
    auto s2 = Index(2,"Site"); 
    auto s3 = Index(2,"Site");

    auto inds = IndexSet(b1,b3,s2,s3);

    //Print all the indices
    for(auto& i : inds) println(i);

    //Or just print the whole set at once
    println("inds = ",inds);

    Print(order(inds)); //prints 4

## Constructors ##

* `IndexSet()` 

   Default constructor. For a default-constructed IndexSet "inds", `order(inds) == 0`.

* `IndexSet(Index i1,Index i2,Index i3,...)`

   Constructor taking any number of Index objects.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site"), 
      auto s2 = Index(2,"Site");
      auto inds = IndexSet(s1,s2);

* `IndexSet(IndxContainer C)` 

  `IndexSet(std::vector<Index> ii)`

  `IndexSet(std::array<Index> ii)`

  `IndexSet(std::initializer_list<Index> ii)` 

   Constructors accepting various containers of indices.

   Functions defined to accept an input `IndexSet` will also accept
   `std::vector<Index>`, `std::array<Index>`, and `std::initializer_list<Index>`.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("Site 1",2,"Site"), 
      auto s2 = Index("Site 2",2,"Site");
      auto vinds = std::vector<Index>(2);
      vinds[0] = s1;
      vinds[1] = s2;
      auto inds = IndexSet(vinds);

      Print(inds == IndexSet({s1,s2})); //prints: true

* `IndexSet(storage_type && store)` 

   Constructor which "moves" indices from an IndexSet storage container.
   This is the most efficient way to construct an IndexSet other than
   explicitly providing all of the indices in a single constructor call.
   Useful when you want to build an IndexSet in a loop.

   The type `storage_type` is guaranteed to have the same interface
   as a std::vector.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site,s=1"), 
      auto s2 = Index(2,"Site,s=2");
      auto store = IndexSet::storage_type(2);
      store[0] = s1;
      store[1] = s2;
      auto inds = IndexSet(std::move(store));


## Accessor Methods ##

* `order(IndexSet is) -> long`

   Return number of indices in this set.

* `operator[](int j) -> Index&`

   Access the jth index in the set, starting from 0.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("s1",2,"Site");
      auto l = Index("l",10);
      auto a = Index("a",1);

      auto inds = IndexSet(s1,a,l);

      //Access indices
      Print(inds[0]); //prints: (2,"Site")
      Print(inds[1]); //prints: (1,"Link")
      Print(inds[2]); //prints: (10,"Link")

      //Modify an Index
      auto i = Index(3);
      inds[0] = i;
      Print(inds[0]); //prints: (3,"Link")

* `.index(int j) -> Index&`

  `index(IndexSet I, int j) -> Index`

   Access the jth index in the set, starting from 1.

<a name="tag_methods"></a>
## Index Tag Methods

* `.setTags(TagSet tsnew, ...)`
  
  `setTags(IndexSet is, TagSet tsnew, ...) -> IndexSet`

  Set the tags of the indices in this IndexSet to be exactly those in the TagSet `tsnew`.

  Optionally, only set the tags of the listed indices, or indices
  with the matching tags.

* `.noTags(...)`

  `noTags(TagSet tsnew, ...) -> IndexSet`

  Remove all tags of the indices in this IndexSet.

  Optionally, only remove the tags of the listed indices, or indices
  with the matching tags.

* `.addTags(TagSet tsadd, ...)`

  `addTags(IndexSet is, TagSet tsadd, ...) -> IndexSet`

  Add the tags in TagSet `tsadd` to the existing tags of 
  the indices in this IndexSet.

* `.removeTags(TagSet tsremove, ...)`

  Remove the tags in TagSet `tsremove` from the existing tags of 
  the indices in this IndexSet

* `.replaceTags(TagSet tsold, TagSet tsnew, ...)`
  
  `replaceTags(IndexSet is, TagSet tsold, TagSet tsnew, ...) -> IndexSet`

  For any index containing all of the tags in `tsold`, replace
  these tags with those in `tsnew`. 

  Optionally, only replace the tags of the listed indices, or indices
  with the matching tags.

* `.swapTags(TagSet ts1, TagSet ts2, ...)`
  
  `swapTags(IndexSet is, TagSet ts1, TagSet ts2, ...) -> IndexSet`

  For any index containing all of the tags in `ts1`, replace
  these tags with those in `ts2` and vice versa.

  Optionally, only swap th tags of the listed indices, or indices
  with the matching tags.

* `.prime(int inc = 1, ...)`

  `prime(IndexSet is, int inc = 1, ...) -> IndexSet`

  Increment prime level of all indices by 1, or by the optional amount "inc".

  <div class="example_clicker">Click to Show Example</div>

      auto l1 = Index(2,"l1");
      auto s2 = Index(2,"s2");
      auto s3 = Index(2,"s3");
      auto l3 = Index(2,"l3");

      auto inds = IndexSet(l1,s2,s3,l3);
      Print(inds[1]); //prints: (2|id=456|l1)

      prime(inds,2);
      Print(inds[1]); //prints: (2|id=456|l1)''

*  `.setPrime(int plnew, ...)`

   `setPrime(IndexSet is, int plnew, ...) -> IndexSet`

  Set the prime level of all indices to plnew. Optionally, only set the 
  prime levels of indices containing tags tsmatch

*  `.noPrime(...)`

   `noPrime(IndexSet is, ...) -> IndexSet`

  Set the prime level of all Index objects in the IndexSet to zero.

## Set Operations

*  `findInds(IndexSet is, TagSet tsmatch) -> IndexSet`

   Find all indices containing tags in the specified TagSet.

*  `findIndsExcept(IndexSet is, TagSet tsmatch) -> IndexSet`

   Find all indices not containing tags in the specified TagSet.

*  `findIndex(IndexSet is, TagSet tsmatch) -> Index`

   Find the Index containing tags in the specified TagSet.

   If multiple indices are found, throw an error.
   If none are found, return a default Index (evaluates to false).

*  `hasInds(IndexSet is, IndexSet ismatch) -> bool`

   Return true if the IndexSet has all of the provided indices (if
   `ismatch` is a subset of `is`).

*  `hasIndex(IndexSet is, Index imatch) -> bool`

   Return true if the IndexSet has the provided Index `imatch`.

* `commonInds(IndexSet is1, IndexSet is2) -> IndexSet`

   Return the intersection of the two IndexSets.

* `unionInds(IndexSet is1, IndexSet is2) -> IndexSet`

  `unionInds(std::vector<IndexSet> iss) -> IndexSet`

  `unionInds(Index i, IndexSet is) -> IndexSet`
  
  `unionInds(IndexSet is, Index i) -> IndexSet`

   Return the set union of IndexSets.

* `uniqueInds(IndexSet is1, IndexSet is2) -> IndexSet`

  `uniqueInds(IndexSet is1, std::vector<IndexSet> is2) -> IndexSet`

   Return the indices that are in `is1` but not in `is2` (the set difference).

* `noncommonInds(IndexSet is1, IndexSet is2) -> IndexSet)`

  Return all indices not shared by `is1` and `is2` (the symmetric set difference).

## Other IndexSet Functions

*  `sim(IndexSet is, ...) -> IndexSet`

   Replace all indices by "similar" indices (same tags and dimensions but different id numbers).

   Optionally, provide a list of indices, IndexSet, or TagSet to specify
   a subset of the IndexSet to replace with similar indices.

*  `maxDim(IndexSet is) -> long`

   Return the maximum dimension of all indices in the IndexSet.

*  `minDim(IndexSet is) -> long`

   Return the minimum dimension of all indices in the IndexSet.

## Other Methods and Features

* `.dag()`

  `dag(IndexSet I) -> IndexSet`

  Call the dag() operation (which flips Index arrows) on each index in the set.

* `.swap(IndexSet & other)`

  Efficiently swap the contents of this IndexSet with another.

* One can iterate over an IndexSet in a range-based for loop

  Example:
  
      auto inds = IndexSet(s1,a,l);
      //Iterate over and print each index in the set
      for(auto& I : inds) println(I);

* IndexSets can be printed.

## Advanced Methods

* `.extent(size_type i) -> long`

   Return the extent (size, or dimension) of the ith index; the argument i is 0-indexed.

* `.stride(size_type i) -> size_type`

   Return the stride of the ith index; the argument i is 0-indexed.<br/>
   For a "normal" (unpermuted) IndexSet, the stride of an index is the product
   of the extents of all previous indices.

* `.front() -> Index const&`

   Return the first index in the set.

* `.back() -> Index const&`

   Return the last index in the set.

* `.range() -> parent const&`

   Reference to this IndexSet as its parent type, namely `RangeT<index_type>`
   where `index_type` is Index for IndexSet or IQIndex for IQIndexSet.

<br/>
_This page current as of version 3.0.0_
