# Peer review - Round 1

Editors:
- Jeremy J Day, https://ror.org/008s83205 University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69571.sa0](https://doi.org/10.7554/eLife.69571.sa0)

This article describes an exciting new approach for tagging and isolation of unique neuronal subpopulations based on machine learning selection of cell-specific enhancer elements in the genome. The article highlights a specific test case of this technology with neurons expressing Parvalbumin, but this method could be applied to any neuronal or even non-neuronal cell type. The tools and overall approach described here will enable cell tagging in model organisms for which transgenic lines are not commonly available or even expression of other transgenes for control of cell function or genetic perturbation.


---

# Peer review - Round 1

Editors:
- Jeremy J Day, https://ror.org/008s83205 University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69571.sa1](https://doi.org/10.7554/eLife.69571.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Machine learning sequence prioritization for cell type-specific enhancer design" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jeremy J Day as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Cliff Kentros (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) To expand on the overall applicability of the cSNAIL approach, it would be useful to determine whether identified PV-specific sequences using this approach extend to ATAC-seq signal from PV neurons in other species. Showing this would also help to generate confidence that the selected AAV sequences can drive expression in PV neurons in other systems. At a minimum, it would be important to demonstrating the accessibility of the machine-learning identified enhancer sets studied here in publicly available snATAC-seq datasets from other brain regions and in other species. This addition would go a long way to indicating the ability to generalize this approach, which is important for a resource manuscript like this.

2) In many cases, the computational approaches are not fully described and may introduce confusion for a more general readership. It would be useful for descriptions of what each model actually does to be incorporated into the manuscript.

3) Points raised by all reviewers regarding technical and interpretational clarifications should be addressed in a revised manuscript.

Reviewer #1 (Recommendations for the authors):

1. The introduction is a bit lengthy, and may be improved by efforts to consolidate the last three paragraphs.

2. It is encouraging that population-derived SVMs and single nucleus-derived SVMs arrive at similar conclusions with respect to selected sequences (Figure 1F). However, if I understand correctly all of this data is from mouse cortex. To extend the applicability of this approach, it would be useful to determine whether identified PV-specific sequences using this approach extend to ATAC-seq signal from PV neurons in other species. Showing this would also help to generate confidence that the selected AAV sequences can drive expression in PV neurons in other systems (thereby significantly expanding the applicability of this tool beyond the mouse).

3. Similar to the above comment, the extension of this approach to other brain regions will largely drive the application of this technology by other groups. While Figure 4 shows data demonstrating that the predictions generated from mouse cortex may hold for mouse striatum and GPe (although not as well as cortex), this claim is only tested using ATAC-seq. This claim could be strengthened by the addition of co-labelling evidence (as in Figure 2 for cortex) that targeted SUN-GFP cells are also PV+.

4. The text identifies Err3 and Mef2 motifs as being important for the PV-specific activity of SC1 and SC2 sequences. However, without additional experimental evidence demonstrating that loss or mutation of these motifs abolishes the PV-specific expression pattern of these sequences, this conclusion should be moderated.

5. Other reports using open chromatin profiling to identify enhancers for transgene expression in AAV have recently been published (PMID 33789083, 33789096). While these reports are cited here, the Discussion section of this manuscript would benefit from a more systematic comparison of these approaches with the current approach.

Reviewer #2 (Recommendations for the authors):

1) Twice the authors compare the PV specificity of their viral vectors to that achieved with the Pvalb-2A-Cre mouse (line 91, line 271), however no data or references are cited to explain what data the authors are comparing from the mouse strain. Published studies using Cre-dependent viruses in adult Pvalb-2A-Cre show excellent specificity for expressing in PV+ neurons, it is when the strain is crossed to other transgenic reporter mice (like the original Ai14 mouse in the Madisen et al., paper) that there is expression outside the PV+ population in the adult brain. This may not reflect Cre expression outside the PV+ population as much as it reflects Pvalb gene activation during development in cells beyond the highly PV+ population of the adult. Therefore, the authors need to clarify what data from the Pvalb-2A-Cre mice to which they are comparing.

2) in Line 275-276, and Figures 2d-e, the authors state that their PV derived enhancer vectors have a 9-fold increase in PV specificity over the negative control. However, the negative control vector has no promoter and thus should really have no expression (there is certainly exceptionally little expression in Figure 2C in the right hand most panel). If the image is truly representative, then it seems that the authors probably have too few expressing cells to say much that is meaningful in a quantitative way about the specificity of that negative control.

3) In line 338 the authors use their motif analysis to suggest a distinction in the MEF2 family members that may control the differentiation of different inhibitory cell types. However, to my knowledge there is no rigorous experimental identification of distinct MEF2A versus MEF2C versus MEF2D binding sites (if the authors are aware of a validated study this reference would be good to add). The slight variations in the motifs in the databases interrogated here may rather reflect differences in the methods of the groups that deposited the motifs. The authors would benefit the field to think broadly about their interpretation of these variations in motif enrichment and what they might mean.

4) As to the evidence that MEF2C is required for the PV+ interneuron lineage, what the Mayer 2018 paper actually showed is that conditional knockout of MEF2C in PV+ lineage cells (with Dlx6-Cre) led to loss of PV expression in the adult cortex. However, whether this is loss of PV expression, versus failure of PV cells to develop, was not addressed. The authors should adjust their language here to account for that uncertainty. It is also important that the Mayer study settled on MEF2C because it was more highly expressed in PV interneurons compared with other interneurons (esp. SST interneurons). However, MEF2C is highly expressed in many classes of excitatory neurons especially during development but also in the adult brain. Therefore, MEF2C alone cannot explain cell type specific enhancer function except in collaboration with other cell type specific transcription factors.

5) In Line 351 the authors highlight the association of open chromatin near BDNF especially at promoter IV. However, this is somewhat surprising, given that BDNF is really not expressed in interneurons (see PMID 24855953). This example highlights that the authors need to consider the possibility that not every region of differentially open chromatin reflects enhancers – these may instead be regions bound by repressors that silence nearby genes, or architectural factors that affect long-distance regulation of gene expression. The authors could strengthen this aspect of their analysis if they compared their differential OCRs to differential gene expression at least for their major cell types of interest.

Reviewer #3 (Recommendations for the authors):

To sum up the public review, it is not that we don't believe that there is added value in the SNAIL approach, we suspect there definitely is, and would honestly like to try it ourselves once it is published. It just needs to be properly and clearly demonstrated. The ideal way to show this would be to analyse the same tissue twice, once via SNAIL and once via any of the competing approaches discussed above, find areas of non-overlap and see which one works best at making specific vectors, but this is admittedly a big ask, which I am not making. However, there needs to be a bit more to demonstrate how useful it might be… another less onerous way one could do so can be seen in Figure 1 suppl 6, which shows the predicted PV specificity from SNAIL (1S6b) versus accessibility alone (1S6c). Note that the two panels are largely similar, but there are particular enhancers which have wildly different predicted specificity than from chromatin accessibility alone. The authors could illustrate how well their approach worked by taking an enhancer with very different values by the two methods (e.g. E14, E12) and seeing which prediction holds true in an AAV: SNAIL vs. raw accessibility.

Specific points are below.

Line 16: "introduce" seems out of place, since cSNAIL was already described in the previous 2020 paper… In general this is a real issue… the paper would be greatly aided by making clearer the functional distinctions between the two acronyms, rather than simply say that cSNAIL is Cre-based. The similarity of the acronyms will be confusing to the casual reader who doesn't look up the prior paper, because they are actually quite distinct in application. It is unclear how much of the paper is about the label versus the algorithm (it's almost entirely the latter). This is central to the novelty of the work, so it should be clearer.

Lines 56 to 68: in this description of selection of enhancers one relevant aspect is overlooked, namely that scATAC-seq is a relatively noisy approach to the prediction of active enhancers. A combination of different chromatin marks would likely be equally effective in selecting relevant enhancers. Naturally, this would be harder to accomplish than a simple scATAC-seq. For example the work by Ernst and Kellis is very useful here (for example PMID: 29120462).

Discovery of functional elements does not require necessarily any modeling, the addition of K27Ac marks alone for example improves prediction greatly in the case of active promoters and enhancers.

Figure 1 – supplement 2 and lines 112-114: even though this presentation is convincing in showing the predictive capabilities of machine learning, it does not put the empirically tested promoters into context of all predicted regulatory elements. I would like to see in the text an inclusion of which rank the cell class specific promoters reach (i.e. "the SVM model ranked the Gfap promoter as xx out of xxx astrocyte specific OCRs").

Furthermore, in supplement 2b, I would like to see the inclusion of all enhancers/promoters as gray, points. This will put the verified promoters into context.

Line 130 and other instances: please use "PV+" rather than "PV", in the context of "PV-", only using "PV" for "PV+" is confusing. In the same vein "PV-" may work better to prevent confusion with "PV-specific" in line 132.

Line 133: how many OCRs were present on the merged reproducible list? This information would help to put into context the differentally accessible regions in line 140.

Lines 141 to 153: it is unclear what ROC does for a naïve reader. Please include some more information what actually happens in this model. Furthermore, with OCRs of 500bp and motifs typically 6-20bp (possibly several), that would leave many basepairs of noise. Are the OCRs first screened for relevant motifs, or is the ROC applied directly the full OCRs?

How well does the CNN models perform on the more broad peaks of ATAC-seq compared to the data they were originally designed for with a much higher basepair resolution (ie. CHiP-NEXUS)?

Line 160: how many peaks were present in the merged reproducible list of peaks?

Line 165 to 174: it is unclear what the CNN does for a naïve reader. Please add a few sentences of explanation. Additionally, the true/false positive rate graphs are presented without further explanation.

Lines 221 to 225: Rather than picking out 3 values that correlate with the hypothesis, please report the full data.

In other words, please include a full list/table of enhancers E1-E34 with scores from both models, as well as values of specificity. Then ideally include two graphs with on the X-axis specificity and on the Y axis the model score, for a selection of the contrasts. I requests this because in many cases in figure 1 supplementary 4 and 5 the correlation seems to be driven primarily by E4, E22 and E29.

Could you also provide the correlation between predicted activity and specificity without E4, E22 and E29? This should hold up even without these most obvious examples.

Figure 1 supplement 5a: according to the predicted activity E10, E7 and E9 are particularly specific for PV+ cells compared to VIP+ cells. Similarly E14 should be particularly specific for PV+ cells compared to SST+ cells. This predicted specify is not apparent from the accessibility (supplement 5b) and the general, empirically determined specificity is not particularly high. But, based on the models, these particular enhancers should display specificity for PV+ cells over VIP+ cells. This hypothesis is easily tested by injecting viral vectors with these particular enhancers and counting the transgene expression in PV+ cells compared to VIP+/SST+ cells.

This hypothesis is particularly interesting because the tested enhancers are fully in line with the accessibility predictor of specificity, whereas E10, E7 and E9 predict something different than accessibility.

Figure 1 supplement 5b: It appears the correlation between specificity and accessibility is stronger than the correlation between specificity and predicted activity. Please provide the Pearson correlation of specificity and accessibility also and comment on the difference between the two correlations.

Line 241 to 250: it appears E14, and in lesser extend E11 and E2, have a similarly high specificity. Do these enhancers contain motifs too? For that matter, all other enhancers?

Line 258: what is the motivation for picking SC2 over all other candidates in the 90th percentile?

Figure 2 A-B: It appears the snATAC signal for SC1 and SC2 alone would be very strong in pointing these enhancers out as PV specific enhancers. Based on only Accessibility, how high would they rank? In other words, could you make a list with all enhancers sorted based on log2 fold accessibility difference, and provide the percentile ranks of these enhancers based on this compared to the model predicted ranks?

Figure 2C-E and lines 266 to 276: which region was investigated? Were the same cortical regions investigated to establish the percentages? Some cortical regions are naturally more abundant with PV+ cells. Please include more details on this analysis.

If this is done right: very strong, excellent to see this working! Absolutely convincing SC1 and SC2 drive PV specific expression.

Line 297 to 327: Strong, convincing evidence that SC1 and SC2 are indeed PV specific. This is not only interesting for those researching PV cells, but also an indication that the selection of these enhancers based on the in silico models was successful.

Line 360: it would be interesting to see a GPe or cortical PV+ neuron specific enhancer in a subsequent publication!

Line 444: most interesting, a good lead into functional understanding of enhancers-TF interaction in particular cell types in the brain.

Line 449: This sentence seems a bit of an overstatement. As I understand, first OCRs are selected on differential activity. Meaning a requirement of scATAC data with defined and annontated clusters. For this statement to be true, the models need to be run on all peaks, rather than pre-selected regions with differential activity. Perhaps I misunderstood and the models were actually run on the merged lists of peaks, in that case disregard this comment.

Line 459: I'm not sure which data this is based on. I don't think a direct comparison was made between the average score in Figure 1.sup5a and b. I would like to see this explicitly state in the text, along with correlation plots for specificity vs. predicted activity and specificity vs. accessibility, with pearson correlations.

Line 491: Could you speculate on the possibility to find or generate regulatory elements specific for cell types in these regions. So, instead of generalization, specification.

Lines 493 to 501: Another limitation, is that when supplemented in mature neurons, the viral vector will not undergo the same developmental, epigenomic modifications. This may result in different levels of expression. At least, in our hands we found discrepancies in expression between transgenically provided genes and virally provided ones. There does not seem to be much literature on this topic though, so a discussion may be beyond the scope of this paper.
