# Compute a two-site reduced density matrix from an MPS

Say we have an MPS representing a quantum wavefunction @@\Psi@@, and
wish to compute the reduced density matrix 

$$
\rho_{s_i s_j}^{s'_i s'_j} = \text{Tr}_{\{s \neq s_i,s_j\}}[|\Psi\rangle\langle\Psi|]
$$

In diagrammatic form, what we want to compute is

<img class="diagram" width="60%" src="docs/VERSION/formulas/two_rdm.png"/>

Then we can use the following sample code to compute this quantity 
for fixed i and j.

### Sample code:

    //Given an MPS called "psi",
    //and assuming j > i

    //'gauge' the MPS to site i
    //any 'position' between i and j, inclusive, would work here
    psi.position(i); 

    //index linking i to i+1:
    auto ir = commonIndex(psi(i),psi(i+1));

    auto rho = psi(i)*dag(prime(prime(psi(i),"Site"),ir));
    for(int k = i+1; k < j; ++k)
        {
        rho *= psi(k);
        rho *= dag(prime(psi(k),"Link"));
        }
    rho *= psi(j);
    rho *= dag(prime(psi(j)));
    for(int k = j+1; k <= psi.N(); ++k)
        {
        rho *= psi(k);
        rho *= dag(prime(psi(k),"Link"));
        }

