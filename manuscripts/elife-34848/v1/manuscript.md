# Using paired serology and surveillance data to quantify dengue transmission and control during a large outbreak in Fiji

## Authors

- Adam J Kucharski<sup>1</sup> ([ORCID: 0000-0001-8814-9421](https://orcid.org/0000-0001-8814-9421)) †
- Mike Kama<sup>3</sup>
- Conall H Watson<sup>1</sup>
- Maite Aubry<sup>5</sup>
- Sebastian Funk<sup>1</sup> ([ORCID: 0000-0002-2842-3406](https://orcid.org/0000-0002-2842-3406))
- Alasdair D Henderson<sup>1</sup>
- Oliver J Brady<sup>1</sup>
- Jessica Vanhomwegen<sup>6</sup>
- Jean-Claude Manuguerra<sup>6</sup> ([ORCID: 0000-0002-5202-6531](https://orcid.org/0000-0002-5202-6531))
- Colleen L Lau<sup>7</sup>
- W John Edmunds<sup>1</sup>
- John Aaskov<sup>8</sup>
- Eric James Nilles<sup>9</sup> ([ORCID: 0000-0001-7044-5257](https://orcid.org/0000-0001-7044-5257))
- Van-Mai Cao-Lormeau<sup>5</sup>
- Stéphane Hué<sup>1</sup>
- Martin L Hibberd<sup>10</sup>

### Affiliations

1. Centre for the Mathematical Modelling of Infectious Diseases London School of Hygiene and Tropical Medicine London United Kingdom
2. Department of Infectious Disease Epidemiology London School of Hygiene and Tropical Medicine London United Kingdom
3. National Centre for Communicable Disease Control Suva Fiji
4. University of the South Pacific Suva Fiji
5. Unit of Emerging Infectious Diseases Institut Louis Malardé Tahiti French Polynesia
6. Institut Pasteur Paris France
7. Research School of Population Health Australian National University Canberra Australia
8. Queensland University of Technology Brisbane Australia
9. World Health Organization Division of Pacific Technical Support Suva Fiji
10. Department of Pathogen Molecular Biology London School of Hygiene and Tropical Medicine London United Kingdom

† Corresponding author

## Abstract

Dengue is a major health burden, but it can be challenging to examine transmission and evaluate control measures because outbreaks depend on multiple factors, including human population structure, prior immunity and climate. We combined population-representative paired sera collected before and after the 2013/14 dengue-3 outbreak in Fiji with surveillance data to determine how such factors influence transmission and control in island settings. Our results suggested the 10–19 year-old age group had the highest risk of infection, but we did not find strong evidence that other demographic or environmental risk factors were linked to seroconversion. A mathematical model jointly fitted to surveillance and serological data suggested that herd immunity and seasonally varying transmission could not explain observed dynamics. However, the model showed evidence of an additional reduction in transmission coinciding with a vector clean-up campaign, which may have contributed to the decline in cases in the later stages of the outbreak.

## Introduction

In recent years, the reported incidence of dengue has risen rapidly. In the Asia-Pacific region, which bears 75% of the global dengue disease burden, there are more than 1.8 billion people at risk of infection with dengue viruses (DENV) (World Health Organization, 2009). Increased air travel and urbanisation could have contributed to the geographic spread of infection (Gubler, 1998; Simmons et al., 2012), with transmission by mosquitoes of the Aedes genus, including Aedes aegypti and Aedes albopictus (Halstead, 2007). DENV has four serotypes circulating, with infection conferring lifelong protection against the infecting serotype and short-lived protection against the others (Sabin, 1952; Guzmán and Kourí, 2002). Although four serotypes of DENV may co-circulate in South East Asia, only one serotype circulates in most of the South Pacific islands at any point in time (Cao-Lormeau et al., 2014; Li et al., 2010).

Between November 2013 and July 2014, a major outbreak caused by DENV-3 occurred in Fiji, with more than 25,000 suspected cases reported (Figure 1A). Prior to the 2013/14 outbreak, there were eleven outbreaks of dengue recorded in Fiji, involving serotypes 1, 2 and 4 (Table 1). Most cases in 2013/14 occurred on Viti Levu, the largest and most populous island. This is administratively divided into the Central Division, which includes the port-capital Suva, and Western Division, which contains the urban centres of Lautoka and Nadi, where Fiji’s major international airport is located. Dengue transmission in Central and Western Divisions is likely to be driven mostly by the Aedes aegypti vector, with Aedes albopictus most abundant in the Northern Division. Aedes polynesiensis and Aedes pseudoscutellaris are also present in all divisions (Maguire et al., 1971; Prakash et al., 2001). In response to the 2013/14 outbreak, considerable resources were dedicated to implementing control measures, including a nationwide vector clean-up campaign between 8th and 22nd March 2014 (Break Dengue, 2014). As well as media coverage and distribution of flyers to raise awareness about dengue prevention and protection, a major operation was put in place to remove rubbish that could act as egg laying habitats for mosquitoes. In total, forty-five tonnes of tyres and twenty-five tonnes of other containers were removed during this period.

![Figure 1.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig1-v1.jpg)

**Figure 1.:** Points on the maps show locations of cases arranged by health centre they reported to; these are plotted with jitter and transparency to show concentrations of cases. (A) Weekly reported case totals for Northern, Western, Central and Eastern divisions. (B) Serosurvey study locations. Black circles show the 23 study clusters included in the analysis. (C) Age distribution of Central Division in the 2007 census (blue line) and ages of serosurvey participants in 2013 (black line).

**Table 1.**
 Reported dengue outbreaks in Fiji between 1930–2014.Two studies (Fagbami et al., 1995; Maguire et al., 1974) also included a post-outbreak serosurvey in Central Division. *There is also evidence of DENV-3 circulation during this period (Singh et al., 2005).


<table>
  <thead>
    <tr>
      <th>Year</th>
      <th>Main serotype</th>
      <th>Reported cases</th>
      <th>Seroprevalence</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1930</td>
      <td>?</td>
      <td>Thousands</td>
      <td></td>
      <td>(Maguire et al., 1971)</td>
    </tr>
    <tr>
      <td>1944-5</td>
      <td>1</td>
      <td>Thousands</td>
      <td></td>
      <td>(Reed et al., 1977)</td>
    </tr>
    <tr>
      <td>1971-3</td>
      <td>2</td>
      <td>3413</td>
      <td>26% (Suva)</td>
      <td>(Maguire et al., 1974)</td>
    </tr>
    <tr>
      <td>1974-5</td>
      <td>1</td>
      <td>16,203</td>
      <td></td>
      <td>(Reed et al., 1977)</td>
    </tr>
    <tr>
      <td>1980</td>
      <td>4</td>
      <td>127</td>
      <td></td>
      <td>(Fagbami et al., 1995)</td>
    </tr>
    <tr>
      <td>1981</td>
      <td>1</td>
      <td>18</td>
      <td></td>
      <td>(Kiedrzynski et al., 1998)</td>
    </tr>
    <tr>
      <td>1982</td>
      <td>2</td>
      <td>676</td>
      <td></td>
      <td>(Kiedrzynski et al., 1998)</td>
    </tr>
    <tr>
      <td>1984-6</td>
      <td>?</td>
      <td>490</td>
      <td></td>
      <td>(Fagbami et al., 1995)</td>
    </tr>
    <tr>
      <td>1988</td>
      <td>?</td>
      <td>22</td>
      <td></td>
      <td>(Fagbami et al., 1995)</td>
    </tr>
    <tr>
      <td>1989-90</td>
      <td>1*</td>
      <td>3686</td>
      <td>54% (Suva)</td>
      <td>(Fagbami et al., 1995; Waterman et al., 1993)</td>
    </tr>
    <tr>
      <td>1997-8</td>
      <td>2</td>
      <td>24,780</td>
      <td></td>
      <td>(World Health Organization, 2000)</td>
    </tr>
    <tr>
      <td>2001-3</td>
      <td>1</td>
      <td>?</td>
      <td></td>
      <td>(Halstead, 2008)</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>4</td>
      <td>1306</td>
      <td></td>
      <td>(PacNet Report, 2008; ProMED-mail, 2008)</td>
    </tr>
    <tr>
      <td>2013-14</td>
      <td>3</td>
      <td>25,496</td>
      <td></td>
      <td>Fiji MOH</td>
    </tr>
  </tbody>
</table>

Large dengue outbreaks can place a substantial public health burden on island populations (Fagbami et al., 1995; Sharp et al., 2014). However, understanding the dynamics of infection and evaluating the impact of vector control measures remains challenging. There is a limited evidence base for control measures even in controlled trials (Bowman et al., 2016; Heintze et al., 2007), and post-outbreak evaluation is hindered by the fact that the size and duration of major outbreaks can be influenced by several factors, including population immunity, human movement, seasonal variation in transmission, and proportion of people living in urban, peri-urban and rural communities. In Fiji, dengue outbreaks typically occur during the wetter, warmer season between December and July, when vectors are most abundant (Goettel et al., 1980). Although surveillance data can provide broad insights into arbovirus transmission patterns (Cuong et al., 2011; Funk et al., 2016; van Panhuis et al., 2015), and cross-sectional serosurveys can be used to measure contemporary levels of immunity (Aubry et al., 2015; Ferguson et al., 1999; Maguire et al., 1974; Waterman et al., 1993), characterising infection dynamics in detail requires cohort-based seroepidemiological studies (Cuong et al., 2011; Reiner et al., 2014), which can be difficult to implement in island settings where outbreaks are infrequent and difficult to predict.

Immediately before the 2013/14 dengue outbreak in Fiji, a population-representative serological survey had been conducted to study leptospirosis and typhoid (Lau et al., 2016). To investigate patterns of dengue infection in 2013/14, we followed up participants from this survey in Central Division, to obtain a set of paired pre- and post-outbreak serological samples (see Materials and methods). We tested the paired samples for anti-DENV IgG antibodies using ELISA and a recombinant antigen-based microsphere immunoassay (MIA), and combined these data with dengue surveillance data to compare possible explanations for the outbreak dynamics. We measured age-specific and spatial patterns of infection and reported disease, and tested whether there were demographic and environmental risk factors associated with infection. Having characterised factors shaping individual-level infection risk, we used a Bayesian approach to fit a transmission dynamic model to both the serological survey and surveillance data in order to estimate the contribution of climate and control measures to the decline in transmission observed in 2014.

## Results

The pre- and post-outbreak serological survey included 263 participants from the Central Division, with age distribution of these participants consistent with the population distribution (Figure 1B–C). We found that 58.6% of participants (154/263) were ELISA seropositive to at least one DENV serotype in late 2013. Two years later, in October/November 2015, this had risen to 74.5% (196/263). Additional serotype-specific MIA tests confirmed that the largest rise in seroprevalence in Central Division was against DENV-3, from 33.1% to 53.2% (Table 2), consistent with the majority of RT-PCR-confirmed samples during the outbreak being of this serotype.

**Table 2.**
 Number of participants who were seropositive to DENV in 2013 and 2015 as measured by ELISA and MIA.MIA any DENV denotes participants who were MIA seropositive to at least one DENV serotype. 95% CI shown in parentheses.


<table>
  <thead>
    <tr>
      <th>Test</th>
      <th>N</th>
      <th>2013</th>
      <th>2013 (%)</th>
      <th>2015</th>
      <th>2015 (%)</th>
      <th>Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ELISA</td>
      <td>263</td>
      <td>154</td>
      <td>58.6% (52.3–64.6%)</td>
      <td>196</td>
      <td>74.5% (68.8–79.7%)</td>
      <td>16% (11.8–21%)</td>
    </tr>
    <tr>
      <td>MIA any DENV</td>
      <td>263</td>
      <td>193</td>
      <td>73.4% (67.6–78.6%)</td>
      <td>216</td>
      <td>82.1% (77–86.6%)</td>
      <td>8.75% (5.62–12.8%)</td>
    </tr>
    <tr>
      <td>MIA DENV-1</td>
      <td>263</td>
      <td>177</td>
      <td>67.3% (61.3–72.9%)</td>
      <td>198</td>
      <td>75.3% (69.6–80.4%)</td>
      <td>7.98% (5.01–11.9%)</td>
    </tr>
    <tr>
      <td>MIA DENV-2</td>
      <td>263</td>
      <td>33</td>
      <td>12.5% (8.8–17.2%)</td>
      <td>41</td>
      <td>15.6% (11.4–20.5%)</td>
      <td>3.04% (1.32–5.91%)</td>
    </tr>
    <tr>
      <td>MIA DENV-3</td>
      <td>263</td>
      <td>87</td>
      <td>33.1% (27.4–39.1%)</td>
      <td>140</td>
      <td>53.2% (47–59.4%)</td>
      <td>20.2% (15.5–25.5%)</td>
    </tr>
    <tr>
      <td>MIA DENV-4</td>
      <td>263</td>
      <td>79</td>
      <td>30.0% (24.6–36%)</td>
      <td>99</td>
      <td>37.6% (31.8–43.8%)</td>
      <td>7.6% (4.71–11.5%)</td>
    </tr>
  </tbody>
</table>

To characterise patterns of infection between 2013 and 2015, we first considered individual-level demographic, behavioural and environmental factors. Using a univariable logistic regression model, we compared seroconversion determined by ELISA with questionnaire responses about household environment and health-seeking behaviour (Table 3). The factors most strongly associated with seroconversion between 2013–15 among initially seronegative participants were: living in an urban or peri-urban environment (odds ratio 2.18 [95% CI: 0.953–5.11], p=0.068); reporting fever in preceding two years (odds 2.94 [1.08–8.38], p=0.037); and visiting a doctor with fever in the preceding two years (odds 3.15 [1.06–10.10], p=0.043). Of the participants who seroconverted, 10/38 (26.3% [13.4–43.1%]) reported visiting a doctor with fever in the preceding two years, 2/38 (5.26% [0.644–17.7%]) reported fever but did not visit a doctor, and 26/38 (68.4% [51.3–82.5%]) did not report fever (Supplementary file 1A).

**Table 3.**
 Risk factors from a univariable logistic regression model.Sample population was all individuals who were seronegative in 2013 (n = 97), and outcome was defined as seroconversion as measured by ELISA. Number indicates total individuals with a given characteristic.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Number</th>
      <th>Odds ratio</th>
      <th>p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Demographic characteristics</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Age under 20</td>
      <td>61</td>
      <td>0.49 (0.21–1.13)</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>49</td>
      <td>0.81 (0.36–1.84)</td>
      <td>0.62</td>
    </tr>
    <tr>
      <td>iTaukei ethnicity</td>
      <td>85</td>
      <td>1.33 (0.39–5.32)</td>
      <td>0.66</td>
    </tr>
    <tr>
      <td>Environmental factors present</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Mosquitoes</td>
      <td>90</td>
      <td>4.19 (0.68–80.85)</td>
      <td>0.19</td>
    </tr>
    <tr>
      <td>Used car tires</td>
      <td>61</td>
      <td>1.80 (0.77–4.42)</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>Open water container(s)</td>
      <td>61</td>
      <td>1.49 (0.64–3.58)</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>Air conditioning</td>
      <td>23</td>
      <td>0.46 (0.15–1.26)</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>Blocked drains</td>
      <td>53</td>
      <td>1.04 (0.46–2.38)</td>
      <td>0.92</td>
    </tr>
    <tr>
      <td>Location</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Urban or peri-urban</td>
      <td>50</td>
      <td>2.18 (0.95–5.11)</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>Health seeking behaviour</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Fever in preceding 2 years</td>
      <td>20</td>
      <td>2.94 (1.08–8.38)</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>Visited doctor with fever in preceding 2 years</td>
      <td>16</td>
      <td>3.15 (1.06–10.13)</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>Household member visited doctor with fever in preceding 2 years</td>
      <td>9</td>
      <td>2.08 (0.52–8.94)</td>
      <td>0.30</td>
    </tr>
  </tbody>
</table>

As well as estimating infection by measuring seroconversion based on threshold values, we also considered the distribution of ELISA values. There was a noticeable right shift in this distribution between 2013 and 2015, with ELISA values increasing across a range of values (Figure 2A). As some of the individual-level changes in value between the two tests were likely to be due to measurement error (Salje et al., 2014), we fitted a mixture model to the distribution of changes in ELISA value (Figure 2B). We used a normal distribution with mean zero to capture measurement error, and a gamma distribution to fit rise that could not be explained by this error function. The fitted model suggested that a rise in value of at least three was more likely to be a genuine increase rather than measurement error, as shown by the dashed line in Figure 2B.

![Figure 2.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig2-v1.jpg)

**Figure 2.:** (A) Distribution of values in 2013 and 2015. Orange bars show observed proportion of samples with each value in 2013; blue bars show proportions in 2015. Dashed lines show threshold for seronegativity and seropositivity. (B) Change in ELISA values between 2013 and 2015. Bars show distribution of values. Grey line shows estimated uncertainty in assay measurements; blue line shows estimated increase in value following the 2013–14 epidemic; thin black line shows overall fitted distribution (model $R^{2}$=0.93). Dashed line shows probability of infection for a given rise in value. (C) Relationship between value in 2013 and rise between 2013 and 2015, adjusting for probability of infection as shown in Figure 2B. Points show 1000 bootstrap samples of the data with replacement, with opacity of each point proportional to probability of infection. Blue line shows prediction from generalized additive model, with data points weighted by probability of infection; shaded region shows 95% CI (model $R^{2}$=0.31).

To explore the relationship between the initial ELISA value and rise post-outbreak, given that an individual had been infected, we fitted a generalized additive model to the data and weighted each observation by the probability that a specific participant had been infected based on the dashed line in Figure 2B. By adjusting to focus on likely infections, we found a negative relationship between initial value and subsequent rise, with ELISA values near zero rising by around 10 units, but higher values exhibiting a smaller rise (Figure 2C). Using this approach, we also found strong evidence that self-reported symptoms were associated with larger rise in ELISA value, given likely infection. Using a logistic model with self-reported symptoms as outcome and change in value as dependent variable, adjusting for initial value and again weighting by probability of infection, we found that individuals who reported a fever in the preceding two years had a predicted rise in ELISA value that was 2.2 (95% 0.77–3.6) units higher than those who did not (p=0.003). Further, individuals who reported visiting a doctor with fever had a predicted value 3.3 (1.8–4.9) higher than others (p=0.0005).

Examining age patterns of seroprevalence, we found an increase in the proportion seropositive against DENV with age in both 2013 and 2015, and a rise in seroprevalence was observed in almost all age groups after the 2013/14 outbreak (Figure 3A). However, the high levels of seroprevalence in older age groups made it challenging to estimate age-specific probability of infection, because there was a relative lack of serologically naive individuals in these groups to act as a denominator (Table 4). We therefore again used rise in ELISA value as a correlate of infection, based on Figure 2B. As well as producing more precise estimates of infection risk in older groups (Table 4), this approach also suggested that individuals aged 10–19 years were most likely to be infected. This is in contrast to the surveillance data, which indicated the highest per capita level of reported disease was in the 20–29 age group (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig3-v1.jpg)

**Figure 3.:** (A) Proportion of each age group seropositive against DENV as measured by ELISA (blue squares) and DENV-3 by MIA (green circles). Lighter points show 2013 results, darker points show 2015; lines show 95% binomial confidence intervals. (B) Comparison of estimated age-specific infection and reported cases. Black points, estimated proportion infected based on ELISA rise indicated in Figure 2B; red points, cases reported per 1000 people in each age group; lines show 95% binomial confidence intervals.

**Table 4.**
 Estimated age-specific attack rates based on raw ELISA values, and seroconversion using ELISA cutoff.Estimated proportions of infections were calculated from the total of the probabilities that each individual in that age group had been infected, based on change in ELISA values between 2013 and 2015 (Figure 2B). Binomial 95% confidence intervals are shown in parentheses.


<table>
  <thead>
    <tr>
      <th>Age</th>
      <th>N</th>
      <th>Propn infected based on ELISA values</th>
      <th>Seronegative</th>
      <th>Seroconverted</th>
      <th>Seroconverted (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0–9</td>
      <td>27</td>
      <td>39.3% (22.2–59.3%)</td>
      <td>21</td>
      <td>6</td>
      <td>28.6% (11.3–52.2%)</td>
    </tr>
    <tr>
      <td>10–19</td>
      <td>59</td>
      <td>56% (44.1–67.8%)</td>
      <td>40</td>
      <td>14</td>
      <td>35% (20.6–51.7%)</td>
    </tr>
    <tr>
      <td>20–29</td>
      <td>45</td>
      <td>44.7% (31.1–60%)</td>
      <td>14</td>
      <td>8</td>
      <td>57.1% (28.9–82.3%)</td>
    </tr>
    <tr>
      <td>30–39</td>
      <td>41</td>
      <td>38% (24.4–53.7%)</td>
      <td>12</td>
      <td>4</td>
      <td>33.3% (9.92–65.1%)</td>
    </tr>
    <tr>
      <td>40–49</td>
      <td>28</td>
      <td>24.2% (10.7–39.3%)</td>
      <td>3</td>
      <td>3</td>
      <td>100% (29.2–100%)</td>
    </tr>
    <tr>
      <td>50–59</td>
      <td>28</td>
      <td>25.1% (10.7–42.9%)</td>
      <td>5</td>
      <td>2</td>
      <td>40% (5.27–85.3%)</td>
    </tr>
    <tr>
      <td>60–69</td>
      <td>21</td>
      <td>27.8% (9.52–47.6%)</td>
      <td>1</td>
      <td>1</td>
      <td>100% (2.5–100%)</td>
    </tr>
    <tr>
      <td>70+</td>
      <td>14</td>
      <td>36.6% (14.3–64.3%)</td>
      <td>1</td>
      <td>0</td>
      <td>0% (0–97.5%)</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>263</td>
      <td>39.6% (33.8–45.6%)</td>
      <td>97</td>
      <td>38</td>
      <td>39.2% (29.4–49.6%)</td>
    </tr>
  </tbody>
</table>

Next, we explored spatial patterns of infection in different communities. Previous studies have suggested that dengue outbreaks can spread outwards from urban hubs to more rural areas (Cummings et al., 2004; Salje et al., 2017). A similar spatial pattern was observed from the surveillance data during the early stages of the 2013/14 Fiji outbreak (Figure 4A). The first case was reported at Colonial War Memorial Hospital (CWM), Fiji’s largest hospital located in central urban Suva, in the week ending 4th November 2013. The outbreak took 9 weeks to reach the furthest reporting point from CWM in Central Division, a health centre 51 km away by Euclidean distance (i.e. as the crow flies). We found limited association between Euclidean distance from CWM and proportion of study cluster seropositive to DENV-3 in 2015 (Figure 4B): the Pearson correlation between ELISA seropositivity in each cluster and distance from CWM was $ρ$= –0.12 (p=0.59); for DENV-3 the correlation coefficient was $ρ$= –0.46 (p=0.03). However, we found no significant association between the Euclidean distance from CWM and proportion of cluster infected (Figure 4C). Pearson correlation between estimated proportion infected based on change ELISA value in each cluster and distance from CWM was $ρ$= 0.22 (p=0.30); for DENV-3 the correlation was $ρ$= –0.36 (p=0.09). We did find evidence of dengue seroconversion in every cluster, however, suggesting that the outbreak eventually spread throughout Central Division.

![Figure 4.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig4-v1.jpg)

**Figure 4.:** (A) Relationship between dengue cases reported by each health centre at the start of the outbreak and Euclidean distance from Colonial War Memorial Hospital (CWM) in Suva. Area of circle is proportional to number of cases reported in that week; each health centre is represented by a different colour. (B) Proportion seropositive in each serosurvey study cluster in 2015 vs Euclidean distance from CWM. Blue, ELISA data; green, MIA data; circles, urban or peri-urban clusters; crosses, rural clusters. (C) Proportion infected in each serosurvey study cluster vs Euclidean distance from CWM. Blue, estimate based on ELISA data, using adjustment in Figure 2B; green, seroconversion based on MIA for individuals who were initially seronegative; circles, urban or peri-urban clusters; crosses, rural clusters.

As we did not find strong evidence of individual or community-level heterogeneity in infection, we incorporated the surveillance data and paired serological survey data into mathematical models to test explanations for the observed outbreak dynamics at the division level. We considered three model variants: a simple age-structured model of vector-borne transmission dynamics; the same model structure, but with climate-driven variation in transmission; and a model with both climate-driven variation in transmission and a potential additional reduction in transmission coinciding with the clean-up campaign in March 2014. When we jointly fitted the models to surveillance data and age-specific immunity, as measured by seropositivity to DENV-3 by MIA in 2013 and 2015, the model with both climate-driven variation in transmission and an additional transmission reduction performed best as measured by AIC and DIC (Figure 5A–B and Table 5). This additional reduction in transmission was modelled using a flexible additional sigmoidal transmission rate, and was constrained so that the midpoint of the decline occurred after the start of the campaign on 8th March 2014 (Figure 5—figure supplement 1); we estimated a reduction of 57% (95% CrI: 42–82%) in transmission that coincided with the clean-up campaign (Figure 5C). As the effective reproduction number was near the critical value of one when the clean-up campaign was introduced (Figure 5D–E), it suggests that the main contribution of control measures may have been to bring DENV-3 infections to sufficiently low levels for transmission to cease earlier. We obtained the same conclusions when ELISA rather than MIA seroprevalence was used to quantify immunity during model fitting (Table 5 and Figure 5—figure supplement 2). It was noticeable that the model fitted to the ELISA data produced a qualitatively better fit to the surveillance data than the model fitted to MIA data. This was because the observed MIA values imposed a stronger constraint on the plausible range of model estimated seroprevalence (Figure 5B and Figure 5—figure supplement 2B), so in comparison the model fitted to ELISA data was able to attribute more of the slowdown in growth in the surveillance data during January/February to the accumulation of herd immunity.

![Figure 5.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-v1.jpg)

**Figure 5.:** (A) Model fit to surveillance data. Solid black dots, lab tested dengue cases; black circles, DLI cases; black line, total cases. Blue line shows median estimate from fitted model; dark blue region, 50% credible interval; light blue region, 95% CrI; red region shows timing of clean-up campaign. (B) Pre- and post-outbreak DENV immunity. Red dots show observed MIA seroprevalence against DENV-3 in autumn 2013 and autumn 2015; hollow dots, under 20 age group; solid dots, 20+ age group; lines show 95% binomial confidence interval. Dashed orange line shows model estimated rise in immunity during 2013/14 in under 20 group; solid line shows rise in 20+ group; shaded region shows 95% CrI. (C) Estimated variation in transmission over time. Red region, timing of clean-up campaign; green line, relative transmission as a result of control measures. Black line, basic reproduction number, $R_{0}$; blue line, effective reproduction number, $R$, accounting for herd immunity and control measures. Shaded regions show 95% CrIs. Dashed line shows the $R=1$ herd immunity threshold. (D) Average monthly rainfall (blue lines) and daily temperature (orange line, with black line showing weekly moving average) in Fiji during 2013–15. (E) Change in $R_{0}$ over time. Shaded regions show 95% CrIs.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Daily average temperature in Fiji during 2013/14; black line shows 7 day moving average (B) Average monthly rainfall in Fiji between 2003and 2014; thick lines show 2013/14 season. (C) Assumed relationship between temperature and mean vector lifespan (Mordecai et al., 2017). Blue lines show maximum and minimum temperature observed in Fiji during the 2013/14 season. (D) Relationship between temperature and extrinsic incubation period. (E) Relationship between temperature and probability of vector-to-human transmission. (F) Relationship between temperature and probability of human-to-vector transmission. (G) Relationship between temperature and daily biting rate. (H) Relationship between temperature and vector density (normalised to value at 25°C). (I) Relationship between rainfall and vector density (normalised to value at 400 mm). Solid line shows $K^=0.01$, dashed line, $K^=1$, dotted line, $K^=100$. (J) Illustrative example of a sigmoidal drop in transmission after clean-up campaign introduced on 8th March 2014. Here we assume a decline of 50%; in the model analysis this parameter is fitted, along with the gradient and timing of the decline. Red region shows timing of clean-up campaign.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Model fit to surveillance data. Solid black dots, lab tested dengue cases; black circles, DLI cases; black line, total cases. Blue line shows median estimate from fitted model; dark blue region, 50% credible interval; light blue region, 95% CrI; red region shows timing of clean-up campaign. (B) Pre- and post-outbreak DENV immunity. Red dots show observed MIA seroprevalence against DENV-3 in autumn 2013 and autumn 2015; hollow dots, under 20 age group; solid dots, 20+ age group; lines show 95% binomial confidence interval. Dashed orange line shows model estimated rise in immunity during 2013/14 in under 20 group; solid line shows rise in 20+ group; shaded region shows 95% CrI. (C) Estimated variation in transmission over time. Red region, timing of clean-up campaign; green line, relative transmission as a result of control measures. Black line, basic reproduction number, $R_{0}$; blue line, effective reproduction number, $R$, accounting for herd immunity and control measures. Shaded regions show 95% CrIs. Dashed line shows the $R=1$ herd immunity threshold. (D) Average monthly rainfall (blue lines) and daily temperature (orange line, with black line showing weekly moving average) in Fiji during 2013–15. (E) Change in $R_{0}$ over time. Shaded regions show 95% CrIs.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Histograms show the estimated posterior distributed from the MCMC chain, discarding burn in iterations, for each parameter in Table 7. Red lines show prior distributions if informative priors were used for that parameter.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** Black dots show samples from the joint posterior distribution, with median given by orange circle. Histograms show the marginal posterior for each parameter.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** (A) Model fit to surveillance data. Solid black dots, lab tested dengue cases; black circles, DLI cases; black line, total cases. Blue line shows median estimate from fitted model; dark blue region, 50% credible interval; light blue region, 95% CrI; red region shows timing of clean-up campaign. (B) Pre- and post-outbreak DENV immunity. Red dots show observed MIA seroprevalence against DENV-3 in autumn 2013 and autumn 2015; hollow dots, under 20 age group; solid dots, 20+ age group; lines show 95% binomial confidence interval. Dashed orange line shows model estimated rise in immunity during 2013/14 in under 20 group; solid line shows rise in 20+ group; shaded region shows 95% CrI. (C) Estimated variation in transmission over time. Red region, timing of clean-up campaign; green line, relative transmission as a result of control measures. Black line, basic reproduction number, $R_{0}$; blue line, effective reproduction number, $R$, accounting for herd immunity and control measures. Shaded regions show 95% CrIs. Dashed line shows the $R=1$ herd immunity threshold. (D) Average monthly rainfall (blue lines) and daily temperature (orange line, with black line showing weekly moving average) in Fiji during 2013–15. (E) Change in $R_{0}$ over time. Shaded regions show 95% CrIs.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp6-v1.jpg)

**Figure 5—figure supplement 6.:** (A) Model fit to surveillance data. Solid black dots, lab tested dengue cases; black circles, DLI cases; black line, total cases. Blue line shows median estimate from fitted model; dark blue region, 50% credible interval; light blue region, 95% CrI; red region shows timing of clean-up campaign. (B) Pre- and post-outbreak DENV immunity. Red dots show observed MIA seroprevalence against DENV-3 in autumn 2013 and autumn 2015; hollow dots, under 20 age group; solid dots, 20+ age group; lines show 95% binomial confidence interval. Dashed orange line shows model estimated rise in immunity during 2013/14 in under 20 group; solid line shows rise in 20+ group; shaded region shows 95% CrI. (C) Estimated variation in transmission over time. Red region, timing of clean-up campaign; green line, relative transmission as a result of control measures. Black line, basic reproduction number, $R_{0}$; blue line, effective reproduction number, $R$, accounting for herd immunity and control measures. Shaded regions show 95% CrIs. Dashed line shows the $R=1$ herd immunity threshold. (D) Average monthly rainfall (blue lines) and daily temperature (orange line, with black line showing weekly moving average) in Fiji during 2013–15. (E) Change in $R_{0}$ over time. Shaded regions show 95% CrIs.

![Figure 5—figure supplement 7.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig5-figsupp7-v1.jpg)

**Figure 5—figure supplement 7.:** (A) Model fit to surveillance data. Solid black dots, lab tested dengue cases; black circles, DLI cases; black line, total cases. Blue line shows median estimate from fitted model; dark blue region, 50% credible interval; light blue region, 95% CrI; red region shows timing of clean-up campaign. (B) Pre- and post-outbreak DENV immunity. Red dots show observed MIA seroprevalence against DENV-3 in autumn 2013 and autumn 2015; hollow dots, under 20 age group; solid dots, 20+ age group; lines show 95% binomial confidence interval. Dashed orange line shows model estimated rise in immunity during 2013/14 in under 20 group; solid line shows rise in 20+ group; shaded region shows 95% CrI. (C) Estimated variation in transmission over time. Red region, timing of clean-up campaign; green line, relative transmission as a result of control measures. Black line, basic reproduction number, $R_{0}$; blue line, effective reproduction number, $R$, accounting for herd immunity and control measures. Shaded regions show 95% CrIs. Dashed line shows the $R=1$ herd immunity threshold. (D) Average monthly rainfall (blue lines) and daily temperature (orange line, with black line showing weekly moving average) in Fiji during 2013–15. (E) Change in $R_{0}$ over time. Shaded regions show 95% CrIs.

**Table 5.**
 Comparison of model performance using AIC and DIC.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Serological data</th>
      <th>AIC</th>
      <th>ΔAIC</th>
      <th>DIC</th>
      <th>ΔDIC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SEIR</td>
      <td>MIA</td>
      <td>716.9</td>
      <td>66.69</td>
      <td>625.6</td>
      <td>35.62</td>
    </tr>
    <tr>
      <td>SEIR + climate</td>
      <td>MIA</td>
      <td>672.9</td>
      <td>22.7</td>
      <td>616.6</td>
      <td>26.65</td>
    </tr>
    <tr>
      <td>SEIR + climate + control</td>
      <td>MIA</td>
      <td>650.2</td>
      <td>0</td>
      <td>589.9</td>
      <td>0</td>
    </tr>
    <tr>
      <td>SEIR</td>
      <td>ELISA</td>
      <td>675.1</td>
      <td>25.74</td>
      <td>1219</td>
      <td>643.2</td>
    </tr>
    <tr>
      <td>SEIR + climate</td>
      <td>ELISA</td>
      <td>668.4</td>
      <td>19.09</td>
      <td>599.3</td>
      <td>23.52</td>
    </tr>
    <tr>
      <td>SEIR + climate + control</td>
      <td>ELISA</td>
      <td>649.3</td>
      <td>0</td>
      <td>575.8</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Fitting to the DENV-3 MIA seroprevalence data, we estimated that the mean basic reproduction number, $R_{0}$, over the course of the year was 1.12 (95% CrI: 1.02–1.25), with a peak value of 1.87 (1.70–2.07) in January 2014 (Table 6). Posterior estimates are shown in Figure 5—figure supplement 3 and correlation plots for the transmission rate parameters are shown in Figure 5—figure supplement 4. Accounting for stochastic variability in weekly case reporting, we estimated that 11% (1.1–39%) of infections were reported as laboratory-tested cases and 9.3% (1.1–39%) were reported as DLI cases. The estimated value of $R_{0}$ was larger for the model fitted to ELISA data, with a mean of 1.49 (1.35–1.69); this was the result of a larger proportion of the population assumed to be initially immune to infection.

**Table 6.**
 Parameter estimates for the 2013/14 dengue epidemic when the model was fitted to MIA or ELISA data.Median estimates are shown, with 95% credible intervals shown in parentheses. Mean $R_{0}$ is the average basic reproduction number over a year. Proportion reported was calculated by sampling from the negative binomial distribution that defines the model observation process (i.e. the credible interval reflects both underreporting and dispersion in weekly case reporting). $I_{h⁢c}^{0}$ and $I_{h⁢a}^{0}$ denote the number of initially infectious individuals in the younger and older age group respectively.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>MIA</th>
      <th>ELISA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mean R0</td>
      <td>1.12 (1.02–1.25)</td>
      <td>1.49 (1.35–1.69)</td>
    </tr>
    <tr>
      <td>Peak R0</td>
      <td>1.87 (1.7–2.07)</td>
      <td>2.5 (2.29–2.81)</td>
    </tr>
    <tr>
      <td>Control reduction</td>
      <td>0.57 (0.42–0.82)</td>
      <td>0.70 (0.37–0.95)</td>
    </tr>
    <tr>
      <td>Proportion reported, lab (%)</td>
      <td>11 (1.1–39)</td>
      <td>13 (2.6–36)</td>
    </tr>
    <tr>
      <td>Proportion reported, DLI (%)</td>
      <td>9.3 (0.99–37)</td>
      <td>12 (2.8–35)</td>
    </tr>
    <tr>
      <td>Ih⁢c0</td>
      <td>140 (18–550)</td>
      <td>0.98 (0.21–3.8)</td>
    </tr>
    <tr>
      <td>Ih⁢a0</td>
      <td>130 (19–680)</td>
      <td>1.3 (0.0094–57)</td>
    </tr>
  </tbody>
</table>

As well as performing worse under AIC and DIC, the model with only climate-driven variation in transmission could not capture the overall shape of the surveillance data (Figure 5—figure supplement 5). The basic model, which had neither climate-driven variation in transmission nor an additional reduction in transmission, could not jointly reproduce both sets of data either (Figure 5—figure supplement 6). Fitting the basic model to the surveillance data alone, we could reproduce the observed incidence pattern under the assumption of a simple immunising epidemic. Specifically, the reported cases were consistent with an epidemic that declined as a result of depletion of the susceptible population (Figure 5—figure supplement 7). However, this basic epidemic model underestimated the initial level of immunity and overestimated final immunity. A similar discrepancy between serological surveys and surveillance data has been noted in previous arbovirus modelling studies, albeit for ZIKV rather than DENV (Funk et al., 2016; Kucharski et al., 2016; Champagne et al., 2016).

## Discussion

We analysed surveillance reports and serological survey data to examine the dynamics of a major 2013/14 dengue outbreak in Fiji. Owing to the sporadic and unpredictable nature of dengue outbreaks in the Pacific (Cao-Lormeau et al., 2014), it is rare to have access to paired population-representative sera collected before and after such an epidemic. Comparing surveillance and serological survey data made it possible to investigate the relationship between observed reported cases and the true attack rate and quantify the relative role of climate, herd immunity and control measures in shaping transmission.

Analysis of detailed serological data provided insights into age-specific patterns of infection that would not be identified from seropositivity thresholds alone. We estimated the highest infection rate was in the 10–19-year-old age group, whereas proportionally the most reported cases were in the 20–29-year-old group. The apparent disparity between reported cases and infections estimated from the serological survey may be the result of secondary DENV infections causing more severe clinical disease and therefore increasing the likelihood of seeking medical care (OhAinle et al., 2011). The ELISA results suggested that fewer than 50% of individuals under age 20 had experienced DENV infection in 2013 (Figure 3A), which means an infection during the 2013/14 outbreak in this group was more likely to be primary than secondary. In contrast, the majority of 20–29 year olds already had evidence of infection in 2013, and hence 2013/14 outbreak would have generated relatively more secondary or tertiary infections in this group. In addition, if age-specific infection rates are indeed higher in younger groups, it means that estimating population attack rates based on the proportion of seronegative individuals infected may over-estimate the true extent of infection. Focusing on the seronegative subset of the population leads to children being over-sampled, which in our data inflates attack rate estimates by around 10% compared to estimates based on change in ELISA value (Table 4).

We also found little evidence of spatial heterogeneity in seroconversion. Although the locations of health centres reporting cases in the early stages of the outbreak suggested infection spread outwards from central Suva, we found evidence of DENV infection in all study clusters. This suggests that spatial structure may be more important in driving transmission dynamics early in the outbreak, but might not influence the final attack rate. One limitation of this comparison is that we did not have information on outbreak dynamics in the community: in the surveillance data, we only had the location of the health centres that cases reported to, rather than the location where infection likely occurred.

Analysis of risk factors suggested that presence of self-reported symptoms between 2013–15 was associated with DENV infection. There was also a strong association between rise in ELISA value and self-reported symptoms in individuals who were likely infected, which suggests that raw values from serological tests could potentially be used to estimate the proportion of a population who were asymptomatic during a dengue outbreak, even in older age groups that were already seropositive. However, it is worth noting that the questionnaire that accompanied the serosurvey was brief and only asked about fever and visits to a doctor with fever; there may be specific factors that can better predict prior infection in such settings. We also conducted the follow up survey around 18 months after the outbreak, which means recall bias is a potential limitation of the risk factor analysis. We did not identify environmental factors that were significantly associated with infection, likely as a result of the relatively small sample size in the serological survey, but the estimated odds ratios were broadly consistent with factors that would be expected to increase or decrease infection risk (Table 3).

To investigate potential explanations for the outbreak decline in early 2014, we fitted a transmission dynamic model with two human age groups to both surveillance and serological survey data. Our analysis shows the benefits of combining multiple data sources: with surveillance data alone, it would not have been possible to distinguish between self-limiting outbreak driven by a decline in the susceptible population, and one that had ceased for another reason. With the addition of serological data in the model fitting, however, our model was able to quantify the relative contribution of herd immunity, climate and control measures to the outbreak dynamics. In particular, this model suggested that seasonal variation in transmission and herd immunity alone could not explain the fall in transmission. However, an additional decline in transmission in March 2014, which coincided with a nationwide vector clean-up campaign, could better capture the observed patterns in serological and surveillance data.

There are some limitations to our modelling analysis. First, we assumed that seropositivity in IgG antibody tests was equivalent to protective immunity. High levels of neutralising antibodies have been shown to correlate with protection from symptomatic infection (Katzelnick et al., 2016), but it remains unclear precisely how much an individual with a given ELISA or MIA value contributes to transmission. Second, we focused on seroprevalence against DENV-3 in the main modelling analysis. As prior infection with one dengue serotype can lead to a cross-reactive immune response against other serotypes (Guzmán and Kourí, 2002), we fitted the model to ELISA results (which were not serotype specific) as a sensitivity analysis; this produced the same overall conclusions about which model performed best. Third, we used a flexible time-dependent transmission rate to capture a potential reduction in transmission as a result of control measures in March 2014. The clean-up campaign included multiple concurrent interventions, which occurred alongside ongoing media coverage of the outbreak; it was therefore not possible to untangle how specific actions – such as vector habitat removal or changes in community behaviour that reduced chances of being bitten – contributed to the outbreak decline. Moreover, factors unrelated to control, such as spatial structure or local weather effects, may also have contributed to the observed decline in transmission; there was heavy rain and flooding in Viti Levu at the end of February 2014 (ABC News, 2014).

Although we used a simple function to capture the potential impact of rainfall on vector density, it is unlikely that a more detailed mechanistic relationship would improve the model fit. The peak in rainfall in 2013/14 coincided with the peak in dengue cases; for rainfall to have strongly influenced observed transmission via a reduction in larval carrying capacity, it would need to have peaked earlier, to account for the time delays involved in the vector life cycle (Lourenço et al., 2017). We also assumed that all of the population could potentially be infected in the model. Some of the discrepancy between the high attack rate predicted by a randomly mixing model and lower observed seroconversion could in theory be explained by heterogeneity in transmission (Funk et al., 2016), which would be expected to reduce the overall proportion infected during an outbreak. If such heterogeneity exists, it is unlikely to act in an ‘all-or-nothing’ manner over time, with the same individuals remaining at low risk: the high level of seroprevalence in older age groups suggests that only a small proportion of individuals have consistently avoided infection (Figure 3).

Finally, our analysis focused on Central Division, Fiji. However, much of the data used in our model – such as surveillance data, post-outbreak serology, and climate information – would be available for other settings. For factors that are harder to measure without paired serology, like age-specific infection rates and potential effectiveness of control measures, a joint inference approach could be employed that combines prior distributions based on the data presented here with available outbreak data from the other location of interest (Funk et al., 2016).

Despite these caveats, our results show that transmission dynamic models developed using a combination of serological surveys and surveillance data can be valuable tool for examining dengue fever outbreaks. As well as providing insights into the transmission and control of dengue, the analysis has implications for forecasting of future epidemics. During February and March 2014, members of the research team based at London School of Hygiene and Tropical Medicine provided real-time analysis and outbreak projections for the Fiji National Centre for Communicable Disease Control, to support public health planning (Nand et al., 2016). However, a lack of serological data at the time meant it was necessary to make strong assumptions about pre-existing population immunity. With up-to-date population representative serology now available, forecasting models during future outbreaks will be able to include a more realistic herd immunity profile from the outset. Such seroepidemiological approaches could also be employed in other settings, to provide improved forecasts of dengue transmission dynamics and potential disease burden prior to and during outbreaks, as well as quantitative retrospective evaluation of the effectiveness of control measures.

## Materials and methods

### Surveillance data

In December 2013, the dengue outbreak in Fiji was determined to be due to DENV-3 by RT-PCR performed on serum samples sent to the World Health Organization Collaborating Centre for Arbovirus Reference and Research at the Queensland University of Technology (QUT, Brisbane). Hereafter, samples that were ELISA reactive for NS1 antigen or IgM were presumed to be to DENV-3 infections with a sub-sample of them sent for confirmatory serotyping at QUT, the Institut Louis Malardé (ILM) and the US Centers for Disease Control and Prevention. Of the 10,442 laboratory tested cases that were notified to the Fiji National Centre for Communicable Disease Control between 27th October 2013 and 4th March 2014, 4115 (39.4%) were reactive for DENV NS1 and/or anti-DENV IgM. After this time period, dengue surveillance was transitioned from laboratory to clinical-based reporting (i.e. dengue-like illness, DLI) due to the size of the outbreak (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig6-v1.jpg)

**Figure 6.:** (A) Lab -tested dengue cases reported in Northern (green), Western (blue) and Central (yellow) divisions between 27th October 2013 and 31st August 2014. (B) Total tested and confirmed cases in Central division (solid and dashed lines respectively), as well as proportion of cases that tested positive (grey line). (C) Dengue-like illness (DLI) over time. (D) Total suspected cases (i.e. tested and DLI).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Grey bars show weekly number of samples collected in Central Division across the two studies (paired samples shown only). Red line shows lab-tested cases in Central Division.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/34848/elife-34848-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Orange bars show observed proportion of samples with each value in 2013; blue bars show proportions in 2015. Dashed lines show threshold for seropositivity.

Between 27th October 2013 and 31st August 2014, 25,494 suspected cases of dengue (i.e. laboratory tested or confirmed or DLI) were notified to the Fijian Ministry of Health. Of these, 12,413 (48.7%) cases were in Central Division, predominantly in the greater Suva area (Figure 1). 10,679 cases were reported in the Western Division, 2048 cases were reported in the Northern division, largely in or near Labasa, the largest town of Vanua Levu island, and 354 cases were reported in the Eastern Division. For the lab-confirmed cases, date of testing was used to compile weekly case incidence time series; for the DLI data, date of presentation to a health centre was used, as these dates were most complete. Filter paper-based surveillance conducted by ILM between December 2013 and October 2014 found 24 samples positive for DENV-3 by RT-PCR, as well as three samples positive for DENV-2 and one for DENV-1. During 2014/15, there was a flare up of DENV-2 in Fiji. However, relatively few cases occurred on Viti Levu: of the 543 confirmed cases nationally between 1st January 2015 and 29th April 2015, 437 cases (80%) were from the Northern Division (World Health Organisation, 2015).

### Serological survey

We conducted a serological survey using pre- and post-outbreak sera from 23 communities in Central Division. Pre-outbreak sera were collected as part of population representative community-based surveys of leptospirosis and typhoid conducted in Central Division between September and November 2013 (Lau et al., 2016; Watson et al., 2017). Population-proportionate sampling was used to select local nursing zones (the smallest administrative unit). From each of these zones, one community was randomly selected, followed by 25 households from each community and one individual from each of the households. Coincidentally, the sample collection in Central Division finished the same week as the first dengue cases were reported (Figure 6—figure supplement 1). Post-outbreak sera were collected during a follow-up study carried out in October and November 2015. Field teams visited participants in Central Division who had previously participated in the 2013 serological study and had consented to being contacted again for health research.

Participants who gave informed consent for the 2015 study completed a questionnaire and provided a 5 ml blood sample. The study was powered to measure the rise in prevalence of anti-DENV antibodies between 2013–15. Historical dengue outbreaks in Fiji (Table 1) suggested we would expect to see seroconversion in at least 20% of the study population. Allowing for 5% seroreversion, and 0.05 probability of type-1 error, McNemar’s test suggested 250 paired samples could detect a 15% increase in seroprevalence with 95% power, and a 20% increase with $≈$100% power. We also collected data on potential risk factors and healthcare-seeking behaviour during this period. The questionnaire asked for details of fever and related visits to a doctor in the preceding two years, and the same for household members in the preceding two years. The questionnaire also recorded details of household environment, including potential mosquito breeding grounds (Supplementary file 2).

### Ethical considerations

The 2013 typhoid and leptospirosis studies and the 2015 follow up study were approved by the Fiji National Research Ethics Review Committee (ref 2013–03 and 2015.111.C.D) and the London School of Hygiene and Tropical Medicine Observational Research Ethics Committee (ref 6344 and 10207). Participants in the 2015 follow up study were people who had previously given informed consent to have their blood tested as part of a public health serum bank established in the 2013 typhoid and leptospirosis serosurvey, and agreed to be contacted again by public health researchers. The study was explained in English or the local iTaukei language by bilingual field officers, at the potential participants’ preference. Adults gave written informed consent, or thumbprinted informed consent witnessed by a literate adult independent from the study. For children age 12–17 years, written consent was obtained from both the parent and the child. For children aged under 12 years, written consent was obtained from the parent only, though information was provided to both.

### Serological testing of paired sera

Paired pre- and post-outbreak serum samples were tested using an indirect IgG ELISA kit (PanBio Cat No 01PE30), according to manufacturer guidelines. This assay employs recombinant DENV envelope proteins of all four serotypes (McBride et al., 1998). Samples with ELISA value of $\leq$9 PanBio units were defined as seronegative, $\geq$11 PanBio units seropositive, and values between 9 and 11 as equivocal. Seroconversion was defined as a change from seronegative to seropositive status. Because the indirect IgG ELISA does not distinguish between DENV serotypes, samples were also tested against each of the four specific DENV serotypes using a recombinant antigen-based microsphere immunoassay (MIA), as previously used to examine seroprevalence against different flaviviruses in French Polynesia (Aubry et al., 2017, 2018). Specifically, we wanted to measure the change in seropositivity to DENV-3 during the study period. As an additional validation, a subset of fifty samples from Central Division – including a mixture of those seronegative and seropositive by ELISA and MIA – were tested for the presence of neutralising antibodies against each of the four DENV serotypes using a neutralisation assay as previously described (Cao-Lormeau et al., 2016). A neutralisation titre of $\geq$20 was defined as seropositive (Figure 6—figure supplement 2A). For both MIA and neutralisation assay results, the largest change in seropositivity was for DENV-3 (Supplementary file 1B). When seropositivity to any DENV (i.e. seropositive to at least one serotype) was compared, a similar change was observed across ELISA, MIA and neutralisation assay results between 2013 and 2015.

### Serological modelling

Based on ELISA seropositivity in 2015 alone, it would not be possible to identify infections during the 2013/14 outbreak among individuals who were initially seropositive in 2013. We therefore examined the changes in paired individual-level ELISA values between 2013 and 2015. To estimate the probability that a given increase in ELISA value was the result of a genuine rise rather than measurement error, we fitted a two distribution mixture model to the distribution of changes in value between 2013 and 2015. We used a normal distribution with mean equal to zero to reflect measurement error, and a gamma distribution to capture a rise that could not be explained by the symmetric error function. The observed changes in ELISA value we fitted to ranged from −6 to 20; we omitted two outliers that had a change in value of −9 between 2013 and 2015, as these could not be explained with a normally distributed measurement error function. It was not possible to perform the same analysis using the MIA data because unlike the ELISA and neutralisation assay data, the raw MIA values did not follow a bimodal distribution that indicated likely naive and previously exposed individuals (Figure 6—figure supplement 2B). We used a generalized additive model with binomial link function to examine the relationship between ELISA value in 2013 and rise between 2013 and 2015, with data points weighted by probability that the change in ELISA value was the result of a genuine rise rather than measurement error. Risk factor analysis was performed using a univariable logistic regression model. Both were implemented using the mgcv package in R version 3.3.1 (Wood, 2006; R Core Team, 2015).

### Transmission model

#### Model structure

We modelled DENV transmission dynamics using an age-structured deterministic compartmental model for human and vector populations, with transitions between compartments following a susceptible-exposed-infective-removed (SEIR) structure (Kucharski et al., 2016; Manore et al., 2014; Pandey et al., 2013). As human population size was known, but the vector population was not, the human compartments were specified in terms of numbers and vectors in terms of proportions. Upon exposure to infection, initially susceptible humans ($S_{h}$) transitioned to a latent class ($E_{h}$), then an infectious class ($I_{h}$) and finally a recovered and immune class ($R_{h}$). The mosquito population was divided into three classes: susceptible ($S_{v}$), latent ($E_{v}$), and infectious ($I_{v}$). Mosquitoes were assumed to be infectious until they died. We had two human age groups in the model: aged under 20 (denoted with subscript $c$), and aged 20 and over (denoted with subscript $a$). We included births and deaths for the vector population, but omitted human births and deaths because the mean human lifespan is much longer than the duration of the outbreak. The model was as follows:

$$
dS_{hc}/dt=−\beta_{h}(t)S_{hc}I_{v}
$$



$$
dE_{hc}/dt=\beta_{h}(t)S_{hc}I_{v}−ν_{h}E_{hc}
$$



$$
dI_{hc}/dt=ν_{h}E_{hc}−\gammaI_{hc}
$$



$$
dR_{hc}/dt=\gammaI_{hc}
$$



$$
dS_{ha}/dt=−\beta_{h}(t)S_{ha}I_{v}
$$



$$
dE_{ha}/dt=\beta_{h}(t)S_{ha}I_{v}−ν_{h}E_{ha}
$$



$$
dI_{ha}/dt=ν_{h}E_{ha}−\gammaI_{ha}
$$



$$
dR_{ha}/dt=\gammaI_{ha}
$$



$$
dC/dt=ν_{h}(E_{hc}+E_{ha})
$$



$$
dS_{v}/dt=\delta(t)−\beta_{v}(t)S_{v}(\frac{I_{hc}+I_{ha}}{N})−\delta(t)S_{v}
$$



$$
dE_{v}/dt=\beta_{v}(t)S_{v}(\frac{I_{hc}+I_{ha}}{N})−ν_{v}(t)E_{v}−\delta(t)E_{v}
$$



$$
dI_{v}/dt=ν_{v}(t)E_{v}−\delta(t)I_{v}
$$

The compartment $C$ recorded the cumulative total number of human infections, which was used for model fitting. Based on most recent Fiji census in 2007, we set the population size $N$ to be 342,000 in Central Division (Fiji Bureau of Statistics, 2007), and split this population between the two age groups based on the populations of each reported in the census ($N_{c}$=133,020 and $N_{a}$=208,980). We estimated two initial conditions for each human age group: the initial number of infective individuals, $I_{h}^{0}$, and the initial number immune, $S_{h}^{0}$. We assumed that there were the same number of individuals initially exposed as there are individuals infectious (i.e. $E_{h}^{0}=I_{h}^{0}$). For the vector population, we only estimated the initial proportion infectious. We assumed that $E_{v}^{0}=I_{v}^{0}$ and the remaining proportion of mosquitoes were susceptible. We assumed that the mean intrinsic latent period, $1/ν_{h}$, and human infectious period, $1/\gamma$ remained constant over time, with informative priors (Table 7). As detailed in the sections below, the following parameters were time dependent: transmission rate from vectors to humans, $\beta_{h}⁢(t)$; transmission rate from humans to vectors, $\beta_{v}⁢(t)$; mosquito lifespan, $1/\delta⁢(t)$; and extrinsic latent period, $1/ν_{v}⁢(t)$. To avoid infection declining to implausibly small levels then rising again in the following season, we included potential for extinction in the model. If the number of individuals in any of the $E$ or $I$ human compartments dropped below one, the model set the value to zero. Hence if there were no exposed or infectious individuals in either of the age groups, the epidemic would end.

**Table 7.**
 Parameters fitted in the model.Prior distributions are given for all parameters, along with source if the prior incorporates a specific mean value. All rates are given in units of days$^{-1}$.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Definition</th>
      <th>Prior</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1/νh</td>
      <td>intrinsic latent period</td>
      <td>Gamma(μ=5.9, σ=0.1)</td>
      <td>(Chan and Johansson, 2012)</td>
    </tr>
    <tr>
      <td>1/γ</td>
      <td>human infectious period</td>
      <td>Gamma(μ=5, σ=0.1)</td>
      <td>(Duong et al., 2015)</td>
    </tr>
    <tr>
      <td>1/νv^</td>
      <td>extrinsic latent period at 25∘</td>
      <td>Gamma(μ=10, σ=0.1)</td>
      <td>(Mordecai et al., 2017; Chan and Johansson, 2012)</td>
    </tr>
    <tr>
      <td>1/δ^</td>
      <td>mosquito lifespan at 25∘</td>
      <td>Gamma(μ=8, σ=0.1)</td>
      <td>(Sheppard et al., 1969)</td>
    </tr>
    <tr>
      <td>α^</td>
      <td>biting rate at 25∘</td>
      <td>Gamma(μ=0.25, σ=0.1)</td>
      <td>(Mordecai et al., 2017)</td>
    </tr>
    <tr>
      <td>m^</td>
      <td>baseline vector density</td>
      <td>log⁡𝒰⁢(0,20)</td>
      <td>(Andraud et al., 2012)</td>
    </tr>
    <tr>
      <td>K^</td>
      <td>carrying capacity scaling parameter</td>
      <td>log⁡𝒰⁢(0,100)</td>
      <td></td>
    </tr>
    <tr>
      <td>a1</td>
      <td>gradient of sigmoidal change in transmission</td>
      <td>log⁡𝒰⁢(0,1000)</td>
      <td></td>
    </tr>
    <tr>
      <td>a2</td>
      <td>magnitude of sigmoidal change in transmission</td>
      <td>log⁡𝒰⁢(0,1)</td>
      <td></td>
    </tr>
    <tr>
      <td>aτ</td>
      <td>timing of sigmoidal change in transmission</td>
      <td>log𝒰(8th March 2014, 5th April 2014)</td>
      <td>(Break Dengue, 2014)</td>
    </tr>
    <tr>
      <td>rl⁢a⁢b</td>
      <td>proportion of cases reported as lab tested</td>
      <td>log⁡𝒰⁢(0,1)</td>
      <td></td>
    </tr>
    <tr>
      <td>rD⁢L⁢I</td>
      <td>proportion of cases reported as DLI</td>
      <td>log⁡𝒰⁢(0,1)</td>
      <td></td>
    </tr>
    <tr>
      <td>ρ</td>
      <td>reporting dispersion</td>
      <td>log⁡𝒰⁢(0,∞)</td>
      <td></td>
    </tr>
    <tr>
      <td>Ih⁢c0</td>
      <td>initial number infectious aged &lt; 20</td>
      <td>log⁡𝒰⁢(0,Nc)</td>
      <td></td>
    </tr>
    <tr>
      <td>Rh⁢c0</td>
      <td>initial number immune aged &lt; 20</td>
      <td>log⁡𝒰⁢(0,Nc)</td>
      <td></td>
    </tr>
    <tr>
      <td>Ih⁢a0</td>
      <td>initial number infectious aged 20+</td>
      <td>log⁡𝒰⁢(0,Na)</td>
      <td></td>
    </tr>
    <tr>
      <td>Rh⁢a0</td>
      <td>initial number immune aged 20+</td>
      <td>log⁡𝒰⁢(0,Na)</td>
      <td></td>
    </tr>
    <tr>
      <td>Iv0</td>
      <td>initial proportion of infectious mosquitoes</td>
      <td>log⁡𝒰⁢(0,1)</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Seasonal parameter variation

We assumed that the vector-specific parameters varied over time in the model, as a result of seasonal changes in temperature and rainfall (Descloux et al., 2012). During 2013/14 in Central Division, average monthly rainfall ranged from around 100 to 400 mm, and daily temperature varied between 21 and 30$^{∘}$C (The World Bank, 2016; Fiji Meteorological Service, 2017). Temperature reached its maximum in January/February, and minimum in August/September (Figure 5—figure supplement 1A). As the daily temperature data were noisy and surveillance data were only available on a weekly timescale, in the model we defined $temp_{t}$ as the seven day moving average of temperature on day $t$ (i.e. the average temperature over the preceding week). We also defined $rain_{t}$ as the average rainfall on day $t$, interpolated from monthly data (Figure 5—figure supplement 1B).

Based on estimated mechanistic relationships between temperature and Aedes aegypti dynamics (Lourenço et al., 2017; Mordecai et al., 2017), we assumed that the following vector-specific parameters were temperature dependent: extrinsic incubation period, $1/ν_{v}⁢(t)$; lifespan, $1/\delta⁢(t)$; biting rate, $\alpha⁢(t)$; probability of transmission to a human, $p_{v⁢h}⁢(t)$; and probability of infection from an infectious human, $p_{h⁢v}⁢(t)$. We incorporated these temperature-dependent dynamics using symmetric ($ϕ$) and asymmetric ($ψ$) unimodal thermal response functions (Mordecai et al., 2017; Briere et al., 1999):

$$
ϕ⁢(x,y,T_{m},T_{0})={min⁡{y⁢(x-T_{0})⁢(T_{m}-x),1}if ⁢T_{0}<x<T_{m}0else
$$



$$
ψ⁢(x,y,T_{m},T_{0})={min⁡{y⁢x⁢(x-T_{0})⁢\sqrt{T_{m}-x},1}if ⁢T_{0}<x<T_{m}0else
$$

The parameters were defined using the median estimated value from these functions fitted to empirical data (Mordecai et al., 2017):

$$
1/ν_{v}(t)=1/(ν_{v}^ϕ(temp_{t},6.11\times10^{−5},45.53,10.30)/0.10)
$$



$$
1/\delta(t)=1/(\delta^ψ(temp_{t},9.02,37.66,−0.14)/29.00)
$$



$$
\alpha(t)=\alpha^ϕ(temp_{t},0.00020,40.04,13.76)/0.22
$$



$$
p_{vh}(t)=ϕ(temp_{t},0.00083,35.78,17.23)
$$



$$
p_{hv}(t)=ϕ(temp_{t},0.00049,37.38,12.67)
$$

Here $1/ν_{v}⁢(t)$, $1/\delta⁢(t)$ and $\alpha⁢(t)$ are normalised so that they equal $1/ν_{v}^$, $1/\delta^$, and $\alpha^$ respectively when $temp_{t}=25^{∘}$C. In the model, most of these parameters varied monotonically within the temperature range observed in Fiji (Figure 5—figure supplement 1C–G). We used informative priors for the average extrinsic latent period, $1/ν_{v}^$, mosquito lifespan, $1/\delta_{v}^$, and biting rate, $\alpha^$ (Table 7).

We assumed that vector density, $m⁢(t)$, could vary with both temperature and rainfall (Figure 5—figure supplement 1H–I). The contribution of vector density to transmission was influenced by four factors (Mordecai et al., 2017): fecundity, $f$ (i.e. number of eggs produced per female mosquito per day); egg-to-adult survival probability, $e$, the mosquito development rate, $d$, and the larval carrying capacity $K$. In the model, vector density over time was equal to:

$$
(20)m(t)=m(temp_{t},rain_{t})(21)=\frac{m^}{m_{0}}e(t)f(t)d(t)\frac{K(t)}{1+K(t)}
$$

where $\frac{m^}{m_{0}}$ is a scaling term and the $K/(1+K)$ term incorporating carrying capacity follows from the equilibrium solution of the logistic growth model (Pearl and Reed, 1920) (Figure 5—figure supplement 1I). We assumed that $d$, $e$, and $f$ were temperature dependent, based on functions fitted to empirical data (Mordecai et al., 2017), and $K$ was linearly dependent on rainfall:

$$
d(t)=ϕ(temp_{t},7.84e\times10^{−5},39.10,11.56)
$$



$$
e(t)=ψ(temp_{t},13.58,38.29,−0.0060)
$$



$$
f(t)=ϕ(temp_{t},0.0082,34.44,14.78)
$$



$$
K(t)=K^rain_{t}/222.44
$$

$K⁢(t)$ was normalised so its mean value over the year was equal to $K^$ and we set $m_{0}=0.5752381$ so that $m⁢(t)=m^⁢K/(1+K)$ when the temperature was 25$^{∘}$. Prior distributions for parameter values are given in Table 7. In the absence of control measures, the vector-to-human, $\beta_{h}$, and human-to-vector, $\beta_{v}$, transmission rates were therefore:

$$
\beta_{v}(t)=\alpha(t)p_{vh}(t)
$$



$$
\beta_{h}(t)=\alpha(t)p_{hv}(t)m(t)
$$

### Control measures

To capture the potential additional reduction in transmission over time as a result of the national clean-up campaign between 8th and 22nd March 2014, we used a flexible sigmoid function:

$$
χ(t)=(1−\frac{a_{2}}{1+e^{−a_{1}(t−a_{\tau})}})
$$

We constrained this function so that the midpoint, $a_{\tau}$, was between the start date of the campaign, 8th March 2014, and 5th April 2014, four weeks later (Figure 5—figure supplement 1J). We assumed that this function acted to reduce the vector-to-human transmission rate:

$$
\beta_{h}(t)=\alpha(t)m(t)χ(t)
$$

There were multiple concurrent interventions during the clean-up campaign, including promotion of awareness about protection from bites as well as larval habitat removal. Given the structure of the data available, it would not be possible to independently estimate the extent to which the campaign directly reduced vector-to-human transmission, that is $χ⁢(t)$ acting on $\alpha⁢(t)$, rather than vector density, that is $χ⁢(t)$ acting on $m⁢(t)$. However, if there had been a substantial effect on larval habitat capacity but not on biting rate, we may expect to infer a larger value of $a_{\tau}$, to reflect the delay in impact as a result of the time required for vector development.

### Effective reproduction number

The next generation matrix for humans and vectors was defined as follows (Manore et al., 2014, 2017):

$$
(R_{h⁢h}R_{h⁢v}R_{v⁢h}R_{v⁢v})=(0\frac{\beta_{h}⁢(S_{h⁢c}+S_{h⁢a})⁢ν_{v}}{\delta⁢(\delta+ν_{v})⁢N}\frac{\beta_{v}⁢S_{v}}{\gamma}0)
$$

and the effective reproduction number, $R$, was equal to the dominant eigenvalue of this matrix. The basic reproduction, $R_{0}$, was calculated by the same method, but assuming that both humans and vectors were fully susceptible.

### Model fitting

The model was jointly fitted to laboratory-confirmed case data and serological data using Markov chain Monte Carlo (MCMC) via a Metropolis-Hastings algorithm. For the case data, we considered time units of one week. To construct a likelihood for the observed cases, we defined case count for week $t$ as $c_{t}=C_{t}-C_{t-1}$.

Because reporting switched from lab tested to DLI during the outbreak, we jointly fitted two sets of time series data. The first dataset was lab tested cases. We defined the first observation as 4th November 2013, the week of the first confirmed case in Central Division, and the last observation as 26th May. The second dataset was DLI cases, which we fitted from 1st February until 26th May. Earlier DLI cases were not included as these were likely to reflect reporting artefacts rather than genuine infections. The two time series we fitted were disjoint: cases were either reported as lab tested or DLI.

We assumed that the two set of observed cases followed a negative binomial distributions with mean $q_{t}⁢r_{l⁢a⁢b}⁢c_{t}$ and $(1-q_{t})⁢r_{D⁢L⁢I}⁢c_{t}$ respectively, and a shared dispersion parameter $ρ$, to account for potential temporal variability in reporting (Bretó et al., 2009). We used a negative binomial distribution to allow for both under- or over-reporting, the latter being potentially relevant in the final stages of the outbreak when case numbers were low. Here $q_{t}$ denotes the proportion of cases in week $t$ that are lab tested rather than reported as DLI. As it was not possible to fit this value for each week, it was fixed in the model as $q_{t}=y_{l⁢a⁢b}/(y_{l⁢a⁢b}⁢(t)+y_{D⁢L⁢I}⁢(t))$, where $y_{l⁢a⁢b}⁢(t)$ and $y_{D⁢L⁢I}⁢(t)$ are the number of observed lab tested and DLI cases in week $t$ respectively. The total expected number of reported cases in week $t$ was therefore equal to $(q_{t}⁢r_{l⁢a⁢b}+(1-q_{t})⁢r_{D⁢L⁢I})⁢c_{t}$.

As well as fitting to surveillance data, we fitted the model to the proportion of each age group immune (as measured by seroprevalence) at the start and end of the outbreak. Let $X_{i⁢j}$ be a binomially distributed random variable with size equal to the sample size in group $i$ and probability equal to the model predicted immunity in year $j$, and $z_{i⁢j}$ be the observed seroprevalence in group $i$ in year $j$. The overall log-likelihood for parameter set $\theta$ given case data $Y={y_{t}}_{t=1}^{T}$ and serological data $Z={z_{i⁢j}}_{i\in{1,2},j\in{2013,2015}}$ was therefore:

$$
L(\theta|Y,Z)=\sumtlogP(y_{t}|c_{t})+\sumi=12\sumj\in{2013,2015}logP(X_{i⁢j}=z_{i⁢j})
$$

We considered four model scenarios: an SEIR model without climate-driven variation or control, fitted to surveillance data only; SEIR model without climate-driven variation or control, fitted to surveillance and serological data; SEIR model with climate-driven variation only, fitted to surveillance and serological data; SEIR model with climate-driven variation and control, fitted to surveillance and serological data. We fitted the model to either MIA or ELISA data, to reflect two different assumptions about the relationship between seroprevalence and immunity. The model using MIA data made the assumption that only individuals who were seropositive to DENV-3 were immune to this serotype. As a sensitivity analysis, the model using ELISA data assumed that seropositivity to any DENV serotype indicated immunity to DENV-3.

All observations were given equal weight in the model fitting. The joint posterior distribution of the parameter set $\theta$ was obtained from 200,000 MCMC iterations, each with a burn-in period of 20,000 iterations. We used adaptive MCMC to improve efficiency of mixing: we iteratively adjusted the magnitude of the covariance matrix used to resample $\theta$ to obtain a target acceptance rate of 0.234 (Roberts and Rosenthal, 2009). Posterior estimates for MIA and ELISA data are shown in Supplementary files 1C–D. The statistical and mathematical models were implemented in R version 3.3.1 (R Core Team, 2015) using the deSolve package (Soetaert et al., 2010) and parallelised using the doMC library (Revolution Analytics, 2014).

### Model comparison

We compared the performance of different models using the deviance information criterion (DIC), which accounts for the trade off between model fit and complexity (Spiegelhalter et al., 2002). The deviance of a model for a given parameter set, $\theta$, is given by $D(\theta)=−2L(\theta|Y,Z)$. The DIC is therefore:

$$
D⁢I⁢C=D⁢(\theta¯)+var⁢(D⁢(\theta))
$$

where $\theta¯$ is the median of $\theta$ with respect to the posterior distribution and $var⁢(D⁢(\theta))/2$ is the effective number of parameters. The median of $\theta$ as used rather than mean because the likelihood was non-log-concave in $\theta$, which meant that the posterior mean was a poor estimator (Spiegelhalter et al., 2002). As an additional validation, we compared models using the Akaike information criterion (AIC), which accounts for the trade off between model fit and complexity (Akaike, 1973). The AIC of a model for a given parameter set, $\theta$, is given by $A⁢I⁢C=-2⁢L^⁢(\theta)+2⁢n_{p⁢a⁢r⁢a⁢m}$ where $L^⁢(\theta)$ is the maximised value of the likelihood and $n_{p⁢a⁢r⁢a⁢m}$ is the number of parameters.

### Data availability

Serological, surveillance and climate data are provided in Supplementary file 3. Code and data required to reproduce the main serological and modelling analysis are available at: https://github.com/adamkucharski/fiji-denv3-2014. Copy archived at https://github.com/elifesciences-publications//fiji-denv3-2014.
