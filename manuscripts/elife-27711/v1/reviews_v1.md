# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27711.024](https://doi.org/10.7554/eLife.27711.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Activation of a Class B GPCR by peptide hormones: structural insight from live cells" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and three reviewers, one of whom, Yibing Shan (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity:.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Aiming to elucidate the structural changes associated with activation of Class-B GPCRs, this work used molecular dynamics simulations guided by extensive crosslinking data to construct structural models of corticotropin-releasing factor receptor type 1 (CRF1R) bound with an agonist or with an antagonist. The models suggest a conserved hinge motion and helix tilting in the vicinity of the ligand binding site.

Essential revisions:

MD simulations showed that the "compact" TMD conformation is more optimal than the "wide" conformation for CRF1R interactions with the antagonist. Movements of the extracellular parts of helices VI and VII accounts for the different conformational changes of TMD and may be a key feature of class B GPCR activation. Thus, MD simulation is critical to draw the activation mechanism of class B GPCR by peptide hormones. But the time-scale of nine MD simulations for different systems are inconsistent (Figure 7). As receptors are flexible without distance restraints, in the revision the authors should consider extend run2 and run3 to at least 1-us to provide more convincing results.

The reviewers notice that the agonist and the antagonist models are virtually identical at the cytoplasmic side. This is unlikely to be correct because conformational change at and near the ligand binding site has to be propagated to cytoplasmic side to pass the signal to downstream G proteins. Likely this is due to the simulations' failure in reaching a global equilibrium. In the revision, the models should be adaquated "relaxed" by unrestrained simulations. Other means such as slow mode analysis or coarse-grained simulation may also be appropriate to address this concern. The conformational difference in the cytoplasmic side should be clarified and discussed in the functional context.
