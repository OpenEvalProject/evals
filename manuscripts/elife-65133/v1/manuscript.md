# Relationship between changing malaria burden and low birth weight in sub-Saharan Africa: A difference-in-differences study via a pair-of-pairs approach

## Authors

- Siyu Heng<sup>1</sup> ([ORCID: 0000-0002-9313-3667](https://orcid.org/0000-0002-9313-3667))
- Wendy P O'Meara<sup>3</sup>
- Ryan A Simmons<sup>3</sup>
- Dylan S Small<sup>2</sup> ([ORCID: 0000-0003-4928-2646](https://orcid.org/0000-0003-4928-2646)) †

### Affiliations

1. Graduate Group in Applied Mathematics and Computational Science, School of Arts and Sciences, University of Pennsylvania Philadelphia United States
2. Department of Statistics, The Wharton School, University of Pennsylvania Philadelphia United States
3. Global Health Institute, School of Medicine, Duke University Durham United States
4. Department of Biostatistics and Bioinformatics, School of Medicine, Duke University Durham United States

† Corresponding author

## Abstract

Background:According to the World Health Organization (WHO), in 2018, an estimated 228 million malaria cases occurred worldwide with most cases occurring in sub-Saharan Africa. Scale-up of vector control tools coupled with increased access to diagnosis and effective treatment has resulted in a large decline in malaria prevalence in some areas, but other areas have seen little change. Although interventional studies demonstrate that preventing malaria during pregnancy can reduce the rate of low birth weight (i.e. child’s birth weight <2500 g), it remains unknown whether natural changes in parasite transmission and malaria burden can improve birth outcomes.Methods:We conducted an observational study of the effect of changing malaria burden on low birth weight using data from 18,112 births in 19 countries in sub-Saharan African countries during the years 2000–2015. Specifically, we conducted a difference-in-differences study via a pair-of-pairs matching approach using the fact that some sub-Saharan areas experienced sharp drops in malaria prevalence and some experienced little change.Results:A malaria prevalence decline from a high rate (Plasmodium falciparum parasite rate in children aged 2-up-to-10 (i.e. PfPR2-10) > 0.4) to a low rate (PfPR2-10 < 0.2) is estimated to reduce the rate of low birth weight by 1.48 percentage points (95% confidence interval: 3.70 percentage points reduction, 0.74 percentage points increase), which is a 17% reduction in the low birth weight rate compared to the average (8.6%) in our study population with observed birth weight records (1.48/8.6 ≈ 17%). When focusing on first pregnancies, a decline in malaria prevalence from high to low is estimated to have a greater impact on the low birth weight rate than for all births: 3.73 percentage points (95% confidence interval: 9.11 percentage points reduction, 1.64 percentage points increase).Conclusions:Although the confidence intervals cannot rule out the possibility of no effect at the 95% confidence level, the concurrence between our primary analysis, secondary analyses, and sensitivity analyses, and the magnitude of the effect size, contribute to the weight of the evidence suggesting that declining malaria burden can potentially substantially reduce the low birth weight rate at the community level in sub-Saharan Africa, particularly among firstborns. The novel statistical methodology developed in this article–a pair-of-pairs approach to a difference-in-differences study–could be useful for many settings in which different units are observed at different times.Funding:Ryan A. Simmons is supported by National Center for Advancing Translational Sciences (UL1TR002553). The funder had no role in study design, data collection and interpretation, or the decision to submit the work for publication.

## Introduction

In 2018, according to the WHO, 2019 published by the WHO, an estimated 228 million malaria cases occurred worldwide, with an estimated 405,000 deaths from malaria globally (WHO, 2019). Dellicour et al., 2010 estimated that around 85 million pregnancies occurred in 2007 in areas with stable Plasmodium falciparum (one of the most prevalent malaria parasites) transmission and therefore were at risk of malaria. Pregnant women are particularly susceptible to malaria, even if they have developed immunity from childhood infections, in part because parasitized cells in the placenta express unique variant surface antigens (Rogerson et al., 2007). Women who are infected during pregnancy may or may not experience symptoms, but the presence of parasites has grave consequences for both mother and unborn baby. Parasites exacerbate maternal anemia and they also sequester in the placenta, leading to intrauterine growth restriction, low birth weight (i.e. birth weight <2500 g), preterm delivery and even stillbirth and neonatal death. Preventing malaria during pregnancy with drugs or insecticide treated nets has a significant impact on pregnancy outcomes (Eisele et al., 2012; Kayentao et al., 2013; Radeva-Petrova et al., 2014).

Observational and interventional studies of malaria in pregnant women are complicated by the difficulty of enrolling women early in their pregnancy. However, in one study, early exposure to Plasmodium falciparum (before 120 days gestation), prior to initiating malaria prevention measures, was associated with a reduction in birth weight of more than 200 g and reduced average gestational age of nearly 1 week (Schmiegelow et al., 2017). For other representative studies on the negative influence of malaria infection during early pregnancy on birth outcomes, see Menendez et al., 2000, Ross and Smith, 2006, Huynh et al., 2011, Valea et al., 2012, Walker et al., 2014, and Huynh et al., 2015. These results suggest the impact of malaria infection on stillbirths, perinatal, and neonatal mortality may be substantial and needs more careful examination (Fowkes et al., 2020; Gething et al., 2020).

In the last few decades, malaria burden has declined in many parts of the world. Although the magnitude of the decline is difficult to estimate precisely, some reports suggest that the global cases of malaria declined by an estimated 41% between 2000 and 2015 (WHO, 2016) and the clinical cases of Plasmodium falciparum malaria declined by 40% in Africa between 2000 and 2015 (Bhatt et al., 2015). However, estimates of changing morbidity and mortality do not account for the effects of malaria in pregnancy. In the context of global reductions in malaria transmission, we expect fewer pregnancies are being exposed to infection and/or exposed less frequently. This should result in a significant reduction in preterm delivery, low birth weight and stillbirths. However, declining transmission will also lead to reductions in maternal immunity to malaria. Maternal immunity is important in mitigating the effects of malaria infection during pregnancy as is evidenced by the reduced impact of malaria exposure on the second, third and subsequent pregnancies. Thus, we anticipate a complex relationship between declining exposure and pregnancy outcomes that depends on both current transmission and historical transmission and community-level immunity (Mayor et al., 2015).

Understanding the potential causal effect of a reduction in malaria burden on the low birth weight rate is crucial as low birth weight is strongly associated with poor cognitive and physical development of children (McCormick et al., 1992; Avchen et al., 2001; Guyatt and Snow, 2004). Although we know from previous interventional studies that preventing malaria in pregnancy is associated with higher birth weight (Eisele et al., 2012; Radeva-Petrova et al., 2014), we do not know whether natural changes in malaria transmission intensity are similarly associated with improved birth outcomes. To address this question, we make use of the fact that while the overall prevalence of malaria has declined in sub-Saharan Africa, the decline has been uneven, with some malaria-endemic areas experiencing sharp drops and others experiencing little change. We use this heterogeneity to assess whether reductions in malaria prevalence reduce the proportion of infants born with low birth weight in sub-Saharan African countries. Our approach conducts a difference-in-differences study (Card and Krueger, 2000; Angrist and Pischke, 2008; St. Clair and Cook, 2015) by leveraging recent developments in matching, a nonparametric statistical analysis approach that can make studies more robust to bias that can arise from statistical model misspecification (Rubin, 1973; Rubin, 1979; Hansen, 2004; Ho et al., 2007).

## Materials and methods

### Overview

In this analysis, we combine two rich data sources: (1) rasters of annual malaria prevalence means (Bhatt et al., 2015) and (2) the Demographic and Health Surveys (DHS) (ICF, 2019), and we marry two powerful statistical analysis methods of adjusting for covariates – difference-in-differences (Card and Krueger, 2000; Abadie, 2005; Athey and Imbens, 2006; Angrist and Pischke, 2008; Dimick and Ryan, 2014; St. Clair and Cook, 2015) and matching (Rubin, 1973; Rubin, 2006; Rosenbaum, 2002; Hansen, 2004; Stuart, 2010; Zubizarreta, 2012; Pimentel et al., 2015). We match geographically proximal DHS clusters that were collected in different time periods (early vs. late) and then identify pairs of early/late clusters that have either maintained high malaria transmission intensity or experienced substantial declines in malaria transmission intensity. We then match pairs of clusters that differ in their malaria transmission intensity (maintained high vs. declined) but are similar in other key characteristics. Once these quadruples (pairs of pairs) have been formed, our analysis moves to the individual births within these clusters. We use multiple imputation to categorize missing children’s birth weight records as either low birth weight or not, relying on the size of the child at birth reported subjectively by the mother and other demographic characteristics of the mother. Finally, we estimate the effect of declined malaria transmission intensity on the low birth weight rate by looking at the coefficient of the malaria prevalence indicator (low vs. high) contributing to the low birth weight rate in a mixed-effects linear probability model adjusted for covariates that are potential confounding variables, the group indicator (individual being within a cluster with declined vs. maintained high malaria transmission intensity), and the time indicator (late vs. early).

### Data resources

The data we use in this work comes from the following three sources:

### Data selection procedure

In this article, we set the study period to be the years 2000–2015, and correspondingly, all the results and conclusions obtained in this article are limited to the years 2000–2015. We set the year 2000 as the starting point of the study period for two reasons. First, the year 2000 is the earliest year in which the estimated annual $𝑃𝑓PR_{2-10}$ is published by MAP, 2020. Second, according to Bhatt et al., 2015, ‘the year 2000 marked a turning point in multilateral commitment to malaria control in sub-Saharan Africa, catalysed by the Roll Back Malaria initiative and the wider development agenda around the United Nations Millennium Development Goals'. We set the year 2015 as the ending point based on two considerations. First, when we designed our study in the year 2017, the year 2015 was the latest year in which the estimated annual $𝑃𝑓PR_{2-10}$ was available to us. We became aware after starting our outcome analysis that MAP has published some post-2015 estimated annual $𝑃𝑓PR_{2-10}$ data since then, but, following Rubin, 2007’s advice to design observational studies before seeing and analyzing the outcome data, we felt it was best to stick with the design of our original study for this report and consider the additional data in a later report. Second, the year 2015 was set as a target year by a series of international goals on malaria control. For example, the United Nations Millennium Development Goals set a goal to ‘halt by 2015 and begin to reverse the incidence of malaria’ and `the more ambitious target defined later by the World Health Organization (WHO) of reducing case incidence by 75% relative to 2000 levels.’ (WHO, 2008; Bhatt et al., 2015). It is worth emphasizing that although we set the years 2000–2015 as the study period and did not investigate any post-2015 MAP data because of the above considerations, those published or upcoming post-2015 MAP data should be considered or leveraged for future related research or follow-up studies.

After selecting 2000–2015 as our study period, we take the middle point years 2007 and 2008 as the cut-off and define the years 2000–2007 as the ‘early years’ and the years 2008–2015 as the ‘late years.’ We include all the sub-Saharan countries that satisfy the following two criteria: (1) The rasters of estimated annual $𝑃𝑓PR_{2-10}$ between 2000 and 2015 created by the Malaria Atlas Project include that country. (2) For that country, IPUMS-DHS contains at least one standard DHS between 2000 and 2007 (‘early year’) and at least one standard DHS between 2008 and 2015 (‘late year’), and both surveys include the cluster GPS coordinates. If there is more than one early (late) years for which the above data are all available, we chose the earliest early year (latest late year). This choice was made to maximize the time interval for the decrease of malaria prevalence, if any, to have an effect on the birth weight of infants. For those countries that have at least one standard DHS with available cluster GPS data in the late year (2008–2015), but no available standard DHS or GPS data in the early year (2000–2007), we still include them if they have a standard DHS along with its GPS data for the year 1999 (with a possible overlap into 1998). In this case, we assign MAP annual $𝑃𝑓PR_{2-10}$ estimates from 2000 to the 1999 DHS data. This allows us to include two more countries, Cote d’Ivoire and Tanzania. The 19 sub-Saharan African countries that meet the above eligibility criteria are listed in Table 1.

**Table 1.**
 The 19 selected sub-Saharan African countries along with their chosen early/late years of malaria prevalence (i.e. estimated parasite rate $𝑃𝑓PR_{2-10}$) and IPUMS-DHS early/late years.Note that some DHS span over two successive years.


<table>
  <thead>
    <tr>
      <th rowspan="2">Country</th>
      <th colspan="2">Malaria prevalence</th>
      <th colspan="2">IPUMS-DHS</th>
    </tr>
    <tr>
      <th>Early year</th>
      <th>Late year</th>
      <th>Early year</th>
      <th>Late year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Benin</td>
      <td>2001</td>
      <td>2012</td>
      <td>2001</td>
      <td>2011–12</td>
    </tr>
    <tr>
      <td>Burkina Faso</td>
      <td>2003</td>
      <td>2010</td>
      <td>2003</td>
      <td>2010</td>
    </tr>
    <tr>
      <td>Cameron</td>
      <td>2004</td>
      <td>2011</td>
      <td>2004</td>
      <td>2011</td>
    </tr>
    <tr>
      <td>Congo Democratic Republic</td>
      <td>2007</td>
      <td>2013</td>
      <td>2007</td>
      <td>2013–14</td>
    </tr>
    <tr>
      <td>Cote d’Ivoire</td>
      <td>2000</td>
      <td>2012</td>
      <td>1998–99</td>
      <td>2011–12</td>
    </tr>
    <tr>
      <td>Ethiopia</td>
      <td>2000</td>
      <td>2010</td>
      <td>2000</td>
      <td>2010–11</td>
    </tr>
    <tr>
      <td>Ghana</td>
      <td>2003</td>
      <td>2014</td>
      <td>2003</td>
      <td>2014</td>
    </tr>
    <tr>
      <td>Guinea</td>
      <td>2005</td>
      <td>2012</td>
      <td>2005</td>
      <td>2012</td>
    </tr>
    <tr>
      <td>Kenya</td>
      <td>2003</td>
      <td>2014</td>
      <td>2003</td>
      <td>2014</td>
    </tr>
    <tr>
      <td>Malawi</td>
      <td>2000</td>
      <td>2010</td>
      <td>2000</td>
      <td>2010</td>
    </tr>
    <tr>
      <td>Mali</td>
      <td>2001</td>
      <td>2012</td>
      <td>2001</td>
      <td>2012–13</td>
    </tr>
    <tr>
      <td>Namibia</td>
      <td>2000</td>
      <td>2013</td>
      <td>2000</td>
      <td>2013</td>
    </tr>
    <tr>
      <td>Nigeria</td>
      <td>2003</td>
      <td>2013</td>
      <td>2003</td>
      <td>2013</td>
    </tr>
    <tr>
      <td>Rwanda</td>
      <td>2005</td>
      <td>2014</td>
      <td>2005</td>
      <td>2014–15</td>
    </tr>
    <tr>
      <td>Senegal</td>
      <td>2005</td>
      <td>2010</td>
      <td>2005</td>
      <td>2010–11</td>
    </tr>
    <tr>
      <td>Tanzania</td>
      <td>2000</td>
      <td>2015</td>
      <td>1999</td>
      <td>2015–16</td>
    </tr>
    <tr>
      <td>Uganda</td>
      <td>2000</td>
      <td>2011</td>
      <td>2000–01</td>
      <td>2011</td>
    </tr>
    <tr>
      <td>Zambia</td>
      <td>2007</td>
      <td>2013</td>
      <td>2007</td>
      <td>2013–14</td>
    </tr>
    <tr>
      <td>Zimbabwe</td>
      <td>2005</td>
      <td>2015</td>
      <td>2005–06</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>

From Table 1, we can see that among the 19 countries, only two countries (Congo Democratic Republic and Zambia) happen to take the margin year 2007 as the early year and no countries take the margin year 2008 as the late year. This implies that our study is relatively insensitive to our way of defining the early years (2000–2007) and the late years (2008–2015) as most of the selected early years and late years in Table 1 do not fall near the margin years 2007 and 2008.

### Statistical analysis

#### Motivation and overview of our approach: difference-in-differences via pair-of-pairs

Our approach to estimating the causal effect of reduced malaria burden on the low birth weight rate is to use a difference-in-differences approach (Card and Krueger, 2000; Abadie, 2005; Athey and Imbens, 2006; Angrist and Pischke, 2008; Dimick and Ryan, 2014; St. Clair and Cook, 2015) combined with matching (Rubin, 1973; Rosenbaum, 2002; Hansen, 2004; Stuart, 2010; Zubizarreta, 2012; Pimentel et al., 2015). In a difference-in-differences approach, units are measured in both an early (before treatment) and late (after treatment) period. Ideally, we would like to observe how the low birth weight rate changes with respect to malaria prevalence within each DHS cluster, so that the DHS clusters themselves could be the units in a difference-in-differences approach. However, this is not feasible because within each country over time the DHS samples different locations (clusters) as the representative data of that country. We use optimal matching (Rosenbaum, 1989; Hansen and Klopfer, 2006) to pair two DHS clusters, one in the early year and one in the late year as closely as possible, mimicking a single DHS cluster measured twice in two different time periods. After this first-step matching, we define the treated units as the high-low pairs of clusters, meaning that the early year cluster has high malaria prevalence (i.e. $𝑃𝑓PR_{2-10}$ > 0.4) while the late year cluster has low malaria prevalence (i.e. $𝑃𝑓PR_{2-10}$ < 0.2), and define the control units as the high-high pairs of clusters, meaning that both the early year and late year clusters have high malaria prevalence (i.e. $𝑃𝑓PR_{2-10}$ > 0.4) and the absolute difference between their two values of $𝑃𝑓PR_{2-10}$ (one for the early year and one for the late year) is less than 0.1. The difference-in-differences approach (Card and Krueger, 2000; Angrist and Pischke, 2008; Dimick and Ryan, 2014; St. Clair and Cook, 2015) compares the changes in the low birth weight rate over time for treated units (i.e. high-low pairs of clusters) compared to control units (i.e. high-high pairs of clusters) adjusted for observed covariates. The difference-in-differences approach removes bias from three potential sources (Volpp et al., 2007):

The traditional difference-in-differences approach requires a parallel trend assumption, which states that the path of the outcome (e.g. the low birth weight rate) for the treated unit is parallel to that for the control unit (Card and Krueger, 2000; Angrist and Pischke, 2008; Dimick and Ryan, 2014; St. Clair and Cook, 2015). One way the parallel trend assumption can be violated is if there are events in the late period whose effect on the outcome differs depending on the level of observed covariates and those observed covariates are unbalanced between the treated and control units across time (Shadish et al., 2002). For example, suppose that there are advances in prenatal care in the late year that tend to be available more in urban areas, then the parallel trends assumption could be violated if there are more treated units (i.e. high-low pairs of clusters) in urban areas than control units (i.e. high-high pairs of clusters). To make the parallel trend assumption more likely to hold, instead of conducting a difference-in-differences study simply among all the treated and control units, we use a second-step matching to pair treated units with control units on the observed covariates trajectories (from the early year to the late year) to make the treated units and control units similar in the observed covariates trajectories as they would be under randomization (Rosenbaum, 2002; Stuart, 2010), and discard those treated or control units that cannot be paired with similar observed covariates trajectories. For example, by matching on the urban/rural indicator trajectories between the treated and control units, we adjust for the potential source of bias resulting from the possibility that there may be advances in prenatal care in the late year that are available more in urban areas.

Another perspective on how our second-step matching helps to improve a difference-in-differences study is through the survey location sampling variability (Fakhouri et al., 2020). Recall that when constructing representative samples, the DHS are sampled at different locations (i.e. clusters) across time (ICF, 2019; Boyle et al., 2019). Therefore, if we simply implemented a difference-in-differences approach over all the high-low and high-high pairs of survey clusters and did not use matching to adjust for observed covariates, this survey location sampling variability may generate imbalances (i.e. different trajectories) of observed covariates across the treated and control groups, and therefore may bias the difference-in-differences estimator (Heckman et al., 1997). Imbalances of observed covariates caused by the survey location sampling variability may occur in the following three cases: (1) The survey location sampling variability is affecting the treated and control groups in the opposite direction. Specifically, there is some observed covariate for which the difference between the high-low pairs of sampled clusters tends to be larger (or smaller) than the country’s overall difference between the high malaria prevalence regions in the early years and the low malaria prevalence regions in the late years and conversely, the difference in that observed covariate between the high-high pairs of sampled clusters tends to be smaller (or larger) than the country’s overall difference between the high malaria prevalence regions in the early years and the high malaria prevalence regions in the late years. (2) The survey location sampling variability is affecting the treated and control groups in the same direction but to different extents. (3) The survey location sampling variability only happened in the treated or control group. Specifically, there is some observed covariate for which the difference between the high-low (or high-high) pairs of sampled clusters tends to differ from the country’s overall difference between the high malaria prevalence regions in the early years and the low (or high) malaria prevalence regions in the late years, but this is not the case for the high-high (or high-low) pairs of sampled clusters. Using matching as a nonparametric data preprocessing step in a difference-in-differences study can remove this type of bias because the observed covariates trajectories are forced to be common among the matched treated and control groups (St. Clair and Cook, 2015; Basu and Small, 2020).

An additional important aspect of our approach is that we use multiple imputation to address missingness in the birth weight records. The fraction of missingness in birth weight in the IPUMS-DHS data set is non-negligible and previous studies have noted that failing to carefully and appropriately address the missing data issue with the birth weight records can significantly bias the estimates of the low birth weight rate derived from surveys in developing countries (Boerma et al., 1996; Robles and Goldman, 1999). We address the missing data issue by using multiple imputation with carefully selected covariates. Multiple imputation constructs several plausible imputed data sets and appropriately combines results obtained from each of them to obtain valid inferences under an assumption that the data is missing at random conditional on measured covariates (Rubin, 1987). Our workflow is summarized in Figure 1, in which we indicate both the data granularity (country-level, cluster-level, and individual-level) and the corresponding steps of our statistical methodology (including the data selection procedure described in the previous section and the Steps 1–4 of the statistical analysis listed below).

![Figure 1.](https://cdn.elifesciences.org/articles/65133/elife-65133-fig1-v1.jpg)

#### Step 1: Proximity prioritized in the matching of high-high and high-low clusters

The DHS collects data from different clusters within the same country in different survey years. To construct pairs of early year and late year clusters which are geographically close such that each pair of clusters can mimic a single cluster measured twice in two different time periods to serve as the unit of a difference-in-differences study, we use optimal matching (Rosenbaum, 1989; Hansen and Klopfer, 2006) to pair clusters within the same country, one from the early year and one from the late year, based on the geographic proximity of their locations. Specifically, we minimize the total rank-based Mahalanobis distance based on the latitude and longitude of the cluster with a propensity score caliper to pair clusters so that the total distance between the paired early year cluster and late year cluster is as small as possible (Rosenbaum, 1989; Hansen and Klopfer, 2006). The number of clusters to pair for each country is set to be the minimum of the number of clusters in the early year and the number of clusters in the late year of that country.

#### Step 2: Matching on sociodemographic similarity is emphasized in second matching

We first divide malaria prevalence into three levels with respect to the estimated Plasmodium falciparum parasite rates $𝑃𝑓PR_{2-10}$ (ranging from 0 to 1): high ($𝑃𝑓PR_{2-10}$ > 0.4), medium ($𝑃𝑓PR_{2-10}$ lies in [0.2, 0.4]), and low ($𝑃𝑓PR_{2-10}$ < 0.2). For clusters in the year 1999, we use the $𝑃𝑓PR_{2-10}$ in the nearest year in which it is available, that is, the year 2000. We select the pairs of the early year and late year clusters as formed in Step 1 described above that belong to either one of the following two categories: (1) High-high pairs: both of the estimated parasite rates of the early year and late year clusters within that pair are high (>0.4), and the absolute difference between the two rates is less than 0.1. (2) High-low pairs: the estimated parasite rate of the early year cluster within that pair is high (>0.4), while the estimated parasite rate of the late year cluster within that pair is low (<0.2). A total of 950 out of 6812 pairs of clusters met one of these two criteria with 540 being high-high pairs and 410 high-low pairs. We removed one high-low pair in which the late year cluster had an estimated parasite rate value (i.e. $𝑃𝑓PR_{2-10}$) of zero for every year between 2000 and 2015; this cluster was in a high altitude area with temperature unsuitable for malaria transmission and thus was not comparable in malaria transmission intensity to its paired early year cluster with high malaria transmission intensity. Since we would like to study the effect of reduced malaria burden on the low birth weight rate of infants, we consider high-low pairs of clusters as treated units and high-high pairs of clusters as control units, and conduct a matched study by matching each high-low pair with a high-high pair that is similar with respect to covariates that might be correlated with either the treatment (changes in malaria prevalence) or the outcome (low birth weight). We allow matches across different countries. The covariates we match on are cluster averages of the following individual-level covariates, where we code the individual-level covariates as quantitative variables with higher values suggesting higher sociodemographic status:

The above six sociodemographic covariates were chosen by looking over the variables in the Demographic and Health Surveys (DHS) and choosing those which we thought met the following criteria: (1) The above six covariates are potentially strongly correlated with both the risk of malaria (Baragatti et al., 2009; Krefis et al., 2010; Ayele et al., 2013; Roberts and Matthews, 2016; Sulyok et al., 2017) and birth outcomes (Sahn and Stifel, 2003; Gemperli et al., 2004; Chen et al., 2009; Grace et al., 2015; Padhi et al., 2015), and therefore may be important confounding variables that need to be adjusted for via statistical matching (Rosenbaum and Silber, 2009; Rosenbaum, 2010; Stuart, 2010). (2) The records of the above six covariates are mostly available for all the countries and the survey years in our study samples. Specifically, for the above six covariates, the percentages of missing data (missingness can arise either because the question was not asked or the individual was asked the question but did not respond) among the total individual records from IPUMS-DHS among the 6812 pairs of clusters remaining after Step 1 are all less than 0.3%.

For each cluster, we define the corresponding six cluster-level covariates by taking the average value for each of the six covariates among the individual records from IPUMS-DHS which are in that cluster, leaving out all missing data. This method of building up cluster-level data from individual-level records from DHS has been commonly used (Kennedy et al., 2011; Larsen et al., 2017). We form quadruples (pairs of pairs) by pairing one high-low pair of clusters (a ‘treated’ unit) with one high-high pair of clusters (a ‘control’ unit), such that all the six cluster-level observed covariates are balanced between both the early and late year clusters for the paired high-low and high-high pairs. We use optimal cardinality matching to form these quadruples (Zubizarreta et al., 2014; Visconti and Zubizarreta, 2018). Optimal cardinality matching is a flexible matching algorithm which forms the largest number of pairs of treated and control units with the constraint that the absolute standardized differences (absolute value of difference in means in standard deviation units; see Rosenbaum, 2010) are less than a threshold; we use a threshold of 0.1, which is commonly used to classify a match as adequate (Neuman et al., 2014; Silber et al., 2016). After implementing the optimal cardinality matching, 219 matched quadruples (pairs of high-low and high-high pairs of clusters) remain. See Figure 2 for illustration of the process of forming matched quadruples (pairs of pairs).

![Figure 2.](https://cdn.elifesciences.org/articles/65133/elife-65133-fig2-v1.jpg)

**Figure 2.:** In Step 1, pairs of clusters from the early and late time periods are matched on geographic proximity and categorized as ‘high-high’ (comparison, or control) or ‘high-low’ (treated). In Step 2, pairs of high-high clusters are matched with pairs of high-low clusters based on cluster-level sociodemographic characteristics. The difference-in-differences estimate of the coefficient of changing malaria burden on the low birth weight rate is based on comparing (D–C) to (B–A).

#### Step 3: Low birth weight indicator with multiple imputation to address missingness

We then conduct statistical analysis at the individual child level. Among all the 19,310 children’s records from the quadruples formed above, we exclude multiple births (i.e. twins, triplets etc), leaving 18,499 records. The outcome variable is the indicator of low birth weight, which is defined as child’s birth weight less than 2500 g. However, 48% of the birth weight records of children among these 18,499 records are missing. To handle this, we perform multiple imputation, under the assumption of missing at random (Heitjan and Basu, 1996), with 500 replications. An important predictor that is available for imputing the missing low birth weight indicator is the mother’s subjective reported size of the child. The mother’s reported size of the child is relatively complete in the IPUMS-DHS data set and has been shown to be a powerful tool to handle the missing data problem with birth weight (Blanc and Wardlaw, 2005). We exclude the small number of records with missing mother’s subjective reported size of the child, leaving 18,112 records, 47% of which (8509 records) have missing low birth weight indicator. Among the 9603 records with observed birth weight, 825 (8.6%) had low birth weight. We first use the bayesglm function (part of the arm package in R) to fit a Bayesian logistic regression for the outcome of the low birth weight indicator among those children for whom low birth weight is not missing. To make it more plausible that the missing at random assumption holds, the following covariates are included as predictors in this regression because they might affect both missingness and the low birth weight rate:

We also include quadratic terms for mother’s age in years and child’s birth order in the regression since according to Selvin and Janerich, 1971, the influences of mother’s age and child’s birth order on the birth weight do not follow a linear pattern. Note that among the remaining 18,112 records, there are no missing data for all of the above covariates. The prior distributions for the regression coefficients follow the default priors of the bayesglm function, that is, independent Cauchy distributions with center 0 and scale set to 10 for the regression intercept term, 2.5 for binary predictors, and 2.5/(2 $\timessd$) for other numerical predictors, where sd is the standard deviation of the predictor in the data used for fitting the regression (i.e. the 9603 records with observed birth weight). This default weakly informative prior has been shown to outperform Gaussian and Laplacian priors in a wide variety of settings (Gelman et al., 2008). After fitting this Bayesian logistic regression model, we get the posterior distribution of the regression coefficient associated with each predictor; see Table 2. From Table 2, we can see that in the imputation model, mother’s age, child’s birth order, mother’s education level, and the mother’s reported birth size are significant predictors, which agrees with the previous literature (e.g. Fraser et al., 1995; Strobino et al., 1995; Richards et al., 2001; Valero De Bernabé et al., 2004).

**Table 2.**
 Summary of the Bayesian logistic regression model fitted over records with observed birth weight which is used to predict missing low birth weight indicators.


<table>
  <thead>
    <tr>
      <th>Predictor</th>
      <th>Posterior mean</th>
      <th>Posterior std</th>
      <th>z-score</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(Intercept)</td>
      <td>1.916</td>
      <td>0.628</td>
      <td>3.051</td>
      <td>0.002**</td>
    </tr>
    <tr>
      <td>Mother’s age (linear term)</td>
      <td>−0.207</td>
      <td>0.045</td>
      <td>−4.562</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Mother’s age (quadratic term)</td>
      <td>0.003</td>
      <td>0.001</td>
      <td>3.987</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Wealth index</td>
      <td>0.060</td>
      <td>0.037</td>
      <td>1.591</td>
      <td>0.112</td>
    </tr>
    <tr>
      <td>Child’s birth order (linear term)</td>
      <td>−0.989</td>
      <td>0.338</td>
      <td>−2.925</td>
      <td>0.003**</td>
    </tr>
    <tr>
      <td>Child’s birth order (quadratic term)</td>
      <td>0.211</td>
      <td>0.086</td>
      <td>2.447</td>
      <td>0.014*</td>
    </tr>
    <tr>
      <td>0 - rural; 1 - urban</td>
      <td>0.126</td>
      <td>0.103</td>
      <td>1.214</td>
      <td>0.225</td>
    </tr>
    <tr>
      <td>Mother’s education level</td>
      <td>−0.226</td>
      <td>0.062</td>
      <td>−3.633</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Child is boy</td>
      <td>−0.068</td>
      <td>0.083</td>
      <td>−0.815</td>
      <td>0.415</td>
    </tr>
    <tr>
      <td>Mother is married or living together</td>
      <td>−0.173</td>
      <td>0.117</td>
      <td>−1.482</td>
      <td>0.138</td>
    </tr>
    <tr>
      <td>Indicator of antenatal care</td>
      <td>−0.046</td>
      <td>0.093</td>
      <td>−0.493</td>
      <td>0.622</td>
    </tr>
    <tr>
      <td>Indicator of low birth size</td>
      <td>2.410</td>
      <td>0.090</td>
      <td>26.776</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Indicator of large birth size</td>
      <td>−1.387</td>
      <td>0.129</td>
      <td>−10.786</td>
      <td>&lt;0.001***</td>
    </tr>
  </tbody>
</table>

We then conduct the following procedure in each run of multiple imputation. For each individual with missing birth weight, we first draw from the posterior distribution of the regression coefficients in Table 2, we then use these regression coefficients and the individual’s covariates (as predictors) to find the probability of the individual having low birth weight and then we use this probability to randomly draw a low birth weight indicator for the individual. We conduct this procedure 500 times, getting 500 independent data sets with imputed low birth weight indicators.

#### Step 4: Estimation of causal effect of reduced malaria burden on the low birth weight rate

For each of the 500 imputed data sets, we then fit a mixed-effects linear probability model (using the lmer function in the R package lme4) where there is a random effect (random intercept) for each cluster to account for the potential correlations between the outcomes among the individual records within the same cluster (Gałecki and Burzykowski, 2013). We include in the model the covariates which might be related to both whether an individual is in a high-low vs. high-high pair of clusters and the low birth weight rate. Specifically we include the predictors from the Bayesian logistic regression for multiple imputation as covariate regressors in the mixed-effects linear probability model (listed in Table 2), except for the mother’s reported birth size. We do not include reported birth size because it is not a pretreatment variable and is a proxy for the outcome (Rosenbaum, 1984). In addition to the above covariates, we include in the model the following three indicators: (1) Low malaria prevalence indicator: indicates whether the individual is from a cluster with a low malaria prevalence ($𝑃𝑓PR_{2-10}$ < 0.2). (2) Time indicator: 0 – if the individual is from a early year cluster; 1 – if the individual is from a late year cluster. (3) Group indicator: 0 – if the individual is from a cluster in a high-high pair of clusters; 1 – if the individual is from a cluster in a high-low pair of clusters. Through adjusting for the time varying covariates via matching and including the above three indicators in the regression, our study uses a difference-in-differences approach for a matched observational study (Wing et al., 2018). Note that even though we do not explicitly incorporate matching into the final model (i.e. the mixed-effects linear probability model [1]), matching still reduces the bias due to potential statistical model misspecification in our analysis by being a nonparametric data preprocessing step which makes the distributions of the observed covariates of the selected treated and control units identical or similar, lessening the dependence of the results on the model used to adjust for the observed covariates (Hansen, 2004; Ho et al., 2007). Let $𝟙⁢(A)$ be the indicator function of event $A$ such that $𝟙⁢(A)=1$ if $A$ is true and $𝟙⁢(A)=0$ otherwise. To conclude, we consider the following mixed-effects linear probability model for the individual $j$ in cluster $i$:

$$
P(Y_{ij}=1∣i,X_{ij})=k_{0}+k_{1}⋅𝟙(i is a low malaria prevalence cluster)+k_{2}⋅𝟙(i is a late year cluster)+k_{3}⋅𝟙(i is\ from\ a\ high-low\ pair\ of\ clusters)+\beta^{T}X_{ij},with two error terms \alpha_{i}∼𝒩(0,\sigma_{0}) and ϵ_{ij}∼𝒩(0,\sigma_{1}).
$$

In Model (1), $Y_{i⁢j}$ is the observed outcome (i.e. the low birth weight indicator) and $𝐗_{i⁢j}$ the covariate regressors (including the quadratic terms of mother’s age and child’s birth order) of the individual $j$ in cluster $i$, and $\alpha_{i}$ is the random effect for cluster $i$. See Table 3 for an interpretation of the coefficients of the three indicators and the intercept term (i.e. the $k_{0},k_{1},k_{2},k_{3}$) within each matched quadruple. The estimated causal effect of reduced malaria burden (low vs. high malaria prevalence) on the low birth weight rate is the mean value of the 500 estimated coefficients on the low malaria prevalence indicator obtained (i.e. the k1) from 500 runs of the mixed-effects linear regression described above. See Appendix 2 for more details on the statistical inference procedure with multiple imputation, which are also referred to as Rubin’s rules (Carpenter and Kenward, 2012).

**Table 3.**
 An interpretation of the coefficients of the intercept term and the three indicators defined in model (1) (i.e. the $k_{0},k_{1},k_{2},k_{3}$) within each matched quadruple.The coefficient of the low malaria prevalence indicator (i.e. the k1) incorporates the information of the magnitude of the effect of changing malaria burden (from high to low) on the low birth weight rate.


<table>
  <thead>
    <tr>
      <th rowspan="2">Cluster</th>
      <th rowspan="2">Prevalence</th>
      <th rowspan="2">Time</th>
      <th rowspan="2">Pair</th>
      <th rowspan="2">Coefficients</th>
      <th>Within-pair</th>
      <th>Between-pair</th>
    </tr>
    <tr>
      <th>Contrast</th>
      <th>Contrast</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>High</td>
      <td>Early</td>
      <td>High-low</td>
      <td>k0+k3</td>
      <td rowspan="2">k1+k2</td>
      <td rowspan="4">k1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Low</td>
      <td>Late</td>
      <td>High-low</td>
      <td>k0+k1+k2+k3</td>
    </tr>
    <tr>
      <td>3</td>
      <td>High</td>
      <td>Early</td>
      <td>High-high</td>
      <td>k0</td>
      <td rowspan="2">k2</td>
    </tr>
    <tr>
      <td>4</td>
      <td>High</td>
      <td>Late</td>
      <td>High-high</td>
      <td>k0+k2</td>
    </tr>
  </tbody>
</table>

It is worth clarifying that although we take a Bayesian approach when imputing (i.e. predicting) the missing low birth weight indicators in Step 3 (i.e. imputation model) and then take a frequentist approach when conducting the 500 separate outcome analyses with the 500 imputed data sets in Step 4 (i.e. substantive model), these two different statistical perspectives (i.e. Bayesian and frequentist) do not conflict with each other when we apply Rubin’s rules to combine these 500 separate outcome analyses as the single estimator and inference reported in Table 6. This is because the frequentist validity of applying Rubin’s rules to combine separate outcome analyses with multiple imputed data sets only explicitly depends on the asymptotic normal approximation assumption for each coefficient estimator in Model (1) (see Appendix 2 for more details), and does not directly depend on how the multiple imputed data sets are generated (e.g. either using a Bayesian imputation model as in Step 3 or using a frequentist imputation model instead). Using a Bayesian imputation model followed by a frequentist substantive model is one of the most common strategies when applying Rubin’s rules to conduct statistical inference with multiple imputation; see Rubin, 1996, Chapter 3 of Rubin, 1987, and Chapter 2 of Carpenter and Kenward, 2012. For representative works on justifying the advantages of using a Bayesian imputation model in multiple-imputation inferences, see Meng, 1994 and Chapter 2 of Carpenter and Kenward, 2012.

#### Secondary analyses

We also conducted the following four secondary analyses (SA1) – (SA4) which examine the causal hypothesis that reduced malaria transmission intensity cause reductions in the low birth weight rate in various ways.

#### Sensitivity analyses

As discussed in the ‘Motivation and overview of our approach’ section, using matching as a data preprocessing step in a difference-in-differences study can reduce the potential bias that may result from a violation of the parallel trend assumption arising from failing to adjust for observed covariates and the survey location sampling variability when using the survey data to conduct a difference-in-differences study. However, neither matching nor difference-in-differences can directly adjust for unobserved covariates (i.e. unmeasured confounders or events). The estimated treatment effect (i.e. the estimated coefficient of the low malaria prevalence indicator contributing to the low birth weight rate) from our primary analysis can be biased by failing to adjust for any potential unobserved covariates. How potential unobserved covariates may bias the estimated effect in a difference-in-differences study has been understood from various alternative perspectives in the previous literature. These alternative perspectives are intrinsically connected and we briefly list three of them here (for more detailed descriptions, see Appendix 3):

To assess the robustness of the results of our primary analysis to potential hidden bias, we adapt an omitted variable sensitivity analysis approach (Rosenbaum and Rubin, 1983a; Imbens, 2003; Ichino et al., 2008; Zhang and Small, 2020). Specifically, our sensitivity analysis model (i.e. Model (3) in Appendix 3) extends Model (1) by including a hypothetical unobserved covariate $U$ that is correlated with both the low malaria prevalence indicator and the low birth weight indicator. Specifically, let $U_{i⁢j}$ denote the value of $U$ of individual $j$ in cluster $i$, we consider the following data generating process for $U_{i⁢j}$:

$$
P(U_{ij}=1)=50%+p_{1}%⋅𝟙(i is a low malaria prevalence cluster)+p_{2}%⋅𝟙(the observed or the imputed Y_{ij}=1),
$$

where $p_{1}$ and $p_{2}$ are prespecified sensitivity parameters of which the unit is a percentage point. Our sensitivity analyses investigate how the estimated treatment effect varies over a range of prespecified values for $(p_{1},p_{2})$. See Appendix 3 for the details of the design of the sensitivity analyses and on how our proposed sensitivity analysis model helps to address the concerns about the hidden bias from Perspectives 1–3 listed above.

## Results

In this section, we report and interpret the results of matching, primary analysis, secondary analyses, and sensitivity analyses relating changes in malaria burden to changes in the birth weight rate between 2000–2015 in sub-Saharan Africa. The R (R Development Core Team, 2020) code for producing all the main results and tables of this article is posted on GitHub (https://github.com/siyuheng/Malaria-and-Low-Birth-Weight, Heng, 2021a, copy archived at swh:1:rev:faf6455f95bca6bab364ab95699ea7cd81af1061 Heng, 2021b).

### Matching

We first evaluate the performance of the first-step matching where we focus on the geographical closeness of paired early year and late year clusters from the following three perspectives: (1) the geographic proximity of the early year and the late year clusters within each pair, which is evaluated through the mean distance of two paired clusters, the within-pair longitude’s correlation and latitude’s correlation between the paired early year and late year clusters, and the mean values of the longitudes and the latitudes of the paired early year and late year clusters; (2) the closeness of the mean annual malaria prevalence ($𝑃𝑓PR_{2-10}$) of the early year and late year clusters at the early year (i.e. the early malaria prevalence year in Table 1); (3) the closeness of the mean annual malaria prevalence of the early year and the late year clusters at the late year (i.e. the late malaria prevalence year in Table 1). We report the results in Table 4, which indicate that the first step of our matching produced pairs of clusters which are close geographically and in their malaria prevalence at a given time. Of note, the mean Haversine distance of the early year clusters and late year clusters is 24.1 km among the 219 high-low pairs of clusters, and 28.7 km among the 219 high-high pairs of clusters. The within-pair longitudes’ and latitudes’ correlations between the paired early year and late year clusters among the high-low and high-high pairs are all nearly one.

**Table 4.**
 The mean Haversine distance of the early year clusters and late year clusters is 24.1 km among the 219 high-low pairs of clusters, and 28.7 km among the 219 high-high pairs of clusters.The within-pair longitudes’ and latitudes’ correlations between the paired early year and late year clusters among the high-low and high-high pairs all nearly equal one. The mean values of the longitudes, the latitudes, the annual malaria prevalence (i.e. $𝑃𝑓PR_{2-10}$) measured at the early year, denoted as $𝑃𝑓PR_{2-10}$ (early), and at the late year, denoted as $𝑃𝑓PR_{2-10}$ (late), of the paired early year clusters (clusters sampled at the early year) and late year clusters (clusters sampled at the late year) among the 219 high-low and 219 high-high pairs of clusters used for the statistical inference respectively. Note that an early year cluster has a late year $𝑃𝑓PR_{2-10}$ and a late year cluster has an early year $𝑃𝑓PR_{2-10}$ since the MAP data contain $𝑃𝑓PR_{2-10}$ for each location and for each year between 2000 and 2015.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">High-low pairs</th>
      <th colspan="2">High-high pairs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mean within-pair haversine distance</td>
      <td colspan="2">24.1 km</td>
      <td colspan="2">28.7 km</td>
    </tr>
    <tr>
      <td>Within-pair correlation of longitude</td>
      <td colspan="2">0.9999</td>
      <td colspan="2">0.9996</td>
    </tr>
    <tr>
      <td>Within-pair correlation of latitude</td>
      <td colspan="2">0.9998</td>
      <td colspan="2">0.9997</td>
    </tr>
    <tr>
      <td></td>
      <td>Longitude</td>
      <td>Latitude</td>
      <td>𝑃𝑓PR2-10 (early)</td>
      <td>𝑃𝑓PR2-10 (late)</td>
    </tr>
    <tr>
      <td>Early clusters among high-low pairs</td>
      <td>16.92</td>
      <td>−1.15</td>
      <td>0.52</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>Late clusters among high-low pairs</td>
      <td>16.88</td>
      <td>−1.15</td>
      <td>0.48</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>Early clusters among high-high pairs</td>
      <td>19.15</td>
      <td>0.43</td>
      <td>0.51</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>Late clusters among high-high pairs</td>
      <td>19.13</td>
      <td>0.46</td>
      <td>0.53</td>
      <td>0.49</td>
    </tr>
  </tbody>
</table>

We then evaluate the performance of the second-step matching, where we focus on the closeness of the sociodemographic status of paired high-low and high-high pairs of clusters, by examining the balance of each covariate among high-low and high-high pairs of early year and late year clusters before and after matching. Recall that for each cluster, we calculate the six cluster-level covariates (i.e. urban or rural, toilet facility, floor facility, electricity, mother’s education level, contraception indicator) by averaging over all available individual-level records in that cluster. In each high-low or high-high pair of clusters, there are 12 associated covariates, six for the early year cluster in that pair and six for the late year cluster in that pair. Table 5 reports the mean of each covariate among high-low pairs of clusters and high-high pairs of clusters before and after matching, along with the absolute standardized differences before and after matching. From Table 5, we can see that before matching, the high-high pairs are quite different from the high-low pairs, all absolute standardized differences are greater than 0.2. The high-low pairs tend to be sociodemographically better off than the high-high pairs (higher prevalence of improved toilet facilities and floor material facilities, higher prevalence of domestic electricity, higher levels of mother’s education, higher rate of contraceptive use, and more urban households). To reduce the bias from these observed covariates, we leverage optimal cardinality matching, as described above, to pair a high-low pair of clusters with a high-high pair and throw away the pairs of clusters for which the associated covariates cannot be balanced well. After matching, we can see that all 12 covariates are balanced well – all absolute standardized differences after matching are less than 0.1.

**Table 5.**
 Balance of each covariate before matching (BM) and after matching (AM).We report the mean of each covariate (including early and late years) for high-low and high-high pairs of clusters, before and after matching. We also report each absolute standardized difference (Std.dif) before and after matching.


<table>
  <thead>
    <tr>
      <th rowspan="3"></th>
      <th colspan="2">Before matching</th>
      <th colspan="2">After matching</th>
      <th colspan="2">Std.dif</th>
    </tr>
    <tr>
      <th>High-low</th>
      <th>High-high</th>
      <th>High-low</th>
      <th>High-high</th>
      <th>BM</th>
      <th>AM</th>
    </tr>
    <tr>
      <th>(410 pairs)</th>
      <th>(540 pairs)</th>
      <th>(219 pairs)</th>
      <th>(219 pairs)</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Urban/rural (early)</td>
      <td>0.44</td>
      <td>0.20</td>
      <td>0.26</td>
      <td>0.26</td>
      <td>0.53</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Urban/rural (late)</td>
      <td>0.60</td>
      <td>0.21</td>
      <td>0.37</td>
      <td>0.32</td>
      <td>0.85</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>Toilet facility (early)</td>
      <td>0.88</td>
      <td>0.60</td>
      <td>0.82</td>
      <td>0.79</td>
      <td>0.86</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Toilet facility (late)</td>
      <td>0.94</td>
      <td>0.69</td>
      <td>0.90</td>
      <td>0.88</td>
      <td>0.90</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Floor material (early)</td>
      <td>1.90</td>
      <td>1.68</td>
      <td>1.60</td>
      <td>1.67</td>
      <td>0.31</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Floor material (late)</td>
      <td>2.22</td>
      <td>1.79</td>
      <td>1.92</td>
      <td>1.87</td>
      <td>0.59</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>Electricity (early)</td>
      <td>0.36</td>
      <td>0.12</td>
      <td>0.17</td>
      <td>0.16</td>
      <td>0.70</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>Electricity (late)</td>
      <td>0.54</td>
      <td>0.18</td>
      <td>0.33</td>
      <td>0.30</td>
      <td>0.99</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Mother’s education (early)</td>
      <td>1.00</td>
      <td>0.36</td>
      <td>0.69</td>
      <td>0.64</td>
      <td>1.36</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Mother’s education (late)</td>
      <td>1.23</td>
      <td>0.42</td>
      <td>0.87</td>
      <td>0.83</td>
      <td>1.78</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Contraception indicator (early)</td>
      <td>0.16</td>
      <td>0.12</td>
      <td>0.15</td>
      <td>0.17</td>
      <td>0.27</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Contraception indicator (late)</td>
      <td>0.22</td>
      <td>0.18</td>
      <td>0.24</td>
      <td>0.26</td>
      <td>0.23</td>
      <td>0.10</td>
    </tr>
  </tbody>
</table>

### Effect of reduced malaria burden on the low birth weight rate

Appendix 1—table 3 summarizes the low malaria prevalence indicators, the time indicators, the group indicators, the covariates, and the birth weights of the 18,112 births in the matched clusters. Table 6 reports the estimated causal effect of reduced malaria burden (low vs. high malaria prevalence) on the rate of births with low birth weight, which is represented as the coefficient on the malaria prevalence indicator (diagnostics for the multiple imputation that was used in generating the estimates in Table 6 are shown in Appendix 2—table 1). We estimate that a decline in malaria prevalence from $𝑃𝑓PR_{2-10}$ > 0.40 to less than 0.20 reduces the rate of low birth weight by 1.48 percentage points (95% confidence interval: 3.70 percentage points reduction, 0.74 percentage points increase). A reduction in the low birth weight rate of 1.48 percentage points is substantial; recall that among the study individuals with nonmissing birth weight, the low birth weight rate was 8.6%, so a 1.48 percentage points reduction corresponds to a 17% reduction in the low birth weight rate. The results in Table 6 also show that there is strong evidence that mother’s age, child’s birth order, mother’s education level and child’s sex are also associated with the low birth weight rate. For example, mothers with higher education level are less likely to deliver a child with low birth weight, and boys are less likely to have low birth weight than girls, which agrees with the previous literature (e.g. Brooke et al., 1989; Valero De Bernabé et al., 2004; Zeka et al., 2008). Our estimated reduction in the low birth weight rate of 1.48 percentage points from reducing malaria prevalence from high to low is similar to that from a naive difference-in-differences estimator that ignores covariates and missingness of birth weight records. The observed low birth weight rates among the records with observed birth weight within the early year clusters in high-low pairs is 9.33%, in the late year clusters in high-low pairs is 7.52%, in the early year clusters in high-high pairs is 9.18%, and in the late year clusters in high-high pairs is 9.06%. Therefore, the naive difference-in-differences estimator for the effect of reduced malaria burden without adjusting for covariates and missingness of birth weight records is (7.52% $−$ 9.33%) $−$ (9.06% $−$ 9.18%) = $−$ 1.69% (i.e. 1.69 percentage points reduction on the low birth weight rate).

**Table 6.**
 Inference with multiple imputation and mixed-effects linear probability model (1).The unit of estimates and CIs is a percentage point.


<table>
  <thead>
    <tr>
      <th>Regressor</th>
      <th>Estimate</th>
      <th>95% CI</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0 - high prevalence; 1 - low prevalence</td>
      <td>−1.48</td>
      <td>[−3.70, 0.74]</td>
      <td>0.191</td>
    </tr>
    <tr>
      <td>0 - early year; 1 - late year</td>
      <td>−0.06</td>
      <td>[−1.82, 1.69]</td>
      <td>0.943</td>
    </tr>
    <tr>
      <td>0 - high-high pairs; 1 - high-low pairs</td>
      <td>0.21</td>
      <td>[−1.40, 1.82]</td>
      <td>0.797</td>
    </tr>
    <tr>
      <td>Mother’s age (linear term)</td>
      <td>−1.86</td>
      <td>[−2.48, −1.23]</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Mother’s age (quadratic term)</td>
      <td>0.03</td>
      <td>[0.02, 0.04]</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Child’s birth order (linear term)</td>
      <td>−13.91</td>
      <td>[−18.49, −9.32]</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Child’s birth order (quadratic term)</td>
      <td>2.91</td>
      <td>[1.82, 4.00]</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Wealth index</td>
      <td>0.09</td>
      <td>[−0.38, 0.56]</td>
      <td>0.709</td>
    </tr>
    <tr>
      <td>0 - rural; 1 - urban</td>
      <td>0.82</td>
      <td>[−0.63, 2.27]</td>
      <td>0.269</td>
    </tr>
    <tr>
      <td>Mother’s education level</td>
      <td>−2.02</td>
      <td>[−2.82, −1.22]</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Child is boy</td>
      <td>−1.75</td>
      <td>[−2.75, −0.74]</td>
      <td>&lt;0.001***</td>
    </tr>
    <tr>
      <td>Mother is married or living together</td>
      <td>−1.43</td>
      <td>[−3.04, 0.19]</td>
      <td>0.083</td>
    </tr>
    <tr>
      <td>Antenatal care indicator</td>
      <td>−0.96</td>
      <td>[−2.06, 0.13]</td>
      <td>0.085</td>
    </tr>
  </tbody>
</table>

Among all the high-low pairs of clusters in our sample, there has been a decrease in the low birth weight rate from the early years to the late years of 1.81 percentage points (from 9.33% to 7.52%) for records with observed birth weight and an estimated decrease of 2.04 percentage points (from 10.48% to 8.44%) when multiple imputation is used to impute missing birth weight records. We now explore how much of this decrease can be attributed to reduced malaria burden over time. The estimated effect in Table 6 of the time indicator (late year vs. early year) is a 0.06 percentage points reduction, which is much less than that of the low malaria prevalence indicator. Moreover, the estimated change in the low birth weight rate over time among high-low pairs that comes from changes in the covariates over time is a 0.52 percentage points reduction. This is calculated by looking at the difference between $\beta^^{T}⁢𝐱¯_{early}$ and $\beta^^{T}⁢𝐱¯_{late}$, where $\beta^^{T}$ is the estimated coefficients of the covariate regressors listed in Table 6, and $𝐱¯_{early}$ and $𝐱¯_{late}$ are the average values in high-low pairs of the covariate regressors of the individuals within the early year clusters and those within the late year clusters respectively. These results suggest that after adjusting for the observed covariates listed in Table 6 and missingness of birth weight records, the observed decrease in the low birth weight rate over time in high-low pairs comes mainly from reduced malaria burden over time instead of changes over time in the low birth weight rate that affect both high-low and high-high pairs of clusters. To illustrate this point and further verify the potentially substantial effect of reduced malaria burden on the low birth weight rate, we also plot the estimated low birth weight rate of each cluster among the high-high pairs and high-low pairs in our study sample in Figure 3. From Figure 3, we can see that although in general, for both high-high pairs and high-low pairs, the birth weight rates of the late year clusters are lower than those of the early year clusters, it is clear that the reductions in low birth weight rate from early year to late year among the high-low pairs are considerably greater than those among high-high pairs, suggesting that reducing community-level malaria burden can potentially substantially reduce the low birth weight rate.

![Figure 3.](https://cdn.elifesciences.org/articles/65133/elife-65133-fig3-v1.jpg)

**Figure 3.:** The estimated low birth weight rate for each cluster are obtained from averaging over all the 500 imputed data sets of the 18,112 individual records. We draw a line to connect two paired clusters (one early year cluster and one late year cluster). Box plots for the low birth weight rates are also shown. Two of the four outliers of the late year clusters among the high-low pairs (i.e. the top four late year clusters in terms of low birth weight rate among the high-low pairs) may result from their extremely small within-cluster sample sizes (no more than three individual records for both two clusters).

### Results of secondary analyses

The results of our secondary analyses support the interpretation of our primary analysis:

### Results of the sensitivity analyses

Recall that in the ‘Sensitivity analyses’ section and Appendix 3, our sensitivity analyses consider a hypothetical unobserved covariate $U$ that is correlated with both the low malaria prevalence indicator and the low birth weight indicator. For various values of the sensitivity parameters $(p_{1},p_{2})$, we report the corresponding point estimates and 95% CIs of the estimated treatment effect (i.e. the coefficient of the low malaria prevalence indicator contributing to the low birth weight rate) in Appendix 3—table 1. The results from Appendix 3—table 1 show that the estimated treatment effect ranges from 1.13 percentage points reduction to 1.83 percentage points reduction (on the low birth weight rate) if both $p_{1}$ and $p_{2}$ are between −10 and 10. Recall that $p_{1}$ (or $p_{2}$) equals 10 (or −10) means that the probability of the $U$ taking value one increases (or decreases) by 10 percentage points if the individual’s low malaria prevalence indicator (or the low birth weight rate indicator) equals 1. That is, allowing both the magnitude of $p_{1}$ and the magnitude of $p_{2}$ can be up to 10 means that we allow the existence of a nontrivial magnitude of unmeasured confounding in our sensitivity analyses. Therefore, the estimated treatment effect ranging from 1.13 percentage points reduction to 1.83 percentage points reduction when both $p_{1}$ and $p_{2}$ are between −10 and 10 means that the magnitude of the estimated treatment effect is still evident (no less than 1.13 percentage points) even if the magnitude of unmeasured confounding is nontrivial (both $|p_{1}|$ and $|p_{2}|$ can be up to 10). See Appendix 3 for the detailed results and interpretations of the sensitivity analyses.

To conclude, although the confidence intervals of the coefficient of the low malaria prevalence indicator on the low birth weight rate presented in the ‘Results’ section cannot exclude a possibility of no effect at level 95% based on our proposed study sample selection procedure and statistical approach, the results and the corresponding interpretations of the primary analysis, the secondary analyses, and the sensitivity analyses have contributed to the weight of the evidence that reduced malaria burden has an important influence on the low birth weight rate in sub-Saharan Africa at the community level.

## Discussion

We have developed a pair-of-pairs matching approach to conduct a difference-in-differences study to examine the causal effect of a reduction in malaria prevalence on the low birth weight rate in sub-Saharan Africa during the years 2000–2015. Although we cannot rule out no effect at a 95% confidence level, the magnitude of the estimated effect of a reduction from high malaria prevalence to low malaria prevalence on the low birth weight rate (1.48 percentage points) is even greater than the estimated effect of a factor thought to be important, antenatal care during pregnancy (0.96 percentage points). In a secondary analysis, we find that reduction in malaria burden from high to low is estimated to be especially crucial for reducing the low birth weight rate of first born children, reducing it by 3.73 percentage points (95% CI: 9.11 percentage points reduction, 1.64 percentage points increase). This agrees with previous studies which demonstrate that the effects of malaria on birth outcomes are most pronounced in the first pregnancy (e.g. McGregor et al., 1983).

Previous studies have shown that individual malaria prevention during pregnancy reduces the chances of the woman’s baby having low birth weight (Kayentao et al., 2013). In this paper, we examine the community-level effect of reductions in malaria on pregnancy outcomes as opposed to the individual-level effect of malaria prevention interventions during pregnancy. Our results support extrapolation of studies of antenatal malaria interventions on birth weight to populations experiencing declining malaria burden. Furthermore, we conclude that reports of declining malaria mortality underestimate the contribution of reduced malaria exposure during pregnancy on pregnancy outcomes and neonatal survival. Although some studies have documented higher rates of adverse pregnancy outcomes in malaria-infected women with declining antimalarial immunity, such as may be seen in communities with declining malaria exposure (Mayor et al., 2015), our study demonstrates that overall reduction in exposure to infection, including during pregnancy, outweighs these individual changes in risk once infected.

Strengths of our study include that we use state-of-the-art causal inference methods on a large representative data set. We develop a novel pair-of-pairs matching approach to conduct a difference-in-differences study to estimate the real world effectiveness of public health interventions by combining DHS data with other data sources. There are two major difficulties when using the DHS data to conduct a difference-in-differences study. The first major difficulty is that within each country the DHS samples different locations (clusters) over different survey years. Our first-step matching handles this difficulty through using optimal matching to pair the early year DHS clusters and the late year DHS clusters within the same country based on the geographic proximity of their locations. Then each formed pair of clusters can mimic a single cluster measured twice in two different survey years, which serves as the foundation of a difference-in-differences study. The second major difficulty is that although an advantage of the DHS data is that they contain many potentially important cluster-level and individual-level covariates, it may be difficult to come up with a statistical model that is both efficient and robust to adjust for these covariates. A traditional approach to estimating the real world effectiveness of an intervention in such settings is to run a regression of an outcome of interest on a measure of adherence to the treatment (zero if in the period before the intervention was available and ranging from 0 to 1 after the intervention was available), covariates (individual-level and cluster-level covariates) and a random effect for the cluster (Goetgeluk and Vansteelandt, 2008). This regression approach relies heavily on correct specification of the model by which the covariates affect the outcome (e.g. linear, quadratic, cubic), therefore the result can be severely biased by model misspecification (Rubin, 1973; Hansen, 2004; Ho et al., 2007). We instead use a second-step matching to first optimally select and match the treated units (i.e. high-low pairs of clusters) and control units (i.e. high-high pairs of clusters) to ensure that they have balanced distributions of covariates across time and then run the regression with the dummy variables for the matched sets. Such a nonparametric data preprocessing step before running a regression can potentially reduce bias due to model misspecification (Rubin, 1973; Hansen, 2004; Ho et al., 2007).

Our merged study data set makes use of two aspects of the richness of the relevant data resources. First, from the perspective of sample size and length of time span, the data set includes over 18,000 births in 19 countries in sub-Saharan Africa and describes changes in the low birth weight rate over a 15-year period. Some of the studied regions had substantial changes in malaria parasite prevalence during this time period, whereas others did not, which provides us ample heterogeneity necessary for conducting a difference-in-differences study. Second, from the perspective of the comprehensiveness of information, our merged data set includes various types of information: from cluster-level to individual-level records; from geographic to sociodemographic characteristics; from surveyed data to predicted data.

Some potential limitations of our study should be considered. First, we discretized the mean malaria prevalence (i.e. $𝑃𝑓PR_{2-10}$ from 0 to 1) into high ($𝑃𝑓PR_{2-10}$ > 0.4), medium ($𝑃𝑓PR_{2-10}$ lies in [0.2, 0.4]), and low ($𝑃𝑓PR_{2-10}$ < 0.2), which means that the magnitude of the estimated causal effect depends on how we define these cut-offs. Our primary analysis suggests that reducing the malaria burden from high to low may substantially help control the low birth weight rate, and our secondary analyses suggest that a more dramatic reduction in malaria prevalence can lead to a more dramatic drop in the low birth weight rate. More research needs to be done on the minimum magnitude of the reduction in malaria prevalence that is needed to cause a substantial drop in the low birth weight rate. Second, we assigned the malaria prevalence (i.e. $𝑃𝑓PR_{2-10}$) data to children’s records based on the DHS survey years which may not be exactly the same years as children’s actual birth years. For example, a child whose age is three years at the corresponding DHS survey year should have been born three years earlier before that DHS survey year, in which case we might have assigned the wrong $𝑃𝑓PR_{2-10}$ to that child’s gestational period. We examined this issue via SA1 and the result suggested that this did not induce much bias to the results of our primary analysis.

The novel design-based causal inference approach developed in this work, a pair-of-pairs matching approach to conduct a difference-in-differences study (i.e. the two-step matching procedure to form matched pairs of pairs as a nonparametric data preprocessing step in a difference-in-differences study), is potentially useful for researchers who would like to reduce the estimation bias due to potential model misspecification in the traditional difference-in-differences approach. Moreover, the general statistical methodology developed in this work can be applied beyond the malaria settings to handle the heterogeneity of survey time points and locations in data sets such as the Demographic and Health Surveys (DHS).

In summary, the contribution of malaria to stillbirth and neonatal mortality, for which low birth weight is a proxy, are currently not accounted for in global estimates of malaria mortality. Using a large representative data set and innovative statistical evidence, we found point estimates that suggested that reductions in malaria burden at the community level substantially reduce the low birth weight rate. To our knowledge, this is the first study of its kind to evaluate the causal effects of malaria control on birth outcomes using a causal inference framework. Although our confidence intervals do include a possibility of no effect, the evidence from our primary analysis and secondary analyses is strong enough to merit further study and motivate further investments in mitigating the intolerable burden of malaria.
