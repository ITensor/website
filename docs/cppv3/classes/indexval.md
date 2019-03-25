# IndexVal #

An IndexVal conceptually represents an Index fixed to a specific value.

IndexVal holds both an Index called "`index`" and 
an integer "`val`" representing a particular value the Index can take.
The value is 1-indexed and must be in the range [1,m] where m is the size
of the Index.

IndexVal is defined in "itensor/index.h".

## Synopsis

    auto s1 = Index(4);
    auto iva = IndexVal(s1,3),
    auto ivb = IndexVal(s1,1);
    Print(iva.val); //prints: iva.val = 3
    Print(ivb.val); //prints: ivb.val = 1

    //Can make an IndexVal by "plugging" an
    //integer into an Index
    auto ivc = s1=4; // Same as: auto ivc = s1(4);
    Print(ivc.val); //prints: ivc.val = 4
    Print(ivc.index); //prints: (4)

## Public Data Members ##

* `Index index`

* `long val`

## General Methods

* `IndexVal()`

  Default constructor. A default-constructed IndexVal evaluates to false in a boolean context.

* `IndexVal(Index I, int i)`

  Construct an IndexVal from an Index `I` and integer value `i`.
  The value `i` must be between 1 and `dim(I)`, inclusive.

  An IndexVal can also be constructed from an Index with the operators 
  `operator=(int val) -> IndexVal` and `operator()(int val) -> IndexVal`.

* `dim(IndexVal iv) -> long` 

  Return the dimension of `index`.

* `hasQNs(IndexVal) -> bool`

  Returns true if the Index of the IndexVal has QN information.

* `dag(IndexVal iv) -> IndexVal`

  `.dag()`

  Reverse the Arrow direction of the Index stored within this IndexVal.

* `qn(IndexVal iv) -> QN`

  Return the quantum number QN object associated with the block, or sector, of 
  the Index that the value of this IndexVal falls within.

## Tag Functions

* `addTags(IndexVal iv, TagSet tags) -> IndexVal`

  `.addTags(TagSet tags)`

   Modify the TagSet of `index`, adding the specified tags.

   Note that every Index has one and only one integer tag, so an Integer
   tag cannot be added.

* `removeTags(IndexVal iv, TagSet tags) -> IndexVal`

  `.removeTags(TagSet tags)`

   Modify the TagSet of `index`, removing the specified tags.

   Note that every Index has one and only one integer tag, so an Integer
   tag cannot be removed.

* `setTags(IndexVal iv, TagSet tags) -> IndexVal`

  `.setTags(TagSet tags)`

   Modify the TagSet of `index`, removing all of the tags and setting
   them to the specified tags.

   If no integer tag is specified, the integer tag is set to 0.

* `noTags(IndexVal iv) -> IndexVal`

  `.noTags()`

   Remove all tags from an Index and set the integer tag to 0.

   `noTags(iv)` is the same as `setTags(iv,"")` or `setTags(iv,"0")`.

* `replaceTags(IndexVal iv, TagSet oldtags, TagSet newtags) -> IndexVal`

  `.replaceTags(TagSet oldtags, TagSet newtags)`

   Modify the TagSet of `index`, removing the tags `oldtags` and adding
   the tags `newtags`.

   Note that an integer tag must be replaced by another integer tag. If not
   integer tag is specified, it is not modified.

* `prime(IndexVal iv, int inc = 1) -> IndexVal`

  `.prime(int inc = 1)`

  Convenience function to increment the integer tag of the Index by 1. (Optionally, increment by amount `inc`.)

* `setPrime(IndexVal iv, int `plev`) -> IndexVal`

  `.setPrime(int plev)`

  Convenience function to set the integer tag of `index` to `plev`.

* `noPrime(IndexVal iv) -> IndexVal`

  `.noPrime()`

  Convenience function to set the integer tag of `index` to zero. `noPrime(iv)` is the same as `setPrime(iv,0)`.

## Other Operations With IndexVals

* IndexVals can be compared to each other. They are equal if the have the same Index and value.

* An IndexVal compares equal to an Index objects if its `.index` field matches the Index.

* IndexVals can be printed.


<br/>
_This page current as of version 3.0.0_
