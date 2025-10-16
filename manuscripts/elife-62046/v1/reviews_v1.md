# Peer review - Round 1

Editors:
- Maria Spies, University of Iowa United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62046.sa1](https://doi.org/10.7554/eLife.62046.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Pauszek and colleagues present a number of well executed single-molecule experiments that use E. coli Pol I as a model DNA polymerase to demonstrate domain swapping for its various activities (i.e. DNA synthesis and 5' nuclease). As DNA pol I consists of two main units, one featuring domains for 3' to 5' DNA polymerisation and for 3' to 5' exonuclease activity, and the second containing 5' to 3' nuclease (5' nuc domain), understanding the coordination between these two parts and their three enzymatic activities is of great importance. The most significant results of this study include (1) the observation of reversible swapping between the DNA synthesis domain and 5' nuclease domain during a single encounter with DNA substrate and (2) there are varying positions of the 5' nuclease domain depending on the nature of the DNA substrate (i.e. gap, 5' flap, double flap). Previously, the authors applied similar experimental strategy to Klenow fragment. Comparing the data for KF and the full-length Pol I shows that nuc domain appears to suppress or override pol-exo transitions observed in KF.

Decision letter after peer review:

Thank you for submitting your article "Single-molecule view of coordination in a multi-functional DNA polymerase" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Maria Spies as a Reviewing Editor and José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Harold Kim (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Pauszek and colleagues present a number of well executed single-molecule experiments that use E. coli Pol I as a model DNA polymerase to demonstrate domain swapping for its various activities (i.e. DNA synthesis and 5' nuclease). As DNA pol I consists of two main units, one featuring domains for 3' to 5' DNA polymerisation and for 3' to 5' exonuclease activity, and the second containing 5' to 3' nuclease (5' nuc domain), understanding the coordination between these two parts and their three enzymatic activities is of great importance. The authors chose a comprehensive number of DNA substrates that feature various flaps (downstream, double, mixed), gaps, and constructs without downstream DNA. The most significant results of this study include (1) the observation of reversible swapping between the DNA synthesis domain and 5' nuclease domain during a single encounter with DNA substrate and (2) there are varying positions of the 5' nuclease domain depending on the nature of the DNA substrate (i.e. gap, 5' flap, double flap). Previously, the authors applied similar experimental strategy to Klenow fragment. Comparing the data for KF and the full-length Pol I shows that nuc domain appears to suppress or override pol-exo transitions observed in KF. Overall, the manuscript is well written and presented, and supported by excellent experimental data.

The reviewers agree that the study is interesting, important and well executed. They have, however, identified several points that need to be addressed prior to publication:

Essential revisions:

1) The current study is performed under equilibrium conditions meaning that all potential enzymatic activities were abolished using suitable mutations. Moreover, the measurements were performed in absence of any nucleotides, which, depending on their complementarity to the free base of the template strand (if existing), are likely to influence the binding equilibrium of DNA pol I. Please comment on this and also on whether the DNA binding abilities of Pol I mutant (C262S/C907S/K550C/D424A/D116A, C262S/C907S/ /D424A/D116A/T213C) Pol and 5' nuc domains are similar to that of the WT polymerase.

2) Figure 3C: The L361A mutation compared to WT Pol I histograms seem to indicate that the 0.6 FRET population does not predominately arise from binding of DNA to the exo domain. However, there is a significant shift in the two populations of FRET states, with the L361A mutant having 15% more in the Pol domain bound, or 0.8 FRET efficiency state with the double flap substrate. Can the authors speculate why this may be the case, if not related to exo domain DNA binding? Has this mutant been tested for exo binding in Pol I or just KF?

3) The representation of the histogrammed FRET data is unusual. The analysis of time traces using HMM is clear. Per trace, the authors end up with three FRET values, e.g., 0, 0.61 and 0.78. Summing up over all traces, the authors can calculate three mean values, e.g., 0, 0.6, 0.8. How do the authors then end up with the smooth curves shown in Figure 3D? Convoluting the mean FRET values with a log-Gaussian? To access the quality of the general experimental data, it would be informative to show the raw FRET histograms of all combined time traces in addition to the "smoothed" histograms in Figure 3C, Figure 4B, Figure 5C.

4) Please add some more example traces to the supplement. Whereas the histograms and transition plots of the mixed flap suggest a 50/50 chance of starting in either P or N mode, the example trace suggests all five binding encounters to start in the P mode. Please comment on that observation?

5) Subsection “Movement of DNA between pol and 5’ nuc domains of Pol I”, seventh paragraph: "Interestingly,…"

Transfer rates were obtained from the exponential decay of the dwell time histograms (e.g., Figure 3—figure supplement 1). The fact that these apparent transfer rates P→N (kP→N) and P→U (kP→U) are similar is not a coincidence. Theoretically, the two rates should be similar (barring statistical uncertainty). P state can decay via two parallel pathways to either N or U. Therefore, the decay rate of the P state reflects the sum of the actual transfer rates (kP→N+kP→U) regardless of which state P decays into. To obtain the actual transfer rates (kP→N and kP→U), one should compute the relative frequency of transitions (how many decay to N vs. U as reported in Appendix 3—table 3), which determines the branching ratio kP→N/kP→U. From the sum and the ratio, individual rates kP→N and kP→U can be extracted. The rate constants reported in Appendix 3—tables 1, 2, 4 and 5 should be corrected, accordingly. Likewise, the apparent kP→N and kP→U should be similar for the mixed flap case as well. But the fact that they differ (Figure 3E) may suggest that the P state (0.8 FRET) measured for the mixed flap case is not a pure macrostate (or relatively impure compared to the downstream or double flap case). For example, the mixed flap P state can transition to N and U through different microstates that are all degenerate in their FRET values. This scenario makes a lot of sense because the mixed flap substrate should be in a dynamic equilibrium between different strand displacement intermediates.

6) Figure 3B: There seem to be short-lived events at a low FRET (e.g., at ~3 second). Could these represent unstable binding events like binding of the nuc domain to the downstream strand? How the frequency of these events changes with different substrates?

7) Are the apparent transition kinetics measured with the second labeling scheme similar to those measured with the first labeling scheme? Or perhaps is the data too noisy to extract rate constants?
