# Peer review - Round 1

Editors:
- Richard M White, Memorial Sloan Kettering Cancer Center United States

Reviewers:
- Craig Ceol
- Ian J Jackson, MRC Human Genetics Unit, IGMM United Kingdom

## Review text

DOI: [10.7554/eLife.45181.039](https://doi.org/10.7554/eLife.45181.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Thyroid hormone regulates distinct paths to maturation in pigment cell lineages" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Didier Stainier as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Craig Ceol (Reviewer #2); Ian J Jackson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript defines how thyroid hormone has opposite effects on the abundance of melanophores and xanthophores during adult zebrafish pigment pattern development. The authors originally hypothesized that the imbalance in pigment cell lineages found in hypothyroid zebrafish is caused, in one model, by an amplification of one cell type at the cost of the other during cell-fate specification. In an alternative model, they hypothesized that thyroid hormone has discordant affects on a particular cellular behavior in both lineages. Thus, a perturbation in thyroid hormone function would result in the observed melanophore excess and xanthophore deficit seen in hypothyroid fish. In order to test these hypotheses, the authors used single-cell sequencing to profile thousands of neural crest-derived cells and reconstructed pigment cell developmental trajectories in pseudotime. A comparison of the euthyroid and hypothyroid trajectories revealed a buildup of both immature melanophores and xanthophores, which was incongruent with their first two models and caused the authors to seek another explanation. Utilizing their scRNA-Seq data, they investigated differentially expressed genes in melanophores and found that maturation genes were expressed at lower levels in hypothyroid fish when compared to euthyroid fish. Based on this transcriptional finding, the authors found that some euthyroid melanophores have greater staining for senescence markers when compared to hypothyroid melanophores. In analyzing the xanthophore lineage, the authors found that genes involved with carotenoid pigment production are differentially expressed between hypothyroid and euthyroid xanthophores. In support of this transcriptional finding they utilized a carotenoid mutant to show that immature xanthophores are still present but unable to mature. The authors combined these analyses to construct a new model in which thyroid hormone drives maturation of both adult xanthophores and melanophores, but via independent mechanisms. More broadly, the study provides a wealth of new markers and data for identifying distinct populations of pigment cell classes, which are likely to be of use beyond the zebrafish alone. Overall, the study is well executed and well presented to a non-computational audience.

Essential revisions:

1) Pigment cell subtypes

– In Figure 3, could the authors better explain exactly what differentiates the subtype classifications, i.e. mel1 vs. mel2; is there a morphological difference between these cell types that can be seen by ISH? Is there any possibility that the mel1 vs. mel2 states stratifies against binuclearity?

2) Binucleate cell state

Several issues were raised around these claims:

– In Figure 3—figure supplement 1, it is shown that certain cell types have lower transcriptional activity (i.e. mel2, xan1). In the scRNA-Seq method, how do you account for transcript abundance in relation to the fact that some of the cells being sequenced are binucleate whereas some are mononuclear? This seems like it would confound the transcript counts if this is not accounted for. A better explanation of this or experiments to demonstrate this is not the case would be helpful.

– The relationship between binuclear status and senescence in melanophores is tenuous. Previous literature (including Usui et al., 2018) states that binuclear melanophores are frequently the result of failures in cell division. The authors should carefully clarify the relationship between melanophore maturation, senescence, and binuclear status.

– Understanding the mechanisms of how the cell transitions from uni- to binuclearity would be useful. Are there correlations from the scRNA data that might be candidate mechanisms by which this could occur? Even if correlative, it would be helpful for future studies in the field.

3) The TR experiments

– For the unliganded TR receptors to suppress gene expression, are there markers that mediate this repression that you could show occurs in the hypothyroid fish? This would add strength to the genetic argument that the unliganded state is the correct mechanism. Does the unliganded receptor repress the same genes that the receptor + TH activate?

– The authors should display phenotype data from a thrab(lf);thraa(lf);thrb(lf) triple mutant. The authors observe no overt pigment defects in thraa, thrab, and thrb single knockouts as well as in the thraa(lf);thrab(lf) double knockout, however, to completely conclude that TR mutants don't have a pigment defect the authors should also include the thrb null allele. It is possible that in the thraa(lf);thrab(lf) mutant doesn't have a phenotype because Thyroid Receptor Β is compensating for their loss and mediating thyroid signaling. This concern also applies to the modest rescue seen in Figure 7B-D. A triple mutant may yield a full rescue of the xanthophore population. Imaging and subsequent quantification of the triple mutant would strengthen the authors' interpretations.

4) Senescence

– The authors need to improve the evidence behind their claim that senescence is promoted by thyroid hormone during melanophore maturation. SA-β-Gal is the gold-standard assay for senescence, and while the authors perform SA-β-Gal on euthyroid and hyperthyroid melanophores, they do not quantify the results. Therefore, it is not clear whether the one cell shown represents any appreciable fraction of euthyroid melanophores. Lysotracker is used as a secondary assay to support this idea, but increased lysotracker staining is not a specific feature of senescent cells and is more associated with autophagy. The authors need to bolster their claim that thyroid hormone promotes senescence by quantifying SA-β-Gal and investigate other well-accepted ways to corroborate cellular senescence, e.g. p16 expression.
