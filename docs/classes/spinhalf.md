# SpinHalf and SpinHalfSite

The SpinHalf class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites to be of type SpinHalfSite, representing a S=1/2 spin.

The SpinHalfSite class can also be used to create custom SiteSets which mix SpinHalfSites 
with other types of sites.

SpinHalf and SpinHalfSite are defined in the file "itensor/mps/sites/spinhalf.h"

## Synopsis

    auto sites = SpinHalf(100);

    auto Sz3 = sites.op("Sz",3);

    auto Sp4 = sites.op("S+",4);

    //Use IQIndexVals to get the +,+ element of the Sz operator
    auto Szpp = Sz3.real(sites(3,"Up"),prime(sites(3,"Up")));


## States of a SpinHalfSite

* `"Up"` &mdash; the @@m\_z=+1/2@@ spin state

* `"Dn"` &mdash; the @@m\_z=-1/2@@ spin state

## Operators Provided by SpinHalfSite

* `"Sz"` &mdash; the @@S^z = \frac{1}{2}\sigma^z@@ spin operator 

* `"S+"` &mdash; the @@S^+ = \sigma^+@@ operator (alternate name is `"Sp"`)

* `"S-"` &mdash; the @@S^- = \sigma^-@@ operator (alternate name is `"Sm"`)

* `"Sx"` &mdash; the @@S^x = \frac{1}{2}\sigma^x@@ operator (must be converted to an ITensor prior to usage)

* `"Sy"` &mdash; the @@S^y = \frac{1}{2}\sigma^y@@ operator (must be converted to an ITensor prior to usage)

* `"ISy"` &mdash; defined as @@i\,S^y = \frac{i}{2}\sigma^y@@ (must be converted to an ITensor prior to usage)



