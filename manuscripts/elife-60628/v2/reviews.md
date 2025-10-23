# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60628.sa1](https://doi.org/10.7554/eLife.60628.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study investigates how sensory representations in visual cortex are modulated by ongoing task requirements as rats navigate a virtual environment and make a choice based on the total numbers of discrete stimuli, or 'pulses,' seen along the path. The main finding is that only a small fraction of active neurons had sensory-like responses time-locked to each pulse, and furthermore, for those that did, the amplitude of the response changed systematically as the impending choice advanced to completion. This shows that, even at a very basic level, the representation of sensory stimuli is strongly modulated and shaped by cognitive factors and behavioral relevance, and that a lot of the variability associated with sensory activity is not just random noise, as it often appears.

Decision letter after peer review:

Thank you for submitting your article "Amplitude modulations of sensory responses, and deviations from Weber's Law in pulsatile evidence accumulation" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require additional new data or analyses, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional work and report on how it affects the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This manuscript carefully studies the properties of sensory responses in several visual areas during performance of a task in which head-fixed mice run along a virtual corridor and must turn toward the side that has more visual cues (small towers) along the wall. The results provide insight into the mechanisms whereby sensory evidence is accumulated and weighted to generate a choice, and on the sources of variability that limit the observed behavioral performance. All reviewers thought the work was generally interesting, carefully done, and novel.

However, the reviewers' impression was that the manuscript as it stands is very dense. In fact, it is largely two studies with different methods and approaches rolled into one. The first one (physiology) is still dense but less speculative and with interesting, solid results, and the revisions suggested by the reviewers should be relatively straightforward to address. In contrast, the modeling effort is no doubt connected to the physiology, but it really addresses a separate issue. The general feeling was that this material is probably better suited for a separate, subsequent article, for two reasons. First, because it will require substantial further work (see details below), and second, because it adds a fairly complex chapter to an already intricate analysis of the neurophysiological data.

So, going forward, we suggest that the authors revise the neurophys analyses along the lines suggested below (largely addressing clarity and completeness), leaving out the modeling study for a later report. If, however, the authors wish to maintain the current structure, they should address all the comments, and understand that we would reconsider the manuscript's suitability for publication after full re-review.

Revisions for this paper:

1) More should be done to highlight how very different the sensory representation is in this study compared with the great majority of earlier related work in the primate. This merits at least some discussion, and optimally, additional analyses of correlations in the data. See the comments from reviewer 3 for details.

2) Figure 4E was confusing. What is the point of showing the shades (which extend very far)? If the idea is to contrast the SSA and feedback models, then it would be better to plot their corresponding effects directly, on the same graph, or to show predictions versus actual data in each case, in two graphs. In any case, the data need to be shown in a different way, or the point made differently.

Similarly for Figure 3F. Could the authors explain how each point is calculated? I was specially confused about the meaning of the points for each area in the x-axis.

3) The prediction about the Fano Factor (FF) is problematic in a couple of ways. First, it seems to come out of the blue because Figure 5 is described before any discussion of the variability in the model is presented (except for the dice in the model schematic).

And second, the FF prediction itself is verified for a very small fraction of neurons even when an unusual pValue of 0.1 is used. Furthermore, the mathematical derivation relies on an Taylor series around NR ~ 0? (In most of the paper, CLT is invoked on the assumption NR is "large"). Due to the lack of transparency of this prediction and the mild support, the authors could consider dropping it, at least from the main manuscript.

4). The 1st prediction in Figure 5 seems very unspecific. In particular, it would seem like any "open loop" modulation of the cue-locked response which depended on time, or on location along the track, would induce a trend like the one assessed in Figure 5C-E. It is not clear this is a prediction specific to the multiplicative-feedback model the authors are advocating for.

5) The number of cells showing responses consistent with the model (Figure 5E) seems very small (~15% of 5-10% of cells with cue-locked responses). Could they really underlie the behavioral effects? The authors could perhaps comment on this.

6) It wasn't completely clear how the time of a particular cue onset was defined. In a real environment the cues would appear small (from afar) and get progressively bigger as the animal advances (at least if they are 3D objects, as depicted in Figure 1). What would be the cue onset in that case, and does the virtual environment work in the same way? This is probably not a serious issue, but it comes across as a bit at odds with the supposed "pulsatile" nature of the sensory stream, and would seem somewhat different from the auditory case with clicks.

A related question concerns multiple references to cue timing made in the Introduction, as if such timing were very precise. This seems strange given that all time points depend on the running speed of the mice, which is surely variable. So, how exactly is cue position converted to cue time, and why is there an assumption of very low variability? Some of this detail may be in previous reports, but it would be important to make at least a brief, explicit clarification early on.

Revisions expected in follow-up work:

For details, see comments 1-3 from reviewer 2 and comment 1 from reviewer 1, below.

Reviewer #1:

This study investigates the responses of neurons in the parietal cortex of mice (recorded via two-photon Ca imaging) performing a virtual navigation task, and then relates their activity to the animal's psychophysical performance. It is essentially two studies rolled into one. The analysis of neurophysiological activity in the first part shows that visually driven responses in the recorded "cue cells" are strongly modulated by the eventual choice and/or by the integrated quantity that defines that choice (the difference in left vs. right stimulus counts), as well as by other task variables, such as running speed. The model comparison study of the second part shows that, in the context of a sensory-motor circuit for performing the task, this type of feedback may account for subtle but robust psychophysical effects observed in the mice from this study and in rats from previous studies from the lab. Notably, the feedback explains intriguing deviations in choice accuracy from the Weber-Fechner law.

Both parts are interesting and carefully executed, although both are pretty dense; there are a ton of important technical details at each step. I wonder if this isn't too much for a single study. Had I not been reading it as a reviewer, I probably would have stopped after Figure 4 or just skimmed the rest. After that, the motivation, methods, and analyses shift markedly. I'm not pushing hard on this issue, but I think the authors should ponder it.

Other comments:

1) Figure 6 and the accompanying section of the manuscript investigate a variety of models with different architectures (feedback vs. purely feedforward) and noise sources. Here, if I understood correctly, the actual cue-driven responses are substituted with variables that are affected by different types of noise. It is this part that I found a bit disconnected from the rest, and somewhat confusing.

Here, there's a jump from the actual cells to model responses. I think this needs an earlier and more explicit introduction. It is clear what the objective of the modeling effort is; what's unclear are the elements that initially go into it. This is partly because the section jumps off with a discussion about accumulator noise, but the modeling involves many more assumptions (i.e., simplifications about the inputs to the accumulators).

What I wondered here was, what happened to all the variance that was carefully peeled away from the cue driven responses in the earlier part of the manuscript? Were the dependencies on running speed, viewing angle, contra versus ipsi sensitivity, etc still in play, or were the modeled cue-driven responses considering just the sensory noise from the impulse responses? I apologize if I missed this. I guess the broader question is how exactly the noise sources in the model relate to all the dependencies of the cue cells exposed in the earlier analyses.

Overall, my general impression is that this section requires more unpacking; perhaps it should become an independent report.

Reviewer #2:

In this manuscript, the authors present an in-depth analysis of the properties of sensory responses in several visual areas during performance of an evidence-accumulation task for head-fixed running mice (developed and studied by the authors previously), and of how these properties can illuminate aspects of the performance of mice and rats during pulsatile evidence accumulation, with a focus on the effect of "overall stimulus strength" on discriminability (Weber-Fechner scaling).

The manuscript is very dense and presents many findings, but the most salient ones are a description of how the variability in the large Ca++ transients evoked by the behaviourally-relevant visual stimuli (towers) are related to several low-level behavioural variables (speed, view) and also variables relevant for the task (future choice, running count of accumulated evidence), and a framework based on multiplicative-top down feedback that seeks to explain some aspects of this variability and ultimately the psychophysical performance in the accumulating-towers task. The first topic is framed in the context of the literature on choice-probability, and the second in the context of "Weber-Fechner" scaling, which in the current task would imply constant performance for given ratios of Left/Right counts as their total number is varied.

Overall, the demonstration of how trial to trial variability is informative about various relevant variables is important and convincing, and the model with multiplicative feedback is elegant, novel, naturally motivated by the neural data, and an interesting addition to a topic with a long-history.

1) Non-integrable variability. In addition to 'sensory noise' (independent variability in the magnitude of each pulse), it is critical in the model to include a source of variability whose impact does not decay through temporal averaging (to recover Weber-Fechner asymptotically for large N). This is achieved in the model by positing trial-to-trial variability (but not within-trial) in the dot product of the feedforward (w) and feedback (u) directions. But the way this is done seems to me problematic:

The authors model variability in w*u as LogNormal (subsection “Sources of noise in various accumulator architectures”). First, the justification for this choice is incorrect as far as I can tell. The authors write: "We model m̂R with a lognormal distribution, which is the limiting case of a product of many positive random variables". But neither is the dot product of w and u a product (it's a sum of many products), nor are the elements of this sum positive variables (the vector u has near zero mean and both positive and negative elements allowing different neurons to have opposite preferences on choice – see e.g., in the subsection “Cue-locked amplitude modulations motivate a multiplicative feedback-loop circuit model” where it is stated that ui<0 for some cells), nor would it have a LogNormal distribution even if the elements of the sum were indeed positive. Without further assumptions, the dot product w*u will have a normal distribution with mean and variance dependent on the (chosen) statistics of u and w.Two conditions seem to be necessary for u*w: it should have a mean positive but close to zero (if it's too large a(t) will explode), and it should have enough variability to make non-integrable noise have an impact in practice. For a normal distribution, this would imply that for approximately half of the trials, w*u would need to be negative, meaning a decaying accumulator and effectively no feedback. This does not seem like a sensible strategy that the brain would use.

The authors should clarify how this LogNormality is justified and whether it is a critical modelling choice (as an aside, although LogNormality in u*w allows non-negativity, low mean and large variability, the fact that it has very long tails sometimes leads to instability in the values of a(t)).

2) Related to this point, it would be helpful to have more clarity on exactly what is being assumed about the feedback vector u. The neural data suggests u has close to zero mean (across neurons). At the same time, it is posited that u varies across trials ("accumulator feedback is noisy") is and that this variability is significant and important (previous comment). However, it would seem like neurons keep their choice preference across trials, meaning the trial to trial variability in each element of u has to be smaller than the mean. The authors only describe variability in u*w (LogNormal), but, in addition to the issues just mentioned about this choice, what implications does this have for the variability in u? The logic of the approach would greatly increase if the authors made assumptions about the statistics of u consistent with the neural data, and then derived the statistics of u*w.

3) Overall, it seems like there is an intrinsically hard problem to be solved here, which is not acknowledged: how to obtain large variability in the effective gain of a feedback loop while at the same time keeping the gain "sufficiently restricted", i.e., neither too large and positive (runaway excitation) nor negative (counts are forgotten). While the authors avoid worrying about model parameters by fitting their values from data (with the caveats discussed above), their case would become much stronger if they studied the phenomenology of the model itself, exposing clearly the computational challenges faced and whether robust solutions to these problems exist.

Reviewer #3:

This manuscript describes measurements of neuronal activity in mice performing a discrimination task, and a new model that links these data to psychophysical performance. The key element of the new model is that sensory neurons are subject to gain modulations that evolve during each trial. They show that the model can produce pure sensory integration, Weber-Fechner performance, or intermediate states that nicely replicate the behavioral observations. This is an interesting and valuable contribution.

My only significant comment relates to the Discussion, which should do more to make sure the reader understands how very different the sensory representation is in this study compared with the great majority of earlier related work in the primate:

First, choice related signals are not systematically related to stimulus preferences (no Choice Probability). This is mentioned, but only very briefly.

Second, there appears to be no relationship between stimulus preference (visual field in this case) and noise correlation. Unfortunately, this emerges from the model fits, not an analysis of data. But is an important difference with profound implications for how the coding of information is organized. It really needs a discussion. It should also be supported by an analysis of correlations in the data. I know some people argue that 2 photon measures make this difficult, but if that's true then surely they can’t be used to support a model in which correlations are a key component.
