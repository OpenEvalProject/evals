# Peer review - Round 1

Editors:
- Randy B Stockbridge, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84808.sa0](https://doi.org/10.7554/eLife.84808.sa0)

The current manuscript investigates the energy landscape of the mammalian sugar porter GLUT5 using enhanced molecular dynamics simulations and biochemical assays. The approach generates important insights into the mechanism of GLUT5 conformational change, and into mechanistic diversity among the GLUT sugar porters more generally. The overall strategy is convincing, and the findings will be of interest to the transporter and membrane biology communities.


---

# Peer review - Round 1

Editors:
- Randy B Stockbridge, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84808.sa1](https://doi.org/10.7554/eLife.84808.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Determinants of sugar-induced influx in the mammalian fructose transporter GLUT5" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Randy B Stockbridge as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kenton Swartz as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Krishna D Reddy (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. To show that the differences between the free energy landscapes in Figures 2E and 2F are meaningful, the authors should report a statistical error analysis on the free energy landscapes, for example by calculating the latter with different subsets of the simulation data and evaluating the standard error.

2. Other than statistical errors, the reviewers are also concerned that there may be systematic errors due to slow protein motions and sidechains rearrangements that do not properly equilibrate during the simulation time scale (generating hysteresis). Hence, additional validation of the reliability of the calculated landscapes must be performed. If systematic errors are very high, the free energy landscape would reflect high energy (unphysical) conformations, which are typically present if the initial structures are generated with targeted molecular dynamics (TMD), as in this work. Therefore, the authors should show that conventional MD simulations are compatible with the free energy landscape. If systematic errors are indeed confirmed by the authors, unfortunately, this might entail redoing /redesigning the free energy landscape calculations. Conversely, if the controls show that systematic errors are not large, it would be sufficient that the authors discuss them, together with the potential pitfalls of using a small number of collective variables (just two were used, while in other applications by different authors, these were over ten).

The reviewers' specific concerns with regard to hysteresis/systematic errors include:

a) The fact that simulations convergence depends on the direction (outward-to-inward vs inward-to-outward; the authors describe limitations of inward open to outward open simulations in regards to salt bridge distances) indeed strongly suggests the presence of significant hysteresis/systematic errors. Namely, the lack of reversible formation and disruption of salt-bridges might have artificially over-stabilized outward-facing states (as landscapes are only for outward-to-inward direction).

b) If the free energy landscape in Figure 2E is correct, the reviewers would expect the green fuzzy area (inward open/inward occluded) should have at least overlapped with the blue area (fully occluded). This may indicate that either the MD simulation is too short, in which case the authors should elongate it until equilibration into the closest free energy minimum, or the free energy landscape is not correct.

c) The fact that the inward open X-ray structure is a high energy conformation in the free energy landscape in Figure 2E (bottom right triangle; X-ray structure is without substrate) is also concerning since one would expect it to be in the energetically feasible region (within 2-3 kcal mol from a main free energy minimum) unless the X-ray structure is not a functional state, which seems unlikely.

3. The authors should provide a more detailed description of the computational analysis and/or associated citations. In addition, the authors should provide further details on homology models and simulations based on the latter: number of models generated, criteria to select the final model, side chain refinement prior to simulation, quality scores, etc.

4. The authors should provide additional justification as to why the MD simulated outward-occluded state deviates so highly from the starting model. Are there AlphaFold models, or simulations from other groups, that agree with this inconsistency? Alternatively, is the 'crystallized' state stable in the presence of monoolein?

5. The D-fructose concentration tested in the assays was far below the Km (6uM compared to 10 mM), further complicated by unknown Km values of the mutants. This complicates the interpretation of the relative activities since the activity will be highly dependent on substrate concentration. The authors should consider this caveat in their discussion of the mutant activity.

6. The authors should provide additional discussion or clarification on several points related to the experimental results for the mutants.

a. While the 'quadruple' mutant result is impressive and informative, it is difficult to infer firm conclusions from the data and model presented. It might be expected that this mutation should convert GLUT5 into a glucose transporter – yet this mutant is unable to transport glucose.

b. Could the elevated rate for Y296F (and the quadruple mutant) simply be more efficient salt-bridge breaking?

c. If the authors have tested mutation of the YY motif to SN in GLUT5, it would be informative and interesting to know the result regardless of the outcome, in order to understand whether specificity is encoded by this motif alone, or by more complex global interactions.

d. The importance of N293 and its large conformational change was mentioned a few times. Could the authors include a supplementary figure showing how this residue in particular moves to engage with the substrate in the occluded state? Is there anything to the bimodal distribution of distances to the substrate seen in Figure 3D?

e. There is clearly some activity in the N293A mutation, suggesting that this residue (and thus the interaction with the sugar) is not 'required' for transport. In fact, the MD simulations would support this, as the broken helix state can be visited in the absence of substrate. Thus, the authors should rephrase this point.

Reviewer #2 (Recommendations for the authors):

1. I would like to see some additional justification as to why the MD simulated outward-occluded state deviates so highly from the starting model. Are there AlphaFold models, or simulations from other groups, that agree with this inconsistency? Alternatively, is the 'crystallized' state stable in the presence of monoolein?

2. The authors nicely demonstrate the coordination of the substrate binding site, and that a tightly conserved N residue in TM7b (that coordinates with the substrate sugar) appears to induce the broken helix conformation and thus the occluded state. Though these conclusions are generally supported by the experimental data, I have some concerns about the conclusions:

– There is clearly some activity in the N293A mutation, suggesting that this residue (and thus the interaction with the sugar) is not 'required' for transport. In fact, the MD simulations would support this, as the broken helix state can be visited in the absence of substrate. Thus, the authors should rephrase this point.

– The D-fructose concentration tested in the assays was far below the Km (6uM compared to 10 mM), further complicated by unknown Km values of the mutants. Thus, I do not think it is appropriate to overly interpret relative activities from initial rates and would suggest the authors use more careful language when referring to these results.

– While the 'quadruple' mutant result is impressive and informative, I find it difficult to infer firm conclusions from the data and model presented. It almost seems as if the objective was to convert GLUT5 into a glucose transporter – yet this mutant is unable to transport glucose. Furthermore, could the reason for elevated transport in Y296F (and the quadruple mutant) simply be more efficient salt-bridge breaking?

– I assume the authors have tested the mutation of the YY motif to SN in GLUT5. If this mutation was tested, it would be informative and interesting to know the result regardless of the outcome. Is specificity encoded by this motif alone, or are more complex global interactions required for promiscuity?

Reviewer #3 (Recommendations for the authors):

Currently reported simulation data do not conform to quality standards for publication. In particular, the authors should report an error analysis on the free energy landscapes, for example by calculating the latter with different subsets of the simulation data and evaluating the standard error. Provided the free energy landscapes are converged, free energy minima should correspond to locally stable conformations in conventional MD simulations, hence additional validation of the reliability of the calculated landscapes must be performed also using the latter technique. A good example that the authors could follow and cite, with appropriate quality standards, is Lev et al., PNAS 2017, E4158-E4167, which is also based on the string method with swarms of trajectories and in which the free energies were also obtained from the transition matrix.

The authors reported that they also obtained the free energy in a similar manner but they neither described in detail the methodology nor they cited any reference in this regard, therefore the results are currently not reproducible. A detailed description thereof and/or associated citations must be provided.

The authors should provide further details on homology models and simulations based on the latter: number of models generated, criteria to select the final model, side chain refinement prior to simulation, quality scores, etc.

The authors mentioned that to model efflux was more difficult because of salt bridge formation. A possibility to solve this issue is to increase the number of variables used in the string method, including for example a variable describing salt-bridges formation and disruption. In the previously mentioned reference for example the authors used tens of collective variables rather than just two as in this work. In this regard, the authors should at least discuss the potential issues of a low-dimensional representation.

Assuming the free energy landscapes are reasonably well converged, a suggestion to improve the impact of this work is to obtain the same landscapes with bound glucose, so as to assess how GLUT5 is less selective towards the latter than fructose. Namely, if the alternating access transition in the empty transporter is rate limiting, occlusion with glucose ought to be significantly destabilized with respect to fructose and in this manner, the authors could effectively demonstrate that substrate occlusion controls selectivity.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Determinants of sugar-induced influx in the mammalian fructose transporter GLUT5" for further consideration by eLife. Your revised article has been evaluated by Kenton Swartz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there is one minor remaining issue that needs to be addressed, as outlined below:

1) The reply to the reviewers contains an important discussion of the observed deviations from free energy minima and a plausible justification of their possible meaning (page 4, under the heading "Compatibility of free energy surfaces with control simulations"). Although these controls are summarized in the methods of the updated manuscript, it is also desirable that the manuscript text be expanded upon to include the following information, which is currently reported only in the response to the reviewers: (1) a description of the drifts observed during conventional MD simulations and (2) the justification described in the response to reviewers. (Namely, that those drifts may reflect the fact that the collective variables used for the free energy landscapes might be very sensitive to small structural fluctuations.)

Reviewer #3 (Recommendations for the authors):

The revised manuscript entails significant improvements over the previous version. Namely, statistical errors have now been calculated and reported in the manuscript. Methodological procedures are now better described and the authors clearly exposed the possible limitations of the simulations results.

The authors have clarified most of the critical points in their reply. One remaining issue is that the new controls reported do not rule out the presence of systematic errors in the free energy landscape. In particular, some of those show that unbiased simulations drift out from free energy minima, while ideally they should show equilibration in a local minima across all relevant collective variables.

This notwithstanding, I understand the complexity of modeling conformational transitions in membrane transporters and the stochastic nature of short conventional simulation (which the authors have clearly outlined).

Despite the possible presence of systematic errors, the controls and validations done by the authors seem to indicate that the difference between the free energy landscapes of empty versus bound transporter is meaningful, which together with the structural interpretation and biochemical experiments is the most important result of this work. Therefore, in my opinion, the reported results are relevant and may provide novel important insights into the mechanism of mammalian fructose transporters.

One last suggestion for the authors is to briefly mention and discuss previous computational work where it has been shown that transport is facilitated by energetic stabilization of an occluded state (e.g. upon substrate binding) (Selvam et al. on a SWEET transporter ACS Cent. Sci. 2019, 5, 1085−1096).
