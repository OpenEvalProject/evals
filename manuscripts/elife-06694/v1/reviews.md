# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06694.039](https://doi.org/10.7554/eLife.06694.039)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Dynamical feature extraction at the sensory periphery guides chemotaxis” for consideration at eLife. Your article has been favorably evaluated by Eve Marder (Senior editor) and three reviewers, one of whom, Ronald L Calabrese, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The authors present an extraordinarily thorough electrophysiological and behavioral analysis of the chemotaxis in Drosophila larvae in natural odor gradients, defined odor gradients, and optogenetically induced fictive olfactory gradients. These analyses relate OSN activity empirically determined to behavior using a model of sensory transduction and a GLM relating neural activity to the probability of turning. They also create closed loop virtual reality environments to test the effectiveness of their models. They conclude that OSN activity accurately predicts turning probability by a simple linear transform and thus OSN spiking dynamics in odor gradients are key for understanding chemotaxis.

The major biological findings are:

1) Real odor landscapes even in a controlled chamber are complex and they can be described quantitatively.

2) OSN activity in real odor and in fictive odor landscapes can be assayed and then modeled (albeit in an ad hoc manner) so that OSN activity can be accurately predicted in both real and fictive odor landscapes.

3) Fictive controlled odor landscapes can be navigated in a chemotatic way and turn probability can be accurately predicted (using the OSN model and a further ad hoc model) based on OSN activity. Fictive odor landscapes are elegantly designed to extract real behavioral principles. For example a ‘well’ landscape shows that a precipitous drop in predicted (and confirmed) OSN activity induces turns.

4) When real odor landscapes are chemotaxed, then turn probability can be accurately predicted based on predicted (and confirmed) OSN activity.

The major technical innovations are:

1) Real odor landscapes can be calculated based on diffusion equations with sufficient accuracy to extract real odor dynamics for a moving maggot. Confirmed by IR spectroscopy.

2) It is possible to move between the liquid phase and the gas phase when experiments demand it by matching liquid phase and gas phase OSN activity.

3) Identical fictive and real odor waveform leads to measureable differences in OSN activity owing to adaptive processes in the OSN during odor stimuli.

4) Ad hoc models of OSNs can be constructed that capture their essential activity to real and fictive odor stimuli.

5) GLM ad hoc models can capture the relationship of the ONS activity to turn probability, and used as a tool to understand real chemotaxis in an odor gradient.

6) Tracker technology can present freely moving maggots with fictive odor gradients to determine turn probability.

At the paragraph level the writing is clear and the paper is thoroughly illustrated, but finding the above major contributions amid the voluminous data (especially supplemental data) is difficult owing to the overall structure of the paper. Moreover the Discussion seems to focus too much on the OSN model and its implications at the expense of the biological insights for chemotaxis. The authors must be at pains to bring out these contributions in the way they structure the paper and in Abstract and Discussion. The logical flow of the techniques (tool development) and experiments and the conclusions must be made more apparent. One thing that will help immensely with flow will be to delete some of the supplemental figures on tool development or to place the call outs in Materials and methods (simply refer—no figure call outs—to Materials and methods in the Results): Figure 1–figure supplement 1, 2, 3 in Materials and methods; Figure 2–figure supplement 1 can be eliminated, as it is a negative result; Figure 2–figure supplement 2 can be eliminated; Figure 4 can be made into a supplemental figure and placed in Materials and methods; Figure 5–figure supplement 1, 2, 5 in Materials and methods; Figure 6–figure supplement 1 eliminated; Figure 8–figure supplement 1 in Materials and methods.

There are some technical concerns that must be addressed:

1) Statistics. In Materials and methods add a statistics section and write a clear description of the statistical tests used. This is somewhat scattered throughout Materials and methods now. Much of the statistics is in tables and in the figure legends and needs to be made more apparent. Figures 6F and 8D, E present critical statistical tests that are based on a subset of long run trajectory. The rationale and validity of excluding short runs need to be made more apparent.

2) There is some concern about whether parameters for the models were fixed at some point or whether they were changed with each experiment. One possible reading is that the parameters of Table 1 and Table 3 represent fixed parameters based on the ‘training’ of the associated figure and that subsequent uses of the models used these fixed parameters. The authors must make this explicit. If parameters, were changed with each new experiments then this would seriously diminish the value of the modeling. Specifically, the authors' need to address the question of whether models that were trained on a set of input–output pairs generalize to an equivalent set of pairs that were not in the original training set.

3) There is the concern that the sensory neuron model is fitted to events on a time scale of less than 10 sec (Figure 2, 3, 4, etc.), whereas the dynamics of chemosensory stimuli during behavior in an odor gradient occur on a time scale of about 30 sec. The authors should acknowledge in text any difference in time scale and dynamic range between real odor time courses and the input domain over which the model was fitted.

4) The odor and channelrhodopsin (ChR) experiments are done in Or83b mutant background. Thus the dynamics of Or42a-ORNs can be more easily related to behavior in an otherwise silent olfactory system. Will the same be the case in the presence of spontaneous spiking of other ORNs? Another important issue with doing behaviors in a completely silent system is that local interaction at higher levels of olfactory circuits would likely be diminished if not completely absent. Therefore OSN activity-to-turn probability transformation determined might not be representative of that in the WT animal. The authors must address this limitation forthrightly in Discussion.

5) The logit transform of the equation in Figure 5D caused some reviewer confusion; here is a case where some explanation in the text is needed and not just a reference to Materials and methods.

The results presented and tools developed have important implications for behavioral analysis of chemotaxis in animals and set a standard for further mechanistic studies in this important model system. Moreover, the approach used here can be a model for analyses of sensory-motor transformations in other systems.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Dynamical feature extraction at the sensory periphery guides chemotaxis” for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and one of the original reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

This revision meets the major expectations set down by the previous reviews. The flow of the paper now is greatly improved. All the main technical points have been resolved and the new statistical section adds significantly. There are a few minor points that should still be considered.

1) The authors belabor the description of Figure 3. The figure itself has too much data (3D and 3E are the only panels that are essential.). Emphasize the main point of the figure: the sensitivity of ORNs to concentration slope. Between the subsection “Characterization of the features encoded by a single larval OSN stimulated by controlled olfactory signals”, where you have concluded that linear filters won't work, and the passage, in the subsection “Phenomenlogical model of the olfactory transduction cascade”, where you start with the dynamical system approach, you lose momentum. The authors can do a better job of explaining how the qualitative observations in Figure 3 led them to the model they built in Figure 4.

2) In the Discussion, or when the paper is cited, it might be appropriate to compare the approach of Nagel and Wilson, 2011.
