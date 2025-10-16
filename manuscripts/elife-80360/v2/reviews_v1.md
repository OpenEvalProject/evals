# Peer review - Round 1

Editors:
- Timothy W Nilsen, https://ror.org/051fd9666 Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80360.sa0](https://doi.org/10.7554/eLife.80360.sa0)

This is a valuable study that provides compelling evidence for important nucleotides in five self-cleaving ribozymes. Epistasis analyses are novel in this field.


---

# Peer review - Round 1

Editors:
- Timothy W Nilsen, https://ror.org/051fd9666 Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80360.sa1](https://doi.org/10.7554/eLife.80360.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "RNA sequence to structure analysis from comprehensive pairwise mutagenesis of multiple self-cleaving ribozymes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Timothy Nilsen as Reviewing Editor and James Manley as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Philip Bevilacqua (Reviewer #1); Benoît Masquida (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

All the reviewers felt that the work was, in principle, suitable for publication in eLife. Nevertheless, the reviewers felt that the data was under-interpreted and that analyses from a 3D perspective would improve the paper significantly. Please see the reviews below. In this case, any revised manuscript will be subject to rereview.

Reviewer #1 (Recommendations for the authors):

1. p8. The longer size of HDV does not explain the fewer reads for it because it is only slightly longer than the other ribozymes. What about the stability of the HDV ribozyme and RT not being able to read through it?

2. p8. What is the minimum number of reads per single mutant in HDV? double mutants? For the latter, the average is only 50 (Figure S1) and the minimum appears to be ~10 reads. Can reliable data be attained with so few reads? What is the statistical significance for low read singles and double mutations?

3. p8. more precise language is needed. Suggestions below. These words do not have to be used but some should be provided to guide the reader. "We plotted the relative activity value as heat maps (Figures 1-5 a large plot, shows only blue color)." "We then used this data to calculate epistasis between pairs of mutations (Figures 1-5 insets red to blue colors)".

4. p8. "many paired regions showed an anti-diagonal line of high activity double mutant variants with strong positive epistasis". It would be helpful to dissect this anti-diagonal into two different distributions: WC+wobbles and mismatches. In other words, there are off-diagonal elements within the anti-diagonal square that are meaningful. This should provide an interesting sub-anativealysis in panel C; specifically, it will allow a look at double mutants that lead to the loss of a single base pair (off-diagonal elements within the anti-diagonal square) vs. a loss of two pairs (off-diagonal squares).

5. Overall fraction cleaved varies wildly between the five ribozymes, from 0.19 to 0.68 (Table 1). It would be helpful to know what the fraction cleaved was for the wild-type ribozymes that emerged from the deep sequencing versus just making the wild-type ribozyme alone and measuring the bulk fraction cleaved from a radiolabeled experiment. This could help the authors discuss how sensitive or robust a given ribozyme is to mutations and then speculate why.

6. Why is panel A different colors for different ribozymes? This seems unnecessary and random (e.g. two of them are blue).

7. p9. Not only were the epistasis values for on- anti-diagonal "consistently more positive than two mutations in positions that are not directly base-paired (off-diagonal)" the latter were often negative (at least the mean was), which should be stated. i.e. "more positive" implies both distributions were positive.

8. Figure 4. The inset for LA/LA is not positioned correctly on the main figure. A28-A31 are should be left-shifted. Moreover, epistasis between LA and LB could not be judged, as the authors would like the reader to do on p12. The authors should provide an LA/LB inset for the reader to look at. Additionally, the authors would like the reader to think about interactions of 1 and 46 but don't draw the pair in panel B, making this hard to visualize. The "positive epistasis" for G42U and A64G is missing in the inset which is entirely white for this square. And the A47:G57 showing "positive epistasis for double mutants that result in an AU base pair" doesn't make sense because this can happen with a single mutant at G57U.

9. p14. The authors give details on epistasis between positions 20 and 25 but nothing is shown in the off-diagonals and this data cannot be had on the main diagram in A.

10. p10. The discussion that "differences between epistasis in short and long base-paired regions suggests that the thermodynamic stability of each paired region is important for the observed activity" is clearly supported by the data but should be explained. Short regions cannot withstand the loss of one and especially two base pairs because they are short and once broken cannot be broken again. Bevilacqua and Herschlag have discussed this and could be consulted and referenced. 1. Moody, E. M. and Bevilacqua, P. C. (2003). Folding a stable DNA motif involves a highly cooperative network of interactions. J. Am. Chem. Soc. 125, 16285-16293. 2. Kraut, D. A., Carroll, K. S. and Herschlag, D. (2003). Challenges in enzyme mechanism and energetics. Annu. Rev. Biochem. 72, 517-571.

11. Methods. The authors did reverse transcription. From Table S1, it appears that extra bases were appended to the 3'end of each ribozyme to provide an RT primer binding site [it appears this way from the first unbolded bases listed at the 5'-end of the template in Table S1]. If so how do those bases affect the fraction cleaved of the wild-type? And then the mutants? See comment 5 above. Also, I was unable to understand how the sequence of the RT primer in Table S1 works with the templates.

12. In the epistasis equation, which should be numbered, what are the authors taking the log of? RA? Shouldn't there be a plus sign between the two terms in the denominator? For e.g. assume additivity RAi = RAj = 10^-1, and RAij = 10^-2, we need a plus sign to have this come out to unity; as it would come out to -2. Also, how does it follow that negative epistasis is less than 0? Shouldn't negative be >1 and positive be <1?

13. We could see some trend in the length of paired regions and the intensity of the epistasis effect, but it was hard to tell whether the negative correlation between the median deleterious effects of single mutations and the minimum free energy of the paired regions was significant from the plot in Supplementary Figure 3 and the given Pearson Correlation = -0.53. Also, it may be good to address and explain the difference in the distribution of epistasis value of CPEB3 P1, P2, and P4, which all have 7 base pairs but are very different in the distribution of epistasis value.

Reviewer #2 (Recommendations for the authors):

Regarding the CPEB3 ribozyme, an open question is about the role of the U21-U42 base pair. Figure 1 indicates that positive epistasis has been measured for some sequence combinations. It would be very sound to frame this region of the heat map together with the T1 interaction to discuss the heuristic power of the presented approach since the CPEB3 ribozyme is the only ribozyme studied in this manuscript for which no crystal structure has yet been made available.

Reviewer #3 (Recommendations for the authors):

1) For example, the way the ribozymes have been randomized is already described in Kobori and Yokobayashi (2016). On the other side, it would be necessary to provide more experimental information on the way the template switching reverse transcription is performed. This is not well explained as there is no clear explanation for the usage of the TSO1-4 oligos… The authors should rewrite the experimental method section of their article so that anybody who wants to use this approach could do it without struggling…

2) While some of this 3D information is seldom mentioned in the text, there is no easy way for the reader to find this information in the data provided. A figure exemplifying some of the key 3D interactions of these ribozymes would be most useful.

For example, it would be nice to have more structural details by eventually showing some of the results within the context of the 3D structures of each ribozyme.

For instance, the Watson-Crick base pair interaction G1C-C46G between LA/LB in the hairpin ribozyme could be shown… The same thing with the base pair C20G-G25C in the hammerhead ribozyme. In fact, the 2D structure of the hammerhead ribozyme could be improved as it does not correspond to the active form.

The authors should also provide more data information (as well as supportive figures) about the tertiary interactions that involve non-canonical base pairs and that show positive epistasis… After all, this is a piece of information that has not yet been obtained before for these ribozymes as it cannot be easily obtained by other approaches.

3) The authors could have certainly enhanced dramatically the scope of their article by trying to validate the structure of a self-cleaving ribozyme for which the 3D structure is not known yet. This would have provided a clear test for their approach and would have enhanced dramatically their claim that it could complement chemical and enzymatic probing.
