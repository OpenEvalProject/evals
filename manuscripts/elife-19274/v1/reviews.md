# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19274.028](https://doi.org/10.7554/eLife.19274.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Macromolecular Dynamics, Stability, and Atomistic Interactions in a Bacterial Cytoplasm" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and three reviewers, one of whom, Yibing Shan (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. It should be possible for you to address these issues without running new simulations. Note, also, that the editor asks you to change the title of the manuscript so that it conveys to the reader more clearly what was actually done.

Summary:

This pioneering work simulates a substantial fraction of a bacterial cytoplasm using all-atom molecular dynamics simulations, aiming to elucidate how interactions in a crowded environment affect the stability and diffusion properties of macromolecules. It is a technical feat to construct and to simulate such an enormous all-atom model of more than 100 million atoms. The simulations break new ground of molecular dynamics in terms of system scale. The work shows that, among other findings, protein structural dynamics and ligand binding in the crowded environment differ from diluted solution as theoretically expected and that metabolic enzymes exhibit a tendency to cluster spatially.

Essential revisions:

The reviewers recognize the herculean effort and the groundbreaking nature of this work. To publish this work in eLife, however, the manuscript needs revisions in several aspects:

1) The simulation lengths of tens of nanoseconds are too short for the system to equilibrate and to have a chance to depart significantly from the initial model. Different macromolecules will, on average, experience different environments which will affect their behavior (indeed, the authors observe wildly different behaviors for different copies of the same molecules). Given the very small diffusion coefficients involved (~1*10-3 A2/ps for macromolecules and ~1*10-2 A2/ps for ions), the macromolecules move on average by a few angstroms to a few nanometers during the entire simulation. Given the size of the systems 50-100 nm, they are largely "frozen" in such a short timescale. Ideally, the simulation lengths should be of micro- to milliseconds, allowing enough time for the macromolecules to diffuse the entire length of the simulation box. The reviewers understand that such simulation length is impossible even with today's largest supercomputers, but the manuscript needs to acknowledge this important limitation of the work and discuss in-depth its implications to help the readers correctly interpret the results.

2) The manuscript also needs to discuss the potential issues of inaccuracy of the models the simulations are initiated from. For example, the fact that many of the protein structures the system entails are homology models with only short equilibration (20 picoseconds) will likely have consequences for the findings concerning protein stability. It is difficult to assess the "stability" of these protein models from the RMSD traces, in particular on such short timescale. It is likely that some of these models would undergo substantial unfolding and rearrangements on longer timescales as suggested by the relatively large RMSDs from the stating structure, even when flexible regions are omitted. These potential issued should acknowledged and analyzed to the extent that is feasible.

3) More details should be given concerning how non-specific intermolecular interactions affect protein conformational dynamics. It will be useful to follow one or two protein molecules as examples, with a focus on the intermolecular interactions they experienced in the course of the simulation.

4) The mechanism by which inter-biomolecular interactions affect protein ligand binding is obscure from the manuscript. Why is ATP distribution on the ACKA molecule differs in cytoplasm and in aqueous solution? The reason for this somewhat surprising observation needs further Discussion.

5) The manuscripts and the potential impact of this work would benefit if the authors can make an effort to improve the text. The conclusions need to be clearly stated in the Abstract and the Discussion. For instance, in the Abstract, the authors write about nonspecific interactions 'affecting' several properties. The reader needs to know what is affected, by how much and compared to what. This lack of clarity is a general feature. Similarly, the authors write about 'stability' in the first paragraph of the subsection “Native state stability of biomolecules in cellular environments”, but never define it.

The authors write about decreased distances between proteins in their model, but the reader needs to know, 'compared to what?' For a baseline, the authors could refer to Spitzer and Poolman paper: 2005 Electrochemical structure of the crowded cytoplasm. Trends Biochem Sci 30:536.
