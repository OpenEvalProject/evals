# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58621.sa1](https://doi.org/10.7554/eLife.58621.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers and editors recognized that this study is both important and timely. The membrane interaction and self-assembly of the Gag protein is a critical step in viral capsid assembly. This is an area that has received considerable attention over the past three decades, yet much has remained unknown due to the complexity of this interaction. The insights derived from this systematic analysis based on molecular simulation data constitute a significant advance and are likely to foster novel research in this area.

Decision letter after peer review:

Thank you for submitting your article "Binding mechanism of the matrix domain of HIV-1 gag to lipid membranes" for consideration by eLife. Your article has been reviewed by three peer reviewers, whose comments are provided below. The evaluation has been overseen by José Faraldo-Gómez as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and with the Senior Editor. Based on this discussion, we would like to invite you to submit a revised version of your manuscript that convincingly addresses the concerns and questions raised. Please note the reviewers have asked to re-evaluate your revised manuscript before making a final recommendation on whether or not it should be published in eLife. I therefore urge you to give careful consideration to the revisions of the manuscript as well as your response.

Reviewer #1:

This is an important and timely study that describes novel all-atom MD simulations of interactions and structural changes associated with membrane binding by the MA domain of the HIV-1 Gag protein. This is an area that has received considerable experimental, and some computational, attention over the past three decades, yet much remains unknown due to the complexity of the interactions. Voth and co-workers have done a beautiful and systematic job of parameterizing plasma membrane interactions with MA and then examining the influence of the membrane constituents (Phosphatidylinositol-4,5-bisphosphate, phosphatidyl serine, cholesterol, and others) on membrane binding. They conducted MD trajectories at timescales (40 us) sufficient to follow insertion of the N-terminal myristoyl group of MA into the membrane, and characterize the influence of up to six membrane constituents known to be important for targeting MA specifically to the plasma membrane. Interestingly, all simulations were initiated with the protein in the "myristate sequestered" conformation, and stable sequestration of the myristate chain within the membrane only occurred for membranes homologous to the plasma membrane. Their studies also reveal how MA-MA interactions, known to be important for recruitment of the viral envelope protein, promote reorganization of inner-leaflet membrane constituents.

This appears to me to be a comprehensive and well-executed study. It should be of broad interest to the biomedical community, particularly to groups interested in HIV and protein-membrane interactions. My only recommendation is that the Discussion section include some speculation on the recently discovery by Bieniasz and co-workers that, in the cytoplasm, the MA domain is bound to tRNAs (predominantly tRNALys), and by Summers and co-workers that tRNA binding is tight enough to inhibit binding to liposomes. I'm certainly not suggesting that additional experiments with tRNAs need to be conducted for this paper. But it would be good for the readers to know that, although these studies provide fundamental new insights into the changes and interactions that must happen during virus assembly, the actual mechanism in cells is probably more complex.

Also, it would be really nice if the authors could provide a supplementary video showing one of their trajectories showing MA docking with the membrane (the biologically relevant conformation) and the myristate transitioning from the protein pocket to the membrane.

Reviewer #2:

This paper reports extensive molecular dynamics simulations of the Gag protein interacting with three different membranes: a model of the inner plasma membrane (PM), a cholesterol-free version of the PM, and a lipid raft. It is shown convincingly using unbiased simulations that the myristoylated (Myr) N-terminus of the proteins selectively binds to the PM model. This result and accompanying analysis provides valuable insights into the interactions driving membrane binding, and highlights the importance of selecting appropriate membrane models for such studies. I recommend publication following minor revisions.

I read this paper several times looking for a concise summary-like statement of why Myr preferentially inserts in the inner PM model, but could not find one. Mention is made of PIP2, but the PIP2 concentration is lowest in this model. Cholesterol in critical, but this is included in the raft model. Charge is important, but is it specific are nonspecific interactions of the protein and DOPS? From Supplementary Table 1 the density of the inner PM and raft models appears to be comparable. Is it the replacement of POPE for BSM? Sort this out and write it clearly in the conclusions and the Abstract, don't make readers hunt for it.

Move the Supplementary Table 1 (compositions of the three models) to the main text. It was very hard to follow the arguments in the paper without this table handy. (If there is a space issue, the main text is somewhat wordy and should be easy to trim.) Some other questions/issues with this table:

1) The columns labelled "small" and "large" contain the same numbers of water and ions. Is this a mistake?

2) Include the charge density for each system. What charge is being used for PIP2? Is the + sign in the PIP2 for the chol-free membrane a typo?

3) Let the reader know that the B in BSM stands for behenic acid. (I initially thought it was a misprint of the more common PSM)

4) Perhaps incorrectly I believed that PIP2 is not a component of lipid rafts, or at least the liquid ordered phase. A sentence on the raft composition would helpful.

It would be useful to note studies showing that acyl chains readily insert into numerous membranes. Acyl chains of different RAS insert into liquid ordered phases, liquid disordered phases and the boundaries between them. Hence the interaction of Gag and the PM is special.

Reviewer #3:

In their manuscript "Binding mechanism of the matrix domain of HIV-1 gag to lipid membranes" Monje-Galvan and Voth present extensive simulations (totaling some 40 uses) of the MA domain of the HIV Gag protein interacting with several different model membranes. The membrane interaction and self-assembly of Gag at the inner leaflet is a critical step in viral capsid assembly, which provides a major motivation for the work. The authors compare interaction of the MA domain and insertion (or non-insertion) of its myristoyl anchor in simulations of different model membranes, designed to mimic different subcellular localizations (inner leaflet, raft-like, etc), which is a strength of the work. However, although the technical aspects of the work are sound, the broader implications in terms of mechanism are not clear.

1) What critical new information has been gained regarding capsid assembly, and how does it bear on existing models of assembly? Although there is a good deal of highly technical information in the manuscript, it is never synthesized into a "big picture" for capsid assembly. It is therefore unlikely to find a broad audience, and instead be of interest mainly to the membrane and membrane protein simulation community. What new simulations and experiments do the authors' results and analysis motivate?

2) Although the use of distinct lipid mixtures to compare MA interaction with different membrane regions is overall a strength, the choice of lipid mixtures is not well motivated or explained. There are hardly any lipids like DOPC or DOPS (ie, with identical tails at the sn-1 and sn-2 positions) in mammalian lipidomes. Also, what is the "raft" membrane model supposed to mimic? An inner leaflet raft? If so, on what basis was this particular composition chosen?

3) There is some discussion of Myr insertion as a mechanism to initiate sphingolipid clustering, but this is neither quantified nor discussed in the context of mechanism or function.
