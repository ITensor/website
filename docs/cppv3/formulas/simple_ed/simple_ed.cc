#include "itensor/all.h"

using namespace itensor;
using std::vector;

int main()
{
int N = 6;
Real tau = 10.;
int Npass = 4;

auto sites = SpinHalf(N);

//Make initial wavefunction psi a random state
auto indices = vector<Index>();
for(auto j : range1(N)) indices.push_back(sites(j));
//psi is an ITensor with all of the site indices in "sites";
auto psi = ITensor(indices);
//randomize the elements of psi
randomize(psi);

//Make the Hamiltonian as a single ITensor
ITensor H;
for(auto b : range1(N-1))
    {
    auto term = sites.op("Sz",b)*sites.op("Sz",b+1);
    term += 0.5*sites.op("S+",b)*sites.op("S-",b+1);
    term += 0.5*sites.op("S-",b)*sites.op("S+",b+1);
    for(auto j : range1(b-1)) term *= sites.op("Id",j);
    for(auto j : range1(b+2,N)) term *= sites.op("Id",j);
    H += term;
    }

//Create eH = exp(-tau*H)
auto eH = expHermitian(H,-tau);

//Apply eH to psi a few times to project into ground state
auto gs = psi; //initialize to psi
for(int n = 1; n <= Npass; ++n)
    {
    gs = (eH*gs).noprime();
    gs /= norm(gs);
    }
Print(gs);

//Compute the ground state energy
auto E0 = (prime(gs)*H*gs).real();
Print(E0);

//Compute the variance to check that gs is
//an eigenstate. The result "var" should be very small.
auto H2 = multSiteOps(H,H);
auto var = (prime(gs)*H2*gs).real()-E0*E0;
Print(var);

return 0;
}
