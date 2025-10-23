# Peer review - Round 1

Editors:
- Stephen Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41673.039](https://doi.org/10.7554/eLife.41673.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genetic effects on promoter usage are highly context-specific and contribute to complex traits" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Stephen Parker as the Reviewing Editor and Mark McCarthy as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Roger Pique-Regi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Most transcript usage QTL (tuQTL) studies do not differentiate between events leading to differential isoform usage, such as alternative promoter, alternative 3ʹ end, or alternative splicing that are a likely consequence of different molecular mechanisms. Alasoo and colleagues describe the development of such a tool – txrevise, which processes (Ensembl) transcript annotations to build an annotation of independent promoters, internal exons and 3' ends for use with an external tool such as Salmon for transcript quantification. They additionally map genetic associations for total gene expression, full length transcript usage and exon-exon junction using established methods and compare the approaches and results to those from txrevise. The authors show that promoter usage QTLs are generally more context specific and colocalize with genetic signals for complex traits. The approach is sound, and the methods/observations will be helpful to the field. The paper is well-written and we think will be appealing to a broad audience. However, there are several points that should be addressed, which we outline below.

Essential revisions:

1) There were two QTL scans done, where the initial scan happened over a smaller window. Was there any instance where the larger +/- 500 kb scan resulted in a stronger signal compared to the initial +/- 100 kb scan? If so, how were these treated?

2) More details about assignment of groups 1 and 2 during the txrevise process would be helpful. Surely there are examples that are not as simple as the one depicted in Figure 1—figure supplement 3. How are those more complicated cases treated? Another way of phrasing this: how do you decide when to choose more exons vs. fewer transcripts? Clarification of this approach will be helpful.

3) The word "group" may have different meanings in different sections of the txrevise methods. For example, in the last paragraph of the subsection “Quantifying transcriptional events with txrevise”, "group" describes the two different approaches to creating common scaffolds. At the end of the same section of the Materials and methods, it's not clear here what "group" means. Does it mean as above (the two different scaffold approaches) or one of the three different categories (promoter, internal, 3ʹ UTR)? Clarity here will be helpful for other labs that want to use this approach.

4) Not clear how multiple testing correction happens with txrevise – are you using the --grp-best flag across all the separate bits (promoter, internal, 3ʹ UTR) of a gene model, or only within the three different partitions? And what about across the two groups that are created? When mapping multiple QTLs, it is not clear if the authors map them all simultaneously or if they use a conditional on the lead QTL strategy. The authors should clarify this.

5) In Figure 2B, authors performed a replication analysis of QTLs. This appears to be only based on the LD between the lead QTL variants for different comparisons. However, the direction of effect size is ignored. This should also be included in all the replication analyses.

6) Given that promoter shifts are an important component of context specific tuQTL and are also enriched for complex traits, the authors could use their ATAC-seq data to further illustrate the mechanism and perhaps validate. Are changes on promoter usage dependent on the promoters being open? Do these types of tuQTL also have a QTL on ATAC-seq on the promoters? Even if the outcome is negative, which might indicate a more complex relationship between promoter usage and chromatin accessibility, this would further strengthen the manuscript.

7) The coupling part was uniformly perceived as weaker compared to the rest of the work and could be removed as it is a bit orthogonal to the main focus, especially considering it is not tied to any main figure.
