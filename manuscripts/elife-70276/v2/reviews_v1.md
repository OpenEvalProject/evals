# Peer review - Round 1

Editors:
- Jenny Tung, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70276.sa0](https://doi.org/10.7554/eLife.70276.sa0)

This is an important study that represents a significant contribution to our understanding of how gene expression in the primate brain has evolved across the extant primate phylogeny. It provides solid evidence for potential links between gene expression variation and brain size, although these are somewhat limited by the focus only on adult brains, since many key changes likely occur during development. Nevertheless, both the taxonomically broad data set and the analysis are likely to be of broad interest to the evolutionary biology, anthropology, and comparative neuroscience communities.


---

# Peer review - Round 1

Editors:
- Jenny Tung, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70276.sa1](https://doi.org/10.7554/eLife.70276.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Tempo and mode of gene expression evolution in the brain across Primates" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mehmet Somel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Control for phylogenetic structure in analyzing gene expression changes across the phylogeny, especially in association with brain size. Strongly consider whether phylogenetically informed analysis methods provide greater insight (and reduce the potential for confounding) over pairwise comparisons, especially given advantages afforded by broad sampling across the primate order.

2) Provide key missing detail on criteria for defining orthologues; demonstrate robustness of results to decisions about cut-offs (e.g., for defining highly variable genes) and cell type compositional heterogeneity between species.

3) Address methodological questions raised by the reviewers regarding multiple hypothesis testing correction and enrichment analyses.

4) Test human-specific changes in expression in relationship to outgroup species as well as chimpanzee.

Reviewer #1 (Recommendations for the authors):

1. Trinity output is extremely noisy and returns many isoforms with poor support, or virtually undistinguishable from each other except for a couple of base pairs here and there, especially when run in a de novo mode. How did the authors prioritise the many isoforms, and determine which are credible and worth analysing further? Similarly, since many of the primates lack a reference genome, how did the authors define the set of 3432 testable one-on-one isoforms, or the 15017 genes testable across hominoids? Is it simply on the basis of pairwise orthology to human using BLAST or…? Did the authors control for gene duplication (eg reciprocal BLAST)? In addition, the thresholds for orthology seem very permissive, on the basis of overall coding sequence conservation amongst mammalian species (eg see supp Figure 1B of Chen et al. 2019, where mean coding sequence identity between humans and non-primate one-to-one orthologs is ~85%).

2. Many conclusions are based on data from the top 500 most variable genes (generally defined on the basis of SD, but not always – the sanity check against scRNA from astrocytes and neurons uses CoV). Why 500? How robust are all of the results presented to this choice of threshold? Is there a particular species driving this variance (on the basis of PCoA results I dare speculate it's chimpanzees and humans)? How do these observations (PCoA, phenograms) compare to those made on the entire dataset of 3432 testable genes across the entire dataset? It seems to me that the number of genes in the whole data set is not so large as to be worth focusing only on an arbitrarily chosen threshold, and that it would be more informative to consider the entire dataset in these analyses. Similarly, when looking at positive selection, the authors only focus on the top 200 genes DE between human and chimpanzee. Why these limitations?

3. The authors test the possibility that compositional heterogenity across samples may be biasing their results (line 723 onwards), which I commend, but nonetheless find somewhat incomplete as it currently stands. The only test performed is a comparison of human bulk RNA samples to a small number of astrocyte and neuron RNA-seq samples, which they say proves their tissues are not biased towards either cell type. But combining bulk RNA and scRNA data is not trivial, and since the PCoA shows samples clustering by technology/study (I presume the outlier neuron comes from the same dataset as the astroctyes), it's unclear how to interpret it. Regardless, there's no mention of what I think is the more interesting source of heterogeneity: is there an expectation that the composition of the same tissue type would vary substantially between species? e.g., an excess of, say, glia in the PFC of humans relative to lemurs or loris that could skew results (totally hypothetical example)? I am not sure if this is possible to taste with existing datasets, but it seems to at least be worth discussing?

4. DE testing: As above, I would like to see more detail in the methods here to better contextualise the results. First, I do not think CPM is the accurate unit for comparison here, since it does not control for differences in gene length between species, which may be substantial at some of the orthology thresholds set by the authors – RPKM might be better suited. Second, how many genes were testable between each of the comparisons summarised by figure 3? Was this testing done using in a pairwise fashion, using all genes testable between the pair of species being compared (as suggested by line 190), or using a single model matrix with many different contrasts to leverage information across the entire data set? Altough the latter represents a substantial trade off in terms of testable genes, might provide additional insights in terms of polarising results and perhaps even pinpointing the emergence of expression divergence through the tree for specific genes or families. Since subsequent analyses focus primarily on genes identified as DE between human and chimp, I think it would be worth delving a bit more here into the broader temporal trends, or by comparing other interesting pairs of primates.

5. Evolutionary mode of expression levels: as mentioned above, I think the authors do themselves a disservice by not examining their data deeply, eg, by not placing results in a broader evolutionary context or clearly distinguishing between genes that appear to evolve neutrally vs those that exhibit other trends (are there any?). I think this is where the potential of the dataset most shines, and so I strongly encourage the authors to examine the EVEE output in greater detail and see if there's anything interesting hiding in there, although I am cognisant that this might fall outside the scope of the manuscript as they see it, and thus leave it up to them to decide what to do. Nonetheless, some possible questions: can the authors tease out genes evolving under positive selection or showing bursts of accelerated evolution from the overwhelming sea of neutrality? While it's obvious why the authors choose to focus on humans, is anything interesting happening in any other primate lineage?

6. Brain size and positive selection: the authors use mean expression within a species for PCA this time around, as opposed to just all available data points – but it seems to me that this might obscure some trends? Again, the reason for focusing on humans in these sections is obvious – the change in brain size between human and chimp is monumental – but I wonder if this obscures more subtle signals in the data.

Reviewer #2 (Recommendations for the authors):

Having commended the authors for compiling this remarkable dataset, I need to share a number of concerns, with regards to data analyses and also interpretation.

1) In general, the analyses and interpretation alternate between investigating general patterns of evolutionary divergence across primate brain regions, and investigating human-specific expression divergence (e.g. Figure 3 is human-based). It may be better to separate the two questions and the analyses used to address them. The authors could start by quantifying the overall phylogenetic signal in brain expression divergence, e.g. using the Chen et al. 2018 model.

In general, I think that performing pairwise DE tests makes little sense with such data (except for cases where specific hypotheses are tested). It would be preferable if the authors studied human-specific expression changes also within an OU-based phylogenetic model that can also incorporate lineage-specific positive selection (e.g. https://doi.org/10.1093/sysbio/syv042).

Also, in analyses about human-specific expression changes, the authors should preferably rely on gene sets which show human-specific upregulation relative to chimpanzees and outgroup species, not just DE gene sets between human and chimpanzee, especially if they wish to interpret the results in the context of other observations (e.g. human-specific positive selection in promoters of semaphorin genes, or increased white matter connectivity).

2) Regarding the analyses on expression patterns correlated with brain size expansions, I would suggest to use some type of phylogenetic residuals analysis, because both brain size and expression will reflect phylogenetic relatedness. So, no surprise that the same genes show correlation across brain regions.

Moreover, it is not clear if the gene list presented in Table 1 and discussed in detail is indeed of statistical significance – multiple testing correction has not been applied.

3) A large number of expression changes may be driven by changes in cell type composition, especially in evolutionary time. At least there should be some discussion on this point in the main text.

Currently the only mention is the supplement, and the content is suboptimal – human brain region bulk transcriptome profiles are compared with cell type-specific transcriptomes of neurons and astrocytes, whereas it is still highly possible that DE genes across species reflect changes in composition. This could be studied explicitly: e.g. https://www.biorxiv.org/content/10.1101/010553v2.

4) Humans are used as reference species in a large number of analyses, but the motivation and rationale behind this is not explained. In fact for questions about general expression divergence in the brain, humans may not be a good reference.

5) Many methodological details are lacking, including crucial information on RNA-seq data quality, how different gene sets were defined, and motivations behind different cutoff choices used, etc. Overall rewriting of methods would be helpful.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Tempo and mode of gene expression evolution in the brain across Primates" for further consideration by eLife. Your revised article has been evaluated by George Perry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved in the revision process, and both reviewers note their appreciation for your responsiveness to the previous round of reviews. I am therefore returning it so that you can address some final issues regarding methodological clarity identified by Reviewer 1, and to give you the opportunity to fix some errors identified by Reviewer 2. In addition, I noticed that even though you have removed the analysis of positive selection on regulatory regions from the manuscript, it is still referenced in your abstract--so please do a thorough read-through for consistency throughout.

Reviewer #1 (Recommendations for the authors):

I thank the authors for their reply to my comments and the accompanying revisions and additional details – it's good to see this paper again, as I remain impressed by the dataset and by the scope of the questions the authors are hoping to address.

My responses focus primarily on the points they have addressed in this revision, to avoid dragging this process on forever; I have tried hard to ask only for clarifications, or the absolute minimum, when I have asked for something new. As last time, most of my questions center on methods, so I've brought those to the top, but in all cases, they're requests for additional detail, not for things to be repeated or rerun, so despite the length of the comments I hope they're not too onerous.

1. Trinity output: I would still like a bit more detail on this. Did the authors simply take the best scoring match to a given human gene from the blastnt search? Were there any controls for length or similar? The BUSCO scores are a welcome addition, but some of them are quite low, so additional clarity would be good to help understand what was done. Please note that I am not saying 'redo everything with different thresholds,' but I think more detail would be valuable in parsing the surprisingly low number of genes with data – if 50-70% of the transcriptome is evolving under stabilising selection, but that only covers the 3000 testable genes with one-to-one orthology across the clade, that's actually not a lot of genes at all…

2. PCoA etc: I thank the authors for the additional detail, but I confess I am a bit confused as to how they did what they have done. Line 476 (and 570 for the scRNA data) states that the distance metric is based on log2 fold change distances and that it was generated with plotMDS, but that is not what plotMDS does (plotMDS, by the way, is a limma function, not an edgeR function; limma is loaded in the background when edgeR is loaded). As per the Limma manual, "The distance between each pair of samples (columns) is the root-mean-square deviation (Euclidean distance) for the top genes. Distances on the plot can be interpreted as leading log2-fold-change, meaning the typical (root-mean-square) log2-fold-change between the samples for the genes that distinguish those samples."

If this is not what was done and the authors used a different approach to calculating the distance matrix, why was this done, and how should it be interpreted, especially in light of figure 2? Are the trends reported in this figure (and associated supplements) contingent on the distance metric choice?

3. DE testing methods: It's not clear from the text whether any additional covariates (eg known covariates such as sex or age of the individuals, batches even though they were randomised,) were included in the model or whether samples from the same individual were treated as random effects. As above, I am not asking for a redo at this point, but I think it is important to state these details clearly to ensure reproducibility.

4. Outlier detection: It's not clear to me how this works, from the text (especially as it suggests the opposite of that is described in the response to my original comment). The authors first calculate a mean and sd, and then choose humans as a reference species against which to make comparisons. Does this mean that an outlier gene between humans and chimps is an outlier in the chimpanzee lineage? How can it be an outlier in the human lineage if the human is the reference? I do really appreciate the authors for discussing (line 351) the implications of using humans as the reference, given the general evolutionary shifts we naively expect in the human brain, but in that case, can the data please be included as a supplement?

Other questions:

1. Line 182: Since hominoid expression levels are driving so much of the variation in the PCoA analyses, why do the authors think that this isn't showing up in the phenograms?

2. Line 224: Why are the differences between human and siamang treated as human-specific, rather than informative about all great apes? I do not see how this can be disambiguated with the current setup…

3. Figure 3: I think an upset plot or similar here could be an effective way of visualising results, in terms of exploring how far down the phylogeny some signals are shared, but this is optional.

4. Discussion: I think the sentences beginning in 404 and 407 are fundamentally contradictory, and only 407 seems to truly reflect the results above. Is a reference or a word missing from 404?
