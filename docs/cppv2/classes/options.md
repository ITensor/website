# Options #

<span style="color:red;font-style:italic;">Note: this documentation page refers to code prior to version 2.0</span>

Class for specifying parameters, defined in utilities/options.h
A default set of options is always available via `Global::opts()` and will be used unless locally overridden by the user.

## Synopsis ##

    void 
    function(int arg1, int arg2, const OptSet& opts = Global::opts())
        {
        //the second argument to each 'get' method is a default
        //omitting the default makes the Opt mandatory
        const Real cutoff = opts.getReal("Cutoff",1E-10);
        const int maxm = opts.getInt("Maxm",100);
        const std::string name = opts.getString("Name","");
        //...
        }

    Real cutoff = 1E-8;
    int maxm = 200;
    std::string name = "name";

    function(1,2,Opt("Cutoff",cutoff)+Opt("Maxm",maxm)+Opt("Name",name));
    //or you can do:
    function(1,2,"Cutoff=1E-8,Maxm=200,Name=name");

    //In C++11, this notation is allowed:
    function(1,2,{"Cutoff",cutoff,"Maxm",maxm,"Name",name});

## List of Options ##
These are the options that are used throughout the code. If you want to find out where an option is used try `grep -r -n "<Option Name>"`.
Some of these options have some sensible global default value.

* `AbsoluteCutoff`
* `AtBond`
* `Cutoff`
* `DebugLevel`
* `DoNormalize`
* `DoRelCutoff`
* `Energy`
* `HalfSweep`
* `Maxm`
* `MaxIter`
* `Minm`
* `Noise`
* `Nsweep`
* `Order`
* `ShowEigs`
* `SVDThreshold`
* `Sweep`
* `TimeStep`
* `Time`
* `TotalTime`
* `Truncate`
* `Truncerr`
	This should only be used locally and holds the truncation error. It's currently only used by the [[Spectrum|classes/spectrum]] class.
* `UseSVD`
* `Verbose`
* `Weight`
* `WriteDir`
  Sets the target directory for swap-to-disk operations. Defaults to ./
* `WriteM`
  The number of states above which the MPS/MPO will be swapped to disk.
* `Quiet`

