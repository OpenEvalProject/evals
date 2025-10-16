# Peer review - Round 1

Editors:
- Marianne E Bronner, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64819.sa1](https://doi.org/10.7554/eLife.64819.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This exciting paper characterizes the cellular dynamics of a population of stem cells, recently identified, called neuro-mesodermal progenitors in the chick embryo. By conducting prospective lineage trace and transcriptomic analysis, they identify dynamic cell behaviors that explain previous 'snapshot' studies showing that neuro-mesodermal progenitors contribute over long axial distances. This manuscript makes an important contribution to the understanding of how neuro-mesodermal progenitors contribute to vertebrate axial elongation and provides novel insights into axial morphogenesis.

Decision letter after peer review:

Thank you for submitting your article "Dynamics of primitive streak regression controls the fate of neuro-mesodermal progenitor cells in the chicken embryo" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Valerie Wilson (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions

1. Many of the concerns can be addressed by text changes and minor changes to the existing data presentation as detailed in the full reviews.

2. The main problems are with the bioinformatic analysis, where both reviewers highlight issues where the analysis is too superficial and needs further work.

3. Additional imaging quantification is required to support their findings.

Reviewer #1:

The paper entitled "Dynamics of primitive streak regression controls the fate of neuro-mesodermal progenitor cells in the chicken embryo" from Guillot and colleagues aims to characterize in the context of developing chick embryos the cellular dynamics of a population of stem cells, recently identified, called Neuro-Mesodermal Progenitors (NMPs). The authors provide several lines of evidence supporting their claims that overall look interesting, however, additional imaging quantification and more comprehensive analysis of their transcriptomic datasets are required to support their findings.

Specifically, the authors generated an important scRNA-seq dataset of micro-dissect regions of the chick embryos across developmental time points from stage 5 to 35-somites. Despite the dataset represents a crucial part of the paper supporting the authors' findings of this NMP population, the analysis is not deep enough and does not report several controls and markers. In figure 2 the authors should show heatmap of the marker genes used for classification. Louvain markers genes that define each cluster should be showed in a supplementary not as an unreadable table, instead, a dotplot or heatmap would be better. It is unclear whether Louvain clustering has been used to label the data, did the authors find that each Louvain cluster correspond to a defined cell identity? The pseudotime analysis is incomplete and superficial. Diffusion pseudotime strongly depends on the root cell selection. RNA velocity analysis and/or another trajectory analysis are required to better show lineage trajectory. Figure 4 L-K, the pesudotime time is not progressively ordered and it would be advisable to perform an alternative analysis to visualize lineage trajectory. Furthermore, gene expression trends should be identified and further discussed over those trajectories. The supporting information about the classification analysis using the mouse dataset is incomplete.

– In figure 1 the authors show SOX2-T double staining. Panels A-B-C represent the first evidence of SOX2-T co-expression in stage 5 chick embryos. The merged image is not provided together with the single panels A-B and only appear in panel G of the same figure, this is confusing. Panel B has two scale bars. The authors tried to show SOX2-T co-expression by thresholding and masking SOX2-T signals in panel C and Suppl. Figure 1. The authors should clearly explain how this thresholding is obtained. Is this manually set? Is this set based on global or local signal intensity distribution? Otsu thresholding? In order to avoid artifacts due to thresholding, the authors should also display a scatter plot showing nuclear intensity values for SOX2-T. FACS analysis and quantitative assessments of the percentage of cells would further strengthen the authors' claim.

– The authors should validate SOX2-T expression in quail embryos

– The authors should better discuss the mechanical forces that are implicated in epithelium to mesenchyme, and in the posterior gradient of proliferation that counteracts ingression in the anterior PS epiblast. Is this affecting/related to WNT or hyppo pathway?

– Can the authors speculate about the conservation of this phenomena in the human context? What is the evidence that this conserved in human?

– The authors speculate about in-vitro generated NMPs, did they try transplantation of in-vitro generate cells? Can they compare the transcriptomic signature of the human in-vitro generated NMP with the chick counterpart?

– The tables in Suppl. Figure 4 should be a supplementary table.

– In Suppl.Fig5D there is not scale bar to assess classification efficacy and material and methods do not describe how this analysis has been performed.

– The authors should substantially revise scRNA-seq data.

Reviewer #2 :

In this manuscript, the authors aimed firstly to prospectively identify cells with dual neural and mesodermal fate. Previous studies in mouse had determined that such dual-fated cells existed, and had narrowed down their location to subregions of the axial progenitor zone co-expressing Sox2 and T. However, these studies had not shown that individual cells in the Sox2/T positive region were dual-fated. The authors use three approaches: live imaging, and two prospective clonal labelling studies of the Sox2/T positive region to show, for the first time, that indeed this region harbours dual-fated cells. This is an important missing piece of the current volume of work on NMPs. Whilst the rationale for the experiments are clear, it might be better to present this work more in the context of previous studies. It seems a little harsh to dismiss population fate mapping studies as 'failing to identify' NMPs rather than complementing the clonal analysis by identifying regions potentially harbouring NMPs. In addition, there are interesting parallels with the clonal analysis carried out in mouse. For example, not all NM clones contribute to the tail bud; the observation in live imaging studies that NMPs first contribute to the neural tube and later to mesoderm is also similar to the observations from mouse retrospective clonal analysis; this could perhaps be discussed more fully.

Next, the authors carry out single cell RNA-seq analyses of three stages of chick axial elongation, and compare these with existing datasets in mouse, adding data from a later stage of mouse embryos. This aspect of the study has again confirmed and extended previous studies, showing both similarities and differences between chick and mouse NMPs. Trajectory analysis suggests progression of NMPs towards neural and mesodermal lineages in both chick and mouse. This is a valuable resource for the community. However once again it would be good to present this aspect of the work in the context of previous studies showing maturation of NMPs over time and an increased mesenchymal transcriptomic signature of NMPs at late compared to early timepoints.

Finally, the authors carry out dynamic cell tracking and show that NMPs ingress later, and proliferate faster than more posteriorly-placed cells in the primitive streak, leading to exhaustion of the posterior populations and long-term retention of the NMP population. This part of the study is well-executed and contains important new information that advances our understanding of both NMPs and axial progenitors as a whole.

Suggestions for strengthening the science

1. The results presented in Figure 1 are a little difficult to interpret as there is some background fluorescence in Sox2 and Msgn1 staining. Perhaps the thresholding strategy could be described in the supplementary data to support statements about Sox2 positive time of emergence and the location of Msgn1 positive/Sox2 negative axial levels. It would be good to cite the source of the fate mapping information locating NMP/PMP/LPP/EMP in Figure 1D- is it this study or another? The section at level 5 in Figure 1E is named LPP in 1E but corresponds to a region marked 'EMP' in Fig1D. Together these two factors make it hard for the reader to judge where the posterior limit of Sox2/T positive cells is, relative to Msgn1 and to regions of differential fate. Also, the text (p5) says there are 'low levels [of TBXT] in the node' but the expected high levels in the node/ emerging notochord are visible in Fig1E sections 1-2.

2. In Figure 2, the clustering shows two datasets, (which are presumably batches?) of cells for each stage in chick (st5 1 etc). However, the colour coding does not allow the reader to distinguish these. Do the batches occupy different positions in the UMAP plot? How was batch correction done?

3. The cells annotated as NMPs in chick show elevated expression of Hes5 (6-somite stage) and Dll1 (combined dataset) relative to the cells annotated as PSM or neural (Figure 3, S4,5). Also, some of the NMP signature markers are expressed in a higher percentage of the NMP population in mouse compared to chick. This suggests that the cluster annotated as NMPs in chick also includes the midline primitive streak. The absence of Sox2 from this dataset is not, in my opinion, especially troublesome as it is expressed at low levels. However, it means that the chick single cell transcriptomes cannot be independently verified as NMPs and distinguished from midline streak cells. Perhaps the mouse data can help here. Instead of using the chick as a starting point to define the NMP phenotype, if the authors can work back from cells dissected from the Sox2/T positive regions (ie from Dias et al., eLife 2020 and Gouti et al., Dev Cell 2017), as well as the NMP annotations in the mouse atlas data used here (Pijuan-Sala et al), how well do the chick cells correspond to the mouse ones? If a narrower definition of NMPs is used in chick, does this remove any of the variation seen between mouse and chick?

4. The mouse NMP trajectory analysis (Figure 3M) shows two arrows. What do they represent? if just pseudotime, it looks more like a radiation in all directions from the centre. Interestingly this would suggest NMPs also progress (upwards on the Y axis) as NMPs in pseudotime. Is this effect seen in the chick NMPs?

4. The annotations of chick versus mouse early and late clusters are confusing, In chick, there are two early clusters (coloured the same) annotated nmp-1 and nmp-2, but these do not correspond to the two earlier stages. What do they correspond to? Some discussion of the heterogeneity would be appropriate- or possibly a reanalysis of the NMP annotation in point 3 above may highlight that one of these clusters is less NMP-like. In the mouse, there is one early subcluster and two late ones. These are also annotated nmp-1 and nmp-2. A different nomenclature should be used to highlight that they are not the same as the chick ones. Unlike the chick clusters, these seem to correspond to different stages of development.

Suggestions for improving the manuscript

1. The statements that no previous studies have prospectively identified neuromesodermal-fated cells (abstract, introduction p4, discussion p10) should be modified. Forlani et al., Development 2003 10.1242/dev.00573 and Wood et al. BioRXiv https://doi.org/10.1101/622571 show dual-fated cells in mouse and chick. I think that it would be fairer in the context of previous studies to cite the population or oligoclonal studies of Iimura and Pourquié, (2006) 10.1073/pnas.0610997104, Cambray and Wilson, (2007) 10.1242/dev.02877 and Brown and Storey, (2000) 10.1016/s0960-9822(00)00601-1 as showing potential locations for cells of dual neuromesodermal fate.

2. The words 'bipotent/monopotent' used throughout the manuscript is not appropriate for the studies here, which are demonstrating fate and not potency. I would suggest 'dual fate'.

3. NMPs are presented here as 'stem cells' when the transcriptome analysis shows they mature with time. It would be good to define exactly in what sense the term is being used- it is valid since the manuscript describes an enduring progenitor producing neural and mesodermal tissue but should be used with care.

4. p5. 'We identified 7 clones containing cells expressing the same barcodes' – could this text be modified to clarify, e.g. 'expressing unique (or clone-specific) barcodes'?

5. p7 para 2 'the NMP lineage' should be changed to something not implying lineage, e.g. 'cluster'

6. Figure S7 is entitled 'NMP early and late clusters are not due to different Hox genes expression'- since the authors show differential Hox gene expression, this statement should be moderated. The text describing this observation also suggests that the genes that are differentially expressed early and late in mouse and chick are different. However, many of the genes upregulated in the later chick stage are also upregulated in mouse, eg Wnt5a, Greb1, Fgf8, Figf18, Cyp26a1 (see Wymeersch et al., 10.1242/dev.168161). It would be good to comment on this.

7. Can the authors consider whether 'persistence' of cell tracks is the optimal term? It could suggest persistence of movement rather than just their continued observation over time. Is 'longevity' a possible alternative?
