<span class='article_title'>Periodic vs Open or Infinite Boundary Conditions for DMRG, Which Should You Choose?</span>

<span class='article_sig'>Miles Stoudenmire&mdash;April 28, 2014</span>

One of the weaknesses of the density matrix renormalization group (DMRG) [<a href="#dmrg">1</a>] is that it works
poorly with periodic boundary conditions. This stems from the fact
that conventional DMRG works with open-boundary matrix product state (MPS)
wavefunctions, even if the Hamiltonian itself physically imposes periodic boundary conditions (PBC).

But this begs the question, when are periodic boundary conditions really needed? DMRG offers
some compelling alternatives to PBC:

* Use open boundary conditions (OBC). Though this introduces edge effects, the number of states needed
  to reach a given accuracy is <i>drastically</i> lower than with PBC (see next section below). For gapped systems DMRG
  scales linearly with system size, meaning often one can study systems with many hundreds or even
  thousands of sites.

* Use smooth boundary conditions. The basic idea is to use OBC but 
  send the Hamiltonian parameters smoothly to zero at the boundary so that the system can not "feel"
  the boundary. For certain systems this can drastically reduce edge effects [<a href="#sbc">2</a>].

* Use "infinite boundary conditions," that is, use infinite DMRG. This has a cost that can 
  be even less than with OBC yet is completely free of finite-size effects.

However, there are cases where PBC can be preferable. Here are a few such cases:

* Benchmarking DMRG against another code that uses PBC, such as a Monte Carlo or exact diagonalization code.

* Extracting the central charge of a critical one-dimensional system described by a CFT. In practice, using
  PBC can give an accurate central charge even for quite small systems by fitting the subsystem entanglement
  entropy to the CFT scaling form.

* Checking for the presence or absence of topological effects. These could be edge effects (the Haldane
  phase has a four-fold ground state degeneracy with OBC, but not with PBC), or could be related to some
  global topological sector that is ill-defined with PBC (e.g. periodic vs. antiperiodic boundary conditions
  for the transverse field Ising model).

(Note that in the remaining discussion, by PBC I mean  *fully periodic* boundary conditions in all directions.
For the case of DMRG applied to quasi-two-dimensional systems, it remains a good practice to use
periodic boundaries in the shorter direction, while still using open (or infinite) boundaries
in the longer direction along the DMRG/MPS path.)

Below I discuss more about the problems with using PBC, as well as some misconceptions about when PBC seems
necessary even though there are better alternatives.

## Drawbacks of Periodic Boundary Conditions

Periodic boundary conditions are straightforward to implement in DMRG. The simplest approach is 
to include a "long bond" directly connecting site 1 to site N in the Hamiltonian. However this 
naive approach has a major drawback: if open-boundary DMRG achieves a given accuracy when keeping _m_ states,
then to reach the same accuracy with PBC one must keep _m<sup>2</sup>_ states! The reason is that now every
bond of the MPS not only carries local entanglement as with OBC, but also the entanglement between the first
and last sites.

This change in scaling from  _m_ to _m<sup>2</sup>_  is a severe problem.
For example, many gapped one-dimensional systems only require about m=100 to reach good accuracy
(truncation errors of less than 1E-9 or so). To reach the same accuracy with naive PBC would then
require using 10,000 states, which can easily fill the RAM of a typical desktop computer for a large enough
system, not to mention the extra time needed to work with larger matrices.

But poor scaling is not the only drawback of PBC. Systems that exhibit spontaneous symmetry breaking 
are simple to work with under OBC, where one has the additional freedom of applying edge pinning terms 
to drive the bulk into a specific symmetry sector. Using edge pinning reduces the bulk entanglement and makes measuring 
order parameters straightforward. Similarly one can use infinite DMRG to directly observe symmetry breaking effects.

But under PBC, order parameters remain equal to zero and can only be accessed through correlation functions.
Though using correlation functions is often presented as the "standard" or "correct" approach, such reasoning pre-supposes that PBC is
the best choice. However, recent work in the quantum Monte Carlo community demonstrates 
that open boundaries with pinning fields can be a superior approach [<a href="#pinning">3</a>].


## Cases Where Periodic BC Seems Necessary, But Open/Infinite BC Can be Better

Below are some cases where periodic boundary conditions seem to be necessary at a first glance. 
But in many of these cases, not only can open or infinite boundaries be just as successful, they 
can even be the better choice.

* _Measuring asymptotic properties of correlation functions_: much of our understanding
of gapless one-dimensional systems comes from field-theoretic approaches which make specific predictions
about asymptotic decays of various correlators. To test these predictions numerically, one must 
work with very large systems and avoid edge effects, so researchers often turn to using
fully periodic boundary conditions on very large systems. However, a superior choice is to use
infinite DMRG, which combines the much better scaling of open-boundary DMRG with the ability to 
measure correlators at _arbitrarily long_ distances by repeating the unit cell of the MPS wavefunction.
Although truncating to a finite number of states imposes an effective correlation length on the system,
this correlation length can reach many thousands of sites for quite reasonable MPS bond dimensions.
Karrasch and Moore took advantage of this fact to convincingly check the predictions of Luttinger liquid
theory for one-dimensional systems of gapless fermions [<a href="#karrasch">4</a>].

* _Studying two-dimensional topological order_: a hallmark of intrinsic topological order is the presence
of a robust ground state degeneracy when the system is put on a torus. Also many topological phases 
have gapless edge states which can cause problems for numerical calculations. Thus one might think that
fully periodic BC are the best choice for studying topological phases. However, 
topological phases have the same ground-state degeneracy on an infinite cylinder
as they do on a torus [<a href="#zhang">5</a>]. Cincio and Vidal exploited this fact to use infinite DMRG
to study a variety of topological phases [<a href="#cincio">6</a>]. One part of their calculation did actually require
obtaining ground states on a torus, but they accomplished this by taking a finite segment of an infinite MPS 
and connecting its ends. This approach does not give the true ground state of the torus but was sufficient 
for their calculation and was arguably closer to the true two-dimensional physics.

* _Obtaining bulk gaps_: DMRG has the ability to "target" low-lying excited states or to obtain such
states by constraining them to be orthogonal to the ground state. However, with OBC, localized excitations 
can get stuck to the edges and not reveal the true bulk gap behavior. Thus one may conclude that PBC is 
necessary. But using open or infinite boundaries remains the better choice because they allow much higher accuracy.

  To deal with the presence of edges in OBC, one can use "restricted sweeping". Here one sweeps across the 
full system to obtain the ground state. Then, to obtain the first excited state one only sweeps through the
bulk of the system, allowing the wavefunction to change arbitrarily there but remain fixed in the ground state
near the edges. This traps the particle in a "soft box" which still lets its wavefunction mix with the basis that
describes the ground state outside the restricted sweeping region.

  Within infinite DMRG, boundary effects are rigorously absent if the calculation has converged. To compute bulk 
gaps one again uses a type of restricted sweeping known in the literature as "infinite boundary conditions". For
more see the work by Phien, Vidal, and McCulloch [<a href="#phien">7</a>].


In conclusion, consider carefully whether you really need to use periodic boundary conditions, as they impose
a steep computational cost within DMRG. Periodic BC can actually be worse for the very types of measurements where they are 
often presented as the best or "standard" choice. Many of the issues periodic boundaries circumvent
can be avoided more elegantly by using infinite DMRG, or when that is not applicable, by using open boundary
conditions with sufficient care.

<hr/>

<a name="dmrg"></a>[1] By DMRG, I also mean DMRG-like algorithms such as time-dependent DMRG (tDMRG a.k.a. time-evolving 
block decimation TEBD) or really any other algorithm that works with open-boundary MPS.

<a name="sbc"></a>[2] References on smooth boundary conditions:

* [Smooth boundary conditions for quantum lattice systems](http://dx.doi.org/10.1103/PhysRevLett.71.4283), M.&nbsp;Vekic and Steven&nbsp;R.&nbsp;White, <i>Phys. Rev. Lett.</i> <b>71</b>, [4283](http://dx.doi.org/10.1103/PhysRevLett.71.4283) (1993) cond-mat/[9310053](http://arxiv.org/abs/cond-mat/9310053)

* [Hubbard model with smooth boundary conditions](http://dx.doi.org/10.1103/PhysRevB.53.14552), M.&nbsp;Vekic and Steven&nbsp;R.&nbsp;White, <i>Phys. Rev. B</i> <b>53</b>, [14552](http://dx.doi.org/10.1103/PhysRevB.53.14552) (1996) cond-mat/[9601009](http://arxiv.org/abs/cond-mat/9601009)

* [Grand canonical finite-size numerical approaches: A route to measuring bulk properties in an applied field](http://link.aps.org/doi/10.1103/PhysRevB.86.041108), Chisa&nbsp;Hotta and Naokazu&nbsp;Shibata, <i>Phys. Rev. B</i> <b>86</b>, [041108](http://link.aps.org/doi/10.1103/PhysRevB.86.041108) (2012) 

<a name="pinning"></a>\[3\] [Pinning the Order: The Nature of Quantum Criticality in the Hubbard Model on Honeycomb Lattice
](http://dx.doi.org/10.1103/PhysRevX.3.031010), Fakher&nbsp;F.&nbsp;Assaad and Igor&nbsp;F.&nbsp;Herbut, <i>Phys. Rev. X</i> <b>3</b>, [031010](http://dx.doi.org/10.1103/PhysRevX.3.031010)

<a name="karrasch"></a>\[4\] [Luttinger liquid physics from the infinite-system density matrix renormalization group](http://dx.doi.org/10.1103/PhysRevB.86.155156), C.&nbsp;Karrasch and J.E.&nbsp;Moore, <i>Phys. Rev. B</i> <b>86</b>, [155156](http://dx.doi.org/10.1103/PhysRevB.86.155156)

<a name="zhang"></a>\[5\] [Quasiparticle statistics and braiding from ground-state entanglement](http://dx.doi.org/10.1103/PhysRevB.85.235151), Yi&nbsp;Zhang, Tarun&nbsp;Grover, Ari&nbsp;Turner, Masaki&nbsp;Oshkawa, and Ashvin&nbsp;Vishwanath, <i>Phys. Rev. B</i> <b>85</b>, [235151](http://dx.doi.org/10.1103/PhysRevB.85.235151)

<a name="cincio"></a>\[6\] [Characterizing Topological Order by Studying the Ground States on an Infinite Cylinder](http://link.aps.org/doi/10.1103/PhysRevLett.110.067208), L.&nbsp;Cincio and G.&nbsp;Vidal, <i>Phys. Rev. Lett.</i> <b>110</b>, [067208](http://link.aps.org/doi/10.1103/PhysRevLett.110.067208)

<a name="phien"></a>\[7\] [Infinite boundary conditions for matrix product state calculations](http://link.aps.org/doi/10.1103/PhysRevB.86.245107), Ho&nbsp:N.&nbsp;Phien, G.&nbsp;Vidal, and Ian&nbsp;P.&nbsp;McCulloch <i>Phys. Rev. B</i> <b>86</b>, [245107](http://link.aps.org/doi/10.1103/PhysRevB.86.245107)

