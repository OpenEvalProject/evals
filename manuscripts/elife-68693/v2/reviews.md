# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68693.sa1](https://doi.org/10.7554/eLife.68693.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Mammalian sperm cells achieve locomotion in a liquid environment by beating their flagellum in wave-like pattern. It is well-known that the resulting forward motion is often accompanied by a rolling motion around the cell's longitudinal axis. However, the function of this rolling motion in the context of navigation is not well understood. The authors combine experiments and simulations to show how rolling aids sperm navigation along surfaces and external fluid flows.

Decision letter after peer review:

Thank you for submitting your article "Rolling controls sperm navigation in response to the dynamic rheological properties of the environment" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The conclusion that rolling is "in response to the dynamic rheological properties of the environment", while compelling, could be better supported. To show that sperm swimming responds to the rheology of the medium, the authors would first need to track the same sperm in media of different rheologies. Second, it is unclear if the sperm is responding to the rheology, or the swimming merely manifests differently in response to the rheology. Third, the data presented for the rheological characterization (Figure S1) do not support the clean delineation between the PVP media being "viscous" and the PAM media being "viscoelastic": the PVP media are 1-2 orders of magnitude less viscous than the PAM, and in both cases, the viscosity appears to sharply rise at low shear rates (although this is likely noise as it also manifests for the TALP). The PVP media appear to show weak shear thinning, similar to the PAM. Furthermore, only the shear viscosity is presented for both solutions; to adequately characterize viscoelasticity, the authors need to show data for e.g. the first normal stress difference vs shear rate, or the elastic and viscous moduli vs oscillation frequency, for example.

2. The writing in general is dense and highly technical; it would be useful to the reader if the authors could provide broader introduction and Discussion sections that clearly discuss the context of the work, the findings, and the implications of the findings.

3. The authors say in lines 98-99 that an increase in viscoelasticity slightly increased the propulsive velocity. I do not see this in the data.

4. In Figure 1F, what do the tildes indicate? And what are the units of the quantities plotted?

5. Lines 162-164: The authors discuss the diffusion coefficient, but I do not see a quantitative description in the actual data. Can they plot e.g. a MSD vs time?

6. Figure 2A-B: What are the units? What is shown in blue? What is the influence of experimental noise (e.g. in the imaging) on these results?

7. Figure 2G: It is unclear what the points vs the lines are.

8. Figure 2H: The authors claim this is a normal distribution, but it does not appear to be so.

9. Experimental uncertainties are improperly reported throughout. E.g. 38.7 +/- 12.2 should be reported as 40 +/- 10, given the uncertainty in the measurement.

10. What is the influence of thermal diffusion in the results throughout?

11. Line 46: The phrase "To avoid errors arising from studying sperm motility under external fluid flow, …" is unclear – which specific potential "errors" do the authors mean?

12. Line 119: It is not obvious how "Thus, rolling causes progressive motion." follows from the preceding sentences.

13. Line 134: period before equation 1 seems unnecessary?

14. Line 135: How exactly is x defined?

15. Line 142: "(24, 29)(24, 29)(24, 29)(24, 29)"?

16. Line 343 -344: the notation is unclear. Does the tilde indicate a time or ensemble average ? Assuming the former, why is the time average of \Pi still time-dependent ? Shouldn't it read "average of \β_s(t)" in line 344?

17. The authors should carefully check and correct the reference list. The listing of doi 's seems inconsistent and several references are incomplete. For example:

a. Line 524: doi necessary?

b. Line 525: reference incomplete.

c. Line 559: reference incomplete.

d. Line 587: reference incomplete.

e. Line 601: page number seems incorrect.

f. Line 605: page number missing?

g. Line 611: page number seems incorrect.

h. Line 611: page number seems incorrect?

18. Bold font on rhs. of equation S44 should be removed, similar in S51, S52.

19. Please check constant use of multiplicative dots in SI (sometimes lower dots and sometimes centered dots are used).

20. Major point: The definition of eta in equation S65-S68 is either incomplete or incorrect.

21. What exactly do the authors mean by Gaussian noise in S66-67?

22. S67 does not look standard Gaussian white noise, which should be δ correlated. Are the eta(t)'s time correlated or simply random numbers of variance D? In the latter case, the stochastic process eta(t) would be discontinuous?

23. Below equation S77 the authors mention "white Gaussian noise" which seems inconsistent with S67.

24. Also, if eta(t) has a Gaussian distribution, then we do not see how S73 can be satisfied, since the tails of a Gaussian distribution extend to infinity – in particular, when using D=1, as stated below equation S77.

25. Which type of stochastic calculus do the authors use to arrive at S74? It looks like Stratonovich but this is not explicitly stated.

26. Based on the above, we are not convinced that equations S65-S77 are correct.

This part of the SI should be carefully revised and corrected as needed, or omitted.Reviewer #2 (Recommendations for the authors):

The authors provide a functional explanation for the observation that mammalian sperm roll around their longitudinal axis: it enables a sperm to continue to move progressively. The authors further sought to provide evidence that rolling responds to the rheological properties of the environment.

The use of imaging to track single sperm and directly observe rolling events is a major strength.

The rheological characterization of the media requires further analysis.

The authors nicely show that rolling enables a sperm to continue to move progressively. However, the conclusion that rolling is "in response to the dynamic rheological properties of the environment", while compelling, is not well supported. The authors tested this hypothesis by studying sperm swimming in a "viscous medium" of TALP + PVP and a "viscoelastic medium" of TALP + PAM, although the rheological characterization of these media does not support this clean delineation.

The observation that sperm rolling has a key functional role broadens understanding of sperm swimming. If the authors could more rigorously support the claim that rolling is modulated in response to the dynamic rheological properties of the environment, then this would broaden understanding of sperm swimming in complex environments during e.g. fertilization.Reviewer #3 (Recommendations for the authors):

The wave-like beating patterns of sperm flagella can vary between cells, with some cells exhibiting more symmetric beat patterns than others. To investigate the dependence of rolling motion on beat asymmetry and rheological properties, the author studied bovine sperm motion in a microfluidic device under simple shear flow and within a quiescent reservoir.

The authors' results suggest that rolling becomes suppressed at relatively lower viscosities/viscoelasticity for sperm exhibiting less symmetric beat patterns, with suppression of rolling more sensitive to viscoelasticity than to viscosity. They found that rolling sperm swim on mostly straight trajectories, whereas non-rolling sperm display 2D planar beat forms resulting in circular trajectories.

Building on previous theoretical work, the authors formulate a minimal 2D-projected model that accounts for rolling through a time-dependent prefactor \Pi(t) in equation 4. They find that this model recapitulates their main experimental observations. In particular, their joint theoretical and experimental analysis suggests that, although the rolling component is not required for sperm rheotaxis, it facilitates rheotactic behavior by minimizing the angle between sperm orientation and externally applied fluid flow, thus maximizing the upstream component of sperm motion.

Overall, I find this comprehensive characterization of sperm rolling interesting and it appears to close an existing gap in the literature.
