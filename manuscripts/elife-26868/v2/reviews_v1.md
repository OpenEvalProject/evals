# Peer review - Round 1

Editors:
- Peter Latham, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26868.025](https://doi.org/10.7554/eLife.26868.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Context-Dependent Attractor Dynamics in Visual Cortex" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary of the work:

This paper presents evidence that context-dependent dynamics occur in the sensory cortex, as opposed to the view that sensory cortex encodes the stimulus information and then passes it to the prefrontal areas for task-dependent interpretation. The authors use a very clean experimental setup, where precisely the same visual stimulus is shown regardless of task context. They then use a nonlinear decoder, which maps the neural recordings to 1D stimulus color space, to analyze the dynamics of these recordings. The decoder is trained on one task (the "Discrimination" task) and then used to interpret the results of the other task (the "Categorization" task). The decoder indicates that the dynamics in the Discrimination and Categorization task are different.

Essential revisions:

Although we have a relatively large number of comments, all should be relatively straightforward.

1) The title – Attractor Dynamics in Visual Cortex – may not be correct, and in addition may actually detract from the message of the paper. Technically, there is an attractor whenever activity goes to a fixed point. However, that's kind of trivial: given that input is fixed, we wouldn't be totally surprised if activity goes to a fixed point, so the fact that there's an attractor wouldn't be an especially big deal. It also wouldn't be an especially big deal if activity didn't go to a fixed point, as we know there are long timescales in network dynamics. And, indeed, it looks like it's the latter: while the population averaged firing rate appears to asymptote (Figure 2C), the decoded stimulus is still changing at the end of the trial (Figure 2A).

In any case, attractor dynamics is beside the point; what's really going on here is that there is different activity with identical input. This is a very nice illustration of task switching, but not really of attractor dynamics. That, rather than attractor dynamics, should be emphasized.

2) In the section "The recurrent model explains the stimulus-dependent dynamics," the authors look at different explanations for the differences in activity in the categorization versus discrimination tasks. The winning explanation was a recurrent model (Equation 10). All well and good, except for two things. First, the model described by Equation 10 isn't really recurrent (could have been a typo; see point 9 below). Second, later on the authors consider a different recurrent model (Equations 14-16). Why not use the second one, which seemed better to me? I suspect there's a reason, but I don't think it was well explained (either that or I missed the explanation).

3) In the section "Reconstructed collective dynamics explains choice variability," it would be a good idea to decode individual trials. If the authors really have the right model, the model should make errors on the same trial as the monkeys.

4) There are two problems with the mutual information calculation. First, it makes no sense to compute accumulated information. Even if the responses were uncorrelated across time bins, the stimulus is correlated. You can see this in the very high information differences – they're larger than the total information available. This can be partially fixed by reporting the instantaneous estimates. Here both ICat and IDis should be displayed individually, as the difference does not tell us where the information is coming from.

Second, to compute information accurately, it's necessary to have the correct noise model. And, by the author's own admission, they have the wrong noise model (they assume independent decoders). Not much they can do about this, but they should at least comment on it.

5) In the section "Comparison to other methods of dimensionality reduction," the authors claim that standard dimensionality reduction methods don't capture the difference in the discrimination versus categorization tasks. They need to do two things to back up that claim. First, they need to quantify it: differences between the trajectories in the categorization and discrimination tasks seem about as big in Figure 5D as they do in Figure 2A. And in general it is more difficult to judge separation in a single 3D plot than in 1D, so a purely visual comparison isn't so useful.

Second, they should try a similarly supervised linear approach used for the nonlinear decoder. For example they could try an approach similar to the population vectors used in motor decoding, where they weight the firing rate according to a neuron's stimulus preference. An allied more modern approach is demixed PCA (Kobak et al., eLife 2016). Both of these differ substantially from the unsupervised PCA approach the authors use, which by comparison could be seen as a bit of a straw man for linear decoding. Although maybe not so much of a straw man; see above.

Finally, Figures 5A and 5C should also be made easier to interpret – in particular, the dots are hard to visualize.

6) In the section "Bifurcation of attractor dynamics in a recurrent model," the authors consider a second, different, recurrent model. The nullclines in Figures 6B and C are pretty standard. However, they are known to be somewhat fragile. Do the nullclines really keep their shape no matter what color is presented? The set of nullclines for all color presentations should be shown. It could be in Methods, and it could be all on one plot.

7) Section “Likelihood-based decoding”: Why smooth over the stimulus space? Analysis is probably easier if s is discrete – you can just compute the posterior for the discrete values of s shown to the animal. If there's a benefit to considering s to be a continuous variable, that should be mentioned. Otherwise, it should be discrete.

8) Something seems to be wrong with Equation 10: it's not a recurrent network; instead, r^(t) depends on r(t)andr(t−1). Is this really what the authors meant? If so, it shouldn't be called a recurrent network. If not, it needs to be corrected (there may be a hat missing somewhere).

9) The method for comparing models used in Figure 2C/D, while nice for presentation as the decoder results are 1D, is difficult to interpret. Because the model prediction comes from multiple steps (first fitting the firing rates, then putting it through the decoder which could strongly transform them), it is hard to judge the meaning of the results in Figure 2D. It would be good to report the mean squared error between the actual firing rates in the categorization tasks and the firing rates predicted by the model. Presumably they'll show the same trends as in panel D, but it would be nice to see that.

10) Is there a simple explanation for why the recurrent model does better? It is unclear what about the recurrent model makes it work, and some more intermediate models could be used to elucidate this. Does the recurrence matter, or is it simply fitting an additive component that works? Note that the answer may be "we can't find a simple explanation". If so, use your best judgment as to whether you want to include that in the paper.
