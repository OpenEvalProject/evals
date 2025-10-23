# Peer review - Round 1

Editors:
- Anthony Fodor, University of North Carolina at Charlotte

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21887.024](https://doi.org/10.7554/eLife.21887.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A phylogenetic transform enhances analysis of compositional microbiota data" for consideration by eLife. Your article has been favorably evaluated by Wendy Garrett (Senior Editor) and three reviewers, one of whom, Anthony Fodor, is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Juan José Egozcue (Reviewer #2). All three reviewers found considerable merit in the manuscript praising the originality of the idea, the clarity of the presentation and the effectiveness of the visualizations.

For your reference, I have attached the three original reviews below. Per the eLife policy, you are not required to respond to each individual point raised by each reviewer. Below you will find a summary of the reviews reflecting the consensus of the reviewers of required revisions.

Summary:

It has long been recognized that compositional data is best analyzed in ratio space. For 16S rRNA sequence datasets and other genomic datasets, this leads to the rather difficult question of what ratio to take. In this interesting manuscript, Silverman et al. suggest taking ratios on a bifurcating phylogenetic tree. In their approach, the dependent variable for each node of the tree is a "balance", which is a normalized ratio of all the nodes beneath each node (with the ratio of all the left descendant nodes over all the right descendant nodes). The paper explores the consequences of this normalization showing reasonable performance when used for classification or machine learning. The authors provide an implementation in R and this approach may be of utility for analysts looking for a novel way to analyze microbial data in ratio space.

Essential revisions:

1) There was consensus among the reviewers that the normalization scheme seemed a bit ad-hoc and poorly justified. We suggest that it is made clear to the readers that the choice of weights used in the manuscript, both on the taxa and on the tips, are preliminary choices and further work will be required to ultimately determine the best weighting scheme. In addition, some further clarification on how sparsity was treated would strengthen the manuscript.

2) None of the reviewers were entirely satisfied with the demonstration that the proposed transformation was superior to other transformations. It is unclear what it means, for example, that the PhILR technique sometimes produces a stronger clustering signal and sometimes a weaker clustering signal than weighted UNIFRAC (Figure 2B). There was some discussion among the reviewers about whether a comparison to random binary partitions would be appropriate since this could reflect your null model (that phylogenetic binary partition is superior). Reviewer #2 was not enthusiastic about this idea and argued that a change on a tree does not alter (Aitchison) distances between data points. Therefore, results would likely not change no matter which tree has been selected for defining ILR coordinates.

In the end, the consensus of the reviewers was that exploring such null models might be of interest, but would not be appropriate as a requirement for revision. Nonetheless, reviewer #1 would have been interested to see if machine learning algorithms in fact performed better on the phylogenetic partition in comparison to random partitions. We leave it up to the authors as to whether they feel such an inclusion would improve their paper or be worth the effort. However, all reviewers felt that paper would be improved by more discussion of how to tell when one normalization procedure is superior to another. It seemed to reviewer #1 that it might be adequate to say that the proposed transformation appears to be doing no harm relative to weighted Unifrac but was providing some compositional safeguards. Reviewer #2 argued that the main benefit of the proposed procedure was in interpretability in yielding a phylogenetically aware transformation that could be utilized for test-statistics.

3) There was general consensus among the reviewers that Figure 4 was unconvincing in that technical (non-biological) features of the algorithm could explain the results more easily than exclusionary dynamics. The authors could likely remove Figure 4 without damaging the paper, but if they choose to keep it, they should respond to the concerns below from reviewers #1 and #3 as both reviewers felt that simple lack of association between taxa and stochastic variation in sampling could explain many of the observations in Figure 4.

4) There was consensus among the reviewers that the authors could provide more guidance to the non-specialists about when this algorithm should be used. As reviewer #3 put it, when and why should a reader choose the PhILR approach and when should it be avoided.

5) The authors should be explicit about what filtering and other pre-processing steps were used and whether those choices substantially impacted the performance of their algorithm.

Reviewer #1:

It has long been recognized that compositional data is best analyzed in ratio space. For 16S rRNA sequence datasets and other genomic datasets, this leads to the rather difficult question of what ratio to take. In this interesting manuscript, Silverman et al. suggest taking ratios on a bifurcating phylogenetic tree. In their approach, the dependent variable for each node of the tree is a "balance", which is a normalized ratio of all the nodes beneath each node (with the ratio of all the left descendant nodes over all the right descendant nodes). This is a clever idea and the authors make a reasonably compelling case that this is a useful contribution. While the evidence from the machine learning and clustering portions of the paper provide only modest evidence that this transformation is substantially better than other transformations, the transformation clearly is not making things much worse. As such, the proposed method will be of interest to researchers interested in how best to approach the challenging problem of compositional analyses of microbial datasets.

Suggestions for improvement follows:

1) The mathematical description of the algorithm could be improved in terms of its clarity. For example, it is not always clear how the pluses and minuses in the second equation of the subsection “The ILR Transform” are defined. It is not made immediately clear that the leftmost term (sqrt(ni+ * ni- / (ni+ + ni-)) in that equation is a correction for branch length. For the equation in the subsection “Addressing sparsity through weighting taxa”, please use parentheses to emphasize that the formula is sqrt(sum(xj)) * ((sum(cj 1…N)) ^ 1/N and not sqrt(sum(xj))^N * sqrt(sum(cj 1…N))

2) A limitation of working in ratio space in 16S data is what to do with all of the zeros in the spreadsheet (the "sparse data" problem). There is nothing inherent to the balancing algorithm that can deal with this problem (the sum in the denominator of the balance obviously can't be zero). The authors therefore require some kind of pseudo-count scheme and they have settled on one (given in the equation in subsection “Addressing sparsity through weighting taxa”) which is a function of the number of samples. If I am reading their formula correctly, the weight given to a taxa with 1 read in one sample and zero in all others would be very close to the sqrt(number of samples). The authors might consider giving this as an example and explicitly noting that their method has some similarity to adding the sqrt(number of samples) as a pseudo-count.

3) I struggled a bit with the variance analysis which concludes the Results sections. In the second paragraph of the subsection 2Balance variance and microbiota assembly” it is argued that "When the variance of a balance between two clades approaches zero, the mean abundance of taxa in each of the two clades will be linearly related and thus exhibit shared dynamics across microbial habitats". While this is true (and must be true mathematically as when the variance approaches zero, the ratio of the two normalized abundances of the clades is constant, which means they will become perfectly linearly related with a positive slope), it's not clear to me that a high variance necessarily means "exclusionary dynamics across samples". I don't see how a high variance in this number indicated anything about how direct or indirect the interactions are within the tree. There are lots of reasons two clades could lack perfect linear correlation with a positive slope from direct competition to being completely unrelated biologically with abundances just shifting due to stochastic variation. Also, wouldn't variance have to be lower closer to the tips of the phylogenetic tree as the number of sequences is lower, so the pseudo-count has more of an effect depressing overall variance? Doesn't that explain Figure 4D-F? And if I am reading these graphs correctly, below the species level there are not enough datapoints to support modeling via localized regression one way or another. Although not central to the arguments of the paper, I found Figure 4 to be less convincing than other sections of the paper.

Reviewer #2:

The manuscript introduces two new powerful ideas. They are: (a)construction of the sequential binary partition used to define

ILR coordinates on the base of phylogenetic trees; (b) use therecently published balances in weighted compositions to account forphylogenetic distances between OTU's or taxa. Both ideas aredeveloped and applied successfully to benchmark data sets.

For the originality of main ideas applied to microbiome analysis,the manuscript deserves publication.

Reviewer #3:

The manuscript is, in general, written in a clear and logical manner with a minimum of technical jargon. Figures 1, 3 and 4 are outstanding examples of data visualization and demonstrate the utility of this approach over others extant in the field. Figure 5 seems an afterthought and could be combined with Figure 1, or made supplementary. The binary portion could also be completely described in the Methods without a figure.

Figure 2, and the associated descriptive text are somewhat underwhelming demonstrations of the utility of the approach, which, in theory, should clearly outperform all other methods if the compositional data approach is necessary. The use of box-plots probably does not aid the visual appeal.

That the ILR based distance can seriously underperform the weighted unifrac metric is puzzling and cause for concern, since PhILR becomes another metric to be 'mined' to achieve the desired outcome. Does the PhILR partitioning scheme outperform a simple random binary partition? this is crucial to know.

There needs to be serious guidance given to the reader as to when and why to choose the PhILR approach and when not to. The same can be said for the classification methods shown, where the PhILR generally (but not always) outperforms relative abundance, but not log relative abundance. I am left to wonder if data analysis choices are driving these results.

Finally, I am puzzled as to why the authors chose to take a rigorous variance-based approach (ILR) and analyze it using a distance-based metric. It is established in the CoDa literature that Mahalanobis distances are often more appropriate for clustering based approaches and for outlier detection (see for example: http://www.statistik.tuwien.ac.at/public/filz/papers/2010Compstat.pdf). Did the authors examine other distances?

I believe that Figure 4 is somewhat over-interpreted. Subsection “Balance variance and microbiota assembly”, last paragraph: There are many technical reasons such as inefficient clustering, etc. that closely related sequences (called bacteria here) could exhibit strong correlations. Reading Lovell (referenced in this manuscript), and the points shown in 4G-L, indicate that an alternative explanation to that given in the text (see aforementioned subsection, end of second paragraph) is that a higher balance variance would be compatible with a model of indifference rather than competition since the vast majority of high variance ratio balances are likely to be non-correlated balances (Lovell 2015). Such non-correlated balances persist even out to the extreme tails and there is as yet no general principled approach to identify negative correlations in compositions.

Introduction, last paragraph: “the accuracy of distance.…” – this is a strong statement to make as the underlying standard of truth is assumed, not known from first principles.

Subsection “Addressing sparsity through weighting taxa”, first paragraph: I would argue that total read counts contain information on precision, not variance. It is hard to square this statement with the otherwise compositional approach used in the paper.

Subsection “Addressing sparsity through weighting taxa”, second paragraph: Why use a prior of one. The supplement that I found did not support the assertion that the prior chosen had little effect. This needs to be clarified.

Subsection “Human Microbiome Project (HMP)”: What is the effect of filtering and preprocessing on the method? As with many methods papers, the arbitrary choices here have the potential to become the accepted norm later without evidence.

Subsection “Supervised Classification”, first paragraph: Were the log-transformed data not scaled? if not, this is a problem since it is not a fair comparison.
