# Peer review - Round 1

Editors:
- Timothy EJ Behrens, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12192.019](https://doi.org/10.7554/eLife.12192.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A common mechanism underlies changes of mind about decisions and confidence" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Timothy Behrens) and David Van Essen as the Senior Editor. One of the three reviewers has agreed to reveal his identity: Mark Goldman.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper follows previous papers by the senior authors on decision-making tasks involving an accumulation of evidence, and corresponding models for accuracy, reaction time, and confidence judgments. This paper makes major new contributions to these problems, particularly with regard to the issue of confidence, and whether confidence judgements can be naturally explained in the same framework used to explain accuracy and reaction time. The authors use a very clever experimental paradigm for human psychophysics, in which the direction a lever is moved lets subjects not only indicate their choice (left or right) but also whether this choice has high or low confidence. As a result, both changes of choice and changes of confidence can be seen by changes in hand movement.

All of the reviewers had praise for the manuscript, describing the paradigm as elegant and clever, the paper as insightful and the contribution to the state-of-the-art as important because of the unification into a single framework of decisions and meta-decisions, which have preciously been treated as separate entities. They note that there is clear structure in the data in support of a common driver of these variables such as the model-free analyses of motion energy.

The reviewers, however, suggested that the paper should not be published without some essential revisions (that do not require additional data).

Essential revisions:

First, there were concerns about the extent to which the common mechanism argument was a complete description of the data

Two reviewers raised a related point on these lines.

1) The model fits in Figure 2 show a good fit to accuracy and RT data (panels A and B) but a poorer fit to the proportion of high confidence responses (C), particularly for error trials. E.g. subject 1 has only two (out of 6) error-trial data points situated near the fitted line, and only one data point for subject 2 (part of the issue in realising this is that the purple error trial points are often hidden behind the green correct trial points, it would be useful to jitter these sideways for visualisation). This is the case even though there are several hundred error trials particularly at lower coherences with correspondingly tight error bars on confidence proportions. This discrepancy is particularly apparent at 0% coherence, where subjects 1, 2 and 4 show substantially lower confidence than predicted by the model. I'm not suggesting therefore that there can't be a common mechanism that does a good job of explaining all these data features (e.g. perhaps subjects are inferring on coherence, leading to lower confidence at 0% than predicted by a model that marginalizes coherence?). But it seems reasonable that a putative common mechanism driving choice, RT and confidence should do an equally good job of explaining each feature separately.

2) First, it is not clear to me what data could not be fitted by their model, given multiple fitted parameters per subject. It would be nice to see how a model with a separate "confidence-generating" and "decision-generating" circuit would produce data that would not be fit by their model.

3) I do agree though that using Occam's razor, fitting by one model circuit is preferable to two. However, Figure 2C shows a horrible fit of the model to the 0% coherence data points in a systematic direction across subjects. This suggests a systematic problem with the model, but the authors do not mention this discrepancy.

4) There was agreement in the reviewer discussion that simulation of competing models to demonstrate how the data disconfirm a model that does not rely on a common mechanism would be important if the argument is to shift broader opinion. The reviewers regarded such a demonstration as essential. One suggestion during the discussion was as follows: "Perhaps a simplification of their model and then use of Model comparison techniques to adjust for different numbers of parameters would be a good test to show that a separate computation is needed for confidence as they claim."

Related to these concerns, was a concern about data exclusion.

5) This worry is compounded by the exclusion of data that shows aberrant confidence behaviour. One subject was excluded for a strong high-confidence biasand absence of confidence-accuracy correlation, which is indeed at odds with the proposed mechanism linking choice and confidence, but perhaps not with other models. Similarly the second half of subject 4's data is excluded because they changed the way they reported confidence half way through the session. These exclusions seem to unfairly skew the playing field in favour of the authors' single-mechanism account, particularly as the remaining subjects' data constitute only a little over half of all data that was originally collected.

During the discussion it was made clear that although it is understandable that subjects may have effort-related or other biases that make the data uninteresting, it is a concern when this is 2 of 6 subjects, and it is a concern that the particular exclusions seem to act in your favour. Because of this, it was thought to be essential that the excluded data were presented in the supplement, and that the reason for the odd behaviour was investigated and described.

6) There was also an important question about perceived asymmetries in model that the reviewers required clarification about. It was unclear why you switch between working in accumulator space and log-odds space. In the discussion, it was agreed that it might be possible for you to clarify in the text if there was a strong and compelling reason, but if not then it would be interesting to see a symmetric model.

My largest comment is that, while confidence and decisions are clearly put together in a single framework, I found the framework to be a little awkward and/or unclear in what information/type of model informed decisions versus what informed confidence. The authors use a classic "race to bound" model to inform the decision. However, then they appear to use a separate probabilistic judgment (log odds, or maybe log odds ratio-this was a bit unclear) for confidence and for changes of decision and confidence. This seems awkward: why not just use the log odds metric for all stages of the task instead of artificially making a race to threshold for two completely independent integrators for the decision and then a separate probabilistic framework for confidence and changes of decision?

Or, maybe I am misinterpreting the log odds graph and this could simply be interpreted as a one-to-one mapping between the decision variable and the log odds (so that one could indeed reformulate the race to bound in the decision variable as a race to bound in log odds). If this is the case, then I find the log odds measure for change of choice to be somewhat strange: in the race to threshold model, there are two completely independent accumulators that are racing against each other. In the log odds analysis, it would seem very awkward if only the odds for the initially winning accumulator was used (i.e. I'm assuming either the authors are using odds or odds ratios based upon using both accumulators, or they are just using the winning accumulator, since the figures only indicate a single trace in log odds). If only the winning accumulator is used, then it seems strange that the losing accumulator was never consulted on a change of choice, i.e. that this change of choice was solely driven by a change of log odds in the winning accumulator.

So the bottom line is that, at least as written, it appears to me that one of two awkward modeling choices is occurring:

A) The decision variable is determined by 2 independent integrators of a decision variable but confidence and changes of decision are determined by an odds ratio that combines the 2 integrators, in which case, why wasn't the initial decision made based upon a measure that combines the two integrators, rather than having this sudden switch between what determines the decision?

B) The log odds are determined only by the winning accumulator's log odds, in which case, it seems odd to have a change of choice that occurs without consideration of the new winner's accumulator.

Finally, there were several important points that do not require more analysis but that the reviewers thought merited serious consideration and discussion:

7) The evidence for separate mechanisms includes a correlation of confidence parameters across subjects when completing distinct tasks that is not seen in the decision-making parameters. The model in this paper seems to be distinct from that – it seems that one would expect the low-high confidence boundaries to remain intact but the decision boundary to change when a new task is performed. Hard to imagine why this would occur in one model, so this issue should at least be discussed.

Perhaps the authors data do explain this, but it is unclear to me – there is a well-known "high-low effect" whereby subjects are more confident than they should be at hard decisions (low coherence) and less confident than they should be at easy decisions (high coherence). My intuition is that if a decision is made yet more information affecting confidence is received post-decision then that extra information would more likely favor the decision (so boost confidence) in easy decisions but as often as not favor the non-chosen target (so reduce conference) in difficult decisions. Is this effect accounted for in the authors' framework? The universal increase in log-odds ratio shown in Figure 7 suggests not (but I have not gone through the calculated effect here so may be wrong).

8) In trying to think through the arguments about the amount of stimulus time not affecting the initial decision, I started wondering about a related time scale that I'm not sure was considered: how long does it take to reverse an already begun motor action? If this takes a long time, then it seems that there may be a very narrow window to actually accomplish a change of mind reflected in a hand movement direction change. Is this accounted for implicitly in the time scale arguments and model for the deadline for change of mind, i.e. can the state of belief at tpip actually turn around the hand this late into the process?

9) I think the authors should mention and compare their model with a recent paper by Wei and Wang (J Neurophysiol) which purports a biophysical mechanism that produces similar results. I think one discrepancy may be the confidence in errors (Figure 2C) being of incorrect trend in their model.

With respect to this final point, note that in the reviewer discussion it was made clear that we do not intend you to code up the Wang model, but instead to discuss the likely similarities and differences.
