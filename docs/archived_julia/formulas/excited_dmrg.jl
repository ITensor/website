using ITensors

let
  N = 20

  sites = siteinds("S=1/2",N)

  h = 4.0
  
  weight = 10*h # use a large weight
                # since gap is expected to be large


  #
  # Use the AutoMPO feature to create the
  # transverse field Ising model
  #
  # Factors of 4 and 2 are to rescale
  # spin operators into Pauli matrices
  #
  ampo = AutoMPO()
  for j=1:N-1
    ampo += -4,"Sz",j,"Sz",j+1
  end
  for j=1:N
    ampo += -2*h,"Sx",j;
  end
  H = MPO(ampo,sites)


  #
  # Make sure to do lots of sweeps
  # when finding excited states
  #
  sweeps = Sweeps(30)
  maxdim!(sweeps,10,10,10,20,20,40,80,100,200,200)
  cutoff!(sweeps,1E-8)
  noise!(sweeps,1E-6)

  #
  # Compute the ground state psi0
  #
  psi0_init = randomMPS(sites,2)
  energy0,psi0 = dmrg(H,psi0_init,sweeps)

  println()

  #
  # Compute the first excited state psi1
  # (Use ground state psi0 as initial state 
  #  and as a 'penalty state')
  #
  psi1_init = psi0
  energy1,psi1 = dmrg(H,[psi0],psi1_init,sweeps; weight)

  # Check psi1 is orthogonal to psi0
  @show inner(psi1,psi0)


  #
  # The expected gap of the transverse field Ising
  # model is given by Eg = 2*|h-1|
  #
  # (The DMRG gap will have finite-size corrections.)
  #
  println("DMRG energy gap = ",energy1-energy0);
  println("Theoretical gap = ",2*abs(h-1));

  println()

  #
  # Compute the second excited state psi2
  # (Use ground state psi0 as initial state 
  #  and [psi0,psi1] as 'penalty states')
  #
  psi2_init = psi0
  energy2,psi2 = dmrg(H,[psi0,psi1],psi2_init,sweeps;weight)

  @show inner(psi2,psi0)
  @show inner(psi2,psi1)

  return
end
