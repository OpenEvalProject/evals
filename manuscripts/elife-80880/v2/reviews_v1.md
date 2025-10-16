# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80880.sa0](https://doi.org/10.7554/eLife.80880.sa0)

The manuscript makes an important contribution to feedback control in neural systems. The analysis and modeling together make a compelling case for a nested system, combining visual with mechanosensory feedback, for head and body control in the fruit fly. The experiments that support these results are compelling and well-executed and the strategies for dissecting and modeling feedback are valuable to the field, and broadly applicable to other neural control systems. This paper will reach a wide audience; researchers investigating biological control systems, visual feedback, and gaze stabilization will all be interested in these results.


---

# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80880.sa1](https://doi.org/10.7554/eLife.80880.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Unraveling nested feedback loops in insect gaze stabilization: Mechanosensory feedback actively damps visually guided head movements in fly flight" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

All of the reviewers enjoyed this paper but thought that some revisions to the presentation of results and the discussion would improve the manuscript. New experiments are discussed in the individual reviews but are not required for this revision. However, the reviewers all felt that including alternate paradigms, hypotheses, and the experiments that do or could distinguish them are crucial adds to the text. Those and other essential elements are summarized here, with individual reviews included at the end:

Essential revisions:

1) It is important to distinguish this model from prior ones in flies, from ones in vertebrates, and from other potential models that could account for the data. This kind of hypothesis testing of model architectures seems like it would add a lot to the paper, especially if you could rule out classes of models and suggest multiple alternative models consistent with your data (and other data in the field). Please see R3's comments along these lines, especially.

2) Issues with the presentation of the results:

(2a) Presentation issues should be addressed to clarify experiments and what each is doing/testing. Reviewers found some of the figures hard to follow, which was surprising given what seemed like relatively straightforward modeling. Please see R2's comments along these lines, in particular.

(2b) All reviewers found the presentation of the nested versus feedback architecture confusing, on different levels. Definitely clarify if dissecting this is an assertion from the outset (and if so, please modify that claim according to the detailed feedback from R3 and R3), or a hypothesis that is being tested. If the latter, please make it easier to read out the weight of the evidence supporting the nested feedback hypothesis, along the lines of R1's comments.

Reviewer #1 (Recommendations for the authors):

This paper aims to dissect the structure of feedback control in the stabilization of gaze when both the external world and the body and head are in motion. To achieve this, sensory-motor systems must integrate visual and self-motion cues, but the precise structure of that integration is not generally known in invertebrate systems. The authors focus on the fly as a model system, where previous work establishes a firm grounding for the results but gaps in knowledge of how canonical experimental manipulations, e.g. anchoring the body, affect motor responses still abound. Using an elegant experimental design where the same visual inputs are delivered during body-fixed and body-free tethered flight, the authors are able to quantify how gaze stabilization is impacted by the two forms of feedback. The work reveals that visual feedback shifts the scale of head movements when the external world moves at different frequencies, but that the self-motion cues from body rotations serve to dampen head movements and are nested within the visual control feedback loop. The nonlinearity in this nested control system is quantified convincingly in the paper.

Main strengths:

– The experimental design and analyses are well-motivated and executed.

– There are clear differences between the head movements and frequencies responses to external visual perturbations in the head-fixed and head-free conditions.

– The proposed model accounts for the empirical data in the two scenarios nicely.

Main weaknesses:

– The strength of the evidence for the differentiation between the two feedback schemes was not clear, and Figures 4 and 5 were hard to follow without more information.

– It was not clear if the model proposed is unique as opposed to simply sufficient for explaining the empirical data.

The work will be of interest to motor and systems neuroscientists who study feedback control, across a broad range of species. Biomechanics researchers will benefit from the framework laid out here and this will inspire future work to uncover the possible mechanisms of this control. Beyond biology, engineers and robotics researchers will take interest in this kind of nested feedback control, for the design of bio-inspired robotic systems.

There is a strong assumption about the analytical form of the feedback gain control (G/(1+G)), and this needs a sentence at least of justification and background in the Results.

Figures 4 and 5 highlight the main results of the work, but it was hard to figure out the strength of the evidence for the nested control topology from the figures. It would greatly enhance the broader impact of the work if these figures were made more intuitive for the reader. Perhaps the figures could start by showing a cartoon of what the results should look like in the extreme case of each feedback scenario and weighting, to set expectations.

Are there other options for the control system that would produce different results in the body-fixed versus body-free flies? It seems like this isn't the only feedback control scheme possible, so a more careful discussion of why the one proposed might be the unique solution to the problem and match the data is crucial.

Something needs to be said in the Discussion about how this adds to what we already knew from the primate literature about nested VOR feedback within OKR feedback. Does this new work point to new mechanisms? In the OKR, there's been good work showing that similar feedback is achieved in primates and zebrafish, but with very different circuitry. Can similarly crisp claims be highlighted here?

Are there new experiments suggested by these results in other species that could broaden the impact of work in the future?

Reviewer #2 (Recommendations for the authors):

In this work, the authors present a model for mechanosensory feedback nested inside a visual feedback loop, both controlling body and head yaw rotations. Using a variety of experiments, they fit this model to behavioral data in the fruit fly, where head and body yaw rotations can be easily measured, and in some cases, feedback can be manipulated. They use this data to fit their model and draw conclusions about how different feedback loops interact to stabilize the gaze in the fly.

The strength of this paper is in its rigorous approach to modeling the feedback in the fly's interactions with the visual world. It manages to fit its model non-parametrically at several different ethologically relevant frequencies of feedback. The comparisons of behavior with and without mechanosensory feedback are illuminating, as is the comparison of voluntary with involuntary mechanical feedback. One weakness of the paper is in its presentation, which can be a little opaque for non-specialists in control theory.

This paper provides a methodology for dissecting how different feedback systems interact and combine to jointly control behavior. While the specific manipulations available in the fly are not universally available, the approach seems likely to be useful for investigating many systems.

Overall, this work looks well done and contributes valuably to understanding how head and body feedback systems work in tandem to stabilize gaze in flies. Most of my major comments relate to the presentation.

Major comments

1) In the introduction, it would help if the authors laid out a little more about what's known and not known, and what precisely this paper is adding to the literature. For instance, the authors state that it's already known that mechanosensory feedback represents nested feedback inside the visual feedback loop. So what's left is merely fitting the model to data? Or are there alternative models that could be tested and ruled out with this data? (If there are, I think the framework of testing alternatives could be powerfully convincing about how predictive this particular model is.) At the end of the introduction, I was left puzzled about what the authors were adding.

2) The stimulus pattern should be defined. Pictures show a square wave grating; is this accurate? Does it matter? What was the wavelength? It looks like a 30 d period or so from the illustrations, which would put maximum temporal frequencies of the moving pattern at ~250 d/s / (30 d) = 8 Hz, which is about right for maximally driving optomotor responses.

Questions:

a. The perturbation signal R is a displacement but is measured presumably as a velocity by the eyes, and the direction-selective signal from the eye is a nonlinear function of velocity. If the tuning of the velocity signal is different for guiding body vs. head movements, does that matter or does that fit easily into this theory? In the presented model, there's only one single visual feedback signal to both body and head.

b. In the fastest oscillating stimuli, the pattern only moves back and forth by 2 pixels or so, and I believe these LEDs have something like 8 brightness levels. Is the intended stimulus really accurately captured by this display?

3) The model section of the methods should be clearer about what the different signals and coefficients are. As I understand it, everything is complex, so the products represent both gain and phase shifts of sinusoids, represented as complex numbers. It would be helpful to define why R should be thought of as displacement rather than velocity, and whether H, B, and G represent angles or angular velocities. Head angle is relative to the body, so angle seems reasonable, but I'd expect body orientation signals to be angular velocities or even accelerations. This might all not matter since it's all in a linear framework, but I think this could nonetheless be made clearer to non-specialists by defining the variables and terminology more explicitly. In the text, there's a reference to a complex s, which I assume is part of the integrand for a Laplace transform, but this could be spelled out more clearly or not mentioned at all since Laplace transforms are otherwise avoided. Then these gain and phase shifts are computed for each frequency of the stimulus, and non-parametric curves are found for each complex coefficient.

4) There's at least one alternative way to break the feedback here, and I'm curious about why it wasn't used to test or fit models. Instead of breaking the mechanosensory feedback loop, one could leave it in place, and instead, place flies in a virtual open loop, so that there is no visual feedback from the behaviors. It might be hard to track the head in real time to do this, but I'm interested to know if there are tests of the theory that could result from this sort of perturbation to the system. Along the same lines, gluing the head to the thorax would remove one source of gaze feedback and could be used to test the model for body movements. Are these interesting tests to do? (I'm not necessarily asking for these experiments.)

Reviewer #3 (Recommendations for the authors):

The goal of this paper is to use the fruit fly Drosophila melanogaster to assess the relative contributions of vision and mechanosensory feedback in controlling head motion about the vertical, or yaw, axis. The authors perform a set of behavioral experiments comparing flies that are free to rotate in the yaw plane with rigidly tethered flies, using a control theoretic framework to make quantitative predictions about the importance of each sensory modality. They propose a model where mechanosensory feedback is nonlinearly integrated with visual feedback to control head steering, but only in the presence of whole-body rotations.

Overall, I find the paper well-written and the data very nicely presented. I appreciate the authors' formal use of control theory to make algebraic predictions about how the flies should respond to each perturbation and think this work adds a great deal to understanding the differences between free and tethered flight. I also like the conceptual approach of comparing parallel and nested sensory fusion problems in locomotion. That being said, I do have some major concerns about the approach that needs to be seriously addressed.

Control model and "eliminating" haltere feedback

This paper compares gaze stabilization in flies that can freely rotate about the yaw axis with those that are rigidly tethered. Crucially, in figure 2A, haltere feedback is presented as being a nested feedback loop that is only the result of the animal's body mechanics. In addition, the legend for 2C states, "Note that contributions of body visual and mechanosensory feedback are no longer present and all nested feedback is gone." In light of recent work, specifically Dickerson et al. 2019, I do not think the authors' view on either matter is correct. As that paper shows, the haltere is providing constant input to the wing steering system-even in the absence of body rotations (It is also worth noting that Fayazzuddin and Dickinson 1999 proposed a model of wing steering muscle function where the wing and haltere provide constant, rhythmic input). Those experiments relied on imaging from the haltere axon terminals in the brain that likely synapse onto neck motor neurons that help control gaze (Strausfeld and Seyan 1989). Moreover, that feedback is partially under visual control; the haltere steering muscles change the trajectory of the haltere in the presence of visual input alone, modulating the feedback it provides to the wing steering system. I am not sure if that makes the haltere system parallel or nested with the visual system, but it certainly means that haltere feedback is not solely due to body mechanics. More importantly, this knowledge of physiology means that in a rigidly tethered fly, the authors cannot fully eliminate haltere input. This has tremendous implications for their modeling efforts, as they can never fully bring Ghead,M to zero. This may explain why, in Figure 4, body visual feedback alone cannot account for changes in head gain. It also means that a diagram like Figure 5B is essentially not possible in an intact fly, as the haltere signal is ever-present.

Proposed neural architecture

The authors propose a model of head stabilization in which the visual system sends motor commands to the neck in parallel with a gating command to the haltere that is only present during body motion. To me, this is essentially the "control-loop" hypothesis, proposed by Chan et al. 1998 and confirmed by Dickerson et al. 2019. In that model, the halteres provide continuous, wingbeat-synchronous feedback during flight. As the fly takes visual input, the haltere steering muscle motor neurons receive commands relayed by the visual system, altering the haltere's motion. This, in turn, recruits more campaniform sensilla for each wing stroke, which fire at different preferred phases from those providing the initial rhythm signal. Then, due to the haltere's direct, excitatory connection with the wing steering muscles, this changes the timing or recruitment of the wing steering system, changing aerodynamic forces and the fly's trajectory. This suggests that the haltere's gyroscopic sensing is an epiphenomenon that coopts its likely ancestral role in regulating the timing of the wing steering system, rather than the other way around. Again, whether this means that the visual → haltere connection is parallel or nested within the visual loop proposed by the authors, I am not certain, though I lean toward the former. Additionally, it is crucial to note that the haltere has collateral projections to the neck motor centers. Thus, as the visual system manipulates haltere kinematics and mechanosensory feedback, the haltere is controlling head motion in a reciprocal fashion, even when there are no imposed body motions. Even the nonlinear gating of neck motor neurons the authors note here is not entirely in keeping with the model proposed by Huston and Krapp 2009. There, the presence of haltere beating or visual stimulus alone was not enough to cause the neck MNs to fire. However, simultaneous haltere beating and visual stimulus did, implying that the fly need only be in flight (or walking, in the case of Calliphora) for the halteres to help control head motion; Coriolis forces due to body rotations imposed or otherwise, need not be present. The only difference I can see between what the authors propose and the control-loop hypothesis is that they focus on the head (which, again, is covered by the revised model of Dickerson et al.) and that the nonlinear damping gate requires body motion (which is inconsistent with the findings of Huston and Krapp).

I think the most critical change is rethinking the control model of visual and mechanosensory feedback in light of our understanding of the haltere motor system. As noted earlier, the experiments with rigidly tethered flies do not fully eliminate haltere feedback, which greatly impacts the math used to make predictions about how the animals respond to various perturbations. I recognize this requires a severe overhaul of the manuscript, but my concern is that by considering the haltere as merely a passive gyroscopic sensor leaves out a number of potential explanations for the data in Figures 4 and 5. Additionally, the authors need to think hard about whether the haltere is controlled in parallel or nested with the visual system, given that they have a reciprocal relationship even in the case of a rigidly tethered fly.

I was rather surprised in the section about active damping of head saccades that there was almost no mention of the recent work by Kim et al. 2017 showing that head motion during saccades seems to follow a feedforward motor program (or Strausfeld and Seyan's 1988 (?) work detailing how vision and haltere info combine to help control head motion). Furthermore, the head velocities for body-free and rigidly tethered flies seem similar, which points to it being a feedforward motor program, a la Kim et al. If you subtract body displacement from the free-rotating head motion, do you get a similar result? That would hint that head isn't overcompensating during body-fixed experiments and is driven more reflexively, as proposed in the discussion. I would also recommend looking at Bartussek and Lehmann 2017 for the impact of haltere mechanosensory input on 'visuomotor' gain, or the work from the Fox lab.

Finally, the authors either need to detail how their model is distinct from the control-loop hypothesis or back off their claim of novelty and show that their work lends further evidence to that model. I would also prefer if the figure panel for the model is either more anatomically accurate or stuck with the block diagram framing of information flow.
