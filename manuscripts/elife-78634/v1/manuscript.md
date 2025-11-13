# Robust and Efficient Assessment of Potency (REAP) as a quantitative tool for dose-response curve estimation

## Authors

- Shouhao Zhou<sup>1</sup> ([ORCID: 0000-0002-8124-5047](https://orcid.org/0000-0002-8124-5047)) †
- Xinyi Liu<sup>1</sup>
- Xinying Fang<sup>1</sup> ([ORCID: 0000-0001-9121-5717](https://orcid.org/0000-0001-9121-5717))
- Vernon M Chinchilli<sup>1</sup>
- Michael Wang<sup>2</sup>
- Hong-Gang Wang<sup>3</sup>
- Nikolay V Dokholyan<sup>3</sup> ([ORCID: 0000-0002-8225-4025](https://orcid.org/0000-0002-8225-4025))
- Chan Shen<sup>1</sup>
- J Jack Lee<sup>7</sup>

### Affiliations

1. Department of Public Health Sciences, Pennsylvania State University Hershey United States ([ROR:04p491231](https://ror.org/04p491231))
2. Department of Lymphoma and Myeloma, University of Texas MD Anderson Cancer Center Houston United States ([ROR:04twxam07](https://ror.org/04twxam07))
3. Department of Pharmacology, Pennsylvania State University Hershey United States ([ROR:04p491231](https://ror.org/04p491231))
4. Department of Pediatrics, Pennsylvania State University Hershey United States ([ROR:04p491231](https://ror.org/04p491231))
5. Department of Biochemistry and Molecular Biology, Pennsylvania State University Hershey United States ([ROR:04p491231](https://ror.org/04p491231))
6. Department of Surgery, The Pennsylvania State University Hershey United States ([ROR:04p491231](https://ror.org/04p491231))
7. Department of Biostatistics, University of Texas MD Anderson Cancer Center Houston United States ([ROR:04twxam07](https://ror.org/04twxam07))

† Corresponding author

## Abstract

The median-effect equation has been widely used to describe the dose-response relationship and identify compounds that activate or inhibit specific disease targets in contemporary drug discovery. However, the experimental data often contain extreme responses, which may significantly impair the estimation accuracy and impede valid quantitative assessment in the standard estimation procedure. To improve the quantitative estimation of the dose-response relationship, we introduce a novel approach based on robust beta regression. Substantive simulation studies under various scenarios demonstrate solid evidence that the proposed approach consistently provides robust estimation for the median-effect equation, particularly when there are extreme outcome observations. Moreover, simulation studies illustrate that the proposed approach also provides a narrower confidence interval, suggesting a higher power in statistical testing. Finally, to efficiently and conveniently perform common lab data analyses, we develop a freely accessible web-based analytic tool to facilitate the quantitative implementation of the proposed approach for the scientific community.

## Introduction

The median-effect equation is a unified theory in medicine to describe the dose-response relationship and identify agents or their combinations that activate or inhibit specific disease targets (Chou, 2006). It is a fundamental method established based on the pharmacological principle of mass-action law (Chou, 1976). As the common link for many biomedical systems, it has been used extensively to analyze in vitro experimental data and evaluate the potency of related drugs (Chou and Talalay, 1984; Chou and Rideout, 1991; Greco et al., 1995; Lee and Kong, 2009).

In practice, the median-effect equation can be estimated for drug efficacy or pathway inhibition from normalized data generated from experimental studies. Without knowing the true dose-effect curve during the experimental design and data collection, it is common to observe extreme values of (un)affected cell fraction that is close to the response of either 0 or 100% in the analytic dataset. Quantitatively, it poses a special analytic challenge to estimate the median-effect question in practice. The standard estimation approach, often based on a linear regression model after a logit transformation (Roell et al., 2017; Gadagkar and Call, 2015), could suffer badly from poor estimation in such situations. Figure 1 illustrates a preliminary example in that the standard approach is deficient in describing the median effect curve with a perturbation in one extreme data point. The variation in real experimental data, mostly caused by unavoidable measurement error, often at a much larger degree, therefore challenges the reliability of result presentation and interpretation for many drug assessment studies.

![Figure 1.](https://cdn.elifesciences.org/articles/78634/elife-78634-fig1-v1.jpg)

**Figure 1.:** The original data points are on the true curve. The leftmost data point is changed from 0.005 to 1e-6, referring to a small white noise that cannot be visually recognized. The change leads to the obvious departure between the estimated curve by linear regression model (dotted) and the true curve (solid), which demonstrates that standard regression is sensitive to extreme values. The response at the true IC50 (dotdashed, vertical, left) is only 22% from the estimated curve; the estimated IC50 (dotdashed, vertical, right) corresponds to the 70% fraction of cell affected, effecting a substantive 20% inflation (50% ->70%) in estimation error. In contrast, the estimated curve by beta regression model (dashed) is almost overlapped with the true curve (solid), which shows that BRM is much more robust to extreme values. LRM: linear regression model; BRM: robust beta regression model. Detailed model descriptions of LRM and BRM are provided in Materials and methods section.

Additionally, the modeling strategy of deleting extreme values may not be feasible in many situations (Solzin et al., 2020). For example, a meaningful drug concentration could consist of high inhibition (>90%) or low cell viability (<10%) in cancer research. It is not logical to ignore extreme observations when they are indeed biologically relevant for the target effect, not even to mention an associated loss of power and accuracy by leaving fewer data points for estimation. As illustrated in Figure 2, deleting the extreme values couldn’t eliminate the estimation bias, but only impaired the efficiency of interval estimation with wider nominal 95% confidence intervals (C.I.) and harmed the estimation accuracy with worse coverage probabilities.

![Figure 2.](https://cdn.elifesciences.org/articles/78634/elife-78634-fig2-v1.jpg)

**Figure 2.:** Deleting the extreme values could not eliminate the bias (panel A), but only harmed the accuracy with worse coverage probabilities (panel B) and impaired the efficiency of interval estimation with wider nominal 95% confidence intervals (panel C). A total of 1000 data sets were generated following the data simulating process described in Appendix 1, using the dose sets and true dose-response curve under 7 dose setting with a precision parameter of 100. Responses ≤5% or ≥95% were considered extreme responses. Dashed line in panel B denotes 95% nominal coverage probability. BRM: beta regression with extreme data points; LRM: linear regression model with extreme data points; LRM(t): linear regression model with truncated dataset after deleting extreme values. Detailed model descriptions of LRM and BRM are provided in Materials and methods section.

Furthermore, it is dubious to apply the constant error variance, a default assumption in standard linear regression modeling, in dose-response estimation. As an assumption can be examined with repeated measures, many dose-response data have indicated either a constant variance before logit transformation or a positive correlation with drug dose. It is incongruous to apply linear regression if the assumption is violated due to error heteroscedasticity (Schmidheiny, 2009; Williams et al., 2007). Therefore, it is essential to develop a robust quantitative approach to estimating the median-effect equation.

Here, we introduce a novel approach to improving the quantitative assessment of dose-response relationship and drug potency, together with a user-friendly web-based analytic tool to facilitate the implementation. The proposed method to estimate the median-effect equation is established in the robust beta regression framework, which not only takes the beta law to account for non-normality and heteroskedasticity (Ferrari and Cribari-Neto, 2004), but also minimizes the average density power divergence (DPD) using a tuning parameter (Ghosh, 2019). We apply a data-driven approach to optimizing the tuning parameter, which further compensates for the lack of robustness against outliers. In the simulation studies, we compare the robust beta regression framework with linear regression models either in the standard normal distribution error, or in the heavy-tailed t distribution error with 3 degrees of freedom hopefully to downweigh the influence of extreme observations. Results from simulation studies under various scenarios confirm that the proposed approach consistently gives robust estimation for the median-effect equation. Particularly, we examine two important measures for drug binding affinity: the Hill coefficient, which signifies the sigmoidicity of the curve, and the overall effect, indicated by dose concentration for a specified (e.g. 50%) response (Shen et al., 2008; Sampah et al., 2011). When there are extreme outcome observations, the improvement of robust beta regression in estimation accuracy could be substantial. Moreover, simulation studies further illustrate that the proposed approach provides a narrower confidence interval, which in turn suggests a higher efficiency to achieve better power in statistical testing even without acquiring additional experimental data. Illustrative examples using real-world data for cancer research and SARS-CoV-2 treatment are provided. The analyses are implemented using the freely accessible web-based application REAP, developed based on the Shiny package of R language, with which research scientists could conveniently upload their drug experiment dataset and perform the data analysis.

## Results

### REAP Shiny App

We developed a user-friendly analytic tool, coined ‘REAP’ (Robust and Efficient Assessment of Potency), for convenient application of the robust dose-response estimation to real-world data analysis. It is established in an agile modeling framework under the parameterization of the beta law to describe a continuous response variable with values in a standard unit interval (0.1). We further exploited a robust estimation method of the beta regression, named the minimum density power divergence estimators (MDPDE) (Ghosh, 2019), for dose-response estimation, with the tuning parameter optimized by a data-driven method (Ribeiro and Ferrari, 2020). The technical details are provided in the Materials and methods.

REAP presents a straightforward analytic environment for robust estimation of dose-response curve and assessment of key statistics, including implementation of statistical comparisons and delivery of customized output for graphic presentation (Figure 3). The dose-response curve is a time-honored tool to convey the pharmacological activity of a compound. Through dose-response curves, we can compare the relative activity of a compound on different assays or the sensitivity of different compounds on an assay. REAP aims to make this job simple, estimation efficient, and results robust.

![Figure 3.](https://cdn.elifesciences.org/articles/78634/elife-78634-fig3-v1.jpg)

**Figure 3.:** Using the robust beta regression method, REAP produces a dose-response curve plot with effect and model estimations. The left panel allows users to specify model features and design plot specifics. REAP also provides hypothesis testing results to compare effect estimations, slopes and models.

There are three sections in REAP: Introduction, Dataset and Output. Users can have both overview and instruction of REAP in the Introduction. Dataset is uploaded in the Dataset section. The input dataset is mandated to be in a csv file format and contains three columns of data respectively for drug concentration, response effect and group name, in a specific order. It is recommended that users normalize the response variable to the range of (0,1) by themselves. Otherwise, REAP automatically will truncate the values exceeding the boundaries to (0,1) using a truncation algorithm (see Appendix 1 - Truncation Strategy). In the Output section, it generates a dose-response plot, along with tabulation for effect and model estimations. A special feature of REAP is that it conveniently allows the users to specify the target effect level, rather than fixed at the common median effect (i.e., 50%), in dose estimation. We also enable hypothesis testing for comparisons of effect estimations, slopes and models (i.e. comparing both intercepts and slopes; see Materials and methods). By default, the x-axis of the dose-response plot is log-scaled. In the plot, users can choose to add mean values and sample standard deviations for data points under the same agent and dose level. Both plots and estimation tables are downloadable on REAP to plug in presentations and manuscripts for result dissemination.

The open-sourced REAP is freely available and accessible at https://xinying-fang.shinyapps.io/REAP/. We demonstrated it in two real-world examples, after presenting the simulation results, to illustrate the functionality of REAP.

### Simulations

We conducted simulation studies to investigate the robust beta regression model, in comparison to linear regression models with data transformation, either under a normal distribution error (implemented with R package ‘stats’) or a heavy-tailed t distribution error with 3 degrees of freedom (implemented with R package ‘heavy’), to characterize the median-effect equation under different scenarios. The model assessment is established based on both the point estimation and interval estimation derived from each method. Details on the simulation setting are described in the Appendix 1 - Data simulating process.

With data simulated using normal error terms, the robust beta regression provides sensible estimation of IC50, IC90, $\beta_{1}$, and $\beta_{0}$ from median-effect equation (Figure 4, Appendix 1—table 1). Particularly, when there are extreme outcome observations, the robust beta regression manages much lower bias and root-mean-square error (RMSE) for point estimates and better coverage probability for interval estimates than the linear regression model with normal distribution error. For data without extreme values, their performance is comparable in bias, RMSE and coverage probability, but the linear regression model has much wider 95% CIs (Figure 4). Indeed, the wider 95% CIs occur across all the scenarios, indicating higher estimation efficiency of the robust beta regression approach. In contrast, the heavy-tailed linear regression model demonstrates improved bias and RMSE in point estimation from the standard linear regression, but the nominal 95% CIs are significantly underestimated with coverage probability below 50% in most cases (Appendix 1—table 1). Therefore, the heavy-tailed linear regression model, although sometimes provides good point estimations, cannot maintain consistently robust and statistically efficient estimations. Overall, the robust beta regression model is the most robust and stable in estimating the median-effect equation with reliable performance in both point estimations and 95% CI coverage probabilities.

![Figure 4.](https://cdn.elifesciences.org/articles/78634/elife-78634-fig4-v1.jpg)

**Figure 4.:** The vertical solid lines indicate the true values. The dots represent the averaged point estimates and the bars represent the averaged lower and upper bound of 95% CIs. The point estimation by robust beta regression is consistently closer to the true value with a narrower 95% CI compared to the linear regression model. The 95% CI of heavy-tailed linear regression underestimates the nominal coverage probability. LRM: linear regression model; LRM-7: LRM under 7-dose dataset with extreme data points; LRM-6noL: LRM under 6 dose dataset after removing the highest dose data point; LRM-6noS: LRM under 6-dose dataset after removing the lowest dose data point; LRM-7lessE: LRM under 7-dose dataset with less extreme data points; LRM-7NCP: LRM under 7-dose dataset with extreme data points and dose-dependent precision; HLRM: heavy-tailed linear regression model; HLRM-7: Heavy-tailed LRM under 7-dose dataset with extreme data points; HLRM-6noL: Heavy-tailed LRM under 6-dose dataset after removing the highest dose data point; HLRM-6noS: Heavy-tailed LRM under 6-dose dataset after removing the lowest dose data point; HLRM-7lessE: Heavy-tailed LRM under 7-dose dataset with less extreme data points; HLRM-7NCP: Heavy-tailed LRM under 7-dose dataset with extreme data points and dose-dependent precision; BRM: robust beta regression model; BRM-7: BRM under 7-dose dataset with extreme data points; BRM-6noL: BRM under 6-dose dataset after removing the highest dose data point; BRM-6noS: BRM under 6-dose dataset after removing the lowest dose data point; BRM-7lessE: BRM under 7-dose dataset with less extreme data points; BRM-7NCP: BRM under 7-dose dataset with extreme data points and dose-dependent precision. Detailed model descriptions of LRM, HLRM, and BRM are provided in Materials and methods section.

In parallel, similar results are obtained consistently with data simulated using beta error terms, which induces heteroscedasticity (smaller variation on the two ends and bigger in the middle) at different dose levels (Appendix 1—figure 1, Appendix 1—table 2). All the results above demonstrate the sensitivity of regression models in dealing with datasets including extreme values. In addition, the result comparisons between the seven-dose set and the six-dose set with the largest or smallest dose eliminated display the potential worse influence of deleting extreme values directly in modeling dose-response using linear regression, which further notarizes the robustness and efficiency of the proposed robust beta regression.

Overall, the simulation study suggests that the robust beta regression model produces well-calibrated dose-response curves while being more robust and powerful than the standard regression model and the heavy-tailed linear regression model in estimating the median effect equation.

### B-cell lymphoma data

The first example of REAP application is dose-response curve estimation of the same agent under different cell lines. The data was originally from a study on using a drug called auranofin in treating B-cell lymphomas such as relapsed or refractory mantle cell lymphoma (MCL) (Wang et al., 2019). As an FDA-approved treatment of rheumatoid arthritis, auranofin targets thioredoxin reductase-1 (Txnrd1), and was repurposed as a potential antitumor drug to effectively induce DNA damage, reactive oxygen species (ROS) production, cell growth inhibition, and apoptosis in aggressive B-cell lymphomas, especially in TP53-mutated or PTEN-deleted lymphomas.

In the experiment, the effect of auranofin was evaluated in six MCL cell lines (Z-138, JVM-2, Mino, Maver-1, Jeko-1, and Jeko-R) with auranofin in concentrations ranging from 0 to 5 μM for 72 hr and tested cell viability using a luminescent assay. The interval bars of observed dose-response in Figure 5 show that the sample variance of error from repeated measurements decreased with the increase of auranofin concentrations. To account for the heteroscedasticity and asymmetry in the variance, we enable a dose-dependent precision (proportional to inverse variance) in REAP, adding $log⁡dose$ as an additional regressor for the precision parameter. Figure 5 shows the fitted dose-response curves with the dose-dependent precision. The test for homogeneity (p-value <0.0001) suggests distinct dose-response between cell lines. The estimation of intercepts, hill coefficients and pairwise comparisons of IC50 estimations are provided in Appendix 1—table 3.

![Figure 5.](https://cdn.elifesciences.org/articles/78634/elife-78634-fig5-v1.jpg)

**Figure 5.:** The dose-response curve was fitted with a dose-dependent precision with $log⁡(dose)$ as an additional regressor for the precision estimator. Observed dose effects are displayed with interval bars, which end with arrows when estimated intervals exceed (0,1). Triangles at the bottom indicate IC50 values for each MCL cell line. MCL: mantle cell lymphoma.

### SARS-CoV-2 data

The second example is on the dose-response curve estimation in antiviral drug development for coronavirus disease 2019 (COVID-19). At the beginning of 2020, COVID-19 broke out at an unprecedented pace internationally, but there were limited therapeutic options for treating this disease. Therefore, many compounds and their combinations were rapidly tested in vitro against the SARS-CoV-2 virus to identify potentially effective treatments and prioritize clinical investigation.

In the data (Bobrowski et al., 2021), the benchmark compound collection consists of five known antivirals, including remdesivir, E64d (aloxistatin), chloroquine, calpain Inhibitor IV and hydroxychloroquine. The in vitro experiment was performed using the same biological batch of SARS-CoV-2 virus and conducted in biosafety level-3. In the original publication (Bobrowski et al., 2021), the dose-response curves were fitted by linear regression, which could yield inconclusive estimation (e.g. hydroxychloroquine in Figure 1G of Bobrowski et al., 2021), while the estimated inhibition tends to exceed 1 when concentration is larger than 10 µM. REAP gives reasonable estimation for the dose-response curves (Figure 6). The hypothesis testing results show that at least one slope estimation is different from other antivirals (p-value = 0.0003) and at least one EC50 estimation is different from others (p-value = 0.003). Calpain Inhibitor IV shows a higher potency than other agents including hydroxychloroquine (p-value = 0.0038, Appendix 1—table 4).

![Figure 6.](https://cdn.elifesciences.org/articles/78634/elife-78634-fig6-v1.jpg)

**Figure 6.:** The robust beta regression gives reasonable estimations to the dose-response curve of hydroxychloroquine, compared to the inconclusive dose-response curve fitted by linear regression in Bobrowski et al. (2020). The plot is generated without selecting the option of mean and confidence interval for observations. Triangles indicate the estimated EC50 values for each drug.

## Discussion

Quantifying the potency of a compelling substance is always a central topic in life sciences (Schindler, 2017). It is a vital component of research in pharmacology, but also prevalent in the fields of toxicology, environmental science, agrochemistry, and medicine, among many others. For instance, the description of dose-response curves can provide the initial toxicological risk assessment (National Research Council, 2007), and guide in silico modeling of toxic doses to humans and the environment (Blaauboer et al., 2012). Based on proper identification of dose-response relationship from in vitro assays, studies can successfully predict systemic toxicological effects in vivo without additional in silico modelling (Groothuis et al., 2015). Nevertheless, it necessitates accurate and reliable description of the dose-response curve, which further demands robust and efficient modeling strategies to account for embedded variability in observed response and to derive solid inference with valid quantification of uncertainty.

The dose-response estimation could be substantially biased by the standard regression modeling. In the illustrative example (Figure 1), the estimated IC50 dose indeed effects the 70% fraction of cell affected, while the estimated response at the true IC50 dose is only 22%. Such a large discrepancy is sourced by a small (<0.5%) single measurement error, which is common and inevitable in any regular in vivo experiment, but could engender a profound impact on the assessment of drug potency and determination of synergy in drug combinations. In addition, the modeling strategy of deleting those extreme values (e.g. Figure 2, or 6noL and 6 noS datasets in Figure 4 and Appendix 1—figure 1) is futile to improve the poor performance of standard regression model, but may further impair the estimation efficiency and accuracy. In general, it fails to reduce bias but only introduces larger uncertainty in estimation of dose concentration, especially at extreme responses (e.g. IC90). On the other hand, a heavy-tailed error distribution may help to stabilize the point estimation, but the interval estimation could be largely under-estimated with poor coverage probabilities.

We develop REAP for assessment of drug potency to address concerns in this regard. It has substantial advantages over existing methods by reducing the impact of random errors due to implicit variations in the experimental data. To our best knowledge, it is also for the first time that beta regression is introduced to dose-response estimation. The underlying modified robust beta regression model estimated by the data-driven tuning parameter is resilient to estimation bias caused by extreme observations, which is a routinely encountered situation for deficient dose-response estimation using the standard estimation approach. The proposed approach is also efficient in quantitative characterization of dose-response curves with narrower confidence intervals for key estimators. Furthermore, REAP can simultaneously model the data heterogeneity with a dose-dependent precision component (Figure 5). It is simply different from other dose-response methods, in which a vector of weights have to be (possibly mis-)specified externally. REAP is an open-source and user-friendly platform, developed for diverse non-computational scientists for hands-on wet-laboratory data analysis in regular use, and can be hosted within R shiny environment under Windows, Linux, and Mac systems or deployed in Docker available as a web server.

Our work potentially can be useful in applications of drug screening. The proposed method and the developed REAP App allow for the robust and efficient estimation and accounting for outliers as well, making it fitted particularly in a high-throughput setting. As the result of a complex and dynamic cascade of events, exposure time is another important factor ultimately affecting the dose-response. For in vitro experiments measured at different time points in a choice of cell-lines and expressed by a variety of assays (Byrne and Maher, 2019), the proposed modeling framework can be naturally extended to model time-dependent cytotoxicity while controlling for fixed or random effects. Furthermore, the application of robust and efficient dose-response estimation can be integrated into methods to identify drug interaction effect (Lee and Kong, 2009; Lee et al., 2007). There is a venerable history that multi-agent combination therapies demonstrate great advantages in improving therapeutic efficacy and revolutionize patient outcomes in a wide range of diseases. Robust and efficient estimation of the dose-response curve would be crucial in investigation of adequate drug combinations.

The developed method has limitations. We presented a model of the median effect equation for dose-response curve estimation based on mass action law. While in specific scenarios other laws may be considered more suitable to describe the biomedical systems, the current modeling framework can be naturally adapted for other dose-response functions like probit (via cumulative normal distribution) and Weibull model (Christensen, 1984), or any other continuous distribution functions. In addition, the median-effect equation to characterize pharmacological activity assumes the compound can affect all the cells. From a quantitative perspective, a compound that cannot reach high binding affinity will yield an over-conservative estimation for median effective dose of a drug. However, in comparison to the sensitivity of different compounds in an assay, it is not harmful because the less effective compounds will be more easily identified. If it is a concern that the maximal effects of candidate compounds are different and the aim is to accurately model the dose-response curve, the Emax model could be a better choice (Lee et al., 2010). Furthermore, the robust beta regression approach in REAP cannot handle values equal or less than 0, or equal or greater than 1. Thus, we developed a sequential data truncation algorithm in REAP to overcome the limitation of the conventional transformation (y * (n−1)+0.5) / n, which could be too rough in dose-response curve estimation particularly when the sample size n for each group is relatively small. Although empirically we have validated it using simulated data, the algorithm could be improved by future work to retain information more efficiently.

In summary, a good modeling strategy must effectively characterize the nature of the observed dose-response pattern (Lyles et al., 2008). Rapid advances in novel drug development and considerable deficiency in modeling data with extreme values offer an appealing opportunity for next-generation quantitative approaches. While many aspects of the techniques discussed here fit in the statistical framework of robust beta regression, our aim is to clearly apply and rigorously customize the analytic considerations, to reduce bias and ameliorate efficiency in routinely used dose-effect estimation, and to facilitate the convenient analytic implementation and dissemination. Experimental conditions and candidate drug potency could inevitably vary in practice, but REAP provides a great tolerance for points with extreme values, solid support for accurate and efficient dose-response curve estimation, and useful reference to the future development of methodology in drug investigation. Overall, we anticipate that our work will contribute more to quantitative analysis in assessment of drug potency in preclinical research.

## Materials and methods

### Median-effect equation and dose-response curve

The median-effect equation describes a popular model of the dose-response relationship based on the median effect principle of the mass action law in various biological systems (Chou, 1976). Assume $f_{a}$ and $f_{u}$ are the fractions of the system affected and unaffected by a drug concentration $d$. The median-effect equation states that

$$
\frac{f_{a}}{f_{u}}=(\frac{d}{D_{m}})^{m},                                                                      
$$

where $m$ is the Hill coefficient signifying the sigmoidicity of the dose-effect curve and $D_{m}$ is the dose of a drug required to produce the median effect, which is analogous to the more familiar $IC_{50}$ (drug concentration that causes 50% of the maximum inhibitory effect), $ED_{50}$ (half-maximum effective dose), or $LD_{50}$ (median lethal dose) values (Ghosh, 2019). For example, if an inhibitory substance is of interest, the parameter $m$ measures the cooperativity in the binding of multiple ligands to linked binding sites, and the parameter $D_{m}=IC_{50}$ , defined by the concentration that causes 50% of the maximum inhibitory effect.

Given $f_{a}+f_{u}=1$, the median-effect Equation 1 is equivalent to

$$
logitf_{a}=log⁡\frac{f_{a}}{f_{u}}=-logitf_{u}=-log⁡\frac{f_{u}}{f_{a}}=mlog⁡d-log⁡ D_{m},              
$$

where $logit(p)$ denotes the logit function $log⁡\frac{p}{1-p}$ . The Equation 2 shows a log-linear relationship between the drug dose $d$ and its effect $f_{a}$ (or $f_{u}$ , if it is, for example, the % survival of interest) after a logit transformation. Because from a modeling perspective the identical strategy can be applied to model both $f_{a}$ and $f_{u}$ , for the effect on cell fraction $E$, we can rewrite Equation 2 to be:

$$
logitE=log⁡\frac{E}{1-E}=\beta_{1}log⁡d+\beta_{0}                                               
$$

where $\beta_{0}$ is the intercept and $\beta_{1}$ the slope of the response curve. A linear regression model (LRM) can be applied in the form of Equation 3 with a standard normal distribution error. In simulation studies, we also examine Equation 3 with a heavy-tailed t-distribution error, denoted by heavy-tailed linear regression model (HLRM).

In this presentation, the median effect dose

$$
D_{m}= exp-\frac{\beta_{0}}{\beta_{1}},                                                                 
$$

the Hill coefficient

$$
m={\beta_{1}−\beta_{1}ifE=f_{a}E=f_{u}
$$

and the dose-response curve

$$
E=logit^{-1}\beta_{1}log⁡d+\beta_{0},                                                        
$$

where $logit^{-1}x=\frac{exp⁡(x)}{1+exp⁡(x)}$ is the inverse-logit function.

### Beta regression model for dose-response curve estimation

We will review the beta regression model which for the first time will be applied in dose-response estimation. The effect $E$ and the parameters $\beta=(\beta_{0},\beta_{1})$ in Equation 3 cannot be directly observed, but they can be estimated using experimental data, in which the observed sample cell fraction $y$ produced by the drug dose $d$ is a random variable with mean $E$. It is clear that effective estimation must properly account for random variation and be based upon a model that not only matches the nature of the response variable, but adequately characterizes the observed dose-response pattern (Lyles et al., 2008).

Among all the unknown quantities, the parameters $\beta$ could be first estimated and play a fundamental role in supporting the inference for others. In the standard estimation procedure based on linear regression, $logity=log⁡\frac{y}{1-y}$ is regressed on $log⁡d$ to get the inference on parameters $\beta$. Subsequently, the dose-response curve can be estimated by Equation 6, and $(D_{m},m)$ can be derived based on Equations (4) and (5) for median-effect Equation 2. Because the extreme values of $y$ close to 0 or 1 could yield very large values of $logity$ (approaching to $-∞$ or $+∞$, respectively, if $y→0$ or 1), and induce significant bias in estimation of $\beta$, the accuracy of the estimated dose-response curve and median-effect equation is in question when there exist extreme values in the dataset.

The beta regression model describes a response variable $y$ with continuous values restricted to the open standard unit interval (Johnson et al., 1995; Simas et al., 2010). In a classic beta regression framework, the beta regression model uses a parameterization of the beta law that is indexed by the mean parameter μ, and the precision parameter $ϕ$ that controls the overall variation (Ferrari and Cribari-Neto, 2004). To model the dose-response relationship for the cell fraction $E$, we assume that the response $y$ is a beta-distributed random variable and its mean $\mu=E$ has the form of Equation 6, where $d$ is the dose producing effect $E$, $\beta_{1}$ and $\beta_{0}$ are the regression parameters. Estimation of regression parameters $\beta$ can be performed using maximum likelihood method to derive point estimate $\beta^$ and covariance matrix $Σ$.

Beta regression is resistant to extreme values and provides reliable estimations (Figure 1). Compared with the standard approach, which applies a non-linear transformation in the response for an approximation to the normal distribution, the beta density can take on a variety of shapes to account for non-normality and skewness (Smithson and Verkuilen, 2006). In the presence of heteroskedasticity and asymmetry, two common problems frequently observed in limited range continuous response data, an empirical study showed that the beta regression provided the best estimation among several alternatives (Kieschnick and McCullough, 2016).

### Robust beta regression model with MDPDE

We will present a modified robust beta regression approach in REAP implementation, which is established based on density power divergence for robust estimation (Ghosh, 2019), but further improved after we introduce a data-driven method to identify the optimal tuning parameter. The standard beta regression potentially could still be sensitive against outliers because its inference is based on the maximum likelihood estimation. Ghosh, 2019 developed the robust minimum density power divergence estimators (MDPDE) that address the problem by minimizing the average density power divergence (DPD)

$$
d_{\alpha}(g^, g)=\intg^{1+\alpha}−\frac{1+\alpha}{\alpha}\intg^g^{\alpha}+\frac{1}{\alpha}\intg^^{1+\alpha},d_{0}(g^, g)=lim\alpha→0d_{\alpha}(g^,g)\intg^log⟮\frac{g^}{g}⟯,
$$

between the empirical density $g^$ and the beta model density function $g≡Beta\muϕ, 1-\muϕ$ with $\mu=logit^{-1}\beta_{1}log⁡d+\beta_{0}$ . $\alpha$ is a non-negative tuning parameter, smoothly connecting the likelihood disparity (at $\alpha$ = 0) to the L2-Divergence (at $\alpha$ = 1). The parameter of interest $\beta$ is estimated by minimizing the DPD measure between $g_{i}$ and the density, $g^_{i}$ ,

$$
n^{−1}\sumi=1nd_{\alpha}(g^_{i}(⋅), g_{i}(⋅,\theta))
$$

where $\theta=(\beta,ϕ)^{T}$. After mathematically simplifying Equation 8, (Ghosh, 2019), $\theta$ can be equivalently estimated by minimizing the objective function using the estimation equations:

$$
H_{n,\alpha}\theta=n^{-1}\sumi=1n[K_{i,\alpha}\theta-\frac{1+\alpha}{\alpha}g_{i}y_{i},\theta^{\alpha}]                                     
$$

where $K_{i,\alpha}\theta=\frac{B(1+\alpha\mu_{i}ϕ, 1+\alpha1-\mu_{i}ϕ-\alpha)}{B\mu_{i}ϕ, 1-\mu_{i}ϕ^{\alpha}}$.

MDPDE improves the standard beta regression with the DPD measure and a fixed tuning parameter. The recommended α is around 0.3 to 0.4, but simply assigning a fixed α in [0.3, 0.4] is not applicable in many cases. Here we adopted a data-driven method (Ribeiro and Ferrari, 2020) to identify the optimal α. The search for the optimal α starts with a grid of α, a pre-defined αmax and grid size $ρ$, which generates a sequence of equally spaced ${\alpha_{k}}_{k=0}^{m} (0=\alpha_{0}<\alpha_{1}<⋅⋅\alpha_{m}\leq\alpha_{max})$. MDPDE calculates the corresponding θ and se(θ) with each α so that we get a vector of standardized estimates:

$$
z_{\alpha_{k}}=(\frac{\theta^_{\alpha_{k}}^{1} }{\sqrt{n}se(\theta^_{\alpha_{k}}^{1})}, …, \frac{\theta^_{\alpha_{k}}^{p} }{\sqrt{n}se(\theta^_{\alpha_{k}}^{p})})^{T}
$$

The standardized quadratic variations (SQV) are defined by:

$$
SQV_{\alpha_{k}}=p^{-1}||z_{\alpha_{k}}-z_{\alpha_{k+1}}||.
$$

We compare each $SQV_{\alpha_{k}}$ with a pre-defined threshold $L (L>0)$. If all $\alpha_{k}$ satisfy the stability condition of $SQV_{\alpha_{k}}<L$, then the optimal $\alpha$ equals the minimal $\alpha$ in $\alpha_{k}$ . Otherwise, restart the search with a new grid of $\alpha_{k}$ . The new grid of the same size $p$ is picked from the sequence $\alpha_{k}_{k=0}^{m}$ starting from the largest $\alpha_{k}$ that fails the stability condition. Repeat searching until all $\alpha_{k}$ in the current grid satisfy the stability condition or $\alpha_{max}$ is reached. If the stability condition is satisfied before $\alpha_{max}$ is reached then optimal $\alpha$ equals the minimal value in the grid of $\alpha_{k}$ . If $\alpha_{max}$ is reached, then optimal α equals 0, which is equivalent to the maximum likelihood estimation. We denote this approach by robust beta regression model (BRM) in the simulation study.

### Point estimate and its confidence interval for drug activity measurements

The objective of analysis is to characterize the dose-response curves in equation (2) and quantify in vitro drug potency. Popular drug activity measurements include Hill coefficient $m$ and median effect dose $D_{m}$ . In some circumstances, other measurements such as instantaneous inhibitory potential (IIP), which directly quantifies the log decrease in single-round infection events caused by a drug at a clinically relevant concentration, are of special interest (Shen et al., 2009).

The MDPDE for beta regression model provides a robust strategy to estimate $\beta$, from which the point estimates and confidence intervals of relevant drug activity measurements can be derived. Mathematically, those drug activity quantities can be written as functions of parameters $\beta$ with an explicit form. Subsequently, their point estimates and confidence intervals can be derived based on the inference of $\beta$. For example, given a point estimate $\beta^=(\beta^_{0},\beta^_{1})$, the point estimate for $m^$ , $D^_{m}$ as a single value, and $E^$ as a function of dose $d$ can be computed using Equations 4–6.

It is important to construct the confidence interval around the point estimate to gauge the estimation uncertainty. With different levels of measurement error from either well-managed or lousy experiments, the levels of evidence vary for statistical inference, even if it derives the same point estimates for the intercept $\beta_{0}$ , slope $\beta_{1}$ and the corresponding dose-response curve. Given the point estimate $\beta^$ and its positive-definite covariance matrix $Σ$ to account for variability in observed response, we apply the multivariate delta method and approximate the variance estimate after assuming asymptotic normality (Bickel and Doksum, 2015). As demonstrated in our simulation studies, the constructed $1-\alpha\times100%$ confidence interval consistently provides better results to quantify the $1-\alpha\times100%$ coverage probability. More importantly, the width of the constructed confidence interval was narrower than that from a linear regression model, suggesting that our approach is more efficient with a higher statistical power (Appendix 1—tables 1 and 2).

### Comparison of the dose-response curves

When we estimate multiple dose-response curves with the data collection experiments conducted in a similar setting, it is often of interest to statistically compare the drug potency and/or Hill coefficients. A typical comparison may occur when we examine the similarity of response from different drugs, explore the additional effect of a drug combined with certain monotherapy, or assess the homogeneity of a drug to different patient samples or cell lines. In the beta regression framework, the statistical comparison can be conducted by first comparing independent fits for each curve with a global fit that shares the common parameters among different groups. Subsequently, the likelihood ratio test can be applied to examine whether the same Hill coefficient or one dose-response curve can adequately fit all the data. The only exception is to assess whether median effect doses are the same in different groups, while an F test is used for the single parameter testing. If the global test for potency shows a significant p-value, a pairwise comparison can be conducted using two-sided t-test for the ordered groups with Benjamini-Hochberg correction for multiplicity.
