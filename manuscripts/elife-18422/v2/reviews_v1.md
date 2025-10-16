# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18422.016](https://doi.org/10.7554/eLife.18422.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Perceptual decisions biased by the cost to act" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Joshua Gold as the Reviewing Editor and Sabine Kastner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Birte Forstmann (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this elegant study, the authors report four experiments showing that increased motor costs in one decision can influence decision-making in other decisions, even when these other decisions are fundamentally different in effector (voice vs hand) and choice options (detection task vs discrimination task). They report that: 1) increased force for one hand led to biased choices away from that alternative; 2) the biases persisted through vocal choices; and 3) the results could be modelled as a change in the starting point of a drift-diffusion process.

The reviewers agreed that this study is interesting and novel. However, they also believed the manuscript could be improved considerably by addressing several concerns, listed below.

Essential revisions:

1) The authors miss to cite several important references regarding the hypothesis whether the additional cost of selecting one of the motor responses is encoded as a 'starting point shift' or a 'drift rate shift' (e.g., Bogacz et al., 2006; Simen et al., 2009). The authors may also want to consider recent work suggesting that the optimal strategy during trials with different choice payoffs as well as difficulties is to implement an urgency signal (Drugowitsch et al., 2012).

2) The authors fit a simple DDM model to their data to learn more about underlying latent variables. While I think this is a great approach, I have some critical technical remarks about the fitting itself:

a) In general it is not advised to fit cognitive models to data that is collapsed over subjects. It can obfuscate effects and bias towards invalid models (see, e.g., Estes et al. 2005; Brown and Heathcote, 2003). Instead the authors may present the parameter estimates from the model that is fit to individual data.

b) The DDM is not fit separately to different tasks with different effectors. It appears unreasonable to assume that, e.g., the non-decision time parameter is equal for vocal vs. motor responses and I would suggest to fit the DDM separately for each experiment.

c) The authors use a t-test on individual BIC-values for model comparison. A principled way of doing model comparison would be to present the BIC-values in a table indicating which model fit the experiment(s) best. The authors could consider extending such a table by including so-called AIC/BIC-weights which offer a more principled way of comparing BIC values (Wagnemakers and Farrell, 2004).

d) The authors have chosen to fit the most basic version of the DDM without any across-trial variability in non-decision time, drift rate, or starting point. Such a model predicts that error trials and correct trials have exactly the same RT distribution. This is rarely observed in empirical data (Ratcliff and Mckoon, 2008). Why did the authors choose for this simplified model?

3) It is not clear that experiment 2 shows that "mere exposure to an asymmetric motor costs between the two hands is sufficient to bias subsequent decisions" – especially given the relatively rapid, transient effects presented on the detection task (Figure 3C,D). This point should be at least discussed further.

4) Were there changes in the slope of the psychometric function (e.g., in Experiment 1), in addition to the changes in PSE? The somewhat odd, asymmetric effect on detection performance in Experiment 4 might be predicted to have such effects.

5) More discussion should be given to the interpretation of the vocal-transfer effect, and its implication for mechanisms of decision formation – in particular the idea of decisions being formed in the context of an intentional framework or not, which has received much attention in the literature. It also would be useful to discuss this result in terms of what is known about persistent biases in other contexts.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Perceptual decisions are biased by the cost to act" for further consideration at eLife. Your revised article has been favourably evaluated by Sabine Kastner (Senior editor) and a Reviewing editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) It would be useful to provide more details about Experiment 4, including comments about how those details affect the interpretation of the results. In particular, was the induction phase done like in Experiment 3, with half the participants getting increased resistance to the left, and the other half to the right? I don't think that was the case, but unless I missed something the only mention was in the Figure 3 legend ("Vocal motion detection criterion differences between the leftward (with manual response resistance) and rightward (without resistance) motion (Experiment 4)"), which doesn't indicate whether that statement was true just for the Figure 3D data or more generally for Experiment 4.

2) The claim that "it has been suggested that shifting the starting point of accumulation process is the optimal solution to account for such contextual changes [Bogacz et al., 2006 and Simen et al., 2009]" should probably be tempered to include the possibility that these kinds of criterion shifts alone may not be optimal when the signal strength (motion coherence) is randomised; e.g., Hanks et al., J Neurosci 2011.

3) The argument that the simple version of the DDM used in this study can distinguish the models of interest – change in starting point or evidence accumulation – would be stronger if they could show that the manipulations do not generally affect how well those particular model variants fit the data, relative to other models known to more robustly fit choice and RT distributions for these kinds of tasks. For example, are the patterns of error RTs similar in the biased versus unbiased conditions?
