<span class='article_title'>iDMRG:  Calculating infinite systems</span>

<span class='article_sig'>Thomas E. Baker and Benedikt Bruognolo&mdash;September 16, 2015</span>

If we want to calculate a translationally invariant system, such as an infinite spin-1 chain, then we can use the iDMRG algorithm which grows a large system in a computationally cost effective way to approximate the bulk of large system.  The bulk of a large system mimicks the translationally invariant system.  Calculating infinite systems with DMRG uses the same concepts as [[finite DMRG|tutorials/DMRG]] but does so in a slightly different way.  It is most convenient to use the [[@@\Lambda\Gamma@@|tutorials/MPS]], iDMRG for unit cells with even numbers of sites and odd numbered unit cells.  ITensor's `idmrg` function is detailed [[here|TEBbook/iDMRG]].


## The Algorithm: Infinite DMRG (iDMRG)

Having understood @@\Lambda\Gamma@@ notation, we can introduce the algorithm used by ITensor to calculate the infinite system ground state.

We first begin with an even numbered unit cell (and will discuss the odd unit cell variation afterward) and use an example of a two-site unit cell.  Use of the ITensor function `idmrg` is in the next section.

The two-site unit cell appears diagrammatically as 

<p align="center"><img src="docs/tutorials/iDMRG/unitcell.png" alt="unit cell" style="width: 600px;"/></p>

The @@\Lambda^{-1}@@ term is introduced to make the cell translationally invariant.  If we go back to our discussion of the @@\Lambda\Gamma@@ notation, then we notice that our infinite system is a series of repeating @@\Lambda\Gamma@@ terms like @@\ldots\Lambda\Gamma\Lambda\Gamma\Lambda\Gamma\ldots@@.  But our two site unit cell does not have this form in AB notation by itself!  We are missing a factor of @@\Lambda^{-1}@@ that we included above.

$$
\mathrm{Unit\;Cell}=A\Lambda B\Lambda^{-1}=\Lambda\Gamma\Lambda\Gamma\Lambda\Lambda^{-1}
$$

This produces a translationally invariant unit cell.  Note that we also could have placed the @@\Lambda^{-1}@@ on the left side instead of the right side as shown above.

### Initialization

The main idea of iDMRG is to start with a finite system and insert the unit cell repeatedly until self-consistency.  To begin, we start with the smallest finite system of equal size to the unit cell.  We can run a [[finite system DMRG calculation|tutorials/DMRG]] to obtain the ground state of just the two-site system.
<p align="center"><img src="docs/tutorials/iDMRG/two-site.png" alt="two site" style="width: 300px;"/></p>

$$
=|\psi\rangle
$$

But the wave function for the two-site unit cell does not approximate the infinite system very effectively because it has edges, so the goal will be to start with this wavefunction and grow the system in the middle.  Edge effects from the incorrect boundary conditions will go away as we grow the system.

To prepare the system for an insertion of the unit cell, we take an SVD of this wavefunction and obtain the following diagram
<p align="center"><img src="docs/tutorials/iDMRG/two-site_SVD.png" alt="two site" style="width: 300px;"/></p> 

$$
=A^1_0\Lambda_0 B^2_0
$$

The subscripts corresponds to the level of the calculation (we start on the 0th level).  The @@\Lambda_0@@ tensor is information we need for the first level.  Superscripts show the site index; a site index does not belong to the orthogonality matrix because it sits in between @@A@@ and @@B@@.

The first level of the calculation requires the determination of the system with two unit cells.

<p align="center"><img src="docs/tutorials/iDMRG/four-site.png" alt="two site" style="width: 400px;"/></p>

Once again placing the orthogonality center in the middle, we obtain

<p align="center"><img src="docs/tutorials/iDMRG/four-site_SVD.png" alt="two site" style="width: 400px;"/></p>

$$
=A^1_1A^2_1\Lambda_1 B^3_1B^4_1
$$

This completes the initialization of the problem.  We are now ready to insert the unit cell and may do so with the following steps.  

### Growing the system

The inner two sites of the four-site system look like our unit cell.

<p align="center"><img src="docs/tutorials/iDMRG/four-site_env.png" alt="two site" style="width: 500px;"/></p> 

$$
=A^1_1\Big]A^2_1\Lambda_1 B^3_1\Big[B^4_1
$$

In the diagram above, we have blocked off the inner two sites, sites 2 and 3, from the left and right environment blocks.  The environment tensors will not change for the rest of the computation.  Let's grow the system size by inserting unit cells in between the braces we drew on the diagram.  For example, we show one unit cell inserted (between parentheses) as

<p align="center"><img src="docs/tutorials/iDMRG/unitcellinsert.png" alt="Inserted unit cell" style="width: 500px;"/></p>

$$
=A_1^1\Big]\Big(A_1^2\Lambda_1 B^3_1\Lambda_0^{-1}\Big)A_1^4\Lambda_1 B_1^5\Big[B_1^6
$$

The subscript on @@\Lambda\_0^{-1}@@ is best justified when we review the general algorithm below.  We will briefly mention it is a question of matching the bases of the many body states in the @@U@@ and @@V^\dagger@@ matrices of the SVD. It can be regarded as being consistent with the general algorithm.

The two terms @@A\Lambda B@@ between the braces can be regauged in two ways.  We can "roll" the orthogonality center to the left

<p align="center"><img src="docs/tutorials/iDMRG/rollleft.png" alt="roll left" style="width: 500px;"/></p>

$$
A_1^4\Lambda_1 B_1^5\rightarrow\Lambda_2^L B_2^4B_1^5
$$

Note that the tensor on the right, the rightmost B, is unchanged.  The tensor A has been changed, however. 

We can also roll the center to the right

<p align="center"><img src="docs/tutorials/iDMRG/rollright.png" alt="roll right" style="width: 500px;"/></p>

$$
A_1^2\Lambda_1 B_1^3\rightarrow A_1^2A_2^3\Lambda^R_2
$$

The leftmost tensor @@A_1^2@@ has not been changed while the other, @@B_1^3@@, has.  At this point, we should keep track of which tensors correspond to the current iteration (do not change) and which tensors belong to the next iteration (do change). 

Assigning subscripts of 1 for this step and 2 for the next, we get after rolling

<p align="center"><img src="docs/tutorials/iDMRG/unitcellinsertrolled.png" alt="unit cell roll right" style="width: 500px;"/></p>

$$
A^1_1\Big]\Big(A^2_1\Lambda_1 B^3_1\Lambda^{-1}\_0\Big)A^4_1\Lambda_1 B^5_1\Big[B^6_1
$$
$$
=A_1\Big]\Big(A_1 A_2\Lambda^L_2\Lambda^{-1}\_0\Big)\Lambda_2^RB_2 B_1\Big[B_1
$$

The environment is then grown by one tensor (in the case of a unit cell bigger than two sites, each environment receives the number of tensors in a unit cell divided by two).

<p align="center"><img src="docs/tutorials/iDMRG/newenv.png" alt="unit cell updated environment" style="width: 500px;"/></p>

$$
=A_1A_1\Big] A_2\Lambda^L_2\Lambda_0^{-1}\Lambda_2^RB_2 \Big[B_1B_1
$$

The term @@A_2\Lambda_2^L\Lambda_0^{-1}\Lambda_2^RB_2@@ inside the bracket can then be placed into a [[Davidson|tutorials/davidson]] algorithm.  The output of the Davidson algorithm, decomposed into @@A_2\Lambda_2B_2@@ by an SVD and used in the next step of the algorithm, is the optimized approximation of the ground state. For more sites in the unit cell, we would sweep through the lattice like in finite system DMRG to optimize the unit cell.

### General algorithm

Let's skip ahead to a higher step (@@n@@) and see what everything looks like to review.  Many steps into the algorithm, we have a network that looks like

<p align="center"><img src="docs/tutorials/iDMRG/whole1.png" alt="Deep algorithm" style="width: 500px;"/></p>

$$
=\ldots A\_{n-2}A\_{n-1}\Big]A\_n\Lambda\_nB\_n\Big[B\_{n-1}B\_{n-2}\ldots
$$

Inserting a unit cell, we find

<p align="center"><img src="docs/tutorials/iDMRG/whole2.png" alt="Deep algorithm insert unit cell" style="width: 500px;"/></p>

$$
=\ldots A\_{n-2}A\_{n-1}\Big]\Big(A\_n\Lambda\_nB\_n\Lambda^{-1}\_{n-1}\Big)A\_n\Lambda\_nB\_n\Big[B\_{n-1}B\_{n-2}\ldots
$$

We now discuss why we use the @@\Lambda^{-1}@@ from the @@n-1@@th step.   After the optimization (i.e., [[Davidson|tutorials/Lanczos]] and [[SVD|tutorials/SVD]] steps), we have a term like @@A\_n\Lambda\_nB\_n@@ but the basis of the links connected to the environment tensors must be the same as the first and last tensor in the block.  The environment tensors have links defined in the previous iteration, so they must connect to the tensor from the @@n-1@@th step.

Rolling left and rolling right, we obtain

<p align="center"><img src="docs/tutorials/iDMRG/whole3.png" alt="Rolling the unit cell" style="width: 500px;"/></p>

$$
=\ldots A\_{n-2}A\_{n-1}\Big]A\_nA\_{n+1}\Lambda^L\_{n+1}\Lambda^{-1}\_{n-1}\Lambda^R\_{n+1}B\_{n+1}B\_n\Big[B\_{n-1}B\_{n-2}\ldots
$$

Now we can grow the environment blocks by one tensor.  The environment block tensors never need to be touched again.
 
<p align="center"><img src="docs/tutorials/iDMRG/whole4.png" alt="Grow environment" style="width: 500px;"/></p>

$$
=\ldots A\_{n-2}A\_{n-1}A\_n\Big]A\_{n+1}\Lambda^L\_{n+1\}\Lambda^{-1}\_{n-1}\Lambda^R\_{n+1}B\_{n+1}\Big[B\_nB\_{n-1}B\_{n-2}\ldots
$$

We can use the Davidson algorithm to find the optimal ground state of the term inside the braces @@A\_{n+1}\Lambda^L\_{n+1\}\Lambda^{-1}\_{n-1}\Lambda^R\_{n+1}B\_{n+1}@@ and obtain the SVD of this expression.  This gives the updated tensor @@A\_{n+1}\Lambda\_{n+1}B\_{n+1}@@. Then we can restart the process until  the [[norm of the overlap|tutorials/SVD]] of @@\Lambda@@ matrices is the identity between steps.

$$
\langle\Lambda\_{n-1}|\Lambda\_n\rangle=1
$$

### Odd numbered unit cells

This is not implemented in ITensor at the current time but is similar to the even numbered unit cell algorithm.  The extra tensor is pulled in from the environment when necessary and replaced once computation is finished for that step.

## References

[1] IP McCulloch, arXiv preprint arXiv:0804.2509 (2008) 
