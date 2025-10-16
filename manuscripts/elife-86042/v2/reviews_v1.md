# Peer review - Round 1

Editors:
- John G Albeck, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86042.sa0](https://doi.org/10.7554/eLife.86042.sa0)

This paper presents an important investigation of the relationship between cell morphology, actin cytoskeletal features, and NF-kappaB/RELA signaling dynamics. Solid evidence is provided using quantitative live-cell imaging of pancreatic cancer cell lines. These analyses better establish the connection of cell shape to the NF-kappaB signaling pathway, highlighting the importance of the actin network and several specific regulators in a feedback loop controlling NF-kappaB activity. Because NF-κB controls inflammation and cell survival, this study will be of interest in the fields of cancer and immune signaling.


---

# Peer review - Round 1

Editors:
- John G Albeck, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86042.sa1](https://doi.org/10.7554/eLife.86042.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Actin networks modulate heterogenous NF-κB dynamics in response to TNFα" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including John G Albeck as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Myong-Hee Sung (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication in its current form by eLife.

Specifically, while the reviewers found the approach and overall message of the paper to be potentially of significant interest, a number of concerns were raised about the methodology and inconsistencies within the data. After consultation, the reviewers came to the consensus that the results as they currently stand are insufficient to support the main conclusion of the paper. The main concerns are as follows:

1. The "cytoplasmic ring" method is not an appropriate approach to quantifying the nuclear/cytosolic ratio of RelA in this study. Although this approach is commonly used in the field, it is sensitive to changes in cell shape, raising the possibility that associations based on this measure could be artifacts. The reviewers have made a number of suggestions for how this issue could be mitigated and controlled.

2. The overall evidence for a causal relationship between actin morphology and NF-κB signaling is insufficient to support the main conclusion. Bayesian network analysis is useful for uncovering statistical relationships, but it cannot be used to make hard conclusions about causality. While pharmacological perturbations could in principle be used to support the associations identified by the Bayesian network analysis, the results from these experiments were inconsistent and seemingly contradictory: in some cases where the drug treatments modified the actin structures implicated by the network analysis, no clear effect on NF-κB was observed.

3. The differences in NF-κB signaling in the two PDAC cell types examined by live-cell imaging, both between the lines and between these lines and other cell types in the literature, raise significant questions that are not addressed in adequate detail to conclude that negative feedback is simply weaker in these cells. The data suggest that these cells diverge significantly from how the pathway works in other cells types. At a minimum, this difference must be presented more carefully, and it would greatly strengthen the paper if negative feedback genes could be analyzed to provide an explanation for the unusual behavior of the pathway in these cells.

While these issues prevent eLife from further considering this paper in its current form, we would be open to considering a new submission in which these issues are addressed, attempting to reach the same reviewers.

Reviewer #1 (Recommendations for the authors):

In this study, the authors set out to profile the kinetics of RELA translocation in pancreatic cancer cells. RELA translocation is a widely studied event that occurs in response to a number of inflammatory stimuli, and the authors begin by profiling RELA translocation kinetics in two PDAC cell lines. Relative to other cell lines where this analysis has been performed, the two PDAC cell lines show more sustained signaling (to different extents), rather than oscillatory nuclear localization. Like many other cell lines that have been studied, the authors observe a large degree of heterogeneity in RELA translocation within cells stimulated with physiological doses of TNF. A thorough analysis based on a knock-in PCNA marker reveals that this heterogeneity is not linked to the cell cycle. The authors then hypothesize the connection between actin morphology based on their previous work, and turn to an analysis of 5 PDAC cell lines, using a fixed-cell immunofluorescence assay to quantify RELA translocation, F-actin, and tubulin in each cell. From images of thousands of fixed cells, a series of statistical analyses are used to identify correlations between cytoskeletal morphology and RELA nuclear abundance. This approach reveals clear associations between certain cytoskeletal features and RELA translocation, with substantial differences between cell lines. A follow-up experiment correlates live-cell RELA kinetics with fixed-cell cytoskeletal stains, which provides further support for their associations. Finally, they perturb actin and tubulin function with a variety of chemical agents and quantify the resulting effects on live-cell RELA kinetics. This again shows variation between cell lines but confirms that direct perturbation of cytoskeletal processes can modulate the ability of TNF to stimulate RELA translocation. Together, these lines of evidence provide substantial support for the hypothesis that NF-κB signaling can be modulated downstream of changes in actin dynamics. While there is significant variation in how this works between cell lines, which suggests that a broader exploration of other cell lines will be needed in the future, the data shown here are, with some limitations noted below, adequate to support the authors' hypothesis.

A major strength of this manuscript is its use of quantitative imaging to exploit the existing heterogeneity between cells at a physiological dose of TNF. A series of clever analysis methods are used to draw out correlations that can be found between actin morphology (immunostained) and RELA translocation (either immunostained or by live-cell microscopy). Also important is the careful characterization of NF-κB signaling in pancreatic cancer cells, where this pathway is known to play a role. Importantly, RELA kinetics are assessed using a knock-in fluorescent protein tag, avoiding potential artifacts from overexpression. An interesting feature of this analysis is the use of Bayesian networks to model the dependencies of actin features; to my knowledge, this is a novel use of this algorithm. The drug perturbation data are also beautifully presented, in a way that reveals the full complexity of the cellular responses. In general, the data and conclusions are very clearly presented, and the authors do not shy away from describing the context-dependent intricacies of their observations. The main conclusion that NF-κB signaling is strongly affected by actin dynamics ties together two major signaling axes in cancer cells, and would be of interest to the many researchers working in these two areas. The methods used to show associations at the single-cell level will also have a significant impact on others working with mixtures of live and fixed single-cell data.

There are several weaknesses that limit the interpretability of the findings:

1. It is not clear how the effects of cell shape changes on the recorded nuclear/cytoplasmic ratio are controlled for. Cell shape is a major variable in this study and can alter the apparent (recorded) intensity of nuclear and cytoplasmic stains in many imaging and analysis pipelines, independent of any actual changes in a marker's localization. Without such an assessment, it isn't clear whether differences in RELA behavior (the main observation in the paper) are influenced by how the detection process treats cells with different morphologies.

2. It is not clear whether the cytoskeleton-linked effects are specific to RELA, or rather reflect more widespread changes in nuclear import/export rates. There are reports that changes in actin function can alter nuclear-cytoplasmic translocation (for example, PMIDs 16120220, 31444357). Understanding whether the observed actin-dependent effect on NF-κB localization is unique to this signaling pathway, or a non-specific effect on multiple pathways is important to the interpretation of the findings.

3. It is difficult to assess the importance of the observed differences in RELA translocation without additional information on the pathway's output. Translocation of RELA is an important marker and is known to modulate many downstream genes involved in inflammation. However, given the differences in RELA behavior observed here in PDAC cells, it is difficult to extrapolate from previous work to evaluate whether the actin-modulated changes impact RELA's transcriptional effects. Establishing that such differences exist would be important to conclude that actin shape changes have a biologically significant effect on NF-κB signaling with the potential to alter cellular behavior.

Suggestions that would have a major impact on the interpretability of the study:

1. NF-κB target gene expression, either at the RNA or protein level, should be assessed using a method of the authors' choice. Immunofluorescence for known NF-κB targets could be performed and coupled to the single-cell analysis, comparing expression levels between cells with different actin morphological features. Alternatively, bulk RNA or protein measurements for NF-κB targets could be made on cells treated vs. untreated with actin-perturbing agents.

2. It should also be established whether actin-mediated changes in nuclear import/export are restricted to RelA or occur more generally. Changes in overall nuclear import/export could be assessed using an NLS/NES-containing fluorescent protein reporter, followed by leptomycin B treatment, in a similar setup to the RelA translocation assay. A number of other methods would also be possible, such as testing whether other nuclear localization-based signaling reporters show differences in cells with different actin parameters.

3. The effects of cell shape on the recorded nuclear/cytoplasmic ratio should be quantified. This could be done using generic cytoplasmic and nuclear markers (ideally ones that do not translocate significantly), and testing whether their N/C ratio varies between cells of different shapes/morphological classes.

Reviewer #2 (Recommendations for the authors):

The work by Butera et al. investigates the relationship between the cellular cytoskeleton and NFkB dynamic response to TNF. The authors use single-cell fixed and live cells measurements of RelA dynamics and cellular morphology, pharmacological perturbations, and extensive statistical analysis to draw specific conclusions on what aspects of the actin cytoskeleton modulate TNF-dependent NFkB response. I have identified multiple issues that raise concerns that the conclusions of this paper are not supported by the data presented.

1. The possibility of confounding factors between cell morphology and the approach used by the authors to analyze NFkB dynamics (Figure 1D). The analysis of NFkB dynamics presented here is based on an image segmentation strategy that relies on a single marker, PCNA, and segmentation of the nucleus and "ring" around the nucleus. This strategy should only be applied in contexts where cell shape is not changing and is not a key factor in the investigation and it cannot be used to investigate the dependency of NFkB on cell shape. The main issue is that the "ring" is not a good proxy for the actual concentration of the fluorescent marker in the cytoplasm. For example, in a case where the marker (RelA-GFP in this case) is not changing, the measurement of the "cytoplasmic" signal can change as the cell spreads from a rectangular shape with limited lamellipodia to a cell that is very spread with thin lamellipodia. This change does not mean that the concentration of the marker in the cytoplasm changed, it just reveals the use of "ring" as a proxy is limited. This puts the key measurement of this work in doubt as it is the key theme throughout this paper. To give just one example, as the number of "neighbor contact" increases, cells tend to have thicker and less spread morphology (i.e. they are just denser in culture). Thicker cells will have more cytoplasm in the "ring" compared to very spread cells and therefore the denominator of RelA will be bigger that will cause the overall RelA ratio to be smaller which is exactly what the authors show in Figure 4D. Just to be clear, this is not just an issue with cell thickness, the estimation of total cytoplasmic intensity from a "ring" inherently depends on cell morphology. Therefore, one simply cannot state that RelA activation itself depends on cell morphology using this analysis method.

2. Bayesian network analysis does not provide a causal relationship. The authors make extensive use of Bayesian networks (BN) for inferences of dependencies (Figures 3 and 4). In this analysis, the authors aim to identify the direction of dependency between different nodes in the BN. This is problematic for two reasons. First, The direction of arrows in bayesian networks does not imply causations (i.e. modulation). The direction of arrows in BN only represents correlation and the directionality should not be interpreted as causative. Yet the authors clearly make a key distinction whether RelA depends on a morphological feature or whether the feature depends on RelA. In the literature that the authors cite (e.g. Sachs et al. 2005) pharmacological perturbation is used to infer causation, not the inference of the structure of the BN. Second, the authors did not consider that other factors, not included in the model, could influence both RelA and morphology. For example, if an unknown kinase changes both NFKB and a specific cellular feature the inferred network will still look the same. Therefore, the conclusion that actin-based cellular features modulate (i.e. cause) differences in RelA dynamics is simply unsupported by the BN analysis.

3. Lack of support by pharmacological data. Beyond correlation analysis, the authors used a pharmacological approach to show that manipulation of the cytoskeleton causes changes in RelA dynamics. The data presented in Figures 1-5 makes specific predictions. If one is to interpret the arrows in the BN as the authors present them, one will conclude that perturbations of features like "nuclear roundness" that was presented as key "modulator" of RelA dynamics will cause a change in RelA dynamics. The vast majority of the pharmacological perturbations used by the authors, even those that caused >2 SD change in "nuclear roundness", had very little impact on RelA dynamics. In my reading, this directly invalidates the core conclusion made by the authors on the ability of the actin cytoskeleton to modulate RelA dynamics.

The only drug that seemed to show a meaningful impact (my interpretation as rigorous statistical analysis of this that includes correction of multiple hypotheses is missing) was SMIFH2 which downregulates Formin activity. Naively, I googled "SMIFH2 off target" and found multiple publications suggestions that SMIFH2 has putative off target effects on other proteins such as Myosin (PMID: 33589498) but also completely unrelated targets such as P53 (PMID: 25925024). Therefore I find that the data presented in Figure 6, rather than supporting the authors' conclusion effectively invalidate it.

4. The values of RelA nuclear-cytoplasmic ratio are different across the figures in ways that I was unable to follow. In figures 1-2 the values are ~0.9-1.4. In figures 3B and 4D the same cell lines show a range of 0-3, and 0-5. Figure 3D shows RelA on a log10 scale with values are from -0.5 to 1.5 (3-33 on a linear scale). As it is presented now, this data limits the ability to draw conclusions based on RelA values across figures.

5. The authors perform cluster analysis followed by ANOVA between the clusters. This is problematic and is known as "double-dipping" and it could invalidate the statistical inference (see https://arxiv.org/abs/2012.02936). As the authors don't really use the clusters for any of their conclusions, the grouping can be avoided and analysis done directly on RelA values using correlation analysis with key features. As the authors effectively show in Figure 5A that a simple measure (RelA at 60min) is basically equivalent to cluster identity, this could substantially simplify the work and many of the panels in Figure 2 could be removed.

6. The statement made by the authors about the differences in negative feedback signaling between the two cell lines (line 153) is presented as a conclusion when in fact it is a reasonable hypothesis that is not supported by any of the data shown in the manuscript.

7. The features selected after feature selection are referred to as "independent features", yet the PCA data shown by the authors clearly show that they are not independent of each other.

8. The statement regarding the tSNE analysis (lines 279-282 and Figure 5B) is incorrect as tSNE does not preserve distance metrics and therefore proximity of points in tSNE space is not indicative of actual similarity (see: https://distill.pub/2016/misread-tsne/).

9. A more subtle version of the "double-dipping" problem mentioned in point 5 above exists in Figure 5CD. When the features tested are correlated with the features used to create the clusters, one cannot simple ANOVA between the clusters for statistical inference.

10. The inferred strengths of the arcs in the BN analysis don't fully support the authors' interpretations. For example, in Figure 4C the connection between all morphological features and RelA is very low (2-50) compared to other arcs in the same network (arc lengths are around a few hundreds with max at 4095).

11. The statistical significance of the pharmacological perturbation on RelA should be presented including controls for multiple hypothesis testing.

Specific recommendations:

The dynamic of NFkB can be assessed directly by the nuclear fraction without the cytoplasmic values. This could avoid many of the challenges related to issue 1. Care should still be taken to verify that nuclear signal doesn't vary and creates dependency, but this is much easier compared to the "ring". This is especially true for knock-ins used by the authors where there is no need to "normalized out" ectopic high overexpression levels.

Cluster analysis followed by statistical inference should be avoided and direct inference on the features used for analysis should be done instead.

Reviewer #3 (Recommendations for the authors):

The authors present a deep investigation of the relationship between cell morphology, actin cytoskeletal features and NF-kappaB RELA signaling dynamics. Quantitative live-cell imaging of endogenous RELA (using CRISPR knock-in) and data analyses are leveraged to provide insight into the little-understood roles of actin networks in inflammatory responses of PDAC cells to TNF-α. While the focus is clearly on cell shapes and cytoskeletal features, it will help put the study in the context of others if the PDAC cells are better characterized in terms of the negative feedback loops of NF-kappaB, such as IkappaB α or IkappaB epsilon proteins. As the authors indicated, these results altogether may provide new ideas for therapeutic interventions for PDAC.

1. As the authors mentioned in Discussion (lines 370-373 "…, other studies reported more rapid cytoplasmic REL relocalisation…"), the rapid fall of nuclear RelA (around 40 minutes after TNF-α) has widely been reported by several groups (Alexander Hoffmann, Michael White, Markus Covert, Myong-Hee Sung, Savas Tay and their colleagues), but is absent in both PDAC lines. This indicates that the negative feedback genes such as IkappaB α/epsilon or A20 may have very different kinetics if they are induced at all in these cells. It seems important to determine if this is a property of the parental PDAC cells or an acquired feature in the CRISPR knock-in reporter cells during the generation of the two reporter lines. RTqPCR of a few key negative feedback genes in the parental and derived reporter cells, as well as a control cell line (HeLa, MCF10, or THP-1) would be a straightforward way to answer this question. While this is not the focus of the study, I think that understanding which feedback is dysfunctional is probably relevant for therapeutic strategies against PDAC. It would also help the NF-kappaB signaling community understand the common and distinct features of dynamics observed in different cell systems.

2. On page 7 lines 154-155 "… negative feedback regulation is intact in PANC1…" is too simplistic, given the very slow fall of nuclear RELA even in PANC1. See comment #1 above. It looks like IkappaB feedback genes are strongly compromised in both PDAC lines. Again, this could be an important feature of PDAC and needs to be verified as suggested above. The evaluation of gene induction by RTqPCR would also be reassuring that the C-terminal fusion of RELA is transcriptionally as active as the native RELA protein, even though the EGFP is tagging the transactivation domain (important for NF-kappaB recruitment of co-factors and transcriptional machinery to the target chromatin).

3. Figure 5 has data that will be of broad interest to the community, and I was hoping to glean some recurring theme about what features may affect NF-kappaB signaling. The key results seem to be in 5C-E, but it is not easy to read off which relationships may be shared between the two PDAC lines. It will be helpful if all the ten features are shown for each cell line to see an overall pattern, even though some may fall below statistical significance. 'Actin filament/cell area' shows opposite trends in MIA PaCa2 and PANC1. It seems like 'neighbor contact' was the only feature shared by the two cell lines based on the Bayesian analysis. This was somewhat dissatisfying because it complicates any extrapolating speculations of these findings to other cell systems. But the authors seem to have done a thorough analysis using both ANOVA and Bayesian methods.

4. Cytoskeletal structures may influence rates of oligomerization or recycling of the cell surface receptors for TNF-α. Any thoughts on such indirect effects through the upstream signaling events of NF-kappaB activation?

5. The color scheme used in heatmaps (e.g. Figure 2 panels C and I) is problematic because the white is for both the strongest RelA ratio and NAs (missing values). Please use a different color scheme.

6. Figure 2-supplement 1E seems to show M1-M4 labels mixed up. Please check.

7. In line 263 "… correlation between RELA ratio and breast epithelial…", some word seems missing. Does it mean correlation between RELA ratio and "neighbor contact"?

8. In line 310, please describe what inhibitor SMIFH2 is at the first mention, for the general readers.

9. In line 313, what does "…for 2 hr then simultaneously with 10 ng/ml TNFalpha for 1 hr." mean? Consecutive treatment or simultaneous co-treament?

10. In line 420, is "NIH-T3" NIH-3T3?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Actin networks modulate heterogenous NF-κB dynamics in response to TNFα" for further consideration by eLife. Your revised article has been evaluated by Jonathan Cooper (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions (for the authors):

1) Details on the methods used for transcriptional profiling and gene expression analysis should be provided. Reviewers' requests for additional technical clarifications throughout the paper should be carefully considered and addressed where possible.

2) The method used to quantify "time to first peak" for RELA translocation should be made consistent with similar studies in the field, as noted by Reviewer 2, or should be clarified with explanations of the apparent differences relative to previous literature.

3) Inconsistencies between the text and the data shown for expression differences, as noted by Reviewer #2 (point 2) should be rectified or further explained.

4) Knockdown efficiency for the siRNA experiments should be evaluated with additional data to demonstrate the degree of heterogeneity in knockdown between cells for genes other than RELA. Alternatively, data should be provided to support the assumption that the efficiency of RELA knockdown, at the single-cell level, is representative of the other knocked-down genes.

5) Clarification of replicates and statistical significance should be provided for experiments where noted by reviewer 3.

Reviewer #1 (Recommendations for the authors):

In this revised manuscript, the authors have added substantial new analysis to address the primary critiques of the original manuscript. The authors have made significant changes to their image processing methods and Bayesian network modeling presentation, which in my opinion are adequate to answer the critiques raised on these points. Perhaps the largest change to the manuscript is the inclusion of an RNA-seq experiment and follow-up with knockdowns of genes of interest found in this dataset. The strongest point of this addition is that it is used to investigate the mediators of negative feedback and their differences between the two cell lines analyzed. The RNA-seq data are also used to make a connection between NF-κB activity and actin regulation, which as discussed below, makes less of an impact on the overall conclusions of the paper.

Overall, the changes do significantly strengthen the manuscript, but some revisions are still needed to fully integrate the new data.

1. By displaying NF-κB localization strictly as nuclear intensity, they avoid the difficulty of using a cytoplasmic ring to calculate nuclear/cytoplasmic intensity, a measurement that can be affected by the cell shape changes induced in their study. However, their description of the method lacks a few details – in particular, is the nuclear intensity calculated as the total RELA signal per nucleus, or the average pixel intensity over the nuclear region (line 567)? Also, the ring method is still used in the fixed cell measurements; it would be helpful to comment in more detail on the previous work that supports the insensitivity of this measurement to cell shape changes (the authors refer to Sero 2015 in their response, but it isn't clear to me where in that manuscript the ring method's response to cell shape is evaluated).

2. The addition of RNA-seq analysis provides a significant amount of new data, and the inclusion of the IkB super repressor is a nice feature of this dataset that helps increase its interpretability. However, overall this addition feels incomplete. There doesn't appear to be any description of the relevant experimental procedures in the methods section. Also, the conclusions from these experiments seem somewhat indistinct. Two actin-regulating genes, NUAK1 and ARHGEF31, are identified as targets of NF-κB, and it is shown that their knockdown modestly changes RELA translocation kinetics. However, this finding doesn't address the question of whether the actin-mediated modulation of NF-κB, which is the focus of the first part of the paper, has a functional role in altering gene expression. Thus, the last section is potentially useful, but a bit confusing in juxtaposition to the first part of the paper.

Reviewer #2 (Recommendations for the authors):

The authors have improved the manuscript extensively both in terms of re-analysis and re-organization of the original data and newly added experimental data and results. I appreciate the effort invested in carrying out such a major revision in response to the original comments from me and other reviewers. Many of my comments have been addressed fully or are no longer relevant in the revised version. The authors performed RNA-seq and GFP-trap experiments partly to address my concern about understanding the core regulatory circuit of NF-kappaB in these PDAC cells. However, some details are missing, and clarifications are needed in several places. While there are numerous points to commend about in this much improved version, in the interest of space, I focus here on remaining issues that need to be addressed before the manuscript can be accepted for publication.

New comments:

1. The authors note that "the time to peak RELA was highly heterogenous" (line 103). It seems like their definition is different from what other groups have been using. Instead of detecting the *time to the first peak*, it seems like the reported time to peak is catching the *time to maximum value* of nuclear RELA. This is apparent in Figure 1C (easier to see on the right side, e.g. dose response plot of MIA PaCa), where the first peak occurs earlier for the higher TNF dose (which many groups have reported to be valid in multiple cell types. For example, shown by Markus Covert, MH Sung, Michael White, etc). But the panel 1E shows the time to peak is more than 100 minutes (unit is missing in the y axis, by the way), while panel 1C shows a rapid first peak (e.g. < 30 min for 10 ng/ml TNF). I suggest the authors update their definition of time to peak and provide a more accurate quantification of the dose-dependent timing of first peak (well established in the field). With the revised definition, the time to peak may be actually not so heterogenous between individual cells (based on the data spread in panel 1C time course plots). Moreover, the time to peak of 100 minutes is not compatible with the choice of 1 hour TNF treatment in the subsequent immunofluorescence analysis. This needs to be corrected.

2. There are a few puzzling disconnects between Figure 3 Supplement panels 1A and 1A'-A'. For example, the authors interpret the data in these statements: "NFKB2 is only affected by IκB-SR induction in PANC1 cells (Figure 3 – Supplement 1A).", "NFKB1 is unaffected by RELA-inactivation by IκB-SR in both cell lines", "NFKBIA and NFKBIB were not significantly impacted by RELA inactivation in either cell line, while NFKBIE expression was reduced with IκB-SR in PANC1". But looking at panel 1A, NFKB2 induction is absent in MiaPaCa with IkB-SR; NFKB1 induction is also affected at 5h in both cell lines; NFKBIA induction is off but instead, the constitutive expression is higher (which indicates a high basal transcriptional activity either by NFkB or other TFs like glucocorticoid receptor). Are these simply an outcome of the statistical testing criteria? The discrepancy seems too numerous and pronounced to warrant some double-checking and/or explanation.

3. How was knockdown efficiency assessed (other than RELA) in the data of Figure 4? Individual cells may show significant heterogeneity in siRNA knockdown (which is different from the RELA siRNA), so I wonder if some of the single cell traces may be from those that didn't have a reduced abundance of the target protein (as well as the mRNA).

4. In line 122 "…no differences between cells by cell cycle stage in terms of peak RELA measurements…", it will be good to note that this is in contrast to Michael White's report on cell cycle dependence (Ankers et al. https://elifesciences.org/articles/10473). It is important to note that the crosstalk between cell cycle and NFkB is cell type specific.

5. Regarding the result "Interestingly, the NF-κB protein REL also had reduced interaction with RELA with TNFα.", there is a recent publication (Rahman SMT et al. https://www.cell.com/cell-reports/fulltext/S2211-1247(22)01556-X) reporting that the RelA:c-Rel heterodimer was depleted in the nucleus of TNF-α activated fibroblasts. This reviewer, being the senior author of the study, can't help but find this quite remarkable, and I think that the corroboration might be noteworthy in interpreting the GFP-Trap data.

6. Figure 2: The Bayesian-inferred arrows are sometimes in opposite directions between panel C and panel F (drug treatment data). Any explanations that can help readers understand would be good.

7. Figure 1-Supplement 1 panel A: Please specify that these images are from PCNA.

8. In Figure 4B legend, something seems to be missing in "(p < value)". In 4C, PCNA Scarlet is supposed to be shown.

9. Figure 4-Supplement 1: Indicating "siRNA" and "F-actin stain" in this figure would be helpful, even though they are described in the figure legend.

10. Figure 2C: In the legend, there seems to be a mix-up of "purple" for "orange" arcs in line 864.

Previous comments that still need attention (in original numbering, followed by additional comments appended after "and"):

1. As the authors mentioned in Discussion (lines 370-373 "…, other studies reported more rapid cytoplasmic REL relocalisation…"), the rapid fall of nuclear RelA (around 40 minutes after TNF-α) has widely been reported by several groups (Alexander Hoffmann, Michael White, Markus Covert, Myong-Hee Sung, Savas Tay and their colleagues), but is absent in both PDAC lines. This indicates that the negative feedback genes such as IkappaB α/epsilon or A20 may have very different kinetics if they are induced at all in these cells. It seems important to determine if this is a property of the parental PDAC cells or an acquired feature in the CRISPR knock-in reporter cells during the generation of the two reporter lines. RTqPCR of a few key negative feedback genes in the parental and derived reporter cells, as well as a control cell line (HeLa, MCF10, or THP-1) would be a straightforward way to answer this question. While this is not the focus of the study, I think that understanding which feedback is dysfunctional is probably relevant for therapeutic strategies against PDAC. It would also help the NF-kappaB signaling community understand the common and distinct features of dynamics observed in different cell systems.

and

In response to this comment, the authors "carried out RNAseq with MIA PaCa2 and PANC1 cells with endogenously tagged RELA-eGFP". However, no methods are described in the manuscript itself regarding RNA-seq, either in the Methods or figure legends. Therefore, the readers would be left guessing if the samples were from the parental PDAC or the imaged cell lines. This might be an oversight; regardless, authors need to provide the method section on RNA-seq, including sample source, replicates, sequencing platform, data processing and analysis. Also, an accession ID for the RNA-seq data should be provided after depositing the dataset to a public data repository such as GEO, which is a standard requirement, I believe.

If the RNA-seq was done on the knockin reporter cells (as stated in the response), then the analysis does not directly address the question I raised in the original comment ("…determine if this is a property of the parental PDAC cells or an acquired feature in the CRISPR knock-in reporter cells during the generation of the two reporter lines"). Barring another round of RNA-seq analysis on the parental cell lines, for a minimum effort, the authors can perform RTqPCR of NFKBIA, NFKBIE, REL, RELB, NFKB2 (those found to be regulated by RelA in the reporter cells) in both the parental and the reporter cells. This would confirm that the observed NF-κB pathway gene expression patterns are indeed a property of PDAC cells.

4. Cytoskeletal structures may influence rates of oligomerization or recycling of the cell surface receptors for TNF-α. Any thoughts on such indirect effects through the upstream signaling events of NF-kappaB activation?

and

The author response to this comment contains quite extensive information. The content, or a brief summary, seems to warrant inclusion in the main text of the paper, either in the Results or Discussion. This is an aspect that is not the focus of the study but may be acknowledged as complementary mechanisms to be explored in future studies. Such a bigger picture discussion might encourage readers to explore open topics in their own studies.

Reviewer #3 (Recommendations for the authors):

A revised manuscript presents the study of NF-κB signalling in PDAC tumours. The authors demonstrate that the TNF-induced responses of the canonical p65 signalling are mediated via F- actin dynamics. I believe this represents a novel and important finding.

New data in the revised manuscript provide an analysis of TNF-induced gene expression via RNA-seq and identify specific feedback mechanisms, involving IkappaB inhibitors and family members (RelB) as well as actin regulators NUAK2 and ARHGAP31. Furthermore, the authors perform siRNA knockdown experiments to validate specific targets, which provide an excellent contribution to the narrative.

The manuscript is presented well and analyses are performed to a high standard. However, the manuscript suffers from some ambiguities regarding sample sizes and statistical analyses. Firstly, most if not all data is not triplicated, instead duplicates while some technical replicates are presented (e.g., Figure 1, Figure 3, Figure 3 S1, Figure 4) -sometimes no information at all is provided (Figure 4C, Figure 4 S1). While part of this info is provided in methods, these should be included in appropriate captions. Secondly, there are limited details in terms of the statistical analyses, typically t-tests are performed (with corrections for multiple testing), often in the case of seemingly small sample sizes. E.g. Figure 3 S1 A' A'- t-test based on 2 samples (as far I understand). T critical he siRNa KO experiment (Figure 4) seems to involve 6 or 8 samples (judging by eye Figure A and B), for which typically a non-parametric test should be used instead. Given that the effect of siRNa-KO (in particular of the actin regulator genes) on p65 dynamics in the live-cell imaging data is subtle (Figure 4A), this poses questions about whether the conclusions are robust.

Specific comments:

1. Line 41: "However, most studies characterising RELA translocation dynamics following stimulation use hyperphysiological TNFα doses (e.g. 10 ng/ml) and exogenous RELA reporters." This sentence is not accurate…both have been studied for more than 10 years, e.g. see [1-3],

2. Lines 106-112: Authors report correlations between different times, are they suggesting that total p65 is regulated? Please explain or provide the measurement of the total p65 over time.

3. RELA translocation responses to TNFα are cell cycle independent: Please discuss in the context of the previous work on this subject [4].

4. Figure 1 and S1 have no description of statistical tests

5. Figure 2C: numbers characterising the strength of the relationship span over 3 -orders of magnitude. Please comment on their statistical significance…

6. 2F. Please provide some validation that chemical perturbation causes measurable changes in any of the cell features…in addition to affecting high-level Bayesian analysis. 2F please provide how many cells analysed

7. Figure 3 A. How many replicates were assayed, and how the information about different time points is provided on the graph?

8. Figure 3 S1 A' A'- Statistical analysis using t-test based on 2 samples (as far I understand). (also line 283 in the text).

9. Figure 4 "To identify whether siRNAs affected the early/peak RELA and sustained RELA response to TNFα, we calculated the fold change of mean nuclear RELA with each siRNA to NT siRNA at 1 hr or 12 hr TNFα stimulation, and compared fold changes using t-test with multiple comparison correction (Figure 4B and 4C)."

The effect of NUAK2 and ARGHAP31 siRNA KO appears to be subtle in live cell imaging from A- is there a statical difference in the AUC or any other characteristics of p65 responses?

Analysis in 4B is critical, but not clear to me what is the sample size (how many wells…) and how matching was performed. By eye, it seems that the sample size is between 6-8, but please explicitly provide the number in the legend. T-test with small sample size is not appropriate, a non-parametric test should be used instead.

10. Figure 4C and Supplementary info- no information about data replication -just some images are shown.

11. Line 354: MIA PaCa2 and PANC1 cells in the presence of ARHGAP31 siRNA showed flatter morphology and reduction of stress fibre abundance, while NUAK2 siRNA visibly increased actin abundance and the presence of lamellipodia in both cell lines. -> These claims should be statistically tested based on the replicated data.

12. Line 318: (Figure 4A-D) -there is no D in the figure

Refs:

1. Sung MH, Salvatore L, De Lorenzi R, Indrawan A, Pasparakis M, Hager GL, Bianchi ME, Agresti A: Sustained oscillations of NF-kappaB produce distinct genome scanning and gene expression profiles. PLoS One 2009, 4:e7163.

2. Tay S, Hughey JJ, Lee TK, Lipniacki T, Quake SR, Covert MW: Single-cell NF-kappaB dynamics reveal digital activation and analogue information processing. Nature 2010, 466:267-271.

3. Turner DA, Paszek P, Woodcock DJ, Nelson DE, Horton CA, Wang Y, Spiller DG, Rand DA, White MR, Harper CV: Physiological levels of TNFalpha stimulation induce stochastic dynamics of NF-kappaB responses in single living cells. J Cell Sci 2010, 123:2834-2843.

4. Ankers JM, Awais R, Jones NA, Boyd J, Ryan S, Adamson AD, Harper CV, Bridge L, Spiller DG, Jackson DA, et al: Dynamic NF-kappaB and E2F interactions control the priority and timing of inflammatory signalling and cell proliferation. ELife 2016, 5.
