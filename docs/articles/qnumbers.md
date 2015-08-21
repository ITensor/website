
Using ITensors for all calculations is a perfectly valid way to write a code.  But there is an inherent inefficiency in doing so.  Let's take a look at an @@S^z@@ operator to see why:

$$
S^z=\begin{pmatrix}
\frac12 & 0\\\\
0 & -\frac12\\\\
\end{pmatrix}
$$

Two of the elements are zero.  It is a waste of memory to then store four values.  In fact, in general, there are a lot of zero entries in an ITensor.  IQTensors are implemented in our library to take advantage of the fact that we only need to store non-zero entries of an ITensor.  In this case, we concentrate on group those non-zero entries by quantum number.

## Quantum Numbers

On a diagram, these may be represented with arrows.  The `dag` function automatically reverses the direction of arrows.
