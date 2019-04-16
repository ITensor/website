# ITensor #


An ITensor is a tensor with named indices (of type [[Index|classes/index]]).
The key feature of the ITensor is automatic contraction over all matching indices, 
similar to Einstein summation.

An ITensor is created with a fixed number of Index objects specifying its indices. 
Because Index objects carry identifying information, most of the 
ITensor interface does not depend on the Index order. For example, 
given an ITensor constructed with indices `a` and `b`, 
calling `elt(T,a=2,b=5)` and `elt(T,b=5,a=2)` accesses the same tensor element.

In addition to real-valued storage, ITensors can have other storage types
such as complex storage or various sparse storage types.

If an ITensor is constructed with regular indices (Index objects `I` for which 
`hasQNs(I)==false`) then its storage will be dense.

If instead an ITensor is constructed with indices carrying additional quantum number (QN)
block structure  (Index objects `I` for which 
`hasQNs(I)==true`) then its storage will be block-sparse. 
(Up through version 2 of ITensor, such ITensors were called IQTensors.)

The `ITensor` class is defined in the header "itensor/itensor.h"

## Synopsis ##

    auto b1 = Index(5);
    auto b3 = Index(8);
    auto s2 = Index(2,"Site");
    auto s3 = Index(2,"Site");

    auto phi = ITensor(b1,s2,s3,b3);

    phi.set(b1=2,s2=1,s3=2,b3=2, -0.5);
    phi.set(b1=3,s2=2,s3=1,b3=6, 1.4);
    //...

    auto nrm = norm(phi); //save the original norm of phi
    phi /= nrm; //division by a scalar
    Print(norm(phi)); //prints: 1.0

    //The * operator automatically contracts all matching indices.
    //The prime(phi,b3) method primes the b3 Index of the second
    //ITensor in the product so it is not contracted.

    ITensor rho = phi * prime(phi,b3);

    Print(order(rho)); //prints 2
    Print(hasIndex(rho,b3)); //prints: true
    Print(hasIndex(rho,prime(b3))); //prints: true
    Print(hasIndex(rho,s2)); //prints: false

## Constructors and Accessor Methods

* `ITensor()` 

   Default constructor. <br/>
   A default-constructed ITensor evaluates to false in a boolean context. <br/>
   To construct a order-zero (scalar) ITensor use the `ITensor(Cplx val)` constructor below.

* `ITensor(Index i1, Index i2, ...)` <br/>
  `ITensor(std::vector<Index> inds)`<br/>
  `ITensor(std::array<Index> inds)`<br/>
  `ITensor(std::initializer_list<Index> inds)`

   Construct an ITensor with one or more indices. All elements are initially zero.
   For efficiency reasons no storage is actually allocated when calling this constructor, 
   but automatically gets allocated when, for example, setting an element.

   Indices can be provided as a list or in a vector, array, or initializer_list.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site"); 
      auto s2 = Index(2,"Site");
      auto T = ITensor(s1,s2);

* `ITensor(Cplx val)` 

   Construct an order-zero, scalar ITensor with its single component set to val.
   If the imaginary part of `val` is exactly zero then the storage of the ITensor will
   be real.<br/>
   Because Real numbers automatically convert to Cplx, calling `ITensor(3.14)` calls 
   this constructor.

   <div class="example_clicker">Click to Show Example</div>

      auto R = ITensor(2.71);
      auto C = ITensor(3+4_i);

* `randomITensor(Index i1, Index i2, ...)` <br/>
  `randomITensorC(Index i1, Index i2, ...)` <br/>
  `randomITensor(IndexSet inds)`

  Create an ITensor with the provided indices and with random elements.

  `randomITensorC` makes an ITensor with random complex elements.

   <div class="example_clicker">Click to Show Example</div>

      auto i = Index(2);
      auto j = Index(3);

      auto T = randomITensor(i,j);

      auto TC = randomITensorC(i,j);
      Print(isComplex(TC)); //prints: true

* `matrixITensor(Matrix&& M, Index i1, Index i2)`

  Create an ITensor with the two indices i1 and i2, which correspond to the
  row and column indices of the provided Matrix. The elements of the returned
  ITensor are set to be those of the Matrix provided.

  The Matrix M is expected to be passed as an lvalue, either by passing a temporary
  or by calling std::move. Its storage will be moved into the returned ITensor and
  the Matrix will have empty storage afterward.

   <div class="example_clicker">Click to Show Example</div>

      auto M = Matrix(2,2);
      M(0,0) = 11;
      M(0,1) = 12;
      M(1,0) = 21;
      M(1,1) = 22;

      auto r = Index(2);
      auto c = Index(2);

      auto T = matrixITensor(std::move(M),r,c);


* `inds(ITensor T) -> IndexSet const&`

   Return a reference to the indices of this ITensor, as an [[IndexSet|classes/indexset]]
   container.
   This method is useful for iterating over all of the indices of an ITensor.

   <div class="example_clicker">Click to Show Example</div>

        auto s1 = Index(2,"Site"); 
        auto s2 = Index(2,"Site");
        auto l1 = Index(10,"Link");
        auto l2 = Index(24,"Link");

        auto T = ITensor(l1,s1,s2,l2);

        //Print out just the Link indices of T
        for(auto& I : inds(T))
            {
            if(hasTags(I,"Link")) println(I);
            }

* `explicit operator bool()`

  Evaluate an ITensor in a boolean context. Evaluates to `false` only if an ITensor is default constructed.

   <div class="example_clicker">Click to Show Example</div>

        auto T1 = ITensor();
        if(T1) println("T1 evaluates to true");
        else   println("T1 evaluates to false");
        //prints: T1 evaluates to false

        auto T2 = ITensor(s1,s2);
        if(T2) println("T2 evaluates to true");
        else   println("T2 evaluates to false");
        //prints: T2 evaluates to true

## Element Access Methods

* `elt(ITensor T, IndexVal iv1, IndexVal iv2, ...) -> Real`

  `eltC(ITensor T, IndexVal iv1, IndexVal iv2, ...) -> Cplx`

  Returns the element of the ITensor `T` corresponding to the provided IndexVals.

  An [[IndexVal|classes/indexval]] `iv` is a pairing of an Index `index(iv)` 
  and an integer `val(iv)`.
  The element returned is the one corresponding to holding `index(iv1)` 
  equal to `val(iv1)`, `index(iv2)` equal to `val(iv2)`, etc.

  For `elt(...)`, if the element to be accessed has a non-zero imaginary part, this method 
  throws an exception.

  `eltC(...)` behaves identically to the `elt(...)` except its return type is a complex number. 
  It succeeds whether the ITensor has complex or real storage.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(4,"i");
      auto j = Index(4,"j");
      auto k = Index(4,"k");

      //Make a scalar ITensor
      auto S = ITensor(2.7);
      //Access its value (a real number)
      auto rs = elt(S);

      //Make a random order 3 ITensor
      auto T = randomITensor(i,j,k);
      //Get one of its elements
      auto rt = elt(T,j=2,k=1,i=4);

      //Make a complex scalar ITensor
      auto Sc = ITensor(2.7-4_i);
      //Access its value as a complex number
      auto zs = eltC(Sc);

* `elt(ITensor T, int i1, int i2, ...) -> Real`

  `eltC(ITensor T, int i1, int i2, ...) -> Cplx`

  Shorthand notation for `elt(ITensor, IndexVal, ...)` (or `eltC(...)`) when the ordering 
  of the indices of the ITensor are known.
  For example, for ITensor T with indices ordered as j,i,k, `elt(T,1,2,4)` is equivalent to
  `elt(T,j=1,i=2,k=4)`.

  Note that the ordering of the indices of an ITensor can be set using the 
  `permute(ITensor,IndexSet)` function.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(4,"i");
      auto j = Index(4,"j");
      auto k = Index(4,"k");

      //Make a random order 3 ITensor
      auto T = randomITensor(i,j,k);
      //Order the indices
      T = permute(T,{k,i,j});
      //Get one of its elements
      auto rt = elt(T,2,1,4);
      Print(rt==elt(T,i=1,j=4,k=2)); //prints: true

* `.set(IndexVal iv1, IndexVal iv2, ... , Cplx z)`

  Set the element of this ITensor corresponding to the provided IndexVals to the value `z`.

  If `z` has exactly zero imaginary part and the ITensor storage is real, it will not be 
  switched to complex storage.

  Because Real numbers are automatically convertible to Cplx, one can plug Real 
  numbers into this method.

  <div class="example_clicker">Click to Show Example</div>

      //Make an order 3 ITensor
      auto T = ITensor(i,j,k);

      //Set an element to a real number
      T.set(k=2,j=2,i=3, -1.24);

      //Set an element to a complex number
      T.set(k=4,j=1,i=2, 3.2-4.7_i);

* `.set(int i1, int i2, ... , Cplx z)`

  Shorthand notation for `.set` above when the ordering of the indices of the ITensor are known.
  For example, for ITensor T with indices ordered as j,i,k, `T.set(1,2,4, 3.2)` is equivalent to 
  `T.set(j=1,i=2,k=4, 3.2)`.

  Note that the ordering of the indices of an ITensor can be set using the `permute` function 
  described below.

  <div class="example_clicker">Click to Show Example</div>

      //Make an order 3 ITensor
      auto T = ITensor(i,j,k);

      T = permute(T,j,i,k);
      //Set an element to a real number
      T.set(1,2,3,-1.24); 
      Print(elt(T,j=1,i=2,k=3) == -1.24); //prints "true"

<a name="tag_methods"></a>
## Tag Methods

ITensors have all of the same tagging methods that are defined for
[[IndexSets|classes/indexset]]. See the _Tag Methods_ section of 
the IndexSet documentation for a complete list of methods.

  <div class="example_clicker">Click to Show Example</div>

      auto i1 = Index(2,"i1");
      auto i2 = Index(2,"i2");
      auto i3 = Index(2,"i3");

      auto T = randomITensor(i1,i2,i3);

      auto Tp = prime(T,i1);  // Make a new ITensor Tp with index i1 primed

      Print(hasIndex(Tp,i1)); //prints: false
      Print(hasIndex(Tp,prime(i1))); //prints: true
      Print(hasIndex(Tp,i2)); //prints: true
      Print(hasIndex(Tp,i3)); //prints: true

      // Add the tag "x" to indices with integer tag (prime level) 1
      auto Tx = addTags(Tp,"x","1");

      Print(hasIndex(Tx,i1)); //prints: false
      Print(hasIndex(Tx,prime(i1))); //prints: false
      Print(hasIndex(Tx,prime(addTags(i1,"x")))); //prints: false
      Print(hasIndex(Tx,i2)); //prints: true
      Print(hasIndex(Tx,i3)); //prints: true

## Operators Supported By ITensors ##

In this section, expressions like `ITensor * ITensor -> ITensor` are pseudocode
indicating that two ITensors can be multiplied using the `\*` operator,
and that the result will be an ITensor.

* `ITensor \* ITensor -> ITensor` <br/>
  `ITensor \*= ITensor`

  Contracting product. `A * B` contracts (sums) over all indices common to A and B. 
  The `\*=` version overwrites the ITensor on the left afterward.

  <div class="example_clicker">Show Example</div>

        auto l1 = Index(4);
        auto s2 = Index(2,"Site"); 
        auto s3 = Index(2,"Site");
        auto l3 = Index(4);

        auto A = ITensor(l1,s2,s3,l3);

        auto B = ITensor(l1,s2,prime(s3),prime(l3));

        //... set components of A and B ...

        auto R = A * B; //contracts l1 and s2

        Print(order(R)); //prints 4, the order of R
        Print(hasIndex(R,s3)); //prints "true"
        Print(hasIndex(R,l3)); //prints "true"
        Print(hasIndex(R,prime(s3))); //prints "true"
        Print(hasIndex(R,prime(l3))); //prints "true"
        Print(hasIndex(R,l1)); //prints "false"

* `ITensor + ITensor -> ITensor`<br/>
  `ITensor - ITensor -> ITensor`<br/>
  `ITensor += ITensor`<br/>
  `ITensor -= ITensor`

  ITensor addition and subtraction. Adds ITensors element-wise. 
  Both ITensors must have the same set of indices, though they can be in
  different orders.

  <span style="color:red">Important note:</span> if the left-hand-side
  ITensor is default initialized, doing += or -= will assign the right-hand
  ITensor to it (click to see example below). This is for convenience when summing multiple ITensors in 
  a loop.

  <div class="example_clicker">Show Example</div>

        auto l1 = Index(4);
        auto s2 = Index(2,"Site");
        auto s3 = Index(2,"Site");
        auto l3 = Index(4);

        auto A = ITensor(l1,s2,s3,l3);

        auto B = ITensor(l3,s3,s2,l1);

        //...set components of A and B...

        ITensor S = A + B; //sum of A and B
        ITensor D = A - B; //difference of A and B

        //
        // Calling += on a default-initialized ITensor
        //
        auto T1 = ITensor();
        auto T2 = ITensor(l1,l2);
        if(not T1) print("T1 is default initialized");

        T1 += T2;

        if(T1) print("T1 is now initialized and equals T2");


* `-ITensor -> ITensor`

  Negate each element of an ITensor.

* `ITensor * Real -> ITensor`<br/>
  `Real * ITensor -> ITensor`<br/>
  `ITensor / Real -> ITensor`<br/>
  `ITensor *= Real`<br/>
  `ITensor /= Real`<br/>

  Multiply or divide each element of an ITensor by a real scalar.

* `ITensor * Cplx -> ITensor`<br/>
  `Cplx * ITensor -> ITensor`<br/>
  `ITensor / Cplx -> ITensor`<br/>
  `ITensor *= Cplx`<br/>
  `ITensor /= Cplx`<br/>

  Multiply or divide each element of an ITensor by a complex scalar. 

  If the ITensor initially has real storage
  and the complex scalar has a non-zero imaginary part, the storage automatically
  converts to complex storage. If the complex number has exactly zero imaginary part, the ITensor
  will continue to have real storage.

* `ITensor / ITensor -> ITensor`<br/>
  `ITensor /= ITensor`<br/>

  Non-contracting product (has no relationship to division). 
  `A / B` creates a new tensor out of A and B by "merging" any common indices
  according to the rule R<sub>ijk</sub> = A<sub>ik</sub> B<sub>jk</sub> (no sum over k). 
  (Here i, j, and k could be individual indices or represent groups of indices.)

  <div class="example_clicker">Show Example</div>

        auto s2 = Index(2,"Site"); 
        auto s3 = Index(2,"Site");
        auto l3 = Index(4);

        auto A = ITensor(s2,s3,l3);
        auto B = ITensor(s3,l3);

        //...set components of A and B...

        ITensor R = A / B; //merge indices s3 and l3

        Print(order(R)); //prints 3, order of R
        Print(hasIndex(R,s2)); //prints "true"
        Print(hasIndex(R,s3)); //prints "true"
        Print(hasIndex(R,l3)); //prints "true"

* `ITensor  * setElt(IndexVal) -> ITensor` <br/>
  `setElt(IndexVal) * ITensor  -> ITensor` <br/>
  `ITensor *= setElt(IndexVal)` <br/>

  When multiplied by an ITensor, a setElt(IndexVal) behaves like a order-1 (single Index) ITensor
  whose only non-zero element is the element corresponding to the IndexVal, which has the value 1.0.
  
  <div class="example_clicker">Show Example</div>

      auto i = Index(3);
      auto j = Index(4);

      auto T = ITensor(i,j);
      randomize(T);

      auto S = T * setElt(i(2));

      // Now S will have only Index j
      // and will correspond to the "slice"
      // of T with i fixed to the value 2

      Print(S.elt(j=3) - T.elt(i=2,j=3)); //prints: 0.0


## Complex ITensor Methods

* `.conj()`
  
  `conj(ITensor T) -> ITensor`

   Complex conjugate each element of this ITensor.

* `.takeReal()`
  
   Replace each element of this ITensor with their real part. Afterwards the ITensor
   will have real storage.

* `.takeImag()`
  
   Replace each element of this ITensor with their imaginary part. Afterwards the ITensor
   will have real storage.

* `.dag()`
  
  `dag(ITensor T) -> ITensor`

   Complex conjugate each element of this ITensor. Same as `.conj()` but
   useful for interface compatibility with IQTensor.
   
## Elementwise Transformation Methods

* `.fill(Cplx z)`

  Replace all elements with the number z. If z has zero imaginary part, the ITensor
  will have real storage afterward. Note that Real scalars automatically convert
  to Cplx so this method can be used for either type.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);

      T.fill(1.);
      T.fill(2.+3._i);

      PrintData(T);

* `.generate(Func f)`

  Set each element of this ITensor by repeatedly calling the function `f()`.

  For example, if `f` is a random number generator, then the ITensor elements
  will be randomized by calling `f` once for each element.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);

      //create a lambda function
      //which return a scalar
      auto c = 1.0;
      auto countUp = [&c]() { return c++; };

      T.generate(countUp);

      PrintData(T);

* `.apply(Func f)`

  Transform this ITensor by applying the function `f` to each element
  and replacing the element with the return value of `f`.
  
  If the ITensor has real storage, the function `f` is only required
  to accept Real arguments (accepting a Cplx argument works 
  too since Real is automatically convertible to Cplx).

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);
      randomize(T);

      //create a lambda function
      //which returns the square of its argument
      auto square = [](Real r) { return r*r; };

      T.apply(square);

      PrintData(T);

* `.visit(Func f)`

  Apply the function `f` to each element of this ITensor.
  Calling `visit` has no effect on an ITensor but is useful
  for inspecting each element. For example, it could be 
  print elements meeting a certain criterion.
  
  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);
      randomize(T);

      //create a lambda function
      //which remembers the largest 
      //magnitude number given to it
      Real max_mag = 0.;
      auto maxComp = [&max_mag](Real r)
        {
        if(std::fabs(r) > max_mag) max_mag = std::fabs(r);
        };

      T.visit(maxComp);

      println("Largest magnitude elt of T is ",max_mag);

## Other Facts About ITensors

* An ITensor `T` can be read from or written to a stream using
  `read(s,T)` or `write(s,T)`.

* Printing an ITensor shows its indices and some other
  information such as its norm.

  To view all non-zero elements of an ITensor `T`,
  do one of the following:

  * PrintData(T);

  * printfln("T = %f",T);

  In the `printfln` command, the `%s` formatting token 
  does not display ITensor elements, whereas the `%f` token
  shows all non-zero elements.
  
## Functions for Modifying ITensors

* `.randomize(Args args = Args::global())`

  Randomize all elements the ITensor T. Optimized more for speed than for true randomness.
  Afterward all elements will be real by default.

  Optionally `.randomize()` accepts a named argument "Complex" which if set to `true`
  will make the ITensor have random complex elements.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);
      T.randomize(T);
      T.randomize({"Complex",true});

## Functions for Transforming ITensors

* `apply(ITensor T, Func f) -> ITensor`
  
  Return the ITensor resulting from transforming each element of T by calling `f(x) -> y`. 
  Works similarly to the `.apply` method discussed above but creates a new 
  ITensor instead of modifying an ITensor in-place.

* `permute(ITensor T, IndexSet is) -> ITensor` <br/>

  `permute(ITensor T, Index i1, Index i2, ...) -> ITensor` <br/>

  Given an ITensor T and an IndexSet or list of all of its indices in a particular order,
  return an ITensor with indices in that order.
  The data of the output ITensor is the appropriate permutation of the data 
  of the ITensor T.

  <div class="example_clicker">Click to Show Example</div>

      auto T = randomITensor(i,j,k);

      auto Tp = permute(T,{j,i,k});

      Print(elt(Tp,1,2,4) == elt(Tp,j=1,i=2,k=4)); //prints "true"

* `random(ITensor T, Args args = Args::global()) -> ITensor`

  Return a new ITensor with the same indices as T but with randomized, real elements.

  Optionally `random` accepts a named argument "Complex" which if set to `true`
  will make the returned ITensor have random complex elements.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);

      auto RT = random(T);

      auto CT = random(T,{"Complex",true});


* `realPart(ITensor T) -> ITensor`

  Return just the real part of an ITensor T.

* `imagPart(ITensor T) -> ITensor`

  Return just the imaginary part of an ITensor T.

## Extracting Properties of ITensors

* `order(ITensor T) -> long`

   Return the order (number of indices) of the ITensor T.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site");
      auto s2 = Index(2,"Site");
      auto T = ITensor(s1,s2);

      Print(order(T)); //prints: order(T) = 2

*  `maxDim(ITensor T) -> long`

   Return the maximum dimension of all indices in the ITensor.

*  `minDim(ITensor T) -> long`

   Return the minimum dimension of all indices in the ITensor.

* `norm(ITensor T) -> Real`

  Return the Euclidean norm of this ITensor 
  (the square root of the sum of squares of its elements).
  Equivalent to, but much more efficient than, `sqrt(real(eltC(dag(T)*T)))`

* `isReal(ITensor T) -> bool` <br/>

  Return `true` if the ITensor has real valued storage, otherwise `false`. 

* `isComplex(ITensor T) -> bool` <br/>

  Return `true` if the ITensor has complex valued storage, otherwise `false`. 
  Returns true even if the norm of the imaginary part happens to be zero.

* `sumels(ITensor const& T) -> Real` <br/>
  `sumelsC(ITensor const& T) -> Cplx` <br/>

  Return the sum of all elements of this ITensor. If the ITensor has a non-zero imaginary
  part, throws an exception.

  For a function that works for real or complex ITensors, use `sumelsC`.

## Analyzing ITensor Indices

* `hasInds(ITensor T, IndexSet is) -> bool`

  Returns `true` if ITensor `T` has all of the indices in the IndexSet `is`

* `hasIndex(ITensor T, Index i) -> bool`

  Returns `true` if ITensor T has an Index exactly matching `i` (including its tags).

*  `findInds(ITensor T, TagSet tsmatch) -> IndexSet`

  Find all indices of the ITensor containing tags in the specified TagSet.

* `findIndex(ITensor T, TagSet tags) -> Index`

  Return the first Index of T that contains tags in `tags`. If no such Index is found, returns
  a default-constructed Index (which evaluates to `false` in a boolean context).

  If more than one Index is found, throws an error.

  <div class="example_clicker">Click to Show Example</div>

       auto s = Index(3,"Site");
       auto l = Index(10,"Link");

       auto T = ITensor(s,l);

       auto x = findIndex(T,"Site");
       if(x) println("Found Index with tag Site: ",x);

       auto y = findIndex(T,"x");
       if(!y) println("T does not have an Index with tag x");

* `commonIndex(ITensor A, ITensor B[, TagSet tags]) -> Index`

  Return the first Index found on both A and B. If A and B
  have no Index in common, returns a default constructed Index
  (which will evaluate to `false` in a boolean context).

  If the optional TagSet `tags` is provided, only a common
  Index of with the specified tags will be returned if found.

  <div class="example_clicker">Click to Show Example</div>

      auto A = ITensor(i,j,k);
      auto B = ITensor(k,m,n);

      auto c = commonIndex(A,B);
      if(c) println("Common Index of A and B is ",c);

* `uniqueIndex(ITensor A, ITensor B[, TagSet tags]) -> Index`

  Return the first Index of A found NOT to be on B.

  If all of A's indices are also present on B, returns a 
  default constructed Index
  (which will evaluate to `false` in a boolean context).

  If the optional string `tags` is provided, only a unique
  Index containing the specified tags will be returned if found.

  <div class="example_clicker">Click to Show Example</div>

      auto A = ITensor(i,j);
      auto B = ITensor(k,j);

      auto u = uniqueIndex(A,B);

      Print(u == i); //prints "true"

* `uniqueInds(ITensor A, ITensor B) -> IndexSet`

  `uniqueInds(ITensor A, std::vector<ITensor> const& B) -> IndexSet`

  `uniqueInds(ITensor A, std::initializer_list<ITensor> B) -> IndexSet`

  Return all indices of A not found in ITensor B (or not found in a vector of ITensors).

* `uniqueIndex(ITensor A, ITensor B[, TagSet tsmatch]) -> Index`

  `uniqueIndex(ITensor A, std::vector<ITensor> B[, TagSet tsmatch]) -> Index`

  `uniqueIndex(ITensor A, std::initializer_list<ITensor> B[, TagSet tsmatch]) -> Index`

  Return the Index of A not found in ITensor B (or not found in a vector of ITensors).
  Optionally, return the unique Index of the specified TagSet `tsmatch`.

  If all of A's indices are also present on the other
  ITensors provided, this function returns a default constructed Index
  (which will evaluate to `false` in a boolean context).

  If more than one Index is found, throw an error (and consider using `uniqueInds` instead).

  <div class="example_clicker">Click to Show Example</div>

      auto A = ITensor(i,j,k,l);
      auto B = ITensor(k,j);
      auto C = ITensor(l);

      auto u = uniqueIndex(A,{B,C});

      Print(u == i); //prints "true"

## Other Functions

* `multSiteOps(ITensor A, ITensor B) -> ITensor`

  Multiply two operators whose index structure follows the
  ITensor convention for operators.

  A and B are expected to have indices with a "Site" tag
  s1, s2, s3, ... and s1', s2', s3', ...
  and no other indices with a "Site" tag.

  This function: 
  1. Increments the prime level of A's "Site"
     indices by 1
  2. Contracts A with B
  3. Maps all "Site" indices with prime level 2
     back to prime level 1.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(3,"Site");
      auto s2 = Index(3,"Site");

      auto A = ITensor(s1,s2,prime(s1),prime(s2));
      auto B = ITensor(s1,s2,prime(s1),prime(s2));

      //...set elements of A and B...

      auto C = multSiteOps(A,B);

      //ASCII art drawing:
      s1'' s2''
       |   |     s1'' s2''       s1'  s2'
       [ A ]      |   |           |   |
       |   |   =  [ C ]     ->    [ C ]
       [ B ]      |   |           |   |
       |   |     s1   s2         s1   s2
      s1   s2  

<a name="replaceinds"></a>
* `.replaceInds(IndexSet is1, IndexSet is2)`
  
  `replaceInds(ITensor T, IndexSet is1, IndexSet is2) -> ITensor`

  Search the input ITensor for the indices in IndexSet `is1`. For any
  Index `i` in `is1` found in the ITensor, replace with the corresponding
  index in `is2` (i.e., if `i` is the 3rd index in `is1` and is found in
  ITensor `T`, it is replaced by `is2(3)`).

  Any indices of the ITensor not listed in `is1` are left unchanged.

  Note that for ITensors with QN conservation, the directions of the
  indices are kept the same as the original ones.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site,s=1");
      auto s2 = Index(2,"Site,s=2");
      auto s3 = Index(2,"Site,s=3");
      auto s4 = Index(2,"Site,s=4");

      auto T12 = randomITensor(s1,prime(s1),s2,prime(s2));

      auto T34 = replaceInds(T12,{s1,s2,prime(s1),prime(s2)},{s3,s4,prime(s3,2),prime(s4,2)});

      //ASCII art drawing:
             
      s1'  s2'   s3'' s4''
       |   |      |   |
       [T12]  ->  [T34] 
       |   |      |   |
      s1   s2    s3   s4
              
<a name="swapinds"></a>
* `.swapInds(IndexSet is1, IndexSet is2)`

  `swapInds(ITensor T, IndexSet is1, IndexSet is2) -> ITensor`

  Swap the indices `is1` with the indices `is2` in the ITensor.

  This is the same as calling `.replaceInds({is1,is2},{is2,is1})`.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site,s=1");
      auto s2 = Index(2,"Site,s=2");

      auto T12 = randomITensor(s1,prime(s1),s2,prime(s2));

      auto T21 = swapInds(T12,{s1,prime(s1)},{s2,prime(s2)});

      //ASCII art drawing:

      s1'  s2'   s2'  s1'
       |   |      |   |
       [T12]  ->  [T21]
       |   |      |   |
      s1   s2    s2   s1


## Advanced / Developer Methods

<!--

* `.scaleTo(Real newscale)` <br/>
  `.scaleTo(LogNum newscale)`

  Rescale the elements of this ITensor such that its scale
  factor equals `newscale`. Up to possible roundoff errors,
  does not change the value of any tensor elements, making
  this method "logically const".

* `.scale() -> LogNum&` 

  Directly access the scale factor.

-->

* `.store() -> storage_ptr&`

  Access the storage pointer, which is of an opaque "box"
  type called `ITData`. Useful for writing new methods
  that "dynamically overload" on the storage type
  using the doTask system.

* `ITensor(IndexSet iset, StorageType&& store, LogNum scale = 1.)` <br/>
  `ITensor(IndexSet iset, storage_ptr&& pstore, LogNum scale = 1.)` <br/>

  Construct an ITensor having IndexSet `iset`, storage `dat`,
  and optional scale. The storage object must be a temporary
  or moved using `std::move`. The type of the storage object
  must be one of the registered types in "itensor/itdata/storage_types.h".

  Alternatively a `storage_ptr` can be passed instead of a storage object.


<br/>
_This page current as of version 3.0.0_
