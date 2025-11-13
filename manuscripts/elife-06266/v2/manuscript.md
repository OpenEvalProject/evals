# Dynamics of preventive vs post-diagnostic cancer control using low-impact measures

## Authors

- Andrei R Akhmetzhanov<sup>1</sup>
- Michael E Hochberg<sup>1</sup> †

### Affiliations

1. Institut des Sciences de l'Evolution de Montpellier University of Montpellier Montpellier France
2. Theoretical Biology Lab, Department of Biology McMaster University Hamilton Canada
3. Santa Fe Institute Santa Fe United States
4. Wissenschaftskolleg zu Berlin Berlin Germany

† Corresponding author

## Abstract

Cancer poses danger because of its unregulated growth, development of resistance, and metastatic spread to vital organs. We currently lack quantitative theory for how preventive measures and post-diagnostic interventions are predicted to affect risks of a life threatening cancer. Here we evaluate how continuous measures, such as life style changes and traditional treatments, affect both neoplastic growth and the frequency of resistant clones. We then compare and contrast preventive and post-diagnostic interventions assuming that only a single lesion progresses to invasive carcinoma during the life of an individual, and resection either leaves residual cells or metastases are undetected. Whereas prevention generally results in more positive therapeutic outcomes than post-diagnostic interventions, this advantage is substantially lowered should prevention initially fail to arrest tumour growth. We discuss these results and other important mitigating factors that should be taken into consideration in a comparative understanding of preventive and post-diagnostic interventions.

## Introduction

Mathematical models play an important role in describing and analysing the complex process of carcinogenesis. Natural selection for increases in tumour cell population growth can be represented as the net effect of increased cell division rates and/or decreased apoptosis (e.g., Wodarz and Komarova, 2007). Relatively rare driver mutations confer such a net growth advantage, whereas numerically dominant passenger mutations with initially neutral or mildly deleterious effects (Marusyk et al., 2012; Bozic et al., 2013; McFarland et al., 2013) can increase in frequency due to genetic hitchhiking or subsequent positive selection. Amongst the many passengers in a growing tumour, some can contribute to chemoresistance, and sufficiently large tumours could contain different clones that, taken as a group, can resist some, if not most, chemotherapies (see Michor et al., 2005 for resistance to imatinib). Chemotherapeutic remission followed by relapse suggests that these resistant cells are often present at low frequencies prior to therapy, either due to genetic drift or costs associated with resistance. Resistant phenotypes subsequently increase in frequency during radiotherapy or chemotherapy, and through competitive release they may incorporate one or more additional drivers, resulting in accelerated growth compared to the original tumour (for related discussion on pathogens, see Huijben et al., 2013).

Previous mathematical studies have considered alternatives to attempting to minimize or eradicate clinically diagnosed cancers with maximum tolerated doses (MTDs) of chemotherapeutic drugs. This body of work indicates that MTD is particularly prone to select for chemoresistance (e.g., Foo and Michor, 2009; Foo and Michor, 2010; Lorz et al., 2013), and what little empirical work exists supports this basic prediction (Turke et al., 2010), but see (Kouyos et al., 2014) for other disease systems. Numerous alternatives to the goal of cancer minimization/eradication have been proposed and investigated (e.g., Maley et al., 2004; Komarova and Wodarz, 2005; Foo and Michor, 2009; Gatenby et al., 2009a, 2009b; Bozic et al., 2013; Jansen et al., 2015). For example, Komarova and Wodarz (2005) considered how the use of one or multiple drugs could prevent the emergence or curb the growth of chemoresistance. They showed that the evolutionary rate and associated emergence of a diversity of chemoresistant lineages is a major determinant in the success or failure of multiple drugs vs a single one. Lorz and co-workers (Lorz et al., 2013) recently modelled the employment of cytotoxic and cytostatic therapies alone or in combination and showed how combination strategies could be designed to be superior in terms of tumour eradication or managing resistance than either agent used alone. Foo and Michor (2009) evaluated how different dosing schedules of a single drug could be used to slow the emergence of resistance given toxicity constraints. One of their main conclusions is that drugs slowing the generation of chemoresistant mutants and subsequent evolution are more likely to be successful than those only increasing cell death rates.

These and other computational approaches have yet to consider the use of preventive measures to reduce cancer-associated morbidity and mortality whilst limiting resistance. Prevention includes life-style changes and interventions or therapies in the absence of detectable invasive carcinoma (e.g., Etzioni et al., 2003; Lippman and Lee, 2006; William et al., 2009; Hochberg et al., 2013), for example, reduced cigarette consumption (Doll and Peto, 1976) or chemoprevention (Steward and Brown, 2013). In depth consideration of preventive measures and their likely impact on individual risk and epidemiological trends is important given the likelihood that all individuals harbour pre-cancerous lesions, some of which may transform into invasive carcinoma (Bissell and Hines, 2011; Greaves, 2014), and concerns as to whether technological advances will continue to make significant headway in treating clinically detected cancers (Gillies et al., 2012; Vogelstein et al., 2013).

Here, we model how continuous, constant measures affect tumour progression and the emergence of resistant lineages. We assume that an individual can contract at most a single cancer, originating from a single lesion. Importantly, we consider cases where the measure may select for the evolution of resistant phenotypes and cases where no resistance is possible. Our approach is to quantify the daily extent to which a growing neoplasm must be arrested in order to either eradicate it or to delay a potentially lethal cancer. Several authors have previously argued how constant or intermittent low toxicity therapies either before or after tumour discovery could be an alternative to MTD chemotherapies (Wu and Lippman, 2011; Hochberg et al., 2013), but to our knowledge, no study has actually quantified based on empirical parameter estimates, the extent to which cancer cell population growth needs to be arrested for such approaches to succeed (see related discussion in Bozic et al., 2010; Gerstung et al., 2011; Bozic et al., 2013). Below we employ the terms ‘treatment’, ‘measure’, and ‘therapy’ interchangeably, all indicating intentional measures to arrest cancer cell population growth.

We first derive analytical expressions for the expected total number of cells within a tumour at any given time. We explore dynamics of tumour sizes at given times, and times to detection for given tumour sizes. Specifically, we show that the expected mean tumour size in a population of subjects can be substantially different from the median, since the former is highly influenced by outliers due to tumours of very large size. We then consider constant preventive measures and show that treatment outcome is sensitive to initial conditions, particularly for intermediate-sized tumours. Importantly, we provide approximate conditions for tumour control both analytically and numerically using empirical parameter estimates. We next consider post-diagnostic interventions in which tumour resection either is not complete and leaves residual cells or undetected metastases are present. We contrast these with prevention scenarios where (1) there is no difference in the age at which either prevention or post-diagnostic intervention commences, and (2) prevention and post-diagnostic interventions are alternatives, that is, the former always occurs before the latter. We show as expected that therapeutic outcomes are generally superior under prevention vs post-diagnostic intervention, and that higher impacts on the cancer cell population are usually required for post-diagnostic interventions to achieve a level of control comparable to prevention. Moreover, we find that should resection leave sufficiently large numbers of residual cells (or metastases are not discovered), then a range of the most successful outcomes under prevention is not attainable under post-diagnostic intervention, regardless of potential cell arrest. Finally and importantly, whereas there is little gained in terms of outcomes in post-diagnostic intervention beyond approximately 0.3% cell arrest per day for both small (10,000) and large (1 million) cancer cell populations, prevention outcomes may achieve continual gains for the latter cell number, up to about 0.6% cell arrest per day.

## Modeling framework

Previous study has evaluated the effects of deterministic and stochastic processes on tumour growth and the acquisition of chemoresistance (Komarova and Wodarz, 2005; Bozic et al., 2010; Reiter et al., 2013, see review Beerenwinkel et al., 2015). We first consider both processes through exact solutions and numerical simulations of master equations, using the mean field approach (see Appendix 1 for details). A mean field approach assumes a large initial number of cells (Krapivsky et al., 2010) and averages any effects of stochasticity, so that an intermediate state of the system is described by a set of ordinary differential equations (i.e., master equations; Gardiner, 2004). Solutions to these are complex even in the absence of the explicit consideration of both drivers and passengers (Antal and Krapivsky, 2011; Kessler and Levine, 2013).

We do not explicitly model the different pre-cancerous or invasive carcinoma states. Rather, our approach follows the dynamics of the relative frequencies of subclones, each composed of identical cells (Baake and Wagner, 2001; Saakian and Hu, 2006). We simulate tumour growth using a discrete time branching process for cell division (Athreya and Ney, 1972; Bozic et al., 2010). For each numerical experiment, we initiate a tumour of a given size and proportion of resistant cells.

Briefly, the model framework is as follows. Each cell in a population is described by two characteristics. The first is its resistance status to the measure, which is either ‘not resistant’ (j = 0) or ‘resistant’ (j = 1). The second property is the number of accumulated driver mutations (maximum N) in a given cell line. At each time step of 4 days, cells either divide or die, and when a cell divides, its daughter cell has a probability $u$ of producing a driver mutation and v of producing a resistant mutation. We assume no back mutation, and that cells do not compete for space or limiting resources.

The fitness function fij, the difference between the birth and death rates of a cell, is defined by the number of accumulated drivers (i = 0, 1, …, N) and resistance status (j = 0, 1): a sensitive cancerous cell with a single driver has selective advantage s, and any accumulated driver adds s to fitness, while resistance is associated with a constant cost c. Exposure to a single treatment affects only non-resistant cells (j = 0), incurring a loss σ to their fitness. Thus, the fitness function is:

$$
f_{ij}=s(i+1)−\sigma(1−j)−cj.
$$

The assumption of driver additivity is a special case of multiplicative fitness, and both are approximately equivalent for very small s.

We conducted numerical experiments, each with the same initial states but each using a unique set of randomly generated numbers of a branching process. For each simulation and each time step, the number of cells at time (t + 1) was sampled from a multinomial distribution of cells at time t (see Bozic et al., 2010 for details). Table 1 presents baseline parameter values employed in this study. Hereafter, we refer to σ as the treatment intensity (applied once every cell cycle of 4 days), while the corresponding daily arrest level to non-resistant cells is approximated by σ/4.

**Table 1.**
 Baseline parameter values used in this study


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Variable</th>
      <th>Value</th>
      <th>Range</th>
      <th>Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Time step (cell cycle length)</td>
      <td>T</td>
      <td>4 days</td>
      <td>3–4 days</td>
      <td>(Bozic et al., 2010)</td>
    </tr>
    <tr>
      <td>Selective advantage</td>
      <td>s</td>
      <td>0.4%</td>
      <td>0.1–1.0%</td>
      <td>(Bozic et al., 2010)</td>
    </tr>
    <tr>
      <td>Cost of resistance</td>
      <td>c</td>
      <td>0.1%</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Mutation rate to acquire an additional driver</td>
      <td>u</td>
      <td>3.4 × 10−5</td>
      <td>10−7–10−2</td>
      <td>(Bozic et al., 2010)</td>
    </tr>
    <tr>
      <td>Mutation rate to acquire resistance</td>
      <td>v</td>
      <td>10−6</td>
      <td>10−7–10−2</td>
      <td>(Komarova and Wodarz, 2005)</td>
    </tr>
    <tr>
      <td>Maximal number of additional drivers</td>
      <td>N</td>
      <td>5 (Figures 1, 2) 9 (other figures)</td>
      <td>0–9</td>
      <td></td>
    </tr>
    <tr>
      <td>Initial cell population</td>
      <td>M0</td>
      <td>106 cells</td>
      <td>–</td>
      <td></td>
    </tr>
    <tr>
      <td>Pre-resistance level</td>
      <td>κ</td>
      <td>0.01%</td>
      <td>–</td>
      <td>(Iwasa et al., 2006)</td>
    </tr>
    <tr>
      <td>Number of replicate numerical simulations (excluding extinctions)</td>
      <td>–</td>
      <td>106</td>
      <td>–</td>
      <td></td>
    </tr>
    <tr>
      <td>Detection threshold</td>
      <td>M</td>
      <td>109 cells</td>
      <td>107–1011</td>
      <td>(Beckman et al., 2012)</td>
    </tr>
  </tbody>
</table>

_‘Range’ is values from previous study and employed in the present study._

## Results

### Preventive measures

We first study preventive interventions where a patient has a high risk of developing a cancer and/or a biomarker that indicates the probable presence of a cancer. In either case, so that we can compare and contrast different intervention levels, we assume that the (undetected) tumour contains M0 cells when prevention commences. We examine effects on the mean by considering the distribution of tumour sizes at different times using mean-field dynamics (see Appendix 1). Numerical experiments were then conducted by assuming that tumours initially contained M0 = 106 identical cells (i = 0), of which 0.01% were resistant. These assumptions are obviously oversimplifications, and we relax some of them below and in the next sections.

There is an excellent correspondence between analytical and numerical results for σ varied in range of s (Appendix 1—figure 1A). A more detailed study of the distribution of tumour sizes reveals that the mean diverges considerably from median behaviour in the majority of cases, since the former is strongly influenced by outliers with high-tumour cell numbers (see Appendix 1—figure 1B).

Figure 1 shows four examples of numerical experiments. An untreated tumour reaches the assumed detection threshold of 109 cells by about 18 years on average and because it is not subject to strong negative selection (we assume low c), any emerging resistant cell-lines are likely to remain at low frequency (0.03% at the detection time in the example of Figure 1A). In Figure 1B, low-treatment intensity delays tumour growth and thus time of detection by approximately 16 years, while an increase in dose tends to result in tumours dominated by resistant cells (Figure 1C). Despite being unaffected by treatment, resistant cell populations are sometimes observed to go extinct stemming from stochasticity (Figure 1D), and this tends to occur more at high-treatment levels, because there are fewer sensitive tumour cells to seed new (mutant) resistant cell populations.

![Figure 1.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig1-v2.jpg)

**Figure 1.:** Examples of single patient tumour growth for (A) no treatment. (B) σ = 0.6%. (C) σ = 1.0%. (D) σ = 2.0%. The shaded area shows the change in total tumour size and the hatched area, the resistant part of a tumour. The treatment intensity σ in this and all other figures are represented as cell arrest per day (σ/4). Parameter values as in Table 1.

We next considered how therapies affected the distribution of tumour detection times in cases where the cancer cell population attained a threshold of 109 cells. The magnitude of the selective advantage s shows that tumour growth is largely driven by its non-resistant part for relatively low-impact treatments σ < 2s (Figure 2A). Importantly, the tumour shifts from being mainly non-resistant to resistant at σ ≈ 2s, which is reflected by the inflection point in the trajectory of the median (indicated by point B in Figure 2A,B). Notice that detection times are also most variable at σ ≈ 2s. The median changes smoothly at high-treatment levels (σ > 2s), tending to a horizontal asymptote. This is explained by the fact that the sensitive part is heavily suppressed at high-treatment levels, meaning that the dynamics are strongly influenced by the actual time point at which the first resistance mutation occurs.

![Figure 2.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig2-v2.jpg)

**Figure 2.:** The median (lines) and 90% confidence intervals (shaded areas) of detection times, measured as years beyond the initiation of the preventive measure. Effects of: (A) the selective advantage of each additional driver and (B) the cost of resistance. (C) Samples of the distribution of detection times (in relative frequencies, adjusted for 3-month bins) for corresponding points, indicated in A and B. Dashed black line is the mean and the dashed-and-dotted line is the median. The colour-code indicates the average level of resistance in detected tumours over 3 month intervals (see inset in B). All cells j = 0 at t = 0. Other parameters as in Table 1. Detection time is log-transformed in A and B.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Maximal number of additionally accumulated drivers. (B) Initial cell number. (C) Level of initial partial resistance of a tumour. (D) Presence or absence of resistant cell-lines. Point colour-codes indicate the average level of resistance in detected tumours over 3 month intervals (see inset in B). For simplicity, only the median is indicated in B and C for the baseline case (blue line). Lines and shading otherwise as in Figure 2. Unless otherwise stated, parameter values as in Table 1.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Success is defined as tumour non-detection by 50 years. Daily effect of treatment on cellular arrest is assumed to be 0.25%. Unless otherwise stated, parameter values as in Table 1.

We find, counterintuitively, that early-detected tumours are more likely to be resistant under constant treatments than those detected at later times (A, B, and C in Figure 2C). This is because tumours under treatment that by chance obtain resistance early grow faster than those that do not. By the time of detection, non-resistant tumours usually accumulate up to 4 additional drivers on average, while resistant tumours have fewer. For larger values of cost c, an additional non-regularity emerges at σ ≈ 3s (segment DEF in Figure 2B), and is associated with tumours having a majority of cells with maximum numbers of drivers. This region is also characterized by a different transition to complete resistance (cf. Videos 1, 2 for relatively low and high costs of resistance, respectively). For example, at point D, tumours with a majority of non-resistance have less variable detection times than tumours with a majority of resistant cells (points E and F in Figure 2B and corresponding panels in Figure 2C). Treatment levels along the segment DEF result in tumours that are more likely to be resistant as one goes from the centre to the tails of the distribution of detection times. This differs qualitatively from the previous case of a lower cost of resistance, where the tumours are less resistant in the tail of the distribution of detection times (cf segments ABC and DEF in Figure 2B and corresponding panels in Figure 2C).

![Video 1.](https://cdn.elifesciences.org/articles/06266/elife-06266-media1.mp4.jpg)

**Video 1.:** (A) The median (thick line) and 90% confidence intervals (shaded areas with dashed boundaries) for the distribution of detection times. (B) Arbitrary samples of the distribution of detection times and distribution of the mean number of accumulated drivers. The colour-code indicates the average level of resistance in detected tumours over 3 month intervals. Parameters as in Table 1.

![Video 2.](https://cdn.elifesciences.org/articles/06266/elife-06266-media2.mp4.jpg)

**Video 2.:** (A) The median (thick line) and 90% confidence intervals (shaded areas with dashed boundaries) for the distribution of detection times. (B) Arbitrary samples of the distribution of detection times and distribution of the mean number of accumulated drivers. The colour-code indicates the average level of resistance in detected tumours over 3 month intervals. Parameters as in Table 1 except for the cost of resistance c = 0.4%.

The inflection point at σ ≈ 2s in Figure 2A is due to the accumulation of additional drivers within tumours and associated increases in the likelihood that the tumour eventually resists treatment. Since the initial population consists of 106 cells, in the absence of treatment, a mutant cell with one additional driver and associated fitness 2s will appear very rapidly. Such a tumour can be suppressed only if σ > 2s. This is supported by additional numerical experiments where we vary the maximal number of additional driver mutations N: the inflection point σ ≈ 2s disappears when N = 0 (Figure 2—figure supplement 1A). The inflection points at σ = 3s, 4s emerge at treatment levels that effectively suppress sensitive subclones with the most drivers before resistance mutations are obtained (cf Figure 2—figure supplement 1A–C with Figure 2—figure supplement 1D and Video 3). Specifically, the peaked distributions, corresponding to better therapeutic outcomes, tend to disappear when resistant subclones emerge.

![Video 3.](https://cdn.elifesciences.org/articles/06266/elife-06266-media3.mp4.jpg)

**Video 3.:** (A) The median (thick line) and 90% confidence intervals (shaded areas with dashed boundaries) for the distribution of detection times. (B) Arbitrary samples of the distribution of detection times and the distribution of the mean number of accumulated drivers. The colour-code indicates the average level of resistance in detected tumours over 3 month intervals. The resistance mutation is knocked out (v = 0). Otherwise parameters as in Table 1.

The initial cancer cell number M0 affects both the median and distribution of detection times (Figure 2—figure supplement 1B). For large initial tumours, growth is deterministic and exponential. As the initial size is decreased from 106 to 105, stochastic effects are increasingly manifested by greater variability in tumour inhibition and an inflection point observed at the 95th percentile. Moreover, we find that a tumour is likely to be eradicated under a range of constant treatments when M0 = 105 or fewer initial cells; in contrast, a tumour is virtually certain to persist regardless of treatment level for M0 = 107 cells or greater (Figure 2—figure supplement 2A,B). In other words, our model indicates that tumours that are c. 1% the size of most clinically detectable, internal cancers will typically be impossible to eradicate by single molecule chemoprevention when resistance is possible.

Given the mutation rates assumed here, many tumours with 1 million cells will either already contain or rapidly subsequently acquire resistant cells (Iwasa et al., 2006). It is therefore not surprising that the initial fraction of resistant cells in a tumour has little impact on dynamics (Figure 2—figure supplement 1C). In contrast, another measure of success in control (the fraction of persons with tumours that remain undetected after 50 years of growth) improves substantially with lower numbers of initial resistance mutations, particularly at higher treatment levels (Figure 2—figure supplement 2C). This is because the initial phases of treatment have a major impact on the potential for new resistant mutants: should few be initially present or emerge, they will either go stochastically extinct or will not grow to detection levels (1 billion cells) in the 50 year time frame of these numerical experiments.

We conducted further sensitivity analyses by varying accumulation rates u of additional driver mutations. We find that tumours exhibit more or less deterministic growth depending on the initial number of cells M0 and driver mutation rate u whereby the larger the population (Figure 2—figure supplement 1B) or the higher the mutation rate (Appendix 1—figure 4A), the less apparent are stochastic effects. The corresponding analysis is presented in ’Varying mutation rate and initial tumour size‘ in Appendix 1 and Appendix 1—figure 4.

Finally, we considered scenarios where the cost of resistance is dose-dependent and specifically situations of drug addiction (Das Thakur et al., 2013). Numerical studies presented in more detail in ’A simple form of drug addiction for resistant cell-lines‘ in Appendix 1 show that under dose-dependent costs, a drug treatment only applied when the number of non-resistant cells exceeds the number of resistant cells (e.g., a metronomic therapy [Fischer et al., 2015]) leads to slower long-term tumour growth than does a constant therapy.

### Post-diagnostic interventions

We next investigated how a post-diagnostic measure (usually some form of chemotherapy or radiation therapy, but could also involve adjuvants after an initial therapy) affects the probability of treatment success, the distribution of times for tumour relapse, and resistance levels. We assume that a tumour grows from one cell (i = 0, j = 0) and is discovered either at 109 (early) or 1011 (very late) cells, whereupon the primary tumour is removed, leaving a small number (104 or 106) of residual, and/or undetected or inoperable neighbouring micro-metastatic cells, and/or distant metastatic cells. Below, we contrast this with prevention without discriminating the age at which either intervention type commences, whereas in the following section, we consider these as competing alternatives. Figure 3A and Figure 3—figure supplement 1A present the distributions of driver mutations for each scenario. (Recall that in the previous section, we assumed that when a measure commenced, tumours had no additional drivers (i = 0)).

![Figure 3.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig3-v2.jpg)

**Figure 3.:** (A) The distribution of mean sizes of subclones (hatched bars = before removal and solid bars = post removal). (B) The time distribution of cases in which either intervention type fails to control the tumour below the detection threshold after 50 years (thick line = median, filled area with dashed boundaries = 90% CIs) for different constant treatment intensities. (C) The percentage of cases where the tumour consists of less than 100 resistant cells at 4 years after treatment commences (solid lines), and the percentage of cases where tumour size is below the detection threshold 20 years after the measure begins (dashed-and-dotted lines). (D) The mean number of accumulated drivers within a tumour at the time of detection. Parameter values as in Table 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Same as Figure 3, except interventions against 104 cancer cells. (A) The distribution of mean sizes of subclones for different constant treatment intensities (hatched bars = before removal and solid bars = post removal). (B) The time distribution of cases in which either intervention type fails to control the tumour below the detection threshold after 50 years (thick lines = medians, shaded areas with dashed boundaries = 90% CIs). (C) The percentage of cases when a tumour consists of less than 100 resistant cells at 4 years post-resection (solid lines) and the percentage of cases when tumour sizes are below the detection threshold 20 years after the measure commences (dashed-and-dotted lines). (D) The mean number of accumulated drivers within a tumour at the time of detection. Parameter values as in Table 1.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Time to tumour relapse following resection as function of the time it takes for the initial cancer cell to attain 109 cells (i.e., the point at which the tumour is discovered, resected, and treatment begins). Each dot represents a numerical simulation from the yellow distribution in Figure 3B (only 1,000 simulation results out of 106are shown). Four different treatment levels are considered. Black solid line is a simple linear regression, and grey area with dashed boundaries indicates extrapolation of high and low bounds accounting for 95% of observations (prediction interval). The fitted linear regression model gives an intercept of 7.5 years, a slope of 1.6° and R2 of 0.024 in (A), 10.4 years, 2.2° and R2 of 0.017 in (B), 12.9 years, 3.0° and R2 of 0.009 in (C), and 13.1 years, 3.3° and R2 of 0.008 in (D). Parameters as in Table 1.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Time to tumour discovery is generally more predictive of post-diagnostic therapeutic outcome for lower treatment levels. See Figure 3—figure supplement 2 for details.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** The fitted negative exponential regression model y = ae-bx gives a = 13.5 years, b = 0.3 and R2 = 0.696 in (A), 18.95 years, 0.3 and R2 = 0.537 in (B), 23.0 years, 0.29 and R2 = 0.262 in (C), and 23.9 years, 0.3 and R2 = 0.224 in (D). See Figure 3—figure supplement 2 for details.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Time to tumour discovery is more predictive of post-diagnostic therapeutic outcome for lower treatment levels. See Figure 3—figure supplement 4 for details.

First, we examine the case where post-diagnostic resection leaves 106 cells. As suggested by our studies above on prevention, 1 million cells have a high probability of already containing resistant subclones, and deterministic effects dominate subsequent tumour growth dynamics. Comparing the median expectations of years from tumour excision to relapse, early discovery (at 109 cells) yields an additional 3.4 years compared to late discovery (at 1011 cells) at σ = 1.5% (medians for low vs high detection thresholds are 14.8 and 11.4 years, respectively; Figure 3B). Consider the following example: 20 years after resection and commencing treatment, the probability of tumour non-detection (i.e., the tumour is either eradicated or does not reach the detection threshold) is close to zero, regardless of treatment intensity (Figure 3C). Contrast this with cases of prevention starting at the same cancer cell population size (106 cells) but which fail to control the incipient tumour for the 50 years of the simulation: the detection time of these potentially life-threatening tumours is substantially longer than either of the excision cases (median 25.5 years for σ = 1.5%, i.e., 0.3–0.4% potential cell arrest per day), and tumours are managed below the detection threshold after 20 years in more than 80% of cases for any σ > 1.0% (Figure 3C).

Now consider a residual population of 1/100th the previous case, that is, 104 cells. Here, stochastic effects play a more important role in dynamics (Figure 3—figure supplement 1A,B). Due to initial heterogeneity (i.e., the co-occurrence of many subclones), when there are 4 and 5 (5 and 6) additional drivers in the dominant subclones of a residual cancer from an excised tumour of 109 (1011) cells, we observe a double peak at 4s and 5s (5s and 6s) (cf Figure 3—figure supplement 1B). These peaks in variability of outcomes are a result of the stochastic nature of the appearance of the first resistance mutations and of additional driver mutations. Interestingly, the secondary detection times (i.e., when residual or metastatic cells grow to form a new tumour) are more variable for small initial tumours compared to larger ones (cf the median 35.8 years, 90% CIs [17.0, 70.5] years vs 22.4, [13.7, 37.0] years for 109 vs 1011, respectively, with σ = 1.5%). This effect is due to resistance emergence in more aggressive subclones for larger tumours, such that the tumour relapses more deterministically (i.e., with less variability and faster on average). The probability of tumour non-detection after 20 years and the distribution of the mean number of accumulated drivers within tumours are shown in Figure 3—figure supplement 1C,D, respectively (cf with the previous case, shown in Figure 3C,D).

Importantly, for both thresholds of tumour excision, subsequent cancer cell arrest levels beyond approximately σ = 1.5% make little difference in terms of tumour growth (Figure 3B-D, Figure 3—figure supplement 1B-D), since virtually all of the sensitive cells post-excision will be arrested or killed by the measure beyond this level, leaving uncontrollable resistant cells to grow and repopulate the primary tumour site and/or metastases. (Note that this level is above that found in the previous section. This is because drivers accumulate throughout tumour growth in the results given in Figure 3, whereas tumours were assumed to only start accumulating the first drivers after growth from M0 cells in Figure 2 and Figure 2—figure supplements 1, 2). Moreover, we find that for post-diagnostic interventions knowledge about the number of drivers at the time of tumour discovery is a far better predictor of outcome than information about the time from tumour initiation to discovery, and that increases in treatment intensity tend to decrease predictive accuracy (Figure 3—figure supplements 2–5).

### Prevention vs post-diagnostic intervention

The above results consider preventive measures and post-diagnostic interventions as independent rather than alternative approaches. Thus, although prevention delays tumour growth for longer times on average than does post-diagnostic intervention, because prevention is always initiated before diagnosis, when considering the relative benefits and risks of each, the actual time gained by the former relative to the latter in terms of cancer-free life will be less than the differences reported in Figure 3B and Figure 3—figure supplement 1B.

Figure 4 presents a hypothetical comparative scenario of prevention vs post-diagnostic intervention. Prevention may either succeed without recurrence, or should the measure initially fail and a tumour be clinically detected, the patient has a ‘second chance’ whereby the tumour is resected and treatment continued (assumed at the same treatment intensity σ), either to a further relapse (failure) or non-detection (success) (Figure 4A). Compare this scenario with the more standard post-diagnostic resection followed by treatment, which either results in relapse or detection-free life (Figure 4B). These numerical experiments assume the same starting point (time at which the cancer cell population equals M0, and drivers and resistant subclones are present) for each tumour, and because of a ‘second chance’ following initial failure in prevention, are run for a maximum of 50 years after the starting point (same as the numerical studies in the previous section). We also assume, as before, that potential therapeutic resistance mechanisms to all intervention types are identical.

![Figure 4.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig4-v2.jpg)

**Figure 4.:** A tumour is initiated by one cell and grows to size M0 (either 104 or 106 cells in our numerical studies). Prevention (A) arrests tumour growth at intensity σ (daily level = σ/4). Should the tumour grow to 109 cells, it is diagnosed and resected to M = M0 cells and then treated again at intensity σ. Post-diagnostic intervention (B) does not discover the growing tumour until 109 cells (i.e., $\sigma=\sigma^=0$), whereupon it is resected to M = M0 cells and then treated at intensity σ > 0. Either intervention finally ‘fails’ should the tumour attain 109 cells a second time, no later than 50 years after the initial lesion of size M0. Should the tumour be eradicated or not exceed 109 cells by 50 years after the initial lesion, then the intervention is deemed a ‘success’.

Figure 5 presents the comparative outcomes (see also Videos 4, 5). When prevention starts at (or tumour resection misses) relatively large cancer cell populations (1 million cells), only small comparative gains occur from higher cell arrest in terms of outright treatment success (Figure 5A), whereas interventions starting at much smaller cancer cell numbers (10,000) result in considerably greater outright success (Figure 5B). Looking at situations of relapse only for prevention vs post-diagnostic intervention, the former generally results in superior outcomes in terms of delaying tumour growth, particularly for large residual cell populations (cf Figure 5C,D). In contrast, for lower numbers of residual cells, some post-diagnostic resected tumours in the sample will be initially resistance free (cf Figure 5—figure supplement 1A,B). This, together with fewer accumulated drivers in the highest driver subclones, contributes to improved outcomes should relapse occur (Figure 5D) and overall treatment success at sufficiently high treatment intensities (Figure 5A,B,E,F). Importantly, resected tumours in both the prevention (when it initially fails) and post-diagnostic scenarios may contain numerous resistant cells (example of 0.25% daily cellular arrest: Figure 5—figure supplements 2, 3). Prior selection for resistance in initially failed prevention generally results in larger residual resistant cell populations than pre-therapeutic residual populations in post-diagnostic situations (filled bars, cf captions A and B in Figure 5—figure supplements 2, 3), but smaller residual resistant cell populations than treatment failures following post-diagnostic resection (hatched bars, cf captions A and D in Figure 5—figure supplements 2, 3). Note that, as expected, secondary failures are associated with larger percentages of resistant subclones and a shift in the distributions towards more drivers (cf captions C and D in Figure 5—figure supplements 2, 3).

![Figure 5.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig5-v2.jpg)

**Figure 5.:** Tumours are either treated at M0 = 106 cells (left panels) or M0 = 104 cells (right panels). (A, B) Probability of treatment success, defined as the proportion of cases where the tumour remains undetected (either extinct or below 109 cells) by 50 years after the initial lesion of M0 cells. (C, D) Distribution of times to relapse for treatment failures. (E, F) Distribution of detection times for all cases including relapsed tumours and tumours remaining undetected prior to and after 50 years (detection times are assigned to 50 years in the latter case). Parameters as in Table 1. See Figure 3 for details.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Tumours are either treated at M0 = 106cells (A) or M0 = 104cells (B). Red lines and yellow shading = population following resection. Parameter values as in Table 1.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Cases where a tumour is detected and resected following prevention. (B) Cases where a tumour is detected and resected with no prevention. (C) Cases of relapse following resection and secondary treatment to initially failed prevention. (D) Cases of relapse following resection and primary treatment in cases where there was no prevention. Hatched bars indicate cell numbers in the tumour and solid bar numbers after resection and 106 residual or metastatic cells. Daily arresting level assumed to be 0.25%. Parameter values as in Table 1.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Same as Figure 5—figure supplement 2, except M0 is 104 cancer cells.

![Video 4.](https://cdn.elifesciences.org/articles/06266/elife-06266-media4.mp4.jpg)

**Video 4.:** Tumours are treated at M0 = 106 cells. (A) The median (thick line) and 90% confidence intervals (shaded areas with dashed boundaries) for the distribution of times to relapse for treatment failures. (B) and (C) Arbitrary samples of the distribution of detection times for preventive and post-diagnostic interventions, respectively. The colour-code indicates the mean number of accumulated drivers over a period of 1 year. The rectangles on the top of B and on the bottom of C show the fifth and 95th percentiles, the blue circle indicates the median, and the red line is the mean. Parameters as in Table 1.

![Video 5.](https://cdn.elifesciences.org/articles/06266/elife-06266-media5.mp4.jpg)

**Video 5.:** Tumours are treated at M0 = 104 cells. (A) The median (thick line) and 90% confidence intervals (shaded areas with dashed boundaries) for the distribution of times to relapse for treatment failures. (B) and (C) Arbitrary samples of the distribution of detection times for preventive and post-diagnostic interventions, respectively. The colour-code indicates the mean number of accumulated drivers over a period of 1 year. The rectangles at the top of B and the bottom of C shows the fifth and 95th percentiles, the blue circle indicates the median, and the red line is the mean. Parameters as in Table 1.

Figure 5E,F shows the distributions of detection times for all numerical experiments. We see that when both non-relapse (Figure 5A) and relapse (Figure 5C) are taken into account for large cancer cell populations (1 million cells), treating preventively at levels beyond about 0.3% arrest per day increases median delays in detection times due to outright success (i.e., survival beyond 50 years) but has no effect on the lower 95th percentile (Figure 5E). (Although not shown, arrest beyond approximately 0.6% per day does not yield further gains). In contrast, post-diagnostic intervention improves only marginally beyond daily arrest levels of about 0.3% (Figure 5E). Figure 5F shows the corresponding results for smaller cancer cell populations (based on integrating the results in Figure 5B,D), whereby a high median probability of full success is obtained >0.1% and >0.3% daily arrest for prevention and post-diagnostic intervention, respectively (Figure 5F). Thus for both cell population levels, prevention generally results in better outcomes compared to post-diagnostic intervention.

## Discussion

MTD chemotherapies present numerous challenges, a major one being the selection of resistant phenotypes, which are possible precursors for relapse (Gerlinger and Swanton, 2010). We mathematically and numerically investigated how the intensity of an anti-cancer measure, modelled as the arresting effect on a cancer cell population, resulted in success (i.e., either eradication or long-term tumour control) or failure (tumours growing beyond a threshold indicative of a life threatening cancer). Our central result is that beyond low impact thresholds—approximated by the Darwinian fitness of the subclone with the most driver mutations—little additional control is achieved when resistant subclones are present or likely to emerge during the long-term intervention assumed here.

We considered two contrasting scenarios. In the first, people at high risk of contracting a life threatening cancer make life-style changes or receive continuous, chemopreventive therapies, and in the second, more usual situation, a tumour is discovered and removed, and the patient treated with specific cytotoxic or cytostatic chemicals and/or with radiation. We found that, as expected, to achieve a given outcome, prevention requires smaller effects on cancer cell populations of a given size than do post-diagnostic interventions, the latter having smaller probabilities of complete cure and shorter times to tumour relapse. Inversely and importantly, for any given cell arrest level, prevention is, on average, superior to comparable post-diagnostic interventions, even when including cases where prevention initially fails, and resection and additional therapy are needed.

Specifically, based on empirical parameter estimates, we find that maximal long-term control occurs at surprisingly low daily levels of arrest. In the example where interventions target 1 million cancer cells, these levels are approximately 0.6% and 0.3% for preventive and post-diagnostic interventions, respectively. That the level is higher for preventive scenarios is because effective ‘cure’ (i.e., relapse does not occur during the 50 year period assumed in our numerical experiments) is possible, especially at cell arrest levels beyond 0.3%, whereas ‘cure’ is far less probable for post-diagnostic interventions. However, should prevention initially fail and a tumour be diagnosed and resected, any residual or metastatic cells are likely to contain more resistant clones than the corresponding situation for a post-diagnostic tumour. We stress that this latter result is contingent on our assumption that the same mutations (and mechanisms) are responsible for resistance to both preventive and post-diagnostic interventions. Should preventive and post-diagnostic measures differ substantially in their targets (and therefore resistance mechanisms), then evolved resistance to (failed) prevention could be irrelevant to the efficacy of subsequent traditional therapies.

Our results point to what is perhaps an underappreciated challenge in cancer control: low impact interventions risk being unable to control subclones with the most fitness-enhancing drivers, whereas high levels of arrest risk selecting for resistance (Figure 6). Future models should investigate these contingencies more extensively for alternative assumptions and a range of parameterizations for specific cancer types. Below, we discuss challenges to cancer management for both preventive and post-diagnostic scenarios.

![Figure 6.](https://cdn.elifesciences.org/articles/06266/elife-06266-fig6-v2.jpg)

**Figure 6.:** Increasing treatment intensity selects against subclones with increasing numbers of drivers, whereas, regardless of treatment intensity, all resistant subclones with s(i+1) > c increase in number. The solid lines illustrate how selection and the initial number of resistant cells in a treated tumour predict median detection times and associated resistance levels. Median detection times approach a horizontal asymptote at 100% resistance as treatment intensity increases, whereas if the resistant mutation were to be knocked out, then the vertical asymptote at σcrit = qs (where q is the number of drivers in the fastest growing subclone) would be approached instead for sufficiently small tumours. Asymptotes are shown as dashed lines. We illustrate three cases, each with an initial population of 100,000 identical cells (i = 0) and with one of three different initial numbers of resistant cells: 10, 100 or 1,000 (top to bottom lines). Other parameters as in Table 1.

### Preventive interventions

Whereas primary prevention is becoming an increasingly significant approach in reducing risk of certain cancers (e.g., Colditz and Bohlke, 2014), chemopreventive therapies are uncommon, despite empirical support for their effects (William et al., 2009). Several theoretical and in vitro experimental studies indicate that chemoprevention can reduce risks of life threatening cancers. For example, Silva and colleagues (Silva et al., 2012) parameterized computational models to show how low doses of verapamil and 2-deoxyglucose could be administered adaptively to promote longer tumour progression times. These drugs are thought to increase the costs of resistance and the competitive impacts of sensitive cells on resistant cancer cell subpopulations. However, some of the most promising results have come from studies employing non-steroidal anti-inflammatory drugs (NSAIDs), including experiments (Ibrahim-Hashim et al., 2012), investigations of their molecular effects (Galipeau et al., 2007; Kostadinov et al., 2013), and their use (Cuzick et al., 2015). For example, Ibrahim and co-workers (Ibrahim-Hashim et al., 2012) studied the action of NSAIDs and specifically sodium bicarbonate in reducing prostate tumours in male TRAMP mice (i.e., an animal model of transgenic adenocarcinoma of the mouse prostate). They showed that mice commencing the treatment at 4 weeks of age had significantly smaller tumour masses, and that more survived to the end of the experiment than either the controls or those mice commencing the treatment at an older age. Kostadinov et al. (2013) showed how NSAID use in a sample of people with Barrett's oesophagus is associated with reductions in somatic genomic abnormalities and their growth to detectable levels. It is noteworthy that it is not known to what extent reductions in cancer progression under NSAIDs are due to either cytotoxic or cytostatic effects or both. Although we do not explicitly model cytotoxic or cytostatic impacts, therapies curbing net growth rates but maintaining them at or above zero could be interpreted as resulting from the action of either cytotoxic and/or cytostatic processes. In contrast, therapies reducing net growth rates substantially below zero necessarily have a cytotoxic component. Our model, or modifications of it to explicitly include cytotoxic and cytostatic effects, could be used in future research to make predictions about optimal dose and start times to achieve acceptable levels of tumour control (or, e.g., the probability of a given tumour size and heterogeneity level by a given age).

Decisions whether or not to employ specific chemopreventive therapies carry with them the risk of a poorer outcome than would have been the case had another available strategy (or no treatment at all) been adopted (Esserman et al., 2004). This issue is relevant to situations where alterations in life-style, removal or treatment of pre-cancerous lesions, or medications potentially result in unwanted side effects or induce new invasive neoplasms (e.g., Berrington de Gonzalez et al., 2011). Chemopreventive management prior to clinical detection would be most appropriate for individuals with genetic predispositions, familial histories, elevated levels of specific biomarkers, or risk-associated behaviours or life-styles (Hemminki and Li, 2004; Lippman and Lee, 2006; Sutcliffe et al., 2009; William et al., 2009; Hochberg et al., 2013). Importantly, our approach presupposes that the danger a nascent, growing tumour presents is proportional to its size and (implicitly, all else being equal) a person's age. Due caution is necessary in interpreting our results, since studies have argued that metastatic potential rather than tumour size may be a better predictor of future survival (Hynes, 2003; Foulkes et al., 2010; Sethi and Kang, 2011). However, given the expectation that prevention typically confronts smaller, less heterogeneous neoplasms, which are less likely to have resistant clones and to have metastasised (Hochberg et al., 2013; Gerlinger et al., 2014), support our basic conclusion that prevention is generally a superior strategy in terms of cancer-free survival compared to post-diagnostic intervention.

### Post-diagnostic interventions

Over the past decade, several alternative approaches to MTD have been proposed, where the objective is to manage rather than eradicate tumours (e.g., Maley et al., 2004; Komarova and Wodarz, 2005; Gatenby, 2009; Gatenby et al., 2009a, 2009b; Foo and Michor, 2010; Jansen et al., 2015). Tumour management attempts to limit cancer growth, metastasis, and reduce the probability of obtaining resistance mutations through, for example, micro-environmental modification, or competition with non-resistant cancer cell populations or with healthy cells. These approaches usually involve clinically diagnosed cancers: either inoperable tumours or residual or metastatic cancers after tumour excision. In the former situation, tumours are typically large enough in size to contain numerous resistance mutations. In many, if not most, cases, these neoplasms will have metastasized, meaning greater variability both in terms of phenotypes and potential resistance to chemotherapies, and in penetrance of therapeutic molecules to targeted tumour cells (Klein et al., 2002; Byrne et al., 2005). In contrast, the latter situation involves smaller, residual, or metastatic cancer cell populations, composed of high frequencies of resistant variants or dormant cells (Klein et al., 2002). According to our results, both scenarios are likely to involve populations with large numbers of accumulated driver mutations (or, although not considered in our study, fewer driver mutations but each with larger selective effect), which ostensibly contribute to the speed of relapse. Thus, management of clinically detected tumours need not only limit the proliferation and spread of refractory subpopulations but should also aim to control the growth of multi-driver subclones (Figure 5—figure supplements 2, 3). In other words, in addition to actual resistance mutations (j = 1), subclones with q drivers will be effectively resistant to therapeutic interventions if q s ≫ σ (Figure 6).

We therefore suggest that the frequency distribution of driver mutations and the distribution of resistant subclones within a heterogeneous cancer cell population could be used to instruct decisions of the time course of treatment levels, with the aims of curbing tumour growth, metastasis, and resistance. We found that tumours typically achieve several additional driver mutations by the time they reach detection (Figure 3A; Figure 3—figure supplement 1A; Figure 5—figure supplements 2, 3), which approximates certain estimates (Stratton et al., 2009) but falls short of others (Sjoblom et al., 2006).

### Conclusion

Our results indicate that the two most important variables in determining therapeutic outcome are (1) the size of the initial cancer cell population (i.e., when prevention commences and/or post-diagnosis, following resection), (2) associated tumour heterogeneity in terms of accumulated drivers, and the presence of resistance phenotypes. This highlights the importance of biomarkers as accurate indicators of otherwise undetectable malignancies (Roukos et al., 2007), and the accurate assessment of local or distant metastases (Pantel et al., 1999). We suggest that if order-of-magnitude estimates of cell populations and intra-tumour heterogeneity are possible, then low dose, continuous, constant approaches could be established that lower and possibly minimize risks of the emergence of future, life-threatening cancers. According to our model, such options will generally be superior to more aggressive chemotherapies if therapeutic resistance is a risk factor.

The framework proposed here is sufficiently general to portray major events in different types of cancer with emphasis on solid tumours. However, some aspects of cancerous tumour growth are considered only implicitly, and further research is required to formulate more realistic models to include, for example, spatial aspects of tumour growth (Orlando et al., 2013), competition/cooperation between different subclones (Korolev et al., 2014), combinational (multidrug) resistance (Gillet and Gottesman, 2010; Bozic et al., 2013), drug-addiction, observed for example in certain melanomas (Das Thakur et al., 2013), or advantageous resistant mutations, observed in some leukemias (Michor et al., 2005). Moreover, future studies should investigate alternatives to the traditional post-diagnostic therapeutic scenarios considered here (e.g., molecularly targeted therapies [Yap, 2015]). Our study nevertheless predicts that the main hurdle to post-diagnostic MTD interventions remains resistant subclones, since beyond minimal impacts on the order of 0.3% per day for the larger of the two residual or metastatic cell populations simulated here (which are still very small by clinical diagnostic standards—c 1 mm3), increased therapeutic intensity selects disproportionally for resistance and has negligible benefits in terms of delaying life-threatening cancers.
