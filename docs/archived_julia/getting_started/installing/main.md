# Installing ITensor

Installing the Julia version of ITensor is easy once you
have the Julia language installed. For more information about
installing Julia, please see <a href="https://julialang.org/downloads/">the Julia language downloads page</a>.

Once you have installed Julia on your machine,

1. Enter the command `julia` to launch an interactive Julia session (a.k.a. the Julia "[REPL](https://docs.julialang.org/en/v1/stdlib/REPL/)")
2. Type `]` to enter the package manager (`pkg>` prompt should now show)
3. Enter the command `add ITensors`
4. After installation completes, press backspace to return to the normal `julia>` prompt
5. [Optional but Recommended] Enter the command 
        julia> using ITensors; ITensors.compile() 
   to compile a large fraction of the ITensor library code and following the instructions afterward to make an alias for loading a pre-built ITensor system image with Julia. This step can take up to 10 minutes to complete but only has to be done once for each version of ITensor. See [[this page|getting_started/compilation]] for more information.

Sample screenshot:
<img width="700px" src="docs/VERSION/getting_started/installing/install_screenshot.png"/>

For extra tips about installing Julia on a cluster machine, [[see this page|getting_started/cluster]].
To enhance the performance of ITensor, we recommend [[installing the MKL library|getting_started/mkl]].

