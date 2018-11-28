# Compute a two-site reduced density matrix from an MPS

Say we have an MPS representing a quantum wavefunction @@\Psi@@, and
wish to compute the reduced density matrix 

$$
\rho_{s_i s_j}^{s'_i s'_j} = \text{Tr}_{\{s \neq s_i,s_j\}}[\ket{\Psi}\bra{\Psi}]
$$

In diagrammatic form, what we want to compute is

<img class="diagram" width="60%" src="docs/formulas/two_rdm.png"/>

Then we can use the following sample code to compute this quantity 
for fixed i and j.

### Sample code:

    //Given an MPS called "psi",
    //constructed from a SiteSet "sites"
    //and assuming j > i

    //'gauge' the MPS to site i
    //any 'position' between i and j, inclusive, would work here
    psi.position(i); 

    //index linking i to i+1:
    auto ir = commonIndex(psi.A(i),psi.A(i+1));

    auto C = psi.A(i)*dag(prime(psi.A(i),Site,ir));
    for(int k = i+1; k < j; ++k)
        {
        C *= psi.A(k);
        C *= dag(prime(psi.A(k),Link));
        }
    C *= psi.A(j);
    C *= dag(prime(psi.A(j)));
    for(int k = j+1; k <= psi.N(); ++k)
        {
        C *= psi.A(k);
        C *= dag(prime(psi.A(k),Link));
        }

