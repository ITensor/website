# CustomSpin

The CustomSpin class is a specialization of [[SiteSet|classes/siteset]] which initializes
its sites to be of type CustomSpinSite, representing a spin with total spin quantum
number S (= 1/2, 1, 3/2, 2, ...) where the user can specify S.

CustomSpin and CustomSpinSite are defined in the file "itensor/mps/sites/customspin.h"

## Synopsis

    auto sh_sites = CustomSpin(100,{"S=",0.5}); //100 S=1/2 sites
    auto S+_3 = op(sh_sites,"S+",3);          //obtain "S+" operator

    auto s3h_sites = CustomSpin(100,{"2S=",3}); //100 S=3/2 sites
    auto Sz_7 = op(s3h_sites,"Sz",7);          //obtain "Sz" operator

## Named Arguments Recognized

The `CustomSpin` class accepts the following named arguments. Only one
of these needs to be provided:

* "S" &mdash; the total spin quantum number of the sites. For example
  passing the named argument `{"S=",0.5}` creates S=1/2 spins; passing
  the named argument `{"S=",1.0}` creates S=1 spins.

* "2S" &mdash; two times the total spin quantum number of the sites,
  which is always an integers. For example, passing `{"2S=",1}` 
  creates S=1/2 spins; passing `{"2S=",2}` creates S=1 spins.


## Operators Provided by CustomSpinSite

* `"Sz"` &mdash; the z spin operator

* `"S+"` &mdash; the spin raising operator

* `"S-"` &mdash; the spin lowering operator

* `"Sz2"` &mdash; square of the z spin operator
