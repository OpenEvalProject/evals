# Peer review - Round 1

Editors:
- David Badre, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29718.016](https://doi.org/10.7554/eLife.29718.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Neural computations underlying inverse reinforcement learning in the human brain" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission has agreed to reveal his identity: Samuel J Gershman (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

How people learn what actions lead to preferable outcomes is an important question at the intersection of learning and social cognition. This paper presents a behavioral, computational and neural characterization of observational learning in humans, using a paradigm that contrasts an "inverse reinforcement learning" account with an imitation account. The results suggest that people use inverse RL, tracking value in the observed agents value space rather than their own. This function is supported by regions of the brain involved in goal-directed learning, as well as mentalizing.

Essential revisions:

Though the reviewers differed on the value of the work for a pure behavioral or cognitive science audience, the reviewers with expertise in neuroscience were in agreement regarding the novelty and value of these findings for that domain. Nevertheless, the reviewers identified several points that would need to be addressed in a revision. These points largely cluster under three major themes and so are summarized accordingly below.

1) The framing and background need to be fully reworked in order to better situate the present study in the context of the prior cognitive science literature on observational learning and inverse reinforcement learning. Here are some specific examples from the reviewers of relevant literature that was not addressed sufficiently in the report.

a) Several other papers have also pursued this topic and should be integrated. Baker, Saxe and Tenenbaum, (2009), in an influential paper, showed how a computational theory of goal inference can make very strong and accurate predictions about behavioral judgments, and this was later followed up in many different ways by Jara-Ettinger, Noah Goodman, and others.

b) Considerable research on preference learning by children likewise pursues this topic.

Fawcett and Markson, (2010).

Lucas et al., (2009).

Lucas, C. G., Griffiths, T. L., Xu, F., Fawcett, C., Gopnik, A., Kushnir, T., Markson, L., & Hu, J. (2014). The Child as Econometrician: A Rational Model of Preference Understanding in Children. PloS ONE 9(3): e92160 doi:10.1371/journal.pone.0092160.

Ma and Xu, (2011).

Repacholi and Gopnik (1997). c) There is a large literature on social influence that the paper doesn't touch upon at all.

d) There is recent work by Gershman, Pouncy and Gweon, (2017) on social learning that may be relevant.

2) Several of the specific analyses lacked sufficient justification and so either appeared inappropriate or arbitrary.

a) Much depends on the adequacy of the small volume correction (SVC). Though SVC is an acceptable approach, it is challenging to do in a way that does not introduce hidden degrees of freedom or that is unrealistically specific about the a priori hypotheses. The methods state that SVC was applied to 12mm spheres based on peak voxels from prior work from the authors' lab. This is likely only a modest correction to threshold given the size of these spheres, so it is important to justify such highly specific and small regions. Likewise, the particular choice of prior papers appears arbitrary in the absence of a justification. Thus, it must be clear that these are uniquely justified, were chosen prior seeing the data, and would truly be the only activity in these areas that would have been expected a priori. Indeed, it is not clear such specific predictions can be justified, given that this is the first fMRI study of inverse RL and regions like dmPFC are larger than 12mm. A more reasonable alternative would be a volume encompassing the full anatomically-defined region where observed activation would have been considered consistent with a priori predictions.

b) It was hard to track what thresholds were used throughout the results, discussion, and figures. For example, the discussion mentions a number of regions beyond dmPFC, like DLPFC, striatum, and TPJ. Were these also SVC based on a priori regions? If so, how many a priori regions were included? If not, how were these corrected? The discussion also mentions regions that were evident at a more lenient statistical threshold, though it was not clear what threshold that was.

c) It was not clear from the description how the model-based regressors from the inverse RL versus imitation RL were included in the GLM and then used for model selection, making the specifics of the model-based fMRI approach difficult to evaluate. Were they included in separate models or in the same model in the standard SPM way (which enters them ordered in something like a hierarchical regression)? Or were they allowed to compete for variance? Were they correlated? These points are important to clarify in order evaluate this aspect of the methods.

d) A one-tailed test was applied for some behavioral tests but not others. Though it is understood that the authors might have a directional prediction justifying the use of a one-tailed test, one would have to make an argument why there is a directional prediction for these particular analyses and not for others. The chief concern is that the one-tailed test was chosen after the two-tailed test failed to be significant.

e) The text notes that participants were removed for movement exceeding 10mm. This seems like a lax movement threshold. Movement more than a voxel is difficult to correct, and presumably voxel sizes were smaller than 10mm. How many participants moved more than a voxel?

f) It was not clear where the effect sizes appearing the figures come from. Was that based on unbiased ROIs?

3) Certain aspects of the theoretical models and their predictions were difficult to evaluate based on the description in the text.

a) There are several missing equations Materials and methods section.

b) Results section: "If participants used a simple imitative behavioral (and/or inverting) strategy, we should observe symmetrical performance changes (accuracy decreases) for the best and worst machine, compared to the similar condition, whereas the mid machine should stay unchanged." This prediction is difficult to understand: why is it the case that simple imitation would not produce changes in the mid machine?

c) It would be useful to see a bar graph like Figure 1C for the key models. The relevant data is shown in Figure 2—figure supplement 1B but it's hard to directly compare this to the human data.

d) It is not clear why the models make different predictions for the middle preferred slot machine, or how the models take into account similarity between the observer and agent.
