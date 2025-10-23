# Peer review - Round 1

Editors:
- Sergio Rasmann, University of Neuchâtel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95510.3.sa0](https://doi.org/10.7554/eLife.95510.3.sa0)

This important study presents a significant methodological advance by leveraging previously discarded, unmapped DNA sequence reads to estimate pest infestation loads across plant accessions, and map variation in these apparent pest loads to defense genes. The bioinformatics approach is compelling, and the results should bear broad implications for phenotype-genotype prediction, especially regarding the use of unmapped reads for GWAS.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95510.3.sa1](https://doi.org/10.7554/eLife.95510.3.sa1)

Galanti et al. present an innovative new method to determine the susceptibility of large collections of plant accessions towards infestations by herbivores and pathogens. This work resulted from an unplanned infestation of plants in a greenhouse that was later harvested for sequencing. When these plants were extracted for DNA, associated pest DNA was extracted and sequenced as well. In a standard analysis, all sequencing reads would be mapped to the plant reference genome and unmapped reads, most likely originating from 'exogenous' pest DNA, would be discarded. Here, the authors argue that these unmapped reads contain valuable information and can be used to quantify plant infestation loads.

For the present manuscript, the authors re-analysed a published dataset of 207 sequenced accessions of Thlaspi arvense. In this data, 0.5% of all reads had been classified as exogenous reads, while 99.5% mapped to the T. arvense reference genome. In a first step, however, the authors repeated read mapping against other reference genomes of potential pest species and found that a substantial fraction of 'ambiguous' reads mapped to at least one such species. Removing these reads improved the results of downstream GWAs, and is in itself an interesting tool that should be adopted more widely.

The exogenous reads were primarily mapped to the genomes of the aphid Myzus persicae and the powdery mildew Erysiphe cruciferarum, from which the authors concluded that these were the likely pests present in their greenhouse. The authors then used these mapped pest read counts as an approximate measure of infestation load and performed GWA studies to identify plant gene regions across the T. arvense accessions that were associated with higher or lower pest read counts. In principle, this is an exciting approach that extracts useful information from 'junk' reads that are usually discarded. The results seem to support the authors' arguments, with relatively high heritabilities of pest read counts among T. arvense accessions, and GWA peaks close to known defence genes. Nonetheless, I do feel that more validation would be needed to support these conclusions, and given the radical novelty of this approach, additional experiments should be performed.

A weakness of this study is that no actual aphid or mildew infestations of plants were recorded by the authors. They only mention that they anecdotally observed differences in infestations among accessions. As systematic quantification is no longer possible in retrospect, a smaller experiment could be performed in which a few accessions are infested with different quantities of aphids and/or mildew, followed by sequencing and pest read mapping. Such an approach would have the added benefit of allowing causally linking pest read count and pest load, thereby going beyond correlational associations.

On a technical note, it seems feasible that mildew-infested leaves would have been selected for extraction, but it is harder to explain how aphid DNA would have been extracted alongside plant DNA. Presumably, all leaves would have been cleaned of live aphids before they were placed in extraction tubes. What then is the origin of aphid DNA in these samples? Are these trace amounts from aphid saliva and faeces/honeydew that were left on the leaves? If this is the case, I would expect there to be substantially more mildew DNA than aphid DNA, yet the absolute read counts for aphids are actually higher. Presumably read counts should only be used as a relative metric within a pest organism, but this unexpected result nonetheless raises questions about what these read counts reflect. Again, having experimental data from different aphid densities would make these results more convincing.

Comments on revised version:

The authors have addressed many technical details in their revision, but they did not address my more fundamental concerns about validation of their results. I still believe that validation would be needed, but I also acknowledge that an additional experiment that reliably tests a causal relationship between read counts and pest abundance would go beyond the scope of a revision. Nonetheless, the authors currently only show variation in pest read counts among plant accessions, not in pest abundance. While the two measures are likely correlated, I hope that future studies will address more directly how pest abundance and read counts are causally linked, and whether pest read counts truly are a robust measure of pest abundance across a range of conditions and systems


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95510.3.sa2](https://doi.org/10.7554/eLife.95510.3.sa2)

Summary:

Galanti et al investigate genetic variation in plant pest resistance using non-target reads from whole-genome sequencing of 207 field lines spontaneously colonized by aphids and mildew. They calculate significant differences in pest DNA load between populations and lines, with heritability and correlation with climate and glucosinolate content. By genome-wide association analyses they identify known defence genes and novel regions potentially associated with pest load variation. Additionally, they suggest that differential methylation at transposons and some genes are involved in responses to pathogen pressure. The authors present in this study the potential of leveraging non-target sequencing reads to estimate plant biotic interactions, in general for GWAS, and provide insights into the defence mechanisms of Thlaspi arvense.

Strengths:

The authors ask an interesting and important question. Overall, I found the manuscript very well-written, with a very concrete and clear question, a well-structured experimental design, and clear differences from previous work. Their important results could potentially have implications and utility for many systems in phenotype-genotype prediction. In particular, I think the use of unmapped reads for GWAS is intriguing.

Comments on revised version:

The revisions to the manuscript have significantly enhanced its clarity and scientific rigor. Methodological clarifications, especially regarding the normalization of read counts, now provide a stronger foundation for the presented results. Statistical enhancements, including more robust methods for controlling population structure and refined GWAS approaches, have solidified the reliability of the findings, effectively linking genetic variants and epigenetic modifications to pest loads. The discussion section has been improved to offer a more cautious interpretation of the correlations between transposable element (TE) methylation and pathogen load, emphasizing the associative nature of these findings. Additionally, increased transparency in data handling, particularly the treatment of ambiguous reads, has significantly reduced potential biases. These improvements have made the manuscript better suited to the readership, providing clearer insights into the genomic and epigenetic underpinnings of plant pest resistance.
