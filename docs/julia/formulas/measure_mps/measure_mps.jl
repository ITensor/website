for j=1:length(psi)
  orthogonalize!(psi,j)
  
  s = siteind(psi,j)
  szj = scalar(psi[j]*op(s,"Sz")*dag(prime(psi[j],s)))
  
  println("<Sz_$j> = $szj")
end
