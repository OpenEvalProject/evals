# Peer review - Round 1

Editors:
- Maximilian J Telford, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34226.051](https://doi.org/10.7554/eLife.34226.051)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The ancestral animal genetic toolkit revealed by diverse choanoflagellate transcriptomes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Casey Dunn (Reviewer #2); Warren Francis (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an extremely interesting and very well executed paper that sets a new benchmark in understanding the evolution of gene content within and between animals, choanoflagellates, and their relatives. This is fundamental to answering basic questions about the history of the evolution of genomes and many phenotypes of broad interest.

The authors have sequenced 19 new choanoflagellate transcriptomes and used them to reassess which animal genes have pre-metazoan origins. It's an interesting paper – the data are valuable.

- The results are biologically interesting. It clearly pinpoints in much greater detail than previous studies the history of gene gain and loss along key branches in the tree of life.

- It will be a great technical resource. Investigators interests in particular gene families can refer to this paper to understand where their favorite genes have been gained and lost, and which organisms they are in. Investigators interested in particular branches in this portion of the tree can refer to the paper to see how gene inventory changed along these branches.

I found the results to be well presented, and appreciated how clear and clean the figures are.

The paper does much to clarify what doesn't make animals special – an essential part of understanding what does make them special. Like other lineages, animals have lost many genes. There has not been a march toward increased gene content in animals, with other extant lineages representing snapshots in animal history, as is often implied or assumed (based on scant evidence). There has been gain and loss of genes along many branches, including a similar rate of gain and loss in animals and choanoflagellates.

Essential revisions:

Phylogeny: Please at minimum discuss the following in any response. If necessary comment on the possible impact of using a different phylogeny.

The authors reference the phylogeny of Carr et al., 2017 for the interpretation of their results (e.g. Figure 3). This analysis is based on 6 genes, and differs somewhat from a phylogenomic analysis in Simion et al.. 2017 e.g. in the position of Codosiga and Salpingoeca dolichothecata. I think these discrepancies are important as they affect how parsimonious some of the purported choanoflagellate gene losses are. It is a shame that the authors do not present a more definitive phylogeny using the data that they have produced, or at least discuss interpretative issues in light of different phylogenetic possibilities (even if to say there are no serious issues).

Methodology: My major concern is with the OrthoMCL based approach – it really isn't clear what an OrthoMCL gene family corresponds to (in terms of orthologs/paralogs). This makes summary numbers suspect (1700 gene families with origins in the animal stem lineage of which 36 are conserved across animals). What is an OrthoMCL gene family in terms of true biological entities?

The authors highlight a number of specific examples of gene loss from M. brevicollis and S. rosetta, (TLRs, Delta etc.), but leaving these vignettes aside, and the 350 number in the Abstract (which I don't find in the main text), I cannot find a discussion of how anomalous/representative the authors consider the two taxa with sequenced genomes to be. It would be helpful to include this.

Table 1. I think there's a difference between what the reader is likely to think has been done and what actually has been done, and as the 36 number makes it to the Abstract, it's quite important to be clear. WNT ligands, for instance are a classic example of a metazoan novelty (and to the best of my knowledge have still not been reported in non-animals). The OrthoMCL based protocol breaks up these ligands into a number of different animal specific families, none of which feature in Table 1, perhaps because no single family is present in all animals studied. Yet the innovation itself, the invention in the animal stem lineage of the first Wnt seems to me as though it is exactly the sort of thing the paper is suggesting it will report. I would like to see a clearer discussion of what the 36 number means and how robust it is to methodological approach. If I constructed an alignment and phylogeny for each gene in the dataset and assessed when it had an ortholog in all other animals would I get a number even close to 36? Would the authors be happy for people to cite this paper saying that there were only 36 conserved animal specific gene families?

Surprised that no gene trees are presented. Phylogenetic analyses of gene families could do much to clarify some of the patterns that are discussed. For example, in the section "Construction of gene families and their probabilities of presence" the authors hypothesize that cases where a gene is present in one choano but many animals are due to false positives with blast. Building a multiple sequence alignment and gene tree would be a simple and informative way to evaluate this. There is also the risk that some choano data could be contaminated with animal sequences, and phylogenetic trees would help clarify this.

It also isn't clear to me why the authors didn't use standard maximum likelihood and Bayesian character evolution methods to trace the gain and loss of gene families on the species phylogeny. This would also infer ancestral state probabilities for gene presence/absence under explicit models of evolution. Such methods are well established and highly relevant here.

Subsection “The phylogenetic distribution of animal and choanoflagellate gene families”, first paragraph: I do not think that the use of BUSCO is appropriate for measuring the completeness of transcriptomes, particularly as the whole point of this study was to examine the gene content of choanos relative to animals, hence of a group which is not currently well-represented (for instance, it does not appear that Monosiga or Salpingoeca were in the BUSCO set).

How many gene families/proteins are recovered by the transcriptomes for either or both of the species with genomes i.e. does the RNAseq get most of the genes predicted from the genomes? Is there any reason to consider that the gene numbers vary substantially from Monosiga and Salpingoeca (roughly 10k genes)? For instance, in the Supplementary file 1, Codosiga has 61k proteins, but presumably fewer "genes" if these were clustered. This is mentioned in the Materials and methods, but may be better explicitly discussed in the Results.

Gene family construction, subsection “Construction of gene families and their probabilities of presence”: Relating to whether the "residual probability" genes are true orthologs, it would appear that this method might systematically miss gene presence from taxa with long-branches. One can consider cases where true orthologs have good matches within groups of related species (say within flatworms or roundworms) but other taxa are too distant to have good matches. This was found to be the case in flatworms (see Martin-Duran et al., 2017 Genome Research). This could imply that homology of some fast evolving genes may be overlooked between animals and choanoflagellates. Perhaps discuss how many genes simply have no matches between metazoa and choanoflagellates vs. weak matches.

Subsection “Animal-specific gene families: innovation and loss”, first paragraph: GO terms are often controversial (too broad or wrong) for non-model organisms, a problem highlighted on the GO website. The GO terms discussed in the text are plausible, but the supplemental table also contains a number of implausible ones, such as heterocycle biosynthesis or aromatic compounds biosynthesis, which have smaller p-values than the ones discussed. It is unclear if animals have these pathways as the terms might be carryover from regulatory elements, but the presence of these pathways is also contradicted later saying they do not have the shikimate pathway, etc. Because any annotations are biased by model animals, very little is known about possible functions in choanoflagellates or non-model animals, making it difficult to say any function in early animals (i.e. Burkhardt et al., 2014 Mol Biol Evo). It may be too drastic to say these results should be removed entirely, but perhaps very critically discussed, esp. in light of the results on Figure 2—figure supplement 7, suggesting most genes have no annotation.

ECM Experiments: The referees agree that the final section on ECM experiments does not sit well with the rest of the manuscript. It also does not add a great deal and there is insufficient space to do the experiments justice. We feel this should be omitted from a revision.
