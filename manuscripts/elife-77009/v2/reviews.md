# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77009.sa0](https://doi.org/10.7554/eLife.77009.sa0)

This manuscript puts forward a new idea that topography in neural networks helps to remove noise from inputs. The authors show that there is a critical level of topography that is needed for network to denoise inputs.


---

# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77009.sa1](https://doi.org/10.7554/eLife.77009.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Signal denoising through topographic modularity of neural circuits" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

To increase the impact of this work, it is necessary to

1) Clarify the properties of the critical point (see comments from Reviewer 1).

2) Consider how denoising could work for dynamic inputs (comments raised by both Reviewers).

Reviewer #1 (Recommendations for the authors):

As I have stated in the main review section, my main issue with this work is that I fail to see the impact of the results. The authors provide a detailed analysis of a model for cortical connectivity with topographical connections. On the one side, they do not compare their analysis to neuronal recording or imaging, thus not providing evidence that their analysis of the dynamics is correct and justifies the model. On the other hand, the model does not offer deep theoretical insights and focuses on simplistic computational tasks, denoising, which could be achieved in different ways.

In the following, I give some recommendations to the authors on making the work more meaningful and robust, in my opinion. First, I will address the bigger question of what could be done to increase the impact of the work. Then, I will address some technical issues and lack of coherence.

– I would have liked to see a theoretical derivation of the critical modularity level. For example, the authors can attempt to derive bifurcation curves in Figure 7 and show how they depend on different parameters in the system. The authors show that the single neuron dynamics do not affect the result but other connectivity parameters (e.g., the mean and variance of the different weight matrices). If the authors think that m=0.83 is a universal critical value, they should argue for it.

– One possible way to better understand the dynamics in the network and the role of the recurrent connectivity is to extend the mean-field analysis to the fluctuations around the fixed points of each population. For example, one concern is that while the mean activity would be low in inactive channels, noise fluctuations could still propagate.

– Can the results be compared to a more simplified feedforward network with topographic connectivity? Is the recurrent connectivity needed to explain and interpret the result? Is the inhibitory network required, or can similar effects be achieved with a subcritical excitatory recurrent population in each layer?

Reviewer #2 (Recommendations for the authors):

The manuscript presents an interesting and novel idea. My main suggestions for improvement pertain to the clarity of the presentation. In many cases the results are presented out-of-order and it is difficult to understand the authors point until reading the next paragraph.

For example, the critical value is mentioned in the first paragraph on page 4, but at that point it is not explained that there is a transition. On page 5, the discussion of Figure 2 returns back to Figure 1. It might be better to re-order the panels within figures to ensure continuous sequential description.

An important typo in Figure 2 legend "For" should be "Four".
