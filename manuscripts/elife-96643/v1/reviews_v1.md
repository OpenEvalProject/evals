# Peer review - Round 1

Editors:
- Shozeb Haider, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96643.3.sa0](https://doi.org/10.7554/eLife.96643.3.sa0)

The article presents a machine-learning method to predict protein hotspot residues. The validation is incomplete, along with the misinterpretation of the results with other current methods like FTMap.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96643.3.sa1](https://doi.org/10.7554/eLife.96643.3.sa1)

The paper describes a program developed to identify PPI-hot spots using the free protein structure and compares it to FTMap and SPOTONE, two webservers that they consider as competitive approaches to the problem. We appreciate the effort in providing a new webserver that can be tested by the community but we continue to have major concerns:

(1) The comparison to the FTMap program is problematic. The authors misinterpret the article they refer to, i.e., Zerbe et al. "Relationship between hot spot residues and ligand binding hot spots in protein-protein interfaces" J. Chem. Inf. Model. 52, 2236-2244, (2012). FTMap identifies hot spots that bind small molecular ligands. The Zerbe et al. article shows that such hot spots tend to interact with hot spot residues on the partner protein in a protein-protein complex (emphasis on "partner"). Thus, the hot spots identified by FTMap are not the hot spots defined by the authors. In fact, because the Zerbe paper considers the partner protein in a complex, the results cannot be compared to the results of Chen et al. This difference is missed by the authors, and hence the comparison of the FTMap is invalid.

(2) Chen et al. use a number of usual features in a variety of simple machine-learning methods to identify hot spot residues. This approach has been used in the literature for more than a decade. Although the authors say that they were able to find only FTMap and SPOTONE as servers, there are dozens of papers that describe such a methodology. Some examples are given here: (Higa and Tozzi, 2009; Keskin, et al., 2005; Lise, et al., 2011; Tuncbag, et al., 2009; Xia, et al., 2010). There are certainly more papers. Thus, while the web server is a potentially useful contribution, the paper does not provide a fundamentally novel approach.
