#Measure the properties of an MPS wavefunction#

Here we'll learn how to measure some properties of the
Heisenberg model wavefunction by adding to the code from the [[previous example|recipes/basic_dmrg]].
Essentially we need three pieces to take an expectation value of some property:  
the operator corresponding to that property, the wavefunction, and a way to do the inner
product of the operator with the wavefunction.

For example, consider trying to measure the z-component of
the spin on some site `j` in the Heisenberg chain.  
This operator is a method of the `SpinOne::Model model(N);` class
that we defined last time, and can be represented by an ITensor:

<code>
ITensor szj_op = model.sz(j);
</code>

Likewise there are operators for the site `j` spin raising (S+) and lowering operators (S-),
methods `sp(j)` and `sm(j)`, respectively.
Now there is an efficient way to take the inner product of these local operators with the MPS
wavefunction. To do this, we must first call the function

<code>
psi.position(j);
</code>

_This step is absolutely vital_.  It tells the MPS wavefunction to put all the information
about the amplitudes of the various spin occupations into the site at `j`.
Without which, measuring `sz(j)` would give errors.  Getting these amplitudes is
then very simple, and they will form the ket part of our Dirac "bra-ket" inner product:

<code>
ITensor ket = psi.AA(j);
</code>

After calling `psi.position(j)`, all the `psi.AA(j+n)` for `n != 0` are basis functions
for the sites `j+n`.  As basis functions, these `psi.AA(j+n)` do
not have amplitude information; only the `psi.AA(j)` does.  That is why it is vital to call 
`psi.position(j)` before doing a measurement at site `j`.

To get the bra part of the Dirac bra-ket, think about the ket as a column vector, the operator
as a matrix, and the bra as a row vector.  We get the bra by turning the ket into a row vector and conjugating
any imaginary parts.  The way we do this is simple:

<code>
ITensor bra = conj(primesite(ket));
</code>

The `primesite` function is what turns the ket into a row vector, and `conj` does the conjugation.
(For the Heisenberg model, there isn't a need for the conjugation, though.)
Now we are ready to measure the expectation value of `sz(j)` by using the inner product function `Dot`:

<code>
Real szj = Dot(bra, szj_op*ket);
</code> 

Let's do another, more complicated measurement that will require our kets to be representing information
on two sites `j` and `j+1`.  The vector product S(j) dot S(j+1) will do just fine.  In terms of the 
z-component and raising and lowering operators, S(j) dot S(j+1) = sz(j)*sz(j+1) + 0.5*( sp(j)*sm(j+1) + sp(j+1)*sm(j) ).
For example, one of the operators we'll need is

<code>
ITensor spm_op = model.sp(j)*model.sm(j+1);
</code>

To represent the wavefunction for two sites, we simply call the `bondTensor` method of the wavefunction:

<code>
ITensor bondket = psi.bondTensor(j); 
</code>

`psi.bondTensor(j)` is analogous to `psi.AA(j)`, except that 
`bondTensor` encodes bond information between `j` and `j+1`, so long as `psi.position(j)` has been called previously.
The `bondbra` is made the same as the `bra` from earlier:

<code>
ITensor bondbra = conj(primesite(bondket));
</code>

And expectation values are realized in the same way:

<code>
Real spm = 0.5*Dot(bondbra, spm_op*bondket);
</code>

Below you'll find a complete code for measuring properties of the MPS wavefunction.  
The code writes to file a list of Sz(j) and S(j) dot S(j+1) for plotting.


<code>
#define THIS_IS_MAIN
#include "core.h"
#include "hams.h"
using boost::format;
using std::cout;
using std::cerr;
using std::endl;

int main(int argc, char* argv[])
{
    int N = 100;
    int nsweep = 5;
    int minm = 1;
    int maxm = 100;
    Real cutoff = 1E-5;

    SpinOne::Model model(N);

    MPO H = SpinOne::Heisenberg(model)();

    InitState initState(N);
    for(int i = 1; i <= N; ++i) initState(i) = (i%2==1 ? model.Up(i) : model.Dn(i));

    MPS psi(model,initState);

    cout << format("Initial energy = %.5f\n")%psiHphi(psi,H,psi);

    Sweeps sweeps(Sweeps::ramp_m,nsweep,minm,maxm,cutoff);
    Real En = dmrg(psi,H,sweeps);

    cout << format("\nGround State Energy = %.10f\n")%En;

    //
    //MEASURING SPIN
    //

    Vector Sz(N); //vector of z-components of spin for each site
    Sz = 0.0; //initialize
    std::ofstream szf("Sz"); //file to write Szj info to

    Vector SdotS(N-1); //Sj dot Sj+1 by means of Splus and Sminus
    SdotS = 0.0;
    std::ofstream sdots("SdotS"); //file to write SdotS information to

    Real sumSdotS = 0.0; //also sum up the SdotS and see if it's equal to our ground state energy

    for(int j=1; j<=N; j++) {
        psi.position(j); //move psi to get ready to measure at position j
        //after calling psi.position(j), psi.AA(j) returns a local representation of the wavefunction,
        //which is the proper way to make measurements / take expectation values with local operators.

        ITensor ket = psi.AA(j); //Dirac "ket" for wavefunction
        ITensor bra = conj(primesite(ket)); //Dirac "bra" for wavefunction

        ITensor szj_op = model.sz(j); //operator for sz at site j

        Sz(j) = Dot(bra, szj_op*ket); //take an inner product 
        szf << Sz(j) << endl; //print to file

        if (j<N) { 
            //make a bond ket/bra based on wavefunction representing sites j and j+1:
            ITensor bondket = psi.bondTensor(j); 
            //psi.bondTensor(j) is analogous to psi.AA(j), except that 
	    //bondTensor encodes bond information between j and j+1, so long as psi.position(j) has been called
            ITensor bondbra = conj(primesite(bondket)); 

            ITensor szz_op = model.sz(j)*model.sz(j+1); 
            SdotS(j) = Dot(bondbra, szz_op*bondket); //start with z components

            // add in S+ and S- components:
            // use sp(j)*sm(j) and its conjugate, also note the one-half out front:
            ITensor spm_op = model.sp(j)*model.sm(j+1);
            SdotS(j) += 0.5*Dot(bondbra, spm_op*bondket);
            ITensor smp_op = model.sm(j)*model.sp(j+1);
            SdotS(j) += 0.5*Dot(bondbra, smp_op*bondket);

            sdots << SdotS(j) << endl; //print to file
            sumSdotS += SdotS(j); //figure out the sum of SdotS.  should be the same as the Heisenberg energy
        }
    }

    cout << format("\nSum of SdotS is %f\n")%sumSdotS;

    return 0;
}


</code>

<br>
[[Back to Recipes|recipes]]
