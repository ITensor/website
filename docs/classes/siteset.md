# SiteSet #

<span style="color:red;font-style:italic;">Note: this documentation page refers to code prior to version 2.0</span>

Class for specifying the local Hilbert space of each site of a lattice.<sup>&#8224;</sup>
A SiteSet does not store any information about the topology of the lattice, just the number of sites
and the type of each site.

The class `SiteSet` is an abstract base class, and its features are to be used through a class derived from it
such as `SpinHalf` or `Hubbard`. However, functions to take a `const SiteSet&` argument
when their functionality does not depend on the specific type of SiteSet being passed to it.

## Accessing Site Information

* `int N()`

  Returns the number of sites.

* `IQIndex operator()(int i)`

  Return the `IQIndex` representing the degree of freedom at site i. This is also useful even when not using quantum numbers
  because an `IQIndex` can automatically convert to an `Index`.

  <div class="example_clicker">Show Example</div>

        SpinHalf sites(100);

        Index s4 = sites(4);

        Index l("left",5),
              r("right",4);

        ITensor T(l,sites(3),r);

* `IQIndexVal operator()(int i, const String& state)`

  Return the `IQIndexVal` representing a specific state of site i in the diagonal basis. For example, the state string could be
  `"Up"` or `"Dn"` for the case of a SiteSet representing a lattice of S=1/2 spins.

  <div class="example_clicker">Show Example</div>

        SpinOne sites(100);

        //Create an IQTensor with all entries zero except
        //the one corresponding to site 5 in the "Up" state
        IQTensor up5(sites(5,"Up"));

## Obtaining Operators

* `IQTensor op(const String& opname, int i, const OptSet& opts = Global::opts())`

  Return a single-site operator acting on site i. For a list of operators available for a certain type of SiteSet, see the documentation
  on that particular type. For example, opname could be `"Sz"` for a SiteSet representing a lattice of spins. 

  <div class="example_clicker">Show Example</div>

        Hubbard sites(40);

        IQTensor ndn5 = sites.op("Ndn",5);

        Real dens = (dag(prime(psi.A(8),Site)) * sites.op("Ntot",8) * psi.A(8)).toReal();

  A convenient feature of the `op` method is obtaining a product of two 
  operators by joining their names with an asterisk `*`.
  For example, if opname is `"Nup*Ndn"`, the operator return is the product (in the usual sense of a product of single-site operators
  written from left to right) of the operators `"Nup"` and `"Ndn"`.

  <div class="example_clicker">Show Example</div>

        Hubbard sites(40);

        Real itcn = (dag(prime(psi.A(8),Site)) * sites.op("Nup*Ndn",8) * psi.A(8)).toReal();


&#8224; Until version 1.0 this class was called `Model`.

