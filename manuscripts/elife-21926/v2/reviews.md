# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21926.031](https://doi.org/10.7554/eLife.21926.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Global reorganisation of cis-regulatory units upon lineage commitment of human embryonic stem cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Job Dekker (Reviewer#1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Fiona Watt as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Frank Alber (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. In the course of discussion the reviewers and editors decided that this work would be more appropriately reconsidered as a Tools and Resources (TR) paper rather than a Research Article (RA). The work appears to be a valuable resource but the primary research results are not considered sufficiently novel to warrant publication as an RA. Nonetheless, we hope you are willing to go forward with this in the category of a TR paper.

Summary:

Freire-Pritchett et al. employ Capture Hi-C to detect chromatin interactions between promoters and distal elements in ES cells and in ESC derived neuroectodermal cells (NECs). The authors report significant interactions between many promoters and different distal elements in ESCs and NECs. Analysis of the chromatin state of these elements indicates that these are functional elements including (poised) enhancers. Further, the connectivity between promoters and distal elements differs between ESCs and NECs and this relates to the transcriptional status of the genes and chromatin status of the distal elements. The authors then define cis-regulatory units (CRUs) as promoters and their associated distal elements. Although many of the CRUs are contained within TADs and INs, as had been expected based on earlier studies, the authors report that many can extend beyond TAD and IN boundaries.

The main impact of this paper is to announce the availability of a large data set of enhancer-promoter contacts identified via capture Hi-C. Many of the experimental technologies and statistical analysis methods are established and rely on previously published methodologies. That said the reviewers raise concerns about specific aspects of the analysis. Further, many of the reported correlations are already known and the results confirm earlier studies (e.g. promoters interact with multiple distal elements, these elements coincide with cell type-specific enhancer-like elements and these connections are equally cell type-specific, and enriched for intra-TAD interactions). The main new aspect of this work is the fact that a genome-wide promoter-anchored interaction atlas is described, and this resource could be of interest to the community given that many study these cells.

Essential revisions:

Please address these main criticisms (more details are in the minor points section):

1) Many of the correlations between looping, gene expression and chromatin state are not novel. Focus on the new things, and present the data as a large dataset or resource for the community.

2) The reviewers raised issues related to the statistical analysis and computational methods to determine PIRs (and their hierarchical clustering), TADs, and CRUs (below). Please address all of them.

3) Related to the previous point, the reviewers raised concerns about the claim that CRUs are distinct from INs, TADs. The main point to address is how the methods to determine these features compare and whether lack of overlap can be due to sensitivity of the computational methods.

Minor points:

1) One concern is that the CHiCAGO method identifies significant interactions using only the general distance decay of interactions into account. It does not take into account that any pair of interactions between loci located within a TAD or IN, or between loci located in a similar compartment (A, B or subcompartment types) are generally higher than loci located in different TADs/INs/Compartments. As a result, a number of significant interactions are not necessarily "loops" (specific point-to-point interactions). This is not to say that these loci do not interact more frequently than expected given their genomic distance, but these interactions can reflect general higher order structures such as domains etc. This can explain why many interacting loci appear to not have chromatin marks: these can be "bystander" interactions that are the result of a nearby structural feature. I recommend that the authors repeat their analysis using a background model that takes domains into consideration.

2) The TAD calling procedure is quite simple. Is there any evidence that this procedure produces TAD calls of comparable quality to those produced by, for example, the HMM of Dixon et al. Nature 2012?

3) The TAD and IN comparison is unsatisfying. The main conclusion seems to be that CRUs are not particularly aligned with TADs and INs. This could be because the two phenomena are more or less independent of each other, or because the TADs, INs and CRUs are each defined in a fairly arbitrary fashion. If, for example, the simple TAD calling scheme employed here is not working well, then it would lead to the observed discordance.

4) The finding that CRUs can extend beyond TAD or IN boundaries is interesting, but the data is not sufficient to claim a new "feature of genome architecture". Further analyses are needed such as: when a CRU extends beyond a TAD boundary, is this a weak TAD boundary? It is well known that TADs are nested structures. Do CRUs remain within the larger nested domains? This seems to be the case for POUF2. Quantification of boundary strength is required, as it seems not inconsistent with the TAD/IN models of enhancer action if the authors find interactions across weak boundaries, but not strong boundaries. Also, are these interactions beyond the boundaries equally strong, or are they much lower in contact frequency

5) The main text claims that the promoter capture Hi-C data was processed to identify "significant cis-interactions." Looking at Methods, we learn that these contacts correspond to a threshold of 12, on a "log-transformed, weighted p-value" scale. This vague description makes it impossible to actually interpret the confidence associated with a threshold of 12, especially since we are told that the threshold corresponds to "a threshold of 5 in Chicago v1.0.0+ due to a soft-thresholding procedure introduced in this version." The choice of threshold must be fully justified and described. The text claims that Chicago uses an FDR control procedure, so the interactions that are presented here should be reported along with their FDR threshold.

6) The manuscript contains no details on precisely how ChromHMM was run. Details like software version numbers and any parameter settings should be given. Importantly, the text should specify whether the segmentation was carried out independently on each cell type, or jointly, and if the latter, whether the data tracks were "stacked" (i.e., 8 marks per position) or "concatenated" (4 marks per position, across two concatenated copies of the genome).

7) Details of the "curation" of the 16 inferred states should also be provided. When the 16 states were collapsed to four states, what was the basis for this collapsing? It seems strange that some states were eliminated at this stage because they contained multiple marks.

8) How are PIRs defined: at the level of individual restriction fragments, or are adjacent fragments that both score significant merged into a single PIR?

9) The authors do not show many tracks of real data (only in one of the supplemental figures). Throughout they only show arcs to indicate significant contacts. This makes it difficult to assess the quality of the data.

10) Promoters often interact with CTCF sites. Did the authors find this in their dataset as well?

11) The authors focus on cis-interactions. Can the authors describe trans interactions as well? Given that trans-regulation is considered rare, this analysis will provide context for interpretation of the cis data.

12) Did the authors detect any known enhancer-promoter pairs? Also, the authors imply that the distal elements that touch promoters are regulating these promoters, but beside correlations between interactions, transcription and chromatin state of the distal elements, no evidence for direct regulation is provided. This would require deletion of the elements, e.g. by CRISPR. The Vista analysis of the POUF2 interactions suggests that many PIRs are enhancers. That is similar in information as the observation that PIRs overlap loci with histone modifications associated with enhancers. The key thing to validate is that these enhancers indeed regulate the interacting promoter. The fact that the pattern of activity of these enhancers resembles POU3F2 expression is encouraging but not definitive. The authors should either provide direct evidence for functional relationships or clearly discuss the extent to which the current data predicts such relationships even though the data currently is correlative.

13) The authors examine the dynamic rewiring and recoloring of interactions as cells differentiate from ESCs to NECs. They report gain and loss of interactions and these are related to gain or loss of chromatin marks. This is interesting, but what needs to be tested is whether this is related compartment changes (see above). This is not to say these interactions are not relevant, but it would be important to determine how they relate to larger scale compartment changes. One interesting implication could be that in fact cell type-specific compartment changes are driven by altered interactions between functional elements that are active in a cell type-specific manner.

14) How do the authors interpret interactions that involve non-expressed genes?

15) The hierarchical clustering of PIRs by the prevalence of different chromatin state labels is fairly uninformative. The fact that these different categories exist in the data is not surprising, and the claim that these eight labels somehow have "potential implications for understanding the logic of signal integration at promoters" is not well supported.

16) In the Abstract, the sentence "Here, we generate[…]" should mention what assay was employed.

17).In the Introduction: "The extreme combinatorial complexity of Hi-C[…]" The complexity is really only quadratic, not combinatorial.

18). In the Results section: The URL for data availability should be included at the end of the sentence, "This data resource[…]"

19) Also in the Results section: "NEC PIRs were strongly enriched" This claim requires statistical support.

20) New paragraph at "We next sought[…]"

21) Two of the observations offered in the Discussion do not seem to be supported by direct evidence in Results: "we find extensive promoter connectivity to regions associated with Polycomb-associated repression and poising, and "we[…] detect large numbers of promoter interactions with regions devoid of chromatin features." These observations seem to be offered for the first time in Discussion.

22) The work does not show whether all the interactions are present simultaneously in a cell, or if the promoter state may vary between cells, depending on the probability with which the promoter is interacting with any of the potential alternative enhancers of a given chromatin state. Please discuss this issue in the main text.

23) Out of the ~21000 promoters, the authors focused their CRU analysis on only 16,000 protein-coding genes. Would the authors expect differences in the outcome if the other remaining promoters would be considered?

24) Out of the 16,000 protein-coding promoters about 9000 were defined as CRU. It may be good to know the selection criteria (i.e. is it based on a minimum number of PIRs per promoter?).

25) Figure 3B defines a CRU as a set of PIRs that seem to be concurrently interacting with the promoter in the same cell. Maybe the authors could indicate in the caption that it cannot be ruled out that some PIRs may provide alternative rather then concurrent interactions.
