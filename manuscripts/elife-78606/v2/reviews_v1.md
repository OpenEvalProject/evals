# Peer review - Round 1

Editors:
- Thomas Serre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78606.sa0](https://doi.org/10.7554/eLife.78606.sa0)

This important study presents a theory of generalization in neural population codes and proposes sample efficiency as a new normative principle. The theory can be used to identify the set of 'easily learnable' stimulus-response mappings from neural data and makes strong behavioral predictions that can be evaluated experimentally. Overall, the new method for elucidating inductive biases of the brain is highly compelling and will be of interest to theoretical and experimental neuroscientists working towards understanding how the cortex works.


---

# Peer review - Round 1

Editors:
- Thomas Serre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78606.sa1](https://doi.org/10.7554/eLife.78606.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Population codes enable learning from few examples by shaping inductive bias" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Fabio Anselmi (Reviewer #1); Jeff Beck (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The consensus among all 3 reviewers is that the manuscript describes an insightful and novel mathematical framework for evaluating the ability of a downstream linear decoder to learn new stimulus-response mappings from relatively few training examples. However, there is also broad consensus among the 3 reviewers that (1) the manuscript is too technical and written in a way that may not be palatable to the eLife readership (to paraphrase one of the reviewers "I don't think that many experimentalists will immediately see the sheer utility of having a tool like this in their arsenal" and that 2) some of the assumptions made are overly simplistic and the theory needs to be extended with more realistic neural assumptions regarding noise, readout and kernels.

Wrt (1), before the manuscript can be accepted for publication, it is necessary that the authors expand on possible applications to neural and behavioral experiments. The authors also need to distill the math better, provide more intuitive explanations, and reduce the jargon. Wrt (2) R2 provided a detailed lists of comments with suggestions for more realistic assumptions.

Reviewer #1 (Recommendations for the authors):

The authors provide a simple and clear way to understand an aspect of the implicit bias of a neural population code linking it with well-known machine learning methods and concepts such as kernel regression, sample complexity and efficiency.

Although the mathematical results the authors employ are not novel, the way they apply them to the problem of neural coding is novel and interesting to a broad audience.

In particular, the computational neuroscience community can benefit from this work being it is one of the few dealing with the impact of the model implicit bias in explaining real data.

Reviewer #2 (Recommendations for the authors):

It is my opinion that the principle utility of this approach lies in its ability to identify the set of 'easily learnable' stimulus-response mappings from neural data which makes strong behavioral predictions that can be easily evaluated. I envision a simple experiment in which empirically obtained kernel functions are used to rank stimulus-response mappings according to their learnability which can then be plotted against measures of performance like the observed learning rate and saturated performance. Because kernel functions are empirically obtained, there is even the potential for meaningful cross-species comparisons. If behaviorally validated, one could also use this approach to label cortical populations by the set of easily learned stimulus-response mappings for that population. This allows for the identification of task-relevant neurons or regions which can be subsequently manipulated to enhance or degrade learning rates.

Of course, any theoretical approach is only as good as the underlying assumptions and so while the primary strength is the simplicity and generality of this approach, the primary weakness is its neglect of some very real and very relevant aspects of neural data in particular and statistical learning in general. In particular, the three principle limitations of this work are tied to its reliance on the assumptions that (1) neurons are noiseless, (2) decoders are linear, and (3) learned weights are unbiased.

(1) Within this framework, a realistic stimulus-dependent noise model can be easily introduced and its effects on the kernel and set of easily learned stimulus-response mappings investigated. So while the kernel would be substantially altered via the addition of a realistic noise model, the applications of the approach outlined above would not be affected. The same cannot be said for the efficient coding application described in this manuscript. There, the authors note that rotations and constant shifts of neural activity do not affect the kernel and thus do not affect the generalization error. This kernel invariance is not present when a non-trivial (i.e. non-isotropic) noise model is added. For example, suppose that neurons are independent and Poisson so that noise scales with the mean of the neural response. In this case, adding a baseline firing rate to a population of unimodal neurons representing orientation necessarily reduces the information content of the population while rotations can affect the fidelity with which certain stimulus values are represented. It is important to note, however, that while this particular efficiency result is not compelling, I believe that it is possible to perform a similar analysis that takes into account realistic noise models and focuses on a broad set of 'biologically plausible' kernels instead of particular invariant ones. For example, one could consider noise covariance structures with differential correlations (Moreno-Bote 2014). Since the magnitude of differential correlations controls the redundancy of the population code this would enable an analysis of the role of redundancy in suppressing (or enhancing) generalization error.

(2) Similarly, the linearity assumption is somewhat restrictive. Global linear decoders of neural activity are known to be highly inefficient and completely fail when decoding orientation in the primary visual cortex in the presence of contrast fluctuations. This is because contrast modulates the amplitude of the neural response and doubling the amplitude means doubling an estimate obtained from a linear decoder even when the underlying orientation has not changed. While the contrast issue could be partially addressed by simply considering normalized neural responses, it is not yet clear how to extend this approach to account for other sources of neural variability and co-variability that cause global linear decoders to fail so badly.

(3) This analysis relies on the assumption that decoder weights learned in the presence of finite data are efficient and unbiased. This assumption is problematic particularly when it comes to inductive bias and generalization error. This is because a standard way to reduce generalization error is to introduce bias into the learned decoder weights through a penalization scheme that privileges decoder weights with small magnitudes. This kind of regularization is particularly important when neurons are noisy. Fortunately, this issue could be addressed by parameterizing changes in the kernel function by the degree and type of regularization potentially leading to a more general result.

Finally, I would like to conclude by explicitly stating that while the limitations imposed by the assumptions listed above temper my enthusiasm in regards to conclusions drawn in this work, I do not believe there is some fundamental problem with the general theoretical framework. Indeed, items 1 and 3 above can be easily addressed through straightforward extensions of the authors approach and I look forward to their implementation. Item 2 is a bit more troublesome, but my intuition tells me that an information-theoretic extension based upon Fisher information may be capable of eliminating all three of these limiting assumptions by exploiting the relationship between FI(\theta) and FI(y=f(\theta)).

Ultimately, all I felt the need to say is in the public part of the review. But I wanted to use this space to insure that it was clear that I feel that this approach has a lot of potential and that I very much hope to see it extended/generalized.

If I were to make any suggestions they would be:

(1) a discussion of the consequences of biologically plausible noise models. I believe that this only requires simply augmenting K by a stimulus dependent noise covariance matrix.

(2) using this addition of a noise model to enable a discussion of the role of redundancy in generalization. This could be accomplished by considering perturbations to the noise covariance matrix that introduce differential correlations (Moreno-Bote 2014) of varying magnitude. More differential correlations means more redundancy and, I suspect, better generalization.

(3) the addition of a paragraph or two outlining some of the other ways that this learnability/generalization measure could be of use to physiologists and behavioral scientists. Training a mouse to do anything more complicated simple orientation detection is challenging to say the least. So having any tool that can be used to identify functions $y=f(\theta)$ that a mouse has a good chance of learning quickly would be highly advantageous. Similarly, by strategically subsampling neurons by tuning properties I suspect it may be possible to identify subpopulations of neurons that are particular important for learning certain functions. This is also cool because it allows physiologists to then target those populations for manipulation.

Of these (3) is probably the most important for this manuscript, because I don't think that many experimentalists will immediately see the sheer utility of having a tool like this in their arsenal.

Reviewer #3 (Recommendations for the authors):

The manuscript presents a theory of generalization performance in deterministic population codes, that applies to the case of small numbers of training examples. The main technical result, as far as I understand, is that generalization performance (the expected classification or regression error) of a population code depends exclusively on the 'kernel', i.e. a measure of the pairwise similarity between population activity patterns corresponding to different inputs. The main conceptual results are that, using this theory, one can understand the inductive biases of the code just from analyzing the kernel, particularly the top eigenfunctions; and that sample-efficient learning (low generalization performance with few samples) depends on whether the task is aligned with the population's inductive bias, that is, whether the target function (i.e. the true map from inputs to outputs) is aligned with the top eigenfunctions of the kernel. For instance, in mouse V1 data, they show that the top eigenfunctions correspond to low frequency functions of visual orientation (i.e. functions that map a broad range of similar orientations to similar output value), and that consistent with the theory, the generalization performance for small sample sizes is better for tasks defined by low frequency target functions. In my opinion, perhaps the most significant finding from a neuroscience perspective, is that the conditions for good generalization at low samples are markedly different from those in the large-sample asymptotic regime studies in Stringer et al. 2018 Nature: rather than a trade-off between high-dimensionality and differentiability proposed by Stringer et al., this manuscript shows that in the low-sample regime such codes can be disadvantageous for small sample sizes, that differentiability is not required, that the top eigenvalues matter more than the tail of the spectrum, and what matters is the alignment between the task and the top eigenfunctions. The authors propose sample-efficient learning/generalization as a new principle of neural coding, replacing or complementing efficient coding.

Overall, in my opinion this is a remarkable manuscript, presenting truly innovative theory with somewhat limited but convincing application to neural data. My main concern is that this is highly technical, dense, and long; the mathematical proofs for the theory are buried in the supplement and require knowledge of disparate techniques from statistical physics. Although some of that material on the theory of generalization is covered in previous publications by the authors, it was not clear to me if that is true for all of the technical results or only some.

Fixed population code, learnable linear readout: the authors acknowledge in the very last sentences of the manuscript that this is a limitation, given that neural tuning curves (the population neural code) are adaptable. I imagine extending the theory to both learnable codes and learnable readouts is hard and I understand it's beyond the scope of this paper. But perhaps the authors could motivate and discuss this choice, not just because of its mathematical convenience but also in relation to actual neural systems: when are these assumptions expected to be a good approximation of the real system?

The analysis of V1 data, showing a bias for low-frequency functions of orientation is convincing. But it could help if the authors provided some considerations on the kind of ethological behavioral context where this is relevant, or at least the design of an experimental behavioral task to probe it. Also related, it would be useful to construct and show a counter-example, a synthetic code for which the high-frequency task is easier.

Line 519, data preprocessing: related to the above, is it possible that binning together the V1 responses to gratings with different orientations (a range of 3.6 deg per bin, if I understood correctly) influences the finding of a low-frequency bias?

I found the study of invariances interesting, where the theory provides a normative prediction for the proportion of simple and complex cells. However, I would suggest the authors attempt to bring this analysis a step closer to the actual data: there are no pure simple and complex cells, usually the classification is based on responses to gratings phases (F1/F0) and real neurons take a continuum of values. Could the theory qualitatively predict that distribution?
