# Index #

An Index represents a single tensor index with fixed size m. Copies of an Index compare equal unless
their "prime levels" are set to different values.

An Index has a name just for printing purposes, and an Index
carries an IndexType label (typically `Site` or `Link`&mdash;see [[index conventions|itensor_conventions]]).

## Synopsis ##

    auto i = Index("index i",4);
    Print(i.m()); //prints i.m() = 4

    //Copies of the same Index compare equal
    auto ii = i; //ii is a copy of i
    Print(ii == i); //prints "true"

    //The prime level of an Index can be
    //adjusted to make it distinct
    ii.prime(2);
    Print(ii.primeLevel()); //prints ii.primeLevel() = 2
    Print(ii == i); //prints "false"

    ii.noprime();
    Print(ii == i); //prints "true"


## Constructors ##

* `Index()`

  Default constructor. A default-constructed Index evaluates to false in a boolean context.

  <div class="example_clicker">Click to Show Example</div>

        auto i = Index();
        if(!i) println("Index i is default constructed.");

* `Index(string name, int m, IndexType it = Link, int primelevel = 0)` 

   Construct an Index with the following fields:
   - The name is just for printing purposes. 
   - The integer m is the size of the Index. 
   - The IndexType defaults to `Link`
     but can be set to other values to make it easier to manipulate
     only certain types of indices. 
   - The prime level is an integer
     which can be used to distinguish different copies of 
     the same original Index.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index("Site 1",2,Site);


## Accessor Methods ##

* `.m() -> long` 

  Return the index size.

* `.primeLevel() -> int` 

  Return the prime level.

* `.primeLevel(int n)`  

  Set prime level to n.

* `.type() -> IndexType`  

  Return the `IndexType` of this Index. The [[IndexType|classes/indextype]] is a tag used to distinguish 
  different types of indices to make adjusting their prime levels more convenient.

* `.name() -> string` 

  Return the name of this Index, with prime level information included at the end.

* `.rawname() -> string`  

  Return the name of this Index without prime level information.

* `.id() -> id_type`

  The unique id number of this Index (returned as a string)

## Prime Level Class Methods ##

* `.prime(int inc = 1)`  

  Increment prime level of this Index instance. (Optionally, increment by amount `inc`.)

* `.prime(IndexType type, int inc = 1)`  

  Increment prime level if Index type() matches type. (Optionally, increment by amount `inc`.)

* `.noprime(IndexType type = All)`  

  Reset prime level to zero. (Optionally, only if `type()==type` or `type` is `All`.)

* `.mapprime(int plevold, int plevnew, IndexType type = All)`  

  If Index has prime level plevold, change to plevnew. Otherwise has no effect. 
  (Optionally, map prime level only if `type()==type` or `type` is `All`.)

## Operators and Conversions

* `operator()(int i) -> IndexVal`  

  Return an [[IndexVal|classes/indexval]] representing this Index set to value i.
  This method is one-indexed, meaning i can run from 1 to m().

  <div class="example_clicker">Click to Show Example</div>

      auto I = Index("My Index",10);

      IndexVal iv = I(2); //call Index mi's operator() method

      Print(iv.i); //prints 2
      Print(iv == I); //prints true

* `operator bool()`

  An Index evaluates to `true` in a boolean context if it is 
  constructed (a default constructed Index evalues to `false`).

* `operator==(Index other) -> bool`  

  `operator!=(Index other) -> bool`  

  Comparison operators: two Index objects are equal if they are copies of the 
  same original Index (have the same id) and have the same prime level.

  The name, size, and IndexType of Index objects play no explicit role in comparing them. (Of course,
  all Index objects which compare equal will have the same name, size, and IndexType since they 
  are all copies of the same original Index.) Creating a new Index "i2" with the same name, size,
  and IndexType as another Index "i1" does not mean that i2==i1, since i2 will have a different 
  id number.

* `operator<(Index other) -> bool`  

  Defines an ordering of Index objects &mdash; useful for sorting and finding Index instances in collections.

* `.noprimeEquals(Index other) -> bool`  

  Return `true` if this Index and other are copies of the same original Index, regardless of prime level.

* `explicit operator int()`

  `explicit operator long()`

  `explicit operator size_t()`

  Enables Index objects to be explicitly converting to various integer types.
  The resulting integer is the size of the Index.


## Other Index Class Methods ##

* `.write(std::ostream& s)`  

  Write Index to stream in binary form.

* `.read(std::istream s)`  

  Read Index from stream in binary form.

* `.dag()`  

  Has no effect. Currently only for interface compatibility with [[IQIndex|classes/iqindex]].

* `.dir() -> Arrow` 

  Return the `Arrow` direction of this Index. Always returns `Out`. 
  Currently only for interface compatibility with [[IQIndex|classes/iqindex]].

## Prime Level Functions

* `prime(Index I, int inc = 1) -> Index` 

   Return a copy of  `I` with prime level increased by 1 (or optional amount `inc`).

* `prime(Index I, IndexType type, int inc = 1) -> Index` 

   Return a copy of  `I` with prime level increased by 1 (or `inc`) if `I.type()` equals specified type.

* `noprime(Index I, IndexType type = All) -> Index` 

   Return a copy of `I` with prime level set to zero (optionally only if `I.type()` matches type).

* `mapprime(Index I, int plevold, int plevnew, IndexType type = All) -> Index` 

   Return a copy of `I` with prime level plevnew if `I.primeLevel()==plevold`. Otherwise has no effect.
   (Optionally, only map prime level if type of `I` matches specified type.)

## Other Functions

* `showm(Index I) -> string`

   Returns a string version of the size of Index I.

<br/>
_This page current as of version 2.0.3_
