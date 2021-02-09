using ITensors

let
# Define Hilbert space of N spin-one sites
N = 100
sites = siteinds("S=1",N; conserve_qns=true)

# Create 1d Heisenberg Hamiltonian
ampo = AutoMPO()
for j = 1:N-1
  ampo += 0.5,"S+",j,"S-",j+1
  ampo += 0.5,"S-",j,"S+",j+1
  ampo +=     "Sz",j,"Sz",j+1
end

H = MPO(ampo,sites)

# Choose initial wavefunction
# to be a product state
state = [isodd(n) ? "Up" : "Dn" for n in 1:N]
psi0 = productMPS(sites,state)
@show flux(psi0)

# Perform 5 sweeps of DMRG
sweeps = Sweeps(5)
# Specify max number of states kept each sweep
maxdim!(sweeps,50,50,100,100,200)

# Run the DMRG algorithm
energy,psi = dmrg(H,psi0,sweeps)

# Continue to analyze wavefunction afterward 
@show inner(psi,H,psi) # <psi|H|psi>

for j=1:N
  # Make site j the MPS "orthogonality center"
  orthogonalize!(psi,j)
  # Measure magnetization
  Szj = scalar(psi[j]
               * op("Sz",sites[j])
               * dag(prime(psi[j],"Site")))
  println("Sz_$j = $Szj")
end
end
