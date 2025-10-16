# Peer review - Round 1

Editors:
- Evangelos J Giamarellos-Bourboulis, https://ror.org/04gnjpq42 National and Kapodistrian University of Athens, Medical School Greece

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79720.sa0](https://doi.org/10.7554/eLife.79720.sa0)

Using publicly available genetic data, Li and colleagues tested the association and inferred the causality of genetic variants predicted to alter the levels of testosterone, estrogen, SHBG, or IGF-1, against susceptibility, severity and outcome of SARS-Cov2 infection. The main strength of the study is the large cohort which adds to the robustness of the data.


---

# Peer review - Round 1

Editors:
- Evangelos J Giamarellos-Bourboulis, https://ror.org/04gnjpq42 National and Kapodistrian University of Athens, Medical School Greece

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79720.sa1](https://doi.org/10.7554/eLife.79720.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Genetically predicted high IGF-1 levels showed protective effects on COVID-19 susceptibility and hospitalization: A Mendelian Randomisation study with data from 60 studies across 25 countries" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Evangelos J Giamarellos-Bourboulis as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jos van der Meer as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Recommendations for the authors:

– The main limitation of the study is the lack of any real-world validation cohort where IGF-1 is measured.

– Another limitation is the lack of any transcriptomic data to support the findings. Can the authors describe any eQTLs to recompensate for this?

– The authors leveraged previous reports of genetic variants in association with testosterone, estrogen, SHBG, and IGF-1 levels, outside of COVID-19 cohorts. Testosterone, estrogen, SHBG, and IGF-1 levels were not measured specifically in the context of the COVID-19 Host Genetics Initiative. Secondly, no attempts were made to further validate, either experimentally or in other external cohorts, their findings related to IGF-1 levels. Thirdly, the statistics is seemingly lacking appropriate control of the false discovery rate. Although the study is a targeted meta-analysis, by examining 657 different markers one is bound to identify an association by chance. In fact, applying a Bonferroni correction to the reported p-values for IGF-1 related SNPs yields non-significant probabilities. Fourth, the methods section lacks important details, for example handling of the known "winner's curse" bias in inverse variance weighting mendelian randomization, thereby decreasing the potential for reproducibility by other groups. Lastly, the methods employed did not adequately address potential data confounders, for example treatment of patients with dexamethasone or the influence of BMI (inferred in other studies as a causal risk factor) on model estimates. Against this backdrop, the interpretation of the findings by Li and colleagues is complicated and conclusions related to genetic proxies of IGF-1 levels are unreliable.

– Based on the cited references (13 and 14), selection of SNPs in the meta-analysis is subject to a bias towards non-infectious conditions. It is important to consider that levels of testosterone, estradiol, SHBG, and IGF-1 could be substantially altered during the course of the infection, either in the acute phase or later stages. What are the levels of testosterone, estradiol, SHBG and IGF-1 in the context of viral infections, as well as crucially in COVID-19? How do those levels influence the association of the selected SNPs?

– Throughout the results, particularly in Figure 2, confidence intervals are large and indicates a potential complication due to unaddressed confounders or subgroups within the cohort. How many of the COVID-19 patients were administered corticosteroid therapy? How many were administered tocilizumab? How does treatment effect the model estimates? The authors should provide more characteristics of the COVID-19 patients with a more extensive investigation on the potential confounders and treatment effects on MR estimates. How does BMI influence model estimates and results?

– Inverse-variance weighted two-sample Mendelian randomization is indeed the most extensively used method utilizing GWAS summary stats to infer on causality of the exposure (ie. SNP variant) and outcome variables. The approach suffers from various biases that were seemingly not handled in the study herein described, for example, the winner's curse and potential pleiotropy. The authors should provide a more objective assessment of potential biases and address them accordingly.

– Notwithstanding the large sample size of the discovery cohort obtained from the host genetics in COVID-19 initiative, it is imperative to expand on the findings by ascertaining the robustness of the IFG-1 related SNPs. Do the IGF-1-related SNPs influence IGF-1 levels in the context of a viral infection? Preferably of course in COVID-19. Also, do the SNPs constitute eQTLs for IGF-1 expression in primary organs, particularly lungs, liver, and kidneys?

– The methods section needs to be expanded substantially by the addition of important details. For example, how was LD clumping performed? Using PLINK? Why was an r2 cutoff of < 0.01 used? Why not r2 < 0.001?

– The sentence on page 5 line 38 reading "postmenopausal women (22) and men(13, 23)." needs correction as it implies men were also postmenopausal.

– Page 7, line 196, the statement that reads "The cytokine storm related respiratory distress syndrome…" should be revised, avoiding the sensationalistic "cytokine storm" description of what has been reported elsewhere as merely a cytokine breeze at best.

– The Discussion on cytokine storm is arbitrary and should be omitted. The authors do not provide any evidence on the association of IGF-1 with the cytokine storm.

– This is another trial finding no association of sex hormones to COVID-19. This has to be discussed more extensively in the discussion; now discussion is more focused on IGF (the positive finding) but negative results should be put into context. Please refer also to PMID: 35577073, PMID: 35470422, PMID: 35602518

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Genetically predicted high IGF-1 levels showed protective effects on COVID-19 susceptibility and hospitalization: A Mendelian Randomisation study with data from 60 studies across 25 countries" for further consideration by eLife. Your revised article has been evaluated by Jos van der Meer (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

– The study hinges solely on MR analysis of selected SNPs used as proxies of testosterone, estradiol, SHBG, and IGF-1 levels. None of the markers were directly measured, and no information on their levels in the context of infections or COVID-19 was given. The authors argue at length that measuring the markers in the specific cohort is of limited value because their genetic causality modelling approach supersedes the need for such measurements. While MR models have indeed emerged as interesting tools to infer causality, it is also important to provide a potential mechanism linking genetic variants to the phenotype. Without direct measurements of the said markers minimize the potential to provide readers with a possible mechanism bridging genetic variant and phenotype.

– The number of tests performed in the study is equivalent to the number of SNPs that were investigated, that is, 657. Hence, the multiple-testing correction must take into account 657 tests. The authors are wrong in adjusting their probabilities just for the 4 markers, which is more attuned to p-value hacking. Therefore, my initial comments on the lack of significant findings after considering multiple-test corrections remain a concern. Hence, the conclusions pertaining to IGF-1 variants do not reflect on the author's findings. Based on this result, I suggest being more objective by stating that none of the genetic variants can be deemed as a causal variant.
