# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12248.031](https://doi.org/10.7554/eLife.12248.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A mathematical model explains saturating axon guidance responses to molecular gradients" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present an interesting model to explain turning of growth cones as a function of a guidance cue gradient in vitro. At its core is a principle based on anchor points. All of the reviewers thought that this was interesting work of modeling and experimental interaction to understand why axons turn relatively weakly in response to attractant gradients. However, various aspects of the manuscript gave the reviewers pause, and need to be addressed. They are:

1) To confirm the biological basis and interpretation of the essential part of the model regarding anchor points. Specifically, to address the following questions:

A) Are or are not the authors’ own SCG neuron imaging data consistent with any stiffness, tension, drag or pull of the axon between an anchor point and the growth cone?

B) Do anchor points exist and interact with the mechanics of the axon in specific (and testable) ways?

If answers to the above cannot be definitive, then it should be made clear what experiments are motivated by the work. If not, the authors need to address whether such a model is still of use if anchors are an incorrect assumption.

In essence, the questions on the behavior of their SCG neurons or the question regarding the anchor point existence more generally need to be addressed with data.

2) To tone down overly strong statements. Specifically, see comments by reviewers# 2 and 3 below.

3) To address technical and manuscript issues (see comments from all reviewers below).

Reviewer #1:

Various aspects in the modeling were confusing/unclear.

1) In the “Modeling growth cone trajectories” section, it is not clear how θ(t)=a/a+b ϕ(t) equation comes about. Also, it does not make sense to compare 's' (fixed speed) and 'L' (distance of the growth cone) with s<<L as they are not equivalent in terms of units. Further down it is stated s approx Lt (which does make sense in terms of units). It can't be both.

2) At the end of the section “Modeling growth cone trajectories”, the power law is not clear to me – there seem to be an exponential (10^) aspect missing in the integration of the above equation?

3) In the second paragraph of the section “A correlated walk model of growth cone trajectories” (Results), 's' is used for a length – clearly there is some confusion in the presentation.

4) Figure 1C caption is a bit misleading to say 'different combinations of a and b' when a is fixed at 1.

Overall, I think Figure 1 should be expanded and/or modified. This would probably help together with the equations too, which need clarification. For example, I found the D part could/should illustrate the gradient in some way – it is there in the A part only? Perhaps there can be an additional panel that combines these in some way. Also, it would be nice to show part E for other a, b values. Maybe the authors can take the reader completely through with, say, two sets of a, b values, and then show several parameter value sets as done in parts C and D. I found it confusing as set down and had difficulty visualizing/thinking about the trajectory process. For B part, symbol for turning angles could be included/introduced from equations.

In essence, combine equations and figures more effectively and with a step through for one set of parameters, before showing a collection. Similarly, in Figure 2, the A part shows one set of parameters and the B part, 3 different sets of parameters.

I further think that it might be nice to see the full process for a set of parameters (a, b) with and without noise on the same plot (i.e., Figure 1D and 2A aspects).

In general, equation details need to be clarified, and the figures modified to better help the reader understand the model.

5) Figure 12 – in introducing more anchor points to the model, a parameter 'r' is introduced. However, I could not find it anywhere in the equations. Please explain/show how this is included in the modeling.

Reviewer #2:

Technical questions:

Growth cone angle and 'attractant gradient' are independent terms in equation (Athamneh and Suter, 20151). This surprised me, because I would have thought growth cone angle would move toward the attractant and thus be some function of attractant gradient. Could the authors provide some explanation of why they chose to model things this way?

Saturation of turning is explained nicely by a persistence term in the model, which the authors relate to the axon tension and the limited number of 'anchor points'. Another explanation that crossed my mind is that the receptors in the growth cone that sense the attractants themselves saturate. Could this possibility be addressed or ruled out, even as a discussion point?

Axon stiffness might also play a role in persistence. It would be nice if the authors could comment on this.

Finally, how do the concentrations of NGF relate to what is known about dose-response relationships of trkA receptors, e.g. do the gradients approach a saturating concentration?

Manuscript issues:

There are a number of labelling issues in later figures (e.g. missing axis label in Figure 12H, and reference to empirical distribution that was not plotted in Figure 10D). A thorough check of the figures and labelling would be a good idea.

The unit of replication 'n' is not defined. The authors should clearly state how many experiments generated this dataset and what the unit of replication is. Accordingly, statistical tests should state the number of degrees of freedom.

Issues of clarity/presentation:

This article should in principle appeal to a large cross-section of biologists, including developmental biologists with little or no mathematical background. Though the authors have done a good job of explaining what they did in words, it would help to be even clearer in places, e.g. the curves labels in Figure 12H are not very user-friendly. Reminding the reader of the meaning of terms a, b, r, σ, etc. would also help.

Some of the statements are unnecessarily strong (e.g. "Without such a model, it is impossible to determine if trajectories observed in vivo are in fact consistent with gradient guidance" or the statement in the Discussion that the paper "resolves" an outstanding question).It certainly helps resolve this question, but it raises more questions as I have outlined in these comments. Softer language will get the message across and is less likely to put off readers with preconceived ideas.

Reviewer #2 (Additional data files and statistical comments):

Please clearly state unit of replication and degrees of freedom in statistical tests.

Reviewer #3:

1) I am not convinced that the anchor point model is a good model for growth cone turning behavior. There is no evidence that growth cones perform stepwise turning with respect to an anchor point. In the Discussion, the authors describe: "New anchor points could be established when tension is too high, or when it becomes too energetically expensive to drag the neurite." However, I am not aware of published studies that show growth cones physically 'dragging' a neurite (please direct me to such evidence if incorrect). The anchor point idea indeed predicts that the axon between the growth cone and the nearest anchor point should be 'dragged' into the direction where the growth cone moves. Of course, if the anchor point is far away (paper quote: 'the in vitro data we have presented here was well-fitted by assuming the only anchor point is where the axon emerges from the soma'), then a lot of axon would need to be dragged indeed. What would the stiffness of that axon be? The authors acknowledge that the in vivo environment will be more 'complex', but only by assuming there may be more anchor points. Not surprisingly, a closer anchor point allows sharper turns and results in more variability. This simple conclusion is actually one of the major conclusions of the paper.

In summary, I think the anchor point model may be a good idea, but there is precious little evidence supporting it. I am with the authors that a simplification to an elegant in vitro system is a good approach and I would not look for further in vivo relevance, if the in vitro behavior were to fit the model. But if there is an in vivo or in vitro neurite that actually drags an axon between the growth cone and an anchor point, the reader really needs to be shown one. To my knowledge it is more likely that most axons, including in the SCG culture, lay behind the moving growth cone without experiencing any force or tensions required for provide feedback from a hypothetical anchor point. If there is no such feedback, the core of the model cannot be supported.

2) A key prediction of the anchor point model is the tension on the axon between the growth cone and the closest anchor. If such evidence exists for at least some instance, in vivo or in vitro, I can and should be convinced that the model is applicable. This is a true prediction of the core of the anchor point model. In contrast, the measurements provided on the turning speed and the 'saturation' of turning are not true predictions of the model more than they are the basic data the drove the generation of the model in the first place. For example, the authors describe this 'long-standing mystery' many times, use it to justify the model, and then present the data that was used to make the model in the first place as: 'the average turning angle reached the steady state quickly and did not increase significantly with time, matching the prediction of the model (Figure 4C)'. This is a clear case of a model that was made to fit the data. There is no true prediction of the model (one that would not have been possible before running the model) that is tested in the paper. The authors consistently use the wording 'predicted by the model' to describe an outcome of the anchor point model that fits data past or present. Again, I could and should be convinced when, for example, evidence for a real existing anchor point (even just in the SCG culture) were provided, predictions based on tension of the axon, its predicted stickiness to the substrate (as discussed by the authors), etc.

3) I read this study as a purely hypothetical model based on previous data and some new measurements in the SCG culture using a microfluidic device. Links to biology are present only in the Discussion and as speculations (e.g. focal adhesions), but neither integrated into the model, nor tested in experiments. As it stands, the anchor point model clearly reproduces some significant behavior or growth cone turning in vitro. However, the statements in the Abstract that ‘this model explains the long-standing mystery…’ and that ‘this work introduces the most accurate predictive model […] and deepens our understanding of axon guidance events both in vitro and in vivo’ appear to me quite dramatically overstated.

4) Manuscript issues:

In the section related to Figure 9, the authors measured the bearing angles, step sizes, and mean step sizes of individual growth cones and fitted all these parameters by different distributions. However, the explanations of what these different distributions mean in a biological context is inadequate.

In the subsection "SCG neurons were guided in the microfluidic assay", the authors took into consideration only the axons that made an angle between 70° and 110° with the gradient direction since they expected impact of the gradient would be strongest on these axons. The reason behind this expectation is not well explained. Also, although Figure 4A is referred after this expectation, Figure 4A does not show anything related to this.

Did the neurotrophin gradient majorly influence branching or retraction? Those events were discarded and not compared to the gradient control.

In the section "Modelling growth cone trajectories", "s" is referred as constant speed but in the section “A correlated walk model of growth cone trajectories” it is referred as length of a step.

To test whether fluid flow has any effect on statistics of the steps authors divided the axons in 4 quadrants but how this division helps understanding the effect of fluid flow is not clear.

In Figure 3, please indicate which directions are set as 0° and 90°. Also part E and F can be shown on the same graph.
