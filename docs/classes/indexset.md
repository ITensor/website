## IndexSet (and IQIndexSet)

Container for storing indices. 

The following documentation refers to IndexSet, but also applies to
IQIndexSet, which is implemented using the same template class. 
For IQIndexSet, just replace all usage of the `Index` type with
the type `IQIndex`.

* `IndexSet` is an alias for `IndexSetT<Index>`
* `IQIndexSet` is an alias for `IndexSetT<IQIndex>`


## Synopsis ##

    //Make some indices
    auto b1 = Index("bond 1",5);
    auto b3 = Index("bond 3",8);
    auto s2 = Index("Site 2",2,Site); 
    auto s3 = Index("Site 3",2,Site);

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

## Prime Level Functions

* `prime(IndexSet & is, int inc = 1)`

  Increment prime level of all indices by 1, or by the optional amount "inc".

  <div class="example_clicker">Click to Show Example</div>

      auto inds = IndexSet(l1,s2,s3,l3);
      Print(inds[1]); //prints: (s2,2,Site)

      prime(inds,2);
      Print(inds[1]); //prints: (s2,2,Site)''


* ``` 
  prime(IndexSet & is, 
        Index i1, Index i2, ..., 
        int inc = 1)
  ```

  Increment prime level of the specific indices i1, i2, etc. by 
  1 or by the optional amount `inc`.

  <div class="example_clicker">Click to Show Example</div>

      auto inds = IndexSet(l1,s2,s3,l3);

      //Increment prime level of s2 and s3 by 4
      prime(inds,s2,s3,4);

      Print(inds[1]); //prints: (s2,2,Site)'4

* ``` 
  prime(IndexSet & is, 
        IndexType t1, IndexType t2, ..., 
        int inc = 1)
  ```

  Increment prime level of all indices of the specified IndexTypes
  by 1 or by the optional amount `inc`.

  <div class="example_clicker">Click to Show Example</div>

      auto inds = IndexSet(l1,s2,s3,l3);

      //Increment prime level of all indices of
      //type Site by 5
      prime(inds,Site,5);

      Print(inds[0]); //prints: (l1,1,Link)
      Print(inds[1]); //prints: (s2,2,Site)'5
      Print(inds[2]); //prints: (s3,2,Site)'5
      Print(inds[3]); //prints: (l3,3,Link)

* ``` 
  primeExcept(IndexSet & is, 
              Index i1, Index i2, ..., 
              int inc = 1)
  ```
  ``` 
  primeExcept(IndexSet & is, 
              IndexType t1, IndexType t2, ..., 
              int inc = 1)
  ```

  Increment the prime level of all indices NOT matching the list of
  indices provided (or list of IndexTypes provided) by 1 or the 
  optional amount "inc".


* ` noprime(IndexSet & is)`

  Set prime level of all indices to zero.

* ``` 
  noprime(IndexSet & is, 
          Index i1, Index i2, ...)
  ```
  ``` 
  noprime(IndexSet & is, 
          IndexType t1, IndexType t2, ...)
  ```

  Set prime level all indices listed (or IndexTypes listed) to zero.

* ``` 
  mapprime(IndexSet & is,
           VArgs&&... vargs)
  ```

  Map classes of indices from a current prime level to a new prime level. The arguments
  "vargs" are triples of the form `I,plevold,plevnew` where I is either an Index or an
  IndexType. Any Index matching I that has prime level plevold will have its prime level
  replaced with plevnew.

  <div class="example_clicker">Click to Show Example</div>

      auto b1 = Index("bond 1",5,Link);
      auto b3 = Index("bond 3",8,Link);
      auto s2 = Index("Site 2",2,Site); 
      auto s3 = Index("Site 3",2,Site);

      auto inds = IndexSet(b1,prime(b3,2),s2,s3);

      mapprime(inds,Site,0,4,b3,2,5);

      //Now s2 and s3 will have prime level 4
      //and b3 will have prime level 5

* ``` 
  mapprime(IndexSet & is,
           int plevold, int plevnew, 
           IndexType t = All)
  ```

  Change prime level of all indices having prime level `plevold` to `plevnew`. 
  (Optionally only if their IndexType matches `t`.) 

## Other IndexSet Functions

* `findindex(IndexSet const& inds, Index const& I) -> long`

  Find the position of the Index `I` within the IndexSet `inds`.<br/>
  Returns an integer j such that `inds[j] == I`.<br/>
  If the Index I is not found, returns -1.

* `findtype(IndexSet const& inds, IndexType t) -> Index`

  Finds the first Index in the set whose type matches `t`.

* `finddir(IQIndexSet const& inds, Arrow dir) -> IQIndex`

  Finds the first IQIndex in the set whose arrow direction matches `dir`.

* `dir(IQIndexSet const& inds, IQIndex const& I) -> Arrow`

  Return the arrow direction of the IQIndex `I` as it appears in this IQIndexSet.<br/>
  (Note that arrows are not used for comparing IQIndices, so the argument `I` provided can
  have either direction.)

* `hasindex(IndexSet const& inds, Index const& I) -> bool`

  Return `true` if `inds` contains the Index `I`.

* `hastype(IndexSet const& inds, IndexType t) -> bool`

  Return `true` if `inds` contains an Index of IndexType `t`.

* `minM(IndexSet const& inds) -> long`

  Return the size of the smallest Index in the set.

* `maxM(IndexSet const& inds) -> long`

  Return the size of the largest Index in the set.


<br/>
_This page current as of version 2.0.3_
