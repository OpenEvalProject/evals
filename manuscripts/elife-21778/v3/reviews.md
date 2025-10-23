# Peer review - Round 1

Editors:
- Gilean McVean, Oxford University , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21778.051](https://doi.org/10.7554/eLife.21778.051)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Non-coding cancer driver candidates identified with a sample- and position-specific model of the somatic mutation rate" for consideration by eLife. Your article has been favorably evaluated by Aviv Regev (Senior Editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: David C Wedge (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper introduces a statistical method for detecting non-coding driver mutations in cancer data. It is applied to a modest pan-cancer genome data set (505 tumour-normals). The method recovers some known driver mutations (both coding and non-coding) and identifies a number of other candidates, some of which have corroborative evidence from gene expression and/or survival data. The identification of non-coding driver mutations is an important and unsolved problem that will be of growing importance as whole genome sequence data sets accumulate.

Essential revisions:

1) The method needs to be compared to other approaches (e.g. the Gerstein group approach) for identifying non-coding driver mutations. Given the computational cost of the new approach, it is important to demonstrate that it leads to a substantial advance in precision compared to simpler methods.

2) The Bertl et al. paper referred to as in preparation that describes the method needs to be made accessible – e.g. on a preprint site. Without this, important aspects of the approach cannot be fully assessed. Ideally, this would be combined with the current paper to make a coherent piece of work.

3) The COSMIC protein-coding driver mutation analysis is worrying. It suggests that at q=0.25, only 16% of driver mutations identified are in COSMIC. Given the relatively small size of the dataset used here (compared to the very large exome data sets represented in COSMIC), the 84% of 'drivers' that are not known need to be investigated further. E.g. are there additional mutation-rate varying factors that are relevant for protein-coding mutations?

4) Mutation rate is strongly affected by chromatin state (e.g. Polak, Nature Biotech, 2014) and this should be added as a co-variate. Further, it's unclear whether the model takes into account the sample-specific mutational signature. For example, the probability of TCW→TTW and TCW→TGW mutations is much greater in samples prone to APOBEC-induced mutational processes, particularly in regions of kataegis.

5) It is unclear how the scoring systems are used within the model. The probability of each mutation under a null model seems to be calculated without using the scores and the Q-Q analysis is conducted without apparent use of the scores, so it is not clear how 3 different sets of significant genes are identified.
