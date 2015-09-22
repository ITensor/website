<span class='article_title'>How to use AutoMPO</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 18, 2015</span>

Instead of programming an [[MPO by hand|tutorials/MPO]], ITensor has AutoMPO which allows for the automatic generation of an MPO.  This feature allows for the typing of a chain of input which AutoMPO converts into an MPO for the full system.  

Here is a code snippet for making an MPO for the Heisenberg model on a spin-half chain.

    SpinHalf sites(N);
    AutoMPO ampo(sites);
    for(int j = 1; j < N;++j)
      {
      ampo += 0.5,"S+",j,"S-",j+1;
      ampo += 0.5,"S-",j,"S+",j+1;
      ampo +=     "Sz",j,"Sz",j+1;
      }
    auto H = MPO(ampo);

Let's go line by line through it and see what AutoMPO is doing.  Here, we are just showing the part that makes the MPO. Higher up in the code (maybe the previous line), we must initialize a number `N` to record that we want `N` sites. Below the code, we might use the `dmrg` function to calculate the ground state of the MPO we've made.

The `+=` operator accepts the following input:

    [value],"[operator name]",[site],"[operator name]",[site]

or

    [value],"[operator name]",[site]

for single site operators.  The `[operator name]` must be recognizable by the `SiteSet` (for example, `SpinHalf`) class.  If `[value]` is omitted, it will be assumed to be `1.0`.  Using this syntax, the only concern is adding the correct terms into our Hamiltonian on every site.  AutoMPO will convert these statements to a string and make the appropriate MPO.  

Currently, AutoMPO only accepts operators that act non-trivially on up to two sites.  If we have, for example, @@(S^x_iS^x_iS^y_jS^y_j)@@ then we can indicate two operators with `*` inside of the string:

    ampo += "Sx*Sx",i,"Sy*Sy",j;

Note this only works for two operators on the same site!

Let's say we want to now run a code for a spin one chain.  We only need to make one replacement.  The line that reads `SpinHalf sites(N);` can be changed to

    SpinOne sites(N);

We can also make a custom `SiteSet` and use that if we need.  

## Exponentiating MPOs

A neat trick allows us to produce exponentials of Hamiltonians quickly and easily with the function

    MPO toExpH<ITensor>( MPO, [Complex number])

This function also accepts `IQTensors`.  This method is based on [1] and gives us @@\exp(-\tau\mathcal{H})@@.


