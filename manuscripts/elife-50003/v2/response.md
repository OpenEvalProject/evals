# Author response - Round 1

Authors:
- Edward A Partlow ([ORCID: 0000-0001-5513-088X](https://orcid.org/0000-0001-5513-088X))
- Richard W Baker ([ORCID: 0000-0003-1136-6000](https://orcid.org/0000-0003-1136-6000))
- Gwendolyn M Beacham ([ORCID: 0000-0001-7158-6887](https://orcid.org/0000-0001-7158-6887))
- Joshua S Chappie ([ORCID: 0000-0002-5733-7275](https://orcid.org/0000-0002-5733-7275))
- Andres E Leschziner
- Gunther Hollopeter ([ORCID: 0000-0002-6409-0530](https://orcid.org/0000-0002-6409-0530))

## Response text

DOI: [10.7554/eLife.50003.032](https://doi.org/10.7554/eLife.50003.032)

Overall, the reviewers would be in favor of presentation of the story in eLife if you are able to address the concerns of reviewer #2. After carefully evaluating your data he wrote, "I think the authors did an excellent job interpreting their density, but their maps are not so easy to interpret. The challenge in assigning the phospho-Thr156 position, in particular, arises because there is a big gap in the EM map that breaks the connectivity. The authors modeled up to Ser140 for AP-2 mu, but then the density washes out completely, and the authors couldn't resume modeling until ~Gln154. This assignment looks like a good guess because there are three "landmark" residues further down the chain that fit the density well for a ~3A map: Trp161, Arg162, and Try168. In summary, because their map is discontinuous, it is hard to be confident in the register of their atomic model. Nevertheless, their model is parsimonious and a very good guess, based on the fit-to-density and spacing between Trp161, Arg162 and Tyr168. My recommendation is that they tackle this issue head-on and use clearer figures to illustrate how the landmark residues support their decision to resume modeling the chain at Gln154.

We agree with the reviewer that building the AP2-NECAP interface, and in particular the mu pT156 residue, is vital to our understanding of NECAP function. We acknowledge that how we defined the register of the linker region should be clarified. As suggested by the reviewers, we have added an additional supplementary figure (Figure 1—figure supplement 3) that specifically highlights how we built the mu linker. This shows the docking of the AP2 crystal structure and the 5 residues we built into the new density in our cryoEM map.

In summary, the register of the mu linker is built from an earlier crystal structure of AP2 (PDB 2VGL). This structure is highly congruent with our pAP2-NECAP cryoEM map (Figure 1—figure supplement 2). Additionally, AP2 has been crystallized many times (PDB 2VGL, PDB 2XA7, PDB 2JKR, PDB 4UQI) and all of these models have an identical register in the mu linker region (residues 159-168). Thus, we are confident in the register of mu starting at residue I159. To build our model of the phosphorylated mu linker, we only had to build Q158 and G157 to reach the critical pT156 residue. We hope we have shown this clearly in our new figure (Figure 1—figure supplement 3). We have also added text to the manuscript to clarify these points and direct readers to the new figure.

Results: “The register leading up to this new density is based on a previous crystal structure (PDB 2VGL), and is confirmed by the positions of several landmark residues near T156 that fit the density well. A detailed schematic for building the critical T156 residue in our model is shown in Figure 1—figure supplement 3.”

My other comments may be harder to address. Given the uncertainty around the modeling of Thr156, their combination of protease accessibility, worm fitness, localization microscopy, and genetic suppressors, altogether, leaves some room for doubt.”

We agree that the varying effect of our mutants across our assays is potentially confusing. We have added language in the main text to clarify this point.

Results: “A bona fide interface mutant should reduce the function of NECAP in multiple assays, but not necessarily to the same degree in every assay. This is because each assay exhibits a different linear range, and point mutations may affect C. elegans and vertebrate proteins differently.”

Results: “It is worth noting that mutation of R112 did not fully suppress the fitness defect, and thus would likely not have been isolated from our genetic screen. Additionally, chemical mutagenesis favors cytosine to thymine DNA transitions, thus disfavoring charge reversal of R112.”

“Finally, the use of 2D cryoEM class averages to support their claim of an induced open state does not convince me. If they have an open state in solution due to interactions with polyanions, they should be able to resolve it in 3D, not just in 2D."

3D reconstructions of open AP2 complexes in the presence of DNA oligo are shown in Figure 4—figure supplement 1B. Unfortunately, incubation with DNA causes AP2 complexes to have an extreme preferred orientation in the grid, likely due to exposed hydrophobic regions that interact with the air-water interface. This severely limits the resolution of 3D reconstructions. Nonetheless, we can resolve 3D complexes to 7-10 Å resolution, sufficient to distinguish open and closed complexes.

We have added a new panel to Figure 4—figure supplement 1 which quantifies the 3D classification of complexes into open or closed states and corroborates the results obtained using analysis of 2D classes. The following details were added to the manuscript, and clarifying changes were made to “2D and 3D classification of ‘open’ versus ‘closed’ AP2 complexes” in the “Quantification and Statistical Analysis” section.

Results: “Similar values are calculated when 3D classification is used (Figure 4—figure supplement 1C).”

Method details: “After this initial cleaning step, each particle set was randomly split into 10 subsets and subjected to 2D and 3D classification. […] Quantification of particles in the ‘open’ vs. ‘closed’ conformation is described in the following section.”

Figure 4—figure supplement 1 legend: “(C) Quantification of 3D classification. Four datasets were analyzed and the percentage of particles that classified into open or closed 3D classes were quantified and plotted.”

We would welcome a revised manuscript that addresses these issues and/or clarifies the conclusions so that there is no confusion for readers. We hope you will find these comments constructive, and I include the details to help guide your revision process.

Thank you for including the detailed reviewers comments, which we have found helpful in clarifying and improving our manuscript, especially the Discussion. Below is our response to specific reviewer comments.

We have added a paragraph to the Discussion to better explain our model figure, specifically the open AP2-NECAP complex we propose for which we have not resolved a 3D structure. This complex is poorly behaved in solution, and we have been unable to produce concentrated samples for cryo-EM. In addition, micrographs of grids prepared using low concentration samples have not produced classifiable particles. Nonetheless, we believe there is sufficient evidence to propose this structure and place it early in our model.

Discussion: “The model in Figure 7 depicts NECAP first interacting with an open, unphosphorylated AP2 complex through the NECAPEx domain. […] A priming interaction of NECAPEx with activated AP2 is consistent with these observations; initially, NECAP is not competent to inactivate AP2, but is poised to do so later in the cycle, after phosphorylation (Figure 7C).”

We have also added several sentences later in the Discussion to address the unanswered questions of when and where NECAP acts, how NECAP detaches from AP2, and how AP2 becomes dephosphorylated.

Discussion: “The results of this study do not distinguish whether NECAP acts early in endocytosis to promote productive pit formation by limiting aberrant events, or late in the endocytic cycle to uncoat AP2 and allow the complex to initiate new pits. […] It remains to be determined whether NECAPPHear must disengage prior to dephosphorylation, or whether a phosphatase plays a role in NECAP removal from closed complexes.”

We clarified our choice of using NECAP2 for our in vitro experiments.

Results: “While there are two paralogues of NECAP in vertebrates, we have previously shown that they function equivalently to bind phosphorylated and open AP2 complexes in vitro and rescue loss of NECAP in C. elegans (Beacham et al., 2018). In this work, we use human or mouse NECAP2 for all experiments because of their ease of purification and stability.”

We thank the reviewers for pointing us towards reports of inherited NECAP1 mutations associated with human or canine diseases. While these pathogenic mutations in NECAP are exciting, it is difficult to interpret these mutations in the context of this work. The human variants appear to result in loss of NECAP expression, and the missense mutation observed in Giant Schnauzer dogs is outside the PHearEx region of NECAP that we identified as the minimal functional region in our assays and visualized in our cryo-EM structures.
