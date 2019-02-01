# IndexVal #

An IndexVal conceptually represents an Index fixed to a specific value.

IndexVal holds both an Index called "`index`" and 
an integer "`val`" representing a particular value the Index can take.
The value is 1-indexed and must be in the range [1,m] where m is the size
of the Index.

IndexVal is defined in "itensor/index.h".

## Synopsis

    auto s1 = Index("Site 1",4,Site);
    auto iva = IndexVal(s1,3),
    auto ivb = IndexVal(s1,1);
    Print(iva.val); //prints: iva.val = 3
    Print(ivb.val); //prints: ivb.val = 1

    //Can make an IndexVal by "plugging" an
    //integer into an Index
    auto ivc = s1(4);
    Print(ivc.val); //prints: ivc.val = 4
    Print(ivc.index); //prints: ("Site 1",4,Site)

## Public Data Members ##

* `Index index`

* `long val`

## Class Methods

* `IndexVal()`

  Default constructor. A default-constructed IndexVal evaluates to false in a boolean context.

* `IndexVal(Index I, int i)`

  Construct an IndexVal from an Index `I` and integer value `i`.
  The value `i` must be between 1 and `I.m()`, inclusive

* `.m() -> long` 

  Return the bond dimension of the `Index` "index".

* `.prime(int inc = 1)`  

  Increment prime level of `index`. (Optionally, increment by amount `inc`.)

* `.prime(IndexType type, int inc = 1)`  

  Increment prime level of `index` if Index type() matches type. (Optionally, increment by amount `inc`.)

* `.noprime(IndexType type = All)`  

  Reset prime level of `index` to zero. (Optionally, only if `type()==type` or `type` is `All`.)

* `.mapprime(int plevold, int plevnew, IndexType type = All)`  

  If `index` has prime level plevold, change to plevnew. 
  Otherwise has no effect. (Optionally, map prime level only if `type()==type` or `type` is `All`.)

* `.dag()`

  Reverse the Arrow direction of the Index stored within this IndexVal.

* `.qn() -> QN`

  Return the quantum number QN object associated with the block, or sector, of 
  the Index that the value of this IndexVal falls within.


## IndexVal Functions

* `prime(IndexVal, int inc = 1) -> IndexVal`

  Return an IndexVal with the same value but with the prime level of the index incremented by one
  (or by an optional amount `inc`).

* `noPrime(IndexVal) -> IndexVal`

  Return an IndexVal with the same value but with the prime level of the index set to zero.

* `hasQNs(IndexVal) -> bool`

  Returns true if the Index of the IndexVal has QN information.

## Other Operations With IndexVals

* IndexVals can be compared to each other. They are equal if the have the same Index and value.

* An IndexVal compares equal to an Index objects if its `.index` field matches the Index.

* IndexVals can be printed.


<br/>
_This page current as of version 3.0.0_
