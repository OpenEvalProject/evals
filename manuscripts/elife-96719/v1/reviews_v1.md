# Peer review - Round 1

Editors:
- Axel A Brakhage, Hans Knöll Institute Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96719.3.sa0](https://doi.org/10.7554/eLife.96719.3.sa0)

This important study presents a novel pipeline for the large-scale genomic prediction of members of the non-ribosomal peptide group of pyoverdines based on a dataset from nearly 2000 Pseudomonas genomes. The advance presented in this study is based on convincing evidence. This study of bacterial siderophores has broad theoretical and practical implications beyond a singular subfield.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96719.3.sa1](https://doi.org/10.7554/eLife.96719.3.sa1)

The manuscript introduces a bioinformatic pipeline designed to enhance the structure prediction of pyoverdines, revealing an extensive and previously overlooked diversity in siderophores and receptors. Utilizing a combination of feature sequence and phylogenetic approaches, the method aims to address the challenging task of predicting structures based on dispersed gene clusters, particularly relevant for pyoverdines.

Predicting structures based on gene clusters is still challenging, especially pyoverdines as the gene clusters are often spread to different locations in the genome. The revised manuscript has much improved in clarity and reproducibility. I believe that the method is not yet applicable to all NRPS in general and that there is a clear scalability issue when talking about Big Data. However, the method is highly useful for specific NRPS families such as the pyoverdines, so the manuscript presents a useful bioinformatic pipeline for pyoverdine structure prediction, showcasing a commendable exploration of siderophore diversity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96719.3.sa2](https://doi.org/10.7554/eLife.96719.3.sa2)

Pyoverdines, siderophores produced by many Pseudomonads, are one of the most diverse groups of specialized metabolites and frequently used as model systems. Thousands of Pseudomonas genomes are available, but large scale analyses of pyoverdines are hampered by the biosynthetic gene clusters (BGCs) being spread across multiple genomic loci and existing tools' inability to accurately predict amino acid substrates of the biosynthetic adenylation (A) domains. The authors present a bioinformatics pipeline that identifies pyoverdine BGCs and predicts the A domain substrates with high accuracy. They tackled a second challenging problem by developing an algorithm to differentiate between outer membrane receptor selectivity for pyoverdines versus other siderophores and substrates. The authors applied their dataset to thousands of Pseudomonas strains, producing the first comprehensive overview of pyoverdines and their receptors and predicting many new structural variants.

The A domain substrate prediction is impressive, including the correction of entries in the MIBiG database. Their high accuracy came from a relatively small training dataset of A domains from 13 pyoverdine BGCs. The authors acknowledge that this small dataset does not include all substrates, and correctly point out that new sequence/structure pairs can be added to the training set to refine the prediction algorithm. The workflow unfortunately cannot differentiate between different variants of Asp and OHOrn. To validate their predictions, they elucidated structures of several new pyoverdines, and their predictions performed well. The authors tested their workflow on Burkholderiales A domains and had good results, suggesting it can be used on other taxa. Skimming through the source code and data, the algorithm itself appears to be sound and a clear improvement over existing tools for pyoverdine BGC annotation.

Predicting outer membrane receptor specificity is likewise a challenging problem and the authors have made a promising achievement by finding specific gene regions that differentiate the pyoverdine receptor FpvA from FpvB and other receptor families. Their predictions were not tested experimentally, but the finding that only predicted FpvA receptors were proximate to the biosynthesis genes lends credence to the predictive power of the workflow. The authors find predicted pyoverdine receptors across an impressive 468 genera, an exciting finding for expanding the role of pyoverdines as public goods beyond Pseudomonas. However, whether or not these receptors can actually recognize pyoverdines (and if so, which structures!) remains to be investigated.

In all, the authors have assembled a rich dataset that will enable large scale comparative genomic analyses. This dataset could be used by a variety of researchers, including those studying natural product evolution, public good eco/evo dynamics, and NRPS engineering.
