# Peer review - Round 1

Editors:
- Gianluigi Mongillo, https://ror.org/05f82e368 Université Paris Descartes France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83035.sa0](https://doi.org/10.7554/eLife.83035.sa0)

The study shows that fast and transient modifications of the synaptic efficacies, alone, can support the storage and processing of information over time. Convincing evidence is provided by showing that feed-forward networks, when equipped with such short-term synaptic modulations, perform a wide variety of tasks at a performance level comparable with that of recurrent networks. The results of the study are valuable to both neuroscientists and researchers in machine learning.


---

# Peer review - Round 1

Editors:
- Gianluigi Mongillo, https://ror.org/05f82e368 Université Paris Descartes France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83035.sa1](https://doi.org/10.7554/eLife.83035.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neural Population Dynamics of Computing with Synaptic Modulations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Omri Barak (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The key points consistently raised by all the reviewers in their reports are the following:

1) The main motivation of the study is unclear. Is the study proposing a specific synaptic plasticity mechanism or the goal is to expose the computational advantage(s) of transient, slow-decaying synaptic modulation? In either case, the modeling choices should be motivated more explicitly and, where possible, the link with the existing experimental observations should be made more precise.

2) It is important to test the network's performance on at least one non-integration task.

3) The most biologically-implausible aspects of the synaptic rule, such as the unbounded growth of the amplitude of the synaptic modulations, should be removed. In this context, it would be useful to relate the synaptic plasticity rule to the biology more quantitatively, at least in terms of the underlying time scales and of the required magnitude of the changes in the efficacies.

4) The study should be better contextualized in the existing literature, in order to highlight the elements of novelty in the present approach and in the results.

Reviewer #1 (Recommendations for the authors):

1) The Introductory paragraphs should be reworked to clarify what sort of plasticity mechanisms are being modeled.

2) Short-term plasticity mechanisms are often non-Hebbian, depending only on presynaptic activity. If I am correct that the specific plasticity rule used is understood to be a short-term Hebbian mechanism, for the authors' conclusions is it necessary that the short-term plasticity mechanism be Hebbian, or would more traditional STP mechanisms work?

3) Pg. 4, "where λ and η are parameters learned over training". This adds an element of metaplasticity, in that one typically does not think that such synaptic hyperparameters are optimized during learning a task. Does this make the network less biologically realistic? Is the selection of these during training meant simply as a route to find effective hyperparameters (that apply across tasks) but not necessarily to imply that they are actually learned? And finally, is it even necessary to learn these parameters? The reservoir computing argument in Figure 6 suggests not, though in that case the input weights are not learned either. And if learning these parameters is important for good performance on single tasks then probably not completely accurate to call M unsupervised.

4) I wondered about the robustness of the mechanism by which the MPN performs the task-the readout is based on the variation within the Go cluster and thus seems like it needs to distinguish smaller differences. Does this also make the network more sensitive to noise?

5) Related to the above, the MPN state grows quite dramatically with time ("several orders of magnitude"). Does this growth affect the robustness of the readout and does the mechanism work if the short-term plasticity saturates (and saturation seems reasonable given that synaptic efficacies likely cannot change by several orders of magnitude especially on short timescales)? How important is this large dynamic range to the network capacity?

Reviewer #2 (Recommendations for the authors):

The paper is well-written and the figures are carefully chosen and informative.

As I mentioned in my Public Review, one would like to understand what are the non-obvious limitations (if any) of the general principle, that is, any transient, stimulus-dependent modification of neural/synaptic properties is a memory buffer. For instance, what happens if instead of using Equation (2), you use short-term synaptic plasticity a la Tsodyks-Markram with heterogeneous parameters (e.g., different U, tau_D, and tau_F), and you only learn the synaptic weights (STP parameters are fixed)? It seems to me that this will help clarify some interesting issues, such as, do you really need the synaptic modulation to be associative (i.e., to jointly depend on the pre- and post-synaptic activity)?

Reviewer #3 (Recommendations for the authors):

The paper could be strengthened by tasks that are not integration-based. This could be in the context of RNNs, but then it should be clear what is the added benefit of short-term plasticity.
