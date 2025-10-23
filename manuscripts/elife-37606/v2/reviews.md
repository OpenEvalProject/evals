# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37606.033](https://doi.org/10.7554/eLife.37606.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The roles of vision and antennal mechanoreception in hawkmoth flight control" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ronald L Calabrese as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Noah Cowan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors present an analysis of the interaction of antennal mechanosensory and visual input in the stabilization of hovering flight in a diurnal moth. The analysis compares three antennal conditions (intact control, antennae removed, antennae reattached) and two light conditions mid-range and low, each with two stimuli stationary flower feeding, and oscillating flower feeding consisting of two movements: chirp and sum of sines. They find that for both stimuli in the mid-range lighting, moths show degraded tracking at higher frequencies with removal of antennae and recover somewhat when antennae are reattached, compared to control (intact antennae). In low lighting, all three conditions behave similarly poorly, even at low frequencies. These results are consistent with the emerging conclusion that visual input is essential for moths to identify and track the flower movement relative to their own position – antennal mechanoreceptors cannot provide that required information but are necessary to support fast flight maneuvers. Vision and mechanoreception thus act in different frequency domains and do not compensate. These studies complement those showing similar interactions between haltere mechanoreception and vision in dipterans (most notably Drosophila) by extending them to the greater number of insect orders that lack halteres and thus make the findings of wide interest.

Essential revisions:

The expert reviews are provided, which will require rewriting and some new analyses. Important points include:

1) All three reviewers agreed in consultation that a control diagram is needed to help the reviewers contextualize the findings and point the way forward for further mechanistic analyses.

2) In discussion among the reviewers, there was some concern about the phase analysis and the reviewers discussed whether cross correlation would be a better strategy. However they concluded that cross correlation could be tricky with a chirp or sum of sines. Indeed, cross-correlation should be done at a given frequency. If these data are available then a cross correlation might be in order.

3) The expert reviews provided should all be addressed; they are detailed but consistent and complementary.

Reviewer #1

Concerns

1) I found it confusing that the essential idea or hypothesis that visual input is essential for moths to identify and track movement relative to their own position regardless of frequency is not made clear up front. The presentation could be made a lot clearer, if the contrast between mid-range and low light was presented first for the intact condition. Perhaps this problem will be ameliorated by the inclusion of a control diagram.

Reviewer #2:

Concerns

The most significant issue is the lack of a clear interpretation of the results. The results of this paper are quite interesting; the removal of a "postural" self-motion (similar to proprioception or vestibular) feedback system, the antennae, affects tracking of the exogenous motion of a flower. Why is this so interesting? Because of the subtle but evidently important interaction between these distinct feedback loops (diagram in Author response image 1):

One could explain (at least) qualitatively this interaction, as depicted in a graphical feedback control model such as the one above. It seems interesting that ablating the antenna disrupts the inner loop of the control system, making the outer loop (vision and mechanoreception from proboscis) not as effective at tracking. How does the modulation of these inner-loop dynamics (based on ablation) hinder outer-loop control? This is ripe for interesting computational modeling – such modeling itself could be saved for future work, but the description of this problem, which now is only vaguely hinted at, would elevate the paper substantially. The diagram above is just a rough cut and needs to be fleshed out, but I believe it to be a reasonable stab at the topology of the feedback system in question and if the authors agree, I encourage them to adapt and include something similar. Some possible issues with my above diagram that will require greater thought by the authors:

– the summing junction after the antennal and visuo-mechanosensory blocks is a simplifying assumption,

– before the plant perhaps there should be some sort of CNS integration

– Probably it is a +/- but the second junction may be better as rectangle labeled

"multisensory integration" where the inner-workings are left as future work.

In addition to that we have a number of detailed comments.

Detailed comments:

1) The authors use the word "significantly" even for data that, while statistically significantly different, are not that different from a controls engineering point of view. This is most notable in the discussion of Figure 3B, where the tracking errors of the re-attached and ablated moths were "significantly different" but compared to controls, they were quite similar.

2) Sometimes ablated/reattached moths perform more like controls, and sometimes they perform more like antennectomized moths. Can this be fleshed out a bit? For example as in point #1, the reattached and antennectomized moths performed similarly, but in the chirp task, control and re-attached were more similar.

3) It is unclear that how many trials are performed for each individual animal in each different case. It seems "one set of data", but it should be described in the paper. If you did not do more than one trial per animal (e.g. multiple passes of sums-of-sines), why not? If you did, how many did you do, how did you perform averaging, etc.? As long as that can be clarified, the results are compelling and seem to support the overall claims of the paper.

4) The paper has no citations to the Cohen lab papers that include models of haltere-based flight control in flies over the last 8 years that include roll, pitch, and yaw perturbations. There are crucial experimental differences; you perturb target motion (tracking task) and they provide a mechanical perturbation (i.e. a disturbance), so the experimental topology is different but perhaps their data could give you some insights into the inner-loop control structure?

5) The paper assumes that is the proboscis mechanoreception has "little or no" feedback contribution. Recent and crucial work by Roth et al. that the authors site quite clearly indicates otherwise for a related species of moth. This manuscript does use data in dim and bright light in the phase before proboscis contact with the nectary for a stationary flower (Figure 2—figure supplement 1), in which case this assumption seems valid, but mechanoreception is known to play a large role in tracking a moving flower (Roth et al.). That said, I'm not sure why this rather dubious assumption is needed.

6) Tracking error decreases significantly after reaching to its peak (Figure 3B, Figure 3—figure supplement 1). It is not intuitively clear why or how tracking error would decrease at higher frequencies. Is there any explanation for that? I have some concern that phase lags may have "wrapped" but that the analysis performed didn't identify that wrapping. Could that be possible? See especially Figure 3—figure supplement 1, last row.

7) As shown in Figure 1D, the power for chirp stimulus is much larger than the power for sum-of- sines. In subsection “Chirp movement”, it is mentioned that "chirp stimulus does not fulfill the linearity criterion".

Was this measured quantitatively? If so, how? Maybe if chirp had similar amplitude as the sum-of-sines then it would be linear. Is there a reason for chirp stimulus to have such large amplitude (and consequently high power)?

8) The frequency response could be calculated using the data from the chirp stimulus (by using cross spectral density and power spectral density). Also, in Figure 3C, using a second x-axis to show the frequency would be helpful.

9) The result for chirp stimulus tracking for control and reattached are very similar (Figure 3C, 3D). What is the explanation for this high similarity?

10) In the Results section paragraph four, the sentence is vague: "abdominal jitter of moths with re-attached flagella differed significantly from control moths at only one frequency (1.66 Hz)". What's the explanation for that? Why only one frequency? Is this meant to be the same frequency that is listed as 1.7 Hz in subsection “Behavioural experiments”?

11) In paragraph two of subsection “Flagella ablation reduces flower tracking performance at high frequencies in hawkmoths”, based on Figure 3B, the tracking error doesn't look significantly higher. Does it mean statistically significant?

12) Figure 4C, 4D: The plots in three colors have overlapped each other so much that they are unclear. Other methods can be used to show the change of noise in different frequencies.

13) In Figure 4C, it is unclear why the dimension of amplitude is shown as Hz.

Reviewer #3:

Concerns

– A parallel is made by authors between halteres role in Dipteran and flagella in hawkmoth. However, it is surprising that the work of Itai Cohen group was not cited in the Introduction (paragraph two). Cohen was probably the first to measure disturbance rejection in free flying fruitfly around the three axes of rotation (roll, pitch and yaw).

It is worth noting that halteres have an essential role in the stabilization of the fly, which is not the case in hawkmoth without flagella: the tracking accuracy is degraded but the flight is still stable in hawkmoth. Only the jitter seems to be higher without flagella but the flight remains stable in hover: the tracking seems to be slower indeed. I do not see any instability according to the definition proposed by control engineers. For example in figure 2, hovering flight with ablated flagella is not instable but less accurate. I suggest authors mention more a more accurate control than an instable control.

– Introduction paragraph four: it is mentioned that antennal mechanosensors play a key role but what kind of role? Authors should add a block diagram to clarify their model and to show clearly the closed-loop control the hawkmoth position:

– the tracking error between the insect and target position will be shown

– the inner loop based on the antenna block could be shown with respect to the control of the head in body orientation.

As the antennal ablation does not introduce instability but less accurate visual tracking, authors could discuss the fact that antennal mechanoreceptors could act as the prosternal organs in fly to allow the animal to measure the orientation of its head with respect to the insect body (head in boy orientation). As suggested by Viollet and Zeil, 2013, prosternal organs may be involved in a mechanoreceptive feedback on head position relative to the thorax. Antennal mechanoreceptors in hawkmoth could play a similar role: they could just improve the control (accuracy) of the head orientation (gaze).

– Subsection “Sum-of-sines movement”: about the tracking error, please clarify why you used this particular metric defined by equation 1.

– What kind of algorithms and software were used to estimate the gain and phase? I recommend having an open access to the programs (code).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The roles of vision and antennal mechanoreception in hawkmoth flight control" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have done an excellent job of addressing the reviewer concerns except in two points.

Essential Revisions:

– Adding the detailed block diagram figure:

The expert reviewers are in strong agreement in consultation that the present control diagram is inaccurate. They recommend that the attached block diagram topology with inner loop be adopted. See the detailed reviews for their reasoning. If the authors insist that a 'simpler' diagram is needed, then the attached block diagram with NO inner loop may be used. Again see the detailed reviews for their reasoning.

– Phase analysis:

There are serious concerns about the phase analysis that were not adequately addressed in revision. See the detailed reviews for how these concerns can be addressed.

Reviewer #2:

Block diagram.

The authors introduce a different block diagram than what was suggested originally, they mentioned that they don't want to limit their conclusion to flower tracking so they introduce a more general block diagram. They want to mention the whole flight control in their block diagram, "not just tracking of a moving flower". The authors' new block diagram (Figure 1A) is unfortunately topologically incorrect. A "postural perturbation" is not defined in this paper anywhere that I can find but let us assume that when the diagram is "reduced" to the present paper, it is a moving flower (since that is all the paper addresses in the way of perturbations, although I wouldn't ever refer flower motion as a "postural perturbation" because it is a sensory perturbation that may lead to postural sway but only indirectly through the visuomotor system; not incorrect but not very clear either).

In any case, the moth's motion is subtracted from the flower motion before going into the visual system but self-motion is not subtracted from flower motion before going to the antennae (unless you are somehow modeling the antenna as a wind sensor which is unlikely). Since I am revealing myself in this review I would be happy to discuss this point further but as drawn this diagram does not make sense. The self-motion feedback to the antenna is grounded and is not subtracted from the sensory feedback. A perfectly acceptable approach would be to remove the subtraction bubble altogether, and draw it in the way that I have suggested.

(You would need to re-do the graphics inside the Sensory Input block to not give the sense that self-motion feedback only goes to the antennae.) The left arrow could be something like "Exogenous perturbation" and the return arrow could be "Self-motion feedback" or, maybe "Exafferent perturbation" for the left incoming error and "Reafferent feedback" for the return path.

Phase lag

Second, the problem with your currently unwrapped phase is that it is -π/2 at 10Hz, which means that the time lag between the input stimulus and the moth motion is 25ms, which seems extremely fast. I've never seen it in any visuomotor control paper in any species (from external motion to animal motion). If you look for example at Roth et al., 2016 he shows roughly 3π/4 to 2π (almost 360o) of phase lag, which corresponds to something like 75ms to 100ms which is a lot more sensible. This is very much in line with the feedback delay estimated by Sponberg, 2016 in their "Luminance dependence" paper. It is not possible it is only 25ms of total time lag (delay + low-pass mechanical phase lag). I don't see a problem with the approach but it is a completely unbelievable result. There are many possible sources of this.

One problem I've had is when I have data streams from different sources that get temporally offset or that temporally drift. This can introduce leads / lags. Another more likely possibility is that the roll off is so fast that your attempt to unwrap just misses it. See the incredible roll off in Eatai Roth's recent PNAS paper. The fastest latency I've seen estimated is Dyhr et al., 2013 (hawkmoth abdomen) which was 41ms but keep in mind that was just to the abdomen not the entire flight behavior, and it is quite possible that the high-pass "lead" filter helped mask some of that delay. Even still at 10Hz, the phase lag was π (180o) from stimulus to abdominal movement. The flight mechanics would surely introduce more phase lag.

Based on the error analysis in the complex plane (which I never really doubted even if I got a bit confused at one point – The explanation re: reduced tracking error at high frequencies is reasonable and I should have realized it before.) I don't think this will affect the main conclusions of the paper but it really does need to be addressed.

Reviewer #3:

There are just three points I would like to address again:

– the new block diagram is not accurate enough. I suggest separating the vision block from the antennal mechanosensors. A visual error can result from a difference between the moth's head orientation and the flower's position. These three signals (head's orientation, flower position and visual error) must be indicated on the diagram. This visual error can then be sent into the vision block, the output of which can be sent to the central integration block. As the mechanosensors seem to play a major role in the stabilisation of the moth, I suggest inserting this block in an inner loop with the motor system block. I agree that this point needs further experiments to determine precisely the function of the mechanosensors.

– Would it be possible that antennae act as a lead compensator (derivator) as the oscillations (jitter) are reduced? This point could be addressed in the discussion.

– Discussion about the role of the antenna to stabilise the head on the basis of the work of Viollet and Zeil (JEB paper) is not included.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The roles of vision and antennal mechanoreception in hawkmoth flight control" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor, and one reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

This is an unusual case where the reviewer's rationale for a rather minor required revision requires a rather long argument. Basically this reviewer calls for a caveat to be added to the Discussion in a short paragraph (or a few sentences to an existing paragraph). This caveat will not change the impact of the work, but will help the reader understand the rather remarkable tracking ability of this moth. Revision can be very swift and will not require re-review.

Reviewer #2:

The authors have done a remarkable job addressing my comments. I particularly appreciate their effort on technical issues such as providing extra data, revised PDFs, etc. Scientifically, I am convinced by the arguments in the revised manuscript; the updated block diagram and the other more minor issues I raised have also been addressed.

The one remaining issue about which I found myself concerned was the issue of phase lag. 90o at 8.9Hz is really quite extraordinary in the animal kingdom and having done system ID on moths, fish, humans, cockroaches, fruit flies, and even non-moving system ID on the jamming avoidance response in electric fish (where there is no "inertial low pass filter"), I've never seen such a short delay on a sensorimotor feedback loop except maybe from some work on haltere feedback. But not only have I been able to recapitulate the results based on their uploaded MATLAB data files, but also was able to reproduce the results from the raw image data, performing my own image tracking. In fact, in that video the phase lag at 8.9Hz is a mere 66o(with excellent SNR), corresponding to a mere 20ms visuo-movement response (total phase lag, including delay and mechanical phase lag). I just simply don't believe that is possible.

The authors claim that the animal is smaller and has a higher wingbeat frequency and therefore 'in-cycle' control would mean low phase lag, but I do not believe the synapses are any faster in this moth than in any other insect – and not even a fruit fly with hundreds of wingbeats per second can respond that fast to visual perturbations (fastest shown about 30ms I believe).

However, I do think I have a possible explanation, which is that there is a direct, mechanical coupling between the flower and the head of the moth via the proboscis. It is the only thing that I can see from the videos that could explain this extraordinary response. (Note that I measured to the tip of the head, not the thorax, when measuring the 20ms lag at 8.9Hz). That said, I think it is clear from the video that there is still a strong sensorimotor component to the behavior and the comparison being made in the paper includes this mechanical coupling for both antenna intact and antenna-ablated conditions. So I do not think that the possible mechanical coupling undermines the results in anyway, since the coupling was present in both conditions.

However, I would appreciate if the authors could acknowledge that these phase lags are unusually short (no known examples in the literature), and that some mechanical coupling may be playing a role. This can be a discussion point and needn't be a major point. It should also say that any such mechanical coupling would be present in both groups (intact vs ablated antenna), and doesn't impact the main findings of the paper.

As an extra step I looked at the bode plots from flower to thorax and flower to abdomen. The thought is that "yanking" the proboscis to the left and right might rotate the body quickly (and therefore show a low phase lag to the rostral end of the animal) but may not move the thorax directly. The moth seems to be rotating around the thorax. I did see much greater phase lags – on the order of 50ms – when I looked at the flower-to-thorax (near the rear of the thorax) transfer function.
