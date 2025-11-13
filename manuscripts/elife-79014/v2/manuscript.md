# Novel fast pathogen diagnosis method for severe pneumonia patients in the intensive care unit: randomized clinical trial

## Authors

- Yan Wang<sup>1</sup>
- Xiaohui Liang<sup>2</sup> ([ORCID: 0000-0001-8065-8168](https://orcid.org/0000-0001-8065-8168))
- Yuqian Jiang<sup>2</sup>
- Danjiang Dong<sup>1</sup>
- Cong Zhang<sup>2</sup>
- Tianqiang Song<sup>2</sup>
- Ming Chen<sup>1</sup>
- Yong You<sup>1</sup>
- Han Liu<sup>3</sup>
- Min Ge<sup>4</sup>
- Haibin Dai<sup>5</sup>
- Fengchan Xi<sup>6</sup>
- Wanqing Zhou<sup>7</sup>
- Jian-Qun Chen<sup>2</sup>
- Qiang Wang<sup>2</sup> ([ORCID: 0000-0003-2907-9851](https://orcid.org/0000-0003-2907-9851)) †
- Qihan Chen<sup>2</sup> ([ORCID: 0000-0002-0062-8434](https://orcid.org/0000-0002-0062-8434)) †
- Wenkui Yu<sup>1</sup> ([ORCID: 0000-0003-4218-0321](https://orcid.org/0000-0003-4218-0321)) †

### Affiliations

1. Department of Critical Care Medicine, Nanjing Drum Tower Hospital, The Affiliated Hospital of Nanjing University Medical School Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))
2. The State Key Laboratory of Pharmaceutical Biotechnology, School of Life Sciences, Nanjing University Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))
3. Department of Critical Care Medicine, Nanjing First Hospital, Nanjing Medical University Nanjing China ([ROR:059gcgy73](https://ror.org/059gcgy73))
4. Department of Cardiothoracic Surgery Intensive Care Unit, Nanjing Drum Tower Hospital, The Affiliated Hospital of Nanjing University Medical School Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))
5. Department of Neurosurgery Intensive Care Unit, Nanjing Drum Tower Hospital, The Affiliated Hospital of Nanjing University Medical School Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))
6. Research Institute of General Surgery, Affiliated Jinling Hospital, Medical School of Nanjing University Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))
7. Department of Laboratory Medicine, Nanjing Drum Tower Hospital, The Affiliated Hospital of Nanjing University Medical School Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))
8. Medical School of Nanjing University Nanjing China ([ROR:01rxvg760](https://ror.org/01rxvg760))

† Corresponding author

## Abstract

Background:Severe pneumonia is one of the common acute diseases caused by pathogenic microorganism infection, especially by pathogenic bacteria, leading to sepsis with a high morbidity and mortality rate. However, the existing bacteria cultivation method cannot satisfy current clinical needs requiring rapid identification of bacteria strain for antibiotic selection. Therefore, developing a sensitive liquid biopsy system demonstrates the enormous value of detecting pathogenic bacterium species in pneumonia patients.Methods:In this study, we developed a tool named Species-Specific Bacterial Detector (SSBD, pronounce as ‘speed’) for detecting selected bacterium. Newly designed diagnostic tools combining specific DNA-tag screened by our algorithm and CRISPR/Cas12a, which were first tested in the lab to confirm the accuracy, followed by validating its specificity and sensitivity via applying on bronchoalveolar lavage fluid (BALF) from pneumonia patients. In the validation I stage, we compared the SSBD results with traditional cultivation results. In the validation II stage, a randomized and controlled clinical trial was completed at the ICU of Nanjing Drum Tower Hospital to evaluate the benefit SSBD brought to the treatment.Results:In the validation stage I, 77 BALF samples were tested, and SSBD could identify designated organisms in 4 hr with almost 100% sensitivity and over 87% specific rate. In validation stage II, the SSBD results were obtained in 4 hr, leading to better APACHE II scores (p=0.0035, ANOVA test). Based on the results acquired by SSBD, cultivation results could deviate from the real pathogenic situation with polymicrobial infections. In addition, nosocomial infections were found widely in ICU, which should deserve more attention.Conclusions:SSBD was confirmed to be a powerful tool for severe pneumonia diagnosis in ICU with high accuracy.Funding:National Natural Science Foundation of China. The National Key Scientific Instrument and Equipment Development Project. Project number: 81927808.Clinical trial number:This study was registered at https://clinicaltrials.gov/ (NCT04178382).

## Introduction

Sepsis is associated with high morbidity and mortality (Singer et al., 2016). Adequate antibiotic therapy in time could decrease mortality and reduce the length of stay in ICU for patients with sepsis or septic shock (Ferrer et al., 2018; Kumar et al., 2006; Pulia and Redwood, 2020; Seymour et al., 2017). As reported in the previous study, the mortality rate of patients increased approximately 7.6% for every hour delayed (Kumar et al., 2006). Therefore, rapid diagnosis of pathogenic microorganisms is crucial for shortening the time of empirical antibiotic therapy and improving the prognosis of patients with sepsis.

Conventional culture test (CCT) is the most commonly used and golden standard identification method of pathogenic microorganisms in most countries. However, it showed two critical limitations: long time-consuming (2–5 days) and low sensitivity (30–50%), which limited the application of this method in the ICU (Abd El-Aziz et al., 2021; Zhou et al., 2014). To overcome this bottleneck, several new tools were developed and showed significant improvement in time consumption and accuracy. Recently, next-generation sequencing (NGS) technology was applied to acquire the entire information of microorganisms and demonstrated great ability in diagnosing rare pathogens. However, the whole process still needs at least 2 days for the full diagnostic report with high cost (Chen et al., 2020; Wang et al., 2020). On the other hand, NGS provided too much information about microorganisms but only semi-quantification of pathogens, which was hard for most clinical doctors to extract the most important information to determine antibiotic usage. Other new emerging detection techniques designed by BioFire and Curetis are much superior in detection time than these above. However, its original principle was based on nucleotide diversity of conserved genes among species, which could not satisfy the application in the ICU due to potential false-positive results (Edin et al., 2020; Jamal et al., 2014; Trotter et al., 2019). Therefore, a unique diagnosis tool aimed at faster and more accurate pathogen identification in the ICU was still a great challenge.

In this study, we aimed to design a simple and convenient diagnosis tool for sepsis patients in the ICU, which covered the most common pathogenic bacteria and completed the detection process in the shortest possible time with low cost and minimum instrument requirements. A clinical trial with two stages was applied to evaluate the accuracy of the tool and the clinical benefits.

## Materials and methods

### Study design

The full study design was shown in Figure 1. In the discovery stage, we screened species-specific DNA tags of 10 epidemic pathogenic bacteria in the ICU. In the training stage, we optimized reaction conditions and sample preparation process, including detection concentration limitation, DNA purification, and incubation time of the CRISPR/Cas12a reaction. The finalized experiment operating procedure of SSBD was used in the subsequent stages (detailed protocol was shown in Appendix 1).

![Figure 1.](https://cdn.elifesciences.org/articles/79014/elife-79014-fig1-v2.jpg)

**Figure 1.:** This study contained four stages: discovery stage, training stage, validation stage I and validation stage II. All patients were from the Department of Critical Care Medicine, Nanjing Drum Tower Hospital. Patients were randomly divided into two groups for the clinical trial.

In validation stage I, 77 specimens of bronchoalveolar lavage fluid (BALF) directly acquired from patients in ICU were finally detected by SSBD to confirm the specificity and sensitivity of SSBD compared to CCT results. Based on clinical needs, some of the samples were diagnosed by NGS technology in third party commercial company, which provided additional information for reference.

After the stability and accuracy of SSBD were thoroughly evaluated, the validation stage II, a preliminary clinical intervention experiment, was launched to verify the clinical application of SSBD.

### Screening species-specific DNA tags

We designed a process to find the species-specific DNA tags according to the basic principle, intraspecies-conserved and interspecies-specific sequences (illustrated in Figure 2A). A total of 1791 high-quality genomes of 232 microorganism species from the public databases were included in the screening process. To accelerate the screening process, we developed a linear comparison algorithm instead of comparing every two genomes, which could save more than 90% of calculation time cost (Appendix 1—figure 1). According to the epidemiological data by previous retrospective study (Zhou et al., 2014) and 2017 data in ICU of Nanjing Drum Tower Hospital (Appendix 1—figure 2), 10 species of bacteria covered 76% sepsis pathogenic bacteria and therefore were selected as targets for subsequent detecting process, including Acinetobacter baumannii (A. baumannii), Escherichia coli (E. coli), Klebsiella pneumoniae (K. pneumoniae), Pseudomonas aeruginosa (P. aeruginosa), Stenotrophomonas maltophilia (S. maltophilia), Staphylococcus aureus (S. aureus), Staphylococcus epidermidis (S. epidermidis), Staphylococcus capitis (S. capitis), Enterococcus faecalis (E. faecalis) and Enterococcus faecium (E. faecium). Then we designed different DNA primers targeting selected species-specific DNA tags from each species (Appendix 1—tables 1 and 2).

![Figure 2.](https://cdn.elifesciences.org/articles/79014/elife-79014-fig2-v2.jpg)

**Figure 2.:** (A) Schematic diagram of screening species-specific DNA tags. (B) Genomic distribution of species-specific DNA tags in 10 bacteria. (C) Genomic proportion of species-specific DNA tags in 10 bacteria.

To evaluate our primers' specificity in identifying species, we chose S. aureus and S. epidermidis from the same genus as our cross-validated target species. We extracted DNA sequences of the S. aureus and the S. epidermidis amplified by primers used in FilmArray Pneumonia Panel developed by BioFire and in our protocol, which were acquired from NCBI Reference Prokaryotic Representative genomes. We then aligned S. aureus-specific DNA sequences with the representative genome of S. epidermidis using blast to search the most similar DNA sequences. In the FilmArray Pneumonia Panel, DNA amplified sequences from the S. aureus and the S. epidermidis were aligned to each other (two different gene regions, rpoB and gyrB, were used to separate two species).

### Patients

Patients admitted to ICUs and diagnosed with severe pneumonia were recruited from Aug 27, 2019. The recruit criteria for patients were: (1) age ≥18 years; (2) had artificial airway and expected to retain for more than 48 hr; (3) clinically diagnosed as pneumonia, and the microbiology of etiology was unclear; (4) signed informed consent; (5) the expected length of staying in ICU was more than 3 days. According to previous mortality acquired from the adequate anti-infective group, the sample size calculation (two-group rate) for patients was done, and a sample size of 73 patients in each group was needed. The enrolled participants formed a consecutive and convenient series, who were randomly assigned to experimental or control groups as described in the appendix 1.

### Clinical outcomes

BALFs were obtained from all the patients from 2 groups on day 1, day 3–5, and day 7–10 after recruitment and were sent directly to the hospital diagnostic microbiology laboratory for CCT and susceptibility testing. CCT results were obtained in strict accordance with international ERS/ESICM/ESCMID/ALAT guidelines for the management of hospital-acquired pneumonia and ventilator-associated pneumonia, which is currently the guideline for clinical gold standard. BALFs from patients of the experiment group were also sent for SSBD tests immediately after sampling. The time from sample acquisition to feedback of results was defined as the turnaround time, as well as being estimated and compared between SSBD and CCT. Other clinical records included blood routine tests, CRP and PCT examinations.

All enrolled patients received primary empirical antibiotic therapy. Once the SSBD results of the patients in the experiment group were obtained, the decisions about whether antibiotics were adjusted or not were made by two senior doctors according to the SSBD results and other clinical information. While in the control group, adjustment depended on conventional culture results and clinical data. Patient demographics and other vital clinical parameters were recorded. Acute Physiology and Chronic Health Evaluation II (APACHE II) scores and Sequential Organ Failure Assessment (SOFA) scores were calculated and recorded for patients on days 1, 3, 7, 10, and 14 to assess their disease severity and organ function.

### Statistical analysis

The number of improved patients on different clinical indicators of different days was calculated and tested by Fisher’s exact test. APACHE II scores and SOFA scores were tested as a series by two-way ANOVA. Different clinical outcomes were tested by the Mann-Whitney test.

### Funding support

This study was funded by National Natural Science Foundation of China. The National Key Scientific Instrument and Equipment Development Project. Project number: 81927808. The funders were not involved in the initiation or design of this study, collection of samples, analysis and interpretation of data, writing of the paper, or the submission for publication. The study and researchers are independent of the funders.

## Results

### The identification of species-specific DNA fragments

The first step to identify pathogenic bacteria was to figure out the specific genome information of each species. Bacteria were quite similar between close-related species but sometimes quite different among different strains of one species due to fast evolution and horizontal gene transfer (Dombrowski et al., 2020; Brito, 2021; Groussin et al., 2021), which makes it hard to figure out great species-specific DNA fragments. For example, two typical strains PAO1 and PAO7 of P. aeruginosa (NCBI representative genome database) demonstrate less than 94% nucleotide identity, while E. coli and Shigella sonnei both belong to Enterobateriaceae and their representative genomes share more than 98% nucleotide identity. Therefore, the widely used method to identify bacteria with conserved genes may not be a good choice (Maslunka et al., 2015; Liu et al., 2021). We developed an innovative algorithm and designed a workflow to figure out the best DNA tag for each species for diagnostic application based on 1791 microbe genomes from 232 species (Figure 2A). The details could be found in Appendix 1.

We started from 10 common bacteria contributing to sepsis infection as the initial panel according to local epidemic data from ICU of Drum Tower hospital and previous studies about pathogens in ICU (Appendix 1—figure 2; De Pascale et al., 2012; Sakr et al., 2018). To our surprise, bacteria-specific DNA sequences showed a random distribution and turned out to be only 0.3–4.1% in the whole genomes of 10 bacteria (Figure 2B and C). Considering the application scenario of ICU with only basic instruments, PCR +CRISPR/Cas12a system was chosen for the following detection. Based on the identified species-specific DNA fragments, related primers and crRNAs (CRISPR RNA) were designed according to each species (Appendix 1—tables 1 and 2).

### The establishment of species-specific bacteria detection tool

Briefly, CRISPR/Cas12a with designed crRNA could be activated by its target, which could be told by whether the reporter probe was cleaved and demonstrated signal as previously reported (Chen et al., 2018).

To optimize the working conditions of the detection tool in ICU, multiple experiments were applied to optimize the sample preparation and detection process. With the gradient concentration of DNA templates, we confirmed that the lowest detection limit was 10–15 M with PCR amplification and 10–8M without amplification step (Figure 3B), which was consistent with previous studies (Gootenberg et al., 2018). In addition, 30 min’ incubation of CRISPR/Cas12a with PCR products was enough to demonstrate signals (Figure 3B). An additional purification step right after PCR amplification appeared unnecessary to acquire the positive result but helpful for weaker signal (Appendix 1—figure 3A). In addition, the comparison of CRISPR/Cas incubation duration confirmed that fluorescence value showed a significant difference from 5 min and reached its maximum after 30 min compared to the negative control (Appendix 1—figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/79014/elife-79014-fig3-v2.jpg)

**Figure 3.:** (A) SSBD workflow for clinical validation stages. (B) Cas12a and Cas12a-after-PCR detection of different concentrations and reaction times including 30 min (left) and 60 min (right). Blue bars indicated the Cas12a-after-PCR test. Brown bars indicated Cas12a test only. The concentration gradient of pGL3 plasmid from 10–17 M-10–7M was established as the test group. NC stood for the fluorescence values of PCR products of using DEPC-H2O as input. Each group had three repeats. Error bars indicated mean ± SEM of fluorescence value. ** indicated p-value <0.01 and *** indicated p-value <0.001 of unpaired t-test. (C) SSBD results of 10 pathogenic bacteria. Every test panel for each of 10 bacteria was used to detect genome DNA samples of 10 bacteria by SSBD. NC stood for the fluorescence values of PCR products of using DEPC-H2O as input. Each group had three repeats. Error bars indicated mean ± SEM of fluorescence value. *** indicated p-value <0.001 of unpaired t-test.

To confirm the primary behavior of SSBD, two clinical strains separated from different patients for each of 10 selected bacteria species were collected and tested by SSBD as the positive control, which showed clear positive results (Appendix 1—figure 3C). To further confirm the specificity of SSBD, each bacteria strain was tested by 10 SSBD test panels targeting different bacteria. Compared to negative control, only SSBD targeting the tested bacteria showed a positive result, which confirmed its high specificity (Figure 3C).

Putting these results together, a standard operating procedure was finally established for the following validation stages (Figure 3A), which was capable of providing the information about the ten most common pathogenic bacteria in ICU. Since this method was a quite fast and species-specific bacteria detection tool, we named it SSBD.

### The accuracy and clinical benefits of SSBD

We started our study with validation stage I, which was a non-intervention study with 77 samples of BALF extracted from patients. Samples were detected both by SSBD and CCT, and the results were compared (raw detection results were shown in Appendix 1—table 3).

Generally, 5 of 10 selected bacteria were detected by both tests, including A. baumannii, K. pneumoniae, P. aeruginosa, S. aureus, and S. maltophilia. SSBD could detect those five bacteria separately with 100% sensitivity and over 87% specificity, which were calculated by the results of CCT as golden standard (Figure 4A). The other five bacteria were detected by SSBD but not CCT, including E. coli, S. epidermidis, S. capitis, E. faecalis, and E. faecium. Among all samples, 11 of them were determined by patients to acquire results with NGS, which provided extra information to evaluate the results (Appendix 1—table 4). Based on the results, SSBD was highly consistent with NGS, which implied that SSBD might provide more accurate and complete pathogenic information than CCT in the selected panel.

![Figure 4.](https://cdn.elifesciences.org/articles/79014/elife-79014-fig4-v2.jpg)

**Figure 4.:** (A) Cross-tables for 5 of 10 bacteria by both SSBD and CCT in the validation stage I. (B) Cross-tables for 5 of 10 bacteria by both SSBD and CCT in the validation stage II. (C) Antibiotics coverage rate of each test in the two groups. Exp meant the experimental group, and Con meant the control group. Test 1: Day 1. Test 2: Day 3–5. Test 3: Day 7+. Raw antibiotics coverage results of each patient were available in Appendix 1—figure 4B. Detailed judging guidelines were shown in Appendix 1. (D and E) Line charts for APACHE II and SOFA scores, respectively. Error bars indicated mean ± SEM of scores of all the recorded patients. * indicated a significant difference between the two groups using two-way ANOVA.

Based on these accurate results, we started the validation stage II, which was an intervention study aiming to evaluate the clinical benefits of SSBD compared to the current diagnosis and treatment strategy in ICU. Although the study was paused due to the outbreak of SARS-CoV2, 22 patients were recruited into the experiment group and 24 patients into the control group. The baseline characteristics had no significant difference except ages (Table 1).

**Table 1.**
 Demographic and baseline characteristics of the patients in the validation stage II.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Experimental group (n=22)</th>
      <th>Control group(n=24)</th>
      <th>p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Women</td>
      <td>9 (40.9%)</td>
      <td>11 (45.8%)</td>
      <td>0.774</td>
    </tr>
    <tr>
      <td>Men</td>
      <td>13 (59.1%)</td>
      <td>13 (54.2%)</td>
      <td>0.774</td>
    </tr>
    <tr>
      <td>Age, years (SD)</td>
      <td>58 (17.4)</td>
      <td>68 (9.5)</td>
      <td>0.015*</td>
    </tr>
    <tr>
      <td colspan="3">Patients' numbers of chronic comorbidities</td>
      <td></td>
    </tr>
    <tr>
      <td>Hypertension</td>
      <td>9 (40.9%)</td>
      <td>17 (70.8%)</td>
      <td>0.073</td>
    </tr>
    <tr>
      <td>Coronary artery disease</td>
      <td>1 (4.5%)</td>
      <td>3 (12.5%)</td>
      <td>0.609</td>
    </tr>
    <tr>
      <td>Chronic pulmonary disease</td>
      <td>2 (9.1%)</td>
      <td>4 (16.7%)</td>
      <td>0.667</td>
    </tr>
    <tr>
      <td>Chronic kidney disease</td>
      <td>2 (9.1%)</td>
      <td>6 (25.0%)</td>
      <td>0.247</td>
    </tr>
    <tr>
      <td>Diabetes</td>
      <td>5 (22.7%)</td>
      <td>12 (50.0%)</td>
      <td>0.072</td>
    </tr>
    <tr>
      <td>Malignancy</td>
      <td>0 (0.0%)</td>
      <td>2 (8.3%)</td>
      <td>0.490</td>
    </tr>
    <tr>
      <td>Stroke</td>
      <td>3 (13.6%)</td>
      <td>8 (33.3%)</td>
      <td>0.171</td>
    </tr>
    <tr>
      <td>Immunodeficiency/immune suppressive therapy</td>
      <td>5 (22.7%)</td>
      <td>3 (12.5%)</td>
      <td>0.451</td>
    </tr>
    <tr>
      <td>Recent surgery</td>
      <td>4 (18.2%)</td>
      <td>3 (12.5%)</td>
      <td>0.694</td>
    </tr>
    <tr>
      <td>Hemodynamic support (using vasoactive drugs)</td>
      <td>7 (31.8%)</td>
      <td>7 (29.2%)</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>Norepinephrine ≤0.1 μg/(kg•min)</td>
      <td>2</td>
      <td>3</td>
      <td></td>
    </tr>
    <tr>
      <td>Norepinephrine &gt;0.1 μg/(kg•min)</td>
      <td>1</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Dopamine ≤5 μg/(kg•min)</td>
      <td>3</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>Dopamine &gt;5 μg/(kg•min)</td>
      <td>0</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Dobutamine ≤5 μg/(kg•min)</td>
      <td>1</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <td>Dobutamine &gt;5 μg/(kg•min)</td>
      <td>0</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Status at randomization (D1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Temperature, °C</td>
      <td>38.4 (0.6)</td>
      <td>38.3 (0.7)</td>
      <td>0.345</td>
    </tr>
    <tr>
      <td>Coma</td>
      <td>6 (27.3%)</td>
      <td>6 (25.0%)</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>Systolic blood pressure, mmHg</td>
      <td>112.2 (19.3)</td>
      <td>121.6 (17.8)</td>
      <td>0.057</td>
    </tr>
    <tr>
      <td>Invasive mechanical ventilation</td>
      <td>20 (90.9%)</td>
      <td>24 (100.0%)</td>
      <td>0.223</td>
    </tr>
    <tr>
      <td>Renal replacement therapy</td>
      <td>0 (0.0%)</td>
      <td>2 (8.3%)</td>
      <td>0.493</td>
    </tr>
    <tr>
      <td>SOFA score</td>
      <td>6.3 (0.7)</td>
      <td>6.0 (0.5)</td>
      <td>0.935</td>
    </tr>
    <tr>
      <td>APACHE II score</td>
      <td>17.3 (1.6)</td>
      <td>18.9 (1.5)</td>
      <td>0.422</td>
    </tr>
    <tr>
      <td>Albumin, g/L</td>
      <td>32.1 (5.1)</td>
      <td>31.0 (3.7)</td>
      <td>0.442</td>
    </tr>
    <tr>
      <td>Globulin, g/L</td>
      <td>21.8 (3.9)</td>
      <td>23.1 (5.9)</td>
      <td>0.489</td>
    </tr>
    <tr>
      <td>Absolute lymphocyte count, 109 /L</td>
      <td>0.9 (0.7)</td>
      <td>0.7 (0.3)</td>
      <td>0.909</td>
    </tr>
    <tr>
      <td>White blood cells, 109 /L</td>
      <td>11.0 (5.7)</td>
      <td>12.7 (6.3)</td>
      <td>0.210</td>
    </tr>
    <tr>
      <td>CRP, mg/L</td>
      <td>94.7 (101.2)</td>
      <td>108.3 (84.0)</td>
      <td>0.424</td>
    </tr>
  </tbody>
</table>

_SOFA score and APACHE II score are mean (SEM), other data are mean (SD), n (%). Mean (SEM/SD) is compared using Mann-Whitney test, and n (%) is compared using Fisher’s exact test. * indicated p-value <0.05._

We finally got 57 BALF results tested by SSBD, which included 43 results that also had CCT results among them in the experiment group. While in the control group, we got 63 samples tested only by CCT. In the experiment group, 47 samples were positive among 57 samples tested by SSBD, while 28 samples were positive among 43 samples tested by CCT (raw detection results were shown in Appendix 1—table 5). In the control group, 41 samples showed positive among 63 samples. It was shown that SSBD could detect each bacterium with similar high sensitivity and specificity in validation stage II (Figure 4B). Consistent with the local epidemic data, the most frequent occurrence was A. baumannii (Figure 4B). Similar to stage I, 12 samples were determined by patients to test with NGS help us to draw the same conclusion that SSBD seemed to be better that CCT (Appendix 1—table 6).

To explore clinical benefits with the help of SSBD, effective antibiotic coverage rate, APACHE II scores and SOFA scores were calculated and compared to evaluate the rationalization of antibiotic therapy and patients' disease severity and organ function status in the two groups (Figure 4C-E). Effective antibiotic coverage rates for each test were significantly higher in the experimental group than those in the control group in three tests (Figure 4C). The definition of antibiotic coverage and the original calculation results were shown in Appendix 1—figure 4A and B. APACHE II scores were significantly lower in the experimental group than those in the control group after day 1 (p=0.0035, two-way ANOVA); the separation between two groups of patients increased progressively until day 14 (Figure 4D). SOFA scores showed no difference between the groups (p=0.8918, two-way ANOVA) (Figure 4E).

### Polymicrobial infection and nosocomial events observed by SSBD

Based on the previous studies, CCT had defects in the evaluation of polymicrobial infection events due to the limitations of its technology (Azevedo et al., 2017). Therefore, we tried to evaluate whether SSBD demonstrated better performance with polymicrobial infection. Here, we defined situations of infection with more than one pathogenic microorganism as polymicrobial infection events to assess the performance based on the results of both methods. From the results, the detection rate of polymicrobial infection events by SSBD was 41.8% (55/134) in two validation stages, which was significantly higher than 11.7% (14/120) of CCT (Figure 5A). Polymicrobial infection events were compared among SSBD, CCT and NGS, which demonstrated high consistency of SSBD and NGS (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/79014/elife-79014-fig5-v2.jpg)

**Figure 5.:** (A) Statistics of pathogenic infection status of BALF samples in the two validation stages. (B) Verification from NGS results for 6 samples identified as polymicrobial infection by SSBD but not CCT or missed pathogens by CCT. (C) Case study of polymicrobial infection detected by SSBD and CCT. (D) Statistics of pathogens involved in polymicrobial infections in the two stages. (E) Case study of nosocomial infection identified by SSBD. (F) Case study of nosocomial infection identified by CCT. (G) Percentage of nosocomial infection identified by SSBD and CCT.

Since both SSBD and NGS were based on target DNA, we wanted to confirm if some polymicrobial infection events were ‘false positive’ and caused by dead bacteria. Here, we showed patient B19 as an example, who received three times tests at days 1, 3, and 7 by both CCT and SSBD. Based on the results, S. maltophilia was detected as level II in test1 with SSBD but not CCT. Later on, S. maltophilia was detected by CCT in test2 as well with few days’ development from level II to level III based on result of SSBD, which means SSBD discovered the true polymicrobial infection event earlier than CCT (Figure 5C). From the aspect of pathogen species participated in polymicrobial infection events, both methods demonstrated similar results with A. baumannii, S. maltophilia, P. aeruginosa, K. pneumoniae and S. aureus in top 5 (Figure 5D), which were consistent with the frequency of pathogens in ICU (De Pascale et al., 2012).

Hospital infections, also known as nosocomial infections, are an important factor in the incidence rate and mortality of ICU patients with severe pneumonia (Zaragoza et al., 2020). Since CCT has a long delay in clinical feedback of pathogenic results, there is no effective monitoring method in clinical practice. Here, we tried to evaluate nosocomial infections based on the test results. We defined a case as a nosocomial infection event if a pathogenic bacterium was newly detected in the current time point but not before. For example, B17 (K. pneumoniae at test 2, E. faecalis at test 3) and B19 (S. maltophilia at test 2, K. pneumoniae at test 3) patients were discovered as nosocomial infection cases for SSBD and CCT (Figure 5E and F). Based on the results of SSBD, 47.6% (10/21) of patients had nosocomial infections at the test 2, and 28.6% (4/14) of patients had nosocomial infections at the test 3. Similarly, 40% (4/10) of patients were identified as nosocomial infections by CCT at test 2, and 27.3% (3/11) of patients were identified as nosocomial infections at test 3 (Figure 5G).

## Discussion

In this study, we developed a rapid bacteria detection technique based on CRISPR/Cas12a using species-specific DNA tags and detected common bacteria taken from pneumonia in 4 hr with 100% sensitivity and over 87% specificity in the validation stage I. Currently, there are already some market-oriented detection technologies for pneumonia patients, such as FilmArray Pneumonia Panel by BioFire and Curetis Unyvero system, which also could detect microorganisms in several hours (Trotter et al., 2019). However, based on the information in their product instruction, false positive results were widely seen in close relative species. Such problem may due to the marker selection strategy. For example, sequences used by FilmArray Pneumonia Panel from two gene regions had highly similar DNA sequences in the S. epidermidis representative genome (E-value=5e-40, rpoB; E-value=8e-39, gyrB), which could interfere with pathogen identification between species from the same genus. It was ideal for early and rapid screening of infectious diseases but was not applicable in the ICU, considering the complexity and urgency of infection events within the ICU. We have adopted a completely different strategy from the existing methods, getting specific gene regions from species for further test using our developed bioinformatics workflow and algorithm. It was shown that our sequences used for S. aureus diagnosis had no similar fragments in S. epidermidis, which avoided distinguishing different species by gene diversity. It was likely to get the species-specific DNA tags from such amount genomes when aligned bacterial genomes with each other but consuming computational cost. We optimized calculation processes by rescheduling steps and then made it possible for us to acquire species-specific DNA regions after shortening time to a range bearable.

NGS technology is useful in species identification and also shows its advantages in clinical diagnosis. It is valuable to detect uncommon pathogens because of its unique capability in detecting multiple agents across the full microbial spectrum contributing to disease and has already been developed as a new detection platform (Wang et al., 2020). However, in the majority of cases of common pathogens, redundant microorganism results were probably unhelpful to the anti-infection regimen. In addition, the high cost and relatively long turnaround time prevent its widespread application, especially in the ICU circumstance. Therefore, our SSBD method seemed more advantageous in time-consuming and information effectiveness than other mentioned methods, especially when we could quantify bacterial load based on fluorescence intensity for better antibiotic therapy strategy. CRISPR/Cas12a and qPCR are both quantitative methods, but CRISPR/Cas12a shows its robustness and lower equipment requirement, which satisfied our needs for most of the ICU. There are still several challenges in implementing POCT in developing countries, especially the qPCR/POCT system, which will be an alternative. Here, we listed a table to demonstrated the comparison among SSBD, CCT and NGS from main aspects (Appendix 1—table 10).

The results of SSBD demonstrated high sensitivity and specificity. However, we discovered several ‘false positive’ results compared to CCT, which might be caused by two reasons: (1) The low bacterial load of the patient sample was probably not enough or needed much longer time than expected to be cultivated. SSBD provided a lower threshold of detection (10–15 M) than CCT, which could detect pathogens that even existed in trace amounts which unable to be cultivated. In our study, the fluorescence intensity obtained from SSBD was divided into three intervals (level I: 10–15-10–14 M, level II: 10–14 M-10–13 M, level III: over 10–13 M), representing the different strengths of bacteria (roughly equivalent to bacteria amounts according to our lowest detection thresholds, dividing details in SSBD diagnostic report of Appendix 1). All false-positive results were calculated on the count of species and strengths, mostly belonging to the level I or II (Appendix 1—figure 5). Considering most of those false positive samples were also validated by NGS technology, it suggested that some pathogens might be missed in the CCT results. (2) Cultivation could fail in detecting pathogens that failed in competitive growth environments. It was interesting to see that many patients were infected by more than one pathogen, which might cause potential competition between different pathogens in CCT process (Appendix 1—table 9). For example, A. baumannii was found to be the most competitive bacteria in cultivation, which may be due to its fastest growth rate. On the other hand, P. aeruginosa seemed to be relatively the weakest one among them, which was usually concealed in the cultivation with other species existing (sample A16, B19-3, B21-1, B21-2 after we excluded all samples with A. baumannii existing).

When evaluating the clinical benefit from SSBD, the quicker directed therapy adjustment for patients in the experiment group (Exp: 10.2±8.8 hours vs. Con: 96.0±35.1 hr, p<0.0001, Mann-Whitney test) could shorten the empirical anti-infection time and seemed to alleviate illness severity (APACHE II score) during the validation stage II with the help of the SSBD. As showed in Appendix 1—table 8, patients in experiment groups for example demonstrated significant better measures of temperature improvement at day 3, WBC improvement at day 7. It implied that appropriate antibiotic treatment guided by in-time pathogenic information would alleviate acute physiological illness. Nevertheless, at the endpoint, clinical outcomes showed no differences between the two groups, which may due to the insufficient patient numbers.

Despite the size in our intervention stage, there were still some aspects that have not been considered. (1) Resistance genes were not included in the study. Multi-drug resistant organisms (MDROs) prevailed in ICU (Liu et al., 2020; Yang et al., 2020), which might not improve the situation of patients even with accurate pathogenic information. There were a few cases (e.g. B07, B25, and B35 patients) showing no signs of clearing the bacterial infection. (2) The 10 designed pathogens were originated from sepsis, which might not completely overlap with pathogens of severe pneumonia, though pneumonia is one of the most common causes of sepsis. The panel pathogens could be optimized flexibly for meeting diverse clinical needs in the ICU. (3) Other potential pathogenic microbes, such as viruses and fungus, might affect the clinical outcomes considering the complexity of ICU patients.

Previous studies showed that polymicrobial pneumonia is related to an increased risk of inappropriate antimicrobial treatment (Karner et al., 2020). In both phases, a total of 55 samples were identified as polymicrobial infections by SSBD, while only 14 samples were identified as polymicrobial infections by CCT, which suggested that SSBD could provide more precise pathogenic bacteria information than CCT, especially for those patients with polymicrobial infections. On the other hand, nosocomial infections contribute to a considerable proportion of deaths in ICU patients with severe pneumonia (Zaragoza et al., 2020). Although SSBD identified similar ratio of nosocomial infection events with CCT (Figure 5G), SSBD provided more timely information for clinical control and response, which might improve the clinical medication decision in ICU.

As anticipated, SSBD performed well with high sensitivity and specificity in rapid pathogens identification, and it possessed shorter turnover time, which was associated with more rapid administration of appropriate antimicrobial therapy in the experiment cases. SSBD also has enormous potential in expanding pathogens from different diseases with much more pathogen genomes included. We believe that SSBD is an accurate tool with great potential but need to be applied in more clinical research.
