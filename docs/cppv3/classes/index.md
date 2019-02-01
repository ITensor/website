# Index #

An Index represents a single tensor index with fixed size m. Copies of an Index compare equal unless
their _prime levels_ and _tags_ are set to different values.

An Index carries a TagSet, a set of _tags_ which are small strings that specify properties of the Index to help distinguish it from other Indices.

Internally, an Index has a fixed id number, which is how the ITensor library knows two indices are copies of a single original Index. Index objects must have the same id, as well as the same prime level and tags to compare equal.

Index is defined in "itensor/index.h".

## Synopsis ##

    auto i = Index(4);
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

    // Tags can be added or removed to an index
    // Indices must have the same tags to compare equal
    auto ia = addTags(i,"a");
    Print(ia == i); //prints "false"

    Print(removeTags(ia,"a") == i); //prints "true"

    auto iab = addTags(ia,"b");

    Print(i.tags()); //prints ""
    Print(ia.tags()); //prints "a"
    Print(iab.tags()); //prints "a,b"

## Constructors ##

* `Index()`

  Default constructor. A default-constructed Index evaluates to false in a boolean context.

  <div class="example_clicker">Click to Show Example</div>

        auto i = Index();
        if(!i) println("Index i is default constructed.");

* `Index(int m, string tags)` 

   Construct an Index with the following fields:
   - The integer m is the size of the Index. 
   - The string tags is a comma seperated list of tags for the Index.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2 with tags "Site" and "s3"
      auto s1 = Index(2,"Site,s3");


## Accessor Methods ##

* `.m() -> long` 

  Return the index size.

* `.primeLevel() -> int` 

  Return the prime level.

* `.tags() -> TagSet`

  Return the tags of this Index as a TagSet.

* `.id() -> id_type`

  The unique id number of this Index (returned as a string)

## Prime Level Class Methods ##

* `.setPrime(int n)`  

  Set the prime level of this Index to n.

* `.prime(int inc = 1)`  

  Increment prime level of this Index instance. (Optionally, increment by amount `inc`.)

* `.noPrime()`  

  Reset prime level to zero.

## Operators and Conversions

* `operator()(int i) -> IndexVal`  

  Return an [[IndexVal|classes/indexval]] representing this Index set to value i.
  This method is one-indexed, meaning i can run from 1 to m().

  <div class="example_clicker">Click to Show Example</div>

      auto mi = Index(10);

      IndexVal iv = I(2); //call the operator() method of Index mi

      Print(iv.i); //prints 2
      Print(iv == I); //prints true

* `operator bool()`

  An Index evaluates to `true` in a boolean context if it is 
  constructed (a default constructed Index evalues to `false`).

* `operator==(Index other) -> bool`  

  `operator!=(Index other) -> bool`  

  Comparison operators: two Index objects are equal if they are copies of the 
  same original Index (have the same id) and have the same prime level and tags.

  The size of the Index objects play no explicit role in comparing them. (Of course,
  all Index objects which compare equal will have the same size, since they 
  are all copies of the same original Index.) Creating a new Index "i2" with the same size, tags,
  and prime level as another Index "i1" does not mean that i2==i1, since i2 will have a different 
  id number.

* `operator<(Index other) -> bool`  

  Defines an ordering of Index objects &mdash; useful for sorting and finding Index instances in collections.
 
* `equalsIgnorePrime(Index i1, Index i2) -> bool`

  Return `true` if Index i1 and Index i2 are copies of the same original Index and have the same tags,
  regardless of prime level.

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

* `noPrime(Index I) -> Index` 

   Return a copy of `I` with prime level set to zero.

## Tag functions

* `addTags(Index I, string tags) -> Index`

   Return a copy of `I` with `tags` added to the current TagSet.

* `removeTags(Index I, string tags) -> Index`

   Return a copy of `I` with `tags` removed from the current TagSet.

* `setTags(Index I, string tags) -> Index`

   Return a copy of `I` with a new TagSet specified by `tags`.

* `replaceTags(Index I, string newtags, string oldtags)`

   Return a copy of `I` with tags `oldtags` removed and tags `newtags` added.

* `hasTags(Index I, string tags)`

   Check if the Index `I` has a TagSet containing `tags`.

## Other Functions

* `showm(Index I) -> string`

   Returns a string version of the size of Index I.

<br/>
_This page current as of version 3.0.0_
