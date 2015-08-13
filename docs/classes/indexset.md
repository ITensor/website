# IndexSet<IndexT> #

Container for storing indices, templated over the index type `IndexT`. For example, `IndexT` coud be [[`Index`|classes/index]] or [[`IQIndex`|classes/iqindex]].

Internally, indices are stored as a partially ordered array, with `m!=1` indices preceding `m==1` indices (where `m` is the bond dimension).

## Synopsis ##

    Index b1("bond 1",5), 
          b3("bond 3",8),
          a("trivial link",1),
          s2("Site 2",2,Site), 
          s3("Site 3",2,Site);

    IndexSet<Index> inds(b1,b3,s2,s3,a);

    //Print all the indices
    Foreach(const Index& I, inds)
        {
        println(I);
        }

    //Or just print the whole set at once
    println("inds = ",inds);

    Print(inds.r()); //prints 5
    Print(inds.rn()); //prints 4, only 4 m!=1 indices

## Constructors ##

* `IndexSet()` 

   Default constructor. For a default-constructed IndexSet `inds`, `inds.r() == 0`.

* `IndexSet(IndexT i1)` 

  `IndexSet(IndexT i1, IndexT i2)` 

  `IndexSet(IndexT i1, IndexT i2, IndexT i3)` 

   ... etc. up to 8 indices 

   Construct an IndexSet with the given indices. Indices may be partially reordered from the order given.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site);
        IndexSet<Index> inds(s1,s2);
        Print(T.r()); //Prints 2

## Accessor Methods ##

* `int r()`

   Return number of indices in this set.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              l("Bond index",10,Link);

        IndexSet<Index> inds(s1,l);
        Print(inds.r()); //prints 2

* `int rn()`

   Return number of `m!=1` indices in this set.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              l("Bond index",10,Link),
              a("trivial link",1,Link);

        IndexSet<Index> inds(s1,a,l);
        Print(inds.rn()); //prints 2
        Print(inds.r()); //prints 3

* `IndexT operator[](int j)`

   Return the jth index in the set (zero-indexed such that the first element corresponds to j=0).

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              l("Bond index",10,Link),
              a("trivial link",1,Link);

        IndexSet<Index> inds(s1,a,l);

        Print(inds[0]); //prints s1
        Print(inds[1]); //prints l
        Print(inds[2]); //prints a (last since a.m() == 1)

* `IndexT index(int j)`

   Return the jth index in the set (one-indexed such that the first element corresponds to j=1).

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              l("Bond index",10,Link),
              a("trivial link",1,Link);

        IndexSet<Index> inds(s1,a,l);

        Print(inds.index(1)); //prints s1
        Print(inds.index(2)); //prints l
        Print(inds.index(3)); //prints a (last since a.m() == 1)

* `int dim()`

   Return the total dimension of the set, defined as the product of all index bond dimensions.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              l("Bond index",10,Link),
              a("trivial link",1,Link);

        IndexSet<Index> inds(s1,a,l);
        Print(inds.dim()); //prints 20 == 2*10*1


* `Real uniqueReal()`

   Return the unique Real of the set, defined to be the sum of the unique Reals of all the indices.

## Iteration ##

* `const_iterator begin() const` <br/>
  `const_iterator end() const`

   Return beginning and end iterators.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              l("Bond index",10,Link),
              a("trivial link",1,Link);

        IndexSet<Index> inds(s1,a,l);

        //Iterate over and print each index in the set
        for(IndexSet<Index>::const_iterator it = inds.begin();
            it != inds.end();
            ++it)
            {
            cout << *it < endl;
            }

        //More convenient version using the boost Foreach macro
        Foreach(const Index& I, inds)
            {
            cout << I << endl;
            }

## Prime Level Methods ##

* ` prime(int inc = 1)`

  Increment prime level of all indices by 1. (Optionally by amount `inc`.)

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        IndexSet<Index> inds(l1,s2,s3,l3);

        inds.prime();
        Print(hasindex(inds,prime(s2))); //Prints 1 (true)
        Print(hasindex(inds,s2));         //Prints 0 (false)
        Print(hasindex(inds,prime(s3))); //Prints 1 (true)
        Print(hasindex(inds,prime(l1))); //Prints 1 (true)
        Print(hasindex(inds,prime(l3))); //Prints 1 (true)

* ` prime(IndexT I, int inc = 1)`

  Increment prime level of only index `I` by 1. (Optionally by amount `inc`.)
  Throws an exception of the IndexSet does not have index `I`.

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        IndexSet<Index> inds(l1,s2,s3,l3);

        inds.prime(s3);
        Print(hasindex(inds,prime(s3))); //Prints 1 (true)
        Print(hasindex(inds,s3));         //Prints 0 (false)
        Print(hasindex(inds,prime(s2))); //Prints 0 (false)
        Print(hasindex(inds,prime(l1))); //Prints 0 (false)
        Print(hasindex(inds,prime(l3))); //Prints 0 (false)
        Print(hasindex(inds,s2));         //Prints 1 (true)
        //etc.

* ` prime(IndexType t, int inc = 1)`

  Increment prime level of every index of type `t`. (Optionally by amount `inc`.)

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        IndexSet<Index> inds(l1,s2,s3,l3);

        inds.prime(Site);
        Print(hasindex(inds,prime(s2))); //Prints 1 (true)
        Print(hasindex(inds,s2));         //Prints 0 (false)
        Print(hasindex(inds,prime(s3))); //Prints 1 (true)
        Print(hasindex(inds,l1));         //Prints 1 (true)

* ` noprime(IndexType t = All)`

  Set prime level of all indices to 0. (Optionally only indices of type `t`.)

* ` noprime(IndexT I)`

  Set prime level of index `I` to 0. Throws an exception if the set does not have index `I`.

* ` mapprime(int plevold, int plevnew, IndexType t = All)`

  Change prime level of all indices having prime level `plevold` to `plevnew`. (Optionally only if their type matches `t`.) 

## Other Methods ##

* ` addindex(IndexT I)`

  Add index I to the set. Depending on whether `I.m()==1` or not, will add I to the end of the set or to the end of the `m!=1` indices.

* ` swap(IndexSet& other)`

  Efficiently swap contents of this IndexSet with a different IndexSet `other`.

* ` clear()`

  Reset this IndexSet to the empty set.
