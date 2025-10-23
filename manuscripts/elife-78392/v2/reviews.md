# Peer review - Round 1

Editors:
- John T Serences, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78392.sa0](https://doi.org/10.7554/eLife.78392.sa0)

This manuscript combines human behavioral experiments using a categorization task and a convolutional neural network model to test different mechanisms that may support attention-related improvements in perception. Through carefully controlled manipulations of computational architecture and parameters, the authors dissociate the effects of tuning gain vs. tuning shifts. They conclude that increases in gain are the primary means by which attention improves behavioral performance.


---

# Peer review - Round 1

Editors:
- John T Serences, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78392.sa1](https://doi.org/10.7554/eLife.78392.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Behavioral benefits of spatial attention explained by multiplicative gain, not receptive field shifts, in a neural network model" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Albert Compte (Reviewer #1); Kendrick N Kay (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We were all very enthusiastic about the approach and the findings. During our discussions, we collectively focused on several issues regarding the generality of the conclusions and the methods used to arrive at them. Below is a list of the main issues:

1) The Detection vs discrimination. Having at least one other task would allow you to determine if the gain story is specific to detection or if the type of modulation depends on the task. In either case, results from another task would be interesting and would greatly improve the generality and theoretical impact of the claims.

2) Justifying the spatial invariance of the readout mechanism and potentially testing other schemes.

3) What happens when gain isn't just injected into "V1", but into other layers? For example, Lindsay has shown that this matters in the context of CNNs performing attention tasks, and the rationale for injecting a change so early in the system isn't entirely clear.

4) Others, like Compte and Wang 2006, have also explored this question using other architectures. Given that the CORnet-z model does not include recurrent dynamics within each layer, it will be important to discuss and consider the implications of the chosen network and implications for the generality of the conclusions.

Reviewer #1 (Recommendations for the authors):

1) The model requires a more detailed presentation in the text (now lines 93,94). A succinct description of how it is built should be provided so the reader does not have to look up the references for a simple, broad-picture understanding. It is important to mention that the model has been built and trained previously based on the same set of images that will be used here, and the weights are available, so the only further training done here is the linear classifier on the model outputs to detect image categories upon presentation of "composite" grids. It took a while for me to understand this and to see the difference between base images and composite images. There is also a confusing thing about the neural model in Figure 2d: it pictures the ReLU occurring after the max pooling step, but in Figure 1 of Kubilius et al. (2018) it occurs before the max pooling step. The sentence ("Unit activations were measured after the convolution, prior to the max pooling step") in the caption of Figure 2 is also confusing: how is unit activity being measured before the ReLU non-linearity that transforms inputs into output rates?

2) The manuscript emphasizes 3 different RF modulations: scaling, shift, and shrinkage, but then only two of them are specifically isolated with network simulations. RF shrinkage is not addressed. This is not really a problem, but it would be nice to have full "symmetry" in the manuscript. Is there a specific reason why this modulation can not be assessed to make it more parallel to the rest?

3) References are required in lines 145 ("…behavioral benefits of attention") and 250 ("…as others have suggested").

4) In general, scatter plots in the figures should indicate what are the individual data points presented. I think in some cases are units, in other cases they are categories. This should be clearly indicated.

Reviewer #2 (Recommendations for the authors):1. On the issue of the readout.As mentioned in the public review, it appears that the conclusions are heavily dependent on the choice of readout mechanism. Thus, it seems a bit premature at this point to make strong general conclusions about which tuning properties are critical for behavioral improvements. Many recent studies have shown spatial tuning (i.e. large but limited RF sizes) in the high-level visual cortex; hence, in the neural network observer model, it is not clear why the readout (linear classification) is performed on unit activity that has been summed fully across visual space.

Now, it is an open interesting empirical question whether perceptual decisions from the visual system are based on fully spatially invariant units. But note that if that were the case, isn't one counterintuitive implication that our perceptual decisions can be corrupted by visual stimuli far away from the relevant decision zone?

If we entertain the possibility that the readout can be from units that have spatial specificity, then it remains to be seen what sort of modeling outcomes there might be.

Even though the authors show, in the context of their particular model, that tuning shifts do not produce the required behavioral improvements, it seems that in general, it should be possible in theory for shifts to provide the required benefits. For example, if the focal cue is on stimuli in the upper right quadrant, if all receptive fields in the model covering the other quadrants were fully shifted to the upper right quadrant, wouldn't the readout from the model obviously improve?

With regards to the linear classifiers implemented by the authors, it seems there are many important details that need to get spelled out. Things like how exactly was the final predicted category obtained? Was a 20-way classification scheme used, or some winner-take-all scheme from 20 separate binary classifiers used? Was there any regularization used to fit the weights of the logistic regression? If not, how can we be confident that the amount of training data was sufficient? Details on the classification methods are important for interpreting how upstream computational changes impact the behavioral output from the model.

2. Reframing and/or exploring other models.

In light of the uncertainties about how general the conclusions can be from the modeling results, the authors may wish to consider refocusing/reframing their work. Instead of attempting to make strong general conclusions about the relationship between behavior and computational mechanisms, the author might reframe their work into more of a computational and theory-building exercise.

In particular, the authors show interesting insights regarding how a Gaussian applied to an early layer of a CNN can have effects that propagate through the network and which manifest as complex, rich RF tuning changes elsewhere in the model (e.g. as the authors state, "RF shifts are a result of the signal gain…") (see also Compte Cerebral Cortex 2006). The distinction between architecture (internal computational mechanisms) and what might manifest at the level of input-output behavior of a unit is an important one, as the authors discuss (p. 17, lines 257-268). Certainly, a number of previous studies have adopted the latter mindset. Note that doing so is not necessarily inconsistent with the former "mechanistic" mindset (they are just different modeling stances one can take). Emphasizing and generating insights from adopting a "mechanistic" mindset is valuable research output.

Thus, one suggestion is to reframe the work to focus more on this insight and think about the theoretical ramifications (and/or concrete experimental predictions) that might stem from this. Related to this effort might be to consider other models. For example, it would be interesting to understand the similarities and differences between the 'attentional field' model (Reynolds, Heeger) and the current model. As another example, it would be interesting to consider models in which the "Gaussian gain" is applied at the end (deep layers) and effects propagate backwards, as opposed to being applied at the beginning and effects propagating forwards.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Gain, not concomitant changes in spatial receptive field properties, improves task performance in a neural network attention model" for further consideration by eLife.

Reviewer #2 and I have re-evaluated your revised submission and we both agree that it is much improved and makes a strong contribution to the literature. There are a few remaining issues that need to be addressed that are captured in Reviewer #2's comments, and I'd ask you to address them before a final decision is made. Please let me know if you have any questions, and thanks.

Reviewer #2 (Recommendations for the authors):

I have reviewed the revisions and the authors' responses.

Overall, the revisions are solid and substantial. The additions to the paper are useful, in particular, the new analyses exploring exactly how spatial information is included, restricted, or "averaged over", which provide insights into the potential equivalency of the gain effects and the selection (or suppression) of irrelevant information. In addition, the new framing and discussion provide helpful clarity over the original manuscript and make for a more straightforward read. The computational modeling performed in this paper represents a novel and well-executed foray into a challenging area. While it does not necessarily definitively resolve the issues at stake, I believe it provides and demonstrates an interesting and non-trivial approach.

A few critical comments on the revisions:

The authors state, "At larger scales or in other tasks there are theoretical reasons to expect that task performance will improve due to these effects". In this sentence, the referent of "these effects" is a bit unclear. Also, I am not sure what 'larger scales' refers to. Finally, it would be useful to give specific examples of what types of 'other tasks' might be implied by the sentence here.

In response to the reviews, the authors added some detail on the linear classifier methods, but the text is still not sufficient. More detail on exactly what was implemented seems important. For example, details on the "under the curve" quantification. In addition, perhaps there is a misspecification of the methods: As the authors state, "Weights were fit using logistic regression with an L2 loss and no regularization, using scikit-learn and the LIBLINEAR package (Pedregosa et al., 2011)." However, if I understand correctly, for each category, there are effectively 512 parameters that need to get learned and only 100 instances to train these parameters. Hence, if no regularization were used, this presumably would lead to a very noisy (overfit) solution. Perhaps the authors meant that they used L2 regularization (and the default settings for the regularization hyperparameter in the scikit-learn package)? Note that logistic regression implies a probabilistic formulation of the classification problem, and would seem to suggest that the authors don't actually mean that they used an L2 loss (which implies additive Gaussian noise). Hopefully, these important analysis choices and details can be clarified and do not have larger ramifications for the rest of the paper.
