# A four-DNA methylation biomarker is a superior predictor of survival of patients with cutaneous melanoma

## Authors

- Wenna Guo<sup>1</sup>
- Liucun Zhu<sup>2</sup>
- Rui Zhu<sup>2</sup>
- Qihan Chen<sup>1</sup>
- Qiang Wang<sup>1</sup> ([ORCID: 0000-0003-2907-9851](https://orcid.org/0000-0003-2907-9851)) †
- Jian-Qun Chen<sup>1</sup> †

### Affiliations

1. State Key Laboratory of Pharmaceutical Biotechnology, School of Life Sciences Nanjing University Nanjing China
2. School of Life Sciences Shanghai University Shanghai China

† Corresponding author

## Abstract

Cutaneous melanoma (CM) is a life-threatening form of skin cancer. Prognostic biomarkers can reliably stratify patients at initial melanoma diagnosis according to risk, and may inform clinical decisions. Here, we performed a retrospective, cohort-based study analyzing genome-wide DNA methylation of 461 patients with CM from the TCGA database. Cox regression analyses were conducted to establish a four-DNA methylation signature that was significantly associated with the overall survival (OS) of patients with CM, and that was validated in an independent cohort. Corresponding Kaplan–Meier analysis displayed a distinct separation in OS. The ROC analysis confirmed that the predictive signature performed well. Notably, this signature exhibited much higher predictive accuracy in comparison with known biomarkers. This signature was significantly correlated with immune checkpoint blockade (ICB) immunotherapy-related signatures, and may have potential as a guide for measures of responsiveness to ICB immunotherapy.

## Introduction

Cutaneous melanoma (CM) is a malignant neoplasia characterized by rapid progression, metastasis to regional lymph nodes as well as distant organs, and limited responsiveness to therapeutics (MacKie et al., 2009). It contributes to more than 80% death of skin cancer patients (Miller and Mihm, 2006), and its incidence is one of the most rapidly increasing cancers in the United States where it is estimated that there will be 91,270 new cases and 9,320 deaths due to this disease in 2018 (Siegel et al., 2018). Although significant progress has been made in both understanding CM biology and genetics, and in therapeutic approaches, the prognosis remains poor due to the high potential for CM invasion and metastasis. This malignancy still represents a major public health problem worldwide. Primary localized melanoma has a relatively high survival rate. The 5- year survival rate prognosis of patients with lymph node or distant metastases was only 15–20% (Siegel et al., 2018; Weiss et al., 2015). Assessment of patients prior to therapy may aid in the identification of individuals at high risk for recurrence and may guide the development of future targeted treatment strategies. For example, for patients who are at high operative risk, conservative therapy may be helpful in the operative decision-making process. Molecular biomarkers could provide additional prognostic information and insight into the mechanisms of melanoma progression, as well as guide treatment selection. Consequently, new strategies for the identification of effective prognostic biomarkers may improve the clinical management of melanoma by providing more accurate prognostic information.

Aberrant DNA methylation is an epigenetic hallmark of cancer and actively contributes to cancer development and progression by inactivating tumor suppressor genes (Egger et al., 2004). Some characteristics of methylation markers render them particularly attractive for development of clinically applicable biomarkers, including high stability in biologic samples, limited susceptibility to tumor environmental factors, and ease of detection (Keeley et al., 2013). A growing number of studies have demonstrated that aberrant DNA methylation plays important roles in tumorigenesis and progression, and DNA methylation has great potential to act as a biomarker for predicting the prognosis of patients with a variety of malignancies (Egger et al., 2004; Guo et al., 2004; Roh et al., 2016). For instance, GATA4 is epigenetically silenced in gastrointestinal cancers (Akiyama et al., 2003) and lung cancer (Guo et al., 2004); OPCML promoter methylation has been identified as a biomarker for predicting ovarian cancer prognosis (Zhou et al., 2014); PCDH19 methylation is associated with poor hepatocellular carcinoma prognosis (Zhang et al., 2018) and Sigalotti et al. identified a 17-gene methylation signature as a molecular marker of survival in stage IIIC melanoma (Sigalotti et al., 2012). Unfortunately, many recent melanoma studies have several limitations including relatively small sample cohorts, lack of subsequent biomarker validation, narrow focus on patient specimens with specific clinical features, or investigation of only one or a few genes. These studies lack the comprehensive and systematic approach of genome-wide methylation analysis. Because of this, the identified methylation signatures do not have universal prognostic power, and their capability is limited by the specimen type. The Cancer Genome Atlas (TCGA) database (Hudson et al., 2010), a large well-annotated database with nearly 500 CM samples collected worldwide is a helpful resource for developing promising biomarkers with prospective studies into a methylation signature which can be of clinical utility.

Consequently, the purpose of this study was to identify DNA methylation biomarkers so as to explore the utility of DNA methylation analysis for cancer prognosis. The whole genome methylation profiles of tumor tissues from patients with CM in the TCGA database were analyzed, and the potential clinical significance of methylation biomarkers serving as molecular prognostic predictors was examined using the Kaplan–Meier method and receiver operating characteristic (ROC) analyses. Furthermore, the prognostic capacity of the identified methylation biomarker was evaluated with an independent cohort of patients in the Gene Expression Omnibus (GEO) database. Also, we investigated the independence and reproducibility in various clinical groups, as well as the possible role of the methylation biomarker in immune-checkpoint blockade (ICB) immunotherapy.

## Results

### Clinical characteristics of the study populations

The study was conducted on 461 CM patients who are clinically and pathologically diagnosed with CM. Of these patients, 286 (62.04%) were male and 175 (37.96%) were female. The median age at diagnosis and Breslow thickness of these patients were 58 years (range, 15–90) and 3.0 mm (range, 0–75 mm), respectively, and the median OS were 1,827 days. In regard to tumor tissue site, the regional lymph node was the most common site, followed by primary tumor, regional cutaneous or subcutaneous metastatic tissue and distant metastasis. The pathologic stage was defined according to the American Joint Committee on Cancer (AJCC) Cancer staging manual, and 6 (1.30%), 75 (16.27%), 139 (30.15%), 171 (37.097%) and 23 (4.99%) patients were in stage 0, I, II, III and IV, respectively. Anatomic sites were located at various positions of the patients, including head and neck, extremity and trunk, and the extremities were the most common location (42.08%). Ulceration occurs in 167 patients, and only 26.68% (N = 123) of patients received postoperative or adjuvant chemotherapy. The distribution and selected demographic characteristics of melanoma patients are summarized in Table 1.

**Table 1.**
 Clinicopathological characteristics of CM patients from TCGA database.


<table>
  <thead>
    <tr>
      <th rowspan="3">Characteristics</th>
      <th rowspan="3">Groups</th>
      <th colspan="6">Patients</th>
    </tr>
    <tr>
      <th colspan="2">Total (N = 461)</th>
      <th colspan="2">Training cohort (N = 307)</th>
      <th colspan="2">Validation cohort (N = 154)</th>
    </tr>
    <tr>
      <th>No</th>
      <th>%</th>
      <th>No</th>
      <th>%</th>
      <th>No</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Sex</td>
      <td>Male</td>
      <td>286</td>
      <td>62.04</td>
      <td>195</td>
      <td>63.52</td>
      <td>89</td>
      <td>57.79</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>175</td>
      <td>37.96</td>
      <td>112</td>
      <td>36.48</td>
      <td>65</td>
      <td>42.21</td>
    </tr>
    <tr>
      <td rowspan="4">Age at diagnosis</td>
      <td>Median</td>
      <td>58</td>
      <td></td>
      <td>58</td>
      <td></td>
      <td>58</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>15–90</td>
      <td></td>
      <td>15–90</td>
      <td></td>
      <td>19–90</td>
      <td></td>
    </tr>
    <tr>
      <td>≤58</td>
      <td>234</td>
      <td>50.76</td>
      <td>154</td>
      <td>50.16</td>
      <td>80</td>
      <td>51.95</td>
    </tr>
    <tr>
      <td>&gt;58</td>
      <td>227</td>
      <td>49.24</td>
      <td>153</td>
      <td>49.84</td>
      <td>74</td>
      <td>48.05</td>
    </tr>
    <tr>
      <td rowspan="5">Tumor tissue site</td>
      <td>Primary tumor</td>
      <td>104</td>
      <td>22.56</td>
      <td>76</td>
      <td>24.76</td>
      <td>28</td>
      <td>18.18</td>
    </tr>
    <tr>
      <td>Regional cutaneous or subcutaneous tissue</td>
      <td>73</td>
      <td>15.84</td>
      <td>51</td>
      <td>16.61</td>
      <td>22</td>
      <td>14.29</td>
    </tr>
    <tr>
      <td>Regional lymph node metastasis</td>
      <td>216</td>
      <td>46.85</td>
      <td>154</td>
      <td>50.16</td>
      <td>62</td>
      <td>40.26</td>
    </tr>
    <tr>
      <td>Distant metastasis</td>
      <td>65</td>
      <td>14.10</td>
      <td>23</td>
      <td>7.49</td>
      <td>42</td>
      <td>27.27</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>3</td>
      <td>0.65</td>
      <td>3</td>
      <td>0.98</td>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td rowspan="6">Pathologic stage</td>
      <td>0</td>
      <td>6</td>
      <td>1.30</td>
      <td>5</td>
      <td>1.63</td>
      <td>1</td>
      <td>0.65</td>
    </tr>
    <tr>
      <td>I</td>
      <td>75</td>
      <td>16.27</td>
      <td>53</td>
      <td>17.26</td>
      <td>22</td>
      <td>14.29</td>
    </tr>
    <tr>
      <td>II</td>
      <td>139</td>
      <td>30.15</td>
      <td>92</td>
      <td>29.97</td>
      <td>47</td>
      <td>30.52</td>
    </tr>
    <tr>
      <td>III</td>
      <td>171</td>
      <td>37.09</td>
      <td>117</td>
      <td>38.11</td>
      <td>54</td>
      <td>35.06</td>
    </tr>
    <tr>
      <td>IV</td>
      <td>23</td>
      <td>4.99</td>
      <td>13</td>
      <td>4.23</td>
      <td>10</td>
      <td>6.49</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>47</td>
      <td>10.20</td>
      <td>27</td>
      <td>8.79</td>
      <td>20</td>
      <td>12.99</td>
    </tr>
    <tr>
      <td rowspan="4">Anatomic site</td>
      <td>Head and neck</td>
      <td>36</td>
      <td>7.81</td>
      <td>21</td>
      <td>6.84</td>
      <td>15</td>
      <td>9.74</td>
    </tr>
    <tr>
      <td>Extremity</td>
      <td>194</td>
      <td>42.08</td>
      <td>129</td>
      <td>42.02</td>
      <td>65</td>
      <td>42.21</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>167</td>
      <td>36.23</td>
      <td>117</td>
      <td>38.11</td>
      <td>50</td>
      <td>32.47</td>
    </tr>
    <tr>
      <td>Others/Unknown</td>
      <td>64</td>
      <td>13.88</td>
      <td>40</td>
      <td>13.03</td>
      <td>24</td>
      <td>15.58</td>
    </tr>
    <tr>
      <td rowspan="4">Breslow thickness (mm)</td>
      <td>&lt;2</td>
      <td>126</td>
      <td>27.33</td>
      <td>85</td>
      <td>27.69</td>
      <td>41</td>
      <td>26.62</td>
    </tr>
    <tr>
      <td>2–5</td>
      <td>124</td>
      <td>26.90</td>
      <td>79</td>
      <td>25.73</td>
      <td>45</td>
      <td>29.22</td>
    </tr>
    <tr>
      <td>&gt;5</td>
      <td>106</td>
      <td>22.99</td>
      <td>78</td>
      <td>25.41</td>
      <td>28</td>
      <td>18.18</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>105</td>
      <td>22.78</td>
      <td>65</td>
      <td>21.17</td>
      <td>40</td>
      <td>25.97</td>
    </tr>
    <tr>
      <td rowspan="3">Ulceration</td>
      <td>Present</td>
      <td>167</td>
      <td>36.23</td>
      <td>120</td>
      <td>39.09</td>
      <td>47</td>
      <td>30.52</td>
    </tr>
    <tr>
      <td>Absent</td>
      <td>145</td>
      <td>31.45</td>
      <td>100</td>
      <td>32.57</td>
      <td>45</td>
      <td>29.22</td>
    </tr>
    <tr>
      <td>NA/Unknown</td>
      <td>149</td>
      <td>32.32</td>
      <td>87</td>
      <td>28.34</td>
      <td>62</td>
      <td>40.26</td>
    </tr>
    <tr>
      <td rowspan="3">Chemotherapy</td>
      <td>Yes</td>
      <td>123</td>
      <td>26.68</td>
      <td>70</td>
      <td>22.80</td>
      <td>53</td>
      <td>34.42</td>
    </tr>
    <tr>
      <td>NO</td>
      <td>319</td>
      <td>69.20</td>
      <td>227</td>
      <td>73.94</td>
      <td>92</td>
      <td>59.74</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>19</td>
      <td>4.12</td>
      <td>10</td>
      <td>3.26</td>
      <td>9</td>
      <td>5.84</td>
    </tr>
    <tr>
      <td rowspan="2">Vital Status</td>
      <td>Alive</td>
      <td>241</td>
      <td>52.28</td>
      <td>167</td>
      <td>54.40</td>
      <td>74</td>
      <td>48.05</td>
    </tr>
    <tr>
      <td>Dead</td>
      <td>220</td>
      <td>47.72</td>
      <td>140</td>
      <td>45.60</td>
      <td>80</td>
      <td>51.95</td>
    </tr>
  </tbody>
</table>

### Derivation of prognostic DNA methylation markers from the training cohort

By subjecting the DNA methylation level data in the training cohort to univariate Cox proportional hazard regression analysis, a total of 4454 DNA methylation sites that significantly (p<0.001) correlated with the OS of patients with CM were identified as candidate markers. Subsequently, these candidate markers were used to perform multivariate Cox stepwise regression analyses, and a hazard ratio model consisting of four methylation sites (cg06778853, cg24670442, cg18456782, cg26263675) was selected as the optimum prognostic model for predicting OS. The risk score formula based on the DNA methylation level and regression coefficients of four methylation sites was created as follows: Risk score = –1.912 × β value of cg06778853 +4.262 × β value of cg24670442 +1.229 × β value of cg18456782 – 2.108 × β value of cg26263675. Among these methylation sites, cg24670442 and cg18456782 had positive coefficients, indicating a correlation between higher DNA methylation level and shorter OS, while higher levels of DNA methylation in cg06778853 and cg26263675 sites correlated with longer OS. The genes corresponding with these four sites were KLHL21 (kelch like family member 21), GBP5 (guanylate binding protein 5), OCA2 (OCA2 melanosomal transmembrane protein), and RAB37 (RAB37, member RAS oncogene family). The list of these four DNA methylation sites, their chromosomal locations, their P values and coefficients obtained in Cox regression analysis, are shown in Supplementary file 1.

Meanwhile, for these four DNA methylation sites, the DNA methylation level between patients exhibiting long-term (>5 years) and short-term (<5 years) survival was significantly different (Figure 1A) (p<0.001, Mann–Whitney U test). Patients exhibiting long-term survival tended to have lower methylation levels of cg24670442, cg18456782 and higher methylation levels of the other two methylation sites, consistent with the results of multivariate Cox regression analysis. Moreover, principal component analysis (PCA) was carried out using four methylation values at selected biomarkers (Figure 1—figure supplement 1). The difference of PC1 and PC4 is 15.42%, indicating the continuous capturing of information. And the combination of four methylation markers can effectively distinguish patients with long- and short-term survival.

![Figure 1.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig1-v1.jpg)

**Figure 1.:** (A) Methylation β values of samples from patients with short survival (OS <5 years) and long survival (OS >5 years) in the training cohort. Within each methylation site, the thick line represents the median value, the bottom and top of the boxes are the 25th and 75th percentiles (interquartile range). The whiskers encompass 1.5 times the interquartile range. The difference between short and long survival groups was compared through the Mann–Whitney U test, and P values are shown below the plots. The Kaplan–Meier curves along with the Wilcoxon test were used to visualize and compare the OS of the low-risk versus high-risk groups in the training cohort (N = 307) (B) and the validation cohort (N = 154) (C). Here ‘low-risk (57/153)’ refers to that a total of 153 patients in the low-risk group, in which 57 with last clinical status ‘death’, and ‘low-risk (83/154)’ refers to that a total of 154 patients in the high-risk group, in which 83 with last clinical status ‘death’. It can be concluded that higher risk scores are significantly associated with worse OS (p<0.001).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) The contribution of each component is ranked based on the magnitude of its corresponding percentage of explained variances. The difference of PC1 and PC4 is 15.42%, indicating the continuous capturing of information. (B) The differences between short survival (OS <5 years) and long survival (OS >5 years) in the training cohort.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** The horizontal lines in the boxes indicated the median, and the top and bottom of the boxes the second and third quartiles. The whiskers represent the minimum and maximum values.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** Reported P values are two sided. Level of gene expression is reported as log2-transformed Fragments Per Kilobase of transcript per Million mapped reads (FPKM), and methylation β-values defined by the Infinium HumanMethylation 450 BeadChip.

### Association between the four-DNA methylation signature and patient OS in training and validation cohorts

According to the results of Cox regression analysis, the four-DNA methylation signature were significantly associated with the OS of patients using the risk scores as a continuous variable in both the training and validation cohorts (training cohort: p=1.73E-7, HR: 2.72, 95% CI of HR: 1.91–3.88; validation cohort: p=3.19E-6, HR: 3.58, 95% CI of HR: 2.04–6.29). To determine the potential predictive value of this four-DNA methylation signature in the prognosis, Kaplan–Meier curves along with the Wilcoxon test were used to visualize and compare the OS of patients in the low- versus high-risk group which were classified using the median risk score (3.69) of the training cohort as the cutoff point, and the distribution of the risk predictor scores for the training and validation cohort was illustrated in Figure 1—figure supplement 2. As expected, the survival of patients in the low-risk group was significantly improved in comparison with patients in the high-risk group (Figure 1B for training cohort, median OS of 2,639 and 1,119 days, respectively, and Figure 1C for validation cohort, median OS of 2,306 and 1,297 days, respectively). These results confirmed that the novel four-DNA methylation signature could successfully stratify patients into high- and low-risk groups, implying its significance in determining CM prognosis.

### The prognostic potential of the four-DNA methylation signature

To understand the specificity of the four-DNA methylation signature in predicting survival, the AUC values of the ROC curves were calculated by time-dependent ROC analysis using a categorical variable for OS < 5 years compared with the signature. For this purpose, patients for whom we did not have at least 5 years of follow-up were excluded, unless death had been documented. In both training and validation cohorts, the four-DNA methylation signature has good discriminatory capacity for predicting patient OS, with dynamic AUC estimates exceeding 0.80 (Figure 2A) and 0.75 (Figure 2B) in training and validation cohorts, respectively. These results indicate that the four-DNA methylation signature has high sensitivity and specificity, and has great potential to serve as a prognostic biomarker in clinical applications.

![Figure 2.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig2-v1.jpg)

**Figure 2.:** (A) ROC analysis of sensitivity and specificity of the four-DNA methylation signature in predicting the OS of patients in training cohort, with an AUC of 0.822 (B) ROC analysis in validation cohort, with an AUC of 0.754. (C) Kaplan–Meier survival curves demonstrating the correlation between the four-DNA methylation signature and poorer OS of patients in an independent cohort (GSE51547). (D) ROC curves show the sensitivity and specificity of the signature in predicting the patient’ OS, AUC = 0.708.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the individual methylation signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Kaplan–Meier survival curves with show correlation between expression of four-mRNA signature and OS of patients. Wilcoxon test was performed to estimate the differences between the low-risk and high-risk patients. (B) ROC curves of the four-mRNA signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the individual methylation signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

### Evaluation of the four-DNA methylation signature for OS prediction in an independent cohort

To further examine the prognostic values of the four-DNA methylation signature in another independent cohort, Kaplan–Meier and ROC analyses were carried out in an independent cohort (GSE51547, N = 47). Similarly, patients with high or low risk were grouped based on the median risk score of the training cohort. The results showed that the four-DNA methylation performed well, and patients in the low-risk group had a significantly longer OS than those in the high-risk group (p<0.05) (Figure 2C). Here, due to the limited sample size of the independent cohort with follow up times more than 5 years (N = 2, 4.25%), the AUC was calculated using 1 year as the cutoff (N = 32, 68.08%), and the AUC estimate was 0.708 (p=0.022, 95% CI: 0.54–0.88) (Figure 2D), suggesting that the four-DNA methylation signature can also predict the survival of CM patients in other independent cohorts.

### Independence of the four-DNA methylation signature in the OS prediction from clinical and pathological factors

An important feature of a good prognostic signature is that it should be independent or additive to currently used clinicopathologic prognostic factors. Clinical and pathological characteristics, such as patients’ age, sex, AJCC stage, tumor thickness and ulceration status also have been considered to be the predominant predictors used to determine prognosis of melanoma patients. To assess the independence and applicability of this four-DNA methylation signature, patients were regrouped according to different clinicopathological characteristics. Over the last few decades, the incidence of CM has been increasing rapidly in males compared to females of all ages, with the exception of young women who appear to be at higher risk than young men (Robsahm et al., 2013). The incidence in male patients is 1.6 times higher than that of female patients, and regrouping was performed based on patients’ sexes and ages at initial diagnosis in the following way: age ≤50 (N = 141, 30.58%), 50 < age ≤ 70 (N = 202, 43.82%), and age >70 (N = 118, 25.60%). Irrespective of sexes and ages, Kaplan–Meier curves showed that patients in the low-risk group had significantly (p<0.001) longer OS, and the AUC values were more than 0.75 (Figure 3 and Figure 3—figure supplement 1), suggesting that the four-DNA methylation signature is independent of patient sex and age. Considering that once the tumor metastasizes to distant tissues, the 5 year survival rate is very low (Siegel et al., 2018), we regrouped patients based on the site of sample obtainment, including distant metastasis, subcutaneous tissue, and regional lymph node metastasis. Kaplan–Meier and ROC analyses demonstrated that the survival of patients in low-risk groups was much improved in comparison with patients in high-risk groups, and the four-DNA methylation signature had high predictive performance (Figure 3—figure supplement 2). Meanwhile, research has shown that DNA methylation changes in relation to disease stage (Wouters et al., 2017), and survival outcomes can vary widely even at a single stage (Weiss et al., 2015). Because of limited sample size at each stage, patients were separated into early-stage (0 and I and II) and advanced-stage (III and IV) cohorts. Despite the markedly different outcomes in terms of the extent of disease, the OS between high- and low-risk groups are significantly (p<0.001) different, and the AUC in early-stage and advanced-stage cohorts were 0.814 and 0.809, respectively (Figure 3—figure supplement 3). Furthermore, whether the tumor was located in head and neck or extremity or trunk, the four-DNA methylation signature performed well in differentiating low- and high-risk groups, and patients in high-risk groups showed a trend towards worse OS (Figure 3—figure supplement 4).

![Figure 3.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-v1.jpg)

**Figure 3.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low-risk and high-risk patients. (B) ROC curves of the four-DNA methylation signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Kaplan–Meier estimates of the patients’ OS for low- and high-risk patient, and the OS differences between two groups were determined by Wilcoxon test; (B) ROC curves show the sensitivity and specificity of the signature in predicting the OS of patients.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) Kaplan–Meier estimates of the patients’ OS for low- and high-risk patient in different stage cohorts, and the OS differences between two groups were determined by Wilcoxon test; (B) ROC curves show the sensitivity and specificity of the signature in predicting the OS of patients.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp6-v1.jpg)

**Figure 3—figure supplement 6.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig3-figsupp7-v1.jpg)

**Figure 3—figure supplement 7.:** (A) Kaplan–Meier analysis with Wilcoxon test was performed to estimate the differences in OS between the low- and high-risk patients. (B) ROC curves of the signature were used to demonstrate the sensitivity and specificity in predicting the OS of patients.

Considering that Breslow thickness is the strongest prognostic factor in CM, patients who have Breslow thickness more than 2 mm are at the greatest risk of developing locoregional cutaneous metastases (Messeguer et al., 2013), we investigated whether the four-DNA methylation signature could classify patients with different survival risk for patients with different Breslow thickness. The results indicated that the four-DNA methylation signature was effective in distinguishing the high-risk patients from low-risk patients for patients of any Breslow thickness groups (Figure 3—figure supplement 5). CM ulceration status has also been shown in many studies to be a major and independent prognostic parameter. Regardless of ulceration, four-DNA methylation signature proved useful for identifying patients with low risk (Figure 3—figure supplement 6). Additionally, we found no association between the predictive performance of the four-DNA methylation signature and whether a patient received adjuvant chemotherapy (Figure 3—figure supplement 7). All these results indicated that the four-DNA methylation signature provides a better reference for different regrouped cohorts owing to the effectiveness of risk stratification, suggesting that the signature was an independent applicable prognostic predictor of patient survival. The results of Kaplan–Meier and ROC analyses are summarized in Table 2.

**Table 2.**
 Results of Kaplan–Meier and ROC analyses based on various regrouping methods.


<table>
  <thead>
    <tr>
      <th>Regrouping factors</th>
      <th>Group</th>
      <th>Sample size</th>
      <th>Kaplan–Meier P-value</th>
      <th>AUC</th>
      <th>95% CI of AUC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Sex</td>
      <td>Male</td>
      <td>286</td>
      <td>4.69E-10</td>
      <td>0.786</td>
      <td>0.72–0.85</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>175</td>
      <td>2.82E-08</td>
      <td>0.844</td>
      <td>0.77–0.92</td>
    </tr>
    <tr>
      <td rowspan="3">Age at diagnosis</td>
      <td>≤50</td>
      <td>141</td>
      <td>3.46E-06</td>
      <td>0.792</td>
      <td>0.71–0.88</td>
    </tr>
    <tr>
      <td>51–70</td>
      <td>202</td>
      <td>1.14E-07</td>
      <td>0.816</td>
      <td>0.74–0.89</td>
    </tr>
    <tr>
      <td>&gt;70</td>
      <td>118</td>
      <td>1.75E-05</td>
      <td>0.807</td>
      <td>0.70–0.92</td>
    </tr>
    <tr>
      <td rowspan="3">Tumor metastasis site</td>
      <td>Distant metastasis</td>
      <td>65</td>
      <td>2.63E-03</td>
      <td>0.836</td>
      <td>0.73–0.94</td>
    </tr>
    <tr>
      <td>Regional cutaneous or subcutaneous tissue</td>
      <td>73</td>
      <td>1.79E-09</td>
      <td>0.859</td>
      <td>0.76–0.96</td>
    </tr>
    <tr>
      <td>Regional lymph node metastasis</td>
      <td>216</td>
      <td>2.01E-07</td>
      <td>0.749</td>
      <td>0.67–0.83</td>
    </tr>
    <tr>
      <td rowspan="2">Pathologic stage</td>
      <td>0 and I and II</td>
      <td>231</td>
      <td>1.56E-11</td>
      <td>0.814</td>
      <td>0.75–0.88</td>
    </tr>
    <tr>
      <td>III and IV</td>
      <td>194</td>
      <td>6.75E-07</td>
      <td>0.809</td>
      <td>0.73–0.89</td>
    </tr>
    <tr>
      <td rowspan="3">Anatomic site</td>
      <td>Head and neck</td>
      <td>36</td>
      <td>7.76E-05</td>
      <td>0.960</td>
      <td>0.00–1.00</td>
    </tr>
    <tr>
      <td>Extremity</td>
      <td>194</td>
      <td>9.28E-06</td>
      <td>0.787</td>
      <td>0.71–0.87</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>167</td>
      <td>3.87E-06</td>
      <td>0.756</td>
      <td>0.66–0.85</td>
    </tr>
    <tr>
      <td rowspan="3">Breslow thickness (mm)</td>
      <td>&lt;2</td>
      <td>126</td>
      <td>1.83E-06</td>
      <td>0.830</td>
      <td>0.74–0.92</td>
    </tr>
    <tr>
      <td>2–5</td>
      <td>124</td>
      <td>1.79E-04</td>
      <td>0.742</td>
      <td>0.64–0.85</td>
    </tr>
    <tr>
      <td>&gt;5</td>
      <td>106</td>
      <td>1.31E-02</td>
      <td>0.808</td>
      <td>0.65–0.96</td>
    </tr>
    <tr>
      <td rowspan="2">Ulceration</td>
      <td>Present</td>
      <td>167</td>
      <td>6.84E-05</td>
      <td>0.809</td>
      <td>0.69–0.93</td>
    </tr>
    <tr>
      <td>Absent</td>
      <td>145</td>
      <td>1.79E-04</td>
      <td>0.736</td>
      <td>0.64–0.83</td>
    </tr>
    <tr>
      <td rowspan="2">Chemotherapy</td>
      <td>Yes</td>
      <td>123</td>
      <td>5.46E-06</td>
      <td>0.791</td>
      <td>0.69–0.79</td>
    </tr>
    <tr>
      <td>NO</td>
      <td>319</td>
      <td>1.10E-10</td>
      <td>0.797</td>
      <td>0.74–0.86</td>
    </tr>
  </tbody>
</table>

### Comparison of the four-DNA methylation signature with other known prognostic biomarkers

In addition, numerous prognostic markers have previously been identified for CM, utilizing archival tumor tissues or single institutional studies. MITF has been identified as a lineage survival oncogene amplified in malignant melanoma (Garraway et al., 2005), CTLA-4 expression has been shown to be associated with a more favorable prognosis of patients with CM (Goltz et al., 2018), and CD74 was identified as a useful prognostic marker associated with OS of patients in stage III melanoma (Ekmekcioglu et al., 2016). The presence of MGMT promoter methylation is an independent variable associated with longer OS (Cesinaro et al., 2012), and the methylation of PTEN has been reported as an independent negative prognostic factor in terms of OS (Roh et al., 2016). To determine whether our signature has superior ability to predict patient survival, compared with known biomarkers, ROC analyses of other biomarkers were carried out in the validation cohort (Figure 4A) and independent cohort (Figure 4B), in the same way our four-DNA methylation signature was analyzed. The results demonstrated that the four-DNA methylation signature had higher AUC than all the other known biomarkers in both validation cohort and independent cohort. The results of ROC analysis are shown in Figure 4A and Supplementary file 2, revealing that the four-DNA methylation signature was a superior predictor, and provided better stability and reliability in predicting the OS of patients with CM.

![Figure 4.](https://cdn.elifesciences.org/articles/44310/elife-44310-fig4-v1.jpg)

**Figure 4.:** (A) ROC curves show the sensitivity and specificity of our four-DNA methylation signature and other known biomarkers in predicting the OS of patients from TCGA validation dataset. (B) ROC curves of our four-DNA methylation signature and other known biomarkers in predicting the OS of patients from another independent cohort. (C) ROC curves of our four-DNA methylation signature, GBP5-meth, and known immune checkpoint genes, TMB and MeTIL in predicting the OS of patients from TCGA validation dataset. (D) Correlation analyses between known immune checkpoint genes, TMB and MeTIL, our four-DNA methylation signature, as well as GBP5-meth, one of our four DNA methylation sites. Lower triangle: scatter plots showing the correlation between two signatures. Upper triangle: circle symbols represent the one-to-one correlation coefficient; each correlation coefficient is shown by fill area and intensity of shading, which increases uniformly as the correlation value moves away from 0; blue for positive correlation, red for negative correlation.

### Association of the four-DNA methylation signature with ICB immunotherapy-related signature

In recent years, cancer immunotherapy using ICB has created a paradigm shift in the treatment of advanced-stage cancers, and provides significant clinical benefits for patients with CM (Hugo et al., 2016). ICB treatment primarily targets programmed cell death 1 (PD-1), programmed cell death-ligand 1 (PD-L1), and cytotoxic T-lymphocyte-associated protein 4 (CTLA-4) (Sharma et al., 2017). Programmed cell death-ligand 2 (PD-L2) was found to play a role in the regulation of anti-tumor immunity (Umezu et al., 2019). Multiple studies have shown that tumor mutational burden (TMB) may be a surrogate for overall neoantigen load, and it is correlated with clinical benefit from multiple checkpoint inhibitors (Rizvi et al., 2015). Features of the tumor microenvironment (TME) also were associated with the response to ICB therapy (Jeschke et al., 2017; Riaz et al., 2017). Although TME is determined by both DNA methylation and gene expression, DNA methylation may reflect distributions of cell subtypes more adequately, given that the relationship of only 2 DNA molecules per cell is of a more linear nature than are thousands of mRNA copies exposed to mRNA degradation (Jeschke et al., 2017). Indeed, Jeschke et al have identified a five-DNA methylation signature of tumor-infiltrating lymphocytes (MeTIL), which could more accurately measure TIL distributions in a sensitive manner and predict survival and tumor immune responses than gene expression-based immune markers (Jeschke et al., 2017). Additionally, the tumor immune response is increasingly recognized to be associated with better clinical outcomes (Cristescu et al., 2018; Goltz et al., 2018; Jeschke et al., 2017). Here we investigated the prognostic impact of these immunotherapy-related signatures in the validation cohort (Figure 4C). To investigate the possible role of our four-DNA methylation signature in ICB treatment, we performed one-to-one correlation between these known immunotherapy-related signatures and our signature. As expected, PD-1, PD-L1, PD-L2, and CTLA-4 mRNA were coexpressed (p<0.001) (Figure 4D), which is consistent with the reported coexpression of immune checkpoint molecules (Goltz et al., 2018). TMB was not significantly correlated with any other signature, which is also consistent with previous reports (Cristescu et al., 2018). Surprisingly, our four-DNA methylation signature was significantly negatively correlated with PD-1, PD-L1, PD-L2, and CTLA-4 (p<0.05 and r = –0.485,–0.338, –0.322, and –0.131, respectively); meanwhile, MeTIL was significantly negatively correlated with PD-1, PD-L1, and PD-L2 (p<0.05 and r = –0.411,–0.288, –0.288, respectively), but was not significantly correlated with CTLA-4 (p=0.233 and r = –0.056) (Figure 4C), suggesting that some elements or all of the four-DNA methylation signature may play a role in measures of responsiveness to ICB immunotherapy. In fact, cg24670442, one of the four-DNA methylation signatures, corresponding to GBP5 gene, was significantly negatively correlated with PD-1, PD-L1, PD-L2, CTLA-4 (p<0.001, and r = –0.681,–0.405, –0.436,–0.171, respectively), and patients with long-term survival exhibiting lower methylation levels and higher expression level. Meanwhile, GBP5 has been proved to be induced by interferon-gamma (IFN-γ), and could serve as the substitute indicator of IFN-γ, which promotes not only immunomodulation but also anticancer activity, and play a role in immunotherapy (Chang et al., 2015; Yamamoto et al., 2012). The raw P values of Pearson correlation and Bonferroni correction adjusted P values between our four-DNA methylation signature and other known signatures are shown in Supplementary file 3. Collectively, these results imply that our four-DNA methylation signature, although developed to accurately stratify patients in terms of prognosis, may also play a role in ICB immunotherapy.

## Discussion

CM is the deadliest form of skin cancer and lead to 60,712 deaths in 2018 (Miller and Mihm, 2006). In recent years, the importance of DNA methylation in the biology of CM has been increasingly acknowledged. For instance, hypermethylated estrogen receptor alpha (ER-α) is a significant factor in melanoma progression (Mori et al., 2006); methylation-dependent SOX9 expression mediates invasion in human melanoma cells and is a negative prognostic factor in advanced melanoma (Cheng et al., 2015), and MGMT gene promoter methylation in metastatic CM is associated with longer survival (Cesinaro et al., 2012). However, these studies usually concentrated on single gene methylation or patient samples with specific clinical characteristics, and combinations of DNA methylation as biomarkers could achieve higher sensitivity and specificity than individual DNA methylation (Dai et al., 2011). Moreover, a limited overlap between signatures published by various studies can be observed, possibly due to variation in disease causes, tissue heterogeneity, or stage of disease at the point of analysis (Tremante et al., 2012). The TCGA database provides a large number of samples with a variety of clinical characteristics. Based on a TCGA dataset that included 461 CM samples, the current study identified a prognostic DNA methylation signature with potential clinical applicability, validated it in an independent cohort, and investigated its high reproducibility and utility in various clinical groups.

CM has a high degree of heterogeneity in terms of clinical, dermatological, and histopathological presentation (Coricovac et al., 2018). Several parameters, such as age, sex, stage of disease, Breslow thickness, and ulceration status have significant influence on CM patient prognosis, in which Breslow thickness has been demonstrated as the most important clinicopathological characteristic for predicting prognosis. In order to be clinically useful, a DNA methylation signature must be independent of clinical factors. Here we adopted a grouping method not influenced by our subjective, that is based on the TCGA series number of patients, without adjusting for clinical parameters. If detection, treatment and surgical excision occur when the tumor burden is restricted to a primary site, a patient’s prognostic survival is enhanced, but once the disease has metastasized to distant organs such as the brain and liver, prognosis is poor (Balch et al., 2009). Since patients with primary tumors had shorter follow-ups, none more than 5 years, we analyzed the independence and applicability of our four-DNA methylation signature in samples obtained from distant metastasis, subcutaneous tissue, and regional lymph node metastasis. The results showed that our signature was independent of tumor metastatic sites. Moreover, as patients suffering from early stages of the disease exhibit higher potential for healing, a prognostic signature that can also efficiently risk-stratify these patients would have higher clinical application value (Segura et al., 2010). Our signature has been demonstrated to be not only independent of all clinical factors, but also to have higher predictive performance for patients with tumor thickness of less than 2 mm and patients in early stages (AUCs were 0.830 and 0.814, respectively). Therefore, our signature was an independent applicable prognostic biomarker, which may be of high clinical value.

Considering that an ideal prognostic marker is one that can also efficiently risk-stratify in other independent cohorts, we employed GEO dataset (GSE51547) to further evaluate the practicality of our four-DNA methylation signature. Although the predictive accuracy in the GEO dataset is not as high as in the validation dataset due to the low number of samples (N = 47), the four-DNA methylation signature performed well in distinguishing low- and high-risk groups (AUC = 0.708, p<0.05). Furthermore, it was demonstrated that in both the validation and independent cohorts, our signature outperformed other known prognostic biomarkers, including mRNA, lncRNA, and DNA methylation, and statistical comparison using Z-test revealed that it has significantly higher (p<0.05) predictive performance than almost all the other known biomarkers. When further samples become available it will be important to analyze this methylation signature in another validation dataset.

Targeting immune checkpoints such as PD-1, PD-L1, and CTLA-4 have achieved noteworthy benefit in multiple cancers by blocking immunoinhibitory signals and enabling patients to produce an effective antitumor response, especially in patients with CM (Riaz et al., 2017). However, a significant limitation of ICB is that less than one-third of patients respond to ICB treatment, and identification of ICB response biomarkers and resistance regulators is a critical challenge (Sharma et al., 2017). DNA methylation plays a critical role in cell lineage specification and may serve as a specific molecular marker for measurement of immune responses. Recently, Jeschke et al highlighted the power of MeTIL to evaluate local and functional TIL-based tumor immune responses and the ability of this approach to improve prognosis (Jeschke et al., 2017). However, the identification of MeTIL was focused on CpGs that are highly differentially methylated between T lymphocytes and epithelial cells. Lymphocytes only account for a small fraction of TME (Pretscher et al., 2009); thus, there may be bias when using MeTIL as a prognostic marker to predict survival outcomes. Intriguingly, the correlation analyses and the observed predictive performance suggested that our four-DNA methylation signature was significantly correlated with the ICB immunotherapy-related signature. Additionally, our signature displayed higher predictive performance than other known signatures, including PD-1, PD-L1, PD-L2, CTLA-4, and MeTIL. These results demonstrate that our four-DNA methylation signature, although developed for accurate prognosis, may also have potential as a guide for precision cancer ICB immunotherapy.

Furthermore, epigenetic changes have been shown to alter gene expression, and epigenetic inactivation of tumor suppressor genes has been implicated in tumorigenesis of various malignancies, including CM (Herman and Baylin, 2003). Here, the expression of GBP5 and KLHL21 were significantly (p<0.001) negatively correlated with their methylation levels, and the other two genes show significant positive correlation (p<0.001) between the expression and their methylation levels (Figure 1—figure supplement 3). We also found that expression of this four-gene can also be used as a prognostic biomarker (Figure 2—figure supplement 1), but the four-DNA methylation biomarker offer a better potential to fulfill much more sensitive and specific prognostic test. For our four-DNA methylation sites, researchers have revealed that their corresponding genes may be crucial in immunity and cancer development, including CM. For instance, GBP5 promotes NLRP3 inflammasome assembly and immunity in mammals (Shenoy et al., 2012). GBP5 was induced by IFN-γ, could serve as a marker of IFN-γ-induced classically activated macrophages and the substitute indicator of IFN-γ, which can directly suppress tumorigenesis and infection and/or can modulate the immunological status in cancer cells (Chang et al., 2015; Yamamoto et al., 2012). Meanwhile, GBP5 expression in CM is associated with favorable prognosis (Wang et al., 2018). RAB37, as a tumor suppressor gene, promotes M1-like macrophage infiltration and suppresses tumor growth (Tzeng et al., 2018), and it was frequently down-regulated due to promoter hypermethylation in metastatic lung cancer, can serve as a potential predictive biomarker (Wu et al., 2009). RAB37-mediated SFRP1 secretion suppresses cancer stemness, and dysregulated RAB37-SFRP1 pathway confers cancer stemness via the activation of Wnt signaling (Cho et al., 2018). OCA2 is involved in the melanin biosynthetic process and mammalian pigmentation (Crawford et al., 2017), and the DNA variant in intron of OCA2 (rs4778138) has been found associated with CM risk (Law et al., 2015). The hypomethylation levels of cg18456782 (OCA2) was associated with lower expression of OCA2 and a lower risk. Meanwhile separating CM patients by median expression of OCA2, there is a significant differential survival (p<0.0001) with low expression favoring better survival. All these results suggest a risk pattern for OCA2 gene in CM. KLHL21 could affect cell migration and invasion, play an essential role in tumorigenesis and progression, and it might serve as a potential therapeutic target for cholangiocarcinoma (Chen et al., 2018) and hepatocellular carcinoma (Shi et al., 2016). Although the functional mechanism of these four genes in CM still needs further study, significant correlation between these four genes and OS or response to therapy of patients with CM, and DNA methylation might also be suitable as biomarkers for response to ICB therapy.

In addition, the results of the univariate Cox regression, Kaplan–Meier and ROC analyses for the four individual methylation sites show that each of the DNA methylation sites also could distinguish high- and low-risk patients, but the predictive performances were lower than the combination of these four DNA methylation sites in both the training and validation cohorts (Figure 2—figure supplements 2–3), indicating that single methylation sites are likely to play a role in the prognostic prediction, and a combination of methylation sites might offer better potential to fulfill much more sensitive and specific prognostic tests for patients with CM. To the best of our knowledge, the prognostic value of this multi-marker signature in melanoma has not been previously reported. Therefore, the current study provides new insight that a combination of epigenetic biomarkers could help to improve risk-stratification and prediction of survival in patients with melanoma.

In conclusion, we identified and verified a four-DNA methylation signature that was significantly associated with the OS of patients in TCGA and an independent cohort. The four-DNA methylation signature was not only independent of clinical factors including patient sex, age, stage, tumor location, and Breslow thickness, but also exhibited superior ability in predicting OS compared with known biomarkers. The four-DNA methylation signature was able to stratify patients with startling accuracy in survival differences, suggesting that it may be used to select patients for therapies, and help to determine whether patients may require more or less aggressive treatment. Furthermore, the four-DNA methylation signature was significantly correlated with the ICB immunotherapy-related signature. Therefore, though these exploratory findings are warranted to validate the potential role of this prognostic signature in clinical application and the functional characterization in CM development, these four-DNA methylation sites, or some of them, may participate in the progress of the cancer, and have great potential implications for both risk-stratification, adjuvant management and measures of response to ICB immunotherapy of patients with CM.

## Materials and methods

### DNA methylation data of CM tissues

The DNA methylation data and related clinical information of patients with CM were downloaded from the TCGA database (Hudson et al., 2010). TCGA DNA methylation data (level 3) were obtained using Infinium Human Methylation 450 BeadChip (Illumina Inc, CA, USA). For each CpG site, the ratio of fluorescent signal was measured by that of a methylated probe relative to the sum of the methylated and unmethylated probes, a ratio termed β value, also known as DNA methylation level. β values were standardized and assigned a value from 0 (no methylation) to 1 (100% methylation). Only the data corresponding to patients for whom clinical survival information was available were selected. The correlation between DNA methylation levels and corresponding survival in CM was analyzed. Overall, 461 samples with 485,577 DNA methylation sites were analyzed in this study. According to the TCGA series number, these samples were divided into two cohorts: the first two-thirds were used as the training cohort for identifying and constructing prognostic biomarkers, and the remaining one-third were used as a validation cohort for verifying the predictive performance of the biomarker. Detailed patient eligibility information have been described in the previous study (Cancer Genome Atlas Network, 2015), and the following clinicopathological parameters relevant to this study were selected from the TCGA clinical patient data files to perform analyses: sex, age at diagnosis, tumor tissue site, Breslow thickness, pathologic stage, ulceration status, and last clinical status. The number of samples used from each cohort are shown in Table 1. Also, an additional methylation dataset and corresponding clinical data were downloaded from the GEO database (47 patients, GEO accession number: GSE51547) and used as an independent validation cohort.

### Statistical analyses

As we previously reported (Chen et al., 2017), the outcome of interest was death due to CM, and overall survival (OS) was defined as the time from the date of a patient's diagnosis to the date of CM-related death or last follow-up. The univariate Cox proportional hazard analysis was first conducted in the training cohort to identify methylation markers significantly (p<0.001) associated with patient survival. Then the variables significantly associated with OS in univariate analysis were included in multivariate Cox regression analysis and constructed models comprising all possible combinations of two to five factors, aiming at further selecting combined biomarker correlated with OS. Hazard ratios (HR) and corresponding 95% confidence interval (CI) were assessed using Cox proportional hazard models. The linear combination of model predictors weighted by regression coefficients was defined as the risk predictive formula and was used to predict the survival risk of patients. Briefly, according to the formula, the risk score for each patient was calculated, and the patients were then classified into high- or low-risk groups using the median risk score as the cutoff value. Secondly, the Kaplan–Meier survival curves were drawn using the ‘survival’ package to visualize the cumulative survival time displaying number of patients at risk for some time points, and Wilcoxon rank test was used to assess the differences in OS between the two groups with the consideration that it is a more sensitive measure than the log-rank test to compare differences in survival probability between groups that occur in early points in time (Youden, 1950). Lastly, the risk scores were also evaluated for utility in predicting OS of patients by identifying the area under the Receiver operating characteristic (ROC) curve (AUC) along with 95% CI in the ROC analysis, which was conducted with the ‘pROC’ package. Additionally, Pearson correlation coefficients were calculated to characterize the potential association between DNA methylation level and gene expression level. All statistical calculations were carried out using the R statistical environment (R version 3.4.4).
