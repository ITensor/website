using ITensors

let

  #
  # Obtain an optimized MPS
  # of spinles fermions using
  # the DMRG algorithm
  #
  N = 30
  s = siteinds("Fermion",N; conserve_qns=true)
  t = 1.0
  V = 2.0

  a = AutoMPO()
  for j=1:N-1
    a += -t,"Cdag",j,  "C",j+1
    a += -t,"Cdag",j+1,"C",j
    a += V,"N",j,"N",j+1
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

  Ci = correlator(psi,"Cdag","C")

  # 
  # Compute two-point correlation
  # function <c^\dagger_i c_j> using
  # efficient MPS techniques:
  #
  orthogonalize!(psi,1)
  C = zeros(N,N)
  L = ITensor(1.)
  for i=1:N
    Li = L*psi[i]*op("Cdag",s,i)*dag(prime(psi[i]))
    LiF = Li
    for j=i+1:N
      lind = commonind(psi[j],LiF)
      LiF *= psi[j]
      cij = LiF*op("C",s,j)*dag(prime(prime(psi[j],"Site"),lind))
      C[i,j] = scalar(cij)
      C[j,i] = conj(C[i,j])
      LiF *= op("F",s,j)*dag(prime(psi[j]))
    end
    L *= psi[i]*dag(prime(psi[i],"Link"))
  end

  # Fill in diagonal elements
  for i=1:N
    orthogonalize!(psi,i)
    C[i,i] = scalar(psi[i]*op("N",s,i)*dag(prime(psi[i],"Site")))
  end

  println("C = ")
  display(C);println()

  if N <= 30
    # 
    # Alternatively, compute the
    # correlation function using AutoMPO
    # to make an MPO for each i,j
    # (This is much slower than
    # using the MPS techniques above)
    #
    Ccheck = zeros(N,N)
    @time begin
    for i=1:N,j=i:N
      a = AutoMPO()
      a += "Cdag",i,"C",j
      Ccheck[i,j] = inner(psi,MPO(a,s),psi)
      Ccheck[j,i] = conj(Ccheck[i,j])
    end
    end
    println("Ccheck = ")
    display(Ccheck);println()

    @show norm(C-Ccheck)
    @show norm(Ci-Ccheck)
  end

  return
end
