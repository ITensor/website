# Compute entanglement entropy of an MPS #

### Sample code:

    //Given an MPS or IQMPS called "psi",
    //and some particular bond "b" (1 <= b < psi.N())
    //across which we want to compute the von Neumann entanglement
    
    //"Gauge" the MPS to site b
    psi.position(b); 

    //Here assuming an MPS of ITensors, but same code works
    //for IQMPS by using IQTensor

    //Compute two-site wavefunction for sites (b,b+1)
    ITensor wf = psi.A(b)*psi.A(b+1);
    //SVD this wavefunction to get the spectrum
    //of density-matrix eigenvalues
    ITensor S;
    auto spectrum = svd(wf,psi.Anc(b),S,psi.Anc(b+1));
    //Put singular values back into one of the MPS tensors
    psi.Anc(b) *= S;

    //Get density-matrix eigenvalues
    Vector P = spectrum.eigsKept();
    //Apply von Neumann formula
    Real SvN = 0;
    for(int n = 1; n <= P.Length(); ++n)
        {
        SvN += -P(n)*log(P(n));
        }
    printfln("Across bond b=%d, SvN = %.10f",b,SvN);

