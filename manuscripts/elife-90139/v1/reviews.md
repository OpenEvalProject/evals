# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90139.3.sa0](https://doi.org/10.7554/eLife.90139.3.sa0)

This valuable study reports multi-scale molecular dynamics simulations to investigate a class of highly potent antibodies that simultaneously engage with the HIV-1 Envelope trimer and the viral membrane. The work provides insights into how broadly neutralizing antibodies associate with lipids proximal to membrane-associated epitopes to drive neutralization. After extensive revision, the level of evidence is considered solid, although a quantitative assessment of the underlying energetics remain difficult to obtain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90139.3.sa1](https://doi.org/10.7554/eLife.90139.3.sa1)

Previous experimental studies demonstrated that membrane association drives avidity for several potent broadly HIV-neutralizing antibodies and its loss dramatically reduces neutralization. In this study, the authors present a tour de force analysis of molecular dynamics (MD) simulations that demonstrate how several HIV-neutralizing membrane-proximal external region (MPER)-targeting antibodies associate with a model lipid bilayer.

First, the authors compared how three MPER antibodies, 4E10, PGZL1, and 10E8, associated with model membranes, constructed with two lipid compositions similar to native viral membranes. They found that the related antibodies 4E10 and PGZL1 strongly associate with a phospholipid near heavy chain loop 1, consistent with prior crystallographic studies. They also discovered that a previously unappreciated framework region between loops 2-3 in the 4E10/PGZL1 heavy chain contributes to membrane association. Simulations of 10E8, an antibody from a different lineage, revealed several differences from published X-ray structures. Namely, a phosphatidylcholine binding site was offset and includes significant interaction with a nearby framework region. The revised manuscript demonstrates that these lipid interactions are robust to alterations in membrane composition and rigidity. However, it does not address the reverse-that phospholipids known experimentally not to associate with these antibodies (if any such lipids exist) also fail to interact in MD simulations.

Next, the authors simulate another MPER-targeting antibody, LN01, with a model HIV membrane either containing or missing an MPER antigen fragment within. Of note, LN01 inserts more deeply into the membrane when the MPER antigen is present, supporting an energy balance between the lowest energy conformations of LN01, MPER, and the complex. These simulations recapitulate lipid binding interactions solved in published crystallographic studies but also lead to the discovery of a novel lipid binding site the authors term the "Loading Site", which could guide future experiments with this antibody.

The authors next established course-grained (CG) MD simulations of the various antibodies with model membranes to study membrane embedding. These simulations facilitated greater sampling of different initial antibody geometries relative to membrane. These CG simulations , which cannot resolve atomistic interactions, are nonetheless compelling because negative controls (ab 13h11, BSA) that should not associate with membrane indeed sample significantly less membrane.

Distinct geometries derived from CG simulations were then used to initialize all-atom MD simulations to study insertion in finer detail (e.g., phospholipid association), which largely recapitulate their earlier results, albeit with more unbiased sampling. The multiscale model of an initial CG study with broad geometric sampling, followed by all-atom MD, provides a generalized framework for such simulations.

Finally, the authors construct velocity pulling simulations to estimate the energetics of antibody membrane embedding. Using the multiscale modelling workflow to achieve greater geometric sampling, they demonstrate that their model reliably predicts lower association energetics for known mutations in 4E10 that disrupt lipid binding. However, the model does have limitations: namely, its ability to predict more subtle changes along a lineage-intermediate mutations that reduce lipid binding are indistinguishable from mutations that completely ablate lipid association. Thus, while large/binary differences in lipid affinity might be predictable, the use of this method as a generative model are likely more limited.

The MD simulations conducted throughout are rigorous and the analysis are extensive, creative, and biologically inspired. Overall, these analyses provide an important mechanistic characterization of how broadly neutralizing antibodies associate with lipids proximal to membrane-associated epitopes to drive neutralization.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90139.3.sa2](https://doi.org/10.7554/eLife.90139.3.sa2)

In this study, Maillie et al. have carried out a set of multiscale molecular dynamics simulations to investigate the interactions between the viral membrane and four broadly neutralizing antibodies that target the membrane proximal exposed region (MPER) of the HIV-1 envelope trimer. The simulation recapitulated in several cases the binding sites of lipid head groups that were observed experimentally by X-ray crystallography, as well as some new binding sites. These binding sites were further validated using a structural bioinformatics approach. Finally, steered molecular dynamics was used to measure the binding strength between the membrane and variants of the 4E10 and PGZL1 antibodies.

The use of multiscale MD simulations allows for a detailed exploration of the system at different time and length scales. The combination of MD simulations and structural bioinformatics provides a comprehensive approach to validate the identified binding sites. Finally, the steered MD simulations offer quantitative insights into the binding strength between the membrane and bnAbs.

While the simulations and analyses provide qualitative insights into the binding interactions, they do not offer a quantitative assessment of energetics. The coarse-grained simulations exhibit artifacts and thus require careful analysis.

This study contributes to a deeper understanding of the molecular mechanisms underlying bnAb recognition of the HIV-1 envelope. The insights gained from this work could inform the design of more potent and broadly neutralizing antibodies.
