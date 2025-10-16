# Peer review - Round 1

Editors:
- Rohit V Pappu, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81907.sa0](https://doi.org/10.7554/eLife.81907.sa0)

In this work, the authors introduce an adaptive single-molecule tracking approach for following molecules within biomolecular condensates. Consistent with the emerging idea that condensates are not simple, purely viscous, Newtonian fluids, the authors find that the motions of molecules reveal intrinsic inhomogeneities switching between trapped and more mobile states that suggest the existence of at least two – possibly more – states within condensates. The data appear to be consistent with the formation of percolated networks within condensates – a finding that is likely to be general to other systems.


---

# Peer review - Round 1

Editors:
- Rohit V Pappu, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81907.sa1](https://doi.org/10.7554/eLife.81907.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Biological condensates form percolated networks with molecular motion properties distinctly different from dilute solutions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers agree that the observations provide potentially important new information, but three specific concerns have been raised.

1) Is the parsing into weak, non-specific interactions driven by IDRs and strong, specific interactions driven by folded domains real or a trope? The authors propose that this is their belief. However, the specificity of interactions within IDRs, including the FUS system has been well established via the stickers and spacers framework. Conformational heterogeneity engenders conformational and hence concentration fluctuations. These effects are neither weak nor non-specific. This view is shared by the editor and reviewer 1. Therefore, instead of the artificial partitioning and the unsubstantiated claim that the network is small, it is better to update this perspective based on numerous recent contributions. Please see https://doi.org/10.1038/s41557-021-00840-w, and https://www.biorxiv.org/content/10.1101/2022.05.21.492916v2 as examples. The key point is that the canonical expectation is of shear thinning behavior in viscoelastic materials that have terminal viscous behaviors. Therefore, the issue is not about weak non-specific vs. strong, specific interactions, but more about the modes of motions accessible to folded domains vs. IDRs. Motions of the latter have been discussed extensively by the Schuler, Best, and Blackledge groups, and these motions span a spectrum of timescales and length scales, which explains the observations reported here, as opposed to the binary classification offered up by the authors and in the biochemical literature.

2) Reviewer 1 raises important issues regarding the simplicity of the 2-state model and the apparent cyclic nature of the parameterization, fitting, and analyses. Please respond constructively and completely to all the points raised by reviewer 1. A specific question that comes to mind from the comments of reviewer 1 is why won't a single stretched exponential with at least one less parameter than currently used provide an equivalent description of the data? One can imagine this will be true. And if so, how does something like a Kohlrausch-Williams-Watts function compare to the current approach?

3) Reviewer 2) raises several important points about the imposition of diffusive motions on the analysis. What are the criteria used to adjudicate in favor of diffusion and hence two diffusive processes? Further, the review notes that there are numerous accounts of caging that are described in the physical literature that is highly relevant in the current context.

Reviewer #1 (Recommendations for the authors):

1. Overall, the manuscript should review the relevant literature in the Introduction (at least to some extent) and evaluate the novelty of its own method based on this review. Some specific points are discussed below:

(p. 3) We need references for the sentence "The existing biochemistry and biophysics theories that have been guiding our understandings of molecular behaviours and their interactions in living cells in the past are mainly developed for molecules in dilute solutions." Indeed, there are very few references in the Introduction, which I don't think is appropriate.

(p. 3-4) There are several works trying to quantify the properties of condensates. For example, see 10.1016/j.bpj.2019.08.030 and 10.1038/s41467-020-19476-4; see also a recent review 10.1021/acs.chemrev.1c00774.

(p. 3-4) Also, there have been attempts to use super-resolution microscopy to track individual proteins (especially in vivo). I think that they should be introduced and appreciated. For example, see 10.1126/science.aar4199 and 10.1016/j.molcel.2020.06.034.

2. (p. 6) The authors assume that the phase boundaries are unchanging throughout their measurement. Is it justifiable?

3. (p. 6) They claim to estimate the diffusion coefficients of NR2B. Can they provide the values?

4. The two-state model, assuming trapped and mobile states of molecular diffusion, is a simple and powerful model, but I don't think it necessarily reflects real physics. In my opinion, it is equally likely that the molecules have three or four possible states, or even a continuum of mobility, as the distributions (Figure 3) do not show any "distinct" peaks. Can the authors comment on this?

5. Figure 3A1 and 3B: the authors conclude that a simple diffusion model is a "bad" fit for Figure 3A1 while it explains Figure 3B well – but are they really different? R2 is even better for Figure 3A1 (0.97 vs. 0.91).

6. In their model, they use the "switching probabilities," which in my opinion is not necessary. In a dynamic equilibrium (as in the plateaus of Figure 3C and 3D), the system should be in a quasi-static state, where we can simply assume two diffusion behaviors even without considering their exchange. Can we simply use a linear combination of two simple diffusion distributions to fit the data?

7. I am also curious about the performance of the HMM. How much does it improve the fitting? Can the authors provide the fitting results?

8. (p. 8) The authors claim that the diffusion coefficient of NR2B in a mobile state in the condensed phase and that of NR2B in the dilute phase are "very close," but the reported values are ~0.47 μm2/s and ~0.61 μm2/s. The authors should clarify in what sense they are very close to each other.

9. (p. 8) The authors mention that they did not observe any obvious hinderance against motions when molecules cross the phase boundaries (and hence assume that the flux is simply the diffusion coefficient multiplied by molecular density), but there are reports on the diffusion barrier at the boundaries (see 10.1038/nature22989 and 10.3390/ncrna5040050). In my opinion, the barrier makes sense, as the surface tension will break the symmetry between one side and the other side of the boundary. Can the authors comment on this?

10. (p. 9) The theoretical value for the enrichment fold is 62.8 and its experimental value is ~61, which may look astonishing, but the "theoretical" value is not calculated from scratch. It is based on the parameters that fit the data, so I think it is unsurprising that they obtain very similar values. I would be surprised if there was a big discrepancy.

11. (p. 9) Again, they report the "remarkable" similarity between the diffusion coefficient for the mobile fraction in the condensed phase and that in the dilute phase, but I think the difference (0.17 vs 0.47 μm2/s) can be considered significant, depending on your perspective.

12. The authors conducted a Monte Carlo simulation to obtain the simulated enrichment fold. Is it just for validation of the analytical formula? (If this is the case, I don't think it is necessary to include the simulation results.) Can we obtain any other useful information from the simulation?

13. In Figure 4A and the corresponding text, the authors seem to claim that "weak" interactions will lead to "small" networks, but I think that this statement can be misleading. It may be true that molecules are involved in small networks at a certain time point, but the interactions are transient and dynamic (as the authors mention), so molecules change their partners rapidly and on average, the molecules are involved in a large (if not system-spanning) network. Hence, the "size" of the network should be discussed with care, and I recommend the authors revise the manuscript accordingly.

14. (p. 11) The authors say that the fraction of dwell time is "directly proportional" to the binding affinity and avidity, which I don't think is a mathematically precise statement. Did they mean "directly dependent on the two factors"?

15. If I understand correctly, the FUS experiment was conducted in 3D, unlike the NR2B experiment, where the molecules are attached to the membrane. As the system becomes three-dimensional, the "displacement" is now a 2D-projected value, and we need to devise a way to convert it to a 3D value. Do the authors consider this point? If so, please provide a description of their conversion method.

16. (p. 12) The authors say that phase separation of FUS PrLD took up to 12 hours to occur but do not show any data. Please include the data (microscope images or turbidity data).

17. (p. 15) Can the authors comment on why they have greater error bars for simulated FRAP curves in Figure 5G? Is it because they have a smaller number of measurements (3 vs. 10)?

Reviewer #2 (Recommendations for the authors):

The central finding that the molecules tend to experience transiently confined states in the condensed phase is remarkable and important. This finding is reminiscent of transient "caging"/"trapping" dynamics observed in diverse other crowded and confined systems e.g., https://doi.org/10.1103%2FPhysRevLett.107.178103, https://doi.org/10.1038/s41467-019-10115-1, https://doi.org/10.1103%2FPhysRevLett.89.095704, https://doi.org/10.1103%2FPhysRevLett.92.178101, https://doi.org/10.1529%2Fbiophysj.106.092619, https://doi.org/10.1016%2Fj.bpj.2013.12.013. The authors may wish to comment on these conceptual connections to other systems that highlight the broader context of this fascinating finding; it might motivate others to bring theoretical and analytical approaches developed to understand these other systems to bear on condensates, which would be valuable to the field.

Related to the previous point: it would be interesting to see not just the distribution of displacements, but also the distribution of times spent in the confined state and mobile state. Given the experimental results, the authors likely already have these data. The functional form of this distribution is known to reflect the physics underlying the trapping behavior and transitions between the two states (see e.g., https://doi.org/10.1016/0370-1573(90)90099-N).

Also related to the previous point: it is very surprising to see the authors interpret the single-molecule motion as being 'normal' diffusion (within the context of a two-state diffusion model), instead of analyzing their data within the context of continuous time random walks or anomalous diffusion, which is generally known to arise from transient trapping in crowded/confined systems (again see e.g., https://doi.org/10.1103%2FPhysRevLett.107.178103, https://doi.org/10.1038/s41467-019-10115-1, https://doi.org/10.1103%2FPhysRevLett.89.095704, https://doi.org/10.1103%2FPhysRevLett.92.178101, https://doi.org/10.1529%2Fbiophysj.106.092619, https://doi.org/10.1016%2Fj.bpj.2013.12.013). It is not clear that interpreting the results within the context of simple diffusion is appropriate, given their general finding of the two confined and mobile states. Such a process of transient trapping/confinement is known to lead to transient subdiffusion at short times and then diffusive behavior at sufficiently long times. There is a hint of this in the inset to Figure 3, but these data need to be shown on log-log axes to be clearly interpreted. I encourage the authors to think more carefully and critically about the nature of the diffusive model to be used to interpret their results.
