# Spinless and SpinlessSite

The Spinless class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites to be of type SpinlessSite, representing a spinless particle with maximum 
site occupancy of one (a fermion or "hard-core" boson).

The SpinlessSite class can also be used to create custom SiteSets which mix SpinlessSites 
with other types of sites.

A Spinless site set (and SpinlessSite) accepts the optional named argument "ConserveNf"
which is true by default and will make the quantum numbers carried by a SpinlessSite include
the particle number. If set to false, the quantum numbers will only reflect the particle 
number modulo 2 (the "parity").

Spinless and SpinlessSite are defined in the file "itensor/mps/sites/spinless.h"

## Synopsis

    auto sites = Spinless(100);

    auto N_3 = sites.op("N",3);

    auto A_4 = sites.op("A",4);

    //Make a Spinless site set which only conserves parity
    auto psites = Spinless(100,{"ConserveNf",false});

## States of a SpinlessSite

* `"Emp"` &mdash; the vacuum (empty) state

* `"Occ"` &mdash; the occupied state (one particle)

## Operators Provided by SpinlessSite

* `"N"` &mdash; the density operator @@\hat{n}@@

* `"A"` &mdash; the annihilation operator @@\hat{a}@@

* `"Adag"` &mdash; the creation operator @@\hat{a}^\dagger@@

* `"F"` &mdash; the Jordan-Wigner fermion 'string' operator @@\hat{F}=(1-2\hat{n})=(-1)^{\hat{n}}@@

For the following fermionic operators, it is crucial to note that when obtaining them as individual
tensors from a site set, they do not anti-commute with each other on different sites, only on 
the same site (for more details on how these operators act on a single site read more at
[[this tutorial|tutorials/fermions]]). In contrast, when used as operator names in the
construction of an AutoMPO, they do anti-commute but only in that context.

* `"C"` &mdash; the annihilation operator @@\hat{c}@@.

* `"Cdag"` &mdash; the creation operator @@\hat{c}^\dagger@@.

