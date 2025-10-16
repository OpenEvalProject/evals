# Author response - Round 1

Authors:
- Fei Chen ([ORCID: 0000-0002-1679-9932](https://orcid.org/0000-0002-1679-9932))
- Burcu F Darst
- Ravi K Madduri ([ORCID: 0000-0003-2130-2887](https://orcid.org/0000-0003-2130-2887))
- Alex A Rodriguez
- Xin Sheng
- Christopher T Rentsch
- Caroline Andrews
- Wei Tang
- Adam S Kibel
- Anna Plym
- Kelly Cho
- Mohamed Jalloh
- Serigne Magueye Gueye
- Lamine Niang
- Olufemi J Ogunbiyi ([ORCID: 0000-0002-8748-2879](https://orcid.org/0000-0002-8748-2879))
- Olufemi Popoola
- Akindele O Adebiyi
- Oseremen I Aisuodionoe-Shadrach
- Hafees O Ajibola
- Mustapha A Jamda
- Olabode P Oluwole
- Maxwell Nwegbu
- Ben Adusei
- Sunny Mante
- Afua Darkwa-Abrahams ([ORCID: 0000-0003-0649-3996](https://orcid.org/0000-0003-0649-3996))
- James E Mensah
- Andrew Anthony Adjei
- Halimatou Diop
- Joseph Lachance ([ORCID: 0000-0002-4650-3741](https://orcid.org/0000-0002-4650-3741))
- Timothy R Rebbeck
- Stefan Ambs
- J Michael Gaziano
- Amy C Justice
- David V Conti
- Christopher A Haiman ([ORCID: 0000-0002-0097-9971](https://orcid.org/0000-0002-0097-9971))

## Response text

DOI: [10.7554/eLife.78304.sa2](https://doi.org/10.7554/eLife.78304.sa2)

Essential revisions:

The reviewers have agreed that the work presented here is an important contribution to the literature on polygenic risk scores and their applicability to cohorts of different ancestries. They also have agreed that the manuscript is clear, strong, and informative, and have only a small number of suggestions for improving clarity.

1. A reviewer mentions that added context for PRS is needed in the introduction. At the moment, the paper seems written for cancer epidemiology or genetic epidemiology audience, but it would be helpful if it were clear for a broader life sciences audience, who may not be completely aware of the utility of a PRS or may have preconceived notions about PRS research. Could the authors please add explanations and/or figures in the Introduction for:

– Explaining what a PRS is,

– what a PRS estimates,

– how the specific PRS was trained,

– the utility of a PRS in a clinical setting.

In response to this comment, in the Introduction section we include more background information regarding the development and validation of the multi-ancestry PRS for prostate cancer and what the PRS estimates (page 5). Further discussion on the clinical utility of this multi-ancestry PRS in identifying individuals at high risk of developing prostate cancer is included in the last paragraph of the Discussion section (page 9).

2. Can the authors also please briefly state how "prostate cancer risk" is calculated, either in the main text or in "Materials and methods" to guide the reader?

In our statistical analyses, “prostate cancer risk” refers to the relative risk estimated by the odds ratio calculated from a prostate cancer case-control analysis in each replication study. In all analyses assessing the association of PRS with prostate cancer risk, logistic regression models were used to estimate the odds ratio with case-control status as the outcome (a binary dependent variable) and the PRS categories as independent predictors, adjusting for age and up to ten principal components. The text in the Materials and methods section is modified to elaborate on these details in the statistical analysis (page 13 and page 14).

3. Could the authors please address how the results would be different if a random-effects meta-analysis model were to be used? A reviewer mentions that there is substantial heterogeneity in the environmental effects on prostate cancer risk across these different populations.

Within the European (UK Biobank, MVP, and MGB Biobank) and African population (MVP, MGB Biobank, MADCaP Network, CA UG, and NCI-MD) population, we also meta-analyzed the PRS associations with prostate cancer risk from individual replication studies using a random-effects method. We didn’t observe appreciable differences between the results from a fixed-effects and a random-effects meta-analysis in these two ancestry populations (see , Author response table 1). Given the similarities between these results, we only reported the PRS associations from the fixed-effects inverse-variance-weighted meta-analysis.

The PRS association on prostate cancer risk estimated from individual replication studies within each ancestry population were meta-analyzed using (a) a fixed-effects method and (b) a random-effects method.

4. Have the authors looked into the PRS performance across ancestry proportion estimates and PRS associations with prostate cancer susceptibility across bins of ancestry proportions (i.e., AFR ancestry 0-20%, 20-40%, etc)? Could they comment a little on this topic? This could be an interesting follow-up.

We appreciate the reviewer’s insightful suggestion. In three of the five replication studies included in the African-ancestry meta-analysis (CA UG, MADCaP Network, and NCI-MD), we estimated the proportion of African ancestry (%AFR) from an unsupervised (K=2) ADMIXTURE analysis using the 1000 Genomes Project phase 3 European and African samples as the reference populations. We do not have access to the admixture information in the MVP and MGB Biobank data.

The %AFR was higher and less dispersed in MADCaP (mean = 95.7%, standard deviation [SD] = 4.6%) than in CA UG (mean = 79.2%, SD = 13.5%) and NCI-MD (mean = 77.2%, SD = 10.2%; see Author response table 2). Despite the differences in %AFR, we found that the PRS associations with prostate cancer risk were similar across these three studies, particularly in the top PRS decile (Figure 1 —figure supplementary 1). Although we were not able to formally test the effect modification of African ancestry on the PRS association due to the limited sample sizes of these three studies, the similar PRS associations observed in these studies support the robustness of this multi-ancestry PRS in risk stratification across African populations with varying degrees of admixture. Future investigations with sufficient sample sizes are warranted to better understand the interaction between admixture and PRS.

5. Would it make sense to model select on other demographic/clinical covariates (e.g., SES measures) when estimating the odds ratios?

For prostate cancer, only age, family history, and race are considered well-established risk factors. Given the potential correlation between family history and PRS, family history of prostate cancer is typically not adjusted for in the association analysis of PRS. Other demographic or clinical factors are unlikely to be associated with genotype status and thus not considered as potential confounders in the association between PRS and prostate cancer risk. Therefore, adjusting for these variables will not be expected to influence PRS associations.

Other details

1. Can the authors please clarify what is the difference between Figure 1 and Figure 1 – source data 1? The caption of Figure 1 states that "ORs and 95% CIs for each PRS category are provided in Figure 1 – source data 1." but they seem to be already present in Figure 1. Also, please clarify the difference between Figure 2 and Figure 2 – source data 1.

Figure 1 is a graphic presentation of the results in Figure 1 – source data 1. Figure 1 – source data 1 provides the actual numbers of odds ratios (ORs), 95% confidence intervals (CIs), and P values for each PRS category in each ancestry population, which were cited in the main text. Although they present the same PRS association results, the detailed information included in Figure 1 – source data 1 would allow direct comparison or meta-analysis with other/future replication studies. The same applies to Figure 2 and Figure 2 – source data 2. We believe it is important to include both the figures and the tables (source data) in the manuscript to provide sufficient information for interpretation.

2. The acronym "Partners" is used in the legend of Figure 1 instead of the acronym "MGB" used in the main text.

We thank the reviewer for spotting this error. The legend of Figure 1 – source data 1 has been updated to be consistent with the main text, replacing “Partners” with “MGB Biobank” (page 22).

3. Page 20.- "Age-specific mortality rates are provided from a reference cohort." A reviewer recommends specifying which reference cohort is used.

We modified the text in the Materials and methods (page 15) to specify that the age-specific mortality rates from the National Cancer for Health Statistics, CDC (1993-2013) were used in the calculation of absolute risk of prostate cancer.
