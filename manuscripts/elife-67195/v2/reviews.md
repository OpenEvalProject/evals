# Peer review - Round 1

Editors:
- Michael L Dustin, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67195.sa1](https://doi.org/10.7554/eLife.67195.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your work shows, based on Molecular Dynamics simulations, the structural variability of the T cell receptor complex. Changes in the tilt angles of the extracellular antigen binding domains were observed to correlate with changes in the orientation of transmembrane helices, which may well impact signal transduction during antigen recognition. Your responses to the reviewers have improved the clarity of the approach and interpretations are well supported by experimental observations where available.

Decision letter after peer review:

Thank you for submitting your article "Structural variability and concerted motions of the T cell receptor – CD3 complex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Michael L Dustin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tadatsugu Taniguchi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Brian Baker (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All the reviewers found the early results on MD simulations of full TCR to be of great interest and potential value. The paper currently doesn't provide sufficient insight for publication in eLife, but it was felt that additional discussion could address this in different directions that might be best selected by the authors. The reviewers didn't reach a consensus, but hope that with the individual reviews below the authors can revise the manuscript to increase the value for immunology and signalling audiences along one or two of the lines suggested.

1) There was some consensus regarding discussion of the limitations of the short simulations with implications for stability of the system and the ability to establish correlations. Is there potential to use the results from these simulations to develop coarser simulations over longer time that might get into the time frame of pMHC interaction and force application. A discussion of these future directions could be helpful in addition to pointing out current limitations.

2) A video showing the TCR fluctuations would be nice.

Reviewer #1:

It would be important to determine if this atomistic simulation lasting 1 µs could be used to seed a coarse grained simulation that could operate in time frames relevant to natural ligand binding and capture the major movements documented here, for example the 4 clusters, to enable MD simulations of sufficient duration to ask questions about TCR signalling in a realistic time frame.

Reviewer #2:

While the strengths of the paper are in the testable hypotheses that are generated, there are weaknesses that should be considered:

– The simulations give a window into thermal fluctuations around the 'average' cryoEM structure. The extent these rapid motions give insight into signaling mechanisms is limited. For example, there is no comparison of how the motions of a pMHC bound structure might differ, or how fluctuations might be altered under load.

– The authors do a limited analysis of equilibration, which is always needed in complex simulation papers to ensure the robustness of the data and conclusions.

– There is a limited analysis of structural variance or correlated motion. Overall, the authors give very limited attention to the high level of detail that MD simulations are capable of and arguably best known for.

Comments for the authors:

There are major weaknesses that should be considered:

1) The authors perform a total of 120 microseconds of simulation in explicit solvent, performed by compositing many shorter simulations. This is a considerable amount of simulation time. However, the authors are still looking at motions that would be comparable to experiments on the nanosecond timescale. It is highly unlikely that these simulations would capture what occurs upon binding or applied force, which would occur with higher barriers and over longer timescales. Instead, we are looking at thermal fluctuations around an equilibrium structure. While still providing testable hypotheses regarding how a TCR/CD3 might be 'poised' for signaling, the immediate insight into signaling mechanisms and thus impact is very limited. The authors need to consider this throughout their manuscript.

2) The authors do not do a complete analysis of equilibration, using domain angles and contacts as a window into equilibration. There are none of the analyses that are traditionally performed with long simulations to ensure equilibration of the structure (e.g., is domain assembly maintained, how is secondary or tertiary structure maintained, what about membrane stability, etc.).

3) Similar to the point above, the analysis is limited to contacts and angles. One might expect various higher frequency motions to be insightful – for example, what does the structure of the FG loop do over the course of the simulation? That about the β chain AB loop, which has been implicated in triggering? The overall analysis is very high level and lacking in the kind of rich detail that extensive MD simulations are capable of.

4) There are no direct connections to experiments here. Experimental data do not need to be included, but over the years there have been many mutation, perturbations, etc. performed that the authors could look at. Similarly, there are no pMHC bound or force experiments included that could give insight into actual signaling mechanisms as opposed to the ligand-free and force-free fluctuations that presumably occur as the molecule is waiting for something to happen.

5) Related to the point above, there is data suggesting dynamic allostery as a mechanism contributing to TCR triggering. Dynamic allostery requires correlated motion – none of that is considered here.

Reviewer #3:

Weikl and colleagues used the structure of the T cell receptor complex, which has recently been determined via cryo-electron microscopy, as basis for an atomistic modelling approach. This method offers the advantage to overcome a central limitation of cryo-EM, which is the choice of the membrane lipid environment: while experiments have been based on embedding the protein in detergent, Weikl et al. used here glycerophospholipids and cholesterol, which reflects the natural situation in the plasma membrane more appropriately. In addition, cryo-EM required the addition of fixatives, which is not necessary in the MD simulation approach.

The paper reveals interesting new dynamical information about the TCR complex. It would be informative, if the authors would include a discussion on the following points:

Figure 2: How is contact between residues defined? Would an isolated 10ns encounter already qualify as contact? What about analyzing the contact duration? What is distance between two sites to qualify as contact?

Figure 3a/b:

• It would be helpful to indicate rotation angle 0; maybe by adding an en face view onto the axis A?

• The tilting of the TM helices appears to be accompanied by slight local thinning of the membrane. Is that correct? Do lipids adjacent to the transmembrane helices follow the tilt, and/or is there different ordering of the fatty acids? Is the cholesterol distribution affected by the tilt? How would different lipids with different length or compressibility affect the helix tilting?

• What would generally happen if different lipids were tested, particularly asymmetric lipid distributions across the membrane? In the natural plasma membrane environment lipids are distributed asymmetrically across the leaflets, with saturated and unsaturated lipids of different chain length being enriched in the extracellular and cytoplasmic leaflet, respectively. It would be interesting, whether this compensates or probably even amplifies the observed mechanism. Maybe the authors could add a discussion on this aspect.

Figure 3 c and e: It would be informative to add the results of the cryo-EM study here.

Figure 3: For better comparison, it would be nice to scale the y-axes with identical increments.

If fluctuations of the TCR α/β would be similar in reality as it was revealed in the simulation, I would expect continuous fluctuations of helix tilt angles. If helix tilt angle was indeed a cause for signaling, wouldn't that lead to continuous aberrant activation of the TCR?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Structural variability and concerted motions of the T cell receptor – CD3 complex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Michael L Dustin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tadatsugu Taniguchi as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The paper is significantly improved by the inclusion of the videos and discussion of some biological implications.

1) Is it correct that the rotation angle 0 is defined by the origination in the published cry-EM structure? Regardless, this should be defined more clearly in the text and figure.

2) The authors should address the points raised by reviewer 3 regarding force induced tilt through clarification of the text and explanatory schematics if helpful. It may also be interesting in addressing the last comment to determine if the observation of supine orientation of MHC class I at a membrane surface is relevant to the discussion. see Mitra AK, Celia H, Ren G, Luz JG, Wilson IA, Teyton L. Supine orientation of a murine MHC class I molecule on the membrane bilayer. Curr Biol. 2004;14(8):718-24. Epub 2004/04/16. doi: 10.1016/j.cub.2004.04.004. PubMed PMID: 15084288. Is this natural orientation of MHC class I aligned with the tilt of the TCR when the interface is formed? Does the tilt angle of the TCR create a natural rudder to orient the TCR and would it matter which of the CD3 or zeta-zeta tails are pulled.

Reviewer #3:

In principle, all of my previous questions were adequately addressed. There was a misunderstanding concerning my previous comment on the specification of the rotational angle in Figure 3: My problem was to understand, which TCR conformation corresponds to a rotation angle 0. The authors may still consider to add this information.

Concerning the new data on force-induced tilt, however, I have a few questions:

– First, the authors mention on multiple locations in their paper a force-induced tilt of the TCR-MHC complex. The MHC, however, was not included in their simulations. I suggest being more precise in this aspect.

– Second, if I understand correctly, force was not included in the simulations, but instead the effect was added a posteriori. I had difficulties to understand the rationale behind it. What is the justification for the equation given in line 346? What was actually multiplied by the exponential function?

– Third, wouldn't one expect a directionality of the effect? In other words, if force acted, say, in the opposite direction to the naturally occurring tilt, is the idea that the TCR would align with the external force field?

– Fourth, I would be more careful with speculations concerning CD45 segregation. The authors argue in the discussion (line 175 and following) that TCR tilt brings the two membranes in closer juxtaposition. But that would only be true if MHC would also be sufficiently flexible to compensate for the TCR tilt, keeping the two membranes parallel.
