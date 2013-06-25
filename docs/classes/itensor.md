#ITensor#

The foundational tensor type of the ITensor Library; the key feature of the ITensor is automatic contraction over all matching indices. 

An ITensor is created with a fixed
number of Index objects specifying its indices. Because each Index has a unique id, the
ITensor interface does not depend on a specific Index order. For example, 
given an ITensor constructed with indices `a` and `b`, `T(a(2),b(5))` and `T(b(5),a(2))` refer to the same component.

##Synopsis##

    Index b1("bond 1",5), b3("bond 3",8),
          s2("Site 2",2,Site), s3("Site 3",2,Site);

    ITensor phi(b1,s2,s3,b3);

    phi(b1(2),s2(1),s3(2),b3(2)) = -0.5;
    phi(b1(3),s2(2),s3(1),b3(6)) = 1.4;
    ...

    Real nrm = phi.norm(); //save the original norm of phi
    phi /= phi.norm(); //division by a scalar
    Print(phi.norm()); //Prints 1.0

    //The * operator automatically contracts over 
    //matching indices b1, s2, and s3.
    //The primed method primes the b3 Index of the second
    //ITensor in the product so it is not summed over 

    ITensor rho = phi * conj(primed(phi,b3));

    Print(rho.r()); //prints 2
    Print(hasindex(rho,b3) ? "true" : "false"); //prints "true"
    Print(hasindex(rho,primed(b3)) ? "true" : "false"); //prints "true"
    Print(hasindex(rho,b2) ? "true" : "false"); //prints "false"

    Print(trace(rho,b3,primed(b3))); //Prints 1.0

##Constructors##

* `ITensor()` 

   Default constructor. For a default-constructed ITensor `T`, `T.isNull() == true`. To construct a rank zero ITensor use the `ITensor(Real val)` constructor below.

* `ITensor(Index i1)` 

  `ITensor(Index i1, Index i2)` 

  `ITensor(Index i1, Index i2, Index i3)` 

   ... etc. up to 8 indices 

   Construct an ITensor with the given indices. All components are initialized to zero.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), s2("Site 2",2,Site);
        ITensor T(s1,s2);
        Print(T.r()); //Prints 2, the rank of T
        Print(T.norm()); //Prints 0

* `ITensor(Real val)` 

   Construct a rank zero, scalar ITensor with single component set to val.

* `ITensor(IndexVal iv1)` 

  `ITensor(IndexVal iv1, IndexVal iv2)` 

  `ITensor(IndexVal iv1, IndexVal iv2, IndexVal iv3)` 

   ... etc. up to 8 IndexVals 

   Construct an ITensor with indices `iv1.ind`, `iv2.ind`, etc., such that the component corresponding to `iv1.i`, `iv2.i`, etc. is equal to 1 and all other components are equal to zero. For example, constructing an ITensor `T` by calling `ITensor T(a(1),b(2),c(3));` makes all components of T zero except for `T(a(1),b(2),c(3))==1`.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site);

        ITensor T(s1(2),s2(2));
        Print(T(s1(2),s2(2)); // Prints 1
        Print(T(s1(1),s2(2)); // Prints 0, similarly for other components


##Element Access Methods##

* `Real& operator()(IndexVal iv1, IndexVal iv2, ...)` 

   Access component of this ITensor such that `i1.ind` is set to value `i1.i`, `i2.ind` to `i2.i`, etc. For example, given a matrix-like ITensor `M` with indices `r` and `c`, can access the (2,1) component by calling `M(r(2),c(1))`. Result is independent of the order of the arguments and depends only on the set of IndexVals provided. For the previous example, `M(r(2),c(1)) == M(c(1),r(2))`.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              la("link A",4,Link);

        ITensor T(s1,s2,la);
        T(s1(1),s2(1),la(3)) = 0.113;
        T(s1(2),s2(1),la(4)) = -0.214;
        Print(T(s1(1),s2(1),la(3))); //Prints 0.113
        Print(T(s2(1),s1(1),la(3))); //Also prints 0.113
        Print(T(la(4),s1(2),s2(1))); //Prints -0.214

* `Real toReal()` 

  Return value of a rank zero, scalar ITensor. If the ITensor has rank greater than zero or if ITensor is complex (see below), throws an exception.

  <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              la("link A",4,Link);

        ITensor T(s1,s2,la);
        T(s1(1),s2(1),la(3)) = 0.113;
        T(s1(2),s2(1),la(4)) = -0.214;

        ITensor T2 = T * T; //Calculate T squared - contracts over all indices
        Print(T2.r()); //Prints 0: T2 is a scalar
        Print(T2.toReal()); //Prints 0.058565, the squared norm of T


* `Complex toComplex()`

  Return value of a complex, scalar (rank zero) ITensor. If the ITensor has rank greater than zero, throws an exception.

##Operators##

* `ITensor& operator*=(const ITensor& other)`

  ITensor contracting product. A*B contracts over all Index pairs in common between A and B. 

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        ITensor A(l1,s2,s3,l3);
        //set components of A ...

        ITensor B(l1,s2,primed(s3),primed(l3));
        //set components of B ...

        ITensor R = A * B; //Contracts over l1 and s2

        Print(R.r()); //Prints 4, rank of R
        Print(hasindex(R,s3)); //Prints 1 (true)
        Print(hasindex(R,l3)); //Prints 1 (true)
        Print(hasindex(R,primed(s3))); //Prints 1 (true)
        Print(hasindex(R,primed(l3))); //Prints 1 (true)
        Print(hasindex(R,l1)); //Prints 0 (false)

* `ITensor& operator+=(const ITensor& other)`

  `ITensor& operator-=(const ITensor& other)`

  (and related free methods)

  ITensor addition and subtraction. Adds ITensors element-wise. Both ITensors must have the same set of indices.

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        ITensor A(l1,s2,s3,l3),
                B(l1,s2,s3,l3);
        //set components of A and B...

        ITensor S = A + B; //sum A and B
        ITensor D = A - B; //subtract B from A

* `ITensor& operator*=(Real fac)`

  `ITensor& operator/=(Real fac)`

  `ITensor operator-()`

  (and related free methods)

  Multiplication by a real scalar, division by a real scalar, and negation. Factor is applied to all elements of the ITensor
  (handled lazily internally).

* `ITensor& operator*=(Complex z)`

  Multiplication by a Complex scalar (where Complex is a typedef for std::complex<Real>). Useful for creating complex ITensors
  by using the idiom `ITensor T = A + B*Complex_i` where A and B are real ITensors and Complex_i is a constant equal to
  Complex(0,1).

  <div class="example_clicker">Show Example</div>

        //Create a random complex ITensor T

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        ITensor A(l1,s2,s3,l3),
                B(l1,s2,s3,l3);
        A.randomize();
        B.randomize();

        ITensor T = A+B*Complex_i;

        Print((realPart(T)-A).norm()); //prints zero
        Print((imagPart(T)-B).norm()); //prints zero

##Prime Level Methods##

* `ITensor& prime(int inc = 1)`

  Increment prime level of all indices by 1. (Optionally by amount `inc`.) Returns a reference to the modified ITensor.

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        ITensor A(l1,s2,s3,l3);

        A.prime();
        Print(hasindex(A,primed(s2))); //Prints 1 (true)
        Print(hasindex(A,s2));         //Prints 0 (false)
        Print(hasindex(A,primed(s3))); //Prints 1 (true)
        Print(hasindex(A,primed(l1))); //Prints 1 (true)
        Print(hasindex(A,primed(l3))); //Prints 1 (true)

* `ITensor& prime(Index I, int inc = 1)`

  Increment prime level of only Index `I` by 1. (Optionally by amount `inc`.)
  Throws an exception of ITensor does not have Index `I`. Returns a reference to the modified ITensor.

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        ITensor A(l1,s2,s3,l3);

        A.prime(s3);
        Print(hasindex(A,primed(s3))); //Prints 1 (true)
        Print(hasindex(A,s3));         //Prints 0 (false)
        Print(hasindex(A,primed(s2))); //Prints 0 (false)
        Print(hasindex(A,primed(l1))); //Prints 0 (false)
        Print(hasindex(A,primed(l3))); //Prints 0 (false)
        Print(hasindex(A,s2));         //Prints 1 (true)
        //etc.

* `ITensor& prime(IndexType t, int inc = 1)`

  Increment prime level of every Index of type `t`. (Optionally by amount `inc`.) Returns a reference to the modified ITensor.

  <div class="example_clicker">Show Example</div>

        Index l1("link 1",4),
              s2("Site 2",2,Site), 
              s3("Site 3",2,Site),
              l3("link 3",4);

        ITensor A(l1,s2,s3,l3);

        A.prime(Site);
        Print(hasindex(A,primed(s2))); //Prints 1 (true)
        Print(hasindex(A,s2));         //Prints 0 (false)
        Print(hasindex(A,primed(s3))); //Prints 1 (true)
        Print(hasindex(A,l1));         //Prints 1 (true)

* `ITensor& noprime(IndexType t = All)`

  Set prime level of all indices to 0. (Optionally only indices of type `t`.) Returns a reference to the modified ITensor.

* `ITensor& noprime(Index I)`

  Set prime level of Index `I` to 0. Throws an exception if ITensor does not have Index `I`. Returns a reference to the modified ITensor.

* `ITensor& mapprime(int plevold, int plevnew, IndexType t = All)`

  Change prime level of all indices having prime level `plevold` to `plevnew`. (Optionally only if their type matches `t`.) 
  Returns a reference to the modified ITensor.

##Miscellaneous Methods##

* `void randomize()`

  Randomize all elements of this ITensor. Optimized more for speed than for true randomness.

* `Real norm()`

  Return the norm of this ITensor, that is, the Euclidean norm when treating the ITensor as a vector.
  Equivalent to, but much more efficient than, `sqrt((T*T).toReal())` for some real ITensor `T`.

* `ITensor& takeRealPart()`
    
  Set an ITensor to its real part, dropping its imaginary part. Returns a reference to the resulting ITensor.

* `ITensor& takeImagPart()`
    
  Set an ITensor to its imaginary part, dropping its real part. Returns a reference to the resulting ITensor.

[[Back to Classes|classes]]

[[Back to Main|main]]
