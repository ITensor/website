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
     <span>&nbsp;</span>
  
  * "Minm" &mdash; integer m. At least m singular values will be kept, even if the cutoff criterion would discard more.
  
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
         Args args = Args::global()) -> Spectrum
  ```
  ```
  factor(IQTensor T, IQTensor & A, IQTensor & B, 
         Args args = Args::global()) -> Spectrum
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

      //Make Hermitian tensor out of T
      auto H = T + swapPrime(T,0,1);

      ITensor U,D;
      diagHermitian(H,U,D); 

      Print((H-dag(U)*D*prime(U)).norm()); //prints: 0.0

   The diagHermitian function recognizes the following optional named arguments:
   
   * "Maxm" &mdash; integer M. If there are more than M eigenvalues, only the largest M are kept.

   * "Cutoff" &mdash; real number @@\epsilon@@. Discard the smallest eigenvalues
      @@p\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
      $$
      \frac{\sum\_{n\in\text{discarded}} p\_n}{\sum\_{n} p\_n} < \epsilon \:.
      $$
      <span>&nbsp;</span>

   * "Minm" &mdash; integer m. At least m eigenvalues will be kept, even if the cutoff criterion would discard more.

   * "IndexName" &mdash; string. Specify the name of the new index shared between U and D.

   * "ShowEigs" &mdash; if `true`, print lots of extra information about the truncation of singular values.

   * "Truncate" &mdash; if set to `false`, no truncation occurs. Otherwise truncation parameters ("Cutoff","Maxm", "Minm") will be used to perform a truncation of singular values.

   <br/>

* `expHermitian(ITensor H, Cplx tau = 1) -> ITensor` <br/>
  `expHermitian(IQTensor H, Cplx tau = 1) -> IQTensor`

  Given a Hermitian tensor H, with matching pairs of indices (one with prime level zero, the other 
  with prime level 1), returns the exponential of this tensor.

  Optionally a factor `tau` can be included in the exponent. If `tau` has zero imaginary
  part and the tensor H is real, the returned tensor will also be real.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index("i",2);
      auto j = Index("j",4);

      T = randomTensor(i,j,prime(i),prime(j));

      //Make Hermitian tensor out of T
      auto H = T + swapPrime(T,0,1);

      // compute exp(i * H)
      auto expiH = expHermitian(H,1_i);

      // compute exp(2 * H)
      auto exp2H = expHermitian(H,2);

   <br/>

* ```
  denmatDecomp(ITensor T, ITensor & A, ITensor & B, 
               Direction dir, Args args = Args::global()) -> Spectrum
  ```
  ```
  denmatDecomp(IQTensor T, IQTensor & A, IQTensor & B, 
               Direction dir, Args args = Args::global()) -> Spectrum
  ```

   Factorize a tensor T into products A and B such that `T==A * B`. 
   A and B are passed by reference and overwritten to hold the results. 

   _Returns_: [[Spectrum|classes/spectrum]] object containing information about truncation 
   and density matrix eigenvalues.

   To determine which indices of T should end up on A versus B, the method inspects the 
   initial indices of A (or B if A is default constructed) and keeps the same 
   indices on A upon return, with the rest of the indices going onto B. 
   (This is similar to how the `svd` method above works.)

   If `dir==Fromleft` the tensor A will be "left orthogonal" in the sense that A times the 
   conjugate of A summed over all indices not in common with B will produce an identity 
   (Kronecker delta) tensor. If `dir==Fromright` B will be unitary ("right orthogonal"). 
   
   If `dir==Fromleft`, the result of this method is equivalent to computing an SVD of T 
   such that `T==U * D * V` then setting `A=U` and `B=D * V`. 
   (If `dir==Fromright` it would be equivalent to setting `A=U * D` and `B=V`.) 

   Although the results of this method are related to the SVD, the implementation 
   is different.  Rather than performing an SVD, the method computes a "density matrix" from T 
   (using an analogy where T is a wave function, which may or may not actually be the case) 
   and diagonalizes this density matrix. Two key reasons for doing this versus an SVD
   are computational efficiency and having the ability to implement the DMRG 
   noise term (see the next version of `denmatDecomp` below).

   To compute a truncated version of this decomposition, pass one or both of the
   named arguments "Cutoff" or "Maxm" described below.

   The denmatDecomp function recognizes the following optional named arguments:
   
   * "Maxm" &mdash; integer M. If there are more than M eigenvalues, only the largest M are kept.

  * "Cutoff" &mdash; real number @@\epsilon@@. Discard the smallest eigenvalues
     @@p\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
     $$
     \frac{\sum\_{n\in\text{discarded}} \  p\_n}{\sum\_{n} p\_n} < \epsilon \:.
     $$
     <span>&nbsp;</span>

  * "Minm" &mdash; integer m. At least m singular values will be kept, even if they fall below the cutoff.
  
  * "Truncate" &mdash; if set to `false`, no truncation occurs. Otherwise truncation parameters ("Cutoff",
    "Maxm", "Minm") will be used to perform a truncation of singular values.
  
  * "ShowEigs" &mdash; if `true`, print lots of extra information about the truncation of singular values.
    Default is `false`.

  <div class="example_clicker">Click to Show Example</div>

      auto T = randomTensor(l1,s1,s2,l2);

      auto A = ITensor(l1,s1); //want l1, s1 to end up on A
      ITensor B;
      denmatDecomp(T,A,B,Fromleft); //decompose T into A * B

      Print(norm(T-A*B)); //prints: 0

   <br/>

* ```
  template<class BigMatrixT>
  denmatDecomp(ITensor T, ITensor & A, ITensor & B, 
               Direction dir, 
               BigMatrixT PH,
               Args args = Args::global()) -> Spectrum
  ```
  ```
  template<class BigMatrixT>
  denmatDecomp(IQTensor T, IQTensor & A, IQTensor & B, 
               Direction dir, 
               BigMatrixT PH,
               Args args = Args::global()) -> Spectrum
  ```

  Identical to denmatDecomp function described above, except before the decomposition the density matrix
  formed from T has the "noise term" added to it. For more information on the noise term see the paper
  [Density matrix renormalization group algorithms with a single center site](http://prb.aps.org/abstract/PRB/v72/i18/e180403), 
  S.R.&nbsp;White, <i>Phys.&nbsp;Rev.&nbsp;B</i> *72*, 180403(R) (2005).

  For the PH object to implement the noise term, it must provide the `deltaRho` method. For more information
  see the documentation on [[LocalOp|classes/localop]].

  Named arguments recognized:

  * "Noise" &mdash; real number. Coefficient of noise term; default is 0.

<!--

* `orthoDecomp(Tensor T, Tensor& A, Tensor& B, Direction dir, Args args = Args::global())`

   *Returns*: `Spectrum` object containing density matrix eigenvalues.

   Factorize a tensor T such that `T==A * B`.

   The orthoDecomp method is somewhat similar to denmatDecomp above, in that setting `dir==Fromleft` 
   guarantees A is left orthogonal, except that orthoDecomp provides the additional guarantee that 
   A is real (and similarly for B if `dir==Fromright`). This may come at the cost of a higher 
   bond dimension of the common index of A and B.

   To determine which indices of T appear on A versus B after the factorization, orthoDecomp 
   inspects the initial value of A and B when the method is called and keeps 
   the initial indices of A on A (or inspects B if A is null) and puts the rest on B.

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


-->

<!--

To add:

* eigen

-->

<br/>
_This page current as of version 2.0.10_
