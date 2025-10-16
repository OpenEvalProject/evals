# Peer review - Round 1

Editors:
- Richard A Neher, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08714.029](https://doi.org/10.7554/eLife.08714.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Genomic epidemiology of the current wave of artemisinin resistant malaria" for peer review at eLife. Your submission has been favorably evaluated by Prabhat Jha (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission

Summary:

This study presents a large number of P. falciparum genomes that are a valuable resource for future molecular epidemiology studies. By analyzing these data, the authors demonstrate that:

1) Artimisinin resistance mutations arose many times independently in South East Asia and are associated with drastic amino acid changes in different domains of kelch13;

2) Resistance mutations in Africa arose locally;

3) Resistance mutations in kelch13 likely come at a substantial cost, limiting their spread.

In addition, they provide a population genomic characterization of the P. falciparum diversity.

Essential revisions:

1) The study is currently focused exclusively on kelch13 and lacks comparison to other known resistance loci. While kelch13 is compared to the genome wide distribution of diversity, dN/dS, etc., it should be put into context of other resistance loci. It would be straightforward to repeat some of the analysis done for kelch13 for other loci (e.g. highlight those genes in Figure 5, add trees of haplotypes surrounding these loci in analogy to Figure 2).

2) Data availability: the malariaGEN project hosts a comprehensive website for genomic data. However, in the interest of reproducibility and reusability additional files should be provided. We would like to see metadata for all strains included in this study. Ideally, this metadata include sampling date and location, phenotype information where available, the short read archive identifier. Similarly, the source data for figures, such as tables with dN/dS values for genes in case of Figure 5, should be provided. For follow-up analysis a flat file with the genotypes of all strains at the 935,601 high confidence SNPs and their allele frequencies in the different populations would be useful. Such files should be uploaded on data Dryad, or alternatively, a clear description on how to obtain such data from malariaGEN should be given.

3) Figure 1: a genome wide tree is a bad way to summarize diversity in a sexual population. A projection on the first two principal components could be more useful. Location, isolates with kelch13 mutations, phenotypes could be highlighted by color, symbol, size etc. In addition, genomic differentiation could be summarized by FST or the density of private SNPs, possibly in a sliding window along the genome. kelch13 and other resistance loci should be outliers here.

4) Population genomic characterization: Figure 3 is uninformative. Please show the complete minor allele frequency spectra, possibly on a log-log scale to improve readability at the low frequency end. Panel c is redundant with 5a. In order to interpret Figure 2, estimates of the extent of linkage disequilibrium would be welcome (why not show LD decay surrounding kelch13 and other resistance loci in SEA and Africa and compare to genome wide average).

5) Hydrophobicity and radical substitutions: Given that the function of kelch13 is unknown, the emphasis on hydrophobicity as a score for mutations is not justified. In fact, mutations in SEA are found at hydrophilic and hydrophobic sites alike. The stronger signal seems to come from conservation (but note the outlier Y493H). We suggest focusing on conservation and drop the hydrophobicity discussion unless you provide convincing evidence for a causal role of hydrophobicity changes (otherwise, it could stay as a somewhat speculative supplementary figure). The description of the calculation of the conservation score needs more detail. Why did you use a 9 amino acid window for smoothing? How did you average over multiple pairwise comparisons? While substitution matrices quantify broadly the exchangeability of amino acids, they are often a rather poor guide for site specific mutation effects. Is there a way to assess site specific conservation in a broader alignment than the one used for Table 5?

6) Resistance mutations in Africa: A more detailed analysis is required here. Please point out African strains that carry kelch13 mutations on the tree in Figure 2, show additional trees for different haplotype length, and maybe compare African haplotypes with resistance mutations explicitly to the closest SEA haplotype and the closest African haplotype lacking kelch13 mutations. In Figure 2b, do African isolates that cluster with the SEA ones have special properties (e.g. C580Y mutations)? In order to render the discussion of the resistance mutations observed in Africa more concrete, a supplementary file should be provided that contains their country of origin, any drug phenotype data, whether any were culture adapted, whether these were PCR resequenced to confirm the mutations, whether there were any clinical or parasitological data to indicate that these were associated with delayed clearance rates.

7) How representative is Figure 2b showing imperfect separation between Asia and Africa? How does this depend on the size of the window used for tree building? The two African samples that fall in between the SEA and African clusters should be discussed in greater detail and additional analyses are needed to clarify whether they are admixed.

8) The association of fd, aprs10, mdr2, etc. should be explicitly discussed as correlation rather than causation as no evidence is presented for the latter. Given resource limitation, the case for including these loci in routine surveillance is weak at present. The statement in the Discussion should be toned down.
