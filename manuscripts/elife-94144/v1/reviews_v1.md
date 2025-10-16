# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94144.3.sa0](https://doi.org/10.7554/eLife.94144.3.sa0)

This study provides valuable new insights into the trade-offs associated with the evolution of drug resistance in the yeast S. cerevisiae, based on a solid approach to evolving and phenotyping hundreds of independent strains. The authors identify distinct phenotypic clusters, defined by their growth across defined conditions, which suggest that tradeoffs are diverse but at the same time could be limited to a few classes according to the underlying resistance mechanisms. The methodologies used align with the current state-of-the-art, and the data and analysis are solid as they broadly support the claims, with only a few minor weaknesses remaining after revision. This work will interest molecular biologists working on the evolution of new phenotypes and microbiologists studying multi-drug therapy.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94144.3.sa1](https://doi.org/10.7554/eLife.94144.3.sa1)

Summary:

In their manuscript, Schmidlin, Apodaca et al try to answer fundamental questions about the evolution of new phenotypes and the trade-offs associated with this process. As a model, they use yeast resistance to two drugs, fluconazole and radicicol. They use barcoded libraries of isogenic yeasts to evolve thousands of strains in 12 different environments. They then measure the fitness of evolved strains in all environments and use these measurements to enumerate patterns in fitness trade-offs. They identify only six major clusters corresponding to different trade-off profiles, suggesting the vast genotypic landscape of evolved mutants translates to a highly constrained phenotypic space. They sequence over a hundred evolved strains and find that mutations in the same gene can result in different phenotypic profiles.

Overall, the authors deploy innovative methods to scale up experimental evolution experiments, and in many aspects of their approach tried to minimize experimental variation.

Weaknesses:

(1) The main objective of the authors is to characterize the extent of phenotypic diversity in terms of resistance trade-offs between fluconazole and radicicol. To minimize noise in the measurement of relative fitness, the authors only included strains with at least 500 barcode counts across all time points in all 12 experimental conditions, resulting in a set of 774 lineages passing this threshold. As the authors remark, this will bias their datasets for lineages with high fitness in all 12 environments, as all these strains must be fit enough to maintain a high abundance. One of the main observations of the authors is phenotypic space is constrained to a few clusters of roughly similar relative fitness patterns, giving hope that such clusters could be enumerated and considered to design antimicrobial treatment strategies. However, by excluding all lineages that fit in only one or a few environments, they conceal much of the diversity that might exist in terms of trade-offs and set up an inclusion threshold that might present only a small fraction of phenotypic space with characteristics consistent with generalist resistance mechanisms or broadly increased fitness. The general conclusions of the authors regarding the evolution of trade-offs might thus be more focused on multi-drug resistant phenotypes.

(2) Most large-scale pooled competition assays using barcodes are usually stopped after ~25 to avoid noise due to the emergence of secondary mutations. The authors measure fitness across ~40 generations, which is almost the same number of generations as in the evolution experiment. This raises the possibility of secondary mutations biasing abundance values, which would not have been detected by the whole genome sequencing as it was performed before the competition assay. Previous studies approximated the fraction of lineages that could be overtaken by secondary mutations (Venkataram and Dunn et al 2016). In their calculations, Venkataram and Dunn et al defined adaptive mutations in their data as having a selection coefficient of 5% and highly adaptive mutations at around 10%. From this and an estimation of the mutation rate, they estimate that the fraction of lineages overtaken by adaptive mutations is negligible (10^4) after 32 generations. However, the effects on fitness observed by the authors here tend to be much stronger than 5-10%, with relative fitness advantages above 1 and often reaching 2. This could result in a much higher chance of lineages being overtaken at 40 generations.

(3) The approach used by the authors to identify and visualize clusters of phenotypes among lineages does not seem to consider the uncertainty in the measurement of their relative fitness. As can be seen from Figure S4, the inter-replicate difference in measured fitness can often be quite large. From these graphs, it is also possible to see that some of the fitness measurements do not correlate linearly (ex.: Med Flu, Hi Rad Low Flu), meaning that taking the average of both replicates might not be the best approach. Because the clustering approach used does not seem to take this variability into account, it becomes difficult to evaluate the strength of the clustering, especially because the UMAP projection does not include any representation of uncertainty around the position of lineages.

(4) The authors make the decision to use UMAP and a Gaussian mixed model as well as validation data to identify unique clusters, which is one of their main objectives. The choice of 7 clusters as the cutoff for the multiple Gaussian model is not well explained. Based on Figure S6A, BIC starts leveling off at 6 clusters, not 7, and going to 8 clusters would provide the same reduction as going from 6 to 7. This choice also appears arbitrary in Figure S6B, where BIC levels off at 9 clusters when only highly abundant lineages are considered. All of the data presented in the validations is presented to fit within the 6 clusters structure but does not include evidence against alternative scenarios for additional relevant clusters as might be suggested by Figure S6.

(5) Large-scale barcode sequencing assays can often be noisy and are generally validated using growth curves or competition assays. Reconstructing some of the specific mutants they identified to validate their phenotypes would also have been a good addition. If the phenotypic clusters identified cannot be reproduced outside of the sequencing assay, then their relevance are they as a model for multi-drug resistance scenarios might be reduced.
