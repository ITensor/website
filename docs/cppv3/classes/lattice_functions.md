# Functions for Making Lattices

ITensor provides functions which return a vector of [[LatticeBond|classes/latticebond]]
objects for conveniently working with various lattices such as the square lattice
or triangular lattice.

The source code for these functions can be found in the folder `itensor/mps/lattice`
and are meant to be written in a straightforward style that can be used to develop
similar functions for other lattices. If you would like to contribute a lattice
function (such as kagome, or next-neighbor triangular) which is currently missing,
we would be happy to receive a pull request from you.

## Synopsis

    int Nx = 10;
    int Ny = 10;

    auto square_latt = squareLattice(Nx,Ny,{"YPeriodic=",true});
    for(auto& bnd : square_latt)
        {
        printfln("Bond from site %d -> %d",bnd.s1,bnd.s2);
        }

    auto square_latt_nn = squareNextNeighbor(Nx,Ny,{"YPeriodic=",true});
    for(auto& bnd : square_latt_nn)
        {
        if(bnd.type == "1")
            {
            printfln("First-neighbor bond from site %d -> %d",bnd.s1,bnd.s2);
            }
        else if(bnd.type == "2")
            {
            printfln("Second-neighbor bond from site %d -> %d",bnd.s1,bnd.s2);
            }
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

  First-neighbor bonds in the returned lattice have the type `"1"` 
  while second-neighbor bonds have the type `"2"`.

  This function recognizes the following optional named arguments:
  
  * "YPeriodic" &mdash; (default=false). If true, includes next-neighbor periodic bonds wrapping around the y-direction.

* ```
  triangularLattice(int Nx, int Ny, Args args = Args::global()) -> Lattice
  ```
  
  Return a Lattice (vector<LatticeBond>) of nearest-neighbor
  bonds of the two-dimensional triangular lattice of dimension Nx by Ny.

  This function recognizes the following optional named arguments:
  
  * "YPeriodic" &mdash; (default=false). If true, includes next-neighbor periodic bonds wrapping around the y-direction.
