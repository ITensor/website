#include "itensor/all.h"

using namespace itensor;

int main()
{
int N = 6;
Real ttotal = 1.5;

auto sites = SpinHalf(N);

auto state = InitState(sites);
for(auto j : range1(N))
    {
    state.set(j,j%2==1?"Up":"Dn");
    }
auto mps = MPS(state);

auto psi = mps.A(1);
for(auto j : range1(2,N)) psi *= mps.A(j);

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

auto eH = expHermitian(H,-1_i*ttotal);

auto phi = eH*psi;
Print(phi);
phi.noprime();

PrintData(dag(phi)*psi);

//auto gP = expHermitian(H,-10.);
//auto gs = (gP*psi).noprime();
//Print(gs);
//gs /= norm(gs);
//Print(gs);

//auto E0 = (prime(gs)*H*gs).real();
//Print(E0);
//auto gst = (eH*gs).noprime();
//auto o = (gst*gs).cplx();
//Print(o);
//Print(cos(E0));
//Print(sin(E0));

return 0;
}
