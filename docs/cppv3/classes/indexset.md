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

    Print(rank(inds)); //prints 4

## Constructors ##

* `IndexSet()` 

   Default constructor. For a default-constructed IndexSet "inds", `rank(inds) == 0`.

* `IndexSet(Index i1,Index i2,Index i3,...)`

   Constructor taking any number of Index objects.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("Site 1",2,Site), 
      auto s2 = Index("Site 2",2,Site);
      auto inds = IndexSet(s1,s2);

* `IndexSet(IndxContainer C)` 

   Constructor accepting a container of indices. <br/>
   The container `C` can be either std::array<Index> or std::vector<Index>.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("Site 1",2,Site), 
      auto s2 = Index("Site 2",2,Site);
      auto vinds = std::vector<Index>(2);
      vinds[0] = s1;
      vinds[1] = s2;
      auto inds = IndexSet(vinds);

* `IndexSet(std::initializer_list<Index> ii)` 

   Constructor accepting an initializer list of indices.

* `IndexSet(storage_type && store)` 

   Constructor which "moves" indices from an IndexSet storage container.
   This is the most efficient way to construct an IndexSet other than
   explicitly providing all of the indices in a single constructor call.
   Useful when you want to build an IndexSet in a loop.

   The type `storage_type` is guaranteed to have the same interface
   as a std::vector.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("Site 1",2,Site), 
      auto s2 = Index("Site 2",2,Site);
      auto store = IndexSet::storage_type(2);
      store[0] = s1;
      store[1] = s2;
      auto inds = IndexSet(std::move(store));


## Accessor Methods ##

* `.r() -> long`

   Return number of indices in this set.

* `.operator[](int j) -> Index&`

   Access the jth index in the set, starting from 0.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("s1",2,Site);
      auto l = Index("l",10);
      auto a = Index("a",1);

      auto inds = IndexSet(s1,a,l);

      //Access indices
      Print(inds[0]); //prints: (s1,2,Site)
      Print(inds[1]); //prints: (a,1,Link)
      Print(inds[2]); //prints: (l,10,Link)

      //Modify an Index
      auto i = Index("i",3);
      inds[0] = i;
      Print(inds[0]); //prints: (i,3,Link)

* `.index(int j) -> Index&`

   Access the jth index in the set, starting from 1.

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

## Other Class Methods and Features

* `.dag()`

  Call the dag() operation (which flips IQIndex arrows) on each index in the set.

* `.swap(IndexSet & other)`

  Efficiently swap the contents of this IndexSet with another.

* One can iterate over an IndexSet in a range-based for loop

  Example:
  
      auto inds = IndexSet(s1,a,l);
      //Iterate over and print each index in the set
      for(auto& I : inds) println(I);

* IndexSets can be printed.

## Index Tag Methods

* ```
  .replaceTags(TagSet tsold, TagSet tsnew)
  ```
  ```
  .replaceTags(TagSet tsold, TagSet tsnew, TagSet tsmatch)
  ```
  ```
  .replaceTags(TagSet tsold, TagSet tsnew, int plmatch)
  ```
  ```
  .replaceTags(TagSet tsold, TagSet tsnew, TagSet tsmatch, int plmatch)
  ```
  ```
  .replaceTags(TagSet tsold, TagSet tsnew, Index imatch)
  ```

  For any index containing all of the tags in `tsold`, replace
  these tags with those in `tsnew`. 

  If a third TagSet `tsmatch` is provided, only do the above
  replacement on indices containing the tags in `tsmatch`.
                
  If the argument `int plmatch`, is provided, only do the tag
  replacement for indices having prime level `plmatch`.
  
  If the argument `Index imatch` is provided, only do the tag
  replacement for the Index `imatch`.

* ```
  .setTags(TagSet tsnew)
  ```
  ```
  .setTags(TagSet tsnew, TagSet tsmatch)
  ```
  ```
  .setTags(TagSet tsnew, int plmatch)
  ```
  ```
  .setTags(TagSet tsnew, TagSet tsmatch, int plmatch)
  ```
  ```
  .setTags(TagSet tsnew, Index imatch)
  ```

  Set the tags of indices to be exactly those in the TagSet `tsnew`.

  Optionally, providing the extra TagSet `tsmatch` applies the above
  change only for indices containing tags in `tsmatch`.

  Optionally, providing `int plmatch` applies the above change only
  for indices with prime level `plmatch`.

  Optionally, providing `Index imatch` applies the above change only
  for the Index `imatch`.

* ```
  .addTags(TagSet tsadd)
  ```
  ```
  .addTags(TagSet tsadd, TagSet tsmatch)
  ```
  ```
  .addTags(TagSet tsadd, int plmatch)
  ```
  ```
  .addTags(TagSet tsadd, TagSet tsmatch, int plmatch)
  ```
  ```
  .addTags(TagSet tsadd, Index imatch)
  ```

  Add the tags in TagSet `tsadd` to the existing tags of 
  the indices in this IndexSet

  Optionally, providing the extra TagSet `tsmatch` applies the above
  change only for indices containing tags in `tsmatch`.

  Optionally, providing `int plmatch` applies the above change only
  for indices with prime level `plmatch`.

  Optionally, providing `Index imatch` applies the above change only
  for the Index `imatch`.

* ```
  .removeTags(TagSet tsremove)
  ```
  ```
  .removeTags(TagSet tsremove, TagSet tsmatch)
  ```
  ```
  .removeTags(TagSet tsremove, int plmatch)
  ```
  ```
  .removeTags(TagSet tsremove, TagSet tsmatch, int plmatch)
  ```
  ```
  .removeTags(TagSet tsremove, Index imatch)
  ```

  Remove the tags in TagSet `tsremove` from the existing tags of 
  the indices in this IndexSet

  Optionally, providing the extra TagSet `tsmatch` applies the above
  change only for indices containing tags in `tsmatch`.

  Optionally, providing `int plmatch` applies the above change only
  for indices with prime level `plmatch`.

  Optionally, providing `Index imatch` applies the above change only
  for the Index `imatch`.


## Prime Level Methods

* `.prime(int inc = 1, TagSet tags = "All")`

  Increment prime level of all indices by 1, or by the optional amount "inc".

  If a TagSet is provided, only prime indices containing tags in this set.

  <div class="example_clicker">Click to Show Example</div>

      auto inds = IndexSet(l1,s2,s3,l3);
      Print(inds[1]); //prints: (2,"l1"|id=456)

      prime(inds,2);
      Print(inds[1]); //prints: (2,"l1"|id=456)''

* `.prime(TagSet tags = "All")`

  Increment prime level of all indices by 1.
  If a TagSet is provided, only prime indices containing tags in this set.

* `.prime(int inc, Index i)`

*  ``` 
   .prime(Index i1, Index i2, ..., 
   ```

  Increment prime level of the Index objects `i1`,`i2`, etc. by 1.


*  ``` 
   .prime(int inc, Index i1, Index i2, ..., 
   ```

  Increment prime level of the Index objects `i1`,`i2`, etc. by an amount `inc`.

*  ``` 
   .setPrime(int plnew, TagSet tags = "All")
   ```

  Set the prime level of all indices to plnew. Optionally, only set the 
  prime levels of indices containing tags tsmatch

*  ``` 
   .setPrime(int plnew, Index i1, Index i2, ...)
   ```

  Set the prime level of the Index's `i1`, `i2` to plnew.

*  ``` 
   .noPrime()
   ```

  Set the prime level of all Index objects in the IndexSet to zero.

*  ``` 
   .noPrime(TagSet tags)
   ```

  Set the prime level of the Index's containing the given `tags` to zero. 

*  ``` 
   .noPrime(Index i1, Index i2, ...)
   ```

  Set the prime level of the Index's `i1`, `i2` to zero.

*  ``` 
   .mapPrime(int plold, int plnew, Tags tags = "All")
   ```

  Set the prime level of indices having level `plold` to the new value `plnew`.
  If a TagSet is provided, only do this mapping on indices containing the given tags.

*  ``` 
   .mapPrime(Index imatch, int plold, int plnew)
   ```

  Set the prime level of Index `imatch` having level `plold` to the new value `plnew`.

*  ``` 
   .swapPrime(int pl1, int pl2, TagSet tags = "All")
   ```

  Set the prime level of any index having level `pl1` to `pl2` and 
  simultanously any index having level `pl2` to `pl1`. 

  Optionally, if a TagSet is provided, only perform this swap on 
  indices containing the provided tags.


## Other IndexSet Functions

*  ``` 
   findIndex(IndexSet is,
             TagSet tsmatch,
             int plmatch = -1) -> Index
   ```

   Find the Index containing tags in the specified TagSet
   and, optionally, matching the specified prime level. 

   This is useful if we know there is an Index
   that contains Tags tsmatch, but don't know the other tags.
   If multiple indices are found, throw an error.
   If none are found, return a default Index (evaluates to false).

*  ``` 
   findIndexExact(IndexSet is,
                  TagSet tsmatch,
                  int plmatch = -1) -> Index
   ```

   Find the Index with a certain TagSet and optional prime level.
   If multiple indices are found, throw an error.
   If none are found, return a default Index (evaluates to false).

*  ``` 
   hasIndex(IndexSet is, Index I) -> bool
   ```

   Return true if the IndexSet has the provided Index.

*  ``` 
   sim(IndexSet & is, TagSet t)
   ```

   Replace all indices containing the tags in `t` by "similar" indices
   (same properties but different id numbers).

*  ``` 
   sim(IndexSet & is, Index I)
   ```

   Replace Index `I` by a "similar" index (same properties but different id number).

*  ``` 
   maxM(IndexSet is) -> long
   ```

   Return the maximum dimension of all indices in the IndexSet.

*  ``` 
   minM(IndexSet is) -> long
   ```

   Return the minimum dimension of all indices in the IndexSet.

<br/>
_This page current as of version 3.0.0_
