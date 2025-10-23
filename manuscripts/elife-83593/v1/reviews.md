# Peer review - Round 1

Editors:
- Jenny Tung, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83593.sa0](https://doi.org/10.7554/eLife.83593.sa0)

This is an important paper that combines comparative analysis and experimental assays to investigate the role of protein-coding and regulatory changes at TRNP1 in mammalian brain evolution. The evidence supporting a contribution of TRNP1 is convincing, although the strength of the link between protein-coding changes and trait evolution is stronger and more readily interpretable than the data on gene regulation. The work will be of interest to researchers interested in mammalian evolution, brain evolution, and evolutionary genetics.


---

# Peer review - Round 1

Editors:
- Jenny Tung, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83593.sa1](https://doi.org/10.7554/eLife.83593.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Regulatory and coding sequences of TRNP1 co-evolve with brain size and cortical folding in mammals" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The reviewers appreciated the effort to investigate both coding and regulatory changes and feel the MPRA study was well-designed. However, because the results of the MPRA are somewhat unclear (and necessarily incomplete as a test of regulatory function), please temper your conclusions accordingly. Additionally, clarify how you dealt with the multiple testing burden.

2) Please address the outstanding questions about the appropriateness of the background set of genes used for comparison of brain phenotype-evolutionary rate correlations. This could take the form of additional analysis, or minimally a discussion of the potential limitations and/or biases of the set you used.

Reviewer #1 (Recommendations for the authors):

I think this paper makes an important contribution to the literature. Genomic analyses that control for phylogenetic context/non-independence remain rare (at least in primates), and the integration of functional genomic analysis and experimentation is an important strength. I have a few concerns, however:

1. I am unclear on your interpretation of the correlation between brain size/gyrification and the rate of protein evolution-specifically, why a positive correlation should necessarily be expected. While comparative analyses often analyze correlated evolution between two traits (e.g., brain size and diet), this analysis seems more like analyzing the correlation between brain size and lineage-specific change in diet. If we assume that TRNP1 is a major driver of brain size, and selection on brain size fully accounts for selection on the gene, then the big-brained descendants of a big-brained ancestor might show strongly conserved patterns of evolution (small values of omega) rather than additional evidence for lineage-specific positive selection. In other words, whether selection for big brains translates to evidence for positive versus purifying selection on the sequence (i.e., the value of omega) would seem to depend on ancestral state. It would be helpful to readers if you can outline your hypotheses and predictions here more explicitly, including your expectations related to lineage-specific rates.

2. On a related note, I appreciate the attempt to find a matched set of control genes for the protein molecular evolution analysis; clearly this is difficult. However, I am not entirely convinced that the control genes are an appropriate background set (although I am also not sure how to identify one). Because one of the main filters for identifying these genes was to find genes where homologues can be readily identified, without the additional curation/sequencing done for TRNP1, they are likely to be enriched for genes evolving under constraint within mammals-so they may control for demographic differences, but not for the interaction of Ne with positive selection. This appears to be the case based on Figure 1—figure supplement 3, where most genes show no evidence of sites under positive selection. The comparison therefore works as a null for testing for positive selection, but not as an ideal null for testing whether patterns of positive selection correlate with a brain size/gyrification, as intended here (since most genes don't show the same pattern of positive selection).

3. In Figure 1 C and D and lines 104-105, the strongly attenuated slope in the control genes line is because you are taking the average across control genes for each species. The comparison I think you want is whether the slope for TRNP1 is an outlier relative to the slopes calculated for each of the control genes, not relative to the slope calculated for their average, which will inevitably be attenuated. I think this is the result you report in lines 106-109, but it should also be what is visualized in Figure 1C-1D to avoid overemphasizing the difference between TRNP1 and the control gene distribution (by taking the average, the distribution is not apparent). On a related note: are the results in these figures and text controlled for phylogenetic non-independence? I ask in part because it seems like a lot of the signal is being driven by haplorrhine primates.

4. You show, in a very nice result, that neural stem cell proliferation rate is correlated with brain size and gyrification index. Given that your evidence for the protein evolution-trait link is based on lineage-specific omega, is proliferation rate therefore correlated with omega?

5. Line 189 (and related to the question below about the directional relationship between TRNP1 expression and brain morphology) draws on the MPRA results to argue that the expression regulation of TRNP1 co-evolves with cortical folding. Is TRNP1 indeed more highly expressed in catarrhines with higher GI values (i.e., is this result consistent with a prediction from the literature?).

Reviewer #3 (Recommendations for the authors):

I would suggest that the authors address the following points:

1. Protein evolution rate analyses: I found Fig1S3 surprising, as it seems that about half of all control proteins used by the authors also evolve under positive selection. This seems unlikely high, and suggests that either the alignments contain errors and require cleaning, or the false discovery rate is inadequately corrected for in this analysis. Additionally, it was not always clear to me when the authors use either branch or site tests – I assume that the evolutionary rate analyses use unconstrained branch models, but this does not appear in the methods. In this case, can branch length confound the signal? I would expect that the estimation of omega in human, for example, is less reliable than e.g. dolphin, where the terminal branch is much longer.

2. Throughout the paper, it is unclear how multiple testing was corrected for. In some cases this does not matter, but it does for example when the authors investigate correlations between CRE activity and brain phenotypes at multiple sites. The likelihood of finding one spurious correlation increases rapidly when multiple CREs are tested, and in this case the authors cannot fall back on control regions to estimate the probability of observing such a correlation from background data, as they do for the gene evolution analyses. It may not be possible to control for this, but this should be explicitly acknowledged, and the conclusions toned down as a consequence.

3. I do not think it is surprising that an enhancer active in brain contains an excess of binding sites for TFs involved in neuronal proliferation, especially as I don't fully understand the display of Figure 4C (what does "Fisher's p" mean? P-value of Fisher's exact test – which would mean that these enrichments are not actually significant? What does "significant/annotated" mean?). The evidence that CTCF binding sites are stronger in catarrhines is weak – again, it is not clear to me how multiple testing was corrected for here, and the probability of spuriously finding one TF with a correlation out of 22 is high. I would suggest discussing this more explicitly, and toning down the discussion on CTCF as I am unconvinced that this signal is specific.

4. Spotted a few typos that need correcting e.g. line 111 "showed higher a significant"; line 122 "orthologoues"; also some in the methods which should be caught by a spellcheck editor.
