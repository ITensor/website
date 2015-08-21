
<span class='article_title'>How to Read Tensor Diagrams</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 20, 2015</span>

In classical physics, free body diagrams represent the sum of forces in Newton's equations. In quantum field theories, Feyman diagrams represent integrals found in perturbative calculations.  Both examples express a mathematical equation as a picture; tensor network diagrams do the same for summations.

For example, the expectation value of a Hamiltonian as a tensor diagram looks like:

<p align="center"><img src="docs/articles/psiHpsi.png" alt="Diagram" style="width: 400px;"/></p>

$$=\langle\psi|\hat H|\psi\rangle$$

and the summation we are representing here is

$$=\sum\_{\begin{matrix}
\sigma\_1\ldots\sigma\_5\\\\
\sigma\_1'\ldots\sigma\_5'\\\\
\end{matrix}}
\sum\_{
\begin{matrix}
b\_1'\ldots b\_4'\\\\
a\_1\ldots a\_4\\\\
b\_1\ldots b\_4\\\\
\end{matrix}}
A\_{b\_1'b\_2'}^{\sigma\_2'\dagger}A\_{b\_1'}^{\sigma\_1'\dagger}A\_{b\_2'b\_3'}^{\sigma\_3'\dagger}A\_{b\_3'b\_4'}^{\sigma\_4'\dagger}A\_{b\_4'}^{\sigma\_5'\dagger}H\_{a\_1}^{\sigma\_1'\sigma\_1}H\_{a\_1a\_2}^{\sigma\_2'\sigma\_2}H\_{a\_2a\_3}^{\sigma\_3'\sigma\_3}H\_{a\_3a\_4}^{\sigma\_4'\sigma\_4}H\_{a\_4}^{\sigma\_5'\sigma\_5}A\_{b\_1}^{\sigma\_1}A\_{b\_1b\_2}^{\sigma\_2}A\_{b\_2b\_3}^{\sigma\_3}A\_{b\_3b\_4}^{\sigma\_4}A\_{b\_4}^{\sigma\_5}$$

which shows why we wanted to draw these diagrams instead of writing out this summation.  The diagram is clearer&mdash;once you understood how to read them.

In this discussion, we will see what the diagrams represent, how to understsand each shape and line in a diagram, and understand other things you might see in a diagram.  We will also connect this with the [[MPS|]] and [[MPO|]] tensor networks used for DMRG and other tensor network methods in another discussion.  Better yet, we'll make sure to connect this entire discussion with ITensor code you can use for your own projects!

<br/>
## Diagrams 101

Each diagram will consist of blobs connected by lines.  Each blob represents a tensor (an object with indices) and each line is the index of that tensor.

For example, one tensor with one line is a vector:

<p align="center"><img src="docs/articles/vector.png" alt="Vector Diagram" style="height: 200px;"/></p>

$$=A^\mu$$

To make a vector in ITensor, one may use the code

    Index mu("mu",m);//Index mu ranges from 1 to m
    ITensor A(mu);

Since a matrix is a rank two object (there are two indices), the diagrammatic representation looks like

<p align="center"><img src="docs/articles/matrix.png" alt="Matrix Diagram" style="height: 150px;"/></p>

$$=A^{\mu\nu}$$

    Index mu("mu",m),nu("nu",n);//for an (m x n) matrix
    ITensor A(mu,nu);

A trace over matrices would look like

<p align="center"><img src="docs/articles/trace.png" alt="Matrix Diagram" style="width: 350px;"/></p>

$$=\sum_{\alpha\beta\gamma\eta} A^{\alpha\beta}B^{\beta\gamma}C^{\gamma\eta}D^{\eta\alpha}$$

    Index a("a",z),b("b",y),c("c",x),d("d",w),e("e",v);
    ITensor A(a,b),B(b,c),C(d,e),D(e,a);
    ITensor Tr = A*B*C*D;

Note that when two ITensors are multiplied with the `*` operator, any matching Index is automatically summed over!

Diagrams can be simple, like those above, or they can be complicated like this one:

<p align="center"><img src="docs/articles/complex.png" alt="Matrix Diagram" style="width: 350px;"/></p>

$$=\sum_{\gamma\delta\eta\mu} A^{\alpha\beta\gamma\delta\eta\mu}B^{\gamma\delta\eta\mu\nu\zeta}$$

    Index a("a",z),b("b",y),c("c",x),d("d",w),e("e",v),
          f("f",u),g("g",t),h("h",s);
    ITensor A(a,b,c,d,e,f),B(c,d,e,f,g,h);
    ITensor C = A*B;

## MPSs and MPOs

Returning to our example at the top of the page.  One tensor in a [[matrix product state|tutorials/MPS]] (purple or red block) has two or three indices.  The vertical lines (superscripts) have a different meaning from the horizontal lines (sub-indices).  In ITensor, they are defined as a rank two or three tensor:  one Site (or physical) index and one or two link indices.

One tensor in a [[matrix product operator|tutorials/MPO]] (gray boxes) has two physical indices and one or two link indices. So, it is a rank three or four tensor. The tensors on the edge of the network (sites 1 and 5) have a different form from those in the bulk (sites 2-4).  One can see this by the different numbers of indices on the edges.  That is why there is one less link index on each of the MPS and the MPO.  

### IQMPS

To keep things simple, we've left off arrows in our diagrams.  We'll discuss the role of these when we discuss the quantum block structure for [[IQTensors|articles/IQTensor]].


