
# Operator Matrix Elements Involving Two MPS

Say we have two MPS wavefunctions, @@|\psi\!\rangle@@ and @@|\phi\rangle@@,
and that we wish to compute @@\langle\phi|O_i O_j|\psi\rangle@@ for some 
local operators @@O_i@@ and @@O_j@@. We can do this as follows:

    int N = 20;
    auto sites = SpinHalf(N);
    auto state = InitState(sites,"Up");
    auto psi = randomMPS(state);
    auto phi = randomMPS(state);

    int i = 4;
    int j = 10;
    auto op_i = sites.op("Sz",i);
    auto op_j = sites.op("Sz",j);

    auto phidag = dag(phi);

    auto M = psi(1)*phidag(1);
    for(auto n : range1(2,N))
        {
        M *= psi(n);
        if(n == i)
            {
            M *= op_i*prime(phidag(i),"Site");
            }
        else if(n == j)
            {
            M *= op_j*prime(phidag(j),"Site");
            }
        else
            {
            M *= phidag(n);
            }
        }
    auto result = elt(M);

Note: if @@i@@ or @@j@@ are equal to 1, one must modify the line in the
code above where @@M@@ is first defined.
Note: if a complex valued result is expected, change the last line to use `eltC(M);`.

