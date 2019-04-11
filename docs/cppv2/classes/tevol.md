# Time-Evolving MPS

ITensor includes various types and functions to make assist you in writing codes
to evolve matrix product states (MPS) in real and imaginary time.


## Time Evolution Routines

* ```
   gateTEvol(Iterable gatelist,
             Real ttotal,
             Real tstep,
             MPS & psi,
             Args args = Args::global()) -> Real

   gateTEvol(Iterable gatelist,
             Real ttotal,
             Real tstep,
             IQMPS & psi,
             Args args = Args::global()) -> Real
   ```

   Time evolve an MPS or IQMPS by applying a set of Trotter "gates". A gate is conceptually
   a two-site operator which <i style="color:red;">must act on two consecutive sites</i>
   where consecutive means following the ordering of the MPS.

   To apply a gate which acts on non-consecutive sites, you should insert appropriate
   "swap" gates into the gate list. For assistance in creating time-evolution and
   swap gates, see the [[BondGate|classes/bondgate]] helper class. 
   The gate list argument can be any type of container of gates, 
   such as a <a href="https://en.cppreference.com/w/cpp/container/vector" target="_blank">std::vector</a>.

   The argument `tstep` tells the gateTEvol function how large a time step one application
   of all the gates in `gatelist` corresponds to. (It is up to you to ensure that this
   correspondence is correct.) Then the gateTEvol function applies the gates to the MPS
   a `ttotal/tstep` number of times.

   A key advantage of using the gateTEvol function, besides its convenience, is that it
   uses a "smart" algorithm which "looks ahead" to the next gate and performs the SVD
   toward the next gate, so as to do the minimum number of SVD steps possible.

   Last but not least, the `args` passed to gateTEvol are passed to the routine
   that factorizes the MPS after each gate (whether SVD or density matrix decomposition),
   so it is important to pass arguments such as "Cutoff","Maxm",and "Minm" to truncate
   the MPS and control the costs of the algorithm. For more information on these 
   truncation arguments, see the documentation for the [[tensor decomposition methods|classes/decomp]].
