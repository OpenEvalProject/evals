# Peer review - Round 1

Editors:
- Leemor Joshua-Tor, Cold Spring Harbor Laboratory , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05322.020](https://doi.org/10.7554/eLife.05322.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your work entitled "YcgC Represents a New Protein Deacetylase Family in Prokaryotes" for consideration at eLife. Your article has been favorably evaluated by Michael Marletta (Senior Editor), Leemor Joshua-Tor (Reviewing Editor), and three reviewers.

The Reviewing Editor and the reviewers discussed their comments before we reached this decision, and the Reviewing Editor has assembled the following comments to help you prepare a revised submission.

The paper describes an interesting study that uses an application of proteome array "Clip-Chip" technology to the discovery of new enzymatic functions. This appears to be a new twist on the use of proteome arrays and therefore very appealing. This technology has clearly identified a new class of protein deacetylases that does not require metal ions or NAD+. This is a fortunate happenstance and highlights the utility of the method for discovery of enzymes that informatics would not have picked up by homology searching. Thus, this paper will be of considerable interest to a broad spectrum of biological scientists.

However, several issues have been raised specifically regarding the activity of YcgC as a lysine deacetylase that would have to be addressed:

1) The biochemical data supporting that YcgC has deacetylase activity was based on Western blots using pan-specific acetyl lysine antibodies. One particular concern is that YcgC might be a protease that can cleave RutR at a specific sequence. This cleavage may in turn affect the recognition of an acetyl lysine residue in RutR by the antibody, leading to a decreased acetyl lysine signal on Western blots. This is highly likely because Figure 2A shows that RutR became smaller after treatment with YcgC. In addition, further post-translational modifications adjacent to the acetylated lysine might alter the epitopes for proper readout by an antibody. To rule out this concern, more biochemical data is needed. One suggestion is to examine whether YcgC can deacetylate a synthetic acetyl peptide and monitoring products using LC-MS based methods, which can provide definitive proof for the deacetylase activity.

2) In Figure 1D legend, you state: "using acetylated RutR proteins […] YcgC showed robust deacetylation activity in vitro". It seems that the SDS-PAGE mobility of RutR doesn't change following deacetylation. However, in Figure 2D, there is at least 5KD shift to a lower molecule weight after deacetylation. Such a discrepancy should be addressed.

3) The mass spectrometry data showing the acetylated K52 peptide (Figure 2D) is problematic. Although the spectra itself is not readable, it is clear that the peptide was obtained by trypsin digestion (as stated in the experimental section), which cleaves after lysine and arginine, but not after acetyl lysine. A long peptide with Kac embedded in the center should be detected. Figure 2D shows a peptide cut after acetyl lysine, which is highly unlikely. This indicates that either the acetyl group is not on K52 or the MS data is unreliable. Although all the Y ions are marked, for the C-Kac peptide as shown, the Y ions shouldn't be visible because it lost the positively charged Lys which shouldn't fly in MS. In contrast, the C-Lys peptide should fly. However, the similar ionization efficiency for the b and y ions for the two peptides doesn't make sense. The images are at low resolution and therefore hard to examine in detail. In addition, HPLC retention times should be indicated. The same concern is noted for the MS data shown in the supplementary figures.

4) The gel shown in Figure 2F is not convincing. The authors state in the text that the double mutant provides the lowest level of acetylation of RutR, the substrate protein. This is not apparent. At least by my eye the K62Q and the double mutant appear to provide quite similar results. Some sort of quantification of these results should be provided.

5) It was not clear in the manuscript whether or not YcgC is an essential protein in E. coli. A related point is that when the authors overexpress the protein in vivo, it was not clear whether this was being done in a ∆ycgC strain or on top of the native level of YcgC. Please provide this information.

Other issues to address:

6) It is surprising that 1x or 2x-acetylation/deacetylation can cause such a dramatic mobility shift (Figure 2A). Fortunately, the authors showed that CobB also deacetylates the same substrate. This data should be included to show that deacetylation can indeed cause a 5kD mobility shift.

7) In Figure 2C, why are the band intensities of alpha-Flag and α-YcgC so different? In addition, even given that α-Flag bands have equal intensity, the decreased α-Kac bands should correspond to two α-Flag bands given the decreased mobility shift following deacetylation.

8) For the MS analyses, it is not unclear whether the authors run the SDS page gels first and then cut the band for MS analysis. In theory, there should be two bands (Kac-containing starting materials and K-containing products), which should be resolved well and analyzed in parallel.

9) In Figure 2F, interestingly, although the negative signals of α-Kac antibodies, the Coo. bands showed the similar mobility as shown in Figure 2A. It seems that the same reaction occurs when RutR was mixed with YcgC. It is another strange observation.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "YcgC Represents a New Protein Deacetylase Family in Prokaryotes" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Marletta (Senior Editor), a Reviewing Editor, and two reviewers. The manuscript has been significantly improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers all felt that this work is significant and important. Precisely because of this, it is important to make sure as much as possible that observations reported are not due to a contaminating protease activity. The MS data showing 95% sequence coverage of RutR sequence cannot prove that there is no proteolysis. The fact that YcgC does not work on a synthetic peptide is another reason for concern.

There are a couple of simple things that could be done to address this concern:

1) In Figure 2A, include a negative control with CobB but without NAD+.If there is a protease contamination, it is likely an endogenous E. coli protein that is present in both the YcgC and CobB prep. Using CobB without NAD+ should resolve this.

2) In Figure 2F, K52Q and K62Q mutants were blotted and they appear to be of similar size to the WT protein. One can argue that the K to Q mutant behaves similarly to the acetylated WT protein. However, the authors should repeat these experiments using the K52R and K62R mutants. If these mutants migrate faster as the deacetylated RutR, it will also help address these concerns. In addition, the K to R mutants may improve the Ac Western blot because Q is generally thought to mimic acetyl lysine.

It is interesting that the 5-kd mobility shift only occurs for native YcgC but not N-terminal flagged YcgC. Such an observation should be described explicitly in the text to avoid potential confusion, especially if the K52R and K62R mutants don't migrate as fast. This type of shift by 1 or 2 Ac groups is quite large.

3) Another possibility is to mutate the conserved Ser residues in YcgC and show that the mutant loses deacetylase activity. There are only five conserved Ser residues and mutating them would not be a huge effort.

4) For Figure 1D, the experimental details provided in the main text and response letter are still not clear. Did the authors run "Coo. Stain" on the samples and then use the same sample for the deacelylation reaction or did they run "Coo. Stain" and deacelylation with equal amounts of the two aliquots? If the latter is the case, the samples after the deacelylation reaction should be subsequently stain by a Western-compatible dye followed by anti-acetyllysine antibody.
