# Peer review - Round 1

Editors:
- Richard P Harvey, Victor Chang Cardiac Research Institute Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31683.020](https://doi.org/10.7554/eLife.31683.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Tbx5-dependent enhancer transcription defines a gene regulatory network for cardiac rhythm" for consideration by eLife. Your article has been favorably evaluated by Didier Stainier (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Philip Grote (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an excellent paper both conceptually and technically, and contributes to our general understanding of the role of ncRNAs in enhancer function, and more specifically how individual TFs can control a set of TF-dependent ncRNAs that define enhancers functioning in a cell-specific network. The manuscript describes their work to refine the TBX5 dependent gene regulatory network, required to maintain atrial cardiac rhythm. The make use of a diverse mixture of published datasets (TBX5 ChIP, H3K27Ac ChIP, DNaseI HS) and complement them with their own, new datasets (ATAC-seq, RNA-seq). They go on and show that the expression of eRNAs (enhancer RNAs) improves the predictions of functionally relevant atrial TBX5 dependent enhancers. Moreover, they show the functional relevance of some of the newly discovered eRNAs in regulating nearby genes.

The concept that the eRNAs participate in regulating neighboring genes and the TFs such as TBX5 are actively involved in driving eRNAs is not novel. However, some aspects of their work provides further insight (ncRNA-mRNA correlation in expression strength) and the comprehensive identification of functionally relevant TBX5 enhancers is interesting to the cardiovascular community. The novel approach outlined for identifying functional enhancers and associated ncRNAs could see broad utility in systems biology. However, there are some major issues to address as detailed below:

Essential revisions:

1) The manuscript style is very compact. It may help more general readers to expand explanation of methods and graphical approaches. The first part of the paper (text and Figures 1 and 2) is especially difficult to follow and some work (perhaps from the biologist) is needed. We would recommend that the paper be structured around the series of results and clearly relate how one observation leads on to subsequent analyses and results.

2) Main text, third paragraph: regarding hypothesis: presumably the authors mean active enhancers (those functioning in a specific tissue).

3) Main text, third paragraph: please define de novo? Do the authors mean previously unannotated?

4) Main text, fourth paragraph: please clarify uni-directional and bi-directional?

5) Main text, sixth paragraph: how were candidate regulatory elements chosen for transcriptional analysis. Were they chosen from among those with highest number of Tbx5 canonical sites? Please declare.

6) Main text, eighth paragraph:. The story about Sln is confusing. The text might read as though the Sln regulatory element does not contain Tbx5 binding sites as the prelude refers to those that lack Tbx5 binding. But in fact it does (Figure 2C). What about the category of elements that do not contain Tbx5 sites. What did they show by Tbx5 ChIPseq and were any analysed by Tbx5 ChIP PCR?

7) Please explain the line scans in Figure 4E, F.

8) Since the experiment was performed using a single knockdown reagent, Figure 4A could benefit from other specificity controls. E.g. was Tbx5 or signalling or metabolic genes (not those highly expressed like GAPDH) unaffected.

9) Main text, fourteenth paragraph and Figure 4D. The authors should be very clear about the results of the zebrafish enhancer analysis. As it reads, 67 of 166 embryos showed cardiac expression driven by the RACER-associated enhancer (40%). Mutation of the 7 T-box sites reduced this to 20/84 (23%). This is not a compelling argument for identification of RACER as a Tbx5-dependent element or the function of Tbx5 on this element. While the p value is significant the use of an odds ratio seems rather unusual for this sort of analysis. The assay is poorly quantitative and each injection will lead to a different integration site. Spatial specificity (e.g. atrial) was not scored. I think this should be strengthened or deleted. It would be more compelling to delete the natural enhancer and analyses Ryr2 expression by qRT-PCR.

10) Please explain the line scans in Figure 4E, F. Please correct references to Figure 4 panels in Legends. Check all.

11) Main text, sixteenth paragraph: chromatin enrichment assay. What does this mean? A ncRNA that does not associate with chromatin in the way suggested but, e.g. is a structural component of a TF or splicing complex, may also appear enriched in chromatin. Furthermore, GAPDH seems an inappropriate control. One could use NEAT or another known ncRNA that does not appear to define an enhancer.

12) In the end, the mechanistic link between TF-dependent ncRNA function in transcription of the adjacent genes is not strong. The Pol2 occupancy data is interesting but self-fulfilling. Would knockdown of the RACER change the chromatin landscape around Ryr2 by 4C?

13) It is not clear to the reader why the authors combine H3K27ac and DNAseI HS sites from the whole adult heart with atria specific data (TBX5 ChIP, ATAC, RNA-seq). It should be clearly stated that H3K27Ac and DNaseI HS marks putative, open (active) enhancers in the whole heart, including the atria. Combining ATAC-seq and TBX5 ChIP-seq data are from the HL1 atrial cardiomyocyte cell line and RNA-seq from atrium from cKO mice provide the atria specific data. Please explain in more detail, why you used all the comparison with whole heart data.

14) In the Materials and methods it is mentioned that P300 ChIP-seq data from He et al. was downloaded. Please explain why you didn't use these data for your work? Was it removed? I think could be an interesting addition to see, how the functionally relevant ncRNA regions correlate (or not?) with P300 occupancy.

15) A critical concern is the interpretation of statistical evidence for various enrichment and differential expression analyses. In a number of instances, it appears from the manuscript that significance was determined at a nominal significance of p<0.05 even when a large number of tests were conducted. Was significance determined based on a multiple-testing adjusted p-value?

Throughout the manuscript evidence is often presented in a qualitative manner, making it difficult to judge what weight should be placed on it, and difficult to evaluate the conclusions drawn from it. For example, 'we observed enrichment between…'. It would be helpful to know what level of enrichment and what scale that is on. Also an empirical p-value for said enrichment. Likewise 'we functionally interrogated candidate regulatory elements..' what does functionally interrogate mean? 11/12 have p<0.05, but no correction for that fact that 12 elements tested, so threshold needs to be adjusted. This occurs throughout the manuscript.

I believe that this paper would benefit significantly from using an empirical random-sampling strategy to determine significance of any enrichment. For example, when testing your n TBX5-dependent ncRNAs for enrichment in the 16,000 open regions, randomly sample n regions, determine how many are also candidate Tbx5-dependent enhancers (this value can be called k). Repeat 10,000 times. The position of your observed overlap in the ranked k gives an empirical p-value.

16) In any instance where a p-value is given, you should also provide the test used to estimate it.
