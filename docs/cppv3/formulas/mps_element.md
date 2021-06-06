# Obtaining Elements of a Tensor Represented as an MPS

A matrix product state (MPS) or tensor train (TT) is a format
for representing a large tensor having N indices in terms of
N smaller tensors. Given an MPS represeting a tensor @@T@@
we can obtain a particular element @@T^{s_1 s_2 s_3 \cdots s_N}@@ of that tensor using 
code similar to the following code below.

In this code we will obtain the element @@T^{1,2,1,1,2,1,2,2,2,1}@@ of the tensor @@T@@
which is (implicitly) defined by the MPS `psi`:

    #include "itensor/all.h"
    #include "itensor/util/print_macro.h"
    using namespace itensor;

    int main()
        {

        //Make a random MPS with N=10 indices (10 sites)
        //with each physical index of dimension 2
        //and each link index (bond dimension) of dimension 4
        auto N = 10;
        auto s = SiteSet(N,2);
        auto chi = 4;
        auto psi = randomMPS(s,chi);

        //Make an array of integers of the element we 
        //want to obtain
        auto el = std::vector<int>{{1,2,1,1,2,1,2,2,2,1}};

        auto T = ITensor(1.);
        for(auto j : range1(N))
            {
            T *= (psi(j)*setElt(s(j)=el[j-1]));
            }
        auto val = elt(T);

        //"val" is the element we wanted to obtain:
        Print(val);

        return 0;
        }
