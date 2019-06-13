#include "itensor/all.h"

using namespace itensor;
using std::vector;

int 
main()
  {
  // Create the sites
  auto N = 20;
  auto s = SpinHalf(N,{"ConserveQNs=",false});

  // Create the gates
  auto tau = 0.1; // Time step
  auto G = vector<ITensor>(N);
  for(auto j : range1(N-1))
    {
    G[j] = expHermitian(op(s,"Sx",j)*op(s,"Sx",j+1),-tau);
    }

  // Split up the gates
  auto A = vector<ITensor>(N);
  auto B = vector<ITensor>(N);
  for(auto j : range1(N-1))
    {
    auto [Aj,Bj] = factor(G[j],{s(j),prime(s(j))});
    A[j] = Aj;
    B[j] = Bj;
    }

  // Some temporary internal indices
  auto t = vector<Index>(N+1);
  for(auto j : range1(N))
    {
    t[j] = sim(s(j));
    }

  // Replace internal indices
  // so that the correct indices contract
  for(auto j : range1(2,N-1))
    {
    B[j-1] *= delta(prime(s(j)),t[j]);
    A[j] *= delta(s(j),t[j]);
    }

  // Create and store the MPO tensors
  auto M = MPO(N);
  M.set(1,A[1]);
  for(auto j : range1(2,N-1))
    {
    M.set(j,B[j-1]*A[j]);
    }
  M.set(N,B[N-1]);

  ///////////////////////////////////////////////
  //
  // As a test, apply this MPO to a state
  // and compare to applying the gates
  //

  // Create a starting state
  auto init = InitState(s);
  for(auto j : range1(N))
    {
    init.set(j, "Up"); 
    }
  auto psi = MPS(init);

  // Apply our MPO to the starting state
  auto Mpsi = applyMPO(M,psi);
  
  // Now compare to applying the gates
  auto Gpsi = psi;

  // Put the orthogonality center at position 1
  Gpsi.position(1);
  for(auto j : range1(1,N-1))
    {
    auto phi = Gpsi(j)*Gpsi(j+1)*G[j];
    phi.noPrime();
    auto [U,S,V] = svd(phi,inds(Gpsi(j)));
    Gpsi.set(j,U);
    Gpsi.set(j+1,S*V);
    }

  PrintData(inner(Mpsi,Mpsi));
  PrintData(inner(Gpsi,Gpsi));
  PrintData(inner(Gpsi,Gpsi));

  return 0;
  }
