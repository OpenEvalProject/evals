# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25008.033](https://doi.org/10.7554/eLife.25008.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Modelling the drivers of the spread of Plasmodium falciparum hrp2 gene deletions in sub-Saharan Africa" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Ben Cooper (Reviewer #1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Prabhat Jha as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rachel Daniels (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors adapt a previously published mathematical model of Plasmodium falciparum transmission to consider the impact of rapid diagnostic tests (RDTs) on the prevalence of pfhrp2 gene deleted mutants. Using data from the Democratic Republic of Congo they estimate the prevalence of pfhrp2-deleted mutants prior to RDT introduction and identify the effects of malaria prevalence and frequency of people seeking treatment on the rate of spread on pfhrp2-deleted mutants. Using parasite prevalence and treatment coverage estimates the model is used to identify areas of Sub-Saharan Africa of concern that should be prioritized for surveillance.

Essential revisions:

Broadly, the reviewers agreed this paper addressed an important subject, used an appropriate modelling framework and was well-presented. However the methods were described with insufficient detail to enable a full understanding of what was done. It was also felt that the authors needed to do more to demonstrate that their conclusion about geographical areas of high concern are robust to alternative assumptions. We expand on these concerns below.

1) The Materials and methods section does not precisely define the actual model used. Instead an analogous deterministic model is described. This is problematic as there is not a single corresponding stochastic model. The authors need make it much clearer what they actually did by specifying precisely the stochastic model they actually used (there are no space limitations so this should be possible). Some aspects of the model also don't appear to be directly analogous to the defined d.e. model. For example, the equations in subsection “P. falciparum transmission model” do not allow for superinfection, but the text states that the actual model does, but there is no information on how this is done, what multiplicity of infection is allowed for etc. Another example: in the Materials and methods section it is stated that "each u term represents the time during which immunity cannot be boosted further after a previous boost ", which is straightforward to define for a stochastic model (assuming the authors mean a constant u – do they?), but doesn't have an obvious correspondence with the given PDEs. It is also not made clear in the Materials and methods section what the relationship is between this model and the models of Griffin et al., 2014,2015,2016. This should be clarified.

Additionally, assumptions made for the admin 1 predictions are not clear. For geographic predictions was epsilon 1 at all times when no RDTs are used? What about slow-uptake of coverage of RDT use (or was it assumed that once RDTs are introduced there is immediate 100% coverage)? These assumptions have implications on the selection and on the conclusions about areas of concern for surveillance.

2) It would be a great help to non-modellers and improve readability to outline the key assumptions of the model (without equations) in the Introduction.

3) In the supplement, it would add transparency if some level of validation was provided that the model produces output that matches the prev/incidence by country/admin 1 as previously used by this group

4) It appears that only one clinical case can occur per infection. Does this mean only fully curative treatment is assumed (no sub-curative due to patient non-adherence, low dosing, lack of system compliance/resistance/fake drugs)? This should be clarified and the implications of this considered in the Discussion.

5) In the Results section and Discussion – "using the baseline frequency estimate of 6% prior to RDT" How do areas of concern change if this assumption was relaxed? The caveats around assuming a starting prevalence of 6% everywhere have been addressed in the Discussion, but in a somewhat simplified manner "Fourthly, extrapolating the starting frequency of pfhrp2-deletion strains from the DRC across the rest of SSA is a clear oversimplification; however, in the absence of similar datasets, we feel it provides a reasonable first estimate". However, the work would be further strengthened if the authors undertook a simplified analysis to see if/how priority geographic areas for surveillance change if a lower or higher starting frequency of pfhrp2 was assumed. Along the lines of the other investigations concerning assumptions around epsilon etc. This seems particularly important if the authors agree with their own statement "Thus our results should be interpreted not as predictions of the absolute levels of the gene deletion, but rather indicative of geographical areas in which surveillance should be focused."

6) Discussion section: Concerning assumptions of non-treated RDT negative cases and coverage of RDT usage -"However, the ratio of testing via microscopy versus RDT is likely to have decreased over this period, and hence our estimate of RDT use (which our model assumes is 100% from introduction) is likely too high". It is not clear that this, and adherence/lack of adherence to RDT treatment guidelines, would not have significant impact on the main conclusions. There is a strong argument for additional sensitivity analysis here.

7) Figure 4 and Discussion: the classification of areas into high, moderate, slight and marginal concern is based on the frequency of pfhrp2-deleted mutants. But how does this frequency correlate with prevalence and ability to detect? From the results, it appears that low prevalence areas with high treatment rates are likely to increase in pfhrp2-deleted mutant frequency first, but these areas may not correspond to areas that are easy to detect/sample from nor, more importantly, areas where clinical morbidity will increase as infections go untreated as they result in negative RDTs. Can the authors comment on this and address the impact on Pf prevalence in relative terms considering the dynamic feedback with treatment and transmission?

8) It appears that the selection pressure for deletion mutants arises solely as a result of differential treatment rates of patients who are clinically diseased as a result of malaria. However, in high prevalence areas, many of those treated for malaria may be parasite positive, have a clinical diagnosis of malaria, but have a non-malarial cause of fever. In some settings these non-malarial causes could account for the vast majority of patients treated for malaria (for example Crump JA, Morrissey AB, Nicholson WL, Massung RF, Stoddard RA, Galloway RL, et al. (2013) Etiology of Severe Non-malaria Febrile Illness in Northern Tanzania: A Prospective Cohort Study. PLoS Negl Trop Dis 7(7): e2324. doi:10.1371/journal.pntd.0002324). Intuitively these effects could substantially change the selective pressures acting on the deletion mutants. If this process has been ignored (which is the reviewers' understanding) at the very least there should be a good argument explaining why it can be neglected. Additional analysis allowing for the fact that many patients treated for malaria may have other causes of fever would be the preferred option.

9) A related question is what happens to the patients who do have clinical disease resulting from malaria, but who don't get treated because they are infected only with the pfhrp2 deletion mutants (and don't have cross-reactivity from pfhrp3). It appears from the model description these patients will never get treated for the current infection. If this is correct, how clinically realistic is this? In practice wouldn't a patient who continues to show clinical signs of malaria get treated for malaria even in the absence of a positive test result?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Modelling the drivers of the spread of Plasmodium falciparum hrp2 gene deletions in sub-Saharan Africa" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha (Senior editor) and a Reviewing editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have done a very good job in responding to the reviewers' comments, and the changes have greatly strengthened this work and have addressed the concerns raised.

The only outstanding issues for me are what I presume are typos in one or two equations (and in one case, a clarification is needed). These equations were not given in the original submission, but they are needed for a full description of the work.

Substantive concerns:

1) Something is wrong with the second equation in the Materials and methods section. First, this gives a biting rate that goes down with age, not up (contradicting the text which follows the third equation). Secondly it allows for negative biting rates (and will give them at default parameter values). Minus sign missing?

2) For the hazards for the first three transitions in subsection “Immunity and detection functions it wasn't clear to me why the period u_. (corresponding to the time when immunity cannot be further boosted after a previous boost) was accounted for by scaling the hazard rather than allowing it change with time. Wouldn't it be straightforward to specify a hazard of h_i if no previous boost in the previous u_B days for person i (or u_C or u_D) and 0 otherwise?

3) Two things that seem odd in the Kolmogorov equations in subsection “Stochastic Model Equations”: i) I can't make sense of the first term on the rhs (P_i(j,k,l,m,a,t). Is there a -mu missing here? ii) on the fifth line of these equations shouldn't the $(1-f_t) epsilon$ term be $(1-f_t epsilon)$ ?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Modelling the drivers of the spread of Plasmodium falciparum hrp2 gene deletions in sub-Saharan Africa" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha (Senior editor) and one reviewer, who is also a member of our Board of Reviewing Editors.

The manuscript has been improved and addressed the previous concerns but there are some remaining issues that need to be addressed before acceptance, as outlined below in the review.

Reviewer 1:

This revision has introduced a further change in the way the model is described. This is a good thing if it aids reproducibility and transparency. The one problem is that the new formulation is very difficult to make sense of, and the logic of the revised equation is not clear.

Some text should be added below these equations to explain in a less technical way what these terms on the r.h.s. represent. It may well be that this equation as it stands is correct. Or there could be one or more mistakes which need to be fixed.

Apart from this issue, I don't have any further concerns with the paper.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Modelling the drivers of the spread of Plasmodium falciparum hrp2 gene deletions in sub-Saharan Africa" for further consideration at eLife. Your revised article has been evaluated by Prabhat Jha (Senior editor) and a Reviewing editor.

Unfortunately, the revisions have not sufficiently addressed the concerns raised in the previous review and the issues raised there still need to be addressed before acceptance. Given the lengthy back and forth on this review, we must insist that this will be the last opportunity we will allow for a successful response to the concerns expressed by the Reviewing editor.

In particular, a precise, intelligible description of the model is an essential requirement. While the new mathematical description of the model is precise, it is not fully intelligible. This may be because there are still errors in the description, or it may because sufficient motivation for equations has not been provided. To take just one example, on the sixth line of the equations in subsection “Stochastic Model Equations” there is a term that seems to correspond to bites from infectious mosquitos which do not result in infection (the bites occur at rate h_i, the EIR, and (1-b_i) is the probability of no infection given such a bite). Suppose a susceptible gets bitten, so j is S and t_k< t < t_k + u_b), so the function theta evaluates to 1. So in this case the operator b evaluates to the identify function, and plugging this back into the equation at the top of the page we learn that the rate P_i(S,…) is changing w.r.t time (keeping age constant) for susceptible hosts is (1-b_i) * h_i (..) * P_i(S,…).

Why should this be the case? Why are these non-infecting bites leading to increases in the susceptible population? This is not clear and is merely the first place where the equations in this subsection cannot be readily understood.

We propose two possible ways forward:

i) a detailed explanation of the equations is added, explaining how they represent the model going into a similar level of detail as the text above.

ii) the simulation model is described in pseudocode rather than in equations. We appreciate that R code is already provided on Github. However, R will not be universally readable (either by other researchers now or in the future who are not familiar with R [and the R language is itself evolving so R code that is valid now may not run in the future]). If the model is described in pseudocode that should allow the twin aims of precision and intelligibility.

Option ii) might be easier, and of course (since space is not an issue) both i) and ii) could be done together.
