<span class='article_title'>Singular Value Decompositions</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 19, 2015</span>

A singular value decomposition (SVD) may be performed on any rectangular matrix.  The properties of this decomposition of a matrix allows us to sort out relevant degrees of freedom and only keep the most important parts of the matrix.  Leaving out the small, less important degrees of freedom in a DMRG calculation, for example, allows it to go faster and keep smaller matrices.  Often, the degrees of freedom we throw away are small and don't affect the final answer.

This article will detail what an SVD is and how to represent one diagrammatically.

## Singular Value Decompositions

The singular value decomposition of a matrix @@M@@ is a factorization @@M = U D V^\dagger@@ where
@@U@@ and @@V@@ are unitary, and @@D@@ is diagonal, with real, non-negative entries (known as the singular values).

Consider a rectangular matrix (this is coded in the first [[Tutorial|course]]
$$
M=\begin{bmatrix}
0.435839 & 0.223707 & 0.10\\\\
0.223707 & 0.435839 & -0.10\\\\
0.223707 & 0.435839 & 0.10\\\\
0.223707 & 0.435839 & -0.10
\end{bmatrix}
$$
The singular value decomposition of @@M@@ is 
$$
M=UDV^\dagger=\begin{bmatrix}
1/2 & -1/2 & 1/2\\\\
1/2 & -1/2 & -1/2\\\\
1/2 & 1/2 & 1/2\\\\
1/2 & 1/2 & -1/2
\end{bmatrix}\begin{bmatrix}
0.933 & 0 & 0\\\\
0 & 0.300 & 0\\\\
0 & 0 & 0.200
\end{bmatrix}\begin{bmatrix}
0.707107 & 0.707107 & 0\\\\
-0.707107 & 0.707107 & 0\\\\
0 & 0 & 1
\end{bmatrix}
$$

Thus for this matrix the singular values are 0.933, 0.300, and 0.200. Note that if we take @@MM^\dagger=UD^2U^\dagger@@, then we can see that the singular values are the square roots of the eigenvalues of @@M M^\dagger @@.

The real utility of the SVD is that it provides a controlled method for approximating matrices.
For instance, if we set the smallest singular value to zero, then 

$$
M\approx \tilde{M}=\begin{bmatrix}
1/2 & -1/2 & 1/2\\\\
1/2 & -1/2 & -1/2\\\\
1/2 & 1/2 & 1/2\\\\
1/2 & 1/2 & -1/2
\end{bmatrix}\begin{bmatrix}
0.933 & 0 & 0\\\\
0 & 0.300 & 0\\\\
0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
0.707107 & 0.707107 & 0\\\\
-0.707107 & 0.707107 & 0\\\\
0 & 0 & 1
\end{bmatrix}
$$

$$
= \begin{bmatrix}
0.329773 & 0.329773 & 0\\\\
0.329773 & 0.329773 & 0\\\\
0.329773 & 0.329773 & 0\\\\
0.329773 & 0.329773 & 0
\end{bmatrix}
$$

Since we set the third singular value to zero, we can now safely truncate (discard) the third 
column of @@U@@ and the third row of @@V^\dagger@@ without affecting the result @@\tilde{M}@@

$$
\tilde{M}=\begin{bmatrix}
1/2 & -1/2 \\\\
1/2 & -1/2 \\\\
1/2 & 1/2  \\\\
1/2 & 1/2  
\end{bmatrix}\begin{bmatrix}
0.933 & 0 \\\\
0 & 0.300 \\\\
\end{bmatrix}\begin{bmatrix}
0.707107 & 0.707107 & 0\\\\
-0.707107 & 0.707107 & 0
\end{bmatrix}
$$

$$
= \begin{bmatrix}
0.329773 & 0.329773 & 0\\\\
0.329773 & 0.329773 & 0\\\\
0.329773 & 0.329773 & 0\\\\
0.329773 & 0.329773 & 0
\end{bmatrix}
$$

Even though the values of the modified matrix have changed, the determinant of the difference, @@||M-\tilde M||^2=0.04=(0.2)^2@@.  This is related to the truncation error in a DMRG calculation-the sum of singular values that we neglect in an Schmidt decomposition.  Note that the value is not large and does a good job of approximating the original matrix, but we leave off the rows and columns corresponding to the truncated values.  In the DMRG case, these singular values can go very low, very nearly zero, and leaving them out of the SVD produces almost no change in the matrix.

## Diagrammatically

Consider a two site wavefunction

<p align="center"><img src="docs/tutorials/SVD/singlet.png" alt="SVD Diagram" style="height: 200px;"/></p>

The SVD appears as

<p align="center"><img src="docs/tutorials/SVD/SVD.png" alt="SVD Diagram" style="height: 200px;"/></p>

## In ITensor

To call an `svd` in ITensor, we can use the code

    MPS psi;
    ITensor U,D,V;
    svd(psi,U,D,V);

In fact, any tensor can be used in the first argument. If `U` and `V` are initialied with some value and a set of indices before being placed into `svd`, ITensor will use the first indices in `U` equal to the number of indices in `psi` for the return SVD values.  The same occurs for `V`.  Note that any other values for other indices is set to zero.

## Calculating Entanglement

The von Neumann entanglement can be calculated from the expression

$$
S_\mathrm{vN}=-\sum \rho_i \ln\rho_i
$$

but each element of the density matrix, @@\rho_i@@, is simply the square of the singular values in `D`.  We often abbreviate these as @@\lambda_i(=\sqrt{\rho_i})@@.  The singular values can be accessed through the `eigs` function like

    auto SvN=0;//The von Neumann entropy
    for(auto eig : D.eigsKept())
    {
    SvN += -eig * log(eig);
    } 


