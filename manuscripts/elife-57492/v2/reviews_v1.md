# Peer review - Round 1

Editors:
- Gene W Yeo, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57492.sa1](https://doi.org/10.7554/eLife.57492.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article presents an interesting link between alternative polyadenylation, decay rates and genetic variation in gene expression control.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Alternative polyadenylation mediates genetic regulation of gene expression" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work cannot be considered further for publication in eLife, at least in its current form. However, a substantially revised version that successfully addresses all the major comments raised in the reviews below would be suitable for reconsideration.

Li and colleagues perform 3'seq on nuclear and total RNA to evaluate the diversity of alternative polyadenylation (APA) site choice from 52 lymphoblastoid cell lines. A surprising finding that is a large fraction of the nuclear fraction apaQTLs are intronic. This suggests that apaQTLs may contribute to eQTLs that are not associated with chromatin fractions and can lead to protein level changes without RNA abundance differences. A novel mechanism for genetic variants that modify ribosome occupancy of a transcript independently of its expression level is suggested. While the manuscript is certainly intriguing and highlights the potential importance of APA to human biology, which is of interest to the RNA and genetics field, there are many significant technical concerns that need reanalysis and clarification, in order for the biological implications to be sufficiently justified. The final results are somewhat underwhelming and in its current form insufficient to cross the threshold for publication in eLife.

Reviewer #1:

In this manuscript, Mittleman and colleagues contribute another layer of annotations to a historied collection of LCLs. By performing 3' Seq on nuclear and total mRNA, the authors are able to document the diversity of polyadenylation site choice in cells and the extensive regulatory activity occurring in between nascent transcription and steady state mRNA levels. They find that polyadenylation sites that produce nonfunctional transcripts (predominately but not solely in intronic segments) are invisible in standard RNA-seq datasets. Although they may be used uncommonly, these noncanonical sites may outnumber those in 3' UTRs. The authors extend the repertoire of QTL calling and learn that apaQTLs exhibit chromatin and other features distinct from those of eQTLs. More importantly, they find a novel mechanism for genetic variants that modify ribosome occupancy of a transcript independent of its expression level. However, while this work presents a transparently useful resource, the manuscript is conspicuously narrow in scope; it doubles down on alternate polyadenylation site architecture and chromatin state even when the identified trends are subtle at best.

1) The main takeaways (polyadenylation site choice is more diverse than expected, and traditional datasets obscure the role of alternative polyadenylation in mediating eQTLs) are cemented by the schematic in Figure 4C, but startlingly few figures address this point elsewhere. Figure 2D and Figure 3—figure supplement 3 and 4 are offered as supporting evidence, but the entirety of at least one main text figure should be dedicated to this in this reviewer's opinion. The principal findings simply need more attention.

Figure 1B elliptically addresses mRNA stability versus nucleus-biased transcripts, but there is a lot to unpack here. The panel title argues that polyadenylation choice is only weakly correlated, but the text takes care to establish a positive correlation. The trendline looks very ill fit to me. This is a rather critical point: is 3' Seq complementary, redundant or synergistic with 4su-seq? In other words, is 3' Seq really telling us something new, or is it recapitulating 4su? Additionally, Figure 2D is presented as critical evidence, and I feel that more should be done to bolster it. I was under the impression that more apaQTLs were called in nuclear than total mRNA fractions because transcripts had undergone decay. If effect sizes aren't changing, then does that mean both alleles of apaQTLs are equally disenriched in total mRNA fractions? The discussion does not take a clear stance on the relationship between alternative polyadenylation, translational efficiency and mRNA decay, which should be central to the message of the paper.

2) The majority of the plots delve into subtle differences of polyadenylation in various transcript elements (like introns and UTRs) and in nuclear mRNA versus total mRNA and for explained or unexplained QTLs. While these figure panels may show some slight differences (e.g. Figure 3), this leaves the reader with questions.

What percent of nonsense-mediated decay is dedicated to screening prematurely polyadenylated transcripts? For simultaneous apaQTL/eQTLs, approximately what percent of eQTL variance could be explained by apaQTL variance? Is the same extent of intronic alternative polyadenylation in nuclei observed in other cell types? Does higher variance in alternative polyadenylation for a transcript correlate with higher variance in ribosome occupancy (irrespective of QTLs)? Are alternatively polyadenylated sites enriched for heritability for a panel of traits (i.e. using LD score regression)? More conserved? Are genes with more frequent alternative polyadenylation longer? More highly expressed? Expressed more selectively across tissues? Enriched for certain gene annotations (e.g. GO terms)? More likely to contain certain RNA-binding protein motifs? More likely to bind RBPs as shown by CLIP? Less likely to be annotated with multiple transcription start sites?

3) The manuscript is not an easy read. Even with the current results, the format and layout would be daunting for generalists unfamiliar with this subject matter. Figures are called out too soon in some cases. Axis and panel titles frequently obfuscate rather than illuminate the subject matter. Numerous tracks are illegible at true size and somewhat difficult to discern even in the zoomed in figures (nonetheless a very helpful addition to the manuscript). These points really do need to be addressed.

4) The content of Figure 4 is quite anecdotal. Ideally there would be follow up work on the mechanism of riboQTLs or pQTLs without eQTLs. It may also be appropriate to combine Figures 3 and 4 and send some panels to the supplementary materials.

Reviewer #2:

In this paper, Mittleman et al. used 3' seq to analyze alternative polyadenylation (APA) isoform expression levels in nuclear and total RNA fractions from 52 lymphoblatoid cell lines. They identified about 600 apaQTLs in both fractions. A surprising finding is that a large portion of the nuclear fraction apaQTLs are intronic. They indicate that apaQTLs may contribute to some eQTLs that have not been associated with chromatin functions and can also lead to protein level changes without RNA abundance difference. Overall this proof-of-principle type work highlights the functional relevance of APA to human traits, a message that is of value to both RNA processing and human genetics fields. The experiment and data analysis were well carried out in general. However, some aspects of this work need further polishing and alternative explanations need to be considered in their data interpretations.

It is not clear to what extent internal priming cases have been addressed. The QuantSeq kit uses oligo(dT) for RT priming, which can lead to substantial internal priming at A-rich regions of RNA. Even though the authors seem to have employed a rigorous computational approach to cull their data, internal priming cases can still exist. One way to gauge the extent is to check the nucleotide frequency profile around the polyA sites that matched polyA DB vs. those did not. If internal priming problem persists, they would see an A-rich peak around the polyA site for those non-matched sites. This issue is highly relevant to their conclusion, because many of the intronic polyA sites could well be A-rich regions in retained introns. As such, some of the cases might in fact be intron retention rather than intronic polyadenylation.

For intronic polyA regulation, the authors need to consider the possibility of variations of 5' splice site strength and/or intron size (through insertion or deletion), which were shown to be important for intronic polyadenylation by Tian et al., 2007.

The authors claim that the relative number of nuclear seq reads to total reads is indicative of RNA decay. This is not well supported by their data. The data shown in Figure 1—figure supplement 1 had a quite dismal correlation coefficient and the p-value is not 2.2x10-16 as mentioned in the main text. The possibility of nuclear export control, in addition to decay, should be considered.

The description of ribosome occupancy is quite scant. Because intronic polyadenylation would truncate transcripts, change of ribosome occupancy could be simply due to transcript size change (thus ribosome number per nucleotide changes) rather than ribosome number per transcript. The authors need to distinguish these two different scenarios.

Reviewer #3:

The authors are studying genetic variation that affect APA. While there has been a fair amount of interest in the study of eQTLs the focus on this specific mechanism is less explored. This summer there was a fairly large study of genetic variation and apa published this summer (PMID: 31475030). It may be appropriate to mention this work to set the study in the appropriate context. Nevertheless, there are novel contributions in this study that offer more resolution in terms of mechanism. The work uses 3' RNA-seq (3' Seq) to measure PAS usage in whole cells as well as the nucleus for the purpose of distinguishing differences in PAS usage from differential stability. The use of lymphoblastoid cell lines was a good decision given the deep characterization of this resource in the literature. In general, the study is thorough and makes a solid contribution. I felt that the all the computational analyses were thorough, appropriate and executed well. On the negative side, there is a potential limitation that the functional consequence of the events cannot really be determined from the relative RNA-seq measures in nuclear versus whole cell. It is possible the eQTL that trigger APA create changes in isoform ratios but these are not reflected in ribosome/polysome associated transcripts. In general, I struggled to identify any single high impact discovery but in its totality there is significant biology in the paper in terms of the discovering how variants expressed gene expression.

In terms of impact and broad appeal, I would think this would be appropriate for eLife.
