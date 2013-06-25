# SVD and Related Algorithms #

Methods for performing tensor decompositions such as the singular value decomposition (SVD), density matrix
diagonalization, and Hermitian eigenvalue decomposition are defined in svdalgs.h and svdalgs.cc.

## Synopsis ##

    Index s1("site 1",2,Site),
          s2("site 2",2,Site),
          l1("link 1",10),
          l2("link 2",8);

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
    ITensor diff = rho - primed(U)*D*conj(U);
    Print(diff.norm()); //prints something < 1E-14


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
    diff = psi - A*D*B;
    Print(diff.norm()); //prints something < 1E-14


[[Back to Classes|classes]]

[[Back to Main|main]]
