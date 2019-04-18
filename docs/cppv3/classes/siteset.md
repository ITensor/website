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

    auto sites = SpinHalf(100);

    Print(length(sites)); //prints: length(sites) = 100

    auto s3 = sites(3); //retrieve the Index defining site number 3

    auto s3up = sites(3,"Up"); //obtain the IndexVal defining the "Up" state at site number 3

    auto sz3 = op(sites,"Sz",3); //obtain the "Sz" operator at site number 3


## General SiteSet Interface

This part of the interface is common to all site set objects.

* `length(SiteSet sites) -> int`

  Returns the number of sites of the SiteSet `sites`.

* `operator()(int i) -> Index`

  Return the `Index` representing site i. 

  <div class="example_clicker">Show Example</div>

      auto sites = SpinHalf(100);

      auto s4 = sites(4);

      auto l = Index(5,"left"),
      auto r = Index(4,"right");

      auto T = ITensor(l,sites(3),r);

* `operator()(int i, string state) -> IndexVal`

  Return the `IndexVal` representing a specific state of site i in the diagonal basis. 
  
  For example, the state string could be
  `"Up"` or `"Dn"` for the case of the [[SpinHalf|classes/spinhalf]] SiteSet,
  or `"Emp"`,`"Up"`,`"Dn"`, or `"UpDn"` in the case of the [[Electron|classes/electron]] SiteSet.

  <div class="example_clicker">Show Example</div>

        auto sites = SpinOne(100);

        //Create an ITensor with all entries zero except
        //the one corresponding to site 5 in the "Up" state
        auto up5 = setElt(sites(5,"Up"));

* ```
  op(SiteSet sites,
     string opname, 
     int i, 
     Args args = Args::global()) -> ITensor
  ```

  Return a single-site operator acting on site i using the corresponding index and site type
  of the SiteSet `sites`.
  
  For a list of operators available for a certain type of site, see the documentation
  on that particular type. For example, opname could be `"Sz"` for a S=1/2 site.

  Some of the site types accept optional named arguments (Args).

  <div class="example_clicker">Show Example</div>

      auto sites = Electron(40);

      // Create a random MPS of all up spins
      auto initstate = InitState(sites,"Up");
      auto psi = randomMPS(initstate);

      auto ndn5 = op(sites,"Ndn",5);

      auto dens = elt(dag(prime(psi(8),"Site")) * op(sites,"Ntot",8) * psi(8));

  A convenient feature of the `op` method is obtaining a product of two 
  operators by joining their names with an asterisk `\*`.
  For example, if opname is `"Nup\*Ndn"`, the operator return is the 
  product (in the usual sense of a product of single-site operators
  written from left to right) of the operators `"Nup"` and `"Ndn"`.

  <div class="example_clicker">Show Example</div>

      // Continued from the example above
      auto itcn = elt(dag(prime(psi(8),"Site")) * op(sites,"Nup*Ndn",8) * psi(8));

* `inds(SiteSet sites) -> IndexSet`

  Return an IndexSet of the indices of the SiteSet (the SiteSet without the site
  type information).

  <div class="example_clicker">Show Example</div>

      auto sites = SpinHalf(4);

      auto is = inds(sites);

      Print(is(3) == sites(3)); //prints: true

      // Make an ITensor with the indices
      auto T = ITensor(is);

## Operators Defined Automatically for all site types

Regardless of the specialized operators defined by each custom site type (such as the [[SpinHalfSite|classes/spinhalf]]
site type), the SiteSet class automatically provides the following operators which can be retrived 
as described from the `.op` method.

* `"Id"` &mdash; identity operator

   Example:

       auto sites = SpinHalf(N);
       auto id3 = op(sites,"Id",3);

* `"Proj"` &mdash; diagonal projection operator
  Requires additional named argument "State" specifying
  which state to project onto.

  Example:

      auto sites = SpinHalf(N);
      //Projects site 3 onto state 2 (i.e. the down state)
      auto P3_2 = op(sites,"Proj",3,{"State",2});

## Generic SiteSet class

You can also use the SiteSet class itself as a generic collection of site
indices which defines only the minimal set of operators discussed above
above (for example "Id" and "Proj"). 
A generic SiteSet can still be very useful for keeping track
of Hilbert spaces not necessarily equipped with specific local site
operators.

* `SiteSet(int N, int d)`

  Construct a generic SiteSet object with N sites and local dimension size d.

  The site indices created with this constructor have no QN information.

* `SiteSet(IndexSet is)`

  Construct a SiteSet with the indices provided in the IndexSet
  (or any container of indices convertible to an IndexSet).

  <div class="example_clicker">Show Example</div>

      auto sites = SpinHalf(10);

      // Make an IndexSet of the indices 
      // of the SpinHalf siteset
      auto is = inds(sites);

      // Make a new SpinHalf site set from the indices
      // grabbed from the original one
      auto sites2 = SpinHalf(is);

      Print(norm(op(sites,"Sz",1)-op(sites2,"Sz",1))); //prints: 0.0

