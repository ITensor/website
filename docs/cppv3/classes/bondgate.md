# BondGate

BondGate objects represent a quantum "gate" acting on a nearest-neighbor
bond of a 1D system. Currently, the associated `gateTEvol` function of
ITensor assumes that sites of a BondGate are neighbors along a 1D ordering
of the sites of a system, so please only make BondGates which have this property.

For an example of using BondGate in conjunction with the `gateTEvol` function,
please see [[this code formula page|formulas/tevol_trotter]].

## Examples

    int N = 100;
    auto sites = SpinHalf(N);

    // Make an ITensor "hterm" which is the term
    // of the Heisenberg model acting on spins 
    // 2 and 3:
    auto hterm = op(sites,"Sz",2)*op(sites,"Sz",3);
    hterm += 0.5*op(sites,"S+",2)*op(sites,"S-",3);
    hterm += 0.5*op(sites,"S-",2)*op(sites,"S+",3);
 
    // Make a BondGate which acts as the operator
    // exp(-i * hterm * tstep/2)
    auto real_h23 = BondGate(sites,2,3,BondGate::tReal,tstep/2.,hterm);

    // Make a BondGate which acts as the operator
    // exp(-hterm * tstep/2)
    auto imag_h23 = BondGate(sites,2,3,BondGate::tImag,tstep/2.,hterm);

    // Make a BondGate which swaps sites 7 and 8
    auto swap78 = BondGate(sites,7,8);

## Constructors

* `BondGate(SiteSet const& sites,int i1,int i2, BondGate::Type type, Real tau, ITensor bondH)`

  Construct a BondGate which acts as the real or imaginary time-evolution operator
  for the Hamiltonian term `bondH` over the time interval `tau`. 
  The integers `i1` and `i2` must correspond
  to the indices of the provided SiteSet `sites` which match the indices of the 
  provided ITensor `bondH`. 

  The argument `type` one of the following:
  - `BondGate::tReal`
  - `BondGate::tImag`

  If the type is `BondGate::tReal`, the BondGate acts as the operator `exp(-i * tau * bondH)`.
  If the type is `BondGate::tImag`, the BondGate acts as the operator `exp(-tau * bondH)`.

* `BondGate(SiteSet const& sites,int i1,int i2)`

  Construct a BondGate which swaps sites `i1` and `i2` when acting on a tensor with indices
  `sites(i1)` and `sites(i2)`. The resulting BondGate can be passed as part of a container
  of gates to the gateTEvol function for implementing MPS time evolution algorithms using
  swap gates as a method to time evolve under Hamiltonians which are not nearest-neighbor
  in 1D.

## Accessor Methods

* `.gate() -> ITensor`

  Obtain the gate stored within this BondGate, as an ITensor.

* `.i1() -> int`

  Obtain the number of the first site on which this BondGate acts.

* `.i2() -> int`

  Obtain the number of the second site on which this BondGate acts.

* `.type() -> BondGate::Type`

  Obtain the type of this BondGate.

## Operators

* `operator*(BondGate const& G, ITensor T) -> ITensor` <br/>
  `operator*(ITensor T, BondGate const& G) -> ITensor`

  Contract a BondGate with an ITensor. The result is the same as doing
  `G.gate() * T`, that is, retrieving the gate stored within the BondGate
  and contracting it with the ITensor `T`.
