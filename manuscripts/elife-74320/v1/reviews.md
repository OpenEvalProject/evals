# Peer review - Round 1

Editors:
- Mashaal Sohail, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74320.sa0](https://doi.org/10.7554/eLife.74320.sa0)

The manuscript uses genetic effects on BMI to test whether BMI affecxts childhood emotional and behavioural problems: symptoms of depression, anxiety, and attention-deficit and hyperactivity disorder (ADHD) at age 8. By using a within-family design in a large sample of children with genotyped parents in Norway, the study finds that previous estimates of the effect of BMI on childhood emotional and behavioural symptoms may have been overestimated due to confounding with the environment. Larger samples will be needed to determine whether there is a causal effect of BMI on childhood emotional or behavioural problems, and what size it is.


---

# Peer review - Round 1

Editors:
- Mashaal Sohail, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74320.sa1](https://doi.org/10.7554/eLife.74320.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Body mass index and childhood symptoms of depression, anxiety, and attention-deficit hyperactivity disorder: a within-family Mendelian randomization study" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ma-Li Wong as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Daniel Jordan (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The null result reported by the authors is potentially important to the epidemiology of childhood obesity, and would also be an important practical illustration of the power of recently-developed within-family Mendelian Randomization (MR) approaches. The paper is generally well-written and well presented. However, given that these within-family methods are known to have lower power than traditional MR, confidently reporting a null association requires demonstrating that the study design has sufficient power to detect the expected association. The authors have not sufficiently demonstrated this in the current version of the manuscript. This is the major point that needs to be addressed and all three reviewers provide detailed suggestions on this end. There are also further points raised by the reviewers regarding the multivariate regression analysis and doing a formal statistical comparison between MR and within family MR that need to be addressed.

Reviewer #1 (Recommendations for the authors):

1) No direct statistical comparison of 'classic MR' and 'within-family MR' estimates are given. It is hard to know whether there is any statistically sound evidence that the within-family MR estimates are different from the 'classic MR' estimates. It would help to compute the difference between these estimates along with their standard errors. A way to do this would be to derive 'classic MR' estimates from the 'within-family MR' model. The 'classic MR' estimate should be approximately equal to the within-family MR estimate plus the average of the coefficients on the paternal and maternal PGS. (This becomes slightly more complicated when taking assortative mating into account, but this does not seem to be much of an issue here.) Expressing things in this way, the 'classic MR' and 'within-family MR' estimates could both be expressed as linear combinations of the parameters of the within-family MR model, and the standard error of the difference easily computed.

2) It would help to see if there is a non-zero within-family effect of the full childhood and adult BMI PGSs on childhood emotional problems. The authors could use genome-wide summary statistics to construct a PGS using LD-pred or similar tool. While this goes outside of the typical practice of MR, it would be considerably more powerful since the PGS would explain a lot more variance than the PGSs constructed from genome-wide significant SNPs alone. A null result from this analysis would support the authors argument that the classic MR estimate is the result of confounding due to gene-environment correlation.

3) Given the impressive sample size of genotyped trios, the fact that the estimates for within-family MR are still rather imprecise deserves some discussion. Does within-family MR have data requirements that currently cannot be met outside of certain privately held datasets?

Reviewer #2 (Recommendations for the authors):

In addition to the broader comment about the need to demonstrate that the study would be powered to detect an association if one is present, I have only one other substantive scientific comment:

1. The multivariate regression analyses control for a series of parental traits, while the MR analyses do not. Meanwhile, the MR analyses control for genetic ancestry (in the form of PCs), while the regression analyses do not. Could the difference in results between multivariate regression and MR come from the difference in the covariates used, rather than the use of the genetic instrument? Is there a good reason to believe that controlling for ancestry would make no difference in the regression analysis, or that controlling for parental traits would make no difference in the MR analysis?

In addition, I have a few comments about presentation that would make the paper easier to read and follow:

2. I find it confusing the use of the phrase "multivariate regression" to describe the observational epidemiology approach, because many MR methods are arguably a form of regression themselves, just using the genetic instrument as an independent variable rather than the observed trait.

3. The Results section reads as though some pieces of it may have been reordered or moved down to the Methods section. This is most glaring at the very beginning, where the MoBa cohort and the analytic sample are not properly introduced. It would benefit from a readthrough to make sure that everything mentioned in the Results section is sufficiently explained there.

4. Most of the Results paragraphs read like listing off statistics, and it's very difficult to tell what conclusions we are meant to draw from each paragraph. Simply adding a concluding sentence to each paragraph would go a long way towards fixing this. It also might be helpful to see p-values in the Results, rather than just estimates and confidence intervals.

5. The MR methods used are not described in very much detail, and the MR methods papers cited in the introduction are not sufficient for me to reconstruct the analyses performed. At a minimum, the methods used in the primary analysis in figures 2-3 and tables 2-3 should be identified by name like the methods used in the robustness analysis in tables 5-6. Ideally the methods and the differences between them should also be described in more detail in the text, as not all readers will necessarily be familiar with the range of MR methods available.
