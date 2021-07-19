using ITensors

let
  N = 10
  sites = siteinds("S=1",N)

  ampo = AutoMPO()
  for j=1:N-1
    ampo += (0.5,"S+",j,"S-",j+1)
    ampo += (0.5,"S-",j,"S+",j+1)
    ampo += ("Sz",j,"Sz",j+1)
  end
  H = MPO(ampo,sites)


  sweeps = Sweeps(5) # number of sweeps is 5
  maxdim!(sweeps,10,20,100,100,200) # gradually increase states kept
  cutoff!(sweeps,1E-10) # desired truncation error

  psi0 = randomMPS(sites,2)

  energy,psi = dmrg(H,psi0,sweeps)

  for j=1:length(psi)
    orthogonalize!(psi,j)
    s = siteind(psi,j)
    szj = scalar(psi[j]*op(s,"Sz")*dag(prime(psi[j],s)))
    println("<Sz_$j> = $szj")
  end

  return
end
