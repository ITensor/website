# IQTensor #

An IQTensor is similar to an ITensor in that it has named indices. 
But an IQTensor also has a block sparse structure related to conservation of Abelian "quantum numbers". 
IQTensors actually have the same interface as [[ITensors|classes/itensor]], but the indices of an
IQTensor are of type [[IQIndex|classes/iqindex]]. 

IQTensors obey the rule that the only blocks allowed to be non-zero are those with
the same [[QN|classes/qn]] "flux" or "divergence". A block of an IQTensor corresponds to a
specific sector of each IQIndex of the tensor. The flux of a given block is the sum
of the QNs of the sectors it corresponds to times the Arrow direction of each IQIndex.
On an intuitive level, the flux of an IQTensor is how much it changes the total quantum
number of a tensor network when it is contracted with this network. As an example involving
spins, an "Sz" operator has zero flux while an "S+" operator has flux +2 since it 
increases the total Sz by +2 (in units of spin 1/2).

In addition to explicitly conserving quantum numbers, computing products of IQTensors is much more efficient 
than for comparably sized ITensors (in the limit of large index dimensions). This is because IQTensors have an explicit sparse structure and only the non-zero elements (the ITensor blocks) need to be summed over.

## Synopsis ##

    auto L = IQIndex("L",Index("L-",2),QN(-1),
                         Index("L0",4),QN( 0),
                         Index("L+",2),QN(+1));
    auto S = IQIndex("S",Index("S-",1),QN(-1),
                         Index("S+",1),QN(+1));

    
    //Create a zero IQTensor
    auto A = IQTensor(L,S);

    //Setting an element determines
    //the flux of this IQTensor
    A.set(L(2),S(2),2.2);

    Print(flux(A)); //prints: QN(0)

    //Create an IQTensor with flux QN(0)
    //but otherwise random elements
    auto B = randomTensor(QN(0),dag(L),S);

    //Contracting IQTensors is very similar to 
    //contracting ITensors except contracted 
    //IQIndex's must have opposite Arrow directions
    auto R = A * B; //contract over common IQIndex L


Because IQTensor and ITensor have an identical interface (both implemented using the 
same template class), to see a list of class methods available for IQTensors 
see the [[ITensor|classes/itensor]] documentation.

Functions acting on ITensors which are not listed here can 
be assumed to have the same behavior for IQTensors.

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

* `IQTensor += ITensor`

  Add an ITensor whose set of Index objects correspond to a specific block 
  of this IQTensor to that block. Each Index of the ITensor must be a 
  block Index of an IQIndex of the IQTensor.

* `IQTensor / IQTensor -> IQTensor` <br/>
  `IQTensor /= IQTensor`

  The non-contracting product is not currently implemented for IQTensors
  since it can give results with ill-defined flux in certain cases.

## Functions for Constructing IQTensors

* `randomTensor(QN q, IQIndex i1, IQIndex i2, ...) -> IQTensor` <br/>
  `randomTensorC(QN q, IQIndex i1, IQIndex i2, ...) -> IQTensor`

  Create an IQTensor having IQIndex's i1, i2, etc. and having flux `q`. 
  All non-zero blocks of this IQTensor are initialized with random elements.

  `randomTensorC` is the same except blocks are initialized with random complex
  elements.

* `randomTensor(IQIndexVal iv1, IQIndexVal iv2, ...) -> IQTensor` <br/>

  Given a set of [[IQIndexVals|classes/iqindexval]], return an IQTensor
  having IQIndex's corresponding to the IQIndexVals. The flux of the IQTensor
  is determined by which block contains the element corresponding to the IQIndexVals.
  All blocks having this flux are filled with random elements.


## Functions for Analyzing IQTensors

* `flux(IQTensor T) -> QN` <br/>
  `div(IQTensor T) -> QN`

  Return the total flux of this IQTensor (`div` is alternate name for `flux`).

  Flux is defined as follows:

  1. All non-zero blocks of an IQTensor have the same flux.
  2. For any non-zero block, identify the sector of each IQIndex it corresponds to.
  3. Compute the product of the QN of each IQIndex sector the block corresponds to times
     the Arrow direction of that IQIndex.

     (Recall that Arrows can be either `In` or `Out`; multiplying a QN by `In` 
      flips its sign while `Out` leaves a QN's sign unchanged.)

  4. The flux is the sum of these QN * Arrow products, which is again a QN.





