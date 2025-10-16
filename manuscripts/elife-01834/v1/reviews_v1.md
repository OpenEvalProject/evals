# Peer review - Round 1

Editors:
- Benoit Roux, University of Chicago , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01834.025](https://doi.org/10.7554/eLife.01834.025)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Single Molecule FRET Reveals Pore Size and Opening Mechanism of MscL” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, John Kuriyan, and 2 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

In this paper the authors use single-molecule FRET measurements (smFRET) to analyze the degree and nature of the opening of a mechanosensitive channel in a lipid bilayer environment. The smFRET measurements permitted the authors to estimate the change in the distance between donors and acceptors from the closed to open states. To quantitatively investigate in detail how the MscL channel opens, the authors developed a computational model for the open state, starting from the crystal structure of MscL in the closed state (PDB: 2OAR) employing the measured residue movements. For this purpose, MD simulations with distance constraints were performed. This is an impressive piece of work because it analyzes the channel in a lipid bilayer environment rather than in detergent micelles, and because the authors use photobleaching to ensure that they are studying channels with one donor and one acceptor, thus avoiding complications that might otherwise undermine the analysis. The importance of the work arises because there is no crystal structure for an open form of these channels, and so the paper potentially fills in major gaps in understanding.

Major concerns:

1) It is emphasized that the modeled open structure resulting from the molecular dynamics satisfies all the distance constraints derived from their smFRET experiments. But this statement leaves out completely any uncertainty due to the size of the FRET probes themselves. It is stated that, for each measured residue, ten virtual springs were placed, five springs between identical residues from adjacent monomers and five springs between identical residues from non-adjacent monomers. The equilibrium lengths of the springs were chosen by adding the distance changes measured from smFRET to the equilibrium distances seen in the closed state. However, it is not specified between which atoms the virtual spring are introduced.

2) The discussion of the maximum possible errors in R0 is extensive, but mainly concerns the experimental FRET aspects of the problem. However, there are additional difficulties in trying to convert the measurements into a structural model. In fact, converting the changes in distance into a structural model is not straightforward. The channels were labeled with Alexa Fluor 488 (AF488) and Alexa Fluor 568 (AF568). The smFRET distances report the donor-acceptor distances. To model this correctly, it is necessary to account for the size and length of the probes.

3) The authors should discuss, on the structural level, the expected effect of inserting a molecule of the size of AF488 or AF568.

4) The binding of one donor and one acceptor molecule per pentamer will break the five-fold symmetry. In what way does this affect the geometric construction in Figure 5B?

5) Can the activity of the mutants from Figure 6 be explained/rationalized with the final model?
