# Author response - Round 1

Authors:
- Aleksandar Bartolome
- Julia C Heiby
- Domenico Di Fraia
- Ivonne Heinze
- Hannah Knaudt
- Ellen Spaeth ([ORCID: 0000-0002-3851-3931](https://orcid.org/0000-0002-3851-3931))
- Omid Omrani
- Alberto Minetti
- Maleen Hofmann
- Joanna M Kirkpatrick
- Therese Dau ([ORCID: 0000-0003-0251-9490](https://orcid.org/0000-0003-0251-9490))
- Alessandro Ori ([ORCID: 0000-0002-3046-0871](https://orcid.org/0000-0002-3046-0871))

## Response text

DOI: [10.7554/eLife.93256.3.sa3](https://doi.org/10.7554/eLife.93256.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations For The Authors):

Specific comments to improve the quality of the work:

(1) The choice of subunits to tag are really not ideal. In the available structures of the human proteasome, The C-terminus of Rpn3/PSMD3 points directly toward the ATPase pore and is likely to disrupt the structure and/or dynamics of the proteasome during proteolysis (see comments regarding controls for functionality below). Similarly, the C-terminal tail of Rpt1/PSMC2 has a key role in the opening of the 20S core particle gate for substrate translocation and processing (see 2018 Nature Communications, 9:1360 and 2018 Cell Reports 24:1301-1315), and Alpha3/PSMA4 can be substituted by a second copy of Alpha4/PSMA7 in some conditions (although tagging Alpha3/PSMA4 would admittedly provide a picture of the canonical proteasome interactome while actively excluding the interactome of the non-canonical proteasomes that form via replacement of Alpha3/PSMA4). Comparison of these cell lines with lines harboring tags on subunits that are commonly used for tagging in the field because of a lack of impacts, such as the N-terminus of Rpn1/PSMD2, the C-terminus of Rpn11/PSMD14, and the C-terminus of Beta4/PSMB2 would help instill confidence that the interactome reported largely arises from mature, functional proteasomes rather than subcomplexes, defective proteasomes, or other species that may occur due to tagging at these positions.

We thank the reviewer for pointing this out. The original purpose of our strategy was to establish proximity labeling of proteasomes to enable applications both in cell culture and in vivo. The choice of PSMA4 and PSMC2 was dictated by previous successful tagging with GFP in mammalian cells (Salomons et al., Exp Cell Res 2010)(Bingol and Schuman, Nature 2006). However, the choice of C-terminal PSMC2 might have been not optimal. HEK293 cells overexpressing PSMC2-BirA* show slower growth and the BioID data retrieve higher enrichment of assembly factors suggesting slower assembly of this fusion protein in proteasome. Although we did not observe a negative impact on overall proteasome activity and PSMC2-BirA* was (at least in part) incorporated into fully assembled proteasomes as indicated by enrichment of 20S proteins.We apologize for not making it clear that we labeled the N-terminus of PSMD3/Rpn3 and not the C-terminus (Figure 1a and S1a). Therefore, we included in Figure S1a of the revised manuscript structures of the proteasome where the tagged subunit termini are highlighted: C-terminus for PSMA4 and PSMC2 and N-terminus for PSMD3.Additionally, we would like to point out that, differently from PSMC2-BirA, cells expressing BirA-PSMD3 did not show slower growth, and BioID data showed a more homogenous enrichment of both 19S and 20S proteins, as compared to PSMC2-BirA* (Figure 1D and 1E). However, the overall level of enrichment of proteasome subunits was not comparable to PSMA4-BirA* and, therefore, we opted for focusing the rest of the manuscript on this construct.

In support of this point, the data provided in Figure 1E in which the change in the abundances of each proteasome subunit in the tagged line vs. the BirA control line demonstrates substantial enrichment of the subcomplexes of the proteasome that are tagged in each case; this effect may represent the known feedback-mediated upregulation of new proteasome subunit synthesis that occurs when proteasomal proteolysis is impaired, or alternatively, the accumulation of subcomplexes containing the tagged subunit that cannot readily incorporate into mature proteasomes. Acknowledging this limitation in the text would be valuable to readers who are less familiar with the proteasome.

We would like to clarify that the data shown in Figure 1E do not represent whole proteome data, but rather log2 fold changes vs. BirA* control calculated on streptavidin enrichment samples. The differences in the enrichment of the various subcomplexes between cell lines derives from the fact that the effect size of the enrichment depends on both protein abundance in the isolated complexes, but also on the efficiency of biotinylation. The latter will be higher for proteins located in closer proximity to the bait. A similar observation was pointed out in a recent publication (PMID: 36410438) that compared BioID and Co-IP for the same bait. When a component of the nuclear pore complex (Nup158) was analyzed by BioID only the more proximal proteins were enriched as compared to the whole complex in Co-IP data (Author response image 1):

The bait protein NUP158 is filled in yellow. Proteins enriched in the pulldown falling outside the SigA/B cutoff are filled in gray. NPC, nuclear pore complex. SigA, significant class A; SigB, significant class B. Reproduced from Figure 6 of Moreira CMDN et al., 2023 (PMID: 36410438).

However, we would like to point out that despite quantitative differences between different proteasome subunits, both 19S and 20S proteins were found to be strongly enriched (typically >2 fold) in all the constructs compared to BirA* control line (Figure 1E). This indicates that at least a fraction of all the tagged subunits are incorporated into fully assembled proteasomes.

Regarding the upregulation of proteasome subunits as a consequence of proteasome dysfunction, we did not find evidence of this, at least in the case of PSMA4. The immunoblot shown in Figure 2A and its quantification in S3A indicate no increased abundance of endogenous PSMA4 upon tetracycline induction of PSMA4-BirA*.

(2) The use of myc as a substrate of the proteasome for demonstration that proteolysis is unaffected is perhaps not ideal. Myc is known to be degraded via both ubiquitin-dependent and ubiquitin-independent mechanisms, such that disruption of one means of degradation (e.g., ubiquitin-dependent degradation) via a given tag could potentially be compensated by another. A good example of this is that the C-terminal tagging of PSMC2/Rpt1 is likely to disrupt interaction between the core particle and the regulatory particle (as suggested in Fig. 1D); this may free up the core particle for ubiquitin-independent degradation of myc.

Aside from using specific reporters for ubiquitin-dependent vs. independent degradation or a larger panel of known substrates, analysis of the abundance of K48-ubiquitinated proteins in the control vs. tag lines would provide additional evidence as to whether or not proteolysis is generally perturbed in the tag lines.

We thank the reviewer for this suggestion. We have included an immunoblot analysis showing that the levels of K48 ubiquitylation (Figure S3d) are not affected by the expression of tagged PSMA4.

(3) On pg. 8 near the bottom, the authors accidentally refer to ARMC6 as ARMC1 in one instance.

We have corrected the mistake.

(4) On pg. 10, the authors explain that they analyzed the interactome for all major mouse organs except the brain; although they explain in the discussion section why the brain was excluded, including this explanation on pg. 10 here instead of in the discussion might be a better place to discuss this.

We moved the explanation from the discussion to the results part.

Reviewer #2 (Recommendations For The Authors):

(1) Perhaps the authors can quantify the fraction of unassembled PSMA4-BirA* from the SEC experiment (Fig. 2b) to give the readers a feeling for how large a problem this could be.

The percentages based on Area Under the Curve calculations have been added to Figure S3b.

(2) Do the authors observe any difference in the enrichment scores between proteins that are known to interact with the proteasome vs proteins that the authors can justify as "interactors of interactors" vs the completely new potential interactors? This could be an interesting way to show that the potential new interactors are not simply because of poor false positive rate calibration, but that they behave in the same way as the other populations.

We thank the reviewer for this suggestion. We analyzed the enrichment scores for 20S proteasome subunits, known PIPs, first neighbors and the remaining enriched proteins. The remaining proteins (potential new interactors) have very similar scores as the first neighbors of known interactors. This plot has been added to Figure S3g.

(3) Did the authors try to train a logistic model for the miniTurbo experiments, like it was done for the BirA* experiments? Perhaps combining the results of both experiments would yield higher confidence on the proteasome interactors.

Following the reviewers suggestion, we applied the classifier on the dataset of the comparison between miniTurbo and PSMA-miniTurbo. We found a clear separation between the FPR and the TPR with 136 protein groups enriched in PSMA-miniTurbo. We have added the classifier and corresponding ROC curve to Figure S4f and S4g.

75 protein groups were found to be enriched for both PSMA4-BirA* and PSMA4-miniTurbo (Author response image 2), including the proteasome core particles, regulatory particles, known interactors and potential new interactors. As we focused more on the identification of substrates with PSMA4-miniTurbo, we did not pursue these overlapping protein groups further, but rather used the comparison to the mouse model to identify potential new interactors.

(4) Perhaps this is already known, but did the authors check if MG132 affect proteasome assembly? The authors could for example repeat their SEC experiments in the presence of MG132.

We thank the reviewer for the suggestion, however to our knowledge there are no reports that MG132 has an effect on the assembly of the proteasome. MG132 is one of the most used proteasome inhibitors in basic research and as such has been extensively characterized in the last 3 decades. The small peptide aldehyde acts as a substrate analogue and binds directly to the active site of the protease PSMB5/β5. We therefore think it is unlikely that MG132 is interfering with the assembly of the proteasome.

(5) Minor comment: at the bottom of page 8, the authors probably mean ARMC6 and not ARMC1.

We have corrected the mistake.

(6) It would be interesting to expand the analysis of the already acquired in vivo data to try to identify tissue-specific proteasome interactors. Can the authors draw a four-way Venn diagram with the interactors of each tissue?

We thank the reviewer for this suggestion. We have generated an UpSet plot showing the overlap of ProteasomeID enriched proteins in the four tissues that gave us meaningful results (Author response image 3). In order to investigate whether the observed differences in ProteasomeID enriched proteins could be meaningful in terms of proteasome biology, we have highlighted proteins belonging to the UPS that show tissue specific enrichments. We found proteasome activators such as PSME1/PA28alpha and PSME2/PA28beta to enrich preferentially in kidney and liver, respectively, as well as multiple deubiquitinases to enrich preferentially in the heart. These differences might be related to the specific cellular composition of the different tissues, e.g., number of immune cells present, or the tissue-specific interaction of proteasomes with enzymes involved in the ubiquitin cycle. Given the rather preliminary nature of these findings, we have opted for not including this figure in the main manuscript, but rather include it only in this rebuttal letter.

Reviewer #3 (Recommendations For The Authors):

(1) In the first paragraph of the Introduction, the authors link cellular senescence caused by partial proteasome inhibition with the efficacy of proteasome inhibitors in cancer therapy. Although this is an interesting hypothesis, I am not aware of any direct evidence for this; rather, I believe the efficacy of bortezomib/carfilzomib in haematological malignancies is most commonly attributed to these cells having adapted to high levels of proteotoxic stress (e.g., chronic unfolded protein response activation). I would suggest rephrasing this sentence.

We thank the reviewer for the comment and have amended the introduction.

(2) For the initial validation experiments (e.g., Fig. 1B), have the authors checked what level of Streptavidin signal is obtained with "+ bio, - tet" ? Although I accept that the induction of PSMA4-BirA* upon doxycycline addition is clear from the anti-Flag blots, it would still be informative to ascertain what level of background labelling is obtained without induction (but in the presence of exogenous biotin).

We tested four different conditions +/- tet and +/- biotin (24h) in PSMA4-BirA* cell lines (Author response image 4). As expected, biotinylation was most pronounced when tet and biotin were added. When biotin was omitted, streptavidin signal was the lowest regardless of the addition of tet. Compared to the -biotin conditions, a slight increase of streptavidin signal could be observed when biotin was added but tet was not added. This could be either due to the promoter leaking (PMID: 12869186) or traces of tetracycline in the FBS we used, as we did not specifically use tet-free FBS for our experiments.

For the sample used as expression control tetracycline was omitted (-tet). To test background biotinylation, biotin supplementation was omitted (-bio). Immunoblot against BirA* and PSMA was used to verify induction of fusion proteins, while GAPDH was used as loading control.

(3) For the proteasome structure models in Fig. 1D, a scale bar would be useful to inform the reader of the expected 10 nm labelling radius (as the authors have done later, in Fig. 2D).

We have added 10 nm scale bars to Figure 1d.

(4) In the "Identification of proteasome substrates by ProteasomeID" Results subsection, I believe there is a typo where the authors refer to ARMC1 instead of ARMC6.

We have corrected the mistake.

(5) I think Fig. S5 was one of the most compelling in the manuscript. Given the interest in confirming on-target efficacy of targeted degradation modalities, as well as identifying potential off-target effects early-on in development, I would consider promoting this out of the supplement.

We thank the reviewer for the comment and share the excitement about using ProteasomeID for targeted degradation screening. We have moved the data on PROTACs (Figure S5) into a new main Figure 5.

In addition, in relation to the comment of this reviewer regarding the detection of endogenous substrates, we have now included validation for one more hit emerging from our analysis (TIGD5) and included the results in Figure 4f, 4g and S4j.
