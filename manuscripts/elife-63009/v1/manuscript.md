# A modular approach to integrating multiple data sources into real-time clinical prediction for pediatric diarrhea

## Authors

- Ben J Brintz<sup>1</sup> ([ORCID: 0000-0003-4695-0290](https://orcid.org/0000-0003-4695-0290)) †
- Benjamin Haaland<sup>3</sup>
- Joel Howard<sup>4</sup>
- Dennis L Chao<sup>5</sup>
- Joshua L Proctor<sup>5</sup>
- Ashraful I Khan<sup>6</sup>
- Sharia M Ahmed<sup>2</sup>
- Lindsay T Keegan<sup>1</sup>
- Tom Greene<sup>1</sup>
- Adama Mamby Keita<sup>7</sup>
- Karen L Kotloff<sup>8</sup>
- James A Platts-Mills<sup>9</sup>
- Eric J Nelson<sup>10</sup>
- Adam C Levine<sup>12</sup>
- Andrew T Pavia<sup>4</sup>
- Daniel T Leung<sup>2</sup> ([ORCID: 0000-0001-8401-0801](https://orcid.org/0000-0001-8401-0801)) †

### Affiliations

1. Division of Epidemiology, Department of Internal Medicine, University of Utah Salt Lake City United States
2. Division of Infectious Diseases, Department of Internal Medicine, University of Utah Salt Lake City United States
3. Population Health Sciences, University of Utah Salt Lake City United States
4. Division of Pediatric Infectious Diseases, University of Utah Salt Lake City United States
5. Institute of Disease Modeling, Bill and Melinda Gates Foundation Seattle United States
6. International Centre for Diarrhoeal Disease Research, Bangladesh Dhaka Bangladesh
7. Centre Pour le Développement des Vaccins-Mali Bamako Mali
8. Division of Infectious Disease and Tropical Pediatrics, University of Maryland Baltimore United States
9. Division of Infectious Diseases and International Health, University of Virginia Charlottesville United States
10. Departments of Pediatrics, University of Florida Gainesville United States
11. Departments of Environmental and Global Health, University of Florida Gainesville United States
12. Department of Emergency Medicine, Brown University Providence United States
13. Division of Microbiology and Immunology, Department of Internal Medicine, University of Utah Salt Lake City United States

† Corresponding author

## Abstract

Traditional clinical prediction models focus on parameters of the individual patient. For infectious diseases, sources external to the patient, including characteristics of prior patients and seasonal factors, may improve predictive performance. We describe the development of a predictive model that integrates multiple sources of data in a principled statistical framework using a post-test odds formulation. Our method enables electronic real-time updating and flexibility, such that components can be included or excluded according to data availability. We apply this method to the prediction of etiology of pediatric diarrhea, where 'pre-test’ epidemiologic data may be highly informative. Diarrhea has a high burden in low-resource settings, and antibiotics are often over-prescribed. We demonstrate that our integrative method outperforms traditional prediction in accurately identifying cases with a viral etiology, and show that its clinical application, especially when used with an additional diagnostic test, could result in a 61% reduction in inappropriately prescribed antibiotics.

## Introduction

Healthcare providers use clinical decision support tools to assist with patient diagnosis, often to improve accuracy of diagnosis, reduce cost by avoiding unnecessary laboratory tests, and in the case of infectious diseases, deter the inappropriate prescription of antibiotics (Sintchenko et al., 2008). Typically, data entered into these tools is related directly to the patient’s individual characteristics, but data sources external to the patient can be informative for diagnosis. For example, climate, seasonality, and epidemiological data inform predictive models for communicable disease incidence (Colwell, 1996, Chao et al., 2019 Fine et al., 2011). The emergence of advanced computing and machine learning has enabled the incorporation of large data sources in the development of clinical support tools (Shortliffe and Sepúlveda, 2018) such as SMART-COP for predicting the need for intensive respiratory support for pneumonia (Charles et al., 2008) or the ALaRMS model for predicting inpatient mortality (Tabak et al., 2014).

Clinical decision support tools rely on the availability of information sources and computing at the time of patient encounter. Although increased availability of internet/mobile phones have increased access to information and computing power in low-resource settings, there may be times when connectivity, computing power, or data-collection infrastructure is unavailable. Thus, there is a need to build clinical decision support tools which can flexibly include features of external sources when available, or function without them if unavailable. Methods that enable the dynamic updating of predictive models are advantageous due to potential cyclical patterns of infectious etiologies. Furthermore, with the emergence of point-of-care (POC) tests for clinical decision-making (Price, 2001), predictive models that are able to integrate results of such diagnostic testing could enhance their usefulness.

We develop a novel method for diagnostic prediction which integrates multiple data sources by utilizing a post-test odds formulation with proof-of-concept in antibiotic stewardship for pediatric diarrhea. Our formulation first fits separate models from different sources of data, and then combines the likelihood ratios from each of these independent models into a single prediction. This method allows the multiple components to be flexibly included or excluded. We apply this method to the prediction of diarrhea etiology with data from the Global Enteric Multicenter Study (GEMS) (Kotloff et al., 2013) and assess the performance of this tool, including with the addition of a synthetic diagnostic, using two forms of internal-validation and by showing its potential effect on reducing inappropriate antibiotic use.

## Materials and methods

We present our approach to building and assessing a flexible multi-source clinical prediction tool with (1) the data sources, (2) the individual prediction models, (3) the use of the likelihood ratio for integrating predictive models, (4) validation of the method, (5) the impact of an additional diagnostic, and (6) a simulation of conditionally dependent tests. We program our prediction tool using R version 3.6.2 (R Project for Statistical Computing, RRID:SCR_001905).

### Data sources

We apply our post-test odds model using clinical data from GEMS, a prospective, case-control study from 2007 to 2011 which took place in seven countries in Africa and Asia. Methods for the GEMS study have been described in detail (Kotloff et al., 2012). Briefly, 9439 children with moderate-to-severe diarrhea were enrolled at local health care centers along with one to three matched control-children. A fecal sample was taken from each child at enrollment to identify enteropathogens and clinical information was collected, including demographic, anthropometric, and clinical history of the child. We used the quantitative real-time PCR-based (qPCR) attribution models developed by Liu et al., 2016 in order to best characterize the cause of diarrhea. Our dependent variable was presence or absence of viral etiology, defined as a diarrhea episode with at least one viral pathogen with an episode-specific attributable fraction (AFe ≥ 0.5) and no bacterial or parasitic pathogens with an episode-specific attributable fraction. Prediction of viral attribution is clinically meaningful since it indicates that a patient would not benefit from antimicrobial therapy. We defined other known etiologies as having a majority attribution of diarrhea episode by at least one other non-viral pathogen. We exclude patients with unknown etiologies when fitting the model, though it has been previously shown that these cases have a similar distribution of viral predictions using a model with presenting patient information as those cases with known etiologies (Brintz et al., 2020).

We obtained weather data local to each site’s health centers during the GEMS study using NOAA’s Integrated Surface Database (Smith et al., 2011). The incidence of many pathogens, including rotavirus (Cook et al., 1990), norovirus (Ahmed et al., 2013), cholera (Emch et al., 2008), and Salmonella (Mohanty et al., 2006), are known to have seasonal patterns, and other analyses have established climatic factors to be associated with diarrheal diseases (Colwell, 1996, Chao et al., 2019, Farrar et al., 2019). Stations near GEMS sites such as in The Gambia exhibit seasonal patterns (Figure 1). We used daily temperature and rain data weighted most by those weather stations closest to the GEMS sites (Appendix 1).

![Figure 1.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig1-v1.jpg)

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The purple and green lines represent the prior 2-week average of daily rain and temperature averages.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** The purple and green lines represent the prior 2-week average of daily rain and temperature averages.

### Construction of predictive models

We define each model using the features described in the below sub-sections in an additive logistic regression model. Each model can be trained using a sample of data from a specific country, continent, or all available data.

#### Predictive model (A) presenting patient

The patient model derived from the GEMS data treats each enrolled patient as an observation and uses their available patient data at presentation to predict viral only versus other etiology of their infectious diarrhea. In order to make a parsimonious model, we used the previously published random forests variable importance screening (Brintz et al., 2020). Using the screened variables (Table 1), we fit a logistic regression including the top five variables that would be accessible to providers at the time of presentation. These include age, blood in stool, vomiting, breastfeeding status, and mid-upper arm circumference (MUAC), an indicator of nutritional status. We note that while variables such as fever and diarrhea duration were shown to be important in previous studies (Fontana et al., 1987), adding these variables did not improve performance. Additionally, we excluded 'Season', since variables representing it are included in the climate predictive model (discussed below), as well as 'Height-for-age Z-score', another indicator of nutritional status, which would require a less feasible calculation than measurement of MUAC.

**Table 1.**
 Rank of variable importance by average reduction in the mean squared prediction error of the response using Random Forest regression.Greyed rows are variables that would be accessible for providers in LMICs at the time of presentation. Table 1 is reproduced from Brintz et al., 2020, PLoS Negl Trop Dis., published under the Creative Commons Attribution 4.0 International Public License (CC BY 4.0; https://creativecommons.org/licenses/by/4.0/).


<table>
  <thead>
    <tr>
      <th colspan="2">Viral etiology</th>
    </tr>
    <tr>
      <th>Variable name</th>
      <th>Variance reduction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age</td>
      <td>51.6</td>
    </tr>
    <tr>
      <td>Season</td>
      <td>29.0</td>
    </tr>
    <tr>
      <td>Blood in stool</td>
      <td>26.1</td>
    </tr>
    <tr>
      <td>Height-for-age Z-score</td>
      <td>24.7</td>
    </tr>
    <tr>
      <td>Vomiting</td>
      <td>23.0</td>
    </tr>
    <tr>
      <td>Breastfeeding</td>
      <td>22.0</td>
    </tr>
    <tr>
      <td>Mid-upper arm circumference</td>
      <td>20.9</td>
    </tr>
    <tr>
      <td>Respiratory rate</td>
      <td>18.5</td>
    </tr>
    <tr>
      <td>Wealth index</td>
      <td>18.3</td>
    </tr>
    <tr>
      <td>Body Temperature</td>
      <td>16.7</td>
    </tr>
  </tbody>
</table>

#### Predictive model (B) climate

We use an aggregate (mean) of the weighted (Appendix 1) local weather data over the prior 14 days to create features that capture site-specific climatic drivers of etiology of infectious diarrhea. By taking an aggregate, we create a moving average that reflects the seasonality seen in Figure 1. An example of the aggregate climate data from The Gambia is shown in Figure 1—figure supplement 1. From the figure, which also shows a moving average of the viral rate, We see that the periods of higher viral cases of diarrhea tend to have low temperatures and less rain.

#### Predictive model (C) seasonality

We include a predictive model with sine and cosine functions as features as explored in Stolwijk et al., 1999. Assuming a periodicity of 365.25 days, we have functions $s⁢i⁢n⁢(\frac{2⁢\pi⁢t}{365.25})$ and $c⁢o⁢s⁢(\frac{2⁢\pi⁢t}{365.25})$. We show that standardized seasonal sine and cosine curves correlate with a rolling average of daily viral etiology rates in The Gambia over time (Figure 1—figure supplement 2). These functions can be used to model the country-specific seasonality of viral etiology rate.represent multiple underlying processes that result in a seasonality of viral etiology.

### Use of the likelihood ratio to integrate predictive models from multiple data sources

We integrate predictive models from the multiple sources of data described above using the post-test odds formulation. Using Bayes’ Theorem, $P⁢(A|B)=\frac{P⁢(B|A)⋅P⁢(A)}{P⁢(B)}$, to construct the post-test odds of having a viral etiology,

$$
(1)\frac{P(V=1|T_{1}=t_{1},T_{2}=t_{2},⋯,T_{k}=t_{k})}{P(V=0|T_{1}=t_{1},T_{2}=t_{2},⋯,T_{k}=t_{k})}=\frac{P(V=1,T_{1}=t_{1},T_{2}=t_{2},⋯,T_{k}=t_{k})}{P(V=0,T_{1}=t_{1},T_{2}=t_{2},⋯,T_{k}=t_{k})}(2)=\frac{P(T_{1}=t_{1},T_{2}=t_{2},⋯,T_{k}=t_{k}|V=1)⋅P(V=1)}{P(T_{1}=t_{1},T_{2}=t_{2},⋯,T_{k}=t_{k}|V=0)⋅P(V=0)}(3)=\frac{P(V=1)}{P(V=0)}⋅\prodj=1k\frac{P(T_{j}=t_{j}|V=1)}{P(T_{j}=t_{j}|V=0)}
$$

where $V=1$ represents a viral etiology and $V=0$ represents an other known etiology, $T_{1},T_{2},⋯,T_{k}$ represent the k tests, the distribution of the predictions from one or more predictive models, used to obtain the post-test odds, and $\frac{P(V=1)}{P(V=0)}$ is the pre-test odds. Note that going from line (2) to line (3) requires conditional independence between the tests, that is, that $P(T_{i}=t_{i},T_{j}=t_{j}|V=1)$ = $P(T_{i}=t_{i}|V=1)⋅P(T_{j}=t_{j}|V=1)$ and $P(T_{i}=t_{i},T_{j}=t_{j}|V=0)=P(T_{i}=t_{i}|V=0)⋅P(T_{j}=t_{j}|V=0)$ for all i and j. We test for conditional independence to assess the necessity of making higher-dimensional kernel density estimates using the $c⁢i.t⁢e⁢s⁢t$ function from the ${b⁢n⁢l⁢e⁢a⁢r⁢n}$ package in R (Scutari, 2010). We derive each $P(T_{j}=t_{j}|V=1)$ and $P(T_{j}=t_{j}|V=0)$ using Gaussian kernel density estimates on conditional predictions from a logistic regression model fit on the training set (Silverman, 1986). The distribution of $P⁢(T_{j}|V)$ is derived using the kernel density estimator $f⁢(t_{j})=\frac{1}{n⁢h}⁢\sum_{i=1}^{n}K⁢(\frac{t_{j}-x_{i}}{h})$ where, in our case, $K⁢(x)=ϕ⁢(x)$, the standard normal density function, and the bandwidth, h, is Silverman’s 'rule of thumb' and the default chosen in the $d⁢e⁢n⁢s⁢i⁢t⁢y$ function in R (Parzen, 1962).

Figure 2 shows an example of the frequency of predictions from a logistic regression model conditional on the viral-only status (V = 0 and V = 1) determined from attributable fractions. Additionally, we overlaid the estimated one-dimensional kernel density. To obtain the value of $\frac{P(T_{j}=t_{j}|V=1)}{P(T_{j}=t_{j}|V=0)}$, the predicted odds, from a model’s prediction, we divide the kernel density estimate from the $V=1$ set (right) by the kernel density estimate from the $V=0$ set (left). It is feasible to estimate a multi-dimensional kernel density so that it is not necessary to make the conditional independence assumption to move from line 2 to line 3 in the equation above. Figure 2—figure supplement 1 shows an example two-dimensional contour plot for kernel density estimates of predicted values obtained from logistic regression on GEMS seasonality and climate data in Mali which we will discuss further below. The density was created using R function $k⁢d⁢e⁢2⁢d$ (Venables and Ripley, 2002).

![Figure 2.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig2-v1.jpg)

**Figure 2.:** The left graph represent other known etiologies and the right graph represent viral etiologies. The dashed lines do not represent standardized density heights so the heights for V = 0 and V = 1 should not be compared from this graph.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** The right graph represents viral etiologies and the left graph represents other known etiologies.

#### Pre-test odds from historical data

We calculated pre-test odds using historical rates of viral diarrhea by site and date. We utilize available diarrhea etiology data for a given date, regardless of year, and site using a moving average such that pre-test probability $\pi_{d}$ for date d is

$$
\pi_{d}=\frac{D_{d−n}+D_{d−n+1}+⋯+D_{d}+⋯+D_{d+n−1}+D_{d+n}}{k_{d−n}+k_{d−n+1}+⋯+k_{d}+⋯+k_{d+n−1}+k_{d+n}}D_{d}=Σ_{i=1}^{k_{d}}D_{di}
$$

where kd is the number of observed patients on date d, $D_{d⁢i}$ is 1 if the etiology of the patients’ diarrhea is viral and 0 otherwise, and n is the number of days included on both sides of the moving average. We would expect $\pi_{d}$ to represent a pre-test probability of observing a viral diarrhea etiology on date d. Given that this rate information will likely be unavailable in new sites without established etiology studies, we provide an alternative formula based on recent patients’ presentations (Appendix 2). Additionally, we include a sensitivity analysis by calculating pre-test odds using conventional diagnostic methods data as qPCR data are unlikely to be available in high-burden settings.

### Validating the method

Given the temporal nature of some of the tests we developed, we estimate model performance using within rolling-origin-recalibration evaluation. This method evaluates a model by sequentially moving values from a test set to a training set and re-training the model on all of the training set (Bergmeir and Benítez, 2012); for example, we train on the first 70% of the data and test on the remaining 30%, then train on the first 80% of the data and test on the remaining 20%. No data from the training set is used as part of the prediction for the test set. In each iteration of evaluation, predictions on the test set are produced and corresponding measures of performance obtained: the receiver operating characteristic (ROC) curve, and area under the ROC curve (AUC), also known as the C-statistic, along with AUC confidence intervals (LeDell et al., 2015). Figure 3 depicts one iteration of within rolling-origin-recalibration evaluation.

![Figure 3.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig3-v1.jpg)

We additionally include a joint density for the climate and seasonal data in which we estimate a two-dimensional kernel density (not shown in Figure 3). This model is called ”Joint’ in the results to follow. To assess how this model might generalize to a site that was not used for model training, we used a leave-one-site-out validation. By excluding a site and training the model’s tests at a higher level, such as on the entire continent, we get an idea of performance at a new site within one of the continents for which we have data. Lastly, we define a threshold for the predicted odds ratio based on the desired specificity of the model. We use this threshold to evaluate the effect of the model on prescription or treatment of patients with antibiotics in the GEMS data.

### Modeling the impact of an additional diagnostic test

We include a theoretical diagnostic which indicates viral versus other etiology with a given sensitivity and specificity specifically to show the effect of an additional diagnostic-type test, such as a host biomarker-based point-of-care stool testpoint-of-care stool test, on the performance of our integrated post-test odds model. We include three scenarios: (1) 70% sensitivity and 95% specificity, (2) 90% sensitivity and 95% specificity, and (3) 70% sensitivity and 70% specificity. In order to estimate the performance of an additional diagnostic test, for each patient in each of 500 bootstrapped samples of our test data, we randomly simulated a test result based on the sensitivity or specificity of the diagnostic test. From the simulated test result, we derive the likelihood ratio of the component directly from the specified sensitivity and specificity of the test. A positive test results in a component likelihood ratio of $\frac{s⁢e⁢n⁢s⁢i⁢t⁢i⁢v⁢i⁢t⁢y}{1-s⁢p⁢e⁢c⁢i⁢f⁢i⁢c⁢i⁢t⁢y}$ and a negative test results in a component likelihood ratio of $\frac{1-s⁢e⁢n⁢s⁢i⁢t⁢i⁢v⁢y}{s⁢p⁢e⁢c⁢i⁢f⁢i⁢c⁢i⁢t⁢y}$. We then take an average the measure of performance of the bootstrapped samples.

### Simulation of conditionally dependent tests

We demonstrate the utility of the two-dimensional kernel density estimate through simulation. In each iteration of the simulation (100 iterations), we generate 3366 responses from a random Bernoulli variable Z with a $\frac{1}{3}$ probability of success (the approximate proportion of GEMS cases with a viral etiology). Then, conditioned on Z we generate predictive variables X and Y such that:

$$
(4)X=Z+\sigma(5)Y=\gammaX˙+Z+\sigma
$$

where $\sigma$ is a random draw from the standard normal distribution and values of $\gamma$ ranging from −10 to 10 determine the level of conditional dependence between the two predictors conditional on the value of Z. $\gamma=0$ indicates conditional independence. Using an 80% training set, we derive the kernel density estimate for the likelihood ratio (no pre-test odds included) using X and Y as two separate tests and as a single two-dimensional test and calculate the AUC from the 20% test set.

### Determination of appropriate antibiotic prescription

We demonstrate the clinical usefulness of our models by applying them directly to the prescription of antibiotics. For each version of the model, we determined the threshold of prediction that would amount to attaining a model specificity of 0.90 and 0.95. Since the prediction of a viral only etiology of diarrhea indicates that antibiotics should not be prescribed, we chose these high specificities due to the potential harm or even death that could occur if a patient who needed antibiotics did not receive them. Using the thresholds, we determine which patients our models would correctly predict a viral only etiology of their diarrhea (true positives) as well as patients our model would incorrectly predict a viral only etiology of their diarrhea (false positives).

## Results

### Integrative post-test odds models outperformed traditional models for prediction of diarrhea etiology

Of the 3366 patients in GEMS with an attributable identified pathogen, 1049 cases were attributable to viral only etiology. We first examined whether our integrative post-test odds model can better discriminate between patients with diarrhea of viral-only etiology and patients with other etiologies than a traditional prediction model which includes only the presenting patient’s information. We found that the best integrative model with an AUC of 0.839 (0.808–0.870) had a statistically better performance than the traditional model with an AUC of 0.809 (0.776–0.842) with a p-value of 0.01 (DeLong, two-sided). Overall, using the AUC as a discrimination metric, the integrative models (AUC: 0.837 (0.806–0.869)) outperformed the traditional model (AUC: 0.809 (0.776–0.842)). Overall, the best performing models were ones in which either the seasonal sine and cosine curves, or the prior patient pre-test component alone was added to the presenting patient information with AUC’s of 0.830 and 0.839 (with 80% training data), respectively (Figure 4). Including additional components, especially including both climate and seasonality (although not as a joint density), appears to reduce the performance. As expected, a reduced testing set increases the AUC but also increases the variance of the estimate (Figure 4—figure supplement 1). Using conventional diagnostic methods data data to calculate pre-test odds instead of qPCR data reduces AUC slightly from 0.839 to 0.829 (0.798–0.860).

![Figure 4.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig4-v1.jpg)

**Figure 4.:** 'PresPtnt' refers to the predictive model using the presenting patient’s information. 'Pre-test' refers tot he use of pre-test odds based on prior patients’ predictive models. 'Climate' refers to the predictive model using aggregate local weather data. 'Seasonal' refers to the predictive model based on seasonal sine and cosine curves. 'Joint' refers to the two-dimensional kernel density estimate from the Seasonal and Climate predictive models.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Individual plot titles show the proportion of data used in training.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Pre-test refers to the use of prior patient predictions. Individual plot titles show the site left out of training.

To assess our model’s performance more granularly, we then examine performance of the top two predictive models by individual sites. We found that the AUC, with 80% training and 20% testing, varied greatly by site, ranging from 0.63 in Kenya to 0.95 in Bangladesh (Table 2). Of note, the African sites have fewer patients in their testing and training sets than the Asian countries due to a combination of fewer patients enrolled at those sites and proportionately fewer patients with known etiologies. In leave-one-site-out validation testing, we found that the climate test tends to outperform the seasonality test, and that there were notable differences in c-statistics between sites with the order of performance similar to within rolling-origin-recalibration evaluation (Figure 4—figure supplement 2).

**Table 2.**
 AUC results by site using 80% of data for training and 20% of data for testing of the top two models.PresPtnt refers to the model fit using presenting patient information.


<table>
  <thead>
    <tr>
      <th>Country</th>
      <th>Test set size</th>
      <th>Formula</th>
      <th>AUC (95% CI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Kenya</td>
      <td rowspan="3">79</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.65 (0.53–0.77)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.66 (0.54–0.78)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.63 (0.51–0.75)</td>
    </tr>
    <tr>
      <td rowspan="3">Mali</td>
      <td rowspan="3">88</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.74 (0.61–0.86)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.78 (0.66–0.89)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.75 (0.62–0.87)</td>
    </tr>
    <tr>
      <td rowspan="3">Pakistan</td>
      <td rowspan="3">108</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.81 (0.72–0.89)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.8 (0.72–0.88)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.81 (0.73–0.89)</td>
    </tr>
    <tr>
      <td rowspan="3">India</td>
      <td rowspan="3">119</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.84 (0.76–0.91)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.85 (0.78–0.92)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.81 (0.74–0.89)</td>
    </tr>
    <tr>
      <td rowspan="3">The Gambia</td>
      <td rowspan="3">80</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.89 (0.82–0.96)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.87 (0.79–0.94)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.78 (0.67–0.88)</td>
    </tr>
    <tr>
      <td rowspan="3">Mozambique</td>
      <td rowspan="3">66</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.88 (0.79–0.97)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.9 (0.82–0.98)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.77 (0.66–0.89)</td>
    </tr>
    <tr>
      <td rowspan="3">Bangladesh</td>
      <td rowspan="3">141</td>
      <td>Pre-test * PresPtnt</td>
      <td>0.91 (0.82–1)</td>
    </tr>
    <tr>
      <td>PresPtnt * Seasonal</td>
      <td>0.93 (0.88–0.99)</td>
    </tr>
    <tr>
      <td>PresPtnt</td>
      <td>0.95 (0.92–0.99)</td>
    </tr>
  </tbody>
</table>

#### Addition of a diagnostic test to integrative models improves discrimination

Emerging efforts to develop diagnostic devices, including laboratory assays as well POC tests, have focused on the performance of the test used in isolation. Here, we consider the use of a diagnostic device in combination with clinical predictive models. We used the integrative model to examine the impact that an additional diagnostic would have on discrimination of two of the best performing models. We show that an additional diagnostic, with varying sensitivity and specificity, would improve the cross-validated AUC as expected (Table 3). An additional test with a 70% sensitivity and 70% specificity increases the AUC by 3–5%, while a more specific test could increase the AUC by 10%.

**Table 3.**
 AUC and 95% confidence intervals from 80% training set after adding an additional point-of-care diagnostic test with specified sensitivities (Se.) and specificities (Sp.) to the current patient test and pre-test odds.Additionally, + and - refer to our model indicating a true positive or false positive, respectively, based on the threshold for each model which achieves a 0.90 or 0.95 specificity. Only patients who were prescribed/given antibiotics are included in the count.Table 3—source data 1.Frequency table of pathogens in which the post-test odds formulation with varying specifity (Sp.) chosen have false positives.


<table>
  <thead>
    <tr>
      <th colspan="3"></th>
      <th colspan="2">Specificity=0.90</th>
      <th colspan="2">Specificity=0.95</th>
    </tr>
    <tr>
      <th>Model</th>
      <th>Addl. diag. (Se.,Sp.)</th>
      <th>Auc (95% CI)</th>
      <th>True +</th>
      <th>False +</th>
      <th>True +</th>
      <th>False +</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Pre-test * PresPtnt</td>
      <td>None</td>
      <td>0.839 (0.809–0.869)</td>
      <td>88</td>
      <td>29</td>
      <td>60</td>
      <td>16</td>
    </tr>
    <tr>
      <td>(0.7, 0.7)</td>
      <td>0.876 (0.849–0.902)</td>
      <td>102</td>
      <td>31</td>
      <td>78</td>
      <td>16</td>
    </tr>
    <tr>
      <td>(0.7, 0.95)</td>
      <td>0.933 (0.914–0.952)</td>
      <td>132</td>
      <td>31</td>
      <td>123</td>
      <td>16</td>
    </tr>
    <tr>
      <td>(0.9, 0.95)</td>
      <td>0.972 (0.960–0.984)</td>
      <td>154</td>
      <td>34</td>
      <td>147</td>
      <td>18</td>
    </tr>
    <tr>
      <td rowspan="4">PresPtnt * Seasonal</td>
      <td>None</td>
      <td>0.830 (0.798–0.861)</td>
      <td>70</td>
      <td>25</td>
      <td>54</td>
      <td>11</td>
    </tr>
    <tr>
      <td>(0.7, 0.7)</td>
      <td>0.870 (0.842–0.897)</td>
      <td>101</td>
      <td>27</td>
      <td>68</td>
      <td>14</td>
    </tr>
    <tr>
      <td>(0.7, 0.95)</td>
      <td>0.931 (0.912–0.951)</td>
      <td>130</td>
      <td>27</td>
      <td>121</td>
      <td>16</td>
    </tr>
    <tr>
      <td>(0.9, 0.95)</td>
      <td>0.971 (0.959–0.984)</td>
      <td>154</td>
      <td>30</td>
      <td>149</td>
      <td>18</td>
    </tr>
    <tr>
      <td rowspan="4">PresPtnt</td>
      <td>None</td>
      <td>0.809 (0.776–0.842)</td>
      <td>66</td>
      <td>31</td>
      <td>41</td>
      <td>15</td>
    </tr>
    <tr>
      <td>(0.7, 0.7)</td>
      <td>0.857 (0.827–0.886)</td>
      <td>98</td>
      <td>33</td>
      <td>68</td>
      <td>16</td>
    </tr>
    <tr>
      <td>(0.7, 0.95)</td>
      <td>0.925 (0.904–0.946)</td>
      <td>129</td>
      <td>33</td>
      <td>117</td>
      <td>18</td>
    </tr>
    <tr>
      <td>(0.9, 0.95)</td>
      <td>0.968 (0.955–0.981)</td>
      <td>153</td>
      <td>34</td>
      <td>149</td>
      <td>18</td>
    </tr>
  </tbody>
</table>

We next examined ROC curves, which visually demonstrate the effect of additional diagnostics with varying levels of sensitivity and specificity (Figure 5). We show that a similar level of sensitivity and specificity is achievable by the model with the pre-test information versus the model with seasonal information. Additionally, the additional diagnostics result in improved overall sensitivity and specificity corresponding to sensitivity and specificity of the diagnostic. The overall sensitivity and specificity of each model is greater than the diagnostic alone.

![Figure 5.](https://cdn.elifesciences.org/articles/63009/elife-63009-fig5-v1.jpg)

**Figure 5.:** Curves shown for three models with additional diagnostics.

### Breaking the conditional independence assumption can be addressed using 2-D Kernel density estimates

Our integrative post-test odds method assumes the conditional independence of its component tests, and thus we performed simulation of increasingly conditionally dependent components to assess the performance of the method when the assumption is broken. We showed that the AUC of the post-test odds model deteriorates quickly as the conditional independence assumption is violated (Table 4). With no conditional dependence between predictions from models X and Y, the result using one-dimensional kernel density is comparable to the result with two-dimensional kernel density model. However, as the conditional correlation between the tests increase to −0.90, the one-dimensional AUC decreases by about 11% while the post-test odds with the two-dimensional test performs consistently across this range of conditional correlation.

**Table 4.**
 Average AUC’s from one-dimensional and two-dimensional kernel density estimates (KDE) when the post-test odds conditional independence assumption is broken.The table shows the factor ($\gamma$) used to simulate induced conditional dependence between two covariates and their average conditional correlation. Additionally, it shows the average AUC resulting from a post-test odds model where a one-dimensional kernel density estimate (conditional independence assumed) is generated for each covariate, and a post-test odds model where a two-dimensional joint kernel density estimate is derived for the two covariates.


<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th colspan="2">AUC</th>
    </tr>
    <tr>
      <th>γ</th>
      <th>c⁢o⁢r⁢(X,Y∥Z)</th>
      <th>1D-KDE</th>
      <th>2D-KDE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>-2.000</td>
      <td>−0.894</td>
      <td>0.725</td>
      <td>0.830</td>
    </tr>
    <tr>
      <td>-1.000</td>
      <td>−0.709</td>
      <td>0.758</td>
      <td>0.828</td>
    </tr>
    <tr>
      <td>-0.500</td>
      <td>−0.446</td>
      <td>0.824</td>
      <td>0.838</td>
    </tr>
    <tr>
      <td>0.000</td>
      <td>0.002</td>
      <td>0.838</td>
      <td>0.836</td>
    </tr>
    <tr>
      <td>0.500</td>
      <td>0.448</td>
      <td>0.836</td>
      <td>0.836</td>
    </tr>
    <tr>
      <td>1.000</td>
      <td>0.708</td>
      <td>0.831</td>
      <td>0.840</td>
    </tr>
    <tr>
      <td>2.000</td>
      <td>0.894</td>
      <td>0.810</td>
      <td>0.836</td>
    </tr>
  </tbody>
</table>

### Clinician use of an integrative predictive model for diarrhea etiology could result in large reductions in inappropriate antibiotic prescriptions

Given that one potential application of an integrative predictive model for diarrhea etiology would be as support for clinical decision making for antibiotic use (i.e. antibiotic stewardship), we then examined the impact that the top predictive model would have on prescription of antibiotics by clinicians in GEMS. Of the 3366 patients included in our study, 2653 (79%) were treated with or prescribed antibiotics, 806 (30%) of whom were prescribed to those with a viral-only etiology as determined by qPCR. Here, we examined how use of integrative predictive model could have altered antibiotic use in our sample. Of the 681 patients in the 20% test set, 540 (79%) were prescribed antibiotics, including 166 (30%) with a viral-only etiology. Of those prescribed/given antibiotics the model with pre-test odds, with threshold chosen for an overall specificity of 0.90, identified 88 (53%) viral cases as viral, and 29 non-viral cases as viral. With an additional diagnostic with a sensitivity and specificity of 0.70, the same model would on average identify 102 (61%) viral cases as viral with the same 31 non-viral cases identified as viral. Assuming that clinicians would not prescribe antibiotics for those cases identified by the predictive model with the additional diagnostic as viral, we would avoid 88 (53%) and 102 (61%) of inappropriate antibiotic prescriptions in the two scenarios described. The majority of the false positives (29 and 30 in the two scenarios) were episodes majority attributed to Shigella, ST-ETEC, and combinations of rotavirus with a non-viral pathogen (Table 3—source data 1). All of these false positive, with exception of 1 case, had non-bloody diarrhea, and thus would have been deemed as not requiring antibiotics by WHO IMCI guidelines.

## Discussion

The management of illness in much of the world relies on clinical decisions made in the absence of laboratory diagnostics. Such empirical decision-making, including decisions to use antibiotics, are informed by variable degrees of clinical and demographic data gathered by the clinician. Traditional clinical prediction rules focus on the clinical data from the presenting patient alone. In this analysis, we present a method that allows flexible integration of multiple data sources, including climate data and clinical or historical information from prior patients, resulting in improved predictive performance over traditional predictive models utilizing a single source of data. Using this formulation, if certain sources of data such as climate or previous patient information are not available (e.g. due to a lack of internet connection or data infrastructure), the prediction can still be made using current patient information or seasonality, as appropriatethe other sources. A mobile phone application is an ideal platform for a decision support tool implemented in low-resource settings. Through internet access by wifi or cellular data, a smartphone platform could automatically download recent patient or climate data, while its portability would facilitate clinicians in entering current patient clinical information. We show that application of such a predictive model, especially with an additional diagnostic test, may translate to reductions in inappropriate antibiotic prescriptions for pediatric viral diarrhea.

The global burden of acute infectious diarrhea is highest in low- and middle-income countries (LMICs) in southeast Asia and Africa (Walker et al., 2013), where there is limited access to diagnostic testing. The care of children in these regions could greatly benefit from an accurate and flexible decision making tool. Decisions for treatment are often empiric and antibiotics are over-prescribed (Rogawski et al., 2017), although the majority of cases of diarrhea do not benefit from antibiotic use and also many instances of acute watery diarrhea are self-limiting . For example, 2653 (79%) of the 3366 patients in our study were treated with or prescribed antibiotics. Of these 806 (30%) were prescribed to those with a viral-only etiology. Unnecessary antibiotic use exposes children to significant adverse events including serious allergic reactions (Logan et al., 2016, Marra et al., 2009) and clostridium difficile infection (Jernberg et al., 2010), and contributes to increased antimicrobial resistance. We show that a predictive model can be used to discriminate between those with and without a viral-only etiology and that the inappropriate use of antibiotics can be avoided in 54% cases using our model with no additional diagnostics.

We found using within rolling-origin-recalibration evaluation that models which include either the pre-test odds calculated historical rates or the seasonal test were the best at discriminating between viral etiologies and other etiologies, a finding that held true across training and testing set sizes. However, in the leave-one-out validation, models which included the alternate pre-test odds and climate tended to perform the best. This difference is likely due to the generalizeability of the individual tests, i.e, the leave-one-out tests are trained at the continental level and the effect of climate on etiology is intuitively more generalizeable than seasonal curves which are very specific to each location. We found that our integrative model with only the historical (pre-test) information included (without additional diagnostics) would have identified a viral-only etiology in 88 (53%) patients who received antibiotics. We then show that even the use of an additional diagnostic test with modest performance (70% sensitivity and specificity) would further decrease inappropriate antibiotic use by another 14 (for a total of 102, or 61% of) patients. In the context of calls by the WHO for the development of affordable rapid diagnostic tools (RDTs) for antibiotic stewardship (Declaration, 2017), our findings suggest that development and evaluation of novel RDTs should not be performed in isolation. Potential for integration of rapid diagnostic tests into clinical prediction algorithms should be considered, although this needs to be balanced with the additional time and resources needed. The incremental improvement in discriminative performance achieved by the addition of an RDT to a clinical prediction algorithm may not be cost-effective in lower resourced settings. Finally, providing this model in the form of a decision support tool to the clinician could translate to reductions in inappropriate use of antibiotics, although further research needs to be done to explore the degrees of certainty that clinicians require to alter treatment decisions.

The novel use of kernel density estimates to derive the conditional tests when calculating the post-test odds enabled a flexibility in model input. While kernel density estimates have been used for conditional feature distributions in Naïve Bayes classifiers (John and Langley, 1995, Murakami and Mizuguchi, 2010), here we show that they can be used to derive conditional likelihoods for diagnostic tests constituting one or more features, stressing the effect of the overall test on the post-test odds and not individual features. As such, complicated machine learning models can be combined with simple diagnostics as part of the post-test odds. For example, we could have fit neural networks in lieu of logistic regression models, and in addition to these more complicated models, it is possible to incorporate the result of an RDT that make results available to the clinician at the point-of-care. Additionally, our method of using two-dimensional kernel density estimates can also be used to overcome the conditional independence assumption for tests based on potentially interrelated diagnostic information. Densities with higher than two dimensions can be considered, though, computational limitations are likely in both speed and, we expect, accuracy, as the dimensions increase.

Our study has a number of limitations. First, a robust training set of both cases and non-cases is required to adequately build the conditional kernel densities. Second, the post-test odds calculation, at the time of prediction, lacks interpretation on a feature level like a logistic regression or decision tree. Although, we do observe the effect of a test on an observation, we cannot see which features caused that effect without diving deeper into the training of the diagnostic tests.Thirdly, the prediction algorithm generated by the post-test odds model using GEMS data was only validated internally, and further studies are need for external validation and field implementation. Fourth, our estimation of antibiotic use reduction used data from a clinical research study, which may have biases inherent to such studies. Last, our study uses the AFe cut-off of greater than or equal to 0.5 to assign etiology from the qPCR data. This cutoff was selected based on expert elicitation, but the effect of using this cut-off has not been explored. Bacterial cases with AFe¡0.5 were excluded in our analysis, but may still benefit from antibiotic treatment.

In conclusion, we have developed a clinical prediction model that integrates multiple sources external to the presenting patient, through use of a post-test odds framework and showed that it improved diagnostic performance. When applied to the etiological diagnosis of pediatric diarrhea, we demonstrate its potential for reducing inappropriate antibiotic use. The flexible inclusion or exclusion of output from its components makes it ideal for decision support in lower resourced settings, when only certain data may be available due to limitations in information computation or connectivity. Additionally, the ability to incorporate new training data in real-time to update decisions allows the model to improve as more data is collected. Such a predictive model has the potential to improve the management of pediatric diarrhea, including the rational use of antibiotics in lower resourced settings.
