# Peer review - Round 1

Editors:
- Vaughn S Cooper, https://ror.org/01an3r305 University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76491.sa0](https://doi.org/10.7554/eLife.76491.sa0)

Johnson and Desai developed an innovative yeast experimental-evolution system where they can insert barcoded disruptive mutations into the genome and measure their individual effect on fitness. They use this system to test whether these mutations have different effects on evolving lineages as they adapt over time. As expected, the mean fitness effect does decline in most (but not all) populations as lineages adapt, but in another condition, mean fitness effects of mutations do not change as the populations adapt. The authors suggest an intriguing interpretation that the ‘control coefficient’ of selection on growth can shift between different genetic modules over time, resulting in differing magnitudes of epistasis.


---

# Peer review - Round 1

Editors:
- Vaughn S Cooper, https://ror.org/01an3r305 University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76491.sa1](https://doi.org/10.7554/eLife.76491.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mutational robustness changes during long-term adaptation in laboratory budding yeast populations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Craig Miller (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) Justify the selection of the 91 mutants and how they are broadly representative. If they are not for the following reasons, considerable additional experiments are required.

In the authors' 2019 study, of ~1,147 insertion mutants assayed, ~91 of them had fitness effects distinguishable from neutral, i.e. ~8% are "effective". If (a) the percentage of "effective mutations" are similar between the genetic backgrounds used in the 2019 study and the current study, and (b) the genetic backgrounds used in these two studies are not correlated, then "effective mutations" from the 2019 study could still be "effective" only by chance. If the same percentage holds, then only 8% of 91 may (7 mutants) be drivers of the DFE or epistasis forms reported here. Though the paper suggests that 20-30 mutants are deleterious in the current dataset (figure 1 supplement 5), the lack of proper error estimates as mentioned below makes it difficult to evaluate these estimates

(2) Clarify the statistical power of various comparisons, as follows. Fitness is obtained by averaging effects on two clones from a population and variation between these measurements due to genetic differences or error are insufficiently accounted for. Some measures have r-squares <0.5, which begs the question, how much of the noise is coming from mutational differences between clones and how much from measurement noise? Was there any replication of fitness estimation on identical clones so that one has a good estimate of the measurement noise? How is noise accounted for and how does it influence the epistasis modeling? Much is made about the amount of the distribution with positive vs negative coefficients-but sampling noise alone will make coefficients deviate from zero.

3) Both reviewers and the editor were confused by the rationale and choice of the nested statistical framework, as noted in greater detail below by Reviewer 2. For example, It is unclear why for many mutations the idiosyncratic model explains more of the variance than the full model (e.g. Figure 3A). (Note, the fitness-mediated model never fits better than the full model). Also, when dealing with nested models in general, one should ask whether the more complex model fits the data enough better to justify accepting it over simpler model(s). There are clearly details and constraints in the models used here (and likely in the fitting process) that matter, but these are not discussed in any detail, or is the choice of model selection explained adequately.

Reviewer #1 (Recommendations for the authors):

Comments on figures:

Figure 1B: What is the error bar on y-axis? Without an error bar, conclusions cannot be made, particularly due to small fitness changes on y-axis (0.015 to 0.02 fitness changes while the difference between two clones from the same population is up to ~0.02). As acknowledged in Line 124, noise in fitness measurements contribute significantly to the modest differences in the DFE between clones.

Figure 2: Make it clear that each dot in the figure represents a disruption mutation, whose fitness is averaged on the background of two clones from the same timepoint/population. Define "background fitness". The label of x-axis is currently missing. Fitness errors on x-axis are not considered when inferring the significance of the correlation. Furthermore, the examples in Figure 2 are sufficient to conclude that epistasis is not strictly fitness-mediated. Authors could foreshadow the conclusions of the next section.

Figure 3: Line 214-215, walk the reader through the paper. Current writing is difficult to understand. What do the coefficients represent?

3B: Include a positive or negative model of IM. Consider also show models with x-axis as fitness to keep it consistent with 3C. Similarly, show examples with coefficient ~0 in 3C. The current selection of examples in 3B and 3C can lead to misunderstanding of the IM and Full-M.

One thing I don't quite understand is that models with more parameters as in IM or full-M are going to give better explanatory power than those with fewer parameters as in Fitness-M. Are there alternative ways to evaluate these models taking the number of parameters in the model into consideration?

Line-by-Line comments:

Line 81: Introduce the concept of mutational robustness. The immediate relation between mutational robustness and directional evolution experiments where bottleneck/drift likely plays little role in is not obvious. The authors should explain it in the introduction to motivate the rest of the manuscript.

Line 106: Explain why these 91 insertion mutations were chosen.

Line 108-112: Fitness correlation between clones from the same population is not enough to justify the averaging of their fitness as detailed in Public Review.

Line 118: How was p-value calculated? Was error of fitness measurements considered?

Line 159-160: What is the rationale underlying the choice of 0.05 for slope cutoff?

Line 203-210: Briefly describe the models, for instance, what (how many) parameters were used. If possible, include the formula of the model.

Line 235-236: Explain why the remaining epistatic effects are more likely to be negative.

Line 237-238: between the epistasis and environment ("GXGXE" effects).

Line 243: Which figure to look at?

Additional analysis that authors could consider:

Will the conclusion change if more/fewer time points from the evolving populations has been studied (for instance, clones were isolated from longer or shorter evolution)?

How could the magnitude of fitness increase during evolution affect the conclusion (i.e. the maximum fitness increase of clones from YPD is ~0.06 while the maximum fitness increase in SC is ~0.03)?

Reviewer #2 (Recommendations for the authors):

I am enthusiastic about this work. My main criticism is that the modeling is not laid out with enough care and thoroughness, leaving me to question some of the downstream conclusions. I have also offered many specific comments to the authors that are all in the form of comments within the manuscript pdf. I have emailed this annotated pdf to the editors who will upload it on my behalf.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mutational robustness changes during long-term adaptation in laboratory budding yeast populations" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer 1 identified issues with some of the supplemental figures, which must be fixed. However, we all appreciate this extensive revision and look forward to a final version.

Reviewer #1 (Recommendations for the authors):

The authors have sufficiently addressed the previous concerns over the choice of mutants and statistical analysis.

However, multiple supplement figures in the revised manuscript do not have any data points. The technical errors should be fixed before the publication.

I believe once the errors are fixed, the manuscript is ready to be published.
