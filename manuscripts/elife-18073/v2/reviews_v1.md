# Peer review - Round 1

Editors:
- Naoshige Uchida, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18073.011](https://doi.org/10.7554/eLife.18073.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for resubmitting your work entitled "Adaptive learning and decision-making under uncertainty by metaplastic synapses guided by a surprise detection system" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder as the Senior Editor, a Reviewing Editor, and three reviewers.

The author has performed additional simulations and revised the manuscript extensively. All the referees agreed that the manuscript has greatly improved. However, there are some remaining issues to which we would like to see your response.

1) The reviewers pointed out that it is unclear whether the author's model is biologically plausible as proposed. During discussion, however, the reviewers noted that "biophysiological plausibility" is often difficult to define or relative, and that abstract models are often useful. Nevertheless, because the author now emphasizes biological plausibility in order to contrast with existing models (e.g. Bayesian models; Mackintosh; Pearce-Hall), the reviewers thought a little more clarifications or toning down of this point would be required.

We do appreciate that the proposed model is an important step toward a mechanistic investigation of the interesting question; yet, it appears very difficult to implement some of the key components of the model. Specifically, one important proposal is the "surprise detection system" which takes the difference between the current and expected uncertainty, with uncertainty defined as the range of fluctuation (Figure 2G). To compute this, the author proposes to calculate the difference in synaptic weights of two groups. This is a very interesting idea yet it is unclear how a neural circuit computes the difference in synaptic weights. One reviewer thought that precisely computing the difference of synaptic weights is beyond the ability of neural circuits (or "out of biological constraints"). We would like you to address this point either by showing how such a computation can be performed or approximated while obeying biological constraints or by simply further de-emphasizing the claim for implementation on specific parts although we note that you already state explicitly that network architecture of the surprise detection system is not specified in the present study, and that the efforts toward biophysical implementation is an important aspect of the present study overall.

2) Please make sure that you do not say that the model "implements" Bayes-optimal solution.

3) One reviewer suggested two additional considerations (Reviewer 1's point #2 and #3). Although we do not see these as essential for revision, they might improve the manuscript. So we would like to see your response.

4) During discussion, all the reviewers agreed that we should not raise the concern of biological plausibility of the cascade model.

Below please find the reviewers' original comments, which contains additional comments for your reference.

Reviewer #1:

The author has mostly addressed my comments. Some lingering issues:

1) I don't think it's correct to say that the model implements the Bayes-optimal solution. There's nothing showing that this is true mathematically. What was shown is that it achieves comparable performance. The discussion should be modified to reflect this.

2) The model accounts for the findings of Mazur's second experiment; can it account for the findings of Mazur's first experiment, namely that spontaneous recovery is towards roughly the average of recent sessions? I think it can, which would be a compelling demonstration.

3) While it is nice to see a further application of the model, this seems like a rather random choice of application. Since the author is emphasizing the neural implementation perspective, what one would really like to see is a simulation of specific neural phenomena. Note that the (small number of) phenomena modeled here are all behavioral results. Are there really no neural data bearing on the neural predictions of the model?

Reviewer #2:

The manuscript has been significantly improved and also contains new simulation data. I appreciate all these efforts made for improving the clarity of the manuscript. This work shows an interesting idea in computation and will be highly appreciated by computational journals. However, I still doubt whether the model is biologically plausible enough for publication in eLife.

The author claims that the model is biologically plausible as it is based on a previously published work of the "cascade synapse model". In fact, I doubt the biological plausibility of the cascade model itself even though the cascade model is unique and provides interesting computational functions. The cascade model assumes binary states to avoid unbounded growth of synaptic strength. However, results from various cortical areas have revealed long-tailed or skewed distributions for the strength of cortical synapses (e.g., Song et al., PLoS Biol 2005; Buzsaki and Mizuseki, Nat Rev Neurosci 2014). These results do not seem to be consistent with binary synapses having only a depressed and a potentiated state. Though the long-tailed distributions contain very strong synapses, these synapses only constitute a small fraction of several thousands of synapses a cortical neuron receives, meaning that the fraction of synapses in the potentiated states should be much smaller than that of synapses in the depressed states. However, it is unclear whether the cascade model, or multi-timescale plasticity, also works under such constraint.

Another concern is that there will be a plenty of different ways to implement a surprise detection system. For example, the detection system may be realized within the framework of reinforcement learning as a system that simply monitors the expected amount of instantaneous reward. Though the author claimed that the previous models of surprised detection did not provide much insight into biological implementation (e.g., in the Discussion), so does the present model. This is my honest impression. I feel that the surprise detection system was proposed in this study just to save the specific cascade model.

Reviewer #3:

In the revised paper, several things have been improved.

First, the model by Iigaya is now compared to the Bayesian model by Behrens et al. (2007), and it is shown that the model essentially yields similar results. Second, the model is applied to another type of behavior, and the model can successfully account for this behavior, as well. Third, the method section has been improved and more details to the underpinning of the model have been provided.

In my original review, I had specifically addressed the lack of a clear biophysical implementation of the model. With respect to these points, the author has now more clearly specified the network model, the location of the synapses, and the way they are being modeled. In these respects, I find that the paper has been improved. However, the surprise detection system is still modeled on a purely phenomenological level. This would in principle be fine, except that the author really emphasizes how this model is about a circuit implementation (Marr's third level) of the observed behaviors, and I don’t find that this is really the case.

In fact, my main problem is not even that the surprise detection system is not explicitly modeled as a circuit/ network. Rather, it is that some of the key computations required – taking differences of synaptic strength – seem to rule out any halfway realistic circuit computation. How would information about synaptic strength be propagated to reach a location where the subtraction can then be carried out? Apart from wildly speculative ideas, this is not clear to me. The author addressed this by saying that it is left for future work, but the problem is that it looks like this type of computation cannot be implemented biophysically. There may be other ways of performing the relevant computations, but the current set of computations really seem to rule out that this could work biophysically.

[Editors’ note: a previous version of this study was rejected after peer review, but the author submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Adaptive learning and decision-making under uncertainty by metaplastic synapses guided by a surprise detection system" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Naoshige Uchida as Reviewing Editor and Eve Marder as the Senior Editor. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All the reviewers thought that this work addresses an important question of how the brain adjusts its learning rates in the face of changing volatility of the environment. The author introduce a surprise detection system to a "cascade model" that was previously proposed by Fusi and colleagues. The manuscript is clearly written although it would benefit from better explanations of modeling (see below). Overall, all the reviewers thought that the idea and the results are promising. On the other hand, the reviewers raised a number of concerns that would require substantial revisions. Addressing these concerns would require a substantial amount of simulations and rewriting. It is eLife's policy to not invite revisions that require substantial new scientific work. For that reason, we are forced to reject the manuscript in its current form.

The detailed comments from each referee are attached below. After discussion, the referees thought that the following four points are especially important. First, previous work (e.g. Behrens et al. 2007) have addressed a similar question and presented computational models. The author should compare different models and make the novelty of the current model more explicit. Second, this study only addresses one empirical finding and it is unclear whether this model can explain other phenomena. Applying the current model to other data that demonstrated changes in learning rates would be illuminating. Third, it is argued that the current model is biophysically-inspired but some reviewers thought that the model is still very phenomenological, although this argument could be strengthened by further simulations. Fourth, the methods section requires more work to fully explain the model, and the simulation code should be made available.

Reviewer #1:

This paper presents a new computational model of metaplasticity, building on ideas from the cascade model, which allows synapses to rapidly adapt to changing volatility. This is an important question for biological decision-making systems. The article is clearly written and the theory is elegantly simple. However, I have several fundamental concerns that prevent me from recommending this paper for publication.

1) The model only explains a single empirical finding (adaptation of learning rate to reward volatility). This finding is already explained by a number of other models (for example, see Behrens et al. 2007). So it's not clear to me what this new model is adding.

2) While the model is discussed in terms of synapses, no specific biological evidence is presented that directly supports the assumptions of the model.

3) There's a huge literature on the effects of various experimental manipulations on learning rate. Much of this research was inspired by the seminal models of Mackintosh (1975) and Pearce & Hall (1980). Addressing at least some of this literature is important for demonstrating the explanatory power of the model.

Reviewer #2:

In this work, Iigaya investigates how organisms can adjust their learning rates to the time scales of a randomly varying and somewhat unpredictable environment. The author studies this problem in the context of models of synaptic plasticity. In these 'cascade' models, learning operates on many different time scales. Iigaya shows that an organism can rapidly switch to the right time scale if it has access to a 'surprise' system that detects any changes in an agents' ability to predict outcomes in the environment. The results are illustrated through various simulations.

Overall, I found the paper quite well written and a pleasure to read. I also think it addresses an interesting and important topic. The only quibble I have is that the model, despite being announced as mechanistic and biophysical, is actually rather phenomenological. It would be nice if the author could find a way to better tie the 'synaptic' plasticity to the underlying neurobiology. For instance, if I were to run an experimental lab and was really interested in these learning questions, what exactly should I measure to test this theory? I elaborate a bit more on this below.

Comments:

1) Biophysical realism: Iigaya emphasizes that this is a model of 'synaptic' plasticity. However, the synapses seem to be considered completely in isolation, and their embedding within a network is only hinted at in words. For instance, no neuron model is specified in the method section, and a (somewhat unspecific) network model is only referenced in the main text. I'd be completely fine with a learning model on a purely phenomenological level. However, if the author wants to emphasize that this type of learning occurs at the level of synapses, he should make the model more biophysical, e.g., by introducing a specific neuron and network model etc. The biophysical plausibility is particularly stretched in equation (24) which learns 'differences' between synaptic weights. I am fine with the learning rules per se, but talking about them in terms of networks and synapses seems a stretch. So either really show that this works within a network, or de-emphasize the biophysical interpretation.

2) One simplification of the whole model seems to be that, if an animal has learnt a particular environment quite well, and synapses are fairly stable with slow plasticity, then a change in environment and the concomitant set of 'surprise signals' would essentially erase everything that had been learnt, and start things from scratch (at least for all learning rates faster than the detected surprise). The author states that longer time scales could remain stable, but it seems to me that does not exactly solve problem of switching between environments each of which changes on a faster time scale. This kind of context-dependence may be worth discussing.

Reviewer #3:

Behavioral learning by humans and other animals occurs at multiple timescales. Some years ago, the cascade synapse model successfully modeled the multi-timescale dynamics of synaptic plasticity for decision-making. However, as the overall learning performance gradually shifts to slower timescales in a stationary environment, the cascade synapse model has a difficulty in adapting sudden changes in the environment. To overcome this difficulty, the author proposes a "surprise" detection system for decision-making. The basic idea is to compare the reward information stored in plastic synapses on multiple timescales to detect change points in the environment. Since pieces of evidence suggest that such a signal exists in the brain, the idea and results are of potential interest. However, I feel that the current manuscript is not unambiguously written and is hard to follow for readers unfamiliar with the cascade model. Some improvement is necessary.

Major comments:

1) Figure 2A and E explains the cascade model and surprise detection system, respectively. While reading the manuscript, I wondered whether the two systems work in harmony or work independently without interactions. Though now I find that the former should be the case, how the two systems interact with one another, or how a surprise signal is informed to the cascade synapses, during decision-making is not perfectly clear to me. Methods also do not clarify my doubt. Please explain more about this point. In Methods, mathematical descriptions also require some revisions. For instance, the definition of RB+(-) remains unclear in equations. (20-23). Are there also quantities like RA+(-) as in equations 5-19 of the cascade model? Should the cascade model and surprise detection system have the same depth of multi-timescales? The parameters αrand αnr in the r.h.s. of equations 25 and 26 are not defined, and the meaning of these operations is also unclear.

2) Related to the above point, I want to see in Figure 2F how multiple state variables in the cascade model and surprise detector simultaneously evolve on multiple timescales during decision-making. Showing synaptic strength only for two timescales in Figure 2G is not sufficient to understand the entire decision-making system. For example, is a surprise signal detected only at a pair of some timescales or at multiple pairs of different timescales slower than a critical timescale? Does the complex entire system (cascade model + surprise system) always work consistently on all timescales?

3) Results section, subsection “C. Our model self-tunes the learning rate and captures key experimental findings”: The author mentioned that optimal Bayesian model and the proposed model show a similar behavior of the learning rate in each block of trials. Given this information, the readers may wonder what is the advantage of the proposed model over the optimal Bayesian model. Please make comments on this point.
