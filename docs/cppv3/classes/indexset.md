## IndexSet

Container for storing indices. IndexSets are ordered lists of Index objects,
but in certain contexts are treated as sets (order independent).

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

* `IndexSet(Index i1, Index i2, Index i3, ...)`
 
  `IndexSet(std::initializer_list<Index> ii)` 

  `IndexSet(std::vector<Index> ii)`

  `IndexSet(std::array<Index,N> ii)`

  `IndexSet(IndxContainer C)` 

  Constructors accepting either lists of Index objects or various containers of indices.

  Note that functions defined to accept an input `IndexSet` will also accept
  `std::vector<Index>`, `std::array<Index,N>`, and `std::initializer_list<Index>`.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site,s=1"), 
      auto s2 = Index(2,"Site,s=2");

      // All of the following construct the same IndexSet:
      auto is1 = IndexSet(s1,s2);

      auto is2 = IndexSet({s1,s2});

      auto vinds = std::vector<Index>({s1,s2});
      auto is3 = IndexSet(vinds);

      Print(equals(is1,is2)); //prints: true
      Print(equals(is1,is3)); //prints: true

* `IndexSet(IndexSet is1, IndexSet is2)`

  `IndexSet(Index i, IndexSet is)`

  `IndexSet(IndexSet is, Index i)`

  Construct an IndexSet from two IndexSets, keeping the ordering of the
  original IndexSets. Alternatively, create an IndexSet be appending or
  prepending a single Index.

  <div class="example_clicker">Click to Show Example</div>

      auto i1 = Index(2,"i1"),
      auto i2 = Index(2,"i2");
      auto i3 = Index(2,"i3");
      auto i4 = Index(2,"i4");

      // All of the following construct the same IndexSet:
      auto is1 = IndexSet({i1,i2},{i3,i4});
      auto is2 = IndexSet({i1,i2,i3},i4);
      auto is3 = IndexSet(i1,{i2,i3,i4});

* `IndexSet(storage_type && store)` 

  Constructor which "moves" indices from an IndexSet storage container.
  This is the most efficient way to construct an IndexSet other than
  explicitly providing all of the indices in a single constructor call.
  Useful when you want to build an IndexSet in a loop.

  The type `storage_type` is guaranteed to have the same interface
  as a std::vector.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site,s=1");
      auto s2 = Index(2,"Site,s=2");
      auto store = IndexSet::storage_type(2);
      store[0] = s1;
      store[1] = s2;
      auto inds = IndexSet(std::move(store));


## Accessor Methods ##

* `order(IndexSet is) -> long`

  `length(IndexSet is) -> long`

  Return the number of indices in the IndexSet.

* `operator()(int j) -> Index&`

  `operator[](int j) -> Index&`

  Access the jth index in the IndexSet. `operator()` is 1-indexed,
  and `operator[]` is 0-indexed.

  <div class="example_clicker">Click to Show Example</div>

      auto s = Index(2,"s");
      auto l = Index(10,"l");
      auto a = Index(1,"a");

      auto inds = IndexSet(s,a,l);

      //Access indices
      Print(inds(1)); //prints: (2|id=321|s)
      Print(inds(2)); //prints: (1|id=231|a)
      Print(inds(3)); //prints: (10|id=943|l)

      //Modify an Index
      auto i = Index(3);
      inds(1) = i;
      Print(inds(1)); //prints: (3|id=542)
      Print(inds[0]); //prints: (3|id=542)

<a name="tag_methods"></a>
## Tag and Prime Methods ##

Note: all of the following functions listed of the form:

  `.f(TagSet, ...)`

  `.f(TagSet, TagSet, ...)`

  `.f(int, ...)`

perform an in-place modification of the IndexSet. `...` stands for 
optional arguments to specify a subset of indices of the IndexSet
to apply the operation `.f()`.

 - If no optional arguments are specified, `.f()` is applied to all
   indices of the input IndexSet.

 - If `...` is a list of indices, an IndexSet, or a collection of indices 
   convertible to an IndexSet, `.f()` is applied to only the specified indices.

 - If `...` is a TagSet, `.f()` is only applied to the indices in the IndexSet 
   containing all tags in the TagSet.

Functions of the form:

  `f(IndexSet, TagSet, ...) -> IndexSet`

  `f(IndexSet, TagSet, TagSet, ...) -> IndexSet`

  `f(IndexSet, int, ...) -> IndexSet`

perform the same operation as the above in-place operations and accept the
same optional arguments, but do not modify the input IndexSet and instead 
return a new, modified IndexSet.

* `.addTags(TagSet tsadd, ...)`

  `addTags(IndexSet is, TagSet tsadd, ...) -> IndexSet`

  Add the tags in TagSet `tsadd` to the existing tags of 
  the indices in this IndexSet.

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

  <div class="example_clicker">Click to Show Example</div>

      auto i1 = Index(2,"i,n=1");
      auto i2 = Index(2,"i,n=2");
      auto i3 = Index(2,"i,n=3");

      auto is = IndexSet(i1,i2,i3);

      auto isx = addTags(is,"x","n=1");

      Print(hasIndex(isx,i1)); //prints: false
      Print(hasIndex(isx,addTags(i1,"x"))); //prints: false
      Print(hasIndex(isx,i2)); //prints: true
      Print(hasIndex(isx,i3)); //prints: true

* `.removeTags(TagSet tsremove, ...)`

  `removeTags(IndexSet is, TagSet tsremove, ...) -> IndexSet`

  Remove the tags in TagSet `tsremove` from the existing tags of 
  the indices in this IndexSet.

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

* `.replaceTags(TagSet tsold, TagSet tsnew, ...)`
  
  `replaceTags(IndexSet is, TagSet tsold, TagSet tsnew, ...) -> IndexSet`

  For any index containing all of the tags in `tsold`, replace
  these tags with those in `tsnew`. 

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

* `.swapTags(TagSet ts1, TagSet ts2, ...)`
  
  `swapTags(IndexSet is, TagSet ts1, TagSet ts2, ...) -> IndexSet`

  For any index containing all of the tags in `ts1`, replace
  these tags with those in `ts2` and vice versa.

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

* `.setTags(TagSet tsnew, ...)`
  
  `setTags(IndexSet is, TagSet tsnew, ...) -> IndexSet`

  Set the tags of the indices in this IndexSet to be exactly those in the TagSet `tsnew`.

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

* `.noTags(...)`

  `noTags(TagSet tsnew, ...) -> IndexSet`

  Remove all tags of the indices in this IndexSet.

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

* `.prime(int inc = 1, ...)`

  `prime(IndexSet is, int inc = 1, ...) -> IndexSet`

  Increment prime level of all indices by 1, or by the optional amount "inc".

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

  <div class="example_clicker">Click to Show Example</div>

      auto i1 = Index(2,"i,n=1");
      auto i2 = Index(2,"i,n=2");
      auto i3 = Index(2,"i,n=3");

      auto is = IndexSet(i1,i2,i3);

      auto isp = prime(is);

      Print(hasIndex(isp,prime(i1))); //prints: true
      Print(hasIndex(isp,prime(i2))); //prints: true
      Print(hasIndex(isp,prime(i3))); //prints: true

      is.prime(2,"n=2");

      Print(hasIndex(is,i1)); //prints: true
      Print(hasIndex(is,prime(i2,2))); //prints: true
      Print(hasIndex(is,i3)); //prints: true

* `.setPrime(int plnew, ...)`

  `setPrime(IndexSet is, int plnew, ...) -> IndexSet`

  Set the prime level of all indices to plnew. Optionally, only set the 
  prime levels of indices containing tags tsmatch

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

* `.noPrime(...)`

  `noPrime(IndexSet is, ...) -> IndexSet`

  Set the prime level of all Index objects in the IndexSet to zero.

  Optionally, only modify the tags of the listed indices, or indices
  with the matching tags, as described at the top of the section.

## Comparison and Set Operations

* `equals(IndexSet is1, IndexSet is2) -> bool`

  Return true if the IndexSets have the same indices in the same order.

  For set equality, use `hasSameInds(IndexSet is1, IndexSet is2) -> bool`.

   <div class="example_clicker">Click to Show Example</div>

       auto i1 = Index(2,"i1");
       auto i2 = Index(2,"i2");

       Print(equals({i1,i2},{i1,i2})); //prints: true
       Print(equals({i1,i2},{i2,i1})); //prints: false

* `findInds(IndexSet is, TagSet tsmatch) -> IndexSet`

  Find all indices containing tags in the specified TagSet.

  <div class="example_clicker">Click to Show Example</div>

      auto i1b = Index(2,"i1,bra");
      auto i2b = Index(2,"i2,bra");
      auto i1k = replaceTags(i1b,"bra","ket");
      auto i2k = replaceTags(i2b,"bra","ket");

      auto is = IndexSet(i1b,i2b,i1k,i2k);

      Print(hasSameInds(findInds(is,"bra"),{i1b,i2b})); //prints: true

* `findIndsExcept(IndexSet is, TagSet tsmatch) -> IndexSet`

  Find all indices not containing tags in the specified TagSet.

* `findIndex(IndexSet is, TagSet tsmatch) -> Index`

  Find the Index containing tags in the specified TagSet.

  If multiple indices are found, throw an error.
  If none are found, return a default Index (evaluates to false).

* `hasInds(IndexSet is, IndexSet ismatch) -> bool`

  Return true if the IndexSet has all of the provided indices (if
  `ismatch` is a subset of `is`).

* `hasIndex(IndexSet is, Index imatch) -> bool`

  Return true if the IndexSet has the provided Index `imatch`.

* `hasSameInds(IndexSet is1, IndexSet is2) -> bool`

  Return true if the IndexSets are the same (have all of the same
  indices, i.e. are equal sets).

  For equality that also checks the indices are in the same order,
  use `equals(IndexSet is1, IndexSet is2) -> bool`.

  <div class="example_clicker">Click to Show Example</div>

      auto i1 = Index(2,"i1");
      auto i2 = Index(2,"i2");

      Print(hasSameInds({i1,i2},{i2,i1})); //prints: true

* `commonInds(IndexSet is1, IndexSet is2) -> IndexSet`

  Return the intersection of the two IndexSets.

* `unionInds(IndexSet is1, IndexSet is2) -> IndexSet`

  `unionInds(std::vector<IndexSet> iss) -> IndexSet`

  `unionInds(Index i, IndexSet is) -> IndexSet`
  
  `unionInds(IndexSet is, Index i) -> IndexSet`

  Return the set union of IndexSets, respecting the current order.

  <div class="example_clicker">Click to Show Example</div>

      auto i1 = Index(2,"i1");
      auto i2 = Index(2,"i2");
      auto i3 = Index(2,"i3");

      Print(equals(unionInds({i1,i2},{i2,i3}),{i1,i2,i3})); //prints: true

* `uniqueInds(IndexSet is1, IndexSet is2) -> IndexSet`

  `uniqueInds(IndexSet is1, std::vector<IndexSet> is2) -> IndexSet`

  Return the indices that are in `is1` but not in `is2` (the set difference).

* `noncommonInds(IndexSet is1, IndexSet is2) -> IndexSet`

  Return all indices not shared by `is1` and `is2` (the symmetric set difference).

## Other IndexSet Methods and Features

* `.dag()`

  `dag(IndexSet I) -> IndexSet`

  Call the dag() operation (which flips Index arrows) on each index in the set.

* `sim(IndexSet is) -> IndexSet`

  `sim(IndexSet is, IndexSet ismatch) -> IndexSet`

  `sim(IndexSet is, TagSet tsmatch) -> IndexSet`

  Replace all indices by "similar" indices (same tags and dimensions but different id numbers).

  Optionally, provide an IndexSet or a TagSet to specify
  a subset of the IndexSet to replace with similar indices.

* `maxDim(IndexSet is) -> long`

  Return the maximum dimension of all indices in the IndexSet.

* `minDim(IndexSet is) -> long`

  Return the minimum dimension of all indices in the IndexSet.

* `.swap(IndexSet & other)`

  Efficiently swap the contents of this IndexSet with another.

* One can iterate over an IndexSet in a range-based for loop, for example:
  
      auto inds = IndexSet(s1,a,l);
      //Iterate over and print each index in the set
      for(auto& I : inds) println(I);

* IndexSets can be printed.

## Range Methods

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

  Reference to this IndexSet as its parent type, namely `RangeT<Index>`.

<br/>
_This page current as of version 3.0.0_
