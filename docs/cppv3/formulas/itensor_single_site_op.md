# Making a single-site operator (no quantum numbers) 

Measuring the properties of a wavefunction (for example, an MPS) usually
involves expectation values of single-site operators or  products and sums of such operators.

Say we have an Index s representing a particular site. We could have created s (thinking here of spin 1/2 or a hardcore boson):

    auto s = Index(2,"Site");

Or we could obtain s from a set of Site indices already created earlier (see the recipe for [[creating a set of Site indices|index_sites]]).

Once we have this site index, we can make various operators as follows:

    Index sP = prime(s); //convenient to save this as a different variable

    auto sz = ITensor(s,sP);
    sz.set(s=1,sP=1,+0.5);
    sz.set(s=2,sP=2,-0.5);

    auto sx = ITensor(s,sP);
    sx.set(s=1,sP=2,0.5);
    sx.set(s=2,sP=1,0.5);

We can even get fancy and create a 'factory' function which takes our site and an operator-name string and returns the operator we want:

    ITensor
    myOp(Index s, string name)
        {
        Index sP = prime(s);
        auto res = ITensor(s,sP); //res is short for result

        if(name == "Sz")
            {
            res.set(s=1,sP=1,+0.5);
            res.set(s=2,sP=2,-0.5);
            }
        else
        if(name == "Sx")
            {
            res.set(s=1,sP=2,0.5);
            res.set(s=2,sP=1,0.5);
            }
        else
            {
            Print(name);
            Error("Operator name not recognized.");
            }

        return res;
        }

Finally, note that this 'operator factory' feature is actually built into the 
[[SiteSet|classes/siteset]] classes which automate the creation
of sites and operators for you. But of course there are always reasons you may 
want to get your hands dirty and create these operators yourself.



Complete sample code:


    #include "itensor/all.h"

    using namespace itensor;
    using std::string;

    ITensor
    myOp(Index s, string name)
        {
        Index sP = prime(s);
        ITensor res(s,sP); //res is short for result

        if(name == "Sz")
            {
            res.set(s=1,sP=1,+0.5);
            res.set(s=2,sP=2,-0.5);
            }
        else
        if(name == "Sx")
            {
            res.set(s=1,sP=2,0.5);
            res.set(s=2,sP=1,0.5);
            }
        else
            {
            Print(name);
            Error("Operator name not recognized.");
            }

        return res;
        }

    int 
    main(int argc, char* argv[])
        {
        const int d = 2;

        auto s1 = Index(d,"Site,s1");
        auto s2 = Index(d,"Site,s2");

        ITensor sz1 = myOp(s1,"Sz");
        ITensor sz2 = myOp(s2,"Sz");
        ITensor sx1 = myOp(s1,"Sx");

        PrintData(sz1);
        PrintData(sz2);
        PrintData(sx1);

        return 0;
        }
