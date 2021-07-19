using ITensors

let
  N = 100

  # Make an array of N Index objects with alternating
  # "S=1/2" and "S=1" tags on odd versus even sites
  # (The first argument n->isodd(n) ... is an 
  # on-the-fly function mapping integers to strings)
  sites = siteinds(n->isodd(n) ? "S=1/2" : "S=1",N)

  # Couplings between spin-half and
  # spin-one sites:
  Jho = 1.0 # half-one coupling
  Jhh = 0.5 # half-half coupling
  Joo = 0.5 # one-one coupling

  ampo = AutoMPO()
  for j=1:N-1
    ampo += 0.5*Jho,"S+",j,"S-",j+1
    ampo += 0.5*Jho,"S-",j,"S+",j+1
    ampo += Jho,"Sz",j,"Sz",j+1
  end
  for j=1:2:N-2
    ampo += 0.5*Jhh,"S+",j,"S-",j+2
    ampo += 0.5*Jhh,"S-",j,"S+",j+2
    ampo += Jhh,"Sz",j,"Sz",j+2
  end
  for j=2:2:N-2
    ampo += 0.5*Joo,"S+",j,"S-",j+2
    ampo += 0.5*Joo,"S-",j,"S+",j+2
    ampo += Joo,"Sz",j,"Sz",j+2
  end
  H = MPO(ampo,sites)

  sweeps = Sweeps(10)
  maxdim!(sweeps,10,10,20,40,80,100,140,180,200)
  cutoff!(sweeps,1E-8)

  psi0 = randomMPS(sites,4)

  energy,psi = dmrg(H,psi0,sweeps)

  return
end
