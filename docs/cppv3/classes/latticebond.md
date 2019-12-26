# LatticeBond Objects

A LatticeBond is a simple struct which represents an
interaction bond in a lattice model. It does not have to
be a nearest-neighbor bond only, and can represent interactions
of various distances and types.

Functions such as `squareLattice` and `triangularLattice`
return a std::vector of LatticeBond objects which can be 
iterated over in a range-based for loop. For more information
about these functions see [[Functions for Making Lattices|classes/lattice_functions]].

## Synopsis

    int Nx = 10;
    int Ny = 10;
    auto lattice = squareLattice(Nx,Ny);
    // lattice is a std::vector<LatticeBond>

    for(auto& bnd : lattice) // bnd is of type LatticeBond
        {
        printfln("Bond from site %d -> %d",bnd.s1,bnd.s2);
        printfln("  Connecting points (%s,%s) -> (%s,%s)",bnd.x1,bnd.y1,bnd.x2,bnd.y2);
        printfln("  This bond is of type %s",bnd.type)
        }

## LatticeBond Data Members

- `s1` (int) &mdash; site number of the first site
- `s2` (int) &mdash; site number of the second site
- `x1` (Real) &mdash; x coordinate of the first site
- `y1` (Real) &mdash; y coordinate of the first site
- `x2` (Real) &mdash; x coordinate of the second site
- `y2` (Real) &mdash; y coordinate of the second site

