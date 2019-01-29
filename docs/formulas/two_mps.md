
# Operator Matrix Elements Involving Two MPS

Say we have two MPS wavefunctions, @@|\psi\!\rangle@@ and @@|\phi\rangle@@,
and that we wish to compute @@\langle\phi|O_i O_j|\psi\rangle@@ for some 
local operators @@O_i@@ and @@O_j@@. We can do this as follows:

    int i = 4;
    int j = 10;
    auto op_i = sites.op("Sz",i);
    auto op_j = sites.op("Sz",j);

    auto M = psi.A(1)*dag(prime(phi.A(1),"Link"));
    for(auto n : range1(2,N))
        {
        M *= psi.A(n);
        if(n == i)
            {
            M *= op_i*dag(prime(phi.A(i)));
            }
        else if(n == j)
            {
            M *= op_j*dag(prime(phi.A(j)));
            }
        else
            {
            M *= dag(prime(phi.A(n),"Link"));
            }
        }
    auto result = M.real();

Note: if @@i@@ or @@j@@ are equal to 1, one must modify the line in the
code above where @@M@@ is first defined.
Note: if a complex valued result is expected, change the last line to use `M.cplx();`.

