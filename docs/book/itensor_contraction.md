# ITensor Contraction

Tensor contraction is often the most expensive
part of a tensor algorithm. 
Code for contracting tensors can also be quite fragile
and error-prone.
ITensor makes it possible to transcribe tensor
contraction diagrams directly to high-level code. 
The resulting code is robust to changes in 
implementation details, such as the ordering
of tensor indices.

Pairs of ITensors are contracted by "multiplying" them
using the `*` operator, which sums over all matching indices.

### A Simple Example

Given Index objects i,j,k and ITensors

    auto A = ITensor(i,j);
    auto B = ITensor(k,j);

the code

    auto C = A * B;

computes the elementwise operation
$$
C\_{i k} = \sum\_j A\_{i j} B\_{k j} \ .
$$
In other words, C is the result of contracting of A and B
over the index j. If there had been other matching indices
besides j, the `*` operator would have contracted them too.
Indices i and k did not match, so they appear on the result C.

Interestingly, because of the way ITensor contraction is defined
`B*A` gives the same result as `A*B`.
Contraction in ITensor is a commutative operation.

### A More Complex Example

Of course, the real usefulness of a tensor library is in handling
cases where tensors have three or more indices.

Say we have an ITensor with indices i,s, and j
     
    auto W = ITensor(i,s,j);

and want to contract W with itself, summing over indices i and j,
but leaving s uncontracted.

In "classical" tensor notation, we want to compute
$$
D\_{s s^\prime} = \sum\_{i,j} W\_{i s j} W\_{i s^\prime j} \ .
$$
But this notation can be difficult to read for complicated contractions.

A nicer way to visualize this tensor contraction is 
to use the following diagram

<img class="diagram" width="300px" src="docs/book/images/WW_contraction.png"/>

In diagram notation a tensor is a blob and each line denotes an index. 
Connecting two lines implies those indices are summed over.
The remaining unpaired lines are the indices of the resulting tensor.

Both notations indicate our contraction strategy should be to 
prime the Index s on one copy of W. Calling `prime(W,s)` returns
a copy of W with s replaced by s'. Then doing

    auto D = W * prime(W,s);

automatically contracts over i and j, but not s and s' since these
no longer compare equal. Printing the result D confirms that it
has only i and j as indices.



<span style="float:left;"><img src="docs/book/images/left_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[ITensor Basics|book/itensor_basics]]
</span>
