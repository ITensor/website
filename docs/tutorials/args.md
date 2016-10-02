
# The Args Named Argument System

<span class='article_sig'>Miles Stoudenmire&mdash;Mar 26, 2016</span>

### The Problem

A unfortunate fact about C++ functions is that arguments must be passed in a fixed order.
This is frustrating when you are ok with certain default arguments, but must provide
them anyway to reach arguments further down the list.

To make matters worse, function arguments can be opaque and hard to interpret.
<br/>Consider the following code:

    truncateMPS(psi,500,1E-5,false);

While it is clear that psi is some matrix product state to be truncated, what do
the other parameters mean?

If the truncateMPS function accepted an Args object instead, we
could call it like this

    truncateMPS(psi,{"Maxm=",500,"Cutoff=",1E-9,"ShowSizes=",false});

This is easier to read and lets us specify the parameters we care about,
leaving the rest to have default values. For example, if we are happy with the default
value for "Maxm" and "ShowSizes", we could call truncateMPS as

    truncateMPS(psi,{"Cutoff=",1E-9});

The named arguments can be passed in any order we like

    truncateMPS(psi,{"ShowSizes=",false,"Maxm=",500,"Cutoff=",1E-9});

Trailing equals signs "=" after each argument name are optional, and are ignored by the args
system. So the following call would have identical results

    truncateMPS(psi,{"ShowSizes",false,"Maxm",500,"Cutoff",1E-9});

Of course, in production code it is bad practice to "hard wire" numbers directly 
into functions; a better practice is to define all parameters one place, like at 
the top of main when reading from a parameter file. Even in this situation,
the Args system makes things more readable and flexible
regarding argument order and default arguments:

    int maxm = 500;
    Real cut = 1E-9;
    bool show_sizes = false;
    ...
    truncateMPS(psi,{"ShowSizes=",show_sizes,"Maxm=",maxm,"Cutoff=",cut});

<br/>
### Creating a Function that Accepts Args

To allow a function to take an Args object, first make sure the Args class is available

    #include "itensor/util/args.h"

Or just do

    #include "itensor/all.h"

Next define the last argument of your function to be

    func(..., Args const& args = Args::global());

where the "..." means all the usual arguments the function "func" accepts.
For example, the truncateMPS function above could be declared as

    MPS truncateMPS(MPS const& psi, Args const& args = Args::global());

Making the default value `Args::global()` does the following: if no named arguments
are passed then "args" will refer to the global Args object. By default the
global Args object is empty;
however, one can add arguments to Args::global() to set
global defaults&mdash;for more details see the section on argument lookup order below.

Sometimes you may want to further modify the args object within your function.
For such cases it is better to accept args by value

    func(..., Args args = Args::global());

<br/>
### Accessing Named Arguments Within a Function

Using the fictitious truncateMPS function as an example, recall that it 
accepts three named arguments:
* "Maxm" &mdash; an integer
* "Cutoff" &mdash; a real number
* "ShowSizes" &mdash; a boolean

(Named arguments can also be string valued.)

To access these arguments in the body of the function, do the following:

    MPS
    truncateMPS(MPS const& psi,
                Args const& args) //no Args::global() because we already
                                  //specified it in the declaration
        {
        auto maxm = args.getInt("Maxm",5000);
        auto cutoff = args.getReal("Cutoff",1E-12);
        auto show_sizes = args.getBool("ShowSizes",false);

        ...

        }


The second argument to each of the above "get..." methods is the default value
that will be used if that argument is not present in `args`. The 
order in which these functions are called is not important.

Occasionally a named argument should be mandatory. To make it so, just
leave out the default value when calling getInt, getReal, getBool, or getString:

    void
    func(...
         Args const& args)
        {
        //Mandatory named argument
        auto result_name = args.getString("ResultName");
        ...
        }


<br/>
### Lookup Order and Global Args

When calling one of the "get..." methods (such as getInt or getString) on an Args instance,
the value returned will be as follows:

1. The value if defined in the instance itself

2. If not defined in the instance, the value defined in the global Args object

3. If not defined in the global Args, the default value provided to "get..."

Here is an example:

    Args::global().add("DoPrint",true);

    auto args = Args("Cutoff",1E-10);

    auto do_print = args.getBool("DoPrint",false);
        // ^ do_print == true, found in Args::global()

    auto cutoff = args.getReal("Cutoff",1E-5);
        // ^ cutoff == 1E-10, found in args

    auto maxm = args.getInt("Maxm",5000);
       // ^ maxm == 5000, not found in args or Args::global() so default used
    

<br/>
### Creating Args Objects

There are a few different ways to construct args objects. The simplest is the Args constructor,
which accepts any number of name-value pairs:

    auto args = Args("Name=","some_string",
                     "Size=",100,
                     "Threshold=",1E-12,
                     "DoThing=",false);

The above constructor is what is called when calling a function using the syntax

    someFunc(...,{"Name=","some_string","Size=",100});

Args objects can also be constructed from strings of the form `"Name1=value1,Name2=value2,..."`.
So for example

    auto args = Args("Name=some_string,Size=200,Threshold=1E-10");

Finally, arguments can be added to an Args object that is already defined using the add method.
Adding an argument that is already defined overwrites the previously defined value.

    auto args = Args("Name=","name1");

    args.add("Threshold=",1E-8);

    if(args.defined("Threshold")) println("args contains Threshold");


