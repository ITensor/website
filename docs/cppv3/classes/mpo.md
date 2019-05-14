# MPO

MPO is a class for storing matrix product operators, which are similar to matrix product states but 
represent operators. Thus each MPO tensor, one for each site of the system, has two indices. The 
convention in ITensor is that these two site indices have prime level zero and one, respectively,
similar to the ITensor convention for single-site operators.

The MPO class is actually derived from the MPS class, so MPOs have nearly the same interface for
most purposes. For example, to obtain the tensor for an MPO K on site j, one calls `K(j)`.

Beyond those inherited from MPS, MPO currently offer a few additional algorithms.
Their main purpose is to serve as containers for MPO site tensors, for example, those generated
by the AutoMPO helper class.

For algorithms that take MPOs as input or which manipulate MPOs, see [[MPS and MPO algorithms|classes/mps_mpo_algs]].

Below we list methods that are unique to MPOs, for other methods refer to the [[MPS documentations|classes/mps]].

## MPO Tag and Prime Methods

MPO have the same tag and prime methods that are defined for
ITensors, MPS and IndexSets. See the __Tag and Prime Methods__ section of the
[[IndexSet documentation|classes/indexset]] for a complete list of methods.

When applied to an MPO, the method is applied to every MPO tensor.

## Index Methods

MPOs generally have the same Index functions as MPSs (see the __Index Methods__ section of the 
[[MPS documentations|classes/mps]] for more details). Here we list Index methods that are unique
to MPOs.

* `siteInds(MPO K, int j) -> IndexSet`

  Return the site indices of the MPO tensor `K(j)`.

* `siteIndex(MPO K, int j, TagSet tsmatch = "0") -> Index`

  Return the site index of the MPO tensor `K(j)` containing the tags `tsmatch`.

* `uniqueSiteIndex(MPO K, IndexSet is, int j) -> Index`

  Return the site index of the MPO tensor `K(j)` that is not in the IndexSet `is`. 
  If `K(j)` does not have any indices in `is`, throw an error. If `is` contains both
  site indices of `K(j)`, return an empty index `Index()`.

* `uniqueSiteInds(MPO K, MPS A) -> IndexSet`

  Return an IndexSet of the sites that are unique to MPO `K`, assuming MPO `K` and MPS `A` share
  a set of site indices.

* `uniqueSiteInds(MPO K, MPO L) -> IndexSet`

  Return an IndexSet of the sites that are unique to MPO `K`, assuming MPO `K` and MPO `L` share
  a set of site indices.

  If `K` and `L` share both site indices, return a default constructed index `Index()`.

* `uniqueSiteInds(MPO K, IndexSet is) -> IndexSet`

  Return an ordered IndexSet `sites` such that `sites(j)` is one of the indices of the MPO tensor
  `K(j)` for each site `j`. The site index is the one that is not the index `is(j)`. If `K(j)` does
  not have the index `is(j)`, throw an error.

* `hasSiteInds(MPO A, IndexSet is) -> bool`

  Returns true if, for all sites `j`, `hasIndex(siteInds(A,j),is(j))` is true.

* * `.replaceSiteInds(IndexSet is_old, IndexSet is_new)`

  `replaceSiteInds(MPO K, IndexSet is_old, IndexSet is_new) -> MPO`

  For each site `j`, search the site indices of the MPO tensor `K(j)` for the the index `is_old(j)`.
  If it is found, replace it with the Index `is_new(j)`, otherwise leave `K(j)` unmodified.

* * `.swapSiteInds()`

  `swapSiteInds(MPO K) -> MPO`

  For each site `j`, swap the site indices of the MPO tensor `K(j)`.

<br/>
_This page current as of version 3.0.0_
