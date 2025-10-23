# Peer review - Round 1

Editors:
- Bruno Lemaitre, École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64919.sa1](https://doi.org/10.7554/eLife.64919.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Krautz et al. demonstrate that a tissue-autonomous innate immune response regulates hypertrophic growth using a Drosophila salivary gland model. A key finding is that the antimicrobial peptide Drosomycin inhibits the Jun-Kinase apoptotic feedback loop, permitting continued hypertrophic growth.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Tissue-autonomous immune response regulates stress signalling during hypertrophy" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that the decision was to reject the manuscript while allowing re-submission. In this way, you are more than two months to submit a revised version that address all the point of the reviews. Importantly, you submission will be considered as a new submission but is likely to reviewed by the same reviewers. At this stage, the reviewers that important control are lacking to ascertain the solidity of the claim. If you feel that you will not be able to address the reviewer's comments, you can decide to transfer the manuscript to another journal.

Reviewer #1:

This work proposes that tissue-autonomous Drosomycin (Drs) negatively regulates JNK signalling in a hypertrophic salivary gland (SG) model. The flow of experiment ideas is thorough, but lacking critical control treatments. There appears to be a spatial bias in the BxGal4 expression model used. Additionally, there is no demonstration that this is Drs-specific, as the authors never test for the effect of Gal4 dilution by involving additional UAS constructs such as other AMPs or a control like UAS-GFP. As the paper relies entirely on a BxGal4>UAS model, alternate Gal4 and UAS control treatments are essential to avoid spatial bias and the effect of multiple UAS diluting RasV12 production and consequent hypertrophy.

List of substantive concerns:

1) The authors use a BxGal4 model to drive SG expression throughout this manuscript. The assumption seems to be that BxGal4 is a pan-SG driver, and that differences in the proximal and distal parts of the SG arise due to differences in Drs expression in these regions. However it is revealed in Figure 2B that BxGal4 does not efficiently drive dorsal-RNAi in the proximal part (PP) of the SG, as this tissue retains abundant dorsal expression. In Figure 4A there is a weakening of Drs signal in situ in the BxGal4>Drs at the PP, indicating BxGal4 is not efficiently driving Drs in the PP. Finally, the PCA analysis of RNAseq data shows totally independent clustering of the PP transcriptome from whole SGs; no BxGal4>w1118 PP control is given for comparison.

Thus, throughout the manuscript, the PP is very likely a region with significantly reduced RasV12 expression, readily explaining most differences between the sick and apoptotic DP and the (relatively) healthy PP. For instance, this would readily explain differences in hemocyte attachment between the DP and PP. This may also imply a Drs response is seen in the PP solely because this relatively healthy tissue remains immune competent for longer than the DP.

Finally, Drs expression in the SG increases between the L3 and prepupa stages of development (FlyAtlas). It is unclear how BxGal4>RasV12 might affect SG developmental patterning, and indeed the model relies on rapid overgrowth of the tissue. Moreover there is an expected Drs response in immune-responsive tissues to sterile injury or stress. It is likely that SG remodelling during RasV12-induced stress leads to corresponding programmed cell death and similarly induction of NF-κB. This interpretation is congruous with the findings of Araki et al. (2018) and Parvy et al. (2019) that suggest NF-κB effectors cooperate in clearing tumorous tissue and responds to cell death signals.

2) Throughout the manuscript, the authors combine additional UAS constructs without controlling for the dilution of their Gal4 drive. This affects almost every figure in the latter half of the manuscript, and the effect of this dilution is apparent in Figure S5C, where Drs levels in BxGal4>Drs alone are 1-2 fold higher than BxGal4>Drs,RasV12 double drive. If RasV12 is diluted in combined UAS lines, this would promote a delayed phenotype, resulting in an apparent rescue effect if you simply compare equal time points. But it would be expected that continued monitoring to 144h would reveal the same apoptotic effects as the lone BxGal4>RasV12 tissue at 120h, similar to how BxGal4>RasV12 at 96h displays less apoptosis than 120h.

There is one argument that can be made in favour of the dilution not mattering: Drs-RNAi has a mild but opposite effect at 96h. However it should be noted that RNAi vs. protein overexpression leads to significantly different metabolic burdens on the cell, and thus RNAi is not a good control for this dilution effect. The authors should use a control overexpression construct such as UAS-GFP or UAS-RFP throughout.

3) There is no logic presented within the paper that this effect should be Drs-specific. Many other AMPs and immune effectors were similarly upregulated in their transcriptome (e.g. AttD, Def). If AttD and Def are similarly induced in this model, it is assumed their expression is similarly regulated, and that overexpression of AttD or Def could similarly rescue RasV12 SGs, and RNAi of AttD or Def could similarly exacerbate RasV12 SGs. I would recommend that, alongside a UAS-GFP control, the authors also test at least some subset of NF-κB effectors alongside their Drs model to elucidate if this is specific to Drs or a general effect. Given findings in other papers on AMP-tumor interactions where overexpressing Drs, Dpt, or Def all had similar effect (Araki et al., 2019), it seems likely that many AMPs should result in the same phenotype, implying there is no molecular pathway where specifically Drs inhibits JNK.

Reviewer #2:

Krautz et al. presents an interesting finding on regulation of stress signaling during hypertrophy via tissue-autonomous immune signaling. Data shows that Drosomycin, downstream of the NFkB factor Dorsal, interferes with overgrowth of the salivary gland caused by RasV12 expression. The authors investigate the underlying mechanism of this finding using different approaches, presenting copious data which are generally supportive their model.

However, in some cases the findings lack direct demonstration of key aspects of their model. The conclusions, highlighted in the model shown in Figure 8, claim that Drs inhibits JNK signaling which is shown with some key experiments. Yet, this model also claims that JNK signaling drives tissue disintegration effects of RasV12 through induction of MMP2, yet MMP2 is not upregulated until a very late time point and only to a modest degree. Moreover, they don't show that MMP2 or Hid (another JNK target) are required for these events. Also, in some cases the data is not as robust as would be expected in the field; activation of JNK is shown with compelling reporter data and pBsk staining, but the gene expression for JNK targets is underwhelming, for example Puc. Perhaps the issue is more with the model figure over-extending beyond the actual data presented.

In addition, the authors claims have relied mostly on qualitative nature of the data, whereas quantification could have strengthened their claim. For example, authors conclude that endoreplication leads to increase in nuclear volume but have not shown any quantitative increase in nuclear DNA content. The DAPI data shows most of the nuclei as disintegrated which will amount to higher nuclear volume but is less informative about DNA content. Further, authors have not stated whether the disintegrated nuclei were excluded from the analysis or not. Similarly, RasV12 stimulated MMPs-dependent tissue disintegration and Hid-dependent nuclear disintegration are not directly demonstrated.

Apart from the above-stated experimental concerns, issue with data presentation also significantly dampens the enthusiasm for this study. The data-presentation is incredibly cumbersome; throughout, the text does not present clearly the rationale of their experimental design, some key figure panels are not even mentioned in the text, other key data is buried in the supplemental figures, while other data is replicated in separate figure panels without clear reasoning, and importantly most of the legends/labeling on the graphs are so small, they are illegible. This last issue makes this work nearly impossible to critically evaluate. Also, I would encourage the authors to use gene names and symbols on their figures that are understood by a wide readership. For example, Bsk might be alternatively JNK in S5.

Reviewer #3:

This article is interesting because it shows that some immune genes, mostly antimicrobial peptide (AMP) genes, are induced in a highly artificial system in which the overgrowth of salivary glands is induced by ectopic expression of the Ras[V12] gain-of-function allele. The expression of immune genes would rely solely on Dorsal and not the Toll pathway (see below). The most important point is that the overexpression of Drosomycin is sufficient to reduce the induction of JNK-pathway regulated genes that occurs in the distal part of salivary glands, including pro-apoptotic genes, thus introducing the concept of a direct or indirect intracellular signaling function for an antimicrobial peptide.

In the longer term, it will be interesting to determine whether Dorsal plays a role in wild-type larval salivary glands and why it is differentially repressed in the DP.

Substantive concerns

1) The authors use RNAi lines to determine whether the Toll pathway is required for the induction of immune genes, which are not even validated. Since it is close to impossible to demonstrate the generation of a null phenotype by RNAi, the authors should imperatively use at least one null mutant of the Toll pathway, e.g., MyD88 and possibly spz.

2) The authors should look at and quantify Dorsal nuclear localization in the salivary glands and not solely at its expression. Upon looking at Figure 2B, one gets the impression it is nuclear only in the very proximal region of the organ.

3) Multiple AMPs are induced in the PP and it is surprising that the one AMP they have overexpressed is having such a biological function. A control is missing, ideally a Drosomycin mutant in which disulfide bridges cannot form; at least a nonrelevant gene should be used as a control to exclude nonspecific effects linked to overexpression in the Ras[V12] context. Also, the Drosomycin RNAi line does not abolish the expression of its target gene and does not have such a "drastic" effect: several genes are only mildly more strongly expressed. It would be interesting to use a Drosomycin null mutant. Perhaps less important for this work but of interest, it would have been informative to test mutants affecting AMP families that have recently been published.

4) It is not clear whether Drosomycin is secreted in the lumen or basally in the hemolymph. To really conclude that this is a tissue-autonomous response, inasmuch the authors do not state whether Drosomycin is expressed in other tissues, it would be useful to overexpress Drosomycin in the fat body and test its effects on the DP of the salivary glands.
