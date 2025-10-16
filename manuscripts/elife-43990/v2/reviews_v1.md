# Peer review - Round 1

Editors:
- M Dawn Teare, Newcastle University United Kingdom

Reviewers:
- Stephen Burgess, University of Cambridge United Kingdom

## Review text

DOI: [10.7554/eLife.43990.013](https://doi.org/10.7554/eLife.43990.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The effects of intelligence and education on health, a bidirectional two-sample Mendelian randomization analysis" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eduardo Franco as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Stephen Burgess (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper consists of a series of Mendelian Randomization (MR) studies related to intelligence, education, and later-life outcomes attempting to disentangle the complicated relationship between them. The analyses included in this study appear to be comprehensive, using many of the latest tools that have been developed. The choice of methods is generally appropriate, and the presentation of results is clear and measured. This work is interesting, and a great example of the potential of the multivariable MR approach to disentangle the effects of related risk factors. However, we have major concerns regarding the extensive use of causal language as there is some evidence that the key assumptions of MR may not hold in this application.

Essential revisions:

1) It is appreciated that the authors include the assumptions required for univariate and multivariate MR and the discussion of the limitations. However, the discussion of these assumptions and limitations need to be more complete and more central in the paper. MR analyses live or die to the degree that they satisfy the assumptions of the method. When this entire discussion is added to a section at the very end of the paper, it makes it very difficult as a reader to assess the credibility of the evidence being presented. Some further formal evaluation of whether assumptions hold could be presented. If the genetic risk score is as associated with confounders (notably socio-economic) as education itself, then the benefit of MR is less clear. (Note some association with confounders is expected, as education itself will influence socio-economic variables somewhat.) Perhaps a comparison with parental socio-economics would be helpful here – genetic variants should be less associated with parental socio-economics (if the MR assumptions are satisfied).

2) Related to the above point, the causal language throughout the paper is too strong. For example, in the limitations section, the authors acknowledge that dynastic effects and assortative mating could be driving "some of the effects [they] report." Indeed, the data is consistent with a model where the nurturing environment affects health but where education and intelligence have no effect at all. Despite this, there is unqualified causal language in the title, Abstract and throughout the manuscript. This should all be greatly softened.

3) Intelligence and education are difficult to define and measure – particularly intelligence. This is an intrinsic concern of any research involving intelligence, but it is particularly relevant for research that makes causal inferences and public policy recommendations (as per the final line of the Abstract). What would it look like to increase intelligence? What aspect of intelligence would we increase? There is also a methodological concern here – while the multivariable Mendelian randomization analyses are important for understanding questions of aetiology, the univariable Mendelian randomization analyses are more important for understanding the impact of public health interventions. As most interventions to increase intelligence would do so via education. Hence the total effects of intervention on intelligence and education should be as important as the direct effects. We would therefore encourage a co-equal presentation of these results.

4) The reviewers raised concerns about the use of multivariable Mendelian randomization for two variables that are so highly correlated. This is alleviated by the reasonably healthy Sanderson-Windmeijer F statistics, but particularly when the direct effects are in opposite directions (as for several examples in Figure 4 in Supplementary file 1), we worry slightly that this is just an artifact of including two highly correlated predictors in a regression model – due to chance variation, one will end up with a positive estimate and the other with a negative estimate. Having said that, it is reassuring that this pattern doesn't hold for all the outcomes. What is the correlation between genetic associations with education and genetic associations with intelligence?

5) Measurement error – while you are correct that standard univariable Mendelian randomization is not particularly influenced by measurement error, the same is not necessarily true for multivariable Mendelian randomization. As this is based on multivariable regression, it is possible for measurement error in genetic association estimates to lead to bias in any direction. It may be the case that the expected bias is low, but we are not aware of any theoretical or simulation work on this topic.

6) While we understand removing participants in the interim release for the analysis of genetic associations with intelligence/education, these participants could be included in analyses for other outcomes. We understand if you prefer to keep a consistent sample definition for comparability, but you may get improvement in power by using a wider sample for the gene-outcome associations. As a side point, in Figure 1 in Supplementary file 1, could you make clear where the two samples come from in the two-sample analyses? Currently there is only one box, but logically we'd expect there should be two.

7) It was difficult to identify the exact procedures followed in the paper at times. This was especially the case when they describe what data are used and which summary statistics are used. For example, the authors state, "The characteristics of 124,661 participants of UK Biobank who met our quality control and inclusion criteria for our primary analysis are described in Table 1." What is considered the "primary analysis" of this paper? The bidirectional EA vs. intelligence analysis, the univariate analysis, or the bivariate analyses? Or perhaps all three of them? Given that the authors also describe using published GWAS results, it is not clear how these UK Biobank participants are used. Just for the outcome phenotypes? Additionally, the descriptions of the Sanderson-Windmeijer test and the clumping procedure is ambiguous and hard to follow.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Intelligence, education and health, evidence from bidirectional two-sample Mendelian randomization" for further consideration at eLife. Your revised article has been favorably evaluated by Eduardo Franco as the Senior Editor, M Dawn Teare as the Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed in a new revision round before acceptance, as outlined below:

The evidence that the IV assumptions may have been violated is rather underplayed and this needs to be more firmly acknowledged and stated within this manuscript either in the Discussion or in the limitations. One reviewer also highlights that measurement error can have an impact on Multivariable MR.

Reviewer #1:

I'm happy with how the authors have edited the paper. While the paper relies on assumptions, these are clearly laid out and considerable effort has been made to assess the assumptions.

Reviewer #2:

I appreciate the authors' substantial revisions in response to comments of the reviewers. The specific steps that were taken by the researchers is much more clear. I also appreciate the new analyses to test the assumptions of the method. I still have two substantive concerns, however.

1) While the authors describe the limitations of the methods they employ, they give a much more rosy interpretation of their sensitivity results than I think is merited. The two well-powered pieces of evidence the authors present related to the validity of the MR assumptions are the published studies on indirect effects of parents and the evidence that the polygenic scores are strongly associated with covariates related to childhood environment. Despite this, the authors make conclusions like "the impact of these associations on the final results may be small" and that "Assumption 2 [no confounders] is plausible because of the random inheritance of alleles at conception". My conclusion upon reading the analyses is that the assumptions of MR probably don't hold in this case and that the bias is potentially substantial. Do the authors disagree? If so, the authors should provide evidence for why they think this is the case or what evidence they have that the bias induced by violations of this assumptions is negligible. Otherwise, the authors should use more conservative language throughout about their sensitivity analyses and should minimally include a line in the Abstract about how they find evidence that the MR assumptions may not hold in this case.

2) I was not able to follow what was being done exactly based on the description of the bias component plots in the last paragraph of the subsection “Sensitivity analysis”, subsection “Investigating bias” of the Materials and methods, and the figure legends for Figures 6 and 7 in Supplementary file 1. A description of the procedure for producing this plot should be clarified.
