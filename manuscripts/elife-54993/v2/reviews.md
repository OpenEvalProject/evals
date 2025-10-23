# Peer review - Round 1

Editors:
- Xiaobing Shi, Van Andel Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54993.sa1](https://doi.org/10.7554/eLife.54993.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "NuRD subunit CHD4 regulates super-enhancer accessibility in Rhabdomyosarcoma and represents a general tumor dependency" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Xiaobing Shi as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors provide a combination of CRISPR/Cas9 knockout, co-immunoprecipitation, and ChIP-seq studies to argue that CHD4 is a potential therapeutic target for the treatment of PAX3-FOXO1 fusion-positive rhabdomyosarcoma. This work builds on the previous observation that CHD4 knockout decreases the growth of FP-RMS cell lines. The studies are fairly thorough and most of the experiments appear well-done. However, the primary conclusions that CHD4 functions independently of NuRD and that there exists a NuRD-only complex are not well supported due to several flaws in the approach and interpretation.

Essential revisions:

1) Only one cell line was used throughout the entire mechanistic study. Are there other PF-positive cell lines that the authors could use to validate at least some of the findings?

2) The authors perform a CRISPR/Cas9 screen of major NuRD components which shows that knockout of CHD4 and RBBP4 reduce viability of FP-RMS cells to a greater extent than other components. Based on this observation, they conclude that CHD4 functions independently of the full NuRD in FP-RMS (subsection “CHD4, unlike other NuRD members, is essential for FP-RMS cell viability”, first paragraph). However, there are multiple orthologs for all NuRD core components that may or may not functionally substitute for one another. As they demonstrate in the supplementary material, multiple orthologs are expressed in these cells (MBD2 and MBD3, MTA1 and MTA2). Therefore, although knockout MBD2 or MBD3 alone does not recapitulate the phenotype of CHD4 knockout, simultaneous knockout of both MBD2 and MBD3 indeed recapitulates the phenotype (personal communications). Hence, the conclusion that CHD4 is acting independently of NuRD is not correct. The authors need to either modify this conclusion or provide additional data by simultaneously eliminating functionally substituting orthologs (e.g. MBD2/MBD3 or MTA1/MTA2/MTA3).

3) The authors claim that a NuRD-only complex localizes to distinct regions (TSS) as compared to CHD4-NuRD. This claim is based on ChIP-seq of CHD4, HDAC2, and RBBP4 (subsection “CHD4/NuRD localizes to enhancers while CHD4-free NuRD to promoters”, last paragraph). However, as the authors later acknowledge (Discussion, second paragraph) RBBP4 and HDAC2 proteins are found in other chromatin-associated complexes (e.g. RBBP4 is found in PRC2, NuRF, and SIN3 complexes; HDAC2 is found in SIN3 and CoREST complexes). Hence, ChIP-seq of HDAC2 and RBBP4 does not necessarily reflect a NuRD-only complex and is inappropriate for this analysis and to make this claim. ChIP-seq of the MTA proteins would be much more appropriate for this experiment. As far as I am aware, the MTA proteins have not been found in other chromatin complexes; hence, they function as core NuRD components (Zhang et al., 2016) Therefore, the authors need to perform ChIP-seq for MTA proteins instead of HDAC2/RBBP4 in order to support this conclusion.

4) The authors endogenously Flag-tag the CHD4 protein to identify co-purifying proteins by mass spectrometry analyses. Based on this work, they develop a model in which CHD4 interacts with a different set of chromatin-associated proteins (BRD4). However, the key challenge with this approach is that CHD4 (NuRD) strongly interacts with chromatin. Hence, it is very difficult to determine whether co-purification reflects direct protein-protein interaction or indirect binding bridged by chromatin. While CHD4 itself has not been shown to directly bind DNA (as the authors point out), it does have chromatin-binding domains (PHD and chromodomains). Of note, histone proteins are among those identified in the mass-spectrometry data (Figure 2) indicating that NCPs are being co-purified. Furthermore, most of the co-purified proteins are from other chromatin-associated complexes or NuRD. These results suggest to me that the majority of the co-purified proteins could easily be explained by indirect/non-specific interaction through NCPs/chromatin. The authors want to carefully discuss this or perform additional experiments to eliminate indirect/non-specific interactions through NCPs/chromatin.
