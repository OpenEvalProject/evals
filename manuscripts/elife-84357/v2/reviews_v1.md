# Peer review - Round 1

Editors:
- Lila Davachi, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84357.sa0](https://doi.org/10.7554/eLife.84357.sa0)

This article contributes to our section on research advances which offers important follow-up information about previously published articles in eLife. This advance offers a valuable integration of work across species that contribute to an ongoing debate about the precise role of medial temporal lobe structures in processes supporting perception as well as memory. The work presented herein uses a model of the ventral visual stream to harmonize predictions across species and leads to compelling evidence for more principled predictions about when and how one might expect contributions to performance. Using this approach has allowed the authors to revise the conclusions of previous work and will likely contribute significantly to future work in this area.


---

# Peer review - Round 1

Editors:
- Lila Davachi, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84357.sa1](https://doi.org/10.7554/eLife.84357.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your Research Advance "Inconsistencies between human and macaque lesion data can be resolved with a stimulus-computable model of the ventral visual stream" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jonathan Winawer (Reviewer #2).

Reviewer #1 (Recommendations for the authors):

This article describes the application of a computational model, previously published in 2021 in Neuron, to an empirical dataset from monkeys, previously published in 2018 in eLife. The 2021 modeling paper argued that the model can be used to determine whether a particular task depends on the perirhinal cortex as opposed to being soluble using ventral visual stream structures alone. The 2018 empirical paper used a series of visual discrimination tasks in monkeys that were designed to contain high levels of 'feature ambiguity' (in which the stimuli that must be discriminated share a large proportion of overlapping features), and yet animals with rhinal cortex lesions were unimpaired, leading the authors to conclude that perirhinal cortex is not involved in the visual perception of objects. The present article revisits and revises that conclusion: when the 2018 tasks are run through the 2021 computational model, the model suggests that they should not depend on perirhinal cortex function after all, because the model of VVS function achieves the same levels of performance as both controls and PRC-lesioned animals from the 2018 paper. This leads the authors of the present study to conclude that the 2018 data are simply "non-diagnostic" in terms of the involvement of the perirhinal cortex in object perception.

The authors have successfully applied the computational tool from 2021 to empirical data, in exactly the way the tool was designed to be used. To the extent that the model can be accepted as a veridical proxy for primate VVS function, its conclusions can be trusted and this study provides a useful piece of information in the interpretation of often contradictory literature. However, I found the contribution to be rather modest. The results of this computational study pertain to only a single empirical study from the literature on perirhinal function (Eldridge et al, 2018). Thus, it cannot be argued that by reinterpreting this study, the current contribution resolves all controversy or even most of the controversy in the foregoing literature. The Bonnen et al. 2021 paper provided a potentially useful computational tool for evaluating the empirical literature, but using that tool to evaluate (and ultimately rule out as non-diagnostic) a single study does not seem to warrant an entire manuscript: I would expect to see a reevaluation of a much larger sample of data in order to make a significant contribution to the literature, above and beyond the paper already published in 2021. In addition, the manuscript in its current form leaves the motivations for some analyses under-specified and the methods occasionally obscure.

– The manuscript does not make a compelling argument as to why Eldridge et al. (2018) is a particularly important example of the prior literature whose reevaluation will change the interpretation of the literature as a whole.

– Considerable effort is expended on evaluating how well the model can "approximate more granular subject behaviors" but it is not explained why this is important, or whether it matters that the model cannot, in fact, approximate image-level subject behavior.

– The section "determining model performance" does not provide sufficient detail for a reader to reproduce the modeling work. The statement that "we estimate the optimal regularization strength for the logistic regression model" appears to be the only statement detailing how the model is trained. This is too sparse and opaque and needs expanding considerably.

– The section "8.2 Consistency estimates" and the caption to Figure S4 both refer to the procedure for estimating the correspondence between subject-subject or subject-model choice behaviors. But these two sections appear to contradict each other. The figure caption says that the authors generate a random split of each subject's data. But in Section 8.2, the last sentence implies (although it's not completely clear) that for the between-subjects metric, all the data from each subject is used. (And it is true that, for a between-subjects analysis, you could use all the data to compute a correlation). Please clarify exactly how the 'split' was generated and whether a split was used for all analyses including between subjects.

Reviewer #2 (Recommendations for the authors):

The goal of this paper is to use a model-based approach, developed by one of the authors and colleagues in 2021, to critically re-evaluate the claims made in a prior paper from 2018, written by the other author of this paper (and colleagues), concerning the role of perirhinal cortex in visual perception. The prior paper compared monkeys with and without lesions to the perirhinal cortex and found that their performance was indistinguishable on a difficult perceptual task (categorizing dog-cat morphs as dogs or cats). Because the performance was the same, the conclusion was that the perirhinal cortex is not needed for this task, and probably not needed for perception in general, since this task was chosen specifically to be a task that the perirhinal cortex *might* be important for. Well, the current work argues that in fact the task and stimuli were poorly chosen since the task can be accomplished by a model of the ventral visual cortex. More generally, the authors start with the logic that the perirhinal cortex gets input from the ventral visual processing stream and that if a task can be performed by the ventral visual processing stream alone, then the perirhinal cortex will add no benefit to that task. Hence to determine whether the perirhinal cortex plays a role in perception, one needs a task (and stimulus set) that cannot be done by the ventral visual cortex alone (or cannot be done at the level of monkeys or humans).

There are two important questions the authors then address. First, can their model of the ventral visual cortex perform as well as macaques (with no lesion) on this task? The answer is yes, based on the analysis of this paper. The second question is, are there any tasks that humans or monkeys can perform better than their ventral visual model? If not, then maybe the ventral visual model (and biological ventral visual processing stream) is sufficient for all recognition. The answer here too is yes, there are some tasks humans can perform better than the model. These then would be good tasks to test with a lesion approach to the perirhinal cortex. It is worth noting, though, that none of the analyses showing that humans can outperform the ventral visual model are included in this paper - the papers which showed this are cited but not discussed in detail.

Major strength:

The computational and conceptual frameworks are very valuable. The authors make a compelling case that when patients (or animals) with perirhinal lesions perform equally to those without lesions, the interpretation is ambiguous: it could be that the perirhinal cortex doesn't matter for perception in general, or it could be that it doesn't matter for this stimulus set. They now have a way to distinguish these two possibilities, at least insofar as one trusts their ventral visual model (a standard convolutional neural network). While of course, the model cannot be perfectly accurate, it is nonetheless helpful to have a concrete tool to make a first-pass reasonable guess at how to disambiguate results. Here, the authors offer a potential way forward by trying to identify the kinds of stimuli that will vs won't rely on processing beyond the ventral visual stream. The re-interpretation of the 2018 paper is pretty compelling.

Major weakness:

It is not clear that an off-the-shelf convolution neural network really is a great model of the ventral visual stream. Among other things, it lacks eccentricity-dependent scaling. It also lacks recurrence (as far as I could tell). To the authors' credit, they show detailed analysis on an image-by-image basis showing that in fine detail the model is not a good approximation of monkey choice behavior. This imposes limits on how much trust one should put in model performance as a predictor of whether the ventral visual cortex is sufficient to do a task or not. For example, suppose the authors had found that their model did more poorly than the monkeys (lesioned or not lesioned). According to their own logic, they would have, it seems, been led to the interpretation that some area outside of the ventral visual cortex (but not the perirhinal cortex) contributes to perception, when in fact it could have simply been that their model missed important aspects of ventral visual processing. That didn't happen in this paper, but it is a possible limitation of the method if one wanted to generalize it. There is work suggesting that recurrence in neural networks is essential for capturing the pattern of human behavior on some difficult perceptual judgments (e.g., Kietzmann et al 2019, PNAS). In other words, if the ventral model does not match human (or macaque) performance on some recognition task, it does not imply that an area outside the ventral stream is needed - it could just be that a better ventral model (eg with recurrence, or some other property not included in the model) is needed. This weakness pertains to the generalizability of the approach, not to the specific claims made in this paper, which appear sound.

A second issue is that the title of the paper, "Inconsistencies between human and macaque lesion data can be resolved with a stimulus-computable model of the ventral visual stream" does not seem to be supported by the paper. The paper challenges a conclusion about macaque lesion data. What inconsistency is reconciled, and how?
