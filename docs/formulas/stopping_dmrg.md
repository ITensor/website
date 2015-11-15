
# Stopping a DMRG Run "Gracefully"

Often it is helpful to set DMRG to do more sweeps than is needed, monitor
its convergence, then stop it manually when converged. But killing the process
would not allow any cleanup, final measurements, or saving of the wavefunction.

## Stopping DMRG

Fortunately the DMRG code included with ITensor can be stopped gracefully
(meaning, it finishes whichever sweep it is on then exits normally)
by simply putting a file named `STOP_DMRG` in the directory where
the DMRG process is running. A nice unix command to use for 
creating this file is:

    touch STOP_DMRG

The `touch` command creates an empty file if it doesn't already exist
(otherwise it updates the file's time stamp). 

## Stopping iDMRG

The iDMRG code included with ITensor works a bit differently from the 
finite DMRG code, in that it uses the finite DMRG as an inner loop. 
Creating the `STOP_DMRG` file will only exit from this inner loop and
won't stop the iDMRG process. 

To stop iDMRG, do the following:

    touch STOP_DMRG_ALL

Internally, this keeps the object governing the DMRG algorithm's behavior
in a permanent "stop now" state, causing iDMRG to quit after it finishes
the step it is currently on.

## Advanced Customization

The above `STOP_DMRG` and `STOP_DMRG_ALL` file functionality is handled
in ITensor by the `DMRGObserver` class. You can customize this class
by creating your own subclass of it. The (virtual) class method
of DMRGObserver responsible for ending a DMRG calculation is called
`checkDone`, and in `DMRGObserver`, `checkDone` just looks for
the `STOP_DMRG` and `STOP_DMRG_ALL` files, signaling done
(by returning `true`) if they are found.

In your own subclass of `DMRGObserver` you have a few options:

* Not overriding `checkDone` just inherits the same behavior
  as `DMRGObserver`.

* Overriding `checkDone` but calling `DMRGObserver::checkDone()`
  allows you to combine your own custom "done" conditions
  with the default behavior.

* Finally, overriding and ignoring `DMRGObserver::checkDone()`
  lets you turn off the `STOP_DMRG` file checking, allowing 
  you to replace it with other custom "done" conditions.
