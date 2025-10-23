# Peer review - Round 1

Editors:
- Dario Riccardo Valenzano, Max Planck Institute for Biology of Ageing Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65394.sa1](https://doi.org/10.7554/eLife.65394.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript is of interest in the field of comparative genomics as it provides novel genomic resources for the whale shark, which belongs to a group of vertebrates with a unique biology, which to date had limited available genomic data. This work provides important insights into the evolution of several key vertebrate-specific gene families, including genes involved in pathogen recognition receptors (PRRs) and cancer suppression.

Decision letter after peer review:

Thank you for submitting your article "The whale shark genome reveals patterns of vertebrate gene family evolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael Hiller (Reviewer #2).

Essential revisions:

1. Despite the sequencing of long-range reads, the authors did not scaffold the contig assembly. What is the reason for this? Did the authors use the mate pair data from previous studies (e.g. Read et al)?

2. Cancer gene families seem to be prone to shifts anywhere (line 493). Therefore, the authors should test if swapping the large animals for their normal sized sister taxa (e.g. whale shark for bamboo shark, minke whale for dolphin) also results in a significant enrichment in cancer genes. If that is the case, then there is probably no or only a weak connection between cancer gene family evolution and body size.

3. Expand the explanation regarding the evolutionary analysis of PRRs (reviewer #3, point1).

4. Expand the methods part, providing detailed information for reproducibility and transparency reasons (see reviewer #3, point 2). At the same time, integrate more of the methods section into the Results section, providing essential information about the methods and databases used.

5. Invertebrate deuterostomes are often used in the paper as an example of animals that have an expanded PRR repertoire due to the lack of an adaptive immune system. However, despite often using invertebrate deuterostomes as an outgroup, the authors never quantify PRR repertoire shifts between invertebrate deuterostomes and the vertebrate groups used for comparison. Quantifying these shifts between groups will strengthen such arguments. Also, a more effective outgroup might be non-jawed vertebrates lacking a lymphocite-based adaptive immune system provided there is enough genomic data to interrogate PRR diversification.

Reviewer #1 (Recommendations for the authors):

The world-wide increase of genomic surveys across vertebrates (see genome 10K) have significantly raised the bar for genomic studies and publication of individual genomes. Long-read technologies should be also coupled with HiC and provide chromosome-level genome assemblies. In this respect, this manuscript does not reach the standards that would grant a publication in a journal like eLife. Furthermore, the present whale shark genome is an upgrade from a previous assembly, hence does not meet the criterion of "novel species". Additionally, the work presented does not provide significant insights into the biology of the species studies.

Reviewer #2 (Recommendations for the authors):

1) The authors compared gene families with shifts in large animals (and possibly other lineages) and show enrichments for cancer genes. This is interesting, however cancer gene families seem to be prone to shifts anywhere (line 493). Therefore, the authors should test if swapping the large animals for their normal sized sister taxa (e.g. whale shark for bamboo shark, minke whale for dolphin) also results in a significant enrichment in cancer genes. If that is the case, then there is probably no or only a weak connection between cancer gene family evolution and body size.

Reviewer #3 (Recommendations for the authors):

1. The evolutionary analysis of PRRs is not sufficiently explained. For instance, the authors say that they used subsampling of a previously used set for the TLR analysis (line 699). The nature of the original set is not described satisfactorily (i.e. species, database, etc; see point 4 below), the method and depth of subsampling is not explained (i.e. software used, % of coverage, random or guided), and the scientific rationale for such a choice instead of using a full set is not given. In addition, there are other potential issues emerging, notably why does the TLR analysis include more species than for NLR and RIG-like? When trying to infer NLR repertoire shifts in vertebrates, the authors compare humans (mammal, bony vertebrate), zebrafish (bony fish), and whale shark (cartilaginous fish). However, comparing only three groups seems insufficient to make conclusions regarding the evolution of NLR repertoire shifts. Why not include the breadth of species used in the TLR phylogenetic analysis? The selection of other included species in that analysis needs to: (i) be transparent, including information about how the other species/sequences are selected and obtained and (ii) be unified, i.e. include the same taxonomic depth for all considered groups.

2. There are a number of missing pieces of information that need to be provided for reproducibility and robustness. The method section, particularly, needs to be completely revamped and developed.

a. Please make sure all version numbers of used software's are explicitly stated in the methods section. Although many are specified, version numbers are not available for a number of used software or packages, and version numbers (or date of access) also need to be provided for annotation databases (e.g. genBLAST, BLAST, DIAMOND, biomaRt, gVolante, etc.).

b. Please indicate all necessary information for which species were included, which genome builds were used for the other species used for phylogenetic analyses in the main methods. Please also explain why genome builds for Refseq, Ensembl 89 and 99 are mixed (see Table S3).

c. Please provide additional details/information on the refseq pipeline they used to annotate the genome (Gene prediction section in methods), including software version, parameters, etc. Intriguingly, although the gene prediction section in methods mentions the refseq annotation pipeline, Table S2 mentions another annotation software, MAKER (not mentioned anywhere in the methods section). Please make sure to describe accurately which methods were used.

d. "We also performed assembly-free estimation of genome size, heterozygosity, and repeat content.", line 586. This is not enough detail for a methods section to ensure reproducible analysis. Please provide an explanation of how this was done, using which softwares, etc.

e. In table S1, please indicate DNA source abd raw read data etc without referring to previous paper. Indicate all here for proper comparison, or the table is not providing the needed information.

f. Finally, it is key for long-term reproducibility that all the code for this study be made available to readers (e.g. as a github repository or a supplemental zip file).

3. Too much of core analyses are supplied as supplementary notes, partially redundant to the main text and partially containing information that clearly belongs in the main text. The results need to be integrated and discussed in the main paper, otherwise they will be mostly lost to the readers.

4. The authors make the claim that, "While we found evidence for a core set of NLRs in jawed vertebrate, our analyses also suggest that the immunologically relevant NLR repertoire shifts may be as common in vertebrates as they are in deuterostome invertebrates, despite the presence of the adaptive immune system." Invertebrate deuterostomes are often used in the paper as an example of animals that have an expanded PRR repertoire due to the lack of an adaptive immune system. However, despite often using invertebrate deuterostomes as an outgroup, the authors never quantify PRR repertoire shifts between invertebrate deuterostomes and the vertebrate groups used for comparison. Quantifying these shifts between groups will strengthen such arguments. Also, a more effective outgroup might be non-jawed vertebrates lacking an adaptive immune system provided there is enough genomic data to interrogate PRR diversification.
