# Creating a set of Site indices to use as a lattice #

To begin most calculations you need a set of lattice sites to define your Hilbert space.
Although the ITensor library defines a set of [[SiteSet|classes/siteset]] classes which automate
this for you, there could be a lot of reasons why you would want to do it yourself.
Below is a simple pattern you can use to create a set of site Indices and save them in an IndexSet,
a container for a set of indices used throughout ITensor.

    auto N = 100; //number of sites
    auto d = 2; //dimension of local Hilbert space of each site
    auto sites = IndexSet(N);
    for( auto n : range1(N) )
        sites(n) = Index(d,"Site,n="+str(n));

    //Now we can use these sites, for example, to make tensors
    //such as operators

    //For convenience, save the third index and its primed
    //version
    auto s3 = sites(3);
    auto s3P = prime(s3);

    auto sz3 = ITensor(s3,s3P);
    sz3.set(s3=1,s3P=1, 0.5);
    sz3.set(s3=2,s3P=2,-0.5);


Complete sample code:

    #include "itensor/all.h"

    using namespace itensor;

    int main()
        {
        auto N = 100; //number of sites
        auto d = 2; //dimension of local Hilbert space of each site
        auto sites = IndexSet(N);
        for( auto n : range1(N) )
            sites(n) = Index(d,"Site,n="+str(n));

        auto s3 = sites(3);
        auto s3P = prime(s3);
        auto sz3 = ITensor(s3,s3P);
        sz3.set(s3=1,s3P=1, 0.5);
        sz3.set(s3=2,s3P=2,-0.5);

        return 0;
        }

<br>
