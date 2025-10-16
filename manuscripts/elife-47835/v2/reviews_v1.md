# Peer review - Round 1

Editors:
- Daniel Zilberman, John Innes Centre United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47835.026](https://doi.org/10.7554/eLife.47835.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Epigenetic silencing of a multifunctional plant stress regulator" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Daniel Zilberman as the Reviewing Editor, and the evaluation has been overseen by Christian Hardtke as the Senior Editor. The other reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Zander et al. present a detailed analysis of the ethylene-insensitive ein6-1 mutant, which, fascinatingly, turns out to carry mutations in both the REF6 H3K27me3 demethylase and a putative subunit (EEN) of the INO80 chromatin remodeling complex. Both mutations are required for the ethylene insensitivity phenotype, which apparently results from silencing of EIN2 in the double mutant. The authors show that both H3K27me3 and H2A.Z accumulate at the EIN2 locus in the double mutant, suggesting that REF6 and INO80 cooperate to prevent polycomb silencing of EIN2. Interestingly, they also present evidence that this silencing is initiated at an intron in the 5' UTR of the EIN2 gene. Although the precise mechanism underlying this phenomenon remains to be elucidated, the results are very exciting in that they shed light on the control of a central player in the ethylene response and add further depth to the recently identified connection between H2A.Z deposition and Polycomb silencing.

Essential revisions:

1) The interaction between H2A.Z and H3K27me3 was recently described in Arabidopsis, as the authors note: "H2A.Z and H3K27me3 are functionally linked and both repress transcription in Arabidopsis (Carter et al., 2018, Coleman-Derr and Zilberman, 2012)." However, the authors do not mention the work by Carter et al. further, including in the discussion of how H3K27me3 and H2A.Z might interact (Discussion). Carter et al. show that H2A.Z deposition in gene bodies is dependent on the H3K27me3 methyltransferase CLF, and H3K27me3 is promoted by the H2A.Z deposition factor PIE1. They propose a model for mutual reinforcement, where H2A.Z incorporation promotes H3K27me3 and H3K27me3 stabilizes H2A.Z by fostering nucleosome retention. Importantly, the work by Carter et al. indicates that the relationship between H3K27me3 and H2A.Z is quite general and not confined to a few genes that include EIN2. The authors should discuss their findings in light of this work, including in the model in Figure 5C. The integration of work by Carter et al. should also clarify the model, as the "blocking" connectors from EIN6 to SWR1 and from INO80 to PRC2 are not apparently supported by sufficient data. The authors may also wish to cite Dong et al., 2012, which noted an enrichment of H2A.Z associated with H3K27me3.

2) The authors' results and those of Carter et al. indicate that K3K27me3 should be lost at EIN2 in ref6;een;pie1 triple mutants. The authors should evaluate this, as the loss of K3K27me3 at EIN2 is an important prediction of their model.

3) The H2A.Z antibody used in this study is a commercial preparation raised against the full-length budding yeast H2A.Z protein. The WT and pie1 ChIP-seq data strongly suggest that this antibody recognizes Arabidopsis H2A.Z, but given the importance of the data for the paper's conclusions, validation of the antibody and the ChIP-seq data is important. At minimum, please include a comprehensive comparison of the H2A.Z ChIP-seq data to one or more of the publicly available Arabidopsis ChIP-seq datasets derived from well-validated H2A.Z antibodies. A western blot using the antibody on WT and pie1 chromatin fractions would also be helpful.

4) The reviewers expressed concerns about the re-ChIP data-set. Visualization of these data (as provided in the authors' link) indicates that they are not very convincing and that the IgG control is not clean. Since the data are not extensively integrated into the major conclusions, we suggest removing them. Alternatively, please include an analysis that demonstrates the validity of these data.

5) Related to point 4, the EEN-ChIP dataset did not show a convincing signal to noise ratio, despite the great number of peaks identified by SICER. In Figure 3A, the authors display a profile of enrichment over background at the EIN2 locus, in which the depletion values are cut off. These values would allow an estimation of the signal to noise ratio and probably indicate that the ChIP signals for EEN oscillate around the background. There are potential reasons for EEN's weak enrichment over the background, e.g. if the INO80 complex is distributed with low affinity throughout the genome, associates very transiently with target regions or simply, more specific to EEN, this component, as part of a large protein complex may not be sufficiently cross-linked to DNA. The EEN ChIP-seq data require proper visualization and an indication of the significantly enriched regions within the graph for EIN2. The very weak binding of both EEN and REF6 at EIN2 should also be discussed.

6) In Figure 4C and D, it would be useful to see these data as heatmaps in addition to average plots. Also, are these genes direct targets of INO80 and do they increase in expression in response to ethylene? Another potential interpretation is that INO80 is needed for the activation of these genes, and the loss of H2A.Z is really an effect of increased transcription.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Epigenetic silencing of a multifunctional plant stress regulator" for further consideration at eLife. Your revised article has been favorably evaluated by Christian Hardtke as the Senior Editor and Daniel Zilberman as the Reviewing Editor.

The manuscript has been improved but there is a remaining issue that needs to be addressed before acceptance:

Reviewers expressed serious concerns about the antibody used for H2A.Z ChIP experiments. This antibody was raised against a full-length budding yeast H2A.Z protein and its performance against Arabidopsis H2A.Z has not been evaluated. Several approaches to address this issue were discussed among the reviewers, with the least laborious being a thorough comparison to published H2A.Z ChIP-seq datasets. Hence the request in our decision letter: "At minimum, please include a comprehensive comparison of the H2A.Z ChIP-seq data to one or more of the publicly available Arabidopsis ChIP-seq datasets derived from well-validated H2A.Z antibodies."

The metaplot of genes comparing anti-H2A.Z and anti-GFP-H2A.Z profiles in Figure 2—figure supplement 1G and the genome browser snapshot in Figure 2—figure supplement 1H are not comparisons to validated, published data, nor do they constitute a comprehensive comparison. Therefore, please include a detailed analysis that would unambiguously demonstrate that your H2A.Z ChIP-seq data are comparable to published datasets. This should include correlation analyses, heatmaps, patterns of enrichment in unmethylated genes, methylated genes and transposons, snapshots of representative loci, and any other data that you feel would convince readers that the H2A.Z antibody used in this study performs appropriately.
