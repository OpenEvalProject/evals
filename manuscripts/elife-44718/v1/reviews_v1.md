# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research United States

Reviewers:
- Wei Yang, United States

## Review text

DOI: [10.7554/eLife.44718.016](https://doi.org/10.7554/eLife.44718.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Comment on 'Valid molecular dynamics simulations of human hemoglobin require a surprisingly large box size'" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Yibing Shan), a Senior Editor (John Kuriyan), and the eLife Features Editor (Peter Rodgers). The following individual involved in review of your submission has agreed to reveal his identity: Wei Yang (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please aim to submit the revised version within two months.

Summary:

This comment by Gapsys and de Groot concerns the eLife paper 'Valid molecular dynamics simulations of human hemoglobin require a surprisingly large box size' by El Hage et al.

The comment reports that (a) its authors could not observe an effect of large box size on the T-R transition of hemoglobin in their own simulations, and it argues that (b) the analysis of El Hage et al. may be flawed and the authors therefore challenge the hydrophobic interpretation of the perceived box size effect. The reviewers think that the community of scientists using molecular dynamics simulations will appreciate the efforts by Gapsys and de Groot for their careful re-examination of the box size effect.

Essential revisions:

1) As a whole, the MD community understands relatively little about water box size effects on protein conformational transitions, especially on conformational transitions of large systems. The community's analyses on this topic so far have been mainly based on smaller systems, such as alanine dipeptide, ubiquitin, and the RGGGD pentapeptide. The possibility that the box size effect becomes pronounced only for large protein systems cannot be excluded, although it is far from established. The work by El Hage certainly fell short of performing enough (in the order of hundreds or more) repeats of each simulation to establish statistical significance for their observation. (This is acknowledged by El Hage et al in their response to the comment.) This comment reported substantially more repeats of the simulations (~10) than El Hage et al., but it also falls short of establishing the statistical significance of an opposite observation. The reviewers believe it is important for both parties to not overstate the case, and to clearly acknowledge that the box size effect remains a hypothesis, neither established nor convincingly precluded. Unless the authors think this is not the case, the comment should be revised to reflect this basic reality that neither parties in this debate knows the ultimate answer here.

2) The discussion on the distinction between thermal and kinetic stability in the first paragraph of the results section is not needed and should be removed. (The corresponding section in the reply by El Hage et al. should also be removed.) El Hage highlighted that the observed discrepancy between the experimental timescale of the T-R transition (seconds) and the much shorter simulation timescale of the transition. Although an underlying kinetic effect is also possible, it is not unreasonable to suggest that the thermodynamics of the simulation system is distorted. There is no indication that El Hage et al. are not aware of the distinction between these two scenarios. At this juncture it is a secondary issue to be concerned about whether the box size effect is of thermodynamic or kinetic nature, when the effect itself is under debate.

3) It is known, though rarely formally acknowledged, that when the simulation length is far shorter than the actual timescale of a molecular event, the simulation results are sensitive to the exact simulation setup. We note that the setups by El Hage et al and by Gapsys and de Groot are not identical, and the differences in the setups potentially involve several parameters (e.g., how the initial water box was constructed, how long the water molecules were equilibrated before the production runs, whether the protein system was restrained during the water equilibriation, and what types of baro-stat and thermo-stat were used et al.) To clarify these issues, please be explicit about the differences between your setups and the setups used by El Hage et al.

Also, please revise your manuscript to address the following comments in the response from El Hage et al.a) The comments in the sentence that starts "A possible problem with the comparisons in their figure 3…"b) The comments in the sentence that starts "We also note a difference in the magnitude of the error bars…"c) The comments in the paragraph that starts "When we were still collaborating…"

4) The comment showed that using a different analysis of the water behavior leads to a different conclusion. In the reply, El Hage et al. clarified that their attribution of the box size effect to the hydrophobic effect remains a hypothesis and it requires further investigation. Indeed, this hypothesis needs further examination by careful analyses of water structures and by extensive free energy calculations. The reviewers suggest that in the revision the authors make it clear that the hydrophobic effect hypothesis is not precluded, although the original analysis by El Hage can be improved.

5) The box size effect, if true, is necessarily a subtle one. The authors' simulations of small proteins without observing a box size effect do not serve as proof to preclude the box size effect, especially for large systems. The authors should make this important caveat clear in their discussions.
