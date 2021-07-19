using ITensors
let
  s = siteinds("S=1/2",6)
  psi = randomMPS(s,2)
  cpsi = deepcopy(psi)
  G = randomITensor(s[3],s[4],s[3]',s[4]')
  orthogonalize!(psi,3)

  wf = psi[3]*psi[4]
  wf *= G
  noprime!(wf)
  U,S,V = svd(wf,inds(psi[3]),cutoff=1E-8)
  psi[3] = U
  psi[4] = S*V

  @show psi
  @show inner(psi,cpsi)
  @show inner(cpsi,cpsi)
  return
end
