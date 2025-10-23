# Peer review - Round 1

Editors:
- Andrea E Martin, https://ror.org/00671me87 Max Planck Institute for Psycholinguistics Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84602.sa0](https://doi.org/10.7554/eLife.84602.sa0)

This important work advances the available statistical methods for estimating the degree to which the neural response is phase-locked to a stimulus. It does so by taking a compelling Bayesian approach that leverages the circular nature of the phase readout and demonstrates the added value of the approach in both simulated and empirical datasets.


---

# Peer review - Round 1

Editors:
- Andrea E Martin, https://ror.org/00671me87 Max Planck Institute for Psycholinguistics Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84602.sa1](https://doi.org/10.7554/eLife.84602.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Bayesian analysis of phase data in EEG and MEG" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Reviewing Editor Andrea Martin and Senior Editor Joshua Gold. The following individual involved in the review of your submission has agreed to reveal their identity: Benedikt Zoefel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All reviewers agree that a more extensive quantitative demonstration of the advantages of your methodological approach compared to existing approaches is needed. For example, first, quantifying the advantage of your analysis over the ITPC analysis in the manuscript would be more convincing than the current graphical approach.

Furthermore, it seems that using a simulation approach could be helpful. Simulation of common experimental and data situations, as well as extreme or tough cases where traditional methods run into problems (but your method does not, or is more robust), could be persuasive and help make the impact of the approach more demonstrable and quantifiable.

2) Comparison of data – More thorough and extensive quantitative comparison of the performance of your method compared to existing approaches, as all Reviewers mention, could be carried out on multiple (open) datasets of various sample sizes.

3) Reviewer 3 gives helpful concrete suggestions and concerns regarding the impact of this method for statistical inference (viz., mixed models). These, too, need to be addressed, ideally also quantitatively, but could also be addressed formally/mathematically.

4) Reviewer 1 helpfully explains how the perspective of experimentalists needs to be taken into approach in order for the work to have more impact. Similar to (3) above.

Reviewer #1 (Recommendations for the authors):

The study by Dimmock et al. proposes a Bayesian approach to measuring phase coherence. Although I'm familiar with the kind of EEG data analyzed here, I didn't figure out the purpose of the study. It seems like the aim of the study is neither to provide a more powerful statistical test nor to demonstrate some new neural phenomena. The only purpose seems to provide a Bayesian test, but why do we want it?

If the aim is to provide a more powerful test, it should be compared to classic tests for steady-state responses, such as the ones described in the following article.

Picton, Terence W., et al. "The use of phase in the detection of auditory steady-state responses." Clinical Neurophysiology 112.9 (2001): 1698-1711.

The current article is certainly not written in a way that can be understood by an experimentalist. It doesn't matter too much if the methods are hard to follow, but it does matters if no interpretable results are shown. For example, the authors argue that the topographic plots using the new method have a clearer structure than the traditional ones. As an experimentalist, however, I can't figure out which structure is clearer and why it helps to answer scientific questions.

As a methodological paper, testing the method on multiple datasets is a basic requirement. More importantly, the method has to have a clear goal and clearly demonstrate how the goal is achieved.

Reviewer #2 (Recommendations for the authors):

This paper presents a novel Bayesian approach to testing for phase coherence in neurophysiological recordings. The approach is centred on probability distributions and therefore allows for more fine-grained conclusions about the existence of such phase consistency, in contrast to the often artificial yes/no decision on the acceptance of the alternative hypothesis that can be found in the literature.

I find this manuscript well written and the rationale well explained. The authors demonstrate that their approach can produce similar, but potentially clearer and less noisy results as compared to more commonly applied techniques (such as inter-trial coherence). It remains difficult to quantify differences between the two approaches (Bayesian vs frequentist) – for instance, the authors write that "these graphs [from Bayesian analysis] show a clearer structure than the corresponding ITPC analysis" without providing a quantification of the difference.

Together, this paper will be useful to the community, possibly opening up new ways of analysing phase-locked neural responses.

Reviewer #3 (Recommendations for the authors):

This paper proposes a Bayesian take on the inter-trial phase coherence (ITPC) used to estimate how consistent the oscillatory phase is across trials for a given condition of interest. For standard ITPC the statistical power of the comparisons on the group level is determined by the sample size of the dataset since estimates are derived by first averaging across trials to derive a single condition-level estimate per subject. The advantage of the proposed Bayesian approach is that the resulting model is more robust as it is estimated from the trial level without averaging. It also allows us to derive subject-level estimates (slopes) and explore subject-variable noise. The authors illustrated this by replicating the ITPC analysis from the paper by Burroughs et al. (2021a) using the Bayesian ITPC and demonstrating perceivable noise reduction in the resulting estimates across frequencies and topographical EEG plots. Another key advantage of this method, as illustrated by the authors, is the ability to generate stable estimates for much smaller EEG datasets. While the authors show that Bayesian ITPC can replicate the findings obtained with the standard ITPC, it is not clear what advantages the proposed Bayesian approach offers over other previously proposed methods that allow for trial-level modelling such as linear mixed effects modelling. Secondly, a broader and more accessible description of the steps of the model settings, estimation, and the derivation of the summary statistics should be provided to enable the reader to replicate this method for their own dataset

Abstract

1) lines 12-17 please consider re-phrasing as the message here is not very clear. Please be more specific (based on your analysis findings) what Bayesian approach to coherence contributes more than the traditional one? 'More descriptive' and 'data-efficient' are vague descriptions.

Introduction

2) Lines 26-44. Here to help the readers I would recommend communicating your main point early in the paragraph – that measurement of coherence is an important methodological tool in M/EEG research that is used to answer a wide variety of scientific questions, yet there is room for improvement in how ITPC is estimated.

3) Line 84 – 'this plots', instead of 'this graphs'

4) Lines 96-107 – the main message from this section is not clear. Do authors argue that in the per-electrode ITPC approach the Bonferroni correction for multiple comparisons precludes finding meaningful spatial patterns in the data? In such cases, Bonferroni is rarely used, and spatial cluster-based permutation is a typically used approach that is less conservative and allows the finding of significant clusters of spatially connected electrodes.

5) Lines 126-128 – please unpack a bit more what is meant by 'a better description of the data' and 'a narrative phrased in terms of models and their consequence'.

6) Line 161 – here you mean Figure 4?

Methods section

7) Authors provide a detailed explanation and mathematical descriptions for the distributions from which the phase data can be modelled, and parameters are sampled when building up a Bayesian model of the ITPC. The supplementary materials then detail equations behind the full model used. Yet from these two sources of information, it is challenging for the reader to reconstruct the set of steps authors took to derive the results they plot in Figure 5. If the aim of the paper is to have the reader use the Bayesian approach to ITPC for their own datasets a more accessible step-by-step description of the model estimation is necessary – from calculating participant and electrode slopes/estimates to averaging steps used to produce Figure 5. This can be done by expanding relevant sections in the Methods.

8) Other methods such as Linear mixed models that likewise allow trial-level analysis and model subject slopes have been broadly applied to the EEG data and also ITPC. To increase the contribution of this paper, authors need to outline and demonstrate analytically the advantages of the Bayesian approach over these other non-Bayesian methods.

Discussion section

9) The section Model design choices seem to belong in the Results and not the Discussion section.

10) The Data efficiency section is very helpful in demonstrating the advantage of the Bayesian approach for smaller datasets. This section can be expanded by demonstrating further key advantages of the Bayesian approach over other non-Bayesian methods that use a trial-level approach (as proposed in point 8).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Bayesian analysis of phase data in EEG and MEG" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewers 2 and 3 are satisfied with your revisions, however, given that eLife works on consensus and the fact that Reviewer 1 is not satisfied with a major concern of theirs from the first round of review, we ask that you directly address Reviewer 1's queries thoroughly. This includes those concerns regarding interpretability for experimentalists, and specifically, that you compare your method to the classic tests for steady-state responses as the Reviewer suggests. Please pay close attention to each of Reviewer 1's queries and address them in full.

Reviewer #1 (Recommendations for the authors):

1. The authors did not address my all my comments and I copied them here.

If the aim is to provide a more powerful test, it should be compared to classic tests for steady-state responses, such as the ones described in the following article.

Picton, Terence W., et al. "The use of phase in the detection of auditory steady-state responses." Clinical Neurophysiology 112.9 (2001): 1698-1711.

The current article is certainly not written in a way that can be understood by an experimentalist. It doesn't matter too much if the methods are hard to follow, but it does matter if no interpretable results are shown. For example, the authors argue that the topographic plots using the new method have a clearer structure than the traditional ones. As an experimentalist, however, I can't figure out which structure is clearer and why it helps to answer scientific questions.

2. I'm glad that the authors included a new dataset in the analysis. However, as an experimentalist, I still cannot see why the new method outperforms the traditional ITPC analysis in the newly added experiment. For the session "Case study – statistical learning for an artificial language", we need at least a few conclusions, explicitly stating whether the new method or the traditional method gives a more reasonable result and why.

3. Simulation is also important. However, I can't really understand the "Simulation study" section. What is exactly R1 or R2? Why do we care about the bias? A more helpful simulation is probably just to simulate the time-domain EEG signal (e.g., using sinusoids and noise) and demonstrate that the new method, e.g., can yield statistical significance with fewer subjects.

"We then use this modified model to generate fictive datasets with different numbers of participants and trials", but where are the results? It seems like Figure 11 does not show how the results change with the number of participants and trials.

For the new section on "Data efficiency", why just one dataset and why only 4 participants? Testing two datasets and all possible numbers of participants are minimal requirements. Also, as an experimentalist, I really cannot understand what is shown in Figure 12.

4. "the power is not a useful measure. Instead, the typical approach to frequency-tagged data for cognitive tasks is to use the inter-trial phase coherence." In fact, most of the studies cited in the introduction used power rather than phase analysis.

5. "The Bayesian approach is more descriptive than traditional statistical approaches: it is a generative model of how the data arises and each component is interpretable and informative about data characteristics."

It's great. But why is the method more interpretable? Could you please summarize it in a way that can be understood by experimentalists?

"It is also more data-efficient: it detects stimulus-related differences for smaller participant numbers than the standard approach."

How is this demonstrated in the two datasets? Is there a guideline about how many participants can be saved using the new approach?
