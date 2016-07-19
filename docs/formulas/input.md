# Reading input from a file

For code maintainability and convenience, it is good practice to read simulation
parameters from an external input file rather than hard-coding them into your program.

To make reading parameters easier, ITensor includes a simple input system. Here is an example:

    #include "itensor/all.h"

    using namespace itensor;

    int main(int argc, char* argv[])
    {
    if(argc < 2) 
        { 
        printfln("Usage: %s input_file",argv[0]); 
        return 0; 
        }
    auto input = InputGroup(argv[1],"input");

    auto N = input.getInt("N");
    auto t = input.getReal("t",1.);
    auto do_print = input.getYesNo("do_print",false);

    // ...

    return 0;
    }

Including the above code at the top of your main makes the program expect the first command
line argument to be the name of an input file, which the InputGroup constructor will open and parse.

For example, if your input file is named `input_file`, then you'd call your program like

    ./myprogram input_file

The contents of `input_file` could be as follows

    input
    {
    N = 100
    t = 2.0
    do_print = yes
    }

The `"input"` argument to the InputGroup constructor says that the inputs will be grouped in 
a scope labeled `input { ... }`.

Once the InputGroup object `input` is constructed, various parameters are read by calling 
`input.getInt`, `input.getReal`, or `input.getYesNo`. Each of these methods takes an optional
second argument, which specifies the default value of the parameter if it is not provided in
the file. If no default is given, the parameter must be provided in the file.


