# Helpful Reading #
Here are a few papers we have found to be helpful introductions to tensor product or DMRG methods.

## Matrix / Tensor Product State Algorithms ##

* [The density-matrix renormalization group in the age of matrix product states](http://dx.doi.org/10.1016/j.aop.2010.09.012), U.&nbsp;Schollw&ouml;ck, <i>Annals of Physics</i> *326*, p. 96-192 (2011) arxiv:1008.3477

  *Comments*: This paper is currently the most thorough and up-to-date discussion of tensor product state methods, especially DMRG. The concepts described in the paper align closely with the features of the ITensor Library.

* [Algorithms for Entanglement Renormalization](http://prb.aps.org/abstract/PRB/v79/i14/e144108),
  G.&nbsp;Evenbly and G.&nbsp;Vidal, <i>Phys.&nbsp;Rev.&nbsp;B</i> *79*, 144108 (2009) arxiv:0707.1454

  *Comments*: Good introduction to MERA wavefunctions which are a promising post-DMRG application of tensor network ideas.

* [From density-matrix renormalization group to matrix product states](http://iopscience.iop.org/1742-5468/2007/10/P10014/), I.P.&nbsp;McCulloch,  <i>J. Stat. Mech.</i> P10014 (2007) cond-mat/0701428

  *Comments*: Explores many of the practical issues involved in doing DMRG with matrix product states.

* [Finite automata for caching in matrix product algorithms](http://link.aps.org/doi/10.1103/PhysRevA.78.012356), 
  G.M.&nbsp;Crosswhite and D.&nbsp;Bacon, <i>Phys.&nbsp;Rev.&nbsp;A</i> *78*, 012356 
  (2008) arxiv:0708.1221

  *Comments*: This paper is essential for gaining a better understanding of why MPS and MPOs work and how to construct them.

## The Density Matrix Renormalization Group ##

* [The density matrix renormalization group](http://link.aps.org/doi/10.1103/RevModPhys.77.259), U.&nbsp;Schollw&ouml;ck,
  <i>Rev.&nbsp;Mod.&nbsp;Phys.</i> *77*, 259-315 (2005) cond-mat/0409292

  *Comments*: An extremely thorough and well-written review of DMRG methods and applications.

* [Diagonalization and Numerical Renormalization Group Based Methods for Interacting Quantum Systems](http://link.aip.org/link/\?APC/789/93/1),
  R.M.&nbsp;Noack and S.&nbsp;Manmana, <i>AIP Conference Proceedings</i> *789* 93-163, (2005)

  *Comments*: This DMRG review article is very useful because it goes into the nuts and bolts of writing a DMRG code, including
  the Davidson algorithm commonly used as a DMRG sparse matrix eigensolver.

* [Density matrix formulation for quantum renormalization groups](http://link.aps.org/doi/10.1103/PhysRevLett.69.2863),
  S.R.&nbsp;White, <i>Phys.&nbsp;Rev.&nbsp;Lett.</i> *69*, 2863-2866 (1992) 

  *Comments*: Original DMRG paper - named the PRL Milestone of 1992.

* [Infinite size density matrix renormalization group, revisited](http://arxiv.org/abs/0804.2509), I.P.&nbsp;McCulloch,
  arxiv:0804.2509 (2008)

  *Comments*: Solution of the wavefunction acceleration problem plaguing infinite DMRG. This paper really demonstrates
  the power of the MPS formalism.

* [Studying Two Dimensional Systems With the Density Matrix Renormalization Group](http://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-020911-125018), E.M.&nbsp;Stoudenmire and S.R.&nbsp;White,
  arxiv:1105.1374 (2011)

  *Comments*: Lots of useful advice about the best practices for applying DMRG to 2d systems.

[[Back to Main|main]]
