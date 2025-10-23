# Peer review - Round 1

Editors:
- Carol A Mason, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71864.sa0](https://doi.org/10.7554/eLife.71864.sa0)

Your study is a thorough transcriptomics study demonstrating previously uncharacterized transcriptional diversity, discriminating the embryonic domains that produce interneurons. You have responded well to the requests for amendments, adjusted figures and better emphasized gene diversity in the ganglionic eminence.


---

# Peer review - Round 1

Editors:
- Carol A Mason, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71864.sa1](https://doi.org/10.7554/eLife.71864.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Transcriptional heterogeneity of ventricular zone cells throughout the embryonic mouse forebrain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife at this time.

The three reviewers found your study of transcriptional diversity of cortex and ganglionic eminences (GE) of the mouse embryo, focusing on progenitors that produce cortical interneurons of the brain, of importance to the field. They appreciated your use of a Nestin GFP line enabling enrichment for progenitors, and were positive about your finding of previously uncharacterized transcriptional diversity discriminating the embryonic domains producing interneurons.

Nonetheless, even with your novel findings and extensive analysis, the reviewers concurred that potential impact of the study is weakened by technical concerns on the sc RNA Seq analysis as well as by the lack of data supporting relevance of observed sub-types. They call for lineage analysis of at least one potential progenitor subtype to bolster the notion that transcriptionally heterogeneous progenitors are relevant to different fate outcomes. There was praise for the in situs but a call for additional in situ analysis, adding more genes and looking at different embryonic stages. Finally, they suggest that you pose your findings more broadly and beyond the lists of genes, classifying potential subtypes in a model to implicate which are primarily early born and those that are late born. Some of these revisions would be possible without performing additional work (cleaning up the sc RNA Seq analysis) but other inquiries would require further bench work. We hope that the reviewers' comments will help you to strengthen your story based on this data set.

Reviewer #1:

The manuscript describes the RNA fingerprint of developing telencephalic cells. To focus on progenitors, the authors use a transgenic line that drives the expression of a destabilized-venus GFP under the Nestin promoter. With this strategy, the authors find higher diversity of developing precursors than when they dissociate single cells from unlabeled WT brains because the latter contains higher proportions of postmitotic cells. The main finding is that early VZ precursors are more heterogeneous than inferred from previous studies. In situs in brain sections confirm molecularly distinct clusters of progenitors in medial, lateral, and dorsal VZ. The work is nicely written and organized. The results support the main conclusions. The findings advance the field, and the data will be useful in future research.

1. The work is nicely written and the conclusions about the heterogeneity of ventral precursors are well supported and important contribution to the field. However, the study of dorsal cell is minor. The analysis of dorsal cells seems to include many dorsal venus-expressing cells that are postmitotic neurons, and the number of analyzed cells from the dorsal origin is small.

My advice is to include the data of the study of dorsal cells as supplementary data, not as principal data.

2. On the other hand, I consider that the current supplementary Figure 1 showing the histological expression of the venus reporter should be presented as the main figure.

3. The field is rapidly offering new reports describing single cell analysis of telencephalic progenitors. The authors should revise and update the bibliography and discussion accordingly, including: "Single-cell transcriptomics of the early developing mouse cerebral cortex disentangle the spatial and temporal components of neuronal fate acquisition. Moreau et al., Development (2021) 148 (14): dev197962"; "Molecular logic of cellular diversification in the mouse cerebral cortex. Di Bella et la., Nature. 2021 Jul;595(7868):554-559".

Reviewer #2:

In this study, Lee et al. investigate the molecular diversity of cortex and ganglionic eminences (GE) of the mouse embryo. The authors used single-cell transcriptomics technology to acquire gene expression profiles of telencephalic regions, which they separated by microdissection of the lateral, caudal and medial ganglionic eminences along with the cortex in E12.5 and E14.5 mouse embryos. Using the Nes-dVenus line combined with Fluorescence-activated sorting they could enrich their dataset in ventricular zone cells, mainly neuronal progenitors. With this dataset, they could identify common differentiation lineages between the different GEs. Using the RNAscope technology, the authors validated unreported genes expressed in a specific ganglionic eminence and compartment within the GEs (VZ, SVZ, or MZ). In addition, the manuscript shows a bigger temporal mark on VZ cells compared to post-mitotic neurons between E12.5 and E14.5.

This manuscript presents a complete dataset of single-cell sequencing of ganglionic eminences during development. The effort put in the microdissection of the different GEs, central for the understanding of spatial implication in molecular identity and diversity, along with the validation of newly discovered genes with the RNAscope technique is very appreciated. Nevertheless, the manuscript shows significant weaknesses in the analysis of the transcriptomics data and quality controls. The overall tone is very descriptive such that this manuscript is rather intended for a specialized readership. I have the following comments:

1. In the methods, the authors describe the quality control applied to exclude bad quality cells from the data set (Supplementary Figure 2). At line 384, the authors say: "we first removed cells that had unique molecular identifies (UMI) counts over 4500 or less than 200." From what is shown in supplementary figure 2 we observe that this filtering is done on the number of expressed genes and not on the UMI counts. In addition, in the violin plot of a number of genes per cell, the distribution looks binomial with a population of cells expressing around 500 genes (highlighted in orange) and another population expressing around 3000 genes per cell (highlighted in blue below). The population with a low number of genes expressed should be excluded for further analysis because it is likely that it represents 10x GEMs containing ambient RNA or dying cells instead of GEMS containing a whole cell. This is supported by the post-filtering graph at the bottom of the figure (% of Mitochondrion vs Counts Depth) where, strikingly for the cortex, we observe a population of cells with low % of mitochondrial RNA and high Count depth and a band of cells formed by low Count Depth cells with a variety of mitochondrial RNA (highlighted in red). I strongly recommend the authors filter out the low number of genes population (in orange) by setting a threshold of around 1500 genes per cell which will probably clean the populations with low count depth and thus avoid including bad quality GEMs for further analysis.

2. At the lines 90-92 of the manuscript, the authors write: "Conversely, cortical neurogenesis does not begin until ~E14 (Noctor et al., 2004; Sessa et al., 2008; Tyler et al., 2015), so the majority of E12.5 cortical cells are mainly VZ neural progenitors, specifically RGCs." Indeed, at E12.5 the ventricular zone is the predominant compartment of the developing pallium and most of the cells present at this stage are radial glial cells, nevertheless, asymmetric division of radial glia to produce neurons has been reported as soon as E11.5 in the mouse (Kwan et al. Development, 2012, doi: 10.1242/dev.069963), explaining the small but present proportion of neurons found in the dataset.

3. In line 258 the authors write: "To compare the E12.5 and E14.5 cells, we integrated these datasets together". It is unclear whether the two datasets were just merged in a common Seurat object or if they were integrated with SCTransform normalization and integrated with the Seurat v3 pipeline. I would suggest that this sort of integration not be applied when combining datasets generated in such similar conditions because it can remove the differences between datasets, in this case, age of collection.

4. In Figure 7, the authors nicely show a big overlap and few differentially expressed genes in post-mitotic cells between E12.5 and E14.5. It would be very interesting to know if this overlap is shared for different areas of the telencephalon such as the pallium or if it is specific to the subpallium.

5. In order to isolate basal progenitor cells, the authors selected cells expressing both neuronal markers such as Dcx and cycling marker as Mki67. Since in the 10x experiments it is frequent to have doublets and their exclusion is usually very hard in standard quality control based on genes and UMI counts, I would recommend running a doublet prediction analysis (as DoubletFinder McGinnis et al., 2019 doi:10.1016/j.cels.2019.03.003 ), in order to be sure that the population isolated are indeed basal progenitors and not doublets composed of progenitor and neuron.

6. The sequencing of spatially resolved data is extremely interesting and opens the possibility for addressing the contribution of space to the transcriptome. Here it would be extremely interesting to examine whether the different ganglionic eminences have sharp distinct molecular identities or if there is a gradient of identity between the different eminences.

7. From line 187 on, the supplementary figures references are wrongly numbered.

Reviewer #3:

This study investigates transcriptional diversity of cortical interneuron progenitors in embryonic mice. A major strength of this study is the use of a Nestin GFP line which enables the authors to enrich for progenitors, more so than has been done in previous studies. Using this line the authors uncover previously uncharacterized transcriptional diversity discriminating embryonic domains which produce interneurons at an early stage of development (E12.5). Importantly, the authors make use of smFISH to validate many of these changes. The study provides new lists of transcripts which may highlight diversity of progenitors across domains. Finally the authors perform some analysis at E14.5 to evaluate temporal differences.

While the study has some important novelty and generates evidence of transcriptional diversity, the potential impact of this study is weakened by technical concerns as well as lack of data supporting relevance of observed sub-types. Lineage analysis of at least one potential progenitor subtype would further support the notion that transcriptional heterogeneous progenitors are important (give rise to different fates) as opposed to transcriptional noise.

1. A major conclusion of this paper is that progenitors exhibit transcriptional heterogeneity. When focusing specifically on VZ cells with high Nestin expression (figure 4), how many cells are the authors examining-ie how many cells is this conclusion based upon? Likewise, it would be helpful to better understand how many samples were sequenced to conclude heterogeneity as well as how replicates compare. From the methods it appears that E12.5 is based on 2 Nestin GFP mice. This raises the question as to what extent is this transcriptional diversity reflecting noise of different samples (which could be slightly different stages?) or even technical variation of sequencing.

2. Previous studies have used scSEQ of GE at E13.5 and E14.5 (Fishell lab) and E12.5-E14.5 (Marin lab). The discriminating point here is that the current study uses FACS and a Nestin reporter to isolate and sequence specifically VZ cells. The previous studies also examined VZ cells within their sequenced population, with the Marin study highlighting heterogeneous progenitors evident at E12.5 as well as across MGE and CGE. In the current study the authors conclude their gene expression profiles provide new insight into transcriptional diversity of interneurons. However mainly this study is a list of differential genes (albeit which extends that previously identified). To make this study more impactful it would be helpful if the authors could provide some data such as lineage analysis to support the conclusion that observed diversity impacts fate.

3. Further classification of potential subtypes in a model of some kind would also be helpful-ie are there subtypes which are primarily early born and others that are late born, etc?

4. The authors use Nestin GFP to sort out VZ cells in this study. In Figure 1 they show that Nestin- GFP cells also express markers of newborn neurons (Dcx positive), neurons (Tbr1), and IPS/neurons (Neurod6), particularly in the cortex. The authors should clarify if this is reflecting some perdurance of the GFP into post-mitotic cells? As figure 1 includes WT cells, it is unclear in subsequent figures (such as Figure 3) if they are only focusing on GFP sorted cells or if they are segregating data solely by looking at Nestin transcript. This may be a simple text fix but these missing details make the paper confusing. Due to potential perdurance of GFP protein and even transcript these are not necessarily the same.

5. Analysis of E14.5 is limited-especially as the authors again just sample 1 nestin GFP brain at this stage. The authors conclude that there is more diverse neurogenic and postmitotic expression at E14.5. Additional analysis of cell populations as well as validation would be important to tease out these differences and support this conclusion.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Transcriptional heterogeneity of ventricular zone cells throughout the embryonic mouse forebrain" for further consideration by eLife. Your revised article has been evaluated by Marianne Bronner (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers find your paper valuable and suggest several revisions that should improve the presentation of your study. Although Reviewer #1 appears satisfied with the study in the appended review, in the Reviewer Consultations offline, this reviewer agreed with the other two that a deeper analysis of the expression (in situ and immunostaining) at different developmental times (at least the 2 stages you sequenced) would verify whether a specific marker is stable or not in CGE MGE and LGE. Fabp7 characterization in particular would be welcome; if the results show selectivity, you could minimally address the request of Reviewer 4 to highlight a marker.

This reviewer would also like to revisit the previous request to move data concerning the dorsal progenitors to supplementary data so as to further focus on the GE, to emphasize the ganglionic eminences.

Reviewer 2 asks for highlighting the impact of the study with respect to the ganglionic eminences, to better showcase the special focus of your work. This can be done by modifying the summary to better represent content of the paper.

Also recommended is to address in the Discussion the discordance between spatial (in situ) patterns vs sc seq for Id4 and Mest.

Finally, and readily done, is to place in situs next to the relevant UMAPs in the figures; this would aid the reader's navigation through your very detailed and rich data.

Reviewer 4 is new and asks for proof of some genes suggested to be region-specific, such as Igfbp5, and also linking progenitor heterogeneity to proliferation or fate differences or even protein levels, toward using these differences to isolate subsets by FACS. Proof that expression differences link to functional differences, by, for example, targeting candidate genes with a Cre construct, or doing localization/birthdating. Targeting genes experimentally would involve much more extensive work at this point, and Reviewer 1 especially agrees. But all three reviewers believe that because your paper is very descriptive, if you could add some functional evidence, it would increase the paper's impact. At the very least, you could try to do birthdating/cell cycle analyses, and should they work, this would help the significance of the paper. Minimally, the deeper analysis of Fabp7 expression is warranted, and should address the "ask" of Reviewer 4 to provide a marker for further cell isolation.

Reviewer #1:

The authors have resolved the main concerns of the manuscript. I consider that the addition of the new controls improves the quality of the manuscript. The figures showing comparisons with previous studies explain the added value of this study.

Reviewer #3:

The authors have been generally attentive to concerns raised. They have adjusted their analysis of scSEQ datasets, included new validation experiments for E14.5, and made some additional minor changes. They have revised the writing of the manuscript to explain the novelty of their findings relative to other papers (one of my original concerns) as well as to flesh out more details which increases readability. While the paper is still largely descriptive, the authors have generated some valuable new insights for the field. I do have a few remaining minor suggestions.

1. The impact of this study is mainly their analysis of the ganglionic eminences where interneurons are born. In this regard the authors might consider adjusting the summary to reflect that emphasis even more. This may attract more readers to their work and increase impact.

2. The finding that Id4 and Mest spatial patterns by in situ are different than that predicted from the scseq is interesting (but also somewhat concerning for the field). It would be nice if the authors comment on this discordance in the discussion as an important point of consideration for sc seq experiments.

3. Figure 7-supplement 1F labels Nestin expressing cells. The use of red for labeling nestin is confusing here as red also labels CGE.

4. The representation of the in situs adjacent to UMAPS in Figure 8 is really helpful. For this figure I think they should also add in annotations with the UMAPs labeled for each respective region/stage. There are labels for panel A but not the plots below. In addition, I wish the authors would use this approach in prior in situ figures-ie include the relevant UMAPs beside the in situs (for perhaps a subset), as opposed to putting in supplement. It facilitates analysis of their data.

5. Line 366 in discussion (types may be singular)

Reviewer #4:

In this manuscript the authors profile nestin-expressing cells from the 3 ganglionic eminences in E12 and E14 murine embryos by scRNA-seq. This yields several region-specific genes, some of which could serve as a new regional marker, such as Igfbp5 for CGE, but they do not prove this. Most importantly, they do not analyze the region-specific differences across at least the 2 stages they sequenced to verify if these markers are stable at least for these 2 days in development.

I fully agree with the authors that it is important to explore progenitor subtypes at higher resolution, i.e. many cells, to explore heterogeneity. This is also highly relevant for the diverse output from these regions, including the generation of adult neural stem cells. However, the manuscript falls short of linking either progenitor heterogeneity or regional heterogeneity to a specific function – e.g. proliferation differences, fate differences or protein levels to allow subset isolation by FACS. Please provide at least 1 example to showcase that the expression differences link to functional differences in output (in utero-electroporation of a Cre construct targeted to a specific subset) or highlighting by RNAscope and EdU cell cycle monitoring that the marker population has indeed specific cell cycle properties (slow division, for example).

One specific example that raises doubts about the usefulness of the markers proposed is Fabp7, as indeed staining seems to label all cells in the ventricular zone, even though levels are always higher at boundary regions. This would mean that the "absent" expression of Fabp7 may simply be due to the depth of sequencing. Therefore, I suggest the authors perform immunostainings to verify or falsify the usefulness of this "marker".

This leads to my last suggestion namely to focus the analysis to some extent on genes encoding cell surface proteins to allow sorting subsets of progenitors.
