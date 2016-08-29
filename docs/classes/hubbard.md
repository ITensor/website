# Hubbard and HubbardSite

The Hubbard class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites of be of type HubbardSite, representing a particle with spin 1/2 (either
a fermion or a spinful boson) occupying a 
single local orbital (meaning that the maximum occupancy of the site is two particles:
one with spin up and one with spin down).

The HubbardSite class can also be used to create custom SiteSets which mix HubbardSites
with other types of sites.

A Hubbard site set (and HubbardSite) accepts the following optional named arguments: 
- "ConserveNf" &mdash; (default is true) make the quantum numbers carried by a HubbardSite include
  the particle number. If set to false, the quantum numbers will only reflect the particle 
  number modulo 2 (the "parity").
- "ConserveSz" &mdash; (default is true) make the quantum numbers carried by a HubbardSite include
  the spin. If set to false, the quantum numbers will only charge or parity, depending on 
  the value of "ConserveNf"

Hubbard and HubbardSite are defined in the file "itensor/mps/sites/spinless.h"

## Synopsis

    auto sites = Hubbard(100);

    auto Ntot_3 = sites.op("Ntot",3);

    auto C_4 = sites.op("C",4);

    //Make a Hubbard site set which only conserves parity
    auto psites = Hubbard(100,{"ConserveNf",false});

## States of a HubbardSite

* `"Emp"` &mdash; the vacuum (empty) state (alternate name `"0"`)

* `"Up"` &mdash; site occupied by one spin up particle (alternate name `"+"`)

* `"Dn"` &mdash; site occupied by one spin down particle (alternate name `"-"`)

* `"UpDn"` &mdash; site occupied by two particles, one of each spin (alternate name `"S"` for singlet)

## Operators Provided by HubbardSite

* `"Nup"` &mdash; density of up-spin particles @@\hat{n}\_\uparrow@@

* `"Ndn"` &mdash; density of down-spin particles @@\hat{n}\_\downarrow@@

* `"Nupdn"` &mdash; density of doubly-occupied sites @@\hat{n}\_\uparrow \hat{n}\_\downarrow@@

* `"Ntot"` &mdash; the total density operator @@\hat{n}\_\text{tot} = \sum\_\sigma \hat{n}\_\sigma@@

* `"Aup"` &mdash; the up-spin annihilation operator @@\hat{a}\_\uparrow@@

* `"Adagup"` &mdash; the up-spin creation operator @@\hat{a}^\dagger\_\uparrow@@

* `"Adn"` &mdash; the down-spin annihilation operator @@\hat{a}\_\downarrow@@

* `"Adagdn"` &mdash; the down-spin creation operator @@\hat{a}^\dagger\_\downarrow@@

* `"F"` &mdash; the Jordan-Wigner fermion 'string' operator @@\hat{F}=(-1)^{\hat{n}\_\text{tot}}@@

* `"Sz"` &mdash; the z-component spin operator (+0.5 for an up spin, -0.5 for a down spin)

For the following fermionic operators, it is crucial to note that when obtaining them as individual
tensors from a site set, they do not anti-commute with each other on different sites, only on 
the same site (for more details on how these operators act on a single site read more at
[[this tutorial|tutorials/fermions]]). In contrast, when used as operator names in the
construction of an AutoMPO, they do anti-commute but only in that context.

* `"Cup"` &mdash; the up-spin annihilation operator @@\hat{c}\_\uparrow@@. 

* `"Cdagup"` &mdash; the up-spin creation operator @@\hat{c}^\dagger\_\uparrow@@.

* `"Cdn"` &mdash; the down-spin annihilation operator @@\hat{c}\_\downarrow@@. 

* `"Cdagdn"` &mdash; the down-spin creation operator @@\hat{c}^\dagger\_\downarrow@@.

