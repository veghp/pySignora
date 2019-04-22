# pySignora

**pySignora** is a Python implementation of pathway gene-pair SIGnature OverRepresentation Analysis (SIGORA).

SIGORA has been published in PeerJ and implemented in R (https://cran.r-project.org/web/packages/sigora/index.html) by *Foroushani et al.* (2013). Shortly, the method compiles a set of weighted markers, *pathway gene-pair signatures* (Pathway-GPS), for each pathway in a repository. Subsequently, it identifies statistically overrepresented Pathway-GPSs in a user-specified gene list, using an adapted version of the hypergeometric test.
A *pathway* here is defined as a set of genes with the same pathway-ontology annotation. A pathway gene-pair signature is a pair of genes that, as a combination, are specific to a single pathway. The *weight* of a GPS expresses the average specificity of the two gene components towards the common pathway. The weight range is \[0, 1\].

For more details, see the inventors' original publication: [https://peerj.com/articles/229/]

The two core functions, GPS-generation and signature ORA, have been implemented, but the package is still **under development** and many important features will be added in the future.

## Usage

```python
import pysignora as ps
gps = ps.makegps(repodf)
res = ps.signora(gps, genelist)
```
