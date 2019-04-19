# Measure a correlator from an MPS wavefunction #

See this in a diagrammatic form [[here|tutorials/correlations]].

### Sample code:

    //Given an MPS called "psi",
    //constructed from a SiteSet "sites"
    
    //Replace "Op1" and "Op2" with the actual names
    //of the operators you want to measure
    auto op_i = sites.op("Op1",i);
    auto op_j = sites.op("Op2",j);

    //below we will assume j > i

    //'gauge' the MPS to site i
    //any 'position' between i and j, inclusive, would work here
    psi.position(i); 

    //psi.ref(1) *= psi(0); //Uncomment if doing iDMRG calculation

    //index linking i to i+1:
    auto ir = commonIndex(psi(i),psi(i+1),Link);

    auto C = psi(i)*op_i*dag(prime(psi(i),Site,ir));
    for(int k = i+1; k < j; ++k)
        {
        C *= psi(k);
        C *= dag(prime(psi(k),Link));
        }
    C *= psi(j);
    C *= op_j;
    //index linking j to j-1:
    auto jl = commonIndex(psi(j),psi(j-1),Link);
    C *= dag(prime(psi(j),jl,Site));

    auto result = elt(C); //or eltC(C) if expecting complex

### Notes:
* `auto` is a C++11 keyword that tells the compiler to automatically deduce the correct type from the expression on the right-hand side
* `C` is the tensor holding our partial result for the correlator
* The for loop builds into C the MPS tensors making up the MPS "transfer matrices" which carry correlations from i to j


