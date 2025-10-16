# Peer review - Round 1

Editors:
- Daniel Zilberman, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17082.052](https://doi.org/10.7554/eLife.17082.052)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the paper was accepted for publication after the authors resubmitted for further consideration.]

Thank you for choosing to send your work entitled "5-hydroxymethylcytosine marks regions with reduced mutation frequency" for consideration at eLife. Your full submission has been evaluated by Diethard Tautz (Senior editor) and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers.

Based on our discussions and the individual reviews below, we felt that your manuscript requires major alterations that are unlikely to be accomplished within the time frame typically allotted for revised eLife manuscripts. We therefore regret to inform you that your work, in its present form, will not be considered further for publication in eLife. However, we would be happy to consider a new submission if you can demonstrate that 5hmC causes a strong and general reduction of C>T mutations associated with 5mC.

Reviewer #1:

The main claim of the manuscript is that hydroxylation of methylcytosine (hmC) lowers the C>T transition rate of methylated cytosine (mC) in brain (cancer) cells approximately 2-fold. The authors support this claim by re-analyzing published data for the localization of DNA hydroxymethylation (BS/TAB-Seq in normal brain tissue, Wen et al., Genome Biol 2014) and for substitution rates (inferred from brain cancers, Alexandrov et al., Nature 2013). The phenomenon of less elevated transition rates in lineages leading to cancer at hydroxymethylated bases in normal brain cells is somewhat supported, but support would be bolstered by additional analyses.

Overall, the paper appears methodologically sound, but I am concerned by discrepancies with published data, and the biology doesn't quite add up. A paper published last year and cited here (Supek at al., PLoS Genetics 2014) reported elevated levels of C>G transversions associated with hmC in human and mouse. The same paper also found modest but significant reduction of C>T transitions in both species, interpreted as an expected outcome of the chemical differences between hmC and mC. This important result isn't mentioned by the authors, who report a much greater reduction – the main novel finding of this paper. Unlike the published result, the authors' analysis relies on a single human brain hmC dataset, and the substitution rates in cancer lineages are not obviously matched to bulk modification levels of an individual brain. Although the authors claim the matching of datasets is a strength of their analysis, it is actually somewhat of a weakness because the samples are not directly comparable.

It is noted that "all brain cancer types individually displayed a significant (28-53%) reduction of C>T mutations in 5hmChigh sites (Figure 1E,F), making it highly improbable that the observation is an artefact of tissue type or sequencing method", however a similar result across the board makes it suspect of a systematic artifact, potentially caused by reliance on a single hmC dataset. I think it is very important for the authors to perform their analyses with additional hmC datasets.

I find the author's functional claims problematic. hmC modification decreases in most cancer lineages measured (Ficz and Gribben, Genomics 2014), so how can hmC continue to lower mutation rates if it is increasingly lost in the proliferating cancer cells? Even if it were only acting early in cancer development when hmC would presumably still be high, wouldn't its mutational signature be quickly overwhelmed by subsequent mutations occurring on non-hydroxymethylated cytosines? Furthermore, the most mitotically active cells, neuronal progenitors and neural stem cells, have the least hmC (Wen and Tang, Genomics 2014) – yet, aren't these thought to be more likely to give rise to the cancer lineages?

More generally, the argument that elevated hmC protects long-lived cells like neurons is odd, because these cells are not in obvious need of special protection from mutations. Mutations have the greatest potential for harm when arising in cells that give rise to many other cells. Primary adult brain tumors overwhelmingly arise from glial cells. Elevated levels of hmC in long-lived cells would seem to argue against a function in reducing mutations, or at least not for such a function.

Reviewer #3:

General Assessment

The authors analyze the relationship between the distribution of hydroxymethylation and mutational patterns in brain cancer exomes and whole genomes. Authors make a nice effort to collect a large sample size of brain cancer samples. The paper is well written and I do not see any major methodological pitfall in most of their analyses. However, I am skeptical about the generality about their findings, and also feel that some of their claims should be toned down or strengthened by additional analyses.

1) The title and some of the Discussion indicates that the findings in this paper may represent a universal mutational trend. However, their findings clearly cannot be generalized to all somatic mutations. In this respect the title should be changed to specify that the patterns were observed in brain cancers.

Specifically, if 5hmC is intrinsically linked to lower C>T mutability, this pattern should be also observed in other cancer types as well as in non-cancer context. As cited in this paper, reduced C>T pattern was not consistently observed in a previous study (Supek et al.) using population variation and SNPs from several cancer types. Authors mention that this discrepancy is due to specific 5hmC patterns of each tissue. However, to claim that C>T mutation is universal authors need to discard specific mutational biases in brain cancer. For example, one might come up with an alternative explanation that the repair machineries for 5mC mismatch is specifically impaired in brain cancers, and consequently they are highly mutable in these specific cell types. A scenario such as this can be easily tested by comparing expression patterns of genes involved in 5mC and 5hmC repair machineries for different cell types. Second, it might be necessary to confirm that the discrepancies are not because of different methodological approaches. Authors could follow 5hmC – 5mC context matching procedure from the previous study and/or analyze population-based SNP data themselves. Finally, even though germline 5hmC maps are not yet available, one can infer those patterns using the existing maps and using the principles of parsimony. For example, the cytosines that are hydroxymethylated in both ESC and a differentiated tissue such as cortex may be inferred to be hydroxymethylated in germline and should associate with less C>T SNP at the population level (having a larger number of 5hmC maps would increase the confidence of the inference). In contrast, brain-specific 5hmC (5mC in ESC) are expected to show less C>T mutations in brain cancers, but more C>T at population-level (since these positions are expected to be 5mC in germlines).

2) In addition, it is stated in the Abstract that the levels of 5hmC have 'predictive' power for mutation frequencies, in particular non-synonymous mutation frequencies. However, without the total R2 of the model it is impossible to judge the predictive power of their models. Moreover, the differences in R2 of models including or excluding 5hmC levels are so small (in the other of 1/1000th, per Figure 4A), it is a stretch to state that the '5hmC levels are predictive of lower non-synonymous mutation frequency' (as in the Abstract).

3) The authors conjecture that a potential (additional) role of hydroxymethylation may be to 'protect' some cell types from mutations. The authors relate to the abundance of hydroxymethylation in long-lived neurons and such a potential role. However, as authors acknowledge in the Discussion, this must be taken with caution since the biological significance as well as tissue-wide distribution of hydroxymethylation is still poorly understood. Authors might also acknowledge that an additional caveat of this work is that the sample studied is heterogeneous. The frontal cortex is composed of not only long-lived neurons but also shorter-lived glial cells. To directly test their hypothesis, it might be necessary to compare sorted cell types with close developmental origin and biological function but with different division rates.

4) Regarding the analysis on driver genes, authors show that cancer driver genes show more 5hmC/total methylated than non-drivers genes. I feel this analysis alone is not sufficient to delineate the relationship between 5hmC and occurrence of cancer driver mutations.

The comparison between drivers and non-drivers might not be fair, since they might show different mutation rates in cancer. To test the role of 5hmC in genome stability and progression in cancer, would not it be more relevant to test if drivers are enriched for 5hmC compared to passenger genes (i.e., genes that also accumulate mutations in cancer, while not as drivers)?

If the presence of 5hmC is linked to low mutability at key genes, a testable prediction using ESC 5hmC map would be to show that the genes that are active in development show enrichment for 5hmC.
