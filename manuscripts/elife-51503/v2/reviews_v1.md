# Peer review - Round 1

Editors:
- Stephen Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51503.sa1](https://doi.org/10.7554/eLife.51503.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers found this to be an exciting application of deep learning CNN models and pancreatic islet epigenomic data to type 2 diabetes (T2D) genome wide association study (GWAS) variants, including the convincing experimental validation of a single-locus effect. Additionally, the bulk enrichment analyses shown in Figure 3 demonstrate the likely broad utility of such an approach. Congratulations on the nice work, and we will look forward to seeing how these models are further used to provide mechanistic insights across diverse complex diseases for which GWAS and tissue-relevant epigenomic annotations are available.

Decision letter after peer review:

Thank you for submitting your article "Deep learning models predict regulatory variants in pancreatic islets and refine type 2 diabetes association signals" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Harry Dietz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Wesolowska-Andersen et al. present a convolutional neural network (CNN) derived approach to predict regulatory variants in pancreatic islets and refine T2D GWAS signals. Specifically, the authors measure the regulatory potential of T2D associated variants using the CNN trained on diverse islet functional genomics data and compare their predictions to those derived from genetic and functional fine-mapping approaches. They highlight examples of deep learning derived predictions that help them refine signals at multiple loci in a tissue-specific manner. This is a well-written and interesting paper. Perhaps the most striking result is shown in Figure 3 which convincingly shows differential enrichment when T2D GWAS signals are partitioned into insulin action vs. secretion loci. The single locus validation is also quite nice.

Overall, the findings are reasonable and the validation at the end ties the manuscript together nicely. However, we recommend revisions that would improve the overall clarity of the manuscript and associated figures.

Essential revisions:

Showing a cartoon/schematic of the CNN architecture used and how the input and output map to this architecture will be useful for guiding the general readership at eLife.

The authors should mention in the Discussion how their prediction method contrasts with doing some experimental rapid high-throughput approach like Hidra.

It is clear that the authors are aiming to make the case that their models are an improvement over previous prediction approaches. Although they make a strong case, one does wonder if pancreatic islets are the best setting in which to initially do this. After all, pancreatic islets represent a mixed cell population, so any epigenomic features will be drawn from all the diverse cells of this tissue. Given there is an abundance of 'pure' cell types with this sort of data available (for example, in ENCODE), it would have utility to 1) run in that setting first to demonstrate the optimal power of this approach for a relevant disease with an abundance of GWAS hits, and then 2) understand what the 'cost' is if you subsequently run in a mixed cell setting like the one they delineate. The problem with this will be with getting a relevant GWAS data set that aligns with a very densely-profiled cell line and other orthogonal validation data. Another alternative "validation" approach could be to compare the models to islet eQTLs, for which there are now good data sets available. The models presented here should be highly enriched for islet eQTL. Our discussion led to the conclusion that implementing one of the above approaches will strengthen the work: either implementing the models in a homogeneous cell line (to circumvent the issues associated with mixed cell populations) or to perform model comparisons with islet eQTL signals.
