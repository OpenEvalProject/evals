# Projected long-term effects of colorectal cancer screening disruptions following the COVID-19 pandemic

## Authors

- Pedro Nascimento de Lima<sup>1</sup> ([ORCID: 0000-0001-9057-198X](https://orcid.org/0000-0001-9057-198X)) †
- Rosita van den Puttelaar<sup>2</sup> ([ORCID: 0000-0003-2216-6557](https://orcid.org/0000-0003-2216-6557))
- Anne I Hahn<sup>3</sup> ([ORCID: 0000-0003-4061-2303](https://orcid.org/0000-0003-4061-2303))
- Matthias Harlass<sup>2</sup>
- Nicholson Collier<sup>4</sup> ([ORCID: 0000-0002-2376-4156](https://orcid.org/0000-0002-2376-4156))
- Jonathan Ozik<sup>4</sup> ([ORCID: 0000-0002-3495-6735](https://orcid.org/0000-0002-3495-6735))
- Ann G Zauber<sup>3</sup> ([ORCID: 0000-0002-1764-5994](https://orcid.org/0000-0002-1764-5994))
- Iris Lansdorp-Vogelaar<sup>2</sup>
- Carolyn M Rutter<sup>5</sup> ([ORCID: 0000-0002-4396-8594](https://orcid.org/0000-0002-4396-8594))

### Affiliations

1. RAND Corporation Santa Monica United States ([ROR:00f2z7n96](https://ror.org/00f2z7n96))
2. Erasmus MC Rotterdam Netherlands ([ROR:018906e22](https://ror.org/018906e22))
3. Memorial Sloan Kettering Cancer Center New York United States ([ROR:02yrq0923](https://ror.org/02yrq0923))
4. Argonne National Laboratory Lemont United States ([ROR:05gvnxz63](https://ror.org/05gvnxz63))
5. Fred Hutchinson Cancer Center Seattle, WA United States ([ROR:007ps6h72](https://ror.org/007ps6h72))

† Corresponding author

## Abstract

The aftermath of the initial phase of the COVID-19 pandemic may contribute to the widening of disparities in colorectal cancer (CRC) outcomes due to differential disruptions to CRC screening. This comparative microsimulation analysis uses two CISNET CRC models to simulate the impact of ongoing screening disruptions induced by the COVID-19 pandemic on long-term CRC outcomes. We evaluate three channels through which screening was disrupted: delays in screening, regimen switching, and screening discontinuation. The impact of these disruptions on long-term CRC outcomes was measured by the number of life-years lost due to CRC screening disruptions compared to a scenario without any disruptions. While short-term delays in screening of 3–18 months are predicted to result in minor life-years loss, discontinuing screening could result in much more significant reductions in the expected benefits of screening. These results demonstrate that unequal recovery of screening following the pandemic can widen disparities in CRC outcomes and emphasize the importance of ensuring equitable recovery to screening following the pandemic.

## Introduction

The novel SARS-Cov-2 (COVID-19) pandemic has resulted in major health consequences across the globe. In addition to the over 1 million COVID-19 deaths in the United States (Johns Hopkins Univerity & Medicine Coronavirus Resource Center, 2022), the pandemic has also contributed to steep declines in cancer screening, most notably in the early phases of the pandemic due to government-mandated shutdowns of non-emergency medical services (Gupta et al., 2020). It is estimated that colorectal cancer (CRC) screening decreased by 85% in the United States during the early phase of the pandemic, from March through April 2020 (London et al., 2022). The pandemic continues to affect CRC screening and diagnosis through staff shortages that reduce capacity at gastroenterology clinics and patient hesitancy to seek care (Wilensky, 2022; Del Vecchio Blanco et al., 2020). Despite cancer screening reopening efforts, CRC screening has not yet returned to pre-pandemic levels (Ong, 2021).

CRC remains the second-leading cause of cancer deaths in the United States, with approximately 153,020 new cases and 52,550 deaths estimated in the year 2023 (Siegel et al., 2023). There is clear evidence that screening has a major impact on reducing the burden of CRC (Edwards et al., 2010; Zauber et al., 2012) and that it is cost-effective (Knudsen et al., 2021; Lansdorp-Vogelaar et al., 2011). The current United States Preventive Task Force (USPSTF) report recommends multiple screening options, including annual fecal immunochemical tests (FIT) and colonoscopy every 10 years for average-risk individuals (Davidson et al., 2021). However, CRC screening uptake was of concern even before the pandemic, with CRC screening rates well below the goal of 70.5% for Healthy People 2020 and the National Colorectal Cancer Roundtable goal of 80% by 2018 (Shapiro et al., 2021). Low rates of CRC screening have been exacerbated by the COVID-19 pandemic, and delays in screening will result in delays in diagnosis, stage progression, and increased CRC mortality.

The pandemic may also further exacerbate existing disparities related to screening. The burden of unemployment and associated loss of access to healthcare varies across different racial and ethnic groups (Marcondes et al., 2021). Because of this, the pandemic may contribute to widening disparities in cancer outcomes. A recent analysis using National Health Interview Survey (NHIS) data postulated that unemployment was adversely associated with being up-to-date with screening, with only 16.7% of unemployed individuals participating in recent CRC screenings, only 48.5% of whom were up-to-date with CRC screening (Fedewa et al., 2022).

The objective of this study is to estimate the impact of ongoing screening and treatment disruptions induced by the COVID-19 pandemic on long-term CRC outcomes. We examine 25 scenarios that reflect different levels of pre-pandemic adherence to colonoscopy and FIT screening to assess how unequal recovery in screening may contribute to widening disparities in CRC lifetime outcomes.

## Methods

This paper uses two independently developed microsimulation models of CRC, CRC-SPIN and MISCAN-Colon, to estimate the effects of pandemic-induced disruptions in colonoscopy screening for eight pre-pandemic average-CRC risk population cohorts in the United States. CRC-SPIN and MISCAN-Colon models are part of the National Cancer Institute’s CISNET consortium and describe the natural history of CRC in an unscreened population based on the adenoma-carcinoma sequence. Detailed descriptions of these models and underlying assumptions may be found elsewhere (Knudsen et al., 2021; Loeve et al., 1999; Rutter et al., 2019, van Hees et al., 2014). We consider variations on two commonly used screening strategies in the USPSTF recommendations during the onset of the pandemic in March 2020 (Knudsen et al., 2016): Decennial colonoscopy from age 50 to 70 and annual FIT from age 50 to 75, with diagnostic colonoscopy after a positive FIT.

### Cohorts

We simulated eight pre-pandemic population cohorts that represent average-risk individuals in the United States, defined by both cohort members’ age in April 2020 and their pre-pandemic screening regimens: (i) unscreened 50-year-olds (U50), (ii) unscreened 60-year-olds (U60), (iii) colonoscopy screening-adherent 60-year-olds (C60, who received their first screening colonoscopy at age 50 but have not yet had a colonoscopy at age 60), (iv) FIT screening-adherent 60-year-olds (F60, who performed annual FIT from age 50 to 59), (v) FIT screening semi-adherent 60-year-olds (f60) – those who received biannual FIT from age 50 to 56, (vi) unscreened 70-year-olds (U70), (vii) colonoscopy screening-adherent 70-year-olds (C70, who received screening colonoscopies at age 50 and 60), and (viii) FIT screening-adherent 70-year-olds (F70, who performed annual FIT from age 50 to 69). We simulated 10 million individuals within each cohort to reduce the stochastic variability in our runs and to ensure sufficient precision in our estimates. For each cohort, we simulated three sets of post-pandemic scenarios: no disruption, delays, and no screening.

### Screening regimens under no disruption

The no-disruption scenarios simulate post-pandemic screening scenarios for each cohort in the counterfactual scenario where no pandemic-induced screening disruptions occurred. In no-disruption scenarios, all these cohorts would have been screened during the pandemic first lockdowns in March 2020. Cohorts with colonoscopy and FIT adherent individuals (U50, C60, F60 C70, F70) continue to follow guideline-recommended strategies strictly, with no delays. Cohorts with delayed initiation (U60, U70) begin screening late but otherwise follow guideline-recommended strategies with no delays but without any additional screening beyond the usual stopping age. Finally, for the FIT-semi-adherent 60-year-olds (f60), we simulate resumption of biannual FIT at age 60, continuing to age 75.

### Pandemic-induced disruptions in CRC screening

#### Delays

The pandemic has been shown to affect CRC outcomes through delays in screening. Screening colonoscopy and FIT are assumed to be delayed for a set duration of months starting at the onset of the COVID-19 pandemic in April 2020. Short-term screening delays may have occurred for a series of reasons. First, elective procedures were postponed during the first months of the pandemic. The cancellation of elective procedures caused a sharp decline in CRC screening exams during the initial phase of the pandemic (Gupta and Lieberman, 2020). To represent the full spectrum of delays caused by the pandemic – either due to cancellation of elective procedures or disruption in access to healthcare – we consider three sets of delays: a 3-, 9-, or 18-month delay in screening, which we label as short-term delays. For each delay scenario, the delay was applied on the first post-March 2020 screening exam and carried forward to any subsequent exams.

Second, the pandemic may have caused long-term delays in CRC screening. While the recovery in screening rates among insured individuals was rapid, (Choy et al., 2022) the pandemic also caused a sharp economic recession. The uneven recovery in labor force participation has the potential to cause disparities in access to healthcare in the United States due to unemployment and discontinuation of health insurance. To examine these longer-term effects of the pandemic, we consider scenarios where screening is paused for an extended period. For the 50- and 60-year-old cohorts, we simulated scenarios where screening is discontinued until the start age of Medicare enrollment (65 years). For 70-year-olds, we consider a scenario where screening is only resumed at age 75 – 5 years after the pandemic onset.

#### Screening regimen switching

The pandemic may also affect CRC behavior via screening regimen switching – that is, changing from a colonoscopy screening regimen to one based on FIT. There is evidence that during the pandemic some patients switched from colonoscopy to FIT (Fedewa et al., 2022) to reduce the need for in-person endoscopy procedures. Considering this possibility, we model scenarios where individuals who initially participated in a regimen of screening colonoscopy (C60 and C70) permanently switch from decennial colonoscopy to annual FIT screening as a boundary case. While one might expect pandemic-induced regimen switching to be temporary, permanent switching can serve as a boundary case for our analysis – that is, the effect of short-term regimen switching is expected to be lower than the effect of permanent regimen switching.

#### Screening discontinuation

We also simulate scenarios where screening is completely discontinued after the pandemic onset as the most consequential boundary case scenario. While only a small (unknown) proportion of individuals will discontinue screening after the pandemic, this scenario serves as an upper bound for the worst possible disruption in CRC screening following the pandemic.

#### Scenarios

Each of the scenarios simulated in this study results from the combination of a pre-pandemic population cohort, a no-disruption screening scenario that serves as a counterfactual, and one or more screening disruptions (i.e. switching to FIT screening occurred in tandem with short-term delays). Table 1 lists those combinations and the scenario labels used in this analysis. We code our scenarios as [pre-pandemic screening cohort] | [post-pandemic disruptions].

**Table 1.**
 Study cohorts and scenarios.


<table>
  <thead>
    <tr>
      <th rowspan="2">Cohort</th>
      <th rowspan="2">No-disruption counterfactual</th>
      <th colspan="2">CRC screening disruption scenario</th>
    </tr>
    <tr>
      <th>Description</th>
      <th>Label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Unscreened50-year-olds (U50)</td>
      <td rowspan="2">Decennial COL from age 50 to 70</td>
      <td>Short-term delays of [d] months*</td>
      <td>U50 | C[d]m</td>
    </tr>
    <tr>
      <td>Long-term delay (COL at age 65 and 75)</td>
      <td>U50 | C@65</td>
    </tr>
    <tr>
      <td>Annual FIT from age 50 to 75</td>
      <td>Short-term delays*</td>
      <td>U50 | F[d]m</td>
    </tr>
    <tr>
      <td rowspan="3">Unscreened60-year-olds (U60)</td>
      <td rowspan="2">Decennial COL from age 60 to 70</td>
      <td>Short-term delays*</td>
      <td>U60 | C[d]m</td>
    </tr>
    <tr>
      <td>Long-term delay (COL at age 65 and 75)</td>
      <td>U60 | C@65</td>
    </tr>
    <tr>
      <td>Annual FIT from age 60 to 75</td>
      <td>Short-term delays*</td>
      <td>U60 | F[d]m</td>
    </tr>
    <tr>
      <td rowspan="4">COL-adherent60-year-olds (C60)</td>
      <td rowspan="4">Decennial COL from age 50 to 70</td>
      <td>Short-term delays*</td>
      <td>C60 | C[d]m</td>
    </tr>
    <tr>
      <td>Switch to annual FIT and short-term delays</td>
      <td>C60 | F[d]m</td>
    </tr>
    <tr>
      <td>Long-term delay (COL at age 65 and 75)</td>
      <td>C60 | C@65</td>
    </tr>
    <tr>
      <td>Discontinue screening</td>
      <td>C60 | U</td>
    </tr>
    <tr>
      <td rowspan="2">FIT-adherent60-year-olds (F60)</td>
      <td rowspan="2">Annual FIT from age 50 to 75</td>
      <td>Short-term delays*</td>
      <td>F60 | F[d]m</td>
    </tr>
    <tr>
      <td>Discontinue screening</td>
      <td>F60 | U</td>
    </tr>
    <tr>
      <td rowspan="2">FIT-semi-adherent60-year-olds (f60)</td>
      <td rowspan="2">Biannual FIT from age 50 to 56, annual FIT from age 60 to 75</td>
      <td>Short-term delays*</td>
      <td>f60 | F[d]m</td>
    </tr>
    <tr>
      <td>Discontinue screening</td>
      <td>f60 | U</td>
    </tr>
    <tr>
      <td rowspan="3">Unscreened70-year-olds (U70)</td>
      <td rowspan="2">COL at age 70</td>
      <td>Short-term delays*</td>
      <td>U70 | C[d]m</td>
    </tr>
    <tr>
      <td>Long-term delay (COL at age 75)</td>
      <td>U70 | C@75</td>
    </tr>
    <tr>
      <td>Annual FIT from age 70 to 75</td>
      <td>Short-term delays</td>
      <td>U70 | F[d]m</td>
    </tr>
    <tr>
      <td rowspan="4">COL-adherent70-year-olds (C70)</td>
      <td rowspan="4">Decennial COL from age 50 to 70</td>
      <td>Short-term delays*</td>
      <td>C70 | C[d]m</td>
    </tr>
    <tr>
      <td>Switch to annual FIT and short-term delays</td>
      <td>C70 | F[d]m</td>
    </tr>
    <tr>
      <td>Long-term delayPerform COL at age 75</td>
      <td>C70 | C@75</td>
    </tr>
    <tr>
      <td>Discontinue screening</td>
      <td>C70 | U</td>
    </tr>
    <tr>
      <td rowspan="2">FIT-adherent70-year-olds (F70)</td>
      <td rowspan="2">Annual FIT from age 50 to 75</td>
      <td>Short-term delays*</td>
      <td>F70 | F[d]m</td>
    </tr>
    <tr>
      <td>Discontinue screening</td>
      <td>F70 | U</td>
    </tr>
  </tbody>
</table>

_Notes: This table presents the scenarios considered in this study. Each scenario corresponds to a combination of a population cohort, indicated by their age during the first COVID-19 lockdowns (March 2020), a pre-pandemic, and a post-pandemic screening regimen. The scenarios aim to represent possible combinations of screening regimens followed in the United States. The first letter in the scenario code represents screening before the pandemic and the second letter represents screening after the pandemic.*Delays of 3, 9, and 18 months. Letter d stands for the number of months of delays._

#### Outcomes

The primary measure used to assess the benefit of CRC screening programs is the expected lifetime life-years gained (LYG) from screening. All outcomes in this study correspond to expected value of life-years (LY) across the US population with average CRC risk. This study investigates the extent to which benefits from screening are expected to be lost due to pandemic-induced disruptions to CRC screening. Therefore, we calculated the total number of LY for each cohort and scenario, including the number of LY under no screening (LYNS) and the number of LY under no disruptions (LYND). LYNS is computed by simulating the cohort in the absence of CRC screening and LYND is computed by simulating the same cohort under an ideal screening scenario where no disruptions to screening happened, as defined in Table 1.

The key outcome estimated in this study is the expected number of LY lost (LYL) due to disruptions in screening, defined as $LYL= LYND−LY$. The hypothetical number of LY gained (LYG) from screening under no disruptions are $LYG_{no disruption} = LYND−LYNS$. Finally, we compute the percentage of life-years gained or lost due to disruption as $% LY Lost =100* LYL / LYG_{no disruption}$ . The first outcome measure (LYL) is an absolute measure of the loss of screening benefit due to pandemic disruptions. The percent LY lost due to disruptions indicates the share of screening benefit lost due to the pandemic. Following the previous analyses, we present all outcomes as LY per 1000 individuals or life days per person. We compute each of those outcomes separately for each model and report the range of outcomes observed across both models. In addition to LY outcomes, we present lifetime number of CRC cases over the remaining lifetime of individuals and number of CRC deaths (Supplementary files 2 and 3).

### Test characteristics

Table 2 specifies sensitivity and specificity assumptions underlying colonoscopy and FIT exams evaluated in this study. Our main results present colonoscopy sensitivity following assumptions used in the analysis that informed the most recent USPSTF screening recommendations (Zauber et al., 2008). In addition, we simulate all screening disruption scenarios under assuming lower colonoscopy sensitivity.

**Table 2.**
 Per lesion test sensitivity and specificity.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">Sensitivity*</th>
      <th rowspan="2">Specificity†</th>
    </tr>
    <tr>
      <th>Test</th>
      <th>Adenoma1–5 mm</th>
      <th>Adenoma6–9 mm</th>
      <th>Adenoma ≥10 mm</th>
      <th>Preclinical cancer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Colonoscopy, high sensitivity‡</td>
      <td>0.75</td>
      <td>0.85</td>
      <td>0.95</td>
      <td>0.95</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>Colonoscopy, low sensitivity§</td>
      <td>0.55</td>
      <td>0.70</td>
      <td>0.90</td>
      <td>0.95</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td colspan="6">FIT¶</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>0.00</td>
      <td>0.114</td>
      <td>0.159</td>
      <td>0.62565/0.886</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>CRC-SPIN</td>
      <td>0.05</td>
      <td>0.15</td>
      <td>0.22</td>
      <td>*0.74</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>

_Notes: This table presents the assumed test characteristics. We simulated two colonoscopy sensitivity scenarios seeking to represent a range of colonoscopy sensitivity of gastroenterologists in the United States.*Sensitivity is for lesions within reach of the scope. We assume the same test characteristics for follow-up and surveillance colonoscopy as for screening colonoscopy.†For FIT, the lack of specificity reflects detection of bleeding from other causes. We assume other-cause bleeding is independent of adenoma status. For colonoscopy, the lack of specificity reflects detection of non-adenomatous lesions, but specificity is handled in post-processing in cost-effectiveness analyses. Since this study does not consider burden outcomes, specificity is not considered in this paper. Specificity values were obtained from Lin et al., 2021.‡Baseline scenarios used in Zauber et al., 2008.§In line with low-sensitivity scenarios compatible with Rutter et al., 2022.¶CRC-SPIN uses per-person test sensitivity for stool-based tests that are based on the size of the most advanced lesion. To account for the likelihood that a person with multiple adenomas is more likely than a person with only one to have a positive stool test, MISCAN uses lesion-based sensitivities instead of person-based sensitivities. Lesion-based sensitivities were derived by calibrating the person-based sensitivities to the number of people having one or more small/medium/large adenomas or cancers detected by stool-based testing with diagnostic colonoscopy, divided by those having one or more small/medium/large adenomas or cancers detected by colonoscopy screening._

### CRC surveillance

We assume that individuals with an adenoma detected undergo colonoscopic surveillance according to the Multi-Society Task Force (MSTF) guidelines. These guidelines provide intervals for surveillance based on baseline findings and findings at the first surveillance colonoscopy. We assume that the intervals provided can be more generally expressed as the intervals based on the most recent colonoscopy (‘first-most recent colonoscopy’) and the colonoscopy prior to that (‘second-most recent colonoscopy’). In situations where the MSTF provided a range rather than a single interval, we assumed that the shortest interval would be used in routine practice. The resulting intervals are shown in Table 3.

**Table 3.**
 CRC surveillance intervals.


<table>
  <thead>
    <tr>
      <th>Finding at second-most recent colonoscopy*†</th>
      <th>Finding at first-most recent colonoscopy*†</th>
      <th>Interval‡ to next colonoscopy, years</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No prior colonoscopy</td>
      <td>Normal colonoscopy</td>
      <td>See note below§</td>
    </tr>
    <tr>
      <td></td>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>7</td>
    </tr>
    <tr>
      <td></td>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>10 adenomas &lt;10 mm or any adenoma ≥10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>&gt;10 adenomas</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Normal colonoscopy</td>
      <td>Normal colonoscopy</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>7</td>
    </tr>
    <tr>
      <td></td>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>5–10 adenomas &lt;10 mm or any adenoma ≥10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>&gt;10 adenomas</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>Normal colonoscopy</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>7</td>
    </tr>
    <tr>
      <td></td>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>5–10 adenomas &lt;10 mm or any adenoma ≥10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>&gt;10 adenomas</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>Normal colonoscopy</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>7</td>
    </tr>
    <tr>
      <td></td>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>5–10 adenomas &lt;10 mm or any adenoma ≥10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>&gt;10 adenomas</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5–10 adenomas &lt;10 mm</td>
      <td>Normal colonoscopy</td>
      <td>5</td>
    </tr>
    <tr>
      <td>or</td>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>5</td>
    </tr>
    <tr>
      <td>any adenoma ≥10 mm</td>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>5–10 adenomas &lt;10 mm or any adenoma ≥10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>&gt;10 adenomas</td>
      <td>1</td>
    </tr>
    <tr>
      <td>&gt;10 adenomas of any size</td>
      <td>Normal colonoscopy</td>
      <td>5</td>
    </tr>
    <tr>
      <td></td>
      <td>1–2 adenomas &lt;10 mm</td>
      <td>5</td>
    </tr>
    <tr>
      <td></td>
      <td>3–4 adenomas &lt;10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>5–10 adenomas &lt;10 mm or any adenoma ≥10 mm</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>&gt;10 adenomas</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

_*A normal colonoscopy is one in which no adenomas, SSPs (not currently simulated), or CRC is detected.†This table omits the case where CRC is detected at a screening, diagnostic, or surveillance colonoscopy because the CISNET CRC models do not simulate detailed events following CRC diagnosis.‡The Multi-Society Task Force provides a range for some intervals (e.g. the interval for 3–4 adenomas <10 mm is 3–5 years). In such cases, we selected the shortest intervals provided.§A person whose first screening or diagnostic colonoscopy is normal does not enter surveillance but instead resumes screening with the original modality 10 years after the normal colonoscopy. The exception to the 10-year waiting period is when the first colonoscopy is a screening colonoscopy with an x-year interval, where x>10. In that case, the next colonoscopy is in x years._

We assume that persons in whom adenoma(s) have been detected remain on surveillance until age 85, provided that no adenomas are detected at the last surveillance colonoscopy. If adenomas are detected, then surveillance continues according to the clinical findings at the last colonoscopy until the person has a colonoscopy with no adenomas detected. For example, if a person has a surveillance colonoscopy at age 83 and no adenomas are detected at this exam or the exam before this one, they would be recommended to have their next surveillance at age 93. Age 93 is after the surveillance stopping age of 85 and the exam prior to age 85 was negative, so they will not have any more surveillance colonoscopies after age 83. However, if the exam at age 83 instead detected 1–2 small adenomas, they would come back for their surveillance colonoscopy at age 90, because adenomas were detected at the exam at age 83.

## Results

Loss of life due to screening disruptions was the largest for cohorts with severe disruptions after the pandemic (Figure 1). Aside from not receiving any screening, the worst-case scenario for the 50-year-old cohort was to postpone screening until age 65 when they become Medicare eligible. This cohort (scenario U50 | C@65) is expected to lose 104–127 LY per 1000 individuals – a 38–42% loss in LYG compared to a no-disruption scenario where they start screening at age 50 (Table 4). This cohort would be 1.3–1.9 times more likely to have CRC over their lifetime (Supplementary file 2) and 1.6–2.0 times more likely to die with CRC (Supplementary file 3) compared to a cohort that started screening at age 50. Other disruption scenarios are predicted to have minor effects on this cohort. For example, 50-year-olds with colonoscopy screening delayed by 18 months (scenario U50 | C18m) are expected to experience a loss of 6–7 LY per 1000 individuals, and a 2% loss in LYG from screening compared to a no-disruption scenario.

![Figure 1.](https://cdn.elifesciences.org/articles/85264/elife-85264-fig1-v1.jpg)

**Figure 1.:** Notes: Each dot represents the estimated life-years lost per 1000 individuals or life-days lost from one model under the high sensitivity scenario. Results are ordered from highest to lowest reduction in benefit induced by the pandemic. Scenarios that result in less than 2 life-days lost per person are omitted from this figure and presented in a Supplementary figure. This figure does not present a counterfactual no-screening scenario for the 50-year-olds.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/85264/elife-85264-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Notes: Each dot represents the estimated life-years lost per 1000 individuals or life-days lost from one model under the high sensitivity scenario. Results are ordered from highest to lowest reduction in benefit induced by the pandemic. This figure supplement only shows scenarios that resulted in in less than 2 life-days lost per person. This figure does not present a counterfactual no-screening scenario for the 50-year-olds.

**Table 4.**
 Projected life-years (LY) per 1000 individuals.


<table>
  <thead>
    <tr>
      <th rowspan="2">Scenario</th>
      <th rowspan="2">Model</th>
      <th>No screening</th>
      <th colspan="2">Screening without disruptions</th>
      <th colspan="2">Screening with disruptions</th>
      <th colspan="2">Loss due to disruptions</th>
    </tr>
    <tr>
      <th>LY[a]</th>
      <th>LY[b]</th>
      <th>LYG[b-a]</th>
      <th>LY[c]</th>
      <th>LYG[c-a]</th>
      <th>LY[b-c]</th>
      <th>% LYG loss[(b-c)/b]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">U50 | C3m</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,893</td>
      <td>299</td>
      <td>31,892</td>
      <td>297</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,494</td>
      <td>273</td>
      <td>31,491</td>
      <td>270</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">U50 | C9m</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,893</td>
      <td>299</td>
      <td>31,890</td>
      <td>295</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,494</td>
      <td>273</td>
      <td>31,490</td>
      <td>268</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="2">U50 | C18m</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,893</td>
      <td>299</td>
      <td>31,886</td>
      <td>291</td>
      <td>7</td>
      <td>2</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,494</td>
      <td>273</td>
      <td>31,488</td>
      <td>266</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="2">U50 | C@65</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,893</td>
      <td>299</td>
      <td>31,766</td>
      <td>172</td>
      <td>127</td>
      <td>43</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,494</td>
      <td>273</td>
      <td>31,390</td>
      <td>169</td>
      <td>104</td>
      <td>38</td>
    </tr>
    <tr>
      <td rowspan="2">U50 | F3m</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,866</td>
      <td>271</td>
      <td>31,865</td>
      <td>270</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,483</td>
      <td>261</td>
      <td>31,481</td>
      <td>259</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">U50 | F9m</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,866</td>
      <td>271</td>
      <td>31,862</td>
      <td>268</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,483</td>
      <td>261</td>
      <td>31,480</td>
      <td>258</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">U50 | F18m</td>
      <td>CRCSPIN</td>
      <td>31,595</td>
      <td>31,866</td>
      <td>271</td>
      <td>31,858</td>
      <td>264</td>
      <td>7</td>
      <td>3</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>31,222</td>
      <td>31,483</td>
      <td>261</td>
      <td>31,478</td>
      <td>256</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | C3m</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,557</td>
      <td>221</td>
      <td>23,560</td>
      <td>224</td>
      <td>-3</td>
      <td>-1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,309</td>
      <td>195</td>
      <td>23,304</td>
      <td>190</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | C9m</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,557</td>
      <td>221</td>
      <td>23,555</td>
      <td>219</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,309</td>
      <td>195</td>
      <td>23,301</td>
      <td>187</td>
      <td>8</td>
      <td>4</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | C18m</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,557</td>
      <td>221</td>
      <td>23,547</td>
      <td>211</td>
      <td>10</td>
      <td>4</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,309</td>
      <td>195</td>
      <td>23,296</td>
      <td>182</td>
      <td>14</td>
      <td>7</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | C@65</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,557</td>
      <td>221</td>
      <td>23,512</td>
      <td>176</td>
      <td>45</td>
      <td>20</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,309</td>
      <td>195</td>
      <td>23,267</td>
      <td>153</td>
      <td>42</td>
      <td>21</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | F3m</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,528</td>
      <td>191</td>
      <td>23,529</td>
      <td>193</td>
      <td>-2</td>
      <td>-1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,291</td>
      <td>177</td>
      <td>23,288</td>
      <td>174</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | F9m</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,528</td>
      <td>191</td>
      <td>23,525</td>
      <td>189</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,291</td>
      <td>177</td>
      <td>23,285</td>
      <td>171</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <td rowspan="2">U60 | F18m</td>
      <td>CRCSPIN</td>
      <td>23,336</td>
      <td>23,528</td>
      <td>191</td>
      <td>23,519</td>
      <td>183</td>
      <td>8</td>
      <td>4</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,114</td>
      <td>23,291</td>
      <td>177</td>
      <td>23,280</td>
      <td>166</td>
      <td>11</td>
      <td>6</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | C3m</td>
      <td>CRCSPIN</td>
      <td>23,243</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,541</td>
      <td>299</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,320</td>
      <td>243</td>
      <td>23,318</td>
      <td>241</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | C9m</td>
      <td>CRCSPIN</td>
      <td>23,242</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,541</td>
      <td>299</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,319</td>
      <td>243</td>
      <td>23,317</td>
      <td>240</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | C18m</td>
      <td>CRCSPIN</td>
      <td>23,242</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,540</td>
      <td>298</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,320</td>
      <td>243</td>
      <td>23,317</td>
      <td>239</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | F3m</td>
      <td>CRCSPIN</td>
      <td>23,242</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,532</td>
      <td>289</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,320</td>
      <td>243</td>
      <td>23,310</td>
      <td>233</td>
      <td>10</td>
      <td>4</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | F9m</td>
      <td>CRCSPIN</td>
      <td>23,243</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,532</td>
      <td>289</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,319</td>
      <td>243</td>
      <td>23,310</td>
      <td>233</td>
      <td>9</td>
      <td>4</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | F18m</td>
      <td>CRCSPIN</td>
      <td>23,243</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,532</td>
      <td>289</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,320</td>
      <td>243</td>
      <td>23,309</td>
      <td>232</td>
      <td>11</td>
      <td>4</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | C@65</td>
      <td>CRCSPIN</td>
      <td>23,243</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,538</td>
      <td>295</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,320</td>
      <td>243</td>
      <td>23,308</td>
      <td>231</td>
      <td>11</td>
      <td>5</td>
    </tr>
    <tr>
      <td rowspan="2">C60 | U</td>
      <td>CRCSPIN</td>
      <td>23,243</td>
      <td>23,541</td>
      <td>298</td>
      <td>23,435</td>
      <td>192</td>
      <td>106</td>
      <td>36</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,077</td>
      <td>23,320</td>
      <td>243</td>
      <td>23,195</td>
      <td>118</td>
      <td>125</td>
      <td>51</td>
    </tr>
    <tr>
      <td rowspan="2">F60 | F3m</td>
      <td>CRCSPIN</td>
      <td>23,307</td>
      <td>23,579</td>
      <td>272</td>
      <td>23,576</td>
      <td>269</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,144</td>
      <td>23,377</td>
      <td>234</td>
      <td>23,377</td>
      <td>233</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">F60 | F9m</td>
      <td>CRCSPIN</td>
      <td>23,306</td>
      <td>23,578</td>
      <td>272</td>
      <td>23,575</td>
      <td>269</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,143</td>
      <td>23,376</td>
      <td>234</td>
      <td>23,376</td>
      <td>234</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">F60 | F18m</td>
      <td>CRCSPIN</td>
      <td>23,307</td>
      <td>23,578</td>
      <td>272</td>
      <td>23,573</td>
      <td>267</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,143</td>
      <td>23,377</td>
      <td>234</td>
      <td>23,376</td>
      <td>233</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">F60 | U</td>
      <td>CRCSPIN</td>
      <td>23,307</td>
      <td>23,579</td>
      <td>272</td>
      <td>23,467</td>
      <td>160</td>
      <td>111</td>
      <td>41</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,143</td>
      <td>23,376</td>
      <td>234</td>
      <td>23,283</td>
      <td>141</td>
      <td>93</td>
      <td>40</td>
    </tr>
    <tr>
      <td rowspan="2">f60 | F3m</td>
      <td>CRCSPIN</td>
      <td>23,314</td>
      <td>23,562</td>
      <td>249</td>
      <td>23,560</td>
      <td>247</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,136</td>
      <td>23,355</td>
      <td>219</td>
      <td>23,353</td>
      <td>217</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">f60 | F9m</td>
      <td>CRCSPIN</td>
      <td>23,314</td>
      <td>23,563</td>
      <td>249</td>
      <td>23,559</td>
      <td>245</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,136</td>
      <td>23,355</td>
      <td>219</td>
      <td>23,352</td>
      <td>216</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">f60 | F18m</td>
      <td>CRCSPIN</td>
      <td>23,313</td>
      <td>23,562</td>
      <td>249</td>
      <td>23,556</td>
      <td>242</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,136</td>
      <td>23,355</td>
      <td>219</td>
      <td>23,350</td>
      <td>214</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="2">f60 | U</td>
      <td>CRCSPIN</td>
      <td>23,313</td>
      <td>23,562</td>
      <td>249</td>
      <td>23,419</td>
      <td>105</td>
      <td>143</td>
      <td>58</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>23,134</td>
      <td>23,353</td>
      <td>219</td>
      <td>23,203</td>
      <td>68</td>
      <td>150</td>
      <td>69</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | C3m</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,102</td>
      <td>128</td>
      <td>16,099</td>
      <td>126</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,866</td>
      <td>117</td>
      <td>15,857</td>
      <td>108</td>
      <td>9</td>
      <td>8</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | C9m</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,102</td>
      <td>128</td>
      <td>16,094</td>
      <td>120</td>
      <td>8</td>
      <td>6</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,866</td>
      <td>117</td>
      <td>15,852</td>
      <td>103</td>
      <td>14</td>
      <td>12</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | C18m</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,102</td>
      <td>128</td>
      <td>16,086</td>
      <td>113</td>
      <td>16</td>
      <td>12</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,866</td>
      <td>117</td>
      <td>15,845</td>
      <td>97</td>
      <td>21</td>
      <td>18</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | C@75</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,102</td>
      <td>128</td>
      <td>16,052</td>
      <td>79</td>
      <td>50</td>
      <td>39</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,866</td>
      <td>117</td>
      <td>15,815</td>
      <td>66</td>
      <td>51</td>
      <td>43</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | F3m</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,069</td>
      <td>95</td>
      <td>16,067</td>
      <td>93</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,840</td>
      <td>92</td>
      <td>15,833</td>
      <td>85</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | F9m</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,069</td>
      <td>95</td>
      <td>16,063</td>
      <td>90</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,840</td>
      <td>92</td>
      <td>15,830</td>
      <td>81</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <td rowspan="2">U70 | F18m</td>
      <td>CRCSPIN</td>
      <td>15,973</td>
      <td>16,069</td>
      <td>95</td>
      <td>16,058</td>
      <td>84</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,748</td>
      <td>15,840</td>
      <td>92</td>
      <td>15,824</td>
      <td>76</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | C3m</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,968</td>
      <td>285</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,590</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,823</td>
      <td>234</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | C9m</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,968</td>
      <td>285</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,590</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,823</td>
      <td>233</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | C18m</td>
      <td>CRCSPIN</td>
      <td>15,684</td>
      <td>15,969</td>
      <td>285</td>
      <td>15,968</td>
      <td>285</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,589</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,822</td>
      <td>233</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | C@75</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,968</td>
      <td>285</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,590</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,819</td>
      <td>229</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | F3m</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,964</td>
      <td>281</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,590</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,818</td>
      <td>228</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | F9m</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,964</td>
      <td>281</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,590</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,817</td>
      <td>228</td>
      <td>7</td>
      <td>3</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | F18m</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,964</td>
      <td>281</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,589</td>
      <td>15,824</td>
      <td>234</td>
      <td>15,817</td>
      <td>227</td>
      <td>7</td>
      <td>3</td>
    </tr>
    <tr>
      <td rowspan="2">C70 | U</td>
      <td>CRCSPIN</td>
      <td>15,683</td>
      <td>15,968</td>
      <td>285</td>
      <td>15,930</td>
      <td>247</td>
      <td>38</td>
      <td>13</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,581</td>
      <td>15,815</td>
      <td>234</td>
      <td>15,726</td>
      <td>146</td>
      <td>89</td>
      <td>38</td>
    </tr>
    <tr>
      <td rowspan="2">F70 | F3m</td>
      <td>CRCSPIN</td>
      <td>15,764</td>
      <td>16,024</td>
      <td>259</td>
      <td>16,023</td>
      <td>259</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,676</td>
      <td>15,902</td>
      <td>226</td>
      <td>15,902</td>
      <td>226</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">F70 | F9m</td>
      <td>CRCSPIN</td>
      <td>15,765</td>
      <td>16,024</td>
      <td>259</td>
      <td>16,023</td>
      <td>259</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,677</td>
      <td>15,903</td>
      <td>226</td>
      <td>15,903</td>
      <td>225</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">F70 | F18m</td>
      <td>CRCSPIN</td>
      <td>15,766</td>
      <td>16,025</td>
      <td>259</td>
      <td>16,024</td>
      <td>258</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,677</td>
      <td>15,903</td>
      <td>226</td>
      <td>15,903</td>
      <td>226</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">F70 | U</td>
      <td>CRCSPIN</td>
      <td>15,764</td>
      <td>16,024</td>
      <td>259</td>
      <td>15,990</td>
      <td>226</td>
      <td>33</td>
      <td>13</td>
    </tr>
    <tr>
      <td>MISCAN</td>
      <td>15,677</td>
      <td>15,903</td>
      <td>226</td>
      <td>15,873</td>
      <td>196</td>
      <td>30</td>
      <td>13</td>
    </tr>
  </tbody>
</table>

_Notes: Outcomes calculated over the lifetime of a cohort of 1000 average-risk, CRC-free individuals with age at pandemic defined in the scenario description. The scenario column describes colorectal cancer screening disruption scenarios, as presented in Table 1. Life-years (LY) and Life-years gained (LYG) are computed over the remaining lifespan of individuals starting at the beginning of 2020. All values refer to cohort-level estimates – that is, the expected LY of an average-risk person. This table presents results assuming high colonoscopy sensitivity. Supplementary file 1 presents additional results for the low colonoscopy sensitivity scenario, and Supplementary files 2 and 3 present CRC cases and deaths outcomes._

Similarly, 60-year-olds are expected to incur a substantial reduction in the benefit of screening if screening is discontinued after the pandemic. Those who started screening at age 50 and stopped after the pandemic are expected to lose 106–124 or 92–111 LY per 1000 individuals if pursuing a colonoscopy (C60 | U) or a FIT (F60 | U) screening regimen, respectively. Those who were semi-adherent to FIT screening before the pandemic and discontinued screening (f60 | U) lose even more LY – from 143 to 149 LY per 1000 individuals, or 58–69% of the benefit of screening. Similarly, unscreened 60-year-olds who start screening at age 65 (scenario U60 | C@65) are predicted to lose 42–45 LY per 1000 individuals compared to a scenario where they would have begun screening at age 60 – a 20–22% loss in LYG from screening due to this disruption.

Switching the screening regimen from colonoscopy to FIT and short-term delays will cause only a modest reduction in the benefit of screening. For the 60-year-old cohort, switching from colonoscopy to annual FIT after the pandemic with an 18-month delay is expected to result in a loss of 9–11 LY per 1000 individuals, a 3–4% loss relative to a scenario with no change in screening regimen and no delays. Similarly, short-term delays are predicted to cause minimal decreases in the benefits of the screening program. A 3-month delay in colonoscopy screening results in a loss of 0–2 LY per 1000 individuals for the 60-year cohort (scenarios C60 | C3m), whereas a 9- or 18-month delay (C60 | C9m and C60 | C18m) is expected to result in a loss of 0–2 or 0–3 LY per 1000 individuals, respectively. The worst-case scenario of an 18-month pause starting in March 2020 (scenario C60 | C18m) resulted in a 0–1% loss of the benefit of screening.

Seventy-year-olds lose fewer LY due to screening disruptions but can still be affected by the pandemic as they are at greater risk for CRC than younger age groups. When discontinuing screening after the pandemic, 70-year-olds are expected to lose 38–87 or 29–33 LY per 1000 individuals due to the pandemic if pursuing a colonoscopy (C70 | U) or FIT (F70 | U) screening regimen, respectively. Unscreened 70-year-olds who only come back to screening at age 75 (scenario U70 | C@75) are expected to lose 49–50 LY per 1000 individuals, a 39–43% reduction in LYG relative to a scenario where they would have received colonoscopy screening at age 70.

Seventy-year-olds who were up-to-date with their screening and experienced short-term delays of up to 18 months can expect minimal loss of LY due to pandemic-induced CRC screening disruptions, even if they switch to FIT after the pandemic. Those who transitioned from colonoscopy to FIT screening at age 70 can expect a reduction of 5–7 LY per 1000 individuals even if a return to FIT screening was delayed by 18 months (scenario C70 | F18m). This reduction in benefit represents a 2–3% reduction in LYG of colonoscopy-only screening.

### Low-sensitivity scenarios

While colonoscopy sensitivity affects the overall benefit of screening, conditional on colonoscopy sensitivity, the loss of LY due to pandemic-induced scenarios is similar across sensitivity levels. Figure 2 compares LYG and LYL for high- and low-sensitivity scenarios. High-sensitivity scenarios are expected to yield higher LYG benefits than low-sensitivity scenarios, and the magnitude of this difference is higher for more intensive screening regimens. For 60-year-olds with a prior colonoscopy at age 50 who experience an 18-month delay during the pandemic (scenario C60 | C 18m), the benefit of screening is 240–297 LYG per 1000 individuals under a high colonoscopy sensitivity scenario, whereas it is 217–272 under a low colonoscopy sensitivity scenario.

![Figure 2.](https://cdn.elifesciences.org/articles/85264/elife-85264-fig2-v1.jpg)

**Figure 2.:** Notes: Each dot represents one scenario considered in this study. The horizontal axis displays the number of LYG estimated in that scenario under a high colonoscopy sensitivity scenario. The vertical axis shows the results for the same cohort under a low colonoscopy sensitivity scenario. If sensitivity did not affect the estimate, then all points would be on top of a 45-degree line. Different colors represent CRCSPIN and MISCAN models.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/85264/elife-85264-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Notes: Each dot represents one scenario considered in this study. The horizontal axis displays the number of life-years lost due to disruptions (LYL) estimated in that scenario under a high colonoscopy sensitivity scenario. The vertical axis shows the results for the same cohort under a low colonoscopy sensitivity scenario. If sensitivity did not affect the estimate, then all points would be on top of a 45-degree line. Different colors represent CRCSPIN and MISCAN models.

Nevertheless, conditional on the sensitivity scenario, the effect of pandemic disruptions on LY lost is expected to be very similar for low-sensitivity scenarios. An 18-month delay in colonoscopy screening is expected to result in a loss of 0–3 LY per 1000 individuals for 60-year-olds assuming high sensitivity, whereas it is expected to result in a loss of 0–4 LY per 1000 individuals assuming low sensitivity.

## Discussion

Model-based screening cost-effectiveness analyses present estimates under guideline-concordant scenarios, but there are many reasons why real-world screening will not follow guidelines. Chief among them in 2020, the COVID-19 pandemic severely disrupted screening. Under those conditions, disparities in health outcomes can arise if disruptions are unevenly distributed in the population.

Our results suggest that the COVID-19 pandemic will have an uneven effect on CRC outcomes depending on whether and how fast screening is resumed after the pandemic onset. Consider three cohorts with the same pre-pandemic screening regimen and behavior: 60-year-olds with a prior colonoscopy at age 50. Cohorts that experience short-term disruptions (e.g. 3–18 months) only experience a small loss of life due to short-term delays – up to 3 LY per 1000 individuals. Those who switch from colonoscopy to FIT screening are projected to experience a greater loss of life – from 9 to 11 to LY per 1000 individuals. If screening is only resumed at age 65 (e.g. age at Medicare enrollment) or abandoned, the loss of benefits from screening could be 3–11 LY per 1000 individuals (scenario C60 | C@65). Lastly, discontinuing screening after the pandemic is projected to cause a loss of 106–124 LY per 1000 individuals, a decrease of 36–51% in the benefit of screening (scenario C60 | U). These results imply that the pandemic will become a disparity-widening mechanism if it differentially affects screening access and/or behavior across different population groups. These results also show that the pandemic is unlikely to substantially affect those whose screening is only interrupted momentarily.

These results highlight the potential implications of disruptions to preventative care due to loss of insurance following the pandemic. According to data from the Bureau of Labor Statistics Current Population Survey, more dramatic declines in the number employed during the COVID-19 pandemic were seen in Black, Asian American, and Hispanic groups (Gemelas et al., 2022). Moreover, data from the US Census Household Pulse Survey suggests that Black and Hispanic workers were not only more likely to be unemployed but were also more likely to be without unemployment insurance (Mar et al., 2022). These results provide important clinical insight on the projected impact of these populations which may guide future policy on the aftereffects of the pandemic. Those who were previously uninsured for long periods of time throughout the pandemic should resume CRC screening to mitigate the long-term effects projected in these simulations.

These results also add to the growing evidence of the implications of delayed CRC care following the COVID-19 pandemic. A microsimulation study based on a Canadian population explored scenarios of differing screening delays and transition periods due to attenuated screening volumes and found that a 6-month delay in primary screening could increase CRC incidence by 2200 cases and 960 more cancer deaths over a lifetime (Yong et al., 2021). A microsimulation paper based on a Chilean population illustrated similar results with respect to CRC incidence and mortality due to the screening backlog and strained patient care during the pandemic (Ward et al., 2021). Our results mirror these conclusions and provide new scenarios which consider the aftereffects of loss of healthcare insurance due to disparities magnified by the COVID-19 pandemic.

### Limitations

This analysis presents a series of limitations. First, we do not present population-level estimates of reductions in benefits. While doing so could prove helpful, one would have to estimate how many people will be screened following each scenario we modeled. That would require individual-level data describing the distribution of delays and screening regimen switching in the population after the pandemic, which will not be available for many years. Instead of pursuing a population-level study, we conditioned our estimates on a discrete set of pre-specified disruption scenarios. This approach makes our study feasible but prevents us from making population-level predictions. Moreover, our approach does not account for potential correlation between risk factors and disruptions – we only provide estimates using models calibrated to represent cohorts with average risk.

Second, the scenarios presented in this analysis represent only a subset of the real-world changes in screening due to the pandemic. Even in the absence of a pandemic, individuals may switch from colonoscopy to FIT, and return to colonoscopy screening. To keep this analysis tractable, we restrict the variations considered in this paper to one switch from colonoscopy to FIT. Further, we only consider changes in screening regimens immediately following the COVID-19 pandemic. Third, this analysis only considers uncertainty stemming from structural differences between models and two scenarios of test characteristics and does not evaluate parameter or sampling uncertainty. Our estimates represent the expected value of estimates conditional on scenarios across an average-risk cohort drawn from the general US population.

Finally, this paper identifies the effect of disruptions on the effectiveness of screening interventions but does not explicitly identify policy interventions or prioritization rules to amend those inequities. Future research could use extended cost-effectiveness analysis to evaluate CRC screening interventions in the context of healthcare disparities (Asaria et al., 2016; Richard et al., 2020).

### Conclusion

This study quantified the potential effect of disruptions to colonoscopy screening and demonstrated that unequal recovery of CRC screening following the pandemic will predictably widen disparities in CRC outcomes. The COVID-19 pandemic will severely reduce the benefits of CRC screening if it causes screening discontinuation or long-term (e.g. 5 year) delays. Short-term delays of 3–18 months and regime switching from colonoscopy to FIT are not expected to have significant consequences.
