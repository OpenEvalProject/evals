# Peer review - Round 1

Editors:
- Douglas L Black, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37184.033](https://doi.org/10.7554/eLife.37184.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An alternative splicing switch in FLNB promotes the mesenchymal cell state in breast cancer" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Douglas Black as the Reviewing Editor and James Manley as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study by Li and colleagues examines the role of splicing regulation in driving the epithelial mesenchymal transition (EMT). EMT is a key event in the progression of tumors to a metastatic state and is controlled by an array of genetic mechanisms, including the transcription factors SNAI1, Twist, ZEB1 and others, as well as splicing regulators such as ESRP, RBFOX2 and QKI. The authors previously developed a breast cancer model by transforming mammary epithelial cells with oncogenic factors. The derived cells (HMLER) can be segregated into pre and post EMT populations based on CD44 expression, a marker of metastasis. The CD44 high cells express other mesenchymal markers and exhibit additional properties of these cells, including mammosphere formation. To identify drivers of the transition, the authors infected CD44 low cells with a bar coded cDNA expression library and cells were sorted for CD44 expression. Barcodes enriched in the CD44 high population identified candidates for cDNAs that can induce EMT in HMLER cells. These included the known EMT factor, SNAI1, an indication that other hits in the screen could be similarly important for EMT. These other hits included a preponderance of RNA binding proteins (RBP), two of which, RBFOX1 and QKI, can induce EMT. The authors show that RBFOX1 and QKI alone can increase mesenchymal marker expression and stimulate mammosphere formation. These RBPs are upregulated by SNAI1, and depletion of these proteins by RNAi or CRISPR reduces the effect of SNAI1 on CD44 expression and mammosphere formation. QKI and to a lesser extent RBFOX1 are upregulated in other breast tumors and tumor progression models. Using RNAseq the authors identify changes in splicing induced by QKI and RBFOX1 in their cells and find exons that are coregulated by these RBPs, whose splicing changes are induced by SNAI1. Using CLIP to identify binding sites for QKI and RBFOX1, they show that the proteins bind to sequences adjacent some of the EMT regulated exons making them likely direct targets of QKI and RBFOX1. Focusing on an alternative exon in the actin binding protein Filamin B (FLNB), they show that its skipping correlates with the basal B type of breast cancer. The exon skipped isoform is more active in inducing mesenchymal markers. Using genome editing to force skipping of this exon, they observe modest increases in these markers, in the percent of CD44 high cells, and in mammosphere formation. FLNB was previously shown to bind to the transcription factor FOXC1. Through knockdown experiments the authors show that FOXC1 is needed for the marker expression induced by the RBPs and FLNB.

The reviewers all agreed that his study is a significant contribution to the growing literature on the roles of RBP's and posttranscriptional regulation in EMT and tumor progression. Some of the effects are not large, much smaller than SNAI1, leading to questions as to how central these new players are to EMT. Nevertheless, there is a lot of interesting data here, and the experiments are generally well performed and comprehensive. This work will be of broad interest to groups working on both RNA biology and cancer. However, there are a number of issues that need to be addressed before the paper can be considered for publication.

Essential revisions:

1) There is no characterization of which QKI and RBFOX1 isoforms came out of the screen. Both of these genes produce multiple isoforms, nuclear and cytoplasmic, that have different functions and can cross regulate each other. One cannot assess the true targets of whatever forms were isolated from the library without knowing their structure. Similarly, there needs to be an assessment of whether the endogenous Rbfox or QKI isoforms change with EMT or with ectopic expression of a particular isoform. It appears that the RBFOX1 isoforms could change between HME cells and HMLER cells from the immunoblots in Figure 2—figure supplement 2.

2) In Figure 2, did the cell proliferation change when the candidate RNA binding proteins were overexpressed? Were there any morphological differences between the CD44-high cells induced by SNAI1 overexpression and those induced by overexpression of QKI or RBFOX1?

3) RBFOX2 is expressed in a wide variety of cell types and was previously implicated in EMT. In contrast, RBFOX1 is reported to be most abundant in heart, muscle and brain. It is thus important to show validation of the RBFOX1 antibodies, confirming that they do not cross-react with RBFOX2. The isolation of RBFOX1 from an ectopic expression screen is not so surprising, but why was RBFOX2 not isolated? Is it not active for inducing EMT? Given the previous data on RBFOX2 and EMT, it seems surprising that it does not have similar activity.

4) Many RNA binding proteins co-immunoprecipitate because they bind to common RNAs. The interaction between QKI and RBFOX1 described in Figure 4—figure supplement 1C is not meaningful unless the sample has been treated with RNase.

5) In Figure 6, the effects of the two FLNB isoforms are relatively small, especially in the CRISPR experiments. It is difficult to draw conclusions from these data, and some of these results appear to be contradictory. In Figure 6C, FLNB-ΔH1 is shown to induce EMT marker expression. But the model in Figure 7 seems to be that the ΔH1 isoform sequesters less of the FOXC1 transcription factor leading to more expression of the EMT markers. If this were true, then over expression of FLNB-L should reduce marker expression and FLNB-ΔH1 should have no effect. The reduction in nuclear FLNB presented in Figure 7—figure supplement 1A is difficult to see and needs to be quantified. The proposed model does not agree with the reported data.

6) In Figure 6, the protein levels of Filamin B should be shown after siRNA and CRISPR knockdown.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "An alternative splicing switch in FLNB promotes the mesenchymal cell state in human breast cancer" for further consideration at eLife. Your revised article has been favorably evaluated by James Manley (Senior Editor) and Reviewing Editor Douglas Black.

In this revised manuscript from Li and colleagues, the authors have added extensive new data and addressed nearly all of the concerns raised by the reviewers. The manuscript is largely ready for publication in eLife. However, the editors request that one final point be addressed. The RBFOX1 isoform isolated from the screen and used in the analysis, NM_145893.2, appears to contain the third to last exon (hg38 chr16:7,693,315-7,693,367). Since isoforms containing this exon have been found to be largely localized to the cytoplasm (PMID: 15824060; PMID: 19762510), this raises questions regarding the mechanisms leading to the RBFOX1 dependent splicing change. It is possible that the localization may be different in the system studied here, but this should be confirmed and described. Alternatively, if the RBFOX1 protein driving EMT is cytoplasmic as seen previously, the authors should note this and revise their model in the text.
