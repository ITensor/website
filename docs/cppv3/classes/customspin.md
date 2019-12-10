# CustomSpin

The CustomSpin class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites to be of type CustomSpinSite, representing a spin with a value S/2 
where the user can specify S (or 2S if one prefers).

CustomSpin and CustomSpinSite are defined in the file "itensor/mps/sites/customspin.h"

## Synopsis

    auto s3h_sites = CustomSpin(100,{"S=",3}); //100 S=3/2 sites
    auto Sz_7 = op(s3h_sites,"Sz",7);          //obtain "Sz" operator

    auto sh_sites = CustomSpin(100,{"S=",0.5}); //100 S=1/2 sites
    auto S+_3 = op(sh_sites,"S+",3);          //obtain "S+" operator

## Operators Provided by CustomSpinSite

* `"Sz"` &mdash; the z spin operator

* `"S+"` &mdash; the spin raising operator

* `"S-"` &mdash; the spin lowering operator

* `"Sz2"` &mdash; square of the z spin operator
