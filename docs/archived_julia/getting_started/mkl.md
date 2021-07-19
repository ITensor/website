# Enhancing Performance by Installing MKL

To have the highest-performing possible code, we recommend the use of the Intel MKL library
which offers state-of-the-art BLAS and LAPACK routines for linear algebra. This is especially
true for machines using Intel CPUs.

To install and configure Julia to use MKL, just do the following steps:
1. type `julia` to enter an interactive Julia session
2. type `]` to enter the package manager (`pkg>` prompt should now show)
3. enter the command `add MKL`

Note that after entering this command, the MKL library will be compiled from source on your
machine, which can take quite a long time but only happens once. To check that it worked,
you can enter the Julia commands `using LinearAlgebra; BLAS.vendor()` which should return
`:mkl` if MKL was successfully installed. (You may need to restart Julia for this change
to take effect.)

For more information, see the <a target="_blank" href="https://github.com/JuliaComputing/MKL.jl">MKL.jl</a> Github repo.
