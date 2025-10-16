# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61548.sa1](https://doi.org/10.7554/eLife.61548.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A major current challenge in human genetics is the effect that population structure can have on results from genome-wide association studies and the applications thereof, including with polygenic scores for trait variation or disease risks. Uncorrected biases may be subtle at the level of individual genotype-phenotype associations but can still have meaningfully large effects on an additive basis for a complex trait. The present study from Zaidi and Mathieson meaningfully advances the field by both demonstrating that recent population structure cannot be corrected effectively via a common approach and presenting potential solutions.

Decision letter after peer review:

Thank you for submitting your article "Demographic history impacts stratification in polygenic scores" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by George Perry as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alicia R Martin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper provides a strong and clear advance on the issue of population stratification in human genome-wide association studies and the downstream biases that arise from it. The authors reaffirm that while such biases can be subtle regarding individual SNP effects, polygenic scores nonetheless accumulate large errors genome-wide. Through simulations of various realistic demographic models, they show that no single approach they tested completely corrects for population structure, indicating that complex demographic considerations are required to elucidate the role of stratification on polygenic scores. Principal components calculated from rare variants appear to better capture recent population structure than common variants, such that a multivariate approach with multiple sets of PCs may be superior.

Essential revisions:

1) Demographic parameters: There is immense interest in clinical applications of PRS, but as this and previous work has shown, FST between discovery and target cohorts is only the first indicator of issues in translation. In the Discussion, the authors should consider proposing more comprehensive frameworks for assessing stratification beyond FST. For example, is there a standard approach that the field could use to quantify stratification in GWAS summary statistics (e.g. in comparison to a reference panel)? Since FST itself is insufficient, what demographic parameters or metrics in the discovery and target cohorts could be reported to facilitate translation?

2) Effects of imputation: The results reported here indicate that GWAS summary statistics contain less population stratification when PCs are calculated using rare variants. This solution seems great in theory. In practice, concerns with this approach in GWAS studies may arise because of varying imputation accuracy as a function of ancestry and allele frequency, with especially low imputation accuracy among rarer variants and in underrepresented ancestries. It would be very helpful to use the simulation framework and data here to determine the extent to imputation errors impact PRS accuracy in the UK Biobank when including PCs from more accurately imputed common versus less accurately imputed rare variants.

(3a) One proposal in the Discussion is that considering two sets of PCs in a standard linear regression or linear mixed model may reduce residual stratification. How collinear are PCs computed from common and rare variants, e.g. in Figures 1, 2, 4, 6, Figure 1—figure supplement 2, Figure 2—figure supplement 1, Figure 4—figure supplements 1 and 2, Figure 5—figure supplement 1 and Figure 3—figure supplement 1, particularly as a function of number of SNPs used in their calculation? Further analysis would be helpful to guide whether and the extent to which there is a tradeoff between stratification and power differences from collinearity and # degrees of freedom. (This may have consequences for study design, e.g. GWAS arrays vs. exome or genome sequencing).

(3b) Is it actually important that the PCs be obtained by independent eigendecomposition/SVD on variants from different frequency bins? Alternatively, would it be sufficient to just make sure to include variants of different frequency classes in the genotype matrix, and then get a single set of PCs from the combined set? E.g. if you combine the common and rare variants into a single genotype matrix and then include the top 200 PCs from that matrix, does this approach perform equally as well as the one where you independently get the top 100 PCs each from common and rare? Some care would need to be taken to make sure this comparison was done fairly, as you'd want to make sure that the common and the rare variants explained an equal amount of variance in the top 200 PCs, mimicking the situation where you've provided an equal number of rare and common PCs. Given that PCA is a linear procedure, the answer to this question seems like it would depend on whether the decision to split the genotype matrix by frequency bin before doing the PCA(s) represents some important non-linearity in your model of population structure. If this is indeed the case, it seems like breaking out of the linear constraint of PCA would be a more general path forward, and that would seem worth noting. If the combined approach can indeed match the approach of performing PCA separately, then it suggests that it's just a matter of making sure certain patterns are represented in some way in the underlying genotype matrix, and that, also, would seem worth noting.

4) Previous work, e.g. by Kerminen et al., 2019, has shown reduced overprediction across geographical regions when using mixed models. As this manuscript further considers PCs and LMMs as a function of allele frequency, more guidance regarding which PCs and GRM(s) should be included based on rare and/or common variants to minimize stratification would be helpful.

5) Fine-mapping: How much does fine-mapping have the potential to help? E.g. if we use state-of-the-art fine-mapping methods like SuSiE that produce posterior probabilities, can we diminish PRS stratification from lead SNP effects, and to what extent (maybe dependent on demographic history and sample size)?

6) Siblings: We agree with the authors' statement that ascertaining SNPs in the usual way and re-estimating effect estimates in siblings is not immune to stratification (Figure 5, subsection “Sibling-based tests are robust to environmental stratification”). In addition to stratification, there is also most likely also a tradeoff in accuracy. With these different strategies and tradeoffs in mind, in addition to correlation between polygenic scores and latitude, it would also be helpful to know how correlation between polygenic scores and phenotype vary with different SNP selection and effect size estimation strategies (e.g. in an additional panel C).

7) To help round out the manuscript, we would like the authors to add one or more examples based on their simulation results to illustrate how strategies they propose for dealing with uncorrected, residual population structure would actually work.
