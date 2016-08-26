# SiteSet 

Class for specifying the local Hilbert space of each site of a lattice by storing
the associated site index.
A SiteSet does not store any information about the topology of the lattice, 
just the number of sites and information about each site.

ITensor comes with specialized subclasses of SiteSet, such as the [[SpinHalf|classes/spinhalf]]
and [[SpinOne|classes/spinone]] classes, which provide facilities to create sites of a certain
type (S=1/2 or S=1 spins, for example). However, these classes differ from SiteSet mainly in 
their constructors and read/write methods; after creating a specialized SiteSet type (such as [[SpinHalf|classes/spinhalf]])
it can be safely converted to the base SiteSet type (for example, in the following code: `SiteSet sites = SpinHalf(N);`) 
without losing information about the underlying site type.

## Synopsis

    SiteSet sites = SpinHalf(100);

    Print(sites.N()); //prints: sites.N() = 100

    sites(3); //retrieve the IQIndex defining site number 3

    sites(3,"Up"); //obtain the IQIndexVal defining the "Up" state at site number 3

    sites.op("Sz",3); //obtain the "Sz" operator at site number 3

## SiteSet Interface

* `N() -> int`

  Returns the number of sites of this SiteSet.

* `operator()(int i) -> IQIndex`

  Return the `IQIndex` representing site i. 

  This is also useful even when not using quantum numbers
  because an `IQIndex` can automatically convert to an `Index`.

  <div class="example_clicker">Show Example</div>

        auto sites = SpinHalf(100);

        Index s4 = sites(4);

        Index l("left",5),
              r("right",4);

        ITensor T(l,sites(3),r);

* `operator()(int i, string state) -> IQIndexVal`

  Return the `IQIndexVal` representing a specific state of site i in the diagonal basis. 
  
  For example, the state string could be
  `"Up"` or `"Dn"` for the case of the [[SpinHalf|classes/spinhalf]] SiteSet,
  or `"Emp"`,`"Up"`,`"Dn"`, or `"UpDn"` in the case of the [[Hubbard|classes/hubbard]] SiteSet.

  <div class="example_clicker">Show Example</div>

        auto sites = SpinOne(100);

        //Create an IQTensor with all entries zero except
        //the one corresponding to site 5 in the "Up" state
        auto up5 = setElt(sites(5,"Up"));

* ```
  op(string opname, 
     int i, 
     Args args = Args::global()) -> IQTensor
  ```

  Return a single-site operator acting on site i. 
  
  For a list of operators available for a certain type of site, see the documentation
  on that particular type. For example, opname could be `"Sz"` for a S=1/2 site.

  Some of the site types accept optional named arguments (Args).

  Although the return type is IQTensor, the `op` method can be used with ITensors as well.
  Just convert the returned IQTensor to an ITensor (this will happen automatically if
  the returned tensor is contracted with or added to an ITensor).

  <div class="example_clicker">Show Example</div>

        auto sites = Hubbard(40);

        IQTensor ndn5 = sites.op("Ndn",5);

        Real dens = (dag(prime(psi.A(8),Site)) * sites.op("Ntot",8) * psi.A(8)).toReal();

  A convenient feature of the `op` method is obtaining a product of two 
  operators by joining their names with an asterisk `*`.
  For example, if opname is `"Nup*Ndn"`, the operator return is the 
  product (in the usual sense of a product of single-site operators
  written from left to right) of the operators `"Nup"` and `"Ndn"`.

  <div class="example_clicker">Show Example</div>

        auto sites = Hubbard(40);

        Real itcn = (dag(prime(psi.A(8),Site)) * sites.op("Nup*Ndn",8) * psi.A(8)).toReal();

## Operators Defined Automatically for all site types

Regardless of the specialized operators defined by each custom site type (such as the [[SpinHalfSite|classes/spinhalf]]
site type), the SiteSet class automatically provides the following operators which can be retrived 
as described from the `.op` method.

* `"Id"` &mdash; identity operator

   Example:

       auto sites = SpinHalf(N);
       auto id3 = sites.op("Id",3);

* `"Proj"` &mdash; diagonal projection operator
  Requires additional named argument "State" specifying
  which state to project onto.

  Example:

       auto sites = SpinHalf(N);
       //Projects site 3 onto state 2 (i.e. the down state)
       auto P3_2 = sites.op("Proj",3,{"State",2});

