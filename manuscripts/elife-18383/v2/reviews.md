# Peer review - Round 1

Editors:
- Naoshige Uchida, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18383.026](https://doi.org/10.7554/eLife.18383.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Asymmetric Effects of Activating and Inactivating Cortical Interneurons" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Naoshige Uchida (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Maria Neimark Geffen (Reviewer #2); Andrea Benucci (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors examined how activation and inactivation of specific types of interneurons in the auditory cortex affect gain, frequency tuning, or information content of tone-evoked responses in excitatory neurons. The authors found that activation of interneurons did not produce cell-type specific effects, but inactivation caused cell-type specific effect in all three measures. The authors also include a simple multilayered network model to show how subtraction and addition could produce these asymmetrical effects.

All the referees found that this is a timely and important study demonstrating some caveats in interpretations of experiments involving transient inactivation. The manuscript is well-written and the authors make careful discussions.

While all the referees were enthusiastic, there are some issues to which we would like to see your response. We therefore would like to invite you to revise the manuscript.

Essential points:

1) One main issue that was common in the reviewers' comments is considering the normal operating regime of neural circuit to design and interpret experiments. First, can the authors mention how PV and SST interneurons fire in a normal condition (reviewer #1, point #1)? If the authors have relevant data or if there are some literature on these, it would be great to describe them more clearly. Second, it seems that the authors have conducted a number of analyses to control for varying effects of optogenetic stimulation on different neurons during the tone responses. How do the effects of optogenetic stimulation on spontaneous activity compare to effects on tone-evoked responses? Would it be possible to quantify tone response magnitude rather than firing rate, which may be the more relevant quantity used by the brain to make behavioral decisions (reviewer #2, point #2)? Related to this issue, have the authors looked at the effect of varying intensity of laser stimulations? Third, it appears that one way to look at the experiments is that they are testing the dynamic range at which the neural circuits operate in a linear regime with regard to gain, frequency tuning, or information content of tone-evoked responses (reviewer #3, point #2). More detailed comments on each of these points can be found in the individual referees' comments appended below. Based on these, please make coherent discussions on the dynamics of neural circuits, model, and the experimental results.

2) Please quantify the specificity of Arch/ChR2 expression in SSTs (reviewer #2, point #1).

3) Please clarify how the authors selected neurons for analysis. Can the authors select putatively pyramidal or wide-spiking neurons for analysis (reviewer #1, point #1)?

Reviewer #1:

This study compared the effects of optogenetically inactivating versus activating specific types of inhibitory interneurons, pervalbumin (PV)- or somatostatin (SST)-expressing interneurons, on the tuning curve of neurons in the primary auditory cortex in mice. To quantify whether these manipulations caused divisive or subtractive changes in tuning curves, responses in light-on trials were regressed by responses in light-off trials. Divisive changes were detected as a significant change in slope whereas subtractive changes were detected as a significant change in intercept. Furthermore, the authors compared the ability of each neuron to transmit stimulus information using mutual information between the two conditions (activation versus inactivation). The authors' results showed that activating and inactivating specific interneurons often caused inconsistent results across these two conditions. The authors further explored potential mechanisms underlying these discrepancies using a simple network model, suggesting that some nonlinearity such as flooring of firing rates may explain these discrepancies. The authors discuss other potential caveats of their and other experiments in Discussion.

Although optogenetic as well as other manipulations such as pharmacological, pharmaco- and magneto-genetic manipulations plays critical roles in elucidating the role of specific neuronal populations, various caveats in interpreting these results have not been fully appreciated. This study adds a timely and important warning to the neuroscience community. The results are interesting and presented clearly. Although there are some points that need to be clarified, I believe this study warrants publication at eLife.

1) How do PV and SST neurons respond to different stimuli with or without optogenetic manipulations? What are the time courses and what are their tuning curves of these interneurons during auditory stimulation? These types of information are very important in designing optogenetic stimulation parameters (such as the timing and magnitude of manipulations, as the authors discuss). Also, one important assumption of these experiments appears to be that each neuronal population shows homogeneous (or similar) responses across stimuli and neurons (as neurons were homogeneously manipulated by optogenetics). Is this true to begin with?

2) It is important to know how the authors selected neurons for their analysis (beyond focusing on those that changed their firing). Ideally, the analyses should be separately performed for putative pyramidal and interneurons, and further, PV and SST neurons. Even though the classification might not be perfect, can the authors analyze subsets of their data that belong putatively to specific neuron types?

Reviewer #2:

In this important, timely, and elegant study, the authors demonstrate that activating and inactivating two different interneuron subtypes in the auditory cortex has asymmetrical effects on gain, frequency tuning, and information content of neural responses. Specifically, that optogenetic activation of interneurons did not produce cell-type specific effects on gain, frequency tuning, or information content of tone-evoked responses in excitatory neurons, but optogenetic inactivation of interneurons caused cell-type specific effect in all three measures. The effects on putative excitatory neuronal responses to tones were multiplicative with inactivation of SOMs and additive with inactivation of PVs, whereas activation of either PVs or SOMs led to a mix of subtractive and divisive effects. The latter result is consistent with a recent paper by the authors (Seybold et al., Neuron, 2015), whereas the former is novel to this manuscript. The authors also include a simple multilayered network model to show how subtraction and addition could produce these asymmetrical effects.

I have the following suggestions:

1) The evidence for Arch/ChR2 expression in SSTs seems to be missing. While Arch/ChR2 does not co-localize with PV, that does not necessarily mean that it is expressed in SSTs, and exclusively in SSTs. Quantifying this is essential to interpreting the results from the paper, which rely on the comparison between the effects of activating SSTs and PVs. Please provide a picture of the stain for somatostatin and demonstrate co-localization of Arch and ChR2 expression and som. Please provide quantitative data for co-localization (specificity and efficiency).

2) It seems that the authors have conducted a number of analyses to control for varying effects of optogenetic stimulation on different neurons during the tone responses. How do the effects of optogenetic stimulation on spontaneous activity compare to effects on tone-evoked responses? Would it be possible to quantify tone response magnitude rather than firing rate, which may be the more relevant quantity used by the brain to make behavioral decisions?

3) The model is intuitive and easy to understand. However, it seems to be an oversimplification to exclude excitatory/inhibitory dynamics, and it would be beneficial to make the model more biologically relevant by examining rate dynamics for excitatory and inhibitory populations. Optogenetic manipulation of PVs and SSTs is represented as a multiplicative or divisive shift in the input units. It would be interesting whether this effect can be modeled through rate equations in which the optogenetic inputs would be represented as enhanced drive to inhibitory neuronal populations. This would also be interesting to examine w/r varying light intensity or varying magnitude of the effect of laser on spontaneous activity.

Reviewer #3:

The paper "Asymmetric Effects of Activating and Inactivating Cortical Interneurons" by Elizabeth Phillips and Andrea Hasenstaub emphasizes how the results of optogenetic activation and inactivation of interneurons are difficult to relate to the "natural" computations implemented by the population they belong to. In my view this is a fair warning worth disseminating among the optogenetic community. The manuscript is easy to read, and the data nicely presented. However, I have three concerns:

1) The main motivating argument of the study, that optogenetic activation is commonly believed to strengthen computation and inactivation to weaken it, is questionable. I think there is a widespread understanding that inactivation at most can probe the 'necessity' of a population in a given information-processing context, while activation can probe the 'sufficiency'. In my view, a preferable motivation would be the one presented in the Discussion (last paragraph) about the use of optogenetics to characterize linear regimes of information processing within non-linear networks.

2) The demonstration of "separable effects" or "asymmetric results" following activation or inactivation of interneurons, if taken literally in its generality, is a fairly well-understood concept. Instead, I believe the authors wanted to focus on the role of interneurons within physiological dynamical ranges (e.g. away from epileptic states, when completely silencing PV+ interneurons, or from an unresponsive network, when strongly driving PV+ interneurons), and on how optogenetic perturbations can shed light onto the linearity (or lack of thereof) of gain changes, tuning, and information content of the network. I would make this point more explicit.

3) A significant amount of (similar) data and analyses shown here have already been presented in their Neuron 2015 Viewpoint paper. Figures 1–8 in that paper cover most of the results shown here for optogenetic activation of SST+ and PV+. Similarly, a key point presented here regarding the subtractive suppression and its flooring effect (Figure 7M) was already made in Figure 8K in the 2015 paper. The novelty of this work is about the inactivation experiments, and I think this should be more explicit.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Asymmetric Effects of Activating and Inactivating Cortical Interneurons" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Naoshige Uchida (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Maria Neimark Geffen (Reviewer #2); Andrea Benucci (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have been responsive to the referees' comments, and overall the manuscript has been improved significantly.

There are some issues that need to be revised or clarified. Please respond the comments appended below. These issues are relatively minor.

Reviewer #1:

The authors have performed new analyses and modified the manuscript. These changes have improved the manuscript significantly, and addressed most of my concerns.

Reviewer #2:

The authors did a good job addressing the concerns of the reviewers and the manuscript is much improved.

Reviewer #3:

The authors have addressed my concerns and overall the manuscript has significantly improved. The concern on the linear/non-linear operating range has been nicely addressed with the new Figure 8, describing "consistent or paradoxical" effects depending on baseline activity. Although I could grasp the general idea behind this model simulation, it was not easy to find the exact details. Apologies if I missed it, but for example I could not find the difference between moderate-high-low activities (e.g. a fractional change?). A few more details to allow for reproducibility of this simulations would be helpful.
