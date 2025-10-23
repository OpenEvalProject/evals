# Peer review - Round 1

Editors:
- Petra Anne Levin, Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100914.3.sa0](https://doi.org/10.7554/eLife.100914.3.sa0)

Data presented in this useful report suggest a potentially new model for chemotaxis regulation in the gram-negative bacterium P. putida. Data supporting interactions between CheA and the copper-binding protein CsoR, reveal potential mechanisms for coordinating chemotaxis and copper resistance. There was, however, concern about the large number of CheA interactors identified in the initial screen and it was felt that the study was incomplete without a substantial number of additional experiments to test the model and bolster the authors' conclusions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100914.3.sa1](https://doi.org/10.7554/eLife.100914.3.sa1)

Summary:

This manuscript focuses on the apparent involvement of a proposed copper-responsive regulator in the chemotactic response of Pseudomonas putida to Cu(II), a chemorepellent. Broadly, this area is of interest because it could provide insight into how soil microbes mitigate metal stress. Additionally, copper has some historical agricultural use as an antimicrobial, thus can accumulate in soil. The manuscript bases its conclusions on an in vitro screen to identify interacting partners of CheA, an essential kinase in the P. putida chemotaxis-signaling pathway. Much of the subsequent analysis focuses on a regulator of the CsoR/RcnR family (PP_2969).

Weaknesses:

The data presented in this work does not support the model (Figure 8). In particular, PP_2969 is linked to Ni/Co resistance not Cu resistance. Further, it is not clear how the putative new interactions with CheA would be integrated into diverse responses to various chemoattract/repellents. These two comments are justified below.

PP_2969

• The authors present a sequence alignment (Figure S5) that is the sole based for their initial assignment of this ORF as a CsoR protein. There is conservation of the primary coordinating ligands (highlighted with asterisks) known to be involved in Cu(I) binding to CsoR (ref 31). There are some key differences, though, in residues immediately adjacent to the conserved Cys (the preceding Ala, which is Tyr in the other sequences). The effect of these change may be significant in a physiological context.

• The gene immediately downstream of PP_2969 is homologous to E. coli RcnA, a demonstrated Ni/Co efflux protein, suggesting that P2969 may be Ni or Co responsive. Indeed PP_2970 has previously been reported as Ni/Co responsive (J. Bact 2009 doi:10.1128/JB.00465-09). The host cytosol plays a critical role in determining metal-response, in addition to the protein, which can explain the divergence from the metal response expected from the alignment.

• The previous JBact study also explains the lack of an effect (Figure 5b) of deleting PP_2969 on copper-efflux gene expression (copA-I, copA-II, and copB-II) as these are regulated by CueR not PP_2969 consistent with the previous report. Deletion of CsoR/RcnR family regulator will result in constitutive expression of the relevant efflux/detoxification gene, at a level generally equivalent to the de-repression observed in the presence of the signal.

• Further, CsoR proteins are Cu(I) responsive so measuring Cu(II) binding affinity is not physiologically relevant (Figures 5a and S5b). The affinities of demonstrated CsoR proteins are 10-18 M and these values are determined by competition assay. The MTS assay and resulting affinities are not physiologically relevant.

• The DNA-binding assays are carried out at protein concentrations well above physiological ranges (Figs 5c and d, and S5c, d). The weak binding will in part result from using DNA-sequences upstream of the copA genes and not from from PP_2970.

CheA interactions

There is no consideration given to the likely physiological relevance of the new interacting partners for CheA.

• How much CheA is present in the cell (copies) and how many copies of other proteins are present? How would specific responses involving individual interacting partners be possible with such a heterogenous pool of putative CheA-complexes in a cell. For PP_2969, the affinity reported (Figure 5A) may lay at the upper end of the CsoR concentration range (for example, CueR in Salmonella is present at ~40 nM).

• The two-hybrid system experiment uses a long growth time (60 h) before analysis. Even low LacZ activity levels will generate a blue colour, depending upon growth medium (see doi: 10.1016/0076-6879(91)04011-c). It is also not clear how Miller units can be accurately or precisely determined from a solid plate assay (the reference cited describes a protocol for liquid culture).

Comments on revised version:

The authors have replied in detail to the various comments about the original manuscripts. However, the responses are generally lengthy rationalisations of the original interpretation of the data and do not fundamentally address critical concerns raised about the physiological relevance of the results. The response appears to rest on the assumption that the numerous interacting partners obtained from the initial screen are all true positives and that all subsequent experimental results are interpreted to justify that assumption. In the case of CsoR, the experimental results and interpretation are inconsistent with previously published studies of the metal and DNA-binding properties of CsoR proteins. The following points reiterate comments from the previous review, in the hopes that the authors will, at the very least, consider the likelihood that the "CsoR" protein they have identified is in fact responsive to a different metal. Further, that the authors consider multiple possible interpretations of the data, particularly those that are inconsistent with the model/hypothesis and take this into account in their experimental design.

• (Figure 4) Almost all purified proteins will bind Cu(II) most tightly in vitro, followed by Zn(II) and Ni(II). This behaviour is a consequence of the Irving-Williams affinity series (doi.org/10.1038/162746a0 and doi.org/10.1039/JR9530003192, especially Figure 4) and is not considered an indicator of physiological metal preference. Biomolecules will exhibit the same behaviour as small organic ligands towards first row transition ions because of the flexibility of their structures. Thus, the results obtained are unsurprising and, because of the method used, have no physiological relevance.

• The authors cite other in vivo work as evidence for varied metal-response by regulator proteins. However, experiments in these citations are of limited relevance because some focus on other structural classes of metalloregulator proteins (so not relevant here) while others focus on changes in metal accumulation by overexpression of the regulator protein, with no examination of the metal-specificity of the efflux protein the key determinant of the physiological response of the regulator protein - why turn on expression of an efflux protein that can't pump out a particular metal? Finally, adding equivalent concentrations of metals to growing cells is not a good comparison as metals are toxic at different concentrations. The regulators will only have evolved to be just good enough, not perfect, with respect to selectivity. Laboratory experimental conditions often explore non-physiological conditions.

• It is also important to re-emphasise the authors' own statements on lines 90-93 that P. putida has a CueR protein. This is consistent with the phylogenetic distribution of CueR proteins in gram-negative bacteria. The CsoR proteins, in contrast, are found only in gram-positive bacteria. This inconsistency is ignored by the authors.

• The implications of the Irving-Williams series on metal-specific responses of bacterial metalloregulator proteins are described in the following references: 10.1016/j.cbpa.2021.102095, 10.1074/jbc.R114.588145, and 10.1038/s41589-018-0211-4. The last reference of this set provides an experimental basis for why metalloregulator affinities for Cu (and Zn and Ni) are so tight (and why the values obtained in Figure 4 in this manuscript are not relevant).

• Similarly, the previous experimental studies of CsoR proteins not cited by the authors (10.1021/ja908372b 10.1021/bi900115w) provide rigourous experimental approaches for measuring metal and DNA-binding affinities and further highlight the weakness of the experimental design in this manuscript.

• The DNA-binding assays are not physiologically relevant because they do not use DNA from the operator regulated by the candidate protein (why this was not explored in the revision is difficult to understand). The mobility shift observed at these high protein concentrations will result from non-specific binding. It is unsurprising that Cu(II) has an effect on DNA binding as it is added at such high concentrations relative to both protein and DNA so as to compete for DNA-binding with the protein (which binds weakly because there is no specific recognition site). The 10:1 ratio of Cu:CsoR is 10-times higher than needed as this class of proteins will show decreases in DNA-affinity in the presence of the correct metal at 1:1 stoichiometry. As indicated above, the authors need to consider alternative interpretations for their results rather than try to rationalise the results to fit the model.

The points raised above readily address the authors' own comments in the response as to their surprise at some of the results and their inconsistency with the model.

Even if the authors were to identify the correct metal to which the protein responds, there are still fundamental issues with experimental design and interpretation that would need to be addressed to indicate any link between the protein and chemotaxis.
