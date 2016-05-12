<span class='article_title'>ITensor Quickstart Guide</span>

<span class='article_sig'>Thomas E. Baker&mdash; May 4, 2016</span>

This article provides code for a quick introduction to the fundamentals of ITensor. For a quickstart guide oriented towards performing a DMRG calculation, go [[here|tutorials/DMRGquickstart]].

The contents of `helloitensor.cc`.

    #include "itensor/all.h"

    using namespace itensor;

    int main()
    {
    auto i = Index("index i",4);//initializes index "i" with size 4 (i.e., four possible values)
    auto j = Index("index j",6,"MyIndexType",2);//another index with a custom type (third field) and prime level 2
    auto T = ITensor(i,j);

    T.set(i(3),j(2),3.14159);

    PrintData(T);

    return 0;

    }

The following sample program generates a code to establish several indices, `ITensors` and `IQTensors` as well as setting manipulating values of tensors.

These files contain functions we use below.  They are found through the Makefile.  Include "all.h" is a catch-all for every header file that you might need.  This reduces compile time slightly.  Speed this up by only including the header files you actually need (example: "/itensor/mps/dmrg.h").

We also must show what namespace to look in for special functions.  This is called as `using namespace itensor;`

    //        +------------------------+
    //>-------|    (1) Header Files    |-------<
    //        +------------------------+
    #include "itensor/all.h"

    using namespace itensor;

Now we declare the main program.  C++ requires this declaration and that it is called `main`.

    //        +------------------------+
    //>-------|    (2) Main object     |-------<
    //        +------------------------+

    int main()//master object in program--must be called main
    {

    //...rest of code here

    return 0;

    }

Here is the body of the code.  It will define two indices and create an [[ITensor|classes/itensor]] from them.  [[Priming|tutorials/primes]] and [[index types|classes/index]] are discussed on the linked pages.

    //        +----------------+
    //>-------| (3) Code body  |-------<
    //        +----------------+
    //

    auto i = Index("index i",4);//initializes index "i" with size 4 (i.e., four possible values)
    auto j = Index("index j",6,"MyIndexType",2);//another index with a custom type (third field) and prime level 2
    auto T = ITensor(i,j);

    T.set(i(3),j(2),3.14159);

    PrintData(T);//prints ITensor T

