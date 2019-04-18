# SpinOne and SpinOneSite

The SpinOne class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites to be of type SpinOneSite, representing a S=1 spin.

The SpinOneSite class can also be used to create custom SiteSets which mix SpinOneSites 
with other types of sites.

The SpinOne site set accepts the optional named arguments "SHalfEdge" which makes the 
first and last sites S=1/2 spins, or "SHalfLeftEdge" which only makes the first site
a S=1/2 spin. (This is useful, for example, to study the edge physics of the Haldane
phase of a one-dimensional S=1 Heisenberg chain.)

SpinOne and SpinOneSite are defined in the file "itensor/mps/sites/spinone.h"

## Synopsis

    auto sites = SpinOne(100);

    auto Sz_3 = op(sites,"Sz",3);

    auto Sx2_4 = op(sites,"Sx2",4);

    auto Sp_5 = op(sites,"S+",5);

    //Use IndexVals to get the 0,+ element of the S+ operator
    auto Spzp = elt(Sp_5,sites(5,"Z0"),prime(sites(5,"Up")));

## States of a SpinOneSite

* `"Up"` &mdash; the @@m\_z=+1@@ spin state

* `"Z0"` &mdash; the @@m\_z=0@@ spin state

* `"Dn"` &mdash; the @@m\_z=-1@@ spin state

## Operators Provided by SpinOneSite

* `"Sz"` &mdash; the @@S^z@@ spin operator 

* `"S+"` &mdash; the @@S^+@@ operator (alternate name is `"Sp"`)

* `"S-"` &mdash; the @@S^-@@ operator (alternate name is `"Sm"`)

* `"Sx"` &mdash; the @@S^x@@ operator (must be converted to an ITensor prior to usage)

* `"Sy"` &mdash; the @@S^y@@ operator (must be converted to an ITensor prior to usage)

* `"ISy"` &mdash; defined as @@i\,S^y@@ (must be converted to an ITensor prior to usage)

* `"Sz2"` &mdash; the @@(S^z)^2@@ operator

* `"Sx2"` &mdash; the @@(S^x)^2@@ operator

* `"Sy2"` &mdash; the @@(S^y)^2@@ operator

* `"S2"` &mdash; the @@(\vec{S})^2@@ operator


