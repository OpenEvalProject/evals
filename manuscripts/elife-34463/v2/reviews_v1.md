# Peer review - Round 1

Editors:
- Urszula Krzych, Walter Reed Army Institute of Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34463.019](https://doi.org/10.7554/eLife.34463.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Predicting mosquito infection rates and infection intensity from Plasmodium falciparum gametocyte density and sex ratio" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Edward A. Wenger (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work in the present format will not be considered further for publication in eLife. However, the authors are encouraged to make all the suggested revisions and submit the manuscript as a new submission for review.

This study builds on results from previously published eLife paper in that the authors now include new estimates of male gametocytes densities and that provides more detailed prediction of the human-to- mosquito infectiousness. What follows is a summary of the main issues and detailed comments from the reviewers are attached below.

1) The new laboratory methods (quantification of male gametocytes and greater precision for female gametocytes) are described in other publications, and only very briefly here. Please expand on this topic in the discussion.

2) Even with the final model including male gametocyte densities, there is uncertainty. There are substantial between-site differences, and within sites there is unexplained variation with more than a few points lying away from the fitted lines. Please provide explanations.

3) There are a number of issues with the data analysis (correct data, sample size in one site, highly influential points, investigation into the Balonghin data). Please, re-analyze the results and provide a significantly revised interpretation.

4) It is stated that there is a change in the shape of the relationship between gametocyte densities and infectivity by including male gametocyte densities. However, the model may have greater prediction accuracy since two methods to estimate parts of the gametocyte population are used rather than one (the male and female gametocyte densities are added together in the model). In addition, the shape of the relationship does not appear to differ with the current datasets if only female gametocytes are used, compared to male and female together (the best fit for both would be the power function). It may be that there is a difference between the previous data and the current datasets.

Reviewer #1:

The subject of human-to-mosquito infectiousness and its determination by gametocyte density and other factors is a very important one. The authors make an important contribution here that is of general interest.

I have three core concerns with the paper that should be addressed:

1) The paper claims that we can now "reliably predict" mosquito infectiousness by including male and female gametocyte density quantification. However, the significant site-specific differences and other sources of unexplained variance are barely discussed.

- Given the role that seasonality and immunity play on the underlying density distributions (Ouedraogo, 2015; Gerardin, 2015), more information in the Materials and methods section would be appreciated on year and season of sampling (e.g. January 2013 to November 2014 enrollment), enrollment protocol (e.g. microscopy positive gametocytes), and immunity (e.g. incidence per year) beyond "see Dicko, 2016" (not open access).

- You should discuss the implications of the Bobo, Cameroon, and Mali data consisting of microscopy-positive gametocyte carriers, but the Balonghin site only requiring Pfs25 positive.

- You should include this information in Table 1, so the reader isn't forced to discover for herself the reasons for the very different gametocyte density ranges in spite of more similar asexual density ranges.

- Why is infectivity 3.65 times higher in Bobo-Dioulasso? The list of possible differences put forth in the Discussion section, "vector permissiveness, local parasite strains, human [immunity]" is vague and only serves to propagate the general confusion in the community. Without a satisfactory understanding, the claim of "reliably predicting" infectiousness is not very strong.

2) This paper claims to make an important breakthrough in improved precision on female gametocyte density quantification. The Discussion section touches on this, but the implications of this are important and should be expanded upon.

- Presently, there is insufficient detail on the determination of confidence intervals on density quantification. The only hint is the Materials and methods section sentence that they are "based on plate-specific calibration trendlines".

- An example of where I doubt the veracity of the error quantification is in Figure 2B, where there are two samples with very low density, in spite of both being microscopically positive. Note the microscopy detection threshold is almost 2 orders of magnitude higher, or ~10σ if error bars are 95% CI. Were these samples extreme outliers in leukocyte counts and the microscopy threshold is an invalid comparison? Does the female gametocyte density measurement error have significantly wider non-Gaussian tails?

3) A core assertion in this paper is that the addition of male gametocyte densities improves prediction. This could be caused by a combination of the following two factors: (1) mechanistically there is a threshold below which there are not enough male gametocytes present in the blood meal; or (2) the combination of two independent imprecise density measures gives a more accurate estimate of the "true" total gametocyte densities and hence more predictable infectiousness.

The authors are strongly suggesting the first mechanism. However, there are indications that the latter mechanism is also playing an important role - take for example the Mali points that populate the lower-right quadrants of Figure 1A and 2A.

- A version of Figure 2B colored according to male gametocyte ratio would help discern how important each effect might be.

- A direct look at the Balonghin data, which in most plots is hiding in the corner of linear plots, would be instructive as it also includes submicroscopic gametocyte infections.

The source data has Balonghin and Bobo swapped compared to what appears in Table 1. The authors should verify this hasn't introduced any errors into their analysis. (I presume the correct information is in the Table and not in the 'site' column of the source data, because Balonghin is the only site that didn't select samples based on microscopic gametocytes and hence has a much lower density distribution.)

There is a third even lower female gametocyte density point in Mali (in spite of microscopically observed gametocytemia) that is truncated from Figure 2B.

Bobo-Dioulasso has a very high male fraction, very low measured female density, in spite of all points being microscopically detected and infecting large fractions of mosquitoes.

Figure 2B tells one narrative (threshold male gametocyte density below which transmission is less efficient). But the attached colors points by male gametocyte fraction, which I think can be thought of as correcting for imprecise female gametocyte density quantification when comparing the infectiousness vs. density curves.

Reviewer #2:

This paper follows from a previous eLife paper which quantified the relationship between female gametocyte densities and infectiousness to mosquitoes. This paper includes new estimates of male gametocyte densities which, in view of the changing sex-ratio at low female densities, provides a more complete description of the relationship and removes the need for the double hump previously seen and instead uses a simpler saturating relationship. It is not in itself an advance on statistical methods or the laboratory methods (described in another paper) and the sex-ratio was already thought to be important, but it is a step forward. In addition, there is a finding that the proportion of mosquitoes infected plateaus, but number of oocysts continues to rise with increasing gametocyte densities.

It is not clear how the density of male gametocytes or the sex-ratio were included in the model for the relationship between female gametocytes and the proportion of mosquitos infected. The methods merely states "Bayesian Markov Chain Monte Carlo techniques were used to fit the relationship and compare models as described previously". The Results section states "The best fit model shows negative density dependence". This model equation and parameter estimates may be in an Appendix but I could not find it. (The equation for gametocyte density and oocyst density is given in the legend to Figure 3).

In some cases, the fitted lines seem to miss the weight of the data (Figure 2A and C, and Figure 3B). The fitted lines are also dependent on some highly influential points at the righthand side of the graph.

Cameroon has few observations (n=13). Given that there is a skew to low gametocyte density infections, it is not obvious that the sample size is large enough to fit a line meaningfully.

In the Discussion section, the difference in the shape of the relationship in this compared to the previous paper is assumed to be due to more accurate automated methods and the inclusion of male gametocytes. As far as I can gather, different datasets were used here compared to the previous paper, so it could be a factor related to the datasets as well. It would be useful to know how much of the change in the shape of the relationship was due to the male gametocytes, and this could be investigated by using the previous model on the current datasets.

The relationship between gametocytes and infectivity are different between the datasets from Mali, Yaoundé and Burkina Faso. There is a brief mention in the Discussion section, but the reasons are not really known, and it should be stated that there is still considerable uncertainty, even with male and female gametocyte densities.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Predicting the likelihood and intensity of mosquito infection from sex specific Plasmodium falciparum gametocyte density" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers agreed that this study represents an important body of work of a high general interest and a significant advance on the previously published paper. The current submission is much improved over the original version. Nonetheless, there are several issues that collectively, the reviewers thought still need to be addressed.

1) It has been proposed that the authors expand either the Introduction or the Discussion section by describing the previously fitted relationship and explicitly contrasting it with the new relationship. This would help to highlight the differences in the conclusions made in each of the two studies.

2) It would helpful if the authors would include some information explaining the importance of male densities in the context of the evolutionary theory of sex ratios. There is a reasonable body of theory and data (from P. mexicanum and P. chabaudi mostly) that can give ecological and evolutionary context to the results. Specifically, the fact that at low densities of gametocytes, males are limiting is something that has been called "fertility insurance". (there are papers by Gardner et al., 2003 and Ramiro et al, 2011 that explain and explore fertility insurance).

3) There should also be a more coherent integration of the oocyst results with the overall message of the paper. Total gametocytes are indicator to be the most important predictor for oocysts, but for prevalence it is female gametocytes with sex-ratio.

4) For completeness, the relationship between male-only gametocyte densities and infectiousness should be investigated to confirm that it is the weakest.

Motivated by the suspicion that some important data might be discarded by ignoring the microscopy densities, the authors should also indicate the performance of including both PCR and microscopy in the same model. Suggested fits were: gametocyte density by microscopy, geometric mean of male +female by PCR, geometric mean of female PCR + microscopy.

Amongst the specific comments, the following should be addressed.

Please mention and reference Da et al., 2015) that P. falciparum oocyst rise has also been observed.

Introduction, please drop "for the first time" from the text, as it has not: https://www.sciencedirect.com/science/article/pii/S0014489414002896#f0015 (Figure 1A.)

"Gametocyte density estimates by microscopy and qRT-PCR were correlated in Oueleesebougou (r=0.74), Bobo Dioulasso (r=0.27), Balonghin (r=0.56) and Yaoundé (r=0.91)." Correlation is not binary. The wording should reflect the wide range of correlation coefficients.

Subsection “Gametocyte sex ratios in natural infections”: Is the decreasing male-female ratio with increasing density still significant in a hold-one-out sensitivity analysis of the 4 sites? For example, what if Bobo is excluded?

Figure 1A: There are measurements with lower measured densities that do not appear on this figure.

Subsection “Infectivity in relation to gametocyte density”: It looks to my eyes that 200/μL is more like 30% infected.

Discussion section: I appreciate the inclusion of a previous comment in the sentence, "concurrent quantification […] leads to an improved estimation of total gametocyte biomass". However, the following sentence builds a false straw-man argument around the situation where that improved quantification would have to take the form of naively adding together the two imprecise measurements. As a rebuttal, take the following example:

Figure 1—figure supplement 1 in Mali shows that a qRT-PCR density of 50/μL is observed for microscopy measurements of between 20 and 300/μL. The Mali points in Figure 1 show that if the true female density is around 20/μL, then our expected male measurement would be about 2/μL, while if the true female density is 300/μL, the expected male measurement would be about 20/μL.

The point is that if we observe a (female+male) density of (50+2)/μL or (50+20)/μL, we should not expect a model that treats those as 52 or 70/μL total biomass to behave very well under the logarithmic measurement uncertainty. Rather, the previous paragraph would suggest that (50+2) is more consistent with 22/μL while (50+20) is more consistent with 320/μL!

As such, I am convinced the authors have done an important and more predictive measurement, but I disagree with the sentence "this work provides direct evidence of the epidemiological importance of male gametocytes" if that is intended to imply predominantly male-limited mating success (Discussion section).

Figure 1—figure supplement 1: Unless I am mistaken, all measurements are microscopy positive (except in Balonghin), so there should be 3 points missing from panel A (off the bottom?), 3 points from panel B (off the right?), 1 point from panel C (off the bottom?) and about 30 points from panel D, which are submicroscopic, but in the spirit of transparency might be presented also on a broken axis at x=zero.

Figure 1—figure supplement 1: The legend has the name Yaoundé in the wrong place. Move to after (C).

Density, rather than number of female, male parasites, is the technically correct term to be used.

Introduction: It's not clear to that separately quantifying the sexes is needed for estimating total gametocyte density. Is this because each sex may express different levels of the target gene?

Reconciling Figure 1A and 1B may be confusing because Figure 1A suggests the more gametocytes there are (because females make up the bulk of gametocytes), the more males there are. Some comments on why the pattern in Figure1B emerges would help.

A comment in the Discussion section on the relative ease of quantifying females vs total gametocytes or males would be useful information for others to take this forward.

Given their importance to this paper, the sex ratios could be mentioned in the text, currently they are in Figure 1 only.
