# Index #

An Index represents a single tensor index with fixed dimension. 
Copies of an Index compare equal unless their _tags_ are different.

An Index carries a TagSet, a set of _tags_ which are small strings 
that specify properties of the Index to help distinguish it from other Indices.
There is a special tag which is referred to as the _integer tag_ or _prime level_
which can be incremented or decremented with special priming functions.

Internally, an Index has a fixed id number, which is how the ITensor library 
knows two indices are copies of a single original Index. 
Index objects must have the same id, as well as the tags to compare equal.

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
    Print(hasTags(j,"j,Link")); //prints: true

    // Tags can be added to or removed from an index
    // Indices must have the same tags to compare equal

    Print(tags(i)); //prints: 

    auto ia = addTags(i,"a");
    Print(tags(ia)); //prints: a
    Print(ia == i); //prints: false
    Print(removeTags(ia,"a") == i); //prints: true

    auto iab = addTags(ia,"b");
    Print(tags(iab)); //prints: a,b
    Print(hasTags(iab,"b,a")); //prints: true
    Print(removeTags(iab,"b") == ia); //prints: true

    auto iap = prime(ia);
    Print(tags(iap)); //prints: (a)'
    Print(primeLevel(iap) == 1); //prints: true

## Constructors ##

* `Index()`

  Default constructor. A default-constructed Index evaluates to false in a boolean context.

  <div class="example_clicker">Click to Show Example</div>

        auto i = Index();
        if(!i) println("Index i is default constructed.");

* `Index(int dim[, TagSet tags])` 

   Construct an Index. 
   The integer `dim` is the size of the Index (the dimension of the vector space that
   the Index defines).
   An Index is assigned a random id that is used to uniquely determine an Index
   (and indices that are made from copies of that Index).

   Optionally, the TagSet `tags` can be specified as a comma seperated string listing the tags 
   that that the Index will have. If none is specified, the Index will have no tags and the 
   integer tag (prime level) will be set to 0.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto i = Index(2);

      // Create a different Index of dimension 2
      auto j = Index(2);

      Print(i == j); //prints: false (since their ids are different)

      // Create an Index of dimension 3 with tags "Site" and "s1"
      auto s1 = Index(3,"Site,s1");

      // Create an Index with dimension 4, tag "x" and integer tag (prime level) 1
      auto x = Index(4,"x,1");
      
      Print(hasTags(x,"x")); //prints: true
      Print(hasTags(x,"x,1")); //prints: true
      Print(primeLevel(x) == 1); //prints: true
      
      //Not allowed: a TagSet can have only one integer tag (prime level)
      //auto y = Index(4,"1,2");

* `sim(Index i) -> Index`

    Make a new index with all of the same properties as i (dimension, tags, direction,
    and quantum numbers) but with a new id.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto s = Index(2,"s,Site");

      auto t = sim(s);

      Print(s == t); //prints: false
      Print(tags(s) == tags(t)); //prints: true
      Print(dim(s) == dim(t)); //prints: true

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

## Comparison Methods ##

* `operator==(Index other) -> bool`

  `operator!=(Index other) -> bool`

  Comparison operators: two Index objects are equal if they are copies of the
  same original Index (have the same id) and have the same TagSet.

  The size of the Index objects play no explicit role in comparing them. (Of course,
  all Index objects which compare equal will have the same size, since they
  are all copies of the same original Index.)
  Creating a new Index `j` with the same size and TagSet
  as another Index `i` does not mean that `i==j`, since `j` will have a different
  id number.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto i = Index(2);

      // Create a different Index of dimension 2
      auto j = Index(2);

      Print(i == j) // False, since their ids are different

## Tag Methods ##

* `.addTags(TagSet tags)`

  `addTags(Index I, TagSet tags) -> Index`

   Modify the TagSet of the Index, adding the specified tags. The first
   version modifies the Index in-place. The second
   version creates a new Index, keeping the original Index unmodified.

   Note that every Index has one and only one integer tag, so an Integer 
   tag cannot be added.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto i = Index(2,"i");

      auto ia = addTags(i,"a");

      Print(hasTags(ia,"i,a")); //prints: true

* `.removeTags(TagSet tags)`

  `removeTags(Index I, TagSet tags) -> Index`

   Modify the TagSet of the Index, removing the specified tags.

   Note that every Index has one and only one integer tag, so an Integer 
   tag cannot be removed.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto is = Index(2,"i,Site");

      auto i = removeTags(is,"Site");

      Print(hasTags(i,"Site")); //prints: false

* `.replaceTags(TagSet oldtags, TagSet newtags)`

  `replaceTags(Index I, TagSet oldtags, TagSet newtags) -> Index`

   Modify the TagSet of the Index, removing the tags `oldtags` and adding
   the tags `newtags`.

   Note that an integer tag must be replaced by another integer tag. If no
   integer tag is specified, it is not modified.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto is = Index(2,"i,Site");

      auto il = replaceTags(i,"Site","Link");

      Print(hasTags(il,"i,Link")); //prints: true
      Print(tags(il)=="i,Link,0")); //prints: true

* `.setTags(TagSet tags)`

  `setTags(Index I, TagSet tags) -> Index`

   Modify the TagSet of the Index, removing all of the tags and setting
   them to the specified tags.

   If no integer tag is specified, the integer tag is set to 0.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto i = Index(2,"i,1");

      Print(tags(i) == "i,1"); //prints: true

      auto a = setTags(i,"a");

      Print(tags(a) == "a,0"); //prints: true

* `.noTags()`

  `noTags(Index I) -> Index`

   Remove all tags from an Index and set the integer tag to 0.
   
   `noTags(I)` is the same as `setTags(I,"")` or `setTags(I,"0")`.

   For two indices `I` and `J`, `noTags(I) == noTags(J)` if and only 
   if the ids of `I` and `J` are the same.

  <div class="example_clicker">Click to Show Example</div>

      // Create Indices of dimension 2
      auto i = Index(2);
      auto j = Index(2);

      auto xp = prime(addTags(i,"x"));

      Print(noTags(xp) == i); //prints: true
      Print(noTags(xp) == j); //prints: false

* `.prime(int inc = 1)`

  `prime(Index I, int inc = 1) -> Index`

  Convenience function to increment the integer tag (prime level) of the Index by 1.
  (Optionally, increment by amount `inc`.)

* `.setPrime(int plev)`

  `setPrime(Index I, int `plev`) -> Index`

  Convenience function to set the integer tag (prime level) of the Index to `plev`.

* `.noPrime()`

  `noPrime(Index I) -> Index`

  Convenience function to set the integer tag (prime level) of the Index to zero.
  `noPrime(I)` is the same as `setPrime(I,0)`.

## Index properties ##

* `hasTags(Index I, TagSet tags) -> bool`

   Check if the Index `I` has a TagSet that contains the TagSet `tags`.

* `.dag()`

  `dag(Index I) -> Index`

  Change the arrow direction of the Index. 
  Only relevant for [[Indices with QN data|classes/index_qn]].

* `.setDir(Arrow)`

  Set the arrow direction of the Index. 
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

      auto iva = i=2; // Call the operator= method of Index i
      auto ivb = i(2);  // This creates the same IndexVal

      Print(iva == ivb); //prints: true
      Print(val(iva)); //prints: 2
      Print(index(iva) == i); //prints: true

* `operator bool()`

  An Index evaluates to `true` in a boolean context if it is 
  constructed (a default constructed Index evalues to `false`).

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index();
      if(!i) println("Index i is default constructed.");

* `explicit operator int()`

  `explicit operator long()`

  `explicit operator size_t()`

  Enables Index objects to be explicitly converted to various integer types.
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
