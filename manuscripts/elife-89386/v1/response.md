# Author response - Round 1

Authors:
- Masha Karelina ([ORCID: 0000-0003-1880-4536](https://orcid.org/0000-0003-1880-4536))
- Joseph J Noh
- Ron O Dror ([ORCID: 0000-0002-6418-2793](https://orcid.org/0000-0002-6418-2793))

## Response text

DOI: [10.7554/eLife.89386.2.sa3](https://doi.org/10.7554/eLife.89386.2.sa3)

We thank the reviewers and editor for their careful evaluation of our manuscript, and we appreciate their favorable assessment of our work. Below, we clarify a few points concerning the relationship between our study and previous studies evaluating ligand docking to protein models.

As reviewer 2 correctly notes, several previous assessments of AF2 models have simply excluded templates above a sequence identity cutoff when using AF2 to predict structures. Such AF2 predictions are still informed by all structures in the PDB before April 30, 2018, because these structures were used to train AF2—that is, to determine the tens of millions of parameters (“weights”) in the AF2 neural network. Machine learning methods nearly always perform better when evaluated on the data used to train them than when evaluated on other data. For this reason, we consider AF2 models only for proteins whose structures were not used to train AF2—that is, for proteins whose structures were not available in the PDB before April 30, 2018.

Previous papers (including Beuming and Sherman, 2012, https://doi.org/10.1021/ci300411b) have shown a clear correlation between the binding pocket RMSD of a protein model and pose prediction accuracy based on that model. Our main findings are unexpected in light of these previous reports: we find that AF2 models yield pose prediction accuracy similar to that of traditional homology models despite having much better binding pocket RMSDs, and that AF2 models yield substantially worse pose prediction accuracy than experimentally determined structures with different ligands bound despite having similar binding pocket RMSDs.

Reviewer 2 also correctly notes that previous papers have described AF2 models as “apo models,” because these models do not include coordinates for bound ligands. As noted by the AF2 developers (e.g., https://alphafold.ebi.ac.uk/faq), however, AF2 is designed to predict coordinates of protein atoms as they might appear in the PDB, and AF2 models are thus frequently consistent with structures in the presence of ligands even though those ligands are not included in the models. GPCR structures in the PDB, including those used to train AF2, nearly always contain a ligand in the orthosteric binding pocket. An AF2 model of a GPCR should thus not be viewed as an attempt to predict the GPCR’s structure in the unliganded (apo) state.

Finally, we did not apply flexible docking in this study because previous work has found that standard flexible docking protocols typically improve pose prediction performance only when given prior information on which amino acid residues to treat as flexible. For example, previous studies that performed successful flexible docking to AF2 models generally used prior knowledge of the ligand’s experimentally determined binding pose to identify the residues to treat as flexible.
