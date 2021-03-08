using ITensors

let
  N = 100
  cutoff = 1E-8
  tau = 0.1
  ttotal = 5.0

  # Compute the number of steps to do
  Nsteps = Int(ttotal/tau)

  # Make an array of 'site' indices
  s = siteinds("S=1/2",N;conserve_qns=true)

  # Make gates (1,2),(2,3),(3,4),...
  gates = ITensor[]
  for j=1:N-1
    s1 = s[j]
    s2 = s[j+1]
    hj =       op("Sz",s1) * op("Sz",s2) +
         1/2 * op("S+",s1) * op("S-",s2) +
         1/2 * op("S-",s1) * op("S+",s2)
    Gj = exp(-1.0im * tau/2 * hj)
    push!(gates,Gj)
  end
  # Include gates in reverse order too
  # (N,N-1),(N-1,N-2),...
  append!(gates,reverse(gates))

  # Function that measures and prints <Sz> on center site c
  function measure_Sz(psi,t)
    s = siteinds(psi)
    c = div(length(psi),2)
    orthogonalize!(psi,c)
    Sz = scalar(dag(prime(psi[c],"Site"))*op("Sz",s[c])*psi[c])
    println("$t $(real(Sz))")
  end

  # Initialize psi to be a product state (alternating up and down)
  psi = productMPS(s, n -> isodd(n) ? "Up" : "Dn")

  measure_Sz(psi,0.0)

  # Do the time evolution by applying the gates
  # for Nsteps steps
  t = 0.0
  for step=1:Nsteps
    psi = apply(gates, psi; cutoff)
    t += tau
    measure_Sz(psi,t)
  end

  return
end
