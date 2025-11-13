# Topological network analysis of patient similarity for precision management of acute blood pressure in spinal cord injury

## Authors

- Abel Torres-Espín<sup>1</sup> ([ORCID: 0000-0002-9787-8738](https://orcid.org/0000-0002-9787-8738))
- Jenny Haefeli<sup>1</sup>
- Reza Ehsanian<sup>2</sup>
- Dolores Torres<sup>1</sup>
- Carlos A Almeida<sup>1</sup>
- J Russell Huie<sup>1</sup>
- Austin Chou<sup>1</sup>
- Dmitriy Morozov<sup>4</sup>
- Nicole Sanderson<sup>5</sup>
- Benjamin Dirlikov<sup>6</sup>
- Catherine G Suen<sup>1</sup>
- Jessica L Nielson<sup>7</sup>
- Nikos Kyritsis<sup>1</sup> ([ORCID: 0000-0001-7801-5796](https://orcid.org/0000-0001-7801-5796))
- Debra D Hemmerle<sup>1</sup> ([ORCID: 0000-0003-2796-6107](https://orcid.org/0000-0003-2796-6107))
- Jason F Talbott<sup>9</sup>
- Geoffrey T Manley<sup>1</sup>
- Sanjay S Dhall<sup>1</sup>
- William D Whetstone<sup>10</sup>
- Jacqueline C Bresnahan<sup>1</sup>
- Michael S Beattie<sup>1</sup>
- Stephen L McKenna<sup>11</sup>
- Jonathan Z Pan<sup>13</sup> ([ORCID: 0000-0001-5814-3707](https://orcid.org/0000-0001-5814-3707)) †
- Adam R Ferguson<sup>1</sup> ([ORCID: 0000-0001-7102-1608](https://orcid.org/0000-0001-7102-1608)) †
- MS Beattie

### Affiliations

1. Weill Institute for Neurosciences; Brain and Spinal Injury Center (BASIC), Department of Neurological Surgery, University of California, San Francisco; Zuckerberg San Francisco General Hospital and Trauma Center San Francisco United States
2. Division of Physical Medicine and Rehabilitation, Department of Orthopaedics and Rehabilitation, University of New Mexico School of Medicine Albuquerque United States
3. San Francisco Veterans Affairs Healthcare System San Francisco United States
4. Computational Research Division, Lawrence Berkeley National Laboratory Berkeley United States
5. Lawrence Berkeley National Laboratory Berkeley United States
6. Rehabilitation Research Center, Santa Clara Valley Medical Center San Jose United States
7. Department of Psychiatry and Behavioral Science, and University of Minnesota Minneapolis United States
8. Institute for Health Informatics, University of Minnesota Minneapolis United States
9. Department of Radiology and Biomedical Imaging, University of California, San Francisco San Francisco United States
10. Department of Emergency Medicine, University of California, San Francisco; Zuckerberg San Francisco General Hospital and Trauma Center San Francisco United States
11. Department of Physical Medicine and Rehabilitation, Santa Clara Valley Medical Center San Jose United States
12. Department of Neurosurgery, Stanford University Stanford United States
13. Department of Anesthesia and Perioperative Care, University of California, San Francisco; Zuckerberg San Francisco General Hospital and Trauma Center San Francisco United States

† Corresponding author

## Abstract

Background:Predicting neurological recovery after spinal cord injury (SCI) is challenging. Using topological data analysis, we have previously shown that mean arterial pressure (MAP) during SCI surgery predicts long-term functional recovery in rodent models, motivating the present multicenter study in patients.Methods:Intra-operative monitoring records and neurological outcome data were extracted (n = 118 patients). We built a similarity network of patients from a low-dimensional space embedded using a non-linear algorithm, Isomap, and ensured topological extraction using persistent homology metrics. Confirmatory analysis was conducted through regression methods.Results:Network analysis suggested that time outside of an optimum MAP range (hypotension or hypertension) during surgery was associated with lower likelihood of neurological recovery at hospital discharge. Logistic and LASSO (least absolute shrinkage and selection operator) regression confirmed these findings, revealing an optimal MAP range of 76–[104-117] mmHg associated with neurological recovery.Conclusions:We show that deviation from this optimal MAP range during SCI surgery predicts lower probability of neurological recovery and suggest new targets for therapeutic intervention.Funding:NIH/NINDS: R01NS088475 (ARF); R01NS122888 (ARF); UH3NS106899 (ARF); Department of Veterans Affairs: 1I01RX002245 (ARF), I01RX002787 (ARF); Wings for Life Foundation (ATE, ARF); Craig H. Neilsen Foundation (ARF); and DOD: SC150198 (MSB); SC190233 (MSB); DOE: DE-AC02-05CH11231 (DM).

## Introduction

Spinal cord injury (SCI) may result in motor, sensory, and autonomic dysfunction in various degrees, depending on the injury severity and location. In the USA, the incidence of SCI is around 18,000 new cases per year, with a total prevalence ranging from 250,000 to 368,000 cases (National Spinal Cor Injury Statistical Center, 2021). The dramatic life event of SCI imposes a high socioeconomic burden, with an estimated lifetime cost between $1.2 and $5.1 million per patient (National Spinal Cor Injury Statistical Center, 2021).

Prior retrospective observational single-center studies in humans suggest that lower post-surgery mean arterial pressure (MAP) predicts poor outcome (Cohn et al., 2010; Hawryluk et al., 2015; Saadeh et al., 2017; Ehsanian, 2020), which have resulted in clinical guidelines focused on avoidance of hypotension by maintaining MAP >85 mmHg during the first 7 days of injury (Aarabi et al., 2013). The rational for MAP augmentation to avoid hypotension is based on the hypothesis that decreased spinal cord prefusion leads to ischemia and additional tissue lost (Mautes et al., 2000; Soubeyrand et al., 2014). Importantly, experimentally raising MAP during acute SCI in animals by using vasopressors increases the risk for hemorrhage and consequent tissue damage (Soubeyrand et al., 2014; Streijger et al., 2018; Guha et al., 1987). In acute cervical patients with SCI, spinal cord hemorrhage correlates with poor prognosis for neurological recovery (Miyanji et al., 2007). These findings collectively suggest that hypo- and hypertension must be accounted for in MAP management, but there remains a gap in evidence from clinical studies that definitively informs MAP guidelines (Saadeh et al., 2017).

One of the challenges resulting in the lack of strong evidence for MAP management in patients with acute SCI is the heterogeneity of injury. The heterogeneity of SCIs results in data complexity that benefit from modern analytic tools. Using the machine intelligence approach of topological data analysis, we have previously shown that hypertension during SCI surgery (ultra-acute phase) predicts long-term functional recovery in rodent models (Nielson et al., 2015). These prior cross-species findings motivated the present multicenter study where we apply a data-driven workflow in patients with ultra-acute SCI surgical records from two different Level 1 trauma centers. By employing machine intelligence tools, we show that deviation from an optimal MAP range during surgery predicts lower likelihood of neurological recovery and suggest new targets for therapeutic intervention.

## Methods

### Retrospective data extraction and cohort selection

Operating room (OR) records from n = 94 patients (98 surgical records, 3 patients with multiple surgeries) from the Zuckerberg San Francisco General Hospital (ZSFG, from 2005 to 2013) and n = 33 patients (33 surgical records) from the Santa Clara Valley Medical Center (SCVMC, from 2013 to 2015) that underwent spinal surgery were collected retrospectively. For ZSFG, monitoring data was extracted from the values manually recorded by the anesthesiologist at 5 min intervals (Q5). For SCVMC, monitoring data was extracted from the Surgical Information Systems (SIS) (Alpharetta, GA) at 1 min intervals (Q1). Demographics and outcome variables were extracted from an existing retrospective registry. AIS (American Spinal Injury Association [ASIA] Impairment Scale) grade at admission (first complete AIS upon admission to the hospital before surgery) and discharge (latest complete AIS grade after surgery before discharge from hospital) were estimated using the available ISNCSCI exams (International Standards for Neurological Classification of SCI) and the neurosurgery, trauma surgery, emergency department, and physical medicine and rehabilitation physical exam notes. To ensure compatibility between centers on the estimated AIS grades, one independent physician conducted the estimates for all the patients in each center (SM for SCVMC and JT for ZSFG) and one independent ISNCSCI certified physician (WW) extracted the AIS grades for all the patients (across centers). In case of conflict between grades, both physicians established a consensus. From the total 131 surgical records, three records were excluded for not having monitoring recorded for both MAP and HR, three were excluded because surgeries were not related to SCI, and seven surgeries were excluded from three patients that were submitted to more than one surgery. The final cohort for exploratory topological data analysis included 118 patients with complete MAP and heart rate (HR) monitoring. For confirmatory regression analysis, 15 patients were excluded because AIS grade could not be extracted either at admission and/or discharge (Figure 2—figure supplement 1). AIS improvement was defined as an increase of at least one AIS grade from admission to discharge. The final list of extracted variables included: MAP and HR continuous monitoring, age, length of surgery in minutes, days from surgery to hospital discharge, estimated AIS grade at admission, estimated AIS grade at discharge and AIS improvement (‘yes’, ‘no’). All data was de-identified before pre-processing and analysis. Protocols for retrospective data extraction were approved by Institutional Research Board (IRB).

### Cohort statistics

The differences in the AIS improvers/non-improvers population characteristics were tested at the univariate level using R (see software below). For continuous numerical variables (age, length of surgery, and days from surgery to discharge), the group mean differences were tested using unpaired Student’s t-test (two-sided test). For categorical variables (AIS admission, AIS at discharge, and dichotomized neurological level of injury [NLI]), their levels were compared using Fisher’s exact test (two-sided test). p-Values are presented in Table 1.

**Table 1.**
 Cohort demographics split by AIS (American Spinal Injury Association [ASIA] Impairment Scale) improvement.


<table>
  <thead>
    <tr>
      <th></th>
      <th>AIS improve. N/A(n = 15)</th>
      <th>AIS improve. NO(n = 61)</th>
      <th>AIS improve. YES(n = 42)</th>
      <th>Univariate p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age (years)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>46.0 (17.6)</td>
      <td>45.3 (19.1)</td>
      <td>51.4 (19.7)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median [min, max]</td>
      <td>45.5 [19.0, 87.0]</td>
      <td>47.0 [18.0, 82.0]</td>
      <td>55.0 [18.0, 86.0]</td>
      <td></td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>1 (6.7%)</td>
      <td>2 (3.3%)</td>
      <td>1 (2.4%)</td>
      <td></td>
    </tr>
    <tr>
      <td>AIS admission</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>A</td>
      <td>1 (6.7%)</td>
      <td>33 (54.1%)</td>
      <td>18 (42.9%)</td>
      <td></td>
    </tr>
    <tr>
      <td>B</td>
      <td>0 (0%)</td>
      <td>5 (8.2%)</td>
      <td>8 (19.0%)</td>
      <td></td>
    </tr>
    <tr>
      <td>C</td>
      <td>0 (0%)</td>
      <td>5 (8.2%)</td>
      <td>11 (26.2%)</td>
      <td></td>
    </tr>
    <tr>
      <td>D</td>
      <td>0 (0%)</td>
      <td>14 (23.0%)</td>
      <td>5 (11.9%)</td>
      <td></td>
    </tr>
    <tr>
      <td>E</td>
      <td>0 (0%)</td>
      <td>4 (6.6%)</td>
      <td>0 (0%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>14 (93.3%)</td>
      <td>0 (0%)</td>
      <td>0 (0%)</td>
      <td></td>
    </tr>
    <tr>
      <td>AIS discharge</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>A</td>
      <td>0 (0%)</td>
      <td>35 (57.4%)</td>
      <td>0 (0%)</td>
      <td></td>
    </tr>
    <tr>
      <td>B</td>
      <td>0 (0%)</td>
      <td>5 (8.2%)</td>
      <td>5 (11.9%)</td>
      <td></td>
    </tr>
    <tr>
      <td>C</td>
      <td>1 (6.7%)</td>
      <td>4 (6.6%)</td>
      <td>15 (35.7%)</td>
      <td></td>
    </tr>
    <tr>
      <td>D</td>
      <td>0 (0%)</td>
      <td>14 (23.0%)</td>
      <td>17 (40.5%)</td>
      <td></td>
    </tr>
    <tr>
      <td>E</td>
      <td>1 (6.7%)</td>
      <td>2 (3.3%)</td>
      <td>5 (11.9%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>13 (86.7%)</td>
      <td>1 (1.6%)</td>
      <td>0 (0%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Surgery duration (min)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.66</td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>433 (167)</td>
      <td>392 (146)</td>
      <td>407 (181)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median [min, max]</td>
      <td>432 [121, 725]</td>
      <td>389 [120, 728]</td>
      <td>343 [151, 950]</td>
      <td></td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>1 (6.7%)</td>
      <td>2 (3.3%)</td>
      <td>1 (2.4%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Surgery to discharge (days)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.33</td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>9.50 (2.12)</td>
      <td>18.8 (20.6)</td>
      <td>23.4 (23.8)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median [min, max]</td>
      <td>9.50 [8.00, 11.0]</td>
      <td>11.0 [1.00, 128]</td>
      <td>14.5 [4.00, 120]</td>
      <td></td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>13 (86.7%)</td>
      <td>4 (6.6%)</td>
      <td>2 (4.8%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Dichotomized neurological level of injury at admission</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.054</td>
    </tr>
    <tr>
      <td>Cervical</td>
      <td>2.00 (13.3%)</td>
      <td>36 (59%)</td>
      <td>33 (78.6%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Non-cervical</td>
      <td>13.00 (86.7%)</td>
      <td>25 (41%)</td>
      <td>9 (21.4%)</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Topological network extraction and exploration of monitoring data workflow

#### Monitoring data pre-processing

Two datasets were generated, one for each center. To ensure compatibility, both datasets were harmonized. Given the difference in the sampling frequency of the monitoring data (Q5 for ZSFG and Q1 SCVMC) between centers and protocols for data collection, SCVMC monitoring data was first pre-processed. Briefly, electronic data was exported from the SIS SQL database, de-identified and imported into MATLAB version 2016b (Mathworks Inc, Natick, MA) for filtering. A custom MATLAB script generated by the SCVMC team implemented filtering criteria established by clinicians and researchers to correct for invalid data (e.g., motion artifacts and injections). Thus, MAP values under 10 and above 200 mmHg as well as point-to-point changes greater than 40 mmHg were filtered, as these instances were found to represent data artifacts. This process was validated by comparing clinical curated data and the extracted data from the script with an accuracy of 99.1%. After filtering, SCVMC Q1 monitoring data was downsampled to Q5 by taking the average of five consecutive Q1 intervals for compatibility with ZSFG data. Given that the duration of the monitoring for each patient was different and the continuous time-series data is not aligned between patients (without time dependency on monitoring values), the empirical cumulative distribution function (CDF) for each time-series and each patient was computed. To account for the different scales between MAP and HR, a bin width for CDF was set as a 1% of the range of each measure, producing 100 CDF bins for MAP and 100 bins for HR (Figure 2—figure supplement 2). Additionally, the average MAP (aMAP) and HR (aHR) across time for each patient was calculated for posterior analysis.

#### Similarity between patients

The CDF bins for both MAP and HR were serialized in one vector per patient and the Euclidean distance ($d(p,q)=\sqrt{\sumi=1n(p_{i}−q_{i})^{2}}$, where p and q are two patients’ CDF vectors and n is the number of CDF bins) calculated for each pair of patients’ vectors. The Euclidean distance matrix was then processed using dimensionality reduction.

#### Dimensionality reduction

Our goal for dimensionality reduction was to increase the signal-to-noise ratio by mapping to a lower number of dimensions (d) that contained the major information in the dataset. Dimensionality reduction was achieved by using the Isomap algorithm (Tenenbaum et al., 2000). Isomap is a non-linear dimensionality reduction method that uses multidimensional scaling (MDS) with geodesic distances instead of the Euclidean distances as the classic MDS does, and it has been suggested before for health data (Weng et al., 2005). Isomap performs three steps: (1) construct an NNG (near neighbor graph), (2) estimate the geodesic distances from the graph (shortest paths), (3) compute MDS embedding with the geodesic distances. The algorithm takes one parameter (k or e) to set the threshold for the NNG (we used k, the number of near neighbors for NNG). For selecting k, we considered the minimal k the smallest one that produced a connected NNG, in our case k = 3. Then two criteria were established for both k optimization and d selection, distance preservation (RV, residual variance) and topological persistent homology preservation as described (Rieck and Leitte, 2015; Paul and Chalup, 2017). We considered Isomap solutions for k = 3–7 (Figure 2—figure supplement 1). The RV was computed as (Tenenbaum et al., 2000): $1−R^{2}(D_{m}^,D_{y})$ where $R$ is the standard linear correlation coefficient taken over all entries of $D^_{m}$ and $D_{y}$. $D^_{m}$ is the input distance matrix that the algorithm is trying to estimate the real dimensions of (k-geodesic distance matrix for k-Isomap). $D_{y}$ is the Euclidean distance matrix of the low-dimensional solution. No major differences were observed in RV between the solutions for different k, except for the first dimension where RV increases as k increases. Isomap persistence diagrams were obtained using Vietoris-Rips filtration (Paul and Chalup, 2017) for $D^_{m}$ and $D_{y}$ for different d solutions (Figure 2—figure supplement 1). Then the topological zero-dimensional and one-dimensional Wasserstein (power = 2) distances (WD0 and WD1, respectively) were computed between $D^_{m}$ and $D_{y}$. In persistent homology, dimension 0 measures zero-dimensional holes in the data (the connectivity of the datapoints, i.e., the number of connected sets) and topological dimension 1 measures one-dimensional holes, namely loops. We sought to select the solution (determine d and k) that minimized the WD0 and WD1, indicative of the optimal solution preserving the major topological information (Rieck and Leitte, 2015; Paul and Chalup, 2017). Given that k = 6 and k = 7 showed the lowest WD0 and WD1, we considered k = 6 as the final solution (Figure 2—figure supplement 1). A d = 4 (four dimensions kept in the k = 6 Isomap) was chosen for being the one at the ‘elbow’ of the RV, the one that minimized WD0 in k = 6 Isomap and presented a good compromised WD1.

#### Network analysis

A network from the k = 6 d = 4 Isomap solution was created for visual representation of the connectivity of patients (similarity) in the low-dimensional space. In this network, nodes represent each patient and edges the connection of two patients that are similar in the Isomap solution. An adjacency (whether two nodes are connected) matrix was obtained by computing a k-NNG for the low-dimensional space. The cutoff threshold for adjacency was set to the minimal k that produced a full-connected network. For network clustering, the walktrap algorithm was used (Pons and Latapy, 2005) as implemented in the igraph R package. Walktrap takes a single parameter, the number of random steps the algorithm uses to determine if nodes are in the same cluster or not. To select the optimal number of steps we computed walktrap solutions of a set of random steps (1–100) and chosen the first solution which maximized modularity (Q) as implemented in igraph R package (Clauset et al., 2004). In network analysis, modularity can be interpreted as the proportion of within cluster compared to the between clusters connectivity (edges). This solution was 47 random steps, producing a dendrogram tree of connectivity which maximal modularity cut the tree in 11 clusters (Figure 2—figure supplement 1). Then the network was contracted for visual representation of a cluster network of patients, where nodes represented the clusters and edges connected clusters that had at least one edge in the similarity network. Both the similarity and the cluster networks were used for exploratory network analysis and hypothesis generation by mapping patient features and visual inspection (Figure 2—figure supplement 1). We used the assortativity coefficient (Ar) to explore the possibility that the network was capturing the association between patients and the time of MAP out of a range (Figure 4; see time MAP out of range). The Ar was calculated using the igraph implementation in R (Newman, 2003) and it can be interpreted as the Pearson coefficient (−1–1) between nodes connectivity and value of a variable.

### Regression analysis

#### Logistic regression

We first used a logistic regression to model the probability of predicting improvement by aMAP. Visual inspection of the plot (Figure 2) suggested a non-linear relationship between aMAP and the probability of improvement. Consequently, the following logistic models were considered ($l$ being the log-odds or logit of the probability of improving): the null model with no predictors ($l=\beta_{0}$, the simple model ($l=\beta_{0}+\beta_{1}x$), the two-grade polynomial model ($l=\beta_{0}+\beta_{1}x+\beta_{2}x^{2}$), the three-grade polynomial model ($l=\beta_{0}+\beta_{1}x+\beta_{2}x^{2}+\beta_{3}x^{3}$) and a natural spline model ($l=\beta_{0}+f_{1}(x)$ )where $f_{1}x$ is the natural spline function with 2 or 3 degrees of freedom (df)). The natural cubic spline was chosen to relax the symmetric constraints of polynomial models given that the visual inspection of the data suggested an asymmetric aMAP range (Figure 2, distribution of aMAP of improvers is skewed to the left). The results of fitting these models and the likelihood comparison between them (by likelihood ratio test) are shown in Table 2. The best fitting model was the two-grade polynomial (Figure 3) and the natural spline (2df) with significant coefficients, confirming our hypothesis. These results were confirmed by leave-one-out cross-validation (LOOCV) (Table 2). To account for the potential confounding effect of AIS grade at admission (given differences between groups, Table 1), aHR, length of surgery (minutes), days from surgery to discharge and age, we fitted the quadratic model with those covariates and LOOCV (Table 3). Considering the independence of the predictors (small correlation coefficients between variables; Table 4), the results of the quadratic term being significant still holds for the covariate model.

**Table 2.**
 Logistic regression likelihood ratio test and leave-one-out cross-validation (LOOCV) error (n = 103 patients).


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>AIC</th>
      <th>Residual df</th>
      <th>Residualdeviance</th>
      <th>Deviance</th>
      <th>p-Value</th>
      <th>LOOCV error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Null model(l=β0)</td>
      <td>141.26</td>
      <td>102</td>
      <td>139.26</td>
      <td></td>
      <td></td>
      <td>0.246</td>
    </tr>
    <tr>
      <td>Linear model(l=β0+β1x)</td>
      <td>134.8</td>
      <td>101</td>
      <td>130.80</td>
      <td>8.46(vs. null model)</td>
      <td>0.0036**(vs. null model)</td>
      <td>0.231</td>
    </tr>
    <tr>
      <td>Quadratic model(l=β0+β1x+β2x2)</td>
      <td>128.48</td>
      <td>100</td>
      <td>122.48</td>
      <td>8.32(vs. linear model)</td>
      <td>0.0039**(vs. linear model)</td>
      <td>0.210</td>
    </tr>
    <tr>
      <td>Cubic model(l=β0+β1x+β2x2+β3x3)</td>
      <td>126.97</td>
      <td>99</td>
      <td>118.97</td>
      <td>3.50(vs. quadratic model)</td>
      <td>0.061(vs. quadratic model)</td>
      <td>0.213</td>
    </tr>
    <tr>
      <td>Natural Spline model (df = 2)(l=β0+f1(x))</td>
      <td>128.29</td>
      <td>100</td>
      <td>122.29</td>
      <td>8.50(vs. linear model)</td>
      <td>0.0035**(vs. linear model)</td>
      <td>0.210</td>
    </tr>
    <tr>
      <td>Natural Spline model (df = 3)(l=β0+f1(x))</td>
      <td>127.13</td>
      <td>99</td>
      <td>119.13</td>
      <td>3.34(vs. quadratic model)</td>
      <td>0.067(vs. quadratic model)</td>
      <td>0.213</td>
    </tr>
  </tbody>
</table>

_** p < 0.01._

**Table 3.**
 Evaluation of logistic regression (Wald test) and leave-one-out cross-validation (LOOCV) error.


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β1x1+β2x12 where x1: average MAP (n = 103 patients)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.66; average kappa statistic = 0.334</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= –0.55</td>
      <td>0.242</td>
      <td>–2.293</td>
      <td>0.02183*</td>
    </tr>
    <tr>
      <td>Average MAP (x1)</td>
      <td>β1= 8.62</td>
      <td>2.944</td>
      <td>2.931</td>
      <td>0.00338**</td>
    </tr>
    <tr>
      <td>Average MAP (x12)</td>
      <td>β2= –7.601</td>
      <td>3.039</td>
      <td>–2.501</td>
      <td>0.0123*</td>
    </tr>
  </tbody>
</table>

_*p < 0.05; **p < 0.01._

**Table 4.**
 Evaluation of logistic regression with covariates (Wald test) and leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="10">Model: l=β0+β11x1+β12x12+β2x2+β3x3+β4x4+β5x5+β6x6+β7x7+β8x8+β9x9, where x1: average MAP; x2 : average HR; x3: length of surgery (min); x4: days to AIS discharge (days); x5: age; x6: AIS admission D (‘yes’,’no’); x7: AIS admission C (‘yes’,’no’); x8: AIS admission B (‘yes’,’no’); x9: AIS admission A (‘yes’,’no’); (AIS admission E was set as the reference level for AIS admission variable and is part of the intercept) (final n = 93)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="10">LOOCV: average observed accuracy = 0.688; average kappa statistic = 0.362</td>
    </tr>
    <tr>
      <td colspan="2">Predictor</td>
      <td colspan="2">Coef. estimate (logit)</td>
      <td colspan="2">Std. error</td>
      <td colspan="2">z-Value</td>
      <td colspan="2">p-Value</td>
    </tr>
    <tr>
      <td colspan="2">Intercept</td>
      <td colspan="2">β0= –1.530</td>
      <td colspan="2">121.8</td>
      <td colspan="2">–0.013</td>
      <td colspan="2">0.99</td>
    </tr>
    <tr>
      <td colspan="2">Average MAP (x1)</td>
      <td colspan="2">β11= 7.398</td>
      <td colspan="2">3.112</td>
      <td colspan="2">2.377</td>
      <td colspan="2">0.017*</td>
    </tr>
    <tr>
      <td colspan="2">Average MAP (x12)</td>
      <td colspan="2">β12= –8.053</td>
      <td colspan="2">3.530</td>
      <td colspan="2">–2.281</td>
      <td colspan="2">0.022*</td>
    </tr>
    <tr>
      <td colspan="2">Average HR (x2)</td>
      <td colspan="2">β2= –2.087</td>
      <td colspan="2">0.0245</td>
      <td colspan="2">–0.851</td>
      <td colspan="2">0.394</td>
    </tr>
    <tr>
      <td colspan="2">Length of surgery (x3)</td>
      <td colspan="2">β3= 0.0011</td>
      <td colspan="2">0.0015</td>
      <td colspan="2">0.728</td>
      <td colspan="2">0.466</td>
    </tr>
    <tr>
      <td colspan="2">Days to AIS discharge (x4)</td>
      <td colspan="2">β4= 0.0037</td>
      <td colspan="2">0.0109</td>
      <td colspan="2">0.344</td>
      <td colspan="2">0.730</td>
    </tr>
    <tr>
      <td colspan="2">Age (x5)</td>
      <td colspan="2">β5= 0.0082</td>
      <td colspan="2">0.013</td>
      <td colspan="2">0.634</td>
      <td colspan="2">0.526</td>
    </tr>
    <tr>
      <td colspan="2">AIS admission D (x6)</td>
      <td colspan="2">β6= 1.454</td>
      <td colspan="2">1.218</td>
      <td colspan="2">0.012</td>
      <td colspan="2">0.990</td>
    </tr>
    <tr>
      <td colspan="2">AIS admission C (x7)</td>
      <td colspan="2">β7= 1.645</td>
      <td colspan="2">1.218</td>
      <td colspan="2">0.014</td>
      <td colspan="2">0.989</td>
    </tr>
    <tr>
      <td colspan="2">AIS admission B (x8)</td>
      <td colspan="2">β8= 1.585</td>
      <td colspan="2">1.218</td>
      <td colspan="2">0.013</td>
      <td colspan="2">0.989</td>
    </tr>
    <tr>
      <td colspan="2">AIS admission A (x9)</td>
      <td colspan="2">β9= 1.527</td>
      <td colspan="2">1.218</td>
      <td colspan="2">0.013</td>
      <td colspan="2">0.990</td>
    </tr>
    <tr>
      <td colspan="10">Correlation matrix (Spearman)</td>
    </tr>
    <tr>
      <td></td>
      <td>Average MAP</td>
      <td>AverageHR</td>
      <td colspan="2">Length of surgery</td>
      <td colspan="2">Days to AIS discharge</td>
      <td colspan="2">Age</td>
      <td>AIS admission</td>
    </tr>
    <tr>
      <td>Average MAP</td>
      <td>1</td>
      <td></td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td></td>
    </tr>
    <tr>
      <td>Average HR</td>
      <td>–0.126</td>
      <td>1</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td></td>
    </tr>
    <tr>
      <td>Length of surgery</td>
      <td>–0.152</td>
      <td>0.101</td>
      <td colspan="2">1</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td></td>
    </tr>
    <tr>
      <td>Days to AIS discharge</td>
      <td>0.088</td>
      <td>–0.059</td>
      <td colspan="2">0.165</td>
      <td colspan="2">1</td>
      <td colspan="2"></td>
      <td></td>
    </tr>
    <tr>
      <td>Age</td>
      <td>0.006</td>
      <td>–0.245</td>
      <td colspan="2">0.011</td>
      <td colspan="2">0.022</td>
      <td colspan="2">1</td>
      <td></td>
    </tr>
    <tr>
      <td>AIS admission</td>
      <td>0.024</td>
      <td>0.003</td>
      <td colspan="2">–0.01</td>
      <td colspan="2">0.258</td>
      <td colspan="2">–0.13</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
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

_*p < 0.05._

### Time out of MAP range

We sought to determine a range of MAP in which time outside that range might predict improvement. To consider the time at which MAP was outside a range, we performed an increasing window of MAP for either a symmetric range or an asymmetric one. For the symmetric range, a 1 mmHg range increment at each site of the center (90 mmHg, the mean MAP for improvers) was created. For the asymmetric range, the lower limit was fixed at 76 mmHg and the upper limit was incremented 1 mmHg at the time. The time of MAP (in min) being outside each range was estimated for each patient.

#### LASSO regression

LASSO (least absolute shrinkage and selection operator) regression (Tibshirani, 1996) was used for selecting a single range of MAP (see time MAP out of range) predictor of the logistic model: $l=\beta_{0}+\sum_{j=1}^{p}\beta_{j}x_{j}$, where $x_{j}$ is the jth MAP range. LASSO takes as parameter lambda that sets the amount of shrinkage or regularization (using L1-norm penalty). LOOCV was used to determine the lambda that shrunk the models to one predictor or MAP range. The one-predictor solutions (MAP range of 76–104 for symmetric range model, and 76–117 for the asymmetric range model) were used as the solo predictor of AIS improvers in a logistic regression with LOOCV (see above). It is important to note that given the high multicollinearity in the range data, the Q5 time estimation and the low sample size, the LASSO solution should be taken with caution and as an indicator of the MAP range hypothesis rather than a hard rule for medical decision making.

### Prediction modeling

Logistic regression (see above) was used to build prediction models for three binary outcome metrics: AIS improvement of at least one grade from admission to discharge, whether patient was AIS grade A at discharge, or whether the patient was AIS grade D at discharge. For each one of the classification tasks, the following predictors were considered: quadratic aMAP (both linear and quadratic terms), aHR, length of surgery (min), days from surgery to discharge, age, AIS grade at admission, and dichotomized NLI. We performed model selection (a.k.a. feature selection) through an exhaustive search of all potential combinations of at least one of the predictors using the glmulti R package (Calcagno, 2020). The most parsimonious models were selected to be the one minimizing the small-sample corrected Akaike information criteria (AIC) for each task. We then investigated the performance of each one of the most parsimonious models using LOOCV and adjusting the classification threshold to balance prediction sensitivity and specificity. Briefly, each model was trained n (patient) times with an n−1 training sample and tested the performance in the remaining sample. A vector of n probabilities of predictions was then used to measure the LOOCV model performance. Model fitting and prediction performance were conducted using the caret R package (Kuhn et al., 2019). Receiving operating curves (ROC) and area under the curve (AUC) for the LOOCV prediction were obtained using the ROCR R package (Sing et al., 2005).

### Software

All data wrangling, processing, visualization, and analysis was performed using the R programming language (R version 3.5.1) (R core team, 2019) and RStudio (RStudio version 1.2.1335) (Team, 2018) in Windows 10 operating system, with the exception of the Q1 OR measures form SCVMC that were preprocessed in MATLAB before downsampling to Q5 in R. The most relevant R functions and packages (beyond the installed with R) used and the references for each function/package and methods are reported in the following table. For more details, see the source code available (Supplementary file 1 and Source code 1).

### R packages used

<table>
  <thead>
    <tr>
      <th>Package</th>
      <th>Version</th>
      <th>Usage</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>igraph</td>
      <td>1.2.4.1</td>
      <td>Building, manage and analyze networks</td>
      <td>Csárdi and Nepusz, 2006</td>
    </tr>
    <tr>
      <td>dplyr</td>
      <td>0.8.3</td>
      <td>Data cleaning and wrangling</td>
      <td>Wickham et al., 2018</td>
    </tr>
    <tr>
      <td>ggplot2</td>
      <td>3.2.1</td>
      <td>Data visualization and plotting</td>
      <td>Wickham, 2016</td>
    </tr>
    <tr>
      <td>vegan</td>
      <td>2.5–5</td>
      <td>For Isomap implementation</td>
      <td>Jari et al., 2019</td>
    </tr>
    <tr>
      <td>RColorBrewer</td>
      <td>1.1–2</td>
      <td>To control and create colormaps</td>
      <td>Neuwirth, 2014</td>
    </tr>
    <tr>
      <td>TDAstats</td>
      <td>0.4.0</td>
      <td>Utilities for topology data analysis for persistent homology</td>
      <td>Wadhwa et al., 2018</td>
    </tr>
    <tr>
      <td>cccd</td>
      <td>1.5</td>
      <td>For generating NNGs</td>
      <td>Marchette, 2015</td>
    </tr>
    <tr>
      <td>table1</td>
      <td>1.1</td>
      <td>Generates table of demographics</td>
      <td>Rich, 2018</td>
    </tr>
    <tr>
      <td>glmnet</td>
      <td>2.0–18</td>
      <td>For fitting LASSO</td>
      <td>Friedman et al., 2010</td>
    </tr>
    <tr>
      <td>glmnetUtils</td>
      <td>1.1.2</td>
      <td>For fitting LASSO</td>
      <td>Ooi, 2019</td>
    </tr>
    <tr>
      <td>caret</td>
      <td>6.0–84</td>
      <td>To fit logistic regression with leave-one-out cross-validation</td>
      <td>Kuhn et al., 2019</td>
    </tr>
    <tr>
      <td>splines</td>
      <td>3.5.1</td>
      <td>To fit the spline models</td>
      <td>R core team, 2019</td>
    </tr>
    <tr>
      <td>VisNetwork</td>
      <td>2.0.7</td>
      <td>Visualization suit for network graphs using the vis.js JavaScript library</td>
      <td>Almende, 2019</td>
    </tr>
    <tr>
      <td>stats</td>
      <td>3.5.1</td>
      <td>Fit generalized linear models</td>
      <td>R core team, 2019</td>
    </tr>
    <tr>
      <td>glmulti</td>
      <td>1.0.8</td>
      <td>For model search</td>
      <td>Calcagno, 2020</td>
    </tr>
    <tr>
      <td>ROCR</td>
      <td>1.0–11</td>
      <td>For ROC visualization and performance</td>
      <td>Sing et al., 2005</td>
    </tr>
    <tr>
      <td>reshape2</td>
      <td>1.4.3</td>
      <td>From wide to long view dataframe formatting</td>
      <td>Wickham, 2007</td>
    </tr>
  </tbody>
</table>

### Data and code availability

The final de-identified datasets for analysis are deposited and accessible at the Open Data Commons for SCI (odc-sci.org, RRID:SCR_016673) under DOIs 10.34945/F5R59J and 10.34945/F5MG68. The R code to run all the analysis present in this publication, including visualizations, is available as supplementary material. The code would reproduce the entire analysis and plots when run using the same versions of R, RStudio, and packages specified in this publication. Otherwise results might change.

## Results

### Exploratory network analysis suggests an upper and lower limit of intra-operative MAP for recovery

Intra-operative monitoring records (MAP, HR) and neurological outcome data were extracted and curated from two Level 1 trauma centers. A final cohort of 118 patients was included (Figure 1a and Table 1). The cohort represents a varied dataset of intra-operative MAP and HR patterns and respective aMAP across time in surgery and aHR across time in surgery values (Figure 1b–c). Using a machine intelligence analytical pipeline (Figure 2a), we extracted a similarity network of patients (Pai and Bader, 2018; Parimbelli et al., 2018) from a low-dimensional space embedded using a non-linear algorithm, Isomap (Tenenbaum et al., 2000), on a distance matrix derived from the MAP and HR records and then performed topological network extraction using persistent homology metrics (Rieck and Leitte, 2015; Figure 2a and Figure 2—figure supplement 1). The results of this dimensionality reduction suggested that four dimensions are enough to capture most of the variance and the topological structures of the original data (Figure 2—figure supplement 1c-e). Clustering the network of patients through a random-walk algorithm, Walktrap (Pons and Latapy, 2005), revealed 11 different clusters where patients were regarded to share intra-operative hemodynamic phenotypes (Figure 2 andFigure 2—figure supplement 1f-h). Importantly, this workflow was unsupervised: only the OR hemodynamic time-series was used to derive patient clustering, and therefore any association captured by the network must be dependent on hemodynamic patterns. Exploratory network analysis showed a gradient distribution of patients by their aMAP (Figure 2b–d) and aHR (Figure 2e–g), confirming that the network captured a valid representation of the raw high-dimensional dataset. We then investigated the association of the clusters to patient recovery as defined by whether the patient improved at least one AIS grade A–D (Roberts et al., 2017) between time before surgery and time of discharge from the hospital. Mapping the proportion of patients with AIS improvement onto the similarity network (Figure 2h–j) revealed that patients with recovery localized to clusters associated with a middle range of MAP (Figure 2k). Those clusters also showed a higher proportion of less severe AIS grades at discharge (AIS C, D, and E) than other clusters (Figure 2—figure supplement 2). In contrast, clusters of patients showing an extreme variation of MAP were highly enriched with patients with no AIS recovery and patients with more severe AIS grades at discharge (AIS A and B, Figure 2—figure supplement 2). This analysis suggested that there is a limited range of MAP during surgery associated with neurological recovery.

![Figure 1.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig1-v4.jpg)

**Figure 1.:** Flowchart of retrospective study and cohort selection criteria (a). A final cohort of 118 patients were identified and values of mean arterial pressure (MAP) (b) and heart rate (HR), (c) by time (bins of 5 min; Q5) retrospectively extracted from patients’ records. Colormaps represent the MAP (mmHg; green marks normotensive MAP, while blue and red marks hypotension and hypertension, respectively) and HR (beats per min, bpm; dark yellow lowest to purple highest) at each Q5 time, depicting the temporal fluctuation of each measure for each patient (row). The average MAP (aMAP, right plot in b) and average heart rate (aHR, right plot in c) were computed.

![Figure 2.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig2-v4.jpg)

**Figure 2.:** Intra-operative mean arterial pressure (MAP) and heart rate (HR) sampled every 5 min (Q5) were curated, processed, and formatted in a unique data matrix (a) (Figure 2—figure supplement 1). The similarity matrix between patients was computed and a four-dimensional subspace extracted using Isomap (Figure 2—figure supplement 1). A network was constructed where nodes represent patients and edges the connection of pairs of patients under a specified threshold of similarity (see Methods). The network was clustered and collapsed (Figure 2—figure supplement 1) by using the walktrap algorithm conveying in 11 clusters. These networks captured both the average MAP (aMAP) (b–d) and the average HR (aHR) (e–g) in a gradient fashion. Similarly, at least one AIS grade gain at discharge (‘yes’, ‘no’) was mapped over the network (h–j, gray: 15 AIS grades could not be extracted). Clusters of higher proportion of patients with recovery had an aMAP in a middle range, while clusters with higher proportion of patients without recovery presented extreme aMAPs (k). The mean cluster aHR showed a less apparent relationship with the proportion of AIS improvers (l).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig2-figsupp1-v4.jpg)

**Figure 2—figure supplement 1.:** The time-series signal between patients is not aligned (changes at specific time point might not reflect the same for each patient) and of different length due to the different duration of surgery (a). To be able to compute a distance metric between patients, we pre-processed the time-series data by calculating the cumulative distribution function (CDF) of each signal and each patient (b, see Methods). CDF was then used to compute the similarity between patients (Figure 2b, see Methods), input of Isomap for dimension reduction (Figure 2c). Two criteria were used to select the optimal solution for the Isomap. We first sought the solution that preserved major information in terms of the similarity between patients (distance metric) by minimizing the residual variance (c). We considered the minimal k being the one that produced a continuous (non-fragmented) k-NNG (k = 3). Residual variance was compared for different solutions of Isomap (3≤ k ≤ 7), without major differences between solutions, except for the first dimension (see Methods). This first analysis also suggested the real dimensionality of the data to be around three to four dimensions by looking at the ‘elbow’ in which no more substantial information would be added. We then selected the solution that minimized the loss of topological information by persistent homology. Wasserstein zero-dimensional (WD0, d) and one-dimensional (WD1, e) distances were computed. A final solution of k = 6 and 4 Isomap dimensions was chosen for being the one minimizing WD0 and WD1. Walktrap algorithm was chosen for network clustering. To determine the optimal number of random steps, an increasing number of steps were set and modularity (Q) computed (f). The first solution that maximized Q (Q = 0.837) was selected (dashed line in f and g). The optimal solution determined 11 clusters (h).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig2-figsupp2-v4.jpg)

**Figure 2—figure supplement 2.:** The proportion of AIS grades at discharge for each cluster was mapped into the network and its association with the mean average mean arterial pressure (aMAP) per cluster explored. Clusters with lower proportion of AIS A (a) and AIS B (b) were associated with central mean aMAP values (~90 mmHg in AIS A and 80–90 mmHg in AIS B) with higher proportion of those AIS grades at the extremes of mean aMAP. Contrary, AIS C (c), AIS D (d), and AIS E (e) at discharge showed the inverse relationship, clusters with higher proportion of AIS C, D, and E were associated with middle ranges of mean aMAP, while cluster with lower proportion of those grades trended to have extreme values of mean aMAP. This suggests that the population of patients with extreme values of aMAP had higher probability to be discharged with AIS A and B grades, while patients with central values of aMAP had higher probability of discharge with AIS C, D, and E. Moreover, the clusters with higher proportion of AIS improvers (C1, C2, C4, and C10, Figure 2) also showed higher proportions of AIS C, D, and E at discharge (f) than the clusters with lower proportion of improvers (C5, C8, C9, C11, Figure 2). These results further support the hypothesis that both hypotensive and hypertensive MAP during surgery is related with lower probability of recovery of at least one AIS grade at discharge. Trend lines (blue) were plotted to aid visual exploratory analysis.

### MAP has a non-linear association with probability of recovery

The exploratory network analysis revealed that clusters with higher proportion of patients that increased AIS of at least one grade were associated with having a middle range aMAP (Figure 2 and Figure 2—figure supplements 1 and 2) and that clusters of patients with aMAP on the extremes contained fewer improvers. We hypothesized that there might be a non-linear relationship between intra-operative MAP and the probability of AIS grade improvement. To confirm this hypothesis, logistic regression models with LOOCV were used (Figure 3, Table 2). We fitted a null model (no predictors) as well as linear, polynomial, and cubic models of aMAP (Figure 3, Table 2) to test the non-linearity of the hypothesis. The linear model showed a significant improvement over the null model with a positive association, suggesting that the higher the aMAP, the higher the probability of AIS grade improvement. However, polynomial logistic regression demonstrated a significant quadratic fit (Table 2) with lower LOOCV error than the linear model, indicating that a quadratic form of aMAP better predicts the probability of improvement. Notably, the cubic model did not show significant improvement over the quadratic one. Exploratory network analysis suggested an asymmetrical function of AIS improvement with respect to aMAP (Figure 2k); we therefore also tested spline models to relax the symmetry of polynomial models. A spline model of degree 2 resulted in a significant fit over the linear model (Table 2) while a spline model of degree 3 resulted in a similar fit as compared to the cubic model. There was no evidence from which to choose between the spline model of degree 2 and the quadratic model. Accordingly, we did not pursue the asymmetric model further, although we explore an asymmetric MAP range below.

![Figure 3.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig3-v4.jpg)

**Figure 3.:** Logistic regression models were fitted to study the potential non-linearity of the aMAP predictor as suggested by the exploratory analysis. Six different models were studied: naïve, linear, quadratic, cubic, spline of degree 2, and spline of degree 3. The estimated leave-one-out cross-validation (LOOCV) error for each model showed that both the quadratic and the spline of degree 2 have the minimal cross-validation error (a). This suggests that the linear model did not capture all the potential explainable variance of the response variable by aMAP, while the cubic and spline of degree 3 were probably overfitting the model (Table 2). (b) shows the logit function (blue line) and standard error (gray ribbon) of the quadratic model over the fitted values (points).

### Factors influencing MAP association with recovery

We sought to explore additional patient characteristics that might explain or affect MAP association with recovery. To test whether other factors could be responsible for the observed non-linear association, we first compared the quadratic model with aMAP as a predictor alone, a model that also includes several covariates (aHR, length of surgery, days from surgery to discharge, age, and AIS grade at admission), and a model with only the covariates. The significance of the quadratic fit holds even after accounting for the covariates (Table 3, 4), and none of the terms in the covariates-only model had a significant coefficient (Table 5). These results indicate that even in the presence of the other factors, aMAP is still non-linearly associated with AIS grade improvement at discharge.

**Table 5.**
 Evaluation of logistic regression covariates only (Wald test) and leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β2x2+β3x3+β4x4+β5x5+β6x6+β7x7+β8x8+β9x9, where x2 : average HR; x3: length of surgery (min); x4: days to AIS discharge (days); x5: age; x6: AIS admission D (‘yes’,’no’); x7: AIS admission C (‘yes’,’no’); x8: AIS admission B (‘yes’,’no’); x9: AIS admission A (‘yes’,’no’); (AIS admission E was set as the reference level for AIS admission variable and is part of the intercept) (final n = 93)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.612; average kappa statistic = 0.17</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= –1.585</td>
      <td>138.2</td>
      <td>–0.011</td>
      <td>0.991</td>
    </tr>
    <tr>
      <td>Average HR (x2)</td>
      <td>β2= –0.0209</td>
      <td>0.029</td>
      <td>–0.911</td>
      <td>0.362</td>
    </tr>
    <tr>
      <td>Length of surgery (x3)</td>
      <td>β3= 0.0016</td>
      <td>0.00141</td>
      <td>1.151</td>
      <td>0.250</td>
    </tr>
    <tr>
      <td>Days to AIS discharge (x4)</td>
      <td>β4= 0.0105</td>
      <td>0.0106</td>
      <td>0.993</td>
      <td>0.320</td>
    </tr>
    <tr>
      <td>Age (x5)</td>
      <td>β5= 0.0052</td>
      <td>0.012</td>
      <td>0.424</td>
      <td>0.672</td>
    </tr>
    <tr>
      <td>AIS admission D (x6)</td>
      <td>β6= 1.511</td>
      <td>1.382</td>
      <td>0.011</td>
      <td>0.991</td>
    </tr>
    <tr>
      <td>AIS admission C (x7)</td>
      <td>β7= 1.715</td>
      <td>1.382</td>
      <td>0.012</td>
      <td>0.991</td>
    </tr>
    <tr>
      <td>AIS admission B (x8)</td>
      <td>β8= 1.643</td>
      <td>1.382</td>
      <td>0.012</td>
      <td>0.990</td>
    </tr>
    <tr>
      <td>AIS admission A (x9)</td>
      <td>β9= 1.574</td>
      <td>1.382</td>
      <td>0.011</td>
      <td>0.991</td>
    </tr>
  </tbody>
</table>

Patients with more severe injuries are more likely to suffer hemodynamic dysregulations (Lehmann et al., 1987). Hence, we studied whether the relationship of MAP and AIS improvement was maintained in the subcohort of patients with an AIS grade of A at admission. We first filtered the data for the subcohort and then fitted a full model as above but without the AIS grade at admission covariate. The resulting model showed the linear aMAP coefficient to be significant and the quadratic term close to significant (p = 0.14) with the second biggest coefficient (Table 6). A likelihood ratio test between a linear model with covariates and a quadratic model with covariates resulted in p-values = 0.07. On the other hand, in the full model with covariates fitted to the entire cohort, none of the AIS grades at admission had significant coefficients, which suggested that the non-linear relationship of MAP with neurological recovery was sustained across injury severity in that model. This apparent divergence in results might be explained by the reduction in power for the AIS A cohort model.

**Table 6.**
 Evaluation of logistic regression in American Spinal Injury Association (ASIA) Impairment Scale (AIS) A at admission cohort (Wald test) and leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β11x1+β12x12+β2x2+β3x3+β4x4+β5x5, where x1: average MAP; x2 : average HR; x3: length of surgery (min); x4: days to AIS discharge (days); x5: age (final n = 51)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.63; average kappa statistic = 0.197</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= –0.931</td>
      <td>3.433</td>
      <td>–0.271</td>
      <td>0.786</td>
    </tr>
    <tr>
      <td>Average MAP (x1)</td>
      <td>β11= 10.79</td>
      <td>5.014</td>
      <td>2.153</td>
      <td>0.031*</td>
    </tr>
    <tr>
      <td>Average MAP (x12)</td>
      <td>β12= –6.73</td>
      <td>4.591</td>
      <td>–1.468</td>
      <td>0.142</td>
    </tr>
    <tr>
      <td>Average HR (x2)</td>
      <td>β2= –0.016</td>
      <td>0.035</td>
      <td>–0.468</td>
      <td>0.639</td>
    </tr>
    <tr>
      <td>Length of surgery (x3)</td>
      <td>β3= 0.0039</td>
      <td>0.0026</td>
      <td>1.504</td>
      <td>0.132</td>
    </tr>
    <tr>
      <td>Days to AIS discharge (x4)</td>
      <td>β4= 0.0067</td>
      <td>0.014</td>
      <td>0.477</td>
      <td>0.633</td>
    </tr>
    <tr>
      <td>Age (x5)</td>
      <td>β5= –0.012</td>
      <td>0.020</td>
      <td>–0.599</td>
      <td>0.549</td>
    </tr>
  </tbody>
</table>

_*p < 0.05._

Next, given that the level of the cord injury can be related to different degrees of hemodynamic dysregulation (Lehmann et al., 1987), we studied the effect of the NLI at admission on the association of MAP and patient recovery. Our cohort was very heterogeneous on the NLI, with most patients having cervical injuries and the rest distributed along the mid and lower segments of the cord (Table 7). Thus, we divided the population into two categories: cervical and non-cervical patients. Running the same full model with just the cervical patients resulted in similar results as compared to the full model on the entire cohort, maintaining the quadratic aMAP significance (Table 8). In the non-cervical cohort, we did not find a significant association of the quadratic aMAP to recovery (Table 9). We then performed additional analyses to determine whether this difference in aMAP relationship to recovery between cervical and non-cervical patients was due to differences in the likelihood of recovery between the two NLI populations. A univariate analysis suggested that the proportion of improvers and not improvers in the cervical and non-cervical population were marginally different (Table 1). Moreover, a logistic regression predicting AIS grade improvement by NLI categorization indicated that non-cervical patients were significantly less likely to recover ($\beta$ = –0.93, p = 0.041). While these results suggest that a quadratic aMAP is important for predicting AIS grade recovery in cervical patients, the lack of significant results in the non-cervical patients must be interpreted with caution due to the reduced number of cases, the heterogeneous distribution, and the low number of improvers in the group.

**Table 7.**
 Neurological level of injury cases.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="7">Cervical (n = 71)</th>
      <th colspan="13">Non-cervical (n = 32)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NLI</td>
      <td>C2</td>
      <td>C3</td>
      <td>C4</td>
      <td>C5</td>
      <td>C6</td>
      <td>C7</td>
      <td>C8</td>
      <td>T2</td>
      <td>T3</td>
      <td>T4</td>
      <td>T5</td>
      <td>T6</td>
      <td>T7</td>
      <td>T8</td>
      <td>T9</td>
      <td>T10</td>
      <td>T11</td>
      <td>T12</td>
      <td>S1</td>
      <td>S5</td>
    </tr>
    <tr>
      <td>Cases</td>
      <td>3</td>
      <td>3</td>
      <td>24</td>
      <td>28</td>
      <td>4</td>
      <td>8</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

**Table 8.**
 Evaluation of logistic regression in Cervical cohort (Wald test) and leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β11x1+β12x12+β2x2+β3x3+β4x4+β5x5+β6x6+β7x7+β8x8, where x1: average MAP; x2 : average HR; x3: length of surgery (min); x4: days to AIS discharge (days); x5: age; x6: AIS admission D (‘yes’,’no’); x7: AIS admission C (‘yes’,’no’); x8: AIS admission B (‘yes’,’no’); (AIS admission A was set as the reference level for AIS admission variable and is part of the intercept, no AIS admission E was present in this cohort) (final n = 93)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.688; average kappa statistic = 0.362</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= 2.747</td>
      <td>3.018</td>
      <td>0.91</td>
      <td>0.363</td>
    </tr>
    <tr>
      <td>Average MAP (x1)</td>
      <td>β11= 7.594</td>
      <td>3.056</td>
      <td>2.485</td>
      <td>0.013*</td>
    </tr>
    <tr>
      <td>Average MAP (x12)</td>
      <td>β12= –7.528</td>
      <td>3.358</td>
      <td>–2.242</td>
      <td>0.025*</td>
    </tr>
    <tr>
      <td>Average HR (x2)</td>
      <td>β2= –0.055</td>
      <td>0.034</td>
      <td>–1.608</td>
      <td>0.108</td>
    </tr>
    <tr>
      <td>Length of surgery (x3)</td>
      <td>β3= 0.0014</td>
      <td>0.0019</td>
      <td>0.720</td>
      <td>0.472</td>
    </tr>
    <tr>
      <td>Days to AIS discharge (x4)</td>
      <td>β4= 0.0022</td>
      <td>0.012</td>
      <td>0.182</td>
      <td>0.855</td>
    </tr>
    <tr>
      <td>Age (x5)</td>
      <td>β5= 0.0079</td>
      <td>0.016</td>
      <td>0.482</td>
      <td>0.630</td>
    </tr>
    <tr>
      <td>AIS admission D (x6)</td>
      <td>β6= –0.747</td>
      <td>0.87</td>
      <td>–0.840</td>
      <td>0.730</td>
    </tr>
    <tr>
      <td>AIS admission C (x7)</td>
      <td>β7= 0.745</td>
      <td>0.80</td>
      <td>0.925</td>
      <td>0.355</td>
    </tr>
    <tr>
      <td>AIS admission B (x8)</td>
      <td>β8= 0.301</td>
      <td>0.88</td>
      <td>0.346</td>
      <td>0.401</td>
    </tr>
  </tbody>
</table>

_*p < 0.05._

**Table 9.**
 Evaluation of logistic regression in non-cervical cohort only (Wald test) and leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β11x1+β12x12+β2x2+β3x3+β4x4+β5x5+β6x6+β7x7+β8x8+β9x9, where x1: average MAP; x2 : average HR; x3: length of surgery (min); x4: days to AIS discharge (days); x5: age; x6: AIS admission D (‘yes’,’no’); x7: AIS admission C (‘yes’,’no’); x8: AIS admission B (‘yes’,’no’); x9: AIS admission A (‘yes’,’no’); (AIS admission E was set as the reference level for AIS admission variable and is part of the intercept) (final n = 93)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.688; average kappa statistic = 0.362</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= –1.883</td>
      <td>352.4</td>
      <td>–0.005</td>
      <td>0.996</td>
    </tr>
    <tr>
      <td>Average MAP (x1)</td>
      <td>β11= –0.206</td>
      <td>4.713</td>
      <td>–0.044</td>
      <td>0.965</td>
    </tr>
    <tr>
      <td>Average MAP (x12)</td>
      <td>β12= –8.064</td>
      <td>7.643</td>
      <td>–1.055</td>
      <td>0.291</td>
    </tr>
    <tr>
      <td>Average HR (x2)</td>
      <td>β2= –0.0002</td>
      <td>0.0649</td>
      <td>0.004</td>
      <td>0.997</td>
    </tr>
    <tr>
      <td>Length of surgery (x3)</td>
      <td>β3= 0.0018</td>
      <td>0.0054</td>
      <td>0.336</td>
      <td>0.737</td>
    </tr>
    <tr>
      <td>Days to AIS discharge (x4)</td>
      <td>β4= 0.076</td>
      <td>0.0613</td>
      <td>1.240</td>
      <td>0.215</td>
    </tr>
    <tr>
      <td>Age (x5)</td>
      <td>β5= –0.0047</td>
      <td>0.051</td>
      <td>–0.921</td>
      <td>0.357</td>
    </tr>
    <tr>
      <td>AIS admission D (x6)</td>
      <td>β6= 1.727</td>
      <td>3.524</td>
      <td>0.005</td>
      <td>0.996</td>
    </tr>
    <tr>
      <td>AIS admission C (x7)</td>
      <td>β7= 3.557</td>
      <td>5.782</td>
      <td>0.005</td>
      <td>0.996</td>
    </tr>
    <tr>
      <td>AIS admission B (x8)</td>
      <td>β8= 1.738</td>
      <td>3.524</td>
      <td>0.005</td>
      <td>0.995</td>
    </tr>
    <tr>
      <td>AIS admission A (x9)</td>
      <td>β9= 1.686</td>
      <td>3.524</td>
      <td>0.005</td>
      <td>0.996</td>
    </tr>
  </tbody>
</table>

Finally, we sought to determine whether the probability of recovery associated to MAP could be influenced by the time the patient is in the hospital. For that, we break down the potential causal pathway between MAP dysregulation, AIS improvement, and days from surgery to discharge. We first fitted a logistic regression model with AIS improvement as response and days to discharge as the only predictor. This resulted in a non-significant p-value of p = 0.32, suggesting that days to discharge does not associate with probability of improvement. Second, we fitted a linear model with days to discharge as a response and quadratic aMAP (both linear and quadratic terms) as predictors. This resulted as a significant coefficient of the quadratic term (p = 0.047), although the model was not significant (p = 0.13 for the F statistic) and the adjusted R2 was small (0.0217). We also investigated whether days to discharge interacts with MAP and quadratic MAP to predict AIS improvement, with no significant results on the interaction (interaction days to discharge with aMAP: linear term p = 0.61; quadratic term p = 0.91). These suggest that these two factors do not moderate each other. Finally, eliminating days to discharge from the full covariate model predicting AIS improvement does not have a major effect on the model fit. A likelihood ratio test between both models shows a non-significant change in variance explained (p = 0.729) with a deviance difference of ~0.1%. All together indicates that the non-linear relationship between aMAP and AIS improvement is independent of the days from surgery to discharge.

### Intra-operative MAP range from 76-[104-117] mmHg predicts recovery

Since aMAP can obscure episodes of high deviation from average (Hawryluk et al., 2015) and has a non-linear relationship with recovery, we hypothesized that there might be a range of intra-operative MAP that better predicts AIS grade improvers. To test this hypothesis, we analyzed the amount of time MAP was out of a specific range (Figure 4). Since our modeling suggested both a symmetric and asymmetric range, we performed two different analyses. First, starting at a MAP of 90 mmHg, we implemented an algorithm to iteratively expand the MAP range symmetrically 1 mmHg higher and lower and calculate the time MAP was outside the range (Figure 4a). Exploratory analysis of the similarity network indicated a high association between the time out of a MAP range of 73–107 mmHg with the topological distribution of patients (Figure 4b and Figure 4—figure supplement 1). To validate this range and the associated lower and upper MAP thresholds, we used a logistic model with LASSO regularization with the predictors being the time outside of each MAP range as in Figure 4b. This allowed us to systematically reduce the number of relevant predictors until only one remained (non-zero coefficient). Interestingly, the logistic LASSO regression with LOOCV revealed that a MAP range from 76 to 104 mmHg was optimal in our dataset since it produced the most reproducible prediction of recovery (average LOOCV prediction accuracy of 61.16%; Figure 4c and Figure 2—figure supplement 2, Table 9). Next, we studied the possibility of an asymmetric range by fixing the lower limit to 76 mmHg and increasing the upper limit by 1 mmHg at the time (Figure 4d). The association of the patient distribution in the network plateau at a range of 76–116 mmHg (Figure 4e and Figure 4—figure supplement 1) and the logistic LASSO found the range 76–117 mmHg be the most predictive of recovery (average cross-validation prediction accuracy of 57.28%; Figure 4f and Figure 4—figure supplement 2a, Table 10). While both the exploratory analysis and the logistic LASSO produced similar ranges, the later analysis is performed through statistical modeling rather than descriptive associations, and therefore we further discuss the results of the LASSO.

![Figure 4.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig4-v4.jpg)

**Figure 4.:** To find the optimal MAP range, a moving MAP range was computed and the time of MAP outside range calculated (a and d, example of the same patient for symmetric and asymmetric map range, respectively). Calculating the assortativity coefficient (Ar) of the network for each range revealed that the distribution of patients in the network was most highly associated with the range 73–107 mmHg for the symmetric range (b, Figure 4—figure supplement 1), and 76–116 mmHg for the asymmetric range study of upper limit threshold (e, Figure 4—figure supplement 1). A logistic LASSO (least absolute shrinkage and selection operator) regression (Figure 4—figure supplement 2a, Figure 4—figure supplement 3) was used as a confirmatory analysis and to obtain the MAP range that most highly predicts AIS grade recovery. For the symmetric range, the time of MAP outside the 76–104 mmHg (c, Table 10) was found to be the ‘last-standing’ predictor during LASSO regularization (Figure 4—figure supplement 2a), suggesting that greater duration outside this range is associated with lower probability of neurological recovery. In the case of the asymmetric range (Figure 4—figure supplement 3), the last non-zero coefficient was for the range 76–117 mmHg (f, Table 11).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig4-figsupp1-v4.jpg)

**Figure 4—figure supplement 1.:** We further explored the relationship of the distribution of patients in the network and the amount of time their MAP was out of a specific range (Figure 4). For each MAP range, the assortativity coefficient (Ar) was calculated (Figure 4). The major Ar was achieved when considering the time of MAP out of the range 73–107 mmHg for the symmetric range (a–c), and the range 76–116 mmHg for the asymmetric one (d–f). Mapping those values of time into the similarity network (a), we observe patients with the longest times or patients with the shortest times were localized together, indicating that the network was capturing the clustering structure associated with time of MAP out of the specific range. The mean time out of that range per cluster presented an inverse relationship with its proportion of AIS improvers (c and f) where clusters of patients with longer times of MAP out of range has lower proportion of AIS improvers. This reinforced the hypothesis that low probability of improvement at least one AIS at discharge is related with the amount of time MAP is out of a lower and upper boundary. Consequently, we performed confirmatory analysis of this hypothesis using a logistic LASSO (least absolute shrinkage and selection operator) regression (Figure 4 and Figure 4—figure supplement 2a, Figure 4—figure supplement 3). Trend lines (blue) are plotted to aid visual exploratory analysis.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig4-figsupp2-v4.jpg)

**Figure 4—figure supplement 2.:** (a) The deviance of the binomial model used as cross-validation error (mean and standard deviation) in the LOOCV (see Methods) against the values of l (in log form). The two vertical doted lines express the model that produces the minimal error (left line) and the first model to reach one standard deviation from the minimal error (see Methods). (b) The coefficients (each colored line) for a given value of l (in log form). The values on top in (a) and (b) express the number of non-zero coefficients for a given l. A value of l = 0.121 shrinks the model to one single predictor (time of MAP out of range 76–104). A logistic regression for time of MAP out of range 76–104 was then fitted (Figure 4). (c) Plots of fitting a logistic regression for each range of MAP. It can be appreciated how as the range of MAP gets wider, the relationship of time out of range and probability of AIS improvement gets stronger until a point where the range is too wide to discriminate between AIS improvers and non-improvers.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig4-figsupp3-v4.jpg)

**Table 10.**
 Least absolute shrinkage and selection operator (LASSO) solution and logistic regression of most predictive symmetric range with leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β1x1, where x1: time of MAP outside range 76–104 mmHg (n = 103 patients)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.61; average kappa statistic = 0.158</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= 0.368</td>
      <td>0.333</td>
      <td>1.103</td>
      <td>0.269</td>
    </tr>
    <tr>
      <td>Time MAP out 76–104 (x1)</td>
      <td>β1= –0.006</td>
      <td>0.0026</td>
      <td>–2.566</td>
      <td>0.0103*</td>
    </tr>
  </tbody>
</table>

_*p < 0.05._

**Table 11.**
 Least absolute shrinkage and selection operator (LASSO) solution and logistic regression of most predictive asymmetric range with leave-one-out cross-validation (LOOCV).


<table>
  <thead>
    <tr>
      <th colspan="5">Model: l=β0+β1x1, where x1: time of MAP outside range 76–117 mmHg (n = 103 patients)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">LOOCV: average observed accuracy = 0.5728; average kappa statistic = 0.102</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Std. error</td>
      <td>z-Value</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= 0.2881</td>
      <td>0.287</td>
      <td>1.002</td>
      <td>0.316</td>
    </tr>
    <tr>
      <td>Time MAP out 76–117 (x1)</td>
      <td>β1= –0.00788</td>
      <td>0.0027</td>
      <td>–2.828</td>
      <td>0.00468**</td>
    </tr>
  </tbody>
</table>

_**p < 0.01._

Altogether, the findings indicate that the time of MAP outside a measurable normotensive range during surgery is associated with lower odds of recovering at least one AIS grade. Our analysis suggests the optimal range for recovery is between 76–104 and 76–117 mmHg. Notice that while range 76–104 mmHg has higher predictive utility than 76–117 mmHg (mean LOOCV accuracy of 61.16 % vs. 57.28%), the difference in variance of the probability of AIS improvement explained by these two predictors is minimal (<4% difference in RV). Therefore, from a modeling perspective, we broadly conclude that the upper limit of the MAP range is probably anywhere between 104 and 117 mmHg.

### Building a predictive model of outcome

Finally, we wanted to study the prediction utility of a model including the analyzed features together with other patient characteristics. We focused on three classification tasks: a model predicting AIS improvement of at least one grade at discharge, a model predicting AIS A at discharge, and a model predicting AIS D at discharge. We chose to predict AIS A and D instead of a multiclass prediction of the AIS at discharge in concordance to our previous studies (Kyritsis et al., 2021) and because of the low representation of other grades in our dataset (Table 1). For each of the three classification tasks, we performed an exhaustive search of all possible additive models with at least one of the predictors of interest: quadratic aMAP, aHR, length of surgery, days from surgery to discharge, age, AIS grade at admission, dichotomized NLI (cervical, non-cervical), time of MAP out of range 76–104, and time of MAP out of range 76–117. We selected the parsimonious model as the model that minimized the small-sample corrected AIC (Table 12). Next, for the selected best model for each task, we performed LOOCV performance evaluation and prediction threshold calibration balancing prediction sensitivity and specificity (Figure 5). The model predicting AIS improvement had a cross-validated AUC of 0.74, the model predicting AIS A at discharge had a cross-validated AUC of 0.88, and the model predicting AIS D at discharge had a cross-validation AUC of 0.84. Other metrics of classification performance can be seen in Table 12. Both the parsimonious model predicting AIS improvement and the one predicting AIS A at discharge included quadratic aMAP as an important predictor. The model predicting AIS A also included the time of MAP out of range 76–117 mmHg. The model predicting AIS D did not include any of the MAP associated terms, suggesting that patients discharged with AIS D can be predicted without considering their MAP during OR. In fact, training the same model but with the inclusion of the quadratic aMAP term resulted in slightly worse prediction performance (AUC 0.84 vs. 0.83). Training the models predicting AIS improvement and AIS A at discharge but without a MAP component (quadratic MAP term or time of MAP out of range) reduced the model performance considerably (AUC, AIS improvement: 0.74 vs. 0.52; AIS A discharge: 0.88 vs. 0.78).

![Figure 5.](https://cdn.elifesciences.org/articles/68015/elife-68015-fig5-v4.jpg)

**Figure 5.:** We built three prediction models, one to predict American Spinal Injury Association (ASIA) Impairment Scale (AIS) improvement of at least one grade at discharge (AIS impro., a), one to predict AIS A at discharge (A at disch., b) and one to predict AIS D at discharge (D at disch., c). The sensitivity and specificity for each model was computed out of the prediction probability of LOOCV, where each leave-one-out patient is predicted with the model that was trained without that patient. For each model, the classification threshold was set at the probability that balances sensitivity and specificity (dashed red line). The receiving operation curve (ROC) and area under the curve (AUC) for the three models are presented in d.

**Table 12.**
 Best prediction models of outcome.


<table>
  <thead>
    <tr>
      <th colspan="4">Model predicting AIS improvement:l=β0+β11x1+β12x12+β2x2+β3x3+β4x4+β5x5Model predicting AIS A:l=β0+β11x1+β12x12+β2x2+β3x3+β4x4+β5x5+β6x6+β7x7Model predicting AIS D:l=β0+β2x2+β3x3+β4x4+β5x5+β8x8+β9x9where x1: average MAP; x2 : AIS admission A (‘yes’, ‘no’); x3 : AIS admission B (‘yes’, ‘no’); x4 : AIS admission C (‘yes’, ‘no’); x5 : AIS admission D (‘yes’, ‘no’); x6 : NLI non-cervical; x7 : Time MAP out 76–117; x8 : Length of surgery; x9 : Age; (AIS admission E and NLI cervical were set as the reference levels for the corresponding variable and are part of the intercept). All metrics are on LOOCV prediction (n = 93)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td></td>
      <td>Model AIS improv.</td>
      <td>Model AIS A</td>
      <td>Model AIS D</td>
    </tr>
    <tr>
      <td>Predictor</td>
      <td>Coef. estimate (logit)</td>
      <td>Coef. estimate (logit)</td>
      <td>Coef. estimate (logit)</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>β0= –16.24</td>
      <td>β0= 20.466</td>
      <td>β0= 1.558</td>
    </tr>
    <tr>
      <td>Average MAP (x1)</td>
      <td>β11= 7.374</td>
      <td>β11= 27.031</td>
      <td></td>
    </tr>
    <tr>
      <td>Average MAP (Cohn et al., 2010) (x1)</td>
      <td>β12= –8.215</td>
      <td>β12= –17.138</td>
      <td></td>
    </tr>
    <tr>
      <td>AIS admission A (x2)</td>
      <td>β2= 15.54</td>
      <td>β2= –22.814</td>
      <td>β2= 2.324</td>
    </tr>
    <tr>
      <td>AIS admission B (x3)</td>
      <td>β3= 16.1818</td>
      <td>β3= –20.38</td>
      <td>β3= 0.41</td>
    </tr>
    <tr>
      <td>AIS admission C (x4)</td>
      <td>β4= 16.752</td>
      <td>β4= –19.01</td>
      <td>β4= –2.591</td>
    </tr>
    <tr>
      <td>AIS admission D (x5)</td>
      <td>β5= 14.828</td>
      <td>β5= 0.217</td>
      <td>β5= –2.624</td>
    </tr>
    <tr>
      <td>NLI non-Cervical (x6)</td>
      <td></td>
      <td>β6= –1.228</td>
      <td></td>
    </tr>
    <tr>
      <td>Time MAP out 76–117 (x7)</td>
      <td></td>
      <td>β7= 0.017</td>
      <td></td>
    </tr>
    <tr>
      <td>Length of Surgery (x8)</td>
      <td></td>
      <td></td>
      <td>β8= –0.0044</td>
    </tr>
    <tr>
      <td>Age (x9)</td>
      <td></td>
      <td></td>
      <td>β9= 0.03</td>
    </tr>
    <tr>
      <td>Model performance metric</td>
      <td>Metric value</td>
      <td>Metric value</td>
      <td>Metric value</td>
    </tr>
    <tr>
      <td>Accuracy (95% CI)</td>
      <td>0.73 (0.629, 0.818)</td>
      <td>0.82 (0.735, 0.898)</td>
      <td>0.806 (0.71, 0.881)</td>
    </tr>
    <tr>
      <td>AUC</td>
      <td>0.743</td>
      <td>0.88</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>Kappa</td>
      <td>0.45</td>
      <td>0.629</td>
      <td>0.573</td>
    </tr>
    <tr>
      <td>Sensitivity</td>
      <td>0.71</td>
      <td>0.812</td>
      <td>0.793</td>
    </tr>
    <tr>
      <td>Specificity</td>
      <td>0.74</td>
      <td>0.836</td>
      <td>0.812</td>
    </tr>
    <tr>
      <td>Positive predicted value</td>
      <td>0.658</td>
      <td>0.72</td>
      <td>0.657</td>
    </tr>
    <tr>
      <td>Negative predicted value</td>
      <td>0.788</td>
      <td>0.89</td>
      <td>0.896</td>
    </tr>
  </tbody>
</table>

Altogether, this suggests that models can be built for predicting AIS improvement or AIS A at discharge and that such the model performance critically depends on MAP during OR. Conversely, we did not find evidence that predicting AIS D at hospital discharge is dependent on intra-operative MAP.

## Discussion

Acute hypotension is common in patients with SCI due to neurogenic shock (Lehmann et al., 1987; Krassioukov et al., 2007) and autonomic dysregulation (Lehmann et al., 1987), probably contributing to post-traumatic spinal ischemia (Streijger et al., 2018; Hall and Wolf, 1987), which is known to cause impaired neurological recovery in animal models (Fehlings et al., 1989). Level 4 evidence from a small single-center case series study in the 1990s suggested that MAP augmentation to 85–90 mmHg during the first 5–7 days after injury was linked to neurological recovery in acute SCI (Levi et al., 1993; Vale et al., 1997). These results are the basis of clinical guidelines for avoidance of hypotension in acute SCI management (Aarabi et al., 2013). However, while numerous clinical studies support MAP augmentation, the arbitrary, recommended MAP goal has been controversial (Cohn et al., 2010; Hawryluk et al., 2015; Saadeh et al., 2017). Recent analysis of high-frequency ICU monitoring data (Hawryluk et al., 2015) and systematic meta-analysis of post-surgery management (Saadeh et al., 2017) suggest that the MAP threshold to avoid is actually lower (~75 mmHg) than the current recommendation of 85 mmHg, and that MAP management might be effective at shorter duration (< 5 days post-injury) than the 7-day goal (Saadeh et al., 2017). The present study represents a multicenter, data-driven, and cross-validated re-evaluation in a different setting (during surgery as compared with prior ICU studies).

Our analysis support that there must be a MAP range during surgery at which neurological recovery is maximized, providing further evidence that MAP management for maintaining normotension might be more beneficial for patient outcome than MAP augmentation for hypotension avoidance alone (Ehsanian, 2020; Nielson et al., 2015). The low boundary of 76 mmHg found in our ultra-early analysis further supports previous suggestions for lowering the intervention threshold (Cohn et al., 2010; Hawryluk et al., 2015; Saadeh et al., 2017). On the other side, we find an upper boundary to MAP management between 104 and 117 mmHg, above which the probability of improvement is reduced. Thus, the proposal for MAP augmentation with vasopressors to increase spinal cord perfusion (Saadoun and Papadopoulos, 2016) has a limit since spinal hyper-perfusion pressure can be detrimental (Saadoun and Papadopoulos, 2016). The physiological rational is that high blood pressure induced by vasopressors can translate to increased risk of hemorrhage in the injured spinal cord, exacerbating tissue damage (Soubeyrand et al., 2014; Streijger et al., 2018; Guha et al., 1987). Moreover, the use of some vasopressors might cause more complications in patients (Inoue et al., 2014) while also potentially contributing to intra-spinal hemorrhage. In fact, recent results in acute experimental SCI suggest controlling for hemodynamic dysregulation through a cardiac-focused treatment instead of using standard vasopressors such as norepinephrine (Williams et al., 2020). Specifically, the authors demonstrated that dobutamine can correct for hemodynamic anomalies and increase blood flow to the spinal cord while reducing the risk of hemorrhage compared to norepinephrine. Furthermore, hypertension during surgery in rodent SCI has been associated with lower probability of recovery (Nielson et al., 2015), probably related to higher tissue damage. Our findings together with previous work (Ehsanian, 2020) also translate these animal study results to humans, indicating that prolonged periods of hypertension early after injury can be a predictor of poor neurological recovery in patients with SCI.

An important finding of our study is the indication that level of injury and injury severity modify the association of MAP with neurological recovery. We observed that normotensive MAP during surgery predicts AIS improvement in patients with cervical SCI but not in patients with lower injuries (thoracic, lumbar, and sacral). While the heterogeneity of our population and low sample size for patients with non-cervical SCI sets limitations on interpreting the results, our finding raises a relevant question regarding precision management of patients with SCI. Patients with cervical SCI present more frequently with hemodynamic and cardiac abnormalities than patients with thoracolumbar SCI, increasing the need for treatment (Lehmann et al., 1987). This is due to sympathetic dysregulation in upper cord injuries, which reduces sympathetic tone likely causing reduced heart contractility, bradycardia, and hypotension (Lehmann et al., 1987; Myers et al., 2007; Teasell et al., 2000). This is particularly true for individuals with severe cervical injury (Lehmann et al., 1987). In that context, our results may indicate that those patients with cervical SCI that are more difficult to maintain within a normotensive MAP are probably less likely to improve in neurological function. Alternatively, it could also be the case that more aggressive MAP management treatment is performed in these patients during their course in the hospital, which could increase the chances of aggravating secondary cord injury. Hemodynamic instability early after injury could serve as a prognostic physiology-based biomarker in a subset of the population, providing a potential tool for precision medicine in SCI. Hence, we have established basic prediction models around non-linear features of MAP that could serve as a benchmark for future machine learning development.

Another relevant contribution of this work is the analytical workflow. First, we demonstrate that topology-based analytics can undercover associations for hypothesis generation during exploratory analysis in a cross-species validation. Our group has previously used a similar workflow in data from animal models (Nielson et al., 2015) suggesting that hypertension is a predictor of neurological recovery and providing rational for the present study. Hence, our work constitutes a successful story of translating machine intelligence analytical tools from animals to humans. Second, we provide further illustration that patient similarity networks are useful and interpretable representations of multidimensional datasets that capture associations during exploratory analysis that can then be validated by network-independent confirmatory analysis. Third, we successfully combine Isomap, a non-linear dimensionality reduction method, with topology-based metrics to evaluate embedding solutions. Fourth, our method for finding the MAP range could be expanded and deployed in other settings. Lastly, our workflow captures representations of multidimensional time-series of different lengths into a network that is actionable.

Limitations of this study include the retrospective nature of the analysis, the relatively small sample size (although large for SCI), and the use of an estimated ordinal scale (AIS grade) as an indicator of neurological recovery. An important consideration is the difficulty of determining AIS grade early after injury. Moreover, other factors not considered in this analysis such as MAP levels before or after surgery or the use of vasopressors might influence the results. Future research with more granular data should address these and other important questions.
