# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21184.034](https://doi.org/10.7554/eLife.21184.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Extensive cargo identification reveals distinct biological roles of the 12 importin pathways" for consideration by eLife. Your article has been favorably evaluated by James Manley (Senior Editor) and three reviewers, one of whom, Karsten Weis (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Yuh Min Chook (Reviewer #2); John D Aitchison (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Kimura and colleagues employ a functional in vitro transport assay combined with SILAC-based mass spectrometry experiments to identify in a comprehensive manner cargoes for 12 nuclear transport receptors (NTRs; 10 human Importins and 2 bidirectional Karyopherins). In general, the work is of high quality and carefully analyzed. The results should be of interest to a very broad audience and provide an excellent resource for researchers studying a variety of nuclear processes. However, there are some concerns regarding the data presentation and interpretation that need to be addressed prior to publication.

Required revisions:

1) Certain aspects of the manuscript are not well presented. This is particularly problematic in the second part of the paper where the authors present a GO term analysis for the various NTRs. These results could simply and more effectively presented in tabular form (including a list of the actual cargoes that fall into each GO term). Then the highlights of this analyses should be mentioned and discussed. Claims of collective activity of individual or a few NTRs in designated cellular processes from this GO term analysis should be avoided in the absence of experimental support.

2) Lists like the ones shown in Figure 2 and lists of 3rd-Z-4% cargoes for each of the 12 NTRs should be easily accessible in the main or supplemental figures.

3) Additional supportive information needs to be added to increase the confidence in the presented results. For example, information on the results of halo binding assays is not easily accessible. It was not clearly shown how many of their "highly reliable" (3rd-Z-4%) cargoes were tested for direct NTR binding, what fraction of those tested bound the NTRs and which 3rd-Z-4% cargo did not bind directly to its NTR. Also, it is unclear what criteria were applied to select proteins for the bead halo assay.

4) There is a concern about the 'context' of cargoes used in the assays. The authors added nuclear extract as the source of cargoes to digitonin-permeabilized cells. This is presumably because nuclear extract is much more enriched than cytoplasmic extract in import cargoes as most ultimately reside in the nucleus. However, many cargoes may assume different 'states' (binding partners, PTM, etc.) that are quite different from their cytoplasmic states. Nuclear import cargoes are recognized by their NTRs in the cytoplasm, hence in their cytoplasmic states and not in their nuclear states. Some proteins in nuclear extract may respond to different NTRs than they would in their cytoplasmic states. Have the authors attempted to address this? At least this should be discussed as a potential caveat.

5) How do the authors explain well-established functions of Imp-9 such as import of actin into the nucleus? Imp-9 and Exp-6 (which exports actin) are used routinely to control levels of nuclear actin, but it is curious that the authors did not find actin or actin-binding proteins in their list of potential Imp-9 cargoes.

6) How does the approach consider endogenous NTRs that are abundant in the nucleoplasm at steady state? Presumably these proteins are still present and able to cycle during the import reaction?

7) Why are there such high numbers of proteins detected as imported in the absence of recombinant NTRs? Is this due to residual NTRs, either in the nucleus or cytosolic fraction?

8) Depletion of β-1 from the cytoplasm presumably depletes α. Is this quantified and incorporated into the analysis?

9) 0.3 to 0.7 μM of NTR was used in the experiment. How was this concentration decided for each NTR? How does this compare to the endogenous concentration of each NTR?

10) Subsection “SILAC-Tp”, end of first paragraph – How was the nuclear extract prepared after import? The authors only mention that the cells were suspended in nuclear buffer, sonicated and centrifuged.

11) Based on the SILAC-tp experimental design, a positive Z-score value of a particular protein would mean that the given protein was imported into the heavy-nuclei. A large number of proteins are listed with negative 2nd Z-scores. Does this mean that these proteins were 'exported' out of the recipient nuclei in the presence of the various NTRs?

12) Supplementary file 1, Sheet: 'Trn-1' contains three columns of L/H ratios for each identified protein. For some top ranked proteins, (e.g. mitochondrial glutamate dehydrogenase), a large variation between SILAC ratios is observed between the three replicates. For some proteins, no ratios were calculated in some technical replicates. Was this because of low quality LCMS data or due to low abundance of these proteins? For such cases, the authors need to include an extracted ion chromatogram (EIC) of a respective peptide from all replicates to exclude the possibility of SILAC quantification artifacts. (By the way, why is this protein, among other cytoplasmic proteins, present in the nuclear fraction? The authors should comment and edit as necessary).

13) The authors don't specify whether or not they considered 2 or more peptides/protein for a SILAC ratio. Quantification based on a single peptide with sub-optimal signal quality may affect the L/H ratios. A detailed description should be included in the Methods section on the criteria and software used to calculate SILAC ratios.

14) The statistical language (e.g. definition of statistical parameters and their use to justify designated cargoes) would benefit from better visual support via figures/tables.

15) In general, the Z-ranking is cumbersome and difficult to interpret. On the whole, the addition of some descriptive statistics would be helpful for the interpretation; however, they are unlikely to significantly change the conclusions.

16) The cutoffs of 15% (and others) are arbitrary. To determine if the 'reported cargo' proteins are lumped at one end of the ranked list, the authors could use something like a Kolmogorov-Smirnov (KS) or Mann-Whitney (MW) test.

17) It should also be possible to estimate the sensitivity and a lower bound on the specificity at different index cutoffs using those receptors with high numbers of reported cargoes (i.e. TRN-1 and 2). The sensitivity at a cutoff will be (# reported cargoes selected) / (# reported cargoes selected + # reported cargoes not selected). The specificity is harder to quantify since the 'not carriers' is not known. However, one could consider all of the 'grey bar' proteins in Figure 1 as negatives, then one could estimate the upper bound on the number of false positives. An estimated sensitivity and specificity like this would help ground otherwise arbitrary cutoffs (e.g. top 100 proteins) as something interpretable. It would also help explain what it means for a cargo to pass the 2nd-Z-15% and 3rd-Z-4% criteria.

18) The enrichments of reported cargoes in highly ranked proteins should have a p-Value, for example as calculated from the hypergeometric distribution.

19) 'To calculate the +NTR/Ctl value, one protein has to be quantified in both the control and +NTR reactions, and we discarded L/H+NTR values that lacked the counterpart L/HCtl values.' Wouldn't this remove the most interesting hits? That is to say, proteins that can only get into the nucleus through the added receptor?

20) In the second paragraph of the Introduction, the authors mentioned that NTR binding sites for cargoes have been established for Importins α, β, Trn-1/2 and Trn-SR. They missed the Imp-5 and its homologous Kap121p systems, where the Matsuura group very nicely elucidated the binding site for IK-NLSs found in Imp5/Kap121p cargoes.

21) In the second paragraph of the Introduction, the last part of the sentence "…the PY-NLS motif has been defined, although the motif is not an absolute determinant of transport (Soniat and Chook, 2015)." is a bit confusing. Do the authors mean that presence of a PY-NLS does not necessarily determine transport, or do they mean that there are other motifs that may direct Trn-1/2 mediated transport?
