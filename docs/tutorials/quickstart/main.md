<span class='article_title'>ITensor Basics Quick Start</span>

<span class='article_sig'>Thomas E. Baker&mdash; May 4, 2016</span>

Let's get started with ITensor by looking at the simplest program we can write involving a tensor.
For a similar guide oriented towards DMRG calculations, see [[DMRG Quick Start|tutorials/DMRGquickstart]].

The contents of `hello_itensor.cc`.

    #include "itensor/all.h"

    using namespace itensor;

    int main()
    {
    auto i = Index("index i",4);
    auto j = Index("index j",6);
    auto T = ITensor(i,j);

    T.set(i(3),j(2),3.14159);

    PrintData(T);

    return 0;
    }


To understand what this program does, let us start at the top. The line

    #include "itensor/all.h"

pulls in _all_ of the ITensor library. You could instead just include the parts of
ITensor you want; for more information
on which headers define each feature see the [[detailed documentation|classes]].

The next line of the program 

    using namespace itensor;

says to pull in every function and object type defined in
the `itensor` namespace. Otherwise you would have to type things like `itensor::Index` instead of
just `Index`.


Now we reach the actual code our program will run.
C++ requires that all programs have
a function named `main` which is the first function
to run when your program is executed

    int main()
    {

    //...rest of code here

    return 0;
    }

Now let us look at the body of the code. 
First we define tensor indices i and j, of type `Index`.

    auto i = Index("index i",4);
    auto j = Index("index j",6);

Each Index has a name and a size. Using these indices, we can define
an ITensor

    auto T = ITensor(i,j);

which starts out with all elements zero. To change an element, we
can call

    T.set(i(3),j(2),3.14159);

which sets the i=3, j=2 element to the value 3.14159. 

The `PrintData` macro conveniently prints information about the
ITensor T (such as its indices) and shows all of its non-zero elements:
 
    PrintData(T);

