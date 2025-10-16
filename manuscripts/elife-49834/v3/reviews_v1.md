# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49834.sa1](https://doi.org/10.7554/eLife.49834.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study investigates how past choice history influences decisions that, in principle, should be guided just by currently available sensory information. It combines two classic approaches, perceptual decision making and reinforcement learning, to show that the success of prior choices and the quality of the perceptual information guiding them are automatically tracked, and that both factors are used to bias upcoming choices that are difficult, i.e., those for which the quality of the sensory information is poor and the subject is largely guessing. The effect is robust across sensory modalities, species, task details, and labs. It explains an important source of variance in behavior.

Decision letter after peer review:

Thank you for sending your article entitled "Confidence-guided updating of choice bias during perceptual decisions is a widespread behavioral phenomenon" for peer review at eLife. Your article has been evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor.

All reviewers found the work interesting and appealing. However, some potentially

serious issues were identified that could undermine the main conclusions. The full set of recommendations is below. Please focus your revisions on points 1, 2, and 4, which are most critical.

Essential revisions:

1) The first major concern is in regard to a claim made throughout the paper, namely that how easy or hard the current stimulus is affects the strength of the modulation. This is first presented in Figures 1F and 1G, and then repeated in almost all the figures. However, the measure presented in figures of the style of Figure 1F and summarized in Figure 1G is the% change in responses (given a particular current and previous stimulus, and relative to the overall average for that stimulus). This measure suffers from a large problem that, unfortunately, appears to not be addressed (apologies if it was missed on reading): there is a ceiling effect, in the sense that when a choice is easy (near 100%) it cannot increase further, even if there were strong underlying plasticity. The ceiling applies preferentially to easy stimuli, and therefore will manifest as a difference between easy and hard stimuli. It is currently impossible to tell whether the data shown in support of the claim of "current stimulus strength modulates effect" is merely an artifact resulting from this ceiling issue, or an actual finding. It is very important that the authors clarify this issue.

2a) Another key claim is that only the model with a belief state could account for the results. But the data are not convincing. Let's start with a TD model, without learning of actions, merely learning the values VR and VL, and let's suppose the value of VR is modified only after R choices (and similarly for VL and L choices). Under these conditions (and assuming R-L symmetry) VR and VL will converge to the overall% correct. This will be more than 50%; for a typical smooth psychometric curve it might be 75% or 80%. Now move to a TDRL model that also learns actions: because there are more errors for hard stimuli, the error signal (VC – r) will, on average, be greater for hard stimuli than for easy stimuli. And therefore, in this situation, there will on average be greater plasticity after hard stimuli than after easy stimuli, entirely without a belief state. Could this not account for the authors' experimental data?

The situation and conclusion sketched here could be wrong. But readers are likely to think about it and wonder whether it undermines the authors' conclusions. Thus, explicitly addressing this argument, and whether it is qualitatively or quantitatively incorrect, would strengthen the manuscript.

2b) A related concern is that, if we understand correctly, the model produces only step-function psychometric curves: for a given stimulus s, the response is deterministic, and when VR = VL, the model would produce 100% correct behavior. This might seem unimportant, since the details of the shapes of psychometric curves are not the focus of the manuscript, and replacing the distribution-based model with one that uses noisy samples might seem a trivial change. However, distinguishing between hard and easy trials is central to the arguments in the manuscript, and the corresponding difference in error rates might easily become important (as in the situation sketched in point 2a above). So a model that produces smooth psychometric functions (as opposed to step-shaped) might be important after all (and at least cosmetically would be an obviously better match to the data).

2c) The authors posit that the subjects use an internal measure of decision confidence to update their decision policy. In support of this claim, they show that a qualitatively similar modulation can be produced by a temporal difference reinforcement learning (TDRL) model with prediction errors based on perceived stimulus strength. In this model, the prediction errors are used to update the stored value of each choice. We found this model design counterintuitive. It seems that an equivalent model could be constructed in which prior stimulus probabilities (pR and pL) are updated instead. This would be more consistent with the fact that the animal always receives the same amount of reward on rewarded trials, but may have uncertainty about exactly where to set the decision boundary leading to trial-to-trial updating. It would be helpful if the authors reformulated their model, or explained why reward values are being updated rather than reward probabilities.

2d) The Bayesian model that updates stimulus statistics seems to ignore which choice was made in the previous trial or whether it was correct. That is, there is a built-in handicap of no feedback, compared to the confidence-based models. How much does this "handicap" contribute to the poor match between model predictions and data in Figure 9A?

2e) Model predictions should be comparable to real data. In Figure 2, the plots for rats' average performance show three levels of previous stim (%A) for each direction, more or less evenly distributed. In Figure 3, however, previous stim (%A) are 20, 50 and another value very close to 50. Does the model performance depend on the stimulus strength used? The same stimulus strengths used in behavioral testing should be used for model predictions.

2f) Parameter values used to generate Figure 3 should be reported.

3) More detail and clarity are needed regarding the description of the basic phenomenon (e.g., sorting and analysis of the shown quantities). The Materials and methods section should include a brief section on how the psychophysical results were generated. That could include all the details of what was conditioned on what, as well as how the trials were divided into "Hard" and "Easy".

Many of the key figures depict "updating% " and "updating index." These terms should also be mathematically defined in the Materials and methods.

The equation used to fit the bias, lapse, sensitivity of psychometric curves should also be presented in the Materials and methods. These parameters are said to be "stable." What is the criterion for determining stability?

Also, the trial nomenclature and labels used in Figure 2 (e.g., "Next" and "Previous") were confusing.

Do subjects also show adjustments of sensitivity after correct trials? Would a change in sensitivity contribute to the observed confidence dependence (e.g., if the psychometric curves are shallower, the difference in choice might appear larger for difficult trials)?

4) What happens after errors? The results demonstrate an effect akin to a win-stay strategy but limited to "guesses" only. Is there also a trend toward the corresponding lose-switch strategy? That is, when the choice in trial n-1 is difficult and not rewarded, is the subject more likely to choose the alternative option in trial n (when such decision is also difficult)? There is no obvious reason to expect that confidence-guided choice updating would not also happen after errors, but in any case, error trials should not simply be put aside. The authors should present an analysis of error trials and if they do not see the effect predicted by the model, should propose an explanation for the inconsistency. Other work from the same first author (Lak et al., 2017), presented an alternative TDRL model without the "belief state," which seemed to have qualitatively similar results for correct trials but divergent results for errors. It seems that error trials are needed again in order to rule out this other model.

5) Related to this: "The choice updating remained statistically significant even after this correction." True, but the effect did seem to get a bit weaker. I imagine this is because the history effects are not limited to one trial in the past, but possibly more. If so, you would expect the effect to become stronger when the current difficult choice is preceded by two rewarded guesses made in the same direction. Whether the trend is weak or not, it could be compared to the model's prediction.

6) The transfer of choice updating across modalities is interesting. Comparing Figure 2, 4C, and 8D, it seems that the updating is larger on pure olfactory tasks and about the same for the pure auditory or mixed tasks (this is more obvious in Figure 10). I assume the rats have different sensitivity to olfactory and auditory stimuli. Then the difference seems to contradict the statement that "updating is guided by outcome expectations, rather than stimulus statistics". How much updating was there for trials in the mixed modality task but without modality switches?

7) Figure 10B and C should show scatterplots separately for each task. The authors' hypothesis is that updating is independent of stimulus statistics. If this is true, it makes sense to pool data across tasks. However, if the alternative is true that updating depends on certain properties of sensory stimulus, i.e., there could be different relationships between updating and slope/lapse, which could be obscured by pooling across tasks. A more direct test would be to fit the model to one task and predict results for the other tasks.

8) In Introduction and Discussion, the authors seem to suggest that this phenomenon persists after training is completed or after the subjects performed the task for extended periods and thus may reflect some optimal strategy. Was the training specifically targeting the suboptimal bias? Or is it possible that the subjects just settled on a suboptimal strategy that satisfies the training requirements? It might be useful to clarify what criteria were used to deem these subjects "well-learned".

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Confidence-guided updating of choice bias during perceptual decisions is a widespread behavioral phenomenon" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, including Emilio Salinas as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Carlos D Brody (Reviewer #2); Long Ding (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript presents interesting, important data characterizing how past choice history influences decisions that, in principle, should be guided just by currently available sensory information. The results show that the success of prior choices and the quality of the perceptual information guiding them are automatically tracked, and that this information is used to bias upcoming choices that are difficult, i.e., for which the quality of the sensory information is poor and the subject is largely guessing. The work is significant because the phenomenon seems robust across sensory modalities, species, task details, and labs, and because the modeling results provide insight into the underlying associative mechanisms responsible for the biasing effects.

Essential revisions:

The paper is significantly improved, and the reviewers are now convinced that it contains important work that should be published. Nevertheless, the presentation of the data is still confusing, and some further clarifications would substantially strengthen the manuscript.

1) Explaining more in detail the fundamental difference between the standard TDRL model and the belief model would be important. Specifically, the updating that they generate during easy trials, and how that updating depends on reward, could be the critical reason why the standard TDRL model fails.

2) The control analysis that corrects for potential slow drifts in the internal categorical boundary may also be implicitly addressing a separate issue (whether the shifts in the psychometric curve depend on the previous trial outcome, i.e., rewarded vs. not rewarded). Making this distinction explicit would be helpful.

3) The zig-zag patterns of the main data plots can be confusing because sometimes it is unclear what matters, the slope, the discontinuity, or both. Some suggestions for modifying the plots are provided below. That and/or additional text to guide the reader to the relevant features of the data would be helpful.

4) Figure 4 is a very nice addition to the manuscript. However, the results do differ somewhat from the data and from those of the belief model. Does this simply reflect a fundamental, qualitative difference between the classifier and the other models? It would be helpful to clarify whether the classifier has parameters that can be adjusted.

Details about each of these points are provided below.

Reviewer #2:

1) Figure 3 TDRL model: In the previous round of review, we (the reviewers) presented an argument as to why the TDRL model would lead to updating that depended on previous trial difficulty. The authors replied that this model results "in updating which is independent of previous difficulty." I believe that response is simply not true: in Figure 3C left, one can clearly see a non-zero slope to the updating% on hard trials. (And Figure 3C right worries me no end: since in the TDRL model there are no slow side biases independent of outcome, I am unsettled by the correction for such biases changing the results of the model.) [Note that doing the zig-zag plots in the style suggested below for Figure 1G would focus the eye on that slope much better.] What am I supposed to focus on? That the slope is less than in the belief model? That the belief model reaches zero updating for the easiest previous trials?

I spent a lot of time trying to think this one through – if the TDRL model could indeed be described as accounting for the data, that would be a pretty bad hit at the heart of the manuscript – and eventually hit upon something that I think could help the authors. Assuming I'm not getting this wrong, perhaps the authors had already thought of this, but either way, the suggestion is that it might be clarifying to have it in the manuscript. Here's the idea: in the TDRL model, VL and VR converge onto the average reward given when the subject chooses those ports, where the average is over both correct and incorrect trials. In other words, VL and VR are the value of the port, averaged over all trials. But in the belief model, VL and VR converge onto the value of the reward when a reward is given. Not an average over all trials, but conditioned on the reward having been given. Thus if the reward r = 1, in the belief model, VL and VR will converge on 1. And that means that for very easy trials, the reward prediction error will be zero, and the updating will be zero. In contrast, in TDRL they will converge on something like 0.8; and thus even on very easy correct trials there will be a non-zero RPE and non-zero updating. I may have gotten this wrong, but if it is correct, there are two interesting things here: (a) the difference on what VL and VR converge to in the two cases, in the sense of one being reward averaged over errors and corrects, the other being average reward conditioned on trials being correct; (b) I believe the real difference between TDRL and belief is not that TDRL has a zero slope for updating versus previous stimulus (the non-zero slope is right there in Figure 3C). It is that TDRL will never have zero updating for the easiest stimuli, whereas the belief model will.

While on this topic: don't Figure 9E and 9H look more like TDRL in Figure 3 than like the belief model? Why are they being interpreted as supporting the belief model?

2) Subsection “Choice updating is not due to slow drift in choice side bias”: This confused me the second, the third, and the fourth time I read it. Eventually I realized that there may be two issues being treated simultaneously here. I think things would be a lot clearer if you separated them. Issue (a) is "are shifts in the psychometric curve contingent on the previous trial's outcome?" Issue (b) is "are there slow drifts in the decision boundary that would induce correlations across trials that would make one trial appear to depend on the previous one"? The thing that confused me is that to solve issue (a), the obvious and easiest thing is to compare two psychometric curves, both conditioned on a previous stimulus p, according to the previous trial's outcome, i.e., whether the previous trial was rewarded or not. That would be a really easy plot to make, understand, and interpret: if previous trial's outcome matters, it will be obvious. Why not add it to the paper?

Issue (b) is also interesting. The approach in Figure 2 addresses issue (b). If this section and figure were described as focused on issue (b), it would be a lot easier to understand.

3) Figure 3 model: the full model really needs to be fully explained, in the main text. Please use equations. In particular, while the sentences “Note that although the choice computation is deterministic, the same stimulus can produce left or right choices caused by fluctuations in the percept due to randomized trial-to-trial variation around the stimulus identity (Figure 3—figure supplement 1)” is a welcome addition, it is not enough. Please specify, in the main text, how pR and pL are computed. Note that the integral in subsection “TDRL model with stimulus belief state” needs to specify what you're integrating with respect to (it needs a "ds"), this would make it clear that pR is a function of ŝ, which is itself a random variable drawn anew on each trial. I suggest that you make this explicit in the equation, by writing the left-hand-side as pR(ŝ). (Note that I'm suggesting you bring this integral and some of the description into the main text.)

4) In the previous round, we requested substantial clarifications for panels of the type of Figure 1F and 1G. Even with the clarifications provided, I still find these panels hard to read.

– Figure 1F: this should be explained in a way that readers can understand without having to trawl through the Materials and methods. Here's my current understanding: (a) you plot the average psychometric curve; (b) you plot the psychometric curve conditioned on a particular previous trial stimulus p; (c) for each current stimulus c, you compute the vertical distance between those two curves, and that is what you call "updating".

Why not show this graphically directly, to make it easy for readers to understand? That is, something along the lines of: add a panel to Figure 1 where you show the average curve and the curve conditioned on p, add arrows pointing to the vertical differences between those two curves, and add an arrow from there to Figure 1F to indicate that these two particular curves and the vertical shift between them are what become column pFigure 1F.

Among other things, this would make it obvious why, if the psychometric curves asymptote at 0% and 100%, updating is necessarily going to be small for easy current stimuli. Which is why I don't like the plot of Figure 1F so much: the eye gets drawn to the dominant pattern, which is that the top and bottom row are lighter than the middle rows. But that's the unimportant part, that's the "expected" part, as the authors now write. The important part is happening in the middle rows. Could the authors think of a display format that focuses the eye on that, on the middle rows, instead of the already-expected parts?

– Figure 1G: The zig-zag pattern confused me no end. What is it that I'm supposed to focus on here? The difference between easy and hard? The fact that the pattern is antisymmetrical? The slope on the hard stimuli?

It eventually dawned on me that the "A" response and "B" response are of course anti-symmetrical with each other. For a model which has no intrinsic side bias, this has to be true. And there appears to be no systematic, overall, side bias across the experimental rat data in the paper. So the zig and the zag are actually redundant with each other.

I would therefore suggest the following: collapse the two with each other (the zig and the zag), which gives you better statistics, and in addition focuses the eye on the important parts, not the antisymmetry. In other words, instead of plotting as a function of previous odor A% , plot (% updating towards correct side) as a function of |A% – 50|. By halving the x and y axes, that would also allow you to zoom in by 2x, so readers can see the data better. (An added suggestion would be to plot the easy trials in a light grey, to emphasize that it's in the hard trials that the action is.) And then you'd have a plot that, at a single glance, tells the reader "there is bigger updating for harder stimuli".

Reviewer #3:

The authors addressed my earlier concerns. But their new data raised a new concern:

I think it is good of the authors to try another class of models to explain the data. However, the predictions of the statistical classifier in Figure 4D differ from experimental data in Figure 1G in three aspects: (1) there appears to be a strong dependence on previous stimul us strength for easy choices; (2) perhaps as a consequence, there is a large jump in Updating% going from green to blue at% A = 50; and (3) the range of updating% is only about half of the experimental data. It is hard to judge if these differences represent fundamental deficits of the model or just wrong parameterization. Because this model is not as intuitive as the RL model in Figure 3B, it would be helpful if the authors can expand this section (or add a supplemental figure) to give the readers a sense of how varying each model parameter changes the predictions.
