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
    //...set elems of psi...

    //Set accuracy parameters
    //for truncation by creating an instance
    //of the 'Spectrum' class
    //(after an SVD, spec will store the squares of the singular values)
    Spectrum spec;
    spec.cutoff(1E-10);
    spec.maxm(200);

    //Compute SVD
    //Providing indices of A tells the svd
    //method which indices should end up on A,
    //other indices of psi will end up on B
    //(Spectrum argument is optional, omitting it means "do not truncate")
    ITensor A(l1,s1),
            B;
    svd(psi,A,D,B,spec);

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
    ITensor rho(primed(s1),primed(s2),conj(s1),conj(s2));
    //...set elems of rho, must be Hermitian

    //Compute eigenvalue decomposition
    ITensor U;
    ITSparse D;
    diagHermitian(rho,U,D);

    PrintDat(D); //look at the eigenvalues of rho

    //Check
    diff = rho - primed(U)*D*conj(U);
    Print(diff.norm()); //prints something < 1E-14


## Singular Value Decomposition Methods ##

* `Spectrum svd(Tensor T, Tensor& U, SparseT& D, Tensor& V, OptSet opts = Global::opts())`

   Compute the singular value decomposition (without truncation) of a Tensor T (Tensor is a templated type and could be e.g. ITensor or IQTensor). The arguments U, D, and V are overwritten to hold the resulting factors such that `T==U*D*V`.

   One key difference in computing the SVD of a tensor versus a matrix is that in the tensor case one must specify which indices are considered the "row" indices (i.e. which will end up on the unitary U) and which indices are considered "column" indices (ending up on V). To specify this, one of the unitaries, say U, must already have the desired "row" indices when the method is called. This indicates to the method that these indices should appear on U in the result. The remaining indices of T will appear on V. Note that upon return U will contain an additional index which it shares with the singular value tensor D, and similarly for T.

   Upon return, the sparse type tensor D will be diagonal and contain the singular values of T. The type of D should be ITSparse if T is an ITensor and IQTSparse if T is an IQTensor.

   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor U(l1,s1), //want l1, s1 to end up on U
                V;
        ITSparse D;

        svd(T,U,D,V); //compute SVD

        PrintDat(D); //view singular values
        Print((T-U*D*V).norm()); //prints 0

* `void svd(Tensor T, Tensor& U, SparseT& D, Tensor& V, Spectrum& spec, OptSet opts = Global::opts())`

   Compute the singular value decomposition of a tensor T, truncating the singular values according to the parameters contained in the [[Spectrum|classes/spectrum]] instance `spec`. For instance, if `spec.cutoff() == 1E-8`, only singular values whose squares are greater than 1E-8 will be kept. (The cutoff is applied to the squares of the singular values for consistency with the `denmatDecomp` method below.)


   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor U(l1,s1), //want l1, s1 to end up on U
                V;
        ITSparse D;

        Spectrum spec;
        spec.cutoff(1E-8);
        spec.maxm(100);

        svd(T,U,D,V,spec); //compute SVD and truncate

        PrintDat(D); //view singular values
        Print((T-U*D*V).norm()); //prints a small number since we truncated


## Density Matrix Decomposition ##

* `Spectrum denmatDecomp(Tensor T, Tensor& A, Tensor& B, Direction dir, OptSet opts = Global::opts())`

   Factorize a Tensor T (Tensor is a templated type and could be e.g. ITensor or IQTensor) into products A and B such that `T==A*B`. (A and B are passed by reference and overwritten to hold the results.) If `dir==Fromleft` the tensor A will be unitary ("left orthogonal") in the sense that A times the conjugate of A summed over all indices not in common with B will produce an identity (Kronecker delta) tensor. If `dir==Fromright` B will be unitary ("right orthogonal"). The result of this method is equivalent to computing an SVD of T such that `T==U*D*V` then setting `A=U` and `B=D*V` assuming `dir==Fromleft`. (If `dir==Fromright` it would be equivalent to setting `A=U*D` and `B=V`.) 

   To determine which indices of T should end up on A versus B, the method inspects the initial indices of A (or B if A is default constructed) and keeps the same indices on A upon return, with the rest of the indices going onto B. (This is similar to how the `svd` method above works.)

   Although the results of this method are related to the SVD, the implementation is different. Rather than performing an SVD, the method computes a "density matrix" from T (using an analogy where T is a wave function, which may or may not actually be the case) and diagonalizes this density matrix. Two key reasons for doing this in contrast to just an SVD are computational efficiency and having the ability to implement the DMRG noise term (see the last version of `denmatDecomp` below).


   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor U(l1,s1), //want l1, s1 to end up on U
                V;
        ITSparse D;

        denmatDecomp(T,A,B,Fromleft); //decompose T into A*B

        Print((T-A*B).norm()); //prints 0

* `void denmatDecomp(Tensor T, Tensor& A, Tensor& B, Direction dir, Spectrum& spec, OptSet opts = Global::opts())`

   Factorize a Tensor T, truncating the density matrix eigenvalues (equivalent to the squares of the singular values) according to the parameters contained in the [[Spectrum|classes/spectrum]] instance `spec`. For instance, if `spec.cutoff() == 1E-8`, only eigenvalues greater than 1E-8 will be kept.


   <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site), 
              s2("Site 2",2,Site),
              l1("Link 1",4,Link),
              l2("Link 1",4,Link);

        ITensor T(l1,s1,s2,l2);
        T.randomize();

        ITensor U(l1,s1), //want l1, s1 to end up on U
                V;
        ITSparse D;

        Spectrum spec;
        spec.cutoff(1E-8);
        spec.maxm(100);

        denmatDecomp(T,A,B,Fromleft,spec); //factorize T and truncate

        Print((T-A*B).norm()); //prints a small number since we truncated


[[Back to Classes|classes]]

[[Back to Main|main]]
