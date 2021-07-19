# Write and Read an MPS or MPO to Disk with HDF5

## Writing an MPS to an HDF5 File

Let's say you have an MPS `psi` which you have made or obtained
from a calculation. To write it to an HDF5 file named "myfile.h5"
you can use the following pattern:

    using HDF5
    f = h5open("myfile.h5","w")
    write(f,"psi",psi)
    close(f)

Above, the string "psi" can actually be any string you want such as "MPS psi"
or "Result MPS" and doesn't have to have the same name as the reference `psi`.
Closing the file `f` is optional and you can also write other objects to the same
file before closing it.

## Reading an MPS from an HDF5 File

Say you have an HDF5 file "myfile.h5" which contains an MPS stored as a dataset with the
name "psi". (Which would be the situation if you wrote it as in the example above.)
To read this ITensor back from the HDF5 file, use the following pattern:

    using HDF5
    f = h5open("myfile.h5","r")
    psi = read(f,"psi",MPS)
    close(f)

Many functions which involve MPS, such as the `dmrg` function or the `AutoMPO` system
require that you use an array of site indices which match the MPS. So when reading in
an MPS from disk, do not construct a new array of site indices. Instead, you can
obtain them like this: `sites = siteinds(psi)`.

So for example, to create an MPO from an AutoMPO which has the same site indices
as your MPS `psi`, do the following:

    ampo = AutoMPO()
    # Then put operators into ampo...

    sites = siteinds(psi) # Get site indices from your MPS
    H = MPO(ampo,sites)

    # Compute <psi|H|psi>
    energy_psi = inner(psi,H,psi)


Note the `MPS` argument to the read function, which tells Julia which read function
to call and how to interpret the data stored in the HDF5 dataset named "psi". In the 
future we might lift the requirement of providing the type and have it be detected
automatically from the data stored in the file.


## Writing and Reading MPOs

To write or read MPOs to or from HDF5 files, just follow the examples above but use
the type `MPO` when reading an MPO from the file instead of the type `MPS`.





