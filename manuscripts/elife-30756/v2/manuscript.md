# Conjunction of factors triggering waves of seasonal influenza

## Authors

- Ishanu Chattopadhyay<sup>1</sup> ([ORCID: 0000-0001-8339-8162](https://orcid.org/0000-0001-8339-8162))
- Emre Kiciman<sup>3</sup> ([ORCID: 0000-0001-5429-468X](https://orcid.org/0000-0001-5429-468X))
- Joshua W Elliott<sup>4</sup>
- Jeffrey L Shaman<sup>5</sup>
- Andrey Rzhetsky<sup>1</sup> ([ORCID: 0000-0001-6959-7405](https://orcid.org/0000-0001-6959-7405)) †

### Affiliations

1. Institute of Genomics and Systems Biology University of Chicago Chicago United States
2. Department of Medicine University of Chicago Chicago United States
3. Information and Data Science Group Microsoft Research Redmond United States
4. Computation Institute University of Chicago Chicago United States
5. Department of Environmental Health Sciences, Mailman School of Public Health Columbia University New York United States
6. Departments of Human Genetics University of Chicago Chicago United States

† Corresponding author

## Abstract

Using several longitudinal datasets describing putative factors affecting influenza incidence and clinical data on the disease and health status of over 150 million human subjects observed over a decade, we investigated the source and the mechanistic triggers of influenza epidemics. We conclude that the initiation of a pan-continental influenza wave emerges from the simultaneous realization of a complex set of conditions. The strongest predictor groups are as follows, ranked by importance: (1) the host population’s socio- and ethno-demographic properties; (2) weather variables pertaining to specific humidity, temperature, and solar radiation; (3) the virus’ antigenic drift over time; (4) the host population’€™s land-based travel habits, and; (5) recent spatio-temporal dynamics, as reflected in the influenza wave auto-correlation. The models we infer are demonstrably predictive (area under the Receiver Operating Characteristic curve 80%) when tested with out-of-sample data, opening the door to the potential formulation of new population-level intervention and mitigation policies.

## Introduction

Seasonal influenza is a serious threat to public health, claiming tens of thousands of lives every year. A large number of past studies have focused on identifying the likely factors responsible for initiating each seasonal disease wave. Typically, each such study focused on one or a few hypothetical factors. Our study aimed at an integrative, joint analysis of numerous suggested disease triggers, comparing their relative importance and possible cooperation in triggering pan-US waves of seasonal influenza infection. The goal of this study was to identify the most informative combinations of statistical predictors associated with the initiation of pan-US influenza infection waves.

### Recent computational studies of influenza:

Computational study of the dynamics and factors influencing infectious disease spread began with compartmental models, such as the Susceptible-Infected-Resistant (SIR) model, which traces its origins to the beginning of the last century (Kermack and McKendrick, 1927). Initially a purely theoretical tool, these SIR-style models were subsequently enhanced with population and geographic data, allowing their application to specific cities and the distances between them (Keeling and Rohani, 2002). For instance, one approach, termed ‘gravity wave’ modeling, used geographic, short- and long-range, work-related human movement and demographic data to formulate gravity potentials between US counties in order to infer the dynamics of infection spread (Viboud et al., 2006).

Some studies have focused on one specific factor affecting infection, such as air travel, to simulate the spread of influenza (Colizza et al., 2006); other studies used SIR models, generalized for a collection of interconnected geographic areas, spatial-network or patch models, to model a number of common infections, including influenza, measles, and foot-and-mouth disease (Riley, 2007).

More ambitious network model approaches have simulated the global transmission of infectious disease using high-resolution, worldwide population data and the locations of International Air Transport Association (IATA)-indexed airports (Balcan et al., 2009). Similar to (Viboud et al., 2006), the authors of the study computed the global infection-pre-disposing ‘gravity field’ over the network of international airports. This network-based approach was subsequently developed further (Balcan and Vespignani, 2011) through the modeling of ‘phase transition’–that is the chain-reaction switch of geographic infection status–in complex networks, utilizing approaches introduced in theoretical physics.

Another layer of sophistication was achieved by incorporating rich historical records. For example, Eggo et al. (Eggo et al., 2011) modeled the Spanish influenza epidemic of 1918–1919, using mortality documents from both the UK and the US, explicitly accounting for the size and distances between cities. In the same spirit, Brockmann and Helbing (Brockmann and Helbing, 2013) represented infection as diffusion on a complex network, estimating arrival times for infection across the globe.

Following the formulation of the hypothesis that absolute humidity modulates influenza survival and transmission (Shaman and Kohn, 2009), researchers began incorporating climate variables into SIR-like models (Chowell et al., 2012). More recent dynamic models have incorporated a probabilistic description of influenza infection’s spatial transitions in space and time, accounting for selected demographic confounders (Gog et al., 2014) and (Charu et al., 2017).

In this study, rather than following the SIR-style modeling tradition, we used statistical epidemiology- and econometric-like approaches, in addition to a causality-network method presented here for the first time. There are some prior studies that are close to ours in spirit (but not in details). For example, (Barreca and Shimshack, 2012) used historical US influenza mortality data (1973–2002) in conjunction with collinear humidity and temperature records to establish county-level statistical associations between variables in the datasets. They concluded that absolute humidity was ‘an especially critical determinant of observed human influenza mortality, even after controlling for temperature.’ Another study, focusing on historical influenza records in the Netherlands, (te Beest et al., 2013) used the number of weekly influenza-like patient visits (transformed into an estimated rate of infection) as a response variable in a regression analysis of climate data. They concluded that the bulk of explained variation (57%) was attributed to the depletion of susceptible hosts during the disease season and non-weather-related ‘between-season effects,’ with only 3% explained by absolute humidity, represented as a continuous predictor variable. Additionally, this study observed that school holidays did not have a statistically significant effect on influenza transmission.

As all causality detection methods come with dissimilar limitations and are imperfect in unique ways, we designed our study intentionally to attack the same target problem using three different statistical approaches: Approach 1: A non-parametric Granger analysis (Granger, 1980) focusing on infection flows’ directionalities across the US and whether influenza propagates via long- vs. short-distance travel (we run analysis across all pairs of air- and land-travel county neighbors, respectively). Approach 2: A mixed-effect Poisson regression (Hedeker and Gibbons, 2006) explicitly accounting for the auto-correlation of infection waves in time and space, along with the full set of socioeconomic, climate, and geographic predictors. Approach 3: A county-matching, non-parametric analysis to identify the minimum predictive set of factors that distinguish those counties associated with the onset of the influenza season (Morgan and Winship, 2015).

Our study became possible through access to several, very large longitudinal datasets: (1) a nine-year collection of insurance records capturing the dynamics of influenza-like illnesses (ILIs) in the United States (Truven MarketScan database, see Materials and methods); (2) temporally collinear, high-resolution weather measurements over every US county; (3) detailed air travel (The United States Bureau of Transportation Statistics, 2010) and geographic proximity data (The United States Census, 2016) showing connectivity between US counties; (4) billions of geo-located Twitter messages reflecting long- and short-distance human movement patterns, and; (5) US census data accounting for US county and county-equivalent population distribution, demographic, and socioeconomic properties (HRSA, 2016). An explicit comparison of the ILI data in the insurance claims to the influenza records provided by the Center for Disease Control and Prevention (CDC, 2016) showed that the two sources agree well ($ρ=0.91,p=3.5\times10^{-201}$), with insurance claims providing higher data resolution, see Figure 1—figure supplement 1. Curiously, the relationship between the two sources of ILI observations is not linear: We attribute this to the lower resolution of the CDC data. These three types of analysis produce congruent–albeit not identical–results.

## Results

The logical flow of our analysis is as follows: (1) We first show that our definition of ILIs corresponds well with CDC data, and that our causality coefficients, defined in Approach 1, have similar meanings to coefficients in the regression analysis; (2) We then explain the outcomes of the analysis according to Approach 1; (3) We then analyze the importance of putative casual factors, Figure 1, as applied to an initiation of influenza season, Figure 2; (4) In Approach 2, we pay special attention to the relative importance of short- and long-distance travel in influenza propagation, Figure 4; (5) We further test the best regression model in terms of predictive accuracy, Figure 5, using disjointed data parts for training and testing, and; (6) We culminate our analysis with a county-matching analysis, Figure 6.

![Figure 1.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-v2.jpg)

**Figure 1.:** Plate A shows the significant variables along with their computed influence coefficients from the mixed-effect Poisson regression analysis (the best model chosen from $126$ different regression equations with different variable combinations). The statistically significant estimates of fixed effects are grouped into several classes: climate variables, economic and demographic variables, auto-regression variables, variables related to travel, and those related to antigenic diversity (see the last entry in Table 5 for the detailed regression equation used. The complete list of all models considered is given in Table S-D7). The fixed-effect regression coefficients plotted in Plate A are shown on a logarithmic scale, meaning that the absolute magnitude of predictor-specific effect is obtained by exponentiating the parameter value. A negative coefficient for a predictor variable suggests that the influenza rate falls as this factor increases, while a positive coefficient predicts a growing rate of infection as the parameter value grows. The integrated influence of individual predictors, under this model, is additive with respect to the county-specific rate of infection. For example, a coefficient of $-0.6$ for parameter AVG_PRESS_mean tells us that the average atmospheric pressure has a negative association with the influenza rate. As the mean atmospheric pressure for the county grows, the probability that the county would participate in an infection initiation wave falls. As $exp⁡(-0.6)=0.54$, the rate of infection drops by $46%$ when atmospheric pressure increases by one unit of zero-centered and standard-deviation-normalized atmospheric pressure. Similarly, an increase in the share of a white Hispanic population predicts an increase in influenza rate: A coefficient of 1.3 translates into a $exp⁡(1.3)\times100%-100%=267%$ rate increase, possibly, because of the higher social network connectivity associated with this segment of population. Plates B - I enumerate the average spatial distribution of a few key significant factors considered in Poisson regression: (B) average temperature; (C) average maximum specific humidity; (D) average wind velocity in miles per hour; (E) average solar flux; (F) logarithm of population density (people per square mile); (G) total precipitation; (H) income, and; (I) percent of poor as deviations about the country average. Plates J-M show the strong dependence between our estimated antigenic diversity (normalized, see Definition in text) corresponding to the HA, NA, M1, and M2 viral proteins, and the cumulative fraction of the inoculated population (normalized between 0 and 1), where both sets of variables are geo-spatially and temporally stratified. Pearson’s correlation tests shown in Plates J-M were performed under null hypothesis that there the two quantities (plotted along axes X and Y) are statistically independent ($H_{0}:ρ=0$).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Plate A: Diverse data sets processed via multiple techniques to reach convergent, and reinforcing, conclusions. Approach 1 (the Granger-causality analysis) shows that the epidemic tends to begin near water bodies, and that short-range travel is more influential compared to air travel for propagation. Approach 2 (Poisson regression) identifies significant predictive factors, suggesting that the epidemic begins near the southern shores of the US, and corroborates the result on short- vs. long-range travel. Approach 3 (county-matching) points to south eastern shores of the continental US as where the epidemic initiates, and identifies a validated subset of predictive factors. Plate B shows that influenza prevalence as reported by Truven dataset positively correlates with CDC reports. Plate C illustrates that our conclusions regarding a putatively causal influence between neighboring counties, inferred using different techniques (mixed-effect regression vs. non-parametric Granger-causality), match up positively. Pearson’s correlation tests shown in Plates B and C are performed under null hypothesis that there the two types of quantities (plotted along axes X and Y) are statistically independent ($H_{0}:ρ=0$).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-figsupp2-v2.jpg)

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-figsupp3-v2.jpg)

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** We note that with the exception of the antigenic variation of the surface protein hemagglutinin (HA), and some derivatives of maximum absolute humidity, significant mass of the individual violin plots fall either entirely on the positive or entirely on the negative half-plane; implying that the significant factors rarely flip sign. Thus, while the coefficients inferred change as we explore different models, the direction of influence remains mostly unchanged.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-figsupp5-v2.jpg)

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** As expected, we yielded more informative models as we increased complexity.

![Figure 2.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig2-v2.jpg)

**Figure 2.:** Characteristics of seasonal influenza in the continental US An analysis of county-specific, weekly reports on the number of influenza cases for a period of $471$ weeks spanning January 2003 to December 2013 (Plates A-H) for recurrent patterns of disease propagation.In particular, the weeks leading up to that in which an epidemic season peaks (determined by significant infection reports from the maximum number of counties for that season) demonstrate an apparent flow of disease from south to north, which cannot be explained by population density alone (also see movie in Supplement). Plate I illustrates the near-perfect time table for a seasonal epidemic. Plates J and K compare the county-specific initiation probabilities of an influenza season, and the causality streamlines.

**Table 1.**
 Social connectivity: The US Southern region appears to have an unusually high level of social connectivity.(In GSS survey results, the number of close friends, close friends who are neighbors, and number of friends who all or mostly know each other is higher in the South, especially in the East/South/Central census region, than in the country at large.)


<table>
  <thead>
    <tr>
      <th></th>
      <th>WSC (TX, OK, AR, LA)</th>
      <th>ESC (MS, AL, TN, KY)</th>
      <th>SA (FL, GA, SC, NC, VA, WV, MD, DC)</th>
      <th>Country-at-large</th>
      <th>WNC (ND, SD, NE, KS, MO, IA, MN) (not in South/Southeast) this is the second most social region following ESC (MS, AL, TN, KY)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Close friends</td>
      <td>7.22</td>
      <td>12.76</td>
      <td>8.20</td>
      <td>7.57</td>
      <td>10.56</td>
    </tr>
    <tr>
      <td>Close friends who are neighbors</td>
      <td>1.02</td>
      <td>3.40</td>
      <td>1.32</td>
      <td>1.45</td>
      <td>3.15</td>
    </tr>
    <tr>
      <td>% of friends who all or mostly know each other</td>
      <td>All:20% Mostly: 43%</td>
      <td>All:18% Mostly: 58%</td>
      <td>All: 11% Mostly: 52%</td>
      <td>All: 12 Mostly: 50%</td>
      <td>All: 16% Mostly: 58%</td>
    </tr>
    <tr>
      <td>How often visit closest friends*</td>
      <td>107</td>
      <td>151</td>
      <td>126</td>
      <td>122</td>
      <td>129</td>
    </tr>
  </tbody>
</table>

_*Survey options are: lives in household, daily, several times a week, once a week, once a month, several times a year, and less often. These are converted to approximate number of visits per year (see Supplement for more information about the GSS analysis)._

**Table 2.**
 Fisher’s exact test results on matched treatment combinations


<table>
  <thead>
    <tr>
      <th>YR</th>
      <th>dh⋆0</th>
      <th>dh⋆1</th>
      <th>dt⋆0</th>
      <th>h⋆</th>
      <th>t⋆</th>
      <th>u⋆</th>
      <th>M1⋆</th>
      <th>M2⋆</th>
      <th>V⋆0</th>
      <th>V⋆1</th>
      <th>a⋆</th>
      <th>p-value</th>
      <th>Odds ratio</th>
      <th>Lower 99% cnf. bnds.</th>
      <th>Upper 99% cnf. bnds.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2003</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>1.9×10-8</td>
      <td>2.83</td>
      <td>1.73</td>
      <td>4.66</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>6.5×10-3</td>
      <td>6.22</td>
      <td>1.08</td>
      <td>132.03</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>3.4×10-6</td>
      <td>8.31</td>
      <td>2.16</td>
      <td>54.93</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>5.3×10-7</td>
      <td>4.56</td>
      <td>1.96</td>
      <td>12.0</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>2.1×10-2</td>
      <td>3.85</td>
      <td>0.82</td>
      <td>28.16</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>1.9×10-3</td>
      <td>5.26</td>
      <td>1.23</td>
      <td>50.2</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>3.1×10-10</td>
      <td>4.78</td>
      <td>2.38</td>
      <td>10.34</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>X</td>
      <td>1.4×10-2</td>
      <td>3.64</td>
      <td>0.93</td>
      <td>24.27</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>Y</td>
      <td>X</td>
      <td>X</td>
      <td>4.9×10-11</td>
      <td>4.91</td>
      <td>2.51</td>
      <td>10.05</td>
    </tr>
    <tr>
      <td>All Years</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>X</td>
      <td>7.2×10-9</td>
      <td>3.88</td>
      <td>2.10</td>
      <td>7.89</td>
    </tr>
    <tr>
      <td>All Years</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.48</td>
      <td>2.15</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Fisher’s exact test results on matched treatment combinations


<table>
  <thead>
    <tr>
      <th>(a)</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>YR p</th>
      <th>-value 99%</th>
      <th>Conf. Bnd.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>max hus avg</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2003</td>
      <td>0.003603</td>
      <td>1.0, 4.21</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>0.6919</td>
      <td>0.16, 17.63</td>
    </tr>
    <tr>
      <td>2005 0.</td>
      <td>1948</td>
      <td>0.61, 7.89</td>
    </tr>
    <tr>
      <td>2006 0.</td>
      <td>6525 0.28, 3.06</td>
      <td></td>
    </tr>
    <tr>
      <td>2007 0.</td>
      <td>3574 0.49, 18.85</td>
      <td></td>
    </tr>
    <tr>
      <td>2008 0.</td>
      <td>103</td>
      <td>0.55, 1.23</td>
    </tr>
    <tr>
      <td>2009 0</td>
      <td>.1067</td>
      <td>0.68, 8.77</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>0.5318</td>
      <td>0.27, 41.03</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>0.09054</td>
      <td>0.74, 5.17</td>
    </tr>
    <tr>
      <td>ALL YRS</td>
      <td>1[1]10-4</td>
      <td>1.12, 1.88</td>
    </tr>
    <tr>
      <td>t avg mean</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2003</td>
      <td>0.06439</td>
      <td>0.81, 3.65</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>1</td>
      <td>0.27, 10.62</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>0.003339</td>
      <td>1.17, 123.0</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>0.8172</td>
      <td>0.29, 4.0</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>0.537</td>
      <td>0.47, 7.42</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>0.05985</td>
      <td>0.59, Inf</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>0.0006337</td>
      <td>1.37, 51.68</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>0.2853</td>
      <td>0.50, 9.28</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>0.05729</td>
      <td>0.85, 3.49</td>
    </tr>
    <tr>
      <td>ALL YRS 5.87</td>
      <td>[1]10-9</td>
      <td>1.36, 2.23</td>
    </tr>
    <tr>
      <td>d hus 0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2003</td>
      <td>0.5374</td>
      <td>0.55, 3.41</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>1</td>
      <td>0.27, 11.01</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>0.04401</td>
      <td>0.81, 7.13</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>0.001708</td>
      <td>1.31, Inf</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>0.009199</td>
      <td>1.0, 37.34</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>0.3051</td>
      <td>0.60, 5.92</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>0.02726</td>
      <td>0.82, 90.16</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>1</td>
      <td>0.41, 2.78</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>0.577</td>
      <td>0.57, 2.77</td>
    </tr>
    <tr>
      <td>ALL YRS</td>
      <td>1.48[1]10-5</td>
      <td>1.12, 1.64</td>
    </tr>
    <tr>
      <td>d t avg mean 0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2003</td>
      <td>0.004956</td>
      <td>1.0, 24.12</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>0.445</td>
      <td>0.14, 6.0</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>0.001164</td>
      <td>1.23, 12.03</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>0.01198</td>
      <td>0.97, 11.08</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>0.01147</td>
      <td>0.96, 11.05</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>0.08552</td>
      <td>0.74, 11.18</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>0.06847</td>
      <td>0.73, 17.69</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>0.08251</td>
      <td>0.15, 1.63</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>0.6031</td>
      <td>0.47, 3.55</td>
    </tr>
    <tr>
      <td>ALL</td>
      <td>YRS 4.98[1]10-11</td>
      <td>1.35, 2.06</td>
    </tr>
  </tbody>
</table>

### Approach 1: Causality streamlines from non-parametric granger analysis

Our analysis of health insurance claims covers nine years of influenza cycles ($2003$ to $2011$, inclusively), see Figure 2. We visualized weekly, county-level prevalence as a movie (see Supplement); Figure 2A–H show a few relevant weekly snapshots from different years. The plates in Figure 2A–H, and especially the movie, clearly show that seasonal influenza cycles initiate in the South/Southeastern US and sweep the country from south to north. This pattern is repeated, with some variation, each season.

Figure 3G shows the country-wide propagation dynamics as represented by our computed causality streamlines. The alignment of causality flow vectors into long, continuous streamlines suggests a stable propagation mechanism across the country; the probability of a long sequence of summary movement vectors accidentally matching in the direction by mere chance is vanishingly small ($p<10^{-16}$ for longer streamlines).

![Figure 3.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig3-v2.jpg)

**Figure 3.:** Plates C and D: Transformation to difference-series, $i.e.$, change in the number of reported cases between weeks. We imposed a binary quantization, with positive changes mapping to ‘1,’ and negative changes mapping to ‘0.’ From a pair of such symbol streams, we computed the direction-specific coefficients of Granger causality (see Supplement). For each county, we obtained a coefficient for each of its neighbors, which captured the degree of influence flowing outward to its respective neighbors (Plate L). We computed the expected outgoing influence by considering these coefficients as representative of the vector lengths from the centroid of the originating county to centroids of its neighbors. Viewed across the continental US, we then observed the emergence of clearly discernible paths outlining the ‘causality field’ (Plate G). The long streamlines shown are highly significant, with the probability of chance occurrence due to accidental alignment of component stitched vectors less than $10^{-185}$; while each individual relationship has a chance occurrence probability of $∼6%$ (Plates E and F). Plate H: Spatially-averaged travel patterns (see text in Materials and methods) and the sink distribution between expected travel patterns. These patterns (Plate H), along with the inferred causality field (Plate I), match up closely, with sinks showing up largely in the Southern US, explaining the central role played there. In Plate H, the size of the blue circles indicate the percentage of movement streamlines (computed by interpreting the locally averaged movement directions as a vector field) that sink to those locations. In Plate I, the size of the red circles indicate the percentage of causality streamlines that sink to the indicated locations. We note that $∼75%$ of the movement streamlines sink in counties belonging to the Southern states, which matches up well with the sinks of the causality streamlines. In Plates J and K show spatial analysis results for two different infections (HIV and E. coli, respectively) and which exhibit very different causality fields, negating the possibility of boundary effects.

Do epidemics originate from the same counties season after season? To answer this question, we follow ‘causality streamlines’ back to their source county. Informally, influenza onset in these source counties has little or no causal dependency on their neighbors. That is, their epidemic states are seemingly caused by factors outside of disease prevalence in other counties. Figure 2K presents the county-specific likelihood of streamline initiation across our nine years of data. To verify the near-shores position of these source counties is not a mere manifestation of a boundary effect of shore counties (no neighbors at the side of large water body), we carried out identical causality analyses with two different infections, specifically choosing diseases less likely to share etiologies with influenza: HIV and Escherichia coli. The results for both HIV and Escherichia coli infections are shown in Figure 3J and K, which exhibit flow patterns very different from those obtained for influenza. These streamlines almost never originate from the coasts, thus reducing the likelihood that the pattern observed for influenza is a geo-spatial boundary effect. Combined with the exceedingly low probability ($∼10^{-185}$) of chance inference for the streamlines, this strongly supports our conclusion that the epidemics are of coastal origin.

We directly validated our conclusion that influenza waves tend to start in the South by identifying counties which seem to trigger the epidemic. We computed a ‘trigger period’ of five to six weeks for each season, defined as the period immediately preceding an exponential increase in influenza dispersion. To calculate this weekly dispersion, we treated each county as a node in an undirected graph, each with an edge connecting two geographically adjacent counties–only if they had both reported at least one influenza case in the specified week. We defined dispersion as the size of the largest, connected component in this undirected graph. Thus, a trigger period describes the period in which the size of the giant component of the infection graph rises above $250$ counties from being under $100$ as shown in Figure 2I, and then proceeds to the seasonal peak. Figure 2J presents the likelihood of a county being part of this largest, connected component during the trigger period. In the second approach, we followed causality streamlines back to their source county. Figure 2K presents the county-specific likelihood of streamline initiation across nine years.

These approaches produced qualitatively similar results (Figure 2J and K). While epidemics seem to start in many places around the country (see the origins of streamlines in Figure 3J and I), they successfully gain traction near large bodies of water (as evidenced by the most likely places of epidemic onset, see Figure 2J and K)). Otherwise, they fizzle out before triggering an actual epidemic cycle (see Figure 2J). Seasonal initiation is neither spatially uniform nor simply a reflection of county-specific population density.

Our analysis of the Twitter movement matrix indicates that people most frequently travel between neighboring counties, preferentially towards higher-population-density areas, which shows that the maximum-probability movement patterns follow the local gradient of increasing population density (see Figure 4—figure supplement 1). In contrast, the geo-spatially-averaged movement vectors for each county reveal global flows in the movement patterns (see Figure 3H, along with Methods for the calculation of spatial averages).

Figure 3H–I suggest that average movement patterns largely agree with the influenza streamlines: Both patterns, especially in the South/Southeast of the country, are associated with flow pointing away from large bodies of water.

In addition to looking at the direction of short-range travel, we used our non-parametric Granger analysis to investigate the comparative strength of short- vs. long-range influenza propagation. In the first case, we considered the neighborhood map shown in Figure 4A (for a detailed definition of ”neighbors,’ see Materials and methods), and the in the second case, we considered associations between major, airport-bearing counties (see Figure 4B). We then plotted the distribution of the maximum pairwise coefficient of causality, where the maximization is carried out by fixing the source and the target and varying the delay in weeks, after which we attempt to predict the target stream.

![Figure 4.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig4-v2.jpg)

**Figure 4.:** Plate B shows air connectivity as links between airports, with edge thickness proportional to traffic volume. Plate C shows the delay in weeks for the propagation of Granger-causal influence between counties in which major airports are located, and Plate E shows the distribution of the inferred causality coefficient between those same counties. Plates D and F show the delay and the causality coefficient distribution respectively, which we computed by considering spatially neighboring counties. The results show that local connectivity is more important. We reached a similar conclusion using mixed-effect Poisson regression, as shown in Plate G: The inferred coefficients for land connectivity are significantly larger than those for air connectivity, tweet-based connectivity, or exponential diffusion from the top $30$ largest airports. The coefficients shown in Plate G are exponentiated, allowing us to visualize probability magnitudes (see ‘Model Definition’).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig4-figsupp1-v2.jpg)

Conclusions associated with Approach 1: The inferred causality streamlines computed from the infection time series in all counties (Figure 3) show that epidemics are mostly triggered near large water bodies and flow inland and away. They also illustrate that the US continental Southern states act as ‘sinks’ to a large proportion of these streamlines. (‘Sinks,’ in our definition here, are geographic areas that multiple streamlines converge towards; sinks are especially obvious when we look at the vector representation of causality direction. The opposite of a ‘sink’ is a ‘source,’ defined as an area at which at least one streamline starts.) This might explain the increased prevalence in the designated region. Additionally, the analysis shows that human travel is a very important driver of emergent epidemiological patterns, and that short-range, land-based travel is more important than air-travel. This result is cross-corroborated by our Poisson regression analysis (described next in Approach 2).

Approaches 2 and 3 are motivated by the ‘why’ questions: (1) Why do epidemics initiate where and when they do? and; (2) Why do some disease initiations become epidemics while others do not?

### Approach 2: Importance of factors from poisson regression

We focused on a subset of weeks associated with the initial rise of influenza waves (indicated by the gray bars in Figure 2I, and calculated as discussed earlier). The results from our best-fit model are illustrated in Figure 1A. We selected this particular model out of a total of $126$ compared in the Bayesian analysis, a few of which we list in Table 5, ranked by their decreasing goodness-of-fit, measured with the Deviance Information Criterion, DIC (see Supplement). From the values of the inferred coefficients corresponding to the different factors, and taking into account their significance levels and credible intervals, we concluded that the roles played by weather variables, particularly humidity, appear to be substantially more complicated compared to what has been suggested in the literature.

#### The surprisingly unimportant factors

School schedule was not predictive of influenza onset in our analysis: We ended up with a $p$-value of $0.84$ and an odds ratio of $0.8403$, strongly suggesting that school opening dates are not a significant factor in triggering the seasonal epidemic.

We are not claiming here that closing down schools during the seasonal peak, or during an initial phase of a seasonal epidemic, would not have a beneficial effect on maximum incidence. Rather, the observed epidemiological patterns over the time period we analyzed (2003–2011) do not seem to name ‘school opening times’ as a significant predictive factor–at least in the continental US.

We factored in the effect of vaccination coverage by estimating the cumulative fraction of the population that received the current influenza vaccine stratified by geo-spatial location and time of inoculation within each influenza season. Our analysis indicated that vaccination coverage is not a significant predictor of influenza onset/triggering period. It could be a reflection of overall vaccine ineffectiveness, or the choice of outcome predicted (i.e. vaccination might effect overall infection numbers over the entire outbreak, but not the timing of the trigger). It could also reflect the fact that different influenza type/subtypes have different virulence–so a vaccine against H3N2 during an H3N2 year, may be more effective, but due to that fact that H3N2 is more virulent, more people still wind up seeking medical care.

Vaccination coverage failed to reach predictive significance. The variables corresponding to spatio-temporal indicators of the cumulative fraction of the inoculated population are included in our best model (see the last entry in Table 5), but their effect fails to be significant. However, if we drop those variables from the model, the DIC increases. We suggest that the strong dependence between antigenic diversity and vaccination coverage (see Figure 1J–M) is responsible for this effect: Vaccination coverage is important, but its influence is captured by the antigenic variation.

#### The most important factors

The strongest predictor groups (ranked by importance) are the population’s socio-demographic properties, weather, antigenic drift of the virus, land-based travel, and auto-correlation of influenza waves.

Weather As far as weather effects are concerned, epidemics tend to originate in places with high mean, maximum specific humidity, high average temperature, and low average air pressure, namely, in counties at the Southern, and, to a lesser extent, Eastern and Western US coastlines. Additionally, the spread of an epidemic is significantly influenced by a drop in specific humidity up to four weeks before its onset. However, this effect is weaker than the mean maximum specific humidity effect. Drop in average temperature that dips one to three weeks prior to the epidemic onset is also significantly important (this is consistent with earlier experiments [Lowen et al., 2008]), especially when the temperature drop is accompanied by a decrease in specific humidity, average wind speed, and solar flux. However, high levels of solar flux in the week of onset are also important. This complicated set of weather conditions, a signature of the cold air front (Shaman et al., 2010), is validated by our out-of sample predictions to increase the risk of triggering the seasonal epidemic. Total precipitation also plays a positive role.

#### The weather/humidity paradox

How can colder weather and lower humidity be a predictor of influenza, if influenza epidemic waves tend to start in the South with warmer climates and higher humidity? Our resolution of this seeming controversy is as follows: The stress is on the drop in both humidity and temperature in those areas with high average annual values of these measurements. A blast of colder, lower-humidity weather in these warm-climate areas has two effects: (1) The influenza virus can stay viable in water droplets longer than in hot, sunny weather, and; (2) Humans tend to interact indoors, in more crowded conditions. Both of these factors are favorable for transmission of the virus to the population at large.

Antigenic variation Antigenic diversity for HA, NA, M1, and M2 are important predictors. While HA, NA, and M1 inhibit the trigger, M2 diversity enhances it. This peculiar difference in the direction of influence might be a manifestation of the roles played by the individual viral proteins in its life-cycle.

The first three proteins are directly involved in the viral binding to host cell surface receptors, while M2 activity is needed only during HA biosynthesis. Additionally, proteolysis experiments indicated that M2 proton channel activity helped to protect (H1N1)pdm09 HA from premature conformational changes as it traversed low-pH compartments during transport to the cell surface (Alvarado-Facundo et al., 2015).

We found that antigenic diversity is a significant predictor in all four of the viral proteins we considered. Interestingly, while the increasing diversity found in HA, NA, and M1 inhibits the epidemic trigger, the higher diversity in M2 enhances it (see Discussion).

Travel Land travel intensity one to three weeks before epidemic onset is a strong predictor. Air travel is also predictive, but its strength is an order of magnitude weaker than that of land travel.

Autocorrelation The increase in an influenza outbreak’s infection weekly rate one and two weeks before an epidemic onset (in the epidemic source county itself) is predictive of epidemic wave origin.

We have used substantially richer datasets than those used by earlier studies (Shaman et al., 2010; Tamerius et al., 2013), which lends strong statistical support to our conclusions. It also allowed us to disentangle and make precise the contributions from different factors, $e.g.$, mean county humidity vs. drops in humidity before an infection. While we found the former effect to be clearly stronger (in accordance to previously reported results [Shaman et al., 2010]), the other diverse set of factors were also found to be significant.

#### Validation of predictive capability

The robustness of our results is established in a number of ways:

![Figure 5.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig5-v2.jpg)

**Figure 5.:** Plate A shows the correlation between the observed incidence and the model-predicted response. We show significant positive correlation, particularly within the trigger periods, between the model predictions and the actual held-out data. This gives us confidence to construct ROC curves for each week. Plates B-D show the ROC curves for the last three weeks of each of the three seasons in the out-of-sample period (potentially, these computations can be repeated for all possible partitions of study weeks into training and test samples). Plates E-G illustrate that the normalized decision variable, which is the normalized response from the model, identifies the South and Southeastern counties as the trigger zones.

### Approach 3: Matching counties and factor combinations

In Approach 3, we investigated combinations of factors presented as ‘treatment’ via a non-parametric, exact-matching analysis of US counties during the weeks of epidemic onset on a season-by-season basis.

First, we collected the list of all counties with a drop in maximum specific humidity during the weeks leading up to an influenza season in a particular year. This is the ‘treated set’: the set of counties that may be thought of as subjected to the positive ‘treatment’ of a drop in specific humidity. We split this set into two, considering counties that also experience increased influenza prevalence during the epidemic onset, and ones that do not (counties with two different values of the outcome variable). The number of counties in these two sets define the first row of a $2\times2$ contingency table. In the second row (the ‘control set’), we focused on counties that do not experience a drop in the maximum specific humidity. However, we only considered counties that have a matching counterpart in the treated set in the following sense: For each county in the control set, we found at least one in the treated set such that the rest of the significant variables (other than specific humidity) had similar variation patterns in both counties. Once we defined the control set, we split it in the manner described for the treated set: We counted the number of control counties that experienced an increased influenza prevalence during epidemic onset, and those which did not. This defined the second row of the contingency table. Finally, we used Fisher’s exact test to compute an odds ratio (the odds of realizing these numbers by chance), along with the test-derived significance of the association between the ‘treatment’ and epidemic wave initiation (p-value). Furthermore, we defined our treatment to consist of multiple factors simultaneously, $e.g.$ specific humidity and its change in the preceding week, along with average temperature and degree of urbanity, see Figure 6.

![Figure 6.](https://cdn.elifesciences.org/articles/30756/elife-30756-fig6-v2.jpg)

**Figure 6.:** Plate A illustrates the factor combinations that turn out to be significant over the nine seasons. Notably, for each season, we have multiple, distinct factor sets that turn out to be significant ($p<0.05$) and yield a greater-than-unity odd ratio. Plotting the probability with which different factors are selected when we look at season-specific county matchings (the top panel in Plate A), we see a corroboration of the conclusions drawn in Approach 2. We find that specific humidity and average temperature, along with their variations, are almost always included. We do see some new factors that fail to be significant in the regression analysis, $e.g.$, degree of urbanity and vaccination coverage. While vaccination coverage is indeed included as a factor in our best performing model, in Approach two it failed to achieve significance, perhaps due to its strong dependence on antigenic variation (see Figure 1J–M). Degree of urbanity is indeed significant for some of the regression models we considered (see Supplementary Information), but was not significant for the model with the smallest DIC. Note that ‘Treatment’ here is defined as a logical combination of weather factors. A treatment is typically a conjunction of several weather variables. For example, the treatment shown in top left panel of Plate B involves a conjunction of: (1) a drop in average temperature during the week of infection; (2) a drop in temperature during the week of infection; (3) a higher-than-average specific humidity; (4) a higher-than-average temperature, and; (5) a high degree of urbanity. With respect to the ‘treatment,’ we can divide counties into three groups: (1) ‘treated counties,’ shown in green; (2) at least one matching county for each of the treated counties (matching counties are very close to the treated counties in all aspects but in treatment, which we called ‘control’ counties), shown in black, and; (3) other counties, shown in grey. The counties in the ‘treatment’ and ‘control’ groups are further subdivided into those counties that initiated an influenza wave and those that have not, resulting in four counts arranged into a two-by-two contingency table. We then used the Fisher exact test to test for association between treatment and influenza onset. Panels in Plate B show both the treated and control sets for the $9$ seasons for a subset of chosen factors. The results are significant, as shown in Tables 2 and 3. The variable definitions are given in Table 4. Notably, some of the variables found significant in the regression analysis are not included above, and some which are not found to be significant in the best regression model show up here. This is not to imply that they are not predictive or lack causal influence. The matched treatment approach, as described above, is not very effective if we use more than $∼10-15$ factors simultaneously to define the treated set (for the amount of data we have); this results in a contingency table populated with zero entries.

Note that geographic clustering of ‘treated’ and ‘untreated’ counties arose automatically as a result of similar weather patterns being imposed via the constraint of multiple climate variables.

**Table 4.**
 Variables in mixed-effect Poisson regression analysis (Approach 2)


<table>
  <thead>
    <tr>
      <th>Variable name</th>
      <th>physical effect</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>N</td>
      <td>Total number of patient visits given week and county (the offset)</td>
    </tr>
    <tr>
      <td>max_HUS_mean</td>
      <td>Mean county-specific maximum specific humidity over nine years</td>
    </tr>
    <tr>
      <td>d_max_HUS_i</td>
      <td>Normalized and zero-centered deviations of maximum humidity, i = 0–4 weeks before</td>
    </tr>
    <tr>
      <td>t_avg_mean</td>
      <td>Mean county-specific temperature over nine years</td>
    </tr>
    <tr>
      <td>d_t_avg_i</td>
      <td>Normalized and zero-centered deviations of mean temperature, i = 0–4 weeks before</td>
    </tr>
    <tr>
      <td>RSDS_mean</td>
      <td>Mean county-specific solar insolation over nine years</td>
    </tr>
    <tr>
      <td>d_RSDS_i</td>
      <td>Normalized and zero-centered deviations of mean solar insolation, i = 0–4 weeks before</td>
    </tr>
    <tr>
      <td>AVG_PRESS mean</td>
      <td>Mean county-specific solar insolation over nine years</td>
    </tr>
    <tr>
      <td>d_AVG_PRESS_i</td>
      <td>Normalized and zero-centered deviations of mean surface pressure, i = 0–4 weeks before</td>
    </tr>
    <tr>
      <td>tot_prec_mean</td>
      <td>Mean county-specific total precipitation over nine years</td>
    </tr>
    <tr>
      <td>d_tot_prec_i</td>
      <td>Normalized and zero-centered deviations of mean total precipitation, i = 0–4 weeks before</td>
    </tr>
    <tr>
      <td>Wind_avg_mean</td>
      <td>Mean county-specific average wind speed over nine years</td>
    </tr>
    <tr>
      <td>d_Wind_avg_i</td>
      <td>Normalized and zero-centered deviations of average wind speed, i = 0–4 weeks before</td>
    </tr>
    <tr>
      <td>Income</td>
      <td>County-specific mean income</td>
    </tr>
    <tr>
      <td>airport_diffusion</td>
      <td>Influence from proximity to airports, modeled as human traffic-weighted exponential diffusion from the 30 largest US airports</td>
    </tr>
    <tr>
      <td>Am_Ind</td>
      <td>% of American Indians in the county</td>
    </tr>
    <tr>
      <td>Asian</td>
      <td>% of Asians</td>
    </tr>
    <tr>
      <td>White_Hisp</td>
      <td>% of Caucasian/Hispanics</td>
    </tr>
    <tr>
      <td>W_non_Hisp</td>
      <td>% of Caucasian/Non-Hispanics</td>
    </tr>
    <tr>
      <td>Black_Hisp</td>
      <td>% of Black/Hispanics</td>
    </tr>
    <tr>
      <td>B_non_Hisp</td>
      <td>% of Black/Non-Hispanics</td>
    </tr>
    <tr>
      <td>Pacific</td>
      <td>% of Pacific Islanders</td>
    </tr>
    <tr>
      <td>Insured</td>
      <td>% of county population insured</td>
    </tr>
    <tr>
      <td>Poor</td>
      <td>% of county population under poverty line</td>
    </tr>
    <tr>
      <td>Urban</td>
      <td>% of county population classified as urban</td>
    </tr>
    <tr>
      <td>land_i</td>
      <td>influenza velocity change in the land neighbors of the county i weeks before the current week</td>
    </tr>
    <tr>
      <td>tweet_i</td>
      <td>influenza velocity change in the Twitter neighbors of the county i weeks before the current week</td>
    </tr>
    <tr>
      <td>air_i</td>
      <td>influenza velocity change in airport neighbors of the county i weeks before the current week</td>
    </tr>
    <tr>
      <td>v_i</td>
      <td>change in rate of infection in the county itself i weeks from the current</td>
    </tr>
    <tr>
      <td>M1</td>
      <td>Diversity in M1 protein primary structure</td>
    </tr>
    <tr>
      <td>M2</td>
      <td>Diversity in M2 protein primary structure</td>
    </tr>
    <tr>
      <td>NA</td>
      <td>Diversity in NA protein primary structure</td>
    </tr>
    <tr>
      <td>HA</td>
      <td>Diversity in HA protein primary structure</td>
    </tr>
    <tr>
      <td>Cum_vac_per_N_i</td>
      <td>vaccination coverage in the county cumulated over past 20 weeks i weeks from the current</td>
    </tr>
  </tbody>
</table>

_(a) Definition of variables_

Unlike the mixed-effect regression approach (Approach 2), this matching analysis is non-parametric, and intended to reveal whether multiple factors are, indeed, simultaneously necessary.

The results of Approach 3’s analysis are presented in Figure 6 and Tables 2 and 3. We found that no single variable was able to consistently yield a statistically significant odds ratio greater than one; multiple factors interacted to shape an epidemic trigger (see Table 3 for a few examples). With a total of $47$ significant variables in our best mixed-effect model, an exhaustive search for all combinations was not feasible. Instead, we performed a standard evolutionary search, looking for combinations that yielded a significant odds ratio for individual seasons. Additionally, we considered all seasons together (by simply adding the contingency tables, element-wise) in order to increase the test’s statistical power.

We isolated ten variables (as shown in Figure 6, Plate B) in this manner which included maximum specific humidity and average temperature along with their variations, the degree of urbanity, antigenic variation, and vaccination coverage.

The factors that appeared most often in our analysis are illustrated in Plate A: It appears that maximum specific humidity and average temperature, along with their variations, and the degree of urbanity have the most frequent contribution, followed by antigenic variation and vaccination coverage.

We did see some new factors here that failed to be of significance in the regression analysis (Approach 2), $e.g.$, degree of urbanity and vaccination coverage. While vaccination coverage was included as a factor in our best performing model in Approach 2, it failed to achieve significance, perhaps due to its strong dependence on antigenic variation (see Figure 1J–M). Degree of urbanity was indeed significant for some of the regression models we considered (see Supplementary Information), but failed to be so for the model with the least DIC.

Thus, Approach three corroborates and strengthens key claims of Approach 2.

The exact set of factors varied somewhat over the seasons; nevertheless, together, they yield significant results when all seasons are considered together. The matching analysis corroborates our results from both the mixed-effect regression and the geographic streamline analyses: The sets of counties initiating the wave are near coasts on the Southern region of the continental US (see Plates A - I in Figure 6).

### Local travel vs. long-distance travel and influenza

Our conclusion that local travel is predominantly responsible for disease wave propagation is supported by several lines of analysis.

First, continuous land-movement infection waves are visible in the weekly influenza rate movie; we computed this movie from insurance claim data and made it available with results of this study.

Second, because our all-weeks-included dataset was too large for the R MCMCglmm package to handle, we performed mixed-effect Poisson regression calculations using a 50 percent random sample of all the weeks for which data were available. In this computation, the airport-proximity, fixed-effect coefficient turned out to be statistically significantly negative (see Supplement A, as well as the editable output file ‘flu-50-percent-weeks.txt’).

Third, the results from our Granger-causality inference showed that:

## Discussion

A summary of the complex relationship between the driving factors that contribute to the trigger and subsequent development of a seasonal epidemic can be clarified with a forest fire metaphor.

The maturation of a forest fire requires the collusion of multiple factors—namely the presence of flammable media, an initiating spark, and a wind current to help spread the fire. Our conceived mapping of this analogy to influenza infection is as follows:

Each of our three types of computational approaches has their strengths and weaknesses: (1) The Poisson mixed-effect regression allows for the direct comparison of the predictive strength of numerous predictor variables and accounts for spatial and temporal autocorrelation, but relies on strong modeling assumptions; (2) The non-parametric Granger analysis is not limited by restrictive modeling assumptions in our implementation, though it focuses only on trends of infection propagation between counties, and; (3) The county-matching analysis is also model-free, but this freedom comes at the expense of lesser statistical power.

### What is new in this study?

The following aspects make our study of influenza triggers new in the influenza literature: (1) Instead of simulating the plausibility of one particular epidemic trigger model with a dynamic disease transmission model, we used formal model selection tools to compare the goodness of fit of hundreds of plausible models; (2) We explicitly attempted to systematically cross-compare the importance of numerous individual factors typically hypothesized to contribute to epidemic onset; (3) To accomplish this, we collected an unprecedented volume of temporal and spatial data on disease dynamics and the dynamics of putative predisposing factors; (4) We used several orthogonal, computational causality-inference techniques (one of which was developed specifically for this study) to probe associations between disease onset and putative epidemic triggers; (5) We tested our best models for their predictive potential and demonstrated that they are, indeed, suitable for forecasting disease waves, and; (6) We combined, for the first time, numerous candidate factors in a single, integrative study.

Convergent conclusions, culled from these radically different techniques, strengthen our claims and make it statistically unlikely that we are observing analysis artifacts. First, the Granger causality analysis results (Approach 1) provide insights into the details of influenza’s epidemiological dynamics. Figure 3G traces out the paths most likely followed by the infection, on average, across the continental US. We note that $∼75%$ of the streamlines sink in counties belonging to the Southern states, which matches up well with the streamline-encoded dynamics of weekly disease incidence over nine years (see Figure 3I). What drives this particular causality field’s geometry? While we cannot definitively answer this question, a comparison of the global patterns emerges from the local mobility data culled from the aforementioned Twitter database and offers a tentative explanation (see Figure 3H). Second, contrary to reported human travel pattern influence on seasonal epidemics (Viboud et al., 2006) (but consistent with [Gog et al., 2014]), we find that short-distance travel contributes more significantly to disease spread (see Figure 4). In particular, we find that long-range air travel is important as an epidemic trigger, but once infection waves are triggered, air travel patterns (or proximity to major airports) become less important. Short-range mobility, on the other hand, is apparently important for sustaining infection transmission over each season. Thus, we find short-range travel to be more important for defining the emergent spatio-temporal geometry of infection waves, while proximity to airports is more important for actually triggering an influenza season; the latter loses positive influence once an infection is under way. This conclusion is justified as follows: (1) When we performed regression calculations using all weeks for which data were available (as opposed to wave initiation weeks only) the airport proximity predictor coefficient turned out to be statistically significantly negative (see Supplement). (2) Results from our Granger-causal inference indicate that, on average, the local, putatively causal connections are far stronger compared to the putatively causal connections between counties within which the major airports are located (see Figure 4C and F). Additionally, from our best mixed-effect regression model (Figure 1A), we find that land connectivity effects are significantly stronger than air connectivity effects. The predictive value of Twitter connectivity, which intuitively captures both local and long-distance travel, lies in-between land and air connectivity coefficients. Note that Twitter connectivity is represented as a directed graph, where for each pair of counties, $i$ and $j$, the $(i,j)$ edge weight represents the conditional probability of ending at county $j$, given that a traveler/Twitter user started her journey in county $i$. Transition probabilities from $i$ to $j$ sum to one over all $j$. Therefore, intuitively, the Twitter connectivity graph should have the features of both a land-connectivity and an air travel graph; which indeed appears to be close to reality. 3) While airport diffusion is a significant factor in our best Poisson model (using data from the initiation period), the causal streamlines (constructed with the complete, all-year incidence data) do not seem to originate from airport-bearing counties.

The role of short-distance travel is particularly crucial in explaining influenza’s time-averaged, geo-spatial prevalence. While the mixed-effect regression analysis explains seasonal initiation in the vicinity of the continental US Southern shores, it might not, by itself, adequately explain its average prevalence patterns across the country.

Also not explained solely by our regression models is the occurrence of relatively high infection prevalence in the central parts of the country. These differences cannot be attributed to long-distance air travel, as discussed before. However, the routes taken by the causality streamlines (as computed by the non-parametric Granger analysis), interpreted as paths followed by an infection on average, suggest an explanation: The close match between the Granger-causal flow and the short-range mobility patterns (derived from Twitter analysis) strongly suggest that average disease prevalence is modulated by short-range mobility.

### Rationale for observational analysis

The traditional empirical approach of testing a causal link between a factor and an outcome of an experiment was to vary one factor at a time, while keeping the other factors (experimental conditions) constant. This ‘all the rest of the conditions are equal’ assumption is often referred to by its Latin form as ceteris paribus. R.A. Fisher ([Fisher, 1935], p. 18) noted that, in real-life experiments, perfect ceteris paribus is not achievable ‘because uncontrollable causes which may influence the results are always … innumerable.’ Fisher’s proposed solution to this problem is to design experiments to involve random assignment of treatment (the putative causal factorâ€™s states) to individual trials and then use regression analysis to estimate the value and significance of the putative causal effect.

Likewise, hypothesis-driven science, wherein investigators formulate a single, testable hypothesis and design specific experiments to test it, is a core element of the scientific method, and works well in most scientific fields. However, a new challenge emerges in data-rich scientific fields, such as genomics, epidemiology, economics, climate modeling, and astronomy: How do we choose the most promising hypotheses among millions of eligible candidates that potentially fit data? One solution to this challenge is the many-hypotheses approach, a method of automated hypothesis generation in which many hypotheses are systematically produced and simultaneously tested against all available data. This approach is currently used, for example, in whole-genome association or genetic linkage studies, and often enables truly unexpected discoveries. In contrast to the single-hypothesis approach, the many-hypotheses approach explicitly accounts for the large universe of possible hypotheses through calibrated statistical tests, effectively reducing the likelihood of accidentally accepting a mediocre hypothesis as a proxy for the truth (Nuzzo, 2014).

The many-hypotheses approach provides a complement to carefully controlled and highly focused wet laboratory experiments. Running controlled experiments to test a single hypothesis necessarily ignores many of the complexities of a real-world phenomenon; these complexities are necessarily present in large, longitudinal datasets. Of course, the data-driven ‘many-hypotheses’ approach is only one aspect of the broader scientific process progressing toward the development of verifiable general theories.

### Agreement and disagreement between methods

Intuitively, we expected that all three approaches would produce similar, if not identical results. In practice, while the three approaches agreed in most cases, this agreement was not perfect. For example, the highlighted areas (greater incidence) in the first influenza season snapshot for Figure 2A–H each should match relatively well to the maps in Figure 6B (or at least some unspecified subset of ‘high incidence treatment counties’). While the county-matching results point to initiation at coasts, in Figure 2, 2006-2007 initiation seems to spread from the West Coast and, in , 2010 has a scattered pattern across the middle of the US.

The intuitive explanation of perceived discrepancy is that the matching method agrees with other analysis types predominantly, but not in all cases. Each analysis has limitations. In the case of the matching analysis, we have less statistical power than in, for example, Poisson regression; matching by numerous parameters reduces the initial set of thousands of counties to a handful of matching ‘treated’ counties (which meet a particular combination of weather and sociodemographic conditions) and ‘untreated’ counties (very similar to ‘treated’ ones in all respects but treatment). The difficult-to-match, ‘weeded out’ counties may happen to be in the coastal areas indicated as the most likely places of influenza wave origin by other analyses.

In the case of the 2007 and 2010 results, the matching analyses pick patterns that are different from those produced by the causality streamline analysis and mixed-effect Poisson regression models.

Figure 6’s Plate B shows the distribution of the treatment counties and matched-non-treatment counties. Note that here, we are not directly predicting initiation, so while the patterns in Figure 2 and Figure 6 should indeed show some similarity, they are not required to match up perfectly. The most similar treated counties do indeed show up in the Southern shores.

### Generalizability

Our analysis uses no prior knowledge specific to influenza epidemiology. As such, these methods are not limited by either the pathogen under consideration (influenza), or the geospatial context (United States). The tools developed here are expected to be equally applicable to analyzing general epidemiological dynamics for pathogens other than influenza, unfolding in arbitrary geographical regions. The specific conclusions we draw about the initiation and propagation of the seasonal influenza in US might not hold true for influenza epidemiology in a different geographical context. However, the analysis tools are still applicable. More broadly, our tools delineate a general approach to modeling complex spatio-temporal dynamics, with applications beyond solely disease epidemiology.

We conclude by highlighting the structure of overlapping conclusions delivered by our three approaches. Approach 1: Granger-causality analysis suggests that an epidemic tends to begin in the South, near water bodies and that short-range, land-based travel is more influential compared to air-travel for infection propagation, providing a map of mean infection flow across the continental US. Approach 2: Poisson regression identifies significant predictive factors, ranks these factors by importance, suggests that Southern shores are where the epidemic begins, and corroborates Approach 1’s result on short-range vs. long-range travel. Approach 3 (county-matching): This approach drills down further to the epidemic onset source to the Southeastern shores of continental US, and identifies a smaller validated subset of predictive factors.

## Materials and methods

The methods and putative predictors identified in our study should be directly applicable to data outside the US. While the balance (relative importance) of putative triggers of influenza waves may vary, the factors themselves should be universal globally, because the virus and host biology are universal.

### Candidate factors in influenza initiation

To investigate county-specific variability, we grouped candidate factors into several categories: demographic, relation to human movement, infection state of county neighbors, and county’s own recent state, and climatic.

Major hypotheses regarding putative causal factors affecting infection dynamics can be traced to a handful of earlier publications:

#### Human movement

We considered two measurements of human movement: (1) The first measurement reflects the proximity of counties to major airports. We computed an exponentially-diffusing influence from counties with major US airports, weighted by passenger enplanements at their respective locations. This accounted for people moving to and from both major airports and neighboring counties, and; (2) The second measurement is a large-scale movement matrix representing people’s week-to-week travels between counties. These data were culled from a complete collection of geo-located Twitter messages, captured over $3.5$ years, and constituted a large-scale, longitudinal sample of individual movements. We used only automatically geo-tagged tweets.

#### Demographic

Influenza is transmitted through direct contact with infected individuals, via contaminated objects, and virus-laden aerosols. Thus, human population density (how many people happen to be around) and social connectivity (how many people interact with each other and how frequently [Bedford et al., 2015]) are factors expected to affect local virus incubation and spread. In addition to population density, we considered socioeconomic factors such as county-mean household income, levels of poverty and urbanity, as well as the prevalence of ethnic and age groups. All these socio-demographic and socio-economic data were derived from reports provided by the US Census ([Web Page]; 2017. Available from: https://www.census.gov/geo/reference/ua/uafacts.html).

#### Return-to-school effect

Social contact among children in schools has been extensively investigated as a determinant of the peak incidence rate. This is one of the few factors that might lend itself to intervention relatively easily, and hence the interest is well-justified. While any reduction in social contact should, in theory, directly impact transmission, quantifying the effect of this specific mode of contact on the incidence rate has been difficult to calculate. Predictions of the reduction in the peak incidence associated with reduced social contact were typically 20–60% (Ferguson et al., 2006; Haber et al., 2007), with some studies predicting much larger reductions of $≧$90% (Mniszewski et al., 2008; Ghosh and Heffernan, 2010). Reductions in the cumulative attack rate (AR, ratio of the number of new cases to the size of the population at risk) were usually smaller than those in the peak incidence. Several studies predicted small ($∼$10%) or no reduction in the cumulative AR (Ferguson et al., 2006; Haber et al., 2007; Yasuda et al., 2005; Ciofi degli Atti et al., 2008; Yasuda et al., 2008; Kelso et al., 2009; Davey et al., 2008; Rizzo et al., 2008; Vynnycky and Edmunds, 2008; Glass and Barnes, 2007; Lee et al., 2010; Yang et al., 2011; Zhang et al., 2012), whilst a few predicted substantial reductions (e.g. $≧$90%) (Glass et al., 2006; Davey et al., 2008; Elveback et al., 1976; Davey and Glass, 2008). Only two studies (Glass et al., 2006; Lee et al., 2010) predicted that peak incidence might increase markedly under certain circumstances following school closures, for example by 27% if school closures caused a doubling in the number of contacts in the household and community, or by 13% if school systems were closed for two weeks at a prevalence of 1% in the general population. Studies have also investigated the effect of such interventions on children vs. adults; one study predicted an overall reduction in the cumulative AR, but an increase of up to 48% in the cumulative AR for adults in some situations (Araz et al., 2012).

While this diverse set of predictions in the literature often pertains to the effect of school closures as an intervention tool, we are more interested in the influence that the current school schedule has, if any, on triggering an epidemic. To answer this specific question, we formulated a simple statistical test to determine whether the timing of return-to-school after summer and winter holidays significantly predicts influenza season initiation. We found insufficient evidence in support of this effect (see Methods and materials).

#### Climate variables

Specific humidity and a drop in temperature have been suggested as the key drivers in triggering seasonal influenza epidemics (Lowen et al., 2008; Shaman et al., 2010). These initial conclusions were drawn from experiments conducted using an animal model (guinea pig), under controlled laboratory conditions (Lowen et al., 2008), followed by indirect support from epidemiological modeling (Shaman et al., 2010).

#### Vaccination coverage

Vaccination is widely regarded as our most promising tool to combat influenza, though antigenic variation between seasons makes it difficult to craft an effective vaccination strategy (Boni, 2008). Understanding how the virus will evolve in the short-term is key to finding the correct antigenic match for an upcoming influenza season. Additionally, short-term molecular evolution might rapidly give rise to immune-escape variants that, if detected, might dictate intra-season updates in vaccine composition. More importantly, vaccination itself might exert significant selection pressure to influence antigenic drift. The effect of vaccination on viral evolution has been documented in an avian H5N2 lineage in vaccinated chickens (Lee et al., 2004), suggesting that similar processes might be occurring in human counterparts. The diversity of the surface proteins at any point in time between seasons suggests that our current vaccination strategies are limited to confer partial immunity, which can result in a highly immune or vaccinated population selectively pressurizing the viral population to evolve more quickly than usual. Given that influenza moves quickly across geographies and that there are multiple, co-circulating strains that may confer partial cross-protection, changing viral service proteins represent a ‘moving target’ for the human immune system. There are additional complexities due to early-life immune imprinting in humans.

#### Accounting for non-vaccination host immunity

Resistance to influenza infection in human hosts arises via two related mechanisms: immunological memory from a previous infection by an identical or sufficiently similar strain, or vaccination against the current strain (or a sufficiently similar strain). In our analysis, we explicitly account for the degree of vaccination coverage. Accounting for host immunity is more difficult, because resistance to infection is not directly observable; however, our analysis also uses the antigenic variation of influenza virus as a proxy to host resistance: If the relative antigenic variation is large, then the susceptibility of non-vaccinated hosts increases, while low antigenic variation increases the probability of encountering a resistant host. In addition, we use the absolute antigenic deviation of the later-season virus from the first-season virus in our data set (winter of 2003–2004) as a predictor, in order to capture longer-term effects of immunological memory. Thus, if the magnitude of the relative drift between two succeeding years is small, we have a likely decrease in susceptibility. Likewise, if the absolute deviation from a few years back starts decreasing, we would also register a decrease in susceptibility. Incorporating these factors in the diverse set of models that we investigate, guarantees that we are indeed considering host susceptibility contributions from a wide range of possible mechanisms.

#### Antigenic Variation

The influenza virus counteracts host immunity via subtle genomic changes over time. The more gradual process, known as antigenic drift, is a manifestation of a gradual accumulation of mutations within viral surface proteins recognized by human antibodies, such as hemagglutinin (HA) and neuraminidase (NA). These mutations are typically introduced during cycles of viral replication (Boni et al., 2004). Most of these mutations are neutral, $i.e.$ they do not affect the functional conformation of the viral proteins. However, some of these alterations do, in fact, sufficiently change secondary and tertiary protein structures to have a negative impact on the binding of host antibodies raised in response to previously circulating strains (Webby and Webster, 2001). (Many such mutations also reduce the virus’s viability.) Thus, while a single infection episode is potentially enough to provide long-term host immunity to the invading strain, antigenic variation due to intense selection pressure gives rise to novel viral strains, making re-infections possible within the span of a few years (Andreasen, 2003). This kind of perpetual Red-Queen arms race injects influenza dynamics with auto-correlative dependencies over multiple seasons. It has been suggested that substantial antigenic drift might be associated with more severe, early-onset influenza epidemics, resulting in increased mortality (Treanor, 2004). In contrast to antigenic drift, antigenic shift is an abrupt, major change in virus structure due to gene segment re-assortment that occurs during simultaneous infection of a single host by multiple influenza subtypes (De Clercq, 2006). Antigenic shift results in new versions of viral surface proteins. Antigenic shift due to re-assortment gives rise to novel influenza subtypes that, if capable of sustained human-to-human transmission, can have devastating consequences for human populations, $e.g.$ the 2009 H1N1 pandemic (Neumann et al., 2009).

In our analysis, we factor in the potential effect of antigenic variation by estimating the surface protein’s population diversity – hemagglutinin (HA), neuraminidase (NA), matrix protein 1 (M1), and matrix protien M2 – as a function of time and geographical sample collection location. Our rationale for our focus on these proteins is that HA, NA, and to some degree M1, are all present on the viral surface (Lamb et al., 1985), contribute to viral assembly, and mediate the release of membrane-enveloped particles (Chlanda et al., 2015). M2 has been shown to have enhanced the pandemic 2009 influenza A virus [(H1N1)pdm09] (Friedman et al., 2017) HA-pseudovirus infectivity (Alvarado-Facundo et al., 2015).

### Data sources

#### Social connectivity

Data was obtained from the General Social Surveys, NORC, See Table 1, [].

#### Clinical data source

The source of the clinical incidence data used in this study is the Truven Health Analytics MarketScan® Commercial Claims and Encounters Database for the years 2003 to 2012 (Hansen, 2017). The database consists of approved commercial health insurance claims for between 17.5 and 45.2 million people annually, with linkage across years, for a total of approximately 150 million individuals. This US national database contains data contributed by over 150 insurance carriers and large, self-insuring companies. We scanned 4.6 billion inpatient and outpatient service claims and identified almost six billion diagnosis codes. After un-duplication, we identified approximately $12.8$ unique diagnostic codes per individual. We processed the Truven database to obtain the reported weekly number of influenza cases over a period of $471$ weeks spanning from January $2003$ to December $2013$, at the spatial resolution of US counties. To define influenza in insurance claims, we used the following set of ICD9 codes: 487.8, 488.12, 488.1, 488.0, 488.01, 488.02, 487.0, 487.1, 488.19, 488.09, 488, 487, and 488.11. We also considered including non-specific codes representing unspecified viral infection (079.99), as suggested in (Viboud et al., 2014), and decided against it. (We provide explicit annotation for each code, as well as rationale for choosing narrower ICD-code definition of ILIs, in the Supplement Section S-D).

A peak percentage of ILI-affected people of $20%$ may seem high–especially given that it is a much greater percentage than the change in seropositivity over most influenza seasons. Note that our apparent estimates of influenza infection rate are unavoidably inflated, because what we are measuring is the week- and county-specific prevalence of influenza-like illnesses among insured patients who contacted their physician for any reason during the week in question. In other words, the denominator that we used for computing prevalence was almost certain to be much smaller than the overall population of the corresponding county.

#### Data on antigenic drift for influenza A

Sequence data for this computation was obtained from the National Institute of Allergy and Infectious Diseases (NIAID) Influenza Research Database (IRD) (Zhang et al., 2017) through their web site at http://www.fludb.org.

#### Data on vaccination coverage

Data on vaccinations was extracted from our EHR database corresponding to the procedural codes 90661 and Q2037, which corresponds to the dominant influenza vaccines. (http://flu.seqirus.com/files/billing_and_coding_guide.pdf)

#### Data on human air travel

We used a complete, directed graph of passenger air travel for 2010, accounting for the number of passengers transported in each direction (The United States Bureau of Transportation Statistics, 2010). For each county, we computed an air neighborhood network: For counties $i$ and $j$, the incoming edge to county $i$ represents the proportion of passengers, and $p_{j⁢i}$ represents the ratio of all passengers who traveled from county $i$ to county $j$ by plane,mto the total number of travelers who left county $i$ by plane during the year, so that $\sum_{j\neqi}p_{j⁢i}=1$.

#### Data on general human travel patterns in the US

Using the complete Twitter dataset, we aggregated a movement matrix to capture people’s week-to-week travels between counties from geo-located Twitter messages (captured during the period of January 1, 2011 through June 30, 2014). This dataset includes approximately $1.7\times10^{9}$ messages and represents $3\times10^{8}$ user-days of location information. A small, but significant, percentage of Twitter messages are automatically tagged with the author’s current latitude/longitude information, as determined by their mobile device. Each latitude/longitude-annotated tweet was mapped to a FIPS county code based on Tiger/Line shape files from the 2013 Census dataset (http://www.census.gov/geo/maps-data/data/tiger-line.html). In addition, we calculated a variant of our movement matrix to capture seasonality and other temporal dynamics: A set of 52 movement matrices captured weekly, county-to-county movements, observed in each week of the year, aggregating each week based on the corresponding observations, from each year from 2011 through 2014.

This dataset constitutes a large-scale, longitudinal sample of individual movements. We found that the movement patterns are consistent with intuitive patterns and prior studies of large-scale movements; the majority of people in a county remain in the same county week-over-week. Most travel between counties occurs between neighboring counties, and between counties and large metropolitan areas, conditioned on distance and size of the metropolitan area. We represent our movement data as an $n\timesn$ matrix $𝐌$ that captures the likelihood that a person observed in county $i$ during the course of a week will be observed in county $j$ in the following week. We calculate the entries $m_{i,j}$ of matrix $𝐌$ as follows:

$$
m_{i,j}=\sumt<T\frac{1}{P⁢o⁢p_{i,t}}⁢\sumu<mx_{u,i,t}⁢x_{u,j,t+1}
$$

For each time interval, we computed the mean movement vector from a given county by summing all county-to-county movement vectors, weighted by the proportion of people moving in each direction.

To investigate the role of proximity to major airports, we modeled influence diffusion as follows: Let $x_{i}$ be the $i^{t⁢h}$ county, and $v_{i}$ be the total contribution obtained by diffusing influences from the major airport bearing counties. Let $x_{k}^{⋆}$ be the $k^{t⁢h}$ airport-bearing county, and let $N$ be the total number of major airport locations considered, in our case, $N=27$. Let $g_{k}$ be the volume of traffic for the $k^{t⁢h}$ major airport location. We then compute $v_{i}$ as follows:

$$
v_{i}=\sumk=1Ng_{k}⁢e^{-C_{0}⁢Θ⁢(x_{k}^{⋆},x_{i})}
$$

where $Θ⁢(⋅,⋅)$ is the distance in miles between two locations, we computed using the Haversine approximation. The value of the constant $C_{0}$ was chosen to be $0.1$. Small variations in the constant do not significantly alter our conclusions. As noted above, proximity to airports had a significant positive influence in sparking seasonal epidemics; the influence is significantly weaker once an outbreak is well under way.

#### Estimating antigenic diversity

In this study, we measured antigenic diversity as follows: Let $S_{i,x,t}$ be the set of amino acid sequences for the $i^{t⁢h}$ protein (one of HA, NA, M1, or M2), collected in year $t$ ($t$ ranging between 2003 and 2011), in state $x$ of the continental US. The temporal resolution of the sequence data is thus set to years instead of weeks, and the spatial resolution to states instead of counties. These resolutions are coarse compared to our EHR data on infection incidences, and is set in this manner to maintain sufficient statistical power. For each such set of amino acid sequences $S_{i,x,t}$, we compute the set $D⁢(S_{i,x,t})$ of pairwise edit distances:

$$
D(S_{i,x,t})={y:y=ℒ(s_{1},s_{2}),s_{1},s_{2}\inS_{i,x,t},s_{1}\neqs_{2}}
$$

where $ℒ⁢(s_{1},s_{2})$ is the standard edit distance (also known as the Levenshtein distance) between the sequences $s_{1},s_{2}$. Mathematically, the Levenshtein distance between two strings $a,b$ (of length $|a|,|b|$ respectively) is given by:

$$
ℒ⁢(a,b)=lev_{a,b}⁡(|a|,|b|),where 
$$



$$
lev_{a,b}⁡(i,j)={max⁡(i,j)if⁢min⁡(i,j)=0,min⁡{lev_{a,b}⁡(i-1,j)+1lev_{a,b}⁡(i,j-1)+1lev_{a,b}⁡(i-1,j-1)+1_{(a_{i}\neqb_{j})}otherwise.
$$

where $1_{(a_{i}\neqb_{j})}$ is the indicator function equal to 0 when $a_{i}=b_{j}$ and equal to one otherwise, and $lev_{a,b}⁡(i,j)$ is the distance between the first $i$ characters of $a$ and the first $j$ characters of $b$.

The antigenic diversity of the $i^{t⁢h}$ protein at time $t$ in state $x$ was then defined as the median of the distribution of the values in the set $D⁢(S_{i,x,t})$. Clearly, as the sequences became more diverse at a point in time and space due to molecular variations brought about by either drifts or shifts, the measure deviated more from zero. Use of the median provided robustness to outliers.

Importantly, here we did not compare temporal changes in viral antigenic makeup directly, but estimated the time-specific diversity in the viral protein primary structure. We expected our diversity measure to be representative of the cumulative changes that occurred within each of the nine influenza seasons.

#### Estimating vaccination coverage

We incorporated the effect of vaccination coverage by estimating the cumulative fraction of the population that received the current influenza vaccine within the previous 20 week period. This approach to estimating vaccination coverage does not correct for season-specific antigenic match, or the lack thereof. Nevertheless, because we explicitly included measures of antigenic diversity in addition to vaccination coverage, we expected that effects arising from the degree of antigenic match would indeed be factored in; if there is a significant mismatch, we expected the antigenic diversity in that year to be less and vice verse. This assumes implicitly that vaccination does indeed play a major role in exerting significant selection pressure, the assumption that was reinforced by our observation of a strong dependency between vaccination coverage and normalized antigenic diversity.

We found that antigenic diversity is quite strongly affected by vaccination coverage. This reflects the theoretical predictions in Boni et al. (Boni et al., 2006), where it is shown that the amount of observed antigenic drift increases as immunity in the host population increases and pressures the virus population to evolve.

#### Estimating the effect of return-to-school days

The absence of consensus, and the diversity of modeling assumptions pertaining to this effect (described above) makes it difficult to validate conclusions in large scale epidemiological data. We carried out a simple test to determine whether there is statistical evidence that after-holiday, return-to-school periods in August-September and in January predict or trigger the seasonal epidemic.

For this test, we assumed a broad window to cover all such school openings across the continental US including the last week in August, the entire month of September, two weeks in October, and two weeks in January. We next carried out a Fisher’s exact test to determine whether the overlap between these weeks and the identified ‘trigger period’ (See Table LABEL:SI-tabschool) for the seasonal epidemic are sufficiently non-random.

#### Weather data

The dataset starts with the week beginning December 31 st, 2002 and includes 522 weeks (which ends exactly on the week ending December 31 st, 2012). Temperature and precipitation data come from the 2.5 arcminute (approximately 4 km) PRISM (Oregon State University, 2014) dataset and other variables (wind speed, specific humidity, surface pressure, downward incident, and shortwave solar radiation) come from the 7.5 arcminute (approximately 12 km) Phase 2 North American Land Data Assimilation System (NLDAS-2) dataset (Mitchell, 2004; Cosgrove et al., 2003). These datasets were selected in large part due to the fact that both are updated in near real-time, making it possible to use these datasets for future monitoring applications. PRISM is released daily, with an approximately 13 hr delay (data for the previous day is released at 1pm EST each day) while NLDAS is released daily, with an approximately 2.5 day delay).

Variables were aggregated to county boundaries based on shapefiles from the GADM database of Global Administrative Areas (Areas, 2014). Where appropriate, we considered both the average daily climate variable (for example, the daily maximum temperature averaged over the week) as well as the the maximum and/or minimum of the variable experienced over the week. For precipitation, we considered only the cumulative total precipitation experienced during the week.

### Three approaches

#### Approach 1: Non-parametric Ganger analysis of county-specific incidence

##### Analysis of quantized clinical data

For the causality analysis, we started with an integer-valued time series for each US county, and to carry out the causality analysis, we first quantized the series in two steps:

This mapped each data series to a symbol stream over a binary alphabet. The binary quantization is not a restriction imposed by the inference algorithm; while we do require quantized magnitudes, longer data streams can be encoded with finer alphabets to accommodate an arbitrary precision. For this specific dataset, the relatively short length of the county-specific time-series necessitated a coarse quantization in order for the results to have a meaningful statistical significance.

Given a pair of such quantized streams $s_{a},s_{b}$, the algorithm described in the Supplement computes two coefficients of causality, one for each direction. Intuitively, the coefficient $\gamma_{b}^{a}$ from $s_{a}$ to $s_{b}$ is a non-dimensional number between $0$ and $1$ that quantifies the amount of information that one may acquire about the second stream $s_{b}$ from observing the first stream ($s_{a}$). More specifically, $\gamma_{b}^{a}$ is the average reduction in the uncertainty of the next predicted symbol in stream $s_{b}$ in bits, per bit, acquired from observed symbols in stream $s_{a}$. It can be shown that the coefficient of causality $\gamma_{b}^{a}$ is $0$ if and only if there is no causal influence from $s_{a}$ to $s_{b}$ in the sense of Granger, and assumes the maximum value $1$ if and only if $s_{b}$ is deterministically predictable from $s_{a}$. Moreover, $\gamma_{b}^{a}=\gamma_{a}^{b}=0$ if and only if $s_{a}$ and $s_{b}$ are statistically independent processes (Chattopadhyay, 2014). It is trivial to produce examples where we would have $\gamma_{b}^{a}=0,\gamma_{a}^{b}>0$ illustrating the ability of the algorithm to capture the asymmetric flow of causal influence in one preferred direction and not the other.

Additionally, whenever we computed the causality coefficient, it was always associated with a time delay: We calculated the coefficient for predicting the target stream some specified number of steps in the future, and the computed coefficient was thus parameterized by this delay. In our analysis, we computed coefficients up to a maximum delay of $10$ weeks, and, for each pair of counties, selected the optimum delay which gave rise to the largest coefficient. For more details on the algorithm, see the Supplement.

##### Computation of causality fields and causality streamlines

To analyze the propagation dynamics of disease, we defined the notion of a Granger causal flow between two counties. Treating county-specific changes in disease prevalence as a time-stamped data stream, we quantified the directional strength of the causal flow between two counties as the degree of predictability of one stream’s future, given the history of the other (see Figure 3A–D). Our new algorithm was able to compute a coefficient of causality: an information-theoretic measure of the information in bits that one stream communicates about another in a direction-specific manner. A strong coefficient of this type suggests that either the disease itself, or an underlying cause, may be propagating from the former county to the latter.

To explore the country-wide propagation dynamics, we stitched together the properly-aligned, adjacent between-county causal flow vectors across the whole US map into causality streamlines, representing the average of multiple spatial infection propagation waves over time. To compute causality streamlines, we needed a precise notion of county neighbors. We considered two counties to be neighbors if either they shared a common border, or if one county was reachable within a line-of-sight distance of 50 miles from any point within another. The latter condition removed ambiguities as to whether counties touching at a point should be still considered as neighbors. The exact distance value (50 miles) does not significantly change our results, as long as it does not vary significantly. With the definition of the neighborhood map in place, we proceeded to compute the direction-specific coefficients of causality between neighboring counties. It follows that we would obtain a set of coefficients for each county and one for each of its neighbors, capturing the degree of causal influence from a given particular county to its respective neighbors. Our algorithm also computed the probability of each coefficient arising by chance alone, and we ignored coefficients that have more than a $6%$ probability that two independent processes lacking any causal connection gave rise to the particular computed value of the coefficient. Once the coefficients had been calculated for each neighbor, we computed the resultant direction of causal influence outflow from that particular county. This was carried out by visualizing the causality coefficients as weights on the length of the vectors, from the centroid of the considered county to the centroids of its neighbors. We then calculated the resultant vector (see Figure 3). Viewed systematically across the continental US, these local vectors formed a discernible pattern; we observed the emergence of a non-random structure with clearly discernible paths outlining the ‘causality field’ (see Figure 3, Plates G, J, K). To interpret the plots, note that streamlines start at their thinnest part, their direction is indicted with thickening line; typically multiple streamlines coalesce into a river-like pattern.

##### Inferring statistical ‘Granger-causality’ from data

Granger attempted to obtain a precise definition of causal influence (Granger, 1980) from the following intuitive notion: $Y$ is a cause of $X$, if it has unique information that alters the probabilistic estimate of the immediate future of $X$.

Here, we used a new, non-parametric approach to Granger causal inference (Chattopadhyay, 2014) (Approach 1). In contrast to state-of-the-art binary tests (Baek and Brock, 1992; Hiemstra and Jones, 1994), we computed the degree of causal dependence between quantized data streams from stationary ergodic sources in a non-parametric, non-linear setting.

Our approach was significantly more general to common, regression-based implementations of Granger causal inference, and did not involve any autoregressive moving average (ARMA) modeling. All such commonly used techniques impose an a priori linear structure on the data, which then constrains the class of dependency structures we can hope to distill.

True causality, in a Humean sense, cannot be inferred (Hume, 1993; Kant, 1998). Among other reported approaches to ascertaining causal dependency relationships, the work of J. Pearl (Pearl, 2009a) is perhaps most visible, and builds on the paradigm of structural causal models (SCM) (Pearl, 2009b). While Pearl’s work is often claimed to be able to answer causal queries regarding the effects of potential interventions, as well as regarding counterfactuals, our objective in this paper is somewhat different. We are interested in delineating whether infection transmission pathways can be distilled from the patterns of infection’s spatio-temporal incidence.

#### Approach 2: Poisson regression on putative factors

In Approach 2, we investigated the relative importance of putative factors as follows: Specifically, let $N_{i⁢j⁢k}$ denote the total number of patients in county $i$, who are of age $j$, and gender $k$. Denoting the number of individuals diagnosed with influenza in a given county during given week as $y_{i⁢j⁢k}$, we modeled the within-county disease incidence counts for every county (for which data was available) in the US using the following mixed-effect Poisson regression model:

$$
P(y_{i⁢j⁢k}|\lambda_{i,j,k})=\frac{\lambda_{i⁢j⁢k}^{y_{i⁢j⁢k}}⁢e^{-\lambda_{i⁢j⁢k}}}{y_{i⁢j⁢k}!}
$$



$$
with \lambda_{ijk}=N_{ijk}exp⁡{\alpha+Xb+s_{i}b_{1,i}+n_{i}b_{2,i}+Zv},
$$

where, $\alpha$ is the intercept, $𝐗$ and $𝐛$ are a fixed-effect design matrix and a vector of fixed effects, respectively, $𝐬_{i}$ is $1\timesm$ vector of changes in rate of infection in the $i^{t⁢h}$ county $1,2,..,m$ weeks prior to the current, $𝐛_{1,i}$ is a $m\times1$ vector of auto-correlation fixed effects, $𝐧_{i}$ is a $1\times(3⁢m)$ vector of changes in the rate of infection in the neighbors of the $i^{t⁢h}$ county $1,2,..,m$ weeks prior to the current (the neighbors are subdivided into land neighbors, Twitter neighbors, and air neighbors), $𝐛_{2,i}$ is a $(3⁢m)\times1$ vector of county-neighborhoods fixed effects, and $𝐯$ and $𝐙$ are random effects and their design matrix, respectively. Variable $m$ represents the depth of ‘memory’ of auto-regression in weeks, in our case $m=4$.

In this way, the total number of rows in matrix $𝐗$ is $510\times3,143$ (weeks $\times$ counties), with county-specific socioeconomic covariates and week-specific weather covariates. For disease initiation analysis, we included only a subset of time series covering approximately $50$ weeks.

We did not use an explicit spatial smoothing. The county-level random effects were used to account for possible heterogeneity in disease reporting across counties. However, as predictors, we used average infection rate values of immediate neighbors for the county (one, two, three, and four weeks in the past). This prediction structure afforded an implicit spatial smoothing, dampening spurious fluctuations in infection rates.

##### Out-of-sample prediction and ROC analysis with mixed-effect poisson regression

We carried our out-of-sample prediction with the models inferred with mixed-effect regression. The steps were as follows:

As expected, the predicted incidence does not exactly match the observed out-of-sample data. Nevertheless, we see positive correlation (Figure 5, Plate A). Because we were modeling a necessarily spatio-temporal stochastic process, the predictive ability of the model is difficult to judge simply from the observed positive correlation. To resolve this, we investigated the performance of our model by computing how well it predicted the counties that experience flare-ups during the trigger-periods in the out-of-sample data. This exercise is reduced to a classification problem, by first choosing a threshold on the number of reported cases per week to define what is meant by a ‘flare-up’ (see description below). To quantify the prediction performance, we constructed ROC curves for each of the three target seasons, for each fixed week, as follows:

#### Variable and model selection

Approaches 2 and 3 have different limitations; these affect which approach is most effective at which statistical detection task.

Approach 2 (mixed-effect regression analysis) can use a whole dataset for model selection, that can span individual predictors, their combinations, and even interactions between factors (see Table 5; Figure 1—figure supplement 2; Figure 1—figure supplement 3; Figure 1—figure supplement 4; Source data 2; Source data 3; Supplementray file 3; Source code 1). Model selection allows us to choose a model with the right balance of complexity and explanatory power, thus enabling this analysis to detect collinear explanatory variables and drop the weaker predictors that increase model complexity but do not add explanatory power.

**Table 5.**
 Different Models Considered and DIC Ranking


<table>
  <thead>
    <tr>
      <th>Equation used in Poisson regression</th>
      <th>DIC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + max_HUS_mean * t_avg_mean + d_max_HUS_0 * d_t_avg_0 + d_max_HUS_min_1 * d_t_avg_min_1 + d_max_HUS_min_2 * d_t_avg_min_2 + d_max_HUS_min_3 * d_t_avg_min_3 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4+air1+air2+air3+air4+HA + M1+M2+NA.</td>
      <td>185942</td>
    </tr>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + d_max_HUS_min_4 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + d_t_avg_min_4 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + d_RSDS_min_4 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + d_AVG_PRESS_min_4 + tot_prec_mean + d_tot_prec_0 + d_tot_prec_min_1 + d_tot_prec_min_2 + d_tot_prec_min_3 + d_tot_prec_min_4 + Wind_avg_mean + d_Wind_avg_0 + d_Wind_avg_min_1 + d_Wind_avg_min_2 + d_Wind_avg_min_3 + d_Wind_avg_min_4 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4+air1+air2+air3+air4+HA + M1+M2+NA.+HA * NA.</td>
      <td>185940.6</td>
    </tr>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + max_HUS_mean * t_avg_mean + d_max_HUS_0 * d_t_avg_0 + d_max_HUS_min_1 * d_t_avg_min_1 + d_max_HUS_min_2 * d_t_avg_min_2 + d_max_HUS_min_3 * d_t_avg_min_3 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4air1+air2+air3+air4+HA + M1+M2+NA.+Cum_vac_per_N_0</td>
      <td>185938.1</td>
    </tr>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + d_max_HUS_min_4 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + d_t_avg_min_4 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + d_RSDS_min_4 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + d_AVG_PRESS_min_4 + tot_prec_mean + d_tot_prec_0 + d_tot_prec_min_1 + d_tot_prec_min_2 + d_tot_prec_min_3 + d_tot_prec_min_4 + Wind_avg_mean + d_Wind_avg_0 + d_Wind_avg_min_1 + d_Wind_avg_min_2 + d_Wind_avg_min_3 + d_Wind_avg_min_4 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4+air1+air2+air3+air4+HA + M1+M2+NA.+Cum_vac_per_N_diff_1 + Cum_vac_per_N_diff_2 + Cum_vac_per_N_diff_3 + Cum_vac_per_N_diff_4</td>
      <td>185935.9</td>
    </tr>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + d_max_HUS_min_4 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + d_t_avg_min_4 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + d_RSDS_min_4 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + d_AVG_PRESS_min_4 + tot_prec_mean + d_tot_prec_0 + d_tot_prec_min_1 + d_tot_prec_min_2 + d_tot_prec_min_3 + d_tot_prec_min_4 + Wind_avg_mean + d_Wind_avg_0 + d_Wind_avg_min_1 + d_Wind_avg_min_2 + d_Wind_avg_min_3 + d_Wind_avg_min_4 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4+air1+air2+air3+air4+HA + M1+M2+NA.</td>
      <td>185933.7</td>
    </tr>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + d_max_HUS_min_4 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + d_t_avg_min_4 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + d_RSDS_min_4 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + d_AVG_PRESS_min_4 + tot_prec_mean + d_tot_prec_0 + d_tot_prec_min_1 + d_tot_prec_min_2 + d_tot_prec_min_3 + d_tot_prec_min_4 + Wind_avg_mean + d_Wind_avg_0 + d_Wind_avg_min_1 + d_Wind_avg_min_2 + d_Wind_avg_min_3 + d_Wind_avg_min_4 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4+air1+air2+air3+air4+HA + M1+M2+NA.+Cum_vac_per_N_0</td>
      <td>185932.3</td>
    </tr>
    <tr>
      <td>flu ∼LOGN + 1 + max_HUS_mean + d_max_HUS_0 + d_max_HUS_min_1 + d_max_HUS_min_2 + d_max_HUS_min_3 + d_max_HUS_min_4 + t_avg_mean + d_t_avg_0 + d_t_avg_min_1 + d_t_avg_min_2 + d_t_avg_min_3 + d_t_avg_min_4 + RSDS_mean + d_RSDS_0 + d_RSDS_min_1 + d_RSDS_min_2 + d_RSDS_min_3 + d_RSDS_min_4 + AVG_PRESS_mean + d_AVG_PRESS_0 + d_AVG_PRESS_min_1 + d_AVG_PRESS_min_2 + d_AVG_PRESS_min_3 + d_AVG_PRESS_min_4 + tot_prec_mean + d_tot_prec_0 + d_tot_prec_min_1 + d_tot_prec_min_2 + d_tot_prec_min_3 + d_tot_prec_min_4 + Wind_avg_mean + d_Wind_avg_0 + d_Wind_avg_min_1 + d_Wind_avg_min_2 + d_Wind_avg_min_3 + d_Wind_avg_min_4 + Income + airport_diffusion + Am_Ind + Asian + White_Hisp + W_non_Hisp + Black_Hisp + B_non_Hisp + Pacific + Insured+Poor + Urban+v1+v2+land1+land2+land3+land4+tweet1+tweet2+tweet3+tweet4+air1+air2+air3+air4+HA + M1+M2+NA.+Cum_vac_per_N_0 + Cum_vac_per_N_1 + Cum_vac_per_N_2 + Cum_vac_per_N_3</td>
      <td>185926.6</td>
    </tr>
  </tbody>
</table>

For example, the best model in our mixed-effect regression model series, with deviance information criterion (DIC) $185,926.6$ (see Table 5, the last model), includes a term d_max_HUS_min_3 * d_t_avg_min_3 that denotes an interaction between the weekly change in the maximum specific humidity and the weekly change in the average temperature, both of which are weather parameter changes recorded three weeks before the current week. Because it does not split datasets, Approach two is more powerful at detecting interactions between explanatory variables and rather complicated models. However, this approach is more susceptible to bias (picking non-causal correlations that are inherent in the raw data), if the data are unbalanced, unlike with Approach 3.

We added and removed random effects to the model structure, taking out and adding fixed effects, executing the regression algorithm, and plotting the DIC achieved against model complexity. Here, model complexity is simply proxied by the descriptional complexity in terms of how large the model was (the number of factors in the regression equation). We stopped when the drop in DIC stabilized (See Figure 1—figure supplement 3 ). Notably, the DIC has been shown to select overfits (Ando, 2011; Plummer, 2008; van der Linde, 2012), and does not properly account for model complexity in practice. Our driving idea was the identification of the Pareto front that trades off accuracy (in terms of DIC) with model complexity in a transparent manner. This is, of course, a ‘greedy approach,’ in the sense that we do not guarantee that we have indeed found the ‘best’ possible model. However, because our cross-validation (Figure 5) yielded good results, we deemed the stopping rule to be satisfactory.

#### Approach 3: County-matching effect analysis

We designed Approach three specifically to balance biased observational data. While Approach three does not allow for explicit model selection, it is good at detecting simpler combinations of predictors putatively ‘causally’ affecting the outcome variable. However, because this approach involves splitting data into smaller and smaller subsets, as the complexity of predictor function (‘treatment’) grows, it quickly runs out of statistical power.

These two approaches’ properties explain the perceived misalignment of results from the two streams of analysis. For an intuitive understanding of matching approaches, consider specific humidity’s effect on influenza prevalence. The county-matching method’s goal is to deduce associations putatively interpreted as causality relations. For example, consider testing the question of whether counties with higher-than-average mean maximum specific humidity do, indeed, have higher influenza prevalence, in a statistically significant sense, when compared to counties that do not, provided all other factors are held constant.

Let $𝕐$ denote the set of all US counties, and let $𝕊$ be the set of all factors we find to be significant in our mixed-effect regression analysis. Now, for any subset of factors $K⫅𝕊$, we denote the complement set as $K¯=𝕊∖K$. Additionally, we define the Boolean function $𝒯:𝕊\times𝕐→{t⁢r⁢u⁢e,f⁢a⁢l⁢s⁢e}$, (the treatment function) where for some factors $s\in𝕊$, and some counties $y\in𝕐$, the Boolean value $𝒯⁢(s,y)$ is true if the signal or treatment corresponding to the factor $s$ is present in county $y$. We used the sign for the coefficients we obtained in our best mixed-effect regression model to determine what counts as a positive signal. For example, because maximum specific humidity (denoted by the variable $m⁢a⁢x⁢_⁢h⁢u⁢s⁢_⁢a⁢v⁢g$) enters with a positive coefficient, if county $y$ experiences a higher-than-average maximum specific humidity, then $𝒯⁢(m⁢a⁢x⁢_⁢h⁢u⁢s⁢_⁢a⁢v⁢g,y)$ is true.

To simplify the notation, we used $𝒯_{y}^{s}$ to denote a true signal, and $¬⁢𝒯_{y}^{s}$ to denote a false one.

Finally, for any $K⫅𝕊$, we define the following three sets, which we refer to as the $W$-sets:

$$
W_{t⁢r⁢e⁢a⁢t⁢e⁢d}^{K}={y\in𝕐:⋀k\inK𝒯_{y}^{k}}
$$



$$
W_{m⁢a⁢t⁢c⁢h⁢e⁢d-c⁢o⁢n⁢t⁢r⁢o⁢l}^{K}=
$$



$$
{y\in𝕐:(¬⋀k\inK𝒯_{y}^{k})⋀(∃y^{′}\inW_{t⁢r⁢u⁢e}^{K}(∀r\inK¯((𝒯_{y^{′}}^{r}∧𝒯_{y}^{r})∨(¬𝒯_{y^{′}}^{r}∧¬𝒯_{y}^{r}))))}
$$



$$
W_{other}^{K}={y\inY:(¬⋀k\inK𝒯_{y}^{k})}∖W_{matched−control}^{K}
$$

Clearly, $W_{t⁢r⁢e⁢a⁢t⁢e⁢d}^{K}$ is the treated set, that is, the set of counties which exhibit the signal encoded by the set $K$ is then the matched control set of counties, which lack the signal, but each county in this set has a matching counterpart in $W_{t⁢r⁢e⁢a⁢t⁢e⁢d}^{K}$.

The $W$-sets allow us to set up a $2\times2$ contingency table for any chosen subset of factors $K⫅𝕊$ as described before. Specifically, we split the sets $W_{t⁢r⁢e⁢a⁢t⁢e⁢d}^{K}$ and $W_{m⁢a⁢t⁢c⁢h⁢e⁢d-c⁢o⁢n⁢t⁢r⁢o⁢l}^{K}$ into two subsets each, representing those counties which experience a spike in influenza prevalence and which do not. The $2\times2$ contingency table is then subjected to Fisher’s exact test.
