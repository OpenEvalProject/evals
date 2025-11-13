# Augmented curation of clinical notes from a massive EHR system reveals symptoms of impending COVID-19 diagnosis

## Authors

- Tyler Wagner<sup>1</sup>
- FNU Shweta<sup>2</sup> ([ORCID: 0000-0001-6634-6272](https://orcid.org/0000-0001-6634-6272))
- Karthik Murugadoss<sup>1</sup>
- Samir Awasthi<sup>1</sup>
- AJ Venkatakrishnan<sup>1</sup> ([ORCID: 0000-0003-2819-3214](https://orcid.org/0000-0003-2819-3214))
- Sairam Bade<sup>3</sup>
- Arjun Puranik<sup>1</sup>
- Martin Kang<sup>1</sup>
- Brian W Pickering<sup>2</sup>
- John C O'Horo<sup>2</sup>
- Philippe R Bauer<sup>2</sup>
- Raymund R Razonable<sup>2</sup>
- Paschalis Vergidis<sup>2</sup>
- Zelalem Temesgen<sup>2</sup>
- Stacey Rizza<sup>2</sup>
- Maryam Mahmood<sup>2</sup>
- Walter R Wilson<sup>2</sup>
- Douglas Challener<sup>2</sup> ([ORCID: 0000-0002-6964-9639](https://orcid.org/0000-0002-6964-9639))
- Praveen Anand<sup>3</sup> ([ORCID: 0000-0002-2478-7042](https://orcid.org/0000-0002-2478-7042))
- Matt Liebers<sup>1</sup>
- Zainab Doctor<sup>1</sup>
- Eli Silvert<sup>1</sup>
- Hugo Solomon<sup>1</sup>
- Akash Anand<sup>3</sup>
- Rakesh Barve<sup>3</sup>
- Gregory Gores<sup>2</sup>
- Amy W Williams<sup>2</sup>
- William G Morice<sup>2</sup>
- John Halamka<sup>2</sup>
- Andrew Badley<sup>2</sup> †
- Venky Soundararajan<sup>1</sup> ([ORCID: 0000-0001-7434-9211](https://orcid.org/0000-0001-7434-9211)) †

### Affiliations

1. nference Cambridge United States
2. Mayo Clinic Rochester United States
3. nference Labs Bangalore India
4. Mayo Clinic Laboratories Rochester United States

† Corresponding author

## Abstract

Understanding temporal dynamics of COVID-19 symptoms could provide fine-grained resolution to guide clinical decision-making. Here, we use deep neural networks over an institution-wide platform for the augmented curation of clinical notes from 77,167 patients subjected to COVID-19 PCR testing. By contrasting Electronic Health Record (EHR)-derived symptoms of COVID-19-positive (COVIDpos; n = 2,317) versus COVID-19-negative (COVIDneg; n = 74,850) patients for the week preceding the PCR testing date, we identify anosmia/dysgeusia (27.1-fold), fever/chills (2.6-fold), respiratory difficulty (2.2-fold), cough (2.2-fold), myalgia/arthralgia (2-fold), and diarrhea (1.4-fold) as significantly amplified in COVIDpos over COVIDneg patients. The combination of cough and fever/chills has 4.2-fold amplification in COVIDpos patients during the week prior to PCR testing, in addition to anosmia/dysgeusia, constitutes the earliest EHR-derived signature of COVID-19. This study introduces an Augmented Intelligence platform for the real-time synthesis of institutional biomedical knowledge. The platform holds tremendous potential for scaling up curation throughput, thus enabling EHR-powered early disease diagnosis.

## Introduction

As of June 3, 2020, according to WHO there have been more than 6.3 million confirmed cases worldwide and more than 379,941 deaths attributable to COVID-19 (https://covid19.who.int/). The clinical course and prognosis of patients with COVID-19 varies substantially, even among patients with similar age and comorbidities. Following exposure and initial infection with SARS-CoV-2, likely through the upper respiratory tract, patients can remain asymptomatic with active viral replication for days before symptoms manifest (Guan et al., 2020; Gandhi et al., 2020; Verity et al., 2020). The asymptomatic nature of initial SARS-CoV-2 infection patients may be exacerbating the rampant community transmission observed (Hoehl et al., 2020). It remains unknown why certain patients become symptomatic, and in those that do, the timeline of symptoms remains poorly characterized and non-specific. Symptoms may include fever, fatigue, myalgias, loss of appetite, loss of smell (anosmia), and altered sense of taste, in addition to the respiratory symptoms of dry cough, dyspnea, sore throat, and rhinorrhea, as well as gastrointestinal symptoms of diarrhea, nausea, and abdominal discomfort (Xiao et al., 2020). A small proportion of COVID-19 patients progress to severe illness, requiring hospitalization or intensive care management; among these individuals, mortality due to Acute Respiratory Distress Syndrome (ARDS) is higher (Zhang et al., 2020). The estimated average time from symptom onset to resolution can range from three days to more than three weeks, with a high degree of variability (Bi et al., 2020). The COVID-19 public health crisis demands a data science-driven approach to quantify the temporal dynamics of COVID-19 pathophysiology. However, for this there is a need to overcome challenges associated with manual curation of unstructured EHRs in a clinical context (Argenziano et al., 2020) and self-reporting outside of the clinical settings via questionnaires (Menni et al., 2020).

Here we introduce a platform for the augmented curation of the full-spectrum of patient symptoms from the Mayo Clinic EHRs for 77,167 patients with positive/negative COVID-19 diagnosis by PCR testing (see Materials and methods). The platform utilizes state-of-the-art transformer neural networks on the unstructured clinical notes to automate entity recognition (e.g. diseases, symptoms), quantify the strength of contextual associations between entities, and characterize the nature of association into ‘positive’, ‘negative’, ‘suspected’, or ‘other’ sentiments. We identify specific sensory, respiratory, and gastro-intestinal symptoms, as well as some specific combinations, that appear to be indicative of impending COVIDpos diagnosis by PCR testing. This highlights the potential for neural network-powered EHR curation to facilitate a significantly earlier diagnosis of COVID-19 than currently feasible.

## Results

The clinical determination of the COVID-19 status for each patient was conducted using the SARS-CoV-2 PCR (RNA) test approved for human nasopharyngeal and oropharyngeal swab specimens under the U.S. FDA emergency use authorization (EUA) (Mayo Clinic Laboratories, 2019). This PCR test resulted in 74,850 COVIDneg patient diagnoses and 2,317 COVIDpos patient diagnoses. The COVIDpos cohort had a mean age of 41.9 years (standard deviation = 19.1 years) and was 51% male and 49% female while the COVIDneg cohort had a mean age of 50.7 years (standard deviation = 21.4 years) and was 43% male and 57% female. Only 11 (0.5%) of COVIDpos and 196 (0.3%) of COVIDneg patients were hospitalized 7 days or more prior to PCR testing, indicating that the vast majority of patients were not experiencing serious illness prior to this time window. During the week prior to PCR testing, 135 (5.8%) of the COVIDpos and 5981 (8.0%) of the COVIDneg patients were hospitalized. Additionally, the frequencies of ICD10 diagnosis codes for these cohorts were found for the week prior to PCR testing, with unspecified acute upper respiratory infection appearing in over 20% of both cohorts (Supplementary file 1a-b). In order to investigate the time course of COVID-19 progression in patients and better define the presence or absence of symptoms, we used BERT-based deep neural networks to extract symptoms and their putative synonyms from the clinical notes for the week prior to the date when the COVID-19 diagnosis test was taken (see Materials and methods; Table 1). For the purpose of this analysis, all patients were temporally aligned, by setting the date of COVID-19 PCR testing to ‘day 0’, and the proportion of patients demonstrating each symptom derived from the EHR over each day of the week preceding testing was tabulated (Table 2). As a negative control, we included a non-COVID-19 symptom ‘dysuria’.

**Table 1.**
 Augmented curation of the unstructured clinical notes from the EHR reveals specific clinically confirmed phenotypes that are amplified in COVIDpos patients over COVIDneg patients in the week prior to the SARS-CoV-2 PCR testing date.The key COVIDpos amplified symptoms in the week preceding PCR testing (i.e. day = −7 to day = −1) are highlighted in gray (p-value<1E-10). The ratio of COVIDpos to COVIDneg proportions represents the fold change amplification of each phenotype in the COVIDpos patient set (symptoms are sorted based on this column).


<table>
  <thead>
    <tr>
      <th>Symptom (p-value&lt;1E-10 in gray)</th>
      <th>COVID+ Count (%) (N = 2317)</th>
      <th>COVID- Count (%) (N = 74850)</th>
      <th>(COVID+/COVID-) Relative Ratio</th>
      <th>Relative ratio (95% CI)</th>
      <th>2-tailed p-value</th>
      <th>BH-corrected p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Altered or diminished sense of taste or smell</td>
      <td>145 (6.3%)</td>
      <td>173 (0.2%)</td>
      <td>27.08</td>
      <td>(21.81, 33.62)</td>
      <td>&lt;1E-300</td>
      <td>&lt;1E-300</td>
    </tr>
    <tr>
      <td>Fever/chills</td>
      <td>750 (32.4%)</td>
      <td>9421 (12.6%)</td>
      <td>2.57</td>
      <td>(2.42, 2.74)</td>
      <td>3.57E-169</td>
      <td>4.64E-168</td>
    </tr>
    <tr>
      <td>Cough</td>
      <td>769 (33.2%)</td>
      <td>11083 (14.8%)</td>
      <td>2.24</td>
      <td>(2.11, 2.38)</td>
      <td>4.60E-129</td>
      <td>3.99E-128</td>
    </tr>
    <tr>
      <td>Respiratory difficulty</td>
      <td>681 (29.4%)</td>
      <td>10082 (13.5%)</td>
      <td>2.18</td>
      <td>(2.04, 2.33)</td>
      <td>3.06E-105</td>
      <td>1.99E-104</td>
    </tr>
    <tr>
      <td>Myalgia/Arthralgia</td>
      <td>288 (12.4%)</td>
      <td>4620 (6.2%)</td>
      <td>2.01</td>
      <td>(1.8, 2.25)</td>
      <td>5.35E-34</td>
      <td>2.78E-33</td>
    </tr>
    <tr>
      <td>Rhinitis</td>
      <td>200 (8.6%)</td>
      <td>2947 (3.9%)</td>
      <td>2.19</td>
      <td>(1.92, 2.52)</td>
      <td>2.25E-29</td>
      <td>9.75E-29</td>
    </tr>
    <tr>
      <td>Headache</td>
      <td>325 (14.0%)</td>
      <td>6124 (8.2%)</td>
      <td>1.71</td>
      <td>(1.55, 1.9)</td>
      <td>1.34E-23</td>
      <td>4.98E-23</td>
    </tr>
    <tr>
      <td>Congestion</td>
      <td>228 (9.8%)</td>
      <td>4261 (5.7%)</td>
      <td>1.73</td>
      <td>(1.53, 1.96)</td>
      <td>4.45E-17</td>
      <td>1.45E-16</td>
    </tr>
    <tr>
      <td>GI upset</td>
      <td>195 (8.4%)</td>
      <td>10670 (14.3%)</td>
      <td>0.59</td>
      <td>(0.52, 0.68)</td>
      <td>1.74E-15</td>
      <td>5.03E-15</td>
    </tr>
    <tr>
      <td>Wheezing</td>
      <td>49 (2.1%)</td>
      <td>3765 (5.0%)</td>
      <td>0.42</td>
      <td>(0.32, 0.56)</td>
      <td>1.82E-10</td>
      <td>4.73E-10</td>
    </tr>
    <tr>
      <td>Dermatitis</td>
      <td>26 (1.1%)</td>
      <td>2519 (3.4%)</td>
      <td>0.33</td>
      <td>(0.23, 0.5)</td>
      <td>2.60E-09</td>
      <td>6.15E-09</td>
    </tr>
    <tr>
      <td>Generalized symptoms</td>
      <td>169 (7.3%)</td>
      <td>8129 (10.9%)</td>
      <td>0.67</td>
      <td>(0.58, 0.78)</td>
      <td>4.82E-08</td>
      <td>1.04E-07</td>
    </tr>
    <tr>
      <td>Respiratory Failure</td>
      <td>73 (3.2%)</td>
      <td>1363 (1.8%)</td>
      <td>1.73</td>
      <td>(1.38, 2.19)</td>
      <td>3.09E-06</td>
      <td>6.18E-06</td>
    </tr>
    <tr>
      <td>Diarrhea</td>
      <td>228 (9.8%)</td>
      <td>5452 (7.3%)</td>
      <td>1.35</td>
      <td>(1.19, 1.53)</td>
      <td>3.47E-06</td>
      <td>6.44E-06</td>
    </tr>
    <tr>
      <td>Pharyngitis</td>
      <td>160 (6.9%)</td>
      <td>3635 (4.9%)</td>
      <td>1.42</td>
      <td>(1.22, 1.66)</td>
      <td>7.05E-06</td>
      <td>1.22E-05</td>
    </tr>
    <tr>
      <td>Chest pain/pressure</td>
      <td>148 (6.4%)</td>
      <td>6122 (8.2%)</td>
      <td>0.78</td>
      <td>(0.67, 0.92)</td>
      <td>1.88E-03</td>
      <td>3.06E-03</td>
    </tr>
    <tr>
      <td>Change in appetite/intake</td>
      <td>95 (4.1%)</td>
      <td>2271 (3.0%)</td>
      <td>1.35</td>
      <td>(1.11, 1.66)</td>
      <td>3.37E-03</td>
      <td>5.15E-03</td>
    </tr>
    <tr>
      <td>Otitis</td>
      <td>13 (0.6%)</td>
      <td>874 (1.2%)</td>
      <td>0.48</td>
      <td>(0.29, 0.85)</td>
      <td>6.98E-03</td>
      <td>1.01E-02</td>
    </tr>
    <tr>
      <td>Cardiac</td>
      <td>95 (4.1%)</td>
      <td>2443 (3.3%)</td>
      <td>1.26</td>
      <td>(1.03, 1.54)</td>
      <td>2.62E-02</td>
      <td>3.59E-02</td>
    </tr>
    <tr>
      <td>Fatigue</td>
      <td>229 (9.9%)</td>
      <td>8268 (11.0%)</td>
      <td>0.89</td>
      <td>(0.79, 1.02)</td>
      <td>7.83E-02</td>
      <td>1.02E-01</td>
    </tr>
    <tr>
      <td>Conjunctivitis</td>
      <td>9 (0.4%)</td>
      <td>167 (0.2%)</td>
      <td>1.74</td>
      <td>(0.95, 3.52)</td>
      <td>1.00E-01</td>
      <td>1.24E-01</td>
    </tr>
    <tr>
      <td>Dry mouth</td>
      <td>5 (0.2%)</td>
      <td>316 (0.4%)</td>
      <td>0.51</td>
      <td>(0.24, 1.3)</td>
      <td>1.28E-01</td>
      <td>1.51E-01</td>
    </tr>
    <tr>
      <td>Hemoptysis</td>
      <td>13 (0.6%)</td>
      <td>283 (0.4%)</td>
      <td>1.48</td>
      <td>(0.89, 2.65)</td>
      <td>1.61E-01</td>
      <td>1.78E-01</td>
    </tr>
    <tr>
      <td>Dysuria</td>
      <td>16 (0.7%)</td>
      <td>732 (1.0%)</td>
      <td>0.71</td>
      <td>(0.45, 1.18)</td>
      <td>1.64E-01</td>
      <td>1.78E-01</td>
    </tr>
    <tr>
      <td>Diaphoresis</td>
      <td>35 (1.5%)</td>
      <td>979 (1.3%)</td>
      <td>1.15</td>
      <td>(0.84, 1.63)</td>
      <td>3.99E-01</td>
      <td>4.15E-01</td>
    </tr>
    <tr>
      <td>Neuro</td>
      <td>150 (6.5%)</td>
      <td>4952 (6.6%)</td>
      <td>0.98</td>
      <td>(0.84, 1.15)</td>
      <td>7.86E-01</td>
      <td>7.86E-01</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Temporal analysis of the EHR clinical notes for the week preceding PCR testing (i.e. day −7 to day −1), leading up to the day of PCR testing (day 0) in COVIDpos and COVIDneg patients.Temporal enrichment for each symptom is quantified using the ratio of COVIDpos patient proportion over the COVIDneg patient proportion for each day. The patient proportions in the rows labeled ‘Positive’ and ‘Negative’ represent the fraction of COVIDpos (n = 2,317) and COVIDneg (n = 74,850) patients with the specified symptom on each day. Symptoms with p-value<1E-10 are highlighted in green and 1E-10 < p value<1E-03 in gray.


<table>
  <thead>
    <tr>
      <th>Symptom</th>
      <th>COVID-19 (N = 77167)</th>
      <th>Day = −7</th>
      <th>Day = −6</th>
      <th>Day = −5</th>
      <th>Day = −4</th>
      <th>Day = −3</th>
      <th>Day = −2</th>
      <th>Day = −1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Altered or diminished sense of taste or smell</td>
      <td>Positive (n = 2317)</td>
      <td>4.75E-03</td>
      <td>3.88E-03</td>
      <td>3.45E-03</td>
      <td>2.59E-03</td>
      <td>1.73E-03</td>
      <td>0.00E+00</td>
      <td>4.75E-03</td>
    </tr>
    <tr>
      <td>Negative (n = 74850)</td>
      <td>1.07E-04</td>
      <td>4.01E-05</td>
      <td>1.07E-04</td>
      <td>1.07E-04</td>
      <td>9.35E-05</td>
      <td>2.27E-04</td>
      <td>9.75E-04</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>44.42</td>
      <td>96.91</td>
      <td>32.30</td>
      <td>24.23</td>
      <td>18.46</td>
      <td>0.00</td>
      <td>4.87</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>1.14E-44</td>
      <td>2.24E-48</td>
      <td>3.17E-28</td>
      <td>2.35E-18</td>
      <td>8.94E-11</td>
      <td>4.68E-01</td>
      <td>5.85E-08</td>
    </tr>
    <tr>
      <td rowspan="4">Cough</td>
      <td>Positive</td>
      <td>2.55E-02</td>
      <td>2.29E-02</td>
      <td>1.90E-02</td>
      <td>1.64E-02</td>
      <td>1.38E-02</td>
      <td>8.63E-03</td>
      <td>7.94E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>4.88E-03</td>
      <td>5.30E-03</td>
      <td>5.21E-03</td>
      <td>5.33E-03</td>
      <td>5.73E-03</td>
      <td>8.40E-03</td>
      <td>8.71E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>5.22</td>
      <td>4.31</td>
      <td>3.64</td>
      <td>3.08</td>
      <td>2.41</td>
      <td>1.03</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>8.42E-40</td>
      <td>7.44E-28</td>
      <td>2.43E-18</td>
      <td>2.68E-12</td>
      <td>6.68E-07</td>
      <td>9.06E-01</td>
      <td>1.95E-01</td>
    </tr>
    <tr>
      <td rowspan="4">Diarrhea</td>
      <td>Positive</td>
      <td>8.20E-03</td>
      <td>7.77E-03</td>
      <td>6.04E-03</td>
      <td>4.32E-03</td>
      <td>4.75E-03</td>
      <td>2.59E-03</td>
      <td>2.68E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>3.70E-03</td>
      <td>4.26E-03</td>
      <td>4.58E-03</td>
      <td>4.09E-03</td>
      <td>4.58E-03</td>
      <td>5.61E-03</td>
      <td>3.78E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>2.22</td>
      <td>1.82</td>
      <td>1.32</td>
      <td>1.06</td>
      <td>1.04</td>
      <td>0.46</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>5.59E-04</td>
      <td>1.17E-02</td>
      <td>3.08E-01</td>
      <td>8.66E-01</td>
      <td>9.08E-01</td>
      <td>5.32E-02</td>
      <td>5.81E-03</td>
    </tr>
    <tr>
      <td rowspan="4">Fever/chills</td>
      <td>Positive</td>
      <td>2.42E-02</td>
      <td>2.20E-02</td>
      <td>1.94E-02</td>
      <td>1.68E-02</td>
      <td>1.34E-02</td>
      <td>6.47E-03</td>
      <td>7.90E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>3.39E-03</td>
      <td>3.74E-03</td>
      <td>3.90E-03</td>
      <td>4.42E-03</td>
      <td>4.61E-03</td>
      <td>6.77E-03</td>
      <td>7.48E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>7.12</td>
      <td>5.88</td>
      <td>4.98</td>
      <td>3.81</td>
      <td>2.90</td>
      <td>0.96</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>1.15E-54</td>
      <td>4.31E-40</td>
      <td>6.52E-29</td>
      <td>1.64E-17</td>
      <td>2.36E-09</td>
      <td>8.62E-01</td>
      <td>4.52E-01</td>
    </tr>
    <tr>
      <td rowspan="4">Respiratory Difficulty</td>
      <td>Positive</td>
      <td>2.24E-02</td>
      <td>2.11E-02</td>
      <td>1.81E-02</td>
      <td>1.55E-02</td>
      <td>1.25E-02</td>
      <td>8.20E-03</td>
      <td>5.35E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>5.06E-03</td>
      <td>5.70E-03</td>
      <td>5.81E-03</td>
      <td>5.87E-03</td>
      <td>6.16E-03</td>
      <td>8.66E-03</td>
      <td>7.65E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>4.43</td>
      <td>3.71</td>
      <td>3.12</td>
      <td>2.65</td>
      <td>2.03</td>
      <td>0.95</td>
      <td>0.70</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>2.07E-28</td>
      <td>8.72E-21</td>
      <td>9.41E-14</td>
      <td>4.56E-09</td>
      <td>1.48E-04</td>
      <td>8.15E-01</td>
      <td>3.89E-05</td>
    </tr>
    <tr>
      <td rowspan="4">Change in appetite/intake</td>
      <td>Positive</td>
      <td>1.73E-03</td>
      <td>1.73E-03</td>
      <td>1.73E-03</td>
      <td>5.18E-03</td>
      <td>4.32E-03</td>
      <td>5.61E-03</td>
      <td>1.86E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>1.30E-03</td>
      <td>1.36E-03</td>
      <td>1.34E-03</td>
      <td>1.39E-03</td>
      <td>1.40E-03</td>
      <td>1.91E-03</td>
      <td>1.35E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>1.33</td>
      <td>1.27</td>
      <td>1.29</td>
      <td>3.73</td>
      <td>3.08</td>
      <td>2.94</td>
      <td>1.37</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>5.72E-01</td>
      <td>6.42E-01</td>
      <td>6.14E-01</td>
      <td>3.53E-06</td>
      <td>3.43E-04</td>
      <td>9.41E-05</td>
      <td>4.03E-02</td>
    </tr>
    <tr>
      <td rowspan="4">Myalgia/Arthralgia</td>
      <td>Positive</td>
      <td>8.20E-03</td>
      <td>9.06E-03</td>
      <td>7.77E-03</td>
      <td>6.47E-03</td>
      <td>5.61E-03</td>
      <td>2.59E-03</td>
      <td>3.84E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>2.24E-03</td>
      <td>3.05E-03</td>
      <td>3.17E-03</td>
      <td>2.99E-03</td>
      <td>2.87E-03</td>
      <td>3.99E-03</td>
      <td>2.72E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>3.65</td>
      <td>2.98</td>
      <td>2.45</td>
      <td>2.16</td>
      <td>1.95</td>
      <td>0.65</td>
      <td>1.41</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>9.33E-09</td>
      <td>4.91E-07</td>
      <td>1.44E-04</td>
      <td>2.98E-03</td>
      <td>1.68E-02</td>
      <td>2.88E-01</td>
      <td>1.18E-03</td>
    </tr>
    <tr>
      <td rowspan="4">Congestion</td>
      <td>Positive</td>
      <td>6.91E-03</td>
      <td>6.47E-03</td>
      <td>5.18E-03</td>
      <td>3.45E-03</td>
      <td>5.18E-03</td>
      <td>2.16E-03</td>
      <td>1.94E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>1.95E-03</td>
      <td>2.38E-03</td>
      <td>1.98E-03</td>
      <td>2.36E-03</td>
      <td>2.18E-03</td>
      <td>2.95E-03</td>
      <td>2.63E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>3.54</td>
      <td>2.72</td>
      <td>2.62</td>
      <td>1.46</td>
      <td>2.38</td>
      <td>0.73</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>2.87E-07</td>
      <td>1.01E-04</td>
      <td>8.47E-04</td>
      <td>2.92E-01</td>
      <td>2.78E-03</td>
      <td>4.86E-01</td>
      <td>4.07E-02</td>
    </tr>
    <tr>
      <td rowspan="4">Rhinitis</td>
      <td>Positive</td>
      <td>7.77E-03</td>
      <td>6.04E-03</td>
      <td>4.32E-03</td>
      <td>3.02E-03</td>
      <td>2.16E-03</td>
      <td>8.63E-04</td>
      <td>1.38E-02</td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>1.23E-03</td>
      <td>1.42E-03</td>
      <td>1.32E-03</td>
      <td>1.36E-03</td>
      <td>1.38E-03</td>
      <td>2.04E-03</td>
      <td>1.96E-02</td>
    </tr>
    <tr>
      <td>Ratio (Positive/Negative)</td>
      <td>6.32</td>
      <td>4.27</td>
      <td>3.26</td>
      <td>2.22</td>
      <td>1.57</td>
      <td>0.42</td>
      <td>0.70</td>
    </tr>
    <tr>
      <td>p-value</td>
      <td>2.08E-16</td>
      <td>2.61E-08</td>
      <td>1.58E-04</td>
      <td>3.63E-02</td>
      <td>3.21E-01</td>
      <td>2.11E-01</td>
      <td>4.59E-02</td>
    </tr>
  </tbody>
</table>

Altered or diminished sense of taste or smell (dysgeusia or anosmia) is the most significantly amplified signal in COVIDpos over COVIDneg patients in the week preceding PCR testing (Table 1; 27.1-fold amplification; p-value<<1E-100). This result suggests that anosmia and dysgeusia are likely the most salient early indicators of COVID-19 infection, including in otherwise asymptomatic patients. However, it must be noted that the prevalence of a symptom in the population must be taken into consideration. Thus, while anosmia/ dysgeusia see the most dramatic difference in prevalence between the COVIDpos and COVIDneg cohorts, the overall prevalence of 318 out of 77,167 patients, or 0.4%, precludes it from being a standalone predictor of infection. However, with the recent addition of anosmia and dysgeusia to the CDC guidelines (Mayo Clinic Laboratories, 2019) these symptoms will likely be reported more frequently as the pandemic progresses. Alternatively, fever/chills also have an increased signal in the COVIDpos compared to the COVIDneg cohort (2.6-fold amplification; p-value = 3.6E-169) while appearing in 10,171 out of 77,167 patients (13.2%).

Diarrhea is also significantly amplified in the COVIDpos patients for the week preceding PCR testing (Table 1; 1.4-fold; p-value = 3.5E-06). Some of these not yet-diagnosed COVID-19 patients that experience diarrhea prior to PCR testing may be unintentionally shedding SARS-CoV-2 fecally (Xu et al., 2020; Wu, 2020). Incidentally, epidemiological surveillance by waste water monitoring conducted recently in the state of Massachusetts observed SARS-CoV-2 RNA (Xu et al., 2020 Wu, 2020). The amplification of diarrhea in COVIDpos over COVIDneg patients for the week preceding PCR testing raises concern for other modes of viral transmission and highlights the importance of washing hands frequently in addition to wearing respiratory protection.

As may be expected, respiratory difficulty is enriched in the week prior to PCR testing in COVIDpos over COVIDneg patients (1.9-fold amplification; p-value = 1.1E-22; Table 1). Among other common phenotypes with significant enrichments in COVIDpos over COVIDneg patients, cough has a 2.2-fold amplification (p-value = 4.6E-129) and myalgia/arthralgia has a 2.0-fold amplification (p-value = 5.3E-34). Rhinitis is also a potential early signal of COVIDpos patients that requires some consideration (2.2-fold amplification, p-value = 2.25E-29). Finally, dysuria was included as a negative control for COVID-19, and consistent with this assumption, 0.69% of COVIDpos patients and 0.97% of COVIDneg patients had dysuria during the week preceding PCR testing.

Next, we considered the 325 possible pairwise combinations of 26 symptoms (Supplementary file 1c) for COVIDpos versus COVIDneg patients in the week prior to the PCR testing date (Supplementary file 1d). As expected from the previous results, altered sense of smell or taste (anosmia/dysgeusia) dominates in combination with many of the aforementioned symptoms as the most significant combinatorial signature of impending COVIDpos diagnosis (particularly along with cough, respiratory difficulty, and fever/chills). Examining the other 300 possible pairwise symptom combinations, excluding the altered sense of smell of taste, reveals other interesting combinatorial signals. The combination of cough and diarrhea is noted to be significant in COVIDpos over COVIDneg patients during the week preceding PCR testing; that is cough and diarrhea co-occur in 8.0% of COVIDpos patients and only 2.8% of COVIDneg patients, indicating a 2.8-fold amplification of this specific symptom combination (BH corrected p-value = 5.6E-32, Supplementary file 1d).

We further investigated the temporal evolution of the proportion of patients with each symptom for the week prior to PCR testing (Table 2). Altered sense of taste or smell, cough, diarrhea, fever/chills, and respiratory difficulty were found to be significant discriminators of COVIDpos from COVIDneg patients between 4 to 7 days prior to PCR testing. During that time period, cough is significantly amplified (>3 fold, p-value<0.05) in the COVIDpos patient cohort over the COVIDneg patient cohort by 5.2-fold on day −7 (p-value = 8.4E-40), 4.31-fold on day −6(p-value = 7.44E-28), 3.6-fold on day −5 (p-value = 2.4E-18), and 3.1-fold on day −4 (p-value = 2.7E-12). The diminishing odds of cough as a symptom from 7 to 4 days preceding the PCR testing date is notable and this temporal pattern could potentially suggest that the duration of cough and other symptoms, in addition to their presence or absence, is a useful indicator of infection. Similarly, diarrhea is amplified in the COVIDpos patient cohort over the COVIDneg patient cohort for days furthest preceding from the PCR testing date, with an amplification of 2.2-fold on day −7 (p-value = 5.6E-04) and 1.8-fold on day −6 (p-value = 1.2E-02). Likewise, fever/chills and respiratory difficulty both show matching trends, with significant amplification in the COVIDpos cohort on days −7 to −4 and days −7 to −5, respectively. However, unlike diarrhea, cough, fever/chills, and respiratory difficulty, we find that change in appetite may be considered a subsequent symptom of impending COVID-19 diagnosis, with significant amplification in the COVIDpos cohort over the COVIDneg cohort on day −4 (3.7-fold, p-value = 3.53E-06), day −3 (3.1-fold, p-value = 3.4E-04), and day −2 (2.9-fold, p-value = 9.4E-05). The delay in the onset of change in appetite/intake compared to the other aforementioned symptoms indicates that this change only appears after other symptoms have already manifested and thus could be secondary to these symptoms rather than directly caused by infection.

This high-resolution temporal overview of the EHR-derived clinical symptoms as they manifest prior to the SARS-CoV-2 PCR diagnostic testing date for 77,167 patients has revealed specific enriched signals of impending COVID-19 onset. These clinical insights can help modulate social distancing measures and appropriate clinical care for individuals exhibiting the specific sensory (anosmia, dysgeusia), respiratory (cough, difficulty breathing), gastro-intestinal (diarrhea, change in appetite/intake), and other (fever/chills, arthralgia/myalgia) symptoms identified herein, including for patients awaiting conclusive COVID-19 diagnostic testing results (e.g. by SARS-CoV-2 RNA RT-PCR).

## Discussion

While PCR testing is the current diagnostic standard of COVID-19, identifying risk of a positive diagnosis earlier is essential to mitigate the spread of the virus. Patients with these symptom risk factors could be tested earlier, undergo closer monitoring, and be adequately quarantined to not only ensure better treatment for the patient, but to prevent the infection of others. Additionally, as businesses begin to reopen, understanding these risk factors will be critical in areas where comprehensive PCR testing is not possible. This study demonstrates how such symptoms can be extracted from highly unstructured institutional knowledge and synthesized using deep learning and neural networks (Devlin et al., 2019). Such augmented curation, providing fine-grained, temporal resolution of symptoms, can be applied toward supporting differential diagnosis of patients in a clinical setting. Expanding beyond one institution’s COVID-19 diagnostic testing and clinical care to the EHR databases of other academic medical centers and health systems will provide a more holistic view of clinical symptoms enriched in COVIDpos over COVIDneg patients in the days preceding confirmed diagnostic testing. This requires leveraging a privacy-preserving, federated software architecture that enables each medical center to retain the span of control of their de-identified EHR databases, while enabling the machine learning models from partners to be deployed in their secure cloud infrastructure. To this end, seamless multi-institute collaborations over an Augmented Intelligence platform, which puts patient privacy and HIPAA-compliance first, are being advanced actively over the Mayo Clinic’s Clinical Data Analytics Platform Initiative (CDAP). The capabilities demonstrated in this study for rapidly synthesizing unstructured clinical notes to develop an EHR-powered clinical diagnosis framework will be further strengthened through such a universal biomedical research platform.

There are a few caveats that must be considered when relying solely on EHR inference to track symptoms preceding the PCR testing date. In addition to concerns regarding testing accuracy, there is an inherent delay in PCR testing, which arises because both the patient and physician must decide the symptoms warrant PCR testing. More specifically, to be tested, the patient must first consider the symptoms serious enough to visit the clinic and then the physician must determine the symptoms present a possibility of COVID infection. The length of this delay could also be influenced by how well-informed the public is of COVID-19 signs and symptoms, the availability of PCR testing, and the hospital protocols used to determine which patients get tested. Each of these factors would be absent or limited at the beginning of a pandemic but would increase or improve over time. This makes synchronization across patients difficult because the delay between symptom onset and PCR testing changes over time. For example, patients infected early in the pandemic would be less inclined to visit the clinic with mild symptoms, while those infected later have more information and more cause to get tested earlier. Similarly, in the early stages of the COVID-19 pandemic when PCR testing was limited, physicians were forced to reserve tests for more severe cases or for those who were in direct contact with a COVIDpos individual, whereas now PCR testing is more widespread. In each case, the delay between symptom onset and PCR testing would be expected to change over time for a given patient population.

Additionally, there are caveats surrounding data availability when working with such real-world datasets, including data sparsity and reporting. For example, while each patient had at least one clinic visit, accompanied by physician notes, between days −7 and 0, only 6 (0.3%) of the COVIDpos and 372 (0.5%) of the COVIDneg patients had notes from all 7 days prior to PCR testing. Moreover, the number of patients with notes prior to PCR testing tends to decrease with each day prior to the PCR testing date for both cohorts (Supplementary file 1e). With regard to reporting, mild symptoms, particularly those seemingly unrelated to presentation for clinical care, such as anosmia, may go unreported. Finally, it should also be noted that COVIDneg patients may not necessarily be representative of a ‘healthy’ cohort comparable to a randomly selected group from the general population, as these patients each had a reason for seeking out COVID-19 PCR testing. With all of these caveats in mind, the fact that the temporal distribution of symptoms significantly differs between the COVIDpos and COVIDneg patients remains and demonstrates that synchronization using the PCR testing date is apt for the real-world data analysis described herein. Thus, by understanding the temporal progression of symptoms prior to PCR testing, we aim to reduce the delay between infection and testing in the future.

As we continue to understand the diversity of COVID-19 patient outcomes through holistic inference of EHR systems, it is equally important to invest in uncovering the molecular mechanisms (Anand et al., 2020) and gain cellular/tissue-scale pathology insights through large-scale patient-derived biobanking and multi-omics sequencing (Venkatakrishnan et al., 2020). To correlate patterns of molecular expression with EHR-derived symptom signals of COVID-19 disease progression, a large-scale bio-banking system has to be created. Such a system will enable deep molecular insights into COVID-19 to be gleaned and triangulated with SARS-CoV-2 tropism and patient outcomes, allowing researchers to better evaluate disease staging and synchronize patients for analyses similar to those presented here. Ultimately, connecting the dots between the temporal dynamics of COVIDpos and COVIDneg clinical symptoms across diverse patient populations to the multi-omics signals from patient-derived bio-specimen will help advance a more holistic understanding of COVID-19 pathophysiology. This will set the stage for a precision medicine approach to the diagnostic and therapeutic management of COVID-19 patients.

## Materials and methods

### Augmented curation of EHR patient charts

The nferX Augmented Curation technology was leveraged to rapidly curate the charts of SARS-CoV-2-positive (COVIDpos) patients. First, we read through the charts of 100 COVIDpos patients and identified symptoms, grouping them into sets of synonymous words and phrases. For example, ‘SOB’, ‘shortness of breath’, and ‘dyspnea’, among others, were grouped into ‘shortness of breath’. For the SARS-CoV2-positive patients, we identified a total of 26 symptom categories (Supplementary file 1c) with 145 synonyms or synonymous phrases. Together, these synonyms and synonymous phrases capture how symptoms related to COVID-19 are described in the Mayo Clinic Electronic Health Record (EHR) databases.

Next, for charts that had not yet been manually curated, we used state-of-the-art BERT-based neural networks (Devlin et al., 2019) to classify symptoms as being present or not present in each patient based on the surrounding phraseology. More specifically, SciBERT (Beltagy et al., 2019), a BERT model pre-trained on 3.17B tokens from the biomedical and computer science domains, was compared to both domain-adapted BERT architectures (e.g. BioBERT [Lee et al., 2019], ClinicalBioBERT [Alsentzer et al., 2019]) and different transformer architectures (e.g. XLNet [Yang et al., 2019], RoBERTa [Liu et al., 2019a], MT-DNN [Liu et al., 2019b]). We found that SciBERT performed equally or better than these models (Supplementary file 1f and data not shown). SciBERT differs from other domain-adapted BERT architectures as it is trained de novo on a biomedical corpus, whereas BioBERT is initialized with the BERT base vocabulary and fine-tuned with PubMed abstracts and PMC articles. Similarly, Clinical BioBERT is initialized with BioBERT and fine-tuned on MIMIC-III data. When comparing different transformer architectures, SciBERT and RoBERTa had equivalent performance, slightly better than the other models tested, including XLNet and MT-DNN (data not shown). Thus, SciBERT was chosen for the analyses performed, using the architecture and training configuration shown in Figure 1 and Figure 1—figure supplement 1.

![Figure 1.](https://cdn.elifesciences.org/articles/58227/elife-58227-fig1-v3.jpg)

**Figure 1.:** (a) Augmented curation of the unstructured clinical notes from Electronic Health Records (EHRs). (b) COVID-19-related symptom entity recognition, sentiment analysis and grouping of synonyms. (c) Comparison of symptoms extracted from EHR clinical notes of COVIDpos vs. COVIDneg patients.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58227/elife-58227-fig1-figsupp1-v3.jpg)

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/58227/elife-58227-fig1-figsupp2-v3.jpg)

The neural network used to perform this classification was initially trained using 18,490 sentences containing nearly 250 different cardiovascular, pulmonary, and metabolic diseases and phenotypes. Each sentence was manually classified into one of four categories: 'Yes' (confirmed phenotype), 'No' (ruled out phenotype), 'Maybe' (suspected phenotype), and 'Other' (alternate context, e.g. family history of a phenotype, risk of adverse event from medication, etc.), with examples of each classification shown in Figure 1—figure supplement 2. Using a 90%:10% train:test split, the model achieved 93.6% overall accuracy and a precision and recall of 95% or better for both positive and negative sentiment classification (Supplementary file 1g). To augment this model with COVID-related symptoms, 3188 sentences containing 26 different symptoms were added to the 18,490 previously tagged sentences for a total of 21,678. Classification was performed using that same labels and model performance was equivalent to the previous model, with an overall accuracy of 94.0% and a precision and recall of 96% or better for both positive and negative sentiment classification (Supplementary file 1h).

This model was first applied to 35,790,640 clinical notes across the entire medical history of 2,317 COVIDpos patients and 74,850 COVIDneg patients. Each patient is counted only once. Once they have a positive SARS-COV-2 PCR test, they are considered COVIDpos. If a patient were to test negative and then positive subsequently, that day of positive PCR testing is considered day 0 for that patient. We then focus on the notes from seven days prior to the SARS-CoV-2 diagnostic test (Supplementary file 1e). For each patient, the difference between the date on which a particular note was written and the PCR testing date were used to compute the relative date for that note. The PCR testing date was treated as ‘day 0’ with notes preceding it assigned ‘day −1’, ‘day −2’, and so on. BERT-based neural networks were applied on each note to identify the set of symptoms that were present at that time for each patient. This patient-to-symptom mapping over time was then inverted to determine the set of unique patients experiencing each symptom at any given time. Here, the presence of a symptom was defined as either a ‘Yes’ or ‘Maybe’ classification by the model. The ‘Maybe’ classification was included because of differences in how phenotypes/diseases and symptoms are described in the clinical notes. For example, when physicians describe ‘evaluation for’ a phenotype/disease, for example ‘the patient underwent evaluation for COVID-19’, it does not imply a diagnosis for the disease, rather the possibility of a diagnosis. On the other hand, when a patient is seen ‘for evaluation of cough, fever, and chills’, this statement suggests that these symptoms are present. Thus, we included both classifications for the definition of a symptom being present.

To validate the accuracy of the BERT-based model for COVID-related symptoms, a validation step in which the classifications of 4001 such sentences from the timeframe of highest interest (day 0 to day −7) were manually verified. Sentences arising from templates, such as patient education documentation, accounted for 10.2% of sentences identified. These template sentences were excluded from the analysis. The true positive rate, defined as the total number of correct classifications divided by the number of total classifications, achieved by the model for classifying all symptoms was 96.7%; the corresponding false positive rate was 6.1%. The model achieved true positive rates ranging from 93% to 100% for the major symptom categories of Fever/Chills, Cough, Respiratory Difficulty, Headache, Fatigue, Myalgia/Arthralgia, Dysuria, Change in appetite/intake, and Diaphoresis. Classification performance was slightly lower for Altered or diminished sense of taste and smell; here, the true positive rate was 82.2%. Detailed statistics are displayed in Supplementary file 1i.

For each synonymous group of symptoms, we computed the count and proportion of COVIDpos and COVIDneg patients that had positive sentiment for that symptom in at least one note between 1 and 7 days prior to their PCR test. We additionally computed the ratio of those proportions to determine the prevalence of the symptom in the COVIDpos cohort as compared to the COVIDneg cohort; we then computed 95% confidence intervals around these ratios. A standard 2-proportion z hypothesis test was performed, and a p-value was reported for each symptom. A Benjamini-Hochberg adjustment was then applied on these 26-symptom p-values to account for multiple hypotheses. To capture the temporal evolution of symptoms in the COVIDpos and COVIDneg cohorts, the process was repeated considering counts and proportions for each day independently. (note we report un-adjusted p-values only in the temporal analysis). Pairwise analysis of phenotypes was performed by considering 325 symptom pairs from the original set of 26 individual symptoms. For each pair, we calculated the number of patients in the COVIDpos and COVIDneg cohorts wherein both symptoms occurred at least once in the week preceding PCR testing. With these patient proportions, a Fisher exact test p-value was computed. A Benjamini-Hochberg adjustment was applied on these 325 Fisher test p-values to account for multiple hypothesis testing.

This research was conducted under IRB 20–003278, ‘Study of COVID-19 patient characteristics with augmented curation of Electronic Health Records (EHR) to inform strategic and operational decisions’. All analysis of EHRs was performed in the privacy-preserving environment secured and controlled by the Mayo Clinic. nference and the Mayo Clinic subscribe to the basic ethical principles underlying the conduct of research involving human subjects as set forth in the Belmont Report and strictly ensures compliance with the Common Rule in the Code of Federal Regulations (45 CFR 46) on Protection of Human Subjects.
