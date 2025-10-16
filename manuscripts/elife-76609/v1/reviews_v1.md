# Peer review - Round 1

Editors:
- Isabel Rodriguez-Barraquer, https://ror.org/043mz5j54 University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76609.sa0](https://doi.org/10.7554/eLife.76609.sa0)

The authors use data from three cross-sectional age-stratified serosurveys on Enterovirus D68 from England between 2006 and 2017 to examine the transmission dynamics of this pathogen. This study's convincing methodology provides valuable insights into the changing dynamics of enterovirus D68, uncovering potential changes in the transmissibility of the virus. It will be of interest to infectious disease epidemiologists and surveillance professionals.


---

# Peer review - Round 1

Editors:
- Isabel Rodriguez-Barraquer, https://ror.org/043mz5j54 University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76609.sa1](https://doi.org/10.7554/eLife.76609.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Changes in transmission of Enterovirus D68 (EV-D68) in England inferred from seroprevalence data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

The authors use data from 3 cross-sectional age-stratified serosurveys on Enterovirus D68 from England between 2006 and 2017 to examine the transmission dynamics of this pathogen in this setting. Understanding these dynamics, including how it changes over time, may help uncover potential changes in the transmissibility of the virus. While the topic is relevant, interpretation of the results challenging largely due to the great uncertainty around how to interpret the serological (serostatus) data, and the impact this has on the inferences made. We ask the authors to perform some additional analyses and to provide more intuition to understand some of the key findings of this analysis.

1. We struggle to reconcile the evidence of a stable or even small drop in FoI after 2010 in the 1:64 models in contrast to the continued increase using the 1:16 cut-point.

2. It is hard to reconcile evidence of drops in FoI in the 1:64 (models 4 and 5 from 2010/11 (Figure 3)) with steadily increasing R0 in this period (Figure 4). Is this due to changes in the susceptibility proportion. It would be good to understand if there are important assumptions in the Farrington approach that may also contribute to this discrepancy.

3. One of the major findings of the paper is that there is a steadily increasing R0 (using the 1:64 cut-point). This again is difficult to understand and would suggest there are either year on year increases in inherent transmissibility of the virus through fitness changes, or year on year increases in the mixing of the population. It would be useful for the authors to discuss potential explanations for an inferred gradual increase in R0.

4.The estimated FOI in 1 year olds is very very high (with a suggestion that up to 75% get infected within a year) and difficult to believe, especially as the force of infection is assumed much lower for all other ages. The authors exclude all <1s due to maternal antibodies, which seems sensible, however, does this mean that it is impossible for <1s to become infected in the model? We know for other pathogens (e.g., dengue virus) with protection from maternal antibodies that the protection from infection is gone after a few months. Maybe allowing for infections in the first year of life too would reduce the very large, and difficult to believe, difference in risk between 1 year olds and older age groups. I suspect you wouldn't need to rely on <1 serodata – just allow for infections in this time period.

5. Relatedly would it be possible to break the age data into months rather than years in these infants to help tease apart what happens in the critical early stages of life.

6. Additional context of EV-D68 in the study setting of England would be useful. While the Introduction does mention AFM cases "in the UK and elsewhere in Europe" (line 53), a summary of reported data on EV-D68/AFM in England prior to this study would provide important context. The Methods refers to "whether transmission had increased over time (before the first reported big outbreak of EV-D68 in the US in 2014)" (lines 133-134), rather than in this setting. It would be useful to summarize the viral genomic data from the region for additional context – particularly since the emergence of a viral clade is highlighted as a co-occurrence with the increased transmissibility detected in this analysis.

7. Given the substantial uncertainty in the assay, it seems optimistic to attempt to fit annual force of infections in the 30 year period prior to the start of the sampling periods. Authors should consider including a constant λ prior to the dates of the first study across the models considered.

8. While the authors have made data sets available, it would be good to make computer code available as well.

Reviewer #1 (Recommendations for the authors):

In the abstract it would be helpful to have some info on the AFM in England as a link between the global picture explained and then this analysis which is for England.

Line 188-120: I agree with the point here, but wonder if a little more to be added to help guide the reader through this thinking from lower seroprevelance to age. I also wonder if it isn't due to an increase in transmission what is it due to? Perhaps this could also be elaborated on.

Line 169 (and methods): Please provide more information on the LOO criteria and what was left out. More required in the main text and also in the methods.

Reviewer #2 (Recommendations for the authors):

– The submission lists only 2 contributing authors, but the manuscript lists additional authors. The author lists should be synced.

– While the authors have made data sets available, computer code was not available as far as I could tell.

– For Models 4 and 5: what were the estimated values of sigma0 and σ? They were not included in Table S1. In the Methods section, λ_{t=t1} is modeled as a Normal centered at 0 – is this on the log scale?

– Figure 2 (E and F): what does the purple class indicate for this model? Is it an average across all other age classes?

– Table 1: it was not clear why Model 3's δ LOO is so poor compared to Model 5 despite the similar visual fits of the models (Figure 3 vs. Figure S5), particularly among the under 20 year-olds. Could the authors provide some more intuition on this? Are there particular data points that are highly influential on the LOO statistic?

– Line 142: should this sentence also include γ?

– Lines 159-167: the values cited in the text do not seem to match those in Table S1.

– Line 172: what do these p-values represent?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Changes in transmission of Enterovirus D68 (EV-D68) in England inferred from seroprevalence data" for further consideration by eLife. Your revised article has been evaluated by Eduardo Franco (Senior Editor) and a Reviewing Editor.

The manuscript has been improved, but there are a couple of issues that need to be addressed, as outlined below (see comments from reviewer #4)

Reviewer #4 (Recommendations for the authors):

I have two comments on the revision:

1. I agree with the authors' decision to implement maternal antibodies as part of their modeling approach. However, the estimated proportion of individuals with maternal antibodies by age seems very high for the 1:16 cutoff. Is it realistic to have maternal antibodies in >25% of 2 year olds? If not, it might be prudent to have m(a) go to zero by a certain age.

2. I had made a comment in the previous round of review about extending the x-axis to the start of the time period of estimation: this was in reference to FOI, not seroprevalence. The FOI estimates in Figure 3A begin in 1990, but the oldest cohort in this analysis are 40 y in 2006, and it's not clear what is assumed about FOI between 1966 and 1990. Or does the random walk on the FOI begin in 1966? It would be good to show those results.
