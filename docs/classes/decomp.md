# Tensor Decompositions

Methods for computing decompositions such as the singular value decomposition (SVD), 
Hermitian diagonalization, and density matrix diagonalization.

These methods are defined in "itensor/decomp.h" and "itensor/decomp.cc".

## Synopsis ##

    //
    //Singular value decomposition (SVD)
    //
    auto T = randomTensor(l1,l2,s1,s2);

    //Providing indices of U tells the svd
    //method which indices should end up on U,
    //other indices of psi will go on V

    ITensor U(l1,s1),S,V;
    svd(T,U,S,V);

    Print(norm(T-U*S*V)); //prints: 0.0

    svd(T,U,S,V,{"Cutoff",1E-4});

    Print(sqr(norm(T-U*S*V)/norm(T))); //prints: 1E-4

    //
    //Eigenvalue decomposition
    //of Hermitian tensors
    //
    //Assumes matching pairs of indices
    //with prime level 0 and 1
    //

    auto rho = ITensor(s1,s2,prime(s1),prime(s2));
    //...set elements of rho...

    ITensor U,D;
    diagHermitian(rho,U,D);

    Print(norm(rho-prime(U)*D*dag(U))); //prints: 0.0


## Singular Value Decomposition Algorithms

* ```
  svd(ITensor T, ITensor & U, ITensor & S, Tensor & V, 
      Args args = Args::global())
  ```
  ```
  svd(IQTensor T, IQTensor & U, IQTensor & S, Tensor & V, 
      Args args = Args::global())
  ```

  Compute the singular value decomposition of a tensor T.
  The arguments U, S, and V are overwritten, and the product `U*S*V` equals T.
  
  *Returns*: [[Spectrum|classes/spectrum]] object containing information about truncation and singular values.
  
  To determine which indices should be grouped together as the "row" indices and thus end up on 
  the final U, versus the remaining "column" indices which end up on the final V, the svd 
  function inspects U. All index common to both U and T are considered "row" indices 
  (other indices of U are ignored). If U has no indices, the svd function inspects the indices of V.
  
  The svd function also recognizes the following optional named arguments:
  
  * "Maxm" &mdash; integer M. If there are more than M singular values, only the largest M are kept.
  
  * "Cutoff" &mdash; real number @@\epsilon@@. Discard the smallest singular values
     @@\lambda\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
     $$
     \frac{\sum\_{n\in\text{discarded}} \lambda^2\_n}{\sum\_{n} \lambda^2\_n} < \epsilon \:.
     $$
  
  * "Minm" &mdash; integer m. At least m singular values will be kept, even if they fall below the cutoff.
  
  * "Truncate" &mdash; if set to `false`, no truncation occurs. Otherwise truncation parameters ("Cutoff",
    "Maxm", "Minm") will be used to perform a truncation of singular values.
  
  * "ShowEigs" &mdash; if `true`, print lots of extra information about the truncation of singular values.
    Default is `false`.
  
  * "SVDThreshold" &mdash; real number less than 1.0; default is 1e-3. If the ratio of any singular values to the largest
    value fall below this number, the SVD algorithm will be recursively applied to the part of the matrix 
    containing these small values to achieve better accuracy. Setting this number larger can make the SVD more accurate
    if the singular values decrease very rapidly.
  
  * "LeftIndexName" &mdash; set the name of the index connecting S to U.
  
  * "RightIndexName" &mdash; set the name of the index connecting S to V.
  
  * "IndexType" &mdash; set the IndexType of the indices of S connecting to U and V.
  
  * "LeftIndexType" &mdash; set just the IndexType of the index connecting S to U.
  
  * "RightIndexType" &mdash; set just the IndexType of the index connecting S to V.
     
  <!---->
  
  <div class="example_clicker">Click to Show Example</div>
  
      auto s1 = Index("Site 1",2,Site);
      auto s2 = Index("Site 2",2,Site);
      auto l1 = Index("Link 1",4,Link);
      auto l2 = Index("Link 1",4,Link);
  
      auto T = randomTensor(l1,s1,s2,l2);
  
      //want l1, s1 to end up on U
      auto U = ITensor(l1,s1);
      //ok to leave S and V uninitialized
      ITensor S,V;
  
      //compute exact SVD
      svd(T,U,D,V);
  
      Print(norm(T-U*D*V)); //prints: 0.0
  
      //compute approximate SVD
      svd(T,U,D,V,{"Cutoff",1E-9});
  
      Print(sqr(norm(T-U*D*V)/norm(T))); //prints: 1E-9

* ```
  factor(ITensor T, ITensor & A, ITensor & B, 
         Args args = Args::global())
  ```
  ```
  factor(IQTensor T, IQTensor & A, IQTensor & B, 
         Args args = Args::global())
  ```

  The "factor" decomposition is based on the SVD,
  but factorizes a tensor T into only two
  tensors `T==A*B` where A and B share a single
  common index.
  
  If the SVD of T is `T==U*S*V` where S is a diagonal
  matrix of singular values, then A and B
  are schematically `A==U*sqrt(S)` and `B==sqrt(S)*V`.

  To decide which indices of T should go on the final A
  versus B, the code first inspects A for any common indices
  it shares with T; if found all of these indices go on A 
  afterward with the rest on B. Otherwise B is used to
  determine how to split the indices.
  
  In addition to the named Args recognized by the 
  svd routine, factor accepts an Arg "IndexName"
  which will be the name of the common index 
  connecting A and B.

  <div class="example_clicker">Click to Show Example</div>

      auto T = ITensor(i,j,k,l);
      //...set elements of T...

      //putting i,k on A tells
      //factor to keep these on A,
      //put j,l on B
      auto A = ITensor(i,k);
      ITensor B; //uninitialized

      factor(T,A,B);

      Print(norm(T-A*B)); //prints: 0.0

## Hermitian Matrix Algorithms

* ```
  diagHermitian(ITensor H, ITensor & U, ITensor & D, 
                Args args = Args::global()) -> Spectrum
  ```

  ```
  diagHermitian(IQTensor H, IQTensor & U, IQTensor & D, 
                Args args = Args::global()) -> Spectrum
  ```

  Diagonalize a Hermitian tensor T such that `T==dag(U)*D*prime(U)`. Tensors U and D are 
  passed by reference and overwritten upon return.

  The method assumes that the indices of T come in pairs, one index with prime level 0 and a 
  the same index but with prime level 1 (reflecting the Hermitian nature of T). 
  For example, T could have indices i,i',j,j'. 
  Saying that T is Hermitian means that `T == dag(swapPrime(T,0,1))`.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index("i",2);
      auto j = Index("j",4);

      T = randomTensor(i,j,prime(i),prime(j));

      //Make T Hermitian
      T = T + swapPrime(T,0,1);

      ITensor U,D;
      diagHermitian(T,U,D); 

      Print((T-dag(U)*D*prime(U)).norm()); //prints: 0.0

<!--

## Density Matrix Decomposition ##

* `denmatDecomp(Tensor T, Tensor& A, Tensor& B, Direction dir, OptSet opts = Global::opts())`

   *Returns*: `Spectrum` object containing density matrix eigenvalues.

   Factorize a Tensor T into products A and B such that `T==A*B`. "Tensor" is a templated type and could be e.g. ITensor or IQTensor. A and B are passed by reference and overwritten to hold the results. If `dir==Fromleft` the tensor A will be unitary ("left orthogonal") in the sense that A times the conjugate of A summed over all indices not in common with B will produce an identity (Kronecker delta) tensor. If `dir==Fromright` B will be unitary ("right orthogonal"). The result of this method is equivalent to computing an SVD of T such that `T==U*D*V` then setting `A=U` and `B=D*V` assuming `dir==Fromleft`. (If `dir==Fromright` it would be equivalent to setting `A=U*D` and `B=V`.) However, the implementation is different from the SVD (see below).

   To determine which indices of T should end up on A versus B, the method inspects the initial indices of A (or B if A is default constructed) and keeps the same indices on A upon return, with the rest of the indices going onto B. (This is similar to how the `svd` method above works.)

   Although the results of this method are related to the SVD, the implementation is different. Rather than performing an SVD, the method computes a "density matrix" from T (using an analogy where T is a wave function, which may or may not actually be the case) and diagonalizes this density matrix. Two key reasons for doing this in contrast to just an SVD are computational efficiency and having the ability to implement the DMRG noise term (see the last version of `denmatDecomp` below).

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor A(l1,s1), //want l1, s1 to end up on A
                B;

        denmatDecomp(T,A,B,Fromleft); //decompose T into A*B

        Print((T-A*B).norm()); //prints 0


* `denmatDecomp(Tensor T, Tensor& A, Tensor& B, Direction dir, LocalOpT PH, OptSet opts = Global::opts())`

   *Returns*: `Spectrum` object containing density matrix eigenvalues.

   Factorize a Tensor T, truncating the density matrix eigenvalues (equivalent to the squares of the singular values) according to the parameters contained in the [[Spectrum|classes/spectrum]] instance `spec`. Also add a noise term constructed out of the projected Hamiltonian `PH` with strength given by `spec.noise()`. For more information on the noise term see [Density matrix renormalization group algorithms with a single center site](http://prb.aps.org/abstract/PRB/v72/i18/e180403), S.R.&nbsp;White, <i>Phys.&nbsp;Rev.&nbsp;B</i> *72*, 180403(R) (2005).

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor A(l1,s1), //want l1, s1 to end up on A
                B;

        //Create a OptSet object to control the truncation
        OptSet opts;
        opts.add("Cutoff",1E-8);
        opts.add("Maxm",100);
        opts.add("Noise",1E-10); //set the noise level to 1E-10

        //Given an appropriately constructed Hamiltonian MPO H,
        //create a projected Hamiltonian
        LocalMPO<ITensor> PH(H);
        //...may have to call position method of PH to correctly initialize...

        denmatDecomp(T,A,B,Fromleft,PH,opts); //add noise term to T, factorize,and truncate

        Print((T-A*B).norm()); //prints a small number since we truncated

## Hermitian Diagonalization ##

* `diagHermitian(Tensor T, Tensor& U, Tensor& D, OptSet opts = Global::opts())`

   *Returns*: `Spectrum` object containing eigenvalues of T.

   Diagonalize a Hermitian Tensor T such that `T==dag(U)*D*prime(U)`. "Tensor" is a templated type and could be e.g. ITensor or IQTensor. U and D are passed by reference and overwritten on return.

   The method assumes that the indices of T come in pairs, one index with prime level 0 and a matching index with prime level 1 (reflecting the Hermitian nature of T). For example, T could have indices i,i',j, and j'. Saying that T is Hermitian means that `T == dag(swapPrime(T,0,1))`.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site);

        ITensor T(s1,s2,prime(s1),prime(s2));
        T.randomize();

        T = T + swapPrime(T,0,1);

        ITensor U,D;

        diagHermitian(T,U,D); 

        Print((T-dag(U)*D*prime(U)).norm()); //prints 0

## Orthogonal (Real) Factorization ##

* `orthoDecomp(Tensor T, Tensor& A, Tensor& B, Direction dir, OptSet opts = Global::opts())`

   *Returns*: `Spectrum` object containing density matrix eigenvalues.

   Factorize a Tensor T such that `T==A*B`. "Tensor" is a templated type and could be e.g. ITensor or IQTensor. A and B are passed by reference and overwritten on return.

   The orthoDecomp method is somewhat similar to denmatDecomp above, in that setting `dir==Fromleft` guarantees A is left orthogonal, except that orthoDecomp provides the additional guarantee that A is real (and similarly for B if `dir==Fromright`). This may come at the cost of a higher bond dimension of the common index of A and B.

   To determine which indices of T appear on A versus B after the factorization, orthoDecomp inspects the initial value of A and B when the method is called and keeps the initial indices of A on A (or inspects B if A is null) and puts the rest on B.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor A(l1,s1), //want l1, s1 to end up on A
                B;

        orthoDecomp(T,A,B,Fromleft); //factorize T such that A is real orthogonal

        Print(A.isComplex()); //prints 0 (false)
        Print((T-A*B).norm()); //prints 0


## Inverse Singular Value Decomposition ##

* `csvd(Tensor T, Tensor& L, Tensor& V, Tensor& R, OptSet opts = Global::opts())`

   *Returns*: `Spectrum` object containing density matrix eigenvalues.

   Compute the "inverse" singular value decomposition of a Tensor T. "Tensor" is a templated type and could be e.g. ITensor or IQTensor. On return, the arguments L, V, and R are overwritten to hold the resulting factors such that `T==L*V*R`.

   The inverse SVD works similarly to the normal SVD method defined above (and uses the same implementation), but on return the factor V is set to the inverse of the singular value matrix D. The tensors L and R are constructed from the unitaries computed by the SVD times an extra factor of D.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor L(l1,s1), //want l1, s1 to end up on U
                V,R;

        csvd(T,L,V,R); //compute inverse SVD

        Print((T-L*V*R).norm()); //prints 0


-->
