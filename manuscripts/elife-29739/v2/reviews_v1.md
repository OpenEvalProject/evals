# Peer review - Round 1

Editors:
- Diethard Tautz, Max-Planck Institute for Evolutionary Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29739.011](https://doi.org/10.7554/eLife.29739.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Intrinsic adaptive value and early fate of gene duplication revealed by a bottom-up approach" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ashley Teufel (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

As you will see, the referees found the problem to be interesting and appreciated your approach, but they also raised a number of issues which preclude publication in eLife. These include:

My read of the reviews is that while there might be an interesting glimmer of an idea here, it hasn't been cashed out properly and what we're left with is a not particularly persuasive model/argument.

It seems that the problems include:

1) An inadequate treatment of previous literature in the area;

2) A possible overstatement of the possible fitness benefits associated with reducing intrinsic noise;

3) Highly optimistic assumptions about how dosage compensation would work and how gene expression would be partitioned.

Reviewer #1:

Authors propose that gene duplication reduces gene expression noise, which could be beneficial and hence lead to the fixation of newly duplicated genes. However, I believe this model is untenable. My detailed comments follow.

1) There is no lack of evolutionary models to explain the fixation and long-term retention of duplicates. In terms of fixation, which is the focus of the present study, a new duplicate may be fixed by positive selection for increased gene dose (for either the main or minor function of the gene) or genetic drift. The Introduction seems to suggest a lack of suitable models (hence need for a new model), which is misleading.

2) The present model relies on a reduction of gene expression noise caused by gene duplication. This noise reduction is tiny. In the best case scenario, the intrinsic noise measured by CV is reduced by 29% upon duplication. But because expression noise is mainly from extrinsic noise, which is not reduced by gene duplication, the fraction of total expression noise reduced is minute (likely <5%).

3) The fitness benefit from 5% noise reduction will be swamped by a much greater fitness cost of doubling the expression of the gene owing to gene duplication. So, authors propose that the total expression level of the duplicate pair is halved by a mutation. Simply halving the total expression is actually not sufficient, because the above calculation of the noise reduction assumes equal expression levels of the two genes. If the two genes have different expression levels, the amount of noise reduced becomes even smaller. So, two very special mutations that reduce the expression of each gene by ~50% are required. I believe the probability of simultaneously acquiring two such mutations in a cell is almost 0.

4) Compared with the probability of acquiring the above two mutations, the probability of acquiring mutation(s) conferring a new function may be larger. In other words, neofunctionalization is probably more likely to happen than the scenario proposed by the authors.

5) Authors based their calculations on one gene (lacZ), but wrote as if the calculations apply to all genes.

6) I wonder why lacZ is not duplicated in E. coli if their theory predicts that duplication of lacZ is beneficial.

7) They provide no empirical evidence for even one duplicate gene that was likely fixed by the mechanism proposed.

Reviewer #2:

Rodrigo and Fares examine the immediate effect of gene duplication on gene expression and fitness, specifically on the reduction of noise in gene expression. The subject is of interest to a large community, including those interested in gene duplication, the evolution of regulatory systems and also microbial adaptation. The way to approach the problem is rather novel and brings to light new aspects on the issue of why would immediate gene duplication be maintained if dosage itself is not favored. The fact that gene duplication may reduce intrinsic noise in gene expression has been noticed before (Wang and Zhang, as cited by the authors) and directly derives from the fact the average of two random values from a distribution are closer to the mean of that distribution than any of the single values are, at least for the type of distributions we are dealing with. Showing this using a well-known regulatory system is valuable, especially if other factors such as trade-off that may derive from the cost of expression or the cost of having two gene copies are considered. That being said, the manuscript as presented would require additional work before it can be considered for publication. Here are some points:

1) The writing needs to be improved. Some wordings are confusing and also the overall structure of the paper would benefit from a more logical organization. The different alternative assumptions should be confronted directly side by side to clarify the limitations and the conditions in which the system could evolve. The issue of trade-off that is introduced as being important in the Introduction should be better addressed.

Here are some examples of sentences that need to be revisited:

- The first sentence of the Abstract is difficult to read. The fact that duplication contributes to complexity implies that duplicates are maintained. Why use “albeit”?

- Introduction, second paragraph, first sentence. This sentence is also hard to follow and brings multiple important elements in a single sentence.

- Introduction, fifth paragraph, second to last sentence. Again hard to follow.

- Introduction, last paragraph. What is a real gene?

- “Here, we simply considered a cost function based on LacZ expression, although it would be more precise a cost based on lactose permease (LacY) activity (Eames and Kortemme, 2012)”. This sentence is difficult to follow.

- “The population was let to evolve without introducing any artifact…”? What does artifact refer to here?

- Subsection “Most of the new-born duplicated genes are costly for the cell and do not offer phenotypic accuracy”, last paragraph. It is strange to start this paragraph with “even though”. We would expect a contrast to be made but it is not the case.

- Subsection “Most of the new-born duplicated genes are costly for the cell and do not offer phenotypic accuracy” “as long as” is not used in the proper context.

- Subsection “Fixation is conditioned by the unexpected recurrence of creation and deletion of gene duplications in a population”, first sentence. The word “created” is used to refer to gene duplication. Gene duplication is a process that cannot be created. Gene duplicates can be created, although I would refrain from using “created” here.

- The authors use “simple” and “punctual” mutation rates. They may want to refer to per base or nucleotide mutation rate instead, or use other standard nomenclature.

- Subsection “A comprehensive model compatible with population genetics to explain the early fate of gene duplications”, second paragraph. It would be better to state directly the effect of generation time rather than mention “simple” organisms because they have short generation time.

.…

2) A large fraction of the results presented assume that the sum of expression of the two copies is equal to the expression of the ancestral copy. This assumption is later relaxed in the paper. However, because expression is likely to scale with copy number, this assumption is most likely extremely optimistic. In addition, it is possible that with two copies, repression is not as efficient and the genes are now expressed even when not needed. The two different scenario (2X expression and 1X expression, and their intermediates if possible) should be compared side-by-side and better arguments should be presented as to why 1X is achievable.

3) The issue of intrinsic and extrinsic noises should be brought earlier in the paper as this is a very important consideration. They could be introduced in the Introduction. Gene duplication is not expected to reduce extrinsic noise and extrinsic noise is usually the primary source of differences among cells. As far as I understand, they are treated as potentially contributing equally in the model, which is clearly not the case in reality.

4) An alternative to duplication is also an increase in expression level, which would make protein abundance more often above the critical expression value and thus also increase fitness, without the need for duplication. Mutations that increase abundance would also then compete with duplications.

5) Subsection “Gene duplication helps to better resolve the fitness trade-off”, second paragraph. The authors describe the fitness landscape as rugged but a rugged fitness landscape has multiple local peaks, which is not the case here.

6) The authors define and introduce phenotypic accuracy, which is basically the inverse of noise. I am not sure more terms are necessary in this field. Not sure also that the use of information transmission helps this study and adds anything to the results.

7) Subsection “Gene duplication helps to better resolve the fitness trade-off”, last paragraph. The authors say that the two surfaces reassemble. This interpretation appears to be rather subjective. It would be useful to explain why this matters and how similar they really are.

8) The authors introduce the concept of trade-off in the Introduction and argue that this is an important factor in evolution but largely ignore them as a constraint on the evolution of expression. At the same time, they state that an increase in expression is detrimental in most environments (subsection “Most of the new-born duplicated genes are costly for the cell and do not offer phenotypic accuracy”, first paragraph). This question needs clarification and again, a better organization of the text would allow to better contrast the systems with and without trade-offs.

9) The authors use a biological context that is laboratory populations and experimental evolution. For instance, they say in the first paragraph of the subsection “Fixation is conditioned by the unexpected recurrence of creation and deletion of gene duplications in a population”, that typical bacteria populations are 109 cells. I presume that they refer to cell populations in the laboratory. It would be more appropriate to refer to biological conditions that occur in nature. Even if laboratory conditions favor some evolutionary paths or dynamics, it would be irrelevant if the conditions do not exist in nature. This comment is also relevant for the simulations with dilutions and exponential growth in a flask. These simulations would be interesting if they were tested experimentally in the laboratory in this study. However, since we want to understand evolution in nature, why not use what is expected to be relevant in natural populations, including effective population size estimates, which have been computed for E. coli I presume. Since theory has shown that duplication reduces noise, what the readers will be really interested in is whether this is sufficient to favor the maintenance of duplicates in a biologically realistic system.

10) Subsection “Phenotypic accuracy can lead to the fixation of a new-born duplicated gene in the population”, first paragraph. Cis regulatory mutations are assumed to act on the average expression and not on the noise in expression. This is a convenient assumption but not necessarily true. Mutations most likely affect both at the same time (See the work of P. Wittkopp). This could reduce the mutational target site available for mutations reducing expression level.

11) Subsection “Phenotypic accuracy can lead to the fixation of a new-born duplicated gene in the population”, first paragraph. The authors discuss the fact that about 10% of mutations affect expression (reduction by about 50%). To calculate the rate at which these mutations occur, one needs to know how many sites in the genome have these effects, not what fraction of mutations that have been studied reduce expression. It is not 10% of all mutations in the genome that reduce expression, but rather 50% of the 75 bp region as studied by Kinney et al. This should be clarified in the calculation. Also, the probability that a duplication and a mutation that reduces expression by 50% occur in the same cell in the same generation depend on their equilibrium frequency and somehow the effective population size? The order of appearance would also matter because reducing the expression of only one of the copy (if the mutation occurs after the duplication) is not going to bring the expression level to the ancestral state.

12) Discussion, second paragraph. It is not clear that all of the results mentioned here derive from the theory proposed and if the results actually suggest a reinterpretation of the results. To be useful, it would be important to have predictions from this model that would be specific to this model and could not be explained by the previous models proposed. Also, it would be useful if some were tested here to actually show that some cases known in nature seem to fit the model. Any variation in gene copy number in bacteria that cannot be explained by dosage effects alone or other models of duplicate evolution?

13) The authors assume that the gene expression partitioning seen for pairs of duplicates is 50-50%, but according to Gout and Lynch, this is very often not the case. It is not clear how an expression partitioning that is not 50% contributes to reduce noise in expression. This could be explored here.

14) Some reasoning needs to be revisited carefully. For instance, in the third paragraph of the Discussion, the authors predict that essential genes would be less duplicable as a consequence of their reduced expression noise. Essential genes are not created essential and may derive from non-essential genes, which were noisy initially. If these genes show less expression noise because they contribute more to fitness, it means that selection for lower noise could have favoured their duplication (at the same time making them non-essential, making this effect hard to see).

15) Subsection “In silico evolution”. Why is evolution envisioned as if it occurred in the laboratory? It is already unclear if experimental evolution reflects evolution in natural systems so simulating experimental evolution appears to move away from nature.

16)Subsection “Genetic diversity”, last paragraph. Wouldn't the equilibrium frequency just be Uc/Ud?

17) Figure 1. Should explain what is x/x0 in the legend.

Reviewer #3:

This manuscript puts forth an interesting new theory on how newly birthed duplicated genes could eventually fix in a population. While the work laid out here seems to be of large interest, I have a few concerns that I would like to see addressed before publication.

My main concern with this publication is that the bulk of the work is centered on examining a system where a duplication does not result in a change of total expression, which is at best a very rare occurrence. While this is discussed later in the manuscript, some justification of why this situation was chosen for the biases of this work should be included in the "Gene duplication helps to better resolve the fitness trade-off" section.

The claim that the actual and the optimal dose-response curves (Figure 1E and Figure 2F) are similar doesn't seem very convincing. Showing this data in something like a q-q plot and reporting a correlation would aid in the argument. This is especially important for Figure 2F when you make the comparison between the duplicate and the singleton, because there does not appear to be much of difference between both.

The comparison of non-normalized mutual information is confusing. Stating what the I values are and that one is 25% higher than the other doesn't convey the message that the duplication changes fidelity in a significant way. Is there an additional metric that could be used to better make this point?

The set up in the Introduction could be improved by adding further detail about why reducing gene expression inaccuracies results in increased fitness.

Often the model is linked to values that have been "experimentally determined" but there doesn't appear to be a clear reference to where these values have come from.

The amount of in. noise is an important parameter in this model. Any statement about the amount of in. noise that exists in biological systems would aid in linking this model back to the biology. Is a moderate (0.3) amount of in. noise to be expected?

The Discussion section largely centers on further directions of this work and ends abruptly. Including a section about the limitations of this work and also casting this work into a larger context would be appreciated.

I believe that eLife requires that you make any code used available. I would suggest putting your simulation code in a repository and including the link in the manuscript.

Overall, this is an interesting manuscript but I feel the way some of the data is presented could be changed to strengthen the author's arguments. By including more detailed statistical analysis and expanding some portions of text for clarity would improve this manuscript substantially.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Intrinsic adaptive value and early fate of gene duplication revealed by a bottom-up approach" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz as the Senior and Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

One reviewer still has some comments on the presentation of your results. Please check these carefully and clarify the issues as much as possible. Such changes should improve the impact that this manuscript will eventually have. While I do not think that further reviewing will be necessary after these changes are introduced, I should like to ask you to provide nonetheless a careful response letter, indicating which changes were incorporated.

Reviewer #2:

I maintain my comments on the previous version of the manuscript. I believe the paper is hard to follow and extremely specialized such that it is hard to evaluate whether the observations are generalizable.

Important concepts in some sections are not introduced properly in the Introduction (tradeoffs for instance do not only include production costs but any other types of negative effects, including in other environments). Some assumptions made for the analysis are not well detailed, for instance the extent of noise in expression, the cost of expression. Another example is the statement made from Figure 6A that most mutations are nearly neutral. Given what was said about the importance of gene expression tuning and the large Ne for E. coli, most of these changes are most likely not neutral at all. This is a surprising statement given that the paper shows that small changes in the distribution of expression levels can affect the fate of gene duplication.

What we would like to know is under which noise regime (showed to be likely based on observations) this mechanism could affect evolution given a clear set of assumptions that are shown to be realistic. I do not feel we know this by reading the paper as it is.

Some of the concepts introduced is not defined properly, for instance phenotypic accuracy. Here the authors say that phenotypic accuracy (…subsection “Gene duplication helps to better resolve the fitness trade-off”, second paragraph) is the fact that phenotypic responses generated by duplicated genes give on average higher fitness values than responses generated by singletons. This is simple corollary to the fact that duplication reduces noise, this is not a new concept that needs the be defined. Using such definitions is just a distraction that reduces our understanding. Same could be said about information content. This is not appropriate for a generalist journal such as eLife.

It is not clear why we need simulations at all if the selection coefficient have been estimated given all of the analytical work that has been done previously (fixation prob. versus Ne and S).

The section on expression demand in extreme environments (subsection “Expression demand in extreme environments can also lead to the fixation of a newborn duplicate in the population”) does not really deal with the question in hand, which is the effect of duplication of noise reduction. There are examples of arbitrary assumptions here too, for instance the consideration of a lac promoter with 40% lower activity as a starting point.

Examples of sections with lack of logical flow:

Introduction, fifth paragraph; subsection “Gene duplication helps to better resolve the fitness trade-off”, first two paragraphs; subsection “Expression demand in extreme environments can also lead to the fixation of a newborn duplicate in the population”, second paragraph.

Reviewer #3:

This version of the manuscript is much improved. I thank the author for careful and detailed comments. I especially appreciate the inclusion of significance statistics and the addition of the "Maintenance of a duplication upon fixation in the population" section.
