# Measure Local Properties of an MPS

## Example of measuring "Sz"

For matrix product states (MPS) representing the wavefunction of a quantum
system, a common task is to measure expected values of local observables acting on each site or physical degree of freedom. To see how to do this in ITensor,
let's start from the following example of measuring the `"Sz"` operator
for each site of an MPS `psi`:


    for j=1:length(psi)
      orthogonalize!(psi,j)
  
      s = siteind(psi,j)
      val = scalar(psi[j]*op(s,"Sz")*dag(prime(psi[j],s)))
  
      println("$j $val")
    end

Now let's discuss each part of the code above. The for loop runs from 1 up to the number of sites of the MPS (number of tensors of the MPS). 

The next line `orthogonalize!(psi,j)` shifts the _orthogonality center_ of the MPS to site number `j`. Practically speaking, this step is what lets us only use the tensor `psi[j]` when doing the measurement, ignoring the other MPS tensors. But to be more precise, we are not actually ignoring the other MPS tensors, it's just that because `orthogonalize!` brings the MPS into a canonical form, the other MPS tensors obey left- and right-canonical conditions so would cancel anyway even if we included them in the expectation value calculation.

The line `s = siteind(psi,j)` retrieves the site, or physical index of the jth MPS tensor. If we already have access to this Index such as through an array obtained from the `siteinds` function then we could also obtain it that way.

The line

    val = scalar(psi[j]*op(s,"Sz")*dag(prime(psi[j],s)))

actually performs the computation of the expected value of the operator "Sz". The call to `op(s,"Sz")` makes the ITensor for the "Sz" operator, where here we are assuming that the Index `s` carries a physical tag type such that "Sz" is defined for this Index. (Examples could include the tag "S=1/2" or the tag "Fermion".) The returned operator has two indices: `s` and `s'`. Contracting the operator with `psi[j]` contracts over the Index `s`. Then contracting with `dag(prime(psi[j],s))` contracts over `s'` and the two bond indices of the MPS conecting to the jth MPS tensor. Finally, the call to scalar converts the resulting scalar-valued ITensor into a number which is stored into the variable `val` (either Float64 or ComplexF64).

Finally, the line `println("$j $val")` just prints the site number and the variable `val`.


