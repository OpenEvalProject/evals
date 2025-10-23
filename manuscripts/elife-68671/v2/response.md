# Author response - Round 1

Authors:
- Jiahui Si ([ORCID: 0000-0003-0827-4973](https://orcid.org/0000-0003-0827-4973))
- Songchun Yang
- Dianjianyi Sun
- Canqing Yu ([ORCID: 0000-0002-0019-0014](https://orcid.org/0000-0002-0019-0014))
- Yu Guo
- Yifen Lin
- Iona Y Millwood
- Robin G Walters
- Ling Yang
- Yiping Chen
- Huaidong Du
- Yujie Hua
- Jingchao Liu
- Junshi Chen
- Zhengming Chen
- Wei Chen
- Jun Lv ([ORCID: 0000-0001-7916-3870](https://orcid.org/0000-0001-7916-3870))
- Liming Liang
- Liming Li

## Response text

DOI: [10.7554/eLife.68671.sa2](https://doi.org/10.7554/eLife.68671.sa2)

Suggested recommendations:

1) Starting with the main concern, the lack of replication is of course an issue (as in most EWASs). Could you compare the top hits from the largest previous EWAS of incident CHD, to see if the direction of effect is similar and if the significance is suggestive in your data? That would tell us a little bit more about the comparability.

The previous largest EWAS of incident CHD used a meta-analysis of nine population-based cohorts and 11,461 participants from the United States and European countries1. Based on HumanMethylation450 BeadChip data, methylation levels at 30 CpG sites were identified to be associated with incident CHD, and 30 were associated with incident myocardial infarction (MI). The direction of effect was not quite the same. The effect of 55.2% (CHD-associated) and 51.9% (MI-associated) CpGs showed the same directions in our study and in the previous study. (Author response table 1) showed the β coefficient and p-value of these 60 top hits in our study and in the previous study. The genetic background of the study population might be an important factor for this difference and lack of comparability. Also, as the reviewer mentioned in comment 14, age distribution might explain the difference in results. The mean age of the participants in the present study was 50.1 years, and that of the previous EWAS was 64 years.

2) It would be helpful if some of the methods (and sample description) were provided along with the results, to better follow along the findings (without having to go to the end to read the results first). I found Figure 1 helpful in understanding the results and suggest that it could be presented with the results instead of the methods.

We thank the reviewer for the thoughtful comment. We have revised the manuscript to make it easy to follow (Line 81-88).

3) Some minor clarifications and justifications I would find helpful as a reader:

a. I am not very familiar with the co-methylation network approach. Could you provide a brief overview of the method (preferably along with the results)? As the majority of the findings stem from this method, a justification of its robustness would be helpful.

We used weighted gene co-methylation network analysis2 to identify potential co-methylation network related to CHD. This method can be used to identify clusters of highly correlated co-methylation genes and relate modules to external sample traits to find biologically or clinically significant modules. By calculating correlations among the methylation level of selected CpG sites, we constructed a gene co-methylation network. We then identified gene modules using hierarchical clustering. Next, we related gene modules to CHD outcome.

For computational reasons, we selected the top 20,000 CHD-associated CpGs from single-marker tests. This is about the maximum number of CpGs the WGCNA package can handle on our high-performance computing cluster. A previous study has been restricted 23,000 probe sets to 3600 probes to test the robustness. They found that the module detection results were generally similar2. We also additionally carried out a permutation-based test by shuffling the case-control status and re-selected the top 20,000 CpGs based on the permuted data to construct module and test for association with CHD. We found no inflated false positives due to the selection of top 20,000 CpGs (the most significant module has P>0.032, Figure 2—figure supplement 1).

We have added a brief overview of the co-methylation network approach to the “Result” section (Line 111-114).

b. I agree with what you say in the discussion, that it is not possible to say what direction mediation works, but it would be good with a sentence to explain the reason of the directions selected to study mediation.

We thank the reviewer for the thoughtful comment. DNA methylation is responsive to environmental stimuli and unhealthy lifestyles. This makes DNA methylation a potential biomarker of environmental-related and lifestyle-driven diseases of adulthood, for example, metabolic dysfunction. Unhealthy lifestyles, together with metabolic dysfunction, will further increase the risk of cardiovascular disease. We have added to address this comment (Line 59-65).

c. The sample selection: I assume you aimed to capture severe cases by including only fatal IHD or nonfatal MI counted as CHD? Why were individuals with neoplasms or cerebrovascular disease excluded?

Yes, we included fatal IHD and nonfatal acute MI to capture severe cases. Previous studies suggested that DNA methylation was also a potential biomarker for neoplasms3 or cerebrovascular disease.4,5 Thus, cases with both CHD and cerebrovascular or neoplasms could present a mixture of epigenetic changes. We excluded participants who reported at baseline or have developed neoplasms or cerebrovascular diseases during follow-up to better capture the DNA methylation change associated with incident CHD.

4) A couple of questions regarding the statistical analyses:

a. The analysis description for single CpG sites only says linear regression. Were the analyses not matched for case-control status (i.e. conditional linear regression), and if so why not? That should be the more powerful and robust approach.

We didn’t use conditional linear regression in the analysis. Instead, we followed the recommendation by Leek JT, et al.6 to use simple linear regression when yielding surrogate variable analysis for removing batch effects and other unwanted variations in high-throughput experiments. Previous studies7–10 that used matched case-control design also didn’t perform conditional analysis for the matched factors, although the authors employed different methods to remove batch effects and other unmeasured cofounding (SVA,9 adjustment for principal component,7,10 or adjustment for technical variables directly8).

b. In relation to that, why adjust for the matching variables?

We agree with the reviewer’s consideration for the matched design. Besides the reason we mentioned in the last comment, we noticed that cases were still slightly older than controls despite they were already matched by age (Table 1). Thus, we adjusted for matching factors in the model instead of matching for case-control status in the analysis, same as previous studies.7–10

c. I am slightly worried about overadjustment, especially in the mediation analyses as several of the lifestyle covariates are likely correlated (e.g. physical activity and BMI). Might including these adjustments in the mediation analyses mask an effect? And for the main analyses, did you also test a simpler model with only basic adjustments for comparison?

We re-calculated SVs and adjusted for age, sex, body mass index, smoking status, education level, study area, and all SVs for comparison with the previous largest EWAS of CHD. We called this a basic model and our original model as a full model. Please find the results of these two models in Author response table 2. Adjustment for additional lifestyle covariates did not change the association materially.

Similarly, we also fitted basic models in the mediation analysis by including age, sex, BMI (exclude when BMI was exposure), smoking status (exclude when smoking was exposure), education level, study area, and batch as covariates. The results were largely retained (See Author response table 3).

* We added 15 and 10 mmHg to the measured systolic blood pressure and diastolic blood pressure respectively among participants who reported usage of blood pressure-lowering medications.

‡ Additionally adjusted for treatment of diabetes (yes or no) at baseline.

5) Please check the number of incident cases and controls so the numbers are consistent in the abstract, figure 1, introduction, results etc. The numbers as currently shown vary slightly from 489 to 494.

Baseline DNA methylation was measured for 494 CHD cases and 494 matched controls. In the quality control process, we excluded sex mixed-up samples (n=2); samples with missing rate >0.01 across probes (n=2); samples measured in a distinct study batch (n=2). A total of 491 cases and 491 matched controls were retained for the single marker test. Two samples were further excluded during the network analysis because they were outliers during the sample clustering step, with 491 cases and 489 controls retained. We have revised the manuscript to avoid confusion (Line 85-86, and line 114-116).

6) In the first paragraph of the Results section please expand as the readers won't all look at the methodology section. See also (2) above.

Suggest – 491 cases free of CHD at baseline and developing CHD during follow up and 491 controls free of CHD at baseline and follow up and matched for age, gender, region and timing of blood sampling…

We thank the reviewer for the thoughtful comment. We have revised the manuscript to make it easy to follow (Line 81-88).

7) Table 1. Please show statistical significance p value for prevalent hypertension and diabetes and for lipids

We have added the corresponding p values to Table 1.

8) line 122, can you be specific about items related "healthy lifestyle" and are they known risk factors for CHD?

In our study, we found CHD cases were more likely to be daily smokers, have unhealthy dietary habits, and have higher BMI. We have revised the “Results” section to make it clear (Line 92, 93).

9) line 126, in my opinion, the genomic inflation factor is not helpful here as it is not a good indicator for EWAS. It is because CpGs are more much correlated than SNPs, and the inflation factor is very much dependent on the trait.

We showed the inflation factor for comparison with previous studies.12–16 The QQ plot was also shown in Supplementary file 2B. No evidence for inflation was observed in the QQ plots. We have revised the manuscript to address this comment (Line 98, 246). If the reviewer and editor think it is redundant to present the inflation factor, we would be happy to remove it.

10) Line 130: The difference "-0.003" between cases and controls is very small and hard to detect. Can you also show the SD of the two CpGs, or simply plot their distributions in cases and controls.

We have added a column to Table 2 to show the SD of each CpG. We also showed the SD of the top two hits in the “Result” section (Line 104, 105, and 108).

11) Line 144: Why do you use "probe" not "CpG" in this paragraph?

We thank the reviewer for pointing this out. We performed a gene enrichment analysis of the annotated genes of CpG sites from the CHD-associated module. We have revised to keep consistent and avoid confusion (Line 122, 127).

12) Line 156 change none to no

We have revised “none” to “no” (Line 159).

13) Line 242: Did you compare the maximum follow-up time and age distribution in the other two prospective publications? I believe the choice of different follow-up time can be an important factor as we are not sure how long it takes CpGs to have effects on CHD.

We have summarized the mean age and mean follow-up time of our study and two previous prospective studies as below. Our study included younger participants and followed them up for a shorter time period. We agree with the reviewer that different follow-up time and age distribution might explain the differences between our findings and previous prospective publications. We have revised the “Discussion section” to address this comment (Line 223, 227, Author response table 4).

14) Line 312: "lab staff were blinded" does it also mean the cases and controls were randomized on arrays/batches. This is important as we don't want to lose study power by adjusting batch effect.

The cases and controls were not strictly randomized on arrays. However, the lab staff was really blinded to the case/control status. We agree with the reviewer that adjusting the batch effect may lose power to some extent. We have added it as a limitation to address this comment (Line 246-248, 292, and 293).

15) Line 365: Remove the repeated sentence "A total of 56 SVs were generated."

We thank the reviewer for pointing this out. We have deleted (Line 346).

16) Line 434: How were cellular compositions controlled when you could not use SV here?

In the association analyses of 25 CHD-associated CpGs and cardiovascular risk factors, we also have performed smartSVA for each trait. Adjustment for all SVs instead of batch did not change the association materially (Table 4–Source Data 1-7). To further address this comment, we also additionally adjusted for cellular compositions. The results were generally similar (Author response table 5) . If the reviewer and the editors think it is better to present the results with adjustment for cellular compositions, we would be happy to update all tables in the manuscript.

17) Can you also report the corresponding p-value of the FDR 0.05 threshold?

The corresponding p-value of the FDR = 0.05 threshold was 2.01E-07. We have added to report in the “Result” section (Line 101-102).

18) If you used β-values of DNA methylation in the analysis, please state it.

Yes, we used the β-values of DNA methylation in the analysis. We have added to clarify (Line 334).References

1. Agha Golareh, Mendelson Michael M., Ward-Caviness Cavin K., et al., Blood Leukocyte DNA Methylation Predicts Risk of Future Myocardial Infarction and Coronary Heart Disease. Circulation 2019;140(8):645–57.

2. Langfelder P, Horvath S. WGCNA: an R package for weighted correlation network analysis. BMC Bioinformatics 2008;9(1):559.

3. Koch A, Joosten SC, Feng Z, et al., Analysis of DNA methylation in cancer: location revisited. Nat Rev Clin Oncol 2018;15(7):459–66.

4. Martínez-Iglesias O, Carrera I, Carril JC, Fernández-Novoa L, Cacabelos N, Cacabelos R. DNA Methylation in Neurodegenerative and Cerebrovascular Disorders. Int J Mol Sci 2020;21(6):2220.

5. Li X-G, Ma N, Wang B, et al., The impact of P2Y12 promoter DNA methylation on the recurrence of ischemic events in Chinese patients with ischemic cerebrovascular disease. Sci Rep 2016;6(1):34570.

6. Leek JT, Johnson WE, Parker HS, Jaffe AE, Storey JD. The sva package for removing batch effects and other unwanted variation in high-throughput experiments. Bioinforma Oxf Engl 2012;28(6):882–3.

7. Nakatochi M, Ichihara S, Yamamoto K, et al., Epigenome-wide association of myocardial infarction with DNA methylation sites at loci related to cardiovascular disease. Clin Epigenetics 2017;9:54.

8. Guarrera S, Fiorito G, Onland-Moret NC, et al., Gene-specific DNA methylation profiles and LINE-1 hypomethylation are associated with myocardial infarction risk. Clin Epigenetics 2015;7:133.

9. Li J, Zhu X, Yu K, et al., Genome-Wide Analysis of DNA Methylation and Acute Coronary Syndrome. Circ Res 2017;120(11):1754–67.

10. Chambers JC, Loh M, Lehne B, et al., Epigenome-wide association of DNA methylation markers in peripheral blood from Indian Asians and Europeans with incident type 2 diabetes: a nested case-control study. Lancet Diabetes Endocrinol 2015;3(7):526–34.

11. Wahl S, Drong A, Lehne B, et al., Epigenome-wide association study of body mass index, and the adverse outcomes of adiposity. Nature 2017;541(7635):81–6.

12. Nakatochi M, Ichihara S, Yamamoto K, et al., Epigenome-wide association of myocardial infarction with DNA methylation sites at loci related to cardiovascular disease. Clin Epigenetics 2017;9:54.

13. Guarrera S, Fiorito G, Onland-Moret NC, et al., Gene-specific DNA methylation profiles and LINE-1 hypomethylation are associated with myocardial infarction risk. Clin Epigenetics 2015;7:133.

14. Li J, Zhu X, Yu K, et al., Genome-Wide Analysis of DNA Methylation and Acute Coronary Syndrome. Circ Res 2017;120(11):1754–67.

15. Fernández-Sanlés A, Sayols-Baixeras S, Curcio S, Subirana I, Marrugat J, Elosua R. DNA Methylation and Age-Independent Cardiovascular Risk, an Epigenome-Wide Approach: The REGICOR Study (REgistre GIroní del COR). Arterioscler Thromb Vasc Biol 2018;38(3):645–52.

16. Rask-Andersen M, Martinsson D, Ahsan M, et al., Epigenome-wide association study reveals differential DNA methylation in individuals with a history of myocardial infarction. Hum Mol Genet 2016;25(21):4739–48.
