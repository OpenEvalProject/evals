# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18607.015](https://doi.org/10.7554/eLife.18607.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cellular and Neurochemical Basis of Sleep Stages in the Thalamocortical network" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Ronald L Calabrese (Reviewer #1), is a member of our Board of Reviewing Editors and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Paul Garcia (Reviewer #2); Miles Whittington (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this very interesting study that combines computational modeling and some in vivo recordings of brain activity during sleep and wakefulness and under ketamine anesthesia, the authors propose a comprehensive model of how major neuromodulators may control sleep states and their transitions in mammals. The model is grounded in previous experimental evidence and covers the major neuromodulators ACh, GABA, and HA. They show how these modulators might synchronize the spindle (N2) and slow oscillations, SO, (N3) states, as well as REM. Using ECoG recordings from humans and LFP recordings from cats and mice, during NREM sleep they show that the power of spindle and SO is negatively correlated in human and positively correlated in cats and mice, and explain this discrepancy by the differences in the relative levels of ACh. They also explore similarities and differences between SO during N3 and ketamine anesthesia and explain them in terms of influences of ketamine on neuromodulator levels and effects. The study identifies potential intrinsic and synaptic mechanisms through which neuromodulators acting in combination may mediate transitions between sleep stages. These findings should be of wide interest to the sleep, and anesthesia communities and to those interested in coordinated whole brain activity.

Essential revisions:

There are some major concerns about claims but overall this appears to be a strong study of general significance.

1) The authors have gone too far when suggesting that they are modelling the sleep-related effects of the neuromodulators they have chosen. The authors are really basing their conclusions on an oversimplified (and under-developed) link between ACh and effects on membrane currents. Their models do show remarkable state changes with manipulation of the 4 main parameters (K-leak, Ih, GABA, AMPA) and these finding are both interesting and challenging to the field – but the relation back to ACh and HA is not as strong as they imply. There are many precedents for ACh and HA having the opposite effect on the main model parameters on certain cell subtypes cf. the ones they use.

The authors should clarify that they are making a selection of potential modulator effects, and in Discussion suggest this MAY relate to known endogenous brain-state modulators like ACh, Histamine (and many others).

Alternatively the authors can revisit their model and represent more accurately the known effects of HA and ACh on each of the 'loose' cell types included in the model.

2) A similar concern applies to the handling of data gathered with ketamine anesthesia. The authors attempt to mimic ketamine in their model by decreasing NMDA's influence – but ketamine is a promiscuous molecule that has influence on a great number of channels. Additionally, the unconsciousness produced by the "dissociative" anesthetic, ketamine, has a very different phenotype than that of propofol or isoflurane which more or less produce a quiescence resembling sleep. As opposed to these GABAergic anesthetics, ketamine does not activate the sleep nuclei of the hypothalamus (VLPO), does not depress thalamic activity, and activates wake-promoting nuclei in the brain stem. The adjunct agent used in their in vivo experiments (xylazine) does on the other hand promote sleep, but does not do this through NMDA antagonism. Therefore the specificity of their model is really in question. George Mashour has done work on ketamine and his work might be better referenced. http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4076669/

Further, we would expect that an increase in inhibition in the model would produce slow oscillations similar to sleep. This model state could be compared to in vivo data using propofol or isoflurane. Perhaps, this model is "tuned" to produce these stable oscillations in a variety of different parameter regimes – but as mentioned in the expert reviews (Reviewer #2), without an evaluation of the stimulation protocols it is difficult to determine what is a network effect vs. a reflection of the periodicity already present in the stimulation.

The expert reviews of reviewers #2 and #3 are appended to aid in the revision.

Reviewer #2:

This manuscript reports the results of a computational model of sleep cycling based on variations in neurotransmitters. The model was also compared to neuronal oscillations during sleep using human, cat and mouse datasets. The main conclusion is that the initiation of the oscillatory pattern indicative of N2 sleep can be simulated by a decrease in histamine and acetylcholine. A further decrease in acetylcholine can also explain a transition to deeper sleep. In general, this model contributes much to our understanding of the neurochemical basis of sleep macroarchitecture. Additionally, the results challenge theories that increases in the inhibitory neurotransmitter GABA mediate transitions among sleep stages. Although some of the conclusions need to be amended and there are several places that need some grammatical corrections, there is much to be admired in this paper. However some of the grammatical errors and non-sequitors (non-explored ideas) make me concerned that it was hastily prepared.

Summary:

– Some parts of the summary are awkward in regard to sentence structure and punctuation. The second sentence does not sound like proper subject verb agreement, and the third sentence requires the word and between the two subjects to make sense. Α/theta bursts are mentioned in the Summary but not emphasized in the paper (previous version?) please remove.

Introduction:

– First sentence of second paragraph should be reworded so characterize is not repeated. The first sentence of the third paragraph should start with: "Neuromodulators".

Results

– The TC stimulation is not represented in Figure 2. This input is also not described in the methods, given the strong excitatory connections between thalamus and cortex the nature of the stimulation ("simulating sensory input") could be driving the oscillations and must be included to evaluate the main conclusions of the paper.

– Why did they examine such a large frequency range to evaluate phase-locking? When the connections are not completely known (in vivo recordings) phase-locking among narrow frequency bands (especially among specific regions, e.g., thalamus and cortex) is much more important for synchronization. Very little of the quantitative results rely on phase-locking.

– Why is ketamine compared to SWS? Others report it as sharing similarities with REM. Propofol or isoflurane anesthesia would be a better comparison.

Methods

– Extrasynaptic and Intrasynaptic GABA concentrations are mentioned but not explored in the paper, please remove (unless added to discussion as to a potential limitation of the model).

– Network description: radius is not defined explicitly.

– The in vivo description mentions non-anesthetized cats and ketamine is given?

Discussion

–- Much of the Discussion can be considerably shortened.

– The Discussion does not adequately address other potential influences on spindle power (e.g., age and cortical volume).

Reviewer #3:

This is a very interesting paper that uses a fairly detailed computational model, constrained by experimental observations in a variety of species, which is used to demonstrate the dependence of sleeps stage on a variety of network and intrinsic cell properties (leak current, AMPA, GABA, I(h)). The paper extends the findings to link sleep stages to two main neuromodulators known to be involved in controlling sleep – Ach and Histamine.

In general the paper is well written and the data beautifully presented. I very much liked the demonstration of different sleep stages with different intrinsic properties but it would have been good to refer to the very detailed model of Hill & Tononi which, a while ago, came to very similar conclusions.

My only major problem with the manuscript comes from the attempt to relate the model parameter changes to histamine and Acetylcholine. I think a bit more detail and biological realism needs to be included here. For example, Ach is stated to affect AMPA-mediated transmission and leak current. Of the parameters used to construct the model cells it also affects Km and GABA release. Reading the methods it seems Ach was modelled as a scale factor for all intrinsic and synaptic properties – but this scale factor was increased for decreased Ach levels. This means, for example, that properties shown not to be affected by Ach were affected in the model, and properties of Ach well documented (such as depolarisation of main interneuron subtypes) were omitted or modelled conversely.

On a similar note, it is not clear how the 2 modulators chosen fit with the GABA levels used. There is a wealth of evidence linking Ach and Histamine to GABA release and postsynaptic effects – some which fit the basic hypothesis the authors propose (decreased Ach, increased GABA release), and some antagonistic to it (increased histamine, increased tonic GABA). This could be clarified with a more rigorous modelling of the known effects of the two agents to the conductances used in the model. If no changes in sleep stages are seen then this would provide evidence for an involvement of the other major neuromodulators involved in sleep not considered here.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Cellular and Neurochemical Basis of Sleep Stages in the Thalamocortical network" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor), a Reviewing editor, and two reviewers.

The reviewers consider the manuscript to be much improved. There is only one minor issue that you may want to address before final acceptance, as outlined below:

Figure 1C and D Vertical axes might be clearer if they read "Normalized Conductance (%)" It should be obvious they are normalized to the Awake condition by the graph.

Reviewer #2:

This is a re-submission on a computational model of transitions among sleep stages that is firmly based in neurophysiology. The model is compared to neurophysiologic recordings from LFP records obtained in animal models and human ECoG data. Finally, the model's predictions are tested with simulations designed to mimic propofol anesthesia. This revised manuscript has much improved readability in both the precision of writing and clarity of thought. The main conclusions are that a reduction in acetylcholine and histamine levels in the thalamus corresponds to N2 sleep, characterized by spindle activity. And that an increase in GABA alone does not produce the oscillations characteristic of N2. The experiments with propofol anesthesia demonstrate this nicely. The model also predicts that reduced cortical acetylcholine influences the transition to N3 sleep. Overall, this is a nice contribution to the sleep and anesthesia literature.

Reviewer #3:

This one of the best, most comprehensive revisions of a paper I have seen. The authors have taken on every major comment and provided a great deal more clarity, focus and detail. I have no hesitation in recommending it for publication now.
