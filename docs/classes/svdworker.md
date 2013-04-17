#SVDWorker#

Class for performing tensor decompositions, primarily the SVD and eigenvalue decomposition.

##Synopsis##

    Index s1("site 1",2,Site),
          s2("site 2",2,Site),
          l1("link 1",10),
          l2("link 2",8);

    SVDWorker W;

    //
    //Eigenvalue decomposition
    //

    //Create a density-matrix-like tensor
    ITensor rho(primed(s1),primed(s2),conj(s1),conj(s2));
    //...set elems of rho, must be Hermitian

    //Compute eigenvalue decomposition
    ITensor U;
    ITSparse D;
    W.diagonalize(rho,U,D);

    PrintDat(D); //look at the eigenvalues of rho

    //Check
    ITensor diff = rho - primed(U)*D*conj(U);
    Print(diff.norm()); //prints something < 1E-14


    //
    //Singular value decomposition (SVD)
    //

    //Set accuracy parameters
    //for truncation
    W.cutoff(1E-10);
    W.maxm(200);

    //Create a wavefunction-like tensor
    ITensor psi(l1,s1,s2,l2);
    //...set elems of psi...

    //Compute SVD
    //Providing indices of A tells the svd
    //method which indices should end up on A,
    //other indices of psi will end up on B
    ITensor A(l1,s1),
            B;
    W.svd(psi,A,D,B);

    PrintDat(D); //look at singular values of psi

    //Check
    diff = psi - A*D*B;
    Print(diff.norm()); //prints something < 1E-14


[[Back to Classes|classes]]

[[Back to Main|main]]
