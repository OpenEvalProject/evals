# Peer review - Round 1

Editors:
- Anna Panchenko, Queen's University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104901.3.sa0](https://doi.org/10.7554/eLife.104901.3.sa0)

This valuable study uses AlphaFold2 to guide the structural modelling of different states of the human voltage-gated potassium channel KV11.1, a key pharmacological drug target. Follow-up molecular dynamics and drug-docking simulations, combined with experimental characterization, offer convincing evidence supporting the models. The work shows potential for improving drug potency predictions in ion channel pharmacology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104901.3.sa1](https://doi.org/10.7554/eLife.104901.3.sa1)

Summary:

Ngo et. al use several computational methods to determine and characterize structures defining the three major states sampled by the human voltage-gated potassium channel hERG: the open, closed and inactivated state. Specifically, they use AlphaFold and Rosetta to generate conformations that likely represent key features of the open, closed and inactivated states of this channel. Molecular dynamics simulations confirm that ion conduction for structure models of the open but not the inactivated state. Moreover, drug docking in silico experiments show differential binding of drugs to the conformation of the three states; the inactivated one being preferentially bound by many of them. Docking results are then combined with a Markov model to get state-weighted binding free energies that are compared with experimentally measured ones.

Strengths:

The study uses state-of-the-art modeling methods to provide detailed insights into the structure-function relationship of an important human potassium channel. AlphaFold modeling, MD simulations and Markov modeling are nicely combined to investigate the impact of structural changes in the hERG channel on potassium conduction and drug binding.

Weaknesses:

(1) Selection of inactivated conformations based on AlphaFold modeling seems a bit biased.

The authors base their initial selection of the "most likely" inactivated conformation on the expected flipping of V625 and the constriction at G626 carbonyls. This follows a bit the "Streetlight effect". It would be better to have selection criteria that are independent of what they expect to find for the inactivated state conformations. Using cues that favour sampling/modeling of the inactivated conformation, such as the deactivated conformation of the VSD used in the modeling of the closed state, would be more convincing. There may be other conformations that are more accurately representing the inactivated state. In addition, I am not sure whether pLDDT is a good selection criterion. It reports on structural confidence, but that may not relate to functional relevance.

(2) The comparison of predicted and experimentally measured binding affinities lacks of appropriate controls. Using binding data from open-state conformations only is not the best control. A much better control is the use of alternative structures predicted by AlphaFold for each state (e.g. from the outlier clusters or not considered clusters) in the docking and energy calculations. Importantly, labels for open, closed and inactivated state should be randomized to check robustness of the findings. Such a control would strengthen the overall findings significantly.

(3) Figures where multiple datapoints are compared across states generally lack assessment of the statistical significance of observed trends (e,g. Figure 3d).

The authors have successfully achieved their goal of providing new insights into the structural details of the three major conformational states sampled by the human voltage-gated potassium channel hERG, and linking these states to changes in drug-binding affinities. However, the study would benefit from more robust controls and orthogonal validation. Additionally, the generalizability of the approach remains to be demonstrated.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104901.3.sa2](https://doi.org/10.7554/eLife.104901.3.sa2)

Summary:

Ngo et al. use AlphaFold2 and Rosetta to model closed, open, and inactive states of the human ion channel hERG. Subsequent MD simulations and comparisons with experiment support the plausibility of their models.

Strengths:

Ngo et al. employ various computational methods to enhance AlphaFold2's prediction capabilities for the human voltage-gated potassium channel hERG. They guide AlphaFold2 to explore different protein conformations and states, including its open, closed, and inactivated forms, using targeted templates. Additionally, they applied the Rosetta FastRelax protocol with an implicit membrane to refine the conformation of each residue in the predictions and address steric clashes, along with molecular dynamics (MD) simulations to account for membrane-pore flexibility. The methodology is well-described, and the figures are clear and descriptive.

The authors have addressed some of the concerns raised during the first round of reviews. For instance, to mitigate potential bias in selecting the inactivated conformation, they evaluated conformational variability via backbone dihedral angles at specific residues in the selectivity filter and the drug binding sites. They also evaluated the top representative model from inactivated-state-sampling Cluster 3 (termed "AF ic3"), which was initially excluded. This model is now included in the revised manuscript as Figure S9a, b. MD simulations confirmed that this state could be a potential alternative open-state conformation. The authors also acknowledged the limitation of their study by not incorporating other enhanced sampling methods and AF3.

In the revised manuscript, the authors provided more extensive explanations of their methods. For example, they explained that their approach to template selection was guided by their experience-AlphaFold2 with larger templates often overly constraining predictions to the input structure, reducing its flexibility to explore alternative conformations. In contrast, smaller, targeted fragments increase the likelihood that AlphaFold2 will incorporate the desired structural features while predicting the rest of the protein. They also noted that pLDDT scores are not always reliable for selecting new or alternative conformations, citing proper references. They included a model from cluster 3 of the inactivated-state sampling process, which exhibited lower pLDDT scores to illustrate this further.

Another point raised by the reviewers was the exclusion of the N-terminal PAS domain due to GPU memory limitations and its impact on the study. This omission may overlook the PAS domain's potential roles in gating kinetics and allosteric effects on drug binding. The authors acknowledged these limitations in the main text and highlighted the need for future studies to explore these regions in greater detail. They also alluded to potential future research to address these points. Additionally, they have made some of their analysis scripts and tools available on GitHub as a community resource.

Weakness:

The primary issue with the study is the lack of a general pipeline or strategy that can be universally applied to any system, even if limited to ion channels or membrane proteins. A related paper assessed the conformational variability in voltage-sensing domains (VSDs) by applying both the default MSA depth and a range of reduced MSA depths to enhance conformational diversity (please see https://doi.org/10.1101/2025.03.12.642934). They generated 600 models for 32 members of the voltage-gated cation channel superfamily and demonstrated that AlphaFold2 can predict a range of diverse structures of the VSDs, representing activated, deactivated, and intermediate conformations, with more diversity observed for some VSDs compared to others.

The authors have addressed one of the reviewer's concerns about generalizability by including an example in Figure S14 of the modified text, showing how their approach can be applied to model another ion channel system. However, some outstanding questions remain: Is this method better suited for ion channels or membrane proteins with already solved structures and extensive research available? Can this pipeline be applied to other systems as well? Additionally, how does this method compare to other methods using MSA subsampling and other enhanced AF-based techniques to generate alternative conformations of proteins?
