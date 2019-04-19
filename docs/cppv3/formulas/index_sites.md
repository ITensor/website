# Creating a set of Site indices to use as a lattice #

To begin most calculations you need a set of lattice sites to define your Hilbert space.
Although the ITensor library defines a set of [[SiteSet|classes/siteset]] classes which automate
this for you, there could be a lot of reasons why you would want to do it yourself.
Below is a simple pattern you can use to create a set of site Indices and save them in a vector.

    int N = 100; //number of sites
    int d = 2; //dimension of local Hilbert space of each site
    auto site = vector<Index>(N+1); //convenient for these to be 1-indexed
    for(int j = 1; j <= N; ++j)
        {
        site.at(j) = Index(d,"Site,n="+str(j));
        }

    //Now we can use these sites, for example, to make tensors
    //such as operators

    auto sz3 = ITensor(site[3],prime(site[3]));
    sz.set(site[3]=1,prime(site[3]=1, 0.5);
    sz.set(site[3]=2,prime(site[3]=2,-0.5);


Complete sample code:

    #include "itensor/all.h"

    using namespace itensor;
    using std::vector;

    int main()
        {
        int N = 100; //number of sites
        int d = 2; //dimension of local Hilbert space of each site
        auto site = vector<Index>(N+1); //convenient for these to be 1-indexed
        for(int j = 1; j <= N; ++j)
            {
            site.at(j) = Index(d,"Site,n="+str(j));
            }

        auto sz3 = ITensor(site[3],prime(site[3]));
        sz.set(site[3]=1,prime(site[3]=1, 0.5);
        sz.set(site[3]=2,prime(site[3]=2,-0.5);
        PrintData(sz3);

        return 0;
        }

<br>
