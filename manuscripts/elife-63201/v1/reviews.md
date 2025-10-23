# Peer review - Round 1

Editors:
- Lucie Delemotte, KTH Royal Institute of Technology Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63201.sa1](https://doi.org/10.7554/eLife.63201.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript uses un-natural amino acid incorporation into the GHSR1a to examine the exposure of particular residues to changes in polarity (interpreted as solvent exposure) experimentally followed by molecular dynamics simulation. Considering the body of work done on GPCRs, there are surprisingly few studies that carry out a quantitative one-to-one comparison between experimental and simulations. This manuscript presents a convincing attempt at doing so.

Decision letter after peer review:

Thank you for submitting your article "Concerted conformational dynamics and water movements in the ghrelin G protein-coupled receptor" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Lucie Delemotte as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript uses un-natural amino acid incorporation into the GHSR1a to examine the exposure of particular residues to changes in polarity (interpreted as solvent exposure) experimentally followed by molecular dynamics simulation.

Considering the body of work done on GPCRs, there are surprisingly few studies that attempt a quantitative one-to-one comparison between experimental and simulations. This manuscript presented an interesting attempt at doing so. However, the manuscript asks the reader to accept a substantial amount of work that has either obscure, or superficial methods, little supporting data and significant normalization, making it difficult to fully judge its merits.

Essential revisions:

Related to experiments:

1) Please address the functionality of the expressed, refolded and MSP incorporated GHSR1a. Could the authors please provide original Coomassie stained gels and size exclusion chromatography traces that support their purification and re-incorporation of GHSR1a into the MSP scaffold? The authors report that they have expressed GHSR1a in bacteria then unfolded and refolded this protein, the reviewers are not aware of any other GPCR for which this has been successfully performed, indeed the structural paper that the authors discuss (below), uses a thermostabilized GHSR1a expressed in insect cells in order to obtain crystallizable protein. Additionally, the below paper uses a thermofluor assay to demonstrate the stabilization of their construct. The thermofluor assay, by its nature, indicates that GHSR1a does not spontaneously refold.

Shiimura Y, Horita S, Hamamoto A, Asada H, Hirata K, Tanaka M, Mori K, Uemura T, Kobayashi T, Iwata S, Kojima M. Structure of an antagonist-bound ghrelin receptor reveals possible ghrelin recognition mode. Nat Commun. 2020 Aug 19;11(1):4160. doi: 10.1038/s41467-020-17554-1. PMID: 32814772; PMCID: PMC7438500.

2) As evidence of the functionality of the refolded, purified and MSP incorporated GHSR1a the authors provide a FRET competition binding assay. There is insufficient explanation of this assay for this to be reproduced by another group. In the method the authors indicate that the GHSR1a is labelled at the N-terminus with Lumi-4 Tb NHS. NHS esters typically react with any primary amine, in the authors methods they have the purified GHSR1a in a 25 mM Tris buffer, where the Tris would be expected to preferentially react with the Lumi-4 Tb NHS, the GHSR1a is also incorporated into MSP, which has an N-terminus and both proteins have a number of lysine residues where the Lumi-4 Tb NHS would be expected to react with the epsilon amino group. Perhaps there are some significant details missing from their methods that might enlighten this? In any case, could the authors please provide their in-gel fluorescence (or alternative analysis such as mass spectrometry) that demonstrates specific labelling of GHSR1a (and not MSP) on the N-terminus (and not on lysine side chains)? This assay uses a dy647 labelled ghrelin peptide, could the authors please provide details of how the labelling was performed and either HPLC of mass spec data for the resulting labelled reagent? The cited reference (19) does not appear to contain this reagent, whereas the cited reference (33) does contain a "red-ghrelin" where no details about the chemical composition are readily available. The published affinity of ghrelin for GHSR1a is 400 pM (https://www.guidetopharmacology.org/GRAC/ObjectDisplayForward?objectId=246), the authors need to specifically address why the reported affinity in their assay (Figure 1B) appears to be approximately 250 fold lower at ~100 nM? Could the authors also please provide the original, non-normalised FRET data so that the reader can understand the window for this assay along with a specificity control such as Lumi-4 Tb NHS labelled empty MSP nanosdiscs?

3) In figure 1C the authors provide further evidence for functionality of their purified GHSR1a using a GTP turnover assay. The authors need to provide the full details of how the Galpha/β/γ heterotrimer were expressed and purified for this assay. Please include details of which particular isoform and species each G protein subunit is from, the expression system and how they were purified. A representative Coomassie stained gel that demonstrates stoichiometric equivalence of the subunits in the purified complex should also be supplied. The references provided for this assay to not appear to relate to a GTP depletion style assay as appears to be described here. Could the authors also please describe how 0% was defined for the assay and the relative concentrations of GHSR1a and G proteins heterotrimer that were added to the reactions? The authors show apparent differences in bound GTP in this assay, could they please provide a statistical analysis for these differences?

Related to simulations:

1) Driving large structural changes fast is risky, and the reviewers were not convinced the water populations had equilibrated. Indeed, forces to enhance the sampling were applied along each PC separately. Since these PCs represent a linear decomposition of the overall family-wide conformational change, it didn't appear wise to enhance the sampling along them: linear decomposition of the movement could in principle result in very non-physical motions. Can the authors provide the readers with a supplementary figure showing the comparison between the starting and the 2 end structures, as well as the PDBs of the resulting structures so their quality can be checked?

Relatedly, the mix of active-like and inactive-like structures used in the PCA to derive the biasing forces is expected to have a major effect. The authors need to explicitly list (in the supplement) the structures used, and categorize them by activity state and preferably by GPCR family as well. The first principle vector probably point more or less along the path between inactive and active, but it would be nice to check this.

2) The reviewers also asked for a clearer rationalization of why the authors picked this sampling strategy as opposed to (1) building models of the ghrelin receptor in different states and simulating them or (2) enhancing the sampling using a non-linear approach. Ultimately, what do we learn from the fact that PC1 is the most compatible with the experimental data, given that the overall motion is a combination of all the PCs? It would be wise to replicate the results with a more standard MD simulation protocol to rule out artefacts from this choice of enhanced sampling methods.

3) Additionally, the methods section was unclear about several aspects:

a) it is unclear as to how many replicates were done for each mode: if it's a single replicate for each mode, no conclusion could be drawn about the hydration. To have any confidence in the result, the reviewers would want to see the simulations rerun many times (at least 10x, perhaps more depending on how variable the answer is), preferably starting from different structures within the equilibrated ensemble.

b) Which state does the original model represent? Can the comparison to the recently published structure be more thorough than simply showing a Calpha(?) RMSD (Figure S8)? Are the enhanced sampling MD carried out in presence or absence of ligand and why? Finally the method section as well as the Results section explaining the enhanced sampling protocol should be clarified such that it is not necessary to read the original paper explaining the method to understand.

c) Many key details of the simulations are missing: number of lipids, number of waters, electrostatics method (as written, it sounds like they didn't use Ewald, which would be a huge problem).

d) There is no discussion of statistical convergence. The simulations are very short by today's standards, and the reviewers saw no reason to assume the protein has stopped systematically changing after 300-350 ns (given the uncertainty of starting from a homology model), let alone begun actually sampling. The only evidence is Supp Figure 5, which shows the RMSD is still increasing, while nothing at all is shown for the mutants.

e) As it stands, too many details are missing for these calculations to be repeated. Please collect and document all of the scripts used (building the system, running, and analyzing) and put them either into the supplementary info or better yet into a separate repository (e.g. GitHub, zenodo, etc).
