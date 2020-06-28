# Reducing Compilation Overhead

Julia code sometimes takes very long to run initially, or may run very quickly through one section then take a long time to run a certain function. The reason for this is that Julia is a _just in time (JIT) compiled_ language. So instead of compiling at the beginning like a C++ code, the compilation happens at the very last minute when you call a function for the first time. As of Julia version 1.4, the JIT time for Julia can be quite long, but it is expected to get much better with future releases of Julia.

However, there are strategies to reduce JIT compile time, sometimes by quite a large amount. Below we discuss the strategies in order of increasing sophistication.

## Running Code in the REPL (Interactive Julia Terminal)

Say you have Julia code in a file called `code.jl`. You can load and run this code inside an interactive Julia session by doing:

    julia> include("code.jl")

The advantage of doing this is that after the first time you run your code this way, every run after will be able to use library functions that were compiled the first time. So you should see subsequent runs become much more fast and responsive. 

## Compiling an ITensors.jl System Image

The above strategy of running code in the Julia REPL (interactive mode) works well, but still incurs a large start-up penalty for the first run of your code. Fortunately there is a nice way around this issue too: compiling ITensors.jl and making a system image built by the [PackageCompiler.jl](https://github.com/JuliaLang/PackageCompiler.jl) library.

To use this approach, we have provided a convenient one-line command:

    julia> using ITensors; ITensors.compile()

Once ITensors.jl is installed, you can just run this command in an interactive Julia session. It can take a few minutes to run, but you only have to run it once for a given version of ITensors.jl. When it is done, it will create a file `sys_itensors.so` in the directory `~/.julia/sysimages/`.

To use the compiled system image together with Julia, run the `julia` command (for interactive mode or scripts) in the following way:

    $ julia --sysimage ~/.julia/sysimages/sys_itensors.so

A convenient thing to do is to make an alias in your shell for this command. To do this, edit your `.bashrc` or `.zshrc` or similar file for the shell you use by adding the following line:

    alias julia_itensors="julia --sysimage ~/.julia/sysimages/sys_itensors.so -e \"using ITensors\" -i "

where of course you can use the command name you like when defining the alias. Now running commands like `julia_itensors code.jl` or `julia_itensors` to start an interactive session will have the ITensor system image pre-loaded and you will notice significantly faster startup times. The arguments `-e \"using ITensors\" -i` make it so that running `julia_itensors` also loads the ITensor library as soon as Julia starts up, so that you don't have to type `using ITensors` every time.
