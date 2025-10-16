# Peer review - Round 1

Editors:
- Rohit V Pappu, Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68620.sa1](https://doi.org/10.7554/eLife.68620.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This work is timely and relevant as the field grapples with the issue of diffusive dynamics across phase boundaries. The numerical formalism in this work will be of broad interest to the condensate field.

Decision letter after peer review:

Thank you for submitting your article "Quantitative Theory for the Diffusive Dynamics of Liquid Condensates" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Rohit Pappu as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Both reviewers have arrived at similar conclusions. FRAP is a method that is routinely used to study internal dynamics of molecules within biomolecular condensates. Of course, FRAP was introduced in a completely different context, and as has been shown before, its adoption needs appropriate adaptation to the context of interest. How should FRAP data be analyzed in the context of studying biomolecular condensates that form via phase separation. The authors build on the work of Hardt and coworkers, and demonstrate the incorporation of a Flory-Huggins free energy alongside diffusion equations to describe the dynamics of unbleached molecules, using features of mass balance. They show that numerical solutions of the derived equations – see Equation (6) – can be used to fit FRAP data for different systems. The authors also suggest that inferences from FRAP data can go beyond extraction of individual parameters. In other words, FRAP data seem to be more information-rich than originally thought. The current version, although very interesting, features opacities that should be remediable by following the recommendations made by both reviewers.

Essential revisions:

1) Two distinct flowcharts summarizing how Equations (1) and (6) are used in the fitting of FRAP data will be essential.

2) Accounting for interfacial tension and / or interfacial resistance (see Taylor et al.) requires discussion.

3) Please delete references to non-equilibrium situations since the model imposes detailed balance throughout. In fact, this point should be made clear.

4) There is considerable confusion regarding the claims regarding being able to extract Din, Dout, and P from single sets of FRAP data and the actual demonstration of this versatility. This is accentuated by considerable confusion caused, for both reviewers, by the introduction of the cost function, which was opaque, and the sweep of parameters for Dout and P that clearly give satisfactory fits to the FRAP data. At this juncture, the claim of being able to extract more insights from FRAP data than one is accustomed to seeing has not been unequivocally demonstrated.

5) Several scholarly issues, specifically pertaining to the work of Hardt and colleagues, and the semantics of what constitutes a phenomenological vs. physical theory description were raised. These should be addressed and there is a strong desire to see a toning down of what were perceived as over-claims.

Reviewer #1 (Recommendations for the authors):

As it currently stands, the average practitioner of FRAP is likely to find the narrative to be rather opaque. Two flowcharts, that summarize (a) how the dynamic boundary condition and its application lead to the internal diffusion coefficients and (b) the use of equation (6) for experimentalists in their analysis of FRAP data need to be added. In doing so, it is really important to explain when and how the analysis can be used, and when and where it cannot be used.

Other recommendations:

1. phi is a conserved order parameter, because the underlying theory imposes a closed system. Therefore, the relations between phitot and phiu etc. come not from incompressibility, but from mass balance in a closed system.

2. The work of Steffen Hardt, mentioned in passing, and labeled as being phenomenological needs rectification. Elaboration of their work and a clear, scholarly contrast between the current effort, the published work of Hardt that goes beyond the 2008 Langmuir paper, and the differences between the work of Taylor et al., would be helpful for the reader who is interested in understanding what is new, and what is different. In this context, please also see Lin et al., (2003) Science 299: 226, Binks and Lumsdon (2000) Langmuir 16: 8622.

3. The authors classify previous efforts as being phenomenological and the current effort as a physical theory. Respectfully, I disagree with this characterization. Inasmuch as previous efforts largely use the same equations as being used by the authors, with the key difference being the use of the FH functional for extracting the chemical potentials, the extant literature and the current manuscript are both phenomenological or both physical theories. It would be best to drop these prefaces and simply state what has been done. Specifically, the work of Hardt and coworkers does account for phase boundaries. They don't use the FH free energy functional, and this is really the only main difference. And many would rightly argue that the FH functional is phenomenological. So, please do not use terms like "first principles" for this work, and phenomenological to inadvertently dismiss other efforts.

4. Throughout the manuscript, there is a lot of self-congratulation about the excellent fits, the striking agreements etc. This is jarring. It is impossible to know if one should be impressed with the agreements or if such agreements are readily achieved. An unvarnished statement of the facts is sufficient.

5. The description of the cost function analysis needs a lot of work. In effect, the implication is that Dout depends on P. Whether this is an implicit function or not is unclear. The cost function has not been defined in the main text, and why there should be a minimum is unclear. There is also a curious leap that happens: at one point, we see that Dout and P that describe the data can span a wide range. This would lead to inference that the FRAP data cannot pin down these parameters absent independent measurements. However, the conclusions paint a more rosy picture, suggesting that knowledge of Din is sufficient, and that fitting the FRAP data will lead to reliable estimates of Dout and P. The section that describes this leap needs a lot of work. The flowcharts recommended in the public review will help.

6) There are important caveats that apply as well. The slow or non-recovery of fluorescence, becomes a scenario wherein Din will be very small or immeasurable. Alternatively, if the material state has changed, then the usage of the dynamic boundary condition might still yield reliable measurements of Din, due to an anisotropic stress tensor, but this would be an erroneous estimate of Din on the inside. Therefore, it is important to lay out a set of requirements for the applicability of the proposed approach, i.e., under what circumstances can the method be used, and under what circumstances can it not be used.

7) As a logical follow up to the preceding point, how might one falsify the theory? Fitting FRAP data is inadequate for such an effort. This will be very useful for experimentalists and computational scientists alike.

8) Finally, do the authors know that the salt concentrations across the phase boundary are equal to one another or is this implicitly assumed? This is particularly relevant for the synthetic coacervates. Sing and coworkers have proposed that there are differences in salt concentrations (even ion concentrations) across phase boundaries. This is relevant because it requires the addition of a Donnan potential to the equations that describe molecular transport. A discussion of this issue would be helpful.

Reviewer #2 (Recommendations for the authors):

Concerns on figures and writing:

1. Recurrent lack of clarity and/or consistency in how figures are presented

When dissecting the data shown in figures, we often found details in presentation that detracted from our understanding of the study. Notable, but not exhaustive, examples are listed:

a. The retrieval of physical parameters in this study frequently alternates between the use of Equation 1 to track FRAP data, and Equation 6 to model droplet dynamics. The authors do not clearly distinguish the purpose of these equations in the theoretical sections, leaving the reader to understand by context.

b. The data in Figure 3 would benefit from control data sets that entirely lack the coverslip and/or neighbouring droplets for comparison. In particular, showing the retrieval of identical Din across all simulations (including no coverslip nor neighboring droplets condition) will convey the major point of the paper very clearly.

c. In the caption of Figure 5 it is unclear why the authors have denoted the four indicated values of Dout and P as "reference systems' as opposed to example parameter sets.

We recommend the authors reassess their figures for clarity of the information that is meant to be communicated.

2. The theory sections lack needed elaboration in some areas.

a. The authors conclude starting on line 153 that P, Din, and Dout can be treated as independent of each other for sufficiently large P. Their justification is that the unknown mobility functions do not impose constraint on Dout(P) other than shown in Equation 10. While the data demonstrates that this is a valid assumption, we find this justification to be opaque and would like to see further elaboration on how independent P, Din, and Dout follows from the mobility functions being unknown.

Suggestions to the authors for bolstering the overall strength of this study below:

1. When interpreting the Results section, we often found that the nature of the experiment was unclear. This is particularly true for Figure 4 and 5. We recommend specifying the procedure followed to acquire the data more clearly and explicitly.

2. In Figure 1c, the label "Dynamic BC" made this figure confusing to interpret, especially because there is a same-color arrow depicting time progression. The authors should consider some other way of noting that dynamic BC is applied at the max r (=R-). Also, for the line going across the earliest data points, "initial condition" rather than the "fit" label may be more appropriate.

3. If available, showing corrected viscosity data from Jawerth et al., 2020 rather than Jawerth et al., 2018 in Figure 1d would bolster this figure via internal consistency with the text in line 98. We would like to be able to back-calculate consistent viscosities using your diffusion data and the Stokes-Sutherland-Einstein relationship.

4. Since the time progression of FRAP recovery is illustrated in Figure 2c, we believe the time point label in Figure 2 to be unnecessary and possibly confusing.

5. We find that the citation of privately communicated and unseen data in line 234 does not add to the preceding statement. Optimum salt concentration is a very believable observation.

6. There appears to be a typo in the subscripts on line 138. Both read "in".

7. Regarding the concluding statement on line 306: We do not find that Jawerth et al., 2018,2020 contain discussions of altering dense phase kinetics by high labeling fraction. Rather, McCall et al., 2020 describes effects closer to this.

8. Regarding Figure 5a, labelling the "ratio" of Dout and P can be confusing. We suggest noting the specific (Dout, P) pairs to specify the points. Also, a clear distinction between "simulation generating parameters (points)" and the "Dout and P dependence (lines) obtained from simulation result and equation 6" is needed.

9. Please consider labelling the point in Figure 5b as "simulation input" or "simulation parameter" rather than "reference simulation".

10. We suggest the following change in line 230 for clarity: "Specifically, for salt concentrations in the range from 50 mM to 180 mM, we find that the estimated partition coefficient P of PGL-3 droplets decreases more than 10-fold."

11. The significance of the shading in Figure 4d is unclear and inconsistent with how the analogous data in Figure 4e is presented.

12. The text accompanying Figure 5 beginning on line 249 describes the range of Dout and P used as "relevant for protein condensates and coacervate droplets' without citation. We recommend backing up the validity of the range of Dout and P used here with evidence from literature.

13. In Figure 1b, individual FRAP recovery curves cut off at seemingly arbitrary points and are difficult to distinguish based on provided color coding. We also note that the curve of 100mM salt concentration does not seem to fit the same trend as the other data sets, but is not discussed by the authors.

14. Figure 1f shows the precision of Din determination for the two coacervate systems, but not the protein condensate system, and a salt concentration for comparison with Figure 1d is not provided.
