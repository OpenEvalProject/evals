# Peer review - Round 1

Editors:
- Michael Doebeli, University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63661.sa1](https://doi.org/10.7554/eLife.63661.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides an analysis of the metabolic feedback mechanisms regulating overflow metabolism during glycolysis in E. coli. The authors present a kinetic metabolic model incorporating glycolysis, the TCA cycle, and acetate metabolism, and argue that acetate needs to suppress glycolysis and TCA cycle activity for the model to be able to reproduce experimental findings. The assumption of acetate activity is further validated through experiments showing that acetate reduces expression of the glucose phosphotransferase system and of most TCA cycle genes. Another finding is that the control of acetate production shifts from inside (low acetate concentrations) to outside (high concentrations) the acetate pathways.

Decision letter after peer review:

Thank you for submitting your article "Control and regulation of acetate overflow in Escherichia coli" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional work is required before it can be published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Essential revisions:

1) Modeling choices, model robustness and the question of alternative models need to be more thoroughly addressed.

2) Interpretation of experimental results need to be strengthened, in particular with regards to the time scales of transcription and regulation.

3) All comments made by reviewers need to be thoroughly and constructively addressed.

Reviewer #2 (Recommendations for the authors (required)):

The manuscript delves into a major classical question in the study of metabolism, namely how organisms balance the decision of respiring or fermenting carbon sources, and what role fermentation by-products play in this process. Specifically, the authors focus on E. coli and the dependence of its physiology on acetate present in the environment. This is an interesting topic relevant to a broad spectrum of questions, including cancer metabolism. The approach is original, and the specific hypothesis that acetate influences transcription and the metabolic flows in previously unknown ways is well-posed and intriguing. I must admit though that I am not totally convinced that the results provide conclusive evidence about their hypothesis, ruling out other possibilities. Clear comparisons with alternative models, parameter sensitivity analyses, and a clearer expression of possible caveats would alleviate this concern, and help readers clearly understand the possible limitations of the approach employed. The work should be of interest to a fairly broad audience of biochemists, microbiologists and systems biologists.

Subsection “Testing the model”: the authors mention an excellent agreement between model and experiment in Figure 3. I think the agreement is not bad, but I would not call it excellent. I am not sure a p-value is absolutely necessary, but it would be good to at least have an idea of how much variability the experimental data may have beyond the shown error bars, and whether the agreement is really unexpected, also in light of the parameter fitting presented in Figure 1.

It would be useful to see Figure 3 in absence of the acetate inhibition effects. Would the results look only quantitatively different or also qualitatively different? Can the authors comment on the intuitive meaning of these curves. Is any of these curves dramatically affected by the new model, relative to alternative standard models?

As opposed to what is mentioned in the Introduction, stoichiometric models could in principle help address the questions posed by the authors. This would not be the case for regular FBA models, but would be true for dynamics FBA models, in which the extracellular concentration of substrates is explicitly accounted for.

The “Metabolomics experiments” subsection in the Materials and methods is very brief, and does not get into the detail of flux measurements reported, which are crucial for the model and its interpretation.

I am curious about whether acetate inflow and outflow are separately measurable (and measured) in the system, or whether the reports are for the net flow. I am not sure if multiple acetate transporters exist, and whether it is in principle possible for E. coli to simultaneously secrete acetate due to fermentation and take it up from the environment, but it would be good for the authors to comment on this.

No parameter sensitivity analysis was performed. I would recommend that the authors either add it, or comment on why it would not be useful.

The authors' conclusions are presented in an absolute way, that leaves no room for alternative explanations. Partly due to the issues mentioned above, after reading the paper I felt highly intrigued by the results, but not 100% convinced that their explanation is the only possible. I would suggest that the authors (a) take steps to present in a more critical way the results in light of other models that were not explicitly tested, and (b) acknowledge explicitly possible limitation of this study, and avenues to further corroborate the proposed mechanisms.

Introduction, second paragraph: it becomes clear from the context, but the authors should clearly mention that they refer to extracellular concentration of acetate.

Reviewer #3 (Recommendations for the authors (required)):

The manuscript presents an extension of previous work of the group (Enjalbert et al., 2017; Millard, Smallbone and Mendes, 2017). The authors present an interesting dynamical model of overflow metabolism, producing new insights into a long-standing question in bacterial physiology. The model is confronted with new data that appear to confirm specific model predictions. The major novelty of the model is the addition of a direct control by acetate of the activities of glycolysis (or glucose uptake) and the TCA cycle. Very interesting transcriptomics data appear to confirm these regulatory relationships. However, transcriptional regulation and the direct regulations suggested by the model act at different time-scales. In conclusion, the work is very well carried out and interesting. The connection between the transcriptomics data and the model need to be clarified.

1) The first major argument in favor of control of glycolysis and the TCA cycle by acetate is the quality of fit to bioreactor data. It does not seem surprising to me that the quality of fit (Figure 1B) is improved by adding additional regulatory interactions. Even though the figure shows a significant improvement of the fits, it would be nice to see the alternative fits (the equivalent of Figure 1C) in supplementary information.

2) A strong claim of the manuscript is that a kinetic model is needed to account for experimental observations. The fits in Figure 1 use the dynamical model at steady state. How do the predictions compare to the alternative models (global control of metabolism, local control of the acetate pathway)?

3) The transcriptomics data are very interesting. However, these data were acquired at steady state, reflecting a slow adaptation (order of magnitude of the generation time) of physiology. The regulatory interactions (square brackets in the equations in the subsection “Model construction”) are instantaneous effects of the concentration of acetate. I fail to see how the transcriptomics data can argue in favor (or disfavor) of the kinetic model.

4) The perturbation experiments (Figure 3) are probably the best test of a dynamical model. The model correctly predicts the observed dynamics, which are clearly on time-scale of minutes, precluding transcriptional regulation as a cause. The authors could suggest possible molecular mechanisms.

5) The remaining results of the manuscript address model properties and are very well carried out. Under the hypothesis that the model is correct, these analyses yield interesting insights into the physiology of overflow metabolism.

In conclusion: the manuscript describes a very interesting extension to current models of overflow metabolism in E. coli. The experiments are very well carried out and pertinent new data are presented.

My major concern is that the transcriptomics data seem disconnected from the kinetic model. Long-term adaptation can be achieved by modifications in gene expression. However, this does not correspond to the mechanism described by the model equations. The manuscript would be much stronger if the authors could show at least one of the molecular mechanisms by which acetate controls metabolic pathways. I realize that this would be "another" manuscript and cannot be reasonably covered by major revisions. The authors could at least discuss possible molecular mechanisms of this regulation.
