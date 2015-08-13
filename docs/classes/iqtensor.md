# IQTensor #

A tensor with components separated into quantum number blocks. Each block is an ITensor stored within the IQTensor. Each Index of a
block belongs to exactly one IQIndex of the IQTensor.

Every block of an IQTensor must have the same [[QN|classes/qn]] flux, defined as the sum of the QNs of each Index of that block times the Arrow direction
of the IQIndex each Index belongs to. For example, a zero flux (QN conserving) IQTensor could have a block with a +1 Sz QN flowing In and a
-1 Sz QN flowing In. Another block of the same IQTensor might have two Indices both flowing In with 0 Sz QN.
The direction of the flow can be reversed with the `dag` function.

In addition to explicitly conserving quantum numbers, computing products of IQTensors is more efficient than for comparably sized ITensors (in the limit of large index dimensions). This is because IQTensors have an explicit sparse structure and only the non-zero elements (the ITensor blocks) need to be summed over.

## Synopsis ##

    Index l1u("link 1 up",4),
          l10("link 1 0",2),
          l1d("link 1 dn",4),
          l20("link 2 0",10),
          s2u("site 2 up",1,Site),
          s2d("site 2 dn",1,Site);

    IQIndex L1("Link 1",l1u,QN(+1),
                        l10,QN( 0),
                        l1d,QN(-1)),
            L2("Link 2",l20,QN(0)),
            S2("Site 2",s2u,QN(+1),
                        s2d,QN(-1));

    //A is constructed with dag(L1),which
    //has an In Arrow.
    //S2 and L2 have Out Arrow directions.
    //Initially an IQTensor has no non-zero blocks.
    IQTensor A(dag(L1),S2,L2);

    //Setting elements explicitly causes the necessary blocks
    //to automatically be created...

    //L1(1) corresponds to the +1 block (flowing In),
    //and S2(1) to the +1 block (flowing Out), 
    //so the divergence of this IQTensor is zero
    A(L1(1),S2(1),L2(3)) = -0.2;

    //L1(7) corresponds to the -1 block (flowing In)
    //and S2(2) to the -1 block (flowing Out)
    A(L1(7),S2(2),L2(9)) = -0.2;

    //..etc..

    //Print the blocks of this IQTensor
    //one at a time
    Foreach(const ITensor& t, A.blocks())
        {
        PrintDat(t); //PrintDat is a macro which 
                     //makes sure the elements of
                     //an ITensor get printed,
                     //not just its Indices
        }


    //Contracting IQTensors is very similar to 
    //contracting ITensors

    //Create a second IQTensor
    IQTensor B(dag(L2),S3);
    //...set its elements...

    IQTensor R = A * B; //contract over common IQIndex L2

    Print(hasindex(R,L1)); //prints 1 (true)
    Print(hasindex(R,S2)); //prints 1 (true)
    Print(hasindex(R,L2)); //prints 0 (false)
    Print(hasindex(R,S3)); //prints 1 (true)

## Constructors ##

* `IQTensor()` 

   Default constructor. A default-constructed IQTensor evaluates to false in a boolean context.

   <div class="example_clicker">Show Example</div>

        IQTensor T;
        if(!T) println("IQTensor T is default constructed.");


* `IQTensor(Real val)` 

   Construct a scalar, rank zero IQTensor with single real component val.

* `IQTensor(IQIndex i1)` 

  `IQTensor(IQIndex i1, IQIndex i2)` 

  `IQTensor(IQIndex i1, IQIndex i2, IQIndex i3)` 

   ... etc. up to 8 IQIndices

   Construct an IQTensor with the given IQIndices. Initially contains no blocks which means all components are zero.

* `IQTensor(IQIndexVal iv1)`

  `IQTensor(IQIndexVal iv1, IQIndexVal iv2)`

  `IQTensor(IQIndexVal iv1, IQIndexVal iv2, IQIndexVal iv3)`

  ... etc. up to 8 [[IQIndexVals|classes/iqindexval]]

  Construct an IQTensor with IQIndices `iv1`, `iv2`, etc. ([[IQIndexVals|classes/iqindexval]] interpreted as objects of type [[IQIndex|classes/iqindex]]), such that the component corresponding to `iv1.i`, `iv2.i`, etc. is set equal to 1 and all other components are set to zero. The resulting IQTensor will have exactly one block. For example, constructing an IQTensor by calling `IQTensor T(L(3),S(2))` makes all components of T zero except for `T(L(3),S(2))==1`.

* `IQTensor(std::vector<IQIndex> iqinds)`

   Construct an IQTensor with IQIndices given by the elements of the vector "iqinds" (zero indexed).


## Accessor Methods ##

* `int r()`

   Return rank (number of IQIndices) of this IQTensor.

* `bool isComplex()`

   Return `true` if this IQTensor has a non-zero imaginary part, otherwise `false`.

* `const IndexSet<IQIndex>& indices()`

   Return a const reference to the indices of this IQTensor, stored internally in an [[IndexSet|classes/indexset]]<IQIndex> container.
   This enables, among other things, iteration over the indices of an IQTensor. For more possible uses, see the [[IndexSet|classes/indexset]] page.

* `const IQTDat& blocks()`
  
   Return a const reference to the container holding the ITensor blocks of this IQTensor. This is primarily for iterating over the blocks, most 
   conveniently using the Foreach macro.

   <div class="example_clicker">Show Example</div>

        IQIndex S1("Site 1",Index("S1 Up",1,Site),QN(+1),
                            Index("S1 Dn",1,Site),QN(-1)),
                S2("Site 2",Index("S2 Up",1,Site),QN(+1),
                            Index("S2 Dn",1,Site),QN(-1));

        ITensor T(S1,S2)
        T(S1(1),S2(2)) = -0.829;
        T(S1(2),S2(1)) = -0.111;

        Foreach(const ITensor& t, T.blocks())
            {
            cout << t << endl;
            cout << t.norm() << endl;
            }

## Operators ##

* `IQTensor& operator*=(IQTensor other)`

  `IQTensor operator*(IQTensor A, IQTensor B)`

   Contracting product. A*B contracts over all IQIndex pairs in common between IQTensors A and B.
   Contracted IQIndices must have opposite Arrow directions, otherwise throws an ITError exception.

   <div class="example_clicker">Show Example</div>

        IQIndex S1("Site 1",Index("S1 Up",1,Site),QN(+1),
                            Index("S1 Dn",1,Site),QN(-1)),
                S2("Site 2",Index("S2 Up",1,Site),QN(+1),
                            Index("S2 Dn",1,Site),QN(-1)),
                L("L",Index("Lup",10),QN(+1),
                      Index("L0",5)  ,QN( 0),
                      Index("Ldn",10),QN(-1));


        IQTensor A(S1,S2,L),
                 B(dag(L),dag(S2));

        A.randomize();
        B.randomize();

        IQTensor R = A*B; //contract over S2 and L

        Print(R.r()); //prints 1 since R has only the S1 IQIndex
        Print(hasindex(R,S1)); //prints 1 (true)
        Print(hasindex(R,S2)); //prints 0 (false)
        Print(hasindex(R,L));  //prints 0 (false)

* `IQTensor& operator+=(IQTensor other)`

  `IQTensor& operator-=(IQTensor other)`

  (and related free methods)

  IQTensor addition and subtraction. Adds IQTensors element-wise. Both IQTensors must have the same set of IQIndices.

* `IQTensor& operator+=(ITensor block)`

  Add an ITensor block to an IQTensor. If the block is already present, adds to it using regular ITensor addition. If the block
  is not present, it is inserted automatically. In debug mode, if the IQTensor already has blocks and the new block being added has a different
  divergence an ITError exception is thrown. (See the `div` [[IQTensor method|iqtensor_functions]].)

* `IQTensor& operator*=(Real fac)`

  `IQTensor& operator/=(Real fac)`

  `IQTensor operator-()`

  (and related free methods)

  Multiplication by a real scalar, division by a real scalar, and negation. Factor is applied to all elements of the IQTensor.

* `IQTensor& operator*=(Complex z)`

  (and related free methods)

  Multiplication by a Complex scalar (where Complex is a typedef for std::complex<Real>). Useful for creating complex IQTensors
  by using the idiom `IQTensor T = A + B*Complex_i` where A and B are real IQTensors and Complex_i is a constant equal to
  Complex(0,1).

* `IQTensor& operator/=(IQTensor other)`

  `IQTensor operator/(IQTensor A, IQTensor B)`

   Non-contracting product. A/B creates a new tensor out of A and B by "merging" any common indices
   according to the rule R<sub>ijk</sub> = A<sub>ik</sub> B<sub>jk</sub> (no sum over k). Here i,j, and k
   could be single indices or groups of indices. Merged IQIndices must have the same Arrow directions, 
   otherwise an ITError exception is thrown.

   <div class="example_clicker">Show Example</div>

        IQIndex S1("Site 1",Index("S1 Up",1,Site),QN(+1),
                            Index("S1 Dn",1,Site),QN(-1)),
                S2("Site 2",Index("S2 Up",1,Site),QN(+1),
                            Index("S2 Dn",1,Site),QN(-1)),
                L("L",Index("Lup",10),QN(+1),
                      Index("L0",5)  ,QN( 0),
                      Index("Ldn",10),QN(-1));


        IQTensor A(S1,S2,L),
                 B(L,S2);

        A.randomize();
        B.randomize();

        IQTensor R = A/B; //merge S2 and L IQIndices

        Print(R.r()); //prints 3
        Print(hasindex(R,S1)); //prints 1 (true)
        Print(hasindex(R,S2)); //prints 1 (true)
        Print(hasindex(R,L));  //prints 1 (true)

## Element Access Methods ##

* `Real& operator()(IQIndexVal iv1, IQIndexVal iv2, ...)` 

   Access component of this IQTensor such that `iv1` (thought of as an IQIndex) is set to value `iv1.i`, `iv2` to `i2.i`, etc. For example, given a matrix-like IQTensor `M` with indices `r` and `c`, can access the (2,1) component by calling `M(r(2),c(1))`. Result is independent of the order of the arguments and depends only on the set of IQIndexVals provided. For the previous example, `M(r(2),c(1)) == M(c(1),r(2))`.

* `Real at(IQIndexVal iv1, IQIndexVal iv2, ...)` 

   Identical to `operator()(IQIndexVal ...)` element access method above, but forces const (non-reference) access of the element.

* `Real toReal()` 

  Return value of a rank zero, scalar IQTensor. If the IQTensor has rank greater than zero or if IQTensor is complex (see below), throws an exception.

* `Complex toComplex()`

  Return value of a complex, scalar (rank zero) IQTensor. If the IQTensor has rank greater than zero, throws an exception.


## Prime Level Methods ##

* `IQTensor& prime(int inc = 1)`

  Increment prime level of all indices by 1. (Optionally by amount `inc`.) Returns a reference to the modified IQTensor.

* `IQTensor& prime(IQIndex I, int inc = 1)`

  Increment prime level of only IQIndex `I` by 1. (Optionally by amount `inc`.)
  Throws an exception of IQTensor does not have IQIndex `I`. Returns a reference to the modified IQTensor.


* `IQTensor& prime(IndexType t, int inc = 1)`

  Increment prime level of every IQIndex of type `t`. (Optionally by amount `inc`.) Returns a reference to the modified IQTensor.

* `IQTensor& noprime(IndexType t = All)`

  Set prime level of all indices to 0. (Optionally only indices of type `t`.) Returns a reference to the modified IQTensor.

* `IQTensor& noprime(IQIndex I)`

  Set prime level of IQIndex `I` to 0. Throws an exception if IQTensor does not have IQIndex `I`. Returns a reference to the modified IQTensor.

* `IQTensor& mapprime(int plevold, int plevnew, IndexType t = All)`

  Change prime level of all indices having prime level `plevold` to `plevnew`. (Optionally only if their type matches `t`.) 
  Returns a reference to the modified IQTensor.


## Other Methods ##

* `randomize()`

  Randomize the elements of this IQTensor. Optimized more for speed than for true randomness.
  If the IQTensor has no blocks, throws an ITError exception since the IQTensor does not have a well defined
  quantum number flux. If the IQTensor has some, but not all possible blocks, this method automatically generates
  all remaining QN-consistent blocks and randomizes them.

* `Real norm()`

  Return the norm of this IQTensor, that is, the Euclidean norm when treating the elements of the IQTensor as a vector.
  Equivalent to, but much more efficient than, `sqrt((T*T).toReal())` for some real IQTensor `T`.

* `Real sumels()`

  Return the sum of all elements of this IQTensor.

* `IQTensor& mapElems(const Callable& f)`

   Apply the function f to each element of this IQTensor, where f is a function, or function object, mapping Real to Real.
   Returns a reference to this IQTensor on return.

* `insert(ITensor block)`

  Insert an ITensor block into the set of blocks of this IQTensor. If a block with the same Index structure already exists, throws an
  ITError exception. For a method which does not throw if the block already exists, see `operator+=(ITensor block)` above.

* `ITensor toITensor()`
  
  Convert this IQTensor to an ITensor and return the result. The conversion works by casting each IQIndex to an Index (recall that IQIndex is
  a subtype of Index) such that their block structure is forgotten. The blocks of the IQTensor are aligned with the corresponding Index
  ranges and the remaining components of the ITensor are padded with zeros. 

* `IQTensor& takeRealPart()`
    
  Set an IQTensor to its real part, dropping its imaginary part. Returns a reference to the resulting IQTensor.

* `IQTensor& takeImagPart()`
    
  Set an IQTensor to its imaginary part, dropping its real part. Returns a reference to the resulting IQTensor.

* `IQTensor& dag()`

  Hermitian conjugate. Reverses the Arrow directions of all IQIndices of this IQTensor and takes the complex conjugate
  of every component.

* `IQTensor& conj()`
  Complex conjugate. Only takes the complex conjugate of this IQTensor without reversing the arrow direction.
