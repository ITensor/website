# tJ and tJSite

The tJ class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites of be of type tJSite, representing a particle with spin 1/2
single local orbital, but constrained never to doubly-occupy this orbital as in the
t-J model.

The tJSite class can also be used to create custom SiteSets which mix tJSites
with other types of sites.

tJ and tJSite are defined in the file "itensor/mps/sites/tj.h"

## Synopsis

    auto sites = tJ(100);

    auto Ntot_3 = sites.op("Ntot",3);

    auto Cup_4 = sites.op("Cup",4);

## States of a tJSite

* `"Emp"` &mdash; the vacuum (empty) state (alternate name `"0"`)

* `"Up"` &mdash; site occupied by one spin up particle (alternate name `"+"`)

* `"Dn"` &mdash; site occupied by one spin down particle (alternate name `"-"`)

## Operators Provided by tJSite

* `"Nup"` &mdash; density of up-spin particles @@\hat{n}\_\uparrow@@

* `"Ndn"` &mdash; density of down-spin particles @@\hat{n}\_\downarrow@@

* `"Ntot"` &mdash; the total density operator @@\hat{n}\_\text{tot} = \hat{n}\_\uparrow + \hat{n}\_\downarrow@@

* `"Aup"` &mdash; the up-spin annihilation operator @@\hat{a}\_\uparrow@@

* `"Adagup"` &mdash; the up-spin creation operator @@\hat{a}^\dagger\_\uparrow@@

* `"Adn"` &mdash; the down-spin annihilation operator @@\hat{a}\_\downarrow@@

* `"Adagdn"` &mdash; the down-spin creation operator @@\hat{a}^\dagger\_\downarrow@@

* `"F"` &mdash; the Jordan-Wigner fermion 'string' operator @@\hat{F}=(-1)^{\hat{n}\_\text{tot}}@@

* `"S+"` &mdash; the spin raising operator

* `"S-"` &mdash; the spin lowering operator

For the following fermionic operators, it is crucial to note that when obtaining them as individual
tensors from a site set, they do not anti-commute with each other on different sites, only on 
the same site (for more details on how these operators act on a single site read more at
[[this tutorial|tutorials/fermions]]). In contrast, when used as operator names in the
construction of an AutoMPO, they do anti-commute but only in that context.

* `"Cup"` &mdash; the up-spin annihilation operator @@\hat{c}\_\uparrow@@. 

* `"Cdagup"` &mdash; the up-spin creation operator @@\hat{c}^\dagger\_\uparrow@@.

* `"Cdn"` &mdash; the down-spin annihilation operator @@\hat{c}\_\downarrow@@. 

* `"Cdagdn"` &mdash; the down-spin creation operator @@\hat{c}^\dagger\_\downarrow@@.

