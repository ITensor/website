# Measure a correlator from an MPS wavefunction #

See this in a diagrammatic form [[here|tutorials/correlations]].

### Sample code:

    //Number of sites
    auto N = 100;

    //Measure a correlation function
    //at sites i and j
    //Below we will assume j > i
    auto i = 45;
    auto j = 55;

    auto sites = SpinHalf(N);

    //Make a random MPS for testing
    auto state = InitState(sites,"Up");
    auto psi = randomMPS(state);
    
    //Make the operators you want to measure
    auto op_i = sites.op("Sx",i);
    auto op_j = sites.op("Sz",j);

    //'gauge' the MPS to site i
    //any 'position' between i and j, inclusive, would work here
    psi.position(i); 

    //Create the bra/dual version of the MPS psi
    auto psidag = dag(psi);

    //Prime the link indices to make them distinct from
    //the original ket links
    psidag.prime("Link");

    //index linking i-1 to i:
    auto li_1 = leftLinkIndex(psi,i);

    auto C = prime(psi(i),li_1)*op_i;
    C *= prime(psidag(i),"Site");
    for(int k = i+1; k < j; ++k)
        {
        C *= psi(k);
        C *= psidag(k);
        }
    //index linking j to j+1:
    auto lj = rightLinkIndex(psi,j);

    C *= prime(psi(j),lj)*op_j;
    C *= prime(psidag(j),"Site");

    auto result = elt(C); //or eltC(C) if expecting complex

### Notes:
* `auto` is a C++17 keyword that tells the compiler to automatically deduce the correct type from the expression on the right-hand side
* `C` is the tensor holding our partial result for the correlator
* The for loop builds into C the MPS tensors making up the MPS "transfer matrices" which carry correlations from i to j


