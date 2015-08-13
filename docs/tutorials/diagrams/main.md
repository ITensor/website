
<span class='article_title'>How to Read Tensor Diagrams</span>

<span class='article_sig'>Thomas E. Baker&mdash;July 31, 2015</span>

In classical physics, free body diagrams represent the sum of forces in Newton's equations. In quantum field theories, Feyman diagrams represent integrals found in perturbative calculations.  Both examples express a mathematical equation as something more artistic; tensor network diagrams do the same for otherwise complicated summations.

For example, the expectation value of a Hamiltonian as a tensor diagram looks like:

<p align="center"><img src="docs/articles/psiHpsi.png" alt="Diagram" style="width: 400px;"/></p>

$$=\langle\psi|\hat H|\psi\rangle$$

and the summation we are representing here is

$$=\sum_{\sigma_1\ldots\sigma_5,\sigma_1'\ldots\sigma_5'} A^{\sigma_1'\dagger}A^{\sigma_2'\dagger}A^{\sigma_3'\dagger}A^{\sigma_4'\dagger}A^{\sigma_5'\dagger}H^{\sigma_1'\sigma_1}H^{\sigma_2'\sigma_2}H^{\sigma_3'\sigma_3}H^{\sigma_4'\sigma_4}H^{\sigma_5'\sigma_5}A^{\sigma_1}A^{\sigma_2}A^{\sigma_3}A^{\sigma_4}A^{\sigma_5}$$

which shows why we wanted to draw these diagrams instead of writing out this large summation.  The diagram is clearer&mdash;once you understood how to read them.

In this discussion, we will see what the diagrams represent, how to understsand each shape and line in a diagram, and understand other things you might see in a diagram.  We will also connect this with the [[MPS|]] and [[MPO|]] tensor networks used for DMRG and other tensor network methods in another discussion.  Better yet, we'll make sure to connect this entire discussion with ITensor code you can use for your own projects!

<br/>
## Diagrams 101

Each diagram will consist of blobs connected by lines.  Each blob represents a tensor (an object with indices) and each line is the index of that tensor.

For example, one tensor with one line is a vector:

<p align="center"><img src="docs/articles/vector.png" alt="Vector Diagram" style="height: 200px;"/></p>

$$=A^\mu$$

In ITensor, to specify how to make a vector, one may use the code

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

To keep things simple, we've left off arrows in our diagrams.  We'll discuss the role of these when we discuss the quantum block structure for [[MPS|articles/MPS]].


