# Peer review - Round 1

Editors:
- Redmond G O'Connell, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83722.sa0](https://doi.org/10.7554/eLife.83722.sa0)

This important study examines how humans use information about the confidence of collaborators to guide their own perceptual decision making and confidence judgements. The study addresses this question with a combination of psychophysics, electrophysiological modeling, and computational modelling that provides a compelling validation of a computational framework that can be used to derive and test theory-based predictions about how collaborators use communication to align their confidence and thereby optimize their collective performance.


---

# Peer review - Round 1

Editors:
- Redmond G O'Connell, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83722.sa1](https://doi.org/10.7554/eLife.83722.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Interpersonal alignment of neural evidence accumulation to social exchange of confidence" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers agree that your paper has significant merit and represents a potentially important advance for the field. They also do highlight a number of areas where the description of methods needs to be clarified as well as control analyses that would need to be conducted in order to verify the reported results. The reviewers also highlight several areas where the authors' claims should be tempered and/or discussed in more detail.

1) Both reviewers query the extent to which the paradigm was representative of real-world cooperative decisions. Here, the decision was not agreed upon but rather assigned to the most confident observer. Examination of the degree to which the results might be paradigm-specific is warranted. Relatedly, there are several areas where the claims of the authors would need to be tempered or else additional analyses provided. Reviewer 1 highlights that the authors imply that causal links between pupil diameter, CPP, and confidence have been demonstrated when this is not the case. Analyses establishing such links should be conducted or else the authors' conclusions should be amended.

2) Both reviewers indicate that additional control analyses should be conducted to verify the connectivity results.

3) Further analyses need to be conducted in order to establish that the reported ERP signal really is a CPP. Response-locked ERP waveforms should be shown and analysed in order to verify that the observed signal bears the known functional properties of the CPP.

4) Further detail is required regarding the methods used for analysing the pupil data and for calibrating the stimuli to allow meaningful pupillometry. In addition, Reviewer 2 suggests employing a timeseries-based statistical framework rather than relying on averaging over arbitrary timeframes.

5) Both reviewers point to insufficient detail being provided regarding the model fitting procedures to allow for replication. Were all parameter values fit by the model or were some of them fixed according to the authors' own criteria?

Reviewer #1 (Recommendations for the authors):

Abstract: The authors write that their model "spontaneously demonstrated the emergence of social alignment". I don't think that this is correct, social alignment was not spontaneous, as a key aspect was introduced specifically for this purpose (using the confidence of one agent as a top-down drive for the decision process of the other agent).

Introduction: I find that the general use of citations should be improved. Many references are only vaguely related to the content they are supposed to support, and there is a bias towards citing studies that have been published recently and in high-impact journals, at the expense of more relevant ones.

Results:

Please report the method and results of the debriefing questionnaire.

Figure 1b would be easier to understand if the x- and y- axes were swapped, as the participant's confidence is an outcome whereas the agent's confidence is controlled by the experimenter if I understand it correctly.

In Figure 1 supplement 3, the authors write "The results did not change compared to figure 1c indicating the previous trials confidence impacts the behaviors in the upcoming trial regardless of experiment conditions (HCA, LCA)". This is not clear to me. Did they compare the effects reported in this figure between the two experimental conditions?

The authors interpret the larger pupil size (in blocks where participants are paired with a low-confidence agent) as reflecting participants' lower confidence. The evidence supporting this interpretation is far from clear. As noted by the authors, there are several alternative possibilities (arousal for instance). The authors might present more direct evidence linking confidence to pupil size in their own data, e.g. by examining this relation on a trial-by-trial basis, within each block or after the main effect of block is removed from the variables.

(Top of page 8) The 'intuitive description of the impact of global top-down input' does not provide a clear intuition to the reader. When both traces rise faster, why is there an increase in confidence? why does the difference between the two traces also increase in this case?

In the empirical and simulated data, it would be important to test the interactions between factors (coherence and partner's confidence, isolated vs. social) for completeness. In addition, the full specification of the GLMMs should be reported in the methods.

In their modelling work, the authors consider several candidate models in which a specific parameter is affected by the confidence of the partner in the previous trial. Then Figure 3d suggests that in simulations of the 'best' model, confidence matching occurs within the first 5 to 10 trials. When the initial trials are discarded, can we still observe confidence matching? It would be also important to compare this very fast convergence to that occurring in the real data. As the confidence of the partner is mostly modulated across different blocks of trials, it is unclear whether there is really a trial-by-trial adjustment beyond the first few initial trials within each block.

The model comparison (figure 3 —figure supplement 4) indicates that statistical comparisons between different models were done by using 20 initial points for each model. I don't think that this is relevant. Model fits should be estimated for each participant, and the fit quality can be then compared across participants. Figure 3 – supplement 5 is also not very informative. Individual data and fits, in the format of Figure 1c would be more relevant to examine the quality of the data and model fits.

The authors write: "These findings are the first neurobiological demonstration of interpersonal alignment by coupling of neural evidence accumulation to social exchange of information". It is not clear that the CPP contributes to the alignment of confidence. The authors have shown that both CPP and confidence are different between the HCA and LCA conditions. They have not shown that CPP and confidence are actually connected, nor that the change in one variable mediates the change in the other.

The finding of a greater information flow from the prefrontal to centro-parietal cortex in the HCA condition is potentially interesting, but not so convincing in its current presentation. It would be helpful to run control analyses in order to ensure that a flow in the opposite direction is not as likely and that the result would also not be present with a different region of interest instead of PFC. It would also be important to examine this same quantity in the non-social condition, in order to better qualify the results in the social condition.

In this section, it's also unclear how this increase in connectivity for HCA contributes to the CPP. Theoretical arguments and empirical data should be provided to address this.

Finally, I find the writing often unclear, difficult to follow and often trying to oversell the findings. I understand that this is subjective, but I suppose that simpler sentences and shorter expressions would make it easier for the reader (e.g. avoiding word bundles such as "socially observed emergent characteristics of confidence sharing", or "causally necessary neural substrate"). I find that clarity and concision would help the reader understand the true extent of the contribution of the study.

Reviewer #2 (Recommendations for the authors):

To address the weaknesses, it would help if the authors could:

1) Bolster sample sizes.

2) Provide a clearer definition of the types of uncertainties that are associated with communicated low confidence, and a discussion of which of these trigger the observed effects.

3) Describe the pupil analysis in much more detail, in particular how they calibrated the stimuli to allow interpretability of baseline signals and how they selected the specific traces in each trial's ITI so that they are not contaminated by stimuli.

4) Employ a more convincing time-series-based statistical framework for the analyses of the pupil data that does not rely on crude averaging over arbitrary timeframes, while correcting for multiple comparisons and autocorrelation.

5) Provide response-locked analyses of the EEG signals to establish that they correspond to the decision-linked CPPs as reported in the literature.

6) Provide much more information and justification for the selection of the signals that are interpreted as reflecting the top-down drive from the prefrontal cortex, and either also provide source-localization methods or any other type of evidence for the prefrontal origins of these signals. Also please display where in sensor space these signals are taken from (even that is missing).

7) Describe for every single parameter value that is reported whether it was produced by fitting the model and how exactly this was done, whether it was manually adjusted to produce a desired pattern, or whether it was set to a fixed value based on some clearly defined criteria. The aim is that others can replicate this work and use this model in the future, so this information is crucial!

8) Provide robustness analyses that show that the assumptions about linear modulation of parameters by confidence and the offset of the accumulation at the end of the stimulation period are justified.

9) Provide some more discussion about the unnatural properties of the fake interaction partners in this experiment, and to what degree this limits the interpretability of the findings and their generalizability to other contexts. Ideally, the authors would already show in a new sample and setup that the model can apply to real interactions, but that may be too much to ask for a single paper.
