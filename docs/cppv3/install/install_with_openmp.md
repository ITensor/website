# Installing ITensor with OpenMP multithreading support

ITensor provides some native OpenMP multithreading.
Currently, block sparse tensor contractions support
optional multithreading, so any ITensor code using QN
conservation and where the computation time is dominated
by tensor contractions may benefit.

## Steps to Compile ITensor with OpenMP multithreading support

<b>Step 0</b> of compiling ITensor with OpenMP multithreading support
is to have the OpenMP library available on your system. It is likely
already available, since it is included with most modern compilers.
If not, you will have to look up instructions on how to install it
depending on the compiler and system you are using.

<b>Step 1</b> is to modify your options.mk file, which is used to 
configure the ITensor compilation process. In options.mk, find the line

    #ITENSOR_USE_OMP=1

then uncomment this line (remove the "#" character).

<b>Step 2</b> is to compile, or recompile ITensor fully, so that
OpenMP support is built throughout the library:

    make clean
    make


If the compilation succeeds, you will have OpenMP multithreading
support within ITensor.

<b>Step 3</b> is to set the number of threads you want.
Before running your executable, you can set the number of threads
with the following command line command:

    export OMP_NUM_THREADS=8

or by calling your executable as follows:

    OMP_NUM_THREADS=8 ./myappname

We also recommend turning off BLAS/LAPACK multithreading, since 
it may compete with ITensor's native multithreading.

To turn off BLAS multithreading if you are compiling 
ITensor with Intel MKL you can set the environment variable:

    export MKL_NUM_THREADS=1

or directly link to MKL's sequential library (see the BLAS/LAPACK
section of options.mk.sample for an example of how to do that).

To turn off BLAS multithreading if you are compiling ITensor with OpenBLAS, 
you can set the following environment variable:

    export OPENBLAS_NUM_THREADS=1

