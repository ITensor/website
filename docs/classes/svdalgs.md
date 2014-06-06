# SVD and Related Algorithms #

Methods for computing tensor decompositions such as the singular value decomposition (SVD), density matrix
diagonalization, and Hermitian eigenvalue decomposition are defined in svdalgs.h and svdalgs.cc.

## Synopsis ##

    Index s1("site 1",2,Site),
          s2("site 2",2,Site),
          l1("link 1",10),
          l2("link 2",8);

    //
    //Singular value decomposition (SVD)
    //

    //Create a wavefunction-like tensor
    ITensor psi(l1,s1,s2,l2);
    psi.randomize();
    psi *= 1./psi.norm(); //normalize

    //Create an OptSet holding the accuracy parameters
    OptSet opts;
    opts.add("Cutoff",1E-10);
    opts.add("Maxm",200);

    //Compute SVD
    //Providing indices of A tells the svd
    //method which indices should end up on A,
    //other indices of psi will end up on B
    //(opts argument is optional, omitting it means "do not truncate")

    ITensor A(l1,s1),D,B;
    svd(psi,A,D,B,opts);

    PrintDat(D); //look at singular values of psi

    //Check
    ITensor diff = psi - A*D*B;
    Print(diff.norm()); //prints something < 1E-14

    //
    //Eigenvalue decomposition
    //of Hermitian tensors
    //
    //Assumes matching pairs of indices with
    //prime level 0 and 1
    //

    //Create a density-matrix-like tensor
    ITensor rho(prime(s1),prime(s2),s1,s2);
    rho.randomize();

    //Compute eigenvalue decomposition
    ITensor U,D;
    diagHermitian(rho,U,D);

    PrintDat(D); //look at eigenvalues of rho

    //Check
    diff = rho - primed(U)*D*dag(U);
    Print(diff.norm()); //prints something < 1E-14


## Singular Value Decomposition ##

* `svd(Tensor T, Tensor& U, Tensor& D, Tensor& V, OptSet opts = Global::opts())`

   *Returns*: `Spectrum` object containing squares of singular values.

   Compute the singular value decomposition of a Tensor T without truncation (for truncating version see below). "Tensor" is a templated type and could be e.g. ITensor or IQTensor. On return, the arguments U, D, and V are overwritten to hold the resulting factors such that `T==U*D*V`.

   One key difference in computing the SVD of a tensor versus a matrix is that in the tensor case one must specify which indices are considered the "row" indices (i.e. which will end up on the unitary U) and which indices are considered "column" indices (ending up on V). To specify this, one of the unitaries, say U, should already have the desired "row" indices when the method is called. This indicates to the method that these indices should appear on U in the result. The remaining indices of T will appear on V. (Note that upon return U and V will each contain an additional index which they share with the singular value tensor D). Upon return, D will be diagonal and contain the singular values of T.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor U(l1,s1), //want l1, s1 to end up on U
                D,V;

        svd(T,U,D,V); //compute SVD

        PrintDat(D); //view singular values
        Print((T-U*D*V).norm()); //prints 0

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

   Diagonalize a Hermitian Tensor T such that `T==dag(U)*D*primed(U)`. "Tensor" is a templated type and could be e.g. ITensor or IQTensor. U and D are passed by reference and overwritten on return.

   The method assumes that the indices of T come in pairs, one index with prime level 0 and a matching index with prime level 1 (reflecting the Hermitian nature of T). For example, T could have indices i,i',j, and j'. Saying that T is Hermitian means that `T == dag(swapPrime(T,0,1))`.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site);

        ITensor T(s1,s2,primed(s1),primed(s2));
        T.randomize();

        T = T + swapPrime(T,0,1);

        ITensor U,D;

        diagHermitian(T,U,D); 

        Print((T-dag(U)*D*primed(U)).norm()); //prints 0

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



[[Back to Classes|classes]]

[[Back to Main|main]]
