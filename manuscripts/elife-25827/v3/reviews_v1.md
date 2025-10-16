# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25827.023](https://doi.org/10.7554/eLife.25827.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Synaptic input sequence discrimination on behavioral time-scales mediated by reaction-diffusion chemistry in dendrites" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Frances K Skinner (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Paul Smolen (Reviewer #2) and Kim T Blackwell (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

While all of the reviewers felt that this was interesting and significant work, there was a clear consensus that several aspects of the paper were unclear and thus subsequently confusing.

Overall, it was felt that the author needed to expand on his explanations and descriptions in several places. The specific points that need expansion, revision and further explanations in the paper are:

1) the 4 models

2) Q equation has issues

3) sensitivity of the results

Besides this, the reviewers have various issues in their comments (details that seem to need fixing) that should be responded to (see below).

Reviewer #1:

This is an interesting theoretical, computational study that considers sequence discrimination at the level of the single cell (rather than networks) including slower timescales (hundreds and milliseconds and slower). Reaction-diffusion modeling and detailed multi-scale models are used to show attributes of recognizing input in the correct order and over scrambled input and background noise, as well as showing an effect on firing.

While interesting, the manuscript could be more fully explained and expanded in several places to help the reader fully grasp the situation. Also, various details seemed a bit strange to me, and further discussion on some points seem warranted. Specifics are:

1) The author gives the context of place cells (Figure 1), but it would be helpful to explain this a bit further I think. That is, each neuronal ensemble sends a projection to a dendritic segment etc. Should this be considered as a particular postsynaptic cell? Should the network context be ignored, is this on multiple segments of a given cell, cells in a network, or does it matter in the context, etc.? I realize that the focus is on the single cell, and perhaps it doesn't really matter overall for the work, but some consideration/description of this would be helpful to the reader in setting the envisioned context. This would be further helpful in the Discussion when timescales are estimated and discussed.

2) For Figure 2, the author could expand on his 4 models and molecules A and B and Ca – that is, a schematic of the overall relationship would be helpful. Perhaps some sort of simple MAPK pathway (generic as for the 4 models) could be illustrated? The author says "The results were as expected" (subsection “Reaction systems select for distinct speeds and length-scales of sequential input”) in referring to Figure 7 – expand on why this is please. Figure 3 process not quite clear to me – left x-axis 'sequence score' is obtained how? The color on the right is Q, right? – please label.

It was not immediately obvious to me how a Q of -0.001 would be obtained for the sequence given – please explain and/or demonstrate/illustrate more fully.

2-6 μm spatial intervals given in text but in figures, the high Q values (color) are at tens of μm – I think that I am missing something or perhaps confused.

3) Multi-compartment model details are specified as taken from mostly from Traub et al. 1991, but the reference is not listed in the bibliography. Potassium reversal potential of -15 mV seems a bit depolarized, and I assume 60 mV for resting is a typo (-60 mV?). 1 ohm.m2 is 1000mS/cm2 for Rm, and seems rather high? The values in Figure 7 to see effect in firing are even larger by a lot which is perhaps a bit concerning?

4) Does it matter that there is no Ih in the model, which is well-known to be non-uniformly distributed in pyramidal dendrites. Would this be expected to affect the results?

5) Subsection “Sequence speed selectivity scales with reaction rates and diffusion constants” – "As expected, we found that as the rates were increased…". Why? As there was not a complete explanation for the 4 models, this 'expectation' suffers here too.

Reviewer #2:

This is an interesting paper dealing with an important topic in computational neuroscience, sequence discrimination. But some important points need to be addressed. I am asking for a little extra work – not an exhaustive analysis – in only one of my comments, comment 1, given that parameter sensitivity analysis is a common, substantial concern in all modeling studies.

1) Some parameter sensitivity analysis should be done for some of the key results. For example, in Figure 2, rightmost column, it appears that parameter values may be "tuned" to be close to bistability, so that stimuli can give relatively long, but eventually declining, response plateaus. Although, the numbers in the equations above do look pretty generic. Similarly, for Figures 2C and 2D, and other figures that show strong sequence selectivity, how dependent is this selectivity on values of rate constants and other parameters? I'm not asking for an exhaustive analysis, but some degree of analysis and discussion of sensitivity should be given for a few of the key results. For example the sensitivity of the results of Figure 6G, which presents selectivity for the most realistic model, should be discussed.

2) The selectivity criterion in Equation 3 cannot be correct as defined. The quantity Q, from Equation 2, is only related to the input, not the response, so Eq. 3 is also not related to the response. But of course selectivity, as plotted in the right column of Figure 3 and later, is related to the response. In Eq. 3, should Q be simply replaced by the average or maximum of the variable A, and in later cases should A be replaced by MAPK-P?

3) In the subsection “Sequence speed selectivity scales with reaction rates and diffusion constants” the author describes how by varying rates he can achieve good sequence selectivity over a broad range of time intervals, and in the Introduction it is noted that such time-invariance is a "desirable feature". But, for a single neuron or dendrite, the rate constants are presumably fixed, or at least do not vary in anticipation of stimulus time scales? So, I don't see how to get time invariance in a single neuron. So then, how does the author envision getting time invariance in a real neural network? Does he envision different neurons in the network will have different parameters so that they will respond to different time scales? These issues should be addressed in the Discussion.

4) For the channel modulations that underlie the simulations of Figure 7, it is never discussed whether these modulations would result from activation of the MAPK signaling pathway simulated in the rest of the paper. The channel modulations are imposed ad hoc. It would be good to connect these portions of the paper, if not by simulations of MAPK effects on channels, then at least by discussing to what extent some or all of these modulations are thought to be downstream of MAPK activation and are a plausible readout or result of the sequentially amplified activation of the MAPK pathway simulated previously.

5) In the Discussion, large numbers are given for how many sequence discriminations a neuron can perform per second and how many sequences a neuron can discriminate. But I am skeptical of these estimates because no discussion is given of what it means operationally for a neuron, a cell, to "discriminate" a sequence. It seems to me that a change in electrical firing rate or spike timing is needed to say a neuron has discriminated a sequence. Or, a change in synaptic plasticity. A transient biochemical response in a dendrite, just by itself, doesn't seem to me sufficient to constitute "discrimination" by the neuron. These caveats should be noted and discussed.

6) In the Methods, it is stated with regard to the simulations of Figure 7 that we ran the model for 1 second to let the cell settle, before modulating channels. But clarification is needed since 1 second is not enough to allow simulated biochemical pathways to come to equilibrium in the models. Especially in the realistic simulations of Figure 6, how much simulated time was allowed from when biochemical variables were initialized to when stimuli were given.

7) Figure 4F and 4G is a particular instance of the sensitivity issue in comment 1. Here a 20% change in stimulus amplitude leads to a very large change in the selectivity pattern. Is this sensitivity of pattern to stimulus amplitude typical for the models?

Reviewer #3:

The research addresses the important problem of pattern recognition by neurons. Specifically, what mechanisms allow a neuron to discriminate sequence a-b-c from c-b-a, where a, b, c are each a different synaptic input. The ability to discriminate temporal pattern is more difficult than discriminating which synaptic inputs are present. This issue has been addressed in specialized, direction selective cells, but the more general problem has not been investigated. A major strength of the manuscript is that the authors use both a simple, analytical model as well as biophysically and biochemically realistic neuron models to demonstrate principles underlying the results and to demonstrate the plausibility of neurons in tissue accomplishing temporal discrimination. Using the simple models, the author analyzes and presents the critical factors constraining sequence specificity. By using realistic model, the author demonstrates that sequence specificity can be implemented by neurons in tissue, since these simulations include background synaptic inputs, including theta modulated GABA input. For the most part the results are quite clear. There are only two aspects that need better exposition.

1) Though the difference in selectivity is apparent in Figure 3, it is not clear what exactly is being plotted. I understand using R^2, which gives values between 1 (i.e., good) -1 (i.e., bad) for Q if m=1, but I don't understand why add the term m into Q Equation 2. In addition, why does Equation 3 use Q as the selectivity measure. The first time I read this page, I thought that Q was the selectivity measure. Then, I realized that Q was just a convenient way to obtain a monotonic x axis value, and that the important information was in a graph of A versus Q. But then Equation 3 claims to plot a selectivity value which is a function of Q, not A. A more detailed illustration of how values in Figure 3 are obtained (one value from right side graph and one value from left side graph) would be quite helpful. Also, where does the temporal interval come into this equation?

2) The results in the subsection “Local dendritic channel modulations may influence cellular firing”, describing the effect of channel modulation need a bit more explanation. In particular, it is quite surprising that an increase in leak conductance would increase firing rate. Since leak channels are typically potassium channels, I would expect an increase in leak conductance to not only make the cell less sensitive to depolarizing current, but also hyperpolarize the branch a bit, unless Eleak is rather depolarized. An intuitive explanation for this result would be helpful. Also, I don't understand how these manipulations are related to sequence discrimination. Wouldn't these channel modulations change firing rate for all sequences? Or perhaps the neuron can better discriminate the correct from incorrect sequence?
