# QN ITensor #


An QN ITensor is an ITensor whose indices have subspaces labeled by quantum numbers
(QN objects) and which as a result will have block-sparse data storage. Most of
the interface of an ITensor with these properties is the same as for a regular,
dense ITensor. So adding, contracting, setting elements, and so on is done the
same way. However, some operations are a little bit different: for example, 
when contracting two QN ITensors, contracted indices must have opposite arrow
directions or an error will be thrown. Also some constructors require extra
arguments when making a QN ITensor.

Most operations and functions for QN ITensors are documented on the [[ITensor|classes/itensor]]
page since they work for both dense and QN ITensors. Occasional slight differences in behavior for
QN ITensors are noted on that page. The information below is about functions strictly
related to QN ITensors only.

If an ITensor `T` is QN-sparse, that is a QN ITensor, then it will satisfy `hasQNs(I)==true`.

The [[QN section of the ITensor book|book/qnitensor_intro]] has more introductory information
about the QN system and QN ITensors.

## Synopsis ##

    // Make a collection of four QN Index objects 
    // which carry QN information corresponding to
    // S=1/2 spins:
    auto sites = SpinHalf(4,{"ConserveQNs=",true})

    // Generate a random QN ITensor which has an
    // overall QN or flux of QN({"Sz",2}):
    auto T = randomITensor(QN({"Sz",2}),sites(1),sites(2),sites(3),sites(4));

## Constructors and Accessor Methods

* `ITensor()` 

   Default constructor. <br/>
   A default-constructed ITensor evaluates to false in a boolean context. <br/>
   To construct a order-zero (scalar) ITensor use the `ITensor(Cplx val)` constructor below.

* `ITensor(Index i1, Index i2, ...)` <br/>
  `ITensor(std::vector<Index> inds)`<br/>
  `ITensor(std::array<Index> inds)`<br/>
  `ITensor(std::initializer_list<Index> inds)`

   If the Index objects carry QN subspaces, this constructor creates a QN ITensor
   (block sparse ITensor) which will have a flux of zero.
   All compatible elements are initially zero.

* `ITensor(QN q, Index i1, Index i2, ...)` <br/>

   Create a QN ITensor (block sparse ITensor) which will have all blocks 
   compatible with an overall flux of `q` and indices `i1, i2, ...`. The 
   Index objects passed must have QN subspaces. 


* `randomITensor(QN q, Index i1, Index i2, ...)` <br/>
  `randomITensorC(QN q, Index i1, Index i2, ...)` <br/>

   Create a QN ITensor (block sparse ITensor) which will have all blocks 
   compatible with an overall flux of `q` and indices `i1, i2, ...`. 

   The blocks will be filled with random real numbers in the case of
   `randomITensor` or random complex numbers in the case of `randomITensorC`.


## QN ITensor Functions

* `flux(T)`

  Given a QN ITensor `T`, return its QN flux. All QN ITensors by construction have
  a well defined flux. For more information about the definition and meaning of
  QN flux, see the [[QN section of the ITensor book|book/qnitensor_intro]].

<br/>
_This page current as of version 3.0.0_
