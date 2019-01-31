# Input Parameter System

<span class='article_sig'>Thomas E. Baker&mdash;October 9, 2015</span>

This tutorial introduces the optional input parameter system included with ITensor.

## Motivation - Defining Parameters

One way to define simulation parameters is to "hard code" them at the top of your program.
For example:

    int N = 20;
    bool dostep = true;
    Real Q = 4.3;
    Complex T = Complex(0.,0.1);

Defining parameters this way has two drawbacks despite being simple:

  1. Each time you need to change a parameter, you have to recompile the program. 
  2. Passing variables from one part of the program to another can get messy if we don't "bundle" all of the parameters together.

Let's solve both problems using the `InputGroup`.  

## InputGroup Example

At the top of our main function, we can define an `InputGroup` as follows:

    int main(int argc, char* argv[])
    {
    if(argc != 2) 
       { 
       //reminds us to give an input file if we forget
       printfln("Usage: %s inputfile",argv[0]); 
       return 0; 
       }
    auto input = InputGroup(argv[1],"input");
 
    auto N = input.getInt("N"); //number of sites
    auto J = input.getReal("J",1.0); //coupling

    //...


The above code parses whichever file we pass as input, and expects that file to contain a section looking like

    input 
    {
    N = 15
    J = 2.3
    }

The call to `InputGroup(argv[1],"input")` parses the file, storing all parameters in the "input" section (in this case "N" and "J"),
and returns the object we named `input`.

The line 

    auto N = input.getInt("N"); //number of sites

tries to read in the parameter "N" as an integer type. If "N" is not defined, this line will throw an exception.

In contrast, the line

    auto J = input.getReal("J",1.0); //coupling
                              //^ default value of 1.0

tries to read in the parameter "J" as a real number. But if "J" is not defined, `getReal` will return
the default value `1.0` provided and continue with the program.

## Understanding argc and argv

Returning to the top of our sample program, argc will be set by the C++ compiler to always equal the 
number of inputs to our program, and argv is an array of these inputs.
The input argv[0] is always the program name, whereas argv[1] will be the first non-trivial input on the command line.

So if we run our program as `./program filename`, then
- argv[0] == "program"
- argv[1] == "filename"
<br/><br/>

The statement `if(argc != 2)` makes sure we provided the name of the input file. 
Calling `InputGroup(argv[1],"input")` constructs an InputGroup from the input file 
(whose name is stored in argv[1]). The string "input" names the collection of inputs that we 
want to read in (more on this below).

### Input File Organization

A good way to organize things is to place different parameter files in their own folders, separate from where we compiled our program.

To run our program from each separate folder, we can go to that folder and type

    [program location]/program params 2>&1 | tee [output file]

Changing `[program location]` to where we compiled `program` and running the above command does three things:

  1. `params` is given to the program to run.
  2. `2>&1` combines both the output from the file and anything in the error output into one output
  3.  `tee` makes a copy of the output in the termainal to `[output file]` 

