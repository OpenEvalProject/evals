# Peer review - Round 1

Editors:
- Blake Wiedenheft, https://ror.org/02w0trx84 Montana State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81897.sa0](https://doi.org/10.7554/eLife.81897.sa0)

CRISPR-Cas systems are essential components of an adaptive immune system that protects bacteria and archaea from infection of foreign genetic elements like phages and plasmids. The work presented here demonstrates that some CRISPR systems (i.e., type III-A) rely on host nucleases (i.e., RNase R and PNPase) for faithful processing of CRISPR RNAs into short mature CRISPR RNA (crRNAs) that are required for defense. Collectively, this work expands our fundamental understanding of degradosome-associated nucleases, and their contribution to the adaptive immune response in bacteria.


---

# Peer review - Round 1

Editors:
- Blake Wiedenheft, https://ror.org/02w0trx84 Montana State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81897.sa1](https://doi.org/10.7554/eLife.81897.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Critical roles for 'housekeeping' nucleases in Type III CRISPR-Cas immunity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Bavesh Kana as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Based on results in Figure 1E, the authors claim "RNase R alone causes complete loss of precisely-processed mature species and production of crRNAs with a range of aberrant lengths, as well as moderate accumulation of 71 nt intermediates." However, the "moderate accumulation of 71 nt intermediates" is very weak, not quantified, and is not supported by the complementation assay of rnr, which has more 71 nt intermediates than either the WT or the deletion mutant. Quantify data and modify claims for accuracy.

2. Add the Ni-affinity purified Cas10-Csm complex from LM1680/(△pnp/△rnr) cells on the gel presented in Figure 2B.

3. The authors rely on gel shifts to show a physical association between RNase R and Csm5. However, Csm5 doesn't enter the gel for reasons explained by the π and RNase R oligomerizes in a concentration-dependent manner. These factors complicate the interpretation of the gel shift. The authors should complement the gel shift with an alternative method. One referee suggests adding a tag to Csm5 that can be detected by Western blot the other suggests isothermal titration calorimetry (ITC). Acceptance for publication does not require a physical interaction but testing this interaction using an alternative method is required.

4. The authors used the structure of S. thermophilus Csm5 to guide their design of truncations to probe potential intrinsically disordered regions (IDR1 and IDR2) that may be sites of interaction with PNPase or RNase R. Since the authors submitted their manuscript, an AlphaFold predicted structure of the S. epidermidis Csm5 has been released on the AlphaFold Protein Structure Database. In this model, the IDR2 region is predicted by AlphaFold to be a β strand at the center of a β sheet, rather than a disordered region. If the prediction is accurate, deletion of this strand could cause Csm5 to misfold, making it difficult to interpret what causes loss of interaction with PNPase (i.e. deletion of a specific interaction surface versus misfolding of the overall tertiary structure). In light of this, the discussion surrounding these experiments should be altered to include more caveats about the truncations, and conclusions based on this experiment should be softened.

Reviewer #1 (Recommendations for the authors):

1. It is possible with the AlphaFold structural model of S. epidermidis Csm5 (or using AlphaFold Multimer) that the authors may be able to design more conservative truncations or point mutations that block the interaction between PNPase and Csm5. While AlphaFold only provides a structural prediction and should be taken with a grain of salt, this particular sequence is predicted with high confidence, which has generally been found to provide highly accurate structural models. This may therefore be a better alternative to mapping potential interaction regions than comparing to an ortholog that could have gaps/insertions in comparison to the sequence of interest.

2. For the native gels testing an interaction between Csm5 and RNase R, have the authors tested whether Csm5 is present in the shifted band (e.g. by adding a tag to Csm5 and performing a Western blot)? This would substantially strengthen the conclusions that could be drawn from this experiment.

3. In the Discussion section, the authors compare PNPase and RNase R requirements to that of Csm6, stating that all three appear to be dispensable for phage defense when targeting high-abundance transcripts. Have the authors tested anti-phage activity upon deletion of RNase R and PNPase in a strain lacking Csm6? If the three nucleases act synergistically, it is possible that deletion of all three may reduce the anti-phage activity that is not affected in strains lacking csm6 or pnp/rnr. Although I understand this is a lot to ask using the strain with an endogenous CRISPR-Cas locus, this experiment could potentially be done using the Lm1680 strains bearing pcrispr-cas in which csm6 is deleted.

Reviewer #2 (Recommendations for the authors):

Based on results in Figure 1E, the authors claim "RNase R alone causes complete loss of precisely-processed mature species and production of crRNAs with a range of aberrant lengths, as well as moderate accumulation of 71 nt intermediates." However, the "moderate accumulation of 71 nt intermediates" is very weak, not quantified, and is not supported by the complementation assay of rnr, which has more 71 nt intermediates than either the WT or the deletion mutant. Consider revising these statements for accuracy. The addition of deep sequencing would help clarify the identity of these intermediate RNA species and explain the role of RNase R in moving these intermediate RNAs into the mature fraction.

The authors should consider adding deletions of pnp alone to Figure 1, so readers can make a direct comparison between rnr and rnr/pnp double mutants. A pnp complementation (△pnp:: pnp*), and pnp/rnr complementation (△pnp/△rnr:: pnp*/rnr*) should also be added for the same reasons (i.e., side-by-side comparisons).

The authors should consider running the Ni-affinity purified Cas10-Csm complex from LM1680/(△pnp/△rnr) cells on the gel presented in Figure 2B.

The authors rely on gel shift to show a physical association between RNase R and Csm5. However, Csm5 doesn't enter the gel for reasons explained by the π and RNase R oligomerizes in a concentration dependent manner. These factors complicate the interpretation of the gel shift. The authors should consider complementing the gel shift with an alternative method (i.e., ITC) that would enable a quantitative measure of the binding affinity.

The authors speculate "that both nucleases may be recruited by the same/overlapping binding site(s) on Csm5, with one or the other allowed to occupy the site at any given time. Such transient and dynamic interactions are known to occur with proteins." In figure 2 the authors test either or both nucleases, but it may work testing one, then the other, to determine if the order of addition impacts RNA length or efficiency of processing.

"The results showed that while Csm5△46 maintains its interaction with RNase R (Figure 5—figure supplement 1)," The migration of the proteins is modest and complicated by the high PI. These experiments would benefit from another technique that provides a more quantifiable metric.

"striking stimulation of PNPase's nucleolytic activity occurs (Figure 5C)." I do not disagree that there is some stimulation, but it may not be as strike to some readers as it is to these authors. I recommend quantifying these data.
