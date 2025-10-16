# Peer review - Round 1

Editors:
- Bernard Malissen, https://ror.org/035xkbk20 Centre d'Immunologie de Marseille-Luminy, Aix Marseille Université France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74183.sa0](https://doi.org/10.7554/eLife.74183.sa0)

CD4 Th2 effector cells contribute to immune responses to helminths and allergens. There exists little information on Th2 cell heterogeneity and clonal distribution between organs. In this manuscript, Radtke et al. investigate the transcriptional signatures of CD4 Th2 cells in the mesenteric lymph nodes and lungs during helminth infection. By using single cell RNA-sequencing including TCR clonotype analysis, the authors define distinct and overlapping transcriptional signatures and clonal relatedness between CD4 Th2 cells in two different tissues at the peak of a type 2 immune response in vivo.


---

# Peer review - Round 1

Editors:
- Bernard Malissen, https://ror.org/035xkbk20 Centre d'Immunologie de Marseille-Luminy, Aix Marseille Université France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74183.sa1](https://doi.org/10.7554/eLife.74183.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Th2 single-cell heterogeneity and clonal interorgan distribution in helminth-infected mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Dominique Soldati-Favre as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Carolyn Genevieve King (Reviewer #1); Ashraful Haque (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Although the work has potential for publication in eLife, it requires essential additional data to support the central claims of the paper. Each reviewer raised substantive concerns (see below) that need to be resolved experimentally. For instance, new experimental approaches to be considered are: (1) perform a time course (2) extend analysis to lung draining lymph nodes and the gut itself and (3) if possible validation of some of the novel findings in mice. Finally, from a conceptual perspective, CD4 T cells assessed via IL-4-eGFP reporter mice cannot be strictly defined as "Th2": this should be addressed in the revised of manuscript.

Reviewer #1 (Recommendations for the authors):

– This reviewer is not an expert in Nb infection, so it is unclear if some of the findings have already been reported using other methods (e.g. flow cytometry for CXCR3, TNFR2, T-bet, Tcf1, etc). The manuscript would benefit from some biologic confirmation of the transcriptional analysis. For example, can the L2 population be detected by FACS (differential expression of CD62L, CCR7, S1PR1) and is this circulating "bridge" population modulated by treatment with FTY720?

– The authors perform clustering analysis on combined Th2 cells from lung and MLN. To better understand heterogeneity within a particular organ it would also be informative to show an analysis of lung and MLNs clustered separately and then assessing cluster similarity between the two organs.

– Could the authors show PCA alongside UMAP? Do velocity arrows look similar on PCA?

– The idea that differentiation occurs from a proliferating population is in line with the literature on many different T cell types (Th2 cells included, https://doi.org/10.1186/s13059-016-0957-5). The data shown here confirms this but doesn't really refer to previous work or competing hypotheses.

– IL-4+ cells were sorted; why are MLN2 clusters considered "Tfh2" rather than just "Tfh"?

– On page 6 it says "gene for PD-1 hardly detectable in the MLN but present in the lung". In Figure 2, it looks like Pdcd1 is all over the MLN (left) side as well and is even one of the discriminating genes for cluster MLN2 on the heatmap. This should be clarified.

– Could the authors comment on the time points chosen for analysis? For example, given the natural course of infection (parasite entering lung, coughed up and swallowed prior to a gut response) is it expected that lung immune cells at day 10 are primed earlier than those from MLN? Could this affect the interpretation of "static" velocity data which is only capable of showing a difference of a few hours between unspliced/spliced?

– The scVelo algorithm finds the end points (root, end) by comparing unspliced to spliced to find the 'stationary states of the velocity inferred transition matrix'. This happens to coincide with the most proliferating cells. Although is certainly plausible, could these cells seem stationary because they are currently "stuck" in cell cycle? In other words, is the signal used by scVelo being dominated by cell cycle genes and will velocity on samples with proliferating cells always see them as an endpoint? I'm not exactly sure how that could be tested, but maybe by regressing out cell cycle genes or removing a certain set of genes from the analysis?

Reviewer #2 (Recommendations for the authors):

There are four main experimental limitations of the study.

First, as outlined in the Public Review, the approach for isolating Il4-licensed, CD4+ T cells from the lung does not separate intravascular and intraparenchymal cells. Cluster L2 is suggested to represent recent immigrant "Th2 cells" into the lung parenchyma. But L2 may simply represent intravascular (circulating) Il4-licensed, CD4+ T cells rather than recent immigrants into the lung parenchyma. The only way to determine these two possibilities would be to perform intravascular staining and separately sort intravascular and intraparenchymal Il4-licensed, CD4+ T cells for scRNA-seq analysis.

Second, the choice to isolate Il4-licensed, CD4+ T cells from the mesenteric lymph nodes and lungs does not give insight into the similarities and differences between two organ systems (gut vs lung). To do so would require isolating cells from the intestines, mesenteric lymph nodes, lungs, and lung-draining lymph nodes. Identifying shared and distinct transcriptional features of Il4-licensed, CD4+ T cells from the gut and lungs is certainly of interest to the field, but the current approach does not clearly define the transcriptional signatures from these two organs.

Third, the authors analyze a single time point (day 10). scRNA-seq and ATAC-seq of CD4+ T cells has been performed in an allergy model of type 2 immunity at various time points (Tibbitt et al., Immunity, 2019). As a result, it remains unclear how the transcriptional signature of Il4-licensed, CD4+ T cells at different sites would change over the duration of helminth infection, especially given the helminth life cycle involves multiple infection stages. Performing scRNA-seq analysis at more than one time point would likely strength the manuscript by providing a longitudinal transcriptional signature. Alternatively, the manuscript could also be strengthened by taking key features from the single time point of scRNA-seq and performing flow cytometry validation over multiple time points.

Fourth, along the lines of the point above, the study provides no validation experiments of the initial two-mouse experiment. The study would benefit from validating key findings via another approach, such as flow cytometry, to help solidify the main conclusions of the manuscript.

Reviewer #3 (Recommendations for the authors):

I am grateful for the opportunity to review your manuscript. I felt the data was generated and analysed appropriately. In general, I felt there was a lack of clear direction in this manuscript. It was unclear what biological questions were being addressed, and importantly, what novel findings were made. While I do not necessarily feel a hypothesis is essential, a clearer objective is required. I outline below several options for improving the work, from broadening the study to other tissues, using additional trajectory inference tools, and conducting experimental hypothesis testing or validation.

Line 98-104: Initial comment on scRNAseq data concerns a gene that is not commonly studied in CD4+ T cells, TAGLN2. This is a confusing start to the Results section. Readers could be better orientated around the data by starting off with established T helper cell markers, such as transcription factors, chemokines and their associated receptors, cytokines and their cytokine receptors, integrins, etc, as well as gene signatures associated with broader cellular processes such as proliferation and metabolism.

Line 108-128: The authors present several observations from the data, but they lack coherence or sufficient detail to discern the biological point being made. In general the first section of the Results section, pertaining to Figure 1, present neither a clear research objective, nor a clear picture of the findings inferred from the data.

Lines 132-219: The authors present a lengthy transcriptomic assessment of clusters defined from an established unsupervised approach. While there may be merit in the description of many of these apparent clusters, the reader is essentially presented with a dry list of observations that do not form a coherent picture. Of most concern is that no inferences, conclusions or hypotheses are clearly articulated at the end of this section, and no biological validation is presented. I suggest that the authors choose to focus this section on the most important novel findings, and by proceeding back to the wet-lab, they might consider testing their novel findings experimentally.

Lines 224-248: Trajectory inference of cells harvested from a single timepoint, presented solely as the output from an RNA Velocity analysis, is of questionable merit. I suggest that any inferences from RNA Velocity should be tested using other trajectory inference tools, for example Slingshot, Monocle, PAGA etc, when conducted on more than one low-dimensional embedding, e.g adding to this manuscript use of single-cell Variational Inference (scVI) from the Yosef lab. Once a robust inference has been made, this should be tested experimentally in mice.

Lines 253-380: The authors present an extensive assessment of TCR clones across MLN and the lung, but while the analysis appears entirely appropriate, unfortunately no clear biological question is conveyed, and the reader is left wondering at the significance of these data. Crucially, no new hypotheses are presented, and no experimental testing undertaken. To extend this study, I suggest formulation and testing of a hypothesis based on the TCR data.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Th2 single-cell heterogeneity and clonal distribution at distant sites in helminth-infected mice" for further consideration by eLife. Your revised article has been evaluated by Dominique Soldati-Favre (Senior Editor) and a Reviewing Editor.

CD4 Th2 effector cells contribute to immune responses to helminths and allergens. There exists little information on Th2 cell heterogeneity and clonal distribution between organs. In this manuscript, Radtke et al. investigate the transcriptional signatures of CD4 Th2 cells in the mesenteric lymph nodes and lungs during helminth infection. By using single-cell RNA-sequencing including TCR clonotype analysis, the authors define distinct and overlapping transcriptional signatures and clonal relatedness between CD4 Th2 cells in two different tissues at the peak of a type 2 immune response in vivo.

The authors have done a reasonable number of additional experiments and their analyses greatly improved the original study. As described below a couple of minor revisions need to be, however, addressed and uploaded in a final revised version of the manuscript.

1. The authors need to make clear that some of the differences that they have found are differences related to T cells found in peripheral tissue vs. T cells found in a lymph node as opposed to differences in T cells found in the lung vs. gut.

2. The authors also need to clarify more explicitly that since they did not distinguish intraparenchymal T cells from intravascular T cells in their lung preparations and single-cell analyses, that some of the cells included in their data set were likely intravascular (blood) cells and not intraparenchymal cells.

3. It was not clear as to how many mice were used for the repeat scRNAseq experiment.

4. Finally, the TCR cloning and retrogenic experiments that were presented constituted a strength of this revision and certainly opens the door for further interesting experiments with this infection model. Along that line, the authors missed an interesting opportunity to phenotype the Nb TCR transgenic cells that expanded in vivo. Moreover, it might be useful to specify in the Results or Discussion whether TCR transgenic reagents currently exist for this infection model. If they do not exist, the authors might present them to help researchers follow helminth-specific CD4 T cell responses.
