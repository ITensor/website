# Index #

An Index represents a single tensor index with fixed dimension. 
Copies of an Index compare equal unless
their _prime levels_ and _tags_ are set to different values.

An Index carries a TagSet, a set of _tags_ which are small strings that specify properties of the Index to help distinguish it from other Indices.

Internally, an Index has a fixed id number, which is how the ITensor library knows two indices are copies of a single original Index. Index objects must have the same id, as well as the same prime level and tags to compare equal.

Index is defined in "itensor/index.h".

## Synopsis ##

    auto i = Index(4);
    Print(dim(i)); //prints: dim(i) = 4

    //Copies of the same Index compare equal
    auto ii = i; //ii is a copy of i
    Print(ii == i); //prints: true

    //The prime level of an Index can be
    //adjusted to make it distinct
    ii.prime(2);
    Print(primeLevel(ii)); //prints: primeLevel(ii) = 2
    Print(ii == i); //prints: false

    ii.noPrime();
    Print(ii == i); //prints: true

    // Index objects can also hold a set of up to four tags
    auto j = Index(5,"j,Link");
    Print(hasTags(j,"j")); //prints: true

    // Tags can be added to or removed from an index
    // Indices must have the same tags to compare equal
    auto ia = addTags(i,"a");
    Print(ia == i); //prints: false

    Print(removeTags(ia,"a") == i); //prints: true

    auto iab = addTags(ia,"b");

    Print(tags(i)); //prints: ""
    Print(tags(ia)); //prints: "a"
    Print(tags(iab)); //prints: "a,b"

    Print(hasTags(iab,"b,a")); //prints: true

## Constructors ##

* `Index()`

  Default constructor. A default-constructed Index evaluates to false in a boolean context.

  <div class="example_clicker">Click to Show Example</div>

        auto i = Index();
        if(!i) println("Index i is default constructed.");

* `Index(int dim, TagSet tags)` 

   Construct an Index with the following fields:
   - The integer `dim` is the size of the Index (the dimension of the vector space that
     the Index defines).
   - The TagSet `tags` is a comma seperated string listing the tags for the Index.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2 with tags "Site" and "s3"
      auto s1 = Index(2,"Site,s3");


## Accessor Methods ##

* `dim(Index i) -> long` 

  Return the index dimension.

* `tags(Index i) -> TagSet`

  Return all of the tags of this Index as a TagSet. This includes
  the integer tag (prime level).

* `primeLevel(Index i) -> int` 

  Return the value of the integer tag, referred to as the prime level.

* `id(Index i) -> id_type`

  The unique id number of this Index (returned as a string)

## Tag functions ##

* `addTags(Index I, TagSet tags) -> Index`

  `.addTags(TagSet tags)`

   Modify the TagSet of the Index, adding the specified tags.

   Note that every Index has one and only one integer tag, so an Integer 
   tag cannot be added.

* `removeTags(Index I, TagSet tags) -> Index`

  `.removeTags(TagSet tags)`

   Modify the TagSet of the Index, removing the specified tags.

   Note that every Index has one and only one integer tag, so an Integer 
   tag cannot be removed.

* `setTags(Index I, TagSet tags) -> Index`

  `.setTags(TagSet tags)`

   Modify the TagSet of the Index, removing all of the tags and setting
   them to the specified tags.

   If no integer tag is specified, the integer tag is set to 0.

* `noTags(Index I) -> Index`

  `.noTags()`

   Remove all tags from an Index and set the integer tag to 0.
   
   `noTags(I)` is the same as `setTags(I,"")` or `setTags(I,"0")`.

* `replaceTags(Index I, TagSet oldtags, TagSet newtags) -> Index`

  `.replaceTags(TagSet oldtags, TagSet newtags)`

   Modify the TagSet of the Index, removing the tags `oldtags` and adding
   the tags `newtags`.

   Note that an integer tag must be replaced by another integer tag. If not
   integer tag is specified, it is not modified.

* `prime(Index I, int inc = 1) -> Index`

  `.prime(int inc = 1)`

  Convenience function to increment the integer tag of the Index by 1. (Optionally, increment by amount `inc`.)

* `setPrime(Index I, int `plev`) -> Index`

  `.setPrime(int plev)`

  Convenience function to set the integer tag of the Index to `plev`.

* `noPrime(Index I) -> Index`

  `.noPrime()`

  Convenience function to set the integer tag of the Index to zero. `noPrime(I)` is the same as `setPrime(I,0)`.

## Index properties ##

* `hasTags(Index I, TagSet tags) -> bool`

   Check if the Index `I` has a TagSet that contains the TagSet `tags`.

* `dag(Index I) -> Index`

  `.dag()`

  Change the arrow direction of the Index. 
  Only relevant for [[Indices with QN data|classes/index_qn]].

* `dir(Index) -> Arrow` 

  Return the `Arrow` direction of this Index. 
  Only relevant for [[Indices with QN data|classes/index_qn]].
  Always returns `Out` if the Index has no QN data.

## Operators and Conversions ##

* `operator=(int val) -> IndexVal`

  `operator()(int val) -> IndexVal`  

  Return an [[IndexVal|classes/indexval]] representing this Index set to value `val`.
  This method is one-indexed, meaning `val` can run from 1 to `dim(i)` for Index `i`.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(10);

      auto iv = i=2; // Call the operator= method of Index i
      //auto iv = i(2);  // This creates the same IndexVal

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

* `explicit operator int()`

  `explicit operator long()`

  `explicit operator size_t()`

  Enables Index objects to be explicitly converting to various integer types.
  The resulting integer is the size of the Index.


## Reading and Writing ##

* `.write(std::ostream& s)`  

  Write Index to stream in binary form.

* `.read(std::istream s)`  

  Read Index from stream in binary form.

## Other Functions ##

* `showDim(Index I) -> string`

   Returns a string version of the dimension of Index I.

<br/>
_This page current as of version 3.0.0_
