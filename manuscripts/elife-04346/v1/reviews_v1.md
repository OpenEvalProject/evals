# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04346.028](https://doi.org/10.7554/eLife.04346.028)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Linking traits based on their shared molecular mechanisms: A systems phenomics approach” for consideration at eLife. Your article has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing editor, and 2 reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

There is an overall appreciation for methods, such as the proposed GEMOT, that predict causative mutations leading to transcript variations that in turn drive phenotypes. However, to convince that the present method provides an advantage over existing approaches, three additions are required:

1) GEMOT performance should be compared to existing methods. This includes the qtlnet software (PMID 23288936, 21218138, and others) as well as similar methods (PMID 19540336, 21310061, 21242536, 25144184, 15711545, 25114278, 24013639, etc.).

2) Simulations should be used to evaluate the method against a 'truth' standard.

3) With regards to the Klf7 results: a consistent model describing the effect of each allele (B6, DBA, overexpression, knockout) should be presented to provide a clear hypothesis of how Klf7 effect is generated. (The interpretation of the Klf7 effects is unclear in the manuscript. Firstly, what is the nature of variation between the two Klf7 alleles? It has a cis-associated eQTL so, for example, which strain shows higher expression and can be linked to behavioral response to morphine? In the perturbation experiments, what is the strain background? Are the Klf7 knockout and overexpression effects on “driver genes” (up or down-regulation) consistent with corresponding Klf7 expression differences in the BxD population? That is, do Klf7 knockout effects look like a low-expressing Klf7 strain, and do Klf7 overexpression effects look like a high-expressing Klf7 strain? Figure 4 is also confusing as it appears to combine the knockout and overexpression experiments into summary scores. It would be useful to clearly see how these data support the inferred BxD model.)

4) The manuscript would be more convincing if the authors identify a group of traits that show low Pearson correlation among themselves, but share the same driver genes.

5) Considering the many methods already available (see above), the motivation for the present study should be better clarified.

6) The manuscript can be difficult to read at times, primarily due to a reliance on its own jargon. In some cases new nomenclature might be necessary, but many of the new terms seem to be very similar (if not identical) to widely-used, existing terms. In such cases, the paper should conform to standard nomenclature or define why such standards will not suffice. Notable examples are: “variant-gene associations” instead of eQTL; “linked relationships” instead of Pearson correlation and “link potential” instead of averaged correlation; “bipartite module” instead of pleiotropy. Furthermore, “gene drivers” and the “drivers layer” can probably be more simply referred to as “transcripts” and a “transcript layer” with appropriate context. “Causality score” appears to be a P value; why not refer to it as such? In some cases the new nomenclature can be potentially misleading, such as in the Klf7 discussion where a P value is referred to as a “perturbation effect”. Effect size and significance are different concepts with different biological interpretations.

7) High-dimensional approaches like GEMOT are prone to generating false positive associations, especially in such small experimental populations. Are P values systematically corrected for multiple tests? It is also important to estimate false discovery rates for a given significance threshold, which are not addressed in the manuscript. Additionally, the sample size in this study is very small, and BxD lines often exhibit non-local linkage disequilibrium due to limited recombination across few individuals. This can lead to many false-positive associations. How has this potential issue been addressed in the current study?
