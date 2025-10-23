# Author response - Round 1

Authors:
- Huyen Nguyen ([ORCID: 0000-0002-5775-7915](https://orcid.org/0000-0002-5775-7915))
- Peter Dayan ([ORCID: 0000-0003-3476-1839](https://orcid.org/0000-0003-3476-1839))
- Zac Pujic
- Justin Cooper-White
- Geoffrey J Goodhill ([ORCID: 0000-0001-9789-9355](https://orcid.org/0000-0001-9789-9355))

## Response text

DOI: [10.7554/eLife.12248.032](https://doi.org/10.7554/eLife.12248.032)

The authors present an interesting model to explain turning of growth cones as a function of a guidance cue gradient in vitro. At its core is a principle based on anchor points. All of the reviewers thought that this was interesting work of modeling and experimental interaction to understand why axons turn relatively weakly in response to attractant gradients. However, various aspects of the manuscript gave the reviewers pause, and need to be addressed. They are:

1) To confirm the biological basis and interpretation of the essential part of the model regarding anchor points. Specifically, to address the following questions:

A) Are or are not the authors’ own SCG neuron imaging data consistent with any stiffness, tension, drag or pull of the axon between an anchor point and the growth cone?

We are very grateful for the prompt to add material from our study showing this directly. We have added example frames from timelapse movies (Figure 7), and the movies themselves, that show directly that axons are firmly attached to the substrate at a fixed point and are dragged by the growth cone. Since the axons usually remain straight this implies tension in the axons. The literature is abundant with more general evidence that axons are indeed under tension, as we now cite more clearly (Athamneh and Suter, 2015; Betz et al., 2011; Franze and Guck, 2010; Heidemann, Lamoureux and Buxbaum, 1997; Lamoureux, Buxbaum and Heidemann, 1989; Suter and Miller, 2011).

B) Do anchor points exist and interact with the mechanics of the axon in specific (and testable) ways?

From the above movies it is clear that there are points on the axon which are attached to the substrate and do not move. Focal adhesions of axons and growth cones have been well studied in the literature (Katz, George and Gilbert, 1984; Robles and Gomez, 2006; Stoeckli, 2012). We have not definitively established that the anchor points in our assay are focal adhesions in this sense, but we venture it as a reasonable supposition.

If answers to the above cannot be definitive, then it should be made clear what experiments are motivated by the work. If not, the authors need to address whether such a model is still of use if anchors are an incorrect assumption.

We think the timelapse videos provide definitive evidence that anchor points exist (the red arrows point at the putative fixed anchor points). In the Discussion we now suggest experiments that could test this further.

2) To tone down overly strong statements. Specifically, see comments by reviewers# 2 and 3 below.

We have now done this in the Abstract, Introduction and Discussion as detailed below.

3) To address technical and manuscript issues (see comments from all reviewers below).

Please see detailed responses below.

Reviewer #1:

Various aspects in the modeling were confusing/unclear.

We apologise that various aspects of the modeling were confusing/unclear.

1) In the “Modeling growth cone trajectories” section, it is not clear how θ(t)=a/a+b ϕ(t) equation comes about.

We have now clarified this point in the section “A correlated walk model of growth cone trajectories”. In particular, in the idealized noiseless case (ξ=0), as t→∞, the equation reaches a steady state and the growth cone angle stops changing. Mathematically:

a(ϕ(t)−θ(t))+b(0−θ(t))=0and therefore

θ(t)=aa+bϕ(t)Also, it does not make sense to compare 's' (fixed speed) and 'L' (distance of the growth cone) with s<<L as they are not equivalent in terms of units. Further down it is stated s approx Lt (which does make sense in terms of units). It can't be both.

In the section “Modelling growth cone trajectories”, we have clarified that “s denotes a fixed step length reflecting 5 minutes of growth”.

2) At the end of the section “Modeling growth cone trajectories”, the power law is not clear to me – there seem to be an exponential (10^) aspect missing in the integration of the above equation?

The equation in the section “Modelling growth cone trajectories” implies log(ϕ(t))=(α−1)log(t)+constthus ϕ(t)~tα−1. We have added this clarification.

3) In the second paragraph of the section “A correlated walk model of growth cone trajectories” (Results), 's' is used for a length – clearly there is some confusion in the presentation.

We apologise for this confusion. ‘s’ is the distance moved in 5 minutes, and we have now made this more explicit in the section “Modelling growth cone trajectories”.

4) Figure 1C caption is a bit misleading to say 'different combinations of a and b' when it a is fixed at 1.

The caption has been changed to “with the same a =1 and different values of b”.

Overall, I think Figure 1 should be expanded and/or modified. This would probably help together with the equations too, which need clarification (see above points). For example, I found the D part could/should illustrate the gradient in some way – it is there in the A part only?

We have added the gradient direction in 1D.

Perhaps there can be an additional panel that combines these in some way. Also, it would be nice to show part E for other a, b values. Maybe the authors can take the reader completely through with, say, two sets of a, b values, and then show several parameter value sets as done in parts C and D.

We appreciate this suggestion. On reflection, we actually removed 1E, since it really repeated information that was already present – a problem that would be exacerbated with the extra panels.

I found it confusing as set down and had difficulty visualizing/thinking about the trajectory process. For B part, symbol for turning angles could be included/introduced from equations.

We have added the symbol for turning angle in Figure 1B.

In essence, combine equations and figures more effectively and with a step through for one set of parameters, before showing a collection.

We hope with the clarification of the equations, Figure 1 is now clearer.

Similarly, in Figure 2, the A part shows one set of parameters and the B part, 3 different sets of parameters.

We apologise for this inconsistency. We now show three sets of a and b in 2A with a consistent color code.

I further think that it might be nice to see the full process for a set of parameters (a, b) with and without noise on the same plot (i.e., Figure 1D and 2A aspects).

As Figure 2A has now become quite dense, we have added 2B to demonstrate the case without noise.

In general, equation details need to be clarified, and the figures modified to better help the reader understand the model.

We hope the changes outlined above address these issues.

5) Figure 12 – in introducing more anchor points to the model, a parameter 'r' is introduced. However, I could not find it anywhere in the equations. Please explain/show how this is included in the modeling.

We apologise for this oversight, and have now added the definition of ‘r’ in both the Methods and the Results.

Reviewer #2:

Technical questions: Growth cone angle and 'attractant gradient' are independent terms in equation (Athamneh and Suter, 20151). This surprised me, because I would have thought growth cone angle would move toward the attractant and thus be some function of attractant gradient. Could the authors provide some explanation of why they chose to model things this way? We have added the following explanation to the section “Modelling growth cone trajectories”:

“As the bearing is biased by the gradient direction, the overall growth cone angle ϕ(t)will also be biased by the gradient, coupled through the above equation.”

Saturation of turning is explained nicely by a persistence term in the model, which the authors relate to the axon tension and the limited number of 'anchor points'. Another explanation that crossed my mind is that the receptors in the growth cone that sense the attractants themselves saturate. Could this possibility be addressed or ruled out, even as a discussion point?

We believe that we haven’t saturated the receptors since this would cause toxicity (or at least severe loss of neurite growth). According to Ohta et al., 1990, when [NGF] is high (>40 Kd, assuming Kd=0.9±0.3 nM from Wehrman, 2007), it leads to loss of neurite growth. Since our assays did not show poor growth, it suggests that the [NGF] was not saturating. In addition, assuming receptor occupancy = C/(C+Kd), then at one end of the chamber where [NGF]=20Kd, there will be 95% receptors occupied. This is still not a saturating level, and most of the chamber has [NGF] < 20Kd. Furthermore, persistence is inferred from the straightness profile of the trajectories and is sufficient to explain turning saturation even without receptor saturation.

We have added the following text in the section “SCG neurons were guided in the microfluidic assay”:

“Previous work using Scatchard analysis estimated that Kd= 0.9 ±0.3nM (Wehrman, 2007) and showed that SCG neuronal outgrowth is severely inhibited at the saturating NGF concentration of 40 nM (Ohta et al., 1990). Given the healthy growth in our assay, it is clear the concentration in the gradient condition was below saturation point.”

Axon stiffness might also play a role in persistence. It would be nice if the authors could comment on this.

Thank you for this important suggestion. We think that persistence does indeed depend on axonal stiffness, and speculate that higher stiffness will lead to higher persistence. We have added the following text in the second paragraph of Discussion:

“The stiffness of axons is also important (Rajagopalan, Tofangchi and Saif, 2010), and stiffer axons will likely have higher persistence due to their more limited ability to bend.”

Finally, how do the concentrations of NGF relate to what is known about dose-response relationships of trkA receptors, e.g. do the gradients approach a saturating concentration?

We used an estimate of Kd=0.6-1.2 nM for NGF as explained above, and the concentration we used was 10 nM, so 8-16 Kd. As explained above this is not a saturating concentration. We have added this clarification in the section “SCG neurons were guided in the microfluidic assay”.

Manuscript issues:

There are a number of labelling issues in later figures (e.g. missing axis label in Figure 12H, and reference to empirical distribution that was not plotted in Figure 10D). A thorough check of the figures and labelling would be a good idea.

We have carefully checked the labelling of all the figures in the resubmission. Figure 12H (now 14H) is hard to label because it has 3 different plots, however the meaning of the y axis is explained in the legend. We have added the reference distribution in Figure 10D (now 12D).

The unit of replication 'n' is not defined. The authors should clearly state how many experiments generated this dataset and what the unit of replication is. Accordingly, statistical tests should state the number of degrees of freedom.

We have now been clearer about the number of experiments and the replication units in the section “SCG neurons were guided in the microfluidic assay”:

“We analyzed trajectories for 300 axons per condition. These were obtained from 23 individual chambers in the control case, 27 chambers in the NGF gradient case, and 24 chambers in the NGF gradient plus KT5720 case. In most experiments, 2 chambers were run in parallel, so the total numbers of experiments in each case were 12, 15 and 13 respectively.”

The unit of replication is a growth cone. We have discussed degrees of freedom in the accompanying eLife Statistical Submission Form: the degree of freedoms in our pairwise t-tests and Kolmogorov–Smirnov-tests is the total number of samples in the 2 groups minus 2, and the degree of freedom in the Kruskal Wallis test in Figure 4 is the number of groups minus 1 (i.e: 4). Since these are simply standard results we don't think it would be useful to quote them in the main text. We are, of course, happy to do so though if you feel that we should.

Issues of clarity/presentation:

This article should in principle appeal to a large cross-section of biologists, including developmental biologists with little or no mathematical background. Though the authors have done a good job of explaining what they did in words, it would help to be even clearer in places, e.g. the curves labels in Figure 12H are not very user-friendly. Reminding the reader of the meaning of terms a, b, r, σ, etc. would also help.

We apologise for the lack of clarity. We have now included a table summary of all the parameters in Table 1. We have also expanded the figure captions in Figure 1, 2, 6. Figure 12H (now 14H) is hard to label because it has 3 different plots, however the meaning of the y axis is explained in the legend.

Some of the statements are unnecessarily strong (e.g. "Without such a model, it is impossible to determine if trajectories observed in vivo are in fact consistent with gradient guidance" or the statement in the Discussion that the paper "resolves" an outstanding question). It certainly helps resolve this question, but it raises more questions as I have outlined in these comments. Softer language will get the message across and is less likely to put off readers with preconceived ideas.

We have now softened such claims throughout the paper. For instance:

In the Abstract:

“This model provides a mathematical explanation for why average axon turning angles in gradients in vitro saturate very rapidly with time at relatively small values.”

In the Introduction:

“Without such a model, it is difficult to determine if trajectories observed in vivo are in fact consistent with gradient guidance.”

In the Discussion:

“Here we presented a model of axon trajectories in gradients which is intended to help resolve the mystery of why axon turning angles in gradients saturate over time in vitro.”

Reviewer #3:

1) I am not convinced that the anchor point model is a good model for growth cone turning behavior. There is no evidence that growth cones perform stepwise turning with respect to an anchor point. In the Discussion, the authors describe: "New anchor points could be established when tension is too high, or when it becomes too energetically expensive to drag the neurite." However, I am not aware of published studies that show growth cones physically 'dragging' a neurite (please direct me to such evidence if incorrect).

We apologise for not providing direct evidence for this from our data in the first version of the manuscript, but appreciate the opportunity now to do so. In particular we include a new figure (Figure 7) which shows frames from 3 of our timelapse movies, and these 3 movies are now included in their entirety in the paper. These show directly the phenomenon of `neurite dragging’. In particular they show that, while the movements of the growth cone are quite random, the axon is nevertheless generally directed straight back to the last anchor point (cell body or branch point). We feel that the addition of this data significantly strengthens the paper.

However, we accept that we have no evidence to support the particular sentence quoted by the reviewers, and have now removed this.

The anchor point idea indeed predicts that the axon between the growth cone and the nearest anchor point should be 'dragged' into the direction where the growth cone moves. Of course, if the anchor point is far away (paper quote: 'the in vitro data we have presented here was well-fitted by assuming the only anchor point is where the axon emerges from the soma'), then a lot of axon would need to be dragged indeed. What would the stiffness of that axon be?

We have not performed direct measurements of axon stiffness. However a clear implication from visual inspection of the new images and movies now included is that dragged axons must be quite stiff, since they stay fairly straight as they are being dragged.

The authors acknowledge that the in vivo environment will be more 'complex', but only by assuming there may be more anchor points.

We did not mean to imply that we think an increased number of anchor points is the only difference between the in vivo and in vitro cases: it is simply the parameter which we are focusing on in this paper. However, we have acknowledged in the Discussion that stiffness, cell-cell interactions, physical cues, ECM components are some other factors that can affect growth and might all be different in vivo.

Not surprisingly, a closer anchor point allows sharper turns and results in more variability. This simple conclusion is actually one of the major conclusions of the paper.

In summary, I think the anchor point model may be a good idea, but there is precious little evidence supporting it.

While we agree do not have direct evidence, we believe that the data we have now included significantly strengthens our case in this regard.

I am with the authors that a simplification to an elegant in vitro system is a good approach and I would not look for further in vivo relevance, if the in vitro behavior were to fit the model. But if there is an in vivo or in vitro neurite that actually drags an axon between the growth cone and an anchor point, the reader really needs to be shown one.

As described above, we have now done this.

To my knowledge it is more likely that most axons, including in the SCG culture, lay behind the moving growth cone without experiencing any force or tensions required for provide feedback from a hypothetical anchor point. If there is no such feedback, the core of the model cannot be supported.

We now provide additional citations to support the claim that the axon is under tension and this tension is related to the coupling to the substrate via adhesion sites (Athamneh and Suter, 2015; Betz et al., 2011; Franze and Guck, 2010; Heidemann, Lamoureux and Buxbaum, 1997; Lamoureux, Buxbaum and Heidemann, 1989; Suter and Miller, 2011).

2) A key prediction of the anchor point model is the tension on the axon between the growth cone and the closest anchor. If such evidence exists for at least some instance, in vivo or in vitro, I can and should be convinced that the model is applicable. This is a true prediction of the core of the anchor point model. In contrast, the measurements provided on the turning speed and the 'saturation' of turning are not true predictions of the model more than they are the basic data the drove the generation of the model in the first place. For example, the authors describe this 'long-standing mystery' many times, use it to justify the model, and then present the data that was used to make the model in the first place as: 'the average turning angle reached the steady state quickly and did not increase significantly with time, matching the prediction of the model (Figure 4C)'. This is a clear case of a model that was made to fit the data. There is no true prediction of the model (one that would not have been possible before running the model) that is tested in the paper. The authors consistently use the wording 'predicted by the model' to describe an outcome of the anchor point model that fits data past or present. Again, I could and should be convinced when, for example, evidence for a real existing anchor point (even just in the SCG culture) were provided, predictions based on tension of the axon, its predicted stickiness to the substrate (as discussed by the authors), etc.

We apologise if our claims seemed too strong – we have softened them. It is certainly true that we did not formulate the model ab initio: we were initially inspired by our experimental observations that axons tend to always point back to the last anchor point. This led us to write down equation 1 as the simplest description of the balance of forces acting on the growth cone. However, the derivation from this equation of the rapid saturation of turning with time was a complete surprise to us, and was not something we tried to engineer into our model. Thus, it’s not quite fair to say that it was `the basic data that drove the generation of the model’: indeed it was primarily the model that drew our attention to this particular aspect of the experimental data.

We do however agree that, for instance, some aspects of the step statistics were empirically derived, and we have therefore deleted a sentence from the Discussion, which made claims about what was predicted by the model, that we agree with the reviewer were too wide-ranging.

3) I read this study as a purely hypothetical model based on previous data and some new measurements in the SCG culture using a microfluidic device. Links to biology are present only in the Discussion and as speculations (e.g. focal adhesions), but neither integrated into the model, nor tested in experiments.

We do not completely agree with this. In fact there is a strong link between our model and our microfluidics data: in particular we propose biophysical principles guiding axon growth, and show that these principles can accurately predict axon trajectories in biological experiments. Precise measurements of the nature of the focal adhesions assumed in our model are left for future work.

As it stands, the anchor point model clearly reproduces some significant behavior or growth cone turning in vitro. However, the statements in the Abstract that ‘this model explains the long-standing mystery…’ and that ‘this work introduces the most accurate predictive model […] and deepens our understanding of axon guidance events both in vitro and in vivo’ appear to me quite dramatically overstated.

We have softened this statement, and other statements elsewhere in the paper. For instance in the Abstract, we now say:

“This model provides a mathematical explanation for why average axon turning angles in gradients in vitro saturate very rapidly with time at relatively small values.”

4) Manuscript issues:

In the section related to Figure 9, the authors measured the bearing angles, step sizes, and mean step sizes of individual growth cones and fitted all these parameters by different distributions. However, the explanations of what these different distributions mean in a biological context is inadequate.

We have amplified the interpretation in the Discussion section.

In the subsection "SCG neurons were guided in the microfluidic assay", the authors took into consideration only the axons that made an angle between 70° and 110° with the gradient direction since they expected impact of the gradient would be strongest on these axons. The reason behind this expectation is not well explained.

We have added a clarification in the section “SCG neurons were guided in the microfluidic assay”:

“An asymmetric concentration field of guidance cue across the growth cone leads to turning (Song, Ming and Poo, 1997; Höpker et al., 1999; Xiang et al., 2002; Ming et al., 2002) and axons growing in this range experienced between 94% (i.e. sin70°) to 100% (i.e. sin90°) of the maximum possible concentration difference across the growth cone. Thus we expected the impact of the gradient would be strongest on these axons (Figure 4A).”

Also, although Figure 4A is referred after this expectation, Figure 4A does not show anything related to this.

We have added the gradient direction in Figure 4A.

Did the neurotrophin gradient majorly influence branching or retraction? Those events were discarded and not compared to the gradient control.

We are very grateful to the reviewer for raising this very interesting point. We did originally analyse our data to answer this question, but since the answer was ‘no’ we did not include this data in the original manuscript. However we now realise this negative result is still an important piece of information to include, and it is now presented in a new figure (Figure 5). In particular we compared the number of branches in the control vs. gradient conditions, and the number of branches growing up or down the gradient, and did not detect a difference in either case. Similarly, the branching and retraction rates were unchanged. This is all now described in a new section entitled “The gradient did not affect axon branching”.

In the section "Modelling growth cone trajectories", "s" is referred as constant speed but in the section “A correlated walk model of growth cone trajectories” it is referred as length of a step.

We have changed “a constant speed” to “a fixed step size s every 5 minutes” in the section “Modelling growth cone trajectories”.

To test whether fluid flow has any effect on statistics of the steps authors divided the axons in 4 quadrants but how this division helps understanding the effect of fluid flow is not clear.

We added the following text in the section “Flow did not affect the statistics of steps”:

“To test whether fluid flow in the chamber biased the statistics of the steps, axons growing in the gradient condition with fluid flow were divided into 4 quadrants with different relative angles to the fluid flow: 2 quadrants growing perpendicular to the flow, one quadrant growing with the flow, and the other growing against the flow (Figure 6A). Comparing the distribution of bearing changes between the 4 quandrants, and with axons from the control condition without any flow, showed no influence of the flow (p = 0.7 in Figure 6B and p = 0.4 in Figure 6C, Kruskal-Wallis test).”

In Figure 3, please indicate which directions are set as 0° and 90°. Also part E and F can be shown on the same graph.

We have indicated the directions in 3D. We thought about the suggestion for panels 3E and 3F. On balance, we prefer to show them on separate graphs as they almost completely overlap, and would thus be hard to distinguish on the same graph.
