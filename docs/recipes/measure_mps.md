# Measure the properties of an MPS wavefunction #

Here we will learn how to measure some properties of the
Heisenberg model wavefunction by adding to the code from the [[previous example|recipes/basic_dmrg]].
Essentially we need three pieces to take an expectation value of some property: the operator 
corresponding to that property, the wavefunction, and a way to do the inner
product of the operator with the wavefunction.

For example, consider trying to measure the z-component of
the spin on some site `j` in the Heisenberg chain. 
This operator can be retrieved from the `SpinOne sites(N);` class
that we defined last time, and can be saved as an ITensor:

    ITensor szj_op = sites.op("Sz",j);

Likewise we can obtain operators for the site `j` spin raising (S+) and lowering operators (S-),
by calling `sites.op("Sp",j)` and `sites.op("Sm",j)` respectively.
Now there is an efficient way to take the inner product of these local operators with the MPS
wavefunction. To do this, we must first call the function

    psi.position(j);

_This step is absolutely vital_.  It tells the MPS wavefunction to put all the information
about the amplitudes of the various spin occupations into the site at `j`.
Without this step, we would not be measuring Sz in an orthonormal environment and would
get the wrong answer.  Getting the needed amplitudes is very simple, 
and they will form the ket part of our Dirac "bra-ket" inner product:

    ITensor ket = psi.A(j);

After calling `psi.position(j)`, all the `psi.A(j+n)` tensors for `n != 0` form
the basis weighted by the wavefunction amplitudes.
As basis tensors, these `psi.A(j+n)` do not have amplitude information; only the `psi.A(j)` does. 
That is why it is vital to call `psi.position(j)` before doing a measurement at site `j`.

To get the bra part of the Dirac bra-ket, think about the ket as a column vector, the operator
as a matrix, and the bra as a row vector.  We get the bra by turning the ket into a row vector and conjugating
any imaginary parts.  The way we do this is simple:

    ITensor bra = dag(prime(ket,Site));

The `prime` function is what turns the ket into a row vector (because it will contract with the 
row index of our operator), and `dag` does the hermitian conjugation. The argument `Site` passed to prime tells it
to prime Site-type indices only.
Now we are ready to measure the expectation value of Sz by contracting the bra, operator, and ket. The 
call to `.toReal()` below converts the resulting scalar (rank zero) tensor into a real number:

    Real szj = (bra*szj_op*ket).toReal();

<br/>
<br/>
<br/>

Let's do another, more complicated measurement that will require our kets to be representing information <!--'-->
on two sites `j` and `j+1`.  The vector product S(j) dot S(j+1) will do just fine.  In terms of the 
z-component and raising and lowering operators, S(j) dot S(j+1) = `sz(j)*sz(j+1) + 0.5*( sp(j)*sm(j+1) + sp(j+1)*sm(j) )`.
For example, one of the operators we'll need is <!--'-->

    ITensor spm_op = sites.op("Sp",j)*sites.op("Sm",j+1);

To represent the wavefunction for two sites, we simply contract together two site tensors:

    ITensor bondket = psi.A(j)*psi.A(j+1);

The `bondbra` is made the same as the `bra` from earlier:

    ITensor bondbra = dag(prime(bondket,Site));

And expectation values are realized in the same way:

    Real spm = 0.5*(bondbra*spm_op*bondket).toReal();

Below is a complete code for measuring properties of the MPS wavefunction.  
The code writes to file a list of Sz(j) and S(j) dot S(j+1) for plotting.


    #include "core.h"
    #include "model/spinone.h"
    #include "hams/Heisenberg.h"
    using namespace std;

    int main(int argc, char* argv[])
        {
        int N = 100;

        SpinOne sites(N);

        MPO H = Heisenberg(sites);

        InitState initState(sites);
        for(int i = 1; i <= N; ++i) 
            initState(i,i%2==1 ? "Up" : "Dn");

        MPS psi(initState);

        cout << "Initial energy = " << psiHphi(psi,H,psi) << endl;

        Sweeps sweeps(5);
        sweeps.maxm() = 20,40,80,120,200;

        Real En = dmrg(psi,H,sweeps);

        cout << "\nGround State Energy = " << En << endl;

        //
        //MEASURING SPIN
        //

        //vector of z-components of spin for each site
        Vector Sz(N);
        Sz = 0.0;
        std::ofstream szf("Sz"); //file to write Szj info to

        //Sj dot Sj+1 by means of Splus and Sminus
        Vector SdotS(N-1); 
        SdotS = 0.0;

        //file to write SdotS information to
        std::ofstream sdots("SdotS"); 

        //also sum up the SdotS and see if it is 
        //equal to our ground state energy
        Real sumSdotS = 0.0;

        for(int j=1; j<=N; j++) 
            {
            //re-gauge psi to get ready to measure at position j
            psi.position(j);

            //after calling psi.position(j), psi.A(j) returns a 
            //local representation of the wavefunction,
            //which is the proper way to make measurements
            //i.e. take expectation values with local operators.

            //Dirac "ket" for wavefunction
            ITensor ket = psi.A(j);

            //Dirac "bra" for wavefunction
            ITensor bra = dag(prime(ket,Site));

            //operator for sz at site j
            ITensor szj_op = sites.op("Sz",j);

            //take an inner product 
            Sz(j) = (bra*szj_op*ket).toReal();
            szf << Sz(j) << endl; //print to file

            if(j<N) 
                { 
                //make a bond ket/bra based on wavefunction 
                //representing sites j and j+1:
                ITensor bondket = psi.A(j)*psi.A(j+1);
                ITensor bondbra = dag(prime(bondket,Site)); 

                ITensor szz_op = sites.op("Sz",j)*sites.op("Sz",j+1); 

                //start with z components
                SdotS(j) = (bondbra*szz_op*bondket).toReal();

                //add in S+ and S- components:
                //use sp(j)*sm(j) and its conjugate, 
                //also note the one-half out front:
                ITensor spm_op = sites.op("Sp",j)*sites.op("Sm",j+1);
                SdotS(j) += 0.5*(bondbra*spm_op*bondket).toReal();
                ITensor smp_op = sites.op("Sm",j)*sites.op("Sp",j+1);
                SdotS(j) += 0.5*(bondbra*smp_op*bondket).toReal();

                sdots << SdotS(j) << endl; //print to file

                //figure out the sum of SdotS.  
                //should be the same as the Heisenberg energy
                sumSdotS += SdotS(j); 
                }
            }

        cout << "\nSum of SdotS is " << sumSdotS << endl;

        return 0;
        }



<br>
[[Back to Recipes|recipes]]
