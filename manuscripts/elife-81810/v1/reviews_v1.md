# Peer review - Round 1

Editors:
- K Christopher Garcia, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81810.sa0](https://doi.org/10.7554/eLife.81810.sa0)

This paper is of interest to immunologists conducting single-cell analyses of T-cell recognition. It provides improved means of curating datasets to reduce noise and identify T cell-antigen pairs with greater confidence. Experimental data from human virus-specific TCRs are used to validate the methodology.


---

# Peer review - Round 1

Editors:
- K Christopher Garcia, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81810.sa1](https://doi.org/10.7554/eLife.81810.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "ATRAP – Accurate T cell Receptor Antigen Pairing through data–driven filtering of sequencing information from single–cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Michael E Birnbaum (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

This paper is of interest to immunologists conducting single–cell analyses of T–cell recognition. It provides a means of curating datasets to ensure T cell–antigen pairs are identified. However, the data generated through this method often suffers from a relatively high background. The authors present a computational approach to enhance signal–to–noise of this type of analysis. However, from the reviewer's comments, it is unclear if the thresholds and filtering steps described by the authors can be generally applied to other datasets of different qualities than the one used here. The reviewers make suggestions to better stress–test the robustness of the method. Overall this is a potentially valuable contribution but requires additional benchmarking and more clarity on the limitations of the approach.

Essential revisions:

1) The manuscript is more suitable for an eLife Resource given that it is entirely methodological and does not shed new biological insight.

2) There is a need for benchmarking the data against other datasets to assess the robustness and optimal threshold selection.

3) Ensure that the code and data used in the manuscript are publicly available so others can use the method.

4) Address reviewer comments about other technical concerns.

5) Consider the limitations of the study in the revised manuscript and title.

Reviewer #1 (Recommendations for the authors):

1. It will be helpful for the figures in the manuscript to be of higher quality (vectorized) for publication – there are areas where figure quality made data interpretation difficult.

2. Line 34 – MHC should be defined.

3. Line 55 – a and b should be changed to α and β.

4. In figure 2, it is difficult to distinguish between HLA match True and False. May it be worth having the two in different colors?

5. Lines 116 – 121: It would help to clarify the use of the PE–multimers a bit more, than by using them while sorting for APC–only, it ensures that any PE–based signal is purely due to solution–based noise rather than cellular contamination. This was something I only fully understood after reading through the paper once.

6. In lines 160–168, the authors state that 28000 cells were sorted and 45% of the cells were lost in the loading process. It would be helpful if the authors could clarify how were these numbers generated. Were 28000 cells a proxy for 28000 sorted events? How did the authors know that 45% of cells were lost in the process and only 15,700 cells were loaded on the 10X?

7. Based on the observations and discussion in lines 288 through 298, it might be helpful if the authors explicitly stated that they are defining true binders = expected binder=significantly most abundant pMHC for a given clonotype, rather than as defined through orthogonal means.

8. On line 204 the authors mention that the three negative control pMHCs were only present in a few GEMs. However, are these barcodes were captured as ambient contamination or were they captured with distinct clonotypes?

9. Line 274–275: The authors state that for GEMs with TCR multiplets, they take the most abundant chain for analyses. It would help if this were clarified. Is this the most abundant UMI per GEM (so if a given GEM has ⍺1 with 10 UMIs and ⍺2 with 8 UMIs, it counts as ⍺1 ), or the most abundant call per clonotype? (so if there are 5 GEMs with ⍺1 with the most UMIs and 3 GEMs with ⍺2 with the most UMIs, the entire clonotype is called for ⍺1 )? Does this analysis already remove any ⍺ transcripts that are recombined but out of frame or contain stop codons?

10. Line 479–482: The percentages for HLA match and mismatch are provided – what would the probabilities be expected if by chance?

11. Lines 531–535: The authors should further clarify why differences in fluorescence signal may account for differences in analysis for the single–cell sequencing vs FACS, especially given the fact that the sequenced cells are also sorted via FACS before 10x analysis. Is there a difference in avidity and/or concentration between the two staining reagents used?

Reviewer #2 (Recommendations for the authors):

1) Please explain what was the motivation for doing the experiment. Are the donors seropositive/seronegative for CMV/EBV/Flu? Why were these particular epitopes selected? What was the phenotype of sorted cells? What was the hypothesis?

2) Please make the raw data, processed data, and code available. The main strength of the paper is the robust code which could be potentially used to clean up other datasets of the same kind. The link to github returns 404 error.

3) It seems that the approach is not robust in the presence of cross–reactivity. If there are two different pMHC complexes loaded with highly similar peptides recognized by the same clone (and thus two pMHCs with different barcodes bound to the same cell), how the specificity will be assigned (and how will it influence UMI threshold selection, lines 344–345)?

4) It seems that TCR similarity metrics (both for inter and intra–similarity) are defined as maximal similarity values across all the comparisons within the same peptide assignment, or others, lines 888–891. This value should be systematically biased by the sample size (the more pairwise comparisons we do, the more extreme similarity we will find, even if the underlying sequence distance distribution is the same). It is not clear to me, how authors normalize this effect (do they downsample to the minimal number of unique clonotypes across all epitopes)?

5) Figure S1 shows sharing of VJCDRab between GEMs. How will this plot look if we consider sharing of a single chain nucleotide sequence (VJCDR3a_nucleotide or VJCDR3bnucleotide) between GEMs? If a clone has two alphas, will the proposed pipeline split it into two different clonotypes?

6) Please discuss and compare the data analysis strategy to the one from the following recent manuscripts:

https://www.science.org/doi/10.1126/sciimmunol.abk3070

https://www.nature.com/articles/s41590–022–01184–4

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9184244/

7) Line 318 mentions Figure 1d (probably instead of 2d)

Reviewer #3 (Recommendations for the authors):

– It will be clearer if the authors could provide a workflow of ATRAP that describes the key steps in the bioinformatic process.

– The cell number loaded on the 10X Chromium for each donor shown in supplementary table 4 indicated the GEM counts for each donor were less than 264. It would be important for the authors to comment on cell numbers and what threshold would be sufficient to perform this method. This would enable future users of the technique to have more guidance in decision–making.

– For experimental control, the authors only use three additional pMHC multimers bearing a different fluorochrome (PE). However, it would be more interesting to see if the authors could include negative pMHC multimers bearing the same fluorochrome (APC) to estimate the background binding noise for each donor and to check if the ATRAP could successfully remove those negative pMHC multimers.

– In this study, the author only used IEDB (Vita et al., 2019) and VDJ (Bagaev et al., 2020) databases to prove the detected specificities in their data have been cross–referenced on only five clonotypes. However, the author did not provide experimental evidence showing the pMHC selected by the ATRAP is a real target of a specific clonotype and that those pMHCs removed by the ATRAP are not the target of that clonotype. This may be a rather intensive set of experiments to show this, but the authors could consider it or at least make some statements/caveats if they choose not to do such additional validation.

– At lines 654–659, the authors write that low–avidity clonotypes might appear like noise, but this method is only able to detect the binding affinity, not the avidity. The binding affinity of TCR is not always correlated with avidity. I wonder if the information in their dataset really provides avidity measurements.

– At lines 344–345, it said that "This filtering analysis resulted in optimal thresholds of 2 pMHC UMI counts and a ratio pMHC UMI counts between top one and two >1". Is it possible if the sequence results are deeper that it might result in more noise or background pMHC UMI counts, in such a case, how would one adjust the optimal thresholds?

– In general, I think readers would find the V and J gene usage, along with other immune repertoire information interesting for all pMHC binders. The authors should consider this, perhaps as supplementary data.
