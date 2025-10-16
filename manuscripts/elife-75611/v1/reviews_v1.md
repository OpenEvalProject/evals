# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75611.sa0](https://doi.org/10.7554/eLife.75611.sa0)

This ambitious study goes from signalling mechanisms to fly behavior through a model of a memory circuit in the fly brain. The authors call this the incentive circuit. The model draws extensively from anatomical and physiological measurements. The study makes a wide range of predictions about how this circuit mediates behaviour and learning through attractive and repulsive cues.


---

# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75611.sa1](https://doi.org/10.7554/eLife.75611.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors resubmitted a revised version of the paper for consideration. What follows is the authors’ response to the first round of review.]

Thank you for submitting the paper "The incentive circuit: memory dynamics in the mushroom body of Drosophila melanogaster" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mani Ramaswami (Reviewer #3).

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

While all the reviewers appreciate the ambition and value in integrating diverse sources of data to developing a model of learning, they had some substantial concerns. These are elaborated in their detailed comments, and I provide a distillation of the discussion that the reviewers and I had about the paper. Since it will take considerable further work to address these points, the reviewers and I felt that the paper should be rejected. If the authors wish to resubmit after completely addressing the concerns this would be fine.

1. The reviewers found the paper a difficult read. Could the authors rewrite to make it accessible to a wide range of readership?

2. The formulation of the DLR seems to be a variant of RPE (Reward Prediction Error) learning rules, and hence the conclusions need to be re-evaluated.

Can the authors re-think the basic formulation of DLR starting with Equations (2) and (3)? There should be some experimental tests if the DLR is indeed determined to be different from regular RPE.

3. The microcircuits should be better based on experimental data. From our understanding, the data shown in Figures 4H/G, 5B/C/E/F and 6B/C seems to have been obtained by simulations. Would Ca recordings for these figures be feasible? Can there be stronger justification for the connectivity of the proposed incentive circuit?

3b. The proposed circuit connectivity of the 'incentive circuit' needs to be defined for each MBON because most contemporary work shows that different kinds of memory involved plasticity in different subsets of MBONs. Can the model make specific testable predictions for each subset of MBON?

4. Further experimental predictions should be made, based on well-parameterized models of the underlying neurons. Can the authors provide considerably more clarity on which sets of behavioral or physiological data are selected by the authors as targets or tests for specific parts of their model?

5. Can the model account for existing data showing overlapping conflicting engrams? Additional experiments and simulations may be needed to ascertain this.

Reviewer #1 (Recommendations for the authors):

This ambitious study builds a model of a proposed key circuit motif in fly behaviour and learning, the Incentive Circuit. The authors examine its implications for a variety of behaviours, and perform a thorough circuit-level mapping of model neuronal activity to recordings. The model uses abstracted model neurons and synaptic signaling, but with careful attention to experimental data at many steps. The mapping to experiments is good, and the model makes far-reaching predictions for animal behaviour.

The development of the model is generally well presented. The learning rule is derived from earlier work (Handler et al) and then the authors transform the terms for ER-ca2+ and for cAMP to terms emerging from DA inputs. The model development is especially systematic, building up to the final version step by step with reference to experiments. Importantly, these are mapped to specific sets of experimental observations on the circut level.

I have mostly comments to clarify or strengthen the presentation.

1. I had a little trouble to envision the two components of D2 and D1. Are they time-varying? Seems to be, see Equation 4, where they are presented as D1(t) and D2(t). In other words, do they express D2 and D1 as distinct α functions following spike activity in the DAN?

However, in the text and figures it is frequently presented in terms such as D2 > D1 (eg., Figure 3), which looks like a static effect. This was confusing.

Also in Figure 2A, are we seeing the peak values of ER-Ca or area under curve?

Around line 128 it is a hint that it is area under curve, but I am not sure.

2. I would have liked to have seen some more mapping to functional experiments in the figures up to Figure 7, where the components of the model are being built up. The authors mention several in the text. Even a qualitative look at the experimental responses would help to strengthen the motivation of the model design.

3. The authors then utilize this circuit in an aversive olfactory conditioning paradigm, for which they provide experimental data corresponding to the various neuron types. They then simulate this. This is an outstanding way to validate/test their model. It would be helpful to have the experimental and simulated responses interleaved on the same figure so as to better compare.

4. I appreciate that it is quite challenging for a simulation to simultaneously replicate properties of several intermediate stages of circuit activity, even more so when the stimulus is not one that the model has been trained on. Could the authors confirm that this is indeed the case, i.e. that the model outcome for figure 9 was obtained only from the parameter tuning earlier in the paper up to Figure 7?

5. It would be useful to perform a statistical evaluation of the fidelity of the model as compared to experiment.

6. The authors then place their model flies in a virtual arena and explore a number of behaviours. Here they contrast their model behaviour with the predictions from a different learning, reward prediction error. I would have liked to have seen in figure 11 an illustration of the correspondence to experimental observations from the literature.

Reviewer #2 (Recommendations for the authors):

The manuscript in its current form is built around two main threads. In the first thread, the authors review several results in the literature on associative learning in the mushroom body of the adult fruit fly, and construct an Incentive Circuit (IC) consisting of 6 dopaminergic and 6 mushroom body neurons with specific memory dynamics. They provide a coherent functional view of some of the disparate recent results in associative learning of the mushroom body.

The second thread incorporates a Dopaminergic Learning Rule (DLR) into the IC computational model, providing a computational system for evaluating the learning mechanisms involved.

A weakness here is that the acquisition, forgetting and assimilation of memories qualitatively described in the first thread are not strongly linked with the quantitative IC model described in the second thread.

Conversely, the validation of the IC model circuit, given the noisy data that the authors provide, is only possible in terms of trends, i.e., simple visual inspection. Interpreting the data then is difficult as it does not provide enough constraints for the computational model.

Given the limitations inherent in the validation of the IC from their recorded data, the authors proceed to explore the DLR using behavioral experiments purely based on simulations. This is an effective methodology widely employed in, e.g., robotics. The authors extensively compare the 'learning/navigation' performance of DLR with a variant of reward prediction error (RPE) learning rule and demonstrate a better learning performance. While the comparison may be compelling, we found that underlying the DLR, is the computation of a prediction error, i.e., DLR is a variant of RPE. This calls for a re-evaluation, positioning and clarification of some of the key conclusions regarding why the DLR is effective in associative learning tasks.

l.128 The section 'Mushroom Body Microcircuits' makes good first reading. However, most of the key statements could further benefit from more extensive quantitative backing as hinted at in Figures 4, 5 and 6 (see also my comment below). Since these microcircuits are simpler than the IC, my expectation is that they could provide better intuition regarding their function.

Figures 4F and 4G are rather difficult to understand/parse. More caption details, choice of different colors, would help.

Same comment regarding Figures 5B, 5C, 5E and 5F, and 6B, 6C.

While Figure 8 is to be commended, the data is rather noisy and, in my view, despite the best intentions, rather difficult to understand/evaluate. As the authors argue in l.312, 'we computationally modelled the incentive circuit in order to demonstrate all the properties we described before and compare the reconstructed activities to the ones of Figure 8C'. However, a comparison by simple visual inspection is rather unconvincing. The need for introducing a distance measure is in order.

I found 'modeling behavior', as presented in the current version of the manuscript, to be quite effective. However, I'd like to note that in the process, the authors changed the underlying PN activity model. This requires, given that the rest of the paper is based on a binary odor model of the PN activity (see the discussion preceding Equation (6)), some careful/detailed assessment of its implications. Finally, the authors propose to compare their DLR with a variant of RPE. Here a major conceptual problem arises.

The authors argue that DLR is a fundamentally different learning rule from RPE. They state in l.462 that 'The idea behind RPE is that the fly learns to predict how rewarding or punishing a stimulus is by altering its prediction when this does not match the actual reward or punishment experience'.

This can be adapted to the mushroom body circuit by assuming that the MBON output provides a prediction of DAN activity. But this is exactly what Equation (18) states. The differential equation (18) describing the gradient of the DAN activity is equal to sum of the weighted shock delivery ('transform' in l.750) and the weighted MBON activity (l.755).

The sum is just the prediction error between the two terms. Consequently, since the DLR is, in view of this reviewer, a variant of RPE, a comparison with another RPE is of little interest. A substantial re-write of the paper starting with the section on the Incentive Circuit (l. 257) is in order.

l.765: "The above matrices summarise the excitatory (positive) and inhibitory (negative) connections between MBONs and DANs or other MBONs. The magnitude of the weights was hand-tuned in order to get the desired result." This 'hand-tuning" appears, to me, to be a 'construction' of the prediction error on the right hand side of Equation (18). Some details might help clarify to what extent the hand-tuning is based on the assumptions of the binary model of the 2 odors at the PN level. I presume that the generality of the model alluded to in l.743 stating that 'that the number of neurons we are using for PNs and KCs is not very important and we could use any combination of PN and KC populations' breaks down and the hand-tuning needs to be repeated every time the number of neurons is changed.

Reviewer #3 (Recommendations for the authors):

The authors propose an original dopaminergic learning rule, which, when implemented in simple neural circuit motifs shown to exist within the Drosophila mushroom body (MB) , can potentially account for a very large number of independent, poorly integrated physiological and behavioural phenomena associated with the mushroom body. It considers multiple behavioural roles of MB output neurons beyond attraction and aversion and offers new insight to the how the MB functions in acquisition, consolidation and forgetting of memories. The manuscript further attempts to show how similar principles could potentially be useful in the mammalian brain. An ambitious and integrative analysis of this sort is sorely needed in the field.

The paper has obviously involved very broad and deep consideration of the MB connectome as well as genetic, physiological and behavioural studies of the roles of the different classes of Kenyon cells, MBONs and DANs that innervate the mushroom body. It is original and ambitious and potentially very valuable to the field.

My major reservation is that the manuscript is very difficult to read and evaluate by anyone who is not a Drosophila mushroom body aficionado. I consider myself an interested reader and one who keeps broad track of the field, but found the need to read and evaluate far too many papers cited by the authors to decide how well phenomena the authors attempt to model have been demonstrated and how well assumptions made by the authors are justified by data. E.g. I was stymied even at figure 1, where mutual inhibition between MBONs is indicated and it took me considerable (and eventually futile) effort to look into where and how well this has been established.

To make the work more accessible at least to this moderately educated reviewer, I fear that a major re-rewrite will be required. I would suggest that for each section – exactly has been shown be clearly enumerated, with enough detail provided for the reader to judge the strength of these data. The justification and support for three types of MBONs and their incentive should also be particularly clearly indicated.

Moreover, while the authors are correct to point out the limitations of current models based on dopamine prediction-error, I do wonder if there is room for prediction error to also contribute meaningfully within the framework proposed in this paper.

I apologise for the not having a list of specific issues for the authors to address, because I found the basis to be so difficult to explore but here is some general feedback.

1. It is nice that and the dynamics of neural responses obtained with the model correspond closely with ones reported in previous studies (although there are exceptions, some nicely highlighted by the authors).

2. There should be deeper engagement with signalling mechanisms that differentiate the two types of dopamine receptors. I found the assumptions regarding their differences to be useful for the modelling of different effects of reinforcement before or after sensory experience (Ruta Cell 2019), but quite superficial in terms of providing hypothesis for how the receptors may differ in terms of mechanism of action.

3. ON the same note, specific experimental predictions of the model could also be clearly indicated at the end of each section.

4. While the authors admittedly designed informative and clear figures, and their Table 1 points the reader to papers that report relevant neural connections and neuronal functions, this is not enough. Data in support of each assumption should be clearly and specifically mentioned and hypotheses connections also clearly stated. After considerable effort, I still could find no evidence for lthe existence of inhibitory connections between MBONγ4 and MBONγ2 (which is not to say that none exist – but surely it is the authors job to clarify this).

5. The authors should also try to account for the discovery of parallel, independent memory traces (like appetitive LTM formation towards the CS- in classic LTM aversive training paradigms).

6. Does the dopaminergic learning rule explain the differences in dynamics and memory strength between appetitive and aversive memories? These two types of memory involved different molecular components and display different learning rules (stronger short-term aversive memories and longer-lasting appetitive memories requiring less training)? This should perhaps be clarified, particularly since KC output appears dispensable for aversive learning (aquisition) but potentially necessary for the acquisition of appetitive memories (Pribbenow et al., 2021).

7. I found the easy assumption that forgetting involves erasure to be troubling. Perhaps this happens sometimes. But many apparently "forgotten" memories are never erased, simply not reactivated for multiple reasons. Intellectually this point needs to be acknowledged.

[Editors’ note: what follows is the authors’ response to the second round of review.]

Thank you for resubmitting your work entitled "The incentive circuit: memory dynamics in the mushroom body of Drosophila melanogaster" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Could the authors compare their simulated/predicted behavior with some quantitative or semi-quantitative measures of experimental behavior?

2. Can the authors elaborate on their mapping of ER-CA and cAMP in the model with the cited data? This relates to point 4 from Reviewer 1.

3. Can the authors do some parameter sensitivity analysis as suggested by the reviewers?

In addition, the reviewers had a few points for the authors to expand upon in the revision, and a number of useful suggestions to improve clarity.

Reviewer #1 (Recommendations for the authors):

This is an ambitious but also highly complicated odelling study that seeks to account for a wide range of fly learning behaviour in terms of underlying learning rules and circuitry.

The strengths of the study are its ambition, detail and substantial attention to experimental inputs. In principle it builds up a large and testable conceptual framework for understanding many aspects of learning. Its weaknesses, which are readily fixed, are 1. That the study misses opportunities to better compare model to experiments. And 2, that the study doesn’t do a systematic parameter and model exploration to see how robust are the properties.

With these additions the study would be strong and of value to the field in laying out a template for further investigation. The authors posit that this framework could also apply to other organisms.

1. This is an ambitious but also highly complicated odelling study that seeks to account for a wide range of fly learning behaviour in terms of underlying learning rules and circuitry. The authors have made substantial improvements to the clarity of the presentation, particularly with regards to comparison of experimental and simulated data.

I would have liked to see similar comparison for two more features: the behaviour, and the crucial learning rule section, as I comment below. I note that a similar request was made in an earlier review.

2. The other big thing I would have liked to see is an exploration of parameter sensitivity. This is needed both because of model complexity and because of the not-perfect match between model and input data. No model is perfect, but the confidence in a model is much improved if one can see that it still ‘works’ even when the numbers (and other assumptions) shift around a bit.

3. Behaviour: The authors have made the interesting and potentially powerful step of linking their model to measurable behaviour. But they miss the opportunity to put the outcomes (experiment and model) side by side. Even a semi-quantitative distillation to some common metric for displaying and comparing the experimental and model properties would have been valuable.

4. Figure 16: Details of ER-CA and cAMP in the model don’t match data. The form of the pairing for ER Ca is inconsistent with the data of Handler et al., particularly when CS precedes US by a large interval. Handler et al. show no response for forward pairing even several seconds after the last stimulus. Also, the time-course of ER response for the backward pairing case is inconsistent. In the Handler data (Figure 6) the ER signal remains low (i.e, very different from baseline) well past 5 seconds, whereas in Figure 16 the signal returns to baseline within 5s. I am also concerned that there doesn't seem to be experimental support for the reduced cAMP signal at very small overlap intervals. Indeed, the Handler data suggests that there is a large signal at the 0.5s and -1.2s points. Figure 16 shows that the model assumes a low and brief signal at -1.2s.

I would have appreciated having the experimental data from Handler and others illustrated here in the same figure, just to see how well the model forms behave. It would save the reader the step of going to look up another paper and tracking down appropriate figure panels.

5. As one example of a useful parameter sensitivity analysis: The form of the deltaWij seems rather crucial to the model, so I'm homing in on this. It is a difference of two values which are themselves clearly the difference of opposing signals. It would therefore be valuable to show that relaxation of these tight timing requirements does not upset the learning rule and subsequent behaviour.

It would be useful to see similar sensitivity analyses for other key parts of the model.

Clarifications:

6. pg 28: 3 lines from bottom.

Do the authors mean "activity of the ith presynaptic KC? 'Target' sounds like it is postsynaptic.

7. Equation 30 onward.

w_rest: Is this a global parameter for all synapses?

w_rest: The way it is used in the equation looks more like a_rest, the resting activity of the synapse. Sorry to be pedantic, but the units of weight and rate don't match.

This gets further mixed in the equation between lines 853 and 854 where the authors add ki and Wij. Maybe ki is scaled somehow to weights?

8. Figure 5 and later: The responses, both experimental and model, are shown as an up-down oscillation. I assume that the up states are measurements during the training, and down is measurement half a day later. But this is hard to see from the text or legends, and I had to go down to the last section in the methods to see that this seems to be described as on-shock and off-shock values. It is confusing and should be mentioned in the figure legends and accompanying text.

Reviewer #2 (Recommendations for the authors):

The authors propose an original dopaminergic learning rule, which, when implemented in simple neural circuit motifs shown to exist within the Drosophila mushroom body (MB), can potentially account for a very large number of independent, poorly integrated physiological and behavioural phenomena associated with the mushroom body. It considers multiple behavioural roles of MB output neurons beyond attraction and aversion and offers new insight to the how the MB functions in acquisition, consolidation and forgetting of short and long-term memories. They discuss how the motifs and computations discussed would be relevant to other MB functions and altered by known connections, not yet included the simplified model. The manuscript further attempts to show how similar principles could potentially be useful in the mammalian brain. An ambitious and integrative analysis of this sort is sorely needed in the field.

I thank the authors for a very constructive, clear and insightful response to the prior criticism and queries, The manuscript is now hugely improved and can be accepted with no further changes. I think it represents a major contribution to the field. This is a wonderful piece of work that I, at any rate, would recommend to anyone interested in the mushroom body.

Reviewer #3 (Recommendations for the authors):

First, I'd like to thank the authors for responding to my concerns/suggestions. At this point, it reads, in my assessment, much better as a result of the many changes. In particular, the newer figures are of high quality and their stated goals much easier to grasp. Also, shifting most of the discussion of the "formal" model in the (old) Results section to the (new) Methods section makes reading flow more intuitively.

Second, the disagreement we had, appears now to be more in terms of naming/labelling of Equation (18) and (30), thus clarifying the rational for the naming of the 2 learning rules (DPR) and (RPE). However, the "RPE" naming for (30) is, in my view, a bit of a stretch, but I am not raising an objection. Just a friendly note to the authors.

I'd like to make a final suggestion that future readers might benefit from. Reviewer 1 raised this issue already and the authors addressed the question. However, in my view, the presentation starting with "we postulate a mathematical formulation …" just above Equation (32), seems a bit circular. While the authors answered the question, in terms of intuitive modeling (Equation (34)), the presentation thread I am referring to is rather formal. The D's in Equations (32), (33) are not explicitly defined; the equations, when added up are consistent with the Equation above line 854. While Equation (34) provides the intuition of the decomposition of the weights into 2 terms, this decomposition is by no means unique. Having said that, we are then confronted with Equations (35) and (36). There is little justification given for the rational of choosing/postulating these two diff. Equations. I presume that the solution for these Equations are the D's. A careful reading seems to suggest that these are delayed differential equations. In math terms, a single delayed diff. Equation is infinite dimensional, and essentially intractable. The following Equations (37)-(39), while consistent with the discussion above, do not help clarify the matter. Which brings one back to Equations (32), (33). Finally, the Methods section has a sizable number of matrices that have seemingly arbitrary entries.
