using ITensors

let
  Ny = 6
  Nx = 12

  N = Nx*Ny

  sites = siteinds("S=1/2", N;
                   conserve_qns = true)

  # Obtain an array of LatticeBond structs
  # which define nearest-neighbor site pairs
  # on the 2D square lattice (wrapped on a cylinder)
  lattice = square_lattice(Nx, Ny; yperiodic = false)

  # Define the Heisenberg spin Hamiltonian on this lattice
  ampo = AutoMPO()
  for b in lattice
    ampo .+= 0.5, "S+", b.s1, "S-", b.s2
    ampo .+= 0.5, "S-", b.s1, "S+", b.s2
    ampo .+=      "Sz", b.s1, "Sz", b.s2
  end
  H = MPO(ampo,sites)

  state = [isodd(n) ? "Up" : "Dn" for n=1:N]
  # Initialize wavefunction to a random MPS
  # of bond-dimension 10 with same quantum
  # numbers as `state`
  psi0 = randomMPS(sites,state,20)

  sweeps = Sweeps(10)
  maxdim!(sweeps,20,60,100,100,200,400,800)
  cutoff!(sweeps,1E-8)
  @show sweeps

  energy,psi = dmrg(H,psi0,sweeps)

  return
end
