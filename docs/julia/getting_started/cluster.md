# Cluster Install of Julia and ITensor

If you would like to use the Julia version of ITensor Julia on a remote cluster, 
such as at many labs or universities, but Julia is
not available system-wide, you can still easily install your own
local version of Julia. A local install will offer the same performance and
features (package manager, etc.) as a system-wide install, and you can upgrade
it at your own pace.

Once you set up Julia in your cluster account, you can [[install ITensor|getting_started/install]]
in the same way as on your personal computer.

To install Julia locally within your cluster account, follow these
basic steps (details may vary slightly depending on your setup):
1. Download a binary version of Julia <a href="https://julialang.org/downloads/">here</a>
On a remote Unix or Linux cluster, you can use the program "wget" to download remote files.
2. Use the tar program to uncompress the .tar.gz file you have downloaded.
3. Create a soft link somewhere in your PATH (such as in the bin/ subfolder of your
home folder, which you might need to create) pointing to the file "bin/julia" inside
of the uncompressed Julia folder you just created.

For example, the set of commands might look like this (where these commands
are assumed to be executed in your home directory):

    $ cd
    $ mkdir -p bin
    $ wget https://julialang-s3.julialang.org/bin/linux/x64/1.5/julia-1.5.3-linux-x86_64.tar.gz
    $ tar xvzf julia-1.5.3-linux-x86_64.tar.gz
    $ ln -s julia-1.5.3/bin/julia  bin/julia

After these steps, you should be able to type `julia` from your terminal to run Julia 
in interactive mode. If that works, then you have the Julia language and can run it in
all the usual ways. If it does not work, you may need to log out and back in, and check
that the `bin` directory is in your program execution path (PATH environment variable).

Explanation of the sample commands above:<br/>
The first command `cd` goes to your home directory. The second command makes a new folder `bin/`
under your home directory if it does not already exist. The third command downloads the Julia
language as a compressed tar.gz file. (You may want to do this step and the follwing steps in
a different folder of your choosing.) The fourth command uncompresses the tar.gz file into a 
folder called (in this example) `julia-1.5.3`. The last command makes a soft link called `julia`
in your `bin` directory which links to the Julia language binary within the folder you 
just unpacked containing the Julia language.
