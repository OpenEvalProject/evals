# Peer review - Round 1

Editors:
- Lilianna Solnica-Krezel, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60005.sa1](https://doi.org/10.7554/eLife.60005.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript reports comprehensive analysis of single cell sequencing of FACS sorted neural crest cells from the posterior head and trunk of the zebrafish embryo at two developmental time points, generating a ~4,000 cell scRNAseq dataset. By performing standard analysis using Seurat to cluster and annotate the data, the authors identified major cell types within the neural crest at these stages, including pigment cells, craniofacial and enteric neuronal populations, and unique combinatorial hox gene expression among particular neural crest cell types. The results presented here could help other investigators identify populations of neural crest cells as well as how the gene regulatory network functions at later time points in development.

Decision letter after peer review:

Thank you for submitting your article "An atlas of neural crest lineages along the posterior developing zebrafish at single-cell resolution" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard White as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Cecilia Lanny Winata (Reviewer #2); Kristin Artinger (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The manuscript reports comprehensive analysis of single cell sequencing of FACS sorted neural crest cells from the posterior head and trunk of the zebrafish embryo at two developmental time points, generating a ~4,000 cell scRNAseq dataset. By performing standard analysis using Seurat to cluster and annotate the data, the authors identified major cell types within the neural crest at these stages, including pigment cells, craniofacial and enteric neuronal populations, and unique combinatorial hox gene expression among particular neural crest cell types. The results presented here could help other investigators identify populations of neural crest cells as well as how the gene regulatory network functions at later time points in development.

Essential revisions:

There was consensus among the reviewers, that while this work presents a useful data set, the current manuscript falls short on conclusions about neural crest drawn from the data. The manuscript discusses at length about gene expression in various NCC populations without much functional analysis or offering new insights. To become suitable for publication in eLife the manuscript would need to be revised to shorten methodological aspects, present new findings and highlight their significance. Based on the data presented, enteric neurons and hox code present such opportunities. For enteric neurons, the current manuscript has missed the opportunity to use the scRNA-seq data in an unbiased way, the authors searched for known signatures. It will be important to demonstrate that this data set can reveal previously undescribed genes and pathways. It is understood that in the current situation of ongoing pandemic and reduced laboratory efforts, functional analyses are not feasible, although validation of expression of some novel genes, would significantly strengthen the manuscript.

1) The Introduction would be improved by a discussion about the known gene regulatory network at these stages and cell types. It will help put the study in context of what is known in the field. This would include expression analysis by RNA in situ and bulk RNA-seq analysis on this population.

2) The use of PTU does not seem to be necessary for the purpose of the experiment as the GFP signal should still be visible even with pigmentation. The reviewers therefore wondered why the authors incorporated this procedure. Although PTU is technically not supposed to affect the early steps of melanophore differentiation, possible implications of this need to be at least clarified as there is evidence that PTU can affect the organism at molecular and physiological levels.

3) There should be a discussion of how the cell type classification markers where chosen for the clustering. For those not in the field, it is not clear. Please add.

4) The Results section should be shortened and condensed significantly. Over half of the Results section (some 12 to 14 pages) is merely describing the authors' process of annotating the data. This could easily be summarized in a full-page figure with an annotated tSNE plot and a dot plot indicating the markers that were used to define the annotations. It would, in fact, be much clearer for readers.

5) Additionally, many other sections of the Results are so verbose that they obscure the authors' meaning. Tightening the prose would significantly improve the manuscript. Paragraph three of subsection “Pigment cell chromatophore lineages resolved” is such an example. Could the authors not just say "Previous work identified melanophores in distinct proliferative and differentiating states at 5 dpf (Saunders et al., 2019). We find these states arise between 50 and 68 hpf, as all melanophores were in the G1 phase at 48-50 hpf, but formed two distinct clusters at 68-70 hpf differentiated by their cell cycle state."

6) The HCR expression analyses are a nice addition to show the expression of some of the genes that are expressed in specific populations. However, the genes shown are already known and thus higher resolution images (For craniofacial figure, pigment I and J are hard to see, enteric figure is good but also would benefit from sectional analysis) to show neural crest cells at the cellular level and potential overall of expression would move the field and be more similar to the single cell sequencing. It would also be helpful for data interpretation. That being said, it would also be interesting to show some of the genes in the clusters that are novel or that have not been shown to be expressed in that cell type as well.

7) "Hierarchical clustering of cells with General Mesenchyme and Chondrogenic identities using a cluster tree": This is not technically correct, assuming the authors used BuildClusterTree (which it seems so from the Materials and methods). This function does not operate on the level of cells, but hierarchically clusters the mean expression signature of the already-calculated clusters.

8) It's not clear why the authors present the data twice, first as each individual time point and then as a combined analysis, when the same clusters are recovered in the combined analysis. It seems as if it would be easier and more informative to just present the combined data.

9) The authors provide an estimated number of cells reported by 10x Cell Ranger pipeline which corresponds to 2300 and 2580 for 48-50hpf and 68-70hpf, respectively. We understood that these numbers correspond to the estimated number of cells that 10x pipeline was able to identify which in the following steps serves as an input for Seurat analysis in R. The total number of usable cells after all QC steps were 1608 (58-60hpf) and 2410 (68-70hpf). However, there was no information on how many cells were loaded on to the 10x chip. This information would help others, especially in the zebrafish community, to better plan single-cell experiments and would provide additional information about cell suspension quality.

10) The reviewers were surprised that there is a large population of neural crest classified cells at these stages. They wondered if those are progenitor cells and do they remain in adults? In addition, it seems like most of the neuronal population in enteric, where are the dorsal root ganglia and sympathetic neuronal populations?

11) In the two stages of neural crest development, it would be interesting to include how the gene expression changes across developmental time. Could you present a combined UMAP with stages colored to see where stages fall and sets of genes that change expression through developmental time in subclusters? Highlighting genes that change over developmental time in each cluster would be very informative.

12) Discussion penultimate paragraph: This is potentially an interesting conclusion that the authors could spend more time on in the paper. Is it worth generating some version of a figure that combines a review of what is known about these signatures from other systems (and which other systems) with what the authors observe in zebrafish? One could envision some form of dot plot with an organismal color code, but obviously the authors may have more creative ideas.

13) (783/784) Mitochondrial genes were regressed out from the data set during the Cell Ranger alignment. Mitochondrial genes, together with ribosomal genes, are useful metrics for the assessment of cell quality. High expression levels of mitochondrial genes may indicate poor sample quality, apoptotic cells, or multiplets. Or if it is limited to a few clusters, it may reveal the nature of some cells (e.g. increased metabolic activity). However, the authors decided to remove mitochondrial genes from the alignment. Why?

14) The paper makes no mention of how the data and code will be made available. It would be standard practice to deposit the FASTQ files as well as the counts table output by CellRanger in GEO. Moreover, it's fairly standard practice (and generally appreciated) to make the processed Seurat objects available (either through lab website, Data Dryad, or some other hosting platform). Additionally, it's generally accepted practice to publish the code that was used to analyze the data and generate the figures.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "An atlas of neural crest lineages along the posterior developing zebrafish at single-cell resolution" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard White as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Cecilia Lanny Winata (Reviewer #2); Kristin Artinger (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript reports comprehensive analysis of single cell sequencing of FACS sorted neural crest cells from the posterior head and trunk of the zebrafish embryo at two developmental time points, generating a ~4,000 cell scRNAseq dataset. By performing standard analysis using Seurat to cluster and annotate the data, the authors identified major cell types within the neural crest at these stages, including pigment cells, craniofacial and enteric neuronal populations, and unique combinatorial hox gene expression among particular neural crest cell types. The results presented here could help other investigators identify populations of neural crest cells as well as how the gene regulatory network functions at later time points in development.

Revisions:

All reviewers thought that the authors have made significant improvement to the manuscript by removing many of the technical descriptions from their results. However they also thought that more can be done to make the Results section more readable. Many unnecessary details and repetitions remain, which obscures the communication of essential findings. Moreover, the manuscript is perceived as written for a neural crest audience and thus less accessible to a more general (eLife) audience making the authors motivation and essential findings obscured. The specific comments and suggestions of the reviewers that can guide additional revisions are appended below.

Reviewer #1:

My only remaining comment that should not block publication, but perhaps would inspire some additional revisions from the authors, is that overall, I still find that the prose is disappointingly focused on technical aspects of a pretty standard single-cell analysis at the expense of describing discoveries from those analyses. Many sections of the paper end with the main conclusion that the section "demonstrates the power of the sox10 atlas to.…" but I don't know why this is repeatedly considered a result, given that standard and well demonstrated analysis methods were used on data generated using now standard approaches. The new and expanded Discussion section illustrates that the authors have found some interesting results, but I feel that they dilute them significantly by focusing so much on telling us about the power of now-standard single-cell genomics approaches and about the process of annotating the data, when they could instead place the focus on their more interesting findings. For instance, I find this is especially true in the presentation of the mesenchyme - which seems mostly focused on describing existing mesenchyme markers and how they were used to identify the mesenchyme and then the number of clusters found therein, but without significant description of what those clusters are or what defines them.

Reviewer #2:

Despite the new additions, the manuscript remains highly descriptive and a major issue in terms of writing style remains.

1) The authors have made significant improvement by removing many of the technical descriptions from their results. However this did little to make the Results section more readable. Many unnecessary details and repetitions remain, which obscures the communication of essential findings. The language used is often colloquial, with some grammatical errors which makes reading extremely challenging, especially for a non-expert in NCC or single cell biology. Having the manuscript read by a professional scientific editing service might be of help. To cite some examples:

– "We have utilized the Tg(-4.9sox10:EGFP) (hereafter referred to as 117 sox10:GFP) transgenic fish line to identify". Authors were requested to use the term "zebrafish" instead of "fish" since other fishes are used for these types of studies and it is confusing. Please correct this.

– What does "remarkably captured" mean?

– "Taken together, these results show that the scRNA-seq datasets effectively identify discrete subpopulations, and coupled with our HCR analysis, effectively shows we are able to validate these cell populations in vivo". Please clarify which subpopulations are referred to here.

– It is unclear what the authors meant by "early neuronal differentiation". Please specify the exact or range of developmental stage(s) for clarity.

– "Further investigation into these pathways led to the identification of…" – would it be sufficient to simply state for e.g. that "oprl1 and oprd1b, which are members of this pathway, were expressed in subcluster 3"?

– ". patterns of Homeobox transcription factors, known as hox genes…" – how can transcription factors be known as genes? Please rephrase this.

2) The Discussion section is also extremely lengthy, containing many repetitions of the results which could be significantly condensed. There are also a lot of anecdotal information written on opioids – which seems irrelevant and unnecessary.

3) In describing the mesenchymal clusters, the authors used the term "subtypes". It seems more appropriate to call them simply as "clusters" as there were no systematic analyses done (e.g. expression of specific cell type markers) to define whether each of these barx1+ and dlx2a+ clusters represent distinct cell subtypes. Moreover, the number of clusters obtained depends on the threshold set in the scRNA-seq data analysis, which is therefore arbitrary in nature.

Along the same lines, the resolution parameter from Seurat FindClusters function determines the number of obtained clusters. Naturally, the selection of this parameter is arbitrary and needs to be individually tailored for each sample. Looking at the data at different resolutions may help to improve the identification of novel cell types. Is there any particular reason why the authors decided to apply the resolution of 1.2? A clarification on how this threshold was chosen would be helpful.

4) "… pbx3b expression may promote the assumption of an IPAN signature characterized by the presence of calb2a, ache, and slc18a3a and the loss of inhibitor markers nos1 and vipb." – it is unclear how the authors' observations led to this hypothesis as earlier on they stated that "…pbx3b expression was found in combination with calb2a, vipb, and nos1…". Please clarify.

5) "Overall, these results suggest that sub-cluster 0 cells may represent a pool of immature sympatho-enteric neurons, and that sub-clusters 1 and 4 both represent better resolved, yet still immature, pools of enteric and sympathetic neurons." – it is unclear how the authors arrived at this notion, especially since cluster 0, 1, and 4 was not even mentioned at all previously.

6) It would be helpful if the authors also annotate the clusters in Figure 6—figure supplement 2 panel A and Figure 7—figure supplement 1 panel J.

7) "We performed cell filtering and clustering (.) cells which contained low (<200) or high (>2500) genes were removed from analysis".

– As indicated in Figure 1—figure supplement 1 panel C, around 4905 and 4669 cells were loaded for encapsulation into 10x cartridge, resulting in 2300 and 2580 identified cells. After a filtering step that was done on the basis of gene content only, 1608 and 2410 cells were obtained. The expected multiplet rate at such cell suspension concentration should be low (around 2% according to 10x protocol), therefore the great loss of cell numbers is rather surprising. Have the authors checked why the cell loss at the applied threshold level for the 48-50 hpf sample is much higher than expected. Also, did they check the distribution of expressed genes before setting up the thresholds for gene content per cell?

– Additionally, including mitochondrial gene content into the filtering step may help to confidently identify low quality cells.

8) Figure 1—figure supplement 1 panel C – inconsistent number format (comma, dot, space), e.g. mean read per cell (74,017 vs 62109 etc.)

9) “…Major cell type categories were based on the presence of signature marker genes…”. Is the word "presence" an appropriate term in this context? Presence is rather a binary value and takes two options: 1- present, 0 – not present. It seems more accurate to use the term "expression" of these signatures/marker genes.
