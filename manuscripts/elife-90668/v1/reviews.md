# Peer review - Round 1

Editors:
- Marisa Nicolás, Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90668.3.sa0](https://doi.org/10.7554/eLife.90668.3.sa0)

This study presents valuable findings on core genome mutations that might have driven the emergence of the Staphylococcus aureus lineage USA300, a frequent cause of community-acquired infections. The authors present a solid novel approach that combines genome-wide association studies and RNA-expression analyses, both applied to extensive publicly available datasets. This approach generated an intriguing hypothesis that should be validated experimentally. The work will interest microbiologists working in genomic epidemiology and phenotype-genotype association studies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90668.3.sa1](https://doi.org/10.7554/eLife.90668.3.sa1)

Summary:

This is large-scale genomics and transcriptomics study of the epidemic community-acquired methicillin-resistant S. aureus clone USA300, designed to identify core genome mutations that drove the emergence of the clone. It used publicly available datasets and a combination of genome-wide association studies (GWAS) and independent principal-component analysis (ICA) of RNA-seq profiles to compare USA300 versus non-USA300 within clonal complex 8. By overlapping the analyses the authors identified a 38bp deletion upstream of the iron-scavenging surface-protein gene isdH that was both significantly associated with the USA300 lineage and with a decreased transcription of the gene.

Strengths:

Several genomic studies have investigated genomic factors driving the emergence of successful S. aureus clones, in particular USA300. These studies have often focussed on acquisition of key accessory genes or have focussed on a small number of strains. This study makes a smart use of publicly available repositories to leverage the sample size of the analysis and identify new genomics markers of USA300 success.

The approach of combining large-scale genomics and transcriptomics analysis is powerful, as it allows to make some inferences on the impact of the mutations. This is particular important for mutations in intergenic regions, whose functional impact is often uncertain.

The statistical genomics approaches are elegant and state-of-the-art and can be easily applied to other contexts or pathogens.

Weaknesses:

The main weakness of this work is that these data don't allow a casual inference on the role of isdH in driving the emergence of USA300. It is of course impossible to prove which mutation or gene drove the success of the clone, however, experimental data would have strengthen the conclusions of the authors in my opinion.

Another limitation of this approach is that the approach taken here doesn't allow to make any conclusions on the adaptive role of the isdH mutation. In other words, it is still possible that the mutation is just a marker of USA300 success, due to other factors such as PVL, ACMI or the SCCmecIVa. This is because by its nature this analysis is heavy influenced by population structure. Usually, GWAS is applied to find genetic loci that are associated with a phenotype and are independent of the underlying population structure. Here, authors are using GWAS to find loci that are associated with a lineage. In other words, they are simply running a univariate analysis (likely a logistic regression) between genetic loci and the lineage without any correction for population structure, since population structure is the outcome. Therefore, this approach can't be applied to most phenotype-genotype studies where correction for population structure is critical.

Finally, the approach used is complex and not easily reproduced to another dataset. Although I like DBGWAS and find the network analysis elegant, I would be interested in seeing how a simpler GWAS tool like Pyseer would perform.
