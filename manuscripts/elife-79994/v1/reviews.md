# Peer review - Round 1

Editors:
- Fadel Tissir, https://ror.org/02495e989 Université Catholique de Louvain Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79994.sa0](https://doi.org/10.7554/eLife.79994.sa0)

The authors' study investigated the role of m6A epitranscriptomic modification in the developing mouse retina. The study clearly demonstrated the defects of Mettl3CKO retina in mice, including cellular disorganization and abnormal physiological responses. Enriched scRNA-seq and MeRIP-seq data provide excellent resources to study the function of m6A modification in retinogenesis.


---

# Peer review - Round 1

Editors:
- Fadel Tissir, https://ror.org/02495e989 Université Catholique de Louvain Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79994.sa1](https://doi.org/10.7554/eLife.79994.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "m6A epitranscriptomic modification regulates neural progenitor-to-glial cell transition in the retina" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors showed disrupted retina structure in Mettl3cko and claimed that dysfunction of Muller glial cells was the underlying cause. However, based on the data presented in the manuscript, it is not clear whether retinal structure abnormalities are direct effects of Muller glial defects or secondary effects induced by defects in RPCs or other cell types.

2) The authors claimed that m6A is important for RPC to Muller glial transition but didn't clearly state whether m6A regulates gliogenesis, which can be easily assessed by quantifying the number of Muller glial cells. The authors showed that the number of Muller glial cells was increased in mettl3cko at P7 based on Sox9 staining, but the number of Muller glial cells in single cell RNA-seq data stayed unchanged between Mettl3cko and controls. In addition, the number of Muller glial cells in adult retinas (for example, at P14) was not examined. Based on images in Figure 1E, the number of Muller glial cells seemed to be slightly decreased compared to controls. Moreover, in line 130, the authors mentioned that Mettl3cko retinas resembled those with loss of Muller glia in the literature. These discrepancies need to be addressed.

3) The authors showed that there was an increased number of RPCs in Mettl3cko at late stages of retinal development compared to controls. However, some of the data do not seem to be consistent with published literature and their own supplementary data. Specifically, at P7, based on their single cell RNA-seq data, 6% of retinal cells were RPCs in control retinas, and 11% of retinal cells were RPCs in Mettl3cko (Figure 3—figure supplement 2). However, the number seems to be very high for control P7 retinas. In published single cell datasets (Clark et al. 2019), the percentage of retinal cells identified as RPCs was close to 0 at around P7. In addition, in Figure 3—figure supplement 3, the authors stained P7 Mettl3cko and control retinas with Ki67. There was a very limited number of Ki67+ cells in Mettl3cko, which doesn't quite match the 11% found in single cell RNA-seq data.

4) The stage of the retina was not consistent across experiments. The single cell RNA-seq experiment was performed using P7 retinas, whereas MeRIP-seq used P6 retinas. Twenty-four hours could make a big difference in terms of transcription at this stage.

5) Many claims in the manuscript are not fully supported by the data. For example, the authors over-expressed candidate m6A-regulated genes in RPCs and showed that they prevented the RPCs from exiting the cell cycle. However, the data presented in Figure 6 cannot fully support this conclusion. PCNA is not a pan cell cycle marker. Reduction of GFP+PCNA- cells in Mettl3cko doesn't necessarily mean that mutant cells failed to exit the cell cycle.

6) Individual data points and N numbers were not shown in the bar graphs.

7) The authors used six3:cre (expressed from E9.5) to knock out Mettl3 throughout the entire course of retinal development. It would be better if the authors could test the role of m6A in late RPCs directly.

8) In Figure 2, the authors identified müller glia in Mettl3CKO mice using the Sox9 antibody. Due to severe structural abnormality of the retina in Mettl3CKO mice, the identification of cell fate needs additional caution. It is better to verify müller glia using other antibodies (such as glutamine synthetase, GS; GFAP) independently.

9) Some results seem inconsistent. First, in Mettl3CKO mice, the author found an increased number of Müller glia, a reduced number of rods, and no change in other cell types (Figure 2I-N). However, in the retinae with the overexpression of Zfp292, Ckap4, Traf4, or Bcl7a, they found an increase in the percentage of Müller cells at the expense of amacrine cells or rod photoreceptors (Figure 6C-D). Second, in scRNAseq data analysis, only the proportion of RPCs increased, but not Müller glial cells (Figure 3D). This result is not consistent with the IF phenotype (Figure 2I-J). The authors need to discuss these results at least to clarify the inconsistency.

10) Overall, the working model that the authors proposed lacks direct support. The authors may want to identify late RPC clusters that were committed to Müller glia fate as well as were subject to Mttl3CKO, and further verify the expression specificity of m6A-modified transcripts, such as Zfp292, Ckap4, Traf4, or Bcl7a, in such RPC clusters. Also, the authors should experimentally examine the essential roles of the loss of these m6A-modified transcripts in Müller glia development. These analyses will much strengthen the main conclusions of the study.

Reviewer #1 (Recommendations for the authors):

I encourage the authors to include the following info and additional explanations in the manuscript.

1. Line 120, the stage of IF staining should be included.

2. Line 146, please provide references showing that P6 is the peak time point for MG generation.

3. Line 162, the number of BrdU+;Ph3+ RPCs over BrdU+ cells should be quantified. The data presented by the authors cannot support the conclusion.

4. Line 180, please provide evidence showing that the major retinogenesis phase was completed in the central retinas in Mettl3CKO mice.

7. Line 183, how did the authors quantify Rho+ rods based on rhodopsin staining?

8. Line 226, "Considering that RPCs at this age are near the end of retinogenesis, most would become Müller glia. As a consequence, the final proportion of Müller glia in Mettl3CKO retinas should be higher than that in control retinas".

Muller glial proportion was not increased based on single cell RNA-seq data. This claim is confusing.

9. Line 258, "The upregulated genes were enriched for biological processes related to gene expression regulation, while downregulated genes were enriched for biological processes such as 'organelle organization' and 'precursor metabolites and energy'".

These GO terms do not seem to be the top terms based on the figures. Why did the author highlight them?

10. Line 259, "Importantly, key cell cycle machinery components, such as Ki67 and Brca2, was upregulated, but many cell cycle regulators, such as Ccna2 and Cdca8, were downregulated (Figure 3H-3J and Supplementary 261 Table 1), which explained why the cell cycle progression of Mettl3CKO RPCs was distorted".

This claim is very confusing. Does downregulation of Ccna2 and Cdca8 delay cell cycle?

11. Line 386, "p14 showed that while the OLMs of these retinas were grossly intact, at a few regions, the OLMs are broken, and a few rods escaped to the subretinal space".

This may be due to damage from retina sectioning. Please state whether this is a significant phenomenon. In addition, the authors did not quantify the number of Muller glial cells when the four plasmid mix was electroporated into P1 RPCs.

12. Figure 4 and Figure 5 may be combined.

Reviewer #2 (Recommendations for the authors):

1. The authors used six3:cre (expressed from E9.5) to knock out Mettl3 throughout the entire course of retinal development. It would be better if the authors could test the role of m6A in late RPCs directly.

2. In Figure 2, the authors identified müller glia in Mettl3CKO mice using the Sox9 antibody. Due to severe structural abnormality of the retina in Mettl3CKO mice, the identification of cell fate needs additional caution. It is better to verify müller glia using other antibodies (such as glutamine synthetase, GS; GFAP) independently.

3. Some results seem inconsistent. First, in Mettl3CKO mice, the author found an increased number of Müller glia, a reduced number of rods, and no change in other cell types (Figure 2I-N). However, in the retinae with the overexpression of Zfp292, Ckap4, Traf4, or Bcl7a, they found an increase in the percentage of Müller cells at the expense of amacrine cells or rod photoreceptors (Figure 6C-D). Second, in scRNAseq data analysis, only the proportion of RPCs increased, but not Müller glial cells (Figure 3D). This result is not consistent with the IF phenotype (Figure 2I-J). The authors need to discuss these results at least to clarify the inconsistency.

4. Overall, the working model that the authors proposed lacks direct support. The authors may want to identify late RPC clusters that were committed to Müller glia fate as well as were subject to Mttl3CKO, and further verify the expression specificity of m6A-modified transcripts, such as Zfp292, Ckap4, Traf4, or Bcl7a, in such RPC clusters. Also, the authors should experimentally examine the essential roles of the loss of these m6A-modified transcripts in Müller glia development. These analyses will much strengthen the main conclusions of the study.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "m6A epitranscriptomic modification regulates neural progenitor-to-glial cell transition in the retina" for further consideration by eLife. Your revised article has been evaluated by Marianne Bronner (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

While the reviewers appreciate the efforts that have been invested in this revised manuscript, they feel that an additional revision is needed to put the study into the context of previous report, and clarify the novelty of the findings.

Reviewer #1 (Recommendations for the authors):

The authors improved their manuscript. However, to make the study convincing, additional investigation and explanation still need to be conducted.

1. It is still not clear whether m6A depletion specifically affects RPC to muller glia (MG) transition, or just elongates the RPC cell cycle as shown in previously published papers, which investigated the role of m6A in brain development. Elongation of RPC cell cycle can also lead to increased production of MG.

2. The authors showed that there are significant cell death in the cko retinas at P0, P6 and P14, and this may be responsible for the not so significant increase of MG in cko. But they didn't show which types of cells are dying. Many TUNEL positive cells are in ONL (Figure 2-supplement 4, A'-C'). This cell death was also not carefully integrated into their conclusions when they explained the phenotypes or results.

3. The authors claimed that cko RPCs withdrew from the cell cycle shower than control RPCs (Figure 2E and F). If this is the case, there should be more proliferating RPCs in cko. However, the author showed that there are significantly less BrdU+ cells at P1 (2 hours after BrdU injection) in cko (Figure 2B). These results do not seem to support each other.

4. The authors didn't show that Mettl3 is depleted and m6A levels are lowered at embryonic stages.

5. For all the shRNA-based experiments, there aren't any control experiments to show their efficiency and specificity.

6. Lin 254-258, the argument is weak and hard to understand. The Ki67+ region is only at the very tip of the retina in cko. The authors need to provide stronger evidence to clarify whether the number of muller glial cells is increased or unchanged in the cko at different stages.

7. The authors claim that Mettl3cko "…compromises the function of Muller cells" (abstract line 32). There is no direct evidence to support this point.

8. The role of m6A on neural development has been extensively studied in the brain. The authors did not discuss these published papers and did not explain how their work improved the field.

Other concerns:

1. In Figure 1A and 1A', the background color looked very different. It looks like different exposure duration were used. A western blot may be better to show the deletion efficiency.

2. Penetrance (50%) of the OLM break phenotype was not included in the manuscript.

3. Line 161, 2 hour Brdu pulse chase experiment cannot support that the cells proliferate slower. It only suggests that there are less proliferating cells.

4. Figure 2D, label on Y axis was not corrected.

5. Line 201-206, the number of cells cannot be quantified based on markers expressed in the cytosol. These markers may be upregulated in individual cells.

6. The m6A IP was not shown for cko retinas in Figure 6-Supplement 1.

Reviewer #2 (Recommendations for the authors):

The authors have enlisted new experiments and analyses that substantially strengthen the paper in this revised manuscript. All these efforts should be applauded. In particular, the new data of shRNA targeting Mettl3 expressed in late RPCs directly addressed the cell-type specificity of Mettl3's role. Also, the detailed analysis of scRNA data of late RPCs further clarified the transition from late RPCs to the muller glial cells. Furthermore, the authors examined the influences of m6A-associated transcripts on muller glia development by electroporating shRNAs targeting these transcripts into P1 retinae. Besides, additional discussions in the revised manuscript help to clarify the concerns the reviewers raised. In all, all these improvements are satisfying. However, I am surprised that the authors did not provide the background of previous studies of m6A in retinal development. Adding these research backgrounds will further improve the clarity of this study by putting it into context.
