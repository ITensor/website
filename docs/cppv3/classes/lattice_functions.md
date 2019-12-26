# Functions for Making Lattices

ITensor provides functions which return a vector of [[LatticeBond|classes/latticebond]]
objects for conveniently working with various lattices such as the square lattice
or triangular lattice.

## Synopsis

    int Nx = 10;
    int Ny = 10;

    auto square_latt = squareLattice(Nx,Ny,{"YPeriodic=",true});
    for(auto& bnd : square_latt)
        {
        printfln("Bond from site %d -> %d",bnd.s1,bnd.s2);
        }

    //Make a Hamiltonian on the triangular lattice using AutoMPO
    auto sites = SpinHalf(Nx*Ny);
    auto ampo = AutoMPO(sites);
    auto tri_latt = triangularLattice(Nx,Ny);
    for(auto& bnd : tri_latt)
        {
        ampo += "Sz",bnd.s1,"Sz",bnd.s2;
        ampo += 0.5,"S+",bnd.s1,"S-",bnd.s2;
        ampo += 0.5,"S-",bnd.s1,"S+",bnd.s2;
        }
    auto H = toMPO(ampo);

## Lattice Functions

* ```
  squareLattice(int Nx, int Ny, Args args = Args::global()) -> Lattice
  ```
  
  Return a Lattice (vector<LatticeBond>) of nearest-neighbor bonds of
  the two-dimensional square lattice of dimensions Nx by Ny.

  This function recognizes the following optional named arguments:
  
  * "YPeriodic" &mdash; (default=false). If true, includes next-neighbor periodic bonds wrapping around the y-direction.


* ```
  squareNextNeighbor(int Nx, int Ny, Args args = Args::global()) -> Lattice
  ```
  
  Return a Lattice (vector<LatticeBond>) of both nearest-neighbor and
  next-nearest-neighbor (second-nearest-neighbor) bonds of
  the two-dimensional square lattice of dimension Nx by Ny.

  This function recognizes the following optional named arguments:
  
  * "YPeriodic" &mdash; (default=false). If true, includes next-neighbor periodic bonds wrapping around the y-direction.
