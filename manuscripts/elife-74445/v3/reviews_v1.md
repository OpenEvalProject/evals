# Peer review - Round 1

Editors:
- David Badre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74445.sa0](https://doi.org/10.7554/eLife.74445.sa0)

This paper addresses an important problem in control of episodic memory. This paper develops a computationally-based proposal about how semantic, working memory, and episodic memory systems might learn to interact so that stored episodic memories can optimally contribute to reconstruction of semantic memory for event sequences. This is an understudied area and this present work can make a major theoretical contribution to this domain with new predictions. The reviewers were positive about the contribution in review, and the revisions have clarified the model in a number of important ways, including through some additional simulation and analysis.


---

# Peer review - Round 1

Editors:
- David Badre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74445.sa1](https://doi.org/10.7554/eLife.74445.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article ‘When to retrieve and encode episodic memories: a neural network model of hippocampal-cortical interaction’ for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by David Badre as Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tim Rogers (Reviewer #2); Michael E. Hasselmo (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers and editors were in agreement that this paper addresses an important and novel problem using a elegant but powerful approach. There was consensus that this can make a contribution to the literature, pending some revisions for clarify. The major points of clarification raised by the reviewers are provided below.

1) It is not clear how the sequences were constructed and how these relate to the structure of real schematic events. From the methods it looks like the inputs to the model contain a one-hot label indicating the feature observed (e.g., weather), a second one-hot vector indicating the feature value (e.g., rainy), and a third for the query, which indicates what prediction must be made (e.g., ‘what will the mood be’?). Targets then consist of potential answers to the various queries plus the ‘I don't know’ unit. If this is correct, two things are unclear. First, how does the target output (ie the correct prediction) relate to the prior and current features of the event? Like, is the mood always ‘angry’ when the feature is ‘rainy,’ or is it chosen randomly for each event, or does it depend on prior states? Does the drink ordered depend on whether the day is a weekday or weekend---in which case the LSTM is obviously critical since this occurs much earlier in the sequence---or does it only depend on the observed features of the current moment (e.g., the homework is a paper), in which case it's less clear why an LSTM is needed. Second, the details of the cover story (going to a coffee shop) didn't help to resolve these queries; for instance, Figure 2 seems to suggest that the kind of drink ordered depends on the nature of the homework assigned, which doesn't really make sense and makes reviewers question their understanding of Figure 2. In general this figure, example, and explanation of the model training/testing sequences could be substantially clarified. Maybe a figure showing the full sequence of inputs and outputs for one event, or a transition-probability graph showing how such patterns are generated, would be of help. Some further plain-language exposition of the cover-story and how it relates to the specific features, queries, and predictions shown in Figure 2 could be helpful.

2) The authors show that their model does a better job of using episodic traces to reinstate the event representation when such traces are stored at the end of an event, rather than when they are stored at both the middle and the end. In explaining why, they show that the model tends to organize its internal representations mainly by time (ie events occurring at a similar point along the sequence are represented as similar). If episodes for the middle of the event are stored, these are preferentially reinstated later as the event continues following distraction, since the start of the ‘continuing’ event looks more like an early-in-time event than a late-in-time event. This analysis is interesting and provides a clear explanation of why the model behaves as it does. However, reviewers want to know if it is mainly due to the highly sequential nature of the events the model is trained on, where prior observed features/queries don't repeat in an event. They wonder if the same phenomenon would be observed with richer sequences such as the coffee/tea-making examples from Botvinick et al., where one stirs the coffee twice (once after sugar, once after cream) and so must remember, for each stirring event, whether it is the first or the second. Does the ’encode only at the end’ phenomenon still persist in such cases? The result is less plausible as an account of the empirical phenomena if it only "works" for strictly linear sequences.

3) It would be helpful to understand how/why reinforcement learning is preferable to error-correcting learning in this framework. Since the task is simply to predict the upcoming answer to a query given a prior sequence of observed states, it seems likely that plain old backprop could work fine (indeed, the cortical model is pre-trained with backprop already), and that the model could still learn the critical episodic memory gating. Is the reinforcement learning approached used mainly so the model can be connected to the over-arching resource-rational perspective on cognition, or is there some other reason why this approach is preferred?

4) The details of the simulations provided in the methods section could be clarified. First, on page 20, it is unclear about how w_i is computed. It seems to compute w_i (activation of trace i) you need to first compute activation of all other traces j, but since all such computations depend each other it is not clear how this is carried out. Perhaps you initialize this values for tau=0, but some detail here would help. Second, the specification of the learning algorithm for the A2C objective on page 21 has some terms that aren't explained. Specifically, it is not clear what the capital J denotes and what the /pi denotes. Third, other details about the training sufficient to replicate the work should also be provided--for instance, an explanation of the "entropy regularization" procedure, learning rates, optimizer, etc, for the supervised pre-training, and so on.

5) Line 566 – "new frontier in the cognitive modeling of memory." They should qualify this statement with discussion of the shortcomings of these types of models. This model is useful for illustrating the potential functional utility of controlling the timing of episodic memory encoding and retrieval. However, the neural mechanisms for this control of gating is not made clear in these types of models. The authors suggest a portion of a potential mechanism when they mention the potential influence of the pattern of activity in the decision layer on the episodic memory gating (i.e., depending on the level of certainty – line 325), but they should mention that detailed neural circuit mechanisms are not made clear by this type of continuous firing rate model trained by gradient descent. More discussion of the difficulties of relating these types of neural network models to real biological networks is warranted. This is touched upon in lines 713-728, but the shortcomings of the current model in addressing biological mechanisms are not sufficiently highlighted. In particular, more biologically detailed models have addressed how network dynamics could regulate the levels of acetylcholine to shift dynamics between encoding and retrieval (Hasselmo et al., 1995; Hasselmo and Wyble, 1997). There should be more discussion of this prior work.

6) Figure 1 – "the cortical part of the model" – Line 117 – "cortical weights" and many other references to cortex. The hippocampus is a cortical structure (allocortex), so it is very confusing to see references to cortex used in contrast to hippocampus. The confusing use of references to cortex could be corrected by changing all the uses of "cortex" or "cortical" in this paper to "neocortex" or "neocortical."

7) "the encoding policy is not learned" – This came as a surprise in the discussion, so it indicates that this is not made sufficiently clear earlier in the text. This statement should be made in a couple of points earlier where the encoding policy is discussed.
