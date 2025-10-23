# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31035.023](https://doi.org/10.7554/eLife.31035.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Phenotype inference in an Escherichia coli strain panel" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you will see below, the reviewers appreciated the extensive analysis and believe that the data will be a useful resource for the community. Please see below technical issues that were raised by the reviewers, which should be addressed in full, as you revise your submission for the Tools and Resources section.

Reviewer #1:

This paper does an extensive analysis and prediction of phenotypes caused by mutations in a large E. coli strain panel evaluated over several hundred conditions.

Overall, my concern with this paper applies similarly to many large-scale, high-throughput works I see: The authors have done so much, and are trying to present so many different results and approaches in one paper, that it's difficult to evaluate what exactly was achieved. This paper is either a monumental achievement or a collection of trivial results, and I find it difficult to distinguish between the two possibilities.

I am tentatively willing to give the authors the benefit of the doubt, but I have specific questions and concerns that would strengthen my confidence in the work.

- "We detected no strong positive correlation" this is a strange sentence, in particular if it then lists a significant negative correlation. I think the authors need to explain first why they would expect a positive correlation.

Also, with regards to these correlations, because of the phylogenetic dependency among strains they should be calculated on phylogenetic independent contrasts. Alternatively, it would be better to not report a p value than to report an incorrect one.

- Figure 3A: The precision-recall curves don't look particularly impressive. They rapidly decay to a precision below 0.5, at which point more cases are called incorrectly than correctly.

- Figure 3B: This figure is not properly explained. First, what are the small gray dots? Second, what are the three thick gray dots labeled as shuffled strains, shuffled sets, and random sets? Each randomization should provide a distribution which then is compared to one PR-AUC value. If the true PR-AUC value is rare under reshuffling, then it is significant. This relationship is not in any way visible in the figure.

- Figure 4: Again, the precision-recall curve looks pretty bad. I grant that there's some enrichment of phenotypes towards the top end of the predicted phenotype scale, but the prediction quality is not impressive and it's not clear to me whether a trivial predictor (e.g., one only evaluating whether an amino acid has been changed towards a highly biochemically dissimilar one) could do just as well.

- Section on "Experimental validation of causal variants": It is not entirely clear to me what has been achieved here. If a mutation knocks out an essential gene then clearly that defect can be rescued via complementation. So the achievement would have to be to predict that a gene is essential only under specific conditions. Is that what was done? And if so, how? Was essentiality simply observed, by noting that strains with mutations in certain genes wouldn't grow under specific conditions? Or was it somehow inferred from some other data?

- "with prior knowledge on gene essentiality" I'm not entirely convinced that gene essentiality matters all that much. A mutation in a non-essential gene can have a substantial fitness effect, and a mutation in an essential gene that doesn't fully disable that gene's function may have only a minor fitness effect.

- It is unclear to me whether the code underlying the mutfunc database has been provided or not. The database looks nice, but I'm generally wary of any bioinformatics tool that I can't download and run on my own machine. The authors provide several pipelines (https://github.com/mgalardini/screenings, https://github.com/mgalardini/pangenome_variation, https://github.com/mgalardini/ecopredict), but none seems to perform the task of the mutfunc database.

Reviewer #2:

We have read the study entitled "Phenotype inference in an Escherichia coli strain panel" by Galardini et al. This study performs phenotypic screens for 894 E. coli strains across 214 growth conditions. Most of the strains (696) have full genome sequence available. Gene-level functional predictions were correct in up to 38% of cases. This dataset will become an important and useful resource for the systems biology and microbiology community. We would appreciate of the authors addressed our minor comments below:

We commend the authors for putting all of their data in easily accessible format on github with links out to all of the available assemblies and phenotype measurements. This inclusion will ensure that the resource is easy to use for the research community. However, one question remains regarding the new annotations for each strain. Are these available anywhere? It was difficult to find them both on the web or in the authors’ supplemental files.

The authors previously used this approach on yeast with a median predictive performance of 0.76 (Jelier et al. 2011), but were only able to reliably predict 38% of the conditions tested in this instance. Could the authors comment on why their performance was lower?

Why did the authors use ParSNP to compute phylogeny rather than other methods (such as MLST, whole genome alignment, etc). The authors look for a correlation between phylogeny and genotype. Could the lack of correlation be due to assumptions made when calculating the phylogeny?

Why did the authors choose to incubate the most of the conditions at room temperature rather than the more common 37C? Might this significantly impact their results (i.e. would growth capabilities change if incubated at 37C?).

How do the authors define the "accessory genes/genome". Are these simply all genes that are not part of the core genome? Could the authors comment on the completeness of the genomic sequences in the data set?

Were SNPs only called for sequences in common with the reference E. coli K12 genome? Would that potentially explain some of the discrepancies between the model predictions and the experimental outcome?

Does the term "mechanistic" appropriately describe the method used? Especially when one considers disruption scores in many areas of a genome and the conditional essentiality of genes?
