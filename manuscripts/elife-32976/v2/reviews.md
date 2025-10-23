# Peer review - Round 1

Editors:
- Aleksandra M Walczak, Ecole Normale Superieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32976.031](https://doi.org/10.7554/eLife.32976.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Antibiotic-induced population fluctuations and stochastic clearance of bacteria" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Bartek Waclaw (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers found the topic very interesting, however they raise major concerns, both technical and in terms of the discussion of the results, that need to be addressed in great detail if publication is warranted. Please provide a detailed response to all points, the technical points of all reviewers, comparison between the model and experiments, discussion of previous work and the points about the impact of these findings, the parameter regimes where they occur and their link to real environments. While to the best of our knowledge the results presented here have never been reported in exactly this form, the lack of references to past work gives a false impression that no stochastic models of antibiotic resistance have been studied, which is not true (e.g., work from Hermsen and Hwa, the Dunlop group and others, additionally to the ones named by the reviewers (see point 5 below) build on similar ideas). This should be discussed in more detail, especially work that does try to make connections between theory and experiment. In view of these previous papers, the present result is maybe not extremely unexpected and should be presented more as an extension and careful regime exploration than a completely new idea. We therefore urge the authors to present the novelty of these results in a more balanced way.

Major points to be addressed:

1) All reviewers feel that the relevance of the conclusions to real infections is overstated. First, there is a relatively narrow window in which stochastic clearance occurs and it may be challenging to hit this precise window outside of a well-controlled lab experiment. Real infections are not treated when the number of cells is 100 to 10^4 but rather 10^8 or more since only an infection becomes evident. In such large populations different stochastic effects (de novo mutations that confer resistance to antibiotics, phenotypic adaptation) are likely to be more important than demographic fluctuations. Second, antibiotics only help to clear infections in vivo, and the most work is probably done by the immune system. Extrapolating from in vitro experiments where no immune response is present can be misleading. It would be interesting to discuss the possible role of the immune system in bacterial clearance within an actual patient. The authors should discuss these points in detail and tone down their statement.

2) Although the authors present data in Figure 1C showing this is not the case for the two rounds of exposure they use here, please discuss the effect of repeated sub-MIC antibiotic exposure and how this will ultimately impact the evolution of antibiotic resistance in the cells that do survive.

3) The manuscript would be improved by a more thorough and explicit comparison between the data and the model predictions:

- In Figures 1A, 1B and Figure 1—figure supplement 2, trends in the data have been highlighted by gray arrows. While we agree that the data show these trends, such "guides for the eye" can be misleading. Please graph linear regressions of the data (on the whole data set for Figures 1B and figure 1—figure supplement 2, and for concentrations below a certain threshold for Figure 1A). It would be useful to indicate the slope and the correlation coefficients obtained.

- Figure 3B and subsection “A simple, stochastic model of the population dynamics accounts for stochastic clearance of bacterial populations”, last paragraph: The data follow the predicted exponential decay at long enough times, but it would be interesting to push the analysis further:

- Does the slope of the data in this regime agree with the prediction from Equation S7?

- Can the delay before the onset of this decay be understood by the full expression of 1-P0, or are there extra complications at early times?

- Subsection “A population with large inoculum size is subject to stochastic clearance at sub-MIC drug concentrations”, last two paragraphs: Here the fluctuations in inoculum size could play a role in the stochasticity of the outcome, especially for small inoculum sizes. This point should be briefly discussed.

- Figures 4, Figure 4—figure supplements 2-4 and subsection “Alteration of the extinction probability to facilitate bacterial eradication at sub-MIC drug concentrations”, last three paragraphs: The data look quite deterministic, while the phenomenon is stochastic, and while Figure 1B (which corresponds to the same data as the white columns in Figure 4A) included error bars corresponding to a standard deviation over several experimental replicates.

If only one replicate was considered for some experiments, this should be stated. If the mean over different replicates was plotted, it should be mentioned, and error bars should be added, similarly to Figure 1B.

- For example, could the slope of the dashed line in Figure 3B be predicted from the model? Or Figures 3D and 4A – do they quantitatively agree with model predictions? This should be fairly easy to do given the existing data on growth and death rates.

4) In some cases, it would be nice to show more data, especially if it already exists:

- "CV decreased with increasing inoculum size, supporting the expectation above": It would be nice to show the corresponding data.

- Video: it would be helpful to include other videos for comparison purposes, e.g. one without antibiotic and one with a bacteriostatic antibiotic (sub-MIC).

5) As noted in the summary, please reference and discuss previous work more exhaustively. The reviewers feel the novelty of the findings with respect to existing models is exaggerated. It is not true that current models of population dynamics of bacteria exposed to antibiotics are almost exclusively deterministic and that this work is the first to account for stochastic death and replication. A similar approach was used as early as in the 60's, see Nissen-Meyer, 1966. See also a more recent paper that combines stochastic modelling and experiments, Ferrante et al., 2005. in vitro
