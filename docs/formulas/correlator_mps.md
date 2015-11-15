# Measure a correlator from an MPS wavefunction #

See this in a diagrammatic form [[here|tutorials/correlations]].

### Sample code:

    //Given an MPS or IQMPS called "psi",
    //constructed from a SiteSet "sites"
    
    //Replace "Op1" and "Op2" with the actual names
    //of the operators you want to measure
    auto op_i = sites.op("Op1",i);
    auto op_j = sites.op("Op2",j);

    //below we will assume j > i

    //'gauge' the MPS to site i
    //any 'position' between i and j, inclusive, would work here
    psi.position(i); 

    //psi.Anc(1) *= psi.A(0)//Uncomment if using iDMRG calculation

    //index linking i to i+1:
    auto ir = commonIndex(psi.A(i),psi.A(i+1),Link);

    auto C = psi.A(i)*op_i*dag(prime(prime(psi.A(i),Site),ir));
    for(int k = i+1; k < j; ++k)
        {
        C *= psi.A(k);
        C *= dag(prime(psi.A(k),Link));
        }
    C *= psi.A(j);
    C *= op_j;
    //index linking j to j-1:
    auto jl = commonIndex(psi.A(j),psi.A(j-1),Link);
    C *= dag(prime(prime(psi.A(j),Site),jl));

    auto result = toReal(C); //or toComplex(C) if expecting complex

### Notes:
* `auto` is a C++11 keyword that tells the compiler to automatically deduce the correct type from the expression on the right-hand side
* `C` is the tensor holding our partial result for the correlator
* The for loop builds into C the MPS tensors making up the MPS "transfer matrices" which carry correlations from i to j


