# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64740.sa1](https://doi.org/10.7554/eLife.64740.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Global epistasis emerges from a generic model of a complex trait" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Dmitri A Petrov (Reviewer #1); Kristina Crona (Reviewer #2); Joachim Krug (Reviewer #3).

As you will see below, all reviewers were excited about the quality of the work. Still, to make is accessible to broad audience, the paper would benefit from revising the writing, making it more accessible and precise. Please relate to all comments below.

Reviewer #1 (Recommendations for the authors):

I have little to add to the paper and I strongly support its publication.

Some points that come to mind as a reader:

1. I would have liked more detailed analysis of the connection between the extreme value theory and the results in the paper.

2. most experimental evolution is not done in the WMSS regime and indeed the authors suggest that the failure of their predictions in the cases of LTEE might be due to the strong mutation regime of the LTEE. Can more be said about the expected differences in predictions in the strong mutation regime?

3. I imagine these arguments were made in engineering or catastrophe theory or economics or control theory – is this true? The results feel so generic that they would apply to all complex systems.

4. What do you results say about the evolution of modularity and how epistasis would evolve?

Reviewer #2 (Recommendations for the authors):

The authors should address the fact that diminishing return and increases costs occur for landscapes beyond the type considered. For instance, consider a biallelic 20-locus fitness landscapes associated with stabilizing selection, where genotypes are represented as bit strings and

wg=1-∣∑gi-10∣20

A mutation 0 ↦ 1 for a genotype g results in the fitness difference

-120if∑gi≥10120if∑gi<10

There is no regression effect here. However, by adding random noise to the fitness values and instead assume that wg=1-∣∑gi-10∣20+εg the result is a landscape with both diminishing return and increased costs effects.

A. Major comments and recurrent issues.

1. Throughout the paper, the manuscript seems to assume SSWM, and fall back on Gillespie’s theory for small fitness differences between genotypes. For instance the author writes (Page 15):”This analysis suggests that during adaptation, since selection favors mutations with stronger fitness effects on the current background, a mutation that interacts less with previous mutations is more likely to be selected.” However, if two beneficial mutations have strong effects than they are about equally likely to go to fixation.

2. Every mathematical expression in the main text should have an explanation or a reference (for biology journals that is a reasonable requirement).

3. References are missing throughout the manuscript. There is not even a reference for”Krawtchouk polynomials”.

4. The SI is too difficult to read in my view. More detailed argument would help, and also useful references for readers who need to catch up, or review, say Fourier representations or Brownian motion.

5. Throughout the main text, the manuscript abuses notation for Fourier coefficients (without comments). The expansion on Page 2 assumes that i > j for fij (and similarly) but later on the authors use fij where i < j (at first the notation was confusing to me, especially subscripts of the type i 6 = j > k). At least a comment should be provided, or otherwise the notation should be changed (in fact the manuscript uses different notation in the SI, Page 9).

6. The following type of expression was unclear to me before I read the SI (on Page 6 and other places in the manuscript):

∑ fj fij+∑ fjk fijk +….

7. The expression”slope for a double mutant”, and similarly, sounds strange (on Page 9 and other places in the manuscript). Here the fitness of a double mutant is compared to the sum of the fitnesses for the corresponding single mutants (something similar should be stated for clarity).

8. It would be great with an explicit example (a toy example) of a landscape where global epistasis varies substantially between loci, for some intuitive understanding.

B. Detailed comments in order of appearance. Most comments below are very minor and concerns notation or wording. The list is not intended to be complete (in fact most comments concern the first few pages and the corresponding part of the SI). Similar minor issues were noted throughout the manuscript, but all of it can be handled swiftly.

1. Page 1:” However, the mechanistic basis of this global epistasis remains unknown.”

The manuscript provides statistical rather than mechanistic explanations. (A mechanistic explanation would concern protein folding or something.)

2. Page 5: “In other words, Equation 2 implies that widespread independent idiosyncratic epistatic interactions lead to the observed patterns of diminishing-returns and increasing-costs epistasis.”

Equation 2 does not imply anything, since such an expansion is possible for any genotype. It would make more sense to simply say:”We argue that wide spread independent idiosyncratic epistatic lead to diminishing return and increasing costs epistasis.” Alternatively, explain the connection to Equation 2 in a more precise way.

(The heuristic argument on the same page is very nice!)

3. Page 6, L 103: The definition of v~iis very important and should be clarified. Explain the symbols ∑ fj fij+∑ fjk fijk +… and explain the symbols in the denominator. (It would also be nice with a brief description of how the expression is composed from the regression argument in the SI.)

4. Page 6, L108:”Note that these results hold for any fitness landscape”. This is not true, as the text also states a few lines later.

5. Page 6, L 120: Why does the sum scale as l?

6. Page 8, L 162:”The theory additionally predicts.…” What exactly is the claim? Does the claim concern any double mutant such that the corresponding single mutations are beneficial?

7. Page 8, L 171:”To test our analytical results” Sounds strange, simulations do not verify analytical results. What exactly is the purpose of the simulation (an illustration of the analytical results perhaps)?

8. SI: It would be much easier to read the SI if it started with Part A followed by Part I. The reason is that Part I uses vi that is defined in Part A.

9. SI: The notation makes the reading more difficult than necessary in a few places. For instance the symbols yi and yi are unrelated, whereas yi and ξi are closely related. In addition, more informative notation could save time for a reader, such as y(xi = 1), y(xi = −1) rather than y~iand y^i.

10. SI, L102: Since v~iis important, it seems reasonable with more explanations of the derivation. Properties of the Fourier expansions are used for cancelling out terms and other simplifications (which is also mentioned), but explicit arguments are not provided.

11. Why is v~idefined as half of the negative slope? Later on -2v~ishows up in formulas. It would make more sense to define v~ias the slope, which would also make it easier to interpret some formulas in the main text.

Reviewer #3 (Recommendations for the authors):

The results for the symmetric model are much simpler and more transparent – the slope of the regression is strictly negative, and has a natural interpretation in terms of variance fraction, whereas the corresponding expression (4) in the directed case looks intimidatingly complicated and obscure. I had a hard time understanding the difference between the two cases and the meaning of the statement that in the symmetric model "the fitness effects of both xi = -1 \to +1 and xi = +1 \to -1 are regressed against the background fitness". My interpretation of this is now the following:

To apply the symmetric model to experimental data, along with each mutation also the corresponding reversion would have to be included in the data set. Whereas the selection coefficient of the reversion is simply the negative of that of the mutation, it happens on a different background, and therefore the effect of including it in the regression is not trivial. In practice, including the reversions is of course not possible, and therefore the directed model is needed, although conceptually the symmetric model is more appealing.

If the authors agree with the above, I suggest that they add some explanation along these lines in the manuscript.

The following points concern the same issue:

1. In the application to experimental data, it is of course also not possible (or meaningful) to distinguish between the two directions xi = -1 \to +1 and xi = +1 \to -1. It is therefore a bit worrisome that (3,4) depend on the direction. I assume that in practice the data analysis is anyway restricted to the WE limit where the difference between the two direction does not matter. Is that correct? If so, it should be explicitly stated.

2. The description of how the model is applied to the data of Johnson et al. (Methods and Materials, lines 524 ff.) is not entirely clear. Why can the variance fraction be estimated from the Pearson correlation between yi and y? And what does it mean (in line 534) that the slope of the regression is either 2vi – 1 or 2v~i -1? If the directed model applies, the slope should always be 2v~i – 1. Related to this, in Figure 3a it seems -2v should be replaced by -2v~.
