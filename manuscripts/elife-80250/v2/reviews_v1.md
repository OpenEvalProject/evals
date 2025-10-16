# Peer review - Round 1

Editors:
- Timothy E Behrens, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80250.sa0](https://doi.org/10.7554/eLife.80250.sa0)

The paper by Arribas et al. examines the coding properties of adult-born granule cells in the hippocampus at both the single cell and network level. This paper is of interest to the hippocampal and computational neuroscience fields because it provides a framework for understanding how adult-born granule cells in the hippocampus contribute to network processing. The paper contains interesting ideas, such as the analysis of input-output transformation by spike response models and the establishment of "greedy networks", and the conclusions drawn are supported by the data.


---

# Peer review - Round 1

Editors:
- Timothy E Behrens, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80250.sa1](https://doi.org/10.7554/eLife.80250.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Adult-born granule cells improve stimulus encoding and discrimination in the dentate gyrus" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Christoph Anacker (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

This paper is of potential interest to both the hippocampal and computational neuroscience fields because it provides a framework for understanding how adult-born granule cells in the hippocampus contribute to network processing. It contains novel interesting ideas, such as the analysis of input-output transformation by SRM models and the establishment of "greedy networks". However, the degree of novelty is limited. That the adult-born granule cells have a slower integration time constant is known. Further, not all major conclusions are sufficiently supported by the data. The paper demonstrates that mixed networks show better encoding performance than pure networks, but the differences are small and only visible with specific performance metrics. Intuitive explanations are not provided. The reviewers found the approach intriguing and with new analysis, simulation, and experiment, it can form the basis of a future new submission.

Reviewer #1 (Recommendations for the authors):

As a general comment, there were a few points where I was not sure if an analysis was done using recorded spike trains or simulated spike trains. It would be helpful to clarify these points. For instance, the diagram in Figure 3A makes me think that this analysis is of simulated spike trains, but the caption states "Neurons encode a stimulus in spike trains that can be used to estimate the stimulus that produced them." Some of the comments regarding Figure 4 may reflect my confusion here.

In the Figure 1 discussion on page 5, you say, "this [higher coincidence ratios in older vs younger pairs of GCs] could be a consequence of individual immature GCs producing less reproducible responses." To what extent is this from lower reliability vs. differences in response functions (i.e., differences in the SRM parameters between the groups)? I may have missed it, but it seems you could say more on this point from the analysis in Figure 2.

Figure 4B: missing labels for green and blue curves. I'm a little unsure of how it is that the reconstruction is so good when the spike raster has so few spikes, such as between 250ms and 350 ms. It does appear that 4w cells may fire more in that period than m-cells. Is this part of why including 4w cells is helpful? In other words, the "nontrivial synergy" (p. 11) arises from selecting a group of cells in which at least some of the cells are firing at a given time?

In Figure 4, the results of decoding from pseudo-populations of GCs are shown. Something missing for interpretation here is what the ceiling of ideal performance is. In other words, is an r^2 of slightly more than 0.5 "good"? Supposing you took the parameters from models of GCs, then simulated a pseudopopulation using the SRM, and then used these spikes for the decoding procedure. How well would the model-based decoding work with these simulated spike trains?

The authors find that including the mixed ages in the decoding pool can improve the reconstruction, though somehow the information is not quite as high. I do not understand why this is. Is it because of spike count normalization? Or a subtlety in the information calculation?

Regarding the information calculations:

1. Please include an explanation of how the Gaussian approximation for information calculations was justified, and when it may not be (for instance, due to very low spike counts).

2. In Figure 4G, it'd be useful to know the bits per second or bits per spike, rather than bits.

Also in Figure 4, I'm curious about the composition of the multi-cell groups. What are the typical time constants (k, Figure 2I) or other model parameters of these greedy-optimized cell groups? Does the improvement in performance arise from having a broad sample of time constants, irrespective of whether it's a 4w/5w/m cell? Put another way, is the gap between m-groups and mixed-groups accounted for by drawing one of the ~2 cells in the 4w or in the 5w groups that happen to have much longer k time constants than any of the m-cells?

On Figure 5: (sequence discrimination) I cannot find how long the stimuli used for pattern discrimination are. How does pattern discrimination depend on stimulus length? Also, I missed a point made in the methods regarding the sequence design and rho. I would expect that more correlated stimuli would be less separated, but in "Pattern Discrimination," it says that rho is the correlation between eta_1 and eta_2, and low rho is a low degree of separation (rho = 0.99, low; rho = 0.9997, high).

Another question, which is more for discussion than further analysis, is how this heterogeneity relates to integrating new cells into a network. A week is a relatively short timeframe. Is the picture that some optimal downstream decoder is constantly seeking out these 4-week-old cells to improve decoding?

Reviewer #3 (Recommendations for the authors):

I have only one additional comment on this otherwise excellent study:

The authors find that while immature granule cells are not as reliable in stimulus encoding as mature granule cells, populations containing immature neurons perform better in stimulus reconstruction. The authors discuss the potential benefit of cellular diversity in stimulus reconstruction due to immature neurons potentially encoding different stimulus properties depending on their age. It should also be discussed that in addition to contributing to encoding themselves, the immature neurons may have a modulatory role on the mature granule cells that may improve stimulus reconstruction of the granule cell population when immature neurons are included.
