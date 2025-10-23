# Peer review - Round 1

Editors:
- Scott A Armstrong, Memorial Sloan Kettering Cancer Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13087.059](https://doi.org/10.7554/eLife.13087.059)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Transcription-coupled genetic instability marks acute leukemia structural variation hotspots" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

A series of recent studies demonstrated that genetic diversification during adaptive immune responses of B cells comes with an increased risk of malignant transformation, i.e. when AID, RAG1 and RAG2 target non-immunoglobulin genes. Based on integrative analyses of transcriptional activity (GRO-seq) and genetic lesions (whole genome sequencing), Lohi and colleagues propose a novel scenario to explain how AID and RAG1/RAG2 can be aberrantly targeted to Non-Ig sites and thereby cause genetic lesions that drive malignant transformation.

Essential revisions:

1) The scenario in Figure 6 is potentially interesting but goes far beyond what is supported by the actual data presented in the study. The Discussion section dilutes the main findings by additional speculation. A more detailed discussion of their actual data (instead of what could be gleaned from hypothetical future experiments) would be helpful. There is a lot of speculation on the Results section and in particular around findings that build up to this mechanism and it is not clear how the data/analysis supports these observations.

2) The manuscript is of potential interest to a broader audience but mainly written for expert readers in computational biology. To make this work accessible to a wider group of scientists that are potentially interested in the topic, it would seem to be necessary to explain the rationale for the use of certain methods and techniques in some meaningful detail. For instance, the use of t-SNE blots (as for CyTOF) to correlate AID, RAG1 and RAG2 expression with cytogenetic subtypes is of interest, but not discussed what exactly can be seen in the diagrams and why this method was chosen.

3) Expression of AID and RAG1/RAG2 "markedly distinct between pre-B ALL subtypes": The measurements were performed in fully established ALL clones. The interpretation that different expression levels of AID and RAG1/RAG2 point to a different role of these enzymes in different cytogenetic subtypes is likely incorrect. As in B cell lymphoma, AID and RAG1/RAG2 act together in a multi-step process of clonal evolution towards full transformation. In the fully established leukemia, secondary genetic events and consequences of oncogenic signaling may alter expression levels and obscure the role of AID and RAG1/RAG2 in these leukemia subsets. In addition, the significance of AID and RAG1/RAG2 expression only measured at the mRNA level is unclear. Western blot analyses should be performed if authors feel strongly about documenting different expression levels.

4) Do the proposed transcriptional features of instability at SV-sites coincide with cryptic RSS or minimal RAG1/RAG2 substrates? This would add to mechanistic plausibility of their scenario.

5) For the TAD Analysis: Would TAD definition change if a lymphoid origin cell lines or tissue types were used? The authors divide TADS in quartiles on the basis of number of breakpoints within TADs and study how this correlates with% study of convT at these loci. The size range and density of the TADs can vary greatly (T2). The authors should ensure that TAD size does not confound this analysis.

6) Correlation of 'transcriptional features' such as prevalence of POL2 stalling, DNA sequences that are susceptible to R-LOOP formation and also convergent transcription, with regions that are frequently rearranged in ALL, and in regions with high prevalence of RSS.

7) Whilst there is a notable enrichment against other active promoters for example the 'width' of the 'stalling' region, although what this really represents, as defined from GRO-seq data, is the high density of active RNA polymerases, so is it possible that these represent regions of active transcription.

8) With previous reports showing enrichment of genomic rearrangements at active promoters and enhancers it is not clear whether the observations here are a consequence of transcriptional activity in these regions or an enriched mechanism underpinning the regions that are frequently targeted. The authors should present a global analysis – see statistical review section.

9) A major limitation of the analysis here is that there are not overlapping datasets from the same samples. As the authors have access to direct primary patient cells and cell lines representative of B-ALL their interpretations of the data would significantly benefit from performing RNAseq, POL2 chip, and potentially MNase-seq to support their observations (Pol2 stalling and convergent transcription).

10) Overall there is a clear narrative issue, the dataset is complex and the analysis is not clear nor comprehensive – making it rather hard for the reviewer and in time a reader to comprehensively evaluate the analytical approaches used, as well as, the evaluate the interpretation of the findings, which often render conclusions as facts by citing other papers rather than being supported by the data in itself. It would be very helpful if the authors included a supplemental figure containing a flow chart describing what datasets where put together and which subsets of data were used for which analysis.

11) Results should be interpreted on the basis of their analysis. Conclusions that account or include findings from the literature should be placed in the Discussion section.

12) It would be useful if the authors performed a global analysis- accounting for chromatin segmentation in ALL and considering these features. It would be very interesting to show specifically how the parameters they consider (TAD domains, RNA pol stalling, conv T) correlate with promoters/ active transcription first and then evaluate if these metrics show significant deviations (enrichment) in the areas most widely affected by genomic rearrangement in ALL and how do these differ between frequent breakpoints and rare breakpoints?

13) Perhaps incorporating metrics that include expression of genes in those regions in B-ALL might strengthen this analysis and provide additional insights into the proposed mechanism. Whilst it may be really difficult to obtain such additional RNA seq data – the authors could consider using gene expression metrics from prior SNP array studies of distinct ALL subtypes.
