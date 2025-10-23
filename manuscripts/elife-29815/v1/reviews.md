# Peer review - Round 1

Editors:
- Karsten Weis, ETH Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29815.042](https://doi.org/10.7554/eLife.29815.042)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Context-dependent deposition and regulation of mRNAs in P-bodies" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by James Manley as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Roy Parker (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Spang and colleagues apply chemical cross- linking in combination with affinity purification (cCLAP – chemical Cross-Linking coupled to Affinity Purification) with the goal to identify mRNAs that enrich in P-bodies in different stress conditions. The authors use cCLAP in glucose starvation, and upon CaCl2 and NaCl salt stress. They identify more than 1500 mRNAs, which can be classified into mRNAs that are found in all stress condition and mRNAs that are stress specific. A subset of the identified mRNAs is further analyzed to gain insight into how those mRNAs accumulate in P-bodies and what the consequences are of such P-body localization.

The strengths of this manuscript are that it addresses important and interesting issues as to the composition and function of RNP granules. The weakness of the work is that some of the analyses are limited in their methodology and that some results are overinterpreted. Although there is interest from the reviewers, for acceptance in eLife, it will be critical to address these weaknesses (detailed below) to allow the conclusions to be robustly supported.

Essential revisions:

1) Several aspects of the identification of P-body enriched mRNAs need to be clarified and expanded:

a) There is no clear evidence that the authors enrich for PBs, and it appears that they are really identifying mRNAs that interact with Dcp2 or Scd6 in a variation of CLIP analyses (since the RNPs are digested with T1 nuclease before they are even pelleted?), and thus they essentially analyze pelleted Dcp2 or Scd6 assemblies. This needs to be made implicit and clearly discussed since this impacts their claim that P-bodies per se are being purified. This is also important in light of the FISH analyses (see below).

b) It is unclear how enriched mRNAs are identified from the RNA-Seq data. There seems to be no comparison to the total RNA-Seq reads, and there is no control for background RNA contamination. At a minimum the methods for calling an mRNA as enriched in the RNA-Seq needs to be clarified, but the manuscript would be much stronger if the "P-body" associated mRNAs were compared to read density in total (ribo-) RNA-Seq as this should allow a more meaningful description of what mRNAs are enriched in the these fractions.

c) The authors show a principal component analysis as a measure or reproducibility. However, they should also include pair-wise correlations of their read densities and provide R squared values to assess the reproducibility

d) If the authors had a clear population of mRNAs shown to be enriched in P-bodies, one could perform computational analyses on these mRNAs to see i) how they share molecular features (length, translation efficiency, decay rates, overlap with Pat1, Lsm1 bound mRNAs identified by similar (but not identical) methods (Mitchell et al., 2013), etc.). This might provide new insights into the mechanisms of P-body formation and function.

2) A key experiment is shown in Figure 2 examining whether the identified mRNAs enrich in PBs using FISH. Again several improvements are necessary for these analyses.

a) What is the basis for using ACT1 and PGK1 as controls? How were ACT1 and PGK1 determined to not show enrichment in P-bodies from the RNA sequencing? Given the very high abundance of these mRNAs, even a low percentage of these mRNAs in P-bodies would give a high number of reads in the samples. Is this seen? This is another example wherein comparing the number of reads in the "P-body" prep as compared to the total RNA-Seq reads would be helpful.

b) It is important that the authors are explicit about numbers of mRNAs in P-bodies. It appears that an enriched mRNA (such as Bsc1 or ATP11) has approximately 15-12% of the mRNA molecules as overlapping with Dcp2. Thus, the mRNA is enriched over controls, but still a majority of molecules are outside of the P-body assembly. Is this correct? And if so, this needs to be clearly stated and discussed as this makes it more complicated to interpret how P-body localization affects function since at any one time, only a small% of the actual mRNA molecules are associated with P-bodies per se.

c) Whereas several of the identified mRNAs seem to localize to (-) glucose PBs (with the caveats above), no data for the salt-induced PBs are shown. Does this mean the enrichment protocol didn't work well for these stresses? To validate their protocol additional FISH experiments also for the salt stresses should be shown.

3) Examining how mRNA decay rates correlate with P-body localization is a good experiment but needs to be improved as follows.

a) There is a concern that the uracil chase is not effective and this is why some of the mRNAs increase during glucose deprivation relative to actin mRNA. If there is some residual labeling during the chase period, it is difficult to confidently assess how mRNA decay is changing for different classes of mRNAs. Can the authors provide clear data that the chase is robust?

b) The authors should be more cautious in the interpretation that P-body localization affects the stability/storage. In principle, these differences could be due to other regulatory circuits independent of P-bodies. As discussed above, one should be cautious about this point since the majority of mRNA molecules are not in P-bodies at any one time (although they could be cycling in and out in relevant and dynamic manner, which should be clearly stated).

c) It would be appropriate to cite the work of Nissan's group who has recently argued that P-bodies can protect some mRNAs during stress (Huch and Nissan, 2017).

4) The experiments showing Puf5 and the 3' UTR of ATP11 can both affect its concentration in P-bodies and its decay rate raise the possibility that P-body association of this mRNA increases its stability. However, the data could also be interpreted as ATP11 is targeted to P-bodies, and if bound by Puf5, decapping/deadenylation is slowed such that the dwell time within P-bodies is longer and hence more mRNAs at steady state are associated with P-bodies. It would strengthen the manuscript (and be appropriate for publication in a high profile venue like eLife) to resolve this issue particularly also in the light of the observation that the Puf5-independent PB-associated BSC1 mRNA is stabilized in the absence of Puf5. Whether Puf5 affects P-body targeting per se, or decapping within it, could be assessed by measuring the association of ATP11 with P-bodies in puf5∆, dcp1∆, puf5∆ dcp1∆ strains, where the affect of Puf5 on ATP11 in the puf5∆ dcp1∆ should reveal whether it affect targeting of mRNAs into P-bodies or their decay rate once there.

Also, is tethering of Puf5 (via MS2 loops or similar) sufficient for PB localization?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Context-dependent deposition and regulation of mRNAs in P-bodies" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by James Manley as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Roy Parker (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary and Essential revisions:

During the first round of revision, the authors were able to address several concerns that were raised previously, which has improved the manuscript. However, there are some remaining issues that require attention.

1) The reviewers remain unconvinced that the authors specifically purify mRNAs 'enriched in P-bodies', both because of the nature of RNAse treatment before purification, and because the analysis to identify enriched mRNAs relies on comparing the mRNAs associated with Dcp2 or Scd6 without stress, to those associated with these proteins during stress. Thus, the impact is really to identify mRNAs associated with these proteins under different stresses. This is a useful contribution but this point should be clear and be reflected in the wording. For example, reviewer 1 suggests that the authors use wordings such as mRNAs "associated with PB components" instead of "enriched in PBs" throughout the text.

2) The manner by which the enriched mRNAs identified should be shown in a logical flow chart (could be in supplemental). Reviewer 2 asks for this since he is still not sure how the analysis was done and the high similarity between RNA-Seq data sets under all conditions makes him unclear about the statistics. Since all of the manuscript flows from this analysis, it needs to be clear how it was done and what statistical tests were used.

3) The Figure 1 flow chart does not match the written description in the Materials and methods. This adds to the confusion as to how the experiment was done and needs to be clarified.
