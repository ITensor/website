# IQIndexVal #

IQIndexVal conceptually represents an [[IQIndex|classes/iqindex]] fixed to a specific value.

An IQIndexVal holds both an IQIndex `.index` and 
an integer `.val` representing a particular value the IQIndex can take.
The value is 1-indexed and must be in the range [1,m] where m is the size
of the IQIndex.

IQIndexVals correspond to a specific block of their associated IQIndex. 
Consider an IQIndexVal `iv` associated with an IQIndex `I` having
two blocks, both of size 8. If `iv.val <= 8`
it corresponds to the first block of `I`. If `iv.val > 8`
it corresponds to the second block of `I`.

## Synopsis ##

    auto I = IQIndex("I",Index("I+1",8),QN(+1),
                         Index("I-1",8),QN(-1));

    auto iv = IQIndexVal(I,9);

    Print(iv.index == I); //prints: true
    Print(iv.val == 9);   //prints: true

    Print(iv.qn()); //prints: QN(-1)

## Public Data Members

* `IQIndex index`

* `long val`

## Class Methods

* `IQIndexVal(IQIndex I, long val)`

  Constructor taking an IQIndex `I` and value `val`.<br/>
  After constructing an IQIndexVal `iv`, the data members <br/>
  `iv.index == I` and `iv.val == val`.

* `.qn() -> QN`

  Return the quantum number of the block corresponding to
  this IQIndexVal.

* `.indexqn() -> IndexQN`

  Return an IndexQN whose Index and QN are those 
  of the block corresponding to this IQIndexVal.

* `explicit operator IndexVal()`

  Explicit cast IQIndexVal to IndexVal. The resulting IndexVal has the property:
  * `.index` is the result of casting the IQIndexVal's IQIndex to just an Index
  * `.val` is unchanged

  Conceptually this cast views the associated IQIndex as just an Index, ignoring its
  block structure.

* `.blockIndexVal() -> IndexVal`

  Return an IndexVal with the following properties:
  * `.index` is the _block index_ corresponding to the block of the IQIndexVal
  * `.val` is the _relative offset_ within the block of the IQIndexVal

  For example, if an IQIndexVal has value 11, then if the IQIndex is such that
  the first block has size 3; second block has size 6; and third block 3 has size 8; 
  then the IQIndexVal falls inside (corresponds to) the third block, and has relative offset 2 (=11-6-3).

* `.dag()`

  Reverse the Arrow direction of the `.index` field of this IQIndexVal.

* `.prime(IndexType type, int inc = 1)`

  Increment the primelevel of `.index` if its IndexType matches `type` by 1, or by an optional amount `inc`.

* `.noprime(IndexType type = All)`

  Set the primelevel of `.index` to zero (optionally only if its IndexType matches `type`).

* `.mapprime(int plevold, int plevnew, IndexType type = All)`

  If the primelevel of `.index` is `plevold`, change it to `plevnew` (optionally only if its IndexType matches `type`).

## Other IQIndexVal Features

* IQIndexVals are default constructible.

* IQIndexVals compare equal if both their `.index` and `.val` members are equal.

* IQIndexVals can be compared to an IQIndex, in which case only the `.index` field is used.


## IQIndexVal Functions

* `dag(IQIndexVal iv) -> IQIndexVal`

  Return a copy of the IQIndexVal with the Arrow direction of its `.index` reversed.

* `prime(IQIndexVal iv, IndexType type, int inc = 1) -> IQIndexVal`

  Return a copy of the IQIndexVal `iv`, incrementing 
  the primelevel of its `.index` field if its IndexType matches `type` by 1, or by an optional amount `inc`.

* `noprime(IQIndexVal iv, IndexType type = All) -> IQIndexVal`

  Return a copy of the IQIndexVal `iv`, setting the primelevel of its `.index` field to zero (optionally only if its IndexType matches `type`).

* `mapprime(IQIndexVal iv, int plevold, int plevnew, IndexType type = All) -> IQIndexVal`

  Return a copy of the IQIndexVal `iv` such that if the primelevel of its `.index` field is `plevold`, it is changed to `plevnew` (optionally only if its IndexType matches `type`).

<br/>
_This page current as of version 2.0.3_
