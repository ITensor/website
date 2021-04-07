using ITensors

let

  N = 30
  s = siteinds("Fermion",N; conserve_qns=true)
  t = 1.0

  a = AutoMPO()
  for j=1:N-1
    a += -t,"Cdag",j,  "C",j+1
    a += -t,"Cdag",j+1,"C",j
  end
  H = MPO(a,s)

  Nf = div(N,2)
  psi0 = productMPS(s,n->isodd(n) ? "Occ" : "Emp")
  @show flux(psi0)
  @assert flux(psi0) == QN("Nf",Nf,-1)

  sweeps = Sweeps(10)
  maxdim!(sweeps,10,20,40,80,160)
  noise!(sweeps,1E-4,1E-6,1E-8,1E-12)
  cutoff!(sweeps,1E-10)

  energy,psi = dmrg(H,psi0,sweeps)

  # 
  # Using free fermion techniques
  #
  h0 = zeros(N,N)
  for j=1:N-1
    h0[j,j+1] = -t
    h0[j+1,j] = -t
  end
  _, u0 = eigen(h0)
  ϕ = transpose(u0[:,1:Nf])
  rho = ϕ'*ϕ
  println("rho = ")
  display(rho);println()

  # 
  # Using AutoMPO
  #
  Mx = zeros(N,N)
  @time begin
  for i=1:N,j=i:N
    a = AutoMPO()
    a += "Cdag",i,"C",j
    Mx[i,j] = inner(psi,MPO(a,s),psi)
    Mx[j,i] = Mx[i,j]
  end
  end
  println("Mx = ")
  display(Mx);println()

  # 
  # Using MPS techniques
  #
  M = zeros(N,N)
  L = ITensor(1.)
  for i=1:N
    Li = L*psi[i]*op("Cdag",s,i)*dag(prime(psi[i]))
    LiF = Li
    for j=i+1:N
      lind = commonind(psi[j],LiF)
      LiF *= psi[j]
      cij = LiF*op("C",s,j)*dag(prime(prime(psi[j],"Site"),lind))
      M[i,j] = scalar(cij)
      M[j,i] = M[i,j]
      LiF *= op("F",s,j)*dag(prime(psi[j]))
    end
    L *= psi[i]*dag(prime(psi[i],"Link"))
  end

  # Fill in diagonal elements
  for i=1:N
    orthogonalize!(psi,i)
    M[i,i] = scalar(psi[i]*op("N",s,i)*dag(prime(psi[i],"Site")))
  end
  println("M = ")
  display(M);println()

  @show norm(Mx-M)


  @show norm(rho-Mx)


  return
end
