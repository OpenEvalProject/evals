# Peer review - Round 1

Editors:
- Frank Chan, University of Groningen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.102321.3.sa0](https://doi.org/10.7554/eLife.102321.3.sa0)

This study makes the important finding that pleiotropy is positively associated with parallelism of evolutionary responses in gene expression. This finding, if true, runs counter to current expectations in the field. The analysis uses state-of-the art experimental evolution approach to study the genetic basis of adaptation of Drosophila simulans to a hot environment. Although the experimental results are convincing, the theoretical model is incomplete, due to several unusual assumptions. It remains to be seen whether the main conclusion can be replicated in other contexts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102321.3.sa1](https://doi.org/10.7554/eLife.102321.3.sa1)

When different groups (populations, species) are presented with similar environmental pressures, how similar are the ultimate targets (genes, pathways)? This study sought to illuminate this broader question via experimental evolution in D. simulans and quantifying gene-expression changes, specifically in the context of standing genetic variation (and not de novo mutation). Ultimately, the authors showed pleiotropy and standing-genetic variation play a significant role in the "predictability" of evolution.

The results of this manuscript look at the interplay between pleiotropy, standing genetic variation and parallelism (i.e. predictability of evolution) in gene expression. Ultimately, their results suggest that (a) pleiotropic genes typically have a smaller range in variation/expression, and (b) adaptation to similar environments tends to favor changes in pleiotropic genes, which leads to parallelism in mechanisms (though not dramatically). However, it is still uncertain how much parallelism is directly due to pleiotropy, instead of a complex interplay between them and ancestral variation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102321.3.sa2](https://doi.org/10.7554/eLife.102321.3.sa2)

Summary:

Lai and collaborators use a previously published RNAseq dataset derived from an experimental evolution set up to compare the pleiotropic properties of genes which expression evolved in response to fluctuating temperature for over 100 generations. The authors correlate gene pleiotropy with the degree of parallelisms in the experimental evolution set up to ask: are genes that evolved in multiple replicates more or less pleiotropic?

They find that, maybe counter to expectation, highly pleiotropic genes show more replicated evolution. And such effect seems to be driven by direct effects (which the authors can only speculate on) and indirect effect through low variance in pleiotropic genes (which the authors indirectly link to genetic variation underlying gene expression variance).

Weaknesses:

The results offer new insights into the evolution of gene expression and into the parameters that constrain such evolution, i.e., pleiotropy. Although the conclusions are supported by the data, I find the interpretation of the results a little bit complicated.

Major comment:

The major point I ask the authors to address is whether the connection between polygenic adaptation and parallelism can indeed be used to interpret gene expression parallelism. If the answer is not, please rephrase the introduction and discussion, if the answer is yes, please make it explicit in the text why it is so.

The authors argument: parallelism in gene expression is the same as parallelism in SNP allele frequency (AFC) (see L389-383 here they don't mention that this explanation is derived from SNP parallelism and not trait parallelism, and see Fig1 b). In previous publications the authors have explained the low level of AFC parallelism using a polygenic argument. Polygenic traits can reach a new trait optimum via multiple SNPs and therefore although the trait is parallel across replicates, the SNPs are not necessarily so.

In the current paper, they seem to be exchanging SNP AFC by gene expression, and to me, those are two levels that cannot be interchanged. Gene expression is a trait, not a SNP, and therefore the fact that a gene expression doesn't replicate cannot be explained by polygenic basis, because again the trait is gene expression itself. And, actually the results of the simulations show that high polygenicity = less trait parallelism (Fig4).

Now, if the authors focus on high parallel genes (present in e.g. 7 or more replicates) and they show that the eQTLs for those genes are many (highly polygenic) and the AFC of those eQTL are not parallel, then I would agree with the interpretation. But, given that here they just assess gene expression and not eQTL AFC, I do not think they can use the 'highly polygenic = low parallelism' explanation.

The interpretation of the results to me, should be limited to: genes with low variance and high pleiotropy tend to be more parallel, and the explanation might be synergistic pleiotropy.

Comments on revisions: The authors didn't really address any of the comments made by any of the reviewers - basically nothing was changed in the main text. Therefore, I leave my original review unchanged.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102321.3.sa3](https://doi.org/10.7554/eLife.102321.3.sa3)

The authors aim to understand how gene pleiotropy affects parallel evolutionary changes among independent replicates of adaptation to a new hot environment of a set of experimental lines of Drosophila simulans using experimental evolution. The flies were RNAsequenced after more than 100 generations of lab adaptation and the changes in average gene expression were obtained relative to ancestral expression levels from reconstructed ancestral lines. Parallelism of gene expression change among lines is evaluated as variance in differential gene expression among lines relative to error variance. Similarly, the authors ask how the standing variation in gene expression estimated from a handful of flies from a reconstructed outbred line affects parallelism. The main findings are that parallelism in gene expression responses is positively associated with pleiotropy and negatively associated with expression variation. Those results are in contradiction with theoretical predictions and empirical findings. To explain those seemingly contradictory results the authors invoke the role of synergistic pleiotropy and correlated selection, although they do not attempt to measure either.

Strengths:

The study uses highly replicated outbred laboratory lines of Drosophila simulans evolved in the lab under constant hot regime for over 100 generations. This allows for robust comparisons of evolutionary responses among lines.

The manuscript is well written and the hypotheses are clearly delineated at the onset.

The authors have run a causal analysis to understand the causal dependencies between pleiotropy and expression variation on parallelism.

The use of whole-body RNA extraction to study gene expression variation is well justified.

Weaknesses:

The accuracy of the estimate of ancestral phenotypic variation in gene expression is likely low because estimated from a small sample of 20 males from a reconstructed outbred line. It might not constitute a robust estimate of the genetic variation of the evolved lines under study.

There are no estimates of the standing genetic variation of expression levels of the genes under study, only estimates of their phenotypic variation. I wished the authors had been clear about that limitation and had refrained from equating phenotypic variation in expression level with standing genetic variation.

Moreover, since the phenotype studied is gene expression, its genetic basis extends beyond expressed sequences. The phenotypic variation of a gene's expression may thus likely misrepresent the genetic variation available for its evolution. The authors do not present evidence that sequence variation correlates with expression variation.

The authors have not attempted to estimate synergistic pleiotropy among genes, nor how selection acts on gene expression modules. It makes their conclusion regarding the role of synergistic pleiotropy rather speculative.
