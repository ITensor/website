<span class='article_title'>Why DMRG Works: Information Theory</span>

<span class='article_sig'>Thomas E. Baker & Benedikt Bruognuolo&mdash;October 21, 2015</span>

The Density Matrix Renormalization Group was originally derived without the use of [[Matrix Product States|MPS]] from arguments in the broader theory of renormalization group.  The formulation in terms of MPSs shows why the algorithm works so well: the DMRG algorithm correctly calculates the correct entanglement entropy of the system.

This article provides a basic survey of information theory and its connection to quantum entanglement.

### Why DMRG works:  Information Theory and Entanglement

When receiving a message that is known to have some characters distorted, it is necessary to determine what the uncertainty of a particular character @@x@@ might be (especially if some of the characters are garbled).  Otherwise, how sure are we that this was the original character sent?  We therefore must define a mathematically rigorous quantity which is the uncertainty of obtaining the message @@x@@ and connecting this to the the probability of choosing the correct @@x@@. The quantity we are searching for is most critical to the understanding of how much information can be sent though the communication channel is known as the information entropy (also known as the entanglement entropy).  The first step is to quantify how much uncertainty there is in the message.

Beginning from the most general statements, there are four conditions we can expect on any measure of information passing through a channel [1].

 * The probability, @@\rho@@, should increase with more possibilities, @@M@@ available to sample (i.e., @@\rho(M)<\rho(M')@@ if @@M<M'@@)

Consider the task of finding one star in the universe in comparison with predicting the roll of a six sided die.  The former should have a much higher uncertainty in the choice.

 *  The probabilities for two objects should be additive as @@\rho(ML)=\rho(M)+\rho(L)@@

If we have two objects we want to find from two different sets, then we expect that picking the first object will not affect the uncertainty of choosing the second.

 * Assume the grouping axiom:  the uncertainty of picking an object from the set of @@r@@ elements @@x\_1, x\_2, x\_3, x\_4,\ldots@@ with probabilities @@\rho\_1, \rho\_2, \rho\_3, \rho\_4,\ldots@@ is

$$
H\left(\frac{\rho\_1}{\sum\_{\rho=1}^r \rho\_i},\frac{\rho\_2}{\sum\_{\rho=1}^r \rho\_i},\frac{\rho\_3}{\sum\_{\rho=1}^r \rho\_i},\ldots\right)
$$

and the uncertainty of picking an object,  from the second group is @@x\_{r+1}, x\_{r+2}, x\_{r+3}, x\_{r+4},\ldots@@ is then 

$$
H\left(\frac{\rho\_{r+1}}{\sum\_{\rho=1}^M \rho\_i},\frac{\rho\_{r+2}}{\sum\_{\rho=1}^M \rho\_i},\frac{\rho\_{r+3}}{\sum\_{\rho=1}^M \rho_i},\ldots\right)
$$

the sum of these two equations is the uncertainty in each of the two groups plus a term 

$$
H(\rho\_1+\rho\_2+\rho\_3+\ldots+\rho\_r,\rho\_{r+1}+\ldots+\rho\_M),
$$

signifying the uncertainty for picking either group, are the total uncertainty.

 * Small changes in the probability should produce small changes in the uncertainty so that @@H(p,1-p)@@ is continuous.

With these four assumptions, it can be shown that an entropy  function

$$
S=-C\sum_i\rho\_i\ln\rho\_i
$$

where @@C@@ is a constant and @@\rho_i@@ are the probabilities of the @@i^\mathrm{th}@@ possibility, is the only function that can satisfy the four statements above [2].  The special case of @@C=1@@ is the von Neumann entropy.

The meaning of the information entropy is many-fold, but one of the more transparent meanings is that it is the minimum number of questions you must ask to get the answer (on average). For example, consider many variables that could be the answer.  We can search for the correct answer by asking for a yes or no on each variable ("Is it @@x_1@@? @@x_2@@?...").  The minimum of the average number of these questions is the information entropy.  

By calculating the reduced density matrix correctly, DMRG is automatically maximizing the von Neumann entropy.  This is the fundamental reason why DMRG obtains the correct ground state.

A point worth mentioning here is the area law.  Ground states and low lying excited states tend to follow the area law. The area law states that entanglement scales with system size and dimension for two partitions of a system--in effect, with the area.  In one dimension, the "area" between two blocks is zero-dimensional (it is just a point).  Since entanglement doesn't increase with system size in this case, attacking the problem by maximizing the entropy is efficient.  

DMRG still works in higher dimensions, but the area law says that entanglement will increase with system size (in 2D, the area between partitions is a line while 3D has a sheet between partitions).  This can be seen by recognizing that [[higher dimensional lattices can be mapped to lower dimensional lattices with longer range interactions|tutorials/MPO]].  Increasing entanglement is harder to calculate through DMRG, seen by increasing matrix sizes for the MPO (making individual steps in DMRG slower), hence it is known as a minimally entangled algorithm.

## References

[1] Steven R. White, "Density matrix formulation for quantum renormalization groups" Physical Review Letters 69, 19 (1992)

[2] Robert B. Ash and Catherine Doleans-Dade, Probability and measure theory (Academic Press, 2000).
