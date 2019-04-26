# Boson and BosonSite

The Boson class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites to be of type BosonSite, representing a spinless particle with maximum 
site occupancy that can be set by the user. 

The default maximum occupancy is 1, which implements the idea of a "hard core boson".
If the "MaxOcc" argument is passed to Boson or BosonSite, then the maximum number of
bosons will be equal to that value.

The BosonSite class can also be used to create custom SiteSets which mix BosonSites 
with other types of sites.

A Boson site set (and BosonSite) accepts the optional named argument "ConserveQNs"
which is true by default and will make the BosonSite and BosonSites within the Boson
site set carry particle number QN information.

Boson and BosonSite are defined in the file "itensor/mps/sites/fermion.h"

## Synopsis

    auto sites = Boson(100);

    auto N_3 = op(sites,"N",3);

    auto A_4 = op(sites,"A",4);

    //Make a Boson site set where each site has a maximum occupancy of 3
    //(up to three bosons on each site):
    auto sites3 = Boson(100,{"MaxOcc=",3});

    //Make a Boson site set which does not conserve particle number
    auto ncsites = Boson(100,{"ConserveQNs",false});

## States of a BosonSite

* `"0"` &mdash; the vacuum (empty) state

* `"1"` &mdash; the occupied state (one particle)

* `"2"` &mdash; state with two bosons (only allowed if "MaxOcc" >= 2)

* `"3"` &mdash; state with three bosons (only allowed if "MaxOcc" >= 3)

and similar up to the value "MaxOcc" (which defaults to 1 if not specified).

## Operators Provided by BosonSite

* `"N"` &mdash; the density operator @@\hat{n}@@

* `"A"` &mdash; the annihilation operator @@\hat{a}@@

* `"Adag"` &mdash; the creation operator @@\hat{a}^\dagger@@

