# IQIndex #

## (subclass of [[Index|classes/index]]) ##

An IQIndex represents an [[Index|classes/index]] split into quantum number blocks. IQIndex is a subclass of [[Index|classes/index]], so
it has a fixed, total bond dimension "m". But an IQIndex also contains an ordered list of [[Index|classes/index]] and [[QN|classes/qn]] pairs which
define how its bond dimension is split into smaller blocks.

For example, the IQIndex representing a single spin 1/2 site has bond dimension 2, which is further broken into two quantum number blocks: a spin up block of dimension 1 (indicated by a [[QN|classes/qn]](+1) paired with an Index of dimension 1) and a spin down block of dimension 1 (indicated by a [[QN|classes/qn]](-1) paired with an Index of dimension 1).

The bond dimension of an IQIndex is the sum of the bond dimensions of its block indices.

An IQIndex also has an Arrow direction associated with it. For more information on Arrows, see the page on [[index conventions|itensor_conventions]].

## Synopsis ##

    Index ip2("i+2",3),
          ip1("i+1",5),
           i0("i 0",3),
          im1("i-1",8);

    IQIndex L("L",
              ip2,QN(+2),
              ip1,QN(+1),
              i0, QN(0),
              im1,QN(-1),
              Out);

    printfln("L.m() == 19 is %s",L.m()==19);
    //above command prints "L.m() == 19 is true"

    Print(L.index(3)); //prints l0
    Print(L.qn(3));    //prints QN(0)


## Constructors ##

* `IQIndex(std::string name, Index i1, QN q1, Arrow dir = Out)`

  `IQIndex(std::string name, Index i1, QN q1, Index i2, QN q2, Arrow dir = Out)`

  `IQIndex(std::string name, Index i1, QN q1, Index i2, QN q2, Index i3, QN q3, Arrow dir = Out)`

   ... etc. up to 6 Index, QN pairs 

   Construct an IQIndex with the given name, Index and QN pairs, and Arrow direction.

* `IQIndex(std::string name, std::vector<IndexQN> indqn, Arrow dir = Out, int plev = 0)`

   Construct an IQIndex with the given name, Arrow direction, and prime level. The Index and QN pairs are provided as a std::vector (of any size) of [[IndexQN|classes/indexqn]] objects.


## Accessor Methods ##

* `const Storage& indices()`

  Return a const reference to the block indices of this IQIndex. Storage is a typedef for std::vector<IndexQN>. This accessor can be used to iterate over the IndexQN blocks of an IQIndex. For more info, see the [[IndexQN|classes/indexqn]] docs.

* `int nindex()`

  Return the number of blocks of this IQIndex.

* `Index index(int i)`

  Return the ith block Index of this IQIndex.

* `QN qn(int i)`

  Return the ith block QN of this IQIndex.

* `Arrow dir()`

  Return the Arrow direction of this IQIndex. Can be `In` or `Out`. For more information see the [[index conventions|itensor_conventions]] page.

* `primeLevel(int val)`

  Set the prime level of this IQIndex. Also sets the prime level of each block Index contained in this IQIndex.


## Operators ##

* `IQIndexVal operator()(int n)`

  Return the IQIndexVal representing this IQIndex set to a specific value "n". For an IQIndex `I`, n can range from 1 to `I.m()`.


## Other Methods ##

* `dag()`

  Reverse the arrow of this IQIndex.

