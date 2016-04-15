# IQIndex #

## (subclass of [[Index|classes/index]]) ##

An IQIndex is a tensor index with additional structure.
As a subtype of [[Index|classes/index]], an IQIndex has a name, size, type, prime level, and unique id number.
IQIndex also inherits all of the class methods of [[Index|classes/index]].

An IQIndex is also divided into quantum number "blocks". 
Each block is labeled by a [[Index|classes/index]]-[[QN|classes/qn]] pair (an [[IndexQN|classes/indexqn]]), and the size of each 
block is the size of its Index.
The size of an IQIndex is just the total size of all of its blocks.
The number and order of blocks of an IQIndex cannot be changed after the IQIndex is constructed.

For example, the IQIndex representing a single spin 1/2 has total size 2, which is made up of two blocks:
* a spin up block of size 1,
  indicated by a [[QN|classes/qn]](+1) paired with an Index of size 1
* a spin down block of size 1, indicated by a [[QN|classes/qn]](-1) paired with an Index of size 1

An IQIndex also has a direction, which is of type `Arrow`. An Arrow can be `In` or `Out`, 
and the default for an IQIndex is `Out`. <br/>
For more information on Arrows, see the page on [[index conventions|itensor_conventions]].

## Synopsis ##

    // Make an IQIndex with five blocks
    // and total size 4+8+10+8+4=34
    auto I = IQIndex("I",Index("I+2",4),QN(+2),
                         Index("I+1",8),QN(+1),
                         Index("I_0",10),QN(0),
                         Index("I-1",8),QN(-1),
                         Index("I-2",4),QN(-2));

    Print(I.m()); //prints: I.m() = 34

    //Get number of blocks of I
    Print(I.nblock()); //prints: I.nblock() = 5

    //Get Index and QN of block 2
    Print(I.index(2)); //prints: (I+1,8,Link)
    Print(I.qn(2));    //prints: QN(+1)

    //Get direction of I
    Print(I.dir()); //prints: I.dir() = Out

## Class Methods (only showing those not inherited from [[Index|classes/index]])

* ```
  IQIndex(string name, 
          Index i1, QN q1, 
          Index i2, QN q2, 
          ...,
          Arrow dir = Out)`
  ```

  Construct an IQIndex with the given name and blocks corresponding to the Index-QN
  pairs provided.<br/>
  Optionally, the last argument can be an Arrow direction, which defaults to `Out`.

  <div class="example_clicker">Click to Show Example</div>

      auto I = IQIndex("I",Index("I+2",4),QN(+2),
                           Index("I+1",8),QN(+1),
                           Index("I_0",10),QN(0),
                           Index("I-1",8),QN(-1),
                           Index("I-2",4),QN(-2));

* ```
  IQIndex(std::string name, 
          std::vector<IndexQN> && iq, 
          Arrow dir = Out, 
          int plev = 0)
  ```

  Construct an IQIndex with the following attributes:
  * `name` is the name of the IQIndex
  * `iq` is a std::vector&lt;[[IndexQN|classes/indexqn]]&gt; which defines the blocks, in order, of the IQIndex.
    `iq` is an rvalue and its contents will be moved into the IQIndex.
  * Optional `dir` specifying the direction of the IQIndex 
  * Optional `plev` specifying the prime level of the IQIndex 

  For more information on the [[IndexQN|classes/indexqn]] class, [[click here|classes/indexqn]].

  <div class="example_clicker">Click to Show Example</div>

      auto v = stdx::reserve_vector<IndexQN>(5);
      v.emplace_back(Index("I+2",4),QN(+2));
      v.emplace_back(Index("I+1",8),QN(+1));
      v.emplace_back(Index("I_0",10),QN(0));
      v.emplace_back(Index("I-1",8),QN(-1));
      v.emplace_back(Index("I-2",4),QN(-2));

      auto I = IQIndex("I",std::move(v),Out,0);

* `.nblock() -> long`<br/>
  `.nindex() -> long`

  Return the number of blocks of this IQIndex. <br/>
  (`.nindex()` is just an alternative name for
  backwards compatibility reasons.)<br/>

* `.index(int i) -> Index`

  Return the Index of the nth block of this IQIndex. <br/>
  n is 1-indexed.

* `.operator[](int n) -> Index`

  Return the Index of the nth block of this IQIndex. <br/>
  n is 0-indexed.

* `qn(int n) -> QN`

  Return the QN of the nth block of this IQIndex.

* `dir() -> Arrow`

  Return the Arrow direction of this IQIndex. Can be `In` or `Out`. <br/>
  For more information see the [[index conventions|itensor_conventions]] page.

* `.operator()(int n) -> IQIndexVal`

  Return the [[IQIndexVal|classes/iqindexval]] representing this IQIndex set to a specific value "n". <br/>
  For an IQIndex `I`, n can range from [1,m] where m is the size of `I`.

* `.dag()`

  Reverse the arrow of this IQIndex.

## Other Features of IQIndex

* An IQIndex supports iteration, for example

      for(auto& iq : I)
        {
        println(iq.index);
        println(iq.qn);
        }

  IQIndex iterators are read-only and dereference to [[IndexQN|classes/indexqn]]'s.

* An IQIndex `I` can be read to and written from disk by calling
  `I.read(s)` and `I.write(s)` where `s` is a stream object.

## IQIndex Functions

* `dag(IQIndex I) -> IQIndex`

  Return a copy of `I` with its arrow direction reversed.

* `hasindex(IQIndex I, Index j) -> bool`

  Return `true` if the Index `j` labels one of the blocks of the IQIndex `I`.

* `findindex(IQIndex I, Index j) -> long`

  Return the integer `n` of the block of `I` labeled by the Index `j`. <br/>
  The returned integer fulfills the property `I.index(n) == j`. <br/>
  If no block matching `j` is found, the return value is `0`.

* `offset(IQIndex I, Index j) -> long`

  Return the sum of sizes of all blocks of `I` preceding the 
  block corresponding to `j`.

  For example, if `j` labels the third block, and blocks one and 
  two have sizes 4 and 7, then offset(I,j) returns 4+7=11.

* `qn(IQIndex I, Index j) -> QN`

  Return the quantum number of the block labeled by `j`.<br/>
  If there is no matching block, throws an exception.

* `findByQN(IQIndex I, QN q) -> Index`

  Return the Index labeling the first block whose QN matches q. <br/>
  If there is no matching block, throws an exception.

* `showm(IQIndex I) -> string`

  Return a string with detailed information about the total size
  and individual block sizes and quantum numbers of the IQIndex.

## Prime Level Functions

* `prime(IQIndex I, int inc = 1) -> IQIndex` 

   Return a copy of  `I` with prime level increased by 1 (or optional amount `inc`).

* ```
  prime(IQIndex I, 
        IndexType type, 
        int inc = 1) 
        -> IQIndex
  ```

  Return a copy of  `I` with prime level increased by 1 (or `inc`) if `I.type()` equals specified type.

* `noprime(IQIndex I, IndexType type = All) -> IQIndex` 

   Return a copy of `I` with prime level set to zero (optionally only if `I.type()` matches type).

* ```
  mapprime(IQIndex I, 
           int plevold, int plevnew, 
           IndexType type = All) 
           -> IQIndex
  ```

   Return a copy of `I` with prime level plevnew if `I.primeLevel()==plevold`. Otherwise has no effect.
   (Optionally, only map prime level if type of `I` matches specified type.)

<br/>
_This page current as of version 2.0.3_

