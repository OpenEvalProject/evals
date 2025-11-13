# Optimal transport for automatic alignment of untargeted metabolomic data

## Authors

- Marie Breeur<sup>1</sup> ([ORCID: 0000-0003-1251-8360](https://orcid.org/0000-0003-1251-8360))
- George Stepaniants<sup>2</sup> ([ORCID: 0000-0002-7834-7536](https://orcid.org/0000-0002-7834-7536))
- Pekka Keski-Rahkonen<sup>1</sup> ([ORCID: 0000-0001-9437-3040](https://orcid.org/0000-0001-9437-3040))
- Philippe Rigollet<sup>2</sup>
- Vivian Viallon<sup>1</sup> ([ORCID: 0000-0002-9799-4421](https://orcid.org/0000-0002-9799-4421)) †

### Affiliations

1. Nutrition and Metabolism Branch, International Agency for Research on Cancer Lyon France ([ROR:00v452281](https://ror.org/00v452281))
2. Massachusetts Institute of Technology, Department of Mathematics Boston United States ([ROR:042nb2s44](https://ror.org/042nb2s44))

† Corresponding author

## Abstract

Untargeted metabolomic profiling through liquid chromatography-mass spectrometry (LC-MS) measures a vast array of metabolites within biospecimens, advancing drug development, disease diagnosis, and risk prediction. However, the low throughput of LC-MS poses a major challenge for biomarker discovery, annotation, and experimental comparison, necessitating the merging of multiple datasets. Current data pooling methods encounter practical limitations due to their vulnerability to data variations and hyperparameter dependence. Here, we introduce GromovMatcher, a flexible and user-friendly algorithm that automatically combines LC-MS datasets using optimal transport. By capitalizing on feature intensity correlation structures, GromovMatcher delivers superior alignment accuracy and robustness compared to existing approaches. This algorithm scales to thousands of features requiring minimal hyperparameter tuning. Manually curated datasets for validating alignment algorithms are limited in the field of untargeted metabolomics, and hence we develop a dataset split procedure to generate pairs of validation datasets to test the alignments produced by GromovMatcher and other methods. Applying our method to experimental patient studies of liver and pancreatic cancer, we discover shared metabolic features related to patient alcohol intake, demonstrating how GromovMatcher facilitates the search for biomarkers associated with lifestyle risk factors linked to several cancer types.

## Introduction

Untargeted metabolomics is a powerful analytical technique used to identify and measure a large number of metabolites in a biological sample without preselecting targets (Patti, 2011). This approach allows for a comprehensive overview of an individual’s metabolic profile, provides insights into the biochemical processes involved in cellular and organismal physiology (Wishart, 2019; Pirhaji et al., 2016), and allows for the exploration of how environmental factors impact metabolism (Rappaport et al., 2014; Bedia, 2022). It creates new opportunities to investigate health-related conditions, including diabetes (Wang et al., 2011), inflammatory bowel diseases Franzosa et al., 2019, and various cancer types (Loftfield et al., 2021; Li et al., 2020). However, a major challenge in biomarker discovery, metabolic signature identification and other untargeted metabolomic analyses lies in the low throughput of experimental data, necessitating the development of efficient pooling algorithms capable of merging datasets from multiple sources (Loftfield et al., 2021).

A common experimental technique in untargeted metabolomics is liquid chromatography-mass spectrometry (LC-MS) which assembles a list of thousands of unlabeled metabolic features characterized by their mass-to-charge ratio ($m/z$), retention time (RT; Zhou et al., 2012), and intensity across all biological samples. Combining LC-MS datasets from multiple experimental studies remains challenging due to variation in the $m/z$ and RT of a feature from one study to another (Zhou et al., 2012; Ivanisevic and Want, 2019). This problem is further compounded by differing instruments and analytical protocols across laboratories, resulting in seemingly incompatible metabolomic datasets.

Manual matching of metabolic features can be a laborious and error-prone task (Loftfield et al., 2021). To address this challenge, several automated methods have been developed for metabolic feature alignment. One such method is MetaXCMS, which matches LC-MS features based on user-defined $m/z$ and RT thresholds (Tautenhahn et al., 2011). More advanced tools use information on feature intensities measured in samples. For instance, PAIRUP-MS uses known shared metabolic features to impute the intensities of all features from one dataset to another Hsu et al., 2019. MetabCombiner (Habra et al., 2021) and M2S (Climaco Pinto et al., 2022) compare average feature intensities, along with their $m/z$ and RT values, to align datasets without requiring extensive knowledge of shared features. These automated alignment methods have accelerated our ability to pool and annotate datasets as well as extract biologically meaningful biomarkers. However, they demand substantial fine-tuning of user-defined parameters and ignore correlations among metabolic features which provide a wealth of additional information on shared features.

Here, we introduce GromovMatcher, a user-friendly flexible algorithm which automates the matching of metabolic features across experiments. The main technical innovation of GromovMatcher lies in its ability to incorporate the correlation information between metabolic feature intensities, building upon the powerful mathematical framework of computational optimal transport (OT; Peyré and Cuturi, 2019; Villani, 2021). OT has proven effective in solving various matching problems and has found applications in multiomics analysis (Demetci et al., 2022), cell development (Schiebinger et al., 2019; Yang et al., 2020), and chromatogram alignment (Skoraczyński et al., 2022). Here, we leverage the Gromov-Wasserstein (GW) method (Mémoli, 2011; Solomon et al., 2016), which matches datasets based on their distance structure and has been seminally applied to spatial reconstruction problems in genomics Nitzan et al., 2019. GromovMatcher builds upon the GW algorithm to automatically uncover the shared correlation structure among metabolic feature intensities while also incorporating $m/z$ and RT information in the final matching process.

To assess the performance of GromovMatcher, we systematically benchmark it on synthetic data with varying levels of noise, feature overlap, and data normalizations, outperforming prior state-of-the-art methods of metabCombiner (Habra et al., 2021) and M2S (Climaco Pinto et al., 2022). Next, we apply GromovMatcher to align experimental patient studies of liver and pancreatic cancer to a reference dataset and associate the shared metabolic features to each patient’s alcohol intake. Through these efforts, we demonstrate how GromovMatcher data pooling improves our ability to discover biomarkers of lifestyle risk factors associated with several types of cancer.

## Results

### GromovMatcher algorithm

GromovMatcher uses the mathematical framework of OT to find all matching metabolic features between two untargeted metabolomic datasets (Figure 1). It accepts two LC-MS datasets with possibly different numbers of metabolic features and samples. Each feature, $fx_{i}$ in Dataset 1 and $fy_{j}$ in Dataset 2, is identified by its $m/z$, RT, and vector of feature intensities across samples (Figure 1a). The primary tenet of GromovMatcher is that shared metabolic features have similar correlation patterns in both datasets and can be matched based on the distance/correlations between their feature intensity vectors. Specifically, GromovMatcher computes the pairwise distances between the feature intensity vectors of each metabolic feature in a dataset and saves them into a distance matrix, one per dataset (Figure 1b). In practice, we use either the Euclidean distance or the cosine distance (negative of correlation) to perform this step (Materials and methods). The resulting distance matrices contain information about the feature intensity similarity within each study. Using optimal transport, we can deduce shared subsets of metabolic features in both datasets which have corresponding feature intensity distance structures.

![Figure 1.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig1-v1.jpg)

**Figure 1.:** (a) Inputs are two LC-MS datasets of unlabeled metabolic features (rows) identified by their $m/z$, RT, and feature intensities across biospecimen samples. Both studies can have differing numbers of metabolic features and samples. (b) In both datasets, the intensities across samples of each metabolic feature are formed into a vector and Euclidean distances between these feature vectors are computed and stored in a distance matrix. (c) Based on the technique of optimal transport, the unbalanced GW algorithm learns a coupling matrix $Π~$ that places large weights $Π~_{ij}\geq0$ when $fx_{i}$ and $fy_{j}$ likely correspond to the same metabolic feature. It optimizes $Π~$ to match features with similar pairwise distances (red outlined boxes) whose $m/z$ ratios are close. (d) The final step of GromovMatcher plots the retention times of features from both datasets against each other and fits a spline interpolation $f^$ weighted by the estimated coupling weights $Π~$. This retention time drift function is then used to set all entries $Π~_{ij}$ to zero for those outlier pairs $(fx_{i},fy_{j})$ which exceed twice the median absolute deviation (MAD) around $f^$ (green highlighted region). Finally, the coupling matrix $Π~$ is filtered and/or thresholded to obtain a refined coupling $Π^$ which is then binarized to obtain a one-to-one matching $M$ between a subset of metabolite pairs in both datasets.

OT was originally developed to optimize the transportation of soil for the construction of forts (Monge, 1781) and was later generalized through the language of probability theory and linear programming (Kantorovich, 2006), leading to efficient numerical algorithms and direct applications to planning problems in economics. The ability of OT to efficiently match source to target locations found applications in data science for the alignment of distributions (Courty et al., 2017; Alvarez-Melis et al., 2019) and was generalized by the Gromov-Wasserstein (GW) method (Peyré et al., 2016; Alvarez-Melis and Jaakkola, 2018) to align datasets with features of differing dimensions.

In practice, a sizeable fraction of the metabolic features measured in one study may not be present in the other. Hence, in most cases only a subset of features in both datasets can be matched. Recent GW formulations for unbalanced matching problems (Sejourne et al., 2021) allow for matching only subsets of metabolic features with similar intensity structures (Figure 1c). To incorporate additional feature information, we modify the optimization objective of unbalanced GW to penalize feature matches whose $m/z$ differences exceed a fixed threshold (Materials and methods, Appendix 1). The optimization of this objective computes a coupling matrix$Π~$ where each entry $Π~_{ij}\geq0$ indicates the level of confidence in matching metabolic feature $fx_{i}$ in Dataset 1 to $fy_{j}$ in Dataset 2.

Differences in experimental conditions can induce variations in RT between datasets that can be nonlinear and large in magnitude (Zhou et al., 2012; Climaco Pinto et al., 2022; Habra et al., 2021). In the spirit of previous methods for LC-MS batch or dataset alignment (Smith et al., 2006; Brunius et al., 2016; Liu et al., 2020; Vaughan et al., 2012; Habra et al., 2021; Climaco Pinto et al., 2022; Skoraczyński et al., 2022), the learned coupling $Π~$ is used to estimate a nonlinear map (drift function) between RTs of both datasets by weighted spline regression, which allows us to filter unlikely matches from the coupling matrix to obtain a refined coupling matrix $Π^$ (Figure 1d, Materials and methods). An optional thresholding step removes matches with small weights from the coupling matrix. The final output of GromovMatcher is a binary matching matrix $M$ where $M_{ij}$ is equal to 1 if features $fx_{i}$ and $fy_{j}$ are matched and 0 otherwise. Throughout the paper, we refer to the two variants of GromovMatcher, with and without the optional thresholding step as GMT and GM respectively.

### Validation on ground-truth data

We first evaluate the performance of GromovMatcher using a real-world untargeted metabolomics study of cord blood across 499 newborns containing 4712 metabolic features characterized by their $m/z$, RT, and feature intensities (Alfano et al., 2020). To generate ground-truth data, we randomly divide the initial dataset into two smaller datasets sharing a subset of features (Figure 2). We simulate diverse acquisition conditions by adding noise to the $m/z$ and RT of dataset 2, and to the feature intensities in both datasets. Moreover, we introduce an RT drift in dataset 2 to replicate the retention time variations observed in real LC-MS experiments (Materials and methods). For comparison, we also test M2S (Climaco Pinto et al., 2022) and metabCombiner (Habra et al., 2021), both of which use $m/z$, RT, and median or mean feature intensities to match features (Figure 3). MetabCombiner is supplied with 100 known shared metabolic features to automatically set its hyperparameters, while M2S parameters are manually fine-tuned to optimize the F1-score in each scenario (Appendix 2). We assess the performance of GM, GMT, metabCombiner, and M2S across 20 randomly generated dataset pairs in terms of their precision (fraction of true matches among the detected matches) and recall/sensitivity (fraction of true matches detected) averaged across 20 dataset pairs.

![Figure 2.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig2-v1.jpg)

**Figure 2.:** (a) Initial LC-MS dataset taken from the EXPOsOMICS project with $m/z$, RT, and feature intensities of $p=4,712$ metabolites identified in cord blood across $n=499$ newborns. (b) Newborns (rows) are split into two disjoint groups of sizes $n_{1}=249$ and $n_{2}=250$ respectively and metabolic features (columns) are split into two equal groups of size $p_{1}=p_{2}$ with overlap $\lambdap$ where $\lambda=0.25,0.5,0.75$ (Materials and methods). Datasets are perturbed by additive noise of magnitude $(\sigma_{M},\sigma_{RT},\sigma_{FI})$ and a nonlinear drift $f⁢(x)$ is applied to the RTs of dataset 2. (c) The two resulting datasets share $\lambda=25%,50%$, or 75% of the original dataset’s metabolic features.

![Figure 3.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig3-v1.jpg)

**Figure 3.:** (a) Ground-truth matchings, and matchings inferred by metabCombiner, M2S, GM, and GMT. Pairs of datasets are generated for three levels of overlap (low, medium and high), with a medium noise level (Materials and methods). Matches correctly recovered (true positives) are represented in green. True matches that are not recovered (false negatives) are highlighted in grey. Incorrect matches (false positives) are plotted in red. Features in rows and columns of matching matrices are reordered for visual clarity. (b) Average precision and recall on 20 randomly generated pairs of datasets, for three levels of overlap (low, medium, and high) with a medium noise level.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Average precision and recall obtained on simulated data, with fixed overlap $\lambda=0.5$.The noise level corresponds to different values of $\sigma_{RT}$ and $\sigma_{FI}$. High, medium, and low noise level correspond to $(\sigma_{RT},\sigma_{FI})=(0.2,0.1),(0.5,0.5)$ and (1, 1) respectively. We run 20 simulations for each setting.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The feature intensities of both datasets are centered and scaled to have means of 0 and standard deviations of 1. The average precision and recall of the three methods are computed on 20 randomly generated pairs of datasets, for (a) three levels of overlap (low, medium and high corresponding to $\lambda=0.25,0.5$ and 0.75, respectively) with a medium noise level ($(\sigma_{RT},\sigma_{FI})=(0.5,0.5)$), and (b) fixed medium overlap ($\lambda=0.5$) and three different noise levels (low, medium and high corresponding to $(\sigma_{RT},\sigma_{FI})=(0.2,0.1),(0.5,0.5)$ and (1, 1) respectively).

To investigate how the number of shared features affects dataset alignment, we generate pairs of LC-MS datasets with low, medium, and high feature overlap (25%, 50%, and 75%), while maintaining a medium noise level (Materials and methods). Here, we find that GM and GMT generally outperform existing alignment methods, with a recall above 0.95 while metabCombiner and M2S tend to be less sensitive (Figure 3b). All methods drop in precision as the feature overlap is decreased, with GM and GMT still maintaining an average precision above 0.8.

Next we evaluate all four methods at low, moderate, and high noise levels for pairs of datasets with 50% overlap in their features (Materials and methods). Our results show that GMT, GM, and M2S maintain an average recall above 0.89, while metabCombiner’s recall drops below 0.6 for high noise. At large noise levels, RT drift estimation becomes more challenging, leading to a higher rate of false matches between metabolites (lower precision) for all four methods (Figure 3—figure supplement 1). Nevertheless, GMT obtains a high average precision and recall of 0.86 and 0.92, respectively.

A notable difference between GM, metabCombiner, and M2S lies in their use of feature intensities. MetabCombiner expects that the mean feature intensity rankings are identical across studies, while M2S assumes that shared features have similar median intensities. In contrast, GM uses both the mean feature intensities and their variances and covariances. In practice, differences in experimental assays or study populations can lead to greater variation in feature intensities, making matchings based on these statistics less reliable. Centering and scaling the feature intensities to unit variance avoids potential biases arising from inconsistent feature intensity magnitudes, but preserves correlations that GM leverages.

Exploring this further, we test how sensitive all four methods are to centering and scaling of feature intensities. MetabCombiner and M2S are tuned using the same methodology as for non-centered and non-scaled data. For M2S, we match features solely based on their $m/z$ and RT. In this experiment (Figure 3—figure supplement 2), the absence of intensity magnitude information significantly affects metabCombiner’s performance and, to a lesser extent, M2S. GM and GMT still obtain accurate matchings, due to their use of correlation structures which are preserved under centering and scaling.

### Application to EPIC data

Next, we apply GM, metabCombiner and M2S to align datasets from the European Prospective Investigation into Cancer and Nutrition (EPIC) cohort, a prospective study conducted across 23 European centers. EPIC comprises more than 500,000 participants who provided blood samples at recruitment (Riboli et al., 2002). Untargeted metabolomics data were successively acquired in several studies nested within the full cohort.

In the present work, we use LC-MS data from the EPIC cross-sectional (CS) study (Slimani et al., 2003) and two matched case-control studies nested within EPIC, on hepatocellular carcinoma (HCC; Stepien et al., 2016; Stepien et al., 2021) and pancreatic cancer (PC; Gasull et al., 2019). LC-MS untargeted metabolomic data were acquired at the International Agency for Research on Cancer, making use of the same platform and methodology (Materials and methods). The number of samples and features in each study is displayed in Figure 4a.

![Figure 4.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig4-v1.jpg)

**Figure 4.:** (a) Dimensions of the three EPIC studies used. For each ionization mode, the cross-sectional (CS) study is aligned successively with the hepatocellular carcinoma (HCC) study and the pancreatic cancer (PC) study. (b) Demonstration of expert manual matching and GromovMatcher (GM) matching between the CS and HCC studies in positive mode. Experts manually match 90 features (Table 1) from Loftfield et al., 2021 and the correlation matrices of these features in both datasets have similar structure (bottom two matrices). GM discovers 996 shared features between the CS and HCC datasets which have similar correlation structure (top two matrices). We validate that 88 of the 90 features from the manually expert matched subset are contained in the set of features matched by GM. (c) Performance of metabCombiner (mC), M2S and GM in positive mode. Precisions and recalls are measured on a validation subset of 163 manually examined features, and 95% confidence intervals are computed using modified Wilson score intervals. (d) Performance of mC, M2S, and GM in negative mode. Precision and recall are measured on a validation subset of 42 manually examined features, and 95% confidence intervals are computed using modified Wilson score intervals. See Table 2 and Table 3 for exact precisions, recalls, and confidence intervals in positive and negative mode, respectively.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Each scatter plot represents the mean feature intensities of manually matched features from the validation subset. Each dot represents a pair of manually matched features. The axis represent the mean feature intensities recorded in the two different studies.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Venn diagrams are not up to scale.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** Each dot correspond to a candidate matched pair after the first step of GM ($m/z$ constrained GW matching), before the RT drift estimation and RT-based filtering.

Loftfield et al., 2021 previously matched features from the CS, HCC, and PC studies in EPIC for alcohol biomarker discovery. The authors first identified 205 features (163 in positive and 42 in negative mode) associated with alcohol intake in the CS study. These features were then manually matched by an expert to features in both the HCC and PC studies (Materials and methods, Table 1). In our analysis, we use these features as a validation set and compare each method’s matchings to the expert manual matchings on this subset. Due to the imbalance between the number of positive and negative mode features in the validation subset, our main analysis focuses on the alignment results of CS with HCC and CS with PC in positive mode (Table 2). We delegate the matching results between the negative mode studies (Table 3) to Appendix 4.

**Table 1.**
 Results from the manual matching conducted for Loftfield et al., 2021.Features from the CS study (163 features in positive mode, 42 features in negative mode) were manually investigated for matches in the HCC and PC studies.


<table>
  <thead>
    <tr>
      <th>Study</th>
      <th>Manual matches found in positive mode</th>
      <th>Manual matches found in negative mode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hepatocellular carcinoma (HCC)</td>
      <td>90</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Pancreatic cancer (PC)</td>
      <td>66</td>
      <td>28</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Precision and recall on the EPIC validation subset in positive mode.95% confidence intervals were computed using modified Wilson score intervals (Brown et al., 2001; Agresti and Coull, 1998).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">CS⟷HCC</th>
      <th colspan="2">CS⟷PC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Method</td>
      <td>Precision</td>
      <td>Recall</td>
      <td>Precision</td>
      <td>Recall</td>
    </tr>
    <tr>
      <td>GromovMatcher</td>
      <td>0.989 (0.939, 0.999)</td>
      <td>0.978 (0.923, 0.996)</td>
      <td>0.903 (0.813, 0.952)</td>
      <td>0.985 (0.919, 0.999)</td>
    </tr>
    <tr>
      <td>M2S</td>
      <td>0.967 (0.908, 0.991)</td>
      <td>0.978 (0.923, 0.996)</td>
      <td>0.855 (0.759, 0.917)</td>
      <td>0.985 (0.919, 0.999)</td>
    </tr>
    <tr>
      <td>metabCombiner</td>
      <td>0.961 (0.868, 0.993)</td>
      <td>0.544 (0.442, 0.643)</td>
      <td>0.967 (0.833, 0.998)</td>
      <td>0.439 (0.326, 0.559)</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Precision and recall on the EPIC validation subset in negative mode.95% confidence intervals were computed using modified Wilson score intervals (Brown et al., 2001; Agresti and Coull, 1998).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">CS⟷HCC</th>
      <th colspan="2">CS⟷PC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Method</td>
      <td>Precision</td>
      <td>Recall</td>
      <td>Precision</td>
      <td>Recall</td>
    </tr>
    <tr>
      <td>GromovMatcher</td>
      <td>0.950 (0.764, 0.997)</td>
      <td>1.000 (0.832, 1.000)</td>
      <td>0.929 (0.774, 0.987)</td>
      <td>0.929 (0.774, 0.987)</td>
    </tr>
    <tr>
      <td>M2S</td>
      <td>1.000 (0.824, 1.000)</td>
      <td>0.947 (0.754, 0.997)</td>
      <td>0.931 (0.780, 0.988)</td>
      <td>0.964 (0.823, 0.998)</td>
    </tr>
    <tr>
      <td>metabCombiner</td>
      <td>0.875 (0.529, 0.993)</td>
      <td>0.368 (0.191, 0.590)</td>
      <td>1.000 (0.845, 1.000)</td>
      <td>0.750 (0.566, 0.873)</td>
    </tr>
  </tbody>
</table>

In this section, we use the same settings for GM as in our simulation study, and do not apply an additional thresholding step. The parameters of metabCombiner and M2S are calibrated using the validation subset as prior knowledge (Appendix 2).

Preliminary analysis of the validation subset reveals inconsistencies in the mean feature intensities (Figure 4—figure supplement 1), but Figure 4b shows that on centered and scaled data, the 90 expert matched features shared between the CS and HCC studies have similar correlation structures. Hence, to avoid potential errors we center and scale the feature intensities which improves the performance of all three methods tested below (Appendix 4, Appendix 4—table 1).

#### Hepatocellular carcinoma

Here, we analyze the quality of the matchings obtained by GM, M2S, and metabCombiner between the CS and HCC datasets in positive mode. Both GM and M2S identify approximately 1000 shared features while metabCombiner finds a smaller number of about 700 shared features. We refer the reader to Figure 4—figure supplement 2a for the precise matched feature sizes and details on the agreement between the feature matchings of all three methods.

We evaluate the performance of metabCombiner, M2S, and GM on the validation subset in positive mode (Figure 4c, Table 2), which consist of 90 features from the CS study manually matched to features from the HCC study and 73 features specific to the CS study. MetabCombiner demonstrates precise matching but lacks sensitivity. M2S’s precision and recall are comparable with GM, in contrast to its performance on simulated data. This can be attributed to the RT drift shape between the CS and HCC studies (Appendix 2), which is estimated to be close to linear (Figure 4—figure supplement 3). Because the parameters of M2S are fine-tuned in the validation subset, it is able to learn this linear drift and apply tight RT thresholds to achieve accurate matchings. In contrast to metabCombiner and M2S, the GM algorithm is not given any prior knowledge of the validation subset, and nevertheless demonstrates the highest precision and recall rates of the three methods (Figure 4c). Figure 4b shows how GM recovers the majority of the expert matched pairs by leveraging the shared correlations.

#### Pancreatic cancer

Matching features between the CS and PC studies in positive mode, GM and M2S identify approximately 1000 common features, while metabCombiner detects approximately 600 matches (Figure 4—figure supplement 2b). We examine the performance of all three methods on the validation subset consisting of 66 manually matched features between CS and PC along with 97 features specific to the CS study. As before, GM and M2S have high recall while the recall of metabCombiner is less than 0.5.

A decrease in precision is observed for both GM and M2S compared to the previous CS-HCC matchings. We therefore manually inspect the false positive matches; the set of CS features matched by the method to the PC study but explicitly examined and left unmatched in the expert manual matching. Assessing the GM results, we identify seven false positive feature matches. Upon secondary inspection, three pairs are revealed as correct matches that were not initially identified in the expert matching. M2S finds 11 false positive matches which include the 7 false positives recovered by GM. Manual examination of the four remaining pairs reveals two clear mismatches. These results highlight the advantage of using automated methods for data alignment, as both GM and M2S detect correct matches that were not identified by experts, with GM being more precise than M2S.

#### Illustration for alcohol biomarker discovery

Loftfield et al., 2021 identified biomarkers of habitual alcohol intake by first performing a discovery step, where they examined the relationship between alcohol intake and metabolic features in the CS study. They then manually matched the significant features in CS to features from the HCC and PC studies, and repeated the analysis with samples from the HCC and PC studies to determine whether the association with alcohol intake persisted. This led to the identification of 10 features possibly associated with alcohol intake (Figure 5a).

![Figure 5.](https://cdn.elifesciences.org/articles/91597/elife-91597-fig5-v1.jpg)

**Figure 5.:** (a) Loftfield study implemented a discovery step, examining the relationship between alcohol intake and metabolic features in the CS study. The significant features in CS were manually matched to features from the HCC and PC and the analysis was repeated using samples from the HCC and PC studies. After this step, 10 features associated with alcohol intake were identified. (b) GromovMatcher analysis begins by matching features from CS study to HCC and PC studies respectively (top blue, yellow, and red boxes). Samples corresponding to each CS feature are combined with the samples of its matched feature in the HCC study, PC study, or both. This generates a larger pooled data matrix with the same number of features as the CS study but with more samples pooled across the three original studies (center matrix). Because some features in the CS study may not have matches in HCC or PC, the corresponding entries in the pooled matrix are set to NaN/missing values (white regions in matrix). Each column/feature in this matrix is statistically tested for association with alcohol intake (ignoring missing values) and an FDR or a stricter Bonferroni correction is performed to retain only a subset of features from the pooled study that have a strong association. (c) Venn diagrams show intersection of feature sets (in positive and negative mode) found to be associated with alcohol intake by one of the four different analyses.

To extend this analysis and illustrate the benefit of GM automatic matching for biomarker discovery, we use GM to pool features from the CS, HCC, and PC studies, and examine the relationship between metabolic features and alcohol intake in the pooled study (Materials and methods and Figure 5b).

Applying an FDR correction on the pooled study, we identify 243 features associated with alcohol intake, including 185 features consistent with the discovery step of Loftfield et al., 2021, and 55 newly discovered features (Figure 5c). Using the more stringent Bonferroni correction on the pooled data, we identify 36 features shared by all three studies that are significantly associated with alcohol intake. These features include all 10 features identified in Loftfield et al. (Figure 5c). These findings highlight the potential benefits of using GM automatic matching for biomarker discovery in untargeted metabolomics data. Additional information regarding the methodology and findings of our GM and Loftfield et al. analyses can be found in Materials and methods and Appendix 4.

## Discussion

LC-MS metabolomics has emerged as an increasingly powerful tool for biological and biomedical research, offering promising opportunities for epidemiological and clinical investigations. However, integrating data from different sources remains challenging. To address this issue, we introduce GromovMatcher, a method based on optimal transport that automatically aligns LC-MS data from pairs of studies. Our method exhibits superior performance on both simulated and real data when compared to existing approaches. Additionally, it presents a user-friendly interface with few hyperparameters.

While GromovMatcher is robust to noise and variations in data, it may face limitations when aligning LC-MS studies from populations with different characteristics, where the correlation structures between features may be inconsistent across studies. In this case, the base assumption of GromovMatcher can be relaxed by focusing on subsamples with similar characteristics, as exemplified in a recent study (Gomari et al., 2022).

A current limitation is that GromovMatcher does not account for more than two datasets simultaneously, although this can be overcome by aligning multiple studies to a chosen reference dataset, as demonstrated in our biomarker experiments. The extension of Gromov-Wasserstein to multiple distributions (Beier et al., 2022) is another promising approach for generalizing GromovMatcher to multiple dataset alignment. Further improvements can be made by incorporating existing knowledge about the studies being matched, such as known shared features, samples in common, or MS/MS data.

The results obtained from GromovMatcher are highly promising, opening the door for various analyses of metabolomic datasets acquired in different experimental laboratories. Here, we demonstrated the potential of GromovMatcher in expediting the combination and meta-analysis of data for biomarker and metabolic signature discovery. The matchings learned by GromovMatcher also allow for comparison between experimental protocols by assessing the drift in $m/z$, RT, and feature intensities across studies. Finally, inter-institutional annotation efforts can directly benefit from incorporating this method to transfer annotations between aligned datasets. Bridging the gap between otherwise incompatible LC-MS data, GromovMatcher enables seamless comparison of untargeted metabolomics experiments.

## Materials and methods

### GromovMatcher method overview

GromovMatcher accepts as input two feature tables from separate LC-MS untargeted metabolomics studies. Each feature table for dataset 1 and dataset 2 consists of $n_{1},n_{2}$ biospecimen samples respectively and $p_{1},p_{2}$ metabolic features respectively detected in the study. Features in dataset 1 are given the label $fx_{i}$ for $i=1,…,p_{1}$. Every feature is characterized by a mass-to-charge ratio ($m/z$) denoted by $m_{i}^{x}$, a retention time (RT) denoted by $RT_{i}^{x}$, and a vector of intensities across all samples written as $X_{i}\inℝ^{n_{1}}$. Similarly, features in dataset 2 are labeled as $fy_{j}$ for $j=1,…,p_{2}$ and are characterized by their $m/z$, retention time $RT_{j}^{y}$, and a vector of intensities across all samples $Y_{i}\inR^{n_{2}}$.

Our goal is to identify pairs of indexes $(i,j)$ with $i\in{1,…,p_{1}}$ and $j\in{1,…,p_{2}}$, such that $fx_{i}$ and $fy_{j}$ correspond to the same metabolic feature. More formally, we aim to identify a matching matrix $M\in{0,1}^{p_{1}\timesp_{2}}$ such that $M_{ij}=1$ if $fx_{i}$ and $fy_{j}$ correspond to the same feature, hereafter referred to as matched features. Otherwise, we set $M_{ij}=0$.

Because the $m/z$ and RT values of metabolomic features are often noisy and subject to experimental bias, our matching algorithm leverages metabolite feature intensities $X_{i},Y_{j}$ to produce accurate dataset alignments. The GromovMatcher method is based on the idea that signal intensities of the same metabolites measured in two different studies should exhibit similar correlation structures, in addition to having compatible $m/z$ and RT values. Here, we define the Pearson correlation for vectors $u,v\inR^{n}$ as

$$
corr(u,v)=\frac{⟨u−u¯,v−v¯⟩}{‖u−u¯‖‖v−v¯‖}
$$

where we define

$$
u¯=\frac{1}{n}\sumi=1nu_{i},‖u‖=\sqrt{\sumi=1nu_{i}^{2}},⟨u,v⟩=\sumi=1nu_{i}v_{i}
$$

as the mean value, Euclidean norm and inner product respectively. If measurements $X_{i},Y_{j}$ correspond to the same underlying feature, and similarly, measurements $X_{k},Y_{l}$ share the same an underlying feature, we expect that

$$
corr(X_{i},X_{k})≈corr(Y_{j},Y_{l}).
$$

This idea that the feature intensities of shared metabolites have the same correlation structure in both datasets also holds more generally for distances, under a suitable choice of distance. For example, the correlation coefficient $corr(u,v)$ can be turned into a dissimilarity metric by defining

$$
d^{cos}(u,v)=\sqrt{1−corr(u,v)}
$$

commonly referred to as the cosine distance. Preservation of feature intensity correlations then trivially amounts to the preservation of cosine distances.

Another classical notion of distance between vectors $u,v\inR^{n}$ is the normalized Euclidean distance

$$
d^{euc}(u,v)=\frac{1}{\sqrt{n}}‖u−v‖=\sqrt{\frac{1}{n}\sumi=1n(u_{i}−v_{i})^{2}}
$$

which is equal to the cosine distance (up to constants) when the vectors $u,v$ are centered and scaled to have zero mean and a standard deviation of one. The Euclidean distance depends on the magnitude or mean intensity of metabolic features, and hence is a useful metric for matching metabolites as long as these mean feature intensities are reliably collected.

To summarize, the main tenant of GromovMatcher is that if measurements $X_{i},Y_{j}$ correspond to the same feature and $X_{k},Y_{l}$ correspond to the same feature, then for suitably chosen distances $d_{x}:R^{n_{1}}\timesR^{n_{1}}→R$ and $d_{y}:ℝ^{n_{2}}\timesℝ^{n_{2}}→ℝ$, these distances are preserved

$$
d_{x}(X_{i},X_{k})≈d_{y}(Y_{j},Y_{l})
$$

across both datasets. In this paper, the distances $d_{x},d_{y}$ are taken to be the normalized Euclidean distances in Equation 5. We take care to specify those experiments where the metabolic features $X$ and $Y$ are centered and scaled. In these cases, implicitly the Euclidean distance between normalized feature vectors becomes the cosine distance Equation 4 between the original (unnormalized) feature vectors.

#### Unbalanced Gromov–Wasserstein

The goal of GromovMatcher is to learn a matching matrix $M\in{0,1}^{p_{1}\timesp_{2}}$ that gives an alignment between a subset of metabolites in both datasets. However, searching over the combinatorially large set of binary matrices would be an inefficient approach for dataset alignment. The mathematical framework of optimal transport Peyré and Cuturi, 2019 instead enlarges this space of binary matrices to the set of coupling matrices with real nonnegative entries $Π\inR_{+}^{p_{1}\timesp_{2}}$. The entries $Π_{i⁢j}$ with large weights indicate that feature $fx_{i}$ in dataset 1 and feature $fy_{j}$ in dataset 2 are a likely match. Taking inspiration from Equation 6, we minimize the following objective function

$$
E(Π)=\sumi,k=1p_{1}\sumj,l=1p_{2}Π_{ij}Π_{kl}|d_{x}(X_{i},X_{k})−d_{y}(Y_{j},Y_{l})|
$$

to estimate the coupling matrix $Π$.

A standard approach is to optimize this objective over all coupling matrices $Π$ under exact marginal constraints $Π⁢𝟏_{p_{2}}=\frac{1}{p_{1}}⁢𝟏_{p_{1}},Π^{T}⁢𝟏_{p_{1}}=\frac{1}{p_{2}}⁢𝟏_{p_{2}}$. Here, we define $1_{n}$ is the ones vector of length $n$, and $Π_{1}=Π1_{p_{2}},Π_{2}=Π^{T}1_{p_{1}}$ denote the column and row sums of the coupling matrix. Objective Equation 7 under these exact marginal constraints defines a distance between the two sets of metabolic feature vectors ${X_{i}}_{i=1}^{p_{1}},{Y_{i}}_{i=1}^{p_{2}}$ known as the Gromov–Wasserstein distance Mémoli, 2011, a generalization of optimal transport to metric spaces. Note that for pairs $X_{i},Y_{j}$ and $X_{k},Y_{l}$ for which $d_{x}(X_{i},X_{k})≈d_{y}(Y_{j},Y_{l})$, the entries $Π_{i⁢j},Π_{k⁢l}$ are penalized less and hence matches between features $fx_{i},fy_{j}$ and features $fx_{k},fy_{l}$ are more favored. In our optimization, we avoid enforcing exact marginal constraints on the marginal distributions $Π1_{p_{2}}$ and $Π^{T}⁢𝟏_{p_{1}}$ of our coupling matrix as this would enforce that all metabolites in both datasets are matched (Appendix 1). However, without any marginal constraints on the coupling $Π$, the objective function Equation 7 is trivially minimized by $Π=0$, leaving all metabolites in both datasets unmatched.

To account for this, we follow the ideas of unbalanced Gromov–Wasserstein (UGW) (Sejourne et al., 2021) and add three regularization terms to our objective

$$
L_{ρ,\epsilon}(Π)=E(Π)+ρD_{KL}(Π_{1}⊗Π_{1},a⊗a)+ρD_{KL}(Π_{2}⊗Π_{2},b⊗b)+\epsilonD_{KL}(Π⊗Π,(a⊗b)^{⊗2})
$$

where $ρ,\epsilon>0$ and we define $a=1_{p_{1}},b=1_{p_{2}}$. Here ⊗ denotes the Kronecker product. We define $D_{KL}$ as the Kullback–Leibler (KL) divergence between two discrete distributions $\mu,ν\inℝ_{+}^{p}$ by

$$
D_{KL}(\mu,ν)=\sumi=1p\mu_{i}ln⁡(\frac{\mu_{i}}{ν_{i}})−\sumi=1p\mu_{i}+\sumi=1pν_{i}
$$

which measures the closeness of probability distributions.

The first two regularization terms in Equation 8 enforce that the row sums and column sums of the coupling matrix $Π$ do not deviate too much from a uniform distribution, leading our optimization to match as many metabolic features as possible. The magnitude of the regularizer $ρ$ roughly enforces the fraction of metabolites in both datasets that are matched where large $ρ$ implies most metabolites are matched across datasets. The final regularization term $\epsilon$ in Equation 8 controls the smoothness (entropy) of the coupling matrix $Π$ where larger values of $\epsilon$ encourage $Π$ to put uniform weights on many of its entries, leading to less precision in the metabolite matches. However, increasing $\epsilon$ also leads to better numerical stability and a significant speedup of the alternating minimization algorithm used to optimize the objective function (Appendix 1). In our implementation, we set $ρ$ and $ϵ$ to the lowest possible values under which our optimization converges, with $ρ=0.05$ and $ϵ=0.005$.

Our full optimization problem can now be written as

$$
UGW_{ρ,\epsilon}=minΠ\inR_{+}^{p_{1}\timesp_{2}}L_{ρ,\epsilon}(Π).
$$

The UGW objective function is optimized through alternating minimization based on the code of Sejourne et al., 2021 using the unbalanced Sinkhorn algorithm Séjourné et al., 2019 from optimal transport (Appendix 1).

#### Constraint on m/z ratios

Matched metabolic features must have compatible $m/z$ so we enforce that $Π_{i⁢j}=0$ when $|m_{i}^{x}−m_{j}^{y}|>m_{gap}$ where $m_{gap}$ is a user-specified threshold. Based on prior literature (Loftfield et al., 2021; Hsu et al., 2019; Climaco Pinto et al., 2022; Habra et al., 2021; Chen et al., 2021), we set  $m_{gap}$ = 0.01 ppm. Note that $m_{gap}$ is not explicitly used in Equation 10 but is rather enforced in each iteration of our alternating minimization algorithm for the UGW objective (Appendix 1).

Unlike the $m/z$ ratios discussed above, RTs often exhibit a non-linear deviation (drift) between studies so we cannot enforce compatibility of RTs directly in our optimization. Instead, in the following step of our pipeline we ensure matched metabolite pairs have compatible RTs by estimating the drift function and subsequently using it to filter out metabolite matches whose RT values are inconsistent with the estimated drift.

#### Estimation of the RT drift and filtering

Estimating the drift between RTs of two studies is a crucial step in assessing the validity of metabolite matches and discarding those pairs which are incompatible with the estimated drift.

Let $Π~\inR_{+}^{p_{1}\timesp_{2}}$ be the minimizer of Equation 10 obtained after optimization. We seek to estimate the RT drift function $f:ℝ_{+}→ℝ_{+}$ which relates the retention times of matched features between the two studies. Namely, if feature $fx_{i}$ and feature $fy_{j}$ correspond to the same metabolic feature, then we must have that $RT_{j}^{y}≈f(RT_{i}^{x})$.

We propose to learn the drift $f$ through the weighted spline regression

$$
minf\inB_{n,k}\sumi=1p_{1}\sumj=1p_{2}Π~_{ij}|f(RT_{i}^{x})−RT_{j}^{y}|
$$

where $B_{n,k}$ is the set of $n$-order B-splines with $k$ knots. All pairs $(R⁢T_{i}^{x},R⁢T_{j}^{y})$ in objective Equation 11 are weighted by the coefficients of $Π~$ so that larger weights are given to pairs identified with high confidence in the first step of our procedure. The order of the B-splines was set to $n=3$ by default, while the number of knots $k$ was selected by 10-fold cross-validation.

Pairs identified as incompatible with the estimated RT drift are then discarded from the coupling matrix. To do this, we first take the estimated RT drift $f^$, and the set of pairs $S={i,j:Π~_{i,j}\neq0}$ recovered in $Π~$. We then define the residual associated with $(i,j)\inS$ as

$$
r_{f^}(i,j)=|f^(RT_{i}^{x})−RT_{j}^{y}|.
$$

The 95% prediction interval and the median absolute deviation (MAD) of these residuals are given by

$$
PI=1.96\timesstd({r_{f^}(i,j),(i,j)\inS})MAD=median({|r_{f^}(i,j)−\mu_{r}|,(i,j)\inS})\mu_{r}=median({|r_{f^}(i,j)|,(i,j)\inS})
$$

where $|𝒮|$ is the size of $𝒮$ and the functions std and median denote the standard deviation and median respectively. Similar to the approach in Climaco Pinto et al., 2022, we create a new filtered coupling matrix $Π^\inℝ_{+}^{p_{1}\timesp_{1}}$ given by

$$
Π^_{ij}={Π~_{ij}if r_{f^}(i,j)<\mu_{r}+r_{thresh}0otherwise.
$$

where $r_{thresh}$ is a given filtering threshold. Following Habra et al., 2021, the estimation and outlier detection step can be repeated for multiple iterations, to remove pairs that deviate significantly from the estimated drift and improve the robustness of the drift estimation. In our main algorithm, we use two preliminary iterations where estimate the RT drift and discard outliers outside of the 95% prediction interval by setting $r_{thresh}=PI$. We the re-estimate the drift and perform a final filtering step with the more stringent MAD by setting $r_{thresh}=2\timesMAD$.

At this stage, it is possible for $Π^$ to still contain coefficients of very small magnitude. As an optional postprocessing step, we discard these coefficients by setting all entries smaller than $\tau⁢max⁢(Π^)$ to zero, for some user-defined $\tau\in[0,1]$. Lastly, a feature from either study could have multiple possible matches, since $Π^$ can have more than one non-zero coefficient per row or column. Although reporting multiple matches can be helpful in an exploratory context, for the sake of simplicity in our analysis, the final output of GromovMatcher returns a one-to-one matching, as we only keep those metabolite pairs $(i,j)$ where the entry $Π^_{i⁢j}$ is largest in its corresponding row and column. All nonzero entries of $Π^$ which do not satisfy this criterion are set to zero. Finally, we convert $Π^$ into a binary matching matrix $M\in{0,1}^{p_{1}\timesp_{2}}$ with ones in place of its nonzero entries and this final output is returned to the user.

As a naming convention, we use the abbreviation GM for our GromovMatcher method, and use the abbreviation GMT when running GromovMatcher with the optional $\tau$-thresholding step with $\tau=0.3$.

### Metrics for dataset alignment

Every alignment method studied in this paper returns a binary partial matching matrix $M\in{0,1}^{p_{1}\timesp_{1}}$ which has at most one nonzero entry in each row and column. Specifically, $M_{i⁢j}=1$ if metabolic features $i$ and $j$ in both datasets correspond to each other and $M_{i⁢j}=0$ otherwise. In our simulated experiments, we compare the partial matching $M$ to a known ground-truth partial matching matrix $M^{*}\in{0,1}^{p_{1}\timesp_{2}}$.

To do this, we first compute the number of true positives, false positives, true negatives, and false negatives as

$$
TP=\sumi=1p_{1}\sumj=1p_{2}1_{M_{ij}=1}1_{M_{ij}^{∗}=1}FP=\sumi=1p_{1}\sumj=1p_{2}1_{M_{ij}=1}1_{M_{ij}^{∗}=0}TN=\sumi=1p_{1}\sumj=1p_{2}1_{M_{ij}=0}1_{M_{ij}^{∗}=0}FN=\sumi=1p_{1}\sumj=1p_{2}1_{M_{ij}=0}1_{M_{ij}^{∗}=1}
$$

where 1 denotes the indicator function. Then we use these values to compute the precision and recall as

$$
Precision=\frac{TP}{TP+FP}Recall=\frac{TP}{TP+FN}.
$$

Precision measures the fraction of correctly found matches out of all discovered metabolite matches, while recall, also know as sensitivity, measures the fraction of correctly matched pairs out of all truly matched pairs. These two statistics can be summarized into one metric called the F1-score by taking their harmonic mean

$$
F1=2⋅\frac{Precision⋅Recall}{Precision+Recall}
$$

These three metrics, precision, recall, and the F1-score, are used throughout the paper to assess the performance of dataset alignment methods, both on simulated data where the ground-truth matching is known, and on the validation subset in EPIC, using results from the manual examination as the ground-truth benchmark.

### Validation on simulated data

To assess the performance of GromovMatcher and compare it to existing dataset alignment methods, we simulate realistic pairs of untargeted metabolomics feature with known ground-truth matchings. This allows us to analyze the dependence of alignment methods on the number of shared metabolites, dataset noise level, and feature intensity centering and scaling.

#### Dataset generation

Our pairs of synthetic feature tables are generated from one real untargeted metabolomics study of 500 newborns within the EXPOsOMICS project, which uses reversed phase liquid chromatography-quadrupole time-of-flight mass spectrometry (UHPLC-QTOF-MS) system in positive ion mode Alfano et al., 2020. The original dataset is first preprocessed following the procedure detailed in Alfano et al., 2020, resulting in p=4712 features measured in $n=499$ samples available for subsequent analysis. Features and samples from the original study are then divided into two feature tables of respective size $(n_{1},p_{1})$ and $(n_{2},p_{2})$, with $n_{1}+n_{2}=n$ and $p_{1},p_{2}\leqp$. In order to do this, $n_{1}=⌊n/2⌋$ randomly chosen samples from the original study are placed into dataset 1 and the remaining $n_{2}=⌈n/2⌉$ samples from the original study are placed into dataset 2. Here, $⌊⋅⌋$ and $⌈⋅⌉$ denote integer floor and ceiling functions. The features of the original study are randomly assigned to dataset 1, dataset 2, or both, allowing the resulting studies to have both common and study-specific features (Figure 2). Specifically, for a fixed overlap parameter $\lambda\in[0,1]$, we assign a random subset of $≈\lambda⁢p$ features into both dataset 1 and dataset 2 while the remaining $≈(1-\lambda⁢p)$ features are divided equally between the two studies such that $p_{1}=p_{2}$. We choose $\lambda\in{0.25,0.5,0.75}$ corresponding to low, medium and high overlap. For more detailed information on how the dataset split is performed and for additional validation experiments with unbalanced dataset splits (e.g. $n_{1}\neqn_{2},p_{1}\neqp_{2}$) we refer the reader to Appendix 3.

After generating a pair of studies, random noise is added to the $m/z$, RT and intensity levels of features in dataset 2 to mimic variations in data acquisition across two different experiments. The noise added to each $m/z$ value in study 2 is sampled from a uniform distribution on the interval $[-\sigma_{M},\sigma_{M}]$ with $\sigma_{M}=0.01$ (Climaco Pinto et al., 2022). The RTs of dataset 2 are first deviated by the function $f⁢(x)=1.1⁢x+1.3⁢sin⁡(1.2⁢\sqrt{x})$, corresponding to a systematic inter-dataset drift (Habra et al., 2021; Climaco Pinto et al., 2022; Brunius et al., 2016). A uniformly distributed noise on the interval $[-\sigma_{RT},\sigma_{RT}]$ is added to the deviated RTs of dataset 2, with $\sigma_{RT}\in{0.2,0.5,1}$ (in minutes) corresponding to low, moderate and high variations (Climaco Pinto et al., 2022; Habra et al., 2021; Vaughan et al., 2012). Finally, we add a Gaussian noise $𝒩⁢(0,\sigma_{FI}^{2})$ to the feature intensities of both studies where $\sigma_{F⁢I}$ is the scalar variance of the noise. This noise perturbs the correlation matrices of dataset 1 and dataset 2, making matching based on feature intensity correlations more challenging. We vary $\sigma_{F⁢I}$ over the set of values {0.1, 0.5, 1}.

Given this data generation process, we test the performance of the four alignment methods (M2S, metabCombiner, GM, and GMT) under the parameter settings described below.

#### Dependence on overlap

We first assess how the performance of the four methods is affected by the number of metabolic features shared in both datasets. For each value of $\lambda=0.25,0.5,0.75$ (low, medium, and high overlap), we randomly generate 20 pairs of datasets with noise on the $m/z$, RT and feature intensities set to $\sigma_{M}=0.01,\sigma_{RT}=0.5,\sigma_{FI}=0.5$. The precision and recall of each method at low, medium, and high overlap is recorded for each of the repetitions.

#### Noise robustness

Next, we test the robustness to noise of each method by fixing the metabolite overlap fraction at $\lambda=0.5$ and generating 20 random pairs of datasets at low ($\sigma_{RT}=0.2,\sigma_{FI}=0.1$), medium ($\sigma_{RT}=0.5,\sigma_{FI}=0.5$), and high ($\sigma_{RT}=1,\sigma_{FI}=1$) noise levels. Similarly, the precision and recall of each method is saved for each noise level across the 20 repetitions.

#### Feature intensity centering and scaling

In order to test how all four methods are affected when the mean feature intensities and variance are not comparable across studies, we assess their performance when the feature intensities in both studies are mean centered and standardized to have unit standard deviation across all samples. We again generate 20 random pairs of datasets with medium overlap and medium noise, normalize the feature intensities in each pair of datasets, and compute the precision and recall of each method across the 20 repetitions.

### EPIC data

We also evaluate our method on data collected within the European Prospective Investigation into Cancer and Nutrition (EPIC) cohort, an ongoing multicentric prospective study with over 500,000 participants recruited between 1992 and 2000 from 23 centers in 10 European countries, and who provided blood samples at the inclusion in the study (Riboli et al., 2002). In EPIC, untargeted metabolomics data were successively acquired in several studies nested within the full cohort.

In the present work, we use untargeted metabolomics data acquired in three studies nested in EPIC, namely the EPIC cross-sectional (CS) study (Slimani et al., 2003) and two matched case-control studies nested within EPIC, on hepatocellular carcinoma (HCC; Stepien et al., 2016; Stepien et al., 2021) and pancreatic cancer (PC; Gasull et al., 2019), respectively. All data were acquired at the International Agency for Research on Cancer, making use of the same plateform and methodology: UHPLC-QTOF-MS (1290 Binary Liquid chromatography system, 6550 quadrupole time-of-flight mass spectrometer, Agilent Technologies, Santa Clara, CA) using reversed phase chromatography and electrospray ionization in both positive and negative ionization mode.

In a previous analysis aiming at identifying biomarkers of habitual alcohol intake in EPIC, the 205 features associated with alcohol intake in the CS study were manually matched to features in both the HCC and PC studies Loftfield et al., 2021. The results from this manual matching are presented in Table 1. This matching process was based on the proximity of $m/z$ and RT, using a matching tolerance of ± 15 ppm and ± 0.2 min, and on the comparison of the chromatograms of features in a quality control samples from both studies.

#### Preprocessing

In the HCC and PC studies, samples corresponding to participants selected as cases in either study (i.e. participants selected in the study because of a diagnosis of incident HCC or PC) are excluded. Indeed, the metabolic profiles of participants selected as controls are expected to be more comparable across studies than those of cases, especially if certain features are associated with the risk of HCC or PC. Apart from this additional exclusion criterion, the untargeted metabolomics data of each study is pre-processed following the steps described in Loftfield et al., 2021, to eliminate unreliable features and samples, impute missing values and minimize technical variations in the feature intensity levels.

#### Alcohol biomarker discovery

Loftfield et al., 2021 used the untargeted metabolomics data of the CS, HCC and PC studies in their alcohol biomarker discovery study in EPIC, without being able to automatically match their common features and pool the three datasets. Instead, the authors first implemented a discovery step, examining the relationship between alcohol intake and metabolic features measured in the CS study and accounting for multiple testing using a false discovery rate (FDR) correction. This led to the identification of 205 features significantly associated with alcohol intake in the CS study. In order to gauge the robustness of these associations, the authors of Loftfield et al., 2021 then implemented a validation step using data from two independent test sets. The first test set was composed of data from the EPIC HCC and PC studies, while the second was derived from the Finnish Alpha-Tocopherol, Beta-Carotene Cancer Prevention (ATBC) study. The 205 features identified in the discovery step were manually investigated for matches in the EPIC test set, and 67 features were effectively matched to features in the HCC or PC study, or both. The authors then evaluated the association between alcohol intake and those 67 features, applying a more conservative Bonferroni correction to determine whether the association with alcohol intake persisted. This step led to the identification of 10 features associated with alcohol intake (Extended Data Figure 5a). The second test set was then used to determine whether those 10 features were also significant in the ATBC population, which was indeed the case.

To conduct a more in-depth investigation of the matchings produced by the GromovMatcher algorithm, we build upon the analysis previously conducted by Loftfield et al., 2021 by exploring potential alcohol biomarkers using a pooled dataset created from the CS, HCC, and PC studies. Our goal is to assess whether pooling the data leads to increased statistical power and allows for the detection of more features associated with alcohol intake. Namely, we generate the pooled dataset by aligning a chosen reference dataset (CS study) with the HCC and PC studies successively using the GM matchings computed in both positive and negative mode (Materials and methods and Extended Data Figure 5b). Features that are not detected in either the HCC or PC studies are designated as ‘missing’ in the final pooled dataset for samples belonging to the respective studies where the feature is not found.

To evaluate the potential relationship between alcohol consumption and pooled metabolic features, we use a methodology akin to that of Loftfield et al., 2021. The self-reported alcohol intake data is adjusted for various demographic and lifestyle factors (age, sex, country, body-mass-index, smoking status and intensity, coffee consumption, and study) via the residual method in linear regression models. Feature intensities are also adjusted for technical variables (plate number and position within the plate) via linear mixed effect models. The significance of the association is assessed using correlation coefficients computed from the residuals for both self-reported alcohol intake and feature intensities. p-Values are corrected using either false discovery rate (FDR) or Bonferroni correction to account for multiple testing. Corrected p-values less than 5% are considered significant.

### Materials and correspondence

All correspondence and material requests should be addressed to V.V.

### IARC disclaimer

Where authors are identified as personnel of the International Agency for Research on Cancer/World Health Organization, the authors alone are responsible for the views expressed in this article and they do not necessarily represent the decisions, policy, or views of the International Agency for Research on Cancer/World Health Organization.
