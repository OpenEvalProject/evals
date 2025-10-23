# Peer review - Round 1

Editors:
- Daniel J Kliebenstein, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65857.sa1](https://doi.org/10.7554/eLife.65857.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Genetic variation and cell type specific regulation can intersect to influence quantitative traits. However, finding these cell type specific eQTLs is complicated by the factorial nature of these experiments. In this work, the authors use a pooled transcriptome/genotyping approach with single cell sequencing to begin obtaining a broad overview of the genetic architecture of genotype x cell type interactions.

Decision letter after peer review:

Thank you for submitting your article "Whole-organism eQTL mapping at cellular resolution with single-cell sequencing" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ewan Birney (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) Clarify and explain the genotyping information/approach that is largely in the supplement. Each reviewer has a comment along these lines.

2) Temper some claims in the Introduction and Discussion per the reviewers suggestions.

Reviewer #1 (Recommendations for the authors):

The concept of using transcriptomes to simultaneously genotype and phenotype samples is actually a somewhat old concept first established in plants in the era of microarrays. I'm not sure if it is appropriate to not cite the original literature establishing this concept. Some acknowledgment of past developments should be provided.

Introduction – Is it really valid to say that eQTLs have been proposed to underly genetic associations? Seems like there is a ton of validation studies in Yeast, C. elegans, Drosophila, Maize and Arabidopsis that move this beyond the "proposed" stage.

Results – the authors report that the # of eQTLs is correlated with the number of cells of that type in the sequencing data. This suggests that what is actually happening is the # of cells is correlated with the number of independent individuals represented. It would help if the authors could use the genotyping information to estimate the number of individuals contributing to each cell type. This should be obtainable from the genotyping information.

Reviewer #2 (Recommendations for the authors):

My only 3 issues I would like addressed is that I would prefer Supplementary Figure 2, where they use an HHM to impute the genotypes for each cell, to be adapted to be a main figure along with some text to explain exactly how they do this since it is pretty important for the conclusions. I'd also like some discussion about the ultimate biology that the eQTLS underlie – there are differences in the biology of N2 and CB4956 and it would be nice if they would comment on whether any of this can be explained by eQTLS and the genes affected (even if the answer is negative, totally fine with that). Finally, I note that while eQTLS were previously reported to often show transgressive segregation, this appears not to be the case for the ones found here if I understand correctly and I'd be curious to know the reason– It's a great paper, the writing is clear, the conclusions are strong and the approach is important.

Reviewer #3 (Recommendations for the authors):

This paper is great.

My major recommendation is lifting a bit more of the methods into the main text. Naively when I was reading this I was wondering why the authors had not used a more joint model that could borrow power between cell lines; once I had read into Equations 3 and 4 in eQTL mapping I decided that this was a harder problem than I thought. You might want to hint in the Discussion about taking Equations 3 and 4 into a world where you borrow power between cell types, but it would seem inappropriate to suggest you did this in this paper.

Overall I think you should bring this out in the main text more, and have paragraph on this (maybe Equations 3 and 4 in the main text?).

Specifically I was curious about the Xt. Bt term, which seemed to suggest to me that without this term "bad things happened" (fair enough) but if so I think you should expand more (at least in the supplement) why this term is there.

I am somewhat surprised that the probabilistic genotyping does not go closer to 1 for the homozygous calls (at least in the example shown) and I would.… prefer to see some discussion / exploration of this; surely the homozygous segments must be pretty obvious in the data. If one had some elementary error about homozygous calls from the highly expressed genes…what would happen? Is the issue predominantly about the expression levels to "rule out" het calls? Perhaps the average recombination size and the sparsity of the highly expressed genes make this hard? (And please let us know whether choosing F4 over F2 was in hindsight a good choice.) It feels cute but that there is something here which looks wrong. I don't think this invalidates anything, I am curious about your recommendation for future designs. If you think a future design would be better at the F2 level, I would state that.

In theory you should be able to do ASE. Of course, full ASE will just get mis called (goes homozygous) but partial levels should be "callable" (and goes to the question above – to what extend is a F4 too many switches to model). I would comment on it, even if you don't do it.
