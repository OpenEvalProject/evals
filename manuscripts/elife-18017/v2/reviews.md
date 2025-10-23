# Peer review - Round 1

Editors:
- Kenton J Swartz, National Institutes of Health , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18017.028](https://doi.org/10.7554/eLife.18017.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Proton currents constrain structural models of voltage sensor activation" for consideration by eLife. Your article has been favorably evaluated by Gary Westbrook (Senior editor) and three reviewers, one of whom, Kenton J Swartz (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: David E Clapham (Reviewer #3). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting manuscript describing the creation and careful characterization of a proton shuttle in the resting state of the voltage-activated proton channel (Hv1) by introduction of a His residue at the outer R1 position within the S4 helix. The authors have done all the right experiments to understand the R1H mutant, the experimental data appear to have been very thoughtfully collected and analyzed, and are of very high quality. The significance of the proton shuttle is that it positions the R1 position of S4 down near the charge transfer Phe in S2 where one could readily imagine protons hopping between external and internal solutions. The authors also create new models for the resting and activated states of Hv1, and these are compared with structures and models of Hv1 and other proteins containing S1-S4 domains. Overall we think the work is appropriate for eLife, but the text and computational components will require careful revision.

Essential revisions:

1) Throughout the manuscript the authors complicate the story by assuming that the voltage-dependence for GSH must reflect a conformational change in the protein, rather than arising from an intrinsic rectification to proton permeation. Until we get to Figure 4F, all the data actually would support a mechanism involving rectification of permeation. Also, the apparent shifts in the dG/dV analysis are only a hint. We suggest removing all verbiage about gating mechanisms surrounding GSH until you get to the section of the Results where you wish to present the Figure 4F experiment. Then you can raise the issue about mechanism of voltage-dependence to GSH, remind the reader about mutants affecting GAQ and not GSH, and then show how pH seems to shift both and talk about what that might mean. The authors ideas may be on the right track, but they don't have very firm ground to stand on and the presentation should reflect that.

2) The paper is straightforward to read and understand for experts, but it is too longwinded and will be impenetrable for the outsider. Terms like Ftail and Fhook are thrown about and won't be clear to those who haven't read the Larsson paper. In its present form it will probably only be read by scientists working on Hv1 or those who are total nerds and simply love the topic of voltage sensing. We think it can and should be reduced by 25-50% with careful editing and rethinking about what really needs to be discussed. The modeling parts of the Results and Discussion (see also point #4 below), in particular, need serious trimming and prioritization about what really needs to be discussed.

3) It is true that GSH was not evident in the previous paper cited for the R1H mutant, but in that work they only show data down to -10 mV, a voltage where the shuttle current would be very small. That study focused on looking at accessibility of inserted His to Zn, not on explicitly looking for a shuttle conductance. One sentence in the Results section would suffice to accurately state that GSH was not reported in earlier work, but that those authors did not pulse negative enough to see it.

4) We have serious reservations about the analysis of the modeling. First, the description of the generation of Hv1 E is not clear: "Representations of Hv1 E represent the first snapshot in a trajectory of ten possible structural conformations collected from a 1 ns MD production run." What is meant by "ten possible structural conformations"? Second, the analysis presented is based on single snapshots from MD simulations, which may or may not be representative, or may be one of multiple populated configurations, as the authors themselves point out in the last paragraph of the Discussion: "Because Arg side chains may exhibit a high degree of dynamic flexibility (9), distance measurements inferred from static snapshots here and elsewhere should be regarded as relatively coarse descriptions of conformational rearrangements in a highly dynamic protein domain." If only single snapshots are being reported, then what is the point of running MD simulations in the first place? And what is the criterion for a particular choice of snapshot? Were the trajectories clustered and the most populated cluster chosen? Third, with MD trajectories in hand, the authors have the opportunity to analyze internal hydration structure and dynamics, as well as electrostatic potential, as many others have done previously for Kv and Hv channels. However, no such analysis was performed, and statements such as the following (among others), are not substantiated by simple inspection of a single snapshot lacking water molecules:

"Hv1 D and E model structures are consistent with the notion that both gating charges and permeating protons cross the focused electrical field through a hydrated crevice."

"the central crevice remains substantially open, and may accommodate water molecules that are necessary for H+ shuttling via R1H"

"we find that the imidazole ring of R1H is apparently located within the solvent-accessible VS domain central crevice"

"Although Hv1 D and Hv1 E appear to be fully compatible with GSH experimental data reported here, other putative resting-state Hv1 VS domain structures evidently do not contain sufficiently hydrated central crevices to accommodate H+-shuttle function."

"Taken together, the experimental data and model structures reported here suggest that GAQ and GSH share a common H+ permeation pathway with S4 gating charges and that translation of S4 during VS activation must be of sufficient amplitude to 'unblock' the hydrated central crevice to open G_AQ."

In short, we think that many of the conclusions emerging from the modeling are not substantiated by the data presented. We therefore request that the amount of space (text and figures) devoted to the modeling be greatly reduced. To the extent that you wish to draw conclusions from the modeling, we request that you quantitatively analyze your Hv1 models to provide more information on hydration and electrostatics.
