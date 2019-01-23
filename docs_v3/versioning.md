# Versioning of ITensor Releases #

ITensor uses [semantic versioning](http://semver.org/spec/v2.0.0.html), loosely defined. Our version numbers are of the form

<div style="font-size:110%;text-align:center;font-weight:normal;">
<span style="color:red;">Redesign</span>.<span style="color:#336699;">Improvement</span>.<span style="color:green;">Patch</span>
</div>

with the following meaning:


* <span style="color:red;font-weight:normal;">Redesign</span> releases are major releases that are not backwards compatible
in general. They mark major changes to both the library's interface and internal design.

* <span style="color:#336699;font-weight:normal;">Improvement</span> releases may introduce significant new features, extend the current API (e.g. adding optional function arguments), or rearrange internals while attempting to be backwards compatible as much as possible.

* <span style="color:green;font-weight:normal;">Patch</span> releases focus on bug fixes or minor improvements and do not to break client code or change the library API in any way (unless the API is itself the cause of a bug).



Because ITensor is non-commercial and a research project in its own right,
we intend to depart from semantic versioning by not treating any <span style="color:red">Redesign</span> release numbers as special. Redesign release number 0 does not necessarily mean "alpha" code nor does Redesign release 1 indicate a special, stable reference release of the library. Redesign releases also do not have a prescribed size: they may include large and extensive changes or simply small but crucial changes that nevertheless break client code.


