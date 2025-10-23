# Peer review - Round 1

Editors:
- Andrew P Morris, University of Liverpool United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57191.sa1](https://doi.org/10.7554/eLife.57191.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors have presented a detailed evaluation of the effects of gene targets of lipid lowering drugs and lipid subfractions on risk of cancer (all-cause and site-specific) using Mendelian randomisation applied to data from the Global Lipid Genetics Consortium and UK Biobank. Importantly, the authors have demonstrated that variants in the HMGCR locus, which are proxies for statin treatment, are associated with all-cause cancer, whilst those in other loci that are proxies for other lipid lowering treatments are not. In contrast, by using genome-wide variation, there was no evidence of a causal effect of lipids on all-cause cancer. The authors conclude that statins may prevent all-cause cancer as well as site-specific cancers through a non-LDL cholesterol mechanism, although they emphasise that the results are not definitive and require further evaluation in clinical trials.

Decision letter after peer review:

Thank you for submitting your article "Predicting the effect of statins on cancer risk using genetic variants: a Mendelian randomization study in UK Biobank" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is a lightly edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Summary:

Carter and colleagues present the results of a Mendelian randomisation study investigating the effects of gene targets of lipid lowering drugs and lipid subfractions on risk of cancer (all-cause and site-specific) using data from the GLGC and UK Biobank. The authors demonstrate the variants in the HMGCR locus (which are proxies for statin treatment) are associated with all-cause cancer – whilst that in other loci that are proxies for other lipid lowering treatments are not. Using genome-wide variation, there was no evidence of a causal effect of lipids on all-cause cancer (but nominal evidence for association with site-specific cancers). The authors conclude that statins may prevent all-cause cancer as well as site-specific cancers through a non-LDL cholesterol mechanism. The authors emphasise that the results are not definitive and require further evaluation in clinical trials.

Overall, the reviewers felt that the manuscript presented a thoughtfully conducted analysis, which was interesting and informative. However, we had some concerns over the interpretation of the results and felt that the manuscript could be strengthened.

Essential revisions:

1) The authors conclude that there was little consistent evidence for associations of LDL cholesterol with site-specific cancers and very weak evidence for an effect on overall cancer risk. This seems to backup the authors inference that the effect of HMGCR on overall cancer is not likely mediated by LDL cholesterol (further supported by results for the other LDL gene targets). However, these results are also compatible with other quite plausible scenarios whereby the null/inconsistent associations reflect highly variable statistical power and heterogeneity across sites.

a) For the most common / most powered cancers from large GWAS consortia (breast cancer, lung cancer and colorectal cancer), MR studies have reported effects of LDL cholesterol. Although the colorectal cancer study cited by the authors reported weak evidence for an effect of LDL cholesterol, a more recent and larger/better powered MR study did report an effect consistent with the authors' result (Cornish et al., 2020).

b) A large MR study of lung cancer risk showed an opposing direction of effect to results for breast and colorectal cancer (Carreras-Torres et al., 2017). Note that the lung cancer study cited by the authors seems to be the wrong one. The results in Figure 2 are also compatible with some directional heterogeneity between cancers. Such heterogeneity would be expected to bias the effect on overall cancer risk towards the null.

c) The HMGCR results and random effects model chosen by the authors imply the presence of horizontal pleiotropy. Did the authors find evidence that pleiotropy was balanced? Unbalanced pleiotropy between SNPs used in the LDL instrument could bias the effect towards the null.

d) As to the LDL gene targets, the null results for PCSK9, LDLR and NPC1L1, especially for NPC1L1, are also compatible with a lack of power for small effect sizes. In addition, bias from measurement error in the SNP-LDL effect could also attenuate results towards the null. The larger effect of HMGCR on cancer risk compared to other targets could reflect the summed effects of LDL and non-LDL related pathways.

e) It should also be pointed out that few published MR studies of cancer seem to mutually adjust for lipid subfractions, which seems to increase the effect sizes in comparison to the univariate analysis, which would reduce power of those studies.

2) The authors definition of all-cause cancer likely includes a substantial proportion of non-melanoma skin cancers, most of which are likely to be relatively benign basal cell carcinomas. The authors perform sensitivity analyses for the HMGCR association, but not for analyses of the lipid subfractions, which are important given the evidence for prostate cancer that the effect of LDL cholesterol is stronger for more aggressive cancers. The definition also includes self-reported cases, and it would be useful to present sensitivity analyses excluding these cases for the site-specific cancers. It was also not clear if individuals diagnosed with multiple cancers contribute to multiple analyses, or it was only the first cancer diagnosis that was counted. Further clarity regarding the control group would be helpful (i.e. was there a common cancer-free control group used for all analyses or could an individual diagnose with one cancer be used as a control for another cancer).

3) How were the variants in each gene region selected? Were these all variants that reached a pre-defined threshold in GLGC, that were subsequently LD pruned? If so, further details are required in the Materials and methods section. Would it be more appropriate to run an approximate conditional analysis using the GLGC summary statistics? Would it be more appropriate to use effect sizes (for both exposure and outcome) that were derived from a joint model (and not univariate models)? The genetic variants have been selected in specific gene regions to be proxies for different lipid-lowering treatments. However, if the selection is based only on association with lipids, can the authors be sure that they are operating through the genes that are the targets of the drugs. Are all the selected variants missense variants or have strong support as eQTLs of the relevant genes? Some further details would be very useful.

4) For the polygenic analyses, are the 184 variants LD pruned? If so, further details are provided in the Materials and methods section. It would be useful to clarify why total cholesterol has been consider by itself in a separate univariable MR, whilst LDL, HDL and TG are considered together in a multivariable MR. If the same variants are used in both sets of analyses, is this optimal (or appropriate)? Random effects models were appropriately used to account for between-variant heterogeneity. Was there indeed significant heterogeneity between variants?

5) The authors write that the association with bowel cancer for LDL/total cholesterol was attenuated in MR-Egger/weighted median analyses, but is this a fair comparison given that these sensitivity analyses did not take into account pleiotropy with other lipid fractions (as in the multivariable MR)? This is particularly important since it feeds into the general narrative about LDL cholesterol not being causally relevant in cancer.

6) Throughout, it is not entirely clear what threshold is being used for significance. It was not clear that associations would meet a multiple testing correction for the number of site-specific cancers.

7) It would be useful to have some discussion of the following issues:

a) The authors argue that from a public health and primary care point of view, overall cancer risk is more important. This is a fair point but is undermined by the possibility of directional heterogeneity amongst cancer sites. The effect on lung cancer (reported by a separate much larger MR study) is especially concerning, given the very poor survival rates for this cancer.

b) The authors state that power should be greatest in the analysis combining all-cause cancer, but this assumes homogenous effects across site-specific cancers, and thus could be lower in the presence of heterogeneity (especially directional heterogeneity).

c) Based on MR/trial results for statins and coronary disease, the authors write that reductions in cancer risk through statin treatment are likely to be modest. A possible problem with this interpretation is that the mechanism of the effect on coronary disease is through LDL cholesterol whilst that with cancer may not be. Does this interpretation require an assumption that the SNP-LDL effect is strongly correlated with the non-LDL/pleiotropic effect? In addition, the effect of statins could be greater if the effect of statins occurs through both LDL and non-LDL mechanisms, which seems possible for some site-specific cancers (e.g. colorectal cancer and breast cancer).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Predicting the effect of statins on cancer risk using genetic variants from a Mendelian randomization study in UK Biobank" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and two reviewers.

We are happy to see the effort you made at amending the paper to accommodate the concerns and suggestions from the reviewers. In this new review round, the reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a new revised submission.

Summary:

The authors have made changes to the manuscript to address concerns raised by the reviewers, which they believe has improved the manuscript. However, concerns remain, particularly with the use of individuals with a given cancer as a control for another cancer.

Essential revisions:

The authors write that an individual with cancer could serve as a control for another cancer. "Hence an individual with one cancer could be a control for analyses of another cancer." This seems incongruent with the authors' hypothesis that cholesterol could be a common cause for different cancers. Wouldn't this be expected to reduce power for site-specific cancers? For example, if you include a colorectal cancer case as a control for an analysis of breast cancer, won't this attenuate the effect on breast cancer to the null (assuming LDL causes both cancers, which seems to be supported by previous MR studies in BCAC, CORECT/GECCO)?
