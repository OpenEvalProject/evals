# Electric field causes volumetric changes in the human brain

## Authors

- Miklos Argyelan<sup>1</sup> ([ORCID: 0000-0002-7254-1776](https://orcid.org/0000-0002-7254-1776)) †
- Leif Oltedal<sup>4</sup>
- Zhi-De Deng<sup>6</sup>
- Benjamin Wade<sup>7</sup>
- Marom Bikson<sup>8</sup>
- Andrea Joanlanne<sup>1</sup>
- Sohag Sanghani<sup>1</sup>
- Hauke Bartsch<sup>5</sup>
- Marta Cano<sup>10</sup> ([ORCID: 0000-0003-0675-9483](https://orcid.org/0000-0003-0675-9483))
- Anders M Dale<sup>9</sup>
- Udo Dannlowski<sup>14</sup>
- Annemiek Dols<sup>15</sup>
- Verena Enneking<sup>14</sup>
- Randall Espinoza<sup>16</sup>
- Ute Kessler<sup>4</sup>
- Katherine L Narr<sup>16</sup>
- Ketil J Oedegaard<sup>4</sup>
- Mardien L Oudega<sup>15</sup>
- Ronny Redlich<sup>14</sup>
- Max L Stek<sup>15</sup>
- Akihiro Takamiya<sup>19</sup>
- Louise Emsell<sup>21</sup>
- Filip Bouckaert<sup>21</sup>
- Pascal Sienaert<sup>22</sup>
- Jesus Pujol<sup>11</sup>
- Indira Tendolkar<sup>24</sup>
- Philip van Eijndhoven<sup>24</sup>
- Georgios Petrides<sup>1</sup>
- Anil K Malhotra<sup>1</sup>
- Christopher Abbott<sup>27</sup>

### Affiliations

1. Department of Psychiatry The Zucker Hillside Hospital Glen Oaks United States
2. Center for Neuroscience, Feinstein Institute for Medical Research Manhasset United States
3. Department of Psychiatry Zucker School of Medicine Hempstead United States
4. Department of Clinical Medicine University of Bergen Bergen Norway
5. Department of Radiology Haukeland University Hospital, Mohn Medical Imaging and Visualization Centre Bergen Norway
6. Experimental Therapeutics and Pathophysiology Branch National Institute of Mental Health Bethesda United States
7. Department of Neurology, Ahmanson-Lovelace Brain Mapping Center University of California, Los Angeles Los Angeles United States
8. Department of Biomedical Engineering The City College of the City University of New York New York United States
9. Center for Multimodal Imaging and Genetics University of California, San Diego San Diego United States
10. Department of Psychiatry Bellvitge University Hospital-IDIBELL Barcelona Spain
11. CIBERSAM, Carlos III Health Institute Barcelona Spain
12. Department of Radiology University of California, San Diego San Diego United States
13. Department of Neurosciences University of California, San Diego San Diego United States
14. Department of Psychiatry and Psychotherapy University of Muenster Muenster Germany
15. Department of Psychiatry Amsterdam UMC, location VUmc, GGZinGeest, Old Age Psychiatry, Amsterdam Neuroscience Amsterdam Netherlands
16. Department of Neurology University of California, Los Angeles Los Angeles United States
17. Department of Psychiatry and Biobehavioral Sciences University of California, Los Angeles Los Angeles United States
18. Division of Psychiatry Haukeland University Hospital, University of Bergen Bergen Norway
19. Department of Neuropsychiatry Keio University School of Medicine Tokyo Japan
20. Center for Psychiatry and Behavioral Science, Komagino Hospital Tokyo Japan
21. Department of Geriatric Psychiatry, University Psychiatric Center KU Leuven Leuven Belgium
22. Academic center for ECT and Neurostimulation (AcCENT), University Psychiatric Center KU Leuven Kortenberg Belgium
23. MRI Research Unit, Department of Radiology Hospital del Mar Barcelona Spain
24. Department of Psychiatry Radboud University Medical Center Nijmegen Netherlands
25. Donders Institute for Brain Cognition and Behavior, Centre for Cognitive Neuroimaging Nijmegen Netherlands
26. Faculty of Medicine and LVR Clinic for Psychiatry and Psychotherapy University of Duisburg-Essen Essen Germany
27. Department of Psychiatry University of New Mexico School of Medicine Albuquerque United States

† Corresponding author

## Abstract

Recent longitudinal neuroimaging studies in patients with electroconvulsive therapy (ECT) suggest local effects of electric stimulation (lateralized) occur in tandem with global seizure activity (generalized). We used electric field (EF) modeling in 151 ECT treated patients with depression to determine the regional relationships between EF, unbiased longitudinal volume change, and antidepressant response across 85 brain regions. The majority of regional volumes increased significantly, and volumetric changes correlated with regional electric field (t = 3.77, df = 83, r = 0.38, p=0.0003). After controlling for nuisance variables (age, treatment number, and study site), we identified two regions (left amygdala and left hippocampus) with a strong relationship between EF and volume change (FDR corrected p<0.01). However, neither structural volume changes nor electric field was associated with antidepressant response. In summary, we showed that high electrical fields are strongly associated with robust volume changes in a dose-dependent fashion.

## Introduction

Electroconvulsive therapy (ECT) remains the most effective approach for treatment resistant depressive episodes, as well as the most established neuromodulation technique (UK ECT Review Group, 2003; Fink and Taylor, 2007). Despite intensive research, however, the mechanism of action for ECT remains unknown, but does involve at least two potentially therapeutic components: electric perturbation and/or seizure activity. One common element across various neuromodulation techniques is the application of different intensities of electric field (EF) on the human brain. Understanding how ECT-induced EF interacts with the cortex and subcortical structures can both advance our mechanistic understanding of ECT and enrich our understanding of other neuromodulation approaches such as magnetic seizure therapy (MST), transcranial magnetic stimulation (TMS), transcranial direct current stimulation (tDCS), and deep brain stimulation (DBS).

A recent longitudinal ECT-imaging study from the Global ECT-MRI Collaboration (GEMRIC) (Oltedal et al., 2018) assessed hippocampal volume changes in a large cohort of subjects (N = 268) receiving right unilateral (RUL) or bilateral (BL) electrode placements. The results demonstrated that the volume of the hippocampus increased over the course of ECT treatment and correlated with the number of ECT sessions administered during the ECT series. In addition, the subjects receiving RUL electrode placement had a significantly larger volume change ipsilateral to the side of stimulation, consistent with previous ECT-neuroimaging observations (Abbott et al., 2014; Dukart et al., 2014; Pirnia et al., 2016; Bouckaert et al., 2016; Sartorius et al., 2016; Cano et al., 2018). Our most recent study of 331 subjects with longitudinal MRI scanning pre- and post-ECT showed brain volume increases across several subcortical and cortical regions with strong lateralization of the effects if the electrode placement was RUL (Ousdal et al., 2019). Contrary to a priori expectations (Joshi et al., 2016; Cano et al., 2017), increased volume in these key areas did not translate to better clinical outcome. While the association between the number of ECT sessions and volume change and the laterality of the volume changes all implied a dose–response causative relationship, the role of ECT-mediated neuroplasticity and the underlying mechanism for antidepressant response remains elusive. Furthermore, given the naturalistic design of the studies included for mega-analysis (e.g., non-responders had a longer ECT course and were frequently switched to bilateral treatment at varying intervals), both the number of ECT sessions and electrode placement varied depending on the clinical response, further confounding the dose-response association and its interpretation.

Recent research has challenged the notion that a primary purpose of electric stimulation in treating depression is to generate widespread seizure activity (Sackeim, 2015; Regenold et al., 2015). Alternatively, electric stimulation may be a therapeutic component of ECT and similar to other non-convulsive neuromodulation treatments. Finite-element simulation was developed to estimate the spatial distribution of the electric field on a voxel-wise basis (Lee et al., 2012; Bikson et al., 2012). The technique was recently validated in humans (Huang et al., 2017). Preliminary computational analyses based on three realistic head models suggested that the ECT electric field distribution had a direct association with clinical and cognitive outcomes, explaining the rationale behind different electrode placement strategies in ECT treatment (Bai et al., 2017). This finding is in agreement with our previous observation where RUL treatment induced higher volumetric changes in the right hippocampus compared to the left (Oltedal et al., 2018), implying that more lateralized electric stimulation rather than a global generalized seizure, may be responsible at least for part of the antidepressant effects of ECT. However, to date, no study has demonstrated the relationship between ECT electric field distribution and treatment response. In this study, we used the large Global ECT-MRI Research Collaboration (GEMRIC) ECT-imaging data set to explicitly determine the relationships between regional 1) electric field strength and volume changes, 2) volume changes and antidepressant response, and 3) electric field and antidepressant response. For the purpose of our primary research question and in contrast to previous GEMRIC investigations, we limited the analyses to subjects that only received right unilateral electrode placement.

## Results

### Clinical results

Subjects showed an average MADRS improvement of 61.3%±33.9% following ECT (pre-ECT MADRS 33.9 (range: 14–54), post-ECT MADRS 12.9 (range: 0–51). Highly significant correlations between age and clinical response (t = 5.75, df = 149, r = 0.43, p<10−7, older patients responded better), as well as age and total brain volume (t = −7.32, df = 149, r = −0.51, p<10−10) were also observed.

### Laterality of electric field and volume change

ECT was associated with increased volume across all brain regions except the brain stem and bilateral cerebellum cortex (Supplementary file 1). In the majority of the regions, right hemisphere regions had greater volumetric change with respect to the corresponding left hemisphere region; no left hemipshere regions had greater volumetric changes compared to the corresponding right-sided region (Supplementary file 2, Figure 1). Average EF strongly correlated with ∆Vol across the ROIs (Figure 1, t = 3.77, df = 83, r = 0.38, p=0.0003). To show that this correlation was not simply due to a general effect of the hemisphere (right side had higher EF and volume change while left side had lower values), we calculated laterality indices in both EF and volume change. The correlation between laterality indices for EF and ∆Vol also had a positive relationship (Figure 2, t = 2.13, df = 40, r = 0.32, p=0.04) across 42 regions (brain stem is missing, since it is not a bilateral structure).

![Figure 1.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig1-v2.jpg)

**Figure 1.:** Upper panel first row: Mean EF across 85 brain regions; second row: the effect size of volume changes between baseline and at the end of the course of ECT across 85 regions. Lower panel, left: Effect sizes of right unilateral stimulations were consistently higher on the right side than on the left side. Lower panel, right: Scatter plot of regional EF versus regional volume change (r = 0.38; p <0.001; df = 83; t = 3.77). (d) = Cohen’s d effect size..

![Figure 2.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig2-v2.jpg)

**Figure 2.:** Regression line indicates the correlation between laterality indices of EF and volume change (r = 0.32; p<0.05; df = 40; t = 2.13).

### Electric field and volume change

In a multiple regression analysis controlled for age, number of ECT sessions and site, we found that left hippocampus and left amygdala had a strong relationship with EF in these regions (FDR corrected p<0.01, Table 1). Post hoc analyses of the hippocampus (Figure 3) and amygdala (Figure 4) illustrate that the relationship between EF and ∆Vol was dose-dependent and scaled across the hemispheres (hippocampus: t = 5.97, df = 300, r = 0.3259, p<0.0001; amygdala: t = 11.3538, df = 300, r = 0.5482, p<0.0001). Age was a necessary covariate since it was a confound in our model: both the spatial distribution of EF and volume changes correlate with age (Deng et al., 2015). We add number of ECT as a covariate to the model to be able to compare the relative influence of EF and number of ECT on volume change. In both left hippocampus and amygdala the effect size of EF was the largest (hippocampus: tEF = 4.5, tAge = −2.7, tECTnum = 3.3, amygdala: tEF = 3.9, tAge = −1.1, tECTnum = 2.1; Table 1).

![Figure 3.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig3-v2.jpg)

**Figure 3.:** Left: Scatterplot of EF versus volume change in the hippocampus (t = 5.97, df = 300, r = 0.33, p < 0.0001, left and right side together). There is a significant relationship on the left side (orange dots; t = 4.53, df = 149, r = 0.35, p < 0.0001), but not on the right side (probably due to ceiling effect) (t = 1.59, df = 149, r = 0.13, p = 0.11). Right: The difference in right and left hippocampal volume changes is significant (t = 7.76, df = 150, mean difference = 0.011, p < 0.0001).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** To test the specificity of our measures in the left hippocampus (FDR corrected finding) we permutated the labels across the 85 ROIs, both for the volume changes (left) and for the EF values (right) and calculated correlations between the EF and volume change of these regions, respectively. This way we received 85 different values, where one of them was the ‘correct’ correlation, indicated with red dots. The ‘correct’ correlations between the EF and corresponding volume outperformed the other correlations (were in the top five percentile) from non-matching pairs, indicating that our findings were not merely a general correlation with some average values across regions, further strengthening the casual link between EF and volume change.

![Figure 4.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig4-v2.jpg)

**Figure 4.:** Left: Scatterplot of EF versus volume change in the amygdala (t = 11.35, df = 300, r = 0.55, p<0.0001; left and right side together). Both the left (orange dots) and right (blue dots) hemisphere shows highly significant relationships (t = 4.01, df = 149, r = 0.31, p=0.0001; and t = 4.02, df = 149, r = 0.31, p=0.0001). Right: The difference in right and left amygdala volume changes is significant (t = 13.58, df = 150, mean difference = 0.029, p<0.0001).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** To test the specificity of our measures in the left amygdala (FDR corrected finding) we permutated the labels across the 85 ROIs, both for the volume changes (left) and for the EF values (right) and calculated correlations between the EF and volume change of these regions, respectively. This way we received 85 different values, where one of them was the ‘correct’ correlation, indicated with red dots. The ‘correct’ correlations between the EF and corresponding volume outperformed the other correlations (were in the top five percentile) from non-matching pairs, indicating that our findings were not merely a general correlation with some average values across regions, further strengthening the casual link between EF and volume change.

**Table 1.**
 The relationship between volume changes and EF across individuals (Δ Vol ~ EF + Age + ECTnum).


<table>
  <thead>
    <tr>
      <th></th>
      <th>roi</th>
      <th>tEF</th>
      <th>pEF</th>
      <th>tAge</th>
      <th>tECTnum</th>
      <th>BHEFFDR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Δ VOLLeft.Cerebellum.Cortex</td>
      <td>−0.3668</td>
      <td>0.7143</td>
      <td>−0.1150</td>
      <td>1.9368</td>
      <td>0.8205</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Δ VOLLeft.Thalamus.Proper</td>
      <td>0.0244</td>
      <td>0.9805</td>
      <td>−0.4046</td>
      <td>2.8696</td>
      <td>0.9952</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Δ VOLLeft.Caudate</td>
      <td>0.6555</td>
      <td>0.5132</td>
      <td>−0.8301</td>
      <td>2.6428</td>
      <td>0.6924</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Δ VOLLeft.Putamen</td>
      <td>0.5737</td>
      <td>0.5671</td>
      <td>−0.5992</td>
      <td>1.3203</td>
      <td>0.7212</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Δ VOLLeft.Pallidum</td>
      <td>0.0060</td>
      <td>0.9952</td>
      <td>0.1026</td>
      <td>1.2295</td>
      <td>0.9952</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Δ VOLBrain.Stem</td>
      <td>1.2114</td>
      <td>0.2278</td>
      <td>0.8536</td>
      <td>1.2309</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Δ VOLLeft.Hippocampus</td>
      <td>4.5102</td>
      <td>0.0000</td>
      <td>−2.6814</td>
      <td>3.3221</td>
      <td>0.0012</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Δ VOLLeft.Amygdala</td>
      <td>3.9069</td>
      <td>0.0001</td>
      <td>−1.0572</td>
      <td>2.1018</td>
      <td>0.0061</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Δ VOLLeft.Accumbens.area</td>
      <td>2.0238</td>
      <td>0.0449</td>
      <td>−3.4456</td>
      <td>1.7246</td>
      <td>0.1737</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Δ VOLLeft.VentralDC</td>
      <td>0.1740</td>
      <td>0.8621</td>
      <td>0.0605</td>
      <td>2.2614</td>
      <td>0.9395</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Δ VOLRight.Cerebellum.Cortex</td>
      <td>−0.5564</td>
      <td>0.5788</td>
      <td>0.0677</td>
      <td>1.3212</td>
      <td>0.7235</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Δ VOLRight.Thalamus.Proper</td>
      <td>0.4582</td>
      <td>0.6475</td>
      <td>0.3541</td>
      <td>4.0787</td>
      <td>0.7712</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Δ VOLRight.Caudate</td>
      <td>1.2293</td>
      <td>0.2210</td>
      <td>1.0254</td>
      <td>1.5097</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Δ VOLRight.Putamen</td>
      <td>1.0724</td>
      <td>0.2854</td>
      <td>−0.5112</td>
      <td>1.4987</td>
      <td>0.4756</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Δ VOLRight.Pallidum</td>
      <td>0.6045</td>
      <td>0.5465</td>
      <td>0.8016</td>
      <td>2.9589</td>
      <td>0.7181</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Δ VOLRight.Hippocampus</td>
      <td>1.5090</td>
      <td>0.1336</td>
      <td>−1.2924</td>
      <td>3.2473</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Δ VOLRight.Amygdala</td>
      <td>2.9945</td>
      <td>0.0032</td>
      <td>−0.6087</td>
      <td>4.2603</td>
      <td>0.0344</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Δ VOLRight.Accumbens.area</td>
      <td>1.9563</td>
      <td>0.0524</td>
      <td>−0.8782</td>
      <td>3.5228</td>
      <td>0.1937</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Δ VOLRight.VentralDC</td>
      <td>0.3488</td>
      <td>0.7278</td>
      <td>0.5197</td>
      <td>0.7438</td>
      <td>0.8248</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Δ VOLctx.lh.bankssts</td>
      <td>1.1757</td>
      <td>0.2417</td>
      <td>−0.4102</td>
      <td>2.5801</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Δ VOLctx.lh.caudalanteriorcingulate</td>
      <td>1.3404</td>
      <td>0.1823</td>
      <td>−1.2881</td>
      <td>2.2330</td>
      <td>0.4254</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Δ VOLctx.lh.caudalmiddlefrontal</td>
      <td>−1.8989</td>
      <td>0.0596</td>
      <td>−0.3804</td>
      <td>2.0087</td>
      <td>0.2112</td>
    </tr>
    <tr>
      <td>23</td>
      <td>Δ VOLctx.lh.cuneus</td>
      <td>0.9827</td>
      <td>0.3274</td>
      <td>0.1037</td>
      <td>2.0348</td>
      <td>0.5352</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Δ VOLctx.lh.entorhinal</td>
      <td>3.2229</td>
      <td>0.0016</td>
      <td>−1.2447</td>
      <td>1.6659</td>
      <td>0.0335</td>
    </tr>
    <tr>
      <td>25</td>
      <td>Δ VOLctx.lh.fusiform</td>
      <td>3.0717</td>
      <td>0.0026</td>
      <td>−0.1806</td>
      <td>2.1319</td>
      <td>0.0344</td>
    </tr>
    <tr>
      <td>26</td>
      <td>Δ VOLctx.lh.inferiorparietal</td>
      <td>1.5131</td>
      <td>0.1325</td>
      <td>0.8515</td>
      <td>2.3077</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>27</td>
      <td>Δ VOLctx.lh.inferiortemporal</td>
      <td>2.6985</td>
      <td>0.0078</td>
      <td>0.6415</td>
      <td>1.9131</td>
      <td>0.0577</td>
    </tr>
    <tr>
      <td>28</td>
      <td>Δ VOLctx.lh.isthmuscingulate</td>
      <td>−0.3275</td>
      <td>0.7438</td>
      <td>−0.4344</td>
      <td>2.9060</td>
      <td>0.8319</td>
    </tr>
    <tr>
      <td>29</td>
      <td>Δ VOLctx.lh.lateraloccipital</td>
      <td>1.1916</td>
      <td>0.2354</td>
      <td>0.3669</td>
      <td>1.2752</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>30</td>
      <td>Δ VOLctx.lh.lateralorbitofrontal</td>
      <td>1.4274</td>
      <td>0.1557</td>
      <td>−0.0081</td>
      <td>1.5758</td>
      <td>0.3780</td>
    </tr>
    <tr>
      <td>31</td>
      <td>Δ VOLctx.lh.lingual</td>
      <td>0.1391</td>
      <td>0.8896</td>
      <td>0.3506</td>
      <td>2.4745</td>
      <td>0.9572</td>
    </tr>
    <tr>
      <td>32</td>
      <td>Δ VOLctx.lh.medialorbitofrontal</td>
      <td>1.0744</td>
      <td>0.2845</td>
      <td>−0.1246</td>
      <td>1.1852</td>
      <td>0.4756</td>
    </tr>
    <tr>
      <td>33</td>
      <td>Δ VOLctx.lh.middletemporal</td>
      <td>2.0679</td>
      <td>0.0405</td>
      <td>−0.3780</td>
      <td>2.2600</td>
      <td>0.1720</td>
    </tr>
    <tr>
      <td>34</td>
      <td>Δ VOLctx.lh.parahippocampal</td>
      <td>1.2683</td>
      <td>0.2068</td>
      <td>−0.2446</td>
      <td>2.8373</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>35</td>
      <td>Δ VOLctx.lh.paracentral</td>
      <td>−2.0829</td>
      <td>0.0391</td>
      <td>0.2511</td>
      <td>4.0937</td>
      <td>0.1720</td>
    </tr>
    <tr>
      <td>36</td>
      <td>Δ VOLctx.lh.parsopercularis</td>
      <td>−0.6949</td>
      <td>0.4883</td>
      <td>−0.7822</td>
      <td>1.8435</td>
      <td>0.6694</td>
    </tr>
    <tr>
      <td>37</td>
      <td>Δ VOLctx.lh.parsorbitalis</td>
      <td>0.8057</td>
      <td>0.4218</td>
      <td>−1.0427</td>
      <td>0.9524</td>
      <td>0.6289</td>
    </tr>
    <tr>
      <td>38</td>
      <td>Δ VOLctx.lh.parstriangularis</td>
      <td>0.8228</td>
      <td>0.4120</td>
      <td>−1.2157</td>
      <td>2.7977</td>
      <td>0.6254</td>
    </tr>
    <tr>
      <td>39</td>
      <td>Δ VOLctx.lh.pericalcarine</td>
      <td>0.4426</td>
      <td>0.6587</td>
      <td>−0.0479</td>
      <td>1.8463</td>
      <td>0.7712</td>
    </tr>
    <tr>
      <td>40</td>
      <td>Δ VOLctx.lh.postcentral</td>
      <td>0.8692</td>
      <td>0.3862</td>
      <td>−1.7655</td>
      <td>2.5145</td>
      <td>0.5969</td>
    </tr>
    <tr>
      <td>41</td>
      <td>Δ VOLctx.lh.posteriorcingulate</td>
      <td>−0.8698</td>
      <td>0.3859</td>
      <td>−0.6961</td>
      <td>3.3193</td>
      <td>0.5969</td>
    </tr>
    <tr>
      <td>42</td>
      <td>Δ VOLctx.lh.precentral</td>
      <td>−0.7279</td>
      <td>0.4679</td>
      <td>−1.2884</td>
      <td>2.4234</td>
      <td>0.6682</td>
    </tr>
    <tr>
      <td>43</td>
      <td>Δ VOLctx.lh.precuneus</td>
      <td>−1.5879</td>
      <td>0.1145</td>
      <td>−0.4353</td>
      <td>3.6729</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>44</td>
      <td>Δ VOLctx.lh.rostralanteriorcingulate</td>
      <td>1.3315</td>
      <td>0.1852</td>
      <td>−0.4449</td>
      <td>0.5630</td>
      <td>0.4254</td>
    </tr>
    <tr>
      <td>45</td>
      <td>Δ VOLctx.lh.rostralmiddlefrontal</td>
      <td>−0.7192</td>
      <td>0.4732</td>
      <td>−1.6205</td>
      <td>1.1936</td>
      <td>0.6682</td>
    </tr>
    <tr>
      <td>46</td>
      <td>Δ VOLctx.lh.superiorfrontal</td>
      <td>−1.2073</td>
      <td>0.2293</td>
      <td>−0.5851</td>
      <td>2.1065</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>47</td>
      <td>Δ VOLctx.lh.superiorparietal</td>
      <td>−1.7423</td>
      <td>0.0836</td>
      <td>0.6952</td>
      <td>3.3288</td>
      <td>0.2734</td>
    </tr>
    <tr>
      <td>48</td>
      <td>Δ VOLctx.lh.superiortemporal</td>
      <td>2.2820</td>
      <td>0.0240</td>
      <td>−2.0868</td>
      <td>1.6393</td>
      <td>0.1199</td>
    </tr>
    <tr>
      <td>49</td>
      <td>Δ VOLctx.lh.supramarginal</td>
      <td>0.5717</td>
      <td>0.5685</td>
      <td>−0.2467</td>
      <td>2.1282</td>
      <td>0.7212</td>
    </tr>
    <tr>
      <td>50</td>
      <td>Δ VOLctx.lh.frontalpole</td>
      <td>−0.2029</td>
      <td>0.8395</td>
      <td>−0.2904</td>
      <td>0.4776</td>
      <td>0.9267</td>
    </tr>
    <tr>
      <td>51</td>
      <td>Δ VOLctx.lh.temporalpole</td>
      <td>2.5288</td>
      <td>0.0125</td>
      <td>−0.0731</td>
      <td>1.3167</td>
      <td>0.0762</td>
    </tr>
    <tr>
      <td>52</td>
      <td>Δ VOLctx.lh.transversetemporal</td>
      <td>0.4387</td>
      <td>0.6616</td>
      <td>−0.4617</td>
      <td>2.1817</td>
      <td>0.7712</td>
    </tr>
    <tr>
      <td>53</td>
      <td>Δ VOLctx.rh.bankssts</td>
      <td>0.1121</td>
      <td>0.9109</td>
      <td>2.0777</td>
      <td>2.9991</td>
      <td>0.9678</td>
    </tr>
    <tr>
      <td>54</td>
      <td>Δ VOLctx.rh.caudalanteriorcingulate</td>
      <td>−1.4295</td>
      <td>0.1551</td>
      <td>1.2935</td>
      <td>2.4016</td>
      <td>0.3780</td>
    </tr>
    <tr>
      <td>55</td>
      <td>Δ VOLctx.rh.caudalmiddlefrontal</td>
      <td>−2.9569</td>
      <td>0.0036</td>
      <td>1.6943</td>
      <td>2.6065</td>
      <td>0.0344</td>
    </tr>
    <tr>
      <td>56</td>
      <td>Δ VOLctx.rh.cuneus</td>
      <td>−0.0087</td>
      <td>0.9930</td>
      <td>−1.1806</td>
      <td>2.4017</td>
      <td>0.9952</td>
    </tr>
    <tr>
      <td>57</td>
      <td>Δ VOLctx.rh.entorhinal</td>
      <td>1.2514</td>
      <td>0.2129</td>
      <td>0.7897</td>
      <td>2.4722</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>58</td>
      <td>Δ VOLctx.rh.fusiform</td>
      <td>1.5380</td>
      <td>0.1263</td>
      <td>0.7997</td>
      <td>4.7854</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>59</td>
      <td>Δ VOLctx.rh.inferiorparietal</td>
      <td>−2.9902</td>
      <td>0.0033</td>
      <td>1.6520</td>
      <td>0.7114</td>
      <td>0.0344</td>
    </tr>
    <tr>
      <td>60</td>
      <td>Δ VOLctx.rh.inferiortemporal</td>
      <td>0.9300</td>
      <td>0.3540</td>
      <td>1.9310</td>
      <td>3.3455</td>
      <td>0.5677</td>
    </tr>
    <tr>
      <td>61</td>
      <td>Δ VOLctx.rh.isthmuscingulate</td>
      <td>0.0325</td>
      <td>0.9741</td>
      <td>0.4230</td>
      <td>1.1493</td>
      <td>0.9952</td>
    </tr>
    <tr>
      <td>62</td>
      <td>Δ VOLctx.rh.lateraloccipital</td>
      <td>1.1796</td>
      <td>0.2401</td>
      <td>0.6095</td>
      <td>1.5161</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>63</td>
      <td>Δ VOLctx.rh.lateralorbitofrontal</td>
      <td>0.5347</td>
      <td>0.5937</td>
      <td>0.3393</td>
      <td>2.9240</td>
      <td>0.7314</td>
    </tr>
    <tr>
      <td>64</td>
      <td>Δ VOLctx.rh.lingual</td>
      <td>−0.0753</td>
      <td>0.9401</td>
      <td>−1.9555</td>
      <td>3.5258</td>
      <td>0.9865</td>
    </tr>
    <tr>
      <td>65</td>
      <td>Δ VOLctx.rh.medialorbitofrontal</td>
      <td>0.7090</td>
      <td>0.4795</td>
      <td>1.5479</td>
      <td>2.3419</td>
      <td>0.6682</td>
    </tr>
    <tr>
      <td>66</td>
      <td>Δ VOLctx.rh.middletemporal</td>
      <td>−0.6005</td>
      <td>0.5492</td>
      <td>2.1275</td>
      <td>3.6781</td>
      <td>0.7181</td>
    </tr>
    <tr>
      <td>67</td>
      <td>Δ VOLctx.rh.parahippocampal</td>
      <td>1.5217</td>
      <td>0.1303</td>
      <td>0.5057</td>
      <td>3.1874</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>68</td>
      <td>Δ VOLctx.rh.paracentral</td>
      <td>−3.5101</td>
      <td>0.0006</td>
      <td>2.1809</td>
      <td>2.2718</td>
      <td>0.0170</td>
    </tr>
    <tr>
      <td>69</td>
      <td>Δ VOLctx.rh.parsopercularis</td>
      <td>−2.5585</td>
      <td>0.0116</td>
      <td>2.8854</td>
      <td>2.9459</td>
      <td>0.0756</td>
    </tr>
    <tr>
      <td>70</td>
      <td>Δ VOLctx.rh.parsorbitalis</td>
      <td>1.0872</td>
      <td>0.2788</td>
      <td>−0.5812</td>
      <td>2.3737</td>
      <td>0.4756</td>
    </tr>
    <tr>
      <td>71</td>
      <td>Δ VOLctx.rh.parstriangularis</td>
      <td>−1.2468</td>
      <td>0.2146</td>
      <td>1.0686</td>
      <td>2.6086</td>
      <td>0.4466</td>
    </tr>
    <tr>
      <td>72</td>
      <td>Δ VOLctx.rh.pericalcarine</td>
      <td>1.5878</td>
      <td>0.1146</td>
      <td>−0.0096</td>
      <td>2.2815</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>73</td>
      <td>Δ VOLctx.rh.postcentral</td>
      <td>−1.7565</td>
      <td>0.0812</td>
      <td>1.2943</td>
      <td>3.0605</td>
      <td>0.2734</td>
    </tr>
    <tr>
      <td>74</td>
      <td>Δ VOLctx.rh.posteriorcingulate</td>
      <td>−1.5171</td>
      <td>0.1315</td>
      <td>2.0716</td>
      <td>1.4731</td>
      <td>0.3441</td>
    </tr>
    <tr>
      <td>75</td>
      <td>Δ VOLctx.rh.precentral</td>
      <td>−2.4918</td>
      <td>0.0139</td>
      <td>0.9967</td>
      <td>3.7013</td>
      <td>0.0762</td>
    </tr>
    <tr>
      <td>76</td>
      <td>Δ VOLctx.rh.precuneus</td>
      <td>−2.0231</td>
      <td>0.0450</td>
      <td>−0.1921</td>
      <td>2.5419</td>
      <td>0.1737</td>
    </tr>
    <tr>
      <td>77</td>
      <td>Δ VOLctx.rh.rostralanteriorcingulate</td>
      <td>2.2083</td>
      <td>0.0288</td>
      <td>1.3734</td>
      <td>2.3606</td>
      <td>0.1362</td>
    </tr>
    <tr>
      <td>78</td>
      <td>Δ VOLctx.rh.rostralmiddlefrontal</td>
      <td>−2.6842</td>
      <td>0.0081</td>
      <td>0.5804</td>
      <td>2.2235</td>
      <td>0.0577</td>
    </tr>
    <tr>
      <td>79</td>
      <td>Δ VOLctx.rh.superiorfrontal</td>
      <td>−3.0013</td>
      <td>0.0032</td>
      <td>1.1011</td>
      <td>3.2699</td>
      <td>0.0344</td>
    </tr>
    <tr>
      <td>80</td>
      <td>Δ VOLctx.rh.superiorparietal</td>
      <td>−2.7495</td>
      <td>0.0067</td>
      <td>0.9014</td>
      <td>2.0779</td>
      <td>0.0574</td>
    </tr>
    <tr>
      <td>81</td>
      <td>Δ VOLctx.rh.superiortemporal</td>
      <td>0.4377</td>
      <td>0.6623</td>
      <td>1.2455</td>
      <td>4.4002</td>
      <td>0.7712</td>
    </tr>
    <tr>
      <td>82</td>
      <td>Δ VOLctx.rh.supramarginal</td>
      <td>−2.4794</td>
      <td>0.0143</td>
      <td>2.7408</td>
      <td>3.0429</td>
      <td>0.0762</td>
    </tr>
    <tr>
      <td>83</td>
      <td>Δ VOLctx.rh.frontalpole</td>
      <td>1.1256</td>
      <td>0.2623</td>
      <td>−0.1784</td>
      <td>1.9185</td>
      <td>0.4644</td>
    </tr>
    <tr>
      <td>84</td>
      <td>Δ VOLctx.rh.temporalpole</td>
      <td>0.7274</td>
      <td>0.4682</td>
      <td>0.5099</td>
      <td>3.7696</td>
      <td>0.6682</td>
    </tr>
    <tr>
      <td>85</td>
      <td>Δ VOLctx.rh.transversetemporal</td>
      <td>1.1426</td>
      <td>0.2551</td>
      <td>0.6448</td>
      <td>3.2405</td>
      <td>0.4614</td>
    </tr>
  </tbody>
</table>

We also investigated the spatial specificity of these correlations. First, we permutated the regional labels in the volumetric changes across all possible ROIs and calculated the correlations between the EF and ∆Vol. The correlation between EF and the corresponding ∆Vol (Figure 3—figure supplement 1, Figure 4—figure supplement 1, left panels, indicated with red dot) was always in the top 5% among all possible correlations. Second, we permutated the region labels in the EF across all possible ROIs and calculated the correlations between the EF and ∆Vol (Figure 3—figure supplement 1, Figure 4—figure supplement 1 right panels). Overall these results indicate a strong spatial selectivity in the relationship between EF and ∆Vol.

### Electric field, volume change, and clinical response

We further investigated if EF directly or indirectly (mediated via volume change) leads to clinical response. In a multiple regression analysis, we tested if volumetric changes controlled for age, number of ECT sessions, and site had an effect on clinical response measured by MADRS changes. Results indicated that none of the volume changes across the 85 ROIs had a significant relationship with clinical response (Supplementary file 3, hippocampus: tΔVOL = 0.2, tAge = 5.4, tECTnum = −2.7, amygdala: tΔVOL = 0.1, tAge = 5.6, tECTnum = −3.0). These results therefore contradicted the hypothesis that EF by increasing brain volume indirectly exerts its effect on clinical response, given the negative results between the volume change (mediator) and MADRS change (outcome). Testing the direct effect of the EF, we failed to find significant correlations between EF and clinical response (Supplementary file 4, hippocampus: tEF = 1.2, tAge = 5.7, tECTnum = −3.0, amygdala: tEF = 1.1, tAge = 5.7, tECTnum = −3.0). Similar to earlier studies, age strongly correlated with both clinical response (Haq et al., 2015; O'Connor et al., 2001), also see Clinical Results) and EF distribution (Deng et al., 2015), therefore we controlled for age in our model. The rationale for including the number of ECT treatments as covariate needs more explanation. Due to the naturalistic nature of the design, where most sites followed the patient until response or site-determined criteria for ECT discontinuation, we observed a negative relationship between clinical response and the number of ECT treatments. Not controlling for this variable could lead to spurious correlation between volume change and clinical response (for more on this see Oltedal et al., 2018). In a post-hoc analysis, we also examined the interaction between EF and volume change in relation to clinical outcome (excluding age as a covariate), but we again failed to find significant effects for any region. To explore further, we investigated if changing age to baseline volume in the mixed model would modify results, but we did not find significant effects (age and baseline volume correlates strongly across almost all regions – Supplementary file 5).

## Discussion

This study investigated the relationship between electric field, volume change and clinical response to ECT. We used a large sample of subjects with depression receiving ECT with right unilateral electrode placement from the GEMRIC database. The key findings included a lateralization (right >left) of the electric field and changes in regional brain volume in association with ECT. The use of right unilateral electrode placement, which elicits greater right hemisphere electric fields, can thus be dissociated from generalized seizure activity such that their contributions to antidepressant mechanisms may be at least partially distinct. Further, regional volume increase and electric field distributions were strongly related, especially in the left hippocampus and left amygdala. Here, the observed relationships between electric field and volume change suggest that a minimum electric field of 30–40 V/m is necessary for subsequent changes in brain structure, and that EF may have a ‘ceiling effect’ above approximately 100 V/m as illustrated for right hippocampal volume (see Figure 3). However, volume change and electric field were not statistically related to clinical response after controlling for age, number of ECT sessions and site. Below, we discuss potential mechanisms for electric field and volume change that may be considered both independent and synergistic with seizure activity. We also discuss potential future directions to elucidate the role of electric field distributions with clinical response.

The biological underpinnings of ECT-mediated volume change (Oltedal et al., 2018; Ousdal et al., 2019) could be related to seizure activity, cerebral blood flow, electric field strength, or synergy between the generalized seizure and electric field (e.g. the electric field determines site and focality of seizure initiation, which can subsequently affect seizure propagation and termination). Several neuroplastic mechanisms including neurogenesis, angiogenesis, synaptogenesis, gliogenesis may be specific to the rapidly changing electric field (Bouckaert et al., 2014; Tang et al., 2017). Although heavily debated (Sorrells et al., 2018; Boldrini et al., 2018; Andreae, 2018), the support for adult neurogenesis is based on pre-clinical studies demonstrating neuronal division and differentiation related to suprathreshold electric stimulation (Scott et al., 2000; Madsen et al., 2000; Perera et al., 2007; Segi-Nishida, 2011). However, neurogenesis as the sole mechanism of neuroplasticity may be incompatible with the time frame and expansive volume change. Specifically, the ECT series is less than one month in duration, but pre-translational investigations have established that adult neurogenesis may take up to six months (Kohler et al., 2011). Furthermore, adult neurogenesis is limited to the hippocampus and olfactory bulb and does not support the volume change in 82 out of 85 regions demonstrated in our investigation (Kornack and Rakic, 1999). Alternatively, volume change may be related to fluid shifts due to vascularization (Hellsten et al., 2004), blood flow changes (Milo et al., 2001; Leaver et al., 2019) and inflammation (Wennström et al., 2004; Jansson et al., 2009; Fluitman et al., 2011; van Buel et al., 2015; Yrondi et al., 2018). Vasogenic edema secondary to the hypertensive surge commonly associated with electroconvulsive stimulation and possible breach of the blood brain barrier could be a potentially iatrogenic mechanism of volumetric increase, but the available pre-clinical and ECT-imaging studies (focused on T2 relaxtion time) so far have produced mixed results (Andrade and Bolwig, 2014; Kunigiri et al., 2007; Bolwig et al., 1977; Nordanskog et al., 2010; Takamiya et al., 2018). The generalized seizure and global changes in blood flow would not explain the laterality of volumetric changes (right >left) ipsilateral to the hemisphere of stimulation as seen in our current and previous investigations (Abbott et al., 2014; Dukart et al., 2014; Pirnia et al., 2016; Bouckaert et al., 2016; Sartorius et al., 2016; Cano et al., 2018). The laterality with electric field and volume change suggest a mechanistic role of the electric field that may be independent or synergistic with seizure generation. Pre-translational investigations have demonstrated that increased stimulus charge increased dendritic arborization in a dose-related fashion (Smitha et al., 2014). Furthermore, the behavioral improvement after electroconvulsive stimulation are related to increased dendritic complexity, synaptic remodeling, and neuronal survival (Jonckheere et al., 2018). However, additional pre-clinical studies are clearly needed to resolve the mechanistic link between electric field and neuroplasticity.

Our original hypothesis was that a) local electric field had a causal role in clinical outcome and that b) the corresponding volume change was mediating this relationship. In order to support this model, data analysis should have indicated 1) a significant correlation between volume change and electric field, 2) a significant correlation between clinical outcome and volume change, and 3) that only the effect of volume change is significant in a multilinear regression model when both electric field and volume change is added as covariates (outcome ~volume change + electric field). However, since volume change showed no correlation with clinical change, neither in this dataset, nor in the recently published broader dataset with more heterogeneous ECT electrode placement (Ousdal et al., 2019), only the first half of this model, namely that electric field strength was associated with volume change, was supported by our data.

The null relationship between electric field, volume change and clinical outcome may be attributed to demographic (age) and other treatment related factors (number of sessions, rate of response). For example, age-related structural brain changes may mediate these relationships and thus were an important consideration in our analysis. Our results are consistent with previous ECT investigations demonstrating that older patients often have higher response rates (O'Connor et al., 2001; Nordenskjöld et al., 2012; Brus et al., 2017). Previous electric field modeling investigations have demonstrated that age-related structural brain changes modulate the spatial distribution of the calculated electric field (Deng et al., 2009). However, when including age in the assessment with electric field, volume change and clinical outcome, our results suggest more complex or alternative mechanisms underlie differential age-related response to ECT.

Additionally, it was necessary to control in our regression models for the number of ECT treatments. In our earlier paper (Oltedal et al., 2018) we found a mild effect between hippocampus volume change and clinical response, but, counterintuitively, increased volume change was associated with worse outcomes. However, this relationship was completely absent when we controlled for the number of ECTs. We have previously demonstrated a dose-response relationship between hippocampal volume change and the number of ECT sessions (Oltedal et al., 2018). Also, due to the naturalistic design, clinical outcome correlated with the number of ECT sessions: patients with the worse or slower response received more ECT treatments. Mediation analysis supported a very similar situation in our sample with p=0.035 and p=0.034 in L and R Hippocampus reflectively (Sobel test).

It was, therefore, necessary to control for the number of ECT sessions to avoid detecting spurious correlations between clinical response and volume change. Without an earlier, fixed mid-point assessment, we are unable to assess differences in rate of change, which could be relevant to specific depression subtypes (Drysdale et al., 2017) and eventual clinical response. Notably, the overall volume changes measured in this study do not permit us to make conclusions about more structure-function relationships that might be better assessed with shape or hippocampal subfield analysis (Roddy et al., 2019; Takamiya et al., 2019).

Finally, the volume change required for response may be non-linear. A minimum electric field of 30–40 V/m may be necessary to induce neuroplasticity. Increasing the electric field between 30–40 V/m and 100 V/m is related to a monotonic increase in hippocampal volume. Electric field above 100 V/m is still associated with hippocampal neuroplasticity but the dose-response relationship may be less robust and represent a ceiling effect of electric-field induced neuroplasticity as illustrated in Figure 3. Surpassing the neurpolasticity threshold (100 V/m) appears to be unrelated to further volumetric increases and antidepressant response. Thus, the relationship between e-field and volumetric changes may be conceptualized as a ‘neuroplasticity threshold’ between 30–40 V/m and 100 V/m. This thresholding effect also preserves the laterality of electric field and neuroplasticity. Our sample was limited to right unilateral electrode placement. In the left hippocampus, the maximum electric field is ~80 V/m (Figure 3) and below the 100 V/m ‘ceiling effect’ noted in the right hemisphere. Consequently, in our right unilateral sample, hippocampal electric field and related changes in neuroplasticity will demonstrate laterality effects.

Our findings indicate widespread and robust volume changes in both cortical and subcortical regions. The GEMRIC group recently published a comprehensive paper on a larger dataset with similar volumetric findings. The processing pipeline that was used has been validated against many commonly used tools for estimating longitudinal volume change (Holland et al., 2012; Holland et al., 2011). Specifically, it was previously compared head-to-head with FreeSurfer 5.3, and we have already repeated this comparison for data from one of the GEMRIC sites (Oltedal et al., 2017). Our comparisons of power estimations based on results from the FreeSurfer longitudinal pipeline and Quarc (Table 3 in Oltedal et al., 2017) were in line with those of the earlier publications. In agreement with previous research, the effect sizes show regional differences indicating that previous studies with smaller sample sizes were underpowered to detect cortical changes, and that can explain why they only found subcortical volume increase. Furthermore, using the same methodology, we did not find any significant volume change in the 95 healthy controls (received no ECT) who were imaged at two time points (Ousdal et al., 2019).

We acknowledge several limitations that influence result interpretation. First, our approach was agnostic to seizure duration, which may contribute to the effects of EF on regional volumes and clinical response. This investigation also does not preclude the possible role of seizure in both volume changes and clinical outcomes. However, the selection of right unilateral electrode placement subjects does attempt to disentangle the impact of the generalized seizure from the lateralized electric field. Second, the electric field models a single current pulse and ignores the temporal dynamics of stimulus (pulse-width, and frequency and duration of the pulse train) (Swartz, 2006; Swartz et al., 2012). Differences in pulse width, for example, may affect volume change and clinical outcomes. Furthermore, differences in maximal charge, unrelated to current amplitude, are different between the US and Europe (Europe permits twice the US maximal charge). The analysis included patients treated with one of two different ECT devices. We controlled for the differences in current related to the two devices with the electric field modeling (800mA for the spECTrum, 900mA for the Thymatron), but we are unable to control for other differences in stimulus delivery related to the device. Third, the study sites in this mega-analysis likely include heterogeneity in patient selection and other treatment related factors that were not controlled. Despite these site differences, the large sample size and additional inclusion criteria permitted whole brain analyses with electric field, and within-subject volume change and clinical outcomes. Finally, we did not assess cognitive correlates with electric field or volume change. General clinical experience and previous results from studies investigating electrode placement strategies indicate that ECT-mediated neurocognitive side effects are influenced by electrode placement (d’Elia, 1970; Sackeim et al., 2000; Kolshus et al., 2017). Previous electric field studies on simulated head models have already shown that cognitive side effects might be attributed to the electric field spatial distributions associated with different electrode placements (Bai et al., 2017; Deng et al., 2011). These considerations would indicate that these volumetric changes might be associated with cognitive side-effects, but further studies are needed to confirm this relationship.

### Conclusion

This investigation is the first demonstration that the ECT-induced electric field is related to increases in cortical and subcortical structures. These results support that the electric field, independent or synergistic with seizure activity and other stimulation parameters, can have a profound effect on the biology of the human brain. The electric path originates from the ECT electrode handle, which delivers a constant stimulus current from the scalp. From the scalp, the electric path travels through skin, skull, cerebral spinal fluid, and brain. Each tissue type has different conductive properties and abundant individual variability (Deng et al., 2015). This variability creates different electric field doses despite the similar current at the scalp. These differences in current may lead to both differences in volume changes as well as clinical outcomes. In our investigation, the electric field-induced volume change in the bilateral amygdala and the left hippocampus suggests regional specificity, but the association of these volumetric changes with clinical outcomes remains elusive. Better controlled prospective trials are needed to answer if these robust volume changes and corresponding electric field distributions are associated with any clinical or cognitive consequences.

## Materials and methods

### Participants

GEMRIC is a multi-site consortium focused on improving and individualizing ECT by researching the still elusive mechanisms of action and response-related biomarkers (Oltedal et al., 2017). Patients in the GEMRIC database participated in clinical and imaging assessments pre- and post-ECT series. To control for the differential effects of electrode placement on electric fields, we only included subjects who received high-dose (six times the seizure threshold) right unilateral electrode placement throughout the ECT series. We screened 281 patients from 10 sites (Oltedal et al., 2018), and data were included from 7 GEMRIC sites with the RUL only criteria (n = 151, 92 F, age: 57.5 ± 17.1, 12 with bipolar depression, 139 with major depression, demographic summary is in Table 2A and B). Depression severity was assessed with the Montgomery–Åsberg Depression Rating Scale (MADRS) (Montgomery and Asberg, 1979) or 17- or 24-item Hamilton Depression Rating Scale (HAM-D) (Hamilton, 1960). For sites collecting only the 17- or 24-item HAM-D, a validated equation was used to convert the 17-item HAM-D to a MADRS score (Heo et al., 2007). Clinical response was estimated as the percentage change of the MADRS scores (ΔMADRS = (MADRSTP1-MADRSTP2)/MADRSTP1). Although more conservative than absolute change or post-ECT depression outcomes (Vickers, 2001), the rationale for the use of the proportional change score was to control for the variability of the pre-ECT MADRS. The range of the number of sessions for the ECT series was between 7 and 20. Half of the subjects were medication free during the ECT series (n = 69). Concurrent pharmacotherapy for the remaining subjects was as follows: selective serotonin reuptake inhibitors (SSRI, n = 28), serotonin norepinephrine reuptake inhibitors (SNRI, n = 37), tricyclic antidepressants (TCA, n = 10), and no record of concurrent medications (n = 6). Only five subjects received medication changes during the ECT series (two medication free subjects started SSRI and TCA, one subject switched from SNRI to TCA, one from SNRI to TCA and one from SSRI to SNRI). The results did not change if we used medication status or diagnosis (bipolar or unipolar depression) as a nuisance variable in the linear models of this study. All sites’ contributing data (Table 2B) received approval by their local ethical committees or institutional review board, and the centralized mega-analysis was approved by the Regional Ethics Committee South-East in Norway (2013/1032 ECT and Neuroradiology, June 1, 2015).

**Table 2.**
 Clinical and demographics summary.


<table>
  <thead>
    <tr>
      <th colspan="8">Table 2A Overall Summary</th>
    </tr>
    <tr>
      <th>Site</th>
      <th>N</th>
      <th></th>
      <th>Age (sd)</th>
      <th>Medications (med. free, SSRI/SNRI, TCA, AP*)</th>
      <th>Average number of ECT</th>
      <th>Baseline MADRS</th>
      <th>Δ MADRS (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>All</td>
      <td>151</td>
      <td></td>
      <td>57.5 (17.1)</td>
      <td>69,65,10,62</td>
      <td>10.6</td>
      <td>33.9</td>
      <td>61.3</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>92</td>
      <td></td>
      <td>56.4 (18.4)</td>
      <td>42,36,8,42</td>
      <td>10.4</td>
      <td>34.4</td>
      <td>63.4</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>59</td>
      <td></td>
      <td>59.3 (14.7)</td>
      <td>27,29,2,20</td>
      <td>10.9</td>
      <td>33.3</td>
      <td>58.1</td>
    </tr>
    <tr>
      <td colspan="8">Table 2B Site Summary</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Site</td>
      <td>N</td>
      <td>Age (mean)</td>
      <td>Age (sd)</td>
      <td>Baseline MADRS</td>
      <td>Δ MADRS (%)</td>
    </tr>
    <tr>
      <td>1</td>
      <td>30</td>
      <td>39.87</td>
      <td>12.68</td>
      <td></td>
      <td></td>
      <td>40.73</td>
      <td>45.12</td>
    </tr>
    <tr>
      <td>2</td>
      <td>33</td>
      <td>64.48</td>
      <td>8.93</td>
      <td></td>
      <td></td>
      <td>31.36</td>
      <td>69.48</td>
    </tr>
    <tr>
      <td>3</td>
      <td>16</td>
      <td>73.62</td>
      <td>12.45</td>
      <td></td>
      <td></td>
      <td>29.56</td>
      <td>77.24</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>46.87</td>
      <td>9.19</td>
      <td></td>
      <td></td>
      <td>29.96</td>
      <td>43.18</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2</td>
      <td>62.50</td>
      <td>0.71</td>
      <td></td>
      <td></td>
      <td>36.75</td>
      <td>32.03</td>
    </tr>
    <tr>
      <td>6</td>
      <td>18</td>
      <td>48.50</td>
      <td>16.77</td>
      <td></td>
      <td></td>
      <td>33.83</td>
      <td>57.12</td>
    </tr>
    <tr>
      <td>7</td>
      <td>29</td>
      <td>72.66</td>
      <td>7.57</td>
      <td></td>
      <td></td>
      <td>35.07</td>
      <td>79.13</td>
    </tr>
  </tbody>
</table>

_*med. free: medication free, SSRI: selective serotonin reuptake inhibitor, SNRI: serotonin and norepinephrine reuptake inhibitors, TCA: tricyclic antidepressants, AP: antipsychotic medications, there were not patients on MAO inhibitors._

### Imaging

The image processing methods have been detailed previously (Oltedal et al., 2018; Oltedal et al., 2017). In brief, the sites provided longitudinal 3T T1-weighted MRI images (at baseline and after the end of the course of ECT) with a minimal resolution of 1.3 mm in any direction (detailed parameters in Supplementary file 6). The raw DICOM images were uploaded and analyzed on a common server at the University of Bergen, Norway. To guarantee reproducibility, in addition to the common platform, the processing pipelines were implemented in a docker environment (Merkel, 2014). First, images were corrected for scanner-specific gradient-nonlinearity (Jovicich et al., 2006). Further processing was performed with FreeSurfer version 5.3, which includes segmentation of subcortical structures (Fischl et al., 2002) and automated parcellation of the cortex (Desikan et al., 2006). In addition to brainstem and bilateral cerebellum, this automated process identified 33 cortical and eight subcortical regions in each hemisphere. Altogether this resulted in 85 regions of interest (ROIs) (Supplementary file 1). Next Quarc (Holland et al., 2011) was used for unbiased, within-subject assessment of estimation of longitudinal volume change (ΔVol - %) (Figure 5). In summary, we calculated bias-free estimation of volumetric change from 85 brain regions across the timespan of an ECT course in 151 individuals who received between 4 to 20 ECT sessions (1 ½ week to 2 month).

![Figure 5.](https://cdn.elifesciences.org/articles/49115/elife-49115-fig5-v2.jpg)

**Figure 5.:** We analyzed longitudinal structural MRI data from 151 individuals. We calculated the volume change and the magnitude of electrical field in 85 regions across the human cortex and subcortical structures.

### Electric Field modeling

We estimated ECT-induced electric fields with Realistic Volumetric-Approach to Stimulate Transcranial Electric Stimulation (ROAST v1.1) (Huang et al., 2017). After segmentation of the structural MRI T1-weighted images, ROAST builds a three-dimensional tetrahedral mesh model of the head. The segmentation identifies five tissue types: white and gray matter of the brain, cerebrospinal fluid, skull, and scalp, and assigns them different conductivity values: 0.126 S/m, 0.276 S/m, 1.65 S/m, 0.01 S/m, and 0.465 S/m respectively. ECT electrodes of 5 cm diameter were placed over the C2 and FT8 EEG (10–20 system) sites. Study sites from the GEMRIC database used either the Thymatron (Somatics, Venice, Florida, six sites, N = 121) or spECTrum (MECTA Corp., Tualatin, Oregon, one site, N = 30) devices. The electric field was solved using the finite-element method with unit current on the electrodes and, subsequently, it was scaled to the current amplitude of the specific devices (Thymatron 900 mA, spECTrum 800 mA). These procedures resulted in a voxel-wise electric field distribution map in each individual. We calculated the average electric field across the 85 three-dimensional ROIs in every individual (Figure 5) based on the Freesurfer parcellations and segmentations. The voxel values with the top and lowest one percentile in each ROI were omitted during calculations to reduce boundary effects.

### Statistical analysis

#### Laterality of electric field and volume change

Our statistical analysis was performed in R (R Development Core Team, 2013), and the underlying analyses can be found at https://github.com/argyelan/Publications/ (copy archived at https://github.com/elifesciences-publications/Publications-1) in org mode (Schulte et al., 2012). We first calculated the effect sizes (Cohen’s d) for longitudinal volume changes in each region. We assessed the correlations between the average electric fields and the effect sizes of volume changes across all the 85 regions. We further explored the hemispheric differences by calculating the pair-wise difference in volume changes across the corresponding ROIs (42 pairs). We defined the laterality index as the effect size of the pair-wise difference for both EF and ΔVol among homotopic ROIs. We then assessed the correlations between laterality indices of EF and ∆Vol across the 42 pairs of regions.

### Electric field and volume change

We assessed the relationship between EF and ∆ Vol with the following linear mixed effect model in all 85 regions: 1) ΔVol ~EF + Age + number of ECT sessions + site (where EF, age, and number of ECT sessions were fixed effects, and site was random effect, while the dependent variable was volume change). Age, number of ECT sessions, and site, considered as nuisance variables, were included based on our prior observations of an inverse relationship between ECT session number and response (Oltedal et al., 2018). Further, age is also shown to impact clinical response (older patients have increased probability of response, in our sample: t = 5.75, df = 149, r = 0.43, p<10−7) and age-related changes on brain structure are related to EF (Deng et al., 2015). We used Benjamini and Hochberg false discovery rate (FDR) correction method (Benjamini and Hochberg, 1995) to control for multiple comparisons across 85 ROIs, where a conservative FDR -corrected p<0.01 was chosen as the statistical threshold of significance.

### Electric field, volume change, and clinical response

We assessed the relationship between ∆MADRS and EF and ∆ Vol with the following linear mixed effect model in all 85 regions: 1) ΔMADRS ~ ΔVol + Age + number of ECT sessions + site; and 2) ΔMADRS ~EF + Age + number of ECT sessions + site (site as random effect). We used the same Benjamini and Hochberg FDR correction for multiple comparison corrections. In addition to analyzing the percentage change of the clinical response, we also evaluated the same models with absolute changes, using baseline MADRS as a covariate. We provided the results of these analyses in the second half of the corresponding Supplementary Files.
