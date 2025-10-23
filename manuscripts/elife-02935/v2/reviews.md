# Peer review - Round 1

Editors:
- Todd Golub, Broad Institute , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02935.027](https://doi.org/10.7554/eLife.02935.027)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Origins and functional consequences of somatic mitochondrial DNA mutations” for consideration at eLife. Your article has been favorably evaluated by Stylianos Antonarakis (Senior editor), a Reviewing editor, and 3 reviewers.

The editors and the reviewers discussed their comments before we reached this decision, and the Senior editor has assembled the following comments to help you prepare a revised submission.

The substantial concerns of the 3 reviewers are:

Reviewer 1:

1) Is the generated sequence data accessible through a public repository such as GEO? Are database accession numbers provided somewhere in the manuscript.

2) Figure 3–figure supplement 1 is an example of possible artifacts in the authors' results/interpretation. This figure compares the substitution rates between 12 coding genes on heavy strand vs 1 on light strand, but information on how the graph was generated for the 12 genes cannot be found. Does the graph show the sum or average of observed substitution rates? If it is based on average rates, should there not be error bars or p-values from t-tests. Also, why are the 12 genes shown for the L strand, and the 1 gene as the H strand?

3) In Figure 4, what are the authors trying to demonstrate with Figure 4A? What do arrows beside the “box” indicate? What do the different colors of the arrow (blue and red) mean? Why is the “box” designed for the light strand sequence when it has only 1 out of 13 protein-coding genes? What does skew mean here?

Reviewer 2:

1) Do the authors observe differences between tumor types in terms of the relative proportion of negatively selected somatic mutations that are hetero- vs. homoplasmic? This may indicate differential (negative) selective pressures in different tumor types (e.g. negative selection could be less pronounced in tumors with a low rate of oxidative phosphorylation).

2) The authors suggest that the major explanation for lack of visible exogenous mutation signatures (i.e. such related to tobacco smoke or UV light exposure) is that the endogenous mutation rate in mitochondria is several orders of magnitude greater than the exogenous mutation rate. Can the authors, based on the rate of nuclear genome somatic mutations in tumors with pronounced exogenous mutation signatures (i.e. using data from earlier works by the authors) provide an estimate for the relative difference in endogeneous vs. exogeneous mutation rate?

Reviewer 3:

1) Several studies have already used massive parallel sequencing data for the identification of heteroplasmic mutations in cancer (He et al Nature 2010) and in normal samples (Goto et al 2011; Avital et al 2012; Payne et al 2013). These studies already set the standards for such analyses, which to a large extent were overlooked in the current manuscript. As an example, the authors used a threshold of >3% of the reads to be considered as trustworthy heteroplasmic mutations but the minimum coverage that they used does not allow such a threshold (10X!). Other studies used at least 100X (a minimum) or even 1000X coverage (preferable) and a threshold of 1.5% of the reads. Apart from the threshold issue, while considering secondary reads in the mtDNA (heteroplasmy) one should apply several filters such as 'no strand bias', unique mapping (NuMT exclusion) and 'exclusion of mutations at the end of reads'. These should be used in the revised manuscript and the list of mutations should be updated accordingly. These filters are especially important, since the authors give much weight for their strand bias hypothesis and replication-associated mutations. However, nothing is mentioned as to how the authors account for strand bias (i.e. mutations present mostly in forward or reverse reads). Until they exclude sequencing artifacts, including those resulting from strand bias, they cannot interpret the data as actual biological strand bias.

2) The authors claim that their analysis was unbiased and generated a catalogue of somatic mtDNA mutations. However, they excluded all candidate somatic mutations that recapitulated known mtDNA SNPs. The exclusion of SNPs is understood while considering the nuclear genome, however unlike the nuclear DNA the mtDNA molecule is in full linkage disequilibrium. This means that in order to avoid sample contamination the authors should exclude mutations in SNP positions ONLY when they phase along with other SNP mutations to form a haplotype.

3) The functional potential of mutations is not properly analyzed: dN/dS ratio calculated for genes does not reflect the functionality of specific mutations. Some estimation could be given by manipulations of this ratio using PAML or SELECTON. However the best way to assess the functional potential of variants is a comparison to disease causing mutations.
