# No relationship between frontal alpha asymmetry and depressive disorders in a multiverse analysis of five studies

## Authors

- Aleksandra Kołodziej<sup>1</sup> ([ORCID: 0000-0002-6042-8215](https://orcid.org/0000-0002-6042-8215)) †
- Mikołaj Magnuski<sup>1</sup> ([ORCID: 0000-0001-6859-2581](https://orcid.org/0000-0001-6859-2581))
- Anastasia Ruban<sup>1</sup> ([ORCID: 0000-0001-7039-148X](https://orcid.org/0000-0001-7039-148X))
- Aneta Brzezicka<sup>1</sup> ([ORCID: 0000-0003-1950-4180](https://orcid.org/0000-0003-1950-4180))

### Affiliations

1. University of Social Sciences and Humanities Warsaw Poland
2. Cedars-Sinai Medical Center Department of Neurosurgery Los Angeles United States

† Corresponding author

## Abstract

For decades, the frontal alpha asymmetry (FAA) – a disproportion in EEG alpha oscillations power between right and left frontal channels – has been one of the most popular measures of depressive disorders (DD) in electrophysiology studies. Patients with DD often manifest a left-sided FAA: relatively higher alpha power in the left versus right frontal lobe. Recently, however, multiple studies failed to confirm this effect, questioning its reproducibility. Our purpose is to thoroughly test the validity of FAA in depression by conducting a multiverse analysis – running many related analyses and testing the sensitivity of the effect to changes in the analytical approach – on data from five independent studies. Only 13 of the 270 analyses revealed significant results. We conclude the paper by discussing theoretical assumptions underlying the FAA and suggest a list of guidelines for improving and expanding the EEG data analysis in future FAA studies.

## Introduction

Electrophysiological studies on frontal alpha asymmetry (FAA) in depressive disorders (DD) have almost 40 years of history, with first reports presented in 1983 (Schaffer et al., 1983). Since then, many studies have reported relatively higher alpha band power in the left vs right frontal channels (left-sided FAA) in subjects suffering from DD compared to healthy individuals (Allen et al., 2004; Davidson, 1984; Davidson, 2004; Kemp et al., 2010; Schaffer et al., 1983). FAA index, calculated by subtracting the left-side alpha power from the respective right-side channel, is one of the most common electrophysiological indicators of DD in the current literature (de Aguiar Neto and Rosa, 2019). However, multiple studies failed to replicate the relationship between FAA and DD (Allen et al., 2004; Carvalho et al., 2011; Deldin and Chiu, 2005; Gold et al., 2013; Kaiser et al., 2018a; Kentgen et al., 2000; Knott et al., 2001; Mathersul et al., 2008; Szumska et al., 2021; Vuga et al., 2006) and conclusions of meta-analyses remain skeptical (Thibodeau et al., 2006; van der Vinne et al., 2017). In this light statements about FAA being a biomarker of depression (Baskaran et al., 2012; Iosifescu et al., 2009) seem to be too far-fetched.

It is not clear what the causes of above-mentioned inconsistency in the literature are, but methodological issues are mentioned as one potential problem in a recent review by Kaiser et al., 2018b. Factors like age, gender, or education are known to covary with depression (McFarland and Wagner, 2015; Nolen-Hoeksema, 2001; Stordal et al., 2003) and alpha power or asymmetry (Jesulola et al., 2017; Parameshwaran and Thiagarajan, 2019; van der Vinne et al., 2017), but are often not controlled for during recruitment. While counter-balancing groups with respect to these variables can be difficult their effect may be accounted for by including them as predictors in the regression model. Although correlated predictors like education and depression can reduce each other's effect by explaining shared variance in the dependent variable, including confounding variables can also help remove variance unexplained by the variable of interest and therefore increase its effect.

There are also other important methodological problems worth considering when trying to resolve the validity of FAA in DD. Although much attention in the FAA literature has been paid to the choice of EEG reference (see for example: Smith et al., 2017; or Stewart et al., 2014) other aspects of signal processing and analysis seem to be more neglected. Many EEG studies on FAA use and report FAA index calculated only for a few channel pairs (e.g. one or two pairs were used in 12 out of 17 studies [70.6%] included in the meta-analysis by van der Vinne et al., 2017). In combination with the fact that topographical maps of effects are rarely presented (4/17 studies [23.5%] in van der Vinne et al., 2017) this significantly reduces the reliability and interpretability of the reported effects. The FAA effects are frequently assumed to reflect frontal sources of alpha oscillations but without a topographical map to support this claim it is difficult to conclude whether such interpretation is correct. For example, alpha asymmetry at frontal channels may, in principle, arise due to asymmetrical projection from other, non-frontal, sources. This could be identified in the topography, but not at the single channel pair’s level. Without a topographical map it is also more difficult to assess the physiological reliability of the reported effect – significant effect on one channel pair without similar effects on surrounding channels calls for skeptical consideration (van Ede and Maris, 2016). Therefore, it might be better to perform the analysis on many frontal channel-pairs with relevant correction for multiple comparisons (for example, with the very popular cluster-based permutation approach, Maris and Oostenveld, 2007). This is unfortunately rarely done in FAA studies on DDs (0/17 studies in van der Vinne et al., 2017).

However, performing the analysis only at the channel level, when the research question pertains to the neural source of the effects, can also lead to misinterpretations. Even if topographies are shown, they can be inconclusive with respect to the underlying neural source. For this reason it might be useful to perform source localization and continue the analyses in the source space. Given the assumption of frontal alpha sources of FAA presented in the literature, source level analysis would be appropriate. Regrettably, most FAA studies do not perform source localization, although there are notable exceptions (for example, Lubar et al., 2003; Smith et al., 2018).

Incompatible results in FAA literature, summarized briefly above, suggest that the FAA relationship with DD is sensitive to the choice of signal preprocessing and analysis steps. In such a case applying multiverse analysis (Steegen et al., 2016), that is, presenting results of multiple justifiable analysis paths, is a valuable tool to test the robustness of the studied effects. Multiverse analysis seems to be especially well suited for neuroscience research, given the multitude of preprocessing and data analysis choices that result in a complex ‘garden of forking paths’ (Gelman and Loken, 2014). As most neuroscience studies test only one analysis variant it is difficult to assess the robustness of any individual effect, and it seems that at least some neuroscientific findings are sensitive to the choice of signal analysis steps (Cohen, 2015; Cohen and Gulbinaite, 2014; see also Botvinik-Nezer et al., 2019).

The purpose of this article is to thoroughly test the robustness and credibility of FAA as a marker of DDs and address the limitations of FAA research methodology by performing a multiverse analysis of data coming from five independent studies. We performed 270 analyses in total differing in: (a) the signal space used (channel space vs source space); (b) subselection of the signal space (channel pairs vs all frontal pairs with cluster-based correction); (c) statistical contrast used (group contrasts vs linear regression); (d) statistical control for confounding variables (gender, age and education). Finally we perform analyses on data aggregated across studies and propose additional guidelines to improve quality and reliability of the data analysis in FAA research.

## Results

To investigate the validity and robustness of FAA as a marker of DDs we used the multiverse approach (Steegen et al., 2016) and performed a total of 270 analyses of eyes-closed resting EEG recordings (total N = 388) from five independent studies. These data sets differ in EEG recording equipment, cap layout, and characteristics of subject groups (see Figure 1 and Materials and methods, sections: Participants and Electrophysiological data sets).

![Figure 1.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig1-v1.jpg)

**Figure 1.:** (A) Number of participants for each study and group (see Table 12 for details). (B) Stacked histograms showing the distribution of BDI or PHQ-9 scores in each study and each group. (C) Channel montage. Frontal channels used in cluster-based analyses are marked with gray dots. Channels used in channel-pairs analysis are marked with teal dots (F3–F4, F7–F8, and corresponding channels in the EGI montage). (D) Rest period length and scheme.

The analysis variants making up the multiverse analysis can be classified along four major dimensions (Figure 2): (a) statistical contrast used: group comparisons or testing for a linear relationship, (b) the signal space used: channel space (average reference – AVG: 120 analyses, 44%; current source density reference – CSD: 120, 44%) or source space (DICS beamforming, 30, 11%); (c) subselection of the signal space: channel pairs (120, 44%), all frontal pairs with cluster correction (60, 22%) or all frontal channels with cluster-based correction and standardization instead of subtraction (60, 22%; see Signal analysis section); and (d) statistical control for confounding variables (135 without and 135 with control for confounds).

![Figure 2.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig2-v1.jpg)

**Figure 2.:** (A) Schematic depiction of given statistical contrast: group comparisons (left) vs regression (right). (B) Specification of each contrast against depression scores. Left panel shows a schematic range of depression scores for each contrast: diagnosed vs healthy controls (DvsHC) and sub-clinical vs healthy controls (SvsHC). Right panel shows the range of depression scores for data included in each linear contrast: regression on diagnosed subjects (DReg) uses only subjects with clinical diagnosis, while regression on all subjects (allReg) uses all subject groups. The color legend for the subject groups is presented below these figures. (C) Analysis space: AVG – channel level, average reference; CSD – channel level, current source density; SRC – source level, DICS beamforming. (D) Schematic depiction of analysis method: selected channel pairs versus all frontal channels with cluster-based correction for multiple comparisons.

We used four different statistical contrasts in the analyses: two group contrasts using independent t-tests to compare FAA between groups; and two linear contrasts using linear regression to test the relationship between psychometric depression score and FAA. Group contrasts included: comparison between diagnosed and healthy controls (DvsHC) or sub-clinical and healthy controls (SvsHC). The inclusion of SvcHC contrast is motivated by the fact that in some FAA studies depression is not diagnosed by conducting a structured clinical interview – instead groups are created based on score thresholds from psychometric depression questionnaires (for example, De Raedt et al., 2008; Imperatori et al., 2019; Schaffer et al., 1983). For group contrasts we used Welch t-test, which does not assume equal variance of the compared groups (Delacre et al., 2017). Linear contrasts were performed either for all subjects together (allReg) or only for the diagnosed subjects (DReg). allReg contrast quantifies the linear relationship between FAA and BDI across all participants while DReg contrast tests whether FAA increases with depression severity measured with BDI questionnaire (or PHQ-9 in Study V).

Combining all the analytical pathways (studies × statistical contrasts × analysis spaces × analysis approaches × control for confounds) leads to 270 analyses, the results of these analyses are summarized in Tables 1–8.

**Table 1.**
 Results for all channel-pair analyses.Each row represents two channel-pair results for a given contrast, study, and space combination; uncorrected for multiple comparisons. Electrode placement for each study is shown in Figure 1C. (N: number of participants included in given contrast; ES: effect size; Cohen’s d for group comparison and Pearson’s r for regression; CI: bootstrap 95% confidence interval for the effect size).


<table>
  <thead>
    <tr>
      <th rowspan="3">No.</th>
      <th rowspan="3">Contrast</th>
      <th rowspan="3">Study</th>
      <th rowspan="3">Space</th>
      <th rowspan="3">N</th>
      <th colspan="8">Selected electrodes without correction</th>
    </tr>
    <tr>
      <th colspan="4">Pair 1 (F3–F4)</th>
      <th colspan="4">Pair 2 (F7–F8)</th>
    </tr>
    <tr>
      <th>t</th>
      <th>p</th>
      <th>ES</th>
      <th>CI</th>
      <th>t</th>
      <th>p</th>
      <th>ES</th>
      <th>CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>avg</td>
      <td>29 vs 22</td>
      <td>−2.073</td>
      <td>0.043</td>
      <td>−0.573</td>
      <td>[−1.135,–0.024]</td>
      <td>−0.365</td>
      <td>0.717</td>
      <td>−0.101</td>
      <td>[−0.644, 0.465]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>csd</td>
      <td>29 vs 22</td>
      <td>0.132</td>
      <td>0.896</td>
      <td>0.038</td>
      <td>[−0.550, 0.608]</td>
      <td>0.553</td>
      <td>0.583</td>
      <td>0.153</td>
      <td>[−0.415, 0.689]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>27 vs 21</td>
      <td>0.904</td>
      <td>0.371</td>
      <td>0.247</td>
      <td>[−0.316, 0.689]</td>
      <td>−0.536</td>
      <td>0.595</td>
      <td>−0.145</td>
      <td>[−0.760, 0.452]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>27 vs 21</td>
      <td>0.849</td>
      <td>0.401</td>
      <td>0.226</td>
      <td>[−0.307, 0.721]</td>
      <td>−0.129</td>
      <td>0.898</td>
      <td>−0.035</td>
      <td>[−0.590, 0.536]</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>22 vs 72</td>
      <td>0.450</td>
      <td>0.654</td>
      <td>0.094</td>
      <td>[−0.310, 0.510]</td>
      <td>0.277</td>
      <td>0.783</td>
      <td>0.059</td>
      <td>[−0.413, 0.463]</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>22 vs 72</td>
      <td>0.767</td>
      <td>0.449</td>
      <td>0.212</td>
      <td>[−0.287, 0.771]</td>
      <td>−1.396</td>
      <td>0.172</td>
      <td>−0.345</td>
      <td>[−0.808, 0.167]</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>avg</td>
      <td>24 vs 29</td>
      <td>2.823</td>
      <td>0.007</td>
      <td>0.743</td>
      <td>[0.218, 1.255]</td>
      <td>1.927</td>
      <td>0.061</td>
      <td>0.501</td>
      <td>[−0.023, 0.998]</td>
    </tr>
    <tr>
      <td>8</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>csd</td>
      <td>24 vs 29</td>
      <td>0.748</td>
      <td>0.458</td>
      <td>0.208</td>
      <td>[−0.380, 0.775]</td>
      <td>−0.727</td>
      <td>0.471</td>
      <td>−0.202</td>
      <td>[−0.766, 0.370]</td>
    </tr>
    <tr>
      <td>9</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>avg</td>
      <td>23 vs 28</td>
      <td>0.201</td>
      <td>0.841</td>
      <td>0.056</td>
      <td>[−0.502, 0.614]</td>
      <td>−0.662</td>
      <td>0.511</td>
      <td>−0.179</td>
      <td>[−0.780, 0.381]</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>csd</td>
      <td>23 vs 28</td>
      <td>1.144</td>
      <td>0.258</td>
      <td>0.318</td>
      <td>[−0.221, 0.827]</td>
      <td>−0.199</td>
      <td>0.843</td>
      <td>−0.054</td>
      <td>[−0.611, 0.508]</td>
    </tr>
    <tr>
      <td>11</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>33 vs 21</td>
      <td>−0.852</td>
      <td>0.398</td>
      <td>−0.209</td>
      <td>[−0.640, 0.306]</td>
      <td>−1.328</td>
      <td>0.190</td>
      <td>−0.332</td>
      <td>[−0.804, 0.216]</td>
    </tr>
    <tr>
      <td>12</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>33 vs 21</td>
      <td>−1.181</td>
      <td>0.244</td>
      <td>−0.280</td>
      <td>[−0.730, 0.219]</td>
      <td>−1.094</td>
      <td>0.280</td>
      <td>−0.302</td>
      <td>[−0.798, 0.219]</td>
    </tr>
    <tr>
      <td>13</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>21 vs 72</td>
      <td>1.359</td>
      <td>0.184</td>
      <td>0.346</td>
      <td>[−0.198, 0.816]</td>
      <td>1.247</td>
      <td>0.219</td>
      <td>0.254</td>
      <td>[−0.138, 0.646]</td>
    </tr>
    <tr>
      <td>14</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>21 vs 72</td>
      <td>0.558</td>
      <td>0.581</td>
      <td>0.147</td>
      <td>[−0.393, 0.655]</td>
      <td>0.141</td>
      <td>0.889</td>
      <td>0.035</td>
      <td>[−0.388, 0.605]</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>I</td>
      <td>avg</td>
      <td>54</td>
      <td>−1.138</td>
      <td>0.260</td>
      <td>−0.156</td>
      <td>[−0.397, 0.088]</td>
      <td>−0.180</td>
      <td>0.858</td>
      <td>−0.025</td>
      <td>[−0.394, 0.258]</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>I</td>
      <td>csd</td>
      <td>54</td>
      <td>−0.540</td>
      <td>0.591</td>
      <td>−0.075</td>
      <td>[−0.309, 0.167]</td>
      <td>0.077</td>
      <td>0.939</td>
      <td>0.011</td>
      <td>[−0.335, 0.280]</td>
    </tr>
    <tr>
      <td>17</td>
      <td>allReg</td>
      <td>III</td>
      <td>avg</td>
      <td>91</td>
      <td>0.545</td>
      <td>0.587</td>
      <td>0.058</td>
      <td>[−0.105, 0.263]</td>
      <td>−0.781</td>
      <td>0.437</td>
      <td>−0.083</td>
      <td>[−0.271, 0.101]</td>
    </tr>
    <tr>
      <td>18</td>
      <td>allReg</td>
      <td>III</td>
      <td>csd</td>
      <td>91</td>
      <td>0.209</td>
      <td>0.835</td>
      <td>0.022</td>
      <td>[−0.169, 0.207]</td>
      <td>0.422</td>
      <td>0.674</td>
      <td>0.045</td>
      <td>[−0.168, 0.225]</td>
    </tr>
    <tr>
      <td>19</td>
      <td>allReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>117</td>
      <td>1.138</td>
      <td>0.258</td>
      <td>0.106</td>
      <td>[−0.076, 0.264]</td>
      <td>0.675</td>
      <td>0.501</td>
      <td>0.063</td>
      <td>[−0.111, 0.212]</td>
    </tr>
    <tr>
      <td>20</td>
      <td>allReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>117</td>
      <td>1.307</td>
      <td>0.194</td>
      <td>0.121</td>
      <td>[−0.096, 0.312]</td>
      <td>−1.024</td>
      <td>0.308</td>
      <td>−0.095</td>
      <td>[−0.265, 0.093]</td>
    </tr>
    <tr>
      <td>21</td>
      <td>allReg</td>
      <td>V</td>
      <td>avg</td>
      <td>53</td>
      <td>2.489</td>
      <td>0.016</td>
      <td>0.329</td>
      <td>[0.106, 0.517]</td>
      <td>1.463</td>
      <td>0.150</td>
      <td>0.201</td>
      <td>[−0.023, 0.409]</td>
    </tr>
    <tr>
      <td>22</td>
      <td>allReg</td>
      <td>V</td>
      <td>csd</td>
      <td>53</td>
      <td>0.857</td>
      <td>0.395</td>
      <td>0.119</td>
      <td>[−0.127, 0.361]</td>
      <td>−0.220</td>
      <td>0.827</td>
      <td>−0.031</td>
      <td>[−0.262, 0.210]</td>
    </tr>
    <tr>
      <td>23</td>
      <td>DReg</td>
      <td>I</td>
      <td>avg</td>
      <td>29</td>
      <td>0.980</td>
      <td>0.336</td>
      <td>0.185</td>
      <td>[−0.212, 0.531]</td>
      <td>0.320</td>
      <td>0.751</td>
      <td>0.061</td>
      <td>[−0.470, 0.522]</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DReg</td>
      <td>I</td>
      <td>csd</td>
      <td>29</td>
      <td>−1.303</td>
      <td>0.204</td>
      <td>−0.243</td>
      <td>[−0.540, 0.091]</td>
      <td>−0.504</td>
      <td>0.618</td>
      <td>−0.097</td>
      <td>[−0.501, 0.337]</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DReg</td>
      <td>III</td>
      <td>avg</td>
      <td>27</td>
      <td>0.278</td>
      <td>0.784</td>
      <td>0.055</td>
      <td>[−0.268, 0.426]</td>
      <td>0.055</td>
      <td>0.957</td>
      <td>0.011</td>
      <td>[−0.273, 0.238]</td>
    </tr>
    <tr>
      <td>26</td>
      <td>DReg</td>
      <td>III</td>
      <td>csd</td>
      <td>27</td>
      <td>0.407</td>
      <td>0.688</td>
      <td>0.081</td>
      <td>[−0.254, 0.413]</td>
      <td>1.347</td>
      <td>0.190</td>
      <td>0.260</td>
      <td>[−0.047, 0.498]</td>
    </tr>
    <tr>
      <td>27</td>
      <td>DReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>22</td>
      <td>1.754</td>
      <td>0.095</td>
      <td>0.365</td>
      <td>[0.012, 0.643]</td>
      <td>−0.114</td>
      <td>0.910</td>
      <td>−0.026</td>
      <td>[−0.459, 0.427]</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>22</td>
      <td>1.938</td>
      <td>0.067</td>
      <td>0.398</td>
      <td>[−0.043, 0.632]</td>
      <td>−0.415</td>
      <td>0.683</td>
      <td>−0.092</td>
      <td>[−0.519, 0.351]</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DReg</td>
      <td>V</td>
      <td>avg</td>
      <td>24</td>
      <td>1.497</td>
      <td>0.149</td>
      <td>0.304</td>
      <td>[0.045, 0.563]</td>
      <td>−0.367</td>
      <td>0.717</td>
      <td>−0.078</td>
      <td>[−0.444, 0.285]</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DReg</td>
      <td>V</td>
      <td>csd</td>
      <td>24</td>
      <td>0.789</td>
      <td>0.438</td>
      <td>0.166</td>
      <td>[−0.264, 0.501]</td>
      <td>0.635</td>
      <td>0.532</td>
      <td>0.134</td>
      <td>[−0.320, 0.615]</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

**Table 2.**
 Results for all channel-pair analyses corrected for confounds.Each row represents two channel-pair results for a given contrast, study, and space combination; uncorrected for multiple comparisons. Electrode placement for each study is shown in Figure 1C. (N: number of participants included in given contrast; ES: effect size; Cohen’s d for group comparison and Pearson’s r for regression; CI: bootstrap 95% confidence interval for the effect size).


<table>
  <thead>
    <tr>
      <th rowspan="3">No.</th>
      <th rowspan="3">Contrast</th>
      <th rowspan="3">Study</th>
      <th rowspan="3">Space</th>
      <th rowspan="3">N</th>
      <th colspan="8">Selected electrodes corrected for confounds</th>
    </tr>
    <tr>
      <th colspan="4">Pair 1 (F3–F4)</th>
      <th colspan="4">Pair 2 (F7–F8)</th>
    </tr>
    <tr>
      <th>t</th>
      <th>p</th>
      <th>ES</th>
      <th>CI</th>
      <th>t</th>
      <th>p</th>
      <th>ES</th>
      <th>CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>avg</td>
      <td>29 vs 22</td>
      <td>−2.679</td>
      <td>0.010</td>
      <td>−0.789</td>
      <td>[−1.413,–0.218]</td>
      <td>−0.782</td>
      <td>0.438</td>
      <td>−0.230</td>
      <td>[−0.691, 0.288]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>csd</td>
      <td>29 vs 22</td>
      <td>0.269</td>
      <td>0.789</td>
      <td>0.079</td>
      <td>[−0.501, 0.681]</td>
      <td>0.305</td>
      <td>0.762</td>
      <td>0.090</td>
      <td>[−0.404, 0.622]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>27 vs 21</td>
      <td>0.204</td>
      <td>0.839</td>
      <td>0.064</td>
      <td>[−0.642, 0.684]</td>
      <td>−1.161</td>
      <td>0.252</td>
      <td>−0.366</td>
      <td>[−0.994, 0.310]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>27 vs 21</td>
      <td>−0.162</td>
      <td>0.872</td>
      <td>−0.051</td>
      <td>[−0.691, 0.547]</td>
      <td>−0.703</td>
      <td>0.486</td>
      <td>−0.221</td>
      <td>[−0.998, 0.558]</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>22 vs 71</td>
      <td>0.310</td>
      <td>0.757</td>
      <td>0.077</td>
      <td>[−0.338, 0.504]</td>
      <td>0.085</td>
      <td>0.933</td>
      <td>0.021</td>
      <td>[−0.412, 0.450]</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>22 vs 71</td>
      <td>0.978</td>
      <td>0.331</td>
      <td>0.244</td>
      <td>[−0.250, 0.816]</td>
      <td>−1.484</td>
      <td>0.141</td>
      <td>−0.370</td>
      <td>[−0.842, 0.135]</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>avg</td>
      <td>24 vs 29</td>
      <td>1.862</td>
      <td>0.069</td>
      <td>0.540</td>
      <td>[0.033, 1.044]</td>
      <td>1.817</td>
      <td>0.075</td>
      <td>0.527</td>
      <td>[−0.008, 1.101]</td>
    </tr>
    <tr>
      <td>8</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>csd</td>
      <td>24 vs 29</td>
      <td>0.518</td>
      <td>0.607</td>
      <td>0.150</td>
      <td>[−0.415, 0.742]</td>
      <td>−0.722</td>
      <td>0.474</td>
      <td>−0.209</td>
      <td>[−0.689, 0.235]</td>
    </tr>
    <tr>
      <td>9</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>avg</td>
      <td>23 vs 28</td>
      <td>0.351</td>
      <td>0.728</td>
      <td>0.105</td>
      <td>[−0.444, 0.746]</td>
      <td>−0.654</td>
      <td>0.516</td>
      <td>−0.196</td>
      <td>[−0.883, 0.450]</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>csd</td>
      <td>23 vs 28</td>
      <td>1.293</td>
      <td>0.203</td>
      <td>0.387</td>
      <td>[−0.152, 0.943]</td>
      <td>0.035</td>
      <td>0.972</td>
      <td>0.010</td>
      <td>[−0.653, 0.532]</td>
    </tr>
    <tr>
      <td>11</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>33 vs 21</td>
      <td>−1.169</td>
      <td>0.248</td>
      <td>−0.350</td>
      <td>[−0.946, 0.285]</td>
      <td>−1.768</td>
      <td>0.084</td>
      <td>−0.529</td>
      <td>[−1.071, 0.029]</td>
    </tr>
    <tr>
      <td>12</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>33 vs 21</td>
      <td>−1.382</td>
      <td>0.173</td>
      <td>−0.414</td>
      <td>[−1.086, 0.160]</td>
      <td>−1.197</td>
      <td>0.237</td>
      <td>−0.358</td>
      <td>[−0.997, 0.212]</td>
    </tr>
    <tr>
      <td>13</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>21 vs 71</td>
      <td>1.058</td>
      <td>0.293</td>
      <td>0.269</td>
      <td>[−0.232, 0.776]</td>
      <td>0.466</td>
      <td>0.642</td>
      <td>0.118</td>
      <td>[−0.293, 0.515]</td>
    </tr>
    <tr>
      <td>14</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>21 vs 71</td>
      <td>0.739</td>
      <td>0.462</td>
      <td>0.188</td>
      <td>[−0.302, 0.649]</td>
      <td>−0.263</td>
      <td>0.793</td>
      <td>−0.067</td>
      <td>[−0.524, 0.483]</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>I</td>
      <td>avg</td>
      <td>54</td>
      <td>−1.352</td>
      <td>0.182</td>
      <td>−0.188</td>
      <td>[−0.440, 0.078]</td>
      <td>−0.349</td>
      <td>0.728</td>
      <td>−0.049</td>
      <td>[−0.369, 0.240]</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>I</td>
      <td>csd</td>
      <td>54</td>
      <td>−0.431</td>
      <td>0.668</td>
      <td>−0.061</td>
      <td>[−0.313, 0.187]</td>
      <td>−0.019</td>
      <td>0.985</td>
      <td>−0.003</td>
      <td>[−0.335, 0.304]</td>
    </tr>
    <tr>
      <td>17</td>
      <td>allReg</td>
      <td>III</td>
      <td>avg</td>
      <td>91</td>
      <td>0.233</td>
      <td>0.816</td>
      <td>0.025</td>
      <td>[−0.156, 0.263]</td>
      <td>−1.170</td>
      <td>0.245</td>
      <td>−0.127</td>
      <td>[−0.313, 0.092]</td>
    </tr>
    <tr>
      <td>18</td>
      <td>allReg</td>
      <td>III</td>
      <td>csd</td>
      <td>91</td>
      <td>−0.005</td>
      <td>0.996</td>
      <td>−0.001</td>
      <td>[−0.190, 0.204]</td>
      <td>−0.060</td>
      <td>0.953</td>
      <td>−0.007</td>
      <td>[−0.238, 0.224]</td>
    </tr>
    <tr>
      <td>19</td>
      <td>allReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>116</td>
      <td>0.904</td>
      <td>0.368</td>
      <td>0.085</td>
      <td>[−0.088, 0.237]</td>
      <td>0.355</td>
      <td>0.723</td>
      <td>0.034</td>
      <td>[−0.139, 0.197]</td>
    </tr>
    <tr>
      <td>20</td>
      <td>allReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>116</td>
      <td>1.461</td>
      <td>0.147</td>
      <td>0.137</td>
      <td>[−0.064, 0.316]</td>
      <td>−1.300</td>
      <td>0.196</td>
      <td>−0.122</td>
      <td>[−0.296, 0.059]</td>
    </tr>
    <tr>
      <td>21</td>
      <td>allReg</td>
      <td>V</td>
      <td>avg</td>
      <td>53</td>
      <td>1.685</td>
      <td>0.099</td>
      <td>0.236</td>
      <td>[−0.014, 0.449]</td>
      <td>1.544</td>
      <td>0.129</td>
      <td>0.218</td>
      <td>[−0.034, 0.433]</td>
    </tr>
    <tr>
      <td>22</td>
      <td>allReg</td>
      <td>V</td>
      <td>csd</td>
      <td>53</td>
      <td>0.769</td>
      <td>0.446</td>
      <td>0.110</td>
      <td>[−0.148, 0.339]</td>
      <td>−0.058</td>
      <td>0.954</td>
      <td>−0.008</td>
      <td>[−0.214, 0.185]</td>
    </tr>
    <tr>
      <td>23</td>
      <td>DReg</td>
      <td>I</td>
      <td>avg</td>
      <td>29</td>
      <td>0.767</td>
      <td>0.450</td>
      <td>0.152</td>
      <td>[−0.324, 0.503]</td>
      <td>0.265</td>
      <td>0.793</td>
      <td>0.053</td>
      <td>[−0.452, 0.564]</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DReg</td>
      <td>I</td>
      <td>csd</td>
      <td>29</td>
      <td>−1.273</td>
      <td>0.215</td>
      <td>−0.247</td>
      <td>[−0.588, 0.156]</td>
      <td>−0.506</td>
      <td>0.617</td>
      <td>−0.101</td>
      <td>[−0.504, 0.437]</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DReg</td>
      <td>III</td>
      <td>avg</td>
      <td>27</td>
      <td>−0.054</td>
      <td>0.958</td>
      <td>−0.012</td>
      <td>[−0.434, 0.485]</td>
      <td>−0.079</td>
      <td>0.937</td>
      <td>−0.018</td>
      <td>[−0.425, 0.346]</td>
    </tr>
    <tr>
      <td>26</td>
      <td>DReg</td>
      <td>III</td>
      <td>csd</td>
      <td>27</td>
      <td>0.055</td>
      <td>0.957</td>
      <td>0.012</td>
      <td>[−0.407, 0.408]</td>
      <td>1.375</td>
      <td>0.184</td>
      <td>0.294</td>
      <td>[−0.096, 0.614]</td>
    </tr>
    <tr>
      <td>27</td>
      <td>DReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>22</td>
      <td>1.979</td>
      <td>0.063</td>
      <td>0.423</td>
      <td>[−0.001, 0.719]</td>
      <td>−0.062</td>
      <td>0.951</td>
      <td>−0.015</td>
      <td>[−0.409, 0.473]</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>22</td>
      <td>1.761</td>
      <td>0.095</td>
      <td>0.383</td>
      <td>[0.004, 0.674]</td>
      <td>−0.269</td>
      <td>0.791</td>
      <td>−0.063</td>
      <td>[−0.538, 0.418]</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DReg</td>
      <td>V</td>
      <td>avg</td>
      <td>24</td>
      <td>0.926</td>
      <td>0.366</td>
      <td>0.208</td>
      <td>[−0.209, 0.565]</td>
      <td>−0.707</td>
      <td>0.488</td>
      <td>−0.160</td>
      <td>[−0.571, 0.278]</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DReg</td>
      <td>V</td>
      <td>csd</td>
      <td>24</td>
      <td>0.723</td>
      <td>0.478</td>
      <td>0.164</td>
      <td>[−0.345, 0.554]</td>
      <td>0.298</td>
      <td>0.769</td>
      <td>0.068</td>
      <td>[−0.569, 0.735]</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

**Table 3.**
 Results for cluster-based permutation test on frontal asymmetry space.Each row represents cluster-based results for a given contrast, study, and space combination (N: number of participants included in given contrast; min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster size: number of channels participating in the cluster; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis).


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">Study</th>
      <th rowspan="2">Space</th>
      <th rowspan="2">N</th>
      <th colspan="6">Cluster-based permutation test on frontal asymmetry space</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>avg</td>
      <td>29 vs 22</td>
      <td>−2.110</td>
      <td>0.023</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>0.069</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>csd</td>
      <td>29 vs 22</td>
      <td>−0.720</td>
      <td>1.983</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>27 vs 21</td>
      <td>−1.172</td>
      <td>1.058</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>27 vs 21</td>
      <td>−1.258</td>
      <td>1.875</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>22 vs 72</td>
      <td>−0.751</td>
      <td>2.069</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.345</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>22 vs 72</td>
      <td>−1.600</td>
      <td>1.142</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>avg</td>
      <td>24 vs 29</td>
      <td>−1.260</td>
      <td>2.823</td>
      <td>6</td>
      <td>2</td>
      <td>5</td>
      <td>0.026</td>
    </tr>
    <tr>
      <td>8</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>csd</td>
      <td>24 vs 29</td>
      <td>−2.901</td>
      <td>1.425</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0.156</td>
    </tr>
    <tr>
      <td>9</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>avg</td>
      <td>23 vs 28</td>
      <td>−2.581</td>
      <td>0.201</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.164z</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>csd</td>
      <td>23 vs 28</td>
      <td>−0.855</td>
      <td>1.254</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>11</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>33 vs 21</td>
      <td>−1.410</td>
      <td>1.021</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>12</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>33 vs 21</td>
      <td>−2.315</td>
      <td>2.101</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0.227</td>
    </tr>
    <tr>
      <td>13</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>21 vs 72</td>
      <td>−1.356</td>
      <td>2.760</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0.052</td>
    </tr>
    <tr>
      <td>14</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>21 vs 72</td>
      <td>−1.193</td>
      <td>1.296</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>I</td>
      <td>avg</td>
      <td>54</td>
      <td>−1.519</td>
      <td>0.022</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>I</td>
      <td>csd</td>
      <td>54</td>
      <td>−0.727</td>
      <td>1.052</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>17</td>
      <td>allReg</td>
      <td>III</td>
      <td>avg</td>
      <td>91</td>
      <td>−1.207</td>
      <td>0.906</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>18</td>
      <td>allReg</td>
      <td>III</td>
      <td>csd</td>
      <td>91</td>
      <td>−1.290</td>
      <td>2.210</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.287</td>
    </tr>
    <tr>
      <td>19</td>
      <td>allReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>117</td>
      <td>−1.807</td>
      <td>2.153</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.202</td>
    </tr>
    <tr>
      <td>20</td>
      <td>allReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>117</td>
      <td>−1.173</td>
      <td>1.353</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>21</td>
      <td>allReg</td>
      <td>V</td>
      <td>avg</td>
      <td>53</td>
      <td>−1.001</td>
      <td>2.489</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>0.077</td>
    </tr>
    <tr>
      <td>22</td>
      <td>allReg</td>
      <td>V</td>
      <td>csd</td>
      <td>53</td>
      <td>−3.291</td>
      <td>1.552</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0.187</td>
    </tr>
    <tr>
      <td>23</td>
      <td>DReg</td>
      <td>I</td>
      <td>avg</td>
      <td>29</td>
      <td>−0.159</td>
      <td>1.552</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DReg</td>
      <td>I</td>
      <td>csd</td>
      <td>29</td>
      <td>−1.303</td>
      <td>0.487</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DReg</td>
      <td>III</td>
      <td>avg</td>
      <td>27</td>
      <td>−2.041</td>
      <td>0.976</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>26</td>
      <td>DReg</td>
      <td>III</td>
      <td>csd</td>
      <td>27</td>
      <td>−1.420</td>
      <td>1.662</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>27</td>
      <td>DReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>22</td>
      <td>−1.155</td>
      <td>1.754</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>22</td>
      <td>−0.415</td>
      <td>1.938</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DReg</td>
      <td>V</td>
      <td>avg</td>
      <td>24</td>
      <td>−1.482</td>
      <td>1.497</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DReg</td>
      <td>V</td>
      <td>csd</td>
      <td>24</td>
      <td>−2.254</td>
      <td>1.554</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.555</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

**Table 4.**
 Results for cluster-based permutation test on frontal asymmetry space corrected for confounds.Each row represents cluster-based results for a given contrast, study and space combination (N: number of participants included in given contrast; min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster size: number of channels participating in the cluster; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis).


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">Study</th>
      <th rowspan="2">Space</th>
      <th rowspan="2">N</th>
      <th colspan="6">Cluster-based permutation test on frontal asymmetry space corrected for confounds</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>avg</td>
      <td>29 vs 22</td>
      <td>−2.679</td>
      <td>−0.149</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>0.023</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>csd</td>
      <td>29 vs 22</td>
      <td>−1.020</td>
      <td>1.591</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>27 vs 21</td>
      <td>−1.506</td>
      <td>1.361</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>27 vs 21</td>
      <td>−1.310</td>
      <td>1.378</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>22 vs 71</td>
      <td>−0.814</td>
      <td>1.812</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>22 vs 71</td>
      <td>−1.812</td>
      <td>0.978</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>avg</td>
      <td>24 vs 29</td>
      <td>−1.618</td>
      <td>2.341</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>0.327</td>
    </tr>
    <tr>
      <td>8</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>csd</td>
      <td>24 vs 29</td>
      <td>−3.017</td>
      <td>0.738</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0.205</td>
    </tr>
    <tr>
      <td>9</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>avg</td>
      <td>23 vs 28</td>
      <td>−2.622</td>
      <td>0.351</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.177</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>csd</td>
      <td>23 vs 28</td>
      <td>−0.838</td>
      <td>1.742</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>11</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>33 vs 21</td>
      <td>−1.768</td>
      <td>1.218</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>12</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>33 vs 21</td>
      <td>−2.090</td>
      <td>1.899</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.358</td>
    </tr>
    <tr>
      <td>13</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>21 vs 71</td>
      <td>−1.584</td>
      <td>1.490</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>14</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>21 vs 71</td>
      <td>−1.400</td>
      <td>0.739</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>I</td>
      <td>avg</td>
      <td>54</td>
      <td>−1.726</td>
      <td>0.039</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>I</td>
      <td>csd</td>
      <td>54</td>
      <td>−0.816</td>
      <td>0.987</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>17</td>
      <td>allReg</td>
      <td>III</td>
      <td>avg</td>
      <td>91</td>
      <td>−1.231</td>
      <td>0.722</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>18</td>
      <td>allReg</td>
      <td>III</td>
      <td>csd</td>
      <td>91</td>
      <td>−1.540</td>
      <td>2.119</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.335</td>
    </tr>
    <tr>
      <td>19</td>
      <td>allReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>116</td>
      <td>−1.804</td>
      <td>1.852</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>20</td>
      <td>allReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>116</td>
      <td>−1.300</td>
      <td>1.461</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>21</td>
      <td>allReg</td>
      <td>V</td>
      <td>avg</td>
      <td>53</td>
      <td>−1.286</td>
      <td>2.350</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.324</td>
    </tr>
    <tr>
      <td>22</td>
      <td>allReg</td>
      <td>V</td>
      <td>csd</td>
      <td>53</td>
      <td>−3.541</td>
      <td>0.832</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0.173</td>
    </tr>
    <tr>
      <td>23</td>
      <td>DReg</td>
      <td>I</td>
      <td>avg</td>
      <td>29</td>
      <td>−0.244</td>
      <td>1.516</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DReg</td>
      <td>I</td>
      <td>csd</td>
      <td>29</td>
      <td>−1.291</td>
      <td>0.565</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DReg</td>
      <td>III</td>
      <td>avg</td>
      <td>27</td>
      <td>−1.700</td>
      <td>0.852</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>26</td>
      <td>DReg</td>
      <td>III</td>
      <td>csd</td>
      <td>27</td>
      <td>−1.311</td>
      <td>1.574</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>27</td>
      <td>DReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>22</td>
      <td>−1.173</td>
      <td>2.728</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.121</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>22</td>
      <td>−0.269</td>
      <td>2.235</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.260</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DReg</td>
      <td>V</td>
      <td>avg</td>
      <td>24</td>
      <td>−1.593</td>
      <td>0.926</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DReg</td>
      <td>V</td>
      <td>csd</td>
      <td>24</td>
      <td>−2.075</td>
      <td>2.586</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>0.376</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

**Table 5.**
 Results for all cluster-based analyses on standardized data.Each row represents cluster-based results for given contrast, study, and space (N: number of participants included in given contrast). Results for cluster-based permutation test on frontal asymmetry space (min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster size: number of channels by frequency points participating in the cluster; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis).


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">Study</th>
      <th rowspan="2">Space</th>
      <th rowspan="2">N</th>
      <th colspan="6">Cluster-based analyses on standardized data</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>avg</td>
      <td>29 vs 22</td>
      <td>−1.453</td>
      <td>1.434</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>csd</td>
      <td>29 vs 22</td>
      <td>−2.227</td>
      <td>1.879</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>0.718</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>27 vs 21</td>
      <td>−1.999</td>
      <td>2.326</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0.468</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>27 vs 21</td>
      <td>−2.917</td>
      <td>3.882</td>
      <td>23</td>
      <td>3</td>
      <td>16</td>
      <td>0.063</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>22 vs 72</td>
      <td>−4.256</td>
      <td>3.053</td>
      <td>129</td>
      <td>2</td>
      <td>66</td>
      <td>0.007</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>22 vs 72</td>
      <td>−3.180</td>
      <td>2.582</td>
      <td>22</td>
      <td>7</td>
      <td>6</td>
      <td>0.259</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>avg</td>
      <td>24 vs 29</td>
      <td>−2.516</td>
      <td>2.267</td>
      <td>21</td>
      <td>3</td>
      <td>15</td>
      <td>0.223</td>
    </tr>
    <tr>
      <td>8</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>csd</td>
      <td>24 vs 29</td>
      <td>−2.703</td>
      <td>2.420</td>
      <td>10</td>
      <td>6</td>
      <td>3</td>
      <td>0.723</td>
    </tr>
    <tr>
      <td>9</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>avg</td>
      <td>23 vs 28</td>
      <td>−1.685</td>
      <td>2.185</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.774</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>csd</td>
      <td>23 vs 28</td>
      <td>−2.059</td>
      <td>1.714</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.941</td>
    </tr>
    <tr>
      <td>11</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>33 vs 21</td>
      <td>−1.906</td>
      <td>1.946</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>12</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>33 vs 21</td>
      <td>−2.284</td>
      <td>3.091</td>
      <td>7</td>
      <td>4</td>
      <td>3</td>
      <td>0.577</td>
    </tr>
    <tr>
      <td>13</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>21 vs 72</td>
      <td>−2.319</td>
      <td>2.519</td>
      <td>19</td>
      <td>5</td>
      <td>5</td>
      <td>0.306</td>
    </tr>
    <tr>
      <td>14</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>21 vs 72</td>
      <td>−2.950</td>
      <td>3.130</td>
      <td>25</td>
      <td>4</td>
      <td>11</td>
      <td>0.092</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>I</td>
      <td>avg</td>
      <td>54</td>
      <td>−1.295</td>
      <td>1.450</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>I</td>
      <td>csd</td>
      <td>54</td>
      <td>−2.082</td>
      <td>1.899</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>17</td>
      <td>allReg</td>
      <td>III</td>
      <td>avg</td>
      <td>91</td>
      <td>−1.814</td>
      <td>1.949</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>18</td>
      <td>allReg</td>
      <td>III</td>
      <td>csd</td>
      <td>91</td>
      <td>−2.626</td>
      <td>2.547</td>
      <td>14</td>
      <td>4</td>
      <td>6</td>
      <td>0.692</td>
    </tr>
    <tr>
      <td>19</td>
      <td>allReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>117</td>
      <td>−3.406</td>
      <td>2.701</td>
      <td>75</td>
      <td>4</td>
      <td>40</td>
      <td>0.079</td>
    </tr>
    <tr>
      <td>20</td>
      <td>allReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>117</td>
      <td>−2.644</td>
      <td>2.918</td>
      <td>32</td>
      <td>5</td>
      <td>13</td>
      <td>0.179</td>
    </tr>
    <tr>
      <td>21</td>
      <td>allReg</td>
      <td>V</td>
      <td>avg</td>
      <td>53</td>
      <td>−2.752</td>
      <td>2.321</td>
      <td>22</td>
      <td>6</td>
      <td>13</td>
      <td>0.477</td>
    </tr>
    <tr>
      <td>22</td>
      <td>allReg</td>
      <td>V</td>
      <td>csd</td>
      <td>53</td>
      <td>−3.733</td>
      <td>2.023</td>
      <td>15</td>
      <td>6</td>
      <td>5</td>
      <td>0.891</td>
    </tr>
    <tr>
      <td>23</td>
      <td>DReg</td>
      <td>I</td>
      <td>avg</td>
      <td>29</td>
      <td>−2.011</td>
      <td>1.936</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DReg</td>
      <td>I</td>
      <td>csd</td>
      <td>29</td>
      <td>−2.721</td>
      <td>2.093</td>
      <td>8</td>
      <td>5</td>
      <td>3</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DReg</td>
      <td>III</td>
      <td>avg</td>
      <td>27</td>
      <td>−4.167</td>
      <td>3.824</td>
      <td>89</td>
      <td>2</td>
      <td>53</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>26</td>
      <td>DReg</td>
      <td>III</td>
      <td>csd</td>
      <td>27</td>
      <td>−3.525</td>
      <td>3.285</td>
      <td>34</td>
      <td>4</td>
      <td>17</td>
      <td>0.105</td>
    </tr>
    <tr>
      <td>27</td>
      <td>DReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>22</td>
      <td>−1.802</td>
      <td>2.213</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.888</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>22</td>
      <td>−2.219</td>
      <td>2.890</td>
      <td>12</td>
      <td>4</td>
      <td>9</td>
      <td>0.316</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DReg</td>
      <td>V</td>
      <td>avg</td>
      <td>24</td>
      <td>−2.926</td>
      <td>4.155</td>
      <td>58</td>
      <td>7</td>
      <td>18</td>
      <td>0.354</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DReg</td>
      <td>V</td>
      <td>csd</td>
      <td>24</td>
      <td>−3.551</td>
      <td>3.084</td>
      <td>46</td>
      <td>9</td>
      <td>14</td>
      <td>0.387</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

**Table 6.**
 Results for all cluster-based analyses on standardized data corrected for confounds.Each row represents cluster-based results for given contrast, study, and space (N: number of participants included in given contrast). Results for cluster-based permutation test on frontal asymmetry space (min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster size: number of channels by frequency points participating in the cluster; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis).


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">Study</th>
      <th rowspan="2">Space</th>
      <th rowspan="2">N</th>
      <th colspan="6">Cluster-based analyses on standardized data corrected for confounds</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>avg</td>
      <td>29 vs 22</td>
      <td>−1.766</td>
      <td>1.716</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>csd</td>
      <td>29 vs 22</td>
      <td>−2.007</td>
      <td>1.614</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>27 vs 21</td>
      <td>−1.387</td>
      <td>1.896</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>27 vs 21</td>
      <td>−3.345</td>
      <td>3.054</td>
      <td>17</td>
      <td>4</td>
      <td>6</td>
      <td>0.567</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>22 vs 71</td>
      <td>−4.295</td>
      <td>3.304</td>
      <td>143</td>
      <td>2</td>
      <td>72</td>
      <td>0.006</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>22 vs 71</td>
      <td>−3.095</td>
      <td>2.854</td>
      <td>33</td>
      <td>5</td>
      <td>12</td>
      <td>0.179</td>
    </tr>
    <tr>
      <td>7</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>avg</td>
      <td>24 vs 29</td>
      <td>−1.982</td>
      <td>1.976</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>8</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>csd</td>
      <td>24 vs 29</td>
      <td>−2.026</td>
      <td>2.798</td>
      <td>10</td>
      <td>4</td>
      <td>7</td>
      <td>0.772</td>
    </tr>
    <tr>
      <td>9</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>avg</td>
      <td>23 vs 28</td>
      <td>−1.511</td>
      <td>1.841</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>10</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>csd</td>
      <td>23 vs 28</td>
      <td>−2.059</td>
      <td>1.876</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>11</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>avg</td>
      <td>33 vs 21</td>
      <td>−2.964</td>
      <td>2.422</td>
      <td>22</td>
      <td>5</td>
      <td>10</td>
      <td>0.374</td>
    </tr>
    <tr>
      <td>12</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>csd</td>
      <td>33 vs 21</td>
      <td>−2.424</td>
      <td>3.562</td>
      <td>12</td>
      <td>4</td>
      <td>4</td>
      <td>0.865</td>
    </tr>
    <tr>
      <td>13</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>avg</td>
      <td>21 vs 71</td>
      <td>−2.667</td>
      <td>2.858</td>
      <td>34</td>
      <td>3</td>
      <td>31</td>
      <td>0.113</td>
    </tr>
    <tr>
      <td>14</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>csd</td>
      <td>21 vs 71</td>
      <td>−2.389</td>
      <td>3.317</td>
      <td>23</td>
      <td>3</td>
      <td>10</td>
      <td>0.273</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>I</td>
      <td>avg</td>
      <td>54</td>
      <td>−1.404</td>
      <td>1.614</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>I</td>
      <td>csd</td>
      <td>54</td>
      <td>−1.752</td>
      <td>2.155</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>17</td>
      <td>allReg</td>
      <td>III</td>
      <td>avg</td>
      <td>91</td>
      <td>−2.119</td>
      <td>1.963</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>0.612</td>
    </tr>
    <tr>
      <td>18</td>
      <td>allReg</td>
      <td>III</td>
      <td>csd</td>
      <td>91</td>
      <td>−2.558</td>
      <td>2.825</td>
      <td>25</td>
      <td>3</td>
      <td>17</td>
      <td>0.112</td>
    </tr>
    <tr>
      <td>19</td>
      <td>allReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>116</td>
      <td>−3.414</td>
      <td>3.009</td>
      <td>92</td>
      <td>4</td>
      <td>54</td>
      <td>0.038</td>
    </tr>
    <tr>
      <td>20</td>
      <td>allReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>116</td>
      <td>−2.571</td>
      <td>3.112</td>
      <td>32</td>
      <td>6</td>
      <td>11</td>
      <td>0.216</td>
    </tr>
    <tr>
      <td>21</td>
      <td>allReg</td>
      <td>V</td>
      <td>avg</td>
      <td>53</td>
      <td>−1.942</td>
      <td>2.057</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>22</td>
      <td>allReg</td>
      <td>V</td>
      <td>csd</td>
      <td>53</td>
      <td>−3.005</td>
      <td>2.362</td>
      <td>11</td>
      <td>5</td>
      <td>5</td>
      <td>0.945</td>
    </tr>
    <tr>
      <td>23</td>
      <td>DReg</td>
      <td>I</td>
      <td>avg</td>
      <td>29</td>
      <td>−1.902</td>
      <td>1.990</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>24</td>
      <td>DReg</td>
      <td>I</td>
      <td>csd</td>
      <td>29</td>
      <td>−2.583</td>
      <td>2.088</td>
      <td>9</td>
      <td>5</td>
      <td>4</td>
      <td>0.955</td>
    </tr>
    <tr>
      <td>25</td>
      <td>DReg</td>
      <td>III</td>
      <td>avg</td>
      <td>27</td>
      <td>−3.938</td>
      <td>3.530</td>
      <td>70</td>
      <td>4</td>
      <td>36</td>
      <td>0.073</td>
    </tr>
    <tr>
      <td>26</td>
      <td>DReg</td>
      <td>III</td>
      <td>csd</td>
      <td>27</td>
      <td>−3.198</td>
      <td>4.098</td>
      <td>39</td>
      <td>7</td>
      <td>21</td>
      <td>0.035</td>
    </tr>
    <tr>
      <td>27</td>
      <td>DReg</td>
      <td>IV</td>
      <td>avg</td>
      <td>22</td>
      <td>−2.213</td>
      <td>2.662</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>0.659</td>
    </tr>
    <tr>
      <td>28</td>
      <td>DReg</td>
      <td>IV</td>
      <td>csd</td>
      <td>22</td>
      <td>−3.056</td>
      <td>3.114</td>
      <td>16</td>
      <td>4</td>
      <td>10</td>
      <td>0.265</td>
    </tr>
    <tr>
      <td>29</td>
      <td>DReg</td>
      <td>V</td>
      <td>avg</td>
      <td>24</td>
      <td>−3.200</td>
      <td>4.246</td>
      <td>84</td>
      <td>7</td>
      <td>27</td>
      <td>0.266</td>
    </tr>
    <tr>
      <td>30</td>
      <td>DReg</td>
      <td>V</td>
      <td>csd</td>
      <td>24</td>
      <td>−3.533</td>
      <td>3.378</td>
      <td>78</td>
      <td>7</td>
      <td>36</td>
      <td>0.092</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

**Table 7.**
 Results for all source level analyses.Each row represents source level results for given contrast, study, and space (N: number of participants included in given contrast). Results for cluster-based permutation test on frontal asymmetry source space (min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis).


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">Study</th>
      <th rowspan="2">N</th>
      <th colspan="6">Source level analysis</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>29 vs 22</td>
      <td>−1.906</td>
      <td>2.404</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0.489</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>27 vs 21</td>
      <td>−2.557</td>
      <td>1.158</td>
      <td>29</td>
      <td>4</td>
      <td>14</td>
      <td>0.267</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>22 vs 72</td>
      <td>−3.921</td>
      <td>1.151</td>
      <td>320</td>
      <td>2</td>
      <td>316</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>24 vs 29</td>
      <td>−2.612</td>
      <td>0.943</td>
      <td>24</td>
      <td>1</td>
      <td>24</td>
      <td>0.207</td>
    </tr>
    <tr>
      <td>5</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>23 vs 28</td>
      <td>−0.909</td>
      <td>1.321</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>6</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>34 vs 21</td>
      <td>−1.809</td>
      <td>1.341</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>7</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>21 vs 72</td>
      <td>−2.339</td>
      <td>0.679</td>
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>0.340</td>
    </tr>
    <tr>
      <td>8</td>
      <td>allReg</td>
      <td>I</td>
      <td>54</td>
      <td>−2.319</td>
      <td>1.549</td>
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>0.367</td>
    </tr>
    <tr>
      <td>9</td>
      <td>allReg</td>
      <td>III</td>
      <td>92</td>
      <td>−2.232</td>
      <td>0.290</td>
      <td>21</td>
      <td>2</td>
      <td>20</td>
      <td>0.343</td>
    </tr>
    <tr>
      <td>10</td>
      <td>allReg</td>
      <td>IV</td>
      <td>117</td>
      <td>−2.220</td>
      <td>1.211</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>0.466</td>
    </tr>
    <tr>
      <td>11</td>
      <td>allReg</td>
      <td>V</td>
      <td>53</td>
      <td>−2.644</td>
      <td>1.201</td>
      <td>15</td>
      <td>3</td>
      <td>6</td>
      <td>0.574</td>
    </tr>
    <tr>
      <td>12</td>
      <td>DReg</td>
      <td>I</td>
      <td>29</td>
      <td>−2.292</td>
      <td>1.150</td>
      <td>41</td>
      <td>2</td>
      <td>22</td>
      <td>0.328</td>
    </tr>
    <tr>
      <td>13</td>
      <td>DReg</td>
      <td>III</td>
      <td>27</td>
      <td>−2.624</td>
      <td>−0.375</td>
      <td>26</td>
      <td>3</td>
      <td>18</td>
      <td>0.335</td>
    </tr>
    <tr>
      <td>14</td>
      <td>DReg</td>
      <td>IV</td>
      <td>22</td>
      <td>−1.216</td>
      <td>2.064</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>15</td>
      <td>DReg</td>
      <td>V</td>
      <td>24</td>
      <td>−2.068</td>
      <td>1.758</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects._

**Table 8.**
 Results for all source level analyses corrected for confounds.Each row represents source level results for given contrast, study, and space (N: number of participants included in given contrast) Results for cluster-based permutation test on frontal asymmetry source space (min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis).


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">Study</th>
      <th rowspan="2">N</th>
      <th colspan="6">Source level analysis corrected for confounds</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>I</td>
      <td>29 vs 22</td>
      <td>−1.416</td>
      <td>2.057</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.708</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>III</td>
      <td>27 vs 21</td>
      <td>−2.161</td>
      <td>1.704</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>0.555</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>IV</td>
      <td>22 vs 71</td>
      <td>−3.685</td>
      <td>1.066</td>
      <td>365</td>
      <td>2</td>
      <td>346</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>V</td>
      <td>24 vs 29</td>
      <td>−2.630</td>
      <td>0.287</td>
      <td>64</td>
      <td>3</td>
      <td>46</td>
      <td>0.231</td>
    </tr>
    <tr>
      <td>5</td>
      <td>SvsHC</td>
      <td>II</td>
      <td>23 vs 28</td>
      <td>−0.814</td>
      <td>1.911</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>6</td>
      <td>SvsHC</td>
      <td>III</td>
      <td>34 vs 21</td>
      <td>−1.770</td>
      <td>1.526</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>7</td>
      <td>SvsHC</td>
      <td>IV</td>
      <td>21 vs 71</td>
      <td>−2.732</td>
      <td>−0.083</td>
      <td>58</td>
      <td>1</td>
      <td>58</td>
      <td>0.192</td>
    </tr>
    <tr>
      <td>8</td>
      <td>allReg</td>
      <td>I</td>
      <td>54</td>
      <td>−1.846</td>
      <td>1.143</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>9</td>
      <td>allReg</td>
      <td>III</td>
      <td>92</td>
      <td>−2.195</td>
      <td>0.698</td>
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>0.391</td>
    </tr>
    <tr>
      <td>10</td>
      <td>allReg</td>
      <td>IV</td>
      <td>116</td>
      <td>−2.313</td>
      <td>0.910</td>
      <td>44</td>
      <td>4</td>
      <td>19</td>
      <td>0.375</td>
    </tr>
    <tr>
      <td>11</td>
      <td>allReg</td>
      <td>V</td>
      <td>53</td>
      <td>−2.901</td>
      <td>0.317</td>
      <td>79</td>
      <td>4</td>
      <td>36</td>
      <td>0.264</td>
    </tr>
    <tr>
      <td>12</td>
      <td>DReg</td>
      <td>I</td>
      <td>29</td>
      <td>−2.164</td>
      <td>1.010</td>
      <td>15</td>
      <td>2</td>
      <td>11</td>
      <td>0.428</td>
    </tr>
    <tr>
      <td>13</td>
      <td>DReg</td>
      <td>III</td>
      <td>27</td>
      <td>−2.991</td>
      <td>0.175</td>
      <td>66</td>
      <td>3</td>
      <td>63</td>
      <td>0.186</td>
    </tr>
    <tr>
      <td>14</td>
      <td>DReg</td>
      <td>IV</td>
      <td>22</td>
      <td>−1.397</td>
      <td>1.818</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>15</td>
      <td>DReg</td>
      <td>V</td>
      <td>24</td>
      <td>−2.893</td>
      <td>1.784</td>
      <td>22</td>
      <td>1</td>
      <td>22</td>
      <td>0.352</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; nonDReg – linear regression for only the non-diagnosed subjects._

### Channel-pair analyses

We report results of all the channel-pair analyses in Tables 1 and 2. Only 3 out of 60 analyses without control for confounds gave significant results. This is expected by chance, p=0.583, binomial test for a probability of significant result greater than 5%. For analyses controlling for confounds only 1 out of 60 was significant, which is also expected by chance, p=0.954, binomial test. We focus the description below on results from the analyses without control for confounds.

Two of the significant results were found for the diagnosed vs healthy controls contrast (DvsHC) for the average referenced (AVG) F3–F4 channel pair in Study I and V. In Study I right–left alpha asymmetry was lower for the diagnosed group than for healthy controls, t = −2.073, p=0.043 (Figure 3A). However, Study V showed the reverse: alpha asymmetry was higher for the diagnosed group compared to healthy controls, t = 2.823, p=0.007 (Figure 3B). Because we use right minus left alpha asymmetry only results with more negative asymmetry values in depressed individuals (negative t values) are congruent with the classical FAA effect.

![Figure 3.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig3-v1.jpg)

**Figure 3.:** Panels A and B show 2 of 3 significant channel pair results: average referenced F3–F4 channel pair for Studies I (A) and V (B). The remaining panels (C and D) show other channel pair analysis variants: specifically those that differ by exactly one parameter (underlined text) from the result presented in the panel A. Horizontal lines represent averages for each group, and shaded areas show standard error of the mean.

We now examine the FAA-congruent result from Study I in a wider context, comparing it to the outcome of related analyses that differ in a single parameter. Applying CSD instead of average reference to the same channel pair did not reveal a significant result (same study, same contrast, F3–F4 pair, CSD reference, t = 0.132, p=0.896). The results were also not significant for the other channel pair, irrespective of reference (same study, same contrast, F7–F8 pair: average reference, t = −0.365, p=0.717; CSD reference, t = 0.553, p=0.583). Performing the same analysis on data from Study III or IV also did not give rise to a significant outcome (same contrast, F3–F4 pair, AVG reference, Study III: t = 0.904, p=0.371; Study IV: t = 0.450, p=0.654). For Study II the DvsHC contrast was not available, but conceptually closest contrast – Sub-clinical vs Healthy Controls (SvsHC) – was found insignificant for both channel pairs using either AVG or CSD reference. Only this FAA-congruent DvsHC effect on F3–F4, AVG in Study I survives control for confounding variables (t = −2.679, p=0.010).

Another significant result was observed for linear relationship between FAA and BDI score (allReg contrast) on the average referenced F3–F4 channel pair in Study V: more positive values of alpha asymmetry were associated with higher BDI scores (t = 2.489, p=0.016). This result is not consistent with the standard FAA effect, which, when calculated as right minus left alpha, should manifest as a negative correlation (negative t).

However, as we argued in the introduction, single channel analyses are not a particularly good approach to testing FAA. They may be sensitive to small changes in the topography pattern and do not provide any information about the source or physiological plausibility of the effect.

### Cluster-based analyses

The next set of analyses consisted of cluster-based analyses on all frontal channel pairs (Tables 3 and 4). This approach gives a better view of the whole FAA space (correcting for multiple comparisons) especially when coupled with presentation of the effects’ topographies. We observe only one significant effect out of 30 for standard analyses (p=0.785, binomial test) and one out of 30 (p=0.785) when controlling for confounding variables.

The significant result for standard analyses corresponds to DvsHC contrast for the average referenced data in Study V (cluster p=0.026). This is the same analysis combination as the significant channel-pair result for Study V reported in the previous section. And just like in the previous section it represents a result that is not congruent with the classical FAA effect: the positive t values mean more positive right minus left FAA in depressed compared to healthy controls. We compare this effect to other analyses for DvsHC contrast in Figure 4. We do not observe any other significant effect in standard cluster-based results: neither contrasting sub-clinical vs healthy controls nor looking for a linear relationship between FAA and depression questionnaire score. Although single channels sometimes pass the significance threshold (see n significant points column in Table 3) these effects are not significant at the cluster level. In other words the clusters formed by these channels were not convincingly stronger from clusters observed under the null hypothesis (that is, when permuting the data).

![Figure 4.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig4-v1.jpg)

**Figure 4.:** More positive (red) t values indicate more right-sided (less left-sided) alpha asymmetry for diagnosed participants. More negative (blue) t values indicate more right-sided (less left-sided) FAA for healthy controls. Channels that are part of a cluster are marked with white dots.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Topographies of effects are presented in a reference by study matrix. Color bar on the right presents color coding for the t values: more positive (red)/negative (blue) relationship between FAA and BDI. Channels that are part of a cluster are marked with white dots.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Topographies of effects are presented in a reference by study matrix. Color bar on the right presents color coding for the t values: more positive (red)/negative (blue) relationship between FAA and BDI. Channels that are part of a cluster are marked with white dots.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** Topographies of different contrast effects in a reference by study matrix. More positive (red) t values indicate more right-sided (less left-sided) alpha asymmetry for subclinical participants. More negative (blue) t values indicate more right-sided (less left-sided) FAA for healthy controls. Channels that are part of a cluster are marked with white dots.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** First row shows topography of average alpha power for both groups; second row shows topography of average alpha asymmetry for both groups.

However, we observe an interesting effect of controlling for confounds. The significant result mentioned in the previous paragraph is no longer present after controlling for age, gender, and education (see Figure 5A). This change might be related to the fact that the diagnosed group has significantly lower education than the control group in Study V (t = −3.07, p=0.004, see Figure 5B), so a part of the FAA differences between the groups can be explained away by education. On the other hand, one result close to the significance threshold in the standard analyses (DvsHC, Study I, AVG, cluster p=0.069) becomes significant after controlling for gender and age (p=0.023), which may be related to the difference in age between the depressed and the control group in this study (t = 2.73, p=0.0095).

![Figure 5.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig5-v1.jpg)

**Figure 5.:** (A) The logic of the topographical plots is the same as in Figure 4. (B) Swarmplots corresponding to studies in panel A showing the between-group difference in the selected confounding variables. Detailed results for analyses taking into account confounding variables can be found in Table 4.

### Cluster-based analyses on standardized data

All previous analyses assume that asymmetry can be detected by subtracting right and left homologous channels. Because some asymmetry effects may not match such strict left vs right pattern, we performed further analyses to alleviate this issue: in this set of analyses we relied on standardization of alpha power at frontal channels instead of right minus left subtraction. Additionally, to minimize the risk of averaging out an effect confined to a narrow frequency range, we also analyzed all frequency bins in the 8–13 Hz range. This strategy is used in a set of 60 analyses (30 without and 30 with control for confounds) – we report their results in Tables 5 and 6.

Only two out of 30 analyses on standardized data without control for confounds showed statistically significant result – this is expected by chance given our alpha level (p=0.447, binomial test). Specifically, the significant results were found for: (a) DReg contrast, Study III (cluster p=0.025) and (b) DvsHC contrast, Study IV (p=0.007), both for average referenced data. Both these effects are potentially interesting, because they show a similar pattern – a positive relationship between (a) depression severity (BDI score, only the diagnosed subjects) or (b) diagnosis status and power in the higher alpha band (DReg: 11–12.5 Hz, DvsHC: 10.5–12 Hz) across many frontal channels (see Figure 6). Because it is accompanied with an inverse effect in a lower frequency band (DReg: 9–10 Hz, DvsHC: 8–9 Hz) at similar channels, averaging across the whole 8–13 Hz frequency range could lead to both effects cancelling each other in the average. Such a pattern of inverse effects across frequencies could arise due to a frequency shift of the individual alpha peak or the narrowing of the peak with depression severity but it may also be a direct consequence of standardization. However, both effects do not represent FAA as their topography is symmetrical (DReg: χ2(1)=0.153, p=0.696, DvsHC: χ2(1)=0.000, p=1) and were not replicated when using CSD reference in the same studies (Study III, Dreg: cluster p=0.259; Study IV, DvsHC: p=0.105) or performing the same contrast on data from other studies (see more: Table 5, Table 6, and Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig6-v1.jpg)

**Figure 6.:** Heatmaps in the upper part of each panel represent regression t values for channel by frequency search space. More positive/negative t values indicate higher/lower power with higher BDI. Clusters are indicated in the heatmaps with white outline. In each panel we present two topographies below the heatmap: showing average effect for lower and higher frequency ranges determined by the positions of the clusters. Channels that are part of a cluster are marked with white dots in the topographical plots.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Heatmaps in the upper part of each panel represent regression t values for channel by frequency search space. More positive/negative t values indicate higher/lower power with higher BDI. Clusters are indicated in the heatmaps with white outline. In each panel we present two topographies below the heatmap: showing average effect for 9–10 Hz and 11.5–12.5 Hz range respectively. Channels that are part of a cluster are marked with white dots in the topographical plots.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Heatmaps in the upper part of each panel represent regression t values for channel by frequency search space. More positive/negative t values indicate higher/lower power with higher BDI. Clusters are indicated in the heatmaps with white outline. In each panel we present two topographies below the heatmap: showing average effect for 9–10 Hz and 11.5–12.5 Hz range respectively. Channels that are part of a cluster are marked with white dots in the topographical plots.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig6-figsupp3-v1.jpg)

**Figure 6—figure supplement 3.:** Heatmaps in the upper part of each panel represent t values for channel by frequency search space. More positive (red) t values indicate higher power in given channel and frequency for diagnosed participants. More negative (blue) t values indicate higher power in given channel and frequency for healthy controls. Clusters are indicated in the heatmaps with white outline. In each panel we present two topographies below the heatmap: showing average effect for 9–10 Hz and 11.5–12.5 Hz range respectively. Channels that are part of a cluster are marked with white dots in the topographical plots.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig6-figsupp4-v1.jpg)

**Figure 6—figure supplement 4.:** Heatmaps in the upper part of each panel represent t values for channel by frequency search space. More positive (red) t values indicate higher power in given channel and frequency for diagnosed participants. More negative (blue) t values indicate higher power in given channel and frequency for healthy controls. Clusters are indicated in the heatmaps with white outline. In each panel we present two topographies below the heatmap: showing average effect for 9–10 Hz and 11.5–12.5 Hz range respectively. Channels that are part of a cluster are marked with white dots in the topographical plots.

Although the conclusions that can be drawn from these standardization analyses are not in favor of FAA–DD relationship, they demonstrate the strength of the proposed approach in detecting effects that might be otherwise missed when averaging across the whole alpha range or when testing only the differences on corresponding right–left channel pairs.

### Source level analyses

Because observing the effect in the signal recorded from frontal channels does not guarantee that the source of this effect is frontal we conducted a second set of additional analyses using source localization with DICS beamforming. In these analyses the FAA was evaluated in the source space by subtracting power of the corresponding right and left hemisphere vertices.

Results of source level analyses are reported in Tables 7 and 8. One of the 15 source space analyses turned out statistically significant – this is expected by chance given our alpha value (p=0.537, binomial test). The same number of significant results was found when controlling for confounding variables (1/15, p=0.537).

The significant effect was found for DvsHC contrast in Study IV (p=0.010, see Figure 7) and remains significant when controlling for confounds (cluster p=0.011; see Table 8). It represents more negative FAA values for depressed compared to healthy individuals, which is congruent with the traditional FAA effect.

![Figure 7.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig7-v1.jpg)

**Figure 7.:** Cluster limits are marked with white outlines, and corresponding cluster p-values are shown below each panel. Color bar at the bottom presents color coding for the t values.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Cluster limits are marked with white outlines, and corresponding cluster p-values are shown below each panel. Color bar at the bottom presents color coding for the t values: more positive (red)/negative (blue) relationship between FAA and BDI.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** Cluster limits are marked with white outlines, and corresponding cluster p-values are shown below each panel. Color bar at the bottom presents color coding for the t values: more positive (red)/negative (blue) relationship between FAA and BDI. Linear regression restricted to diagnosed subjects; NA: no cluster with p<0.05 is present.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig7-figsupp3-v1.jpg)

**Figure 7—figure supplement 3.:** Cluster limits are marked with white outlines, corresponding cluster p-values are shown below each panel. More positive (red) t values indicate more right-sided (less left-sided) alpha asymmetry for diagnosed participants. More negative (blue) t values indicate more right-sided (less left-sided) FAA for healthy controls.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig7-figsupp4-v1.jpg)

**Figure 7—figure supplement 4.:** Cluster limits are marked with white outlines, corresponding cluster p-values are shown below each panel. More positive (red) t values indicate more right-sided (less left-sided) alpha asymmetry for subclinical participants. More negative (blue) t values indicate more right-sided (less left-sided) FAA for healthy controls. NA: no cluster with p<0.05 is present.

In most of the analyses the pattern and sign of the t values points towards a more left-sided effect. For example in the allReg contrast: the negative t values suggest lower R–L differences in high than in low BDI participants, which means more left-sided alpha power with higher BDI. Although this pattern seems to be in line with FAA–DD literature, almost all of the source space effects are weak and do not survive the correction for multiple comparisons. However, it is important to remember that individual MRI scans and channel locations were not available in the present study: their availability would lead to lower error in source reconstruction.

### Analyses on aggregated data

Finally, to overcome the relatively low statistical power of analyses on separate data sets we aggregate data from all studies that include identical contrasts and perform analyses on the aggregated data. Before aggregation we tested whether the FAA values from both selected channel pairs have similar scale across the five studies with a Levene test. Because the scale was significantly different across studies (F3–F4: W = 8.68, p<0.0001; F7–F8: W = 5.21, p=0.002) and because such scale differences can arise from lab-specific equipment or adopted impedance threshold, we z-scored the FAA values within each study before aggregation. All aggregated channel pair analyses can be seen in Figure 8, Figure 8—figure supplement 1, and Table 9. For brevity we discuss only the results for DvsC and allReg contrasts for average referenced channel pairs.

![Figure 8.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig8-v1.jpg)

**Figure 8.:** Each row corresponds to one analysis on a single channel pair. The contrasts, studies, and channel pairs are labeled on the y axis. The black dots correspond to observed effect sizes in Cohen’s d/Pearson’s r, while the black lines indicate 95% confidence intervals for the effect size estimated using bias-corrected accelerated bootstrapping. The magenta/purple shapes represent bootstrap distributions and the white numbers printed on the distributions are Bayes factors for the null hypothesis (BF01). BF01 of 4 indicates that the data are four times more likely under the null than the alternative hypothesis. BF01 between 3 and 10 are considered moderate evidence for the null hypothesis.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** Each row corresponds to one analysis on a single channel pair. The contrasts, studies, and channel pairs are labeled on the y axis. The black dots correspond to observed effect sizes in Cohen’s d/Pearson’s r, while the black lines indicate 95% confidence intervals for the effect size estimated using bias-corrected accelerated bootstrapping. The magenta/purple shapes represent bootstrap distributions and the white numbers printed on the distributions are Bayes factors for the null hypothesis (BF01). BF01 of 4 indicates that the data are four times more likely under the null than the alternative hypothesis. BF01 between 3 and 10 are considered moderate evidence for the null hypothesis.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** In group contrasts (A) the interaction term is female * diagnosed; in linear contrasts (B) it is female * depression score. Each row corresponds to one analysis on a single channel pair. The contrasts, studies, and channel pairs are labeled on the y axis. The black dots correspond to observed effect sizes in Pearson’s r, while the black lines indicate 95% confidence intervals for the effect size estimated using bias-corrected accelerated bootstrapping. The magenta/purple shapes represent bootstrap distributions and the white numbers printed on the distributions are Bayes factors for the null hypothesis (BF01). BF01 of 4 indicates that the data are four times more likely under the null than the alternative hypothesis. BF01 between 3 and 10 are considered moderate evidence for the null hypothesis.

**Table 9.**
 Results for analyses on data aggregated across studies: tests on frontal asymmetry on selected channel pairs.Each row represents a given contrast × reference × control for confounds combination. N: number of participants included in given contrast, control for confounds: whether the FAA data was residualized with respect to confounding variables (age, gender and education); ES: effect size, measured as Cohen’s d for DvsHC and SvsHC contrasts and Spearman’s r for Dreg and allReg contrasts; CI: bootstrap confidence interval for the effect size; BF01: Bayes Factor for the null hypothesis.


<table>
  <thead>
    <tr>
      <th rowspan="3">No.</th>
      <th rowspan="3">Contrast</th>
      <th rowspan="3">Space</th>
      <th rowspan="3">N</th>
      <th rowspan="3">Control for confounds</th>
      <th></th>
      <th colspan="7">Aggregated channel pair analyses</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="3">Pair 1 (F3–F4)</th>
      <th></th>
      <th colspan="3">Pair 2 (F7–F8)</th>
    </tr>
    <tr>
      <th></th>
      <th>ES</th>
      <th>CI</th>
      <th>BF01</th>
      <th></th>
      <th>ES</th>
      <th>CI</th>
      <th>BF01</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>avg</td>
      <td>102 vs 144</td>
      <td>−</td>
      <td></td>
      <td>0.147</td>
      <td>[−0.111, 0.396]</td>
      <td>3.831</td>
      <td></td>
      <td>0.098</td>
      <td>[−0.161, 0.338]</td>
      <td>5.405</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>avg</td>
      <td>102 vs 143</td>
      <td>+</td>
      <td></td>
      <td>−0.011</td>
      <td>[−0.264, 0.244]</td>
      <td>7.042</td>
      <td></td>
      <td>−0.006</td>
      <td>[−0.266, 0.240]</td>
      <td>7.042</td>
    </tr>
    <tr>
      <td>3</td>
      <td>DvsHC</td>
      <td>csd</td>
      <td>102 vs 144</td>
      <td>−</td>
      <td></td>
      <td>0.188</td>
      <td>[−0.069, 0.449]</td>
      <td>2.597</td>
      <td></td>
      <td>−0.100</td>
      <td>[−0.354, 0.164]</td>
      <td>5.319</td>
    </tr>
    <tr>
      <td>4</td>
      <td>DvsHC</td>
      <td>csd</td>
      <td>102 vs 143</td>
      <td>+</td>
      <td></td>
      <td>0.103</td>
      <td>[−0.159, 0.362]</td>
      <td>5.236</td>
      <td></td>
      <td>−0.164</td>
      <td>[−0.417, 0.108]</td>
      <td>3.300</td>
    </tr>
    <tr>
      <td>5</td>
      <td>SvsHC</td>
      <td>avg</td>
      <td>77 vs 121</td>
      <td>−</td>
      <td></td>
      <td>0.065</td>
      <td>[−0.236, 0.359]</td>
      <td>5.780</td>
      <td></td>
      <td>−0.025</td>
      <td>[−0.320, 0.240]</td>
      <td>6.250</td>
    </tr>
    <tr>
      <td>6</td>
      <td>SvsHC</td>
      <td>avg</td>
      <td>77 vs 120</td>
      <td>+</td>
      <td></td>
      <td>0.024</td>
      <td>[−0.269, 0.315]</td>
      <td>6.211</td>
      <td></td>
      <td>−0.144</td>
      <td>[−0.447, 0.140]</td>
      <td>4.016</td>
    </tr>
    <tr>
      <td>7</td>
      <td>SvsHC</td>
      <td>csd</td>
      <td>77 vs 121</td>
      <td>−</td>
      <td></td>
      <td>0.053</td>
      <td>[−0.223, 0.355]</td>
      <td>5.952</td>
      <td></td>
      <td>−0.108</td>
      <td>[−0.372, 0.179]</td>
      <td>4.878</td>
    </tr>
    <tr>
      <td>8</td>
      <td>SvsHC</td>
      <td>csd</td>
      <td>77 vs 120</td>
      <td>+</td>
      <td></td>
      <td>0.053</td>
      <td>[−0.222, 0.350]</td>
      <td>5.952</td>
      <td></td>
      <td>−0.110</td>
      <td>[−0.389, 0.179]</td>
      <td>4.831</td>
    </tr>
    <tr>
      <td>9</td>
      <td>DReg</td>
      <td>avg</td>
      <td>102</td>
      <td>−</td>
      <td></td>
      <td>0.188</td>
      <td>[0.006, 0.354]</td>
      <td>1.387</td>
      <td></td>
      <td>0.007</td>
      <td>[−0.186, 0.188]</td>
      <td>8.065</td>
    </tr>
    <tr>
      <td>10</td>
      <td>DReg</td>
      <td>avg</td>
      <td>102</td>
      <td>+</td>
      <td></td>
      <td>0.175</td>
      <td>[−0.018, 0.348]</td>
      <td>1.742</td>
      <td></td>
      <td>−0.029</td>
      <td>[−0.211, 0.155]</td>
      <td>7.752</td>
    </tr>
    <tr>
      <td>11</td>
      <td>DReg</td>
      <td>csd</td>
      <td>102</td>
      <td>−</td>
      <td></td>
      <td>0.099</td>
      <td>[−0.072, 0.260]</td>
      <td>4.975</td>
      <td></td>
      <td>0.065</td>
      <td>[−0.136, 0.252]</td>
      <td>6.579</td>
    </tr>
    <tr>
      <td>12</td>
      <td>DReg</td>
      <td>csd</td>
      <td>102</td>
      <td>+</td>
      <td></td>
      <td>0.051</td>
      <td>[−0.131, 0.216]</td>
      <td>7.092</td>
      <td></td>
      <td>0.048</td>
      <td>[−0.157, 0.255]</td>
      <td>7.194</td>
    </tr>
    <tr>
      <td>13</td>
      <td>allReg</td>
      <td>avg</td>
      <td>315</td>
      <td>−</td>
      <td></td>
      <td>0.085</td>
      <td>[−0.017, 0.184]</td>
      <td>4.651</td>
      <td></td>
      <td>0.029</td>
      <td>[−0.080, 0.126]</td>
      <td>12.5</td>
    </tr>
    <tr>
      <td>14</td>
      <td>allReg</td>
      <td>avg</td>
      <td>314</td>
      <td>+</td>
      <td></td>
      <td>0.041</td>
      <td>[−0.063, 0.143]</td>
      <td>10.87</td>
      <td></td>
      <td>0.001</td>
      <td>[−0.120, 0.104]</td>
      <td>14.085</td>
    </tr>
    <tr>
      <td>15</td>
      <td>allReg</td>
      <td>csd</td>
      <td>315</td>
      <td>−</td>
      <td></td>
      <td>0.059</td>
      <td>[−0.054, 0.166]</td>
      <td>8.333</td>
      <td></td>
      <td>−0.026</td>
      <td>[−0.141, 0.082]</td>
      <td>12.821</td>
    </tr>
    <tr>
      <td>16</td>
      <td>allReg</td>
      <td>csd</td>
      <td>314</td>
      <td>+</td>
      <td></td>
      <td>0.055</td>
      <td>[−0.056, 0.168]</td>
      <td>8.772</td>
      <td></td>
      <td>−0.048</td>
      <td>[−0.158, 0.059]</td>
      <td>9.901</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects; avg – average reference; csd – current source density._

Aggregated DvsHC contrast analysis encompasses 246 participants (102 diagnosed and 144 healthy controls) and 245 when controlling for confounds (one participant from the control group was removed due to missing information on confounding variables). For the F3–F4 channel pair the Cohen’s d is 0.147 (CI = [−0.111, 0.396]) and −0.011 when controlling for confounds (CI = [−0.264, 0.244]). Both confidence intervals exclude all but small effect sizes (classical FAA effect for right–left, diagnosed – controls should be negative). The effect sizes for F7–F8 channel pair are similar: d = 0.098, CI = [−0.161, 0.338] without control for confounds and d = −0.006, CI = [−0.266, 0.240] when controlling for confounding variables.

To quantify the support for the null hypothesis we calculate Bayes factors for the null (BF01). For F3–F4 channel pair the BF01 equals 3.831, which means that the data are almost four times more likely under the null than alternative hypothesis. When controlling for confounding variables the BF01 increases to 7.042. For F7–F8 channel pair the BF01 are: 5.405 and 7.042 when controlling for confounds. Bayes factors between 3 and 10 are considered moderate evidence, so the results provide moderate evidence for no FAA difference between diagnosed and healthy individuals.

Aggregated allReg contrast analysis includes 315 participants (314 when controlling for confounds). For F3–F4 channel pair the Pearson’s r is 0.085 (CI = [−0.017, 0.184]) and decreases to 0.041 when controlling for confounds (CI = [−0.063, 0.143]). Corresponding Bayes factors for the null are: 4.651 and 10.87 which suggests moderate to strong evidence for no relationship between FAA and depression score.

We also aggregate the data from relevant studies in the source space and then perform cluster-based permutation tests for all defined contrasts. Just like in the aggregated channel pair analyses, before aggregation the data are z-scored within each study (each source vertex is z-scored across participants separately) to avoid creating non-normal distributions by joining data of different scale. The results of the aggregated source space analyses can be found in Table 10.

**Table 10.**
 Results for analyses on data aggregated across studies, cluster-based permutation tests on frontal asymmetry in the source space.Each row represents the result for given contrast × control for confounds combination. N: number of participants included in given contrast, control for confounds: whether the FAA data was residualized with respect to confounding variables (age, gender and education), min t, max t: lowest and highest t value in the search space, respectively; n significant points: total number of significant points in the search space before cluster-based correction; n clusters: number of clusters found in given analysis; largest cluster p: p-value for the largest cluster, NA means that no cluster was found in given analysis.


<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">Contrast</th>
      <th rowspan="2">N</th>
      <th rowspan="2">Control for confounds</th>
      <th colspan="6">Aggregated source level analyses</th>
    </tr>
    <tr>
      <th>Min t</th>
      <th>Max t</th>
      <th>n significant points</th>
      <th>n clusters</th>
      <th>Largest cluster size</th>
      <th>Largest cluster p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DvsHC</td>
      <td>102 vs 144</td>
      <td>−</td>
      <td>−2.719</td>
      <td>0.956</td>
      <td>178</td>
      <td>5</td>
      <td>100</td>
      <td>0.077</td>
    </tr>
    <tr>
      <td>2</td>
      <td>DvsHC</td>
      <td>102 vs 143</td>
      <td>+</td>
      <td>−2.846</td>
      <td>0.908</td>
      <td>211</td>
      <td>5</td>
      <td>116</td>
      <td>0.066</td>
    </tr>
    <tr>
      <td>3</td>
      <td>SvsHC</td>
      <td>77 vs 121</td>
      <td>−</td>
      <td>−1.831</td>
      <td>−0.11</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>4</td>
      <td>SvsHC</td>
      <td>77 vs 120</td>
      <td>+</td>
      <td>−1.871</td>
      <td>0.182</td>
      <td>0</td>
      <td>0</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>5</td>
      <td>DReg</td>
      <td>102</td>
      <td>−</td>
      <td>−2.387</td>
      <td>1.376</td>
      <td>31</td>
      <td>3</td>
      <td>25</td>
      <td>0.328</td>
    </tr>
    <tr>
      <td>6</td>
      <td>DReg</td>
      <td>102</td>
      <td>+</td>
      <td>−3.095</td>
      <td>1.354</td>
      <td>112</td>
      <td>3</td>
      <td>68</td>
      <td>0.155</td>
    </tr>
    <tr>
      <td>7</td>
      <td>allReg</td>
      <td>315</td>
      <td>−</td>
      <td>−3.044</td>
      <td>0.411</td>
      <td>174</td>
      <td>6</td>
      <td>160</td>
      <td>0.067</td>
    </tr>
    <tr>
      <td>8</td>
      <td>allReg</td>
      <td>314</td>
      <td>+</td>
      <td>−3.107</td>
      <td>0.282</td>
      <td>235</td>
      <td>6</td>
      <td>195</td>
      <td>0.054</td>
    </tr>
  </tbody>
</table>

_DvsHC – diagnosed and healthy controls; SvsHC – sub-clinical and healthy controls; allReg – linear regression for all subjects together; DReg – linear regression for only diagnosed subjects._

Although no analysis yields nominally significant results it is interesting to note that contrasts DvsHC and allReg are at the conventional ‘trend’ level (DvsHC: 0.077 and 0.066 when controlling for confounds; allReg: 0.067 and 0.054 when controlling for confounds) and their direction agrees with the traditional FAA effect.

## Discussion

We conducted a multiverse analysis of EEG data sets from five independent studies, with 388 participants and 270 analyses in total, to test the robustness and credibility of the relationship between FAA and depressive mood. We performed 120 replicatory single channel pairs analyses and 60 corresponding cluster-based analyses. We have also conducted 90 additional analyses addressing some of the limitations of current FAA studies. Out of 270 performed analyses only 13 produced statistically significant results – a result expected by chance when using 0.05 alpha level (binomial test, p=0.595). Moreover, more than half of the significant results (8/13) are incongruent with the traditional FAA effect: by either showing the opposite direction of the effect (6) or not showing asymmetry (two significant effects on standardized data). Overall, the conducted analyses do not provide a basis to reject the null hypothesis of no relationship between resting state FAA and DD.

Our conclusion is similar to this formulated by other research groups (Kaiser et al., 2018b; van der Vinne et al., 2017), stating that treating FAA as a biomarker of DD is not sufficiently empirically grounded. As our data shows, this skepticism is not limited to single channel pair analyses – improving on the limitations of methods commonly used in FAA literature does not change the pattern of results.

Despite this, FAA is one of the most common indicators of DD with a long history of successful studies – it might be difficult to believe that all previous FAA research represents Type I errors. Therefore it is worth considering that we just fail to detect this effect here. First, the FAA effect size may be too small to be reliably observed with a small to moderate sample size. The average number of participants per study is 78 in our case, but most analyses contain around 25 participants per group, which grants sufficient power to detect mostly large effects. Although single analyses reported here can be deemed inconclusive, the whole multiverse set of analyses is incompatible with the presence of moderate to strong relationship between FAA and DD. To strengthen this point we performed analyses on data aggregated across studies (see section Analyses on aggregated data) showing estimated effect sizes, their confidence intervals, and Bayes factors for the null hypothesis (see Figure 8 and Figure 8—figure supplement 1). All confidence intervals for diagnosed vs healthy controls group contrast (DvsHC) and linear relationship between FAA and diagnosis score (allReg) exclude strong and moderate effects in the direction compatible with traditional FAA effect. Moreover, Bayes factors indicate that there is moderate evidence for the null hypothesis (or moderate to strong evidence for the null in allReg contrast). Although we cannot exclude a small FAA–DD relationship, if the effect was in this range then most published studies would have been underpowered to detect it. This line of thought is also supported in the meta-analysis by van der Vinne et al., 2017, which shows that studies with larger samples were less likely to report high effect sizes. For example, the largest EEG FAA study on a sample of 1008 DD patients and 336 controls did not confirm the diagnostic value of FAA in DD (Arns et al., 2016). Such pattern of results suggests publication bias or that the FAA–DD effect, if it exists, is detectable only in highly selected samples and is of small magnitude on the population level.

Although the collected studies contain data from sub-clinical, mild, as well as major depression patients, we do not think our results can be explained by the level of depression severity. Clinical participants in Studies I, III, IV, and V and sub-clinical participants in Studies II and III manifested a wide range of DD symptoms indicated by BDI/PHQ-9 scores (see Figure 1 for BDI histograms), but regression analysis (DReg) did not reveal any relationship between FAA and BDI score in the aggregated analyses. This means that participants with stronger DD symptoms were not better characterized by a specific FAA pattern even when we controlled for confounding variables like age, gender, and education. However, given that 56 out of 102 participants (54.9%) in the aggregated clinical group were diagnosed with mild DD, it would be interesting to repeat the analyses presented here on a data set with more major DD patients.

Smith et al., 2017 previously suggested that the relationship between FAA and DD is stronger when the participant is given some emotion-related task, as opposed to resting condition, where the task is unspecified. Although this is possible, we wanted to stay true to the design of most FAA–DD studies, which measure EEG during rest. An interesting approach for future studies would be to compare rest blocks separated by an emotional task (see, for example, Beeney et al., 2014).

CSD has been previously recommended in the literature (Kayser and Tenke, 2015; Stewart et al., 2014) for studies on FAA because it reduces volume conduction and makes topographies more focal. We do not see support for the claim that CSD is more sensitive to FAA in our results. We even think it may be the contrary – almost all significant or trend-level effects disappear with CSD reference. The fact that CSD produces more focal topographies coupled with potential high variability of topographies across subjects may result in lower probability of detecting an effect. Given that the orientation of the sources responsible for the effect of interest may be variable across subjects, increasing the focality of their projections may only exacerbate the issue.

In contrast to CSD, we see some indication of the traditional FAA effect in the source space analyses. Although only 2/30 source space analyses are significant, partitioning the effects into contrasts (see Table 11) reveals 2/8 significant DvsHC results, which is only barely consistent with 5% error rate (p=0.057, binomial test). Also the direction of the effect in almost all source results is consistent with the traditional FAA effect (negative t values). Finally, the same consistency of the effect direction can be observed in the source space analyses on aggregated data (see Table 10, Figure 9, and Figure 9—figure supplement 1) – all source space vertices with an uncorrected significant effect show negative effect direction. The DvsHC and allReg contrasts on the aggregated data are at the trend level (p=0.077 and p=0.067, respectively) and it might seem that using more rigorous source localization (individual MRI scans and channel positions) could lead to a significant effect. Nevertheless it is difficult to speculate based on statistical tendency – with more subjects or more precise source localization the results might equally likely land further away from the alpha threshold.

![Figure 9.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig9-v1.jpg)

**Figure 9.:** Cluster limits are marked with white outlines, and corresponding cluster p-values are shown below each panel. Color bar at the bottom presents color coding for the t values.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig9-figsupp1-v1.jpg)

**Figure 9—figure supplement 1.:** Cluster limits are marked with white outlines, and corresponding cluster p-values are shown below each panel. Color bar at the bottom presents color coding for the t values.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/60595/elife-60595-fig9-figsupp2-v1.jpg)

**Figure 9—figure supplement 2.:** In group contrasts (DvsHC and SvsHC) the interaction term is female * diagnosed; in linear contrasts (DReg, allReg) it is female * depression score. Cluster limits are marked with white outlines, and corresponding cluster p-values are shown below each panel. Color bar at the bottom presents color coding for the t values.

**Table 11.**
 Number of significant results compatible with the traditional FAA effect partitioned into analyses and contrasts.If one or more such results have been found for a given cell, then the p-value for the binomial test is also shown.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Number of significant results congruent with the FAA effect</th>
    </tr>
    <tr>
      <th></th>
      <th>Channel pairs N = 120</th>
      <th></th>
      <th>Cluster correction N = 60</th>
      <th></th>
      <th>Source space N = 30</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DvsHC</td>
      <td>2/32, p=0.48</td>
      <td></td>
      <td>1/16, p=0.56</td>
      <td></td>
      <td>2/8, p=0.057</td>
    </tr>
    <tr>
      <td>SvsHC</td>
      <td>0/24</td>
      <td></td>
      <td>0/12</td>
      <td></td>
      <td>0/6</td>
    </tr>
    <tr>
      <td>DReg</td>
      <td>0/32</td>
      <td></td>
      <td>0/16</td>
      <td></td>
      <td>0/8</td>
    </tr>
    <tr>
      <td>allReg</td>
      <td>0/32</td>
      <td></td>
      <td>0/16</td>
      <td></td>
      <td>0/8</td>
    </tr>
  </tbody>
</table>

Previous studies have suggested that FAA effect may manifest differently depending on gender (Jaworska et al., 2012; Stewart et al., 2010; van der Vinne et al., 2017). Because all the analyses with control for confounding variables that we have conducted control only for the main effect of gender, we additionally tested the presence of an interaction between gender and diagnosis (or depression score) in predicting FAA. This set of analyses were restricted only to the aggregated data with control for confounds. None of these analyses demonstrated a significant interaction effect (see Figure 8—figure supplement 2 and Figure 9—figure supplement 2).

A challenge for future FAA studies would be to move beyond a ‘marker-only’ approach, describe the theoretical assumptions behind FAA in more detail, and let these assumptions dictate an adequate analytical approach. For example, the assumption that FAA is a phenomenon with a source in the frontal cortex is impossible to address using only a few frontal channel pairs. Using source localization (like DICS Beamforming used here) or source separation (for example, spatial filtering with generalized eigendecomposition/common spatial pattern [Koles et al., 1990; Parra and Sajda, 2003; Tomé, 2006]; or SPACE decomposition [van der Meij et al., 2015]; Roemer [van der Meij et al., 2016]) should be preferred when looking for the answer to this question. This point is important because frontal alpha sources are rarely measured reliably with EEG at the channel level: strong occipital and parietal alpha sources dominate alpha power recorded at frontal channels. As a result measuring FAA at the channel level could lead to poor signal to noise ratio and consequently to small effect size and low probability to observe a true FAA–DD relationship. On the other hand, if FAA does not originate in the frontal regions, it should be measured and interpreted differently. Such scenario is not unlikely because frontal alpha sources are generally difficult to detect with EEG/MEG. For example, Roemer van der Meij et al., 2016, using an advanced source separation method, found that 86.6% of the alpha components detected across subjects were occipito-parietal and only 1% (4/380) were frontal. If frontal alpha sources are difficult to detect using a source separation method designed to capture oscillatory sources, then it is likely that these sources are rarely observed at the channel level at all.

If FAA is not of frontal origin, then where could it come from? This is an open empirical question and we can only offer speculation here. Jiang et al., 2016 have shown that the power of posterior alpha oscillations is reduced in depressed individuals and that this reduction strongly correlates with depression severity. Assuming that frontal projections from occipital or parietal sources will not be perfectly symmetrical, a difference metric like FAA may be sensitive to posterior alpha power. Another possibility is that FAA originates from asymmetry at the source level; Smith et al., 2018 demonstrated that channel-level FAA is related to source level asymmetry in frontal motor regions. However, the authors did not look for correlations with FAA in the full source space, but restricted their analyses to the R–L source level asymmetry and in consequence their analysis is insensitive to symmetrical sources of FAA. Our data and analyses cannot be conclusive in this regard because without a strong and reliable channel-level FAA–DD effect it is difficult to look for its source level correlate.

Tackling all the mentioned issues would require to systemize and unify the FAA methodology for the benefit of future studies. So far, Kaiser et al., 2018a proposed guidelines for methodology regarding subjects selection and controlling for confounding variables. Smith et al., 2017 also suggested possible improvements in experimental procedures and EEG signal preprocessing. We believe there is still room for improvement in the signal analysis standards of FAA studies. Below we summarize our arguments and propose additional guidelines for EEG data analysis in FAA research:

## Materials and methods

We included five data sets in the analyses. These data sets were obtained in five independent studies: Studies I–III have been collected by the authors of the article; Studies IV and V are publicly available: the data from Study IV were obtained from the PREDiCT repository (Cavanagh et al., 2017), while Study V data come from the MODMA database (Cai et al., 2020).

### Participants

In total 408 medication-free participants took part in the collected five studies: all without neurological disorders or head injuries. Thirteen subjects were excluded from further analyses due to excessive artifacts in the EEG signal (Study II: 8; Study III: 4; Study IV: 1) or missing data (Study III: 1; Study IV: 3). Additional three subjects were excluded from Study I because of not fulfilling the analysis criteria. As a consequence a total of 388 participants were included in the reported analyses: Study I, N = 51; Study II, N = 76; Study III, N = 91; Study IV: 117; Study V: 53. For descriptive statistics summarizing each study, see Table 12 and Figure 1.

**Table 12.**
 Descriptive statistics for each study presented in the article (N – number of participants, M – mean score, SD – standard deviation, BDI-I and BDI-II – Beck Depression Inventory I and II, PHQ-9 – Patient Health Questionnaire-9).


<table>
  <tbody>
    <tr>
      <td></td>
      <td colspan="4">Study I (N=51)</td>
    </tr>
    <tr>
      <td></td>
      <td>Diagnosed</td>
      <td>Healthy Controls, BDI-I ≤ 5</td>
      <td>Subclinical</td>
      <td>Unclassified</td>
    </tr>
    <tr>
      <td>N</td>
      <td>29</td>
      <td>22</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="2">Age</td>
      <td>M = 27.66, SD = 7.13</td>
      <td>M = 23.68, SD = 2.83</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>19 - 47 range</td>
      <td>20 - 33 range</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>9 male, 20 female</td>
      <td>11 male, 11 female</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>BDI-I score</td>
      <td>M = 20.93, SD = 8.21</td>
      <td>M = 2.00, SD = 1.48</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">Study II (N=76)</td>
    </tr>
    <tr>
      <td rowspan="2"></td>
      <td></td>
      <td colspan="3">Undiagnosed (N=76)</td>
    </tr>
    <tr>
      <td>Diagnosed</td>
      <td>Healthy Controls, BDI-I ≤ 5</td>
      <td>Subclinical, BDI-I ≥ 10</td>
      <td>Unclassified, 5 &lt; BDI-I &lt; 10</td>
    </tr>
    <tr>
      <td>N</td>
      <td>-</td>
      <td>28</td>
      <td>25</td>
      <td>23</td>
    </tr>
    <tr>
      <td rowspan="2">Age</td>
      <td>-</td>
      <td>M = 25.32, SD = 6.46</td>
      <td>M = 24.44, SD = 5.08</td>
      <td>M = 25.22, SD = 6.78</td>
    </tr>
    <tr>
      <td>-</td>
      <td>18 - 43 range</td>
      <td>19 - 38 range</td>
      <td>18 - 40 range</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>-</td>
      <td>8 males, 20 females</td>
      <td>4 males, 21 females</td>
      <td>9 males, 14 females</td>
    </tr>
    <tr>
      <td>BDI-I score</td>
      <td>-</td>
      <td>M = 2.29, SD = 1.72</td>
      <td>M = 17.56, SD = 8.13</td>
      <td>M = 7.91, SD = 1.16</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">Study III (N=91)</td>
    </tr>
    <tr>
      <td rowspan="2"></td>
      <td rowspan="2">Diagnosed</td>
      <td colspan="3">Undiagnosed (N=64)</td>
    </tr>
    <tr>
      <td>Healthy Controls, BDI-II ≤ 5</td>
      <td>Subclinical, BDI-II ≥ 10</td>
      <td>Unclassified, 5 &lt; BDI-II &lt; 10</td>
    </tr>
    <tr>
      <td>N</td>
      <td>27</td>
      <td>21</td>
      <td>34</td>
      <td>9</td>
    </tr>
    <tr>
      <td rowspan="2">Age</td>
      <td>M = 27.19, SD = 7.23</td>
      <td>M = 24.29, SD = 4.99</td>
      <td>M = 25.06, SD = 6.58</td>
      <td>M = 26.78, SD = 8.74</td>
    </tr>
    <tr>
      <td>19 - 42 range</td>
      <td>19 - 41 range</td>
      <td>18 - 44 range</td>
      <td>22 - 49 range</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>6 males, 21 females</td>
      <td>7 males, 14 females</td>
      <td>10 males, 24 females</td>
      <td>2 males, 7 females</td>
    </tr>
    <tr>
      <td>BDI-II score</td>
      <td>M = 34.26, SD = 9.18</td>
      <td>M = 2.24, SD = 1.70</td>
      <td>M = 24.06, SD = 10.08</td>
      <td>M = 6.78, SD = 0.97</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">Study IV (N=117)</td>
    </tr>
    <tr>
      <td rowspan="2"></td>
      <td rowspan="2">Diagnosed</td>
      <td colspan="3">Undiagnosed (N=95)</td>
    </tr>
    <tr>
      <td>Healthy Controls, BDI-II ≤ 5</td>
      <td>Subclinical, BDI-II ≥ 10</td>
      <td>Unclassified, 5 &lt; BDI-II &lt; 10</td>
    </tr>
    <tr>
      <td rowspan="2">N</td>
      <td>22</td>
      <td rowspan="2">72</td>
      <td rowspan="2">21</td>
      <td rowspan="2">2</td>
    </tr>
    <tr>
      <td>(12 past MDD, 10 present MDD)</td>
    </tr>
    <tr>
      <td rowspan="2">Age</td>
      <td>M = 18.91, SD = 1.34</td>
      <td>M = 19.00, SD = 1.23</td>
      <td>M = 18.43, SD = 0.81</td>
      <td>M = 18.00</td>
    </tr>
    <tr>
      <td>18 - 24 range</td>
      <td>18 - 23 range</td>
      <td>18 - 21 range</td>
      <td>ages 18, 18</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>8 males, 14 females</td>
      <td>33 males, 39 females</td>
      <td>3 males, 18 females</td>
      <td>1 males, 1 females</td>
    </tr>
    <tr>
      <td>BDI-II score</td>
      <td>M = 21.82, SD = 5.70</td>
      <td>M = 1.60, SD = 1.48</td>
      <td>M = 22.95, SD = 4.25</td>
      <td>M = 6.50, SD = 0.71</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4">Study V (N=53)</td>
    </tr>
    <tr>
      <td></td>
      <td>Diagnosed</td>
      <td>Healthy Controls, PHQ-9 ≤ 5</td>
      <td>Subclinical</td>
      <td>Unclassified</td>
    </tr>
    <tr>
      <td>N</td>
      <td>24</td>
      <td>29</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="2">Age</td>
      <td>M = 30.88, SD = 10.37</td>
      <td>M = 31.45, SD = 9.15</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>16 - 52 range</td>
      <td>19 - 52 range</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>13 males, 11 females</td>
      <td>11 males, 13 females</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>PHQ-9 score</td>
      <td>M = 18.33, SD = 3.50</td>
      <td>M = 2.66, SD = 1.80</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

Participants in Studies II and III as well as healthy controls in Study I were recruited from the general population via advertisements in the local media or internal announcements for students at the University of Social Sciences and Humanities in Warsaw. In Study I diagnosed patients were recruited at the Psychiatry Clinic of the Department of Psychiatry, Medical University of Warsaw.

In Studies I–III each participant completed the Beck Depression Inventory (BDI) to determine the current level of mood disorder: we used BDI version I (Beck et al., 1961) in Studies I and II; and BDI version II (Beck et al., 1996) in Study III. Patients in Studies I and III were diagnosed with mild DD (F32.0) according to ICD-10 classification criteria after a structured clinical interview using the MINI – mini-international neuropsychiatric interview (Sheehan et al., 1998).

Participants in Study IV were recruited from the student population at University of Arizona. Participants with BDI score ≥13 were invited to participate in a Structured Clinical Interview for Depression. Participants meeting diagnostic criteria of current or past major DD were included in the group of diagnosed participants. Also, all participants completed BDI-II. More recruitment details can be found in the original papers (Cavanagh et al., 2011; Cavanagh et al., 2019).

In Study V participants with diagnosis of major DD were recruited from the Lanzhou University Second Hospital and healthy controls from the general population. In both groups, each participant completed the Patient Health Questionnaire (PHQ-9) (Kroenke et al., 2001) to evaluate depression level. More recruitment details can be found in the original papers (Li et al., 2017; Sun et al., 2019).

In Studies I, III, and IV all undiagnosed participants (including the subclinical group) and diagnosed participants in Study I reported no past depression episodes. This information was not available for participants of Studies II and V.

Local ethics committees approved studies’ protocols (Study I – the Medical University of Warsaw; Studies II and III – the University of Social Sciences and Humanities; Study IV – the University of Arizona; Study V – the Lanzhou University Second Hospital) and all participants signed consent forms.

### Electrophysiological data sets

The summary of all studies is presented in Figure 1. The equipment specifications and sessions details are provided below:

Study I – EEG signal was recorded with 64 channels (Ag/AgCl electrodes) arranged in the 10–5 system in a WaveGuard EEG Cap (Advanced Neuro Technology, ANT) at a sampling rate of 512 Hz. Impedance was kept below 10 kΩ. EEG signal was recorded during a 5-min session with eyes closed.

Study II – EEG signal was recorded with 64-Channel EGI HydroCel Geodesic Sensor Net, NetStation software, and an EGI Electrical Geodesic EEG System 300 amplifier at a sampling rate of 200 Hz. Impedance was kept below 40 kΩ. EEG signal was recorded during a 5-min session with eyes closed.

Study III – EEG signal was recorded with 64-Channel (Ag/AgCl active electrodes) Brain Products ActiCap system and BrainVision software at a sampling rate of 1000 Hz and downsampled off-line to 250 Hz. Impedance was kept below 10 kΩ. EEG signal was recorded during an 8-min session with alternating eyes open (O) and eyes closed (C) 1-min segments. The ordering of the segments was either OCCOCO or COOCOC (chosen randomly for each participant).

Study IV – EEG signal was recorded with 64-Channel (Ag/AgCl electrodes) Neuroscan Synamps2 system at a sampling rate of 512 Hz. Impedance was kept below 10 kΩ. EEG signal contained six 1-min segments with alternating eyes open (O) and eyes close (C). The ordering of the segments was either OCCOCO or COOCOC.

Study V – EEG signal was recorded with 128-Channel EGI HydroCel Geodesic Sensor Net and NetStation software at a sampling rate of 250 Hz. Impedance was kept below 70 kΩ. EEG signal was recorded during a 5-min session with eyes closed.

### Data preprocessing

The preprocessing was performed with a custom-made EEGLAB-based MATLAB toolbox (eegDb: Magnuski, 2020b) and custom MATLAB scripts. Preprocessing steps were the same for all five studies. Continuous EEG signal was 1 Hz high pass filtered and divided into 1-s consecutive segments. EEG recordings were visually inspected and segments containing strong or non-stereotypic artifacts were marked for rejection. These segments were ignored in all further preprocessing and analysis steps. Independent component analysis (ICA) was applied to remove remaining stereotypical artifacts from the data. Independent components signal, topographies, and power spectra were visually inspected and components related to eye blinks, eye movements, and muscular and cardiac artifacts (Hipp and Siegel, 2013; McMenamin et al., 2010; Shackman et al., 2009) were marked for removal. For extra safety the validity of component removal was also ensured by visually comparing the signal before and after ICA cleaning. The average number of removed components in each study were as follows: M = 7.20, SD = 3.80 in Study I; M = 8.29, SD = 3.50 in Study II; M = 9.41, SD = 5.49 in Study III, M = 3.36, SD = 2.62 in Study IV, M = 4.70, SD = 2.21 in Study V. Bad channels (Study I: M = 0.11, SD = 0.32; Study II: M = 0.72, SD = 1.04; Study III: M = 1.14, SD = 1.23; Study IV: M = 1.23, SD = 1.14; Study V: M = 0.81, SD = 0.92) were not included in the ICA and were interpolated after cleaning the signal with ICA. The signal was then re-referenced to common average (AVG) or CSD, depending on the type of analysis (see tables in Results section).

### Signal analysis

#### Channel-pair and cluster-based analyses

All channel and source level analyses were performed using mne-python (Gramfort et al., 2014) and custom code (Magnuski, 2020a; Magnuski, 2020c; Magnuski and Ruban, 2020; all available on github). Half of the channel level analyses used CSD reference and the other half used average reference (AVG; see Tables 3–6 for a summary). For each data set the continuous signal from eyes-closed rest period was used, starting 2 s after rest onset to avoid potential artifacts related to eyes closing. Power spectra were calculated using Welch method with 2 s long windows and a window step of 0.5 s. Welch windows overlapping with bad signal segments were removed and all remaining windows were averaged. This operation was performed for every channel and every subject giving rise to subjects by channels by frequencies matrix. Alpha asymmetry was calculated by first averaging spectral power in 8–13 Hz band, log-transforming and then for each left–right channel pair subtracting values obtained for left sites from those for right sites. We calculated alpha asymmetry as log(right)–log(left) because this is the most common approach.

#### Cluster-based analyses on standardized data

When the right-side alpha pattern is topographically different from the left-side alpha pattern we cannot expect left vs right subtraction to reliably uncover alpha asymmetry. To alleviate this problem we performed an additional analysis that does not rely on subtraction. In this approach all frontal channels were used including those at the midline. Moreover, the alpha frequency range (8–13 Hz) was not averaged, and all frequency bins in this range were analyzed. Instead of right–left subtraction we standardized (z-scored) power in the selected channels by frequency space for each subject. Standardization should highlight asymmetry patterns that escape the traditional left vs right comparison, while also being sensitive to effects that do not rely on asymmetry at all.

#### Source level analyses

Because channel-level projections can be highly variable depending on the source orientation we additionally perform analyses in the source space. We first digitized channel positions for a representative subject from Study III using photogrammetry. This step was performed because the default channel positions for many EEG caps assume a spherical head, which is not a realistic assumption for source localization. A hand-held video camera was used to record EEG cap placement on the head of the representative subject from multiple angles. The recorded video was processed with 3DF Zephyr (3DFlow 3DF Zephyr, Aerial Education version: Toldo et al., 2015) in order to obtain a 3D model of the subject’s head and EEG cap. Channels positions’ coordinates were extracted by manually placing control points on each channel in the 3d reconstruction. After coregistering the digitized channel positions with the fsaverage FreeSurfer head model (Dale et al., 1999, see next paragraph) we confirmed that the chosen subject’s head shape was very similar to the fsaverage head model. These digitized channel positions (and thus the coregistration with the fsaverage) were used for all subjects in Studies I, III, and IV. As a result in Studies I and IV data from a few channels were not included in the source localization because these channels were not present in the created digitization template. For Studies II and V default EGI channel positions were coregistered with the fsaverage model, because they assume a realistic head shape.

We employed Boundary Element Method (BEM) for the forward problem. We first created a three-layer (inner skull, outer skull, and outer skin) BEM model based on the FreeSurfer fsaverage template (Dale et al., 1999; Fischl et al., 1999). Next, the leadfield was constructed for a grid of 8196 equidistant source points covering the whole fsaverage cortical surface. Finally we used beamforming (Dynamic Imaging of Coherent Sources, DICS: Gross et al., 2001) to infer the source-level activity in alpha band.

The cross-spectral density matrices, necessary for DICS beamforming, were computed using Morlet wavelets (of length equal to seven cycles) on the continuous signal from the eyes-closed rest period starting from 2 s after rest onset. Bad signal segments were ignored, just like in the channel level analyses. To make the inverse solution more stable and noise-resistant we used a regularization parameter of 0.05 (van Vliet et al., 2018). Localized power maps were morphed to a symmetrical version of fsaverage brain (fsaverage_sym; Greve et al., 2013; Van Veen et al., 1997) to allow for left vs right comparisons. The asymmetry was computed in the same way as in the channel-pair and cluster-based analyses.

### Statistical analysis

We performed a multiverse analysis consisting of 270 analyses differing in: (a) the signal space used: channel space (average reference: 120 analyses, 44%, CSD reference: 120, 44%) or source space (DICS beamforming, 30, 11%); (b) subselection of the signal space: channel pairs (120, 44%), all frontal pairs with cluster correction (60, 22%) or all frontal channels with cluster-based correction and standardization instead of subtraction (60; 22%); (c) statistical contrast used: group comparisons or testing for a linear relationship (more information in the paragraph below); and (d) statistical control for confounding variables (135 without and 135 with control for confounds).

### Variants of statistical analysis

We used four different statistical contrasts in the analyses: two group contrasts and two linear contrasts. Group contrasts included: comparison between diagnosed and healthy controls (DvsHC) or sub-clinical and healthy controls (SvsHC). For group contrasts we used Welch t test, which does not assume equal variance of the compared groups (Delacre et al., 2017). Linear contrasts were performed either for all subjects together (allReg) or only for the diagnosed subjects (DReg).

These statistical contrasts are only used in the studies where they apply: for example, contrasting healthy and diagnosed subjects (DvsHC) cannot be done for Study II, where only healthy and sub-clinical participants are available. In the same way, comparing sub-clinical and healthy controls (SvsHC) is not possible in Studies I and V, where only healthy and diagnosed participants are available. The availability of statistical contrasts in individual studies is summarized in Table 13. Whenever a contrast is available for a given study it is performed for all analysis spaces: average reference (AVG), CSD, and source level data.

**Table 13.**
 Summary of the contrasts (DvsHC – diagnosed vs healthy controls; SvsHC – sub-clinical vs healthy controls; allReg – linear regression between FAA and depression questionnaire score for all subjects together; DReg – linear regression only for the diagnosed subjects) and confounds (age, gender, and education) used in each study.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">STUDY</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>I</td>
      <td>II</td>
      <td>III</td>
      <td>IV</td>
      <td>V</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="5">Contrast type</td>
      <td></td>
    </tr>
    <tr>
      <td>DvsHC</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td>SvsHC</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>allReg</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td>DReg</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="5">Control for confounds</td>
      <td></td>
    </tr>
    <tr>
      <td>gender</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td>age</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td>education</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

For each statistical contrast and study we perform two data analysis approaches: (a) classical comparison of selected channel pairs and (b) cluster-based permutation test on the whole frontal asymmetry space. The channel pair analyses use two channel pairs, F3–F4 and F7–F8, or the corresponding channel pairs in the EGI cap (Studies II and V). The source space and standardized data analyses employ only the cluster-based approach.

Finally, all the analysis variants are performed twice: once in their standard form and the second time statistically controlling for potential confounding variables: gender, age, and education. These variables are added to the regression model explaining FAA, where the predictor of interest is either the depression status (DvsHC and SvsHC contrasts) or depression score in BDI/PHQ-9 questionnaire (allReg and DReg contrasts). The availability of these confounding variables in individual studies is shown in Table 13.

### Cluster-based permutation test

All the analyses that involve more than two selected channel pairs use cluster-based permutation tests (Maris and Oostenveld, 2007) to correct for multiple comparisons. Cluster-based permutation test is a nonparametric multiple comparison correction where the hypothesis of difference between conditions is evaluated at the level of multidimensional clusters. Clusters are formed by performing a chosen statistical test in the n-dimensional search space (channels or channels by frequencies in most of the analyses reported here) and grouping adjacent points where the test statistic passed some predefined threshold (typically an alpha level of 0.05). Each obtained cluster is then summarized by summing the statistics of all its members – that is, all adjacent points forming the cluster. These cluster summaries (cluster statistics) are then compared to a permutation null distribution of the maximum cluster statistic to obtain a p-value. The null distribution is approximated by a Monte-Carlo method where in each draw the condition labels are permuted between subjects (in this study: diagnosis status or BDI scores) and the statistical tests and clusters are computed in the same manner as for non-permuted data. As a result each Monte-Carlo draw produces cluster statistics from which the highest positive and the lowest negative value is saved. These values, when aggregated from all Monte-Carlo draws, constitute the null distribution for positive and negative effects to which cluster statistics from the actual analysis are compared.

For cluster-based analyses on standardized data, because they are sensitive to effects that do not have to be asymmetrical, significant test results were followed up with tests for asymmetry of the effects. For each cluster with p-value below 0.05 a chi-square test for two proportions was conducted comparing the proportion of cluster points on the left and right side of the head. Significant outcome of the test suggests that the cluster is asymmetrical.

Throughout all the analyses, including cluster-based permutation tests, we use an alpha level of 0.05. The same alpha level is used for cluster entry threshold in cluster-based tests. Results for single channel pairs, reported in Table 1, include also effect size (Cohen’s d for group comparisons, Pearson’s r for regression) and its 95% confidence interval calculated using bias-corrected accelerated bootstrap (Tibshirani and Efron, 1993; Ho et al., 2019).

### Analyses on aggregated data

To increase statistical power we perform additional analyses where we aggregate data across all studies that include identical contrasts. Because individual studies have different channel layouts these aggregated analyses are only performed when the studies can be mapped into a common space: (a) the selected channel pairs or (b) the source space. Before aggregation we tested the FAA values for selected channel pairs for equal variance across studies. Because the scale of the data can vary depending on lab-specific equipment or adopted impedance threshold, in case of unequal variance the FAA values were z-scored (centered and scaled) across participants within each study. The z-scoring was performed for channel pairs and source space analyses.

For aggregated channel pair data, we calculate the effect size (Cohen’s d for group comparisons and Pearson’s r for linear relationships) for each combination of contrast × channel pair × channel space (AVG vs CSD) and estimate confidence intervals for the effect size using bias-corrected accelerated bootstrapping (Tibshirani and Efron, 1993; Ho et al., 2019). To estimate support for the claim of ‘no effect’ we calculate Bayes factor for the null hypothesis (BF01; Rouder et al., 2009) using the Pingoin python package (Vallat, 2018).

For aggregated source space data, we use cluster-based permutation tests. We do not estimate effect size and its confidence interval in source space because this would require a priori specification of a relatively narrow region of interest, which is not known. For all analyses using allReg or DReg contrasts the depression questionnaire scores are z-scored within each study. This is done because the aggregated studies use different questionnaires: BDI-I (Studies I and II), BDI-II (Studies III and IV), or PHQ-9 (Study V).

The aggregated analyses, like all other analyses, are performed twice: with and without statistical control for confounding variables. However, because not all confounding variables are available across studies, for each study we first explain the FAA data with the confounding variables using a regression model and then standardize and aggregate the model residuals.
