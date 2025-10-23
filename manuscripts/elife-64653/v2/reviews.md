# Peer review - Round 1

Editors:
- Grégoire Altan-Bonnet, Memorial Sloan-Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64653.sa1](https://doi.org/10.7554/eLife.64653.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The T-REX method characterizes rare populations by cytometry. The potential applications in the context of analyzing antigen-specific T cells (as identified as tetramer-positive cells) are important with an interesting use of 2 timepoints-cohort of samples from rhinovirus-infected patients.

Decision letter after peer review:

Thank you for submitting your article "Unsupervised machine learning reveals key immune cell subsets in COVID-19, rhinovirus infection, and cancer therapy" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Stephen De Rosa (Reviewer #2); Ahmed Mahfouz (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Reviewer #1 (Recommendations for the authors):

The machine learning workflow Tracking Responders EXpanding (T-REX) was created to identify changes in both very rare and common cells in diverse human immune monitoring settings. T-REX analysis of paired blood samples provides an approach to rapidly identify and characterize mechanistically significant cells and to place emerging diseases into a systems immunology context. Data types used to challenge the T-REX algorithm here included a new spectral flow cytometry study (Dataset 1) and three existing mass cytometry datasets (Dataset 2, Dataset 3, and Dataset 4). However, some of the more critical questions are as follows:

1. T-REX algorithm was a modular data analysis workflow including UMAP, KNN, and MEM. This is not a new algorithm but a combination.

2. Why choose this workflow, UMAP, KNN, and MEM are traditional classical algorithm, and not compare it with another algorithm? Refer to "A comparison framework and guideline of clustering methods for mass cytometry data".

3. What is the basis for setting the parameters, and what data can be used?

4. The references are not normative, for example, reference 2.

5. The figures are not clearly marked.

Reviewer #2 (Recommendations for the authors):

For the rhinovirus study, much of the data are shown through visualization on UMAP plots and the change in tet+ cells is graphed. Perhaps it would also be informative to graph the data as percent of CD4+ cells across all the participants for both day 0 and day 7 to summarize the results in a single graph and to note the actual frequency of these cells.

Perhaps the T-REX method could be tested with data sets from functional assays (such as flow cytometric intracellular cytokine staining) that are more commonly used to detect and characterize antigen-specific T cells. For such data, could the method perhaps compare the stimulation condition to the unstimulated condition rather than samples from different time points?

Reviewer #3 (Recommendations for the authors):

- Please include additional details on how the enrichment of tertramer positive cells in "hotspot" regions is determined.

- A formal mathematical definition of the two measures: Degree of change and Direction of change will be greatly helpful.

- A table summarizing the details of each dataset (number of cells, markers, individuals, cells per individual…) will be greatly helpful for the readers.

- The two shades of purple in Figure 3A are indistinguishable.
