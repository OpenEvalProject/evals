# Peer review - Round 1

Editors:
- Jeffrey Settleman, Calico Life Sciences United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31098.026](https://doi.org/10.7554/eLife.31098.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Targeting RAS Driven Cancers with Antibodies to Upregulated and Functionally Important Cell-Surface Proteins" for consideration by eLife. Your article has been favorably evaluated by Charles Sawyers (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Martinko and co-authors have generated a toolkit of recombinant antibodies targeting cell surface proteins induced by activated Ras in cancer cells as a therapeutic strategy. Initially using an isogenic cell line pair based on MCF10A mammary epithelial cells with or without mutationally activated KRAS, they characterized the cell surface proteome by mass spec to identify Ras-induced surface proteins. These were enriched for proteins involved in cell adhesion and migration, and the effects were largely dependent on Ras-MEK pathway signaling. Parallel analysis of RNA expression revealed only a small correlation between Ras-induced surface proteins and corresponding RNAs, suggesting that the mass spec approach can reveal novel candidate targets. They made recombinant antibodies targeting some of these surface proteins, which validated the observed Ras-induced surface expression. They then used CRISPi screening of 1600 annotated surface proteins to look for those demonstrating functional dependency specifically in Ras-transformed cells. They prioritized efforts focused on one of these genes, which encodes CDCP1, an integrin-associated protein previously implicated in cancer/ Using CDCP1 antibodies conjugated to a cytotoxin, they demonstrated the potential utility of such an antibody-drug conjugate targeting CDCP1 as a therapeutic.

Overall, while these studies are technically well executed, and represent a potentially useful application of recombinant antibody technology coupled with mass spec analysis of the surface proteome of cancer cells, the manuscript reads like a collection of somewhat orthogonal observations that are not logically well-connected. Moreover, as described below, the emphasis on CDCP1 detracts from the overall enthusiasm, since this has been previously implicated as a target in Ras-driven cancers.

Essential revisions:

1) The logical flow, as presented, complicates the interpretation of the key conclusions. For example, the authors emphasize that the correlation was weak between cell surface proteome and RNA expression; however, the highlighted example CDCP1, has already been reported to be a Ras-induced gene at the RNA level. Similarly, the authors used CRISPRi to establish a list of surface proteins that are functionally required in Ras-transformed cells; however, they then went on to use the CDCP1 antibody to deliver a toxic payload to cancer cells, rather than exploring a function-blocking antibody. This is confusing since it raises a question about the rationale for the CRISPRi analysis.

2) CDCP1 is not an ideal candidate to emphasize as the key example, largely due to the fact that it has been previously published as a Ras-induced candidate target. Notably, in the Discussion, the authors state that,"our work now demonstrates MAPK dependent expression of this protein […]"; however, the previous report from Uekita (which is cited) had already demonstrated the role of MAPK signaling in Ras-induced CDCP1 expression. So, the novelty is quite limited here.

3) The authors argue strongly and for the most part convincingly that the use of MCF10A was reasonable for these experiments. However, the authors should discuss that they may well have missed important cell surface targets using this approach. This is particularly salient given the wide variability of expression of the proteins that they found across other cell lines. MCF-10A is a curious choice for these studies when considering that breast cancer is often highlighted as one of the few cancer types that never harbor KRAS mutations. The authors should probably highlight in more detail why they chose this cell line as the starting point, even if it is just for technical reasons. There are now multiple examples (from different tissue types) of cancer cell lines that are engineered to be +/- KRAS.

4) To address the points raised above, the authors should substantially revise the manuscript to emphasize the recombinant antibody technology as applied to targeting the surface proteome of cancer cells, while reducing the significance of selectively targeting Ras mutant cancer cells. Furthermore, the manuscript should include a more realistic discussion of the implications of the work. Not all KRAS mutant cancers are driven by MAPK and not all of these will have CDCP1 up-regulated. Moreover, since no normal cells or tissues were analyzed (neither MCF-10A or HPNE cells are normal), it is unclear from these experiments whether a therapeutic window really exists for CDCP1 targeting, especially given that no anti-tumor activity is shown.

5) For Figure 3C, the authors mentioned that the 8 cell lines were selected because pancreatic, lung, and colorectal cancers have the highest frequency of KRAS mutation. It is very nice to see that CDCP1 showed high surface expression in almost every cell line tested. However, the other 6 proteins did not. Although a full characterization of all of these proteins goes beyond what is necessary in this report, it would be helpful to have a more robust discussion of this issue.

6) In addition to Figure 5C, it would be more convincing to repeat the same experiment in other cell lines: pancreatic or other lineages that have been shown in Figure 3C to have high expression of CDCP1.

7) In Figure 6B, the BRAF inhibitor SB590885 did not decrease phospho-ERK levels? Is this correct?

8) In Figure 6B, is it a robust result that the AKT inhibitor MK2206 only decrease the surface localization of CDCP1 but not CDCP1 total protein level?

9) NCI-H1299 cells have wild-type KRAS and NRAS-Q61K mutation, not KRAS-Q61 as stated in the text and Figure 6C. More RAS-mutant cell lines should be tested to further support the claim that CDCP1 expression is coupled with activation of MAPK signaling.

10) The authors have used publicly available databases to assess whether CDCP1 is overexpressed in KRAS mutant cancers. It would be helpful to determine this by a different method than probing gene expression (mRNA) as this is not entirely reliable.

11) The experiment described in Figure 3C is not very informative given that no RAS WT cell lines are shown. Moreover, without some sort of KRAS perturbation (knockdown or MEK inhibition), there is no evidence that the expression of any of these proteins has anything to do with RAS mutation status.

12) The type of data shown in Figure 5Ais not very informative from a therapeutic point of view. Even though KRAS mutant and WT are statistically different at the population level, in truth only 7% of PDAC over-express CDCP1. 91% of PDAC (in the TGCA dataset) have mutant KRAS, so, regardless of the claims made in the paper, the general relationship between mutant KRAS is unclear. The Discussion should probably be more frank about this. Moreover, Figure 1F shows a less than impressive correlation between transcriptomics and proteomics, yet they are trying to make an important conclusion about CDCP1 protein expression from transcriptomics data on primary tumors. It would be useful if they could comment specifically on the correlation between RNA and protein for CDCP1 in their original analysis.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Targeting RAS Driven Human Cancer Cells with Antibodies to Upregulated and Essential Cell-Surface Proteins" for further consideration at eLife. Your revised article has been favorably evaluated by Charles Sawyers (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The Abstract, which emphasizes biological findings, remains unchanged. For example, the statement, "we discovered a signature of proteins critical for metastasis that are upregulated on cells transformed with KRASG12V, and driven by MAPK pathway signaling." is misleading in light of the findings presented. Similarly, the phrasing of the statement describing CDCP1 findings still leads readers to conclude that this protein has been newly identified by these studies. The authors need to edit the Abstract to appropriately represent the key novel claims, and the emphasis on the new technology.

The authors have not adequately addressed a concern that was raised regarding the transition from the CRISPRi discovery of a requirement for CDCP1 and the experiments in which it was targeted using an ADC strategy (subsections “Functional characterization of the KRAS surfaceome in MCF10As using a CRISPRi screen” and “Antibodies can selectively deliver toxic and immunotherapy payloads to mutant KRAS pancreatic cancer cells”). In the reply to reviewer comments, the authors refer to a statement they make where they write: "One of the most common mechanisms of resistance to targeted therapies is loss of expression of the protein target." But this is not true. In fact, most targeted therapies are directed to proteins that are required by cancer cells and such targets are therefore not typically reduced in expression as a resistance mechanism. The authors should remove or restate this. More notably, the authors should explain in the transition between these two sections that the dependency of RAS-transformed cancer cells on CDCP1, together with its high surface expression, makes it an attractive ADC target-which is unlikely to be selected against as a resistance mechanism due to its requirement in these cancer cells. Therefore, they explored the ADC approach. They should also comment on the fact that their antibody to CDCP1 is apparently not a function-blocking antibody-since it does not seem to affect cell viability.
