# Peer review - Round 1

Editors:
- Wenfeng Qian, https://ror.org/034t30j35 Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82290.sa0](https://doi.org/10.7554/eLife.82290.sa0)

The study provides a fundamental understanding of the driving forces behind gene losses in genome evolution and connects the propensity for gene losses to local genomic features like mutation rate and expression pattern. The methodology is compelling, as it identifies "elusive human genes" through independent gene losses in at least two mammalian lineages. The comparative genomics and statistical analyses are thorough and rigorous, making this study appealing to readers interested in exploring the global patterns and underlying mechanisms of gene fate evolution across the phylogenetic tree.


---

# Peer review - Round 1

Editors:
- Wenfeng Qian, https://ror.org/034t30j35 Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82290.sa1](https://doi.org/10.7554/eLife.82290.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Gene fate spectrum as a reflection of local genomic properties" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Wenfeng Qian as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by George Perry as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The identification of "elusive genes" in the current manuscript requires additional scrutinization, given it is the foundation of the whole study. Please check published pipelines in the identification of gene losses (e.g., TOGA – https://github.com/hillerlab/TOGA) and use additional tools such as BLASTX search to test for known technical artifacts when calling genes (homology detection failure, refer to https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000862). Please give a reason for the parameters used in the analysis (e.g., CD-Hit clustering) or examine if the conclusions remain supported by various parameters in the computational pipeline. Also, please take a look at the enrichment of elusive genes in human chr19, and use the synteny-based age estimation of the elusive genes (Shao et al. 2019).

2) Please also present the features of other genes (the genomic background other than elusive and non-elusive genes). Are these genes show intermediate patterns between those of elusive and non-elusive genes? Please edit the manuscript accordingly if the definition of non-elusiveness is actually equivalent to the genomic background.

3) It would be informative to test the links between recombination rate / LD and the genomic locations of elusive genes (compared against randomly sampled genes).

4) Please control confounding factors such as gene expression level and confirm whether the proxy of mutation rate (i.e., Ks) is actually confounded by gene importance.

5) Please consider extending the analyses on fish and birds to other genomic features.

6) The authors should reconcile the findings in this study with previous reports about microchromosomes.

7) Please consider improving the clarity/presentation of Figures 5 and 7 and examine whether the pattern remains robust using various parameter sets.

8) Please think of a better term than "elusive gene" to describe the genes that were lost independently in different lineages. Please also clearly define other terms in the manuscript (e.g., functionally indispensable vs. importance, are they the same concept?)

9) Please consider presenting the current study in the framework of mutation-selection balance, and better explain the novelty of the study over previous tremendous studies about gene losses.

Reviewer #1 (Recommendations for the authors):

Line 18. "neutral factor" is better replaced by "factors independent of gene dispensability".

Line 47. "However" should be "on the contrary"?

Lines 113-114. As indicated in the weaknesses part, I am not fully convinced these genomic, epigenomic, and transcriptomic features are completely independent of gene function.

Figure 1b. Define the red and orange crosses in the legend.

Figure 7 appeared first in the Discussion section. Can this part be moved to the Results section?

Reviewer #2 (Recommendations for the authors):

Overall, I believe that this is an interesting study. However, this version of the manuscript could be significantly improved in terms of logical depth and methodological stringency.

1. Authors actually support the concept of mutation-driven evolution, i.e., the high mutation rate in genomic regions harboring the elusive genes would predispose their fate toward death. To increase the significance of their work, I suggest authors cite (Nei 2013; Xie et al. 2019) and put their work in a bigger context.

2. Authors mentioned that elusive genes are less important and thus more prone to loss. In my view, pleiotropy is a better term compared to importance. That is, elusive genes are less pleiotropic [e.g. narrowly expressed, Figure 5] and thus their loss are more tolerable or easily compensated by other genes. Actually, narrow expression breadth has been observed to be correlated with gene loss in both humans and flies (MacArthur et al. 2012; Yang et al. 2015).

3. I am generally convinced that authors reliably identified elusive genes by identifying gene loss events in the common ancestor of multiple descendant species (to control for errors induced by assembly or annotation, Figure 1). However, Figure 7 shows the enrichment of elusive genes in human chr19. This chromosome is well known to be enriched with tandemly duplicated Krueppel-associated box C2H2 zinc-finger protein family (KZNF), many of which are primate-specific (Shao et al. 2019). I suspect that tree-based strategy implemented in Figure 1 could not be able to dissect the evolution of this super complex gene family. I am proposing two specific analyses: how many elusive genes encoded by chr19 are KZNFs? how many of them have Ensembl one-to-one orthologs across mammals?

4. With the patterns in Figure 3 and 7, authors argued that features of elusive genes are deeply ancient and could be inherited from the microchromosomes of early vertebrates. This statement has multiple problems.

a) Figure 3 only show genomic level features (e.g., high GC content) conserved in multiple vertebrates including shark and chicken. Epigenetic features analyzed in Figure 5 to 6 were only based on human data. I suggest authors to extend these analyses to shark or chicken. Although some epigenetic data could not be available for these species, transcriptome data analyzed in Figure 5 should be available for at least some species.

b) In Figure 7, authors propose the concept related with microchromosomes. These chromosomes have been extensively studied, especially in birds. Some features of microchromosomes are consistent with that of elusive genes [e.g., high GC, (Bravo et al. 2021)]. However, microchromosomes are conserved in terms of gene order and their genes generally show high protein-level constraints as shown by low Ka/Ks (Waters et al. 2021; Li et al. 2022). Authors need to reconcile their discovery with the previous rich literature.

c) Line (L) 204, among 982 human elusive genes, only 540~390 are shared by other species (e.g., shark). I suggest taking advantage of genome-level synteny based age data generated in Shao et al. 2019 to examine the age distribution of human elusive genes. If a high proportion of them are dated as being old (e.g., shared by jawed vertebrates), the statement that these genes have an ancient origin could be better supported.

References

Bravo GA, Schmitt CJ, Edwards SV. 2021. What have we learned from the first 500 avian genomes. Annu Rev Ecol Evol Syst 52: 611-639.

Li M, Sun C, Xu N, Bian P, Tian X, Wang X, Wang Y, Jia X, Heller R, Wang M et al. 2022. de novo Assembly of 20 Chicken Genomes Reveals the Undetectable Phenomenon for Thousands of Core Genes on Microchromosomes and Subtelomeric Regions. Mol Biol Evol 39.

MacArthur DG, Balasubramanian S, Frankish A, Huang N, Morris J, Walter K, Jostins L, Habegger L, Pickrell JK, Montgomery SB et al. 2012. A systematic survey of loss-of-function variants in human protein-coding genes. Science 335: 823-828.

Nei M. 2013. Mutation-driven evolution. OUP Oxford.

Shao Y, Chen C, Shen H, He BZ, Yu D, Jiang S, Zhao S, Gao Z, Zhu Z, Chen X et al. 2019. GenTree, an integrated resource for analyzing the evolution and function of primate-specific coding genes. Genome Res 29: 682-696.

Waters PD, Patel HR, Ruiz-Herrera A, Alvarez-Gonzalez L, Lister NC, Simakov O, Ezaz T, Kaur P, Frere C, Grutzner F et al. 2021. Microchromosomes are building blocks of bird, reptile, and mammal chromosomes. Proc Natl Acad Sci U S A 118.

Xie KT, Wang G, Thompson AC, Wucherpfennig JI, Reimchen TE, MacColl AD, Schluter D, Bell MA, Vasquez KM, Kingsley DM. 2019. DNA fragility in the parallel evolution of pelvic reduction in stickleback fish. Science 363: 81-84.

Yang H, He BZ, Ma H, Tsaur SC, Ma C, Wu Y, Ting CT, Zhang YE. 2015. Expression profile and gene age jointly shaped the genome-wide distribution of premature termination codons in a Drosophila melanogaster population. Mol Biol Evol 32: 216-228.

Reviewer #3 (Recommendations for the authors):

– In recent years several gene loss pipelines were already published (e.g. TOGA – https://github.com/hillerlab/TOGA) and it would be highly beneficial for this study to compare their gene loss reports with output obtained from existing pipelines (which also address the false discovery rate issue)

– We did not appreciate Figure 5. We strongly recommend finding a more quantitative approach to visualise these results, since heat maps are misleading and show different x-axis and y-axis ranges (zoom-ins/ zoom-outs)

– All Figures and Supplementary Figures showing violin plots need to report the number of genes that underly these distributions.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Gene fate spectrum as a reflection of local genomic properties" for further consideration by eLife. Your revised article has been evaluated by George Perry (Senior Editor) and a Reviewing Editor. A previous reviewer also read and commented on the revised manuscript.

Apparently, the manuscript has been significantly improved but there are some remaining issues that need to be addressed, as outlined below. In view of these comments, we kindly request that you consider revising the manuscript once more. Our hope is that, through this additional revision, the manuscript will be written more clearly and rigorously. Thank you for your understanding and continued efforts in improving your submission.

Reviewer #2 made the following comment. Please consider it during revision.

"The authors attempt to argue that the elusive status is ancient ("Thus, the heterogeneous genomic features driving gene fates toward loss have been in place since the ancestral vertebrates"). However, in response to my previous suggestion regarding chicken microchromosomes, the authors present mixed results. They observed high GC content, high gene density, and short gene length in chicken, similar to the findings in humans (Figure 3). Yet, the critical functional data between the two species are conflicting: human elusive genes exhibit low expression and fewer ATAC-seq peaks, while their chicken counterparts display the opposite pattern. In other words, chicken elusive genes exhibit higher pleiotropy, which may decrease the likelihood of their loss. Thus, these genes are not elusive, and high GC content, high gene density, and short gene length do not necessarily predict elusiveness. Given that the authors only analyzed the functional data of human and chicken genomes, it is not possible to determine whether the "elusive" status is ancient or derived from the human or mammalian lineage. I suggest that the authors analyze the transcriptome data in shark or spotted gar to provide further phylogenetic context. Otherwise, the authors should significantly tone down their statement."

The reviewing editor also has some comments on the title and abstract.

1. Please consider revising the title to "The Impact of Local Genomic Properties on the Evolutionary Fate of Genes Across Vertebrates".

2. Please consider adding a sentence (or something similar) at the end of the abstract. "This study sheds light on the complex interplay between gene function and local genomic properties in shaping gene evolution across vertebrate lineages."
