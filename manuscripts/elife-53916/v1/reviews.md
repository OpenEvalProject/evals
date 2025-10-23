# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53916.sa1](https://doi.org/10.7554/eLife.53916.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Zygotic pioneer factor activity of Odd-paired/Zic is necessary for establishing the Drosophila Segmentation Network" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Oliver Hobert as the Reviewing Editor and Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erik Clark (Reviewer #2). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All reviewers are in agreement that this is a very nice, interesting study that is of general importance. No additional experiments are required but we all agree that there are a number of editorial changes, clarifications and writing changes that need to be implemented before the manuscript becomes acceptable. Those are detailed in the reviews appended below. In addition, reviewer #1 suggested in points #1 and #2 an additional analysis of the ChIP peaks, which require no further experimentation, but may provide some additional insights; please try to perform this analysis (the experimental analysis suggested in point #3 by reviewer #1 was deemed to not be essential and does not need to be done).

Reviewer #1:

Soluri et al. identified widespread changes in accessibility of cis-regulatory elements of patterning genes as the Drosophila embryo undergoes gastrulation. Using a powerful quadruple mutant embryo and ATAC-seq, the authors demonstrate that the majority of these changes in accessibility are driven by developmental time and not dependent on patterning itself. They identify Odd-paired (Opa) motifs underlying regions that gain accessibility during gastrulation and using a combination of ChIP-seq and ATAC-seq demonstrate that Opa has some defining features of pioneer factors. In general, this is a well-executed paper addressing an important and interesting developmental question.

1) It would be useful to compare the number of peaks identified without using the IDR analysis for comparison with other data sets that do not use a tagged allele and therefore cannot use an IP from wild type as control. If additional peaks are identified in this less stringent analysis are these peaks enriched for a centered Opa motif? This might suggest that the stringent methods used are only identifying the most robust Opa-binding sites. Given that the ATAC-seq analysis on the opa mutant is only focused on these regions some additional information could be gained from looking at potential additional sites.

2) Expanding the ChIP analysis is especially important given that the ATAC-seq analysis is centered only on those stringently identified Opa ChIP peaks. It would be important to more globally discuss the changes in accessibility identified in the opa mutant. These data appears to be all included in the comprehensive ATAC-seq peak list, but should be discussed. How many loci overall gain and lose accessibility? How many of these overlap the stringently called Opa peaks? The focus on stringently called Opa peaks is understandable, but to more broadly assess the impact of the loss of Opa on accessibility, it is important to report all identified changes and not just those that overlap direct targets. Are there motifs selectively enriched in the Opa-dependent vs. Opa-independent regions bound by Opa that might suggest factors that maintain accessibility in the absence of Opa? Is there an enrichment for any genomic regions (enhancers, promoters)?

3) While it is nicely demonstrated that Opa influences chromatin accessibility at sites where it is bound, the downstream effects of this accessibility remain largely unanalyzed. It could be useful to have some orthogonal analysis of the role of Opa on gene expression. Mutating the Opa-binding sites in the odd-late reporter and seeing if that is not expressed would be a useful demonstration of the direct role of Opa at this CRM. Alternatively, the global effect of Opa-mediated accessibility on gene expression could be analyzed by RNA-sequencing of either the opa mutant or the tub-opa overexpression.

4) The impact of this manuscript would be strengthened if the Introduction and Discussion were streamlined for clarity.

Reviewer #3:

Soluri et al. address the important question of the dynamic acquisition of genome accessibility during key developmental transitions. Specifically they focus on the 1h period of Drosophila embryogenesis, from ZGA to gastrulation, during which regulatory networks establish segmental identities across the A/P axis.

By performing single embryo ATAC-seq on carefully staged Drosophila embryos prior to and at gastrulation, they identify a novel set of cis-regulatory elements that gain accessibility at later stages. Through an elegant genetic approach, where all A/P maternal cues are depleted to generate embryos with a uniform unique lineage, the authors were able to distinguish cis-regulatory elements that gain accessibility dynamically, specifically at late stages but in a patterning-dependent fashion.

The analysis of the sequences enriched in this category of ATAC-seq peaks revealed the over-representation of opa motif. While its role as a patterning gene during segmentation was already known, opa's requirement for genome accessibility is novel and nicely demonstrated by both loss and gain of function approaches in this manuscript. Overall I find the experiments presented in this work well-designed and the data of high quality. The manuscript is well written, and I particularly appreciated the tone of the last part of the Discussion where the limits of the study are well-stated.

General comments:

The WT and quintuple mutant embryos are compared at exact similar timing. Can the author comment on the developmental timing status of the quintuple mutant in terms of developmental delays?

Since a novel exciting finding of this study is the fact that opa acts as pioneer factor, it would be exciting to discuss a) the defining properties of a pioneer factor, and b) which of these properties opa seems to fulfil and which ones are still unclear. In such a discussion, a comparison with Zelda, which is the other pioneer factor shown to act as a quantitative temporal timer of gene expression, would be interesting. Additionally, the evidence that opa is able to engage its targets even in the context of nucleosomal DNA is currently absent. I agree that the bioinformatic analysis performed by the authors is consistent with this hypothesis; however, to avoid future confusion, it would be ideal to state it clearly in the Discussion.

Could the authors provide statistics: how many enhancers are analysed in Figure 3C, D and in Figure 1A? In Figure 3E, the number of peaks is indicated, but as an enhancer can exhibit multiple peaks, it's difficult to infer the number of CRMs considered.

Specific comments:

– The manuscript starts by focusing on a small set of known CRM within the segmentation network. Could the authors give a number for the number of segmentation network enhancers for which they observe a dynamic change in chromatin accessibility? Would it be possible to extend this analysis to another type of enhancers, such as the DV patterning network?

– Since the ATAC-seq data have been performed in carefully staged single embryos, it would be interesting to extract more information than the small set of segmentation enhancers.

– Since the authors performed opa ChIP-seq, can they examine if there is a correlation between the number of opa binding sites and the timing of accessibility?

– Could the authors discuss similarities and differences with the pioneer factor Zelda, as several studies (Foo et al., 2014, Dufourt et al., 2018, Yamada et al., 2019) demonstrate its function as a quantitative timer?

– In Figure 6, the authors employ a gene expression analysis on a subset of opa-dependent CRM to support the conclusion that 'the primary function of opa is to modulate the temporally restricted accessibility of a subset of critical CRM'. Although not essential for this manuscript, it would be very exciting to build MS2 reporter transgenes for these critical CRM (for example odd-late) and examine the effect of adding extra opa sites to see if this is sufficient to elicit a premature expression (again like Zelda does, as shown in Yamada et al. and Dufourt et al.).
