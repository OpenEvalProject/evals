# Peer review - Round 1

Editors:
- Rina Rosenzweig, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84645.sa0](https://doi.org/10.7554/eLife.84645.sa0)

This important interdisciplinary study substantially advances our understanding of the prolactin receptor interactions with the membrane lipids and the effect of these interactions on cell signaling. The authors use a combination of state-of-the-art NMR structural analysis, simulations, and cellular assays to provide compelling experimental evidence for protein complexes being regulated by IDR-membrane interactions. The work will be of broad interest to structural biologists and biochemists, and the results presented herein are likely relevant for other non-tyrosine kinase receptors.


---

# Peer review - Round 1

Editors:
- Rina Rosenzweig, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84645.sa1](https://doi.org/10.7554/eLife.84645.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The prolactin receptor scaffolds Janus kinase 2 via co-structure formation with phosphoinositide-4,5-bisphosphate" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Amy Andreotti as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Frauke Gräter (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The introduction needs to be updated to include the motivation for focusing specifically on LID1. In addition, more detailed descriptions of the methodologies used need to be included, specifically how these have been previously successfully applied by researchers to study equivalent membrane systems.

2) Please provide a better connection between the JAK2-PRLR complex conformational states and their functional relevance. This is an important point, as the majority of the simulation part of the paper centers on suggesting different states of the PRLR-JAK2 complex, and their hypothesized functional relevance is presented as a major result, yet not verified by experiments.

3) The connection between simulations and mutational study is not very direct. It is not clear that the mutants can distinguish between the effects of PRLR-PIP2 interaction or PRLR-JAK2 interaction, yet this conclusion is still drawn from the data.

4) Please provide some evidence (from experiments or simulations) regarding the role of PIP3 interactions. Currently (very strong) experimental evidence is provided only for PIP2, showing it to be an important regulator, while no results are provided for PIP3, despite being included in the final model.

5) The conclusions drawn from the mutagenesis study (lines 547-555) are not directly supported by data. There is only a partial correlation between PRLR membrane localisation and STAT5 activation, and this is insufficient to attribute the unexplained part of the STAT5 activation to PRLR-JAK2 interactions without further studies.

6) Based on the method section, the JAK2-FERM-SH2 CG-MD simulations are based on Martini 2.2 forcefield. If it is the case, the results of the orientation of the protein towards the membrane may be affected, as there can be some underestimations of the aromatics-choline interactions (https://pubs.acs.org/doi/full/10.1021/acs.jctc.9b01194). This issue seems to be corrected in the new Martini3 version. Would it be possible to run a few control simulations using Martini3 to compare with Martini2.2 results and see if the protein orientation is affected? Otherwise, this limitation should at least be mentioned in the Discussion section.

7) Relatively large chemical shift changes are detected in PRLR res 285-290 upon lipid binding, these need to be discussed.

8) You might want to move some of the main figures to the supplementary data and further emphasize some of the major conclusions (for example Figure 3H and 3I).

Reviewer #1 (Recommendations for the authors):

The data of Figure 5A are explained as changes in peak intensities are the smallest for φ4G mutant. This is not true as K4G shows similar changes, and K4E shows even fewer changes.

Also, the explanation for the increase in intensity with titration to be due to weak binding is also not convincing. Could binding be measured by ITC for example to show indeed that one mutant binds weaker than the other?

Reviewer #2 (Recommendations for the authors):

The study would benefit from a clearer distinction of mutation effects on PRLR-PIP2 interaction or PRLR-JAK2 interaction by designing mutants that only affect one and not the other, if possible. The same applies to the JAK5 activation: experimental evidence is currently lacking.

Also, the connection between simulations and mutant experiments could be more direct:

– CIF motif identified to be involved in PIP2 interaction using NMR and simulation.

– KxK motif 1 (residue ~252) identified in simulation to interact with PIP2.

– KxK motif 2 (residue ~262) not identified in simulation or NMR as PIP2 contact but as a contact point with JAK2 in simulation (Figure 4 figure supplement 1).

– Parts of φ4G contact point with JAK2 in simulation but L252 is part of KxK motif 1.

Finally, the discussion of different conformational states needs to be revisited and refined: which state should be functionally rather switched off, which state switched on, and how is function inferred from the conformations?

Also, experiments/simulations on PIP3 or at least a discussion on how PIP3 interactions can be inferred from the results on PIP2 would strengthen the study (point 5 above).

Reviewer #3 (Recommendations for the authors):

There are a few points that need to be clarified:

1. In the introduction. While the biological context of this work is well explained, the methodological context is not really detailed. It gives the impression that technically speaking, this work is completely new, which is not the case. There are numerous published studies (both in terms of NMR and modelling) studying PIP2 lipids, IDPs, and membrane receptors. Thus, it may be interesting for the reader to see that other research has already been successfully applied to study equivalent membrane systems showing that the authors' strategy is indeed robust.

2. Figure 3 and Figure 3 supplement1: an RSMF analysis of the peptide LID1 would be useful to evaluate its degree of flexibility for each membrane system. It may help better understand how PIP2 lipids may partly structure the peptide.

3. From the method section, it is not clear where the PIP2 CG model is coming from. How this model can be compared with the recent parametrization of PIP2 (https://pubs.acs.org/doi/abs/10.1021/acs.jctc.1c00615)? If the two models are different how this can affect the modelling results?

4. My main concern is related to the JAK2-FERM-SH2 CG-MD simulations (Figure 4). Based on the method section these simulations seem to be based on Martini 2.2 forcefield. If it is the case, the results of the orientation of the protein towards the membrane may be affected as there can be some underestimations of the aromatics-choline interactions (https://pubs.acs.org/doi/full/10.1021/acs.jctc.9b01194). This issue seems to be corrected in the new Martini3 version. Would it be possible to run a few control simulations using Martini3 to compare with Martini2.2 results and see if the protein orientation is affected? Or, at least, mention this limitation in the Discussion section.

Typos and format:

p.6, figure2-A: MD simulations box: K335 needs to be changed to K235.
