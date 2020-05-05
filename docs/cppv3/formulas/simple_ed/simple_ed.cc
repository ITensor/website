#include "itensor/all.h"
#include "itensor/util/print_macro.h"

using namespace itensor;

int main()
{
int N = 6;
Real tau = 10.;
int Npass = 4;

auto sites = SpinHalf(N);

//inds(SiteSet) -> IndexSet is a convenient function
//for extracting the indices of a SiteSet
auto indices = inds(sites);

//Make a random initial wavefunction psi with 0 magnetization
//psi is an ITensor with all of the site indices in "sites";
auto psi = randomITensor(QN({"Sz",0}),indices);

//Make the Hamiltonian as an MPO
auto ampo = AutoMPO(sites);
for( auto j : range1(N-1) )
    {
    ampo += 0.5,"S+",j,"S-",j+1;
    ampo += 0.5,"S-",j,"S+",j+1;
    ampo +=     "Sz",j,"Sz",j+1;
    }
auto Hmpo = toMPO(ampo);

//Make a single ITensor out of the MPO
auto H = Hmpo(1);
for(auto j : range1(2,N)) H *= Hmpo(j);

//Create expH = exp(-tau*H)
auto expH = expHermitian(H,-tau);

//Apply expH to psi a few times to project into ground state
auto gs = psi; //initialize to psi
for(int n = 1; n <= Npass; ++n)
    {
    gs *= expH;
    gs.noPrime();
    gs /= norm(gs);
    }
Print(gs);

//Compute the ground state energy
auto E0 = elt(prime(dag(gs))*H*gs);
Print(E0);

//Compute the variance <H^2>-<H>^2 to check that gs is
//an eigenstate. The result "var" should be very small.
auto H2 = multSiteOps(H,H);
auto var = elt(prime(dag(gs))*H2*gs)-(E0*E0);
Print(var);

return 0;
}
