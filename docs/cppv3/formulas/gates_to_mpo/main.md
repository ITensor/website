# Transforming a Set of Gates into an MPO

Here we describe how to transform a set of gates into an MPO.

Imagine we have a Hamiltonian that is a sum of local terms
$$
H = \sum\_j h\_{j,j+1}
$$
where @@h\_{j,j+1}@@ only acts non-trivially on sites j and (j+1).

Part of a Trotter decomposition may look like:
$$
e^{-\tau H} \approx e^{-\tau h\_{1,2}} e^{-\tau h\_{2,3}} \cdots e^{-\tau h\_{N-1,N}}
$$

We can turn this into an MPO with the following code:

    include:docs/VERSION/formulas/gates_to_mpo/gates_to_mpo.cc

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/tevol_trotter/tevol_trotter.cc">Download the full example code</a>
