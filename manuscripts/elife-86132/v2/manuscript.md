# Digital wearable insole-based identification of knee arthropathies and gait signatures using machine learning

## Authors

- Matthew F Wipperman<sup>1</sup> ([ORCID: 0000-0003-1436-3366](https://orcid.org/0000-0003-1436-3366)) †
- Allen Z Lin<sup>3</sup> ([ORCID: 0000-0001-5105-308X](https://orcid.org/0000-0001-5105-308X))
- Kaitlyn M Gayvert<sup>3</sup> ([ORCID: 0000-0001-9135-6501](https://orcid.org/0000-0001-9135-6501))
- Benjamin Lahner<sup>1</sup>
- Selin Somersan-Karakaya<sup>2</sup>
- Xuefang Wu<sup>4</sup>
- Joseph Im<sup>4</sup>
- Minji Lee<sup>3</sup>
- Bharatkumar Koyani<sup>4</sup>
- Ian Setliff<sup>3</sup>
- Malika Thakur<sup>4</sup>
- Daoyu Duan<sup>1</sup>
- Aurora Breazna<sup>5</sup>
- Fang Wang<sup>1</sup>
- Wei Keat Lim<sup>3</sup> ([ORCID: 0000-0002-6226-2570](https://orcid.org/0000-0002-6226-2570))
- Gabor Halasz<sup>3</sup>
- Jacek Urbanek<sup>5</sup>
- Yamini Patel<sup>6</sup>
- Gurinder S Atwal<sup>3</sup>
- Jennifer D Hamilton<sup>1</sup>
- Samuel Stuart<sup>4</sup>
- Oren Levy<sup>2</sup>
- Andreja Avbersek<sup>2</sup>
- Rinol Alaj<sup>4</sup> †
- Sara C Hamon<sup>1</sup> †
- Olivier Harari<sup>2</sup> ([ORCID: 0000-0001-8214-489X](https://orcid.org/0000-0001-8214-489X)) †

### Affiliations

1. Precision Medicine, Regeneron Pharmaceuticals Inc Tarrytown United States ([ROR:02f51rf24](https://ror.org/02f51rf24))
2. Early Clinical Development & Experimental Sciences, Regeneron Pharmaceuticals Inc Tarrytown United States ([ROR:02f51rf24](https://ror.org/02f51rf24))
3. Molecular Profiling & Data Science, Regeneron Pharmaceuticals Inc Tarrytown United States ([ROR:02f51rf24](https://ror.org/02f51rf24))
4. Clinical Outcomes Assessment and Patient Innovation, Global Clinical Trial Services, Regeneron Pharmaceuticals Inc Tarrytown United States ([ROR:02f51rf24](https://ror.org/02f51rf24))
5. Biostatistics and Data Management, Regeneron Pharmaceuticals Inc Tarrytown United States ([ROR:02f51rf24](https://ror.org/02f51rf24))
6. General Medicine, Regeneron Pharmaceuticals Inc Tarrytown United States ([ROR:02f51rf24](https://ror.org/02f51rf24))

† Corresponding author

## Abstract

Gait is impaired in musculoskeletal conditions, such as knee arthropathy. Gait analysis is used in clinical practice to inform diagnosis and monitor disease progression or intervention response. However, clinical gait analysis relies on subjective visual observation of walking as objective gait analysis has not been possible within clinical settings due to the expensive equipment, large-scale facilities, and highly trained staff required. Relatively low-cost wearable digital insoles may offer a solution to these challenges. In this work, we demonstrate how a digital insole measuring osteoarthritis-specific gait signatures yields similar results to the clinical gait-lab standard. To achieve this, we constructed a machine learning model, trained on force plate data collected in participants with knee arthropathy and controls. This model was highly predictive of force plate data from a validation set (area under the receiver operating characteristics curve [auROC] = 0.86; area under the precision-recall curve [auPR] = 0.90) and of a separate, independent digital insole dataset containing control and knee osteoarthritis subjects (auROC = 0.83; auPR = 0.86). After showing that digital insole-derived gait characteristics are comparable to traditional gait measurements, we next showed that a single stride of raw sensor time-series data could be accurately assigned to each subject, highlighting that individuals using digital insoles can be identified by their gait characteristics. This work provides a framework for a promising alternative to traditional clinical gait analysis methods, adds to the growing body of knowledge regarding wearable technology analytical pipelines, and supports clinical development of at-home gait assessments, with the potential to improve the ease, frequency, and depth of patient monitoring.

## Introduction

Gait assessment plays several roles in clinical practice and research for many musculoskeletal and orthopedic diseases, such as diagnosis, guiding treatment selection, and measuring intervention response. (Lord et al., 1998). Knee osteoarthritis (OA) contributes to altered gait as individuals try to avoid knee pain and cartilage contact stress (i.e., weight shift or joint loading onto the non-affected limb) (Iijima et al., 2019; Kaufman et al., 2001). Those with knee OA commonly have increased lateral trunk lean toward the ipsilateral limb, along with non-significantly increased trunk/pelvic flexion and resultant significant alterations in external hip adduction moments (Iijima et al., 2019). Clinically, gait is examined in knee OA through clinical visual observation of walking, which is subjective and dependent on expertise. Beyond visual observation, gait has been traditionally objectively assessed in specialized gait laboratories with expensive equipment, such as force platforms, with or without a motion-tracking system. However, gait laboratories are generally not available or feasible within clinical settings due to cost, need for highly trained staff to operate equipment, and the size of equipment. Wearable sensors offer an alternative approach to assessment of gait in those with knee OA (Mills et al., 2013) as they can be deployed within any environment or setting (Stern et al., 2022), are relatively low-cost, and can provide outcomes automatically without the need for highly experienced or trained staff.

Vertical ground reaction force (vGRF) is a gait characteristic that is impaired within knee OA as it relates to the bilateral weightbearing capabilities of the patient (i.e., greater peak vGRF) (Creaby et al., 2013; Davis et al., 2019; Trentadue et al., 2021). Traditionally, vGRF is objectively examined using force plates, which can provide three components of force (vertical, anterior-posterior, and medio-lateral) (Creaby et al., 2013; Davis et al., 2019; Trentadue et al., 2021). Force plate signals can provide information on gait characteristics, postural stability, as well as direction, strength, and duration of stance phase (Arslan et al., 2019; Whittle, 2007). However, force plates only capture intermittent data on vGRF (single or several steps) within controlled experiments that do not represent real-world overground walking. Technological development has led to digital insoles (wearables) that can capture vGRF and other gait characteristics that are relevant to knee OA assessment, which could be used within free-living environments (Stern et al., 2022). The data generated from digital insoles may allow for phenotyping information to characterize patients with knee OA. However, clinical application of wearable digital insoles for gait analysis in knee OA is limited by a paucity of analytical validation data (including face, criterion, and construct validity), such as comparison of gait outcome measures in those with knee OA to ‘gold-standard’ laboratory references (e.g., force plate outcomes) (Goldsack et al., 2020; Rochester et al., 2020).

Gait quantitation generates dense raw sensor time-series data with nonlinear relationships that make analysis and interpretation challenging. As a class, digital gait data analysis pipelines suffer from a lack of well-established analytical methods compared to other biomarker data types (Wipperman et al., 2022; Crouthamel et al., 2021; Horst et al., 2019). Recently, there is interest in developing more streamlined (‘light-weight’) gait algorithms and data processing pipelines using machine learning (ML) to automate and process large volumes of novel digital data obtained from wearable devices (Celik et al., 2022; Godfrey et al., 2018). An ML framework may be used as a tool to evaluate the digital gait outcome quality and consistency, as well as how well these data can be used as potential clinical trial endpoints. Selection of the appropriate modeling modalities for a particular clinical question is challenging (Horst et al., 2019; Slijepcevic et al., 2022). The selection of classical ML versus deep learning methods may be influenced by the structure and size of the data. For example, deep learning models are better suited to handle high-throughput, multimodal data streams, such as raw sensor time series (Alias, 2018; Briouza et al., 2021), but typically require larger datasets than classical statistical or ML methods (in terms of both features and sample size). Finally, clinical wearable data may be collected over several seconds to minutes, and longer in passive monitoring settings; thus, appropriate understanding of large dataset processing is important. Collectively, both data type, size, and model selection are key components of a comprehensive wearable sensor data analysis pipeline and should be considered when evaluating clinical research pipelines with large heterogeneous datasets.

This study aimed to assess the face validity of measuring vGRF using digital insoles compared to the standard laboratory reference of force plates in control adults and those with knee arthropathy. We also aimed to clinically validate the measurement of gait with digital insoles in those with knee arthropathy through (1) development of a novel ML framework (based on ‘gold-standard’ force plate data) for application within digital insoles to detect knee arthropathy status and (2) processed digital insole-derived gait outcomes and raw sensor signals to identify disease-specific gait patterns in knee arthroscopy. Clinical validity is the ability to provide clinically meaningful outcome measures, including the detection of disease-specific patterns relative to controls, and the identification of subject-specific gait patterns.

## Results

### Platform-agnostic visualization of knee arthropathy signatures from vGRF data

vGRF is the major and clinically relevant component of the ground reaction forces generated from walking and can be measured using force plates or digital insoles. We obtained vGRF data from the three studies: the GaitRec Force Plate study of subjects with knee injuries (N = 625) and controls (N = 211) and two digital insole studies in controls (N = 22) and subjects with knee OA (N = 40), respectively (Figure 1, Figure 2—figure supplement 1). We plotted raw and normalized vGRF values recorded by force plate and digital insole devices and observed by visual inspection that the means of vGRF curves within each disease category are similar across platforms (Figure 2A), which highlights face validity of the digital insoles (i.e., the insole data appeared similar to the force plate data). Furthermore, we observed distinct patterns between control subjects and those with knee arthropathy when comparing the normalized vGRF values averaged by group (Figure 2A) or per individual (Figure 2B). Specifically, individuals with knee arthropathy from all evaluated datasets displayed a qualitatively different gait signature than controls, with a ‘flatter’ vGRF curve shape during the middle of stance phase (we use the term ‘arthropathy’ to encompass both knee injury and OA).

![Figure 1.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig1-v2.jpg)

**Figure 1.:** (A) Three datasets were used for analyses. The GaitRec force plate dataset (force plate data) contains N = 211 controls, who walked at three different walking speeds (slow, comfortable, and fast), and N = 625 knee injury subjects, who walked at a comfortable walking speed (Horsak et al., 2020). The second dataset is from a digital insole pilot study, where N = 22 controls walked at three different walking speeds (slow, comfortable, and fast). The third dataset is from a digital insole sub-study from a longitudinal clinical trial in knee osteoarthritis (OA), where N = 40 knee OA subjects performed a 3 min walk test (3MWT) at a comfortable walking speed at baseline (pretreatment) and at day 85 (on treatment). (B) Both force plates and digital insoles produce data collected during stance and swing phases of a person’s gait cycle. (C) Types of data produced by these devices include vertical ground reaction force (vGRF), derived gait characteristics, and raw sensor time series. (D) Clinical research questions addressed in this work include the derivation of gait disease signatures of knee OA and investigation of the individuality and consistency of gait patterns. Two analytical methods were used to evaluate these data. Support vector machine (SVM) models were used to analyze vGRF, derived gait characteristics, and raw sensor time-series flattened stride data. A one-dimensional convolutional neural network (CNN) was used to analyze structured stride raw sensor time-series data.

![Figure 2.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig2-v2.jpg)

**Figure 2.:** (A) Vertical ground reaction force (vGRF) curves derived from force plate and digital insole data for controls, and knee injury and knee OA patients, respectively. Left foot data are shown as mean of values (top panels) and mean of normalized z-scores (bottom panels) at each percent stance phase within each device and health status. Groups are color-coded as in (B) and (C). (B) vGRF curves for an individual’s left foot shown as heatmap rows, after data was z-transformed at each percent stance phase (as in A). Rows are hierarchically clustered within each group of subjects. (C) Uniform Manifold Approximation and Projection (UMAP) dimensionality reduction of the z-transformed left foot vGRF data. Each point represents a subject, and points are colored by phenotype, and shaped by device. (D) Schematic of machine learning model building of training/validation and testing sets. Two support vector machine (SVM) models were created, one for left knee injury (depicted) and one for right knee injury. The full force plate vGRF dataset with both controls (comfortable walking speed) and left or right knee injury subjects (comfortable walking speed, excluding subjects with knee injury on both joints) were split 85% into training/validation datasets, and 15% into a hold-out testing set. One model predicts control versus knee injury subjects using left foot data (of left knee injury subjects and all controls), and the other predicts using right foot data (of right knee injury subjects and all controls). These models were then applied on a separate, independent testing set of digital insoles vGRF data with N = 22 control subjects and N = 38 patients with knee OA. (E) Receiver operating characteristic curve for SVM classification of force plate (85%) cross-validation (CV, training/validation) set, force plate (15%) hold-out test set, and the digital insole test set. (F) Precision-recall curve for SVM classification of the same groups in (E).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Data are z-scored by each column (% stance phase) across all walks. Heatmaps are separate by injury class (control, knee, calcaneus, hip, and ankle), and vGRF from each walk are unsupervised clustered within each category. The right of the heatmap annotates the joint side with the arthropathy (left joint, right joint, both joints, or no injury in the control group).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Linear models were fit at each % stance phase (timepoint), excluding the edges of the curve which are bounded by 0 (and as such have no variance). We used disease (knee arthropathy or control), age, sex (male or female), and body weight as covariates in the model, with each subsequent vGRF % stance phase timepoint as the dependent variable. Within each linear model, using the sum of squares for each category compared to the total sum of squares, we calculated of the variance each component’s contribution to the total variance, with the residuals indicating the unexplained variance in these models. We observed that the disease state is the major contributor to vGRF for most of the curve, with age, sex, and body weight also explaining a smaller proportion of the variance.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Schematic of machine learning model building of training/validation and testing sets with the right foot data, as in Figure 2. (B) Receiver operating characteristic curve for support vector machine (SVM) classification of force plate (85%) cross-validation (CV, training/validation) set, force plate (15%) hold-out test set, and the digital insole test set for right foot data. (C) Precision-recall curve for SVM classification of the same groups in (B) for right foot data.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Force plate repeated cross-validation (CV) set with 85% of the training/validation data, force plate test set with 15% of the observations, and the Moticon digital insole independent test set (see ‘Methods’). We evaluated three models: logistic regression, support vector machine (SVM), and XGBoost modeling approaches, as well as SVM with shuffled labels for comparison. This was repeated 100 times. The top row shows the area under the curve for the precision-recall (top) and ROC (bottom) curves, plotted in a box-and-whisker plot. (B) Precision-recall curves for all three models. (C) ROC curves for all three models.

Using a dimension reduction approach Uniform Manifold Approximation and Projection (UMAP) with normalized vGRF data from each subject in two dimensions, subjects at a population level separated out by arthropathy status (knee arthropathies vs controls) rather than by measurement platform (Figure 2C). Thus, despite performing analysis on data collected from different devices at different sites, we could discern disease-relevant patterns in the vGRF data and show that the digital insole data recapitulated the force plate data.

To investigate how the variation in the vGRF data may be partially explained by the clinical and demographic characteristics of the participants, we fit a series of linear models to each point along the vGRF curve, with arthropathy state (knee arthropathy or control), age, sex (male or female), and body weight as covariates in the model (Figure 2—figure supplement 2). For each linear model, representing the sum of squares for each category compared to the total sum of squares as a percentage of variation explained by that component, we observed that the arthropathy state is the major contributor to the vGRF signal for most of the vGRF curve, with age, sex, and body weight explaining a smaller proportion of the variance. We conclude that the dominant factor likely contributing to variation among participants to these signals is arthropathy state.

### ML models trained on vertical ground reaction force plate data to classify control versus knee injury across different platforms

We next looked to quantify how well force plate data can identify disease using gait signatures and to understand if a wearable insole could detect similar characterizations. To differentiate controls versus knee arthropathies using vGRF data, we divided the complete vGRF force plate dataset into a training/validation set (85%) and a test set (15%) and trained a support vector machine (SVM) model to predict these classes (Figure 2D). The model indicated strong predictive power to classify control versus knee injury subjects using force plate data when evaluated using fivefold cross-validation of the training/validation dataset, a standard method of assessing model performance (left knee: area under the receiver operating characteristics curve [auROC] = 0.92 [SD = 0.03], area under the precision-recall curve [auPR] = 0.94 [SD = 0.03]; right knee: auROC = 0.94 [SD = 0.02], auPR = 0.96 [SD = 0.01]). The predictive power was also strong when assessed on the hold-out test dataset, which was not used for training of the SVM model (left knee: auROC = 0.95, auPR = 0.95; right knee: auROC = 0.93, auPR = 0.95) (Table 1 and Figure 2—figure supplement 3).

**Table 1.**
 Force plate vertical ground reaction force (vGRF) control versus knee arthropathies support vector machine (SVM) classification model evaluation statistics (left foot/right foot).An SVM model was trained on 85% of the force plate dataset vGRF data to predict control or knee arthropathies (knee injury or knee osteoarthritis) classes, with left foot vGRF data used to predict left knee arthropathies and right foot vGRF data used to predict right knee arthropathies. The model was evaluated using fivefold cross-validation, a hold-out force plate test set, and a digital insole test set. Area under the receiver operating characteristics curve (auROC) and area under the precision-recall curve (auPR) statistics are reported for the three models. F1 scores for each class for each model are also reported.


<table>
  <thead>
    <tr>
      <th rowspan="3">Per class binary classification metrics</th>
      <th rowspan="2" colspan="2">auROC actual/mean (SD)</th>
      <th rowspan="2" colspan="2">auPR actual/mean (SD)</th>
      <th colspan="4">F1 score</th>
    </tr>
    <tr>
      <th colspan="2">Control</th>
      <th colspan="2">Arthropathy</th>
    </tr>
    <tr>
      <th>Left</th>
      <th>Right</th>
      <th>Left</th>
      <th>Right</th>
      <th>Left</th>
      <th>Right</th>
      <th>Left</th>
      <th>Right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Force plate fivefold cross validation</td>
      <td>0.917 (0.034)</td>
      <td>0.937 (0.023)</td>
      <td>0.944 (0.029)</td>
      <td>0.960 (0.015)</td>
      <td>0.78</td>
      <td>0.84</td>
      <td>0.87</td>
      <td>0.88</td>
    </tr>
    <tr>
      <td>Force plate test set</td>
      <td>0.949</td>
      <td>0.935</td>
      <td>0.955</td>
      <td>0.950</td>
      <td>0.78</td>
      <td>0.76</td>
      <td>0.87</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>Digital insole test set</td>
      <td>0.928</td>
      <td>0.925</td>
      <td>0.937</td>
      <td>0.938</td>
      <td>0.89</td>
      <td>0.83</td>
      <td>0.95</td>
      <td>0.90</td>
    </tr>
  </tbody>
</table>

_SD, standard deviation._

To further assess generalizability of the model and understand if a digital insole could measure vGRF similarly to a force plate, we applied the model trained using vGRF force plate data to the separate, independent dataset derived from digital insole studies on individuals with knee OA and controls. An important assumption of this analysis was that knee OA and knee injury are represented similarly by vGRF curves as was shown earlier (Figure 1A–C). We found that for the digital insole an SVM model trained only on force plate data performed as well on the digital insole data (left knee: auROC = 0.93, auPR = 0.94; right knee: auROC = 0.93, auPR = 0.94) as it did on the hold-out force plate test data (Figure 2E and E; Table 1, and Figure 2—figure supplement 3).

### Performance of derived gait characteristics of the digital insole versus vGRF and raw sensor time series for disease classification

A potential benefit of a digital insole relative to a force plate is that many more variables can be derived, thus enabling a more comprehensive assessment of gait. For instance, in addition to the vGRF curves, derived gait characteristics and raw sensor time-series data can be obtained using the 50 sensors across both insoles (Figure 3A).

![Figure 3.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of raw sensor time-series data from a digital insole. Data can be processed from the device in three ways: (1) vertical ground reaction forces (Figure 1); (2) derived gait characteristics on force, spatio-temporal, and center of pressure aspects; and (3) raw sensor time-series data from the 50 sensors embedded across both insoles. Each segmented stride of raw sensor time-series data can be analyzed as is (structured strides) or collapsed (flattened strides). (B) The derived gait characteristics (parameters) of the digital insole from all individuals in the pilot study were correlated against each other at the comfortable walking speed. Spearman correlation coefficients were computed and shown in a correlation matrix ranging from –1 (perfect anti-correlation) to +1 (perfectly correlation). Each parameter has a Spearman correlation coefficient of +1 with itself (red diagonal). The parameter, the foot from which it was generated, and its category are labeled on the left of the correlation matrix. (C) Heatmap representation of the average of each of the 82 digital insole parameters (rows) across all walks for each patient (columns) from the pilot study. Parameter values are shown as normalized z-scores (bounded within ± 3), calculated across all participants, and walking speeds. The heatmap is split by the three walking speeds (slow, normal, fast), and columns are clustered within each walking speed using hierarchical clustering with Euclidean distances. The 14 parameters strongly correlated with walking speed are indicated on the right of the heatmap.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Left: boxplots in knee OA, control slow, comfortable, and fast walking speeds for some parameters predictive of knee OA versus controls. Right: scatter plots of select parameters in control versus knee OA subjects at comfortable walking speed.

Time-series data measures different aspects of a stride, including force, angular velocity, and orientation of the foot relative to gravity. The raw sensor time-series data can be evaluated as either structured strides, in which each stride is represented such that each sensor’s values are measured over time, or converted into flattened strides, in which all timepoints and sensors are concatenated into one representation (Figure 3A) providing a linear representation of a person’s stride.

To investigate how derived gait characteristics relate to each other, we clustered the values and their correlations across different walking speeds and disease status (OA vs control). Correlations within and between categories of parameters revealed that similar groups of parameters clustered together (Figure 3B), including 14 derived gait characteristics strongly correlating with walking speed (|Spearman rho| > 0.7). We note that many other gait characteristics will be influenced by walking speed, and as such, we call out these as representing the subset most influenced by speed, defined by this threshold (|Spearman rho| > 0.7). Using a heatmap, where derived gait characteristics were normalized across both control and knee OA populations, we observed distinct patterns between derived gait characteristics at different walking speeds and disease status (Figure 3C). To further explore the relationship with walking speed, we performed a principal component analysis (PCA) dimensionality reduction on each data type. This analysis demonstrated that knee OA arthropathy state can be observed on a continuum related to walking speed. Compared to control subjects, participants with knee OA are walking more slowly as apparent across all data types, including vGRF (Figure 4A), derived gait characteristics (Figure 4B), and raw sensor time-series data (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig4-v2.jpg)

**Figure 4.:** (A) Principal component analysis (PCA) dimensionality reduction of vertical ground reaction force (vGRF) data from all walks of pilot study subjects and baseline walks of knee OA clinical trial patients. Each dot represents data from a single subject at a given walking speed. (B) PCA dimensionality reduction of derived gait characteristic data from the digital insole, without the 14 speed-correlated derived gait characteristics. (C) PCA dimensionality reduction of raw sensor time series of each stride from all walks. Each dot represents data from a single stride and repeat strides from the same participant are shown. (D) Receiver operating characteristic curves for knee OA versus control (both at comfortable walking speed) prediction using only walking speed (speed), derived gait characteristics (excluding 14 speed-correlated features), raw sensor time series, and vGRF. Classification metrics were derived using leave-one-out cross-validation (LOOCV). The single derived gait characteristic speed separates out digital insole knee OA patients versus control subjects. (E) Precision-recall curves of the same comparisons in (D). (F) Classification accuracy using raw sensor time-series data from control subjects versus knee OA patients using subsets or all 50 sensors at each timepoint of the stride (0–100% of the stride). Timepoints start with the stance phase of the right foot and swing phase of the left foot, and end with the swing phase of the right foot and the stance phase of the left foot. Classification accuracy of 1.0 indicates perfect knee OA versus control classification using data from that timepoint.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Principal component analysis (PCA) of all derived gait characteristics measured using the Moticon insole device, where each point represents the average of all walks from a particular subject, and the dot color indicates the group (control or knee osteoarthritis [OA]) or walking speed of control subjects. (B) PCA as in (A), without the walking speed gait characteristic. (C) PCA as in (A), without the 14 derived gait characteristics correlated to walking speed. (D) Classification performance area under the receiver operating characteristics curve (auROC) using walking speed as a sole predictor, vertical ground reaction force (vGRF) data, derived gait characteristics, and time-series data. (E) Precision-recall curve for classification as in (D).

We revisited the question of whether gait data can be used to identify arthropathy status relative to control subjects for each of the three types of data collected by the digital insole: vGRF, summary parameters, and time-series data. Note that this analysis aims to classify whether a subject has knee arthropathy, rather than to determine the severity of arthropathy, which this study was not designed to assess. SVM models were trained on vGRF and assessed using both repeated five-fold cross-validation (r5FCV) and leave-one-out cross-validation (LOOCV), where models were evaluated by iteratively leaving one subject out, building a model, and evaluating where that subject would be classified compared to the true result (see ‘Methods’). This was also performed for derived gait characteristics, and raw sensor time-series (flattened strides) data independently (Figure 4D and E). Additionally, we used walking speed as a single variable predictor of knee OA (both control subjects and OA patients had been asked to walk at a self-paced comfortable walking speed). We found that walking speed alone was able to discriminate between knee OA subjects and controls (auROC = 0.981, auPR = 0.983). vGRF with the digital insole also demonstrated high predictive power (LOOCV: auROC = 0.984, auPR = 0.990; r5FCV: auROC = 0.988, auPR = 0.992).

For derived gait characteristics, we wanted to understand whether aspects of gait other than walking speed could be used to correctly classify whether a subject had knee OA relative to a control as this would suggest potential for broader applicability if disease-specific features in addition to changes in speed could be detected with digital insoles. Using derived gait characteristics that excluded the 14 characteristics strongly correlated to walking speed, we found even better classification accuracy (LOOCV: auROC = 0.997, auPR = 0.988; r5FCV: auROC = 0.996, auPR = 0.986). The most important discriminating parameters included takeoff dynamics, max force (N), mean COP velocity (mm/s), and gait line-associated parameters (sd x and sd y of gait line start point [mm]) (Supplementary file 1, and Figure 3—figure supplement 1). Flattened strides from raw sensor data, which is also independent of walking speed as each stride was interpolated to a consistent 100 timepoints, also were predictive (LOOCV: auROC = 0.997, auPR = 0.998) (Figure 4—figure supplement 1).

Finally, we sought to evaluate the contribution of each sensor at each timepoint along individual segmented strides to the disease classification accuracy. We trained additional SVM models on subsets of sensor type at each timepoint (Figure 4F) and found that classification accuracy for control versus knee OA depends on the type of sensor, the timepoint along a stride, and the foot (left vs right). Measurements of pressure and force from a foot had greater mean classification accuracy during the stance phase of that foot.

### Deriving individual gait signatures using convolutional neural net latent representations of raw sensor time-series data or derived gait characteristics

To determine the extent to which walking patterns are specific to an individual, subjects were split 50:50 into training and testing sets and stratified by disease status (Figure 5A). We then trained a one-dimensional convolutional neural net (CNN) on structured strides of training set individuals and subsequently applied the CNN model on structured strides of testing set individuals. For each stride, we extracted the 60 features in the last connected (penultimate) layer of the CNN (Figure 5B). This layer directly precedes the final output of the CNN model predicting the individual from which the stride came, and thus these 60 features constitute a gait ‘fingerprint’ learned by the CNN model. These features were learned by the CNN to distinguish individuals, and thus these patterns (captured in the latent features) can subsequently be used for classification of new subjects, previously unseen by the model.

![Figure 5.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig5-v2.jpg)

**Figure 5.:** (A) Pilot study subjects and knee osteoarthritis (OA) clinical trial patients were split 50:50 into training and testing sets, stratified by disease status, for the first CNN model investigating the individuality of gait patterns. (B) A CNN was trained on segmented structured strides from the digital insole in the training set, to predict from which subject the stride came. The activation of the last fully connected layer in the CNN consists of 60 features and represents the model’s latent representation of gait. (C) Uniform Manifold Approximation and Projection (UMAP) clustering of these 60 latent features for each stride captures the individuality of participants in both the training and testing sets. Each dot represents a single stride, colors represent each participant, and shapes represent participants’ health status (C = control). Intra- and inter-subject clustering and separation is greater in the training set, as expected, and is present in the testing set as well. (D) Distances (in arbitrary units) between each pair of walks (for derived gait parameters) or strides (for time series) from the testing set shown as heatmaps for each of the three methods (top panels). Subject of the walk/stride are color identified along the edge. Boxplot of mean distance of each walk/stride with other walk/strides from the same individual, and with walk/strides from other individuals separated by disease class (bottom panels). Distances are faceted by the disease class of the individual. A good representation has low distance for ‘with self’, and high distance for ‘with other’ classes.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Color along the edge indicates each person.

To visualize the latent representation of strides from the CNN, a UMAP clustering of these latent features from each stride indicated that this representation captured the individual identity of participants (Figure 5C) as strides from the same individuals clustered together in both the training and testing sets.

We sought to quantify the individuality of each of the three representations of gait: derived gait characteristics from each walk, raw (flattened) time series of each stride, and CNN latent features of each stride. To do so, we calculated the distance between all pairs of test set walks/strides in such representation against each other (see ‘Methods’). These distances are displayed in both heatmaps (Figure 5D, top) and boxplots (Figure 5D, bottom). An ideal representation to quantitate individuality would have low distances between walks/strides from the same person and high distances for between walks/strides from different people (Figure 5—figure supplement 1).

Subjects within their class (control or knee OA) displayed similar gaits; therefore, we separated out comparisons of subjects to their same class versus comparisons to the other class (with other control, with other OA). All three representations had significant differences in distances when comparing strides from the same subjects versus strides from different subjects (p<0.001, t-test). The CNN latent representation was best at minimizing distances of strides from the same subjects while maximizing the distances of strides from different subjects from the same class, as measured by Cohen’s d effect size, suggesting that the CNN latent representations best capture gait individuality, and as such was used for follow-up analysis.

### Evaluation of individual gait signatures after training on raw sensor time series from multiple days

A second CNN model was trained on combined data from both timepoints in the R5069-OA-1849 clinical trial, where input data was labeled only by participant and not by timepoint. We call the first model trained only on day 1 data an ‘individuality’ model, and the second model trained on both day 1 and day 85 a ‘consistency’ model (Figure 6A).

![Figure 6.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig6-v2.jpg)

**Figure 6.:** (A) Knee osteoarthritis (OA) clinical trial participants were split 50:50 into training and testing sets containing both day 1 (baseline) and day 85 (on treatment) data, for the second CNN model investigating the consistency of gait patterns. (B) Distances (in arbitrary units) between pairs of strides in the latent representation from the consistency CNN model in the training and testing sets, shown as heatmaps. Strides from the same person are arranged next to each other, with strides from day 1 listed first then strides from day 85. Color along the edge indicates each person. (C) Boxplots of mean distance of each stride with other strides from the same person on the same day, from the same person on different days, and from other people, for both the individuality model (Figure 5) and consistency model (A–B). Distances are shown using the different models in both the training and testing sets.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/86132/elife-86132-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Values are replotted from Figure 6C, and lines are drawn between the same participants. Significance of difference in distances between the CNN individuality and consistency models was analyzed with paired t-tests.

We tested both models on days 1 and 85 by evaluating the distance of the CNN penultimate layer of all strides with each other. Figure 6B plots the distance for the consistency model on both the training (left) and testing set (right) participants. For each participant, day 1 and 85 strides are arranged next to each other, and the cross-day distance within each participant is shown in squares closest to the diagonal.

Figure 6C shows stride distances for within subject from the same day, within subject from different days, and within other subjects. Within the training set, the consistency model, which was trained on both day 1 and 85 strides, produced lower distances than the individuality model, which was trained on only day 1 strides, in comparing strides within self from different days (p<0.001, paired t-test) (Figure 6—figure supplement 1). Importantly, within the testing set, the consistency model produced lower distances than the individuality model in comparing strides within self from different days (nominal p=0.033, paired t-test), suggesting that training across multiple days improves the ability of the CNN consistency model to identify features that remain consistent across multiple visits. The results also show additional capacity for model improvement with respect to consistency of gait, as in the consistency model, the distances of the data to oneself were lower amongst strides from the same day versus different day in both training and testing participants (nominal p<0.001 and nominal p=0.004, respectively, t-test).

## Discussion

This study investigated whether gait data derived from a wearable digital insole appears to be accurate in comparison to a gold-standard laboratory reference technology (force plates) and whether it can answer questions of clinical interest (with the ultimate clinical goal of yielding useful endpoints). Overall, the digital insoles appeared to have face (analytical) validity for vGRF measurement in knee OA and controls (qualitatively appears to provide similar results to force plate data), and various insole-derived gait outcomes demonstrated early clinical validity as they provided clinically meaningful outcome measures for knee OA.

To address the question of how to estimate disease-specific patterns, we tested whether vGRF data allowed for detection of knee arthropathy relative to control subjects with any device. We built an ML model using force plate vGRF data and tested the model on an independent force plate test dataset. We then extended the analysis to the data from the digital insole. We observed consistent disease versus control differences in vGRF curves with both technologies, such that these models were able to distinguish knee arthropathy subjects from their respective control groups. The predictive performance of the ML model on data collected from a different device at different physical locations and experimental conditions suggests that the model was robust and generalizable (not overfit). While our analysis may be confounded by variables like age, our results imply that disease status is the major signal we observe. Our results suggest that vGRF data likely reflect true differences between control and knee arthropathy subjects, suggesting that digital insoles may be used to screen for knee arthropathy and potentially other diseases that impact gait.

We next sought to identify how different types of digital gait outcomes beyond vGRF (where the digital insole attempts to replicate exactly what is measured on a force plate) can be utilized. To provide additional insight into the advantages of utilizing wearable devices, we investigated alternative data types generated by wearable devices. Findings confirmed that speed-independent gait characteristics play an important role in identifying patients with knee arthropathy and controls. Specifically, evaluation of derived gait characteristics from the digital insole highlighted walking speed as an important determinant of knee OA classification, which is expected (Zeni and Higginson, 2009); however, when derived gait characteristics highly correlated with speed were removed, the model still successfully detected knee OA subjects. Despite walking speed being a prognostic biomarker for mortality and a clinically meaningful outcome measure, it lacks the ability to detect disease-specific impairments or potential improvements with intervention (i.e., speed is the accumulation of other gait characteristics, and more specific gait characteristics can be mapped to specific underlying musculoskeletal, neurological, or cardio-pulmonary impairment) (Morris et al., 2016; Zhou et al., 2022). This highlights that in addition to alterations in speed there are additional gait characteristics in knee OA that differentiate them from controls.

Distinguishing between control and disease subjects, where effect sizes are expected to be large, may have important clinical implications. However, it remains to be seen whether wearable devices can successfully detect disease severity where effect sizes are smaller. Our study was not designed to investigate smaller effect size differences, so future studies are needed to evaluate this further. If future studies show this is feasible, this data would be important to determine disease progression or evaluate the impact of therapeutic interventions, and could have utility in clinical practice, as well as serve as an endpoint tool for clinical trials. A strength of using digital insoles over other lower cost technology (e.g., Inertial Measurement Units, or IMUs) is that they can accurately capture the gait cycle and weight transfer/bearing in OA patients, which was our primary clinical focus here. Unlike IMUs that require algorithms to estimate the initial and final contact of the foot (Paraschiv-Ionescu et al., 2020), digital insoles provide additional information such as the ability to determine when the foot is actually on the ground via raw pressure sensor data, thereby improving the accuracy of gait event detection and proceeding outcomes. This is the reason why digital insoles are often used for analytical validation of IMU algorithms in clinical populations (Mazzà et al., 2021). Although digital insoles may not be as hardwearing as IMUs (i.e., capacitors may deteriorate over time, so are not recommended for free-living assessment) (Vu et al., 2020), they are useful clinical tools for active mobility tasks in an OA population as they provide gait- and pressure-related metrics that are relevant for this clinical condition. Alternatively, in free living settings (e.g., passive monitoring with wearables over hours/days/weeks), digital insoles may have issues with device placement and sensor deterioration (Vu et al., 2020), unlike IMUs that have been shown to be comfortable and have high acceptance across various clinical populations (Keogh et al., 2023). The objectivity of the data also makes these suitable for endpoint tools. For example, derived gait characteristics could represent reliable registrational endpoints in clinical research, given that they describe objective aspects of gait with clinical relevance (e.g., total distance walked in meters, or maximum force applied during a 3 min walk in Newtons).

Finally, evaluation of raw time-series data from digital insoles demonstrated that data from a single stride could identify individual subjects. However, the interpretation of time-series data remains challenging, particularly when analyzed with deep learning methods. In current clinical trial settings, derived gait characteristics may be a simpler approach. Nevertheless, our finding that raw time-series data contain subject-specific latent features suggests that potentially useful gait features, beyond the disease signatures studied here, may exist in this data.

Collecting additional timepoints from individuals may permit the model to learn more consistent subject-specific gait patterns. Individual subject gait patterns have been reported previously (Horst et al., 2019; Horst et al., 2016; Schöllhorn et al., 2002), and understanding their quantification may be useful in clinical development for precision medicine applications. Subject-level gait patterns and the ability to identify unique signatures of an individual’s gait may enable improved monitoring of treatment responses on a per-subject as well as on a population-wide level. Training datasets with participant data from multiple visits improve the ability of the model to detect gait features that remain consistent, or that change, with time. Collection and training on additional timepoints beyond the 2 d in our study may result in models that better learn gait features to consistently identify an individual across time.

This work highlights the potential utility of digital insoles for gait assessment in knee OA. However, the data such devices generate require clear hypothesis-driven validation to detect relevant signals just like research-grade instrumentation. Holistically, by showing that vGRF data from a digital insole replicate the standard clinical data generated from force plates, we demonstrated criterion validity of vGRF data from digital insoles, meaning that digital insoles can to some degree replicate a clinical standard (the criterion). We further demonstrated the external validity within the digital insole study of the disease gait signature across both methodologies (force plate and digital insole) using an ML approach, with a training set built entirely on force plate data and evaluated on both force plate and digital insole data collected elsewhere. Analytical strategies that maximize both clinical understanding and generalizability to other studies are of course standard for biomedical research. However, we go beyond this step, and further attempt an analytical approach to maximize construct validity—how close a digital biomarker reads out the ‘construct’ it is intended to measure—even at the expense of face validity (the degree to which a measure is intuitively interpretable), for a particular clinical question. Here, the fact that raw sensor data lacks face value interpretability but improves upon our ability to ascertain subject-specific gait patterns may inform us that these digital biomarker data contain disease or subject-specific information that could be leveraged in alternative clinical circumstances.

### Study limitations

Limitations of this analysis include the small sample size in the pilot study of controls, in addition to the fact that subjects in this study were not demographically and clinically matched with the OA study. Further, the OA study did not control for knee-only OA on one or both joints, thus making this population heterogeneous and limiting generalizability. Despite this, we were able to show favorable classification performance for these control subjects relative to their force plate counterparts. The study design also did not specifically account for familiarization with the insoles. While this study only looked at knee arthropathies, future work will be focused on a broader set of gait-affecting diseases. The study’s analytical approach, which focused solely on regular walking patterns and excluded outliers and irregular patterns in the insole gait data, may limit the comprehensiveness of the findings; future research should aim to collect more diverse walking data per subject to include nonregular patterns. Additionally, the insoles are currently only capable of providing vGRF outcome measures, but medial and lateral GRF would also be useful outcomes for OA as these also relate to pain and OA severity (Costello et al., 2021). Technology developments would be required to develop a wearable system that would be capable of capturing comprehensive GRFs during walking in OA and should be an area of future research. Only two repeat timepoints were used for subject-level classification in the knee OA group, but we demonstrated a modeling approach to reliably compute an individual’s gait consistency. In the future, this would ideally be performed on data collected at more than two timepoints. In addition, full analytical validation of the digital insoles was not possible as force plate and insole data was not collected simultaneously, and therefore evaluation of criterion and concurrent validity was not possible. Future work should help determine gait outcome measures for accuracy and error.

### Conclusions

This work outlines a framework for an integrated analysis of digital insole data to answer clinical and research questions relevant to digital biomarker development. To identify disease signatures, we built an ML model using only data from force plates, the clinical standard, and analyzing data from a digital insole, we showed comparable disease classification. This platform-agnostic analysis demonstrates that ML approaches can help support and validate digital biomarkers and may yield digital endpoints of clinical utility. In addition, the finding that our models can identify individual gait patterns suggests that data generated from a digital insole may have unforeseen future applications such as the potential to detect changes in individual gait patterns, which may provide better understanding of the impact of a therapeutic intervention for that individual. Ultimately, this work helps support the aspiration that digital technology may provide value in the healthcare delivery setting, aiding in accurate diagnosis or longitudinal monitoring of disease progression or of response to treatment.

## Methods

### Study design

The objectives were to characterize data from a wearable insole device (Moticon), demonstrate their utility relative to a clinical standard, and investigate optimal analytical methods and data types for the analysis relevant to clinical questions of interest. Three datasets were integrated for analysis (Figure 1). The GaitRec force plate vGRF dataset contained force plate control subjects (N = 211) and knee injury subjects (N = 625) (Horsak et al., 2020).

Volunteers were used as control subjects (N = 22) from a pilot study conducted between July 2019 and August 2019 to evaluate the usability of a digital insole to measure gait (Table 2). The date of first visit for the first volunteer in the pilot study was July 6, 2019, and last volunteer was August 5, 2019. Those pregnant or with a body mass index above 40 kg/m2 were excluded from the study. Volunteers were recruited internally within the Regeneron facility located in Tarrytown, NY, and were provided consent prior to participation. The pilot study did not require IRB approval because the research was not subject to the Common Rule (45 CFR Sec 46.104) or FDA regulations and did not meet the definition of ‘Human Research’ under New York law.

**Table 2.**
 Baseline characteristics and gait assessments of subjects in the digital insole pilot study and patients with knee osteoarthritis (OA) in the R5069-OA-1849 clinical trial digital insole sub-study.Note that this table represents the total subjects enrolled with data used in any analysis of this study. Specific Ns are given where relevant and reflect subsets of these subjects.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Controls Pilot study (N=22) Cross-sectional</th>
      <th>Knee osteoarthritis Clinical trial (N=44 enrolled in sub-study, N=43 data collected) Longitudinal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age (years)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Mean</td>
      <td>39</td>
      <td>62.75</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>35</td>
      <td>63</td>
    </tr>
    <tr>
      <td>Range</td>
      <td>19–85</td>
      <td>52–77</td>
    </tr>
    <tr>
      <td>Sex</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Female</td>
      <td>11</td>
      <td>28</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>11</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Body Mass Index (kg/m2)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Mean</td>
      <td>26.2</td>
      <td>34.5</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>26.0</td>
      <td>34.8</td>
    </tr>
    <tr>
      <td>Range</td>
      <td>20.1–37.0</td>
      <td>26.6–38.9</td>
    </tr>
    <tr>
      <td>Arthropathy class</td>
      <td>N/A</td>
      <td>K-L2-3: N=23 K-L4: N=13</td>
    </tr>
    <tr>
      <td>Walk test</td>
      <td>Walk straight for 30 s</td>
      <td>3 min walk test (3MWT)</td>
    </tr>
    <tr>
      <td>Walking speed</td>
      <td>3 speeds (comfortable, fast, slow)</td>
      <td>1 speed (comfortable)</td>
    </tr>
    <tr>
      <td>Number of walk test performed</td>
      <td>~12 times (at each speed)</td>
      <td>1 time at baseline and 1-time on-treatment (day 85)</td>
    </tr>
    <tr>
      <td>Total length of gait evaluation</td>
      <td>20 min</td>
      <td>3 min</td>
    </tr>
  </tbody>
</table>

_K-L, Kellgren–Lawrence._

As part of a clinical trial evaluating the impact of a novel pain therapeutic in moderate to severe knee OA (R5069-OA-1849; NCT03956550), a sub-study of the digital insole was performed to collect data for gait assessment in knee OA patients (results from the clinical trial are published separately) (Somersan-Karakaya et al., 2023). This information is available publicly in the protocol in Section 8.2.6.6, Moticon Digital Insole Device Sub-Study for Gait Assessments. All patients in this sub-study were enrolled at two study sites in the United States and Moldova, and the study was conducted between June 2019 and October 2020. The date of first enrollment in the R5069-OA-1849 trial June 17, 2019, and last patient visit was October 29, 2020. The sub-study targeted to enroll approximately 13 patients per treatment group to obtain data on at least 10 patients per treatment group for a total of approximately 30 patients across the entire sub-study. The treatment groups were as follows: patients were randomized in a 1:1:1 ratio to receive a low dose of REGN5069 at 100 mg IV every 4 weeks (Q4W), and a high dose of REGN5069 at 1000 mg IV Q4W, or matching placebo Q4W. Eligible participants were men and women ≥40 years of age with a clinical diagnosis of OA of the knee based on the American College of Rheumatology criteria with radiological evidence of OA (Kellgren–Lawrence score ≥ 2) at the index knee joint as well as pain score of ≥4 in Western Ontario and McMaster Universities Osteoarthritis Index (WOMAC) pain sub-scale score. The WOMAC score is a self-administered questionnaire consisting of 24 items divided into three subscales, where the pain sub-score is assessed during walking, using stairs, in bed, sitting or lying, and standing upright. The study protocol received Institutional Review Board and ethics committee approvals from Moldova Medicines and Medical Device Agency and National Ethics Committee for Moldova, and the Western Institutional Review Board.

### Study procedures

In the pilot study, each participant walked straight along a hallway with a hard tile floor at three different qualitative speeds for ~12 times at each speed (~36 walks total). For each walking trial, participants wore the digital insole inside their own shoes and were prompted to walk at a normal or comfortable speed, walk fast as if they were in a hurry (fast speed), or walk slow as if they were at leisure (slow speed). Prior to the walking trials, each participant was instructed to practice walking around to get accustomed to the insole. Participants’ clinical and demographic information was also collected prior to walking trials.

In the R5069-OA-1849 clinical trial, a total of N = 44 OA patients were enrolled into a sub-study of a 259-patient clinical trial. Patients were required to bring the same pair of shoes to the study site to perform a 3MWT with the digital insole. Each patient performed the task twice, once at baseline and the other 85 d later post-treatment.

### Equipment

Moticon digital insoles (Moticon Rego AG, Munich, Germany) were used to derive wearable gait outcomes from the participants. Each Moticon digital insole has a total of 25 sensors per foot: 16 vertical plantar pressure sensors that assess force, a trial-axial accelerometer that measures acceleration, and a gyroscope that measures orientation and angular velocity. Each sensor captures data at 100Hz, and dedicated software computes several clinically relevant spatial and temporal-derived gait characteristics comparable to data generated in a gait lab. The Moticon digital insole computes vGRF in the same way as a force plate, generating comparable data outputs. In addition to vGRF data, derived gait characteristics summarizing a subject’s walk and raw sensor time-series data can be obtained.

### vGRF data processing

To normalize the vGRF data across devices (due to the differing sampling frequencies of force plates and Moticon) and subjects, smoothing spline functions (scipy.interpolate.interp1d) were fit to vGRF time-series sensor data from both GaitRec force plate data and Moticon-computed vGRF data. vGRF curves were bounded by 0, and 100 evenly spaced timepoints across the curve were derived for each curve (to derive a % stance phase). All vGRF curves were normalized by participants’ body weight in Newtons. Within each device, the vGRF curves were further normalized using a z-transformation within each stance phase timepoint (Figure 2A).

### Linear models to associate covaraites with vGRF signal

Using the GaitRec force plate dataset, consecutive linear models were fit at each of the 98% stance phase timepoints. We used disease (knee arthropathy or control), age, sex (male or female), and body weight as covariates in the model (linear model (lm) and ANOVA function, R), with each subsequent vGRF % stance phase timepoint as the dependent variable. Within each linear model, using the sum of squares for each category divided by the total sum of squares, we calculated the variance of each component’s contribution to the total variance, with the residuals indicating the unexplained variance in these models. The use of linear models at each of the 98 points during the % stance phase allowed us to examine the relationship between vGRF and the covariates (disease, age, sex, and body weight) at each specific point in time during the stance phase of walking. This is important as the relationship between these variables and vGRF may change throughout the stance phase.

### Digital insole raw sensor time-series data processing

The digital insole collects 25 100-Hz measurements for each foot (50 measurements across both feet), comprising 16 measurements from 16 vertical plantar pressure sensors, 3 x,y,z measurements from an accelerometer, 3 x,y,z measurements from a gyroscope, 1 measurement of total force, and 2 x%,y% measurements of center of pressure. These raw sensor time-series sensor data for both the R5069-OA-1849 clinical study and Regeneron pilot study was preprocessed with custom scripts written in Python 3.6.

For the following analysis, a ‘walk’ was defined as data captured by the digital insole while the subject completed the researcher’s walking task (typical duration of 180 s for the R5069-OA-1849 clinical study and 25 s for the Regeneron pilot study). A ‘stride’ is defined as the data captured by the digital insole between the peak pressure of the right heel (the average of digital insole right pressure 1 and 2 sensors) and the next peak pressure of the right heel. A typical stride duration is 1–2 s, highly dependent on individual walking speed.

Data preprocessing for each subject was performed separately. First, each walk was segmented into individual strides. Since the digital insole did not collect data in regular intervals, each stride was interpolated for each of the 50 sensors to obtain 100 timepoints along the stride. Thus, each interpolated stride consists of 50 vectors (one for each sensor), and each vector is 100 units long.

For the pilot study, walks from each subject were processed individually, treating slow, comfortable, and fast walks separately. Walks without all 50 features and walks with greater than 5% missing data were excluded. For the remaining walks, any missing data was linearly interpolated (scipy.interpolate.interp1d).

Each walk was then segmented into strides, and each stride was interpolated to 100 timepoints. To segment a walk, peaks were identified in the average time series of the Moticon right pressure sensors 1 and 2, located in the right heel using scipy.signal.find_peaks with parameters width = 10 and prominence = 5. The walk was segmented using the peaks, and the number of measurements in each segment was calculated. Segments that had that an outlier number of samples (outliers defined as 1.5 * iqr ± q3 or q1) were excluded, such that only regularly repeating segments, or strides, were analyzed. Each of the 50 features in each stride was then linearly interpolated (scipy.interpolate.interp1d) to 100 time points. Only walks with at least 10 interpolated strides were further analyzed.

Under the assumption that an individual’s strides within a walk should be highly regular to each other, each stride’s Pearson r correlation with the means of the remaining strides was computed (stats.pearsonr), and any strides with an outlier Pearson r correlation (outliers defined as 1.5 * iqr ± q3 or q1) were excluded. This process was then repeated with the remaining strides to obtain a list of the Pearson r coefficients of each stride with the means of the other strides. The entire walk was excluded if the mean of the Pearson r coefficients fell below 0.9. This procedure was repeated one last time, across all walks by an individual at the same walking speed (slow, comfortable, fast). That is, each stride’s Pearson r correlation with the average of remaining strides in all walks at the same speed was computed. Again, assuming strides within a subject and within a given walking speed should be consistent with each other, strides with an outlier Pearson r correlation were excluded (outliers defined as 1.5 * iqr ± q3 or q1). Lastly, features dependent on body weight (i.e., pressure sensors and force sensors) were normalized by the subject’s mass.

For the R5069-OA-1849 clinical trial, data were processed similarly. OA patients had digital insole data collected for only two walks, on day 1 and on day 85, which were processed separately.

### Derived gait characteristics and identification of those speed-correlated

The digital insole derives 85 gait parameters from each walk. Of those, three are directly related to the length of the walk (walking distance and left and right center-of-pressure trace length) and were excluded from further analysis, leaving 82 derived gait characteristics.

Spearman correlations between these 82 parameters were calculated across all walking speeds (slow, comfortable, fast). The silhouette method was used to determine the optimal number of clusters with the factoextra package in R with function fviz_nbclust with 100 bootstrapped samples. Since we were interested in understanding aspects of gait other than walking speed, we correlated all parameters against walking speed and conservatively removed 14 parameters that may be influenced by walking speed in any way (|Spearman rho| > 0.7). This allowed for an investigation into gait parameters less influenced by walking speed.

### Dimensionality reduction

UMAP method for dimensionality reduction was applied using the R UMAP package with default parameters to the z-transformed vGRF data from both the force plate and digital insole datasets to investigate batch effects.

PCA of digital insole vGRF, derived gait characteristics, and raw sensor time series was performed using the prcomp function in the R stats package. Heatmaps of Moticon parameters are displayed per individual, averaged across all individual walks. All heatmaps displayed derived gait characteristics after z-transformation by row across all subjects. All clustering on heatmaps was unsupervised, within groups.

### ML model building

SVM models were built using vGRF, derived gait characteristics, and raw sensor time-series processed data using the sklearn package in Python. This model choice was also benchmarked against logistic regression and XGBoost models from the sklearn and xgboost packages in Python (Figure 2—figure supplement 4).

The force plate dataset was randomly split into 85% training and 15% hold-out test datasets. The 85% training dataset was used for LOOCV and to construct a final trained model, which was then evaluated on the hold-out test dataset. The digital insole dataset was also used as an independent dataset for evaluating the model.

Model performance was evaluated using multiple methods. ROC and precision-recall curves were used to evaluate overall performance. Additionally, we quantitated the auROC curve, which is a standard measure of classification success and describes model performance regardless of baseline likelihood for either class. In addition, we quantitated the auPR and F1-scores, which are useful for evaluating datasets with class imbalances.

### Subject-specific gait signatures

A second question we sought to investigate is whether we could determine subject-specific gait signatures. If we could train models to identify individual subjects from their walk, or from just a single stride, this may suggest that the gait data collected has at a minimum that ability to identify attributes beyond knee disease. We posed this question irrespective of disease state and rather focused on identifying the optimal method to determine an individual participant’s gait pattern.

We approached this question via two approaches commonly used in clinical research settings (Horst et al., 2019; Chau, 2001a; Chau, 2001b; Schöllhorn, 2004). The first is regarding the individuality of human gait patterns. We sought to understand which methodology is best suited to identify generalizable patterns of any person’s gait. The second is understanding which methodology captures features of a specific individual’s gait that have consistency with time. By analogy, a facial recognition software should identify people regardless of whether they wear hats or sunglasses. To learn that these accessories are not stable features of an individual, ML models would need to be trained on images of the same individuals with and without such accessories; that is, trained on these individuals across multiple timepoints. Similarly, we sought to understand whether training on the same individuals across multiple timepoints improves the ability of our models to detect features that identify individuals consistently with time.

### CNN model for control versus OA classification

For the control versus OA model, model performance was determined using LOOCV. A CNN was trained using all strides from all but one participant, after which the model was evaluated on all strides of that left-out participant. Each participant was used as a left-out test participant in one model, such that for N participants, there were N different CNN models each trained on the other N-1 participants. Each stride was labeled as to whether it came from a control or an OA participant.

For each CNN model, strides from the N-1 training participants were split into an 80% training set and a 20% validation set. Each feature within each stride was scaled into 0 min to 1-max range across the 100 interpolated timepoints. The normalized data from each stride was then used as the input to the following CNN architecture: (Functions in italics from the Python [v3.9.7] PyTorch [v1.8.0.post3] package torch.nn were used with the default parameters unless otherwise noted.)

Binary cross entropy loss (BCELoss) was used as the loss function, and stochastic gradient decent (SGD in torch.optim) with a learning rate of 0.001 and momentum of 0.9 was used as the optimizer. Data was loaded into the CNN in batches of 32 with shuffling (DataLoader in torch.utils.data), and backward propagation and parameter optimization were conducted in such batches. Models were trained for 10 epochs, and model parameters from the epoch with the best accuracy on the validation set were chosen as the final model parameters. The model was then tested on the strides of the left-out participant. Model predictions for whether each stride from the left-out participant was from a control or an OA participant were aggregated across the N CNN models, and the overall classification performance was computed.

### CNN model for subject classification and latent representation

As the digital insoles produced high-frequency raw sensor time-series data, we analyzed whether such structured strides (50 measurements along 100 interpolated timepoints for each stride) contained informative subject-specific gait features. To utilize the temporal aspect of the data, we constructed a one-dimensional CNN in which the model could interpret the relationship between sequential timepoints for each sensor. This temporal relationship in the input data was lost in our previous analysis, in which the stride was flattened and interpreted by SVM.

For the individuality and consistency CNN models, the model was trained to identify the subject from which a stride came. However, the purpose of using the CNN model was not to classify training subjects based on their strides, but rather to extract activation of the penultimate fully connected layer for the model’s latent representation of the ‘gait fingerprint’ of a stride. As such, once the CNN model was trained on participants in the training set, the model was then applied to participants in the hold-out testing set and latent representations for each stride were extracted.

To train the CNN model, strides from the training participants were split into a 64% training set, a 16% validation set, and a 20% final validation set. A similar CNN architecture was used as before, except now rather than a binarized control versus OA output, the model outputs the subject label. As such, the model architecture differed starting from the second fully connected layer:

The CNN model was trained in the same manner as before, except multi-class cross entropy loss (CrossEntropyLoss) was used as the loss function. As before, the model was trained for 10 epochs, and model parameters from the epoch with the best accuracy on the validation set were chosen as the final model parameters. The final validation set was then used to check the final model’s performance. A forward hook (register_forward_hook in torch.nn.modules) was attached to the penultimate fully connected layer, to extract activation of that 60-element layer for a new stride inputted into the model.

### Evaluation of subject individuality across different representations

Models were constructed for each data type to predict individual subjects in the training set and then applied on the testing set. Next, distances between each pair of walks/strides were calculated within a subject, within other subjects with the same disease status, and within other subjects with a different disease status.

Each feature was first z-scored (centered and scaled to unit variance, using scale function in base R), and Euclidean distances between all walks/strides in the testing set were calculated using dist function in the R stats package. To compare across representations with differing number of features, distances were divided by the square root of the number of features. The mean distance between every two participants (including with oneself) was then calculated.

To evaluate models for subject individuality, each participant-to-participant comparison was categorized into the groups of control within-self, OA within-self, control with another control, OA with another OA, or one control with one OA. Significance of difference in distances between participant categories was analyzed with t-tests in the R stats package. Effect sizes as Cohen’s d were computed with the R effsize package. Throughout, assumptions of the t-test were checked through creation of univariate histograms of each variable to qualitatively test for normality (i.e., does the data look Gaussian).

### Evaluation of CNN models of subject individuality and consistency

Digital insole sensor data from both baseline (day 1) and on-treatment timepoints (day 85) of OA participants in the R5069-OA-1849 clinical trial was used to evaluate whether training on data from 2 d instead of just 1 d improves the consistency of the CNN representation of participants. A second consistency CNN model was trained on combined data from both timepoints for training set participants, where input data was labeled only by participant identity and not by timepoint. For comparability, both the individuality and consistency CNN models used the same split of train and test participants. Both models were given day 1 and day 85 of testing set participants, and the distance between all stride pairs as represented by the penultimate CNN layer was calculated as before.

To evaluate models for consistency, each participant-to-participant comparison was then categorized into the groups of within-self same day, within-self different day, or subject with another subject. Only OA participants were analyzed for consistency as only they were assessed on two different days. Significance of difference in distances between the CNN individuality and consistency models across the same participant comparisons was analyzed with paired t-tests in the R stats package.
