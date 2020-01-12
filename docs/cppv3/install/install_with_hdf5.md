# Installing ITensor with HDF5 Support

HDF5 is a standardized file format for storing numerical data,
making it ideal for storing data such as tensors or tensor networks.
Benefits of using HDF5 include:
- binary-portable files, which can be read on any system (Mac, Linux, etc.)
- HDF5 files have structure similar to a file system, so that objects stored
can be retrieved using their name
- attributes can be associated to stored data, for example, stating which
version of code was using to write the data


## Steps to Compile ITensor with HDF5 Support

<b>Step 0</b> of compiling ITensor with HDF5 is to have the HDF5
library available on your system. It may already be available: one way
to check is to see if the command `h5cc` exists and is in your path.
If HDF5 is not installed or you are unsure, use your package manager 
on Linux, or a package manager such as Homebrew on Mac to install it.
Alternatively, you can download and install HDF5 from source similar
to many other libraries.

<b>Step 1</b> is then to determine where your HDF5 libraries and header files
are located. A very convenient way to do this is to run the command

    h5cc -show

Which shows the commands used to compile a program with HDF5 support.
By observing the folder names occurring after the "-L" flag in the 
output, you can determine the prefix where HDF5 is installed. This
prefix is the folder just before the part beginning with "/lib/libhdf5...".
So if the output includes "/usr/local/lib/libhdf5_hl.a" then the prefix
is "/usr/local".

<b>Step 2</b> is to modify your options.mk file, which is used to configure
the ITensor compilation process. In options.mk, find the line

    #HDF5_PREFIX=/usr/local

then uncomment this line (remove the "#" character) and edit the prefix
to be the one where HDF5 is installed on your computer.

<b>Step 3</b> is to compile, or recompile ITensor fully, so that
HDF5 support is built throughout the library:

    make clean
    make


If the compilation succeeds, you will have HDF5 support within ITensor.

