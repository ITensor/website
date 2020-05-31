# Applying a Two-site Operator to an MPS

A very common operation with matrix product states (MPS) is 
multiplication by a two-site operator or "gate" which modifies 
the MPS. This procedure can be carried out in an efficient, 
controlled way which is adaptive in the MPS bond dimension.

Say we have an operator @@G^{s'_3 s'_4}_{s_3 s_4}@@ which
is our gate and which acts on physical sites 3 and 4 of our MPS `psi`,
as in the following diagram:

<img class="diagram" width="60%" src="docs/VERSION/formulas/mps_twosite_op/gate_app_mps.png"/>

To apply this gate in a controlled manner, first 'gauge' the MPS `psi` such
that either site 3 or 4 is the *orthogonality center*. Here we make site 3
the center:

    orthogonalize!(psi,3)

<img class="diagram" width="60%" src="docs/VERSION/formulas/mps_twosite_op/gate_gauge.png"/>

The other MPS tensors are now either left-orthogonal or right-orthogonal and can be
left out of further steps without producing incorrect results.

Next, contract the gate tensor G with the MPS tensors for sites 3 and 4

<img class="diagram" width="85%" src="docs/VERSION/formulas/mps_twosite_op/gate_contract.png"/>

    wf = psi[3] * psi[4]
    wf *= G
    noprime!(wf)

Finally, use the singular value decomposition (SVD) to factorize the
resulting tensor, multiplying the singular values into either U or V.
Assign these two tensors back into the MPS to update it.

<img class="diagram" width="85%" src="docs/VERSION/formulas/mps_twosite_op/gate_svd.png"/>

    U,S,V = svd(wf,inds(psi[3]),cutoff=1E-8)
    psi[3] = U
    psi[4] = S*V

Passing `inds(psi[3])` to the `svd` function tells it to treat any indices of
the ITensor `wf` that are shared with `psi[3]` as "row" indices which should
go onto the `U` tensor afterward.
We also set a truncation error cutoff of 1E-8 in the call to `svd` to truncate 
the smallest singular values and control the size of the resulting MPS.
Other cutoff values can be used, depending on the desired accuracy,
as well as limits on the maximum bond dimension (`maxdim` keyword argument).

### Complete code example

    orthogonalize!(psi,3)
    
    wf = psi[3] * psi[4]
    wf *= G
    noprime!(wf)

    U,S,V = svd(wf,inds(psi[3]),cutoff=1E-8)
    psi[3] = U
    psi[4] = S*V
