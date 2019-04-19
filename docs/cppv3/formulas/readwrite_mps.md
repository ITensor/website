# Reading and Writing MPS or MPO To/From Disk #

The following formula is for an MPS, but works the same for an MPO.

## Writing an MPS to a File ##

Writing an MPS to disk is easy. Say you have an MPS created using a particular [[SiteSet|classes/siteset]] class called 'sites':

    int N = 100; //number of sites
    SpinHalf sites(N); //SpinHalf is a subclass of SiteSet
    MPS psi(sites);

Write both the SiteSet and MPS to disk using `writeToFile`:

    writeToFile("sites_file",sites);
    writeToFile("psi_file",psi);

You can choose any file names you want.

<br/>

## Reading an MPS from a File ##

Reading an MPS (or MPO) from disk requires three steps: (1) restoring the SiteSet class originally used to construct the MPS; (2) using it to construct a new MPS; (3) reading the MPS data from disk.
This is easier than it sounds. Continuing with the above example:

    SpinHalf sites;
    readFromFile("sites_file",sites);
    MPS psi(sites);
    readFromFile("psi_file",psi);

<br/>

## Including Information in the File Name ##

A nice trick is to use the `format` string formatting function to add extra information to filenames:

    writeToFile(format("sites_%d",N),sites); //file name will be sites_100
    writeToFile(format("psi_%d",N),psi);     //file name will be psi_100


Of course, make sure to use the same file names when you read the objects back from disk:

    int N = 100;
    readFromFile(format("sites_%d",N),sites);

