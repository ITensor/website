
<span class='article_title>IQTensors: Blocking ITensors by Quantum Number</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 18, 2015</span>

Finding conserved quantities in a Hamiltonian allows for an efficient rewriting of `ITensor`s so that one can identify elements by the numbers denoting these symmettries: the quantum numbers.  Any time that conserved quantities can be identified in a Hamiltonian, it is advantageous to use `IQTensor`s to keep matrix sizes small and computation times faster.  Using the `ITensor`s where an `IQTensor` could be used means that the MPO will carry around a lot of elements that are zero.

In this article, we will detail how to draw diagrams with quantum numbers, identify quantum numbers in a quantum system, and how to program an `IQTensor`.

## How does ITensor use quantum numbers to make calcultions efficient?

Using `ITensor`s for all calculations is a perfectly valid way to write a code.  But there is an inherent inefficiency in doing so.  Let's take a look at an @@S^z@@ operator to see why:

$$
S^z=\begin{pmatrix}
\frac12 & 0\\\\
0 & -\frac12\\\\
\end{pmatrix}
$$

Two of the elements are zero.  It is a waste of memory to then store four values.  In fact, in general, there are a lot of zero entries in an `ITensor`.  `IQTensors` are implemented in our library to take advantage of the fact that we only need to store non-zero entries of an `ITensor`.  In this case, we concentrate on group those non-zero entries by quantum number.

The `IQTensor` will look like a vector divided into quantum numbers:

## Some examples of Quantum Numbers

parity, charge, U(1)

Supeconductiviity

## Diagrams with Quantum Numbers

Diagrams that display the quantum number flux are drawn with arrows.  Fluxes denote the quantum numbers flowing into and out of a block.

<p align="center"><img src="docs/tutorials/IQTensors/iqtensor.png" alt="Diagram" style="width: 400px;"/></p>

    IQMPS psi;
    psi.A(1);

In order to ensure that the flux represented by the arrows in the diagram are correct, we will construct operators that have the corrent flux structure.  This will ensure that our wavefunctions are evaluated in the correct symmetry sector.

The direction of the arrows are a convention.  We want to keep our ket vectors covariant, @@\psi\_\mu@@, so our operators will raise the index, @@\Lambda^{\mu\nu}\psi\_\mu=\psi^\nu@@ on contraction.  The bra vectors are then identified as contravariant vectors.

<p align="center"><img src="docs/tutorials/IQTensors/iqbra.png" alt="Diagram" style="width: 400px;"/></p>

    dag(psi.A(1));

In practice, we don't need to worry about which is which; simply this determines our convention for the direction of arrows. Note that `dag` function reversed the arrow on the physical index.

The link indices (horizontal lines) are chosen from the orthogonality center.  Consider a singlet:

<p align="center"><img src="docs/tutorials/IQTensors/iqnumber1.png" alt="Diagram" style="width: 400px;"/></p>

We can take an SVD of the wavefunction.  The orthogonality center (red diamond) is the source of the quantum numbers (arrows).

<p align="center"><img src="docs/tutorials/IQTensors/iqnumber2.png" alt="Diagram" style="width: 400px;"/></p>

$$
=UDV^\dagger
$$

    IQMPS psi;
    IQTensor U,D,V;
    SVD(psi,U,D,V);

One option is to roll the orthogonality center into the right site.  The arrow then points to the left, naturally. 

<p align="center"><img src="docs/tutorials/IQTensors/iqnumber3.png" alt="Diagram" style="width: 400px;"/></p>

$$
=U(DV^\dagger)=A\Lambda
$$

    auto A = U;//left-normalized tensor
    auto Lambda = D*V;//orthogonality center


We could also have rolled the tensor left:

<p align="center"><img src="docs/tutorials/IQTensors/iqnumber4.png" alt="Diagram" style="width: 400px;"/></p>

$$
=(UD)V^\dagger=\Lambda B
$$

    B = V;//right-normalized
    Lambda = U*D;//orthogonality center

In a less trivial example, the 

<p align="center"><img src="docs/tutorials/IQTensors/iqnumber5.png" alt="Diagram" style="width: 400px;"/></p>

## Operator fluxes 

The flux for the entire Hamiltonian should be zero.  If we had something other than this, we would not have a conservation law! This implies that on the diagram above has a flux of zero on the left and a flux of zero on the right since if this tensor is on either end of the network, this must be the case.  The easiest way to make sure our overall network has a flux of zero is make sure each element has a total flux of zero.

So, the line flowing into the tensor on the left must be zero.

<p align="center"><img src="docs/tutorials/IQTensors/iqflux.png" alt="Diagram" style="width: 400px;"/></p>

The vertical line provides a flux of +1.  It acts like a source of particles.

  <div class="example_clicker">Show Answer</div>

        The missing quantum number on the operator is -1.  Thus, the in quantum number is 1 while the outgoing number is -1.

## Coding IQMPOs


## Not using IQTensors

If necessary, not using the IQTensors for the structure of the MPO is possible.  One simply needs to write the MPO in an approrpriate basis and then use the `dmrg` function.  This invites an increased cost since there are savings, mentioned above, from using quantum numbers.  We strongly recommend using the `IQTensor` feature.




