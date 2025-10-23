# Peer review - Round 1

Editors:
- C Brandon Ogbunugafor, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79665.sa0](https://doi.org/10.7554/eLife.79665.sa0)

The study offers a valuable contribution to the field. While the fields of artificial life and experimental evolution in microbes have been connected for many years, there have been few studies to meaningfully demonstrate how work in evolutionary computation can meaningfully inform the design and execution of microbial experiments. This study represents a truly innovative approach and may fuel further studies at the intersection between computational evolution and experimental evolution.


---

# Peer review - Round 1

Editors:
- C Brandon Ogbunugafor, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79665.sa1](https://doi.org/10.7554/eLife.79665.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Artificial selection methods from evolutionary computing show promise for directed evolution of microbes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Landry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Juan Diaz-Colunga (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please address the issues raised by reviewers 1 and 2, as they can substantially improve the manuscript. In general, the paper could benefit from more clarity in certain aspects.

Reviewer #1 (Recommendations for the authors):

Overall, very nice work. I have a few minor suggestions to improve the paper, as follows:

1) Please specify whether the tournament selection was with or without replacement. Additionally, please justify why you selected tournaments of size 4 (preliminary testing? Heuristic? Arbitrary?)

2) You mentioned that you chose 55,000 generations based on "the number of digital organism generations that elapsed in our directed evolution experiments". I'm confused by what you mean by this. What was the termination criterion in the directed evolution experiments that resulted in 55,000 generations? Later, you say "2,000 generations (the number of cycles in our directed evolution experiments)"; how does the 2,000 generations relate to the 55,000 generations? Please clarify. Also, since you say "digital organisms" I assume you mean in the simulated directed evolution experiments, but please insert the word "simulated" to make this clear.

3) It would be nice to have at least one graph that either summarizes or exemplifies the relative speed of evolution for the various selection methods, and some discussion of this.

4) I suspect that the relatively poor performance of NDE may be due to the large number of objectives, leading to very low selection pressure (because so many solutions are non-dominated). This is also consistent with your observation that NDE selected the most populations on average. I think some discussion of this is warranted.

Reviewer #2 (Recommendations for the authors):

1) Regarding my main concern on the potential presence of an unacknowledged selective pressure favoring populations of generalists, I suggest the authors study the effect of varying (or removing) the bottleneck applied when selected populations are transferred to the offspring metapopulation. In fact, I am not sure I understand why this bottleneck was even introduced in the first place. In laboratory experiments, it is common to apply these bottlenecks in serial batch culture experiments. However, the setting in this work is more similar to a turbidostat where newborn individuals replace existing ones, and thus I do not see why the parent populations could not be propagated into the offspring "as is". It would be helpful to see if a less harsh population bottleneck (or none at all) at the time of propagation would palliate the low diversity of task profiles in the three less effective protocols --- and maybe improve their performance.

2) Along the same lines, I have an additional suggestion: when the selected parent populations are propagated into the next meta-generation, repeats are allowed. Thus, two or more offspring populations from a same parent could potentially be very similar to one another (an issue that could be aggravated as more meta-generations pass). In other words, this could make it so variation is quickly exhausted as the experiment progresses. In fact, this has been observed in artificial selection experiments on microbial communities [Chang et al., Evolution 2020]. It has been suggested that perturbing the populations (for instance through the inoculation of invader species into the selected populations at the time of propagation) could replenish variation upon which selection could further act [Chang et al., Nature Ecology and Evolution 2021; Sánchez et al., Annual Review of Biophysics 2021]. For the purposes of this work, this loss of variation can simply be seen as an intrinsic limitation of the elite, top-10% and tournament treatments. But I am curious to see whether actively replenishing variation before each meta-generation could palliate the loss of diversity and improve performance. This is NOT required to support the findings of the paper as it stands, but it might serve to establish causal links between the success of a selection scheme and its ability to maintain variation in task profiles, further strengthening the results.

3) Regarding the accessibility of the paper to a broad audience: as a non-expert in evolutionary computing, some aspects of the simulations were difficult for me to follow. I think it will not be easy for readers outside of the field of evolutionary computing to build an intuition regarding how the authors' digital evolution framework could be mapped to an evolutionary process of a microbial population in a laboratory setting. I think a way to address this could be to update Figure 1 and section 3, which currently does not read well in prose. It would be very useful to expand panels b) and c) in Figure 1, which are currently a bit generic, to give the reader a better sense of what it means for the population to mature (what happens during the life span of an organism? where do inputs come from? etc.), what kind of properties of the population are assessed at the evaluation stage, and how. This should also serve to establish a clearer analogy with microbial evolutionary processes and make the manuscript more accessible to a broader audience. For the same reason, I think that describing the considered selection schemes the first time they are mentioned would be useful for non-expert readers. Currently they are described in dedicated sections, but I think that introducing them at least minimally when they are first brough up would be helpful.
