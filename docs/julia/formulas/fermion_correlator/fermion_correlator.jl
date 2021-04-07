# 
# Compute two-point correlation
# function <c^\dagger_i c_j> using
# efficient MPS techniques:
#
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
