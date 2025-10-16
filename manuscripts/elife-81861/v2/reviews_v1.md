# Peer review - Round 1

Editors:
- Robert H Singer, https://ror.org/05cf8a891 Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81861.sa0](https://doi.org/10.7554/eLife.81861.sa0)

In this article, Bohrer and Larson revisit previously published imaging datasets in order to tackle a long-standing question in modern genome biology: does the physical proximity of transcribed genes correlate with their co-expression? The authors provide convincing evidence to deduce that when a pair of loci are brought within sufficiently low physical 3D proximity (unrelated to their genomic distance) they are more likely than expected to be co-expressed. This is a result of potentially fundamental importance.


---

# Peer review - Round 1

Editors:
- Robert H Singer, https://ror.org/05cf8a891 Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81861.sa1](https://doi.org/10.7554/eLife.81861.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Synthetic analysis of chromatin tracing and live-cell imaging indicates pervasive spatial coupling between genes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and James Manley as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Robert A Coleman (Reviewer #1); Argyris Papantonis (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Using spatial analysis and modeling, the authors have impressively extended the findings of Su et. al, Cell 2020, who generated the analyzed dataset. A number of important concepts were explored including (1) do genes re-position upon activation and (2) can spatial proximity be correlated with transcriptional co-regulation. In general the authors conclusions are supported by their findings and should provide a blueprint for analysis of additional related big imaging datasets in the future.

Both reviewers find the manuscript important and valuable but have suggestions for improvement of clarity and analyses. These include:

Statistical analysis of the significance of the data needs to be done.

The writing is dense and should be made more readable, less jargon and details that would be more appropriate in the methods. A graphic image would help.

The authors should explore stratifying ON states in high and low to see if additional insights can be extracted.

Reviewer #1 (Recommendations for the authors):

(1) The authors should determine the statistical significance of their findings for figures 1 and 2, along with a thorough description of their bootstrapping and statistical analysis methods in the methods section.

(2) If possible, for Figure 1, it would be highly insightful to see whether known enhancer elements are moving closer to promoters of target genes during transcriptions as a comparison to their existing promoter-promoter data.

(3) An extension of the author's findings would be that histone marks associated with transcriptional activity (e.g. H3K27ac) would be enriched in chromatin loci that are in close proximity to the promoter when the gene is on. As a control, chromatin loci containing histone marks associated with gene activity (e.g. H3K27me3) would not move much between the on and off state. In other words, for a locus that is closest in proximity to a promoter, it would be very beneficial to measure the degree of H3K27ac (e.g. a mark of enhancer activity) compared to other surrounding loci of greater physical distance. ChIP-seq datasets for a variety of histone marks are available for the authors to perform this analysis.

(4) The changes in MPD stated in Figure 1I seem to be confined to a small region within 50Kb. How would the data look in Figure 1J/K if smaller bin sizes (e.g. 50Kb) were chosen instead of 500Kb?

(5) Given the authors findings on chromosome dynamics obscuring true correlation, it would be helpful to see if other datasets exist that measure the diffusion of a locus when the gene is turned on as comparison to the TFF1 mobility. Can authors compare the diffusion of MS2- labeled intronic sequences where they have a much larger dataset to draw upon? How does this mobility compare with dCas9 measurements examining diffusion of loci that presumably aren't transcribing.

(6) Representation of figures should be improved for increased clarity (e.g. Figures 1J/K, 2, 3A-C, 4 have data cutoff).

(7) As a way of orienting a non-specialist reader, it might be very helpful to see a representative tracing map of chromatin/promoter loci centroid repositioning upon transcriptional activity.

(8) One way to increase the general impact of this type of study is to lean into the fact (e.g. further emphasize in the text) that more big imaging datasets are on the way. As such, this study is a good example that re-examining publicly available datasets in a new way can lead to fundamental new insights or answers to long standing questions in the field.

Reviewer #2 (Recommendations for the authors):

I think that the following points, if addressed, can further strengthen a very interesting manuscript.

– The analysis is now confined to "on" (1) and "off" gene expression (0) states. I am wondering if the data provide the possibility to stratify the "on" genes in at least "low" and "high" categories and repeat analysis. These categories could reflect high/low FISH signal and/or high/low bursting frequency in the population (something the authors try to incorporate via their live-cell data; see my other comment below).

– For the analysis in Figure 3, contact frequency is deduced using high-resolution Hi-C data (not clear to me which and at which resolution to match that of the imaging). However, it is now well understood that Hi-C is generally depleted from promoter-promoter contacts, and that promoter-capture "C" data can prove tricky to quantify and can carry biases. On the other hand, Micro-C data would work very well here and might even reconcile the imaging with "C" technologies.

– Finally, regarding the (otherwise commendable) effort to generate a model that allows them to "merge" live-cell with fixed-cell data, the authors (i) make a number of assumptions that can be debated, and (ii) use a perhaps too parsimonious way to model chromatin behaviour. As regards (i), a key example is the generalisation of parameters based on analysis of a single locus, TFF1. Similarly the generalisation of ~13 min time for nascent RNA decay probability for all genes based on the MS2 FISH data from ref. 49 is not clear to me. As regards (ii), I think we must acknowledge that in silicon models of chromatin (also linked to transcription output, like the recent Brackley et al., 2021 Nat Commun paper by the Marenduzzo lab) from a number of labs (Mirny, Marenduzzo, Nicodemi, etc.) are growing more and more complex and approximate chromatin and gene expression behaviour evermore accurately. The model employed here is empirically tuned to match aspects of the data, but does not simulate many of the mechanisms known to work on chromatin (like extrusion, which the authors specifically also refer to). I would also like to note that this part of the paper is the least approachable to the average reader, leaves some concepts without any explanation and would benefit from some rewriting; the Results should describe the essence of the model and its key assumptions clearly, and the more complicated math and jargon should be detailed in the Methods, in my view.

– Last, I would like to note that the 400 nm cutoff deduced here is not at all unreasonable given previous data on "transcription factory" sizes (diameters between 85-250 nm) and the resolution of the analysed data. Mention of these in the Discussion could strengthen the postulation by the authors. Their statement reading "enrichment in co-bursting for genes separated by < 622 nm suggests the working distance of the underlying mechanism is not direct contact" should be accordingly tuned. Also, a comparison to the sizes of "condensates" would be welcome. Nonetheless, I was very happy to see that the manuscript offers a very balanced interpretation of results, previous work, and existing caveats, and was very nice to read overall.
