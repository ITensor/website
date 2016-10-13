# Measure a spinless fermion correlator from an MPS wavefunction #

<span class='article_sig'>Contributed by Jon Spalding, UC Riverside&mdash; Oct 12, 2016</span>

For more background on working with fermions in ITensor and Jordan-Wigner string,
see [[the tutorial on fermions|tutorials/fermions]].

### Sample code:

    // Given an MPS or IQMPS called "psi",
    // constructed from a Spinless SiteSet "sites"
    
    // Consider a pair of fermionic operators,
    // Cdag and C, for spinless fermions.
    // If Cdag(i) and C(j) operate at sites separated by some arbitrary
    // distance, so that i < j, then in order to represent them
    // as bosonic operators Adag(i) and A(j), we need to include 
    // a chain of "string" (F) operators that preserves the commutation
    // relation for Cdag and C.
    
    auto Adag_i = sites.op("Adag",i);
    auto A_j = sites.op("A",j);
    
    //'gauge' the MPS to site i
    //any 'position' between i and j, inclusive, would work here
    psi.position(i); 
    
    //index linking i to i+1:
    auto ir = commonIndex(psi.A(i),psi.A(i+1),Link);
    auto Corr = psi.A(i)*Adag_i*dag(prime(psi.A(i),Site,ir));
    Print(Corr);
    
    for(int k = i+1; k < j; ++k)
        {
        Corr *= psi.A(k);
        Corr *= sites.op("F",k); //Jordan-Wigner string
        Corr *= dag(prime(psi.A(k)));
        }
    Corr *= psi.A(j);
    Corr *= A_j;
    
    //index linking j to j-1:
    auto jl = commonIndex(psi.A(j),psi.A(j-1),Link);
    Corr *= dag(prime(psi.A(j),jl,Site));
    
    auto result = Corr.real(); //or C.cplx() if expecting complex


### Notes:
* `auto` is a C++11 keyword that tells the compiler to automatically deduce the correct type from the expression on the right-hand side
* `Corr` is the tensor holding our partial result for the correlator
* The for loop builds into Corr the MPS tensors making up the MPS "transfer matrices" which carry correlations from i to j
* Since the operators are fermionic, we need to include Jordan-Wigner "string" (F) operators in between them.


