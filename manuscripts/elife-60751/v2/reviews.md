# Peer review - Round 1

Editors:
- Richard S Lewis, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60751.sa1](https://doi.org/10.7554/eLife.60751.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The physical mechanisms by which ion channels open and close to gate ion flow across membranes are fundamental to many physiological processes. The authors showed previously that Orai calcium channels open by a twisting motion that rotates hydrophobic amino acid side chains (phenylalanines) out of the pore. Here, they reveal a previously unknown step in which the rotated phenylalanines engage sulfur-containing methionines, and that this interaction is required to keep the channel open. This work significantly extends our understanding of how calcium signaling via this important class of channels is regulated, and more broadly presents the first example of sulfur-aromatic interactions in ion channel gating.

Decision letter after peer review:

Thank you for submitting your article "A sulfur-aromatic gate latch is essential for opening of the Orai1 channel pore" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Richard S Lewis as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kenton Swartz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael D Cahalan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The mechanisms that control the activity of store-operated calcium channels are a central focus in the field of cellular calcium signaling. This paper describes a novel motif that is critical for the activation of Orai1 channels by the ER calcium sensor STIM1. In previous work, the authors demonstrated that channel opening results from the rotation of a hydrophobic gate comprising six F99 side chains out of the pore, allowing water to enter and promote calcium conduction. Here, the authors provide strong evidence that a sulfur-aromatic interaction between F99 and M101, termed the "gate latch," promotes opening of the hydrophobic gate. Combining molecular dynamics simulations with the experimental introduction of metal ion bridges, they show that the F99-M101 interaction stabilizes the open state of the channel, and without it the channel cannot open even when bound by STIM1. A notable strength of the paper is the effective complementarity of experimental and computational studies which show that the length, flexibility, and chemistry of M101 is essential for its role in gating. While sulfur-aromatic interactions are known to stabilize proteins, this study is the first example of sulfur-aromatic interactions involved in channel gating. Together with previous work by the authors, this paper creates a dynamic view of motions and atomic interactions that underlie the fundamental transitions between closed and open states of the pore.

Essential revisions:

All three reviewers were enthusiastic about the paper, in particular with regard to the powerful combination of experimental and computational approaches, and mostly have only suggestions for clarifying nomenclature and for further discussion of the results to broaden the scope of the conclusions.

1) It is assumed, but not shown, that as the channel opens M101 rotates along with F99 to enable it to contact F99 on the adjacent helix. This should be extracted from the MD simulations and plotted as in Figure 2—figure supplement 1F.

2) The inhibitory effect of M101L on the constitutively open mutant channel H134S suggests that M101-F99 stabilizes the open state. There are other constitutively active mutants with reduced ion selectivity that do not involve rotation of F99, such as V102C. One prediction of the present study is that the M101-F99 latch would not operate in such a mutant, and hence would be unaffected by the M101L mutation. This experiment is optional, as it is not needed to bolster the main conclusion, but it would serve to distinguish the two types of constitutively active mutants and emphasize that helical rotation is needed to engage the latch.

3) In a previous paper (Yeung et al., 2018), the authors showed that M101C did not activate Orai1 even though it destabilizes the closed state, presumably because of an inability to stabilize the open state. Unlike M101C, F187C was previously shown to activate the channel. Does this imply that F187 normally stabilizes the closed state in ways beyond its interaction with M101C? Please comment.

4) It is interesting that the F99C/M101C channel activated by Cd2+ is non-selective (Figure 3), while the same channel activated by STIM1 is Ca2+-selective (Figure 4). This would seem to suggest that trapping F99 in a rotated conformation with Cd2+ does not rotate the E106 selectivity filter to provide Ca2+ selectivity. Please comment.

5) Subsection “Enhancing M101 and F99 interaction boosts F99C/M101C Orai1 channel activity”, third paragraph, Figure 3D. It would be helpful to plot the absolute current levels for the 3 experiments, to provide a sense of how well STIM1 activates WT Orai1 compared to the Cd2+-treatment of F99C/M101C. If Cd2+ doubles the size of the STIM-activated current, does this suggest that the latch is normally engaged about half the time?

6) Discussion: Some explanatory detail should be given for the calculation of free energy stabilization. It is not obvious where the value of 0.5-1 kcal/mol comes from.

7) The manuscript necessarily uses the Drosophila Orai residue numbering in discussing the MD simulations and the human Orai numbering for the electrophysiological data. While the display of both residue numbers in the figures is handled well, the text is sometimes confusing. For example, the manuscript mentions only F99 and M101 in the first few pages, then abruptly switches to Drosophila numbering in the Introduction, without flagging the change for readers. (The human Orai1 numbering follows, in parentheses, but the transition could be accomplished more deftly.) The subheading “Molecular dynamics simulations demonstrate F171-M173 sulfur-aromatic interactions involving the hydrophobic gate in activated states” refers to F171 and the next two lines of text refer to F99, without reminding readers that the two phenylalanine residues occupy the same position in the channel. Minimal rewriting could smooth these transitions.

8) In the first paragraph of the Results, the authors use a mutation in TM2 while focusing on residues in TM1 and TM3. The authors should orient the reader as to where H134 is located somewhere in the subsection “Molecular dynamics simulations demonstrate F171-M173 sulfur-aromatic interactions involving the hydrophobic gate in activated states”, and whether it is well understood how it causes channel opening.

9) Figure 3C nicely shows I-V plots with reversal potentials near zero, in the Cd2+-potentiated current after removing Cd2+, implying a lack of Ca2+ selectivity in the double mutant F99C/M101C after Cd2+ is added. What does the I-V look like just before removing Cd2+? It may be confusing to call this a CRAC current when it seems to be non-selective. A very interesting result, particularly when combined with partial occlusion by STIM1 gating. It might be nice to show the I-V curve of the same mutant in 110 Ca2+ external solution (panel F).

10) The GOF channels with smaller residues at position 187 produced nice CRAC-like I-V curves. What does this tell us?

11) The videos strikingly demonstrate the residues interacting. In videos comparing the two open-state channels, the M173F (Figure 6—video 2) constitutively open pore looked significantly smaller (F171 points toward the center of the pore to a greater degree) than in the H206C constitutively open pore (Figure 2—video 2). Are there any functional differences in ion selectivity?
