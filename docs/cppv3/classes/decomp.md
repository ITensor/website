# Tensor Decompositions

Methods for computing decompositions such as the singular value decomposition (SVD), 
Hermitian diagonalization, and density matrix diagonalization.

These methods are defined in "itensor/decomp.h" and "itensor/decomp.cc".

## Synopsis ##

    auto l1 = Index(12,"l1");
    auto l2 = Index(12,"l2");
    auto s1 = Index(4,"s1");
    auto s2 = Index(4,"s2");

    //
    //Singular value decomposition (SVD)
    //
    auto T = randomITensorC(l1,l2,s1,s2);

    //The IndexSet specifies which indices
    //of T will end up on U.
    //The output is a tuple of the ITensors
    //of the decomposition and the new
    //indices created in the decomposition

    auto [U,S,V,u,v] = svd(T,{l1,s1});

    Print(norm(T-U*S*V)); //On the order of 1E-15

    std::tie(U,S,V,u,v) = svd(T,{l1,s1},{"Cutoff",1E-4});

    Print(sqr(norm(T-U*S*V)/norm(T))); //On the order of 1E-4

    //
    //Eigenvalue decomposition
    //of Hermitian tensors
    //
    //Assumes matching pairs of indices
    //with prime level 0 and 1
    //

    auto H = randomITensorC(s1,s2,prime(s1),prime(s2));
    H = 0.5*(H+dag(swapTags(H,"0","1")));

    auto [Q,D,q] = diagHermitian(H);

    Print(norm(H-prime(Q)*D*dag(Q))); //On the order of 1E-15


## Singular Value Decomposition

* ```
  svd(ITensor T, IndexSet Uis[, IndexSet Vis],
      Args args = Args::global()) -> std::tuple<ITensor,ITensor,ITensor,Index,Index>
  ```

  Compute the singular value decomposition of an ITensor `T`. A tuple of the `U`, `S` and `V` 
  tensors of the decomposition, as well as the newly introduced indices u and v, is returned.
  The product `U*S*V` is equal to T (up to truncation errors), and u (v) is the common index 
  between U (V) and S.
  
  An IndexSet `Uis` is input along with `T` to specify which Indices of `T` end up
  on the `U` tensor of the decomposition, and the rest of the indices end up on the
  `V` tensor.

  Optionally, the indices ending up on the output tensor `V` can be explicitly specified
  by the IndexSet `Vis`. In this case, an extra check is added that the union of the `Uis`
  indices and `Vis` indices are the same as the indices on `T`.

  The svd function also recognizes the following optional named arguments:
  
  * "MaxDim" &mdash; integer M. If there are more than M singular values, only the largest M are kept.
  
  * "Cutoff" &mdash; real number @@\epsilon@@. Discard the smallest singular values
     @@\lambda\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
     $$
     \frac{\sum\_{n\in\text{discarded}} \lambda^2\_n}{\sum\_{n} \lambda^2\_n} < \epsilon \:.
     $$
     <span>&nbsp;</span>
  
  * "MinDim" &mdash; integer M. At least M singular values will be kept, even if the cutoff criterion would discard more.
  
  * "Truncate" &mdash; if set to `false`, no truncation occurs. Otherwise truncation parameters ("Cutoff",
    "MaxDim", "MinDim") will be used to perform a truncation of singular values.
  
  * "ShowEigs" &mdash; if `true`, print lots of extra information about the truncation of singular values.
    Default is `false`.
  
  * "SVDThreshold" &mdash; real number less than 1.0; default is 1e-3. If the ratio of any singular values to the largest
    value fall below this number, the SVD algorithm will be recursively applied to the part of the matrix 
    containing these small values to achieve better accuracy. Setting this number larger can make the SVD more accurate
    if the singular values decrease very rapidly.
  
  * "LeftTags" &mdash; set just the tags of the index connecting S to U.
  
  * "RightTags" &mdash; set just the tags of the index connecting S to V.
     
  * "TruncateDegenerate" &mdash; if `true`, degenerate subspaces will be respected (i.e., if the the truncation lies within a set of degenerate singular values based on a numerical threshold, the degenerate subspace will either be entirely truncated or kept, depending on the other argument options).
    Default is `false`.

  <div class="example_clicker">Click to Show Example</div>
  
      auto s1 = Index(4,"Site");
      auto s2 = Index(4,"Site");
      auto l1 = Index(12,"Link");
      auto l2 = Index(12,"Link");
  
      auto T = randomITensor(l1,s1,s2,l2);
  
      //Compute SVD without truncation
      //Specify we want l1, s1 to end up on U
      auto [U,S,V,u,v] = svd(T,{l1,s1});
  
      Print(u == commonIndex(U,S)); //prints: true
      Print(v == commonIndex(V,S)); //prints: true
      Print(norm(T-U*S*V)); //prints on order of 1E-15
  
      //compute approximate SVD
      std::tie(U,S,V,u,v) = svd(T,{l1,s1},{"Cutoff",1E-4});
  
      Print(sqr(norm(T-U*S*V)/norm(T))); //prints on order of 1E-4

## Hermitian Diagonalization

* ```
  diagHermitian(ITensor H,
                Args args = Args::global()) -> std::tuple<ITensor,ITensor,Index>
  ```

  Diagonalize an ITensor T the can be interpreted as a Hermitian matrix under appropriate
  grouping of indices.
  Results in an ITensor `U` of orthonormal eigenvectors and diagonal ITensor `D` of real
  eigenvalues such that `T==dag(U)*D*prime(U)`. Also return the Index `u` shared by `U`
  and `D`. `D` contains indices `u` and `prime(u)`.

  The method assumes that the indices of T come in pairs, one index with prime level 0 and a 
  the same index but with prime level 1 (reflecting the Hermitian nature of T). 
  For example, T could have indices {i,i',j,j'}. 
  Saying that T is Hermitian means that `T == swapTags(dag(T),"0","1")`.

   The `diagHermitian` function recognizes the following optional named arguments:
   
   * "Tags" &mdash; TagSet. Specify the tags of the index shared by U and D.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(2);
      auto j = Index(4);

      auto T = randomITensorC(i,j,prime(i),prime(j));

      //Make Hermitian tensor out of T
      auto H = T + swapTags(dag(T),"0","1");

      auto [U,D,u] = diagHermitian(H); 

      Print(u == commonIndex(U,D)); //prints: true
      Print(hasInds(D,{u,prime(u)})); //prints: true
      Print(norm(H-dag(U)*D*prime(U))); //prints on the order of 1E-15

* ```
  diagPosSemiDef(ITensor H,
                 Args args = Args::global()) -> std::tuple<ITensor,ITensor,Index>
  ```

  The same as `diagHermitian` above, but assumes the input ITensor is positive
  semi-definite and allows truncation according the the eigenvalues.

  If truncation is performed, negative eigenvalues will be set to zero.

  Along with the named arguments of `diagHermitian`, `diagPosSemiDef` accepts the following
  arguments:

   * "MaxDim" &mdash; integer M. If there are more than M eigenvalues, only the largest M are kept.

   * "Cutoff" &mdash; real number @@\epsilon@@. Discard the smallest eigenvalues
      @@p\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
      $$
      \frac{\sum\_{n\in\text{discarded}} p\_n}{\sum\_{n} p\_n} < \epsilon \:.
      $$
      <span>&nbsp;</span>

   * "MinDim" &mdash; integer m. At least m eigenvalues will be kept, even if the cutoff criterion would discard more.

   * "ShowEigs" &mdash; if `true`, print lots of extra information about the truncation of singular values.

   * "Truncate" &mdash; if set to `false`, no truncation occurs. Otherwise truncation parameters ("Cutoff","MaxDim", "MinDim") will be used to perform a truncation of singular values.

  * "TruncateDegenerate" &mdash; if `true`, degenerate subspaces will be respected (i.e., if the the truncation lies within a set of degenerate singular values based on a numerical threshold, the degenerate subspace will either be entirely truncated or kept, depending on the other argument options).
    Default is `false`.

   <br/>

## General Factorizations

* ```
  factor(ITensor T, IndexSet Ais[, IndexSet Bis],
         Args args = Args::global()) -> std::tuple<ITensor,ITensor,Index>
  ```

  The "factor" decomposition is based on the SVD,
  but factorizes a tensor T into only two
  tensors `T==A*B` (up to truncation errors) where 
  A and B share a single common index.
  The function returns `A` and `B` as ITensors, as well
  as `l`, the common index of `A` and `B`.
  
  If the SVD of T is `T==U*S*V` where S is a diagonal
  matrix of singular values, then A and B
  are schematically `A==U*sqrt(S)` and `B==sqrt(S)*V`.

  An IndexSet `Ais` is input along with `T` to specify 
  which Indices of `T` end up on the `A` tensor of the 
  decomposition, and the rest of the indices end up on the
  `B` tensor.

  Optionally, the indices ending up on the output tensor 
  `B` can be explicitly specified by the IndexSet `Bis`. 
  In this case, an extra check is added that the union of the `Ais`
  indices and `Bis` indices are the same as the indices on `T`.

  In addition to the named Args recognized by the 
  svd routine, factor accepts an Arg "Tags"
  which will be the name of the common index 
  connecting A and B.

  <div class="example_clicker">Click to Show Example</div>

      auto T = randomITensor(i,j,k,l);

      //Put i,k on A
      auto [A,B,l] = factor(T,{i,k});

      Print(l == commonIndex(A,B)); //prints: true
      Print(norm(T-A*B)); //prints on the order of 1E-15


* ```
  denmatDecomp(ITensor T, IndexSet Ais[, IndexSet Bis],
               Direction dir,
               Args args = Args::global()) -> std::tuple<ITensor,ITensor,Index>
  ```

   Factorize a tensor T into products A and B such that `T==A*B` (up to truncation errors). 

   If `dir==Fromleft` the tensor A will be "left orthogonal" in the sense that A times the 
   conjugate of A summed over all indices not in common with B will produce an identity 
   (Kronecker delta) tensor. If `dir==Fromright` B will be unitary ("right orthogonal"). 
   
   If `dir==Fromleft`, the result of this method is equivalent to computing an SVD of T 
   such that `T==U*D*V` then setting `A=U` and `B=D*V`. 
   (If `dir==Fromright` it would be equivalent to setting `A=U*D` and `B=V`.) 

   An IndexSet `Ais` is input along with `T` to specify
   which Indices of `T` end up on the `A` tensor of the
   decomposition, and the rest of the indices end up on the
   `B` tensor.

   Optionally, the indices ending up on the output tensor
   `B` can be explicitly specified by the IndexSet `Bis`.
   In this case, an extra check is added that the union of the `Ais`
   indices and `Bis` indices are the same as the indices on `T`.

   Although the results of this method are related to the SVD, the implementation 
   is different.  Rather than performing an SVD, the method computes a "density matrix" from T 
   (using an analogy where T is a wave function, which may or may not actually be the case) 
   and diagonalizes this density matrix. Two key reasons for doing this versus an SVD
   are computational efficiency and having the ability to implement the DMRG 
   noise term (see the next version of `denmatDecomp` below).

   To compute a truncated version of this decomposition, pass one or both of the
   named arguments "Cutoff" or "MaxDim" described below.

   The denmatDecomp function recognizes the following optional named arguments:
   
   * "MaxDim" &mdash; integer M. If there are more than M eigenvalues, only the largest M are kept.

  * "Cutoff" &mdash; real number @@\epsilon@@. Discard the smallest eigenvalues
     @@p\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
     $$
     \frac{\sum\_{n\in\text{discarded}} \  p\_n}{\sum\_{n} p\_n} < \epsilon \:.
     $$
     <span>&nbsp;</span>

  * "MinDim" &mdash; integer M. At least M singular values will be kept, even if they fall below the cutoff.
  
  * "Truncate" &mdash; if set to `false`, no truncation occurs. Otherwise truncation parameters ("Cutoff",
    "MaxDim", "MinDim") will be used to perform a truncation of singular values.
  
  * "ShowEigs" &mdash; if `true`, print lots of extra information about the truncation of singular values.
    Default is `false`.

  * "TruncateDegenerate" &mdash; if `true`, degenerate subspaces will be respected (i.e., if the the truncation lies within a set of degenerate singular values based on a numerical threshold, the degenerate subspace will either be entirely truncated or kept, depending on the other argument options).
    Default is `false`.

  <div class="example_clicker">Click to Show Example</div>

      auto T = randomITensor(l1,s1,s2,l2);

      auto [A,B,l] = denmatDecomp(T,{l1,s1},Fromleft); //decompose T into A * B

      Print(l == commonIndex(A,B)); //prints: true
      Print(norm(T-A*B)); //prints on the order of 1E-15

   <br/>

* ```
  template<class BigMatrixT>
  denmatDecomp(ITensor T, IndexSet Ais[, IndexSet Bis],
               Direction dir, 
               BigMatrixT PH,
               Args args = Args::global()) -> std::tuple<ITensor,ITensor,Index>
  ```

  Identical to denmatDecomp function described above, except before the decomposition the density matrix
  formed from T has the "noise term" added to it. For more information on the noise term see the paper
  [Density matrix renormalization group algorithms with a single center site](http://prb.aps.org/abstract/PRB/v72/i18/e180403), 
  S.R.&nbsp;White, <i>Phys.&nbsp;Rev.&nbsp;B</i> *72*, 180403(R) (2005).

  For the PH object to implement the noise term, it must provide the `deltaRho` method. For more information
  see the documentation on [[LocalOp|classes/localop]].

  Named arguments recognized:

  * "Noise" &mdash; real number. Coefficient of noise term; default is 0.

## Hermitian Matrix Exponentiation

* `expHermitian(ITensor H, Cplx tau = 1) -> ITensor` <br/>

  Given an ITensor H that can be treated as a Hermitian matrix (by matching pairs of indices, 
  one with prime level zero, the other with prime level 1), returns the exponential 
  of this tensor.

  Optionally a factor `tau` can be included in the exponent. If `tau` has zero imaginary
  part and the tensor H is real, the returned tensor will also be real.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(2);
      auto j = Index(4);

      auto T = randomITensor(i,j,prime(i),prime(j));

      //Make Hermitian matrix out of T
      auto H = T + swapTags(dag(T),"0","1");

      // compute exp(i * H)
      auto expiH = expHermitian(H,1_i);

      // compute exp(2 * H)
      auto exp2H = expHermitian(H,2);

   <br/>

## Old Syntax and Spectrum Output

The following are older interfaces for ITensor decomposition functions for backwards
compatibility and internal usage.

* ```
  svd(ITensor T, ITensor & U, ITensor & S, ITensor & V, 
      Args args = Args::global()) -> Spectrum
  ```
  ```
  diagHermitian(ITensor H, ITensor & U, ITensor & D,
                Args args = Args::global()) -> Spectrum
  ```
  ```
  diagPosSemiDef(ITensor H, ITensor & U, ITensor & D,
                 Args args = Args::global()) -> Spectrum
  ```
  ```
  factor(ITensor T, ITensor & A, ITensor & B,
         Args args = Args::global()) -> Spectrum
  ```
  ```
  denmatDecomp(ITensor T, ITensor & A, ITensor & B, 
               Direction dir, Args args = Args::global()) -> Spectrum
  ```
  ```
  template<class BigMatrixT>
  denmatDecomp(ITensor T, ITensor & A, ITensor & B, 
               Direction dir, 
               BigMatrixT PH,
               Args args = Args::global()) -> Spectrum
  ```

  These are alternative interfaces for the decompositions listed above.
  For example, `svd(T,U,S,V,args)` computes the singular value decomposition of a tensor T.
  The arguments U, S, and V are overwritten, and the product `U*S*V` equals T.

  *Returns*: [[Spectrum|classes/spectrum]] object containing information about truncation 
  and singular values/eigenspectrum.

  For `svd(T,U,S,V)`, `factor(T,A,B)`, and `denmatDecomp(T,A,B,dir[,PH])`,
  to determine which indices should be grouped together as the "row" indices and thus end up on
  the final U (A) tensor, versus the remaining "column" indices which end up on the final V (B) 
  tensor, the function inspects the indices of the input U (A) tensor. 
  All indices common to both U (A) and T are considered "row" indices
  (other indices of U (A) are ignored). If U (A) has no indices, the function inspects the 
  indices of V (B).


<!--

To add:

* eigen

-->

<br/>
_This page current as of version 3.0.0_
