# Peer review - Round 1

Editors:
- Simon G Sprecher, University of Fribourg Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29593.016](https://doi.org/10.7554/eLife.29593.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Natural variation in stochastic photoreceptor specification and color preference in Drosophila" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Simon Sprecher as Guest Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Stein Aerts (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study addresses how stochastic gene expression may be modulated by investigating the impact of a naturally occurring variation in the spineless locus. Identification of a single base pair insertion that may change the binding of the transcription factor Klumpfuss. The presence of the sin variance shifts the ratio two ommatida types as well as the behavioural preference between blue and green light. These findings provide insight into how inter-individual differences in nervous system architecture and behaviour may arise.

Essential revisions:

While the manuscript was perceived positively there are however a few points that should be addressed. As you will see from the points depicted below a main point from several sides concerns the putative mechanistic link between klu, the sin locus and Ss expression. More direct evidence for the altered expression of Ss by the sin locus or klu binding to variants of the sin locus would help to resolve this criticism.

1) The hypothesis drawn by the authors is that Klu represses Ss expression in R7 cells. It would be helpful to examine expression levels of Ss in R7 cells in Klu mutants and animals with increased Klu.

2) The authors claimed that Klu was expressed in R7 cells of the larval eye disc at 'intermediate levels' and altering Klu levels changed the SsON/SsOFF ratio. Can this intermediate level of Klu be quantified? It appears in Figure 4B that endogenous klu is differentially expressed in R7 cells.

3) The authors used bioinformatics to analyze available SELEX-seq binding data sets from Nitta, et al. 2015 and concluded that sin increased the binding affinity for Klu based on the enrichment of the number of reads obtained with sin. Since this was solely based on in vitro data on a randomized set of DNA with N-terminal thioredoxin-HIS tag fusion proteins, a more thorough characterization is necessary to confirm this claim. Would the same tagged-Klu expressed in vivo rescue SsON/SsOFF photoreceptor ratio in Klu null? The authors should further demonstrate altered DNA binding affinity for Klu using a specific DNA probe with or without sin in EMSA assays.

4) The insertion of a C does not seem to affect the core Klu binding site, but rather a flanking nucleotide, and this binding site is a CA rich stretch where an extra C is added (CGCCCACACA to CGCCCACACCA). The authors argue that this may change the affinity of Klu binding. Given that Klu is expressed in the R7, and that perturbations of Klu phenocopy sin, this is a plausible explanation. Nevertheless, no experimental validation is provided to show that Klu actually binds to this region and that the binding is affected by the insertion. I realise that ChIP-seq is difficult given the limited amount of material. Can another experiment be thought of? If not, can this be argued in the text – that this evidence is indirect, and no formal proof is provided that Klu binding in vivo is affected by this insertion. The authors provide surrogate evidence that Klu SELEX-seq is biased towards CGCCCACACCA sequences having sin; this is interesting but it is not convincing to me, because the SELEX logo's do not contain this flanking site, rather they suggest Klu binds to CGCCCACGCA. This is quite different from the site with sin (notice the trailing GCA). Given the very high conservation of a 17 bp stretch that contains a match to Klu, an alternative hypothesis is that actually two (or even more) transcription factors may bind to this 17bp stretch, perhaps Klu together with another factor, and that sin affects binding of the other, yet unknown factor, rather than of Klumpfuss. Klu perturbations would still affect Ss expression in that scenario, but not because of differential affinity with the site, but simply because Klu regulates Ss (in other words, Klu perturbations are not performed with a sin comparison, so they merely confirm that Klu regulates Ss). A possible experiment would be to perform the Klu perturbations with and without the sin insertion. Or to clone this region near an enhancer-reporter construct that activates a reporter, for example, in S2 cells (a strong enhancer that is active in S2 cells, many are known). Given the prediction of Klu-mediated repression, it can be investigated whether the reporter can be repressed by the sin-encompassing region, when transfecting with Klu cDNA, and whether this effect is changed between the wild type and the sin containing sequence. in vivo this would obviously be better, but would require more time. I am aware such experiments are challenging, so other experiments can be proposed by the authors, or if they are not possible given the limited time, the lack of formal evidence what this insertion does, and alternative hypotheses, should be discussed thoroughly (perhaps with a figure/cartoon).

5) Given that the Klu binding site is not very informative (lots of C's), how significant is the prediction that this is a Klu binding site? On 100 random genes with similar size as Ss, how many Klu matches are found? Can this be reported? Does the score change when sin is included? That is, does the Klu PWM score increase with sin compared to control/null sites – likely not because sin is not present in the PWM, correct? Can this be discussed in the paper. This is important because the PWM is a measure for the binding affinity, which is argued to be increased with sin, so the PWM score should change (significantly?).

6) It is written "As sin increases Klu binding affinity" – can this be changed into "As sin is predicted to increase Klu binding affinity"?

7) The role of the encompassing genomic region, how it is involved in the regulation of Ss, is not investigated – is this a new regulatory element of Ss? Are there any Janelia Flylight or VDRC tiles overlapping this region? If not, please discuss this. If there is time to clone this region into an enhancer-reporter and create a transgenic fly, that would be informative. If Flylight/VDRC lines are available, can they be tested with UAS-GFP to investigate whether this region is actually an Ss enhancer.
