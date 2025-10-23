# Author response - Round 1

Authors:
- Daine R Lesniak
- Kara L Marshall
- Scott A Wellnitz
- Blair A Jenkins
- Yoshichika Baba
- Matthew N Rasband
- Gregory J Gerling
- Ellen A Lumpkin

## Response text

DOI: [10.7554/eLife.01488.014](https://doi.org/10.7554/eLife.01488.014)

1) […] There is a high probability, therefore, that the single fibers recorded by the authors innervated multiple touch domes, and thus the electrophysiological records that are pivotal to the validation of their model, likely represent the combined output from multiple touch domes stimulated simultaneously.

The reviewers noted that some SAI afferents innervate multiple touch domes and that the 3-mm probe tip used to gather the electrophysiology data in this study is large enough to stimulate multiple touch domes simultaneously. To address this issue, before applying controlled indentations using the 3-mm probe tip, we manually probed the skin surface with a mechanical stimulator whose tip was smaller than an individual touch dome (100 µm) to specifically test how many touch domes were innervated by the recorded SAI afferent. For computational modeling, we only included fibers that responded to stimulation of a single touch dome. Thus, we are certain that only the Merkel cells in that touch dome could be contacted by the afferent. We thank the reviewers for noting this oversight in the text and we have clarified our procedure accordingly.

Based on published data from cats and neonatal mice, the reviewers raised the concern that most SAI afferents innervate multiple touch domes. To directly address this concern, we analyzed a larger dataset of SAI afferent recordings from adult mouse hindlimb, which is the recording site used in this study. In the mouse strain used here (Atoh1/nGFP transgenic mice on a BDF1 strain background), we found that the majority of SAI afferents innervate a single touch dome (70%; N=27 SAI afferents). We feel that this analysis is a valuable addition to the literature and have included the results in the revised submission.

2) Related to point #1, because of collision/antidromic “resetting” at branch points on the parent axon, the dome that produces the first action potentials to arrive at the branch will dominate the recordings (as shown by Lindblom and Tapper in 1969; Integration of impulse activity in a peripheral sensory unit. Expl Neurol. 15, 63-69). Thus, if two or more domes are activated simultaneously, the spikes recorded more proximally along the parent axon will generally represent the output from one dome only. However, which dome dominates the response is unclear when multiple domes are stimulated simultaneously. If both domes are stimulated simultaneously, you generally get one or the other pattern, and which pattern you get depends on which dome is closer to the branch point (or conducts fastest to reach the branch point first). This effect makes it difficult to connect the anatomical reconstructions with the physiology if one doesn't know which dome provided the output they recorded. The authors should comment on this issue.

We agree that an SAI afferent with more than one receptive field will have interesting firing properties that will differ depending on the receptive field stimulated. These possibilities are not addressed in the present manuscript because, as mentioned above, the electrophysiology data presented here are from SAI afferents that only innervate individual touch domes. Thus, we sought to define the fundamental firing properties set by structural components of a single receptive field. The implications of having multiple punctate receptive fields, as described by Lindblom and Tapper, are now discussed.

3) The driver effect predicts that specific stimulation of partial receptive field innervated by a dominant branch should generate similar responses as those evoked by whole receptive field stimulation. Does the model conform to this prediction?

Our model recapitulates the driver effect because it incorporates resetting of all spike initiation zones in the arbor when an action potential fires from one branch. This is a key component of the driver effect because it suppresses firing from the other branches, which gives a bias to the spike initiation zone that fires first. Although noise in transduction models introduces an element of stochasticity, the branch with the most transduction units has the highest likelihood of reaching spike threshold first.

Given this architecture, the reviewers’ prediction should be upheld by the computational model if one could deliver the same state of stress to just the driver branch as is delivered to the entire touch dome. We cannot confirm this quantitatively with our present models, which are built to simulate flat-field rather than punctate stimuli. During these skin-nerve electrophysiological recordings, we use a 3-mm diameter, filleted stimulus probe to deliver a consistent state of stress to the entire receptive field. This helps accommodate for small but inevitable imprecision in stimulus placement and avoids the uncontrolled stress gradients that would occur with a spherical stimulus. To computationally represent this flat-field stimulus, we have modeled the skin with elements that have edge lengths of 100 µm. This makes it impossible to apply stress to only the driver branch because it would occur on a sub-element scale. To model a punctate stimulus across different branches will require building, validating and experimentally constraining new finite element models with a finer discretized mesh. Future studies will address this fascinating question.

According to the data and models, travel times along branches to the node are much shorter than that of antidromic resetting. It would be interesting to examine whether the initial firings, which should not be affected by the resetting mechanism, from SAI afferents with more Merkel endings are always stronger than those from afferents with fewer Merkel endings no matter how Merkel endings are distributed among different heminodes. This information can be obtained by re-examining existing recording data and the simulations.

We agree that this is an interesting analysis. We re-analyzed our SAI afferent recording data to test for a relationship between the latency of first spikes, which will not be impacted by zone resetting, and the total number of Merkel cells. We focused on suprathreshold stimulus magnitudes that reliably elicited sustained firing.

Although we directly measured the number of Merkel cells in each touch dome for recorded SAI afferents, our reconstructions suggest that up to 15% are not contacted by the afferent (see Figure 1I). To account for this, we grouped small touch domes (12 and 13 Merkel cells) and large touch domes (20 and 22 Merkel cells) to represent our level of resolution. Consistent with the reviewers’ prediction, first spike latencies were significantly shorter in the large touch dome group (mean±SEM, N; for large touch domes: 10.9±1.6 ms, N=57; for small touch domes: 40.0±14.5 ms, N=60; P=0.027; Student’s unpaired t test, one-tailed). We also noted that the variability of first spike latencies was significantly higher in the small touch dome group (P<0.0001), which suggests that touch domes with fewer transduction units fire less reliably during dynamic stimuli.
