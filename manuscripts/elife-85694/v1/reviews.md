# Peer review - Round 1

Editors:
- Malcolm A MacIver, https://ror.org/000e0be47 Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85694.sa0](https://doi.org/10.7554/eLife.85694.sa0)

Cooperative hunting is typically attributed to certain mammals (and select birds) which express highly complex behaviors. This paper makes the valuable finding that in a highly idealized open environment, cooperative hunting can emerge through simple rules. This has implications for a reassessment, and perhaps a widening, of what groups of animals are believed to manifest cooperative hunting.


---

# Peer review - Round 1

Editors:
- Malcolm A MacIver, https://ror.org/000e0be47 Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85694.sa1](https://doi.org/10.7554/eLife.85694.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Collaborative hunting in artificial agents with deep reinforcement learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

1) There are extensive remarks from the reviewers on the validity of some of the more theoretical claims. These need to be carefully addressed. Examples include whether it is correct to infer that more complex cognition is not needed for cooperative hunting because DQN can solve the problem; The absence of an explicit model does not mean that there isn't an implicit model of the other agents behaviors that is encoded in the neural network weights.

2) The lack of causal analysis either needs to be addressed or the "mediated by"-type claims need to be tempered.

3) There has been a translation of the DQN into simple rules, but at present the discussion is too incomplete for readers to understand why this was done and what can be concluded.

4) A discussion of the limitations of this work in terms of the absence of things like shared value functions increasingly common in multi-agent RL and absence of partially observable environments common in predator-prey dynamics, would be helpful.

5) Please address R3's comment that the paper's analysis is possible without RL, such as via behavioral cloning.

6) Some of the reviews suggest better coverage of the relevant literature. Given the size of this literature, this has to be selective, but it appears some effort could be expended to further improve the scholarship of the work.

Reviewer #1 (Recommendations for the authors):

Figure 2 – The gap between individual and shared only occurs at two predators, for both % successful predation and duration. It would be helpful to have a discussion of this point. Wild dog packs, for example, are typically larger: perhaps this because the space they work over is much larger (relative to disk size), the environment complexity, or something else, but in any case it would be interesting to know whether shared vs individual is the ruling condition.

It also suggests that sharing is not needed in the 3 predator situation to obtain the same results. Does that mean that the work is suggesting cooperation even occurs without sharing? This seems to be a significant problem, since it's hard to imagine how the term "collaboration" or "cooperation" can be applied in the absence of shared reward. If it is strictly a matter of reduction of duration and increase in rate of success, it may equate to a more limited form of cooperation? Are their biological analogs of group hunts without sharing?

186 – We found that the mappings resulting in collaborative hunting were mediated by distance-dependent internal representations.

'Mediated' here seems to play the role of a "filler term" as used in neuroscience (see Krakauer et al. 2017 Neuroscience needs behavior).

Only correlations have been shown, but this is a causal claim. To support the causal claim, it would be necessary to intervene in the network and show that the interventions in the internal representations have the predicted causal role.

194 – The organization of this paragraph might be better reversed. One could argue that Figure S8 (which could be referenced here) providing similar results and DQN helps support the hypothesis that the representation of distance in the network plays a causal role in the outcome.

234 – Initial position of each episode is unclear as previously noted.

236 – The text above says -1 for moving out of arena to the prey, so if the prey moves out, is it just that, or does the predator also get +1 since the predator is now deemed "successful"?

Reviewer #2 (Recommendations for the authors):

– I am not clear that there is sufficient evidence for lines 172-174. The absence of an explicit model does not mean that there isn't an implicit model of the other agents behaviors that is encoded in the neural network weights. I'm not clear what sort of experiment would allow you to distinguish this though there might be a way to run a linear probe to confirm that this information is not in the network weights?

– The notation in lines 246-251 is confusing because it alternates between POMDP notation (i.e. that the agent gets an observation that is a transformation of the true state) and MDP notation. Is the setup an MDP or a POMDP?

– Perhaps line 259 should be "by finding a fixed point of the Bellman equations?"

– Line 271 should be "Dueling Networks" not "Dueling Network" – The sentence starting on line 271 and ending on 273 could or should be cut entirely as it doesn't provide much value and I think it's debatable whether DQN was the first algorithm to solve a high dimensional input problem; it very much depends on how you define high dimensiona

– To get equation 3 from equation 2, there needs to be a factor of 1/2 somewhere.

– In line 321 I don't know what identifiability means in the context of Q-learning? Is this a technical term used in some subfield that works on Q-learning? Why does subtracting the mean help with "identifiability?""

– A discount factor of 0.9 is a wildly low discount factor, basically leading agents to only care about the next 10 steps. I don't think this necessarily affects the outcome of your project or necessarily requires any changes as I don't think agents need to do long horizon reasoning here, but it's worth keeping in mind!

– I don't fully understand the claim that this expands the range of things that are understood to be possible to learn via associative learning. There's no theory precluding a model-free algorithm from learning this type of behavior so the claim in the discussion strikes me as odd. In practice, this type of result where model-free RL agents successfully hunt together have been around since the release of the multi-particle envs (see https://proceedings.neurips.cc/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html)

– I think the rule-based model is neat but I don't understand what what question it answers. Did I perhaps miss something?

– I don't find the evidence for the distance-dependent features compelling; is all of the evidence for it the t-SNE embeddings?

– Lines 194-196 are confusing to me. Why does there being a rule-based model employ your DQN agent is also learning a similar rule-based model?

Reviewer #3 (Recommendations for the authors):My largest suggestion is to fit a linear model to rule-based behaviors and compare the t-SNE embeddings of the behavioral cloning policy with the embeddings of the RL policy? Is the use of RL truly important for this paper?Around line 362, the idea of Rule based agents and human controlled agents are also introduced. I would like to see linear models that take as observations the rule-based agents observations and output the rule based agents actions. Would the t-SNE embeddings look similar for these linear models and for the RL-trained models? If the embeddings look similar, what does that say about the emergence of these capabilities as a result of RL? Does training via RL even matter? Do we care if it doesn't matter?

There is a large amount of work on multi-agent learning that this paper seemingly ignores, or fails to evaluate against. Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments has thousands of citations. However, I am willing to accept that there are limitations to what a single paper can cover.

More specific comments:

Line 46-47. I do not know what "simple descriptions with the distances can reproduce similar behavior" is trying to convey.

Lines 50-51: "Our approach of computational ecology bridges the gap between ecology, ethology, and neuroscience and may provide a comprehensive account of them." This is probably too strong of a claim.

Figure 1: The architecture diagram is a little difficult to understand. The key has "layer with ReLU" but then I do not see any clear white boxes? I also do not see any clear units? I think that maybe this is happening inside of the "prey," "predator 1," etc boxes. However, this is all much too small. I think you should decide if you want this figure to be about the neural network architecture, or about the fact the environment is broken into 1 prey and N predators that share an observation.

I think the actions are also not clear. There are probably too many lines in the figure.

For Figure 1 (b), why not just plot the actual density? Actually, I see this is included in Figure 2. I think this is the more helpful Figure!

In Figure 2, what form of Hypothesis testing was used? Was this a KS test? You can't assume the distributions are Gaussian? The presence of a chi-squared statistic seems to indicate Gaussian assumptions. But the distribution is strongly non-Gaussian in this case. A little more clarity would be helpful.

Line 132 mentions that the variance is higher over the action distribution when the predator is about to catch the prey? This is actually the exact opposite of my intuition. I think that the actions hardly matter when the prey is far away, so there is no obvious optimal action, and the choice would be closer to uniform. I'm not sure that this matters very much, but it's interesting.

Line 325 – Usually IL is reserved for Imitation Learning. I have never seen it used for Independent Learning.

Line 324 – I think biological organisms usually model the behavior of other organisms and account for it while planning.

Line 212 – Q-values do implicitly model the competencies of other agents.

Line 196 – What does it mean to switch the decision rules with the distances?

Overall, I think the problems considered by this paper are interesting. And I am happy you took the time to write it. This work made me think a lot about my own research. I appreciate your efforts here. Thank you.
