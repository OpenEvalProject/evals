# Peer review - Round 1

Editors:
- Sean R Eddy, Howard Hughes Medical Institute, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21883.060](https://doi.org/10.7554/eLife.21883.060)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Layer-specific chromatin accessibility landscapes reveal regulatory networks in adult mouse visual cortex" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors use ATAC-seq to probe chromatin accessibility profiles in four layer-specific classes of mouse visual cortical neurons, to identify regulatory elements that maintain layer-specific neuron identity. They present careful descriptive analyses of the data, combined with previous Allen Institute single-cell RNA-seq data from the same cortical region, and compared against relevant histone modification and RNA-seq data from other previously published work. Having identified a likely set of candidate regulatory regions, they present plausible guesses at the transcriptional factor regulatory network that maintains layer-specific adult cortical cell types, such as Foxp2 being expressed in lower layers and repressing TFs for upper layers, and Cux1 doing the reverse.

The referees unanimously agreed that as a data resource, the work is of extraordinarily high rigor and quality, and likely to be a treasure trove for future studies. The referees also agreed that the transcriptional network proposed in the latter half of the paper was speculative and lacked experimental validation. After discussion, we agreed that the paper is a strong contribution as a data resource, suitable for publication in eLife, and that rather than asking for additional experimental validation, various revisions could be made to strengthen the biological interpretation and significance of the data. We also propose some necessary revisions for clarity and for improving access to the data resource.

Essential revisions:

1) The lack of experimental validation of any of the predicted roles for transcription factors and their sites is problematic. Are there published data, such as relevant loss-of-function phenotypes, that you can interpret in light of your data, and test your predictions against?

2) The biological motivation of the work should be clearer, especially for non-neuroscientists. Explain why these neuronal cell classes are of particular interest. The data are for just four layer-specific but heterogeneous cell classes, and cortical cell types are vastly more complicated than this, but you describe the data as "high resolution". Revise the Introduction and the Discussion to be more clear that these data are of intermediate resolution (albeit at the forefront of a rapidly advancing field) and to explain why inferring a transcriptional network at this level of resolution is biologically useful.

3) If in the Discussion you could make one or two specific, important, experimentally testable predictions from your proposed network, this would be a way of clarifying the biological utility of the data resource, and helping to motivate others to make use of it.

4) Clarify the k-means analysis of modules (subsection “ATAC-seq and RNA-seq module analysis” of Methods). Define precisely what vectors you are clustering, how many dimensions they have, and how you define a distance between them. Explain why you use a two-stage clustering approach. Explain what choosing "cluster centers > 0.5" means: the centroids in a K-means clustering are n-dimensional vectors, not single scalar numbers. Explain what you mean by changing cluster centers from >0.5 to 1: arbitrarily moving k-means centroids makes no sense either. Explain in Figure 5—figure supplement 1 what you mean by "Pearson correlation coefficients for comparisons between cluster centers": two k-means centroids are just two points in n-space, and it's not clear how one calculates a correlation coefficient between two points.

5) Please make the data accessible other than as a raw deposition in GEO. How could an interested biologist use these data with minimal computational overhead? We suggest finding a way to have these data hosted as tracks in a public genome browser such as at UCSC.

6) Clarify whether you believe this TF network is only involved in cell fate maintenance, or its establishment in development, and why.

7) In places, log p-values are being plotted and interpreted as if they measure effect strength (e.g. Figures 4A, 5, 6). Be more careful with this. A p-value is a function of both effect size and sample number, and it isn't clear that you are always comparing across equal sample numbers.
