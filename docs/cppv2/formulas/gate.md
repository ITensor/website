# Applying a Two-site 'Gate' to an MPS

A very common operation with matrix product states (MPS) is 
multiplication by a two-site operator or 'gate' which modifies 
the MPS. This procedure can be carried out in an efficient, 
controlled way which is adaptive in the MPS bond dimension.

Say we have an operator @@G^{s'_3 s'_4}_{s_3 s_4}@@ which
is our 'gate' and which acts on physical sites 3 and 4 of our MPS,
as in the following diagram:

<img class="diagram" width="60%" src="docs/formulas/gate_app_mps.png"/>

To apply this gate in a controlled manner, first 'gauge' the MPS such
that either site 3 or 4 is the 'orthogonality center'.

    MPS psi; //psi is an object of type MPS
    //... prepare psi, for example by initializing it to a particular state
    psi.position(3); //shift the gauge position to site 3

<img class="diagram" width="60%" src="docs/formulas/gate_gauge.png"/>

Next, contract the gate tensor G with the MPS tensors for sites 3 and 4

<img class="diagram" width="60%" src="docs/formulas/gate_contract.png"/>

    auto wf = psi.A(3)*psi.A(4);
    wf *= G;
    wf.noprime();

Finally, use the singular value decomposition (SVD) to factorize the
resulting tensor, multiplying the singular values into either U or V.
Assign these two tensors back into the MPS to update it.

<img class="diagram" width="60%" src="docs/formulas/gate_svd.png"/>

    ITensor S,V;
    ITensor U = psi.A(3); //use psi.A(3) as a 'template' for U
                          //U will be overwritten by the svd function
    svd(wf,U,S,V,{"Cutoff=",1E-8});
    psi.setA(3,U);
    psi.setA(4,S*V);

Note that in the SVD above, we set a truncation error cutoff to truncate 
the smallest singular values and control the size of the resulting MPS.
Other cutoff values can be used, depending on the desired accuracy,
as well as limits on the maximum bond dimension ("Maxm").

Complete code example:

    //assume we have an MPS 'psi' and a gate 'G'
    //G is an ITensor with indices s3, s4, s3', s4' 
    //where s3 and s4 are the third and fourth physical
    //indices of the MPS

    psi.position(3);
    
    auto wf = psi.A(3)*psi.A(4);
    wf *= G;
    wf.noprime();

    ITensor S,V;
    ITensor U = psi.A(3);
    svd(wf,U,S,V,{"Cutoff=",1E-8});
    psi.setA(3,U);
    psi.setA(4,S*V);
    

