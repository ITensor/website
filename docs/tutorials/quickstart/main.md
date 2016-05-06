<span class='article_title'>ITensor Quickstart Guide</span>

<span class='article_sig'>Thomas E. Baker&mdash; May 4, 2016</span>

This article provides code for a quick introduction to the fundamentals of ITensor. For a quickstart guide oriented towards performing a DMRG calculation, go [[here|tutorials/DMRGquickstart]].

The following sample program generates a code to establish several indices, `ITensors` and `IQTensors` as well as setting manipulating values of tensors.

    //        +------------------------+
    //>-------|    (1) Header Files    |-------<
    //        +------------------------+
    //These files contain functions we use below.  They are found through 
    //the Makefile.  Include "all.h" is a catch-all for every header file
    //that you might need.  This reduces compile time slightly.  Speed this up
    //by only including the header files you actually need (example: "/itensor/mps/dmrg.h").
    #include "all.h"

    using namespace itensor;// this tells ITensor specific functions where to be found, use everywhere

Now we declare the main program and define some indices.  [[Priming|tutorials/primes]] and [[index types|classes/index]] are discussed in other pages.

    int main()//master object in program--must be called main
    {
    //        +----------------+
    //>-------|  (2) Indices   |-------<
    //        +----------------+
    //

    auto i = Index("index i",4);//initializes index "i" with size 4 (i.e., four possible values)
    auto j = Index("index j",6,"MyIndexType",2);//another index with a custom type (third field) and prime level 2


    println(j.type());//prints "MyIndexType"...see code link above for more options!

ITensor also supports indices that label specific quantum number sectors.  Read more [[here|classes/iqindex]] and [[here|tutorials/Qnumbers]].

    //        +----------------+
    //>-------| (3) IQIndices  |-------<
    //        +----------------+
    //

    auto L = IQIndex("L",Index("L-",2),QN(-1),
                         Index("L0",4),QN( 0),
                         Index("L+",2),QN(+1));//Creates index separated into quantum numbers

The backbone of ITensor is the `ITensor` and `IQTensor` classes.  Read about them [[here|classes/itensor]] and [[here|iqtensors]] as well in-depth dicussions in the [[ITensor book|page=book]].
    
    //        +----------------------------+
    //>-------| (4) ITensors and IQTensors |-------<
    //        +----------------------------+
    auto Q = IQTensor(L);//creates an IQTensor with the quantum number index defined above
                //supports up to 8 indices
    auto T = ITensor(i,j);//creates an ITensor with the index defined above
               //supports up to 8 indices

How to access and store data in ITensors.  See [[this page|classes/itensor]] for more nifty features.

    //        +------------------------+
    //>-------| (5) Set tensor data    |-------<
    //        +------------------------+

    T.set(i(2),j(2),3.14159);//sets value for given index
    println(T.real(i(2),j(2)));//prints 3.14159

    printData(T);//prints data in T

Contracting over indices with the `*` operator.

    //        +------------------------+
    //>-------|   (5)  Contraction     |-------<
    //        +------------------------+

    auto jj = Index("index jj",6,"MyIndexType",1);
    auto k  = Index("index k",3,"OtherIndexType",2);
    auto P  = ITensor(i,jj,k);
    auto result = T*P;//contracts over index "i" only


Note that both prime levels and indices must match to contract.


    return 0;//return value for C++ program

    }



  <div class="example_clicker">Show Full Code!</div>

    #include "all.h"

    using namespace itensor;

    int main()
    {
    auto i = Index("index i",4);//initializes index "i" with size 4 (i.e., four possible values)
    auto j = Index("index j",6,"MyIndexType",2);//another index with a custom type (third field) and prime level 2


    println(j.type());//prints "MyIndexType"...see code link above for more options!

    auto L = IQIndex("L",Index("L-",2),QN(-1),
                         Index("L0",4),QN( 0),
                         Index("L+",2),QN(+1));//Creates index separated into quantum numbers

    auto Q = IQTensor(L);
    auto T = ITensor(i,j);

    T.set(i(2),j(2),3.14159);
    println(T.real(i(2),j(2)));//prints 3.14159

    printData(T);//prints data in T

    auto jj = Index("index jj",6,"MyIndexType",1);
    auto k  = Index("index k",3,"OtherIndexType",2);
    auto P  = ITensor(i,jj,k);
    auto result = T*P;//contracts over index "i" only

    return 0;//return value for C++ program

    }

