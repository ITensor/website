# Writing and reading ITensor objects to and from HDF5 files

Most ITensor objects (ITensor, MPS, MPO, etc.) can be written to HDF5 files and 
read back from these files. HDF5 is a portable file format that uses a structure
similar to a filesystem with folders ("groups") and files ("datasets"). 

ITensor data written to HDF5 files can be opened in the Julia version of ITensor
and vice versa, making this format a way to pass quantities back and forth
between these two implementations of ITensor.

In order to use the HDF5 features, you must 
[[compile ITensor with HDF5 support|install/install_with_hdf5]] by editing
your `options.mk` file to tell ITensor where the HDF5 library is located on your machine.

## Example of writing to HDF5 files

The following code example shows how to write an ITensor to an HDF5 file, but
the same pattern can be used to write other objects as well (MPS, Index, etc.).

    //Make an ITensor with indices i2,i3 and random elements
    auto i2 = Index(2,"index_i2,A");
    auto i3 = Index(3,"index_i3,B");
    auto T = randomITensor(i2,i3);

    //Create or open an HDF5 file "data.h5" and write
    //T to it, storing it in a "dataset" named "itensor_T"
    auto f = h5_open("data.h5",'w'); //open HDF5 file in write 'w' mode
    h5_write(f,"itensor_T",T); 
    close(f);

Multiple objects and datatypes can be written to the same HDF5
file, just by repeatedly calling `h5_write` and using different names 
for each object (names similar to "itensor_T" used to store `T` above).

## Example of reading from HDF5 files

Continuing with the example above, we can read back the ITensor 
from the HDF5 file as follows:

    auto fi = h5_open("test.h5",'r'); //open HDF5 file in read 'r' mode
    auto T = h5_read<ITensor>(fi,"itensor_T");

Note that you must pass the expected type as a template parameter 
(here `<ITensor>`) to the `h5_read` function. To read another type
such as an `MPS`, you would use `h5_read<MPS>`. 

## List of supported types

- TagSet
- QN
- Index (both regular Index and Index with QN blocks)
- IndexSet
- ITensor
  * dense, real storage
  * QN block-sparse, real storage
  * (complex storage not yet supported as of version 3.1.9)
- MPS
- MPO
