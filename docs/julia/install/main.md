# Installing & Running ITensor

Installing the Julia version of ITensor is easy once you
have the Julia language installed. For more information about
installing Julia, please see <a href="https://julialang.org/downloads/">this link</a>
and the Tips About Installing Julia below.

## Installing ITensor

1. launch an interactive Julia session by typing `julia` (a.k.a. the Julia "REPL")
2. type `]` to enter the package manager
3. enter the command `add ITensors`
4. after installation completes, press backspace to return to the normal julia> prompt or Ctrl-D to exit the REPL



## Tips About Installing Julia

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

    > cd
    > mkdir -p bin
    > wget https://julialang-s3.julialang.org/bin/linux/x64/1.4/julia-1.4.1-linux-x86_64.tar.gz
    > tar xvzf julia-1.4.1-linux-x86_64.tar.gz
    > ln -s julia-1.4.1/bin/julia bin/julia

