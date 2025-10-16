# Peer review - Round 1

Editors:
- Erin L Rich, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78205.sa0](https://doi.org/10.7554/eLife.78205.sa0)

This study analyzed viewing behavior in monkeys during value-based decision-making to determine whether relationships between gaze patterns and choices previously described in humans are also present in monkeys. The study used a clever task design and sophisticated modeling approaches to reveal robust evidence for similarities to extant human data. This is important to the field because it suggests common neural mechanisms linking viewing behavior and decision-making, which can now be further explored across species.


---

# Peer review - Round 1

Editors:
- Erin L Rich, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78205.sa1](https://doi.org/10.7554/eLife.78205.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Monkeys exhibit human-like gaze biases in economic decisions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Below are three specific points, distilled from the attached reviews, considered essential revisions for the authors to address. The individual reviews appended below can be consulted for further elaboration on these points and additional suggestions to improve the manuscript.

1. A general concern is that the value associated with an item can potentially attract gaze independent of choice, and reviewers felt that these relationships should be considered in more detail (addressed primarily by R1 and R3). On one hand, given a limited set of values, value difference is highly correlated with both the options and the chosen value, and it is suggested that the authors attempt to disentangle these in their results. Similarly, effects on fixation duration should be explored in more detail, including whether they relate to only one of the option values or both, and how they vary when there are 2 versus 3 fixations in a choice. Finally, it was felt that there should be additional discussion of the complex interplay in which a valuable item attracts attention and attention to an item may also increase its subjective value, and the extent to which these possibilities are disentangled or confounded in the current data. (Note that this final concern may be somewhat addressed by the analyses suggested in point 3 below).

2. A second concern is that the approach to "non-decision time" was viewed as arbitrary and perhaps not entirely valid (addressed primarily by R2 and R1). The current approach assumes that final and non-final fixations should be the same length, although other work has shown that final fixations are generally shorter. It also assumes that motor preparation time is equal across all chosen values, although higher values typically motivate faster motor responses. Point 3 below makes a suggestion about how to consider NDT in alternative choice models. Other potential approaches to address this concern within the present model include testing different estimates for NDTs and demonstrating the robustness of the overall results.

3. Finally, reviewers felt that the study would be strengthened by additional exploration of their data in light of studies that assess whether gaze might directly increase drift rate (i.e., gaze is additive to value), rather than (or in addition to) multiplicative effects, where gaze amplifies the attended value. (See Cavanagh et al. 2014 JEP General, Gluth et al. 2018 eLife, and Smith and Krajbich 2019 Psych Sci.)

Specifically, Westbrook et al. (Science, 2020) suggested a hybrid two stage model whereby gaze is multiplicative on value early during choice and additive later, with a rationale similar to that discussed here ("post-decisional gaze anchoring" – see also recent work by Callaway et al. 2021 PLoS CB for a related but more continuous model). The central assumption of GLAM is that gaze weights the impact of value on evidence accumulation, but given the issues regarding NDT, considering other models in one way or another is important, and the authors have the trial counts to do so quantitatively. Thus, the authors should address the issue of whether gaze effects in monkeys are multiplicative as assumed by GLAM, or whether they might be additive when applied to the data. There was extensive discussion on this topic in consultation, and indeed there is evidence for both in the human literature. Clearly, publication decisions will not depend on the conclusions of this exploration per se, but a strength of the current data set is that it may be able to speak to this unresolved issue.

One consideration in undertaking such an alternative model analysis is that it could be done with and without truncating NDT (so that NDT would be captured by the second phase of a 2-phase model) and/or by better justifying the choice of NDT. Moreover, it was felt that a model/parameter recovery analysis is a critical component of these explorations. In other words, if Model A "wins", simulated data from model A should be able to reproduce key features of the data that Model B cannot capture, and vice versa and parameter estimates should be recoverable when fitting to those data (see Wilson and Collins 2019 eLife).

Reviewer #1 (Recommendations for the authors):

Critique 1: The authors should consider the possibility that unique option values can explain putative effects of value difference. One approach might be to subselect trials and analyze data sets where chosen value varies but value difference is constant and vice versa.

Critique 2: The concern about whether effect first fixated values carry over into behavior during the second fixation could be addressed similarly to critique 1 or with model comparison approaches.

Critique 3: The authors should consider whether a more flexible definition of NDTs could better fit behavior. This concern might also be addressed in approaches to critique 4.

Critique 4: The concern in this critique is that value and choice can have influence on gaze behavior (and drift rates) that is not accounted for by the present models. Addressing this would involve more extensive re-analysis than the previous points, however given that the contribution of this paper is showing that monkey behavior recapitulates what has been reported in humans, I think it is warranted to explore more complex interactions between gaze and choice that have been found in humans subjects. To address this concern, the authors should consider comparing the present results to models that allow the γ parameter to vary with specific task parameters (for instance as in Westbrook, 2020).

Reviewer #2 (Recommendations for the authors):

It seems a little silly to expend all this effort generating bootstrapped distributions of final and non-final fixation differences, only to then arbitrarily choose the 95th percentile of that distribution as the terminal non decision time. Why not instead either simply get the best estimate you can from the literature, and/or demonstrate the robustness of the results to different non-decision time corrections (e.g. 0, 200, 400 ms)?

Regarding the manipulation where onsets were staggered: the analysis here seemed convoluted. Why not directly test whether subjects were more likely to choose the initially presented option? Figure 3 helps to address this, but leaves some ambiguity for Monkey K, who doesn't always initially fixate on the first presented alternative.

It may be worth noting that the effects in Figure 5 appear to be smaller than in most human data. This might be an argument for 'not' cutting the last 200ms of each trial?

On page 28 the authors discuss Krajbich et al. 2021 and argue that their findings are consistent with LIP, frontal eye fields, and the superior colliculus accumulating evidence in studies where eyes are used to report decisions. However, that study was like this one; subjects were free to look around but they chose using the keyboard.

I thought the authors missed an opportunity to discuss some of the human neuroimaging work on value-based SSM, given the focus of their Discussion section. There are a number of well-known articles that are relevant, for example:

Hare et al. 2011 (PNAS); Gluth et al. 2012 (J Neuro); Rodriguez et al. 2015 (European J Neurosci); Pisauro et al. 2017 (Nature Comm).

Why did the authors use different delays for the two monkeys?

How long were the delays between releasing the center lever and pressing left or right?

Was there some criterion for passing the training stage?

p.33-34 – these numbers should go in the Results section, not the Methods.

I think it might make sense to include session-level random effects in the models, given that each session used a different set of stimuli. I doubt this will change much, but it might further help clean up some variance.

p.38 – This argument about how early gaze might be used to explore and evaluate targets while late gaze is used to focus on the to-be-chosen target comes nearly straight out of Westbrook et al. 2020 (Science).

Reviewer #3 (Recommendations for the authors):

I would have liked to see a more extensive discussion of what might underly the observed effects. The sequential sampling models are merely descriptive. One would like to know how fixation influences the neural signals that compute the value of the option. When a human/monkey is looking at one option, information about a previously viewed option must be maintained in working memory and the neural signals might be expected to be noisier, leading to a bias towards the most recently viewed option. Similarly, the first viewed option might have a stronger signal than the second viewed item by virtue of having less interference. This is obviously speculative but it would be nice to see what evidence there is for something like this – indeed the McGinty et al. 2016 paper seems to provide evidence of this kind. One could argue that it shouldn't be too surprising that computations performed at the fixation point are higher S/N than ones off fixation. (In the context of the sequential sampling model this would correspond to adding some noise to the item not currently fixated.)

Related to this, the discussion of how the paradigm might be used for further exploration is a bit vague. The example given of MT and LIP is not particularly well chosen, given the recent evidence from the Huk lab (Katz et al., Nature 2016) against LIP as the site of the perceptual decision.

Another general concern is the absence of any discussion of all the work showing that value associated with an item serves to attract gaze and indeed is a central aspect of the mechanisms of gaze control and learning where to attend. One closely related example is the work of Hikosaka (eg Kim et al., Cell, 2015) showing that cells in the caudate tail coded the value of previously rewarded fractal patterns and attracted gaze. This makes the question of causality a bit difficult to disentangle. It's such a central issue that it needs to be explicitly discussed. Having the stimuli not resolvable in the peripheral retina helps with this issue.

I would also like to see more of the actual fixation time data. If there are only two fixations, having a bias towards the first one viewed is in conflict with a bias towards the last one viewed. Thus it would be nice to see the fixation durations broken down into cases where there are 2 fixations and cases where there are 3 fixations. Just as the calculation that the initial-view bias is equal to about half a drop of juice, it would also be useful to know how fixation duration translates to choice bias. If I am understanding Figure 4 correctly it looks like an extra 200 msec viewing time translates to about a 10% increase in choice probability. More concrete description of the fixations would be helpful. For example, how do the β values on p8-9 translate to fixation durations?
