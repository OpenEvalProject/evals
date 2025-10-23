# Peer review - Round 1

Editors:
- Bavesh D Kana, University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97870.4.sa0](https://doi.org/10.7554/eLife.97870.4.sa0)

This useful study analyzed 335 Mycobacterium tuberculosis Complex genomes and found that MTBC has a closed pangenome with few accessory genes. The research provides solid evidence for gene presence-absence patterns which support the appending conclusions however, the main criticism regarding the dominance of genome reduction remains.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97870.4.sa1](https://doi.org/10.7554/eLife.97870.4.sa1)

Summary:

In this paper, Behruznia and colleagues use long-read sequencing data for 339 strains of the Mycobacterium tuberculosis complex to study genome evolution in this clonal bacterial pathogen. They use both a "classical" pangenome approach that looks at the presence and absence of genes, and a pangenome graph based on whole genomes in order to investigate structural variants in non-coding regions. The comparison of the two approaches is informative and shows that much is missed when focusing only on genes. The two main biological results of the study are that (1) the MTBC has a small pangenome with few accessory genes, and that (2) pangenome evolution is driven by genome reduction. The second result is still questionable because it relies on a method that disregards paralogs.

Strengths:

The authors put together the so-far largest data set of long-read assemblies representing most lineages of the Mycobacterium tuberculosis context, and covering a large geographic area. They sequenced and assembled genomes for strains of M. pinnipedi, L9, and La2, for which no high-quality assemblies were available previously. State-of-the-art methods are used to analyze gene presence-absence polymorphisms (Panaroo) and to construct a pangenome graph (PanGraph). Additional analysis steps are performed to address known problems with misannotated or misassembled genes.

Weaknesses:

The main criticism regarding the dominance of genome reduction remains after two rounds of revisions. A method that systematically excludes paralogs is hardly suitable to draw conclusions about the relative importance of insertions/duplications and deletions in a clonal organism, where any insertion/duplication will result in a paralog. I understand that a re-analysis of the data might not be practical, and the authors have added a few sentences in the discussion that touch on this problem. However, the statements regarding the dominance of genome reduction remain too assertive given this basic flaw.

Here are the more detailed argument from the previous review:

In a fully clonal organism, any insertion/duplication will be an insertion/duplication of an existing sequence and thus produce a paralog. If I'm correctly understanding your methods section, paralogs are systematically excluded in the pangraph analysis. Genomic blocks are summarized at the sublineage level as follows (l.184): "The DNA sequences from genomic blocks present in at least one sub-lineage but completely absent in others were extracted to look for long-term evolution patterns in the pangenome." I presume this is done using blastn, as in other steps of the analysis.

So a sublineage-specific copy of IS6110 would be excluded here, because IS6110 is present somewhere in the genome in all sublineages. However, the appropriate category of comparison, at least for the discussion of genome reduction, is orthology rather than homology: is the same, orthologous copy of IS6110, at the same position in the genome, present or absent in other sublineages? The same considerations apply to potential sublineage-specific duplicates of PE, PPE, and Esx genes. These gene families play important roles in host-pathogen interactions, so I'd argue that the neglect of paralogs is not a finicky detail, but could be of broader biological relevance.
