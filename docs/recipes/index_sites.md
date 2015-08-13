# Creating a set of Site indices to use as a lattice #

To begin most calculations you need a set of lattice sites to define your Hilbert space.
Although the ITensor Library defines a set of [[SiteSet|classes/siteset]] classes which automate
this for you, there could be a lot of reasons why you would want to do it yourself.
Below is a simple pattern you can use to create a set of site Indices and save them in a vector.

    int N = 100; //number of sites
    int d = 2; //dimension of local Hilbert space of each site
    vector<Index> site(N+1); //convenient for these to be 1-indexed
    for(int j = 1; j <= N; ++j)
        {
        site.at(j) = Index(nameint("s",j),d,Site);
        }

    //Now we can use these sites, for example, to make tensors
    //such as operators

    ITensor sz3(site[3],prime(site[3]));
    sz(site[3](1),prime(site[3])(1)) =  0.5;
    sz(site[3](2),prime(site[3])(2)) = -0.5;

A few comments on the above code are in order. The function `nameint` is convenience function we provide
which simply takes a string and an integer and makes a string with the integer appended. So for example:

    string myname = nameint("mysite_",7);
    Print(myname); //prints "mysite_7"

Also, in the Index constructor, after the name and dimension of each Index we passed the `Site` flag.
This flags all of our site indices as having an `IndexType` of `Site` (accessible through the `.type()` accessor
on a given Index e.g. `site[4].type() == Site`). Later this allows useful idioms such as priming only the Site indices of a certain tensor
but not of the Link indices, etc. (For more info see the docs on class [[Index|classes/index]].)


Complete sample code:

    #include "itensor.h"

    using namespace itensor;
    using std::vector;

    int main()
        {
        int N = 100; //number of sites
        int d = 2; //dimension of local Hilbert space of each site
        vector<Index> site(N+1); //convenient for these to be 1-indexed
        for(int j = 1; j <= N; ++j)
            {
            site.at(j) = Index(nameint("s",j),d,Site);
            }

        //Now we can use these sites, for example, to make tensors
        //such as operators

        ITensor sz3(site[3],prime(site[3]));
        sz(site[3](1),prime(site[3])(1)) =  0.5;
        sz(site[3](2),prime(site[3])(2)) = -0.5;

        return 0;
        }

<br>
