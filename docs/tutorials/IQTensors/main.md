
<span class='article_title>IQTensors: Blocking ITensors by Quantum Number</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 18, 2015</span>

Finding conserved quantities in a Hamiltonian allows for an efficient rewriting of ITensors so that one can identify elements by the numbers denoting these symmettries: the quantum numbers.  Any time that conserved quantities can be identified in a Hamiltonian, it is advantageous to use IQTensors to keep matrix sizes small and computation times faster.  Using the ITensors where an IQTensor could be used means that the MPO will carry around a lot of elements that are zero.

In this article, we will detail how to draw diagrams with quantum numbers, identify quantum numbers in a quantum system, and how to program an IQTensor.

## Some examples of Quantum Numbers

parity, charge, U(1)

Supeconductiviity

## Coding IQMPOs

## Diagrams with Quantum Numbers and Fluxes

Diagrams that display the quantum number flux are drawn with arrows.  Fluxes denote the quantum numbers flowing into and out of a block.

<p align="center"><img src="docs/tutorials/IQTensors/iqtensor.png" alt="Diagram" style="width: 400px;"/></p>

    IQMPS psi;
    psi.A(1);

The flux for the entire Hamiltonian should be zero.  If we had something other than this, we would not have a conservation law! This implies that on the diagram above has a flux of zero on the left and a flux of zero on the right since if this tensor is on either end of the network, this must be the case.  The easiest way to make sure our overall network has a flux of zero is make sure each element has a total flux of zero.

So, the line flowing into the tensor on the left must be zero.

<p align="center"><img src="docs/tutorials/IQTensors/iqflux.png" alt="Diagram" style="width: 400px;"/></p>

The vertical line provides a flux of +1.  It acts like a source of particles.

