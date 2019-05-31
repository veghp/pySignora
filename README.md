# pySignora

**pySignora** is a Python implementation of pathway gene-pair SIGnature OverRepresentation Analysis (SIGORA).

SIGORA has been published in PeerJ and implemented in R (https://cran.r-project.org/web/packages/sigora/index.html) by *Foroushani et al.* (2013). Shortly, the method compiles a set of weighted markers, *pathway gene-pair signatures* (Pathway-GPS), for each pathway in a repository. Subsequently, it identifies statistically overrepresented Pathway-GPSs in a user-specified gene list, using an adapted version of the hypergeometric test.
A *pathway* here is defined as a set of genes with the same pathway-ontology annotation. A pathway gene-pair signature is a pair of genes that, as a combination, are specific to a single pathway. The *weight* of a GPS expresses the average specificity of the two gene components towards the common pathway. The weight range is \[0, 1\].

For more details, see the inventors' original publication: https://peerj.com/articles/229/

The two core functions, GPS-generation and signature ORA, have been implemented, but the package is still **under development** and many important features will be added in the future:
* Multiple-testing correction
* KEGG, Reactome, GO and other databases
* Handling hierarchical (multilevel) repositories


## Usage
The input pandas dataframe (`repodf`) has 3 columns: pathway, desccription, gene, e.g.:
```python
import pandas as pd
repodf[:3]
#              pathwayId                           pathwayName             gene
# 1  ecadherin_1_pathway           E-cadherin signaling events  ENSG00000168036
# 2  ecadherin_1_pathway           E-cadherin signaling events  ENSG00000039068
# 3   syndecan_2_pathway  Syndecan-2-mediated signaling events  ENSG00000101680
```

```python
import pysignora as ps
gps = ps.makegps(repodf)
res = ps.signora(genelist, gps)
```
