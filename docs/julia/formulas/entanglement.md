# Computing the Entanglement Entropy of an MPS

A key advantage of using the matrix product state (MPS) format to represent quantum wavefunctions is that it allows one to efficiently compute the entanglement entropy of any left-right bipartition of the system in one dimension, or for a two-dimensional system any "cut" along the MPS path.

Say that we have obtained an MPS `psi` of length N and we wish to compute the entanglement entropy of a bipartition of the system into a region "A" which consists of sites 1,2,...,b and a region B consisting of sites b+1,b+2,...,N.

Then the following code formula can be used to accomplish this task:

    
    orthogonalize!(psi, b)
    U,S,V = svd(psi[b], (linkind(psi, b-1), siteind(psi,b)))
    SvN = 0.0
    for n in dim(S, 1)
      p = S[n,n]^2
      SvN -= p * log(p)
    end
    
As a brief explanation of the code above, the line

    orthogonalize!(psi,b)
    
shifts the orthogonality center to site `b` of the MPS. 

The call to the `svd` routine says to treat the link (virtual or bond) Index connecting the b'th MPS tensor `psi[b]` and the b'th physical Index as "row" indices for the purposes of the SVD (these indices will end up on `U`, along with the Index connecting `U` to `S`).

The code in the `for` loop iterates over the diagonal elements of the `S` tensor (which are the singular values from the SVD), computes their squares to obtain the probabilities of observing the various states in the Schmidt basis (i.e. eigenvectors of the left-right bipartition reduced density matrices), and puts them into the von Neumann entanglement entropy formula @@S_\text{vN} = - \sum_{n} p_{n} \log{p_{n}}@@.