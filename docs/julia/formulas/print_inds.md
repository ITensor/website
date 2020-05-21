# Print only the indices of an ITensor

Sometimes the printout of an ITensor can be rather large, whereas you
might only want to see its indices. For these cases, just wrap the
ITensor in the function `inds` like this:

    @show inds(T)

or this

    println("T inds = ",inds(T))


