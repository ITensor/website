# Introduction to Factorizing ITensors

The real power of tensor algorithms comes from tensor factorization,
which can achieve huge compression of high-dimensional data.
For example, a [matrix product state](https://tensornetwork.org/mps/) 
(a.k.a. tensor train) can be viewed as
the successive factorization of a very high rank tensor.

The ITensor approach to tensor factorizations emphasizes the structure
of the factorization, and does not require knowing the index ordering.

ITensor offers various tensor factorizations, but in this chapter we
focus on the example of the SVD, which is used frequently in physics
applications.

### Singular Value Decomposition

The singular value decomposition (SVD) is a matrix factorization
that is also extremely useful for general tensors.

As a brief review, the SVD is a factorization of a matrix M into the product
$$
M = U S V^\dagger
$$
with U and V having the property @@U^\dagger U = 1@@ and @@V^\dagger V = 1@@.
The matrix S is diagonal and has real, non-negative entries known as the singular
values, which are typically ordered from largest to smallest. 
The SVD is well-defined for any matrix, including rectangular matrices. It also
leads to a controlled approximation, where the error due to discarding columns of U and V
is small if the corresponding singular values discarded are small.

To compute the SVD of an ITensor, you only need to specify which indices are (collectively) 
the "row" indices (thinking of the ITensor as a matrix), with the rest assumed to be the "column" 
indices.

Say we have an ITensor with indices i,j, and k

    T = ITensor(i,j,k)

and we want to treat i and k as the "row" indices for the purpose of the SVD.

To perform this SVD, we can call the function `svd` as follows:

    U,S,V = svd(T,(i,k))

Diagrammatically the SVD operation above looks like:

<img class="diagram" width="95%" src="docs/VERSION/book/images/SVD_Ex1.png"/>

The guarantee of the `svd` function is that the ITensor 
product `U*S*V` gives us back an ITensor identical to T:

    @show norm(U*S*V - T) # typical output: norm(U*S*V-T) = 1E-14

<div class="example_clicker">Click here to view a full working example</div>

    using ITensors

    let
      i = Index(3,"i")
      j = Index(4,"j")
      k = Index(5,"k")

      T = randomITensor(i,j,k)

      U,S,V = svd(T,(i,k))

      @show norm(U*S*V-T)

      return
    end

### Truncating the SVD spectrum

An important use of the SVD is approximating a higher-rank tensor
by a product of lower-rank tensors whose indices range over only
a modest set of values.

To obtain an approximate SVD in ITensor, pass one or more of
the following accuracy parameters as named arguments:

* `cutoff` &mdash; real number @@\epsilon@@. Discard the smallest singular values
  @@\lambda\_n@@ such that the <i>truncation error</i> is less than @@\epsilon@@:
  $$
  \frac{\sum\_{n\in\text{discarded}} \lambda^2\_n}{\sum\_{n} \lambda^2\_n} < \epsilon \:.
  $$
  Using a cutoff allows the SVD algorithm to truncate as many states as possible while still
  ensuring a certain accuracy.

* `maxdim` &mdash; integer M. If the number of singular values exceeds M, only the largest M will be retained.

* `mindim` &mdash; integer m. At least m singular values will be retained, even if some fall below the cutoff

Let us revisit the example above, but also provide some of these accuracy parameters

    i = Index(10,"i")
    j = Index(40,"j")
    k = Index(20,"k")
    T = randomITensor(i,j,k)

    U,S,V = svd(T,(i,k),cutoff=1E-2)

Note that we have also made the indices larger so that the truncation performed will be
non-trivial.
In the code above, we specified that a cutoff of @@\epsilon=10^{-2}@@ be used. We can check that the resulting factorization is now approximate by computing the squared relative error:

    truncerr = (norm(U*S*V - T)/norm(T))^2
    @show truncerr
    # typical output: truncerr = 8.24E-03

Note how the computed error is below the cutoff @@\epsilon@@ we requested.

<div class="example_clicker">Click here to view a full working example</div>

    using ITensors

    let
      i = Index(10,"i");
      j = Index(40,"j");
      k = Index(20,"k");
 
      T = randomITensor(i,j,k)
 
      U,S,V = svd(T,(i,k),cutoff=1E-2)
   
      @show norm(U*S*V-T)
      @show (norm(U*S*V - T)/norm(T))^2
      return
    end

<br/>


<span style="float:left;"><img src="docs/VERSION/arrowleft.png" class="icon">
[[Contracting ITensors|book/itensor_contraction]]
</span>

<span style="float:right;"><img src="docs/VERSION/arrowright.png" class="icon">
[[Case Study: TRG Algorithm|book/trg]]
</span>

<br/>
