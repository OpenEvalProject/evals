# Author response - Round 1

Authors:
- Florian A Steiner
- Steven Henikoff

## Response text

DOI: [10.7554/eLife.02025.025](https://doi.org/10.7554/eLife.02025.025)

1) In Figure 4A, only two regions of the CENP-C X-Chip are shown. To assess the quality of the CENP-C X-Chip it would be really important to see a larger region of DNA as it has been done in other figures of this paper.

The quality of the CENP-C X-ChIP should be most evident from the heat map in Figure 4C, which depicts the signals over the 707 centromere sites. We did not use the CENP-C data to call sites; only to confirm that the sites that we called based on cenH3 data were enriched in CENP-C, and the Figure 4C heat map and Figure 4–figure supplement 2B boxplots clearly make this point. It shows that the enrichment of CENP-C at cenH3 sites is not restricted to the two example peaks shown and extends to the large majority of cenH3 sites genome-wide. We acknowledge that the CENP-C X-ChIP data are inherently much noisier than the cenH3 native ChIP data. The reason for this is at least in part biological, as cenH3 is present on chromatin through the vast majority of the cell cycle, while CENP-C was previously shown to be localized to cenH3 sites during mitosis, but not during interphase (Moore and Roth, 2001 PMID:11402064). As only a small fraction of the embryonic cells analyzed are in mitosis, the signal-to-noise ratio is inevitably much lower. Nevertheless, CENP-C ChIP signal-to-noise is sufficient to confirm that the cenH3 sites correspond to kinetochore sites, and we have further strengthened this conclusion as described below.

- How many CENP-C sites are identified?

- What sub-fraction of cenH3 peaks overlaps with what subfraction of the other sequences with centromere-like behavior: insoluble sites and CENP-C peaks (a Venn diagram or other graphical means could be useful). Most importantly, how does this compare to broad cenH3 domains?

We agree that a direct head-to-head comparison of cenH3 peaks and broad domains with respect to insoluble sites and CENP-C peaks is important to strengthen our conclusion that cenH3 sites correspond to kinetochore sites. There are 347 CENP-C peaks, of which 163 overlap with the cenH3 sites, whereas only 26 CENP-C peaks overlap with the domains. Based on the fact that the coverage of cenH3 peaks is only 0.3% that of broad domains, the enrichment of CENP-C at cenH3 peaks relative to cenH3 domains is (163/26)/0.003 ≈ 2000-fold. Similarly, there are 2060 peaks in the insoluble chromatin, 460 of which coincide with the cenH3 peaks, compared to 147 for the domains, which implies a relative enrichment of insoluble chromatin at cenH3 peaks to cenH3 broad domains of (147/460)/0.003 ≈ 800-fold. Importantly, the densities of both CENP-C and insoluble chromatin peaks within the domains are significantly lower than within the rest of the genome. That is, our CENP-C ChIP data not only confirm that the cenH3 peaks are kinetochore sites, the data also argue against the hypothesis that broad domains harbor kinetochore sites. We have included these new data in Figure 4–figure supplement 2, panels C and D and now make this point in the text (Results section entitled “CenH3 peaks correspond to kinetochore sites”).

2) Given that the MNase digest is important to the argument that the identified cenH3 sites show the properties of point centromeres, the authors should show a control in Figure 2 for MNase digestion, such as an H3 nucleosome where the amplitude is less sensitive when compared to cenH3.

We agree that we had not sufficiently described the characteristic MNase sensitivity of the point centromere sites. To strengthen this point, we have substantially revised Figure 2, added Figure 2–figure supplement 2, and expanded the text describing the MNase sensitivity (Results section entitled “cenH3 peaks are hyper-sensitive to MNase digestion”). We now show the progression of the MNase digest separately for the input and cenH3 ChIP samples, both for an extended region around the two example peaks (Figure 2A) and at all sites genome-wide (Figure 2B). This illustrates that the cenH3 peaks are sensitive to MNase, while the surrounding chromatin features remain relatively unaffected. For comparison, we now also include the pattern for progressive digestion of the input chromatin at the +1 nucleosomes of genes (Figure 2C).

To quantify the MNase-sensitivity of cenH3 nucleosomes, the nucleosomes flanking the cenH3 peaks and the +1 nucleosomes, we plotted the occupancy at these features relative to the occupancy of first time point. This clearly shows that the cenH3 peaks are more MNase-sensitive than both the flanking and +1 nucleosomes (Figure 2D).

3) More information on the peak calling should be provided as this confused two reviewers.

We have extended the description of our very simple peak calling in the Methods section (penultimate paragraph of the section entitled “Illumina sequencing and data analysis”) and added a sentence in the Results section (entitled “High resolution mapping of cenH3 reveals discrete high occupancy sites”). We classified all sites that exceeded 30 normalized counts in at least one of two biological replicate (cenH3 ChIP minus input) as peaks. 30 counts is the equivalent of the genome-wide mean plus seven standard deviations.
