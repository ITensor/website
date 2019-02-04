# ITensor #


An ITensor is a tensor with named indices (of type [[Index|classes/index]]).
The key feature of the ITensor is automatic contraction over all matching indices, 
similar to Einstein summation.

An ITensor is created with a fixed number of Index objects specifying its indices. 
Because Index objects carry identifying information, most of the 
ITensor interface does not depend on the Index order. For example, 
given an ITensor constructed with indices `a` and `b`, 
calling `T.real(a(2),b(5))` and `T.real(b(5),a(2))` accesses the same tensor element.

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

    phi.set(b1(2),s2(1),s3(2),b3(2), -0.5);
    phi.set(b1(3),s2(2),s3(1),b3(6), 1.4);
    //...

    auto nrm = norm(phi); //save the original norm of phi
    phi /= nrm; //division by a scalar
    Print(norm(phi)); //prints: 1.0

    //The * operator automatically contracts all matching indices.
    //The prime(phi,b3) method primes the b3 Index of the second
    //ITensor in the product so it is not contracted.

    ITensor rho = phi * prime(phi,b3);

    Print(rank(rho)); //prints 2
    Print(hasIndex(rho,b3)); //prints: true
    Print(hasIndex(rho,prime(b3))); //prints: true
    Print(hasIndex(rho,b2)); //prints: false

## Constructors and Accessor Methods

* `ITensor()` 

   Default constructor. <br/>
   A default-constructed ITensor evaluates to false in a boolean context. <br/>
   To construct a rank-zero (scalar) ITensor use the `ITensor(Cplx val)` constructor below.

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

   Construct a rank zero, scalar ITensor with its single component set to val.
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


* `.inds() -> IndexSet const&`

   Return a reference to the indices of this ITensor, as an [[IndexSet|classes/indexset]] container.
   This method is useful for iterating over all of the indices of an ITensor.

   <div class="example_clicker">Click to Show Example</div>

        auto s1 = Index(2,"Site"); 
        auto s2 = Index(2,"Site");
        auto l1 = Index(10,"Link");
        auto l2 = Index(24,"Link");

        auto T = ITensor(l1,s1,s2,l2);

        //Print out just the Link indices of T
        for(auto& I : T.inds())
            {
            if(I.type() == Link) println(I);
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

* `.real(IndexVal iv1, IndexVal iv2, ...) -> Real`

  Return the element of this ITensor corresponding to the provided IndexVals as a Real number.

  An [[IndexVal|classes/indexval]] `iv` is a pairing of an Index `iv.index` and an integer `iv.val`.
  The element returned is the one corresponding to holding `iv1.index` equal to `iv1.val`; `iv2.index` equal
  to `iv2.val`; etc.

  If the element to be accessed as a non-zero imaginary part, this method throws an exception.

  <div class="example_clicker">Click to Show Example</div>

      //Make a scalar ITensor
      auto S = ITensor(2.7);
      //Access its value as a real number
      auto rs = S.real();

      //Make a random rank 3 ITensor
      auto T = ITensor(i,j,k);
      randomize(T);
      //Get one of its elements
      auto rt = T.real(j(2),k(1),i(4));

* `.real(int i1, int i2, ...) -> Real`

  Shorthand notation for `.real` above when the ordering of the indices of the ITensor are known.
  For example, for ITensor T with indices ordered as j,i,k, `T.real(1,2,4)` is equivalent to
  `T.real(j(1),i(2),k(4))`.

  Note that the ordering of the indices of an ITensor can be set using the `order` function
  described below.

  <div class="example_clicker">Click to Show Example</div>

      //Make a random rank 3 ITensor
      auto T = ITensor(i,j,k);
      randomize(T);
      //Order the indices
      T = permute(T,k,i,j);
      //Get one of its elements
      auto rt = T.real(2,1,4); //Equivalent to T.real(k(2),i(1),j(4))

* `.cplx(IndexVal iv1, IndexVal iv2, ...) -> Cplx`

  Return the element of this ITensor corresponding to the provided IndexVals as a Cplx number.

  This method behaves identically to the `.real` method described above, except its return type is a complex
  number. It succeeds whether the ITensor has complex or real storage.

  <div class="example_clicker">Click to Show Example</div>

      //Make a complex scalar ITensor
      auto S = ITensor(2.7-4_i);
      //Access its value as a complex number
      auto zs = S.cplx();

* `.cplx(int i1, int i2, ...) -> Cplx`

  Shorthand notation for `.cplx` above when the ordering of the indices of the ITensor are known.
  For example, for ITensor T with indices ordered as j,i,k, `T.cplx(1,2,4)` is equivalent to
  `T.cplx(j(1),i(2),k(4))`.

  Note that the ordering of the indices of an ITensor can be set using the `order` function
  described below.

* `.set(IndexVal iv1, IndexVal iv2, ... , Cplx z)`

  Set the element of this ITensor corresponding to the provided IndexVals to the value `z`.

  If `z` has exactly zero imaginary part and the ITensor storage is real, it will not be 
  switched to complex storage.

  Because Real numbers are automatically convertible to Cplx, one can plug Real numbers into this method.

  <div class="example_clicker">Click to Show Example</div>

      //Make a rank 3 ITensor
      auto T = ITensor(i,j,k);

      //Set an element to a real number
      T.set(k(2),j(2),i(3),-1.24);

      //Set an element to a complex number
      T.set(k(4),j(1),i(2),3.2-4.7_i);

* `.set(int i1, int i2, ... , Cplx z)`

  Shorthand notation for `.set` above when the ordering of the indices of the ITensor are known.
  For example, for ITensor T with indices ordered as j,i,k, `T.set(1,2,4,3.2)` is equivalent to 
  `T.set(j(1),i(2),k(4),3.2)`.

  Note that the ordering of the indices of an ITensor can be set using the `order` function 
  described below.

  <div class="example_clicker">Click to Show Example</div>

      //Make a rank 3 ITensor
      auto T = ITensor(i,j,k);

      T = permute(T,j,i,k);
      //Set an element to a real number
      T.set(1,2,3,-1.24); 
      Print(T.real(j(1),i(2),k(3)) == -1.24); //prints "true"

<a name="primelev_methods"></a>
## Prime Level Methods

* `prime(ITensor T, int inc = 1) -> ITensor` <br/>
  `prime(ITensor T, int inc = 1, string tags) -> ITensor` <br/>
  `prime(ITensor T, int inc = 1, Index i) -> ITensor`

  Return a new ITensor with the prime level of all indices incremented by 1, or an optional amount 
  `inc`. (Optionally only those containing tags specified by `tags` or only the Index `i`.)
  
* `noPrime(ITensor T) -> ITensor` <br/>
  `noPrime(ITensor T, string tags) -> ITensor` <br/>
  `noPrime(ITensor T, Index i) -> ITensor`

  Set the prime level of all indices to zero. (Optionally only those containing tags specified by `tags` or only the Index `i`.)

* `mapPrime(ITensor T, int plevold, int plevnew)` <br/>
  `mapPrime(ITensor T, int plevold, int plevnew, string tags)` <br/>
  `mapPrime(ITensor T, int plevold, int plevnew, Index i)`

  Return a new ITensor with the prime level of all indices of level `plevold` changed 
  to have level `plevnew`. (Optionally only those containing tags specified by `tags` 
  or only Indices equal to Index `i` when prime levels are ignored.)

  <div class="example_clicker">Click to Show Example</div>

      auto b1 = Index(5,"Link");
      auto b3 = Index(8,"Link");
      auto s2 = Index(2,"Site"); 
      auto s3 = Index(2,"Site");

      auto T = ITensor(b1,prime(b3,2),s2,s3);

      T = mapPrime(T,0,4,"Site");
      T = mapPrime(T,2,5,b3);

      //Now s2 and s3 will have prime level 4
      //and b3 will have prime level 5

* `swapPrime(ITensor T, int plev1, int plev2) -> ITensor` <br/>
  `swapPrime(ITensor T, int plev1, int plev2, string tags) -> ITensor` <br/>
  `swapPrime(ITensor T, int plev1, int plev2, Index i) -> ITensor`

  Return a new ITensor modified such that any
  Index having prime level `plev1` now has `plev2`
  and any Index having prime level `plev2` has `plev1`.
  (Optionally only those containing tags specified by `tags` or only Indices 
  equal to Index `i` when prime levels are ignored.)

  Any Index with a prime level other than `plev1` or `plev2`
  remains unchanged.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,prime(i));

      T.set(i(1),prime(i)(2), 12);
      T.set(i(2),prime(i)(1), 21);

      auto TT = swapPrime(T,0,1);

      Print(T.real(i(1),prime(i)(2))); //prints: 21
      Print(T.real(i(2),prime(i)(1))); //prints: 12


<a name="tag_methods"></a>
## Index Tag Methods

* ```
  replaceTags(ITensor T, string tsold, string tsnew, ...) -> ITensor
  ```

  For any index of this ITensor containing all of the tags in `tsold`, replace
  these tags with those in `tsnew`. 

  Additional optional arguments may be provided. For the complete list of 
  these, see the `.replaceTags` methods of [[IndexSet|classes/indexset#tag_methods]].

* ```
  setTags(ITensor T, string tsnew, ...)
  ```

  Set the tags of the indices of this ITensor to be exactly those in the TagSet `tsnew`.

  Additional optional arguments may be provided. For the complete list of 
  these, see the `.setTags` methods of [[IndexSet|classes/indexset#tag_methods]].

* ```
  addTags(ITensor T, string tsadd, ...)
  ```

  Add the tags in TagSet `tsadd` to the existing tags of 
  the indices of this ITensor.

  Additional optional arguments may be provided. For the complete list of 
  these, see the `.addTags` methods of [[IndexSet|classes/indexset#tag_methods]].

* ```
  removeTags(ITensor T, string tsremove, ...)
  ```

  Remove the tags in TagSet `tsremove` from the existing tags of 
  the indices of this ITensor.

  Additional optional arguments may be provided. For the complete list of 
  these, see the `.removeTags` methods of [[IndexSet|classes/indexset#tag_methods]].

## Operators Supported By ITensors ##

In this section, expressions like `ITensor * ITensor -> ITensor` are pseudocode
indicating that two ITensors can be multiplied using the `*` operator,
and that the result will be an ITensor.

* `ITensor * ITensor -> ITensor` <br/>
  `ITensor *= ITensor`

  Contracting product. `A * B` contracts (sums) over all indices common to A and B. 
  The `*=` version overwrites the ITensor on the left afterward.

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

  When multiplied by an ITensor, a setElt(IndexVal) behaves like a rank-1 (single Index) ITensor
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

      Print(S.real(j(3)) - T.real(i(2),j(3))); //prints: 0.0


## Complex ITensor Methods

* `.conj()`
  
   Complex conjugate each element of this ITensor.

* `.takeReal()`
  
   Replace each element of this ITensor with their real part. Afterwards the ITensor
   will have real storage.

* `.takeImag()`
  
   Replace each element of this ITensor with their imaginary part. Afterwards the ITensor
   will have real storage.

* `.dag()`
  
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

* `randomize(ITensor & T, Args args = Args::global())`

  Randomize all elements the ITensor T. Optimized more for speed than for true randomness.
  Afterward all elements will be real by default.

  Optionally `randomize` accepts a named argument "Complex" which if set to `true`
  will make the ITensor have random complex elements.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);
      randomize(T);
      randomize(T,{"Complex",true});

## Functions for Transforming ITensors

* `apply(ITensor T, Func f) -> ITensor`
  
  Return the ITensor resulting from transforming each element of T by calling `f(x) -> y`. 
  Works similarly to the `.apply` method discussed above but creates a new 
  ITensor instead of modifying an ITensor in-place.

* `permute(ITensor T, Index i1, Index i2, ...) -> ITensor` <br/>

  Given an ITensor T and a list of all of its indices in a particular order,
  return an ITensor with indices in that order.
  The data of the output ITensor is the appropriate permutation of the data 
  of the ITensor T.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);
      randomize(T);

      T = permute(T,j,i,k);

      Print(T.real(1,2,4) == T.real(j(1),i(2),k(4))); //prints "true"

* `random(ITensor T, Args args = Args::global()) -> ITensor`

  Return a new ITensor with the same indices as T but with randomized, real elements.

  Optionally `random` accepts a named argument "Complex" which if set to `true`
  will make the returned ITensor have random complex elements.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k);

      auto RT = random(T);

      auto CT = random(T,{"Complex",true});


* `conj(ITensor T) -> ITensor` <br/>
  `dag(ITensor T) -> ITensor`

  Return the complex conjugate of T.

  `dag(T)` has the same result as `conj(T)` and is defined for interface compatibility with IQTensor.

* `realPart(ITensor T) -> ITensor`

  Return just the real part of an ITensor T.

* `imagPart(ITensor T) -> ITensor`

  Return just the imaginary part of an ITensor T.

## Extracting Properties of ITensors

* `rank(ITensor T) -> long` <br/>
  `order(ITensor T) -> long`

   Return rank or order (number of indices) of the ITensor T.

   <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site");
      auto s2 = Index(2,"Site");
      auto T = ITensor(s1,s2);

      Print(order(T)); //prints: order(T) = 2


* `norm(ITensor T) -> Real`

  Return the Euclidean norm of this ITensor 
  (the square root of the sum of squares of its elements).
  Equivalent to, but much more efficient than, `sqrt((T*T).real())`.
  
  For complex ITensors, it is equivalent to `sqrt((dag(T)*T).cplx().real())`

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

* `hasIndex(ITensor T, Index i) -> bool`

  Returns `true` if ITensor T has an Index exactly matching `i` (including its tags and prime level).

* `findIndex(ITensor T, TagSet tags, [int plev]) -> Index`

  Return the first Index of T that contains tags in `tags`. If no such Index is found, returns
  a default-constructed Index (which evaluates to `false` in a boolean context).

  <div class="example_clicker">Click to Show Example</div>

       auto s = Index(3,"Site");
       auto l = Index(10,"Link");

       auto T = ITensor(s,l);

       auto x = findtype(T,Site);
       if(x) println("Found Site Index ",x);

       auto y = findtype(T,MyType);
       if(!y) println("T does not have a MyType Index");

* `commonIndex(ITensor A, ITensor B[, string tags]) -> Index`

  Return the first Index found on both A and B. If A and B
  have no Index in common, returns a default constructed Index
  (which will evaluate to `false` in a boolean context).

  If the optional string `tags` is provided, only a common
  Index of with the specified tags will be returned if found.

  <div class="example_clicker">Click to Show Example</div>

      auto A = ITensor(i,j,k);
      auto B = ITensor(k,m,n);

      auto c = commonIndex(A,B);
      if(c) println("Common Index of A and B is ",c);

* `uniqueIndex(ITensor A, ITensor B[, string tags]) -> Index`

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

* `uniqueIndex(ITensor A, ITensor B, ITensor C, ...) -> Index`

  Return the first Index of A found NOT to be on the
  ITensors B, C, ... (up to any number of additional tensors provided).

  If all of A's indices are also present on the other
  ITensors provided, this function returns a default constructed Index
  (which will evaluate to `false` in a boolean context).

  <div class="example_clicker">Click to Show Example</div>

      auto A = ITensor(i,j,k,l);
      auto B = ITensor(k,j);
      auto C = ITensor(l);

      auto u = uniqueIndex(A,B,C);

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
      s1' s2'
       |   |     s1' s2'
       [ A ]      |   |
       |   |   =  [ C ] 
       [ B ]      |   |
       |   |     s1  s2
      s1  s2  

<a name="replaceinds"></a>
* `replaceInds(ITensor T, Index old1, Index new1, Index old2, Index new2, ...) -> ITensor`

  Given an ITensor T which has indices `old1`, `old2`, and possibly other indices
  or other copies of `old1` etc. with various prime levels, this function
  returns a new ITensor with the same components but 
  with `old1` replaced by `new1`, `old2` replaced by `new2`, etc. 
  Any other indices of T which are not mentioned in the arguments to
  `replaceInds` are left unchanged.

  <div class="example_clicker">Click to Show Example</div>

      auto s1 = Index(2,"Site");
      auto s2 = Index(2,"Site");
      auto s3 = Index(2,"Site");
      auto s4 = Index(2,"Site");

      auto T12 = ITensor(s1,prime(s1),s2,prime(s2));

      auto T34 = replaceInds(T12,s1,s3,prime(s1),prime(s3),s2,s4,prime(s2),prime(s4));

      //ASCII art drawing:
             
      s1' s2'    s3' s4'
       |   |      |   |
       [T12]  ->  [T34] 
       |   |      |   |
      s1  s2     s3  s4
              


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
