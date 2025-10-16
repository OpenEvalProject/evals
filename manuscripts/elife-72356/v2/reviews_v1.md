# Peer review - Round 1

Editors:
- Valentin Wyart, École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72356.sa0](https://doi.org/10.7554/eLife.72356.sa0)

This article describes a carefully designed study on the computational mechanisms underlying judgements of agency in an action-outcome delay task. Model-based analyses of behavior indicate that, unlike judgments of confidence, judgments of agency do not recruit metacognitive processes. This finding is important, because it challenges the assumed relation between agency and metacognition.


---

# Peer review - Round 1

Editors:
- Valentin Wyart, École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72356.sa1](https://doi.org/10.7554/eLife.72356.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Judgments of agency are affected by sensory noise without recruiting metacognitive processing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Valentin Wyart as the Reviewing Editor and Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Valerian Chambon (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

As you will see below, all reviewers agree that the general approach you developed for your study of judgments of agency – combining experimental tasks with explicit computational modeling – is a clear strength of your study. The finding that sensory noise is monitored differently for judgments of agency and confidence judgments is interesting, and novel. However, there are different issues – in particular conceptual ones regarding the definition of metacognition but also experimental ones regarding the relation between the two tasks (and their associated judgments) you have used in your work. The essential revisions below have been discussed among reviewers and should be addressed in a point-by-point response. The individual reviews are also provided below for your information (please check all revisions regarding typos and concerns regarding the presentation of the results), but they do not require point-by-point responses. This is based on your responses to the essential revisions that we will evaluate your revised manuscript.

Essential revisions:

1) A first conceptual issue concerns the definition of metacognition in the study. It appears currently quite loosely defined, which is a problem for a study which makes specific claims about the distinction between metacognition and the sense of agency. In the present version of the manuscript, a metacognitive process appears to mean "being about first-order signals". But this loose definition is not satisfying when thinking about the rescaling model used to explain judgments of agency – which is seen as non-metacognitive. Indeed, this rescaling model still requires agents to track something about internal noise corrupting first-order signals, which would qualify it as metacognitive. A clear and unambiguous definition of metacognition should be provided upfront in the revised manuscript to avoid conceptual confusions.

For example, the authors argue their Bayesian model is a metacognitive one, because it requires the observer to have second-order access to an estimate of their own sensory noise. But even though the Bayesian model in this paper clearly incorporates an estimate of the noise/uncertainty in the signal, not all representations of noise are second-order or metacognitive. For example, Shea (2012) has noted that in precision-weighted Bayesian inference models throughout neuroscience (e.g., Bayesian cue combination, also discussed in this paper) the models contain noise estimates but the models are not metacognitive in nature. For example, when we combine a noisy visual estimate and a noisy auditory estimate, the Bayesian solution requires you account for the noise in the unimodal signals. But the precision parameters in these models do not necessarily refer to uncertainty in the agent's perceptions or beliefs, but uncertainty in the outside world. Similarly, in the Bayesian model proposed in this study, it is not clear why we should think of the uncertainty parameter as something metacognitive (e.g., about the agent's internal comparator representations) rather than something about the outside world (e.g., the sensory environment is noisy). This should be clarified and discussed in the revised manuscript.

Shea (2012) Reward prediction error signals are meta-representational. Nous, DOI: 10.1111/j.1468-0068.2012.00863.x

2) The present manuscript suggests that judgments of agency are subject to only one source of internal noise, the comparator. While it is understandable, given that the task is not likely to be associated with significant action selection (motor) noise, it is possible that this design choice has penalized the hypothesis of metacognitive monitoring of uncertainty by judgments of agency. This would require having a task design that manipulates selection difficulty (and thus selection noise), to see whether judgments of agency are sensitive to selection noise – which would potentially make them metacognitive (since judgments of agency would reflect second-order measures of this selection noise). It is indeed well known that selection noise affects judgments of agency (see, e.g., Wenke et al., 2010), independently of any comparison between predicted and observed signals. While we are not requiring you to perform additional experiments, this prior work and the limitations of the current study along these lines should be explicitly discussed in the revised manuscript.

Related to this issue, the validity of using an action-outcome delay task to generate broad conclusions about the nature of judgments of agency appears currently limited. In the task used in the study, the experience of agency depends only on interval detection, i.e., sensitivity to temporal contiguity. But while this is a popular approach in the field, the temporal contiguity actions and outcomes is only one of the cues that influence judgments of agency. Recent authors (e.g., Wen, 2020) have suggested that this manipulation may be problematic for a number of reasons. In similar types of paradigm, Wen (2020) notes that agents are able to accurately judge their control over action outcomes that are substantially delayed (e.g., well over 1000 ms) and thus it is possible that tasks manipulating action-outcome delays are biasing participants to report variance in the delays they experience rather than their actual experience about what they can and cannot control. Indeed, in the Methods section, the authors note participants were asked to "focus specifically on the timing of the movement" of the virtual hand, which may make this concern particularly salient. The judgment of agency made by participants can thus be reframed in this task as "did I detect a delay?", which limits the generalizability of the findings to many other situations where judgments of agency are not restricted to delay detection.

In practice, these concerns require an explicit discussion in the manuscript. You should at least consider explicitly whether your findings indicate that sensorimotor delay judgements in particular (rather than judgments of agency in general) are non-metacognitive. This alternative, more focused interpretation of the findings, is by no means uninteresting, but it has a somewhat narrower theoretical significance for the key debate used to frame the study ("do agency judgements monitor uncertainty in a metacognitive way?"). Arguments against this alternative (more specific) account should be provided in the discussion to support the interpretation that you have chosen to put forward (that judgments of agency in general are non-metacognitive). It is important that the title and framing of the paper remains as close as possible to what the findings of the study are.

Wen (2020). Does delay in feedback diminish sense of agency? A Review. Consciousness and Cognition, DOI: 10.1016/j.concog.2019.05.007

3) The relationship between the confidence task and the judgment of agency task is not entirely clear. Indeed, the confidence task measures confidence about a discrimination based on judgments of agency, whereas the judgement of agency task is about directly inferring agency from one stimulus. Therefore, the confidence task reflects by design a higher-order judgement about judgements of agency and, in this task setting, the judgments of agency appear to be treated experimentally as first-order judgements. It is unclear whether this choice of task design has triggered in itself the difference in computations underlying confidence and judgments of agency, and whether alternative task settings could show similar computations for the two types of judgments. This does not disqualify the main finding of the study, which is about determining which kind of computations underlie judgments of agency, but it is very important to discuss specifically the relation between the two judgments in this particular task, and how this relation may have something to do with the obtained findings. Further experimental work could – in principle – quash these worries – e.g., by manipulating agency in a different way but demonstrating the same effects of noise on confidence but not agency judgements. We are not requesting you to carry out these additional experiments, but they should be set as critical next steps for addressing the limitations of the current study.

Reviewer #1 (Recommendations for the authors):

1. I find the research question itself really interesting, but I wonder if the authors are arguing against a strawman ("agency judgements are often assumed to be metacognitive"). That agency judgements are assumed to be metacognitive is certainly true according to the references cited in the article (Metcalfe and Miele) but I am not sure that this is a widespread view in the field. To my knowledge, agency judgements are often described as high-level, post-hoc, reflexive or retrospective, but none of these qualifications imply that JoAs are metacognitive per se. More recent references suggesting that indeed JoAs are metacognitive might be needed here.

2. The discussion elaborates on what metacognition is (cognition about cognition, a process that involves 2nd order uncertainty monitoring computations, etc.) but I think a real definition of what a metacognitive process/representation/computation is would be needed in the introductory section, which lacks such a definition.

Is "being about" a first-order signal (whether that signal is perceptual, motor or memory-related) the minimum condition for something to be labelled "metacognitive"?

3. The task is a relatively simple motor task with little motor or premotor noise – in the sense that it does not specifically involve motor preparation or selecting a motor program from alternatives. This premotor/selection noise has been repeatedly shown (e.g. Wenke et al., 2010) to affect JoA, independent of any comparison between predicted and observed signals. Thus, according to this alternative hypothesis, the noise/uncertainty that feeds into participants' JoA does not come from a noisy comparator, as assumed in this paper, but comes directly from the action selection/preparation circuits – i.e. is due to competition between the selected and alternative action program and/or to blurred boundaries between alternative motor plans (e.g. Nachev 2005; Cisek, 2007)

For reasons of parsimony, which I can fully understand, the present study suggests that the JoA is subjected to only one source of internal noise, the comparator.

I wonder to what extent this choice penalizes the hypothesis of (metacognitive) monitoring of uncertainty by the JoA. Is it possible that participants' JoAs are more sensitive to internal selection noise than to comparator noise? This may require replicating the same task by manipulating the selection noise and measuring whether the agency reports reflect second-order measures of this selection noise. Note that I am not asking here for this experiment to be carried out, but perhaps the authors can comment on this.

4. A question of clarification: perhaps I missed something in the manuscript, but what is the internal noise that JoAs monitor? Logically, it should be the noise arising from the comparison between the first-order sensory signals (predicted and observed), a comparison that gives rise to the agentive experience itself. And if so, I am not sure I understand clearly what the source of the noise monitored by the confidence reports in the task is: is it the noise arising from the comparison between the two agentive experiences (which are themselves each the product of a noisy comparison between predicted and observed sensory signals)? Is it then reasonable to assume that this comparison, which gives rise to the confidence report, somehow inherits the noise from the first-order comparison that gives rise to the agentive experience?

Reviewer #2 (Recommendations for the authors):

I was a bit confused about the rationale behind the first criterion which JoA's have to meet in order to be considered metacognitve. It was unclear to me how the JoA's are hypothesized to be influenced by the sensory noise exactly, beyond just making them noisier? Is there a fundamental reason to expect agency ratings to increase or decrease in noisier conditions which we would expect a priori? Expecting 'an effect on agency ratings' sounds rather vague. The results show that the effect of the delay becomes smaller during high noise conditions, which makes a lot of conceptual sense. Maybe pre-empting this somehow before the results will make things a bit clearer?

The contrasting two models elegantly reflect different underlying psychological strategies and are very well designed and implemented. However, I feel like the explanations of the models in the main text are still relatively technical and potentially hard to understand for readers unfamiliar with these specific types of models. I think adding a few extra sentences per model explaining the models in more psychological terms would help (e.g. 'second-order access to estimate their own sensory noise' -> add something like 'i.e. be able to reflect on how noisy their own sensory processing is' and 'rescaling depending on the noise condition' -> 'e.g. give less extreme agency judgments under high noise conditions').

Reviewer #3 (Recommendations for the authors):

In line with these comments above, I would suggest that the authors amend the manuscript to make it clear how detecting action-outcome delays relates to agency detection mechanisms in general – ideally with a persuasive rebuttal of the kinds of concern that Wen (2020) provides. Without a strong reason to believe that action-outcome delay detection is directly measuring the agency detection process (which Wen, 2020 etc. give us cause to doubt), the generality of these conclusions seems potentially limited, and the broadbrush conclusions currently offered might need to be moderated accordingly.

At the same time, I think the authors should also be explicit about what they mean by a 'metacognitive computation'. The real novelty of their approach seems to be getting into the nitty gritty of what different computational models would predict. But if the authors agree with me that models can have uncertainty parameters without being metacognitive, then more needs to be done to justify why the Bayesian model is a metacognitive one. Of course, the authors may disagree with me, but a strong rebuttal of this concern and an explanation for why uncertainty parameters entail metacognition would be an important addition to the paper.

I have a few other points the authors might consider useful and which might help orient a reader:

1. The authors discuss in places that their tasks bring agency judgements into a "standard metacognition framework". But there are some important disanalogies. For example, in a perceptual metacognition task there is a clearly correct Type 1 answer (e.g., stimulus was present or absent) whereas the question posed in these tasks does here does not have an objectively correct answer. Regardless of the stimulus delay, the correct answer is always "I was the agent", so really the task is looking at variance in Type 1 and Type 2 judgements which is separate from the ground truth (i.e., they are always the agent on every trial). This strikes me as an important difference from the standard metacognition framework as it is applied to perception or memory judgements, and may thus be worth flagging explicitly to a reader.

2. The Gaussian schematics of the models in Figure 2, Figure 3 etc. are a bit opaque without describing what the underlying variable is. Making it clear these show a probabilistic representation of sensorimotor delays would make these more intelligible.

3. The authors split the paper into 'confirmatory' and 'exploratory' analyses. I understand why, given their pre-registration, but my personal feeling was this disrupted the flow of the paper somewhat, since it means the reader sees the confidence task, then the agency task, then a model of the agency data, then a return to the confidence task. Grouping the sections by task (e.g., confidence task/ confidence model/ agency task/ agency model) might build up the authors conclusions more naturally since it establishes 'what is metacognition like?' before then asking 'is agency like that?'. Of course, this is just a thought, and doesn't change the substance of what is presented.

4. In Figures that show model predictions or simulated data (e.g., Figure 3) I think it could be helpful to show simulated/predicted data in the same format as the original data displays (e.g., matching the plots of how data is shown in Figure 2c). This would make it easier for the reader to compare qualitative differences between the simulated and real data, and between each of the models. (Admittedly, this is done in Figure 4, but the granularity of the presentation is hard to translate back up to the big picture patterns observed in the experiments).

5. In standard use 'noise' is something added to stimuli to make discriminations harder. Here the signal strength is actually reduced by dimming the virtual lights, rather than adding a noise mask etc. Labelling the conditions as something like 'Signal strength – High/Low' (reversed accordingly) might be more appropriate.

6. p.22 "pre-reflexive FoA". I think the authors may mean 'pre-reflective'
