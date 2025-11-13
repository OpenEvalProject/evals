# Reproducible analysis of disease space via principal components using the novel R package syndRomics

## Authors

- Abel Torres-Espín<sup>1</sup> ([ORCID: 0000-0002-9787-8738](https://orcid.org/0000-0002-9787-8738))
- Austin Chou<sup>1</sup>
- J Russell Huie<sup>1</sup>
- Nikos Kyritsis<sup>1</sup>
- Pavan S Upadhyayula<sup>4</sup>
- Adam R Ferguson<sup>1</sup> ([ORCID: 0000-0001-7102-1608](https://orcid.org/0000-0001-7102-1608)) †

### Affiliations

1. Weill Institute for Neurosciences, Brain and Spinal Injury Center (BASIC), University of California, San Francisco (UCSF) San Francisco United States
2. Department of Neurological Surgery, University of California San Francisco (UCSF) San Francisco United States
3. Zuckerberg San Francisco General Hospital and Trauma Center San Francisco United States
4. School of Medicine, University of California San Diego (UCSD) San Diego United States
5. San Francisco VA Health Care System San Francisco United States

† Corresponding author

## Abstract

Biomedical data are usually analyzed at the univariate level, focused on a single primary outcome measure to provide insight into systems biology, complex disease states, and precision medicine opportunities. More broadly, these complex biological and disease states can be detected as common factors emerging from the relationships among measured variables using multivariate approaches. ‘Syndromics’ refers to an analytical framework for measuring disease states using principal component analysis and related multivariate statistics as primary tools for extracting underlying disease patterns. A key part of the syndromic workflow is the interpretation, the visualization, and the study of robustness of the main components that characterize the disease space. We present a new software package, syndRomics, an open-source R package with utility for component visualization, interpretation, and stability for syndromic analysis. We document the implementation of syndRomics and illustrate the use of the package in case studies of neurological trauma data.

## Introduction

The goal of the burgeoning field of precision medicine is to understand complex disease states and provide opportunities for deep patient phenotyping and highly targeted therapeutics. Precision medicine requires an understanding of multidimensional disease states. Yet, the analysis of biomedical data remains largely univariate, with response variables considered individually and reports involving several distinct analyses. This analytical approach limits our interpretation of the complexity of a disease by not considering the shared information across variables and potentially contributing to irreproducibility due to statistical limitations of multiple comparison testing. Understanding the full set of interrelated disease features through multivariate statistics is the goal of the growing domain of 'syndromics' (Ferguson et al., 2011). In particular, principal component analysis (PCA) and related multivariate statistics such as nonlinear PCA or factor analysis have been proposed as tools for extracting underlying factors or patterns (principal components [PCs]) reflecting disease states (Ferguson et al., 2013; Haefeli et al., 2017a; Haefeli et al., 2017b; Kutcher et al., 2013; Nielson et al., 2014; Nielson et al., 2015; Panaretos et al., 2017; Rosenzweig et al., 2010; Rosenzweig et al., 2018; Rosenzweig et al., 2019; Zhang and Castelló, 2017). There are several other multivariate methods that could be used for multivariate pattern detection: other ordination and dimension reduction techniques, cluster analysis, discrimination analysis, or the plethora of more recent machine learning methods. The use of any of these methods has its advantages and pitfalls (Everitt and Hothorn, 2011). We focus on PCA as being one of the most widely used method for pattern detection. PCA is a multivariate statistical procedure that allows for the generation of new uncorrelated variables, called PCs, as a weighted combination of the original variables (Abdi and Williams, 2010; Hotelling, 1933; Jolliffe and Cadima, 2016). These components are ordered such that the first component explains the major source of variance in the data, the second component the second largest source of variance, etc. The extracted components reflect the interrelation between all the original variables or features, allowing for disease pattern detection, guiding in the interpretation of disease complex space and overcoming univariate analysis limitations.

Despite the extensive use of PCA in some subfields of biological research and the increasing use of PCA for disease pattern discovery, there is very limited information in the literature that can guide applied biomedical researchers about its implementation and interpretation. Here, we offer a practical guide to the application of PCA for the extraction of disease patterns that conform the disease space, with focus on reproducibility. By no means can we cover the extensive field of PCA in the present document. Rather, we aim to provide an introductory manual to extraction of reproducible disease patterns using multidimensional analytics, directed to biomedical researcher practitioners while pointing to additional relevant sources of information. We introduce a software package for the R programming language called syndRomics, implementing some of the tools described here. We will illustrate the analysis workflow and the use of the package in experimental data from case studies in neurotrauma.

The key steps in disease pattern detection by PCA are shown in Figure 1. The syndRomics package offers functionalities that aid in these steps, building on the extensive PCA framework developed by the R open-source community. The package implements a novel visualization tool, the syndromic plot first published by Ferguson et al., 2013, as well as functions to quickly generate two other publication-ready visualizations (a heatmap and a barmap). In addition, the package implements resampling strategies, providing data-driven approaches to analytical decision-making aimed to reduce researcher subjectivity and increase reproducibility. In particular, the package offers a function to extract metrics for component and variable significance by using nonparametric permutation methods (Landgrebe et al., 2002; Linting et al., 2011; Peres-Neto et al., 2003), to inform component selection and component interpretation. Finally, the package incorporates functions to study component stability toward understanding the generalizability and robustness of the analysis (Cattell and Baggaley, 1960; Cattell et al., 1969; Lorenzo-Seva and ten Berge, 2006).

![Figure 1.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig1-v2.jpg)

**Figure 1.:** (A) The theoretical framework of syndromic analysis. The intersection between different outcome measures can create a multivariate measure (principal component if PCA is used) to explain different patterns of variance in the data. The conceptual union of three van diagram forms the core of the syndromic plot symbolizing the multidimensional measure. (B) The different steps of the workflow to using PCA such as for disease pattern analysis.

## Results

We will describe the general steps to use PCA for syndromic analysis and illustrate the use of the syndRomic package along the analytical steps with two case studies of neurotrauma data. Details of the usage and implementation of the package and functions are described in the Materials and methods section. The full code reproducing the analysis can be found in the supplementary material. Code boxes in the text provide snippets illustrating the main sections of the code. The first case study is used as a tutorial to illustrate the steps of analysis; the second case study is discussed at the end of the results section. For the first case, we used a publicly available preclinical dataset on the Open Data Commons for Spinal Cord Injury (odc-sci.org) (Callahan et al., 2017; Fouad et al., 2019). We selected a subset of the dataset with accession number ODC-SCI: 26 (Ferguson et al., 2018) that has been previously used for deriving the so-called spinal cord injury (SCI) syndromics (Ferguson et al., 2013). The dataset contains 159 subjects (rats) that have been studied on different motor functional outcomes across time after cervical spinal cord injury. The subset chosen for the present analysis consists of 18 outcome variables measured at 6 weeks after injury. The included variables for this analysis are shown in Table 1. For additional details of these variables, see Ferguson et al., 2013.

**Table 1.**
 List of variables included in the first case study.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wtChng</td>
      <td>Change of animal weight (grams) from day of Injury to 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>RFSL</td>
      <td>CATWALK SYSTEM RightForelimb StrideLength at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>LFSL</td>
      <td>CATWALK SYSTEM LeftForelimb StrideLength at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>RHSL</td>
      <td>CATWALK SYSTEM RightHindlimb StrideLength at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>LHSL</td>
      <td>CATWALK SYSTEM LeftHindlimb StrideLength at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>RFPA</td>
      <td>CATWALK SYSTEM RightForelimb PrintArea at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>LFPA</td>
      <td>CATWALK SYSTEM LeftForelimb PrintArea at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>RHPA</td>
      <td>CATWALK SYSTEM RightHindlimb PrintArea at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>LHPA</td>
      <td>CATWALK SYSTEM LeftHindlimb PrintArea at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>StepDistRF</td>
      <td>CATWALK SYSTEM RightForelimb Step Distribution Deviation from 25% at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>StepDistLF</td>
      <td>CATWALK SYSTEM LeftForelimb Step Distribution Deviation from 25% at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>StepDistRH</td>
      <td>CATWALK SYSTEM RightHindlimb Step Distribution Deviation from 25% at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>StepDistLH</td>
      <td>CATWALK SYSTEM LeftHindlimb Step Distribution Deviation from 25% at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>TotalSubscore</td>
      <td>Total BBB Subscore at 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>BBB FergTrans</td>
      <td>BBB Ferguson Transformation score 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>Groom</td>
      <td>Grooming Score 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>PawPL</td>
      <td>PawPlacement score 6 weeks post-injury</td>
    </tr>
    <tr>
      <td>ForelimbOpenField</td>
      <td>Forelimb openfield score at 6 weeks post-injury</td>
    </tr>
  </tbody>
</table>

### Step 1: Extracting PCA solution from the data

There is extensive literature on performing PCA (Abdi and Williams, 2010; Jolliffe and Cadima, 2016; Zhang and Castelló, 2017). As a consideration, biomedical data aiming to capture the multivariate disease space usually contains variables of different types (i.e. categorical, continuous, etc.) and scales, known as ‘mixed-type’ data. Moreover, missing data is a common problem in biomedicine (Hollestein and Carpenter, 2017; Kaushal, 2014; Nielson et al., 2020) that needs to be solved to be able to apply most standard PCA algorithms. Therefore, some pre-processing transformations are usually applied before performing PCA. For example, linear PCA is sensitive to the scale of variables, thus when applying a linear PCA to continuous variables of different units or scales, a common practice is to scale the data to unit variance first (i.e. equivalent to performing the PCA on the correlation matrix). The use of the package to conduct syndromics analysis from linear PCA is illustrated on the first case study. In cases of datasets with mixed data types and/or non-linear relationships between variables, nonlinear PCA with optimal scaling transformation (Linting et al., 2007a; Mair and Leeuw, 2019) has been previously used for disease pattern analysis (Rosenzweig et al., 2018; Rosenzweig et al., 2019). We used the syndRomics package to analyze patterns from a nonlinear PCA in the second case study. In cases with missing data, strategies such as data imputation or the use of PCA algorithms allowing missing values might be needed (Dray and Josse, 2015). While missing values analysis and dealing with missingness is an extensive topic that is not covered in detail here (Rubin, 1976; Buuren, 2018), the chosen case studies do contain missing values and illustrate how the package can help to determine the stability of the PCs when imputing missing values (see component stability section).

Another consideration is selecting which variables to include in the analysis. For PCA of experimental data where there are stratifying factors (e.g. control vs. treatment), it is important to leave out variables that directly capture the variance of these factors, which would bias PCA results toward separating the experimental groups. This bias is problematic since in syndromic analysis, the goal is to find the relationship between variables describing different diseases states in an unsupervised (i.e. not guided by our design) manner. For instance, if treatment indicators are included and the variance between treatment groups is high, the PCA solution would directly capture the experimental design and confound the multivariate patterns.

The disease components can be used in subsequent analysis as multivariate outcomes or predictor indicators (Haefeli et al., 2017a; Nielson et al., 2015; Rosenzweig et al., 2018; Rosenzweig et al., 2019). PCA is used to extract the correlation structure between variables, generating new independent variables as linear combinations. Beyond the use of PCs as proxies for disease patterns, the PCs can help mitigate issues that might appear when analyzing several variables such as multicollinearity, overfitting, and multiple testing (Altman and Krzywinski, 2018; Johnson et al., 1973; Lever et al., 2017).

The reader is referred to some materials of interest on considerations and limitations when conducting PCA and related methods for biomedical research (Jiang and Eskridge, 2000; Konishi, 2015; Nguyen and Holmes, 2019; Zhang and Castelló, 2017).

Case study: In the first case study, the goal is to run a linear PCA to study the motor function components 6 weeks after cervical spinal cord injury. This will summarize all motor function variables as a small set of independent components explaining different aspects of the motor behavior after an SCI. The data contains missing values (Figure 4—figure supplement 1), and therefore we performed missing values analysis before continuing with the workflow. Typically, the first step in missing values analysis is to determine patterns of missingness and classify missing values as missing completely at random (MCAR), missing at random (MAR) or missing not at random (MNAR) (Rubin, 1976). The type of missingness will guide the decision on which is an acceptable procedure to deal with missing values. For instance, deleting all subjects that contain at least one missing observation is common practice (aka listwise deletion or complete-case analysis), but it is only acceptable if missing values are MCAR. Otherwise, the robustness and proper estimation of the missing values can not be guaranteed (Schafer and Graham, 2002; Buuren, 2018). In the example data, subjects have been pooled together from different experiments. We know that the observed pattern of missingness (Figure 4—figure supplement 1) is due to a set of animals where some of the outcome measures were not studied, suggesting that missing values are MNAR. We confirmed that missing values are not MCAR using a previously described test of MCAR (Jamshidian and Jalal, 2010) implemented in the MissMech package in R (Jamshidian et al., 2014), which rejected the hypothesis of MCAR missingness in our data. Thus, excluding subjects from the analysis is not justified. Instead, we have used multiple imputation through the mice R package (Buuren and Groothuis-Oudshoorn, 2011) to generate 50 imputed datasets and pooled them using the mean of each observation. We will illustrate on the component stability section how the syndRomics package can be used to determine the robustness of multiple imputation for disease pattern analysis. We extracted the PCA solution of the pooled imputed data using the prcomp() function in R after centering and scaling the data to unit variance (R code box 1). Other similar functions in R or other software can be used.R Code Box 1pca<-prcomp (pca_data, center = TRUE, scale. = TRUE).

### Step 2: Component selection: how many components to keep?

The first question, after running PCA for extracting the disease components is usually to determine how many PCs are relevant. As a general consideration, the PCs with lower eigenvalues (i.e. explain less variance) have a higher chance of representing noise in the data (Jolliffe and Cadima, 2016), questioning their generality and value. The goal is to determine the minimal set of components that can be used to describe the disease space. Importantly, there is not a single, specific rule for this determination. A common method in PCA and related methods is the Scree test by Cattell, 1966, where all PCs are ordered in descending rank by their eigenvalues, and PCs above the ‘elbow’ are retained. Another criterion is the eigenvalue greater than one rule which is applied to standardized PCAs (from the correlation matrix) with the criteria of only keeping PCs with an eigenvalue (i.e. the variance of a component) above 1 (Guttman, 1954; Kaiser, 1960). A more thorough description of these and others methods can be found elsewhere (Glorfeld, 1995; Horn, 1965; Vitale et al., 2017; Zwick and Velicer, 1986). Simulations have shown these methods (specially the eigenvalue greater than one rule) to be less robust than a re-sampling approach for selecting the number of relevant components (Zwick and Velicer, 1986). The syndRomics package incorporates a nonparametric permutation test approximated through Monte Carlo re-sampling of the total ‘variance accounted for’ (VAF) of each PC to aid in the selection of relevant PCs (Buja and Eyuboglu, 1992; Glorfeld, 1995; Horn, 1965; Landgrebe et al., 2002). The permutation test can also assist in component interpretation by studying the contribution of each variable to the PCA solution (Buja and Eyuboglu, 1992; Linting et al., 2011) as we will see in the next section.

The goal of the permutation test is to determine whether the extracted PCs can be considered to be generated not-at-random. This method has been shown to outperform parametric tests for PCA in situations similar to biomedical data where sample sizes are relatively small and the data rarely comply with the assumptions of the models (Buja and Eyuboglu, 1992; Horn, 1965; Zwick and Velicer, 1986). In that regard, a hypothesis test is defined as:

The p values are calculated by:

$$
p=(q+1)/(P+1)
$$

where $q$ is the number of times the chosen metric is higher in the permuted distribution than in the original PCA solution and $P$ is the number of permutations (Buja and Eyuboglu, 1992). Rejecting the null hypothesis is interpreted as evidence of the tested PC being generated from true signal and not by random noise. This sets a lower bound for which PCs to consider 'important' above noise, but does not indicate the magnitude of the 'importance', which is represented by VAF. Importantly, for datasets with several directions of variance and high signal-to-noise ratio, PCs with low VAF can still be statistically significant. The value of interpreting such PCs must be judged by the researcher in the context analysis in question. It is also important to consider how big $P$ needs to be when performing re-sampling, such as with the permutation test incorporated in the package. The reader should note that the lowest $p$ value that can be calculated is dependent on $P$. For example, if $P$ is set to a value of 10 (a relatively low value), the smallest p value that can be detected is 0.09, which occurs when $q=0$. Accordingly, $P$ should be set high enough to reach the desired minimum p value. Moreover, simulation studies have shown that $P$ under 99 have low power and a minimum of 499 permutations is recommended (Buja and Eyuboglu, 1992; Abdi and Williams, 2010; Linting, 2007). By default, we have set the number of permutations to 1000 (smallest p value approximately equal to 0.001) as this has been shown to produce good results (Landgrebe et al., 2002; Linting et al., 2011). Users of the package should keep in mind that higher numbers of permutations will increase computation time with potentially only a small gain on the approximation. Our simulations indicate that between 500 and 1000 permutations provide a good compromise between computing time and precision in estimating confidence intervals, depending on the data volume (Figure 4—figure supplement 1). The package implements a single permutation strategy for VAF, the so-called permD (permutation of the entire data set) (Buja and Eyuboglu, 1992; Linting et al., 2011) where variables are permuted independently and concomitantly (Figure 2A) opposed to permV (permutation of a single variable) (Linting et al., 2011) where variables are permuted one at the time (Figure 2B). These methods are further discussed on the component interpretation section.

![Figure 2.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig2-v2.jpg)

**Figure 2.:** (A) Shows a schematic example of the permutation procedure permD where all the variables are permuted concomitantly but independently. (B) Shows a schematic example of the permutation procedure permV where variables are permuted one at the time for each permutation samples (P), keeping the other variables as in the original dataset. (C) The implemented algorithm for the permutation test algorithm using permD: each one to n permutation sample (P) consist on a random reorganization of observations inside each variable independently and concomitantly for each variable. For each P sample, a PCA is run and either the loadings, communalities or VAF are calculated. All P PCA solutions form the null distribution for non-parametric hypothesis testing of loadings or VAF. (D) The permutation test algorithm for loadings under permV is performed with and extra step of Procrustes rotation between each of the P samples to the parent component loadings. The P rotated loadings will then form the null distribution for each variable.

R Code Box 2.

permut_pc_test (pca, pca_data, p=10000, ndim = 5, statistic = 'VAF', perm.method = 'permD').

Case study: After performing a PCA, we first determined the number of components that can be regarded as informative. Several criteria can be used as mentioned earlier. Here, we opted for the permutation test of VAF, computed using the permut_pc_test() function (R Code Box 2). We have applied this test to the data using 10,000 permutations. The results show that the three first PCs (PC1, PC2, and PC3) are significantly different from random at an alpha of 0.05 adjusting the p value (Figure 3), and therefore we will keep these three PCs for subsequent analysis. PC1 accounts for 32.9% of the variance, PC2 18.3% and PC3 9.8%.

![Figure 3.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig3-v2.jpg)

**Figure 3.:** (A) The graph shows the original VAF for the first five PCs and the average and 95% confidence interval VAF of the permuted PCA distribution (p=10000) using the permD method. * Statistical difference for the non-parametric test at alpha = 0.05 and adjusted p value by BH. The three first PCs were selected for the subsequent analysis. (B) Barmap of the original communalities (bars) and the permuted distribution (permV, p=3000) for each variable calculated over the first three PCs. (C) Barmap of the original loadings (bars) and the permuted distribution (permV, p=3000) for each variable and each of the first three PCs. Solid dotes represent the mean of the permuted distribution and error bars represent the 95% CI.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Shadow plot of missing data for the variables selected for the case study. Approximately 17% are missing values. Four patterns of missingness are observed as shown by the upset plot (B), three patterns with involving more than one variable and a pattern with a single variable. The fact that most missing values are across variables for the same subject (two biggest missing pattern sets) suggest data is missing at random (MAR), meaning there is an external reason to the observed values for that missing. In order to assess the stability of the PCA analysis by performing multiple imputation, we calculated the distribution of loadings generated by 50 multiple imputed datasets (C). The small variation around a pooled loading (average, bar) suggest a very small variation introduced by imputing the data, further corroborated by the component similarity measures for the first three PCs (Tables 4–6). Solid dots represent the mean of the multiple imputed loading distribution and error bars represent the 95% CI.

### Step 3: Component interpretation: what do these components mean?

A key part of the analytical workflow is the interpretation of the main components, where the most relevant PCs can be used to represent the correlation between the original variables as a proxy for multivariate disease patterns. Each component is composed of a weighted combination of all the variables. Some components might be explained by only a few variables with high importance, whereas others might have several variables with important contributions to them. There are a few metrics that can be used for interpreting the relation between the original variables and the PCs (Abdi and Williams, 2010). In the syndRomics package, we use the standardized loadings or correlation vector coefficients (Jackson and Hearne, 1973), and the communalities, which are the sum of squared loadings for each variable across selected PCs representing how much of the variance of each variable can be explained by the total number of kept components. Loadings can be interpreted as the Pearson’s r correlation coefficient between a PC and a variable, and it is used to assess the contribution of individual variables on each PC and the direction on which the variable moves along the PC (i.e. opposite or same direction as in the interpretation of a correlation). Communalities can be interpreted as the global impact of a variable in the chosen PCA solution.

In general, the strategy consists of determining a threshold for the absolute value of loadings or the communalities above which variables are considered to have important contribution in the definition of a component or across the chosen PCs. For example, if a threshold of |loading| > 0.2 is chosen, all variables for a given PC with a loading > 0.2 or a loading < −0.2 will be considered to contribute on the PC (aka salient variable). The matter then turns to determining an appropriate threshold. Some somewhat arbitrary rules of thumb for the loadings have been established. However, those have a strong determination in psychological studies and whether they are appropriate in biomedical research has yet to be verified. An alternative ‘quasi-inferential’ method is to use permutation test as discussed above for PC VAF but testing for metrics of variable contribution such as loadings (Buja and Eyuboglu, 1992; Peres-Neto et al., 2003) or communalities (Linting et al., 2011). Using resampling strategies, these permutation methods offer data-driven determination of variable importance and contribution, which might reduce subjective biases. Thus, rejecting the null hypothesis for a given metric, variable and PC, suggest that such variable has a contribution onto the construction of the component that is above what is expected by random noise. As in the case of VAF, this establishes a lower bound for |loadings| or communalities below which they should be considered noise. In situations with stable solutions and high signal-to-noise ratio, low |loadings| or communalities might still be statistically significant, but the contribution of the variable should be gauged respect to other variables. In the package, we have incorporated permutation test of the loadings as in Buja and Eyuboglu, 1992; Peres-Neto et al., 2003 that can serve to determine the loading threshold, where the variables are permuted independently and concomitantly (Figure 2A and C). Linting et al., designed and tested an strategy for the communalities where only one variable is permuted at the time, showing great results in determining the contribution of variables using communalities (Linting et al., 2011). This method has resulted in better determination of the significant contribution of variables on the PCA solution with higher statistical power and proper type I error, and therefore has been incorporated in the package as the default method for both the communalities and the loadings (Figure 2B and D). Following Linting et al., terminology, users can specify the permutation strategy for the loadings as one variable at the time (permV, as in [Linting et al., 2011]) or as all the variable together (permD, as in [Buja and Eyuboglu, 1992; Linting et al., 2011; Peres-Neto et al., 2003]). See Materials and methods for details on the permutation algorithms. In addition to permutation strategies, the package implements bootstrapping methods for constructing confidence intervals of component loadings and communalities that can also facilitate PCs interpretation (see component stability).

The selection of number of permutations in this case follows similar rationale as described above for the VAF. It is important to note that the minimal number of permutation needed to have enough statistical power and precision will depend on the size of the dataset, both on the number of variables and samples (Buja and Eyuboglu, 1992; Figure 4—figure supplement 1). There is also the understanding that while the permD strategy is less robust than permV as suggested by Linting et al., the computational time increases considerably since variables are permuted one at the time. Moreover, adjusting p values for multiple testing might be recommended depending on the sample size. Linting et al., suggested controlling for false discovery rate (FDR) using the Benjamini and Hochberg (BH) (Benjamini and Hochberg, 1995) method. As a rule of thumb, these researchers advised to only use multiple testing correction (for FDR) when the data contains at least 20 variables and 100 observations or subjects, and to use the uncorrected p-values otherwise (Linting et al., 2011). p-Value adjustment has been incorporated in the permutation function on the package, with controlling for FDR by BH as default.

The reader should be cautioned against overinterpreting or misinterpreting the meaning of a PC. The interpretation can be subjective, and unconscious biases can be reflected on the interpretation of PCs. The tools offered by the package help mitigate potential subjective biases, although data biases will affect the results. Another consideration is that it is possible that some of these metrics seem to ‘contradict’ each other. For example, there is the possibility that a component has an important contribution to the variance of the data (high VAF) and yet all the loadings be small. Contrary, a component with a small set of high loadings could be considered to be insignificant by permuting its VAF (Buja and Eyuboglu, 1992). As in any analytical approach, domain knowledge is critical for the interpretation of disease components.

Case study: After deciding to keep three components, we studied the communalities and loadings to determine their identity. Here, we applied the permut_pc_test() function (R Code Box 3) setting the argument statistic = ‘commun’ or ‘s.loadings’ and the perm.method = ‘permV’ and using the BH method for controlling for FDR. The results of the permutation test on the communalities can be seen in Figure 3B and in Table 3. We can appreciate that all variables are significantly represented by the three chosen PCs, although there are five variables with communality less than 0.5, indicating that the retained PCs only explain 50% of the variance on these variables. In PCA, communalities can suggest which variables do or do not contribute to the extracted components altogether. Considering the loadings, the results for PC1, PC2, and PC3 are shown in Figure 3C and in Tables 4, 5 and 6, respectively. One can appreciate that the cutoff loading for significance at alpha 0.05 using the adjusted p value is approximately |0.21| for PC1, |0.25| for PC2 and |0.4| for PC3. This behavior of different thresholds for significance has been previously described (Buja and Eyuboglu, 1992) and reflects the fact that PCs accounting for less variance might contain more random noise, thus needing a higher loading for a variable to be considered as an important contributor. Loadings are indicative of both strength of association between a variable and a PC and the direction in which they interact. For reading on the interpretation of the loadings and components in this case study, see Ferguson et al., 2013.

**Table 2.**
 List of variables included in the second case study.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Description</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CT_Marshall</td>
      <td>Marshall CT Score</td>
      <td>Range from 1 to 6</td>
    </tr>
    <tr>
      <td>CT_Rotterdam</td>
      <td>Rotterdam CT Score</td>
      <td>Range from 1 to 6</td>
    </tr>
    <tr>
      <td>CT_brain_pathology</td>
      <td>CT Brain Pathology</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_skull_FX</td>
      <td>CT Skull Fracture</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_skullbase_FX</td>
      <td>CT Skull Base Fracture</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_facial_FX</td>
      <td>CT Facial Fracture</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_EDH</td>
      <td>CT Epidural Hematoma</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_SDH</td>
      <td>CT Subdural Hematoma</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_SAH</td>
      <td>CT Subarachnoid Hemorrhage</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_contusion</td>
      <td>CT Contusion</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_midlineshift</td>
      <td>CT Midline Shift</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>CT_cisterncomp</td>
      <td>CT Cisternal Compression</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>PTSD_diagnosis_6mo</td>
      <td>PTSD DSM-IV Diagnosis (6 months)</td>
      <td>0 = ‘No’, 1 = ‘Yes’</td>
    </tr>
    <tr>
      <td>GOSE_3mo</td>
      <td>GOSE Score (3 months)</td>
      <td>Range from 1 to 8</td>
    </tr>
    <tr>
      <td>GOSE_6mo</td>
      <td>GOSE Score (6 months)</td>
      <td>Range from 1 to 8</td>
    </tr>
    <tr>
      <td>WAIS_PSI_6mo</td>
      <td>WAIS PSI Composite Score (6 months)</td>
      <td>Range from 50 to 150</td>
    </tr>
    <tr>
      <td>CVLT_short_6mo</td>
      <td>CVLT Short Delay Cued Recall Standard Score (6 months)</td>
      <td>Range from −4.0–2.5</td>
    </tr>
    <tr>
      <td>CVLT_long_6mo</td>
      <td>CVLT Long Delay Cued Recall Standard Score (6 months)</td>
      <td>Range from −3.5–2.5</td>
    </tr>
    <tr>
      <td>SNP_COMT</td>
      <td>COMT SNP Genotype</td>
      <td>1 = ‘Met/Met’, 2 = ‘Met/Val’, 3 = ‘Val/Val’</td>
    </tr>
    <tr>
      <td>SNP_DRD2</td>
      <td>DRD2 SNP Genotype</td>
      <td>1 = ‘C/C’, 2 = ‘C/T’, 3 = ‘T/T’</td>
    </tr>
    <tr>
      <td>SNP_PARP1</td>
      <td>PARP1 SNP Genotype</td>
      <td>1 = ‘A/A’, 2 = ‘A/T’, 3 = ‘T/T’</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly318Arg</td>
      <td>ANKK1 SNP Gly318Arg</td>
      <td>1 = ‘A/A’, 2 = ‘A/G’, 3 = ‘G/G’</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly442Arg</td>
      <td>ANKK1 SNP Gly442Arg</td>
      <td>1 = ‘C/C’, 2 = ‘C/G’, 3 = ‘G/G’</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Glu713Lys</td>
      <td>ANKK1 SNP Glu713Lys</td>
      <td>1 = ‘C/C’, 2 = ‘C/T’, 3 = ‘T/T’</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Communalities of first three PCs on permutation test with 3000 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original communalities</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wtChng</td>
      <td>0.46</td>
      <td>0.06</td>
      <td>0.01</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>RFSL</td>
      <td>0.59</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>RFPA</td>
      <td>0.85</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>StepDistRF</td>
      <td>0.54</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>LFSL</td>
      <td>0.57</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.18</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>LFPA</td>
      <td>0.61</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>StepDistLF</td>
      <td>0.71</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>RHSL</td>
      <td>0.88</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.18</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>RHPA</td>
      <td>0.81</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>StepDistRH</td>
      <td>0.27</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.18</td>
      <td>0.0020</td>
      <td>0.0020</td>
    </tr>
    <tr>
      <td>LHSL</td>
      <td>0.79</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>LHPA</td>
      <td>0.79</td>
      <td>0.07</td>
      <td>0.00</td>
      <td>0.23</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>StepDistLH</td>
      <td>0.46</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>Groom</td>
      <td>0.53</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>PawPL</td>
      <td>0.70</td>
      <td>0.06</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>BBB_FergTrans</td>
      <td>0.66</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>TotalSubscore</td>
      <td>0.40</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
    <tr>
      <td>ForelimbOpenField</td>
      <td>0.37</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.18</td>
      <td>0.0003</td>
      <td>0.0004</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 PC1 loading results of permutation test for the first case study with 3000 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original loading</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wtChng</td>
      <td>−0.34</td>
      <td>0.00</td>
      <td>−0.19</td>
      <td>0.18</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>TotalSubscore</td>
      <td>−0.56</td>
      <td>0.00</td>
      <td>−0.21</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>StepDistRH</td>
      <td>0.89</td>
      <td>0.01</td>
      <td>−0.20</td>
      <td>0.21</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>StepDistRF</td>
      <td>−0.65</td>
      <td>0.00</td>
      <td>−0.19</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>StepDistLH</td>
      <td>−0.28</td>
      <td>0.00</td>
      <td>−0.18</td>
      <td>0.18</td>
      <td>0.0043</td>
      <td>0.0084</td>
    </tr>
    <tr>
      <td>StepDistLF</td>
      <td>0.54</td>
      <td>0.01</td>
      <td>−0.18</td>
      <td>0.18</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>RHSL</td>
      <td>−0.76</td>
      <td>0.00</td>
      <td>−0.19</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>RHPA</td>
      <td>−0.85</td>
      <td>0.00</td>
      <td>−0.17</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>RFSL</td>
      <td>0.74</td>
      <td>0.01</td>
      <td>−0.18</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>RFPA</td>
      <td>−0.25</td>
      <td>0.00</td>
      <td>−0.18</td>
      <td>0.18</td>
      <td>0.0063</td>
      <td>0.0114</td>
    </tr>
    <tr>
      <td>PawPL</td>
      <td>−0.76</td>
      <td>0.00</td>
      <td>−0.17</td>
      <td>0.17</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>LHSL</td>
      <td>0.62</td>
      <td>0.00</td>
      <td>−0.18</td>
      <td>0.18</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>LHPA</td>
      <td>−0.24</td>
      <td>0.00</td>
      <td>−0.19</td>
      <td>0.17</td>
      <td>0.0163</td>
      <td>0.0259</td>
    </tr>
    <tr>
      <td>LFSL</td>
      <td>0.38</td>
      <td>0.01</td>
      <td>−0.17</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>LFPA</td>
      <td>−0.54</td>
      <td>−0.01</td>
      <td>−0.21</td>
      <td>0.20</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>Groom</td>
      <td>0.49</td>
      <td>0.00</td>
      <td>−0.20</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>ForelimbOpenField</td>
      <td>0.20</td>
      <td>−0.01</td>
      <td>−0.19</td>
      <td>0.18</td>
      <td>0.0323</td>
      <td>0.0459</td>
    </tr>
    <tr>
      <td>BBB_FergTrans</td>
      <td>0.51</td>
      <td>0.01</td>
      <td>−0.18</td>
      <td>0.19</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 PC2 loading results of permutation test for the first case study with 3000 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original loading</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wtChng</td>
      <td>−0.37</td>
      <td>0.00</td>
      <td>−0.23</td>
      <td>0.22</td>
      <td>0.0023</td>
      <td>0.0047</td>
    </tr>
    <tr>
      <td>TotalSubscore</td>
      <td>−0.48</td>
      <td>−0.01</td>
      <td>−0.23</td>
      <td>0.21</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>StepDistRH</td>
      <td>−0.07</td>
      <td>−0.01</td>
      <td>−0.23</td>
      <td>0.23</td>
      <td>0.5122</td>
      <td>0.5644</td>
    </tr>
    <tr>
      <td>StepDistRF</td>
      <td>0.28</td>
      <td>0.00</td>
      <td>−0.23</td>
      <td>0.21</td>
      <td>0.0143</td>
      <td>0.0234</td>
    </tr>
    <tr>
      <td>StepDistLH</td>
      <td>−0.66</td>
      <td>0.01</td>
      <td>−0.23</td>
      <td>0.24</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>StepDistLF</td>
      <td>0.27</td>
      <td>0.00</td>
      <td>−0.22</td>
      <td>0.23</td>
      <td>0.0203</td>
      <td>0.0305</td>
    </tr>
    <tr>
      <td>RHSL</td>
      <td>0.34</td>
      <td>0.00</td>
      <td>−0.24</td>
      <td>0.23</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>RHPA</td>
      <td>−0.30</td>
      <td>0.00</td>
      <td>−0.21</td>
      <td>0.21</td>
      <td>0.0083</td>
      <td>0.0145</td>
    </tr>
    <tr>
      <td>RFSL</td>
      <td>0.40</td>
      <td>0.00</td>
      <td>−0.22</td>
      <td>0.25</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>RFPA</td>
      <td>0.21</td>
      <td>0.00</td>
      <td>−0.22</td>
      <td>0.22</td>
      <td>0.0643</td>
      <td>0.0868</td>
    </tr>
    <tr>
      <td>PawPL</td>
      <td>−0.30</td>
      <td>0.00</td>
      <td>−0.19</td>
      <td>0.22</td>
      <td>0.0023</td>
      <td>0.0047</td>
    </tr>
    <tr>
      <td>LHSL</td>
      <td>0.42</td>
      <td>0.01</td>
      <td>−0.21</td>
      <td>0.23</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>LHPA</td>
      <td>0.12</td>
      <td>0.00</td>
      <td>−0.24</td>
      <td>0.22</td>
      <td>0.3182</td>
      <td>0.3656</td>
    </tr>
    <tr>
      <td>LFSL</td>
      <td>−0.62</td>
      <td>0.00</td>
      <td>−0.25</td>
      <td>0.25</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>LFPA</td>
      <td>0.63</td>
      <td>0.00</td>
      <td>−0.24</td>
      <td>0.26</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>Groom</td>
      <td>−0.65</td>
      <td>0.00</td>
      <td>−0.22</td>
      <td>0.23</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>ForelimbOpenField</td>
      <td>−0.59</td>
      <td>−0.01</td>
      <td>−0.25</td>
      <td>0.23</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>BBB_FergTrans</td>
      <td>−0.32</td>
      <td>−0.01</td>
      <td>−0.22</td>
      <td>0.22</td>
      <td>0.0023</td>
      <td>0.0047</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 PC3 loading results of permutation test for the first case study with 3000 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original loading</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wtChng</td>
      <td>0.46</td>
      <td>0.00</td>
      <td>−0.43</td>
      <td>0.41</td>
      <td>0.0183</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <td>TotalSubscore</td>
      <td>0.22</td>
      <td>0.00</td>
      <td>−0.32</td>
      <td>0.34</td>
      <td>0.2463</td>
      <td>0.2955</td>
    </tr>
    <tr>
      <td>StepDistRH</td>
      <td>0.23</td>
      <td>0.01</td>
      <td>−0.32</td>
      <td>0.35</td>
      <td>0.2303</td>
      <td>0.2826</td>
    </tr>
    <tr>
      <td>StepDistRF</td>
      <td>−0.19</td>
      <td>0.01</td>
      <td>−0.32</td>
      <td>0.34</td>
      <td>0.3102</td>
      <td>0.3642</td>
    </tr>
    <tr>
      <td>StepDistLH</td>
      <td>0.23</td>
      <td>0.00</td>
      <td>−0.34</td>
      <td>0.36</td>
      <td>0.2083</td>
      <td>0.2615</td>
    </tr>
    <tr>
      <td>StepDistLF</td>
      <td>0.50</td>
      <td>−0.01</td>
      <td>−0.36</td>
      <td>0.40</td>
      <td>0.0063</td>
      <td>0.0114</td>
    </tr>
    <tr>
      <td>RHSL</td>
      <td>0.12</td>
      <td>0.00</td>
      <td>−0.35</td>
      <td>0.33</td>
      <td>0.5382</td>
      <td>0.5698</td>
    </tr>
    <tr>
      <td>RHPA</td>
      <td>0.26</td>
      <td>0.00</td>
      <td>−0.35</td>
      <td>0.35</td>
      <td>0.1903</td>
      <td>0.2446</td>
    </tr>
    <tr>
      <td>RFSL</td>
      <td>0.32</td>
      <td>0.00</td>
      <td>−0.36</td>
      <td>0.41</td>
      <td>0.1043</td>
      <td>0.1374</td>
    </tr>
    <tr>
      <td>RFPA</td>
      <td>0.41</td>
      <td>0.00</td>
      <td>−0.34</td>
      <td>0.35</td>
      <td>0.0223</td>
      <td>0.0326</td>
    </tr>
    <tr>
      <td>PawPL</td>
      <td>0.35</td>
      <td>−0.01</td>
      <td>−0.37</td>
      <td>0.35</td>
      <td>0.0583</td>
      <td>0.0807</td>
    </tr>
    <tr>
      <td>LHSL</td>
      <td>0.48</td>
      <td>0.01</td>
      <td>−0.39</td>
      <td>0.44</td>
      <td>0.0123</td>
      <td>0.0208</td>
    </tr>
    <tr>
      <td>LHPA</td>
      <td>0.62</td>
      <td>0.00</td>
      <td>−0.38</td>
      <td>0.35</td>
      <td>0.0003</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>LFSL</td>
      <td>−0.05</td>
      <td>0.00</td>
      <td>−0.35</td>
      <td>0.33</td>
      <td>0.8001</td>
      <td>0.8308</td>
    </tr>
    <tr>
      <td>LFPA</td>
      <td>−0.12</td>
      <td>−0.01</td>
      <td>−0.32</td>
      <td>0.34</td>
      <td>0.5302</td>
      <td>0.5698</td>
    </tr>
    <tr>
      <td>Groom</td>
      <td>0.03</td>
      <td>0.01</td>
      <td>−0.34</td>
      <td>0.34</td>
      <td>0.8680</td>
      <td>0.8844</td>
    </tr>
    <tr>
      <td>ForelimbOpenField</td>
      <td>−0.14</td>
      <td>0.01</td>
      <td>−0.32</td>
      <td>0.34</td>
      <td>0.4802</td>
      <td>0.5402</td>
    </tr>
    <tr>
      <td>BBB_FergTrans</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>−0.33</td>
      <td>0.33</td>
      <td>0.9900</td>
      <td>0.9900</td>
    </tr>
  </tbody>
</table>

R Code Box 3 permut_pc_test (pca, pca_data, p=1000, ndim = 3, statistic = 's.loadings', perm.method = 'permV').permut_pc_test (pca, pca_data, p=1000, ndim = 3, statistic = 'communa', perm.method = 'permV').

### Step 4: Component stability: how robust are the components?

The presence of a syndrome or disease pattern, represented by a component, should hold true regardless of variations in experiments or metrics meant to measure that same pattern. For example, two experiments with different subjects but the same collected variables should result in inferentially equivalent components if they are true features of the disease and not experimental artifacts. The sensitivity of PCs to experimental, metric, or other forms of variation is termed ‘component stability’. Components from different PCAs (from different experiments as an example) that are extremely similar are considered to be a stable, and characterizing component stability is important to determine the robustness of the initial PCA (Guadagnoli and Velicer, 1988; Linting, 2007). A robust PC would be largely unaffected by data variations (i.e. low sensitivity). The goal of the stability analysis is to determine such sensitivity.

Given that performing multiple replication experiments in biomedical research is not always possible, component stability can be approximated by resampling techniques such as bootstrapping (Babamoradi et al., 2013; Linting et al., 2007a; Timmerman et al., 2007; Zientek and Thompson, 2007). Bootstrap methods for component stability have been extensively studied, but users should be aware of the limitations and advantages of these methods and their performance for component stability depending on the use case (Babamoradi et al., 2013; Guadagnoli and Velicer, 1988; Linting et al., 2007b; Timmerman et al., 2007; Zientek and Thompson, 2007).

The package implements functionalities to help study the component stability affected by data selection variability by implementing bootstrapping methods (Babamoradi et al., 2013; Linting et al., 2007b; Timmerman et al., 2007; Zientek and Thompson, 2007) and stability metrics. The default method used in the package is the simple or ordinary bootstrap consisting of generating a new sample that has the same size (i.e. same number of subjects or observations) and same variables as the original data, but where the subjects have been randomly selected from the data with replacement (Figure 4A). This process is repeated several times (here referred as b times) to generate a sample of bootstrapped data. In the first case example, each of the b bootstrapped samples contain 159 subjects and 18 variables, but one subject might appear more than once and another subject might not show up in a specific sample.

![Figure 4.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig4-v2.jpg)

**Figure 4.:** (A) shows a schematic of the bootstrapping procedure where a bootstrap sample is generated by resampling the original samples as many times as there are samples in the original dataset but allowing for replacement. The bootstrapping algorithm for loadings is (B): for each of 1 to n bootstrap sample (b), run a PCA with the same specifications than the parent PCA on the original sample. The bootstrapping method (e.g. balanced bootstrap) can be specified with the sim argument passed to the boot() function of the boot R package. Then, the sample component loading is obtained from the PCA of the bootstrapped sample and a Procrustes rotation of the loading matrix is applied over the parent loading matrix to correct for PCA indeterminacies (C; see text). All b rotated loadings form the bootstrapped distribution of loadings. The component similarity of each b loading with the parent loading solution can be calculated to generate the bootstrapped distribution of component similarity. From these distributions, the average and confidence interval are estimated.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The pc_stability() and permut_pca_test() functions were run 10 times for different number of bootstrapped (A–C) and permuted (D–F) samples (10, 25, 50, 100, 250, 500, 750, 1000, 1500, or 2000) for two datasets with different sizes (n:rows x p:columns; 159 × 18 or 1590 × 54). The computation time (in seconds) increased linearly with the increase of samples, being the rate of increasement higher for the bigger dataset (A and D). The small margin of error for each condition (standard deviation) reflects the little effect of different runs (with different random generated numbers) on the computation time. The computed loading for a variable with high loading (~|0.75|) and another for low loading (~|0.25|) of the PC1 for each condition is shown in (B and E). As the sample size increases, the variability around the loading average decreases. The width of the 95% CI (based on t-distribution with 9 degrees of freedom) for each condition is shown (C and F) as measure of precision around the loading average estimate. The precision is smaller with the smaller size of the data, indicating that the uncertainty of the estimated averaged loading is affected by the data volume. The standard 1000 samples are a good compromise between computation time and precision of the estimated loadings for the big dataset, but smaller dataset might require bigger resamples.

Component stability can be studied at the whole component level or at the level of the individual variables through the loadings and communalities. The package implements component similarity indexes (aka factor matching indexes)(Cattell and Baggaley, 1960; Cattell et al., 1969; Guadagnoli and Velicer, 1991) as metrics to study the stability of PCs. These metrics can be used to determine the similarity between the different bootstrapped samples, to test the validity of the extracted component under two or more experimental conditions, to assess the multidimensional equivalence of two or more replication experiments, or to determine the impact of imputing missing values.

Case study: To understand the sensitivity of variables and components to experimental variations, we used the pc_stability() function with b = 1000 bootstrapped samples (R Code Box 4), setting the sim argument to ‘balanced’ to perform balanced bootstrapping. The function will return the average of the loadings and the specified similarity metric across all the b samples as well as the specified confidence interval. For this example, the 95% CI (accelerated and bias-corrected, see Materials and methods) and the bootstrapped average can be seen in Figure 5. In general, the original loadings are close to the bootstrapped average which indicates that the results are unbiased. Moreover, the confidence regions for most higher value loadings are reasonably small, suggesting that these loadings are stable to experimental variation. In addition, the similarity metrics for the three PCs suggest component stability, meaning that the composition of the components is also stable. The accepted values for these metrics indicating stability might vary by field and the metric of interest. Some indicative values are mentioned in the respective method section, but the user should be aware of subjective biases when determining a threshold for considering stability (Lorenzo-Seva and ten Berge, 2006). Finally, the function will return the average and percentile CI of the communalities, which can be used to assess which variables are more stable in the selected PCA solution.

![Figure 5.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig5-v2.jpg)

**Figure 5.:** Barmap plot of the bootstrap distribution of loadings (A) and communalities (B) representing the average and the 95% confidence interval of 3000 bootstrapped samples for the first three PCs. Assessing the confidence region offers an indicator of the uncertainty of the estimated loadings for each variable on each PC. Solid dots represent the mean of the bootstrap distribution and error bars represent the 95% CI.

R Code Box 4.

pc_stability (pca, pca_data, B = 1000, ndim = 3, s_cut_off = 0.1, test_similarity = T, similarity_metric = 'all', sim = 'balanced', barmap_plot = T).

Assessing the impact of imputation methods on introducing noise when dealing with missing data should be considered. As described earlier, we used multiple imputation to generate the dataset for analysis. Multiple imputation generates m complete datasets where the imputed values might vary, but the observed values are the same (in the case study m = 50). We used the stability analysis described above to determine the sensitivity of the PCA solution to variations introduced by imputing missing values. We calculated the similarity metrics between all the 50 imputed datasets for the first three PCs, as well as the loadings. We observed high similarities between the PCs obtained from the imputed datasets (Table 7) and the loadings showed narrow CIs (Figure 3—figure supplement 1). We concluded that multiple imputation has produced stable solutions with acceptable impact on both the component and variables. A future version of the package might include more robust methods for pooling and testing multiple imputation in PCA context (van Ginkel and Kroonenberg, 2014). Altogether, the results suggest reliable and robust PCs extracted from the original data.

**Table 7.**
 Similarity metrics of the first three PCs between 50 multiple imputed datasets for the first case study.Silent cutoff for S index was set at |0.2|.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">CC index</th>
      <th colspan="2">r index</th>
      <th colspan="2">RMSE</th>
      <th colspan="2">S index</th>
    </tr>
    <tr>
      <th>PC</th>
      <th>Mean</th>
      <th>SD</th>
      <th>Mean</th>
      <th>SD</th>
      <th>Mean</th>
      <th>SD</th>
      <th>Mean</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PC1</td>
      <td>0.999</td>
      <td>0.0003</td>
      <td>0.999</td>
      <td>0.0003</td>
      <td>0.021</td>
      <td>0.004</td>
      <td>0.991</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>PC2</td>
      <td>0.998</td>
      <td>0.0005</td>
      <td>0.998</td>
      <td>0.0005</td>
      <td>0.021</td>
      <td>0.004</td>
      <td>0.93</td>
      <td>0.042</td>
    </tr>
    <tr>
      <td>PC3</td>
      <td>0.997</td>
      <td>0.001</td>
      <td>0.996</td>
      <td>0.002</td>
      <td>0.022</td>
      <td>0.005</td>
      <td>0.965</td>
      <td>0.03</td>
    </tr>
  </tbody>
</table>

### Step 5: Component visualization

Communicating the analysis is a necessary part of the workflow. Although we have included this at the end of the use case, visualization can be also used for aiding in component selection, component interpretation and component stability analysis. There are several ways a PCA solution can be visualized. Here, we describe the plots implemented in the syndRomics package.

We have coded three types of plots (syndromics plot, heatmap, and barmap) using the grammar of the graphics framework (Wilkinson, 2005) implemented in R by the ggplot2 package. This allow users to customize the plots using the rich landscape of the ggplot2 universe. The syndromic plot was first published by Ferguson et al., 2013 and represents PCs as the center of a Venn diagram (Figure 1A), consisting of (1) a middle convex triangle displaying the ‘variance accounted for’ (VAF) for a given PC and (2) radial arrows pointing to the center of the triangle for each variable with a standardized loading above a certain threshold (Figure 6A–C). The width of each arrow and the color saturation are proportional to the magnitude of the standardized loading they represent. The color of each arrow additionally differentiates between positive or negative loadings (e.g. blue represents a loading of +1, red represents a loading of −1, and white represents a loading of 0). Syndromic plots are especially useful for conveying PC identity in an easy to understand, concise way for publication. Heatmap and barmap plots are alternative visualizations of the loadings beyond the syndromic plot. The major difference between these two plots and the syndromic plot is that both the barmap (Figure 5A) and heatmap (Figure 6D) plots display all variables (or a manually selected subset) instead of only the ones with loadings above a given threshold. The absolute loadings that exceed a cutoff threshold can be noted (e.g. by a star *). Moreover, in the case of barmap plots, the cutoff is represented in the graph by vertical lines. This is particularly useful when there are too many above-threshold variables, which would crowd the syndromic plot visualization, or when comparing loadings between PCs more easily. In addition, barmaps are useful for documenting the results of the resampling procedures since error bars can be used to represent the variation of the metrics over the resampling. The permut_pc_test() and pc_stability() functions return such plots.

![Figure 6.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig6-v2.jpg)

**Figure 6.:** (A–C) show the layout of the PC1, PC2, and PC3 syndromic plot of variables |loadings| > 0.45, respectively: arrows pointing the center of the plot representing the magnitude (arrow thickness and color saturation) and direction (color) of the loadings of selected variables. (D) illustrate an example of the same loading solution plotted by a heatmap. * Indicates variables with |loadings| > 0.21, 0.25 or 0.4 for PC1, PC2, and PC3, respectively.

Case study (R Code Box 5): We can visualize the three selected PCs using the plotting functions in syndRomics (Figure 6). In this case, we chose to represent PC1, PC2 and PC3 using the syndromics plots (Figure 6A, B and C, respectably) using a cutoff threshold of |0.45|. Notice that this is higher than the threshold for significance found by the permutation analysis given the high number of variables. The full loading pattern of the three first PCs can be visualized by a heatmap (Figure 6D), where we have chosen a different cutoff for each PC (0.21, 0.25, and 0.4 for PC1, PC2, and PC3 respectively), or a Barmap (Figures 3B and 5A). Barmaps can be obtained for the loadings (barmap_loadings()) or for the communalities (barmap_commun()).R Code Box 5syndromic_plot (pca, pca_data, cutoff = 0.45).heatmap_loading (pca, pca_data, ndim = 3, cutoff = c(0.21,0.25,0.4), star_values = T, text_values = F).

### Case study 2

In the second case study, we used selected variables from the Transforming Research And Clinical Knowledge in Traumatic Brain Injury (TRACK-TBI) pilot study (Yue et al., 2013) that were analyzed previously and made publicly available (Nielson et al., 2017). The released dataset version contains 586 de-identified human subjects who were enrolled in the TRACK-TBI pilot study and the 26 selected variables previously analyzed (Nielson et al., 2017). These variables are a subset of brain imaging results, outcome metrics and genetic polymorphism (Table 2). The goal is to describe patterns of association between these three categories of variables. A noticeable difference between this dataset and the one used in the first case study is that here we are dealing with a mixed type dataset, where some variables are continuous, some nominal and some ordinal. Therefore, we performed a version of nonlinear PCA that allows for the extraction of patterns in these kinds of data. The syndRomics package has been programmed to work with the results of the princals() function from the Gifi R package. The code for this analysis is found in the supplementary material.

Missing data analysis showed an overall 21.2% missingness distributed between the outcomes and genetic polymorphism variables (Figure 7—figure supplement 1). With the exception of ‘MRI results’ that has high missingness (61.7% of the observations), all imaging variables are complete. ‘MRI results’ variable was excluded from the analysis. The subsequent test for MCAR suggest that there are 17 different patterns of missingness and that the hypothesis of MCAR can be rejected overall (p-value<0.001). Thus, excluding subjects from the analysis is not justified (Schafer and Graham, 2002; Buuren, 2018). We instead performed 50 multiple imputations using the mice R package as in the first case study. The 50 imputed datasets where then aggregated to perform nonlinear PCA using princals() (see Materials and methods for details).

Permutation test of PC VAF suggests that the first 6 PCs contain information that can be regarded as significant above random chance. Although a deep analysis of these six PCs might be of interest, the first three PCs explain the major variance (25.6%, 10.6%, and 9.8%, respectively). Therefore, we focused on interpreting these for illustration purposes (Figure 7 and Tables 8–10). The first PC significantly loaded highly on two genetic variants in opposite directions (SNP_DRD2 loading = −0.677, SNP_ANKK1_Gly318AR loading = 0.661) as well as outcomes of neuropsychological function at 6 months after TBI (CVLT_long loading = −0.614, CVLT_short loading = −0.542)(Figure 7A–C). All other variables also significantly loaded on to PC1, but with |loadings| ~ 0.3 (Tables 8–10) suggesting that their contribution in PC1 identity is less important. Lower values in CVLT (California Verbal Learning Test) suggest learning and memory impairments, which are well known after TBI. Given the negative loadings for the included CVLT measures (short and long recall), negative values in PC1 might reflect better CVLT outcomes at 6 months after TBI. The stability of the PC1 pattern to multiple imputation is relatively low, with higher loadings showing high variation (Figure 7—figure supplement 1, Table 11), emphasizing the importance of studying stability of components to multiple imputation. Nonetheless, the bootstrapped loadings were stable (Figure 7B), and decay in CVLT performance after TBI has been previously associated to polymorphisms in DRD2 and ANKK1 genes (Failla et al., 2015; McAllister et al., 2008; Nielson et al., 2017; Yue et al., 2017), providing literature validation of PC1. The variables with higher positive loadings in PC2 were related to the imaging findings and negative loadings with global function outcomes at 3 and 6 months after TBI (GOSE score)(Figure 7. A, D). Lower scores in GOSE are indicative of lower global function and positive values in imaging findings are suggestive of a bigger or more noticeable brain damage. PC2 presented the higher stability to both resampling and to multiple imputation (Figure 7—figure supplement 1, Table 11). Altogether, PC2 might be interpreted as a surrogate for ‘TBI severity’, where higher positive values would indicate higher brain damage with less function at 3 and 6 months after injury, a signature described in the previous analysis of this data (Nielson et al., 2017). Finally, given the instability of PC3, with most loadings being considered non-significant by the permutation test and the high variance to multiple imputation (Figure 7—figure supplement 1, Table 11), PC3 can not be interpreted with certainty, and we should not attempt its explanation.

![Figure 7.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig7-v2.jpg)

**Figure 7.:** (A-B) show thebarmap plots for the loadings for the first three PCs with the 95% CI generated from 500 permutationand 1000 bootstrap resamples. (C-D) show the syndromic plots for the PC1 (VAF=25.8%) and PC2(VAF=10.6%) for |loading|>0.4. Error bars represent the 95%CI of the resampling method.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/61812/elife-61812-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Shadow plot of missing data for the variables selected for the case study. Approximately 22% are missing values. The fact that most missing values are across variables for the same subject (two biggest missing pattern sets) suggest data is missing at random (MAR), meaning there is an external reason to the observed values for that missing. In order to assess the stability of the PCA analysis by performing multiple imputation, we calculated the distribution of loadings generated by 50 multiple imputed datasets (B). Solid dots represent the mean of the multiple imputed loading distribution and error bars represent the 95% CI.

**Table 8.**
 PC1 loading results of permutation test for the second case study with 500 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original loading</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CT_brain_pathology</td>
      <td>0.440589</td>
      <td>0.010978</td>
      <td>−0.17606</td>
      <td>0.202095</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_cisterncomp</td>
      <td>0.1844</td>
      <td>0.003484</td>
      <td>−0.16947</td>
      <td>0.209801</td>
      <td>0.053892</td>
      <td>0.061591</td>
    </tr>
    <tr>
      <td>CT_contusion</td>
      <td>0.382612</td>
      <td>0.008019</td>
      <td>−0.17053</td>
      <td>0.187363</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_EDH</td>
      <td>0.256368</td>
      <td>0.015695</td>
      <td>−0.16239</td>
      <td>0.190167</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_facial_FX</td>
      <td>0.267322</td>
      <td>0.029918</td>
      <td>−0.16465</td>
      <td>0.202063</td>
      <td>0.011976</td>
      <td>0.015128</td>
    </tr>
    <tr>
      <td>CT_Marshall</td>
      <td>0.235242</td>
      <td>0.003685</td>
      <td>−0.16912</td>
      <td>0.191229</td>
      <td>0.00998</td>
      <td>0.013307</td>
    </tr>
    <tr>
      <td>CT_midlineshift</td>
      <td>0.002539</td>
      <td>−0.01082</td>
      <td>−0.2005</td>
      <td>0.190956</td>
      <td>0.988024</td>
      <td>0.988024</td>
    </tr>
    <tr>
      <td>CT_Rotterdam</td>
      <td>0.274699</td>
      <td>0.010723</td>
      <td>−0.17176</td>
      <td>0.195646</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_SAH</td>
      <td>0.376596</td>
      <td>0.009848</td>
      <td>−0.16185</td>
      <td>0.191671</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_SDH</td>
      <td>0.377542</td>
      <td>0.018196</td>
      <td>−0.15488</td>
      <td>0.196538</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_skull_FX</td>
      <td>0.404447</td>
      <td>0.020049</td>
      <td>−0.15398</td>
      <td>0.198067</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CT_skullbase_FX</td>
      <td>0.318179</td>
      <td>0.019653</td>
      <td>−0.18691</td>
      <td>0.195547</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CVLT_long_6mo</td>
      <td>−0.70622</td>
      <td>−0.05218</td>
      <td>−0.37582</td>
      <td>0.295769</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>CVLT_short_6mo</td>
      <td>−0.63345</td>
      <td>−0.04306</td>
      <td>−0.378</td>
      <td>0.258602</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>GOSE_3mo</td>
      <td>−0.32848</td>
      <td>−0.00894</td>
      <td>−0.17465</td>
      <td>0.177456</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>GOSE_6mo</td>
      <td>−0.25329</td>
      <td>−0.00613</td>
      <td>−0.19298</td>
      <td>0.176343</td>
      <td>0.003992</td>
      <td>0.005988</td>
    </tr>
    <tr>
      <td>PTSD_diagnosis_6mo</td>
      <td>0.188743</td>
      <td>0.013079</td>
      <td>−0.15885</td>
      <td>0.190364</td>
      <td>0.041916</td>
      <td>0.050299</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Glu713Lys</td>
      <td>0.358071</td>
      <td>0.028077</td>
      <td>−0.14647</td>
      <td>0.190965</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly318Arg</td>
      <td>0.613624</td>
      <td>0.043104</td>
      <td>−0.17747</td>
      <td>0.244082</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly442Arg</td>
      <td>−0.25194</td>
      <td>−0.02327</td>
      <td>−0.19756</td>
      <td>0.16577</td>
      <td>0.005988</td>
      <td>0.008454</td>
    </tr>
    <tr>
      <td>SNP_COMT</td>
      <td>0.036687</td>
      <td>0.001474</td>
      <td>−0.17511</td>
      <td>0.172543</td>
      <td>0.696607</td>
      <td>0.726894</td>
    </tr>
    <tr>
      <td>SNP_DRD2</td>
      <td>−0.62858</td>
      <td>−0.05017</td>
      <td>−0.24105</td>
      <td>0.168359</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
    <tr>
      <td>SNP_PARP1</td>
      <td>−0.05912</td>
      <td>−0.00576</td>
      <td>−0.18101</td>
      <td>0.166475</td>
      <td>0.512974</td>
      <td>0.559608</td>
    </tr>
    <tr>
      <td>WAIS_PSI_6mo</td>
      <td>−0.36179</td>
      <td>−0.0144</td>
      <td>−0.19646</td>
      <td>0.168075</td>
      <td>0.001996</td>
      <td>0.003194</td>
    </tr>
  </tbody>
</table>

**Table 9.**
 PC2 loading results of permutation test for the second case study with 500 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original loading</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CT_brain_pathology</td>
      <td>0.662378</td>
      <td>0.021655</td>
      <td>−0.12084</td>
      <td>0.158839</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_cisterncomp</td>
      <td>0.709989</td>
      <td>0.024823</td>
      <td>−0.14181</td>
      <td>0.178126</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_contusion</td>
      <td>0.596311</td>
      <td>0.01766</td>
      <td>−0.12222</td>
      <td>0.157785</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_EDH</td>
      <td>0.253079</td>
      <td>0.002735</td>
      <td>−0.13662</td>
      <td>0.135348</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_facial_FX</td>
      <td>0.142602</td>
      <td>0.000971</td>
      <td>−0.12466</td>
      <td>0.133574</td>
      <td>0.041916</td>
      <td>0.055888</td>
    </tr>
    <tr>
      <td>CT_Marshall</td>
      <td>0.809847</td>
      <td>0.026415</td>
      <td>−0.13438</td>
      <td>0.173771</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_midlineshift</td>
      <td>0.69605</td>
      <td>0.034813</td>
      <td>−0.12917</td>
      <td>0.189917</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_Rotterdam</td>
      <td>0.753498</td>
      <td>0.01539</td>
      <td>−0.13205</td>
      <td>0.178638</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_SAH</td>
      <td>0.689084</td>
      <td>0.017617</td>
      <td>−0.12425</td>
      <td>0.155246</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_SDH</td>
      <td>0.698728</td>
      <td>0.017798</td>
      <td>−0.12057</td>
      <td>0.161901</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_skull_FX</td>
      <td>0.493199</td>
      <td>0.007764</td>
      <td>−0.13921</td>
      <td>0.161888</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CT_skullbase_FX</td>
      <td>0.294691</td>
      <td>0.003769</td>
      <td>−0.12863</td>
      <td>0.141375</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>CVLT_long_6mo</td>
      <td>0.056095</td>
      <td>0.019229</td>
      <td>−0.21544</td>
      <td>0.23499</td>
      <td>0.674651</td>
      <td>0.703983</td>
    </tr>
    <tr>
      <td>CVLT_short_6mo</td>
      <td>0.115663</td>
      <td>0.020014</td>
      <td>−0.20152</td>
      <td>0.215121</td>
      <td>0.353293</td>
      <td>0.423952</td>
    </tr>
    <tr>
      <td>GOSE_3mo</td>
      <td>−0.43692</td>
      <td>−0.00787</td>
      <td>−0.14301</td>
      <td>0.139508</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>GOSE_6mo</td>
      <td>−0.40155</td>
      <td>−0.00849</td>
      <td>−0.14484</td>
      <td>0.118386</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>PTSD_diagnosis_6mo</td>
      <td>0.004807</td>
      <td>−0.00863</td>
      <td>−0.14863</td>
      <td>0.140418</td>
      <td>0.94012</td>
      <td>0.94012</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Glu713Lys</td>
      <td>−0.26204</td>
      <td>−0.01604</td>
      <td>−0.15757</td>
      <td>0.132164</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly318Arg</td>
      <td>−0.28622</td>
      <td>−0.01954</td>
      <td>−0.15986</td>
      <td>0.133637</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly442Arg</td>
      <td>0.033308</td>
      <td>−0.00308</td>
      <td>−0.12662</td>
      <td>0.129371</td>
      <td>0.630739</td>
      <td>0.688078</td>
    </tr>
    <tr>
      <td>SNP_COMT</td>
      <td>−0.0406</td>
      <td>−0.00094</td>
      <td>−0.14047</td>
      <td>0.140783</td>
      <td>0.588822</td>
      <td>0.67294</td>
    </tr>
    <tr>
      <td>SNP_DRD2</td>
      <td>0.307457</td>
      <td>0.023806</td>
      <td>−0.11549</td>
      <td>0.178777</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>SNP_PARP1</td>
      <td>0.244246</td>
      <td>0.000876</td>
      <td>−0.14801</td>
      <td>0.133131</td>
      <td>0.001996</td>
      <td>0.002818</td>
    </tr>
    <tr>
      <td>WAIS_PSI_6mo</td>
      <td>−0.13252</td>
      <td>0.001279</td>
      <td>−0.13167</td>
      <td>0.134985</td>
      <td>0.055888</td>
      <td>0.070596</td>
    </tr>
  </tbody>
</table>

**Table 10.**
 PC3 loading results of permutation test for the second case study with 500 random permutations using permV and adjusting p values with BH.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Original loading</th>
      <th>Permuted average</th>
      <th>Lower 95% CI</th>
      <th>Upper 95% CI</th>
      <th>p value</th>
      <th>Adjusted p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CT_brain_pathology</td>
      <td>0.110149</td>
      <td>0.002819</td>
      <td>−0.30242</td>
      <td>0.309376</td>
      <td>0.528942</td>
      <td>0.641916</td>
    </tr>
    <tr>
      <td>CT_cisterncomp</td>
      <td>−0.32449</td>
      <td>−0.00334</td>
      <td>−0.33379</td>
      <td>0.305672</td>
      <td>0.047904</td>
      <td>0.13839</td>
    </tr>
    <tr>
      <td>CT_contusion</td>
      <td>0.060972</td>
      <td>−0.00689</td>
      <td>−0.31444</td>
      <td>0.270176</td>
      <td>0.698603</td>
      <td>0.728977</td>
    </tr>
    <tr>
      <td>CT_EDH</td>
      <td>0.104859</td>
      <td>−0.00125</td>
      <td>−0.27352</td>
      <td>0.321535</td>
      <td>0.518962</td>
      <td>0.641916</td>
    </tr>
    <tr>
      <td>CT_facial_FX</td>
      <td>0.371649</td>
      <td>0.062687</td>
      <td>−0.31692</td>
      <td>0.355691</td>
      <td>0.01996</td>
      <td>0.07984</td>
    </tr>
    <tr>
      <td>CT_Marshall</td>
      <td>−0.24284</td>
      <td>−0.01023</td>
      <td>−0.3038</td>
      <td>0.288171</td>
      <td>0.129741</td>
      <td>0.259481</td>
    </tr>
    <tr>
      <td>CT_midlineshift</td>
      <td>−0.30562</td>
      <td>−0.01988</td>
      <td>−0.32888</td>
      <td>0.308785</td>
      <td>0.063872</td>
      <td>0.153293</td>
    </tr>
    <tr>
      <td>CT_Rotterdam</td>
      <td>−0.24002</td>
      <td>−0.01377</td>
      <td>−0.32884</td>
      <td>0.292959</td>
      <td>0.161677</td>
      <td>0.284003</td>
    </tr>
    <tr>
      <td>CT_SAH</td>
      <td>0.16969</td>
      <td>−0.0017</td>
      <td>−0.30469</td>
      <td>0.323896</td>
      <td>0.347305</td>
      <td>0.520958</td>
    </tr>
    <tr>
      <td>CT_SDH</td>
      <td>0.164146</td>
      <td>0.011718</td>
      <td>−0.33537</td>
      <td>0.308091</td>
      <td>0.339321</td>
      <td>0.520958</td>
    </tr>
    <tr>
      <td>CT_skull_FX</td>
      <td>0.30911</td>
      <td>0.013422</td>
      <td>−0.28309</td>
      <td>0.317483</td>
      <td>0.047904</td>
      <td>0.13839</td>
    </tr>
    <tr>
      <td>CT_skullbase_FX</td>
      <td>0.412507</td>
      <td>0.027909</td>
      <td>−0.29748</td>
      <td>0.350075</td>
      <td>0.005988</td>
      <td>0.047904</td>
    </tr>
    <tr>
      <td>CVLT_long_6mo</td>
      <td>0.071561</td>
      <td>0.007602</td>
      <td>−0.26795</td>
      <td>0.330045</td>
      <td>0.662675</td>
      <td>0.722918</td>
    </tr>
    <tr>
      <td>CVLT_short_6mo</td>
      <td>0.01478</td>
      <td>0.003403</td>
      <td>−0.29415</td>
      <td>0.341327</td>
      <td>0.922156</td>
      <td>0.922156</td>
    </tr>
    <tr>
      <td>GOSE_3mo</td>
      <td>0.512173</td>
      <td>0.027225</td>
      <td>−0.3035</td>
      <td>0.347452</td>
      <td>0.001996</td>
      <td>0.023952</td>
    </tr>
    <tr>
      <td>GOSE_6mo</td>
      <td>0.519654</td>
      <td>0.030422</td>
      <td>−0.28179</td>
      <td>0.361045</td>
      <td>0.001996</td>
      <td>0.023952</td>
    </tr>
    <tr>
      <td>PTSD_diagnosis_6mo</td>
      <td>−0.29067</td>
      <td>−0.02728</td>
      <td>−0.31023</td>
      <td>0.227907</td>
      <td>0.051896</td>
      <td>0.13839</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Glu713Lys</td>
      <td>−0.47272</td>
      <td>−0.02347</td>
      <td>−0.40038</td>
      <td>0.368874</td>
      <td>0.007984</td>
      <td>0.047904</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly318Arg</td>
      <td>−0.14092</td>
      <td>−0.02104</td>
      <td>−0.34164</td>
      <td>0.27799</td>
      <td>0.379242</td>
      <td>0.5354</td>
    </tr>
    <tr>
      <td>SNP_ANKK1_Gly442Arg</td>
      <td>−0.34766</td>
      <td>−0.02656</td>
      <td>−0.38332</td>
      <td>0.353987</td>
      <td>0.083832</td>
      <td>0.182907</td>
    </tr>
    <tr>
      <td>SNP_COMT</td>
      <td>−0.10171</td>
      <td>0.001249</td>
      <td>−0.26635</td>
      <td>0.284647</td>
      <td>0.53493</td>
      <td>0.641916</td>
    </tr>
    <tr>
      <td>SNP_DRD2</td>
      <td>0.081296</td>
      <td>0.013862</td>
      <td>−0.2912</td>
      <td>0.323114</td>
      <td>0.61477</td>
      <td>0.702595</td>
    </tr>
    <tr>
      <td>SNP_PARP1</td>
      <td>0.233007</td>
      <td>0.010172</td>
      <td>−0.29054</td>
      <td>0.318385</td>
      <td>0.165669</td>
      <td>0.284003</td>
    </tr>
    <tr>
      <td>WAIS_PSI_6mo</td>
      <td>0.39706</td>
      <td>0.017391</td>
      <td>−0.27022</td>
      <td>0.337713</td>
      <td>0.011976</td>
      <td>0.057485</td>
    </tr>
  </tbody>
</table>

**Table 11.**
 Similarity metrics of the first 3PCs between 50 multiple imputed datasets for the second case study.Silent cutoff for S index was set at |0.2|.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">CC index</th>
      <th colspan="2">r index</th>
      <th colspan="2">RMSE</th>
      <th colspan="2">S index</th>
    </tr>
    <tr>
      <th>PC</th>
      <th>Mean</th>
      <th>SD</th>
      <th>Mean</th>
      <th>SD</th>
      <th>Mean</th>
      <th>SD</th>
      <th>Mean</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PC1</td>
      <td>0.955</td>
      <td>0.035</td>
      <td>0.958</td>
      <td>0.033</td>
      <td>0.094</td>
      <td>0.06</td>
      <td>0.88</td>
      <td>0.037</td>
    </tr>
    <tr>
      <td>PC2</td>
      <td>0.992</td>
      <td>0.004</td>
      <td>0.991</td>
      <td>0.0054</td>
      <td>0.056</td>
      <td>0.039</td>
      <td>0.93</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>PC3</td>
      <td>0.87</td>
      <td>0.097</td>
      <td>0.874</td>
      <td>0.097</td>
      <td>0.133</td>
      <td>0.127</td>
      <td>0.71</td>
      <td>0.06</td>
    </tr>
  </tbody>
</table>

## Discussion

Biomedical research needs more multivariate analytics to help realize the potential of precision medicine. While multiple variables are collected in typical preclinical experiments and clinical trials, univariate statistics continue to be the major analytical and decision-making approaches across the different biomedical fields, narrowing our understanding of the complexity of any disease. With the advent of ‘omics’, analytical approaches for high-dimensional data have started to become more prevalent for the analysis of biological data. Yet, outside the realm of medical bioinformatics, biomedical research continues to be, for most part univariate. The lack of multivariate approaches in analyzing biomedical data can cause biases and constraints to the interpretation of the results and contribute to the lack of reproducibility and bench-to-bedside translation (Ferguson et al., 2011; Huie et al., 2018).

The extraction of disease space, through the use of multivariate methods, can increase our understanding of complex relationships commonly present in biomedical data while preventing some of the issues associated with an excessive use of univariate analytics such as multiple comparison testing and associated false discoveries by chance (Benjamini and Hochberg, 1995; Ferguson et al., 2013; Krzywinski and Altman, 2014). For example, it is common in biomedicine to measure several behavioral and histopathological outcomes that are analyzed independently at the univariate level. This approach increases the chance of false-positive results due to the accumulation of type I testing errors (Benjamini and Hochberg, 1995; Dunn, 1961; Krzywinski and Altman, 2014). Although there are methods to correct for errors when running numerous tests such as multiple-testing correction, their use in biomedicine outside of bioinformatic analysis is scarce. Even when correcting for multiple testing, performing several univariate analyses limits our understanding since univariate analysis does not allow us to study and infer the relationship between measures that might capture different aspects of the matter of study. In our first example case study, several functional tests can be used to study the recovery of forelimb motor function after cervical spinal cord injury in animal models. Each test further contains multiple measures about particular aspects of recovery. Knowing the relationship between these measures through multivariate approaches can increase our understanding of the matter of study while reducing the burden of multiple testing (Ferguson et al., 2013). Importantly, it is also possible that a single univariate test that does not produce significant results misses true biological effects, while a multivariate analysis including the same variables can find patterns and relationship between variables that are significant. Syndromic analysis is, therefore, a framework that uses multivariate analysis of biomedical data in a holistic way, aiming to reveal interactions within complex (patho)-physiological niches, that would be otherwise challenging to discern. Applying syndromic analysis to biomedical data will help uncover the complex relationships of variables and features that constitute different disease and biological states and ultimately accelerate research toward precision medicine.

The syndRomics package implements several functionalities for the visualization, the interpretation, and the analysis of the stability of principal components to facilitate the extraction and analysis of disease patterns. We have demonstrated its usage, showing the potential of the package to support PCA-based analysis in understanding disease complexity. Although the core functionalities of the package are included, future versions might also implement outputs from other PCA functions as inputs, such as those from the PCA functions in the FactoMineR package (Lê et al., 2008) or the psych package (Revelle, 2017), allowing for better integration to the PCA landscape in R. In addition, other algorithms of bootstrapping and permutation methods for PCA solutions could be incorporated to increase the options and better adapt to the specifics needs of the user (Hong et al., 2006; Linting et al., 2011; Vitale et al., 2017; Zientek and Thompson, 2007).

Here, we emphasize guidance and tools for robust determination of PCA-based disease patterns. We have incorporated resampling methods aiming to reduce subjective biases and to study the stability and generality of the analysis. Although we have shown the use of these functions in different contexts along the process, much more work can be done to extend syndRomics. For example, we demonstrated the stability of our analysis under multiple imputation, and future research could investigate number of multiple imputations or missing conditions necessary for stable disease pattern detection. In addition, visualization features of syndRomics may be extended to help interpret disease patterns resolved by other multivariate or machine learning tools involving structure coefficients or feature impact scores. The syndRomics resampling methods could also be used to estimate the sample size required for stable PCs in the context of syndromic analysis, allowing for sample planning. The implementations in the package are thus positioned to empower both biological and statistical research toward understanding complex biology and diseases.

## Materials and methods

### Availability and requirements

The code to reproduce this analysis can be found in the supplementary material. The data for the first use case comes from the ODC-SCI (Open Data Commons for Spinal Cord Injury, RRID:SCR_016673, http://odc-sci.org), ODC-SCI:26 dataset (https://scicrunch.org/odc-sci/about/odc-sci_26). The data for the second use case comes from TRACK-SCI and can be downloaded from 10.1371/journal.pone.0169490. The package can be installed from GitHub (https://github.com/ucsf-ferguson-lab/syndRomics) where installation instructions, package manual and examples of usage are provided. Descriptions of the arguments and function usage can be found in the internal package documentation once installed or in the package manual. The package has been implemented in R (R Development Core Team, 2019) through RStudio (Team RS, 2018) using a few other packages beyond the ones bundled in R as dependencies: dplyr (Wickham et al., 2018), ggplot2 (Wickham, 2016), stringr (Wickham, 2019), tidyr (Wickham and Henry, 2020), ggrepel (Slowikowski, 2019), ggnewscale (Elio Campitelli, 2020), pracma (Borchers, 2019), png (Urbanek, 2013), boot (Canty and Ripley, 2019; Davison and Hinkley, 1997), rlang (Henry and Wickham, 2020), and Gifi (Mair and Leeuw, 2019).

### Package implementation

The syndRomics package offers two major functionalities for the purpose of aiding in the process of syndromics analysis: (1) visualization functions and (2) functions incorporating resampling methods to determine stability and inference of PCs.

### Visualization functions

The visualization functions are: syndromic_plot(), heatmap_loadings(), barmap_loadings(), barmap_commun() and VAF_plot(). For the visualization functions, the user can pass an R data.frame object with the standardized loadings (or other metrics) obtained by running PCA and related multivariate methods in their preferred software. We opted for this approach to avoid requiring specific implementations of PCA. Loadings obtained from any PCA solution can be easily formatted for usage with the syndRomics visualization functions. All functions in the package that takes a data frame as argument use the same format (Table 12): variables are organized as rows, and the first column is called ‘Variables’ and contains the names of the respective variables. The other columns contain the PC loadings and are named ‘PC1’, ‘PC2’, etc. Alternatively, the visualizations can also be obtained from the output of the prcomp() function in the stats package in R (linear PCA) or from the output of the princals() function in the Gifi package in R (non-linear PCA by categorical PCA). Finally, the results from pc_stability() and permut_pc_test() can be passed to the plot() generic function in R as the package incorporate the corresponding S3 method for ‘syndromics’ class object.

**Table 12.**
 Template/example of data.frame containing loadings that can be passed to the visualization functions (only the loadings for the first three PCs are shown).


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>PC1</th>
      <th>PC2</th>
      <th>PC3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>wtChng</td>
      <td>−0.34</td>
      <td>−0.37</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>TotalSubscore</td>
      <td>−0.56</td>
      <td>−0.48</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td>StepDistRH</td>
      <td>0.89</td>
      <td>−0.07</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>StepDistRF</td>
      <td>−0.65</td>
      <td>0.28</td>
      <td>−0.19</td>
    </tr>
    <tr>
      <td>StepDistLH</td>
      <td>−0.28</td>
      <td>−0.66</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>StepDistLF</td>
      <td>0.54</td>
      <td>0.27</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>RHSL</td>
      <td>−0.76</td>
      <td>0.34</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>RHPA</td>
      <td>−0.85</td>
      <td>−0.30</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>RFSL</td>
      <td>0.74</td>
      <td>0.40</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>RFPA</td>
      <td>−0.25</td>
      <td>0.21</td>
      <td>0.41</td>
    </tr>
    <tr>
      <td>PawPL</td>
      <td>−0.76</td>
      <td>−0.30</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>LHSL</td>
      <td>0.62</td>
      <td>0.42</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>LHPA</td>
      <td>−0.24</td>
      <td>0.12</td>
      <td>0.62</td>
    </tr>
    <tr>
      <td>LFSL</td>
      <td>0.38</td>
      <td>−0.62</td>
      <td>−0.05</td>
    </tr>
    <tr>
      <td>LFPA</td>
      <td>−0.54</td>
      <td>0.63</td>
      <td>−0.12</td>
    </tr>
    <tr>
      <td>Groom</td>
      <td>0.49</td>
      <td>−0.65</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>ForelimbOpenField</td>
      <td>0.20</td>
      <td>−0.59</td>
      <td>−0.14</td>
    </tr>
    <tr>
      <td>BBB_FergTrans</td>
      <td>0.51</td>
      <td>−0.32</td>
      <td>−0.03</td>
    </tr>
  </tbody>
</table>

#### syndromic_plot ()

The list of arguments for the syndromic_plot() function are presented in the package manual. The syndromic_plot() function will internally call extract_syndromic_plot() function (see utility functions) and return a list of ggplot2 objects containing the syndromic plot for the first ndim PCs. For example, if ndim = 5, a syndromic plot for PCs 1 to 5 will be generated. Another important argument is the cut_off, which determines the threshold of absolute standardized loadings to consider for plotting. This argument is chosen by the user and is required (with no default). Another required argument is VAF in case the syndromic_plot() function is called using a data.frame input. If the output of the prcomp() or princals() functions is used, the syndromic_plot() function extracts VAF internally and the user-defined VAF will be ignored. When required, VAF is a character vector of the form ‘XX%”,”XX%”, etc., where XX is the VAF for each PC to plot, starting with the first PC, followed by the second, etc. (e.g. c(‘60.1%”,”25.3%”) for PC1 and PC2, respectively). An issue we found during the implementation is that the arrow visualization does not display correctly in the R graphical device on Windows machines. Rendering the plot into *.pdf format, for instance using the ggsave() function from the ggplot2 package, solves the problem.

#### heatmap_loadings(), barmap_loadings() and barmap_commun()

Most of the functionalities described for the syndromic_plot() function also apply for the heatmap_loading(), the barmap_loading(), and the barmap_commun() functions. A noticeable difference in barmap_loading() is that the function will plot the PCs specified in ndim instead of the first ndim components. For example, if ndim = c(3,4,5), components 3, 4, and 5 will be plotted. This allows for more flexibility on which components to plot, such as isolating a single component (e.g. ndim = 3 will only plot component 3).

#### VAF_plot()

This function can be used to plot a VAF plot from a prcomp() or princals() output. There are two style options, ‘line’ or ‘reduced’.

### Resampling functions

There are two major functions using resampling methods, the permut_pc_test() function that implements nonparametric permutation test for either PC VAF for aiding in component selection or PC loadings and communalities for aiding in component interpretation, and the pc_stability() function that implements bootstrapping of PC loadings for stability analysis. These functions take as input the output of the prcomp() or the princals() functions in R as well as the original dataset used on these functions as inputs. The specific call of prcomp() or the princals() used to obtain the original PCA solution is passed down to the resampling functions in the syndRomics package, ensuring that the same arguments are used for resampling (with the exception of the data argument on the original prcomp() or the princals() call, that will be internally changed for each resampling iteration).

#### permut_pc_test()

In the syndRomics package, the null distribution for the permutation test is generated by permuting the values of each variable independently and concomitantly several times (permD) or permuting one variable at the time (permV) and re-running the PCA on each permuted sample (Figure 2; Buja and Eyuboglu, 1992; Glorfeld, 1995; Linting et al., 2011). When permV method is selected to measure the impact of permuting on loadings, a step of Procrustes rotation of each loading matrix toward the original loading matrix is added to resolve sign reflection, rotation indeterminacy and component translocation (Figure 2D, see pc_stability for detailed explanation). This step is not performed when the analysis is performed on the communalities since are invariant to such PCA resampling issues (Linting et al., 2011). Confidence intervals of the permuted distribution (null distribution) are calculated using the (1-α)x100% (percentile) of the distribution (Buja and Eyuboglu, 1992).

The function calls the permut_pca_D() or permut_pca_V() utility generic function internally to generate the permuted distribution of the selected metric (either “VAF”,“s.loadings” or “comuna”) using either the prcomp() function for linear PCA or the princals() function for nonlinear PCA implemented as S3 R method for the class “prcomp” or “princals”. If “VAF” is specified the permD permutation will be used, ignoring the input of the user on the perm.method argument, returning a matrix containing the VAF for the original PCs, as well as the average and the CI of the permuted VAF distribution. In case “s. loadings” or “communa” are specified, the specified permutation method will be considered (i.e. permD or permV) and the function will return a list of matrices, one for each selected PC, with the original loadings, and the average and CI of the permuted loadings distribution. In both cases, p values are calculated as described in the main text and returned. Adjusted p values using the specified method in the adjust.method argument are also returned.

#### pc_stability()

Component stability can be studied at the whole component level, known as factor invariance, or at the level of the individual loadings. We have implemented both options in the package. By default, the pc_stability() function returns the average and the accelerated and bias-corrected 95% confidence intervals (CI) of the loadings of the bootstrap distribution (Efron, 1987). Depending on the sample size and the number of chosen resamples, the bias-corrected CI will fail and the percentile (1-α)x100% CI will be returned (with corresponding notification). In addition, component similarity or factor matching metrics can be computed by setting the test_similarity=TRUE, which will call the component_similarity() function. For each of the specified similarity metrics, this function returns the average of the metric and its confidence interval (95% CI by default) by the percentiles of the bootstrap distribution. The confidence level and the CI method for the loadings can be changed by changing the conf and ci_type arguments. The function uses the boot() function for generating the bootstrapped samples and the boot.ci() function for extracting the confidence intervals of the loadings. Both boot() and boot.ci() are from the boot package in R. This allows the use of different bootstrapping strategies such as simple or ordinary bootstrapping (by default) or balanced bootstrapping. The reader is referred to the boot package documentation for more details on the different sim methods.

A major problem of performing resampling procedures in PCA is what is known as indeterminacies that can invalidate comparing between bootstrapped samples (Babamoradi et al., 2013; Chan et al., 1999; Linting, 2007; Timmerman et al., 2007; Zabala and Pascual, 2016). Sign reflection refers to the change of sign on the component loadings in a PC given slight variation of the data. In addition, slight data variation can also cause component/factor translocation, the change in the position of a component in the PCA solution (e.g. PC1 shifts to the position of PC2), especially when two components have similar VAF. Another problem on performing PCAs with variations in the data is the possibility of rotation indeterminacy when the PCA solution of a resampled data presents with a different rotation of the original PCA solution. These issues generate artificially biased bootstrapped distributions, potentially invalidating the procedure (Timmerman et al., 2007; Zientek and Thompson, 2007). We have implemented a step of procrustes rotation between the original loadings (target) and the bootstrapped sample, as has been previously demonstrated to be a reasonable method to deal with such issues (Timmerman et al., 2007; Zientek and Thompson, 2007). The Procrustes rotation is obtained by the procrustes() function from the pracma package. The algorithm for bootstrapping the PCA solutions is represented in Figure 4 and implemented in the utility function boot_pca_sample(). The number of bootstrap samples is set to 1000 by default. The user must be careful on setting the number too low, reducing the performance of the approximation (Efron, 1987). However, setting the number of bootstrap samples too high might unnecessarily increase computing time with little gain (Figure 4—figure supplement 1).

### Indexes of component similarity

We have included several component similarity indexes for determining component/factor invariance in syndRomics. The function component_similiarity () returns the specified similarity metrics as well as their summary statistics (average and standard deviation, if applicable) from a list of loading matrices (load.list). The argument s_cut_off is used in the calculation of the Cattell’s s index (see below) and ndim is used to limit the number of components from which to compute the indexes from. Each index has been programmed in a separate utility function for convenience. Although they are not meant to be manually called, users can call them to calculate any of these metrics for a given set of two component loadings. The similarity_metric argument takes a single character or a vector of characters to specify which metrics to compute. These can be: ‘cc_index’, ‘r_correlation’, ‘rmse’ and/or ‘s_index’. The user can also specify ‘all’ to get all metrics. Their definitions are documented below.

#### Congruence coefficient (CC, ‘cc_index’)

First suggested by Burt, 1948, it was popularized by Tucker, 1951 and therefore is also known as Tucker’s congruence coefficient. It is calculated as (2):

$$
ϕ_{x,y}=\frac{\sumi=1nx_{i}y_{i}}{\sqrt{\sumi=1nx_{i}^{2}}\sqrt{\sumi=1ny_{i}^{2}}}
$$

where $x_{i}$ and $y_{i}$ are the loadings of the variable $i$ on the component or factor $x$ and $y$ respectively. $∅x,y$ is equivalent to the cosine of the angle between two vectors and is also referred to as the cosine similarity metric. CC is a measure of proportional similarity between two components, and technically the index has a range from -1 (perfect negative congruence) to 1 (perfect positive congruence). In practice, because the all the loadings of a PC can be multiplied by -1 without changing the meaning of the PC, the absolute value of CC is considered, which correspondingly ranges from 0 to 1. The closer to 1, the more similar the two components are. Chan et al. discussed the 0.9 rule of thumb as an indicator of good matching between PCs (Chan et al., 1999). The application of CC as a similarity metric for factor invariance has been extensively studied (Chan et al., 1999; Lorenzo-Seva and ten Berge, 2006).

#### Pearson’s correlation coefficient (r, ‘r_correlation’)

The calculation of r between two vectors of component loadings has also been used as a pattern matching metric (Guadagnoli and Velicer, 1991). It is computed as (3):

$$
r_{x,y}=\frac{\sumi=1nx_{i}-x-y_{i}-y-}{\sqrt{\sumi=1nx_{i}-x-^{2}}\sqrt{\sumi=1ny_{i}-y-^{2}}}
$$

In the syndRomics package, the Pearson’s correlation coefficient is calculated using the cor() function of the stats package.

#### Root mean square error (RMSE, ‘rmse’)

RMSE has also been used as a metric for factor matching (Guadagnoli and Velicer, 1991). It is calculated as the square root of the average squared difference of the loadings of the variables as (4):

$$
RMSE_{x,y}=\sqrt{\frac{\sumi=1nx_{i}-y_{i}^{2}}{n}}
$$

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">Component 2</th>
    </tr>
    <tr>
      <th>Component 1</th>
      <th>PS</th>
      <th>H</th>
      <th>NS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PS</td>
      <td>f11</td>
      <td>f12</td>
      <td>f13</td>
    </tr>
    <tr>
      <td>H</td>
      <td>f21</td>
      <td>f22</td>
      <td>f23</td>
    </tr>
    <tr>
      <td>NS</td>
      <td>f31</td>
      <td>f32</td>
      <td>f33</td>
    </tr>
  </tbody>
</table>

where $n$ is the number of variables in both components $x$ and $y$. A RMSE of 0 determines a perfect matching, and therefore the smaller the RMSE is, the more equivalent the two components $x$ and $y$ are.

#### Cattell’s s index (‘s_index’)

The s index was first suggested by Cattell and Baggaley, 1960; Cattell et al., 1969. It is based on the factor mandate matrix (Cattell and Baggaley, 1960) where loadings are either one if a component is considered to act on a variable, called a salient variable, or 0 if not (forming the hyperplane space). Cattell’s suggested an arbitrary ± 0.1 cutoff where variables with loadings outside the cutoff range are removed from the hyperplane and considered to be salient variables. In practice, one might want to alter the threshold depending on the experimental conditions. Any loading inside the cutoff range is then interpreted as having been produced by chance. The s index is calculated from the cross-classification of the common variables of two components/factors:

where PS = positive salient variable; H = hyperplane variable; NS = negative salient variable; $f_{ij}$ is the joint frequency. Positive and negative salient variables are variables outside the cutoff range with positive or negative loadings respectively.

Pattern matching is determined by comparing the cell frequencies in the cross-classification table. Here we implement the simplified form of calculating s (5):

$$
s=\frac{f_{11}+f_{33}-f_{13}-f_{31}}{f_{11}+f_{33}+f_{13}+f_{31}+\frac{1}{2}f_{12}+f_{21}+f_{23}+f_{32}}
$$

The reader is referred to Cattell and Baggaley, 1960; Cattell et al., 1969; Guadagnoli and Velicer, 1991 for details on reasoning and calculations. s ranges from 1 (perfect similarity) to −1 (perfect dissimilarity) centered at 0 (pattern due to chance). Similar to CC, the absolute value of s is considered.

### Internal functions

There are internal functions used by the package that the user might never have to call directly, although they are accessible in case the user needs them. Here, we provided a general description of those, leaving the details to the package documentation. All the internal functions to extract similarity metrics are: extract_cc(), extract_s() and extract_rmse(). They all take two numeric vectors and return the corresponding similarity metric between them.

#### new_syndromics()

Helper function to construct the ‘syndromics’ class object that will be use in the S3 generic and method functions. It returns an object of class ‘syndromics’ of the type list.

#### stand_loadings()

This function extracts the standardized loadings from the output of the prcomp() or the princals() functions. In the case of the prcomp() solution, the standardized loadings are calculated as: $s.loadings=eigenvectors\times\sqrt{eigenvalues}$ if the PCA was performed on the standardized (scaled to unit variance) data or $s.loadings=(eigenvector\times\sqrt{eigenvalues})/S$ where $S$ is the vector of the variables standard deviation. In the case of princals(), standardized loadings are returned directly in its output and therefore stand_loadings() returns those. The function returns a data frame with the standardized loadings in the form of variables as rows and PCs as columns.

#### extract_loadings()

This is a wrapper function for stand_loadings() with added functionalities such as error breakers that is used by most functions in the package.

#### extract_syndromic_plot()

This function is internally called by the syndromic_plot() function and returns a ggplot2 object with the syndromic plot for the specified PC. The only argument that is not present in the syndromic_plot() function is the pc argument that specifies which PC to plot. Users should always use syndromic_plot() function instead of extract_syndromic_plot() since syndromic_plot() automatically incorporates other functionalities.

#### component_similarity()

This function is called by the pc_stability() function to calculate the specified similarity metric (see above) between the given list of data frames of loadings. While pc_similarity() uses this function to calculate similarity between the original (parent) loadings and a B sample loadings, the passed list of loadings can be n > 2. Then, the similarity metrics will be calculated between all combinations of n. It returns a list of objects containing a list of the comparisons, a data frame with the averaged metric and the bounds of confidence interval for each specified metric and PC.

#### boot_pca_sample()

This generic function is passed to the statistic argument of the boot() function internally called by the pc_stability() function. It implements the bootstrapping algorithm described above (Figure 2A). Then the boot() function will call boot_pca_sample() B times from the specified data and the pca output of the prcomp() (through the method boot_pca_sample.prcomp()) or princals() (through the method boot_pca_sample.princals()) function, returning a list of B data frames of loadings. The bootstrapping method can be specified using the sim argument.

#### permut_pca_D() or permut_pca_V()

This is a generic function internally called by permut_pca_test() to produce P permutations of the given output of the prcomp() or the princals() functions using permD or permV method. Four S3 R function methods are implemented: permut_pca_D.prcomp(), permut_pca_D.princals(), permut_pca_V.prcomp(), permut_pca_V.princals(). It returns a list of the results of permuting the data, conducting a PCA and extracting either the VAF or the standardized loadings for each P as in Figure 2.

#### Plot.syndromics()

This function implement the S3 method for plotting ‘syndromics’ class objects generated by pc_stability() and permut_pc_test() functions using the R generic plot(). It returns specific plots calling the visualization functions implemented in the package.

### Nonlinear PCA

Nonlinear PCA by optimal scaling and alternating least square was obtained using the princals() function from the {Gifi} package in R. We specified to analyze all variables with nominal restriction scaling, allowing for non-monotonic transformations, and set a restriction of 3 degrees in polynomial transformations for nonlinearity. The corresponding instruction was: princals(nlpca_data, ndim = ncol(nlpca_data), ordinal = FALSE, degrees = 3, knots = knotsGifi(nlpca_data, type=‘E’)), where nlpca_data is the imputed dataset for case study 2 (see supplementary code for more details).

### Missing data analysis

Details on the code are available as supplementary material. Data wrangling for the two case studies was performed using R packages included in the Tidyverse package. Missing pattern visualization were obtained using the naniar (Tierney et al., 2020) R packages. Test for MCAR was performed using the TestMCARNormality() function from the MissMech package (Jamshidian et al., 2014). Multiple imputation was performed using predicting mean matching method available in the mice (Buuren and Groothuis-Oudshoorn, 2011) R package, setting the number of imputations to m = 50. A list of 50 complete datasets were then obtained and processed by PCA as specified in the main text. For each m dataset, the loadings where extracted and rotated using Procrustes rotation (pracma package) toward the average of the imputed datasets. The distributions of loadings and component similarities for the first three PCs where calculated using the syndRomics package as described above.
