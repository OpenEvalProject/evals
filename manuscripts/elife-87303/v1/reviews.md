# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87303.3.sa0](https://doi.org/10.7554/eLife.87303.3.sa0)

This valuable study reports on a new tool that allows for light-controlled protein degradation in Escherichia coli. With the improved light-responsive protein tag, endogenous protein levels can be reduced several fold. The methodology is convincing and will be of interest to the fields of gene expression regulation in bacteria and more generally to synthetic biologists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87303.3.sa1](https://doi.org/10.7554/eLife.87303.3.sa1)

Specifically controlling the level of proteins in bacteria is an important tool for many aspects of microbiology, from basic research to protein production. While there are several established methods for regulating transcription or translation of proteins with light, optogenetic protein degradation has so far not been established in bacteria. In this paper, the authors present a degradation sequence, which they name "LOVdeg", based on iLID, a modified version of the blue-light-responsive LOV2 domain of Avena sativa phototropin I (AsLOV2). The authors reasoned that by removing the three C-terminal amino acids of iLID, the modified protein ends in "-E-A-A", similar to the "-L-A-A" C-terminus of the widely used SsrA degradation tag. The authors further speculated that, given the light-induced unfolding of the C-terminal domain of iLID and similar proteins, the "-E-A-A" C-terminus would become more accessible and, in turn, the protein would be more efficiently degraded in blue light than in the dark.

Indeed, several tested LOVdeg-tagged proteins show clearly lower cellular levels in blue light than in the dark. Depending on the nature and expression level of the target protein, protein levels are reduced modestly to strongly (2 to 20x lower levels upon illumination). Accordingly, the authors propose to use their system in combination with other light-controlled expression systems and provide data validating this approach. The LOVdeg system allows to modulate protein levels to a similar degree and with comparable kinetics as optogenetic systems controlling transcription or translation of protein, and can be combined with such systems.

The manuscript and the figures are generally very well-composed and follow a clear structure. The schematics nicely explain the underlying principles. Besides the advantages of the LOVdeg approach, including its complementarity to controlled expression of proteins, the revised version of the manuscript also highlights the limitations of the method more clearly, e.g., (i) the need to attach a C-terminal tag of considerable size to the protein of interest, (ii) the limited efficiency (slightly less efficient and slower than EL222, a light-dependent transcriptional control mechanism), and (iii) the incompletely understood prerequisites for its application. Taken together, this manuscripts describes the LOVdeg system as a valuable addition to the tool box for controlling protein levels in prokaryotic cells.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87303.3.sa2](https://doi.org/10.7554/eLife.87303.3.sa2)

In this manuscript the authors present and characterize LOVdeg, a modified version of the blue-light sensitive AsLOV2 protein, which functions as a light-inducible degron in Escherichia coli. Light has been shown to be a powerful inducer in biological systems as it is often orthogonal and can be controlled in both space and time. Many optogenetic systems target regulation of transcription, however in this manuscript the authors target protein degradation to control protein levels in bacteria. This is an important advance in bacteria, as inducible protein degradation systems in bacteria have lagged behind eukaryotic systems due to protein targeting in bacteria being primarily dependent on primary amino acid sequence and thus more difficult to engineer. In this manuscript, the authors exploit the fact that the J-alpha helix of AsLOV2, which unwinds into a disordered domain in response to blue light, contains an E-A-A amino acid sequence which is very similar to the C-terminal L-A-A sequence in the SsrA tag which is targeted by the unfoldases ClpA and ClpX. They truncate AsLOV2 to create AsLOV2(543) and combine this truncation with a mutation that stabilizes the dark state to generate AsLOV2*(543) which, when fused to the C-terminus of mCherry, confers light-induced degradation. The authors do not verify the mechanism of degradation due to LOVdeg, but evidence from deletion mutants contained in the supplemental material hints that there is a ClpA dominated mechanism. The LOVdeg is able to target mCherry for protein degradation across different phases of bacterial growth, which is important for regulating processes at stationary phase and a potential additional advantage over transcriptional repression systems. They demonstrate modularity of this LOVdeg by using it to degrade the LacI repressor, CRISPRa activation through degradation of MCP-SoxS, and the AcrB protein which is part of the AcrAB-TolC multidrug efflux pump. In all cases, measurement of the effect of the LOVdeg is indirect as the authors measure reduction in LacI repression, reduction in CRISPRa activation, and drug resistance rather than directly measuring protein levels. Nevertheless the evidence is convincing, although seemingly less effective than in the case of mCherry degradation, although it is hard to compare due to the different endpoints being measured. The authors further modify LOVdeg to contain a known photocycle mutation that slows its reversion time in the dark, so that LOVdeg is more sensitive to short pulses of light which could be useful in low light conditions or for very light sensitive organisms. They also demonstrate that combining LOVdeg with a blue-light transcriptional repression system (EL222) can decrease protein levels an additional 23-fold (relative to 7-fold with LOVdeg alone). Finally, the authors apply LOVdeg to a metabolic engineering task, namely reducing expression of octanoic acid by regulating the enzyme CpFatB1, an acyl-ACP thioesterase. The authors show that tagging CpFatB1 with LOVdeg allows light induced reduction in octanoic acid titer over a 24 hour fermentation. In particular, by comparing control of CpFatB1 with EL222 transcriptional repression alone, LOVdeg, or both the authors show that light-induced protein degradation is more effective than light-induced transcriptional repression. The authors suggest that this is because transcriptional repression is not effective when cells are at stationary phase (and thus there is no protein dilution due to cell division). Overall, the authors have generated a modular, light-activated degron tag for use in Escherichia coli that is likely to be a useful tool in the synthetic biology and metabolic engineering toolkit.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87303.3.sa3](https://doi.org/10.7554/eLife.87303.3.sa3)

The authors present the mechanism, validation, and modular application of LOVtag, a light-responsive protein degradation tag that is processed by the native degradosome of Escherichia coli. Upon exposure to blue light, the c-terminal alpha helix unfolds, essentially marking the protein for degradation. The authors demonstrate the engineered tag is modular across multiple complex regulatory systems, which shows its potential widespread use throughout the synthetic biology field. The step-by-step rational design of identifying the protein that was most dark-stabilized as well as most light-responsive for degradation, was useful in terms of understanding the key components of this system. The most compelling data shows that the engineered LOVTag can be fused to multiple proteins and achieve light-based degradation, without affecting the original function of the fused protein.
