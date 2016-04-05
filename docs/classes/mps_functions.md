# MPS and IQMPS Functions

<span style="color:red;font-style:italic;">Note: this documentation page refers to code prior to version 2.0</span>

Functions for working with matrix product states.

* `int averageM(MPS psi)` <br/>
  `int averageM(IQMPS psi)`

  Compute the average bond dimension of the bonds of the MPS psi.

* `applyGate(BondGate<Tensor> G, MPS psi, OptSet opts = Global::opts())` <br/>
  `applyGate(BondGate<Tensor> G, IQMPS psi, OptSet opts = Global::opts())` <br/>
  `applyGate(ITensor G, MPS psi, OptSet opts = Global::opts())` <br/>
  `applyGate(IQTensor G, IQMPS psi, OptSet opts = Global::opts())`

  

* `Index linkInd(MPS psi, int b)` <br/>
  `IQIndex linkInd(IQMPS psi, int b)`

  Return the link index connecting matrix product state tensors connecting sites `b` and `b+1`.

* `Index rightLinkInd(MPS psi, int i)` <br/>
  `IQIndex rightLinkInd(IQMPS psi, int i)`

  Return the link index connecting matrix product state tensors connecting sites `i` and `i+1`.

* `Index leftLinkInd(MPS psi, int i)` <br/>
  `IQIndex leftLinkInd(IQMPS psi, int i)`

  Return the link index connecting matrix product state tensors connecting sites `i-1` and `i`.

