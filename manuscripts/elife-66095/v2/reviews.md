# Peer review - Round 1

Editors:
- Erica A Golemis, Fox Chase Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66095.sa1](https://doi.org/10.7554/eLife.66095.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work sheds important light on the role of aberrant CRTC-CREB activation in the growth of lung cancers bearing mutations in LKB1. The experiments demonstrating specific impact of pan-CRTC inhibition in suppressing LKB1-mutated lung cancer provide a rationale for the use of inhibitors of CRTC-CREB signaling as therapies for a difficult to treat molecular subtype of non-small cell lung cancer.

Decision letter after peer review:

Thank you for submitting your article "Dependency of LKB1-inactivated lung cancer on aberrant CRTC-CREB activation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Erica Golemis as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: David Barbie (Reviewer #1); Humam Kadara (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. In Figure 1 have the authors looked at cytoplasmic vs nuclear levels of any of the CRTC family members in LKB1 null vs wt cells? Existing models suggest that SIK mediated phosphorylation of CRTCs results in nuclear translocation. Thus, while total levels do not appear to be different between the 2 classes of cell lines, is there differential nuclear translocation of CRTC2, for example, in LKB1 null cells?

2. The most compelling data supporting specificity of their dnCRTC construct is the data in Figure 4, with unbiased RNAseq data identifying CREB target genes as the among the top downregulated genes. But this is only proven in a single cell line. Are similar target genes downregulated by qPCR in H157 cells, which they use as their other model? This is important to establish

3. Moreover, they show that these downregulated genes are upregulated in KRAS-LKB1 mutant tumors in TCGA, supporting the idea that CRTC-CREB is driving their expression uniquely in this context. But it would also be useful to look at the same subset of target genes in their KRAS-p53 mutant cell lines expressing dnCRTC (H322 and H522), to compare the relative overall expression and the degree to which dnCRTC suppresses them in the non-LKB1 mutant context.

4. Finally, isogenic LKB1 mutant cells are typically utilized to prove specificity of downstream signaling. For example if they KO LKB1 in one of their KRAS-TP53 mutant cell lines, what happens to CRTC levels/translocation and expression of these target genes? And if technically feasibly it would be most convincing if LKB1 loss specifically resensitized these cells to their dnCRTC construct.

5. In Figure 1, the authors state that expression of CRTC mRNAs is normalized to that of CRTC1. How is this being done? Is there a single probe used that recognizes all 3 CRTC isoforms? If so, this is not stated in the methods – if not, it is not possible to normalize based on PCR cycles, given the efficiency of different probes. It is also puzzling that CRTC1 appears to be much more abundant in LKB1 wt cells.

6. In Figure 1, the authors make inferences about phosphorylation – and hence activity – of CRTC isoforms in LKB-minus versus wt cells based on the migration of the protein. This is not sufficient, particularly as the Western shown indicates proteins are running in a curve. These experiments need to be supplemented by data showing migration change following phosphatase treatment of lysates, and/or by cell fractionation data showing more nuclear CRTC proteins in LKB1-minus cells.

7. The dominant negative construct dnCRTC is an essential tool for the study. The authors use ChIP to show that it associates with CREB. However, they do not show that it displaces the wt forms of CRTC from interaction with CREB. This is an important control.

8. On page 11, "we identified a list of direct dnCRTC-regulated genes, which represent an extensive set of the potential critical mediators for CRTC-CREB activation in promoting lung cancer cell growth" is a significant overstatement, and should be toned down or removed, unless validation data is provided for the importance of some of the genes identified.

9. Prior reference 42, which the authors frequently cite, note importance of overexpressing CRTC2 for activation of ID1, with validation included. What happens to ID1 expression in cells overexpressing dnCRTC?

10. On page 12, there is description of results from GSEA, but no data is shown, no statistical significance of results is provided, and the described findings are very vague. The data need to be provided and the data more accurately described, or this section should be removed.

11. Various studies have shown that LKB1-mutated lung tumors are immune muted or privileged. In fact, in the past couple of years, studies have shown that a muted immune response is a key, if not the most prominent, feature of LKB1-mutated lung cancers relative to LKB1-wild type tumors or those with other driver alterations. Indeed, LKB1-mutated tumors were shown to be non-responsive, or at best, weakly responsive to immune checkpoint blockade. A major weakness in the study is the sole dependency on immune compromised animal models. It would be important to determine the impact of dcCRTC inhibition on the immune microenvironment, in light of previous reports linking CREB, and immune infiltration/function. At least this weakness should be acknowledged and discussed in the manuscript.

12. The data in Supplementary Figure 2 showing the association of ddCRTC target genes with LKB1 mutations in NSCLC are not clear and difficult to visualize. This conclusion would benefit from statistical analysis that supports the association of dnCRTC target genes with LKB1 mutations.

13. As the authors discussed in the Introduction section, LKB1 deficiency was shown to impair salt-inducible kinases (SIK1,2, and 3) leading to phosphorylation/activation of CRTCs. It is worthwhile for the authors to discuss their finding on reduced SIK1 expression by dnCRTC (Figure 4).

14. The group discusses oncogenic gene signatures that were negatively enriched in dnCRTC-expressing versus control GFP-expressing A549 cells (page 12) but these data are not provided.

15. The H&E staining of mouse lungs colonized with A549 (Figure 7C) are not clear (strong background).

Reviewer #1:

In this manuscript Zhou et al. explore the role of downstream CRTC-CREB activation in KRAS-LKB1 mutant lung adenocarcinoma. First, they characterize expression of the 3 different CRTC family members across LKB1 null vs wt lung cancer cells, observing variable expression with generally higher levels of CRTC2 (previously implicated as a dependency in this setting) and CRTC3. Since KO of each family member was limited by functional reduncancy to some degree, they then engineered a dominant negative model by fusing the common CREB binding domain to GFP, and expressed this in A549 cells. Nicely, RNA-seq confirmed specific downregulation of CRTC-CREB targets in these cells, which was associated with impaired proliferation that was preferentially observed in LKB1 null cells. Finally, they demonstrate that subcutaneous implantation of dnCRTC expressing LKB1 null cells impaired tumor xenograft growth as well as metastatic lung colonization. Overall this is a well conducted study which builds upon an emerging literature highlighting the importance of SIK signaling, CRTC2, and CREB in KRAS-LKB1 mutant cancer, which still lacks effective therapy.

Reviewer #2:

In this article, Zhou et al. investigate the requirement for the three isoforms of CRTC (CRTC1-3) in pathogenesis of LKB1-mutant lung cancers. CRTC proteins serve as co-activators of CREB; LKB1 loss reduces activity of SIK kinases, which normally phosphorylate and cytoplasmically sequester CRTCs; in the absence of LKB1, unphosphorylated CRTCs enter the nucleus and associate with CREB. Previous work has noted that upregulation of CRTC2 is common in lung cancer, and showed elevated CRTC2 promotes lung cancer growth – however, that study found little effect of reducing CRTC2 expression. The present work investigates all three CRTCs, showing depletion of each, alone, has little effect, but simultaneous inhibition of all CRTCs through expression of a dominant negative construct that competes with CRTCs for CREB binding, but fails to activate transcription, specifically blocks the growth of LKB1-deficient but not LKB1-wt lung cancer, in vitro and in vivo. The work also suggests specific CREB transcriptional targets that may contribute to the transforming activity of CRTC-CREB. Overall, the work is carefully performed and makes a useful contribution to the field. However, some points need to be further elucidated. These include better characterization of the relative expression and modification of CRTC proteins, confirmation that the biological activity of the dominant negative construct efficiently displaces CRTCs from interaction with CREB on gene promoters, and more thorough description of the downstream transcriptional consequences of use of dominant negative CRTC.

Reviewer #3:

The study by Zhou and colleagues investigates the role of aberrant activation of CREB-regulated transcription co-activators (CRTCs 1, 2 and 3) and CREB in LKB1-mutated (inactivated) non-small cell lung cancer (NSCLC). Previous work has shown that LKB1-inactivated lung cancer exhibits increased CRTC-CREB activation, yet the relative contributions of the three CRTC co-activators are still not determined. Here, the study evaluated the effects of a pan-CRTC inhibitor on the malignant phenotype of LKB1-inactivated NSCLC cells and tumors. The study first shows that expression levels of the different CRTCs are variable across LKB1-wild type and-inactivated lung cancer cells and that targeting each CRTC alone does not lead to decreased cell growth and progression of LKB1-inactivated lung cancer cells. In contrast, they find that a pan-CRTC inhibitor (dnCRTC) decreased global CREB target gene expression and specifically inhibited in vitro growth of LKB1-inactivated but not LKB1-wild type lung cancer cells. The group also shows that dnCRTC significantly decreases the growth of subcutaneously xenotransplanted human LKB1-inactivated A549 and H157 lung cancer cells in NOD/SCID mice. Also, dnCRTC inhibited lung colonization of A549 and H157 cells intravenously injected in NOD-SCID mice. The study is in general carefully designed and clearly shows the significance of aberrant CRTC-CREB signaling in the growth of LKB1-inactivated lung cancer cells.
