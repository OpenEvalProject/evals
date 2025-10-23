# Peer review - Round 1

Editors:
- Edward D Janus, University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58567.sa1](https://doi.org/10.7554/eLife.58567.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors performed a Mendelian randomization analysis of statin, PCSK9 inhibitor and ezetimibe use on ischemic heart disease to address a clinically relevant question – could the apparent additional benefits of statins and other similar treatments, over and above lowering lipids, be mediated by favourable effects on testosterone levels? They found a potentially interesting link between statins and testosterone – genetic variants in the gene encoding the HMGcoR receptor that are known to alter LDL-cholesterol levels.

Decision letter after peer review:

Thank you for submitting your article "Pleiotropic effects of statins on ischemic heart disease: a Mendelian Randomization study in the UK Biobank" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matthias Barton as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Timothy Frayling (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Title: Please modify the title to comply with eLife requirements. The title should not exceed 120 characters. Two part titles containing a colon punctuation mark (":") are not allowed.

Summary:

This is a neat study using genetics to ask a clinically relevant question – could the apparent additional benefits of statins and other similar treatments, over and above lowering lipids, be mediated by favourable effects on testosterone levels? The question becomes a little more complicated in that higher levels of testosterone tend to be beneficial for men's metabolic health but adverse for women and so the authors have used UK Biobank data, where it is easy to stratify analyses by sex.

The authors performed a Mendelian randomization (MR) analysis of statin, PCSK9 inhibitor and ezetimibe use on ischemic heart disease (IHD), and if these effects were mediated by testosterone in men or women using univariable and multivariable MR.

They have found a potentially interesting link between statins and testosterone – genetic variants in the gene encoding the HMGcoR receptor that are known to alter LDL-cholesterol levels (And so we know they are very good mimics for the on target effects of statins) and testosterone levels in men. The direction is that the alleles associated with lower LDL-cholesterol and therefore mimic statins also lower testosterone. There were no links for the other genes encoding the other targets of lipid lowering therapy. In addition, they assessed whether the genetic variants corresponding to anti-inflammatory effects of anakinra or tocilizumab use had effects on testosterone and IHD. The topic is very interesting.

Revisions for this paper:

1) The main finding is that, when adjusting for testosterone levels, the protective benefit of statins via the HMGcoR on heart disease attenuates from 0.54 odds ratio to 0.73 in men (when using the MR egger approach. There are wide 95% CIs around these estimates but the results imply that the testosterone effect is similar to the lowering LDL-cholesterol effect, which is extremely counter intuitive given that we know about LDL-cholesterol and heart disease. The reliance on a sensitivity analysis – MR egger – when the main analysis showed evidence of pleiotropy means the results could be very sensitive to slight differences in the parameters used. (SNPs and models).

2) A second concern is that the genetic variants in HMGCoR are associated with BMI and adiposity (see Swerdlow et al. Lancet publication using the HMGcoR SNPs to show an association with diabetes) whereas the others are less so. The authors need to assess the potential for the effect being mediated via BMI/adiposity rather than testosterone. Such a mechanism would be consistent with sex differences because women are at lower risk of heart disease than men for a given BMI. Likewise, many of the testosterone SNPs are highly pleiotropic, with many primarily associated with adiposity and insulin resistance and lipid levels. My concern is that the pleiotropy will lead to false inferences. The authors have partially addressed this with some approaches such as MR-Egger, but these are not infallible. The multivariable MR needs to include the adiposity measures. multivariable MR with adiposity measures, steiger filtering of SNPs that have larger effects on metabolic potentially mediating traits than they do on lipids or testosterone could be alternative approaches to try.

3) It would be relevant to see the results replicated in a two sample MR setting where the IHD cases are not from the same dataset as the testosterone and LDL SNPs. The heart disease GWAS consortia have not analysed separately by sex, which makes this very difficult, but there may be other large studies where this is possible ? If this cannot be done readily it should be discussed and noted as a limitation.

4) All of this means that the conclusion that "statins partially operate on IHD by reducing testosterone in men" is likely overstated.

5) A further major concern is the selection of SNPs in vicinity of the HMGCR, NCP1L1 and PCSK9 genes as instruments for the statin, PCSK9 and ezetimibe use, respectively. For example, a lookup of the instrument included for ezetimibe use (rs10260606) in the publicly available sex-combined GWAS on ezetimibe treatment (http://www.nealelab.is/uk-biobank) resulted in an association p-value of 0.02 being a rather weak instrument. Also in the referenced publication of Ference et al., 2019, that was used as basis for the instrument selection, these SNPs were (to my understanding) selected to assess potential drug targets, and not to reflect medication use.

6) Which statistical model was used to calculate the sex-specific genetic associations with IHD (I assume logistic regression)? Please provide the number of cases and controls per sex-stratum that were finally included in this association analysis also in the main text (not only in the Abstract).

Please provide the p-value level that was applied to declare significance of the results.

7) By conducting a sex-stratified analyses, have the authors considered the impact of collider bias. As if the genetic instruments are associated with sex and the outcome measures are also associated with sex, by stratifying based on a common cause of the exposure and outcome, a distorted/erroneous association may occur.

8) Please give more details about multivariate MR analysis. E.g. did you pool the genetic proxies for statin and testosterone all together and then extracted the associations of all these SNPs with LDL-cholesterol and testosterone and fitted it in one model?

Revisions expected in follow-up work:

1) As the authors aim to investigate sex-specific benefits of statin therapies, why only focus on testosterone. I think you should also look at 17β-oestradiol and SHBG (both available in UKBB), and conduct a multivariate MR to determine which would be the independent causal factor for IHD among the three (e.g. PMID: 32203549) and then forward the independent hormones/proteins in a multivariate model with LDL-cholesterol or apoB (drug targets of lipid lowering drugs) to determine whether these hormones would exert independent roles in contributing to IHD beyond the lipids. If this is the case, then it makes sense to further determine whether the genetic instruments of the drug targets show a sex-specific association with the sex hormones. This issue could be addressed in the Discussion.
