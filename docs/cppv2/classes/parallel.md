# Support for MPI Parallelism

The messsage passing interface (MPI) is a framework for creating
parallel algorithms based around passing data between parallel
workers or "nodes". In this paradigm, the nodes do not share
memory (in the sense of being able to write to the same memory 
addresses) but instead send data in the form of "messages".

The file `util/parallel.h` provides some convenient wrappers
and facilities for using MPI to communicate ITensor objects
and other data types between nodes.

To use the code in this file, you must have an implementation
of MPI (such as Open MPI, LAM, or MPICH) and provide both
an include path to the file `mpi.h` as well as link to the 
relevant MPI library files. Most MPI implementations provide
a command named `mpic++` or `mpicxx` that acts as a replacement
C++ compiler that will automatically include MPI support.
These commands also typically come with an option that lets you view
the correct set of compiler and linker flags for your system.
(For some versions of MPI, the command is `mpicxx --showme`.)

At a lower level, MPI is a set of rather simple C functions.
The parallel.h file provided in ITensor mainly provides some
useful wrappers around certain functions that are helpful
to use together, and it provides a convenient C++ interface.
You are encouraged to study the parallel.h code as
it is not too complex and is written in a fairly generic
way (not specific to ITensor internals).


## Initializing the MPI Environment

The simplest MPI parallel code you can write using the 
parallel.h tools is as follows

    #include "itensor/all.h"
    #include "itensor/util/parallel.h"
    using namespace itensor;

    int
    main(int argc, char* argv[])
    {
    Environment env(argc,argv);

    if(env.firstNode()) printfln("There are %d nodes",env.nnodes());

    return 0;
    }

To run this code, you compile it (either using mpic++ or with the 
flags suggested by mpic++) then run it using a command similar to:

    mpirun --np 4 ./myprogram

The precise command depends on your particular MPI implementation.;

Constructing the `Environment` object `env` initializes the MPI
environment and is required. This establishes the basic setup
of the requested number of nodes (i.e. requested by `mpirun`) 

## Simple Communication

An easy to use and convenient type of communication is the
broadcast. This takes a variable whose value is set on the 
root node (node number 0) and sends it to all of the other
nodes. Afterwards the variable will have the same value on
every node.

For example, consider the following code:

    int i = 0;
    if(env.firstNode()) i = 5;

    printfln("Node %d has i=%d",env.node(),i);

    broadcast(env,i);

    printfln("Now node %d has i=%d",env.node(),i);

Running it should print something like:

    "Node 1 has i=0"
    "Node 0 has i=5"
    "Now node 0 has i=5"
    "Now node 1 has i=5"

I say "something like" because due to the vagaries of 
parallel execution, these lines could be printed in 
a different order and the text can even sometimes
be garbled if different nodes print on top of each other.

## Communicating to a Specific Node

For sending data from one node to just one other node,
parallel.h provides a class called `MailBox`. The MailBox
class is mainly a wrapper around MPI_Send, which does a 
_blocking send_, but the MailBox class does other
helpful things too such as breaking data into smaller
pieces to avoid exceeding MPI buffer sizes for large sends.

To set up a MailBox object, just provide the Environment
object and the number (0 indexed) of the other node
the MailBox should always send to.

For node 0 to set up a MailBox it can use to send data
to node 1, it can do:

    //On node 0
    auto mbox = MailBox(env,1);

Then to send an object to node 1:

    mbox.send(obj);

Any object can be sent as long as it is plain
data or it supports the `.read(std::istream&)`
and `.write(std::ostream&) const` methods,
which define how to convert the object from
and to binary streams.

After the sending node begins a send, it waits
for the receiving node to call receive, like this:

    //On node 1
    auto mbox = MailBox(env,0);
    ...
    mbox.receive(obj);

Likewise if the receiving node calls receive before
the sending node calls send, the receiving node also
waits. Once both send and receive have been called
(on the sending and receiving nodes, respectively)
the nodes perform a communication then both
nodes continue with their exection.





