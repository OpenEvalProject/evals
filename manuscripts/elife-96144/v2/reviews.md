# Peer review - Round 1

Editors:
- Alyssa M Wilson, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96144.sa0](https://doi.org/10.7554/eLife.96144.sa0)

This study presents a useful examination of dense neuroanatomy in human postmortem medial entorhinal cortex, using a large number of small electron microscopy image volumes sampled from multiple cortical layers and individuals. The authors use solid experimental and annotation techniques, demonstrating the suitability of postmortem tissue reconstructions for analysis and presenting careful, detailed measurements of synapse properties and overall tissue composition in this brain region. This work would be of interest for studies of cellular neuroanatomy or brain network organization.


---

# Peer review - Round 1

Editors:
- Alyssa M Wilson, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96144.sa1](https://doi.org/10.7554/eLife.96144.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human Entorhinal Cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Alyssa Wilson as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Albert Cardona as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Casey Schneider-Mizell (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions (for the authors):

In the reviewers' discussions, several claims from this article were identified that require further support or alteration. Of the reviewers' recommendations, the following revisions will be expected in follow-up work:

1) Throughout the manuscript, claims of homogeneity should be contextualized more fully, with discussions about the potential contributions of noise to observations, and about the applicability of findings given the spatial scales investigated and the measurements made. In this expanded discussion, please address the following points in particular:

(1a) For each ultrastructural measurement presented, a quantitative characterization of variability should be reported, on a per-image-volume basis (currently, measures appear to be aggregated per individual, per layer, as in Table S3). Additionally, a figure formatted similarly to Figure 3C but with variability measures (e.g. error bars with interquartile range per data point) should be presented for each measurement, to provide a clearer sense of inter-image-volume variability. The degree of this variability should be discussed in the text.

(1b) Similarly, given the substantial clinical differences between brain donors, a characterization of inter-individual variability should be presented, where distributions for each measurement are aggregated by donor, per layer, and compared (again using plots similar to Figure 3C but with variability measures). Here, statistical tests of similarity between donors would also be of interest for assessing the impacts of combining data for multiple donors.

(1c) In the text, the approximate size of each reconstructed volume (~10 µm per side) should be explicitly reported and discussed as it relates to the spatial scales for which structural variability can be interrogated. It would further be helpful to provide context about how these volumes may relate to structure at other spatial scales relevant for human medial entorhinal cortex.

2) Although data acquisition and annotation have been carefully executed in this work, there are several aspects of synapse selection and annotation that should be more thoroughly described, since these factors may have impacted the authors' findings. In particular;

(2a) The authors appear to annotate active zones and postsynaptic densities by thresholding synapse images at some user-defined pixel intensity value, taking only pixels darker than that threshold as their annotations (Lines 806 – 812). This technique seems like it could be prone to producing noisy annotations, particularly since in the EM images provided (Figures S11-16) the pixel intensities of active zones/postsynaptic densities and surrounding neuropil do not appear to be highly distinct.

(2b) The authors note that they have excluded synapses formed onto cell somata or proximal apical dendrites in their analyses. However, this choice may have resulted in disproportionate exclusion of inhibitory synapses, as inhibitory neurons are more likely to form synapses directly onto somata or dendritic shafts. The authors should quantify the number of synapses that were excluded as a result of this approach and should comment about potential impacts on their findings (for example the fraction of asymmetric synapses observed to form on dendritic shafts of spiny neurons as shown in Figure 6).

3) Much of the value of this study derives from the data itself, and further, in order to fully reproduce the findings in this work, the image volumes, corresponding synapse segmentations, and metadata should be made readily available (pending any agreements that may be needed for sharing human tissue data). Currently, it appears that segmentations and annotations, but not the image volumes, have been made available at the EBRAINS Knowledge Graph. Further, while not essential, it would substantially increase the usability of this dataset if it were deposited in a form compatible with industry standard tools for electron microscopy, like Neuroglancer or cloud-volume, and the authors are encouraged to consider this option.

Reviewer #1 (Recommendations for the authors):

I would like to emphasize that overall, this work contains an impressive amount of rigorous analysis. The main concern I have is that the variability in the analysis, some of which I understand is unavoidable given the work involved in EM reconstructions and in identifying appropriate brain donors, should be more explicitly shown. The claim of homogeneity should be stated in such a way that someone who reads the abstract, for instance, does not take away this piece of your findings without also understanding the important caveats.

Reviewer #2 (Recommendations for the authors):

Specific Recommendations and Concerns

1) The concept of "synaptic organization," as introduced on Line 122, is a key part of the framing but it is not clear what specifically the authors aim to measure. Some meanings could indeed be a "crucial aspect" but some might not. This matters when making claims about views of the "best strategy." There are many aspects to the synaptic organization of the nervous system that require whole-cell scale reconstruction and are completely unavailable to small cutouts or, indeed, anything less than whole-brain datasets. There are other aspects of synaptic organization, such as the ones considered in this work, where smaller cutouts are sufficient, and it is thus possible to generate better sampling. It is misleading to suggest that the detailed goals of and the observations produced by circuit-scale connectomics and small-cutout volume EM are the same, but that is not to say that one is any better than the other. The useful descriptions would be better served if the authors argued concretely why these properties they measure are important.

2) The most impressive part of this study is the sampling across multiple individuals, which is often not feasible in larger-scale EM studies, and the most consistent result is the similarity across them. However, the choice of data representation is inconsistent with regards to the replicates within and between individuals, which dilutes the ability to assess these trends. For example, Figure 3C very nicely shows each sample from each individual, while Figure 1A appears to group samples but still shows each individual, while panels like Figure 1B and Figure 4B-E omit these distinctions entirely. A more consistent and complete visualization of the inter-sample and inter-individual data throughout would strengthen the arguments of the paper. Much of this is already done in the supplementary figures, but could be brought more fully into the results and discussion (for example, variability is largely not discussed in terms of synapse shape or size).

3) While synapses onto excitatory dendrites are generally straight-forward to classify into asymmetric and symmetric synapses, the postsynaptic densities of synapses onto inhibitory dendrites are not as clearly defined in my experience. Similarly, experience has shown that manual detection of small synapses can be quite difficult even after several passes. It would be useful to know how the authors approached and mitigated these specific problems in their tissue.

4) I was surprised by the relatively large value of asymmetric synapses onto dendritic shafts of spiny neurons (10-20%, in most cases 4-5 times the number of symmetric synapses onto spiny shafts), and the consistency across layers, as shown in Figure 6. It does not match my experience in mammalian cortex that excitatory inputs onto excitatory shafts significantly outnumber inhibitory inputs onto shafts. Is this a difference between mouse/rodent and human MEC?

5) Much of the value of this study derives from the data itself. It would be extremely beneficial for the authors to deposit the image volumes, synapse segmentations, and metadata online in a form that could be visualized in industry standard tools like Neuroglancer and read by software such as cloud-volume. This could be especially nice if integrated into the tissue coordinates identified from the light level analysis to create a multiscale dataset. I do see the synapse segmentations on the EBRAINS Knowledge Graph platform, but not the associated imagery. Moreover, the.seg format is for Espina, which appears to not be available for Mac OS. Given that the authors are engaging on a series of similar studies.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human Entorhinal Cortex" for further consideration by eLife. Your revised article has been evaluated by Albert Cardona (Senior Editor), a Reviewing Editor, and a peer reviewer. Their feedback is below.

We thank the authors for the improvements made to the new manuscript, which have addressed many of our comments. We note that the authors have clarified the Results text, added some statistical test data, satisfactorily clarified their synapse annotation methods, and reformatted their plots to meet most of the Essential Revisions stipulations.

However, several points in the Essential Revisions still need to be addressed, as outlined below:

(1) As stipulated in Essential Revision 3, the authors are required to include a way to access their EM data in their Data Availability statement. Although we understand the authors' concerns, sharing raw data is journal policy.

(2) As stipulated in Essential Revision 1, the authors are required to present an explicit quantification of variability for each synapse measurement, in two respects:

* Essential Revision 1a): between the 3 image stacks collected per donor+layer.

* Essential Revision 1b): between donors per layer.

We appreciate several revisions and responses made by the authors with respect to these requirements (below). We would like to clarify what additional changes are required to satisfy Essential Revisions 1a) and 1b) beyond these updates.

– The authors have included a of coefficient of variation for each synapse measure by layer (using aggregated donor/stack data).

– While the coefficient of variation is a useful quantification of the per-layer data assuming it is well-mixed, on its own it unfortunately does not address our main concerns of whether the data itself is well-mixed for each layer, across individual stacks per donor and across donors.

– Data visualizations now show inter-stack variability to a much greater extent, with most properties plotted in the format of Figure 3C (Figure 1C, 3A,C, 4C,E; Figure 1S1A, 4S3A,C).

- This represents a substantial improvement but does not include sufficient information to assess data mixing. The image stack means are provided without a measure of variance, but the combination of both mean and variance is necessary for visualizing cross-stack variability. Currently, error bars correspond to per-layer aggregated data, which is useful for the across-layer comparisons but does not address the issue of variability we raised.

– The authors have noted in their response (Essential Revisions 1c) that sampling of multiple small image stacks within a tissue can be sufficient to capture the distributions of synapse properties, citing Merchan-Perez et al. 2009 (which studied synapse numbers in the cerebral cortex).

– We agree that sampling can be a reasonable strategy for the measurement of anatomical synapse properties and that reconstruction of an entire tissue is not necessarily preferable in these cases. However, given that every donor, tissue type/sample, and synapse property is subject to different variability, it is essential to perform a quantitative analysis of the data itself to show that sampling is sufficient for the synapse properties measured. One piece of this analysis would be a demonstration that stacks are well-mixed, which we are requiring. An additional piece would be a power analysis.

With these points in mind, the following changes are required:

2A) Essential Revision 1a): in Figures1C, 3A,C, 4C,E 1S1A, and 4S3A,C, each data point must be given its own error bar to allow visual comparison of stacks (+/-standard deviation is fine). Additionally, statistical comparisons of the 3 image stacks per donor+layer should be explicitly reported for each synapse measure. A nonparametrical test that compares distributions, like the Mann-Whitney/Kruskal Wallis (used by the authors elsewhere in the manuscript) is appropriate and should be used. Test results (p-values) can be reported in a supplemental table; any cases in which stacks for a donor+layer significantly differ should be noted in the figure legends. Some kind of commentary on these results should also be provided in the text.

(2B) Essential Revision (1b): a new figure panel showing inter-donor variability is required. This new figure should have a panel for each of the following measures: synapse density; intersynaptic distance; SAS synapse area; AS synapse area; macular-shaped synapse area (for SAS and AS synapses separately); complex-shaped synapse area (SAS and AS synapses separately). In each panel the mean + standard deviation should be shown for each donor. Statistical testing should also be performed to check whether donor distributions are statistically distinguishable (Mann-Whitney/Kruskal-Wallis is also fine) and p-values should be reported in a supplemental table, with statistical differences between donors noted in the figure panel/legend. Please also briefly comment on these comparisons in the text.

Notably, this step will be quite useful to the field to be able to cite cases like this when handling questions of inter-individual variability.

(3) The term "synaptic organization" must be replaced throughout the manuscript with a term that clearly communicates the types of measurements that were analyzed, to avoid misinterpretation. One suggestion for an acceptable term would be "anatomical synapse features of neuropil". (Essential Revision 1)

(4) The Abstract, Introduction, and Discussion sections should be revised to clearly indicate that anatomical features of neuropil synapses are being studied, and to clearly summarize the paper's findings as being structural patterns that are either repeated across cortical layers based on their dataset or not. The term "homogeneity" should be avoided. (Essential Revision 1)

(5) Essential Revision 1c): In the interest of transparency, the authors are required to report the (x,y,z) sizes of individual blocks in the manuscript.

In the current revision, the authors' reporting on individual block size unfortunately remains less than transparent. They do report a range and mean of individual block volumes in the text (Lines 212-213: "The number of sections per stack ranged from 244 to 319 (Supplementary file 1c), which corresponds to a raw volume ranging from 384 to 502 μm^3 (mean: 450 μm^3)."), but further clarification about what kind of spatial scale these blocks represent is not presented. Other information about block size is also indirect (inclusion volume per block is given in the "Raw Data Densities" sheet of Supplementary file 2; in Figure 9D FIBSEM trenches are shown at low magnification, with the relevant scale bar in a separate panel such that length estimation is difficult).

Being explicit about the 1-dimensional spatial extents of individual image stacks is important for the claims the authors are making. For example, as noted by Reviewer #2 previously, the author's use of F, G, and K functions only allow them to measure deviations in their data from random point distributions if the densities are changing at a scale smaller than their volume samples.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human Entorhinal Cortex" for further consideration by eLife. Your revised article has been evaluated by Albert Cardona (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. We greatly appreciate that the authors have shared the BOSSDB URL for their EM images. We would just ask that the DOI be added to the manuscript prior to acceptance.

2. The p-values for the Kruskal-Wallace (KW) tests used in assessing inter-individual variability should be provided in addition to the p-values reported for the Dunn's multiple comparison tests. We note that the Dunn test is a follow-up to the KW, and in this case would be used to investigate differences between donor pairs when the KW test indicates significant differences among the 3 donors. Unfortunately, Dunn's test can fail to detect differences for several reasons (it applies a z-score approximation to each donor distribution, and it can use conservative p-value corrections). For this reason, Dunn test p-values should be considered alongside their corresponding KW test p-value.

3. The Discussion section should be condensed substantially (one notable part is Lines 516-568), as this version is still difficult to read through.

4. Line 571: it is stated that synapses "were randomly distributed", but the statistical testing used only implies that no differences could be distinguished from random distributions, which is a different conclusion. Please adjust this phrasing to more accurately reflect the conclusions of these tests.

5. Please place a scale bar in each panel of Figure 9 separately, to help readers more easily interpret these images (currently the authors use one scale bar for all panels, and this makes it difficult to visualize sizes in some panels).
