# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56517.sa1](https://doi.org/10.7554/eLife.56517.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Combining synthetic biology, live-cell imaging and stochastic mathematical models, this study demonstrates and explains the non-intuitive observation that, in a single-input module, the expression of genes controlled by a self-regulated transcription factor may differ even when both genes have the same binding sites.

Decision letter after peer review:

Thank you for submitting your article "Inherent regulatory asymmetry emanating from network architecture in a prevalent autoregulatory motif" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The reviewers found the manuscript to be very interesting, in particular the non-intuitive observation that the expression of genes controlled by a self-regulated transcription factor differ even when both genes have the same binding sites. No additional experiments are needed, but both reviewers have asked that some issues be clarified before the paper can be accepted for publication. Please see the reviewer comments below and answer them point-by-point in a revised manuscript.

Reviewer #1:

Using a combined computational and experimental approach, the authors rigorously evaluate a single-input module that shows gene regulation asymmetry for genes with identical regulatory sequences. The authors find that the effect can only be reproduced in a stochastic setting and features such as network size and dilution rate are identified as determinants of the degree of asymmetry. This paper is both well written and executed and its implications in understanding synthetic as well as natural regulatory systems make this well suited for a broad audience. If the authors address some concerns, I would recommend this manuscript for publication in eLife.

1) The experimental methods were not completely clear. Overnight cells were diluted into fresh media and incubated to early log before sampling. Microscopy was then used to quantitate the fluorescence of cells on agarose pads. Are cells assumed to have reached steady-state before sampling and if not could this affect the results? The addition of any time course data that the authors may already have to show that steady-state was achieved would strengthen the data.

2) Why were the results for the 5x decoy plasmid included in the manuscript? The low CFU/mL observed in Appendix 3 and the increased cell size when grown in glucose medium (Appendix 2) suggests that it may have a deleterious effect on the cells, in which case perhaps it would be better to leave out the 5x results. Also, since the estimated copy number for this condition seems to be an outlier as the authors state that the 5x data was not used for copy number estimation in Appendix 3, how was the decoy number for this condition estimated and what number is actually used? The authors should also address whether the different decoy plasmids cause differences in growth rate if known.

3) Another possible explanation for asymmetry could be a difference in translation rates. Even though the promoter and 5'UTRs are the same, regions at the start of the coding sequence (YFP vs LacI) could interact differently with the 5'UTRs. The authors used YFP to show that the promoter with the NoO1v1 operator has similar expression levels to that of the regulated promoter in the absence of LacI. In this case, normalization would not rule out such an effect. The authors could use simulation to comment on how much of the asymmetry could be attributed to differences in translation rates.

4) The authors show that asymmetry exhibits a non-monotonic dependence on TF half-life (degradation rate). The authors should comment on the possible origin of this non-monotonicity. My intuition is that degradation rate allows the TF to reach steady-state faster. Therefore, faster degradation would allow its concentration to better "track" the regulatory state of the TF gene leading to larger asymmetry. But why would an increase in degradation rate above a certain point lead to less asymmetry?

5) The degradation rate experiments required the use of a sspB deletion strain which affects the cell globally. Did the authors observe any changes in growth rate due to the mutation?

6) In the Introduction, the authors claim their aim is to unravel the influence of network size and connectivity on gene regulation. However, their results don't necessarily generalize to more complex networks and different network motifs. It would strengthen the paper if the authors could comment on this in the Discussion.

7) Both in the Introduction and in Figure 1 (panels B and C), much emphasis is put on the role of SIMs in coordination of gene expression timing. The authors should comment on how their results are expected to affect such functions or whether there are any other potential consequences of the discovered asymmetry for natural systems (maybe related to some of the examples given in the Introduction).

Reviewer #2:

In this work, the authors use synthetic biology and live-cell imaging to experimentally characterize the most common regulatory motif in E. coli, the single-input module (SIM). The authors find a non-intuitive result: the expression level of a self-regulatory transcription factor (TF) and their target genes differ, even when both genes have the same binding sites. Using a combination of theory and simulation, they formulate a stochastic model that can account for their experimental observations. A simpler, deterministic model is unable to recapitulate their results.

The paper has sound logic, with a straightforward narrative that allows the reader to grasp the author's model and relate the experimental results with the simulations and theory. The appendices answered several of the questions that arose while reading the manuscript (for example, the effect of genome position and the local diffusion limitation of transcription factors). The results shown are an elegant example of the power of theory and modeling to make sense of non-intuitive biological phenomena. I would be glad to see this work published in eLife.

– The authors calculate the apparent or effective fold change, given that the minimum fluorescent unit measurable does not correspond to zero TFs but the detection limit. The fact that the experiments do not have single-molecule sensitivity should not make a big difference if the detection limit is small. Do the authors have some experimental evidence that this is the case? If no experiments are available, do they have a theoretical expectation of the error they could incur due to such effects? Would the effect still be negligible if both fluorescent proteins have different detection limits? Would we expect different results if they would have used yfp for the TF and mCherry for the target gene?

– Figure 4B seems critical for understanding their model. In principle, showing a single realization of their stochastic model with the transitions between microstates would be useful to convey the idea "at the single-cell level." However, given that the difference between the residency times of states 2 and 3 is small, such a plot may not be clear. Can the authors show, in addition to Figure 4B (maybe in an appendix), a complementary figure with the distributions of "Number of free TFs" and "Time in state"? If the authors have other ideas on how to emphasize this insight, I suggest adding them to the manuscript.

– In the caption of Figure 3, (B-C), the authors write: "the actual free TF measured in simulation." Using the word "measured" to refer to simulation results is confusing. Using "obtained" or "calculated" or omit the word, as used in the titles of Figures 3B-C, would be preferable.

– Figure 5D looks very crowded, which makes it hard to compare distributions between samples and figure panels. Could the authors simplify the plot, for example, by removing the bar plots and leaving the lines (or vice-versa)? If the authors keep the bars, they may want to check whether removing the black outlines and applying transparency makes samples easier to distinguish.

– The authors use "single-input" and "single input" interchangeably. It would be better to be consistent across the text.
