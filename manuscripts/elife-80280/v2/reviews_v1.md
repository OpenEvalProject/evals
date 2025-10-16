# Peer review - Round 1

Editors:
- Kristine Krug, https://ror.org/00ggpsq73 Otto-von-Guericke University Magdeburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80280.sa0](https://doi.org/10.7554/eLife.80280.sa0)

This important study investigates distributed neural coding across the three brain areas MST, 7a, and dlPFC in monkeys carrying out a novel behavioural paradigm with a naturalistic closed action-perception-loop developed by the same group previously. The convincing model-based analysis discerns potential influences (e.g. task variables, hidden variables) on firing rates and supports the claim of task-specific sub-networks being formed. The authors provide an important first step to unravel potential drivers of dynamic activity in distributed networks during recurrent action-perception-loops, which should be augmented by future analyses of, for instance, the contribution of changing visual input, especially as the recordings stem from areas involved in processing optical flow, and of signals across different circuit elements like cortical layers.


---

# Peer review - Round 1

Editors:
- Kristine Krug, https://ror.org/00ggpsq73 Otto-von-Guericke University Magdeburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80280.sa1](https://doi.org/10.7554/eLife.80280.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Coding of latent variables in sensory, parietal, and frontal cortices during virtual closed-loop navigation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Marieke Schölvinck (Reviewer #2) and Sujaya Neupane (#3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this letter to help you prepare a revised submission.

Essential revisions:

1) Heat maps of preferred angle and distance in Figure 3 must be cross-validated across trials to show data reliability. Maybe the authors have done that and these are cross-validated plots. If so, it is not mentioned in the methods anywhere. Please verify the ordering of preferred angle and distance hold up with cross-validation. One can get a spurious, evenly tiled coding of any continuous variable if one takes a random matrix (say mean FR x variable value), normalizes each row (FR) and sorts the column by peak location (i.e. preferred variable value) for each row.

2) We are a bit confused by the distribution of preferred latent variables (Figure 3). For e.g. travelled distance and distance to target are anti-correlated. Isn't it trivial that the preferred coding would appear bimodal across a neural population if some neurons are coding for one and some for the other? For a travelled distance coding neuron, there is nothing to code at the onset since distance travelled is 0 and vice versa for distance to the target coding neuron at the offset.

Related to #2, it would be helpful to see PSTH examples of single neurons that code for travelled distance and those that code for distance to target. PSTH would be obtained by averaging across trials, binned over a range of trial-lengths (e.g. bin1: short trial length, bin2: medium trial length, bin3: long trial length). We would expect clear differences in firing rate at the onset for distance to target coders and at the offset for travelled distance coders. It is difficult to see this in the presented rasters, although according to P-GAM results, that should be the case.

3) It would be helpful to provide a few examples of LFP traces and their filtered form along with spike times to appreciate the phase modulations apparent in their statistical modelling results (Figure 2F).

4) Tuning strength.

From the manuscript it is difficult to judge how representative the different neuronal populations for each area are and to what extent their selectivity differs. The analysis and it variables are quite complex to follow. It would be helpful for the reader to understand how some of them relate to more traditional measures. It is great that the focus on single neurons allows this comparison.

What does "tuned" in this context mean in terms of strength and selectivity?

How many neurons would pass a minimal response criterion like 10 spikes/s. Would these show stronger tuning or correlations?

Figure 2E: "E. Responses from an example MSTd, 7a, and dlPFC neuron (black), aligned to temporal task variables (e.g., time of movement onset and offset), or binned according to their value in a continuous task variable (e.g., linear velocity)." It would be helpful to give the x-axis for each line for the reader to be able to ascertain what the nature of the scale and the range of variables are over which the firing rate changes are depicted.

Could the authors derive from their data one of the traditional measures used for MST, like a direction tuning index? A direct comparison with previous studies could help understand the nature of the sampled pool, particularly (but not exclusively) for areas when smaller neuronal samples, like MST.

5) Eye movements and visual input.

Another issue is the extent that it seems difficult to distinguish the effect of eye position from that of the background stimulus flow patterns, which of course must differ in direction and element size when animals fixate at different locations on the screen. To what extent was this visual input to neurons correlated with "latent variables" like latent distance and angle to target (latent spatial goal)?

In order to dissociate the contribution of eye position and task from visual input, do the authors have data on a passive viewing control condition, in which the animal fixates and the visual pattern is played back to animals exactly as if in an active one? How do neural responses compare across the three areas?

Could the authors discuss in the paper how the visual input is (or not) included in the model?

6) MSTd and dlPFC coupling.

a) As the animals were head-fixed, eye position would compensate in some cases the animals might have moved its head position (for instance to keep track of the target). Both, MSTd and dlPFC encoded eye position. Could the close coupling of MSTd and dlPFC be linked to this element of the task?

b) The authors claim that areas MSTd and dlPFC form a functional sub-network together, on the basis of similarity in the fractions of neurons tuned to certain variables, and the distribution of the preferred value of some of these variables. However, the fractions of neurons tuned to the latent variables in MSTd and dlPFC (see Figure 2F) are actually quite different. Perhaps the authors could comment on this.

c) When there was stronger MSTd-to-dlPFC coupling and better tracking of the hidden firefly with the eyes (Figure 5B), was the performance of the monkey also better (i.e. more hits)?

7) Sampling of areas.

a) Area 7a was exclusively sampled with chronic rather than moveable probes. It has also the largest number of "single units".

To what extent are these single units independent?

Could a sampling bias in these probes (part of 7a; layers) affect the results, especially when it comes to coupling. Please include in the discussion.

b) The number of recorded neurons in the three areas differs greatly: 231 units in MSTd, 823 units in dlPFC, and 3200 units in area 7a. Yet many conclusions in the paper rely on neuronal numbers: the fractions of neurons tuned to certain sensorimotor and latent variables differ between the areas, the variables explaining the firing rates cluster differently in the neurons of the three areas, and both the coarse LFP connectivity and the fine unit-to-unit coupling within areas differ. Especially the clustering results might depend on the number of recorded neurons: the fact that almost all MSTd and dlPFC neurons are categorized as belonging to the same cluster, whereas the area 7a neurons appear in three distinct clusters, could be caused by the much larger number of recorded neurons in area 7a. Also unit-to-unit coupling is more likely to show up in the data with a much larger number of recorded neurons. The data could be corrected for these differences in number of recorded neurons.

8) Lateralisation.

To what extent played the lateralization of the recording and task a role for neuronal response? This applies relative to brain hemisphere, body and eye position? Where in each monkey did the recordings take place? Which hand(s) did each monkeys use for the choice stick?

How was the lateralisation included in the model?

Please comment with regards to responses in MST, 7A, and dPFC and add information to the manuscript.

Specifically, it is unclear from Suppl Figure 1 whether within a particular monkey, some recording sites were interhemispheric, or whether within one monkey, all recordings were done in the same hemisphere. This of course has significant consequences for the effects of ongoing LFP and unit-to-unit coupling.

9) Data fed into the P-GAM model.

a) The P-GAM model is a great analysis tool for these kinds of data. However, the variables that the authors put into it are conceptually very different from each other. There are purely external task variables such as target onset and offset, latent variables such as distance to target that require knowledge of one's own position in space, and purely internal brain dynamics variables such as coupling to the LFP in another area. In that light, the finding of 'many variables contributing to the responses' is not surprising; all neurons in the brain are probably influenced both by external variables and internal brain dynamics. Maybe the authors could comment on the different nature of their variables and how that impacts their results.

b) Given that the sensorimotor and latent variables going into the G-PAM model are so crucial for the story, could you make a figure where you visualize them? This could maybe be added to Figure 1A. Also, 'radial bias' and 'angular bias' (in Fig1D) could be visualized here.

c) Quantification of electrophysiological activity processing that is fed into the P-GAM model is not entirely clear.

More details about the preprocessing of these data are required, for example, are the SUA baselined using pre-stimulus presentation activity? Are the LFP baselined as well? And how similar are the pooled responses within each area and across? This would allow the reader to spot possible problems when computing further neuronal properties, that could bias the main paper result:

An example is the tuning of the neurons to the phase of ongoing oscillation (Β, Α, Theta). There are a number of papers attempting to optimize methods to measure spike field coherency, e.g. the PPC pairwise phase consistency (Vinck et al., 2010). This method gives an estimation independent of spike count and LFP amplitudes (both parameter vary of course widely across time, tasks, subjects, areas…).

Here, it seems these two parameters are not considered and could lead to artefacts in the coupling results presented. The authors use temporal correlations to approximate coupling between spike/spike, and spike/LFP-phase. Correlation methods can potentially lead to artefacts and overestimations of coupling strength.

In their methods, the author state to 'bin spiking activity across 8ms window' prior to feeding this activity to the P-GAM. It means that 1 spike corresponds to an averaged 8ms time window. If you now try to calculate the dependency of this single spike to a specific phase of a β (30Hz) , the α (12Hz) and theta (4Hz) oscillation, it means that the chance level of assigning the binned spike to a particular phase differs considerably. Therefore, the statistical power of this analysis would decrease for higher frequency. It seems that the authors do not apply any correction.

Reviewer #1 (Recommendations for the authors):

1) From the manuscript it is difficult to judge how representative the different neuronal populations for each area are and to what extent their selectivity differs. The analysis and its variables are quite complex to follow. It would be helpful for the reader to understand how some of them relate to more traditional measures. It is great that the focus on single neurons allows this comparison.

What does "tuned" in this context mean in terms of strength and selectivity?

How many neurons would pass a minimal response criterion like 10 spikes/s. Would these show stronger tuning or correlations?

Figure 2E: "E. Responses from an example MSTd, 7a, and dlPFC neuron (black), aligned to temporal task variables (e.g., time of movement onset and offset), or binned according to their value in a continuous task variable (e.g., linear velocity)." It would be helpful to give the x-axis for each line for the reader to be able to ascertain what the nature of the scale and the range of variables are over which the firing rate changes are depicted.

Could the authors derive from their data one of the traditional measures used for MST, like a direction tuning index? A direct comparison with previous studies could help understand the nature of the sampled pool, particularly (but not exclusively) for areas when smaller neuronal samples, like MST.

2) Another issue is the extent that it seems difficult to distinguish the effect of eye position from that of the background stimulus flow patterns, which of course must differ in direction and element size when animals fixate at different locations on the screen. To what extent was this visual input to neurons correlated with "latent variables" like latent distance and angle to target (latent spatial goal)?

In order to dissociate the contribution of eye position and task from visual input, do the authors have data on a passive viewing control condition, in which the animal fixates and the visual pattern is played back to animals exactly as if in an active one? How do neural responses compare across the three areas?

Could the authors discuss in the paper how the visual input is (or not) included in the model?

3) As the animals were head-fixed, eye position would compensate in some cases the animals might have moved its head position (for instance to keep track of the target). Both, MSTd and dlPFC encoded eye position. Could the close coupling of MSTd and dlPFC be linked to this element of the task?

4) Area 7a was exclusively sampled with chronic rather than moveable probes. It has also the largest number of "single units".

To what extent are these single units independent?

Could a sampling bias in these probes (part of 7a; layers) affect the results, especially when it comes to coupling. Please include in the discussion.

5) To what extent played the lateralization of the recording and task a role for neuronal response? This applies relative to brain hemisphere, body and eye position? Where in each monkey did the recordings take place? Which hand(s) did each monkeys use for the choice stick?

How was the lateralisation included in the model?

Please comment with regards to responses in MST, 7A, and dPFC.

6) Quantification of task parameters are quite clear, this is not entirely the case for electrophysiological activity processing that they feed into their P-GAM model.

More details about the preprocessing of these data are required, for example, are the SUA baselined using pre-stimulus presentation activity? Are the LFP baselined as well? And how similar are the pooled responses within each area and across? This would allow the reader to spot possible problems when computing further neuronal properties, that could bias the main paper result:

An example is the tuning of the neurons to the phase of ongoing oscillation (Β, Α, Theta). There are a number of papers attempting to optimize methods to measure spike field coherency, e.g. the PPC pairwise phase consistency (Vinck et al., 2010). This method gives an estimation independent of spike count and LFP amplitudes (both parameter vary of course widely across time, tasks, subjects, areas…).

Here, it seems these two parameters are not considered and could lead to artefacts in the coupling results presented. The authors use temporal correlations to approximate coupling between spike/spike, and spike/LFP-phase. Correlation methods can potentially lead to artefacts and overestimations of coupling strength.

In their methods, the author state to 'bin spiking activity across 8ms window' prior to feeding this activity to the P-GAM. It means that 1 spike correspond to an averaged 8ms time window. If you now try to calculate the dependency of this single spike to a specific phase of a β (30Hz) , the α (12Hz) and theta (4Hz) oscillation, it means that the chance level of assigning the binned spike to a particular phase differs considerably. Therefore, the statistical power of this analysis would decrease for higher frequency. It seems that the authors do not apply any correction.

Reviewer #2 (Recommendations for the authors):

– I am missing a clear motivation for recording in the three areas that you chose. Could you maybe elaborate on this a bit more in the introduction?

– Given that the sensorimotor and latent variables going into the G-PAM model are so crucial for the story, could you make a figure where you visualize them? This could maybe be added to Figure 1A. Also, 'radial bias' and 'angular bias' (in Fig1D) could be visualized here.

– In Figure 1C, you have added 'slope=bias', whereas technically, it is 'deviation from slope=bias'.

– The legend of Figure 2 is extremely long and contains a lot of information that does not pertain directly to the figure. I suggest that the part '(The direct comparison of the goodness-of-fit….the complexity of their areas and tasks, reaches)' in Fig2D is taken out and added to the text somewhere else.

– It is unclear from Suppl Figure 1 whether within a particular monkey, some recording sites were interhemispheric, or whether within one monkey, all recordings were done in the same hemisphere. This of course has significant consequences for the effects of ongoing LFP and unit-to-unit coupling.

– In Fig2F, you show fractions of neurons tuned to the several variables of the G-PAM model, and in Fig4D, you show proportions of neurons phase-locked to LFP phases in other areas. I might have missed it, but I didn't see any quantification of how strong the tuning was, and how strong the phase-locking.

– When there was stronger MSTd-to-dlPFC coupling and better tracking of the hidden firefly with the eyes (Figure 5B), was the performance of the monkey also better (i.e. more hits)?

– There are a few spelling mistakes throughout the paper (psueudo-R on p.6; tunning on p.7)

Reviewer #3 (Recommendations for the authors):

1. Heat maps of preferred angle and distance in Figure 3 must be cross-validated across trials to show data reliability. Maybe the authors have done that and these are cross-validated plots. If so, it is not mentioned in the methods anywhere. Please verify the ordering of preferred angle and distance hold up with cross-validation. One can get a spurious, evenly tiled coding of any continuous variable if one takes a random matrix (say mean FR x variable value), normalizes each row (FR) and sorts the column by peak location (i.e. preferred variable value) for each row.

2. I am a bit confused by the distribution of preferred latent variables (Figure 3). For e.g. travelled distance and distance to target are anti-correlated. Isn't it trivial that the preferred coding would appear bimodal across a neural population if some neurons are coding for one and some for the other? For a travelled distance coding neuron, there is nothing to code at the onset since distance travelled is 0 and vice versa for distance to the target coding neuron at the offset.

3. Related to #2 above, it would be helpful to see PSTH examples of single neurons that code for travelled distance and those that code for distance to target. PSTH would be obtained by averaging across trials, binned over a range of trial-lengths (e.g. bin1: short trial length, bin2: medium trial length, bin3: long trial length). I would expect clear differences in firing rate at the onset for distance to target coders and at the offset for travelled distance coders. It is difficult to see this in the presented rasters, although according to P-GAM results, that should be the case.

4. It would be helpful to provide a few examples of LFP traces and their filtered form along with spike times to appreciate the phase modulations apparent in their statistical modelling results (Figure 2F).
