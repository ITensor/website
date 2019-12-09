# <img src="docs/VERSION/install/icon.png" class="largeicon"> Installing ITensor

The source code for ITensor is hosted on Github at:
[https://github.com/ITensor/ITensor](https://github.com/ITensor/ITensor)

## Downloading the Library

You can download ITensor version 3 by using the following commands:
<div class="commandline"><pre>
git clone https://github.com/ITensor/ITensor itensor
cd itensor
</pre></div>
You can issue these commands within any folder you like on your computer. Also the folder name in the above command does not have to be `itensor`.

If you do not have git on your computer, you can obtain it through your package manager or from the
<a href="http://git-scm.com/" target="blank_">git website</a>.

## Building the Library

1. Check that you have a C++ compiler and LAPACK libraries installed on your system.
   * On Mac OS, this typically requires installing the free XCode package available 
   from the App Store. 
   * On Linux, the `g++` (gcc) program is typically available. Many package managers
     offer a lapack-devel package which includes the LAPACK headers.
   * On Windows, the best option is to install a version of Unix. An Ubuntu Linux 
     terminal can be installed for Windows 10. Another option is to install 
     <a href="https://www.cygwin.com" target="blank_">Cygwin</a>,
     which lets you run Unix programs inside a terminal. If you use Cygwin, make sure to install
     the C++ compiler (gcc) and LAPACK packages.

2. Edit the user configurable options. Start by making a copy 
   of the sample Makefile options file: 

   `cp options.mk.sample options.mk`

   Then begin editing options.mk in a text editor
   and follow the remaining instructions.

3. Within the options.mk file, choose which compiler to use by setting the `CCCOM` 
   variable. Make sure whichever compiler you select supports C++17, the latest version of the
   C++ standard (this is true for [Clang v5 and after](https://clang.llvm.org/cxx_status.html)
   and [G++ v7 and after](https://www.gnu.org/software/gcc/projects/cxx-status.html#cxx17)) as 
   well as the C++17 standard libraries and make sure to set the flag -std=c++17 or similar 
   to enable C++17 language support.
   
5. Within the options.mk file, edit `PLATFORM`, `BLAS_LAPACK_INCLUDEFLAGS` and `BLAS_LAPACK_LIBFLAGS` to reflect the
   type and location of your BLAS/LAPACK libraries. The list of currently
   available platforms is: macos, mkl, acml, lapack
   (for details see matrix/lapack_wrap.h). 
   See examples within the file for common settings of these variables for the various platforms.
   The `PLATFORM` variable 
   selects which function signature definitions will be used to wrap 
   vendor-specific BLAS/LAPACK fortran calls into C.

6. Finally, at the top level of the library (same directory as the options.mk file),
   run the commmand "make" on the command line.
   If all goes well, the built library files should appear in the LIBDIR
   folder specified in options.mk.

7. The resulting compiled library files remain inside the ITensor source
   folder and are not put anywhere else on your machine. To create a 
   program using ITensor, use the files in `tutorial/project_template` as a 
   starting point for making your own code.

Note: sometimes ITensor has issues compiling if the make "-j" flag is used 
(this flag enables parallel compilation on multi-core machines). Try 
disabling it (e.g. explicitly type `make -j 1`) if you have compilation 
errors.

Also, the ITensor build process doesn't work if there are spaces in the path
where you are compiling ITensor. You can avoid this issue by moving the
ITensor source code to a location where the path has no spaces, or make 
a symbolic link to a location where the path has no spaces.

## Building the sample codes

We have provided sample applications under the "sample" directory. If you 
would like to experiment with these, consider making a copy of this folder 
to keep the original sample codes as a reference (and experiment on the copy).

To build the sample apps, simply 'cd' into the "sample" folder and type 'make'.
To build an individual app type 'make app_name' where app_name could be
`dmrg`, `dmrg_table`,  `exthubbard`, etc.


## Linking your own applications to the libraries

We strongly recommend placing your own client/driver code *outside* the 
ITensor library source directory. The location you choose is up to you. 

To get started quickly on your own driver code, we have put a folder
called `project_template` under the `tutorial` folder. Copy the `project_template`
folder to your personal software folder then follow the instructions in the
Makefile to customize it.


## Helpful Makefile variables in options.mk

The `options.mk` file at the top level of the ITensor source directory 
defines a number of Makefile variables that you may find useful in writing 
your own Makefiles. To include these variables, at the top of your Makefile 
put the lines

    LIBRARY_DIR=/path/to/itensor
    include $(LIBRARY_DIR)/this_dir.mk
    include $(LIBRARY_DIR)/options.mk

where of course `/path/to/itensor/` should be replaced with the actual 
location of the ITensor source directory on your machine. 

Including the `options.mk` file in this way defines certain useful 
variables such as 

* `ITENSOR_INCLUDEFLAGS`: compiler flags (of the form `-I/folder/name`) specifying paths to
  ITensor header files, Boost header files, and BLAS/LAPACK header files.

* `ITENSOR_LIBDIR`: the path to the lib/ subdirectory of the ITensor source directory

* `ITENSOR_LIBFLAGS`: flags that specify the names of the statically linked ITensor 
  library files, for example <br/> `-litensor -lmatrix -lutilities`.

* `OPTIMIZATIONS`: user-defined compiler optimization flags, such as `-O2`. It can be helpful for these to 
  match the ones used to build ITensor.

* `DEBUGFLAGS`: user-defined compiler debug-mode flags.
