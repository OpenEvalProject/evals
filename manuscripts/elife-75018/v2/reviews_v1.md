# Peer review - Round 1

Editors:
- Megan R Carey, https://ror.org/03g001n57 Champalimaud Foundation Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75018.sa0](https://doi.org/10.7554/eLife.75018.sa0)

This paper addresses the important question of how the cerebellum transforms multiple streams of sensory information into an estimate of the motion of the body in the world. The authors find that Purkinje cells, the inhibitory principal neurons of the cerebellar cortex, have multimodal and highly diverse responses to vestibular and neck proprioceptive inputs. Notably, this information is combined in a way that is different from what is seen in downstream fastigial neurons, which reflect either head or body motion, but not both.


---

# Peer review - Round 1

Editors:
- Megan R Carey, https://ror.org/03g001n57 Champalimaud Foundation Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75018.sa1](https://doi.org/10.7554/eLife.75018.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Distinct representations of body and head motion are dynamically encoded by Purkinje cell populations in the macaque cerebellum" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephen H Scott (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All Reviewers had concerns about the rFN model, in particular (a) the absence of mossy fiber inputs to fastigial neurons, and (b) whether it's just easiest to get this fastigial response by down-weighting the PCs with ipsilaterally-signed vestibular and proprioceptive signals, which would make it less interesting. More information about the model is required. At a minimum, please add (1) additional discussion of the assumptions and limitations of the model, and (2) analysis of the distribution of model weights over different classes of PCs (especially linear vs v-shaped or rectifying). Please also see the more detailed comments from the individual reviews below.

2) There was concern during the consultation phase that the focus of the paper is the difference in sensitivity to vestibular vs proprioceptive stimuli, and yet different stimuli are being presented in the two conditions (e.g., compare body velocity in Figure 1A Cell 1, and Figure 2A, Cell 1). It was not clear how these differences might impact the regression coefficients and model performance. The velocity differences between conditions should be addressed directly in the manuscript. Specifically, the reason for the discrepancy (and, if relevant, the experimental constraints on matching the velocities) should be explained in the Methods and discussed explicitly in the text. The reviewers further agreed that the authors should address this issue by (1) providing the total variance-accounted-for for all neurons (not just the normalized values in Supp 1and2), (2) plotting the residuals vs predicted firing rate for all neurons, and (3) providing additional justification that the model is not overfit, if possible.

Reviewer #1 (Recommendations for the authors):

– The writing, particularly in the Results section, is very abrupt. The reader has to go to the Methods section immediately to understand what stimulus is even being provided, let alone what the motivation for the experiments is. Even as someone with reasonable experience in the vestibular field, I had difficulty following the logic of the experimental design.

– The authors have used a "naturalistic" rotational stimulus, about which I have several questions. First, I didn't understand the motivation for using this. Second, based on the figures, this rotational stimulus varied significantly across experiments. E.g., the head and velocity traces in Figure 1A are quite different for Cell 1, Cell 2, and Cell 3. Why deliver different stimuli if the goal is to make comparisons across cells? Even more confusing, the body velocity traces delivered to those exact same cells (Figure 2) appear again quite different. Why deliver different body velocity stimuli in the proprioceptive versus vestibular experiments? Since the entire manuscript focuses on the comparison between these stimuli, it would seem important to hold the parameters constant across the experiments. Head velocity traces are also different, or appear different, across the rotations at different head-on-body angles (Figure 5; e.g. the head velocity stimulus in 5A for +15 vs +30 is different in amplitude).

– In Figure 5, the authors make the interesting observation that vestibular sensitivity of PCs actually varies depending on the head angle relative to the body. I was expecting that they would then test whether the neck proprioceptive "position" term (that they had derived from the experiments in Figure 2) could be used to predict this shift in sensitivity. Instead, the authors directly jump to comparisons with the rostral fastigial population recorded in a prior study. Can they calculate whether their proprioceptive position weights (c_a,2 from equation 1) explain the measured difference in vestibular sensitivity?

– In Figure 6, the authors show modeling evidence that linear summation of Purkinje cells can produce the tuning results of fastigial neurons. They don't address whether an alternate explanation, that some of the proprioceptive or vestibular tuning derives from direct mossy fiber afferents to fastigial neurons, is possible. Furthermore, they don't seem to address the basic surprise here, that although the PCs show much less "cancellation" between vestibular and proprioceptive inputs (p. 11, last paragraph) than fastigial neurons do, the summation of PC inputs can produce fastigial responses. One assumes that the only way to obtain this result is preferential summation of the small set of PCs that do show cancellation (oppositely signed proprioceptive and vestibular sensitivities) but this is never discussed. If that is the underlying explanation of their model's success, then it seems quite weak.

Reviewer #2 (Recommendations for the authors):

I think the first experiment is strong and the paper should emphasize even more the comparison between Purkinje cells and the downstream fastigial neurons. I think some example fastigial neurons could be added to contrast with the Purkinje cell responses. Importantly, Figure 4C shows a red and orange cloud to denote the rFN neurons, but this is very hard to see in the figure. I think the individual neurons should be plotted to highlight the substantive difference between these Purkinje cells and fastigial neurons.

I'm not sure the model is that insightful given that it assumes that there is no other input to the fastigial nucleus. I assume that it would have substantive vestibular and neck proprioceptive input from mossy fibers. As stated in the comment above, is the point of the Purkinje cell activity to counter the sensory input from the mossy fibers in order to create two distinct signals, one related to head and one to body motion in the fastigial population? Thus, a variant for the model would be to show how the population model could create distinct head and body motion signals to counter the presence of a random pattern of vestibular and neck proprioceptive input (assumed to be generated by mossy fiber input). A more advanced model might be interesting in which weights of the parallel fibers onto Purkinje neurons are altered given random mossy fiber inputs to granule cells and fastigial neurons leading to distinct head and body motion signals in the fastigial neurons, but this is certainly beyond the scope of this manuscript.

The cells in Figure 1 and 2 show the same patterns (linear, v-shaped, rectified) across the two conditions. I assume this was common for bimodal cells? Was there any analyses done to support or refute this?

Figure 1 shows that all neurons were sensitive to vestibular input, and no unimodal proprioceptive neurons. Is this an order effect of the experiment in that you always tested vestibular first, and if responsive, then you completed the rest of the experiments? Thus, could there be proprioceptive only neurons, but they were not examined in this study due to the protocol. This is important and needs to be clearly stated in the manuscript, one way or another.

The small sample size makes conclusions regarding head-on-body position a bit of a challenge. Notably, there are only 4 unimodal neurons for Purkinje cells in Figure 5C. The number of neurons is only noted in the figure legend and the number of neurons for the fastigial nucleus is not stated at all and looks to be 11 for bimodal and 10 for unimodal. I think the main text needs to clearly state the actual numbers and recognize the very small sample size for this analysis. These limited number of neurons to characterize tuning properties also weakens the modelling results and conclusions about 40 neurons necessary to predict fastigial neuron responses.

In Figure 4C it looks like the positive body sensitivity ratio neurons tend to have larger values than the negative sensitivity ratio neurons. Is this just a random sampling issue?

Reviewer #3 (Recommendations for the authors):

1 – "All non-significant coefficients were set to zero." In the Methods, the authors should briefly describe the rationale for using this approach instead of L1 regularization.

2 – The acceleration term appears to dominate in the non-preferred direction for vestibular stimulation (Figure S1A); why?

3 – Typo: "Albus and Marrs" -> "Albus and Marr".
