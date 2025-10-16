# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04550.018](https://doi.org/10.7554/eLife.04550.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for choosing to send your work entitled “Immunosuppression enables expanded host ranges and can explain mosaic genome structures in Albugo candida races” for consideration at eLife. Your full submission has been evaluated by Detlef Weigel (Senior editor and Reviewing editor) and two peer reviewers, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

First, there were concerns about the evidence for hybridization, both from the side of in vivo experimentation and from the interpretation of the sequence data with respect to ploidy and recombination patterns. Second, the reviewers felt that the failure to identify credible candidate genes or gene networks that arose from hybridization and that are responsible for adaptation weakened the impact of the work.

Reviewer #1:

The article by McMullan and colleagues investigates the genome of the obligate pathogen Albugo candida infecting Brassicas including Arabidopsis. The authors sequenced the genomes of 5 strains sampled from different Brassica hosts falling into 3 distinct clades. Analysis was based mostly on 3 strains, one from each race (clade). Authors identified recombination blocks and regions of divergence among the three races. The authors combine genome sequencing, modeling and genetic work to assemble a nice story on divergence among three races of the pathogen.

The authors should formally test for linkage disequilibrium and clonality using SNPs and the index of association or LD.

I liked the inclusion of simupop simulation to infer patterns and date events. This effort showed that incomplete lineage sorting does not lead to the observed mosaic genome structure. However, I believe Figure 4 of the supplements is missing and I could not see the actual graphs showing this pattern.

The phenotyping work on host range was not repeated in independent experiments and the experiments included a different number of treatments for each strain.

Overall, the manuscript as presented lacks novelty although the work is well done and highly publishable elsewhere. The genome of A. candida was published in 2011 by Links et al. Here the authors resequence 5 strains and analyze 3 strains in fine detail. The races are found to have a mosaic like genome structure and that races diverged a considerable amount of time ago. A. candida is host specific, and thus races associated with a given host are not expected to cross breed with those on another host; the authors established presence of recombination blocks. They also demonstrate that co-inoculated strains from a host and non-host on a host can establish infection by the non-host strain and replicate this effect for several strain-host combination (Figure 6). However, this work is not repeated and lacks the validation from a full second experiment. Furthermore, it only shows the strains can coexist in the same environment, but it does not demonstrate hybridization or recombination. I think if they could demonstrate sexual reproduction or hybridization among diverged races, and tie the hybrid genomes into this story they would have a great paper. As it stands, I think this would be better published in a disciplinary journal given that it mostly provides information on more distant divergence, adaptation and coinfection. Lack of sex also needs to be more formally tested on a larger sample of strains.

Reviewer #2:

This manuscript by McMullan et al describes patterns of genomic variation and exchange between three races of Albugo candida, an oomycete pathogen of Brassicas, and provides evidence that co-infection could allow for such genetic exchange. Virulence tests confirmed prior work on the host-specificity of these isolates (AcNc2, Ac2V and AcBot) to A. thaliana, B. juncea and B. oleracea, respectively. When host plants are first infected by the specific pathogen race, this can allow for subsequent infection of otherwise avirulent races in the same plant, expanding on prior work showing secondary infection by downy mildews on hosts that have primary resistance. By analyzing genome assemblies of five isolates, the authors identified regions that appear to have ancestrally recombined between the races, resulting in a “mosaic genome”, followed by an apparent clonal expansion. The authors hypothesize that immunosuppression by the infectious isolates allowed a non-infectious race to colonize and recombine with it, allowing for new combinations of virulence genes.

This is an interesting study of genetic variability and exchange between pathogenic lineages; however the methods used to detect recombination do not clearly establish the certainty of inferred exchange events. The risk of relying on a single program (RDP3) to determine recombination is highlighted by the primary publication on this method, which states: “The drawback of such a flexible, exploratory framework is that it can often be difficult to assess the uncertainty associated with inferred recombination patterns. However, with its wide range of cross-checking tools, RDP3 is complementary to probabilistic recombination analysis approaches.” The authors have not included any such support for the recombinogenic regions identified using this data, including standard metrics of linkage disequilibrium, and it is unclear if their measure of using events detected by 3 of 5 models in RPD3 represents an optimal concordance. Some simulations are included, although this is used to evaluate the origin of the overall pattern, rather than validate the genomic regions detected with RDP3.

One major point of confusion in reading the manuscript is the lack of clarity on the ploidy level of A. candida and the methods used to analyze nucleotide variation. The authors compared heterozygous sites (suggesting the species is diploid), although there is no description in the supplementary methods of how these sites were identified or their confidence level. The “unphase base calling and the random assignment of one of the nucleotides at each polymorphic site” provided the sequence used for the recombination analysis. This process is then described as “conservative”, based on unphased heterozygous data underestimating variance, but direct support for this statement is not provided. The methods and the analysis of how nucleotide variants were identified through alignments of raw sequence or assemblies need to be more thoroughly described.

Given that ancestral recombination between these races is the main result of this paper to support their hypothesis, this analysis needs to be supported by an additional method, and a more detailed description of how results compare from the individual methods in RDP3 and probability based methods.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

We have considered your appeal regarding your manuscript entitled “Immunosuppression enables expanded host ranges and can explain mosaic genome structures in Albugo candida races”. We have now received comments from an expert on hybridization, and in light of the very positive evaluation, we would like to invite you to revise your article.

Your manuscript presents the analysis of several genomes of different races of Albugo candida. You provide very nice evidence that the genomes show signs of introgression of up to 25% material from other races. Since these races have host ranges which, to the best of the authors' knowledge, exclude each other, it is of great interest to understand how recombination between races can occur. You solve this conundrum by showing that exposure by one pathogen race makes the host plant susceptible to other races, to which they are normally resistant, thus providing a clear path to hybridization between races that normally have nonoverlapping host ranges.

The study is well carried out and convincing, but the presentation could be improved in several places.

1) While the material provided is clearly suitable for eLife, the manuscript is not written in a very accessible style, rather what one would expect for a much more specialist journal. The message of this study is of potential interest for many readers (not only plant pathologists), but there is the danger it will attract little attention as currently presented. For example, proper population genetic terminology is mostly missing, examples from other system are almost absent and comparisons with other cases of hybrid formation (there are many in plants and animals and several nice genomic studies have been published) are ignored. The topic of breakdown of isolation mechanisms has implications for other central topics in evolution and ecology, such as local adaptation and speciation. Here the discussion could go much further.

2) The data suggest that 25% of the genome of a race is introgressed from a genome from a different host race. With this much introgression, and assuming that this study did not find exceptional cases, but rather a representative sample from the wild, one wonders about the genetic architecture of host-range determination. If host-ranges are determined by multiple loci, one would except that recombination will quickly lead to super genotypes, with very wide host ranges. Apparently this did not happen; maybe recombination cannot change this. This would be the case if they are sitting in non-recombining gene clusters, or a single locus (with multiple alleles) is responsible for host ranges. We would like to see some discussion about this.

3) The authors use the term “immunosuppression”. To an animal immunologist, this implies that the study included the assessment of immunological parameters, which is not the case. Rather, you observe in experimental infections that a first infection facilitates infection with a second race of the pathogen. We suggest rephrasing this, so as to not confuse animal immunologists.
