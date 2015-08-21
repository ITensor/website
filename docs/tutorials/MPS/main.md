<span class='article_title'>Matrix Product States</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 17, 2015</span>

The Hilbert space is large.  Scanning through the entire space would be take longer than is reasonable.  Writing down a good guess for the wavefunction can be a great way to get close enough to the right ground state. Finding the answer with MPSs can be comparatively much easier than searching the whole Hilbert space.

A very good guess for the strongly correlated, gapped systems in one dimension is the matrix product state (MPS).  DMRG and many tensor network methods rely on this ansatz to quickly and efficiently calculate the ground state.

A single element of an MPS is a tensor with three indices, @@A^{\sigma\_i}\_{a\_i a\_{i+1}}@@.  The subscripts  convey that different sites may have different links to each other.  These indices catalog the bond dimension (e.g., number of Schmidt states kept in a DMRG calculation).   The index @@\sigma_i@@ corresponds to the physical index.  This has two values for a spin@@-1/2@@ chain.

An MPS diagram for a five site system looks like

<p align="center"><img src="docs/tutorials/MPS/MPS.png" alt="MPS" style="height: 150px;"/></p>

We will discuss some characteristics of MPSs and introduce some concepts that are necessary to design and implement your tensor networks into ITensor.

### ITensor Methods

To make an MPS, we can use the constructor

    MPS psi;//constructs a random MPS
    //or
    SpinHalf sites(5);
    auto psi = MPS(sites);//construct a random product state with indices
                          //based on the SiteSet used (here SpinHalf)

which automatically makes a random MPS.

MPSs have a property that allows for quick manipulation of each tensor.  The orthogonality center can be chosen to be on any site.  If we call

    psi.position(4);

ITensor will take a series of [[SVDs|tutorials/SVD]] (in this case, only one) until we have placed the orthogonality center of the MPS on site 4.  The diagram looks like

<p align="center"><img src="docs/tutorials/MPS/MPS_site2.png" alt="Regauged MPS" style="height: 150px;"/></p>

Regauging the MPS allows us to access its elements.  For example, calling the function

    psi.A(3);

moves the orthogonality center so it covers sites 3 and 4.  The element of site 3 can be accessed then.  This is known as the mixed canonical form (have more than one site as the orthogonality center).  ITensor has been designed so that it will perform the minimum number of operations in every case.

Reorthogonalizing an MPS has other advantages.  To illustrate, we have drawn purple squares to be left-normalized while yellow squares are right-normalized.

<p align="center"><img src="docs/tutorials/MPO/onsite.png" alt="MPS Diagram" style="height: 200px;"/></p>

The utility of this is to take advantage of normalization condition (@@\sum A^{\sigma\_{i}\dagger}\_{a\_ia\_{i+1}}A^{\sigma\_{i}}\_{a\_ia\_{i+1}}=1@@ if both tensors are appropriately gauged).  Two left-normalized tensors are the identity.  For example, another way to calculate the spin expectation value on site 4 would be to call (see [[an article on Correlation functions|tutorials/correlations]] for more details)

    psi.position(4);
    auto Mz = dag(prime(psi.A(4),Site))*sites.op("Sz",4)*psi.A(4);

but notice we only called the tensor on site 4!  We need not bother with the other sites since we know they contract to the identity.

### Singlet Example

To construct a two-site singlet state in ITensor, we may use

    Index s1("s1",2,Site),
          s2("s2",2,Site);//makes indices for wavefunction tensor
    ITensor psi(s1,s2);//initializes wavefunction
    psi(s1(1),s2(2)) = 1./sqrt(2);//element 1,2 defined
    psi(s1(2),s2(1)) = -1./sqrt(2);//element 2,1 defined

This stores a tensor in the `s1`, `s2` basis and appears in matrix form as

<p align="center"><img src="docs/tutorials/MPS/singlet.png" alt="singlet MPS" style="height: 250px;"/></p>

Following the indices we defined, this is written in matrix form as

$$\Sigma^{\sigma\_i}=\begin{bmatrix}
0&1/\sqrt2\\\\
-1/\sqrt2&0\\\\
\end{bmatrix}$$
   
This is a singlet @@(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle)/\sqrt2@@.

### Normalization

To normalize our wavefunction, we can call

    psi.norm();
