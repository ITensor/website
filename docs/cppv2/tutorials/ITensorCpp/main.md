<span class='article_title'>Beginner's guide to C++ for ITensor</span>

<span class='article_sig'>Thomas E. Baker&mdash;November 11, 2015</span>

C++ can often be daunting for a programmer if you are used to programming in a different language like python, Mathematica, or Fortran. ITensor seeks to reduce the amount of high level C++ knowledge that is necessary to make and run code.  In that sense, ITensor emphasizes the parts of C++ that act like python or other higher level programming language making it easy to use.  Even though ITensor has these high level programming features, it is still fast.  For large computations, the most efficient program is always best and C++11 provides us with a compiler that can assemble code so you can run your programs with the least amount of computational time.

The ITensor development community makes sure all the internals of the program are fast and efficient.  As the programmer, this lets you have complete control over the design aspects of your program.

This article will explain the basics of how to set up a general code in C++11.  For an example pertaining specifically to DMRG, see our [[quickstart|tutorials/quickstart]] guide to get going on a fully working DMRG code.  You can also look in the `samples` folder of the ITensor library or the `tutorials`.  To install C++11 on your computer, you can perform an internet search of "install C++11 [operating system]" if it is not already installed.

## Why C++11?

There are a lot of nice features in C++11 that make running the ITensor library fast and efficient like the ability to define classes.  Classes, such as the `ITensor` itself allow the program to encapsulate objects that have many data types.  In contrast, regular C programming didn't have classes, making code more cumbersome.  We would also have to deallocate memory once we were done using it and that is accomplished automatically in C++.

C++11 is a major improvement on the C++ language.  How memory is allocated is done automatically with the `auto` type declaration.  Instead of allocating memory for an integer with the keyword `int`, we can now use `auto` and the compiler will determine which type is needed by looking at how the variable is used.

The ITensor library increases the functionality of C++11 with many functions that are documented [[here|classes]].  Writing a similar library in Fortran would be possible, but there are a ton of advantages for you, the user, to write your code with the newest C++ compiler.  If you're coming from python, Mathematica, Matlab, or some other language, then note that a similar computation in one of those languages may be much slower than can be accomplished in C++.

In the future, we hope to add a higher level programming langauge interface so that programming becomes even easier, but for now using ITensor requires very little knowledge beyond basic programming.

## Hello ITensor

Here is an example of the first introductory program `hello_itensor.cc`.  This program will contract two `ITensor`s together.

    #include "itensor/itensor.h"
    using namespace itensor;
  
    int main() 
    {
    auto i = Index("index i",3);
    auto j = Index("index j",4);
    auto k = Index("index k",2);
  
    auto A = ITensor(i,j);
    auto B = ITensor(k,j);

    A.set(i(3),j(2),3.141);
    B.set(k(1),j(2),2.718);

    auto C = A * B;//contraction over the index j

    printfln("A * B = %f",C);

    return 0;
    }

In this article, we are more concerned with what happens beyond the ITensor functions.  `Index`, `ITensor`, `set`, `printfln`, and other ITensor specific functions and classes are covered in the [[ITensor book|]].  Here, we want to concentrate on the basics of C++11 like `include`, header files, `using namespace`, `auto`, `int`, `main`, and `return` as well as all the semicolons, curly braces {}, and how to run the program.

## Good things to know about C++

Reorder:
semicolon (;)...especially coming from python and julia
type declaration
how to use objects (in addition to built in types, you can define user defined types)
last thing:  how to make objects
header files

### Object-oriented language

instances of user defined objects is a object (compared with a type)...NewType or MyType auto T = NewType...NewType = 5;

looks like previous declarations but it now has a new type...can plug into a function...

exposes methods that are bound to Types...access hidden internal states come with strong guarantees and stuff

first few times with a type is a disastor...takes time!  you do really silly things with the freedom of C++ but then you'll

The general format of any C++ code is block of code that look something like the following:

    class some_object{
    //...code...
    }

There are a couple of things to notice.  These bits of code are what are known as objects and each object in the C++ language is an object. This is in contrast with Fortran or similar languages where you have functions and subroutines.  Here, in C++, everything is an object.  

There are also `struct`s

CLass is private by default and structs are public by default

The `type` of the function is the return value.  So, if the return value is the integer 1, we'd put `int` for `type`.

The very first object in a C++ program is always called `main` by convention.  See an example in our [[quickstart|tutorials/quickstart]] guide.

### Semicolons

Code is always placed in between curly braces (`{}`).  However, there is a feature in C++ that we must mention:  the use of semicolons (`;`).  The semicolon ends a line of code, for example:

   a = 5;

is a good line of code that assigns `a` to the value 5.  If we don't put the semicolon in, we'll get a compiler error when we run the program.

### Data declaration

If you're coming from using python, you're used to defining variables like above `a=5`.  However, C++ needs you to also tell it what type it is so that the compiler can reserve the correct amount of memory (this makes the program faster and able to store more information).  So, we should have defined the memory the compiler needs to allocate like

    int a=5;

C++ has a nice feature that it will determine what type `a` needs to be automatically with the declaration

    auto a=5;#same as int a=5;!

based on how `a` is used, the compiler will determine what type `a` is and how much memory to allocate.

### Header files

simplest layer:  purely from a user point of view is how you obtain other people's code.  Brings in outside code...injects code and tells your code other code exists and then doesn't have to compile

end of the article is more advanced

difference between cc and h files are: Miles' quick spiel:  historically only had cc files (cpp or source files)...there was only one basic rule that basically you have a function and that funciton had to be declared for the code to use it.  the code had to be declared after the declaration....breaking code over several cc files means you have a sorting problem...you can't double define something.  maintenance headache to put declarations before code in all cc files.  Waste of time, so let's make a header file and use the preprocessor "include" trick to declare and then define.

Then the headers took on a life of their own.  The became templates. Templates are patterns for making code.  Must define templates in headers (no other way)...abuse of header system...another trick...endline in function ...something...

there are other source files...we have a naming convention here

habit of putting code in a header file  

convenient over going into the Makefile and then 

Header files are used to define functions in a separate space from where we define what a function does.

no double quotes!

also include itensor/[header]

Let's say in our main program we define a function

    fibonacci(1.)

To avoid clutter when writing our program, and so that future users can figure out what is programmed, we may define the function `fibonacci` in a header file, a completely different file

    void fibonacci(a)
    {
      Real a;//Real is a type in ITensor
      println("hey there!")
    }

This is provided we tell the compiler where to look for the header file at the top of the program.  So, we need to define something like

    #include 'fibonacci.h'

### Naming files

The convention for naming main files (things that contain the `main` function for example) are called with the `.cc` extension.

Header files have a `.h` extension.

## Compiling C++ Code

We could run our programs by typing in a string in a terminal window like

go look in how to rename the executable

    g++ hellodmrg.cc -o
    g++ -c hellodmrg.o 

but that is cumbersome!  Often we have a lot of header files that need to be included by the compiler.  The solution to make this compilation snappy is to create a Makefile and use that to generate all the code.

This command line works for a self-contained code...if we have libraries, then need -I (header files) and -L (second line...linker where .a and .so files...partially compiled files in library) also need -l (these are flags like MKL...Miles needs to add this...LAPACK, etc.)

-l/usr/local/lapakc/include
-L/usr/local/lapack/lib -lblack -llapack
-L/path/to/itensor/lib -litensor
-I/path/to/itensor (before lapack include)


order of -l matters on some compilers (Trial and error) 

### Anatomy of a Makefile

Here is a basic makefile that you can use (copy into a file `Makefile` in the same directory as the main `.cc` file to compile code.

WARNING:  Don't copy this file as there are specific formatting needs that must be fulfilled to actually run the makefile.  Instead, copy a Makefile from the `tutorials/` or `sample/` folder in the ITensor library.

    include ../this_dir.mk
    include ../options.mk
    ################################################################

    #Mappings --------------
    REL_TENSOR_HEADERS=$(patsubst %,$(ITENSOR_INCLUDEDIR)/%, $(TENSOR_HEADERS))

    #Define Flags ----------
    CCFLAGS= -I. $(ITENSOR_INCLUDEFLAGS) $(CPPFLAGS) $(OPTIMIZATIONS)
    CCGFLAGS= -I. $(ITENSOR_INCLUDEFLAGS) $(DEBUGFLAGS)
    LIBFLAGS=-L$(ITENSOR_LIBDIR) $(ITENSOR_LIBFLAGS)
    LIBGFLAGS=-L$(ITENSOR_LIBDIR) $(ITENSOR_LIBGFLAGS)

    #Rules ------------------

    %.o: %.cc $(ITENSOR_LIBS) $(REL_TENSOR_HEADERS)
            $(CCCOM) -c $(CCFLAGS) -o $@ $<

    .debug_objs/%.o: %.cc $(ITENSOR_GLIBS) $(REL_TENSOR_HEADERS)
            $(CCCOM) -c $(CCGFLAGS) -o $@ $<

    #Targets -----------------

    build: hellodmrg

    all: hellodmrg

    hellodmrg: hellodmrg.o $(ITENSOR_LIBS) $(REL_TENSOR_HEADERS)
            $(CCCOM) $(CCFLAGS) hellodmrg.o -o hellodmrg $(LIBFLAGS)

    clean:
            rm -fr *.o .debug_objs hellodmrg hellodmrg-g

To re-emphasize, your header files must have a tab.

The first line is the path to the `this_dir.mk` in the ITensor library (this example was adapted from the `sample` folder, so it is just one directory up--the `../` command).The second points to `options.mk`.

The `TENSOR_HEADERS` are whatever headers we'd like to include.  We don't have to put all the headers we use here.  This is taken care of under the Mappings line.


Rules are assigned in the `options.mk` which include compiler flags to use parallelization with `openmp` and other useful libraries (such as the mkl libraries or using C++11).  

The `build` line tells the Makefile which executable to make (changing the name changes the executable).  The `debug` line is the same for the debugging file.  The `all` line is useful if there is more than one executable to make.

To generalize this makefile to what you might need it for, the directory to the ITensor library needs to be correct in the first two lines.  Also, the names of the executables must be changed or added to the build and all lines as well as listing them where `hellodmrg` only appears now (so a new line with `hellodmrg` must be made for each executable we want the makefile to generate). 

The `clean` line allows the command `make clean` to be run to remove all the files the makefile makes (but it will not remove the `.cc` and `.h` files!  Only the `.o` and executables).

Once you make the executable by typing `make` into the command line, you can type `./[executable name]` to run it.


each point we raise, let's attack it from the python viewpoint.  how to get around

core.h was to update program with library update

maybe make MPScore.h or ITensorcore.h 


### Alternative Makefile

This make file has some alternative ways of expressing the above which are simpler.  This makefile is better if you want to call the executables the same name as the `.cc` files.

    LIBRARY_DIR=../

    APP1=hellodmrg
    #APP2=howdy

    #################################################################
    #################################################################
    #################################################################
    #################################################################

    include $(LIBRARY_DIR)/this_dir.mk
    include $(LIBRARY_DIR)/options.mk

    #Mappings --------------
    REL_TENSOR_HEADERS=$(patsubst %,$(ITENSOR_INCLUDEDIR)/%, $(TENSOR_HEADERS))

    #Rules ------------------

    %.o: %.cc $(REL_TENSOR_HEADERS)
            $(CCCOM) -c $(CCFLAGS) -o $@ $<

    .debug_objs/%.o: %.cc $(REL_TENSOR_HEADERS)
            $(CCCOM) -c $(CCGFLAGS) -o $@ $<

    #Targets -----------------

    build: $(APP1) $(APP2)
    debug: $(APP1)-g $(APP2)-g

    $(APP1): $(APP1).o $(ITENSOR_LIBS)
            $(CCCOM) $(CCFLAGS) $(APP1).o -o $(APP1) $(LIBFLAGS)

    $(APP2): $(APP2).o $(ITENSOR_LIBS)
            $(CCCOM) $(CCFLAGS) $(APP2).o -o $(APP2) $(LIBFLAGS)

    clean:
            rm -fr .debug_objs *.o $(APP1) $(APP1)-g $(APP2) $(APP2)-g

    mkdebugdir:
            mkdir -p .debug_objs

This is the style presented in the `tutorials`.
