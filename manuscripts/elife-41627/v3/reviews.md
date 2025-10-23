# Peer review - Round 1

Editors:
- Chris P Ponting, University of Edinburgh United Kingdom

Reviewers:
- Chris P Ponting, University of Edinburgh United Kingdom

## Review text

DOI: [10.7554/eLife.41627.030](https://doi.org/10.7554/eLife.41627.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Single cell expression analysis uncouples transdifferentiation and reprogramming" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Chris P Ponting as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michel Nussenzweig as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Francesconi et al. have undertaken a time series experiment to compare pre-B cell transdifferentiation into macrophages, with reprogramming into iPSCs. Using single cell RNA sequencing they identify the sequential loss of B cell specific factors and the engagement of myeloid gene expression patterns during transdifferentiation. Concordantly they show that reprogramming leads to a loss of B cell identity and a gain of ESC-like transcriptional state 8 days after reprogramming. Further, they correlate these changes with a number of different factors and ultimately show that expression of Myc, and its downstream target genes, in the starting population are predictive of transdifferentiation and reprogramming efficiency. This difference is predicted by Myc expression but Myc was not demonstrated unequivocally to be causal. This model is consistent with functional experiments, which reveal that the initial starting population was heterogeneous, and consisted of 2 distinct B cell developmental stages, each with reciprocal efficiencies for transdifferentiation and reprogramming.

Essential revisions:

1) Some decisions made in how the single cell data are processed to be poorly motivated and somewhat arbitrary. Additionally, it is not clear how the approach and experimental design taken by the authors address their specific problem, and why a simpler approach could not be taken. In particular, and rather surprisingly, the authors do not check for heterogeneity in the starting population, for instance, is there any indication of structure in the pre-stimulated cells? This could be interrogated very simplistically, particularly as the authors make pains to point out bi- and tri-modality in hard to read violin plots for latter stages post-stimulation. Subsection “Large and small pre-B cells differ reciprocally in their propensity to transdifferentiate or reprogram”, last paragraph, could the small and large pre-B cells be in fundamentally different states?

In the Discussion it is said that "a cell's propensity for transdifferentiation or reprogramming can be disassociated, indicating that these two types of plasticity are fundamentally different". This is overstating the evidence because this statement discusses "a cell" whereas the propensity differences are evident for two different cell types (albeit one differentiation step apart). The authors appear not to show, using highly purified populations of these 2 cell types, that "these two types of plasticity are fundamentally different."

OSKM includes MYC. Why does input MYC matter? Is it merely a marker for the two different cell types that differ in some other way? This needs to be clarified.

The conclusion that MYC level inhibits lineage conversion is based on a single model, which only uses one transcription factor. A general statement should not be made based only on a single model.

Analysis of open chromatin across the time points could be helpful. Does CEBPa open new chromatin or only bind to existing open chromatin sites?

2) The reviewers agree that it is plausible that MYC expression level affects reprogramming. The evidence for this is, however, correlative: the mechanism by which MYC elicits its effects is not determined. To be definitive, the authors could demonstrate that low levels of endogenous Myc (via CRISPRi and/or knockdown) are associated with inefficient reprogramming in one (or preferably more) cell types. It may also be true that cycling cells are easier to reprogram. This may not represent a novel discovery (Tsubouchi et al., Cell 2013). Proliferating cells dilute out existing proteins when transcription rates drop, this may be needed for loss of the starting fate. More generally, at several points the authors state that "X predicts Y". It would be more accurate to state that "X is correlated with Y" since prediction implies a causality that is not proved.

3) The Results section is hard-going at times, particularly when the reader is expected to rederive the conclusions of the text simultaneously using many different figures and panels. Examples are:a) "We found that a signature enriched in Myc target genes (component 5, Figure 1—figure supplement 2, Supplementary file 4) best predicts speed of cell conversion and negatively correlates with the progression of cells at intermediate time points of transdifferentiation (Figure 2B, Figure 2—figure supplement 1)." Here, the reader is requested to compare 3 figures (and 1 table) whilst figuring out what is meant by "speed of cell conversion". We request that you take your time to explain these observations so that the reader better appreciates this important sentence. re: Figure 2D. "low expression of Myc targets is more strongly associated with a rapid gain of the macrophage state than with a rapid loss of the B cell state". Again there is a need to lead the reader through this plot.

4) The authors will need to introduce the experimental system in more detail, in particular the dox-inducible cassette encoding the 4 Yanamaka factors. Additionally, they should provide some justification for the different time points and resolution between the transdifferentiation and reprogramming experiments.

5) When describing the results of the single cell experiments, there needs to be more specific examples of genes and their relevance. Simply describing a 'B cell program' is uninformative. To that end, the presentation of the top 50% of expressed cells feels a little like cherry picking; the authors should present the distribution of expression for all cells, not just the top 50%.

6) Related to the above, the last paragraph of the subsection “Single cell analysis of highly efficient transdifferentiation and reprogramming from the same cell population”, should be split into 2 separate sections, and expanded to include more details as above.

7) The subsection “Rapid transdifferentiation into macrophages is associated with low expression of Myc targets” could potentially be explained by differences in resolution of the time series experiments. The authors need to demonstrate quantitatively that there are differences in the rates of transdifferentiation versus reprogramming, and what are the potential explanations. This is not aided by the difficulty in reading many of the plots, i.e. violin plots, then stating something is evident when it has not been demonstrated. The presentation of these data needs to be clearer. It is better to provide several clear examples that illustrate the authors' point, than to try to squeeze too many plots into a single figure panel.

8) Subsection “The rapid transdifferentiation of cells with low Myc activity is more direct” – it is not clear that higher Myc target expression is associated with a more persistent induction of a GMP-like state, as there is no indication of a relative time difference between Myc-high and Myc-low cells.

9) Unsurprisingly the monocyte and macrophage components are highly correlated – given this Figure 2F is arguably redundant.

10) Subsection “Efficient reprogramming is associated with high expression of Myc targets” – please confirm that the ICM component is not driven by Myc target genes; include a reference to Figure 2—figure supplement 3 for this.

11) Would any population of cycling unsynchronized cells also show considerable variation in Myc target gene expression? A proper comparison to control populations that are synchronized or unsynchronized, e.g. ESCs, would give some indication of where these pre-B cells sit in this respect.

12) Subsection “Variation in Myc activity reflects pre-existing variation in the starting cell population”, last sentence. This statement is too strong. Specifically, at no point have the authors presented evidence about speeds or rates of transdifferentiation and/or reprogramming.

13) Figure 3D – can you justify the thresholds used for the FSC and SSC? In particular, in later figure panels it seems like there is a strong overlap between the "large" cells and "small" cells.

14) a) From a more technical perspective, what is the motivation of using an inverse hyperbolic sine transformation, when a scaling factor would achieve the same result? If it does not, then demonstrate why.

b) Additionally, correction with MNN removes batch effects that are orthogonal to the biological signal. Using only first 2 PCs will likely miss genuine MNNs, and thus will not appropriately correct batch effects embedded in deeper reduced dimensions.

c) Subsection “Computation of similarity index of our single cell RNA-seq data with reference cell types”. Was this regressed out of the similarity index, or were the Myc target genes just removed before re-computing the scores? This needs clarification. More generally, a gene is expressed, not a signature, i.e. talking about the expression of a Myc signature/component does not make biological sense – it is an artificial construction. Say score, or loading, instead of expression.

d) Subsection “Characterization of the components: comparison to the mouse cell atlas” – what correlation coefficient was used here? Pearson's, Spearman's, Kendall's, etc.?

e) Subsection “Diffusion map and diffusion pseudotime” – why use a sigma of 0.12, this seems very specific?

f) Subsection “Differential expression analysis, clustering and heatmaps” – when describing a differential expression analysis it is standard practise to indicate the false discovery rate. Also, why use a fold change of 1.3? Again, this is a strangely arbitrary value that needs some justification.

15) Other issues:

a) Figure 1—figure supplement 3 caption is not complete – sub panel indicators are missing.

b) Abstract. Make it clearer that the two cell types are categorically different ("only a single differentiation step apart", Discussion, also shown in Figure 4).

c) Figure 1I. Clarify why the 6h data were not included.

d) Figure 1—figure supplement 2A. Justify the selections of components and cell types. Explain "Scheme of ICA decomposition the"

e) Figure 1—figure supplement 4 (subsection “Rapid transdifferentiation into macrophages is associated with low expression of Myc targets”) "This is also evident from the bi- or trimodal distribution of key marker genes at intermediate time-points of reprogramming and transdifferentiation". The bi/trimodality is not immediately evident from these violin plots so I suggest that you show the raw data for an exemplar marker gene and cell type (e.g. Nanog). In the text this is described as "asynchronous behaviour" yet formally this is an interpretation and at this stage in the manuscript no data supporting this has been provided.

f) Figure 2B. Explain that the start/end point data are not shown, and say why in the legend.

g) Explain at greater length the "time window of highest responsiveness".

h) Introduction, "homogeneous".

i) Subsection “Efficient reprogramming is associated with high expression of Myc targets”, change "can" to "could".

j) Explain (re: 0.01% to 25%) that the conversion processes remain unclear.
