# IndexVal #

An IndexVal conceptually represents an Index fixed to a specific value.

IndexVal holds both an Index called "`index`" and 
an integer "`val`" representing a particular value the Index can take.
The value is 1-indexed and must be in the range [1,m] where m is the size
of the Index.

IndexVals are primarily used for getting and setting elements of 
an [[ITensor|classes/itensor]].

IndexVal is defined in "itensor/index.h".

## Synopsis

    auto s1 = Index(4);
    auto iva = IndexVal(s1,3),
    auto ivb = IndexVal(s1,1);
    Print(val(iva)); //prints: val(iva) = 3
    Print(val(ivb)); //prints: val(ivb) = 1

    //Can make an IndexVal by "plugging" an
    //integer into an Index
    auto ivc = s1=4; // Same as: auto ivc = s1(4);
    Print(val(ivc)); //prints: val(ivc) = 4
    Print(index(ivc)); //prints: (4|id=490|s1)

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

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(4,"i");

      // These are all ways to make an IndexVal
      auto iva = IndexVal(i,2); // IndexVal constructor
      auto ivb = i=2; // Call the operator= method of Index i
      auto ivc = i(2);  // This creates the same IndexVal

      Print(iva == ivb); //prints: true
      Print(iva == ivc); //prints: true
      Print(index(ivb) == i); //prints: true

* `dim(IndexVal iv) -> long` 

  Return the dimension of `index`.

* `hasQNs(IndexVal) -> bool`

  Returns true if the Index of the IndexVal has QN information.

* `.dag()`

  `dag(IndexVal iv) -> IndexVal`

  Reverse the Arrow direction of the Index stored within this IndexVal.

* `index(IndexVal iv) -> Index`

  Return the Index of this IndexVal.

* `val(IndexVal iv) -> int`

  Return the value of this IndexVal.

* `qn(IndexVal iv) -> QN`

  Return the quantum number QN object associated with the block, or sector, of 
  the Index that the value of this IndexVal falls within.

## Tag Functions

  IndexVals have the same tagging/priming functions as Index objects.
  Tags of the `index` of the IndexVal are modified, and the `val` is left
  unchanged.
  Please see the __Tag Functions__ section of the [[Index documentation|classes/index]]
  for more information.

  <div class="example_clicker">Click to Show Example</div>

      // Create an Index of dimension 2
      auto i = Index(2,"i");

      // Create an IndexVal
      auto iv = i(1);

      auto iva = addTags(iv,"a");

      Print(index(iva) == addTags(i,"a")); //prints: true

## Other Operations With IndexVals

* IndexVals can be compared to each other. They are equal if the have the same Index and value.

* An IndexVal compares equal to an Index objects if its `.index` field matches the Index.

* IndexVals can be printed.


<br/>
_This page current as of version 3.0.0_
