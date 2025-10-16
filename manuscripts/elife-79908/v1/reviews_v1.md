# Peer review - Round 1

Editors:
- Blake A Richards, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79908.sa0](https://doi.org/10.7554/eLife.79908.sa0)

The findings of the paper are very valuable for neuroscientists studying the learning of abstract representations. It provides compelling evidence that neural networks trained on two-way classification tasks will develop responses whose category and context selectivity profiles depend on key network details, such as neural activation functions and initial connectivity. These results can explain apparently contradictory results in the experimental literature, and make new experimental predictions for testing in the future.


---

# Peer review - Round 1

Editors:
- Blake A Richards, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79908.sa1](https://doi.org/10.7554/eLife.79908.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Evolution of neural activity in circuits bridging sensory and abstract knowledge" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Guillaume Hennequin (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Justification of some of the model choices that the reviewers asked about and discussion of how much the results depend on them (especially the use of gradient descent).

2) More intuitive explanations for some of the mathematical statements to help make the paper more accessible for the majority of eLife readers.

3) A longer discussion about how this paper fits into the current literature, and how it can be generalised.

Reviewer #1 (Recommendations for the authors):

We do have a couple of concerns which we would recommend adding some discussion about:

1. We found it strange that authors operationalised what are essentially (binary) classification tasks as regression problems; although the network output is pushed through a sigmoidal nonlinearity with a [0--1] range, here this output is never interpreted as a class probability; indeed, instead of maximizing the cross-entropy loss (i.e. maximising the data likelihood) as is normally done in such a context, the authors chose to minimise a squared error loss; this forced them to introduce somewhat arbitrary "target" outputs (0.25 and 0.75) for the two categories. Several questions arise from this odd choice:

a) why did the authors do that? (e.g. is this standard in the NTK literature?)

b) do the results depend on this choice? robustness to this choice is not a priori obvious to us, because the network is not regularised here (see point 2 below), and learning operates in the vastly overparameterised regime where the cross-entropy loss may (does?) not even have a minimum, so weights could diverge. We suspect this may be the answer to (a), but it would be great to discuss this briefly.

2. The paper does not consider generalisation at all, and indeed the tasks studied here are set up in a way that does not even allow thinking about generalisation; the inputs are chosen completely randomly, as opposed to randomly on some category-specific manifold that could be re-sampled, so it is not even clear how a test set would be constructed. Is this an issue? Does that limit the relevance of this study to only a subset of previously studied relevant neuroscience tasks? Again it would be great to discuss.

3. It was not clear to us how much of the results presented here depend on doing gradient descent, as opposed to more generally minimising the loss? This question was apparently already asked as "Comment 2" in the first round of reviews but we found that the rebuttal did not really answer it, beyond saying that solutions are degenerate.

4. After l311, would it be possible to give the intuition for the emergence of context selectivity, in a couple of sentences? The text currently says that it is a "signature of gradient descent" and that the "mechanism is described in detail in Methods 5.6", but we wonder if the authors could be a bit more specific without getting too technical. It is important because the emergence of context selectivity is the most unexpected of the results presented here.

Reviewer #2 (Recommendations for the authors):

– The methods section seems very long to me, maybe too long for a general audience. I would strongly suggest focusing on the details and derivations that are necessary to reproduce the results and to understand the main findings. The rest (as beautiful as it is), I would put in the supplementary material (if eLife allows for it).

– Do you need both u and w to be plastic? Have you tried to keep one set fixed? Is the system underdetermined? You show how the cat or ctx selectivity depends on the ratio of learning rates but I am not completely sure which set of weights is the crucial one or let's say the dominant one that is strictly necessary to get the results.

– I am a bit confused how you implemented the context. The stimulus and the context are linearly combined to yield the total sensory input x. But from the perspective of the network that is not different from the simple task. The network sees an input vector x. Whether x is a vector representing the stimulus alone or the stimulus and a context is indistinguishable to the network. Is the difference here that the stimuli were random and orthogonal and if they are linearly combined with another set that is random and orthogonal, the resulting vectors do not necessarily share the same properties? Maybe I misunderstand something here. Would be great if you could clarify that and maybe highlight the differences in the text.

– Maybe worth discussing in the Discussion (these are merely suggestions, I don't expect the authors to run simulations on that):

– comment on limitations and – if possible – how you envision your results to change (or hold) in E/I networks (that abide by Dale's principle) and/or recurrent connections are included.

– How strongly depend the results (or which results) on the gradient descent you used?

– How would the results generalise to more than 2 categories? And what is with the option „unclassified" (no mapping possible).

– I assume each neuron in x is projecting to all neurons in y. Is this clearly stated somewhere? Maybe I missed it – sorry it is hot today!

– After learning, cat selectivity, and later ctx selectivity, cover a broad range with many neurons being close to zero and some showing positive selectivity. However, most of them are still unselective it seems. Is this range in line with experimental results? Could you comment on this heterogeneity? In line 95/96 you say that the cat selectivity increases for EACH neuron but to me it seems some neurons remain at zero selectivity, do I read the figure wrong?

– The distribution of the cat selectivity between the two tasks is different. The cat selectivity for the context-dependent task has many cells with a selectivity close to zero or even negative. Could you comment on that. I apologise if I overlooked it.
