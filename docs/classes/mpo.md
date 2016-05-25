# MPO and IQMPO 

MPO is a class for storing matrix product operators, which are similar to matrix product states but 
represent operators. Thus each MPO tensor, one for each site of the system, has two indices. The 
convention in ITensor is that these two site indices have prime level zero and one, respectively,
similar to the ITensor convention for single-site operators.

IQMPO is identical to MPO (both are implemented through the same template class) but uses
[[IQTensors|classes/iqtensor]] instead of [[ITensors|classes/itensor]].

MPO and IQMPO are actually derived from MPS and IQMPS, so have nearly the same interface for
most purposes. For example, to obtain the tensor for an MPO H on site j, one calls `H.A(j)`.

Beyond those inherited from MPS and IQMPS, MPO and IQMPO currently offer few additional algorithms.
Their main purpose is to serve as containers for MPO site tensors, for example, those generated
by the AutoMPO helper class.

For algorithms that take MPOs as input or which manipulate MPOs, see [[MPS and MPO algorithms|classes/mps_mpo_algs]].

<br/>
_This page current as of version 2.0.7_
