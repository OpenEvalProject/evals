# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53151.sa1](https://doi.org/10.7554/eLife.53151.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper explores the hypothesis that OFF responses are single-cell signatures of network dynamics, and shows convincingly that a model based on recurrent interactions does a much better job explaining the data than the de- facto standard model, which is based purely on single cell dynamics. In addition, the proposed recurrent network model generates transient OFF responses very similar to what is seen in experiments.

Decision letter after peer review:

Thank you for submitting your article "Population coding and network dynamics during OFF responses in auditory cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Guillaume Hennequin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please aim to submit the revised version within two months.

Summary:

In this paper, Bondanelli and colleagues study the spatiotemporal structure of OFF responses in A1. They propose that these responses arise from a simple linear mechanism involving a certain form of nonnormal population dynamics. They fit such a network model to A1 data and find that it explains several important aspects of OFF responses, some, but importantly, not all, of which are also captured by a single-neuron mechanism.

Essential revisions:

We're very sorry for the long delay. That's in part because at least one of use found the paper very hard to read, and it took a long time to figure out what was going on. And as you'll see, it's not clear if we did that very well. We think the problem is that you're missing quantitative analysis; in many cases it seems that we're supposed to understand why a particular piece of analysis supported your model, but it simply wasn't clear to us why that was true. Explicit examples of this will be given below.

A major issue for us has been that you begin with a discussion of special cases of Equation (2) (last two paragraphs of page 6) but then go on to test predictions of THE model without telling us which of these special assumptions you are actually making (if any) in the production of your results (Figure 4 specifically). We believe that the first paragraph of "Testing the network mechanisms on the data" should begin with a clear description of the actual model considered (including whether your transient channels are mutually orthogonal, and how initial conditions relate to those planes).

More specifically, to summarize our current understanding: under the assumption that the v's are orthonormal, the u's are orthogonal, and uk dot vl = 0 for all k \ne l (not strictly true, but close enough in high dimensions), the most general solution (a generalization of Eq. 34 to an arbitrary number of modes) is

r(t) = [uperp + sumk uk (ak + vk dot uk t)] exp(-t)

where uperp is perpendicular to all the uk and the ak are arbitrary.

This appears late in Methods. But it's important, because there seem to be hidden assumptions about uperp and the ak. Namely,

- the ak are all set to zero

- uperp = uk for only one k, with k dependent on the stimulus.

Assuming this is correct, it's a critical part of the model. And it is, in fact, an extra assumption.

Given that setup, we believe there were several predictions:

a. Lines 216-228: There's a prediction about the correlational structure that we didn't fully understand. Equations are needed, in the main text, that make the predictions explicit.

b. Lines 229-238: Correlations between the beginning and the peak of the off response should small. Again, equations are needed; this should be quantified.

c. Lines 239-253:

"To further examine to which extent the population dynamics during OFF responses could be accounted for by a non-normal linear dynamical system, we next fitted our network model population OFF responses to all stimuli at once using reduced-rank regression (Figure S1; see Methods). Qualitatively, we found that the fit reproduced well the low-dimensional population trajectories (Figure 4C)."

As far as we could tell, this just tells us that the fit is good; it doesn't tell us anything about whether the OFF responses could be accounted for by a non-normal linear dynamical system. Is that correct, or did we miss something? If that is correct, it seems like this paragraph is mainly a distractor.

d. Lines 254-262: The fitted connectivity, J, had eigenvalues less than 1 and the symmetrized version had eigenvalues greater than 1. That's consistent with the low rank, non-normal model. However, couldn't such a J could come from a high rank, non-normal model? If so, it's not strong evidence for your model. This should be clarified.

e. Lines 263-283: There were several results here, but it's not clear how much they supported the model. For example,

"We computed the overlap between the subspaces spanned by the transient channels for each pair of stimuli s1 and s2 , analogous to the overlap between the vectors u(s1) and u(s2) in Eq. (2) (see Methods). We found that the overlap between the transient channels matched the overlap between the response dynamics and population states at the end of stimulus presentation (Figure 4F, right panel), consistent with the interpretation that individual OFF responses may be generated through transient coding channels of the form given by Eq. (2)."

It's not clear what we should expect here. Is this strong or weak evidence for the model? You need to quantify what we should expect, and be clear whether this is only consistent with the model, or provides evidence for it.

"While the fraction of variance explained when using the matrix JSum was necessarily lower than the one computed using JFull , the model with connectivity JSum could still explain a consistent fraction of the total variance, and yielded values of R2 significantly higher than the ones obtained from the shuffles."

Again, it's not clear what we should expect. Is this strong or weak evidence for the model?

f. Lines 328-331: for the single cell model in Eq. 3, the correlations between the beginning and peak of the off response are high. This seems easily fixable with a very minor tweak. Suppose there are two kinds of neurons, some that peak early,

ri(t) = ai(s) fi(t)

and some that peak late,

ri(t) = bi(s) gi(t)

(for instance, fi(t) = Theta(t) e^{-t} and gi(t) = Theta(t) t*e^{-t}). Different stimuli (s) could activate different sets of neurons.

Alternatively, the single neuron responses could be of the form

ri(t) = ai(s) fi(t) + bi(s) gi(t)

where the a's and b's are anti correlated (either a is large and b is small or vice versa) and fi and gi are as above.

Are these model ruled out by the data? If not, that seems to weaken the paper (although maybe there are other things wrong with these models). In either case, models like these should be discussed.

g. Lines 332-353:

"A second important difference between the two models is that in the single-cell model the temporal shape of the response of each neuron is the same across all stimuli, while for the recurrent model this is not necessarily the case."

Given this opening sentence, why not just show that for the recurrent network model, the temporal shape of the response is not the same across all stimuli? Instead, there's a lot of analysis that we didn't fully understand. In particular, there's a rather sudden switch from specifying the form of Li(t) (Eq. 44) and fitting Li(t) (Eq. 48). What's missing is a quantitative prediction of what we should expect, followed by a demonstration that the data is consistent with that prediction.

In addition, we have some specific suggestions.

1. Lines 174-177,

"We focus on two outstanding properties identified in the OFF responses to different stimuli. The first one is the strong amplification of OFF responses, as quantified by the transient increase of the distance from baseline ||r(t)||. The second important feature is the low-dimensionality of OFF response trajectories and their global structure across different stimuli."

It seems that this is all you're going to focus on, but it's not. It would be nice to know, at some point early in the manuscript, exactly what you're going to do.

2. What's the difference between Figures 2D and 4A (left panel).

3. Lines 329-31,

"The single-cell model predicts that these two states are only weakly decorrelated and essentially lie along a single dimension (Figure 5E and S7), which is inconsistent with experimental observations"

Which experimental observations?

4. Throughout the paper we found it unclear how initial conditions were chosen for the model, e.g. in Figure 3. From line 167, we are led to think that they are picked from the actual data, "we model the firing activity at the end of stimulus presentation as the initial condition of the network dynamics" -- since the model doesn't explicitly models the stimulus period as far as we understand (?), we infer this activity is taken from the data? But does the model even have the same number of neurons?

5. The purpose of Figure 2 is to convey that different stimuli evoke orthogonal OFF responses, and these OFF responses are low dimensional. By my calculation, for each conditional mean (over 20 trials), there are 400ms * 31.5 frame/s ~= 13 samples used to estimate the PCs and variance explained resulting in a maximum dimensionality (PCs to get to 80%) of 13. If this is the case, a more careful comparison to the cross-condition dimensionality is warranted, which accounts for sample size.

Also, we would expect there to be fewer time points on the traces in Figure 2B. How were the trial-averaged responses interpolated?

What steps were taken to insure that the same unit wasn't double counted during pooling across sessions. Mistakes in this process can contribute to inflated variance along primary PC's creating the illusion of low dimensionality.

6. Statements of relative degree of subspace overlap should be verified with a hypothesis test. For data, this can be done by resampling neurons.

7. You should justify why LDA (naive covariance assumption) is more suitable for assessing linear separability in Figure 1C than an SVM. Absent justification, an SVM should be used to get the clearest assessment of linear separability.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Network dynamics underlying OFF responses in the auditory cortex" for further consideration by eLife. Your revised article has been evaluated by Barbara Shinn-Cunningham (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The good news is that the paper is much improved. The writing is more clear, and the analysis of dimensions of amplified trial-to-trial variability is compelling. The less good news is that now that we understand it better, additional issues have come up. All can, we believe, be dealt with relatively easily.

Let's start with the data you're are trying to explain. Basically, after the offset of an auditory stimulus, there is transient amplification, with different stimuli activating nearly orthogonal subspaces.

To model this, low rank linear dynamics is used, of the form

dr/dt = sum_{k=1}^R uk vk r – r,

where r (=r1, r2,.…, rN) is the trial averaged activity. The network had a few additional properties,

a. The rank, R, is much less than the number of neurons, N.

b. The u's and v's are nearly orthogonal.

c. The symmetric part of the connectivity matrix must have eigenvalues with real part >1.

d. The model has no external input, so the response to a particular stimulus (after offset) depends only on the value of r immediately after stimulus offset, here denoted r0(s) where s is the stimulus.

e. For any stimulus, s, r0(s) has appreciable overlap with a small number of vk (on the order of 5).

This model did an OK job explaining the data. In particular, Figure 4H, left (the model), is supposed to match Figure 2D (the data). But the match is not so good: the off-diagonal channel overlap in Figure 2D is near zero, whereas it's around 0.5 in Figure 4H. And the full model explains only about half the variance (Figure 4H, Right).

In addition, you claim that the dynamics is autonomous. The test for this is described on lines 251-9:

"We first tested the starting assumption that the OFF response trajectories are consistent with linear, autonomous network dynamics driven only by the initial pattern of activity and network interactions. If that is the case, the OFF response dynamics are fully determined by the initial activity at stimulus offset (t = 0). This assumption implies that the geometric structure of the initial activity states r0(s) fully predicts the geometric structure of the dynamics r(s)(t) during the OFF responses (see Materials and methods). In particular, two stimuli s1 and s2 corresponding to correlated initial states r0(s1) and r0(s2) will lead to correlated trajectories r(s1)(t) and r(s2)(t) in the model. Conversely, if two OFF-response trajectories r(s1)(t) and r(s2)(t) are orthogonal, the initial states r0(s1) and r0(s2) are necessarily orthogonal."

We're pretty sure that isn't correct: correlations are preserved only if the dynamics causes pure rotation at constant angular speed, something that doesn't happen in general, even for linear dynamics.

And finally, Figure 4E, right, shows that many u's and v's are not orthogonal -- judging from that figure, on the order of 10-20%. These terms were of the form

|u1| v2 v1 – |u2| v1 v2

where v1 and v2 are nearly orthogonal. You claim that terms like this can't lead to transient amplification. That's true if |u_1|=|u_2|. But if |u_1| and |u_2| are sufficiently different, it's not true. But maybe |u_1| \approx |u_2| in the data? If so, that should be clear. In any case, this seems like a detail -- it's certainly possible to do the analysis with these terms included.

The lack of orthogonality between the u's and v's doesn't seem so serious. But the lack of agreement between Figures 2D and 4H, combined with no strong evidence for autonomous dynamics, seems potentially problematic. Of course, no model ever fits perfectly. But it's hard to figure out exactly what the take-home message is. If there was strong evidence that the dynamics is autonomous, that would help -- at least we would know that the intrinsic dynamics is responsible for the transient amplification.

As a potentially important aside: the eigenvalue spectrum of Figure 4D shows one marginally stable, non-oscillatory mode. Based on past experience of one of the reviewers, it may be that the lack of agreement between Figures 2D and 4H is because of this mode. The reasoning is that if this slow mode is present by a small amount in all initial conditions, it will generate the fairly weak overlap in Figure 2D, but because it sticks, it might end up dominating the late off-responses for each stimulus after all the rest has decayed away. If that's the case, then this mode will be part of the principal subspace extracted for each stimulus. The measure of overlap based on "subspace angle" is very sensitive to this, which could explain the large overlaps in Figure 4H. Importantly, that marginally stable eigenvalue may be an artifact of insufficient regularization. There are a lot of "ifs" in the above reasoning, but if this mode can be eliminated, perhaps by different regularization, agreement may improve. We don't know if that's possible, but it's worth thinking about.

There is a lot of very nice analysis in the paper, and all reviewers agree that it should be published. However, it needs a clear take-home message. Exactly what that is depends, we believe, on how strongly the evidence is for autonomous dynamics. If that's very strong, then at the very least the take-home message is:

"Off cells show transient amplification that is generated by internal dynamics, not external input. That transient dynamics is mildly consistent with low rank connectivity in which dynamics can mainly be reduced to multiple 2-D systems. However, we can't rule out more complex behavior, with transient amplification fundamentally involving several dimensions."

Possibly you can come up with a stronger conclusion, but that's the best we could come up with.

If the evidence for autonomous dynamics is weak, that seems to be a fundamental problem, since the transient amplification may be caused solely by external input. But presumably that can never be ruled out -- a fact that you should probably mention. It's not a plausible scenario, so we don't think it will weaken the paper..

Our main comment, then, is to explore more carefully whether or not dynamics is autonomous, and/or be more careful about the conclusions. One possible way to test for autonomous dynamics is to plot the trajectories and look for intersections, or near intersections -- what Mark Churchland calls tangled trajectories, for which quantification is possible. Absence of near intersections would at least be consistent with autonomous dynamics. But there may be better methods. For instance, you might try LFADS: you can fit both an RNN and a linear dynamical model, and see which one fits better. That will, though, be a huge amount of work, and you should do it only if you want to.

In addition, we suggest exploring a richer single-neuron model. The current model has the form

ri^s(t) = r_{0i}^s Li(t).

If ri is non-negative, this can be written

dr_i/dt = fi(t) ri,

with ri(t=0) a function of the stimulus. It would be more convincing to consider a model with a nonlinearity; say

dri/dt = fi(t) gi(ri).

The nonlinearity gi could be parameterized with, probably, only a handful of parameters. For instance, it could be written as a sum of basis functions, much the way Li was parameterised. The single-cell model was rejected because it explained only about 20% of the variance, versus 50% for the recurrent network. It would be reassuring if adding a nonlinearity didn't bring this up to 50%. Again, this also is only a suggestion. However, if you stick with the current single cell model, you'll need to frame your comparison less generally than "recurrent versus single cell".
