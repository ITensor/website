# IQTensor #

An IQTensor is similar to an ITensor in that it has named indices and supports most of the same
operations.
But an IQTensor also has a block sparse structure related to conservation of Abelian "quantum numbers". 
IQTensors actually have the same interface as [[ITensors|classes/itensor]], but the indices of an
IQTensor are of type [[IQIndex|classes/iqindex]]. 

IQTensors obey the rule that the only blocks allowed to be non-zero are those with
the same [[QN|classes/qn]] "divergence". A block of an IQTensor corresponds to a
specific sector of each IQIndex. The divergence of a given block is the sum
of the QNs of the corresponding sectors times the Arrow direction of each IQIndex.
On an intuitive level, the divergence of an IQTensor says how much the total quantum
number will be changed by contracting with that IQTensor.
As an example involving spins, an "Sz" operator has zero divergence while an "S+" operator 
has divergence +2 since it increases the total Sz by +2 (in units of spin 1/2).

Contracting IQTensors can be much more efficient 
than contracting ITensors. This is because IQTensors have an explicit sparse 
structure where many of its blocks are constrained to be zero.

Because IQTensor and ITensor have an identical interface (both implemented using the 
same template class), to see a list of class methods available for IQTensors 
see the [[ITensor|classes/itensor]] documentation.

Functions acting on ITensors which are not discussed below can 
be assumed to have the same behavior for IQTensors.

IQTensor is defined in "itensor/iqtensor.h"; also see "itensor/iqtensor.ih". The 
IQTensor interface is defined in "itensor/itensor_interface.h".


## Synopsis ##

    auto L = IQIndex("L",Index("L-",2),QN(-1),
                         Index("L0",4),QN( 0),
                         Index("L+",2),QN(+1));
    auto S = IQIndex("S",Index("S-",1),QN(-1),
                         Index("S+",1),QN(+1));

    //Create a zero IQTensor
    auto A = IQTensor(L,S);

    //Setting an element determines
    //the divergence of this IQTensor
    A.set(L(2),S(2),2.2);

    //Compute IQTensor divergence
    Print(div(A)); //prints: QN(0)

    //Create an IQTensor with div QN(0)
    //but otherwise random elements
    auto B = randomTensor(QN(0),dag(L),S);

    //Contracting IQTensors is very similar to 
    //contracting ITensors except contracted 
    //IQIndex's must have opposite Arrow directions
    auto R = A * B; //contract over common IQIndex L

## IQTensor Class Methods Specializations

* `.dag()`

  Reverse the Arrow direction of all IQIndex's of this IQTensor
  and complex conjugate all the tensor elements.

## Operations on IQTensors

Most operation available for ITensors work similarly for IQTensors.
The following are operations which have different behavior or are only
defined for IQTensors:

* `IQTensor * IQTensor -> IQTensor` <br/>
  `IQTensor *= IQTensor`

  Contract two IQTensors, summing over all matching IQIndex objects.

  An IQIndex is only allowed to contract with a matching IQIndex of
  the opposite Arrow direction. If two IQIndex's match but
  have the same direction, the `*` operation throws an `ITError` exception.

* `IQTensor + IQTensor -> IQTensor` <br/>
  `IQTensor += IQTensor` <br/>
  `IQTensor - IQTensor -> IQTensor` <br/>
  `IQTensor -= IQTensor`

  Add or subtract two IQTensors. Both IQTensors must have the same 
  set of IQIndex's including Arrow directions. (However the order
  of the IQIndex's are not important.)

* `IQTensor -> ITensor` <br/>
  `toITensor(IQTensor T) -> ITensor`

  Automatically conversion an IQTensor to an ITensor: an IQTensor
  may be converted to an ITensor. 
  * Each Index of the resulting ITensor
    is the result of casting each IQTensor to its parent type, Index.
  * The tensor elements remain unchanged except that it becomes dense.
    Blocks of the IQTensor previously required to be zero are now
    allocated in memory and can be set to non-zero values.

  The function `toITensor` is provided for users to better notate
  that a conversion to ITensor is the intended behavior.

* `IQTensor * ITensor  -> ITensor` <br/>
  `ITensor  * IQTensor -> ITensor` 

  Contracting an IQTensor with an ITensor first converts a copy
  of the IQTensor to an ITensor as described above, then performs
  an ITensor contraction as usual.

* `IQTensor += ITensor`

  Add an ITensor whose set of Index objects correspond to a specific block 
  of this IQTensor to that block. Each Index of the ITensor must be a 
  block Index of an IQIndex of the IQTensor.


* `IQTensor / IQTensor -> IQTensor` <br/>
  `IQTensor /= IQTensor`

  The non-contracting product is not currently implemented for IQTensors
  since it can give results with ill-defined divergence in certain cases.

## Functions for Constructing IQTensors

* `randomTensor(QN q, IQIndex i1, IQIndex i2, ...) -> IQTensor` <br/>
  `randomTensorC(QN q, IQIndex i1, IQIndex i2, ...) -> IQTensor`

  Create an IQTensor having IQIndex's i1, i2, etc. and having divergence `q`. 
  All non-zero blocks of this IQTensor are initialized with random elements.

  `randomTensorC` is the same except blocks are initialized with random complex
  elements.

* `randomTensor(IQIndexVal iv1, IQIndexVal iv2, ...) -> IQTensor` <br/>

  Given a set of [[IQIndexVals|classes/iqindexval]], return an IQTensor
  having IQIndex's corresponding to the IQIndexVals. The divergence of the IQTensor
  is determined by which block contains the element corresponding to the IQIndexVals.
  All blocks having this divergence are filled with random elements.

## Functions for Constructing Sparse IQTensors

* `setElt(IQIndexVal iv1, IQIndexVal iv2, ...) -> IQTensor`

  Return an IQTensor whose only non-zero element is the one corresponding
  to the provided set of [[IQIndexVals|classes/iqindexval]]. This element
  has the value 1.0.

* `delta(IQIndex i1, IQIndex i2, ...) -> IQTensor`

  Return a diagonal-sparse IQTensor with the provided IQIndex's
  and all diagonal elements equal to 1.0. Because all diagonal
  entries are the same, uses only a constant amount of memory
  regardless of IQIndex size.
  
  Contracting an IQTensor
  with a delta IQTensor is implemented through specialized routines
  for maximum efficiency and can be used, for example, to trace a pair of indices
  or replace one IQIndex with another.

* `combiner(IQIndex i1, IQIndex i2, ...) -> IQTensor`

  Return a sparse IQTensor with special "combiner" storage whose
  purpose is to combine the provided IQIndex's into a single 
  larger IQIndex whose size is the product of `i1.m()*i2.m()*...`.

  The returned IQTensor has one extra IQIndex in addition to
  the IQIndex's provided. This extra IQIndex is the combined IQIndex.

  Although combining IQIndex's in a naive way could result in many
  IQIndex blocks with the same quantum number, the IQTensor combiner
  takes extra steps to ensure that all degenerate QN sectors are 
  "condensed" into just one sector for each possible QN.

  To "uncombine" a combined IQIndex, just contract with the 
  `dag` (Hermitian conjugate) of the original combiner.

  <div class="example_clicker">Click to Show Example</div>

      auto A = IQTensor(I,J,K);
      //...set elements of A...

      auto C = combiner(K,I);
      //C has extra "combined" IQIndex
      Print(rank(C)); //prints: 3

      //combine K and I into one IQIndex
      auto cA = A * C;
      Print(rank(cA)); //prints: 2

      //"uncombine" IQIndex back into K and I
      auto uA = cA * dag(C);
      //resulting IQTensor is identical to A
      Print(norm(uA-A)); //prints: 0.0
        


## Functions for Analyzing IQTensors

* `div(IQTensor T) -> QN`

  Return the total divergence of this IQTensor.

  Divergence is defined as follows:

  1. All non-zero blocks of an IQTensor have the same divergence.
  2. For any non-zero block, identify the sector of each IQIndex it corresponds to.
  3. Compute the product of the QN of each IQIndex sector the block corresponds to times
     the Arrow direction of that IQIndex.

     (Recall that Arrows can be either `In` or `Out`; multiplying a QN by `In` 
      flips its sign while `Out` leaves a QN's sign unchanged.)

  4. The divergence is the sum of these QN * Arrow products, which is again a QN.

* `dir(IQTensor T, IQIndex I) -> Arrow`

  Search each IQIndex of T for one that matches the IQIndex I (recall that Arrow directions
  are not used in IQIndex comparison). If a matching IQIndex is found, returns the Arrow
  direction of that IQIndex (as it appears on T).

* `findIQInd(IQTensor T, Index i) -> IQIndex`
 
  Searches each [[IQIndex|classes/iqindex]] of T, checking if the Index i is one of the 
  "block indices" of that IQIndex. Returns that IQIndex if found.

  If no IQIndex is found for which Index i is a block index, returns a default initialized
  IQIndex (recall that a default initialized IQIndex evaluates to `false` in a boolean
  context, so can be used to check whether a matching IQIndex was found).
  
  <div class="example_clicker">Click to Show Example</div>

      auto lm = Index("L-",2);
      auto l0 = Index("L0",4);
      auto lp = Index("L+",2);
      auto L = IQIndex("L",lm,QN(-1),
                           l0,QN( 0),
                           lp,QN(+1));
      auto S = IQIndex("S",Index("S-",1),QN(-1),
                           Index("S+",1),QN(+1));

      auto A = IQTensor(S,L);

      auto I = findIQInd(A,l0);
      if(!I) println("IQIndex not found");

      Print(I == L); //prints: true

* `qn(IQTensor T, Index i) -> QN`

  Searches each IQIndex of T until one is found which has the Index `i` as
  a block index. Returns the corresponding block QN of the IQIndex block
  labeled by `i`.

  If no such IQIndex is found, throws an ITError exception.

* `dir(IQTensor T, Index i) -> Arrow`

  Searches each IQIndex of T until one is found which has the Index `i` as
  a block index. Returns the Arrow direction of that IQIndex.

  If no such IQIndex is found, throws an ITError exception.

## Developer / Advanced Methods

* `mixedIQTensor(IQTensor i1, IQTensor i2,...) -> IQTensor`

  Construct an IQTensor with IQIndex's i1, i2, etc. The IQTensor
  has QMixed storage, which allows any tensor component to be 
  non-zero just like a regular ITensor. This means it has "mixed"
  QN divergence sectors.

  The main purpose of mixedIQTensors is to create an ITensor 
  but from a function that can only return one type; by choosing 
  that return type to be `IQTensor` it is possible for the 
  function to create both IQTensors and ITensors (which might
  not be well-defined IQTensors in general).


<br/>
_This page current as of version 2.0.6_
