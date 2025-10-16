# Peer review - Round 1

Editors:
- Harry T Orr, University of Minnesota United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64984.sa1](https://doi.org/10.7554/eLife.64984.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A novel computational approach, Geomic is used to integrate three Huntington disease (HD) datasets and assess changes with disease progression in two pathways previously linked to disease; homeostatic and pathogenic responses in four striatal cell types in a HD model mice as well as human stem cell HD models. The data and analysis support the concept that a major driver of disease is loss of homeostatic pathways. The authors nicely address issues/concerns raised with previous submission.

Decision letter after peer review:

Thank you for submitting your article "Temporal dynamics of cell type-specific homeostatic and pathogenic responses to mutant huntingtin" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Huda Zoghbi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Joan S Steffan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This work presents a novel computational approach, Geomic, and uses it to integrate three Huntington disease (HD) datasets to assess changes with disease progression in two pathways previously linked to disease; homeostatic and pathogenic responses in four striatal cell types in a HD model mice as well as human stem cell HD models. The data and analysis support the concept that a major driver of disease is loss of homeostatic pathways. The Geomic approach is likely to be of considerable use as a tool in the integration of large datasets.

Essential revisions:

1) The novelty of the Geomic method in comparison to existing methods needs to be more clearly presented/discussed.

2) A gene's cell type(s) expression is assigned to the entire bulk RNA-seq gene deregulation surface (GDS, i.e. the log fold changes across both time and number of repeats) by using the shape deformation method on just the data across expanding CAG repeats at just the six month timepoint. If that's correct, need to demonstrate better that you see the same expression pattern for an individual gene across expanding CAG repeats at the six month timepoint as you do across time with one CAG repeat.

3) What about cancellation effects, i.e. if the pattern in different cell types is drastically different and cancel each other out? For example, if a gene is upregulated in one cell type, downregulated in a second cell type at about the same abundance as the first type, and then a third cell type exhibits no change? Geomic can be adapted to handle cancellation events. Was it here? Why not?
