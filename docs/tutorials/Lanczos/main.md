<span class='article_title'>Eigenvalue Solver: Lanczos Algorithm</span>

<span class='article_sig'>Thomas E. Baker and Benedikt Bruognolo&mdash;September 23, 2015</span>

Diagonalizing an entire matrix can be a costly operation.  Since diagonalizing matrices makes up a large part of solving quantum systems, using a fast algorithm to do this is desirable.  One such algorithm is the Lanczos algorithm.

This article covers what the Lanczos algorithm is and why it finds the ground state, @@\psi_0@@.  Doing this algorithm avoids the full diagonalization of a matrix @@Q@@ since we are only interested in a very specific eigenvalue in a localized region of the Hilbert space.

## The Lanczos algorithm

Given a random guess for the eigenvector @@\psi@@, we start with the equation

$$
Q\psi=\phi
$$

@@\psi_0@@ is not found from this equation.  @@\phi@@ will be a superposition of eigenvalues that contain the ground state, but we need a suitable basis to obtain the ground state.  We can also apply @@Q@@ several more (@@N@@) times 

$$
Q^N\psi=\phi\_N
$$

Taking the collection of @@\\{\phi_N\\}@@ as a good guess for a basis (this is known as the Krylov space), we can diagonalize @@Q@@ using that basis. 


This algorithm will target the extremal eigenvalues (not all of them), so the method is known as a sparse eigensolver.

### Making sure you actually get the ground state 

The above procedure gives you an extreme eigenvalue but not necessarilly the ground state depending on the random guess, @@\psi@@.  To make sure we obtain the ground state, we use the ground state of the diagonalization as a new initial @@\psi@@ and restart the algorithm.

We also use a Gram-Schmidt orthonormalization procedure to ensure the eigenvectors, @@\\{\phi_N\\}@@ are orthogonal and that the algorithm is more stable.

The `davidson` function in ITensor uses the Davidson algorithm which is very similar to Lanczos, but it is slightly more efficient.

## Why the ground state was found

The computational efficiency of Lanczos is that it finds the ground state while using a number of @@\phi_N@@ vectors (in what is called the Krylov space) where @@N\ll i@@ where @@i@@ indexes the wavefunction @@\psi@@ as expanded in an eigenvalue decomposition.

$$
\psi=\sum_i c_i\psi_i
$$

At each step, we can see that applying the operator @@Q^N@@ gives, in this basis,

$$
Q^N\psi^N=\sum_iq_i^Nc_i\psi_i
$$

The largest value @@q^N@@ will grow much faster than the other values and hence the ground state is reached. 

One case of note is when we have a degeneracy in a gapless system.  A gapped system has one eigenvalue with excited states some definite distance away; however, the gapless case can have more than one eigenvalue scale with each other.  This makes determining the true ground state difficult.  This is one of the reasons that DMRG has trouble with gapless states, along with entanglement issues, though good results can be obtained in these systems.

The last point we remark on is the similarity in how Lanczos picks out the dominant eigenvalues and why imaginary time evolution also finds the ground state.  Considering the application of an imaginary time evolution of a state, @@e^{-\beta\mathcal{H}}\psi@@, but expanded as a Taylor series, we can see that each order generates the operator to the order @@N@@.  The same principle, that the dominant eigenvalue should become the largest as @@N@@ becomes large still applies and make imaginary time evolution work.

