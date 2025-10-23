# Author response - Round 1

Authors:
- Augustine Xiaoran Yuan
- Jennifer Colonell ([ORCID: 0009-0009-3940-0689](https://orcid.org/0009-0009-3940-0689))
- Anna Lebedeva
- Michael Okun
- Adam S Charles ([ORCID: 0000-0002-9045-3489](https://orcid.org/0000-0002-9045-3489))
- Timothy D Harris ([ORCID: 0000-0002-6289-4439](https://orcid.org/0000-0002-6289-4439))

## Response text

DOI: [10.7554/eLife.92495.3.sa3](https://doi.org/10.7554/eLife.92495.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1, in both the public review and recommendations to authors, raises the important question of generalizability of the new technique to other brain areas, to analysis with sorters other than Kilosort, and in the absence of reference data. Specifically, how can experimenters working in brain areas other than visual cortex understand if the tracking is functioning, and set the parameters in the tracking pipeline.

We agree that generalizability of the tracking procedure is a serious issue, especially with respect to other brain areas with varying degrees of measured waveform preservation over time. As the number of potential recording conditions is combinatorial to experimentally test, we instead address these issues in the manuscript by providing a general prescription for interpreting the distribution of vertical distances of matched pairs that can be used for data from any recording using any spike-sorter (Methods section 4.2, Supplement section 8.4, figure S9, paragraphs 7-10 of the Discussion section). This extension of the method allows users to estimate the matching success in the context of their own data, even in the absence of reference data. To address the concern of overfitting, we have also added discussion covering adjustment of the two parameters in the procedure (the relative weight of waveform distance vs. physical distance, and the threshold for accepting matches as real) to the Discussion section.

Reviewer #2 suggested clarification of the following points in the public review. We answer those here and have also clarified these points in the main text where appropriate.

(1) What is the purpose of testing the drift correction with imposed drift (Figure 2, page 6 in the original manuscript), and how the value was chosen?

To test the ability of EMD to detect substantial drift, we need examples that resemble experimental data, including error in fit unit positions and units with no correct matches. We chose to create these examples by taking waveform and position sets from real data with modest drift, and adding a fixed shift to one dataset. The value of 12 um in the figure is arbitrary, simply an example in the range of real drift. These tests allow us to demonstrate the success of EMD for detection of drift in real data.

(2) How is performance affected by using a different weighting of the 2 measures (physical distance and waveform distance) in the EMD?

Recovery rate (number of reference units successfully matched in EMD) vs weighting of the waveform distance is shown in Supplement section 8.10. Recovery rate increases with low values of waveform weighting, leveling off at a value of 1500. We selected that inflection point for the analysis in this paper, to avoid coincidental matching of physically distant units with similar waveforms.

(3) Should the intervals measured in the survival plot in Figure 5 be identical for the three different classes of tracked neurons?

The plot includes all chains of tracked neurons, which can start on arbitrary days in the set of all recordings (see the definition of chains in section 2.4). As a result, the gaps between days, which determine where there is a point on the plot, can be different for the three sets of neurons (reference, putative, and mixed). We have added a comment to the Figure 5 caption to ensure this is clear.

(4) Would other metrics of the similarity of visual responses work better?

The similarity metric we use was adopted from the original paper using this data (reference 7). We chose to use the same metric both to take advantage of the original authors’ expertise about the data and allow for reasonable comparison of the new technique to theirs. It is correct that this similarity metric alone does not allow for unique matching (see Discussion and Supplement section 8.2). However, the agreement of EMD with reference pairs determined from the combination of position and visual response similarity is very high, suggesting there are few incorrect reference pairs. Any incorrect reference pairs cause an underestimate of the tracking accuracy.

(5) Add a definition of ROC.

Added this definition to the text.

Reviewer #1 Recommendation to authors:

The main text needs proofreading.

We agree that the manuscript needed more thorough proofreading, and we have made corrections of typos and minor language errors throughout.

Additional comment from the authors:

Since the posting of this manuscript, another method for tracking neurons has been introduced:

Enny H. van Beest, Célian Bimbard, Julie M. J. Fabre, Flóra Takács, Philip Coen, Anna Lebedeva, Kenneth Harris, Matteo Carandini, Tracking neurons across days with high-density probes, bioRxiv 2023.10.12.562040; doi: https://doi.org/10.1101/2023.10.12.562040
