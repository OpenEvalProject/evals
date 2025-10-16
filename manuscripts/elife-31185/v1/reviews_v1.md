# Peer review - Round 1

Editors:
- Geoffrey Schoenbaum, National Institute on Drug Abuse, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31185.029](https://doi.org/10.7554/eLife.31185.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Computations for altered attribute representations underlie cognitive regulation in altruistic and healthy choices" for consideration by eLife. Your article has been favorably evaluated by Michael Frank (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, the authors explore the ability of goals or attentional focus to modulate choices in a food task and in an altruism task. In the tasks, subjects chose or rejected different foods or different monetary offers. Instructions to choose healthy or to make generous choices modulated the behavior in both tasks and also affected neural activity patterns measured using fMRI. Regulatory success – or the ability to use instructions to change default choice behavior – was correlated with DLPFC activity.

Essential revisions:

One reviewer, not someone doing fMRI work, had significant difficulty simply following how the concepts of value versus regulation were operationalized in the task and analysis. What precisely were the conditions compared to isolate regulation for example from value? Describing this in more concrete terms would be helpful. This was related to the overarching concern of the other reviewers as well, which was the distinction between the authors conceptualization versus a more trivial interpretation – namely that when participants pay attention to a particular type of information (by instruction), this information is easier to decode from their brain activity. As noted below: "This effect should be seen as the outcome (and not the process) of cognitive regulation. How cognitive regulation is implemented, and how better decoding translates into biased choices, still need to be explained." Basically what is needed is to provide a more mechanistic account for what is going on.

Suggestions are given in reviews below. For example "it would be important to show that the decoded value (i.e., the decoder output) correlates with the behavioral weights. The alternative would be that changes in decoding accuracy correspond to changes in precision (i.e., signal-to-noise ratio) and not changes in the signal itself. If correct, this would mean that a region downstream to the DLPFC could just read this value, add it to other values corresponding to other attributes, and feed the aggregate value to a selection process that makes the decision. Perhaps functional connectivity could be used to test for such a transfer of information. Thus, the neural model would parallel the behavioral model."

Another suggestion was that some sort of functional connectivity analysis could clarify how DLPFC (and potentially rTPJ) enables successful regulation mechanistically, possibly using additional ROI analyses on VMPFC to ensure this is indeed the case.

These are the essentially revisions or problems identified in our discussion – clarify the approach and provide a more mechanistic account of the proposed interaction to rule out trivial explanations of the findings.

Reviewer #1:

I think the general question is of interest and the authors approach is quite novel to me. They are basically testing how changes in goals affect behavior. This is similar to the use of devaluation in animal learning theory tasks, but here they are using simple instructions in the course of training with humans. I think this is a creative way to integrate economic decision making, which focuses on a unitary utility as guiding choices, with work from experimental psychology and computational neuroscience, which typically distinguishes different sources of information by its associative basis or computational basis. This is excellent.

However, beyond that I had difficulty following the authors framing, predictions and understanding the outcomes of the neural activity analysis. The DLPFC is the key "regulatory" area. But what does that mean? It seems to me that I would expect some areas to represent value independent of goals and some areas to represent that value only when goal relevant. Is this what is meant by regulatory? Does the DLPFC represents value relevant to goals and some other area does not – VMPFC?

Generally I think the question is very interesting and the approach is attractive, but I simply could not follow how the authors framed and then conducted their analysis. I will be interested to see what the other reviewers say. I might grasp things better if it were more clear how the theoretical concepts were operationalized for the analyses – precisely what is "regulatory" for example and how is it distinguished from non-regulatory versus just not involved by the task and then in the data analysis.

Reviewer #2:

Tusche and Hutcherson present a thought-provoking and methodologically impressive study on cognitive regulation of dietary and altruistic choices, a topic of broad interest. The analyses, which combine a drift diffusion computational model of attribute-weighted choice and trial-by-trial MVPA decoding, are sophisticated, appropriate, and comprehensive. They show that while attribute values across choice and regulatory goal contexts can be decoded in VMPFC, they do not appear to be modulated by regulatory goal. Conversely, attribute values in DLPFC are modulated consistently with model-derived behavioral weights across regulatory goals that emphasize either healthiness or tastiness during dietary choice, and personal gain in altruistic choice contexts. Regulatory goals that emphasize another's benefits (e.g. feelings), however, could instead be decoded from right TPJ and precuneus, but not DLPFC, suggesting representations of others' wellbeing is modulated according to the prosocial regulatory goal but only when it requires theory of mind. These findings speak to both the domain-generality and domain-selectivity of cognitive regulation of decision making and importantly advance our understanding of the neural systems important for cognitive control and decision making more generally. In general I am supportive of this paper but think some outstanding issues could be better addressed to confirm some of their interpretations and rule out others.

It is notable that DLPFC flexibly encoded values of tastiness, healthiness, and $Self but not $Other or $Fairness on the one hand but strongly predicted altruistic choices on the other hand. Is the DLPFC prediction of altruistic choices then mediated especially by the change in $Self during altruistic choices, but not the change to $Other or $Fairness?

A related question: Do the rTPJ and precuneus group effects predict individual differences in regulatory success during altruistic choices when goals depended on another's thoughts or feelings? Such evidence would tie together their argument that these latter regions "assume responsibility" for regulatory success when DLPFC does not because of the component process required to meet that goal.

Given the prior literature on this topic, and in order to rule out a model whereby VMPFC value representations are modulated in an attribute-specific manner that depends on regulatory goals, it would be informative to see an ROI-based analysis of VMPFC. I may have missed something but I could not find one. The ROI from the conjunction presented in Figure 3 could be used or prior literature could be used.

One question which is unclear from the conjunction analyses is whether it is the same neural code (e.g. in DLPFC) that is used across task contexts, or whether the code is distinct (context-dependent) but found in the same brain region. What do the authors find if the SVR is trained on one attribute (e.g. tastiness) and tested on the other two (e.g. healthiness and $self)? Can the overlap between representations be better visualized?

It would be informative to visualize the feature weights for the key areas (e.g. VMPFC, DLPFC) across voxel space in every subject. This procedure should help to assess to what extent any decoding effects are due to hard anatomical boundaries between subareas (e.g. dorsal and ventral aspects of DLPFC) or to distributed patterns within areas.

How do the authors interpret the altered representations in some primary sensory and motor areas, e.g. less strong decoding of tastiness values for NC than HC and TC? Have the authors considered a model whereby coupling between DLPFC and distinct regions of sensory cortex is modulated according to the regulatory goal? The DLPFC must get its attribute representations from someplace.

The one comparison in which a match with the behavioral analyses failed to emerge was for ethical considerations compared to normal or personal considerations. I do not view this null finding as problematic, but out of curiosity do the authors have any thoughts as to what is going on when regulatory success depended on changes to fairness due to the goal of complying with social norms? This null finding should be addressed in the Discussion.

Reviewer #3:

In this manuscript, Tusche and Hutcherson report an fMRI study on how cognitive regulation affects the neural representation of choice-relevant attributes. They look for mechanisms that may generalize across two types of choices, one involving conflict between healthiness and tastiness of food items, the other involving conflict between self-interests and altruistic concerns. In different conditions, participants are asked to focus on one or the other attribute, which regulates the weights assigned to the targeted attributes, as shown via computational modeling of choice data. The key findings are the links between these changes in attribute weights and the decoding accuracy obtained for these attributes using multivariate pattern analysis (MVPA) in various cortical regions. The results are quite convincing, with successful decoding across tasks and individuals. There is no clear conclusion about whether the regulation is centralized or distributed though, since changes in decoding accuracy are observed in the DLPFC for most of the attributes but not all.

The role of cognitive control in economic choice is poorly understood and this study brings valuable insights by applying MVPA to standard choice paradigms. My main concern is the absence of a mechanistic account linking brain activity to behavioral output. In a sense, the results seem a bit trivial: when participants pay attention to a particular type of information (by instruction), this information is easier to decode from their brain activity. This effect should be seen as the outcome (and not the process) of cognitive regulation. How cognitive regulation is implemented, and how better decoding translates into biased choices, still need to be explained.

For the latter point, it would be important to show that the decoded value (i.e., the decoder output) correlates with the behavioral weights. The alternative would be that changes in decoding accuracy correspond to changes in precision (i.e., signal-to-noise ratio) and not changes in the signal itself. If correct, this would mean that a region downstream to the DLPFC could just read this value, add it to other values corresponding to other attributes, and feed the aggregate value to a selection process that makes the decision. Perhaps functional connectivity could be used to test for such a transfer of information. Thus, the neural model would parallel the behavioral model.

Other points:

- The correlation across individuals could reflect compliance to the instructions rather than self-regulation capacity. The arguments taken from subjective report and from body-mass index are quite weak. For subjective report it could be that the rating scale is not reflecting the propensity to comply with the instructions. For body-mass index the opposite correlation could be expected: those who regulates food intake in real life should not need instructions in the lab.

- The observation that all attributes are represented in the VMPFC but inaccessible to cognitive regulation is super interesting (and novel, to my knowledge). The dissociation with DLPFC should be more emphasized and discussed. Would this mean that VMPFC representations are closer to stimuli and DLPFC to responses?

- To compare the pattern of attribute weights and the pattern of decoding accuracy across conditions, the authors intend to reproduce significance of pair-wise comparisons. As they know this approach heavily depends on the statistical threshold, which may be matter of debate when multiple comparisons are made. I would favor a straight regression of decoding accuracy against weight (across conditions).
