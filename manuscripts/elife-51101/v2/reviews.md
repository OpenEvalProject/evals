# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- Valerij Kiselev, Freiburg University Germany

## Review text

DOI: [10.7554/eLife.51101.sa1](https://doi.org/10.7554/eLife.51101.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work demonstrates the ability of diffusion magnetic resonance to detect and measure permeability of membrane structures smaller than the cell. The development of the method to non-invasively measure water diffusion and exchange in sub-cellular structures makes may enable imaging of normal changes in organelle structure and permeability within living tissue for basic biology and medicine.

Decision letter after peer review:

Thank you for submitting your article "Magnetic resonance measurements of cellular and sub-cellular membrane structures in live and fixed neural tissue" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Valerij Kiselev (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present a novel technology and experimental setup to measure water molecules restricted diffusion in the range 200-1400 nm attributed to small cellular organelles. The authors designed record-breaking experiments in which they have reached a previously unavailable range of measurement parameters. This paper is a nice contribution with potential new understanding on the biological sources of diffusion MRI signal. It confirms the previous work by Leuze et al. (Neuroimage 2017) suggesting the source for diffusion anisotropy (and restricted diffusion) is the membrane and lipids in the tissue. However, the statements such as "Low-field single-sided Magnetic Resonance diffusion methods detect and measure permeability of sub-micron compartments which are likely organelles and cellular vesicles within ex-vivo mouse spinal cords" needs more thorough validation. Moreover, it would be beneficial for the authors to present their results on single diffusion weighting as mainly experimental, open to future theoretical interpretations. Such an approach is common in other scientific disciplines and we believe that NMR is mature enough to adapt this approach, at least when addressing such a complicated problem as diffusion in living tissues.

Essential revisions:

1) Reproducibility: This work is based on an unknown number of samples. In the results the number six (later on becomes five) for fixated samples appears but it is not mentioned anywhere in the Materials and methods. Nine samples are reported somewhere for live tissues but again – not explicitly mentioned in the Material and methods. In the Materials and methods, however, the number n=2 is mentioned for post Triton treatment. I think the samples need to be explicitly mentioned and described in the Materials and methods. If indeed the numbers were 9/6/5/2 – a proper statistical analysis for reproducibility is required to demonstrate the strength of the results.

2) Why did the authors choose postnatal day 4 spinal cord, and not a mature spinal cord? It does not seem to be a trivial choice.

3) Diffusion time is an important factor in conventional DTI with many implications on the measured signal. While the diffusion encoding time (τ) reflects somehow the diffusion time, its interpretation is different from the diffusion time. I think that for a general journal such as eLife – a better description of the jargon is needed to avoid confusion.

4) On the same subject, restricted diffusion is estimated by a diffusion time dependent experiment (as was shown several times by the senior author). How one can estimate restricted diffusion from a diffusion exchange experiment? The notion "restricted diffusion" appears throughout the paper but without an experiment that proved that (at least to my understanding). DEXSY measures exchange of specific water pool – not restricted diffusion. The fact that a certain population of water molecules has a slow diffusion coefficient within an exchange distance of 200-1400nm- does not mean it is restricted (maybe it is just bound with slow motion?). I think this issue needs to be clarified.

5) The authors note that ACSF diffusivity should be a delta function but eventually turned to be a broad distribution because of a regularization procedure that is required by the inversion analysis. While that might be the case, could it also be that this is due to in-homogeneous gradients? Is it possible to control somehow to the effect of the regularization (maybe perform a more conventional analysis?) What is the effect of such regularization on the slow-diffusing components (those who claimed to be arising from organelles)?

6) The 2D DEXSI experiment is the main result of this paper. In Figure 3 the authors note: "The distribution is divided into a 3x3 grid for the possible exchange pathways between components A (3.2×10−4 −1×10−2), B(1×10−2 −3.2×10−1), and C (5.6 × 10−1 − 1 × 101 D/D0), shown by the color coding and labels." – what is the basis of this division? Just to guide the eye? Was some cluster analysis involved in such division?

7) As this is a constant gradient experiment, there is no indication of rotational invariance of the results. I think this is extremely important – especially since the authors claim to reveal restricted diffusion within organelles, which must be separated from the main source of restricted diffusion in neural tissue – the neural fiber. This issue deserves, at least, to be mentioned in the Discussion.

8) Sampling the domain of ultrahigh diffusion weighting using the single diffusion encoding (Figure 2). This is a very interesting part, which is re-iterated in Discussion with the conclusion about the sub-micrometer-sized water confinement. This conclusion is based on a quantitative analysis, which seems to be applied beyond its validity range, which is the main concern about this manuscript.

9) Another concern is about the interpretation of the numerical inverse Laplace transformation, which is an adequate signal description in a very limited range of parameters. Although the authors declare the usage as a representation, "which makes no assumptions about tissue microstructure", they actually rely on the quantitative outcome of this transformation, in particular, for one of the main finding about the 25% of water restricted by membranes.

10) Studying exchange using two diffusion encoding separated by a mixing time. This is the central part of the study, which - in a clever way - decouples from the problem associated with the previous part.

11) Studying the origin of restrictions using the substitution with deuterated water and the tissue delipidation – this part should have a high impact on the further development in the field.
