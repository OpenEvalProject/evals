# Peer review - Round 1

Editors:
- Maureen E Murphy, The Wistar Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64204.sa1](https://doi.org/10.7554/eLife.64204.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors have identified the importance of ALDH1A1 in preventing oncogene-induced senescence in precursor lesions of pancreatic cancer. Using a combination of sequencing, computational analysis and experimental work they find that ALDH1A is negatively regulated by ARID1A and that loss of ARID1A results in its upregulation and a decrease in intracellular ROS. This highlights a mechanism whereby PanINs prevent senescence and drive a pro-growth phenotype.

Decision letter after peer review:

Thank you for submitting your article "Single-PanIN-seq Unveils that ARID1A Deficiency Promotes Pancreatic Tumorigenesis by Attenuating KRAS Induced Senescence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Maureen Murphy as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please be advised that there was considerable discussion about your work, and that considerable revisions are requested by the reviewers. You may wish to create a plan of attack for the revisions and send this to the Senior Editor, who can share it with reviewers.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors have identified the importance of ALDH1A1 in preventing oncogene-induced senescence in precursor lesions of pancreatic cancer. By a combination of sequencing, computational analysis and experimental work they find that ALDH1A is negatively regulated by ARID1A and that loss of ARID1A results in its upregulation and a decrease in intracellular ROS. This highlights another new mechanism that is exploited by PanINs to prevent senescence and drive a pro-growth phenotype.

Essential revisions:

1. The conclusion that "a highly complex trans-differentiation occurs following the knockout of Arid1a" is not supported by the evidence provided in Figure S3. It is unclear what panels B and C are referring to (no labels) and there is no scale given. The authors also use the RNA-sequencing data to conclude that "the activities of Kras signaling are partially suppressed by ARID1A deficiency." This is a major point and should be supported by experimental evidence in their cell models.

2. Although Figure S5B shows that genetic manipulation of ARID1A was successful, there is no evidence by western blot or PCR that ARID1A has truly been knocked out in their HPNE cells. This model was used for a large portion of the data and must be characterized in a convincing way.

3. The evidence for senescence in vitro is not strong. Several times throughout, a colony formation assay is used as a measure of senescence, rather than SA-b-gal, molecular markers or secreted factors. It is unclear why the authors measured SA-b-gal staining intensity rather than %-positive cells. In particular, the evidence that ARD1A regulates Kras-induced senescence in HPNE cells is lacking.

4. It is unclear if the ROS phenotype is mediated by ALDH1A1. Therefore, the conclusion that "ARID1A knockout can effectively reduce cellular ROS level by upregulating the expression of ALDH1A1" is not supported.

5. There is no functional experimental evidence provided for how ARID1A regulates the expression of ALDH1A1. This is a major point of novelty in the paper and should therefore be supported by experimental evidence.

6. In the patients with pancreatic ductal adenocarcinoma, typically one sees point mutations, InDel or structure variations in the cancer genes; can the authors list the mutations in ARID1A in their samples to see if there are any recurrent mutations (i.e, visualized by lollipop plot, using ICGC-PACA-AU or ICGC-PACA-CA whole genome sequencing dataset, https://dcc.icgc.org/)? Can the authors perform an eQTL analysis (for example using FastQTL) to see if any mutations in ARID1A and +/- 1Mb cis-mutations are associated with the expression of ALDH1A1? The mutations and gene expression datasets could be readily downloaded from ICGC-PACA-AU or ICGC-PACA-CA (ICGC data portal).

7. The authors describe differences in proportions of distinct populations of ADM, PanIN-1, PanIN-2, PanIN-3 populations. At no point in their introduction/results do they describe the PanIN-1/2/3 populations. This would be a good addition for clarity. In addition there are no details on how these were quantified in the methods. In the introduction the authors state that previously ARID1A KO has been found to increased ADM – however Figure S1 shows the opposite that ARID1A KO leads to decreased ADM – while this reflects a trajectory of PanIN progression – not including any background on this is confusing and needs clarification.

8. How many genes in total were differentially expressed following MATQ-seq? Were lowly expressed genes removed? Was there any requirement that a gene was found to be expressed in at least N samples etc? These kind of filters are standard for scRNA-seq analysis and would seem to be appropriate for this type of data.

9. Using multiple pairwise comparisons is a restrictive way of analyzing this data – the authors should consider re-analyzing this data using an interaction test – trying to identify genes that respond differently to KRAS induction dependent on whether ARID1A is knocked out or not. Or consider an approach based on clustering of expression across differentially expressed genes to identify patterns of response across all four conditions. One prediction of the model the authors are proposing should be that SASP genes are upregulated in the KRAS vs WT but blunted in KRAS-ARID1A vs WT – is this observed?

10. Figure 3F: Figure 3F – please add a title containing the gene name – having the y-axis as ABM is confusing at first glance. Any supplementary table/data to show that ALDH1A1 was not in the list of DEG in AKC mice? Or to show that ALDH3A1 was? Is there a difference in regulation between species (i.e. both ALDH1A1 and ALDH3A1 are expressed, but only ALDH1A1 responds) or that only ALDH1A1 is expressed?

11. There is no comprehensive analysis linking the results from the in vitro MATQ-seq in mouse and the in vitro work in human. There is no discussion of whether orthologous genes are seen to up/downregulated in both. Linking together the results from the AKC vs KC lesions with KRAS-ARID1A-KO vs KRAS-Wildtype HPNE cells would allow the results from both models to be compared – which would strengthen the results presented.

12. Figure 4A: What is the expression of ALDH family members in the normal pancreas? This is really needed to make a comparison and statement as presented by the authors. In addition, Figure 4A is really showing high expression of ALDH1A1 and ALDH2 and not all "ALDH family proteins".

13. Figure 4H: The authors have demonstrated no evidence that in PanINs KRAS is a target of ARID1A? Was this observed in their analysis of HPFE cells? The origin of this link is not apparent.

14. ATAC-seq analysis: there is no analysis of the gained or lost regions at all. It is not stated in the text as to the numbers of gained/lost nor is there any analysis of the genes they are near (i.e. using GREAT or something similar). Are the sites that have significant changes in accessibility enriched for specific TFBSs etc.… i.e. other papers have suggested that ARID1A is a co-factor for AP-1 etc.…. (https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-019-0690-5).

15. Figure 5: Figure 5A: the text uses the phrase that Spearmans correlation coefficients are significantly lower.….. this is implying a hypothesis test – please rephrase. Figure 5B/C: needs to be clarified on how it shows "changes in accessibility of regulatory regions were significantly correlated with the alterations in gene expression levels in ARID1A-KO cells". How many of the 311 gained promoter ATAC regions overlap with genes which are upregulated (and vice versa)?

16. Supp. Table S4: There are 12 peaks reported in this table of which 10 are significantly "gained" this is different to the numbers reported in the manuscript. Please clarify/correct.

17. Figure S10: What is significance of identifying TFs? What are the significance of these TFs? Have they appeared in previous publications? Are any of these changing expression in ARID1A-KO RNA-seq? This is an underdeveloped analysis of what looks like good and interesting data.

18. Not all of the results from the differential expression analyses are available as Supplemental tables – this should be fixed.

19. In several parts of the manuscript – significance testing was carried out on only two data points (there can be no reliable estimate of variance using only two data points) using parametric methods – this is likely giving a false impression of significance – please either increase N or use a more appropriate test.
