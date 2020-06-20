# Installing & Running ITensor

Installing the Julia version of ITensor is easy once you
have the Julia language installed. For more information about
installing Julia, please see <a href="https://julialang.org/downloads/">the Julia language downloads page</a>.

## Installing ITensor

Once you have installed Julia on your machine,

1. launch an interactive Julia session by typing `julia` (a.k.a. the Julia "REPL")
2. type `]` to enter the package manager (`pkg>` prompt should now show)
3. enter the command `add ITensors`
4. after installation completes, press backspace to return to the normal `julia>` prompt

For extra tips about installing Julia on a cluster machine, <a href="#cluster">see below</a>.

### Installing the MKL Libraries

To have the highest-performing possible code, we recommend the use of the Intel MKL library
which offers state-of-the-art BLAS and LAPACK routines for linear algebra. This is especially
true for machines using Intel CPUs.

To install and configure Julia to use MKL, just do the following steps:
1. type `julia` to enter an interactive Julia session
2. type `]` to enter the package manager (`pkg>` prompt should now show)
3. enter the command `add https://github.com/JuliaComputing/MKL.jl`

Note that after entering this command, the MKL library will be compiled from source on your
machine, which can take quite a long time but only happens once. To check that it worked,
you can enter the Julia commands `using LinearAlgebra; BLAS.vendor()` which should return
`:mkl` if MKL was successfully installed. (You may need to restart Julia for this change
to take effect.)

For more information, see the <a target="_blank" href="https://github.com/JuliaComputing/MKL.jl">MKL.jl</a> Github repo.

## Running ITensor Codes

The basic outline of a code which uses the ITensor library is as follows

    using ITensors

    let
      # ... your own code goes here ...
      # For example:
      i = Index(2,"i")
      j = Index(3,"j")
      T = randomITensor(i,j)
      @show T
    end

The reason we recommend the `let...end` block is that global scope in Julia
can have some surprising behaviors. Putting your code into a `let` block 
avoids these issues.

### Running a Script

Now say you put the above code into a file named `code.jl`. Then you can run
this code on the command line as follows

    $ julia code.jl

This script-like mode of running Julia is convenient for running longer jobs,
such as on a cluster.

### Running Interactively

However, sometimes you want to do rapid development when first writing and 
testing a code. For this kind of work, the long startup and compilation times
currently incurred by the 1.x versions of Julia can be a nuisance. Fortunately
there is a nice solution: repeatedly load your code into a running Julia session.


To set up this kind of session, take the following steps:

1. Enter the interactive mode of Julia, by inputting the command `julia` on the 
command line. You will now be in the Julia "REPL" (read-eval-print loop) with the
prompt `julia>` on the left of your screen.
2. To run a code such as the `code.jl` file discussed above, input the command

        julia> include("code.jl")

  Note that you must be in the same folder as `code.jl` for this to work; otherwise
input the entire path to the `code.jl` file. The code will run and you will see its output in the REPL.
3. Now say you want to modify and re-run the code. To do this, just edit the file in another terminal window or shell session, without closing your Julia session. Now run the command 

        julia> include("code.jl")

   again and your updated code will run, but this time skipping any of the precompilation overhead incurred on previous steps.

The above steps to running a code interactively has a big advantage that you only have to pay the startup time of compiling ITensor and other libraries you are using once. Further changes to your code only incur very small extra compilation times, facilitating rapid development.

### Other Ways of Running ITensor

The ITensors.jl library should be runnable through any type of setting that runs
Julia code, such as Jupyter notebooks. If you encounter a mode
of running ITensor that doesn't work, please contact us by emailing <i>support -at- itensor.org</i>.

### Why Are There Pauses?

You may often notice that your Julia code will run very quickly through one section, then take a long time to run a certain function. For example, while running an ITensor DMRG calculation, the first sweep is often reported as taking 10 or more seconds while the second and third sweeps take only a second. The reason for this is that Julia is a _just in time (JIT) compiled_ language. So instead of compiling at the beginning like a C++ code, the compilation happens at the very last minute when you call a function for the first time. As of Julia version 1.4, the JIT time for Julia can be quite long, but it is expected to get much better with future releases of Julia. Also we are working on various precompilation strategies with ITensors.jl to make it so that more code only has to be compiled once, until you upgrade ITensors.jl again. 


<a name="cluster"></a>
## Installing Julia on a Cluster

If you are installing Julia on a remote cluster, such as
those available at many labs or universities, and Julia is
not already available by default or through a software 
module system, then you can still easily install your own
local version of Julia.

To install Julia locally on your account, follow these
basic steps (details may vary slightly depending on your setup):
1. Download a binary version of Julia <a href="https://julialang.org/downloads/">here</a>
On a remote Unix or Linux cluster, you can use the program "wget" to download files.
2. Use the tar program to uncompress the .tar.gz file you have downloaded.
3. Create a soft link somewhere in your PATH (such as in the bin/ subfolder of your
home folder, which you might need to create) pointing to the file "bin/julia" inside
of the uncompressed Julia folder you just created.

For example, the set of commands might look like this (where these commands
are assumed to be executed in your home directory):

    $ cd
    $ mkdir -p bin
    $ wget https://julialang-s3.julialang.org/bin/linux/x64/1.4/julia-1.4.1-linux-x86_64.tar.gz
    $ tar xvzf julia-1.4.1-linux-x86_64.tar.gz
    $ ln -s julia-1.4.1/bin/julia  bin/julia

