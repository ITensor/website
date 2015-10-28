# Factorizing ITensors

The real power of tensor algorithms comes from tensor factorization,
which can achieve huge compression of high-dimensional data.
For example, a matrix product state (tensor train) can be viewed as
the successive factorization of a very high rank tensor.

The ITensor approach to tensor factorizations emphasizes the structure
of the factorization, and does not require knowing the index ordering.

### Singular Value Decomposition

The singular value decomposition (SVD) is a matrix factorization
that is also extremely useful for general tensors.

As a brief review, the SVD is a factorization of a matrix M into the product
$$
M = U S V^\dagger
$$
with U and V having the property @@U^\dagger U = 1@@ and @@V^\dagger V = 1@@.
The matrix S is diagonal and has real, non-negative entries known as the singular
values. The  SVD can be computed for arbitrary, rectangular matrices. It also
leads to a controlled approximation, where the error due to discarding columns of U and V
is small if the corresponding singular values are small.
For more background reading on the SVD, see our [[SVD tutorial article|tutorials/svd]].

To compute the SVD of an ITensor, you only need to think about which indices are the "row"
indices (thinking of the ITensor as a matrix), with the rest assumed to be the "column" 
indices.

Say we have an ITensor with indices i,j, and k

    auto T = ITensor(i,j,k);

and we want to treat i and k as the "row" indices for the purpose of the SVD.

We create ITensors U,S, and V to hold the results of the SVD. ITensors S and V can be 
blank, but we will give U the indices i and k to tell the SVD algorithm these
are the "row" indices

    ITensor U(i,k),S,V;
    svd(T,U,S,V);

The call to `svd` function computes the SVD of T and overwrites U,S,V with the results.
Diagrammatically this looks like:

<img class="diagram" width="95%" src="docs/book/images/SVD_Ex1.png"/>

Note that after the SVD, ITensor U still has indices i and k, but also a new index
shared with S. ITensor V gets the index j from T and has the other index of S.
Because of this index structure, the ITensor product `U*S*V` gives us back
an ITensor identical to T:

    Print(norm(U*S*V - T)); //typical output: norm(U*S*V-T) = 1E-13


<div class="example_clicker">Click here to view a full working example</div>

    #include "itensor/svdalgs.h"
    using namespace itensor;

    int main() 
    {
    auto i = Index("index i",3),
         j = Index("index j",4),
         k = Index("index k",5);

    //Make a random ITensor with indices i,j,k
    auto T = randomTensor(i,j,k);

    ITensor U(i,k),S,V;
    svd(T,U,S,V);

    Print(norm(U*S*V-T));

    return 0;
    }

The precise details of the indices of S are not usually important.
However, if needed one can obtain these indices by calling `commonIndex`:

    auto ui = commonIndex(S,U); //get the index S shares with U
    auto vi = commonIndex(S,V); //get the index S shares with V




<span style="float:left;"><img src="docs/book/images/left_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Contracting ITensors|book/itensor_contraction]]
</span>


