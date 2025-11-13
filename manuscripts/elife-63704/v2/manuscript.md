# Quantifying the impact of quarantine duration on COVID-19 transmission

## Authors

- Peter Ashcroft<sup>1</sup> ([ORCID: 0000-0003-4067-7692](https://orcid.org/0000-0003-4067-7692)) †
- Sonja Lehtinen<sup>1</sup> ([ORCID: 0000-0002-4236-828X](https://orcid.org/0000-0002-4236-828X))
- Daniel C Angst<sup>1</sup> ([ORCID: 0000-0002-6512-4595](https://orcid.org/0000-0002-6512-4595))
- Nicola Low<sup>2</sup> ([ORCID: 0000-0003-4817-8986](https://orcid.org/0000-0003-4817-8986))
- Sebastian Bonhoeffer<sup>1</sup> ([ORCID: 0000-0001-8052-3925](https://orcid.org/0000-0001-8052-3925)) †

### Affiliations

1. Institute of Integrative Biology, ETH Zürich Zürich Switzerland
2. Institute of Social and Preventive Medicine, University of Bern Bern Switzerland

† Corresponding author

## Abstract

The large number of individuals placed into quarantine because of possible severe acute respiratory syndrome coronavirus 2 (SARS CoV-2) exposure has high societal and economic costs. There is ongoing debate about the appropriate duration of quarantine, particularly since the fraction of individuals who eventually test positive is perceived as being low. We use empirically determined distributions of incubation period, infectivity, and generation time to quantify how the duration of quarantine affects onward transmission from traced contacts of confirmed SARS-CoV-2 cases and from returning travellers. We also consider the roles of testing followed by release if negative (test-and-release), reinforced hygiene, adherence, and symptoms in calculating quarantine efficacy. We show that there are quarantine strategies based on a test-and-release protocol that, from an epidemiological viewpoint, perform almost as well as a 10-day quarantine, but with fewer person-days spent in quarantine. The findings apply to both travellers and contacts, but the specifics depend on the context.

## Introduction

Quarantining individuals with high risk of recent infection is one of the pillars of the non-pharmaceutical interventions to control the ongoing severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) pandemic (Kucharski et al., 2020). Owing to the large fraction of transmission of SARS-CoV-2 that is pre-symptomatic or asymptomatic (Ashcroft et al., 2020; Buitrago-Garcia et al., 2020; Ferretti et al., 2020b; He et al., 2020), quarantine can prevent a substantial fraction of onward transmission that would not be detected otherwise. In mathematical modelling studies, it was estimated that thermal screening at airports would allow more than 50% of infected travellers to enter the general population (Quilty et al., 2020; Gostic et al., 2020), which could have been prevented by mandatory quarantine. Quarantine is also a fundamental part of the test–trace–isolate–quarantine (TTIQ) intervention strategy to break chains of transmission within a community (Salathé et al., 2020). With the high or increasing case numbers that are observed in many places around the globe, however, more and more people are being placed into quarantine.

There is ongoing public debate about the appropriateness of quarantine and its duration. Quarantine lowers onward transmission in two ways: first, preventing transmission prior to symptom onset (with the assumption that symptomatic individuals will isolate) and decreasing overall transmission from persistently asymptomatic individuals. The appropriate length of quarantine thus depends on both incubation period and the temporal profile of infectiousness. In theory, quarantine periods could be avoided altogether through widespread and regular testing programmes, but the low sensitivity of reverse transcriptase PCR (RT-PCR) tests, particularly in early infection (Kucirka et al., 2020), as well as limitations on testing capacity in most countries preclude this approach. Quarantine has high economic, societal, and psychological costs (Nicola et al., 2020; Brooks et al., 2020). It restricts individual freedoms (Parmet and Sinha, 2020), although the level of restriction imposed is generally judged to be proportionate, given the severity of coronavirus disease 2019 (COVID-19). The low number of individuals placed in quarantine that turn out to be infected is another argument that is given against quarantine.

Individuals are generally placed into quarantine for one of two reasons: either they have been identified as a recent close contact of a confirmed SARS-CoV-2 case by contact tracing, or they have returned from recent travel to an area with community transmission that has been assessed to pose significant epidemiological risk (WHO, 2020). These groups of quarantined individuals differ in two important ways: compared with traced contacts, travel returners may have lower probability of being infected and have less precise information about the likely time of exposure. This raises the question whether the duration of quarantine should be the same for these two groups of individuals.

To our knowledge, there are no published analyses of surveillance data that directly assess the impact of duration of quarantine on SARS-CoV-2 transmission (Nussbaumer-Streit et al., 2020). In this study, we present a mathematical model that allows quantification of the effects of changing quarantine duration. We use the distributions of incubation time (time from infection to onset of symptoms), infectivity (infectiousness as a function of days since symptom onset), and generation time (difference of timepoints of infection between infector and infectee). These distributions have been estimated by Ferretti et al., 2020b, combining multiple empirical studies of documented SARS-CoV-2 transmission pairs (Ferretti et al., 2020a; Xia et al., 2020; Cheng et al., 2020; He et al., 2020).

Using the model, we explore the effect of duration of quarantine for both traced contacts of confirmed SARS-CoV-2 cases and for returning travellers on the fraction of prevented onward transmission. We assess the effects of test-and-release strategies and the time delay between test and result. These considerations are particularly important given that multiple testing has been shown to be of little benefit (Clifford, 2020). We also address the role of pre-symptomatic patients becoming symptomatic and therefore being isolated independent of quarantine. Furthermore, as one of the arguments for shortening the duration of quarantine is to increase the number of people complying with the recommendation, we investigate by how much adherence needs to increase to offset the increased transmission due to earlier release from quarantine. Finally, we assess the role of reinforced individual-level prevention measures, such as mask wearing, for those released early from quarantine.

Making policy decisions about the duration of quarantine fundamentally requires specifying how the effectiveness of quarantine relates to its costs. The effectiveness can be measured in terms of the overall reduction of transmission, while economic, societal, and individual costs are likely a function of the number of days spent in quarantine. In addition to the epidemiological outcome, which considers only the reduction in transmission, we also present results based on the ratio of transmission prevented to the average number of days spent in quarantine.

## Results

### Model description

In the absence of quarantine, individuals that are infected with SARS-CoV-2 can infect further individuals in the population. In the model, the timing of onward transmission from an infected individual is determined by the generation time distribution, which describes the time interval between the infection of an infector and infectee (see Figure 1—figure supplement 1). To quantify how much transmission is prevented by quarantining individuals who have been infected with SARS-CoV-2, we need to know the time at which the individual was exposed ($t_{_}⁢E$), as well as when they enter ($t_{_}⁢Q$) and are released from ($t_{_}⁢R$) quarantine. The fraction of transmission that is prevented by quarantine is then the total transmission probability (i.e. the area under the curve) that lies between $t_{_}⁢Q$ and $t_{_}⁢R$ (Figure 1). We refer to this fraction of prevented transmission as quarantine efficacy and is defined in Equation (1) in 'Materials and methods'. Unless otherwise stated, we assume that adherence to quarantine is 100%.

![Figure 1.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig1-v2.jpg)

**Figure 1.:** Here the y-axis represents the probability of transmission. These infectivity curves are a schematic representation of the generation time distribution shown in Figure 1—figure supplement 1. (A) Traced contacts are exposed to an infector at a known time $t_{_}⁢E=0$ and then enter quarantine at time $t_{_}⁢Q$. Some transmission can occur prior to quarantine. Under the standard quarantine protocol, the contact is quarantined until time $t_{_}⁢R$, and no transmission is assumed to occur during this time. The area under the infectivity curve between $t_{_}⁢Q$ and $t_{_}⁢R$ (blue) is the fraction of transmission that is prevented by quarantine. Transmission can occur after the individual leaves quarantine. Under the test-and-release protocol, quarantined individuals are tested at time $t_{_}⁢T$ and released at time $t_{_}⁢R$ if they receive a negative test result. Otherwise the individual is isolated until they are no longer infectious. The probability that an infected individual returns a false-negative test result, and therefore is prematurely released, depends on the timing of the test relative to infection ($t_{_}⁢T-t_{_}⁢E$) (Kucirka et al., 2020). (B) For returning travellers, the time of exposure $t_{_}⁢E$ is unknown and we assume that infection could have occurred on any day of the trip. The travellers enter quarantine immediately upon return at time $t_{_}⁢Q=0$, and then leave quarantine at time $t_{_}⁢R$ under the standard quarantine protocol. Test-and-release quarantine proceeds as in panel A.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) The timeline of infection for an infector–infectee transmission pair. The generation time is defined as the time interval between subsequent infections ($t_{_}⁢2-t_{_}⁢1$), while the serial interval is defined as the time between symptoms onsets in this transmission pair ($t_{_}⁢S_{_}⁢2-t_{_}⁢S_{_}⁢1$). The incubation period describes the time between infection and symptom onset in a single individual (e.g. $t_{_}⁢S_{_}⁢1-t_{_}⁢1$). (B) The generation time distribution follows a Weibull distribution and is inferred from the serial interval distribution (Ferretti et al., 2020b). (C) The infectivity profile (describing the time between symptom onset in the infector and infection of the infectee) follows a shifted Student’s t-distribution and is also inferred from the serial interval distribution (Ferretti et al., 2020b). (D) The distribution of incubation times follows a meta-distribution constructed from the average of seven reported log-normal distributions (Bi et al., 2020; Jiang et al., 2020; Lauer et al., 2020; Li et al., 2020; Linton et al., 2020; Ma et al., 2020; Zhang et al., 2020), as described in Ferretti et al., 2020b.

Under the standard quarantine strategy, all potentially exposed individuals are quarantined for the same duration. An alternative approach is the test-and-release strategy, which uses virological testing during quarantine to release individuals with a negative test result earlier. Individuals with a positive test result are isolated until they are no longer infectious. The timing of the test ($t_{_}⁢T$) is important due to the substantial false-negative rate of the RT-PCR test in the early stages of infection (Kucirka et al., 2020). A false-negative test result would release an infected individual into the community prematurely, leading to further transmission (Figure 1A). In this case, quarantine efficacy is defined as the expected fraction of transmission that is prevented by quarantine across false-negative and positive testing individuals, as defined in Equation (2) in 'Materials and methods'.

As well as the epidemiological benefit of quarantine (i.e. the fraction of transmission prevented by quarantining an infected individual), we can also quantify the economic and societal costs in terms of the expected number of person-days spent in quarantine. We can then define the utility of a quarantine strategy as the ratio between the quarantine efficacy and the average time spent in quarantine, that is, the transmission prevented per day spent in quarantine, as defined in Equation (4) in 'Materials and methods'. This utility measure is dependent on the fraction of individuals in quarantine that are infected. This definition of utility should be considered as an example of such a utility function, but this may not be the best way to quantify quarantine utility.

Details of the calculations used can be found in 'Materials and methods'. Further extensions to the model, including the role of reinforced hygiene measures, asymptomatic infections, and adherence to quarantine, are described in Appendix 1.

### Quarantining traced contacts of confirmed SARS-CoV-2 cases

Traced contacts have a known (last) time of exposure to a confirmed case. There is usually a delay between this exposure time and the start of quarantine. Under the standard quarantine protocol, traced contacts are released from quarantine once a number of days have passed after the last exposure time. In Switzerland, for example, quarantine lasts until 10 days after the last exposure.

Any shortening of a traced contact’s quarantine duration will lead to an increase in transmission from that individual if they are infected, but the degree of increase depends on the extent of the shortening. The expected onward transmission that is prevented by quarantine shows the diminishing return of increasing the quarantine duration (black line in Figure 2A). Increasing quarantine duration beyond 10 days shows almost no additional benefit (Figure 2—figure supplement 1A): the standard quarantine protocol (here with a 3-day delay between exposure and the start of quarantine) can maximally prevent 90.8% [95% CI: 79.6%,97.6%] of onward transmission from an infected traced contact, while release on day 10 prevents 90.1% [CI: 76.0%,97.5%].

![Figure 2.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig2-v2.jpg)

**Figure 2.:** (A) The fraction of transmission that is prevented by quarantining an infected contact. Quarantine begins at time $t_{_}⁢Q=3$ after exposure at time $t_{_}⁢E=0$, that is, there is a 3-day delay between exposure and the start of quarantine. Under the standard quarantine protocol (black), individuals are released without being tested [Equation (1)]. The test-and-release protocol (colours) requires a negative test result before early release, otherwise individuals remain isolated until they are no longer infectious (day 10) [Equation (2)]. Colour intensity represents the delay between test and release (from 0 to 3 days). The grey line represents the maximum attainable prevention by increasing the time of release while keeping $t_{_}⁢Q=3$ fixed. (B) The relative utility of the quarantine scenarios in A compared to the standard protocol 10-day quarantine [Equation (6)]. Utility is defined as the fraction of transmission prevented per day spent in quarantine. The grey line represents equal utilities (relative utility of 1). We assume that the fraction of individuals in quarantine that are infected is 10%, and that there are no false-positive test results. Error bars reflect the uncertainty in the generation time distribution.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) The fraction of transmission that is prevented by quarantining an infected contact [Equation (1)]. We fix the time of exposure to $t_{_}⁢E=0$, and quarantine begins after a delay of 0–4 days (colour). (B) The relative utility of different quarantine durations compared to release on day 10 [Equation (5)]. Error bars reflect the uncertainty in the generation time distribution.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) The fraction of transmission that is prevented by quarantining an infected contact and enforcing strict hygiene measures after release (see 'Appendix 1: Reinforced prevention measures after early release' for details). The scenarios are the same as in Figure 2 (i.e. exposure at time $t_{_}⁢E=0$ and quarantine entry at time $t_{_}⁢Q=3$), but we reduce post-quarantine transmission by $r=50%$ until day 10, after which further transmission is unlikely. The grey line represents the maximum attainable prevention by increasing release time, but keeping $t_{_}⁢Q=3$ fixed. (B) The relative utility of the quarantine and hygiene scenarios in panel A compared to the standard protocol 10-day quarantine [Equation 6]. The grey line represents equal utilities (relative utility of 1). We assume that the fraction of individuals in quarantine that are infected is $s=10%$, and that there are no false-positive test results. Error bars reflect the uncertainty in the generation time distribution.

The maximum attainable prevention also applies to the test-and-release strategy: the onward transmission prevented under a test-and-release strategy will always be below this level (coloured lines in Figure 2A). This is because of the chance of prematurely releasing an infectious individual who received a false-negative test result. On the other hand, it is always better to test a person prior to release from quarantine so that individuals with asymptomatic and pre-symptomatic infections can be detected and prevented from being released. Hence, these scenarios provide upper and lower bounds for the efficacy of the test-and-release strategy. The fraction of transmission that is prevented increases if we test later in quarantine because we not only increase the duration of quarantine but also reduce the false-negative probability.

The delay between testing and release from quarantine can have a substantial effect on the efficacy. Current laboratory-based RT-PCR tests have a typical turnaround of 24–48 hr (Quilty et al., 2021). This delay is primarily operational, and so could be reduced by increasing test throughput. There are also rapid antigen-detection tests, which can provide same-day results, but with lower sensitivity and specificity than RT-PCR tests (Guglielmi, 2020). Here we assume that tests have the same sensitivity and specificity regardless of the delay to result. Compared to a test with 2-day delay until result, we observe that using a rapid test with same-day release can reduce the quarantine duration of individuals with a negative test result by 1 day while maintaining the same efficacy (Figure 2A): the extra accuracy gained by waiting one extra day until testing balances the increased transmission caused by reducing the duration. For example, a rapid test on day 6 has roughly the same efficacy (80.5% [CI: 67.9%,88.7%]) as testing on day 5 and releasing on day 7 (82.3% [CI: 68.2%,93.4%]) while shortening the quarantine duration of individuals with a negative test result from 7 to 6 days.

In Figure 2 we have assumed a fixed delay of 3 days between exposure and the start of quarantine. Shortening this delay increases the maximum efficacy of quarantine because pre-quarantine transmission is reduced (Figure 2—figure supplement 1A). If the duration of quarantine is longer than 10 days, then little can be gained in terms of prevention by quarantining for longer, but reducing the delay between exposure and quarantine does lead to increased efficacy.

Note that we have assumed that the contact was infected at the last time of exposure. If there have been multiple contacts between them and the index case, then transmission may have occurred earlier and we would overestimate the efficacy of quarantine.

For the standard quarantine strategy, the duration of quarantine is independent of whether individuals in quarantine are infected. Therefore, the utility of the standard quarantine strategy (i.e. the ratio of efficacy to duration) is directly proportional to the fraction of individuals in quarantine that are infected. By comparing two different standard quarantine strategies through their relative utility (i.e. the ratio of the utilities), we can eliminate the dependence on the fraction of infecteds in quarantine (see 'Materials and methods'). Therefore, the argument that we should shorten quarantine because of the low probability of quarantined individuals being infected is misguided in this situation. By calculating the relative utility for the standard quarantine strategy compared to the baseline 10-day quarantine, we observe that there is a quarantine strategy (release after 7 days) which maximises the ratio between the fraction of transmission prevented and the number of days spent in quarantine (black line in Figure 2B). The optimal strategy lies between 6 and 8 days if we vary the delay between exposure and the start of quarantine (Figure 2—figure supplement 1B).

Under the test-and-release quarantine protocol, the average time spent in quarantine is dependent on the fraction of infecteds in quarantine; only the infected individuals can test positive and face a longer period of isolation (i.e. we assume there are no false-positive test results). Hence the utility of the test-and-release strategy, as well as the relative utility of test-and-release compared to the standard quarantine protocol, is dependent on the fraction of individuals in quarantine that are infected. In Figure 2B, we fix the fraction of infecteds in quarantine to 10%. By calculating the relative utility for the test-and-release quarantine strategies shown in Figure 2A compared to the baseline 10-day quarantine, we see that testing-and-releasing before day 10 always increases the utility (Figure 2B). Testing on day 5 and releasing test-negative individuals on day 7 has a relative utility of 1.53 [CI: 1.45,1.62] compared to a standard 10-day quarantine. Reducing the delay between test and result leads to a corresponding increase in utility: a rapid test (zero delay between test and result) on day 6 has a relative utility of 1.90 [CI: 1.83,1.98] for an almost equivalent efficacy.

In Figure 2, we have made the following assumptions: (i) individuals released from quarantine have – in the post-quarantine phase – the same transmission probability as individuals who were not quarantined; (ii) adherence to quarantine is 100%; and (iii) the transmission prevented by quarantine for cases who develop symptoms is attributed to quarantine. We now relax these assumptions to assess their impact on quarantine efficacy.

Reinforced prevention measures post-quarantine, where individuals who are released from quarantine must adhere to strict hygiene and social distancing protocols until 10 days after exposure have passed, can reduce post-quarantine transmission. Considering a 50% reduction of post-quarantine transmission leads to large increases in both efficacy and utility for early testing strategies, but with diminishing returns as the release date is increased towards day 10 (Figure 2—figure supplement 2; see 'Appendix 1: Reinforced prevention measures after early release'). Note that we assume no contribution to the number of days spent in quarantine in the utility function due to mask wearing and social distancing in the post-release phase.

Adherence to quarantine is unlikely to be 100% and could depend on the proposed duration of quarantine. For simplicity we treat adherence to quarantine as a binary variable: a fraction of individuals adhere to quarantine completely for the proposed duration, while the remaining fraction do not undergo any quarantine. We now ask: by how much would the fraction of those who adhere to quarantine have to increase to maintain the efficacy of quarantine if the duration is shortened? In the absence of testing during quarantine, shortening from 10 to 5 days would require almost three times as many individuals to adhere to the quarantine guidelines in order to maintain the same overall efficacy (relative adherence 2.90 [CI: 2.15,4.36]; black line in Figure 3A). This threefold increase is not possible if adherence to the 10-day strategy is already above 33% as the maximum adherence cannot exceed 100%; the required increase in adherence grows rapidly as quarantine is shortened and soon becomes infeasible. Hence the argument of shortening quarantine to increase adherence is of limited use. Shortening to 7 days (without testing) may be effective provided that adherence can increase by 30% (relative adherence 1.30 [CI: 1.08,1.55]). Under the test-and-release strategy, however, the efficacy of the standard 10-day quarantine can be matched with release on day 5 or 6 if adherence is also increased by 30%. Releasing earlier than day 5 would seemingly be infeasible given the sharp increase in adherence required.

![Figure 3.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig3-v2.jpg)

**Figure 3.:** (A) The fold-change in adherence to a new quarantine strategy that is required to maintain efficacy of the baseline 10-day standard strategy. Quarantine strategies are the same as in Figure 2 (standard = black, test-and-release = colours). The grey line represents equal adherence (relative adherence of 1). (B) The impact of symptomatic cases on the fraction of total onward transmission per infected traced contact that is prevented by standard (no test) quarantine [Equation (A9)]. We assume that symptomatic individuals will immediately self-isolate at symptom onset. The time of symptom onset is determined by the incubation period distribution (see Figure 1—figure supplement 1D). The curve for 100% asymptomatic cases corresponds to the black curve in Figure 2A. As in Figure 2, we fix the time of exposure at $t_{_}⁢E=0$ and the time of entering quarantine at $t_{_}⁢Q=3$ days. Error bars reflect the uncertainty in the generation time distribution.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The y-axis is the fraction of total onward transmission per infected traced contact that is prevented by standard (no test) quarantine [Equation (A9)]. Each panel corresponds to a different delay between symptom onset and self-isolation in symptomatic individuals. The left-most panel (zero delay) corresponds to Figure 3B. The time of symptom onset is determined by the incubation period distribution (see Figure 1—figure supplement 1D). As in Figures 2 and 3, we fix the time of exposure at $t_{_}⁢E=0$ and the time of entering quarantine at $t_{_}⁢Q=3$ days. Error bars reflect the uncertainty in the generation time distribution.

As a final consideration, we note that our quantification of the fraction of transmission prevented by quarantine is more relevant to individuals with persistently asymptomatic SARS-CoV-2 infection than to those who develop symptoms during quarantine and are subsequently isolated. If symptomatic cases go into isolation once symptoms appear, then quarantine has no further impact on transmission after symptom onset as these cases would anyway be isolated. To account for this, we can modify the model such that cases are removed from the infectious pool upon symptom onset (see Appendix 1). For example, in a fully asymptomatic population a 10-day quarantine can prevent 90.1% [CI: 76.0%,97.5%] of transmission. However, if 25% of cases are asymptomatic, then only 50.8% [CI: 42.8%,56.5%] of transmission is prevented by quarantine, while 39.3% is prevented by the self-isolation of symptomatic cases (Figure 3B). We assume that self-isolation occurs immediately after symptom onset, but any delay between symptom onset and self-isolation would mean that more transmission is prevented by quarantine (Figure 3—figure supplement 1). The fraction of transmission prevented by quarantine is an increasing function of the fraction of asymptomatic cases (Figure 3B). This means that we likely overestimate the efficacy of quarantine as we are also counting transmission that could be prevented by isolation following symptom onset. Furthermore, we have assumed that the false-negative rate is the same between symptomatic and asymptomatic cases. If the test is less sensitive (higher false-negative probability) for asymptomatic cases, then quarantine efficacy would be further reduced.

### Quarantining returning travellers

The rules for whether travellers returning from abroad are quarantined are frequently changed according to the epidemiological scenario in the travel destination and/or in the home country. A high risk of infection while abroad due to high prevalence, or the possibility of returning with a new virological variant, can lead to the imposition or reinstatement of quarantine measures (Russell et al., 2021). Countries that have already eliminated the infection may be even stricter in their quarantine approach to prevent new community-transmission clusters from being seeded. Here we do not discuss these scenarios or the concept of relative risk, we simply quantify how effective quarantine strategies would be at preventing transmission if the returning traveller was infected while abroad. Should quarantine rules be instated or modified, these results can help determine the optimal quarantine duration and/or testing strategy.

The timing of infection of a traveller during a trip abroad is generally unknown. We assume that infection could have happened on each day of the trip with equal probability. Quarantine begins immediately upon return, which we refer to as day 0, and lasts for a number of days (e.g. currently 10 days in Switzerland) from this timepoint (Figure 1B). We consider the fraction of local transmission that is prevented by quarantine. That is, the fraction of the transmission that could occur in the local country that is prevented by quarantine [Equation (8)]. For a 7-day trip, as in Figure 4, the maximum transmission that could occur in the local country is 73.3% [CI: 65.7%,80.3%]. The remaining infectivity potential was already used up before arrival.

![Figure 4.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig4-v2.jpg)

**Figure 4.:** (A) The fraction of local transmission that is prevented by quarantining an infected traveller returning from a 7-day trip. Quarantine begins upon return at time $t_{_}⁢Q=0$, and we assume that exposure could have occurred at any time during the trip, that is, $-7\leqt_{_}⁢E\leq0$. Under the standard quarantine protocol (black), individuals are released without being tested [Equation (9)]. The test-and-release protocol (colours) requires a negative test result before early release, otherwise individuals remain isolated until they are no longer infectious (day 10). Colour intensity represents the delay between test and release (from 0 to 3 days). While extended quarantine can prevent 100% of local transmission (grey line), this represents 73.3% [CI: 65.7%,80.3%] of the total transmission potential (see Figure 4—figure supplement 1A). The remaining transmission occurred before arrival. (B) The relative utility of the quarantine scenarios in A compared to the standard protocol 10-day quarantine [Equation 6]. Utility is defined as the local fraction of transmission that is prevented per day spent in quarantine. The grey line represents equal utilities (relative utility of 1). We assume that the fraction of individuals in quarantine that are infected is 10%, and that there are no false-positive test results. Error bars reflect the uncertainty in the generation time distribution.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) The fraction of total transmission that is prevented by quarantining an infected traveller [Equation (7)]. (B) The relative utility of the different quarantine durations in A compared to release on day 10, based on the total fraction of transmission prevented. (C) The fraction of local transmission that is prevented by quarantining an infected traveller [Equation (9)]. (D) The relative utility of the different quarantine durations in C compared to release on day 10, based on the local fraction of transmission prevented. Colours represent the duration of travel y, and we assume that infection can occur with equal probability on each day $t_{_}⁢E$ which satisfies $-y\leqt_{_}⁢E\leq0$. Quarantine begins at time $t_{_}⁢Q=0$, which is the time of arrival. Error bars reflect the uncertainty in the generation time distribution.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) The fraction of local transmission that is prevented by quarantining an infected traveller and enforcing strict hygiene measures after release (see 'Appendix 1: Reinforced prevention measures after early release' for details). The scenarios are the same as in Figure 4 (i.e. exposure occurs with equal probability between day –7 and return at day 0, $-y\leqt_{_}⁢E\leq0$, and quarantine starts at time $t_{_}⁢Q=0$), but we reduce post-quarantine transmission by $r=50%$ until day 10, after which further transmission is unlikely. (B) The relative utility of the quarantine and hygiene scenarios in A compared to the standard protocol 10-day quarantine [Equation 6]. We assume that the fraction of individuals in quarantine that are infected is 10%, and that there are no false-positive test results. Error bars reflect the uncertainty in the generation time distribution.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/63704/elife-63704-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) The fold-change in adherence to a new quarantine strategy that is required to maintain efficacy (local fraction of transmission prevented) of the baseline 10-day standard strategy. Quarantine strategies are the same as in Figure 4 (standard = black, test-and-release = colours). The grey line represents equal adherence (relative adherence of 1). (B) The impact of symptomatic cases on the fraction of local transmission per infected traveller that is prevented by standard (no test) quarantine [Equation (A9)]. We assume that symptomatic individuals will immediately self-isolate at symptom onset. The time of symptom onset is determined by the incubation period distribution (see Figure 1—figure supplement 1D). The curve for $a=100%$ corresponds to the black curve in Figure 4A. For both panels, as in Figure 4, we fix the trip duration to 7 days and assume exposure can occur at any time $-y\leqt_{_}⁢E\leq0$. Quarantine begins at time $t_{_}⁢Q=0$. Error bars reflect the uncertainty in the generation time distribution.

A standard (no test) 10-day quarantine will prevent 99.9% [CI: 98.0%,100.0%] of local transmission if the individual was infected during a 7-day trip (Figure 4A). There is little benefit to gain by increasing the duration of quarantine beyond 10 days. On the other hand, standard quarantine efficacy decreases quickly as the duration is shortened.

The test-and-release strategy can improve the efficacy of shorter-duration quarantines. Testing on day 5 and releasing on day 7 (to account for test processing delays) performs similarly to 10-day quarantine, preventing 98.5% [CI: 95.5%,99.6%] of local transmission (Figure 4A). Testing and releasing on day 6 (i.e. no delay between test and result) still prevents 97.8% [CI: 94.4%,99.0%] of local transmission. Hence, if the rapid test has the same sensitivity and specificity as the laboratory-based RT-PCR test, then the duration of quarantine of individuals with a negative test result can be shortened by 1 day with minimal loss in efficacy compared to a test with a 48 hr turnaround.

The timing of the test can have a significant impact on prevented transmission; late testing reduces the false-negative probability but increases the stay in quarantine. An important consequence of this is that testing on arrival is a poor strategy for limiting transmission: testing and releasing on day 0 would prevent only 35.2% [CI: 35.1%,35.3%] of local transmission, while testing on arrival and releasing after 2 days prevents only 54.1% [CI: 49.5%,59.4%]. As was the case for the traced contacts, the fraction of local transmission prevented by standard quarantine bounds the efficacy of the test-and-release quarantine strategy from below (Figure 4A).

We again measure the utility of quarantine by calculating the efficacy (local transmission prevented across all individuals in quarantine, assuming 100% adherence) per day spent in quarantine, and then comparing these utilities for different quarantine strategies to the utility of the standard 10-day quarantine through the relative utility (Figure 4B).

In the absence of testing, the duration of quarantine, and hence the relative utility, is independent of the fraction of individuals in quarantine that are infected. For travellers returning from a 7-day trip, the relative utility is a decreasing function of quarantine duration (black line in Figure 4B). The maximum utility strategy would then be to shorten quarantine as much as possible.

As was the case for traced contacts, under the test-and-release quarantine protocol the average time spent in quarantine, the utility, and the relative utility compared to the standard 10-day quarantine will depend on the fraction of individuals in quarantine that are infected. This fraction may change depending on disease prevalence at the travel destination and the duration of travel. For example, the infected fraction of travellers returning from a long stay in a high-risk country is likely to be higher than the infected fraction of travellers returning from a short stay to a low-risk country. In Figure 4B, we keep this fraction fixed at 10%. Early testing greatly reduces the average duration of quarantine and hence leads to increased utility despite the low fraction of transmission that is prevented (coloured lines in Figure 4B).

The average quarantine duration increases linearly with the fraction of infecteds in quarantine [Equation (3) in 'Materials and methods']. The ratio of quarantine efficacy to the average quarantine duration will also increase, such that quarantine is of higher utility if the fraction of infecteds is higher. However, the relative utility of test-and-release quarantine compared to the standard 10-day protocol will decrease and approach 1 as the fraction of infecteds increases. Hence, if the disease prevalence among those returning from travel abroad is high, then test-and-release may not bring substantial benefits over the standard 10-day protocol.

Our assumption that infection occurs with uniform probability across each day of a trip leads to some interesting results. Returning travellers that have been infected on a short journey will have, on average, used up less of their infectivity potential by the time they return than a traveller who was infected on a long journey. Hence, the total transmission that can be prevented by a long quarantine period (e.g. 10 days) upon arrival is greater for short trips (Figure 4—figure supplement 1A). When considering the fraction of local transmission that can be prevented by quarantine, then shorter quarantine durations have a greater impact on long than short trips (Figure 4—figure supplement 1C). Again, this is because, on average, the traveller on a long trip would have been exposed earlier and they will be infectious for a shorter time period after arrival.

If an individual traveller is to be quarantined, then the optimum duration of quarantine, based on our metric of utility, would depend on the duration of their travel, with shorter journeys requiring longer quarantine (Figure 4—figure supplement 1B, D). This might be counterintuitive because individuals who have been on longer journeys to high-risk countries have a higher probability of being infected. The absolute utility (transmission prevented by quarantine across all individuals in quarantine divided by the average quarantine duration) of quarantining such individuals could indeed be higher than for individuals returning from shorter journeys. However, here, we are not considering the question of whether to quarantine or not, but we are assuming that the individual is quarantined and are trying to optimise the duration of quarantine in response to the expected infection dynamics.

We observe an almost-linear response between quarantine duration and the relative utility of the standard (no test) quarantine: for every day that quarantine is shortened, we see the same additive increase in relative utility (black line in Figure 4B). This almost-linear response is coincidental to the 7-day trip duration: longer or shorter trips show non-linear responses (Figure 4—figure supplement 1D). Trips shorter than 7 days have a maximum relative utility of between 4 and 7 days, while trips longer than 7 days have maximum utility for maximally shortened quarantine durations.

Enforcing additional hygiene and social distancing guidelines post-quarantine can increase both efficacy and utility, but with diminishing returns as the release date is increased (Figure 4—figure supplement 2).

As discussed for traced contacts, the loss of efficacy due to shortening quarantine could be offset by increasing quarantine adherence. Shortening from 10 to 5 days would require adherence to increase by 20% (relative adherence 1.20 [CI: 1.12,1.35]) in order to maintain the same overall efficacy (Figure 4—figure supplement 3A). With test-and-release this required increase in adherence is even smaller. We note that the change in adherence required to balance a change in efficacy for shortened quarantine durations is dependent on the travel duration, with short travel durations requiring a greater increase in adherence compared with longer travel durations.

## Discussion

Quarantine is one of the most important measures in controlling the ongoing SARS-CoV-2 epidemic due to the large fraction of pre-symptomatic and asymptomatic transmission. A quarantine period of 10 days from exposure, as currently implemented in Switzerland, is long enough to prevent almost all onward transmission from infected contacts of confirmed cases from the point of entering quarantine: increasing the duration of quarantine beyond 10 days has no extra benefit. Reducing the delay to quarantining individuals increases the fraction of total transmission that is preventable. The same 10-day quarantine duration will prevent almost all local onward transmission from infected travel returners from the time of arrival, independent of their travel duration.

Any decrease in the duration of quarantine of an infected individual will result in increased onward transmission. Furthermore, our analyses suggest that this increase in transmission cannot realistically be compensated by increased adherence for significantly shortened quarantine (fewer than 5 days). However, there are diminishing returns for each day that we add to quarantine: increasing the duration from 10 days has a negligible effect in terms of reduced transmission. One therefore has to assess how much human cost, measured in terms of days spent in quarantine, we are willing to spend to prevent disease transmission. By comparing the ratio of prevented transmission to quarantine duration, we have shown that maximal utility strategies can exist. This ratio is maximised for quarantine durations of 6–8 days after exposure for traced contacts, and potentially less for returning travellers depending on their duration of travel. Importantly, under this metric the fraction of individuals in quarantine that are infected does not affect the optimal duration of quarantine. Therefore, the argument that we should shorten quarantine because of the low probability of being infected is misguided under our definition of utility and in the absence of testing during quarantine.

A test-and-release strategy will lead to a lower average quarantine duration across infected and non-infected individuals. However, due to the considerable false-negative probability of the RT-PCR test (Kucirka et al., 2020), this strategy also leads to increased transmission as infectious individuals are prematurely released. Nevertheless, test-and-release strategies prevent more transmission than releasing without testing, and hence test-and-release increases the utility of quarantine. Reducing the delay between test and result leads to further reduced transmission and increased utility, and reinforcing individual prevention measures after release is also effective for short quarantine periods.

The ratio of transmission prevented versus days spent in quarantine is only one possible definition of utility. Defining the appropriate function is ultimately a policy question: the economic, societal, and individual costs are likely a function of the number of days spent in quarantine, but we cannot determine the shape of this function. Furthermore, the local epidemiological situation will dictate which metric of quarantine efficacy is to be optimised. In situations where the goal is to prevent the (re)introduction of SARS-CoV-2, one should focus on maximising the reduction of transmission (and hence minimising the transmission risk). If the virus is already endemic, then considering the trade-off between transmission reduction and quarantine duration could determine the optimum strategy. Another perspective is that the utility of preventing transmission is crucially dependent on whether it brings the effective reproductive number under 1.

Ultimately, bringing the reproductive number below 1 requires a combination of effective measures including isolation, physical distancing, hygiene, contact tracing, and quarantine (Kucharski et al., 2020). Effective quarantine is only possible in the presence of efficient contact tracing to find the potentially exposed individuals in a short time, as well as surveillance of disease prevalence to identify high-risk travel. Further reducing the time taken to quarantine a contact after exposure and reducing the delay between test and result will allow average quarantine durations to be shorter, which increases the benefit-to-cost ratio of quarantine.

The scenarios of returning travellers and traced contacts of confirmed SARS-CoV-2 cases differ in the probability of having been exposed and infected and on the information available about the likely window of exposure. The impact of quarantining returning travellers depends on the duration of travel and whether we consider the local prevention of transmission or the total transmission prevented by quarantine. However, a single test done immediately after return can only prevent a small fraction of the transmission from a returning traveller because of the false-negative rate of the RT-PCR test early in infection. Therefore testing should be postponed until as late as possible, and utilising rapid tests could be crucial if their performance characteristics are acceptable. This same principle also applies to traced contacts. Our findings are aligned with those of two recent simulation studies which estimate the role that quarantine plays in limiting transmission from returning travellers (Clifford, 2020) and from traced contacts (Quilty et al., 2021).

Our results are based on the latest estimates of the generation time distribution of COVID-19 (Ferretti et al., 2020b). Potential limitations to our approach could be that these distributions may change throughout the epidemic, particularly depending on how people respond to symptoms (Ali et al., 2020). Furthermore, these distributions, and also the test sensitivity profile, could be different between persistently asymptomatic and symptomatic individuals (Buitrago-Garcia et al., 2020), which ultimately lead to an overestimation of how much transmission is prevented by quarantine. In addition, we have primarily assumed that symptom onset during quarantine has no impact on quarantine efficacy. However, this symptomatic transmission should not be counted towards the efficacy of quarantine as the infected individual should already self-isolate after symptom onset. We have quantified this effect and have shown that this assumption leads us to overestimate quarantine efficacy.

For travellers, another consideration is that lengthy quarantine is seen as a deterrent to travel to high-risk areas (IATA, 2020). Any shortening of quarantine may lead to an increase in travel volume, potentially leading to a compounded increase in disease transmission.

In the absence of empirical data about the effectiveness of different durations of quarantine, mathematical modelling can be used objectively to explore the fraction of onward transmission by infected contacts or returning travellers that can be prevented. However, determining the optimal quarantine strategy to implement depends on the impact that shortening the duration of quarantine has on individuals, society, and the economy versus how much weight is assigned to a consequential increase in transmission. Both the individual, societal, and economic impact, as well as the weight of transmission increase, will have to be considered based on the current epidemiological situation. We have shown that there are quarantine strategies based on a test-and-release protocol that, from an epidemiological viewpoint, perform almost as well as the standard 10-day quarantine, but with a lower cost in terms of person-days spent in quarantine. This applies to both travellers and contacts, but the specifics depend on the context.

## Materials and methods

### Quantifying the benefit of quarantine

For an infected individual who was exposed at time $t_{_}⁢E$, the fraction of transmission that is prevented by the standard quarantine strategy is given by the area under the generation time distribution, $q⁢(t)$ (Figure 1—figure supplement 1B), between the times at which the individual enters ($t_{_}⁢Q$) and leaves ($t_{_}⁢R$) quarantine (Grantz et al., 2020), that is,

$$
F_{_}⁢qs⁢(t_{_}⁢E,t_{_}⁢Q,t_{_}⁢R)=\int_{_}t_{_}⁢Q^{t_{_}⁢R}⁢dt⁢q⁢(t-t_{_}⁢E).
$$

The duration of time that the individual spends in quarantine is then $D_{_}⁢qs=t_{_}⁢R-t_{_}⁢Q$.

The test-and-release strategy uses virological testing during quarantine to release individuals with a negative test result and to place those with a positive test result into isolation. As illustrated in Figure 1A, test is issued at time $t_{_}⁢T\geqt_{_}⁢Q$. If the test is negative, the individual is released when the test result arrives at time $t_{_}⁢R$. Otherwise, the individual is isolated until they are no longer infectious. One challenge with this strategy is the high probability of a false-negative RT-PCR test result (i.e. an infectious individual is prematurely released into the community). As reported by Kucirka et al., 2020, the false-negative rate is 100% on days 0 and 1 post-infection, falling to 67% (day 4), 38% (day 5), 25% (day 6), 21% (day 7), 20% (day 8), and 21% (day 9), before rising to 66% on day 21. We use linear interpolation and label this function $f⁢(t)$, the false-negative probability on day t after infection. The fraction of transmission prevented by quarantining an infected individual under the test-and-release strategy is

$$
F_{_}⁢qtr⁢(t_{_}⁢E,t_{_}⁢Q,t_{_}⁢T,t_{_}⁢R)=f⁢(t_{_}⁢T-t_{_}⁢E)⁢\int_{_}t_{_}⁢Q^{t_{_}⁢R}⁢dt⁢q⁢(t-t_{_}⁢E)+[1-f⁢(t_{_}⁢T-t_{_}⁢E)]⁢\int_{_}t_{_}⁢Q^{t_{_}⁢end}⁢dt⁢q⁢(t-t_{_}⁢E),
$$

where the first term captures the fraction of individuals who receive a false-negative test result and are released at time $t_{_}⁢R$, and the second term captures individuals who return a positive test and are subsequently isolated until they are no longer infectious at time $t_{_}⁢end$. A further challenge with this false-negative rate is that it was calculated by Kucirka et al., 2020 from symptomatic cases only. Here we assume that this test sensitivity profile also applies to asymptomatic cases.

Quarantine is applied pre-emptively, such that we do not know the infection status of individuals when they enter quarantine. If only a fraction s of the individuals that are quarantined are infected, then the average reduction in transmission across all individuals in quarantine is $s⁢F$, where F is the fraction of transmission prevented when an infected individual is quarantined [i.e. Equation (1) or (2)]. For the standard quarantine protocol, the average number of days spent in quarantine is independent of s: all individuals are quarantined for the same duration. However, under the test-and-release protocol, only the individuals who are actually infected can test positive and remain isolated after $t_{_}⁢R$. All non-infected individuals ($1-s$) will receive a negative test result and are released at time $t_{_}⁢R$. Among the infected individuals in quarantine (s), a fraction $f⁢(t_{_}⁢T-t_{_}⁢E)$ will receive a false-negative test result and will be released at time $t_{_}⁢R$, while the remaining fraction [$1-f⁢(t_{_}⁢T-t_{_}⁢E)$] will receive a positive test result and are isolated until they are no longer infectious. Hence the average number of days spent in quarantine for test-and-release is

$$
D_{qtr}=(1−s)(t_{R}−t_{Q})+s[f(t_{T}−t_{E})(t_{R}−t_{Q})+[1−f(t_{T}−t_{E})](t_{end}−t_{Q})]=(t_{R}−t_{Q})+s[1−f(t_{T}−t_{E})](t_{end}−t_{R}),
$$

where $s⁢[1-f⁢(t_{_}⁢T-t_{_}⁢E)]$ is the fraction of quarantined individuals who return a positive test result. We see that the average test-and-release quarantine duration increases linearly with the fraction of individuals in quarantine that are infected (s).

Model parameters and timepoints are summarised in Table 1.

**Table 1.**
 Summary of terms used in the mathematical model.


<table>
  <thead>
    <tr>
      <th>Value</th>
      <th>Definition</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>q⁢(t)</td>
      <td>Generation time distribution</td>
      <td>Weibull distribution: shape = 3.277, scale = 6.127</td>
    </tr>
    <tr>
      <td>t_⁢E</td>
      <td>Time of exposure</td>
      <td>t_⁢E=0 for traced contacts</td>
    </tr>
    <tr>
      <td>t_⁢Q</td>
      <td>Time at which quarantine begins</td>
      <td>t_⁢Q=0 for returning travellers</td>
    </tr>
    <tr>
      <td>t_⁢R</td>
      <td>Time of release from quarantine</td>
      <td>-</td>
    </tr>
    <tr>
      <td>t_⁢T</td>
      <td>Time of test</td>
      <td>-</td>
    </tr>
    <tr>
      <td>t_⁢end</td>
      <td>End of infectiousness</td>
      <td>t_⁢end=t_⁢E+10 days</td>
    </tr>
    <tr>
      <td>g⁢(t)</td>
      <td>Incubation period distribution</td>
      <td>Meta-log-normal distribution ('Appendix 1: Distribution parameters')</td>
    </tr>
    <tr>
      <td>t_⁢S</td>
      <td>Time of symptom onset</td>
      <td>t_⁢S=t_⁢E+ incubation period</td>
    </tr>
    <tr>
      <td>D_⁢qs</td>
      <td>Realised average duration of standard quarantine</td>
      <td>D_⁢qs=t_⁢R-t_⁢Q</td>
    </tr>
    <tr>
      <td>D_⁢qtr</td>
      <td>Realised average duration of test-and-release quarantine</td>
      <td>See Equation (3)</td>
    </tr>
    <tr>
      <td>F_⁢qs⁢(⋅), F_⁢qtr⁢(⋅)</td>
      <td>Quarantine efficacy; the fraction of transmission prevented by quarantining an infected individual</td>
      <td>See Equations (1) and (2)</td>
    </tr>
    <tr>
      <td>y</td>
      <td>Duration of travel journey (days)</td>
      <td>-</td>
    </tr>
    <tr>
      <td>s</td>
      <td>Fraction of individuals in quarantine that are infected</td>
      <td>-</td>
    </tr>
    <tr>
      <td>f⁢(t)</td>
      <td>Probability of returning a false-negative test result if tested t days after exposure</td>
      <td>From Kucirka et al., 2020</td>
    </tr>
    <tr>
      <td>r</td>
      <td>Reduction of transmission under reinforced prevention measures post-quarantine</td>
      <td>-</td>
    </tr>
    <tr>
      <td>α⁢(D)</td>
      <td>Probability to adhere to quarantine of duration D</td>
      <td>-</td>
    </tr>
    <tr>
      <td>a</td>
      <td>Fraction of persistently asymptomatic cases</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Δ</td>
      <td>Delay between symptom onset and isolation (days)</td>
      <td>See 'Appendix 1: Persistently asymptomatic infections and the role of self-isolation'</td>
    </tr>
  </tbody>
</table>

### Transmission reduction versus days spent in quarantine

One possible metric to relate the effectiveness of quarantine to its negative impact on society is to consider the ratio between the amount of overall transmission prevented and the number of person-days spent in quarantine. We refer to this ratio as the utility of quarantine. Concretely, for an efficacy F [$F_{_}⁢qs$ or $F_{_}⁢qtr$ as defined by Equation (1) or (2), respectively], fraction of individuals in quarantine that are infected s, and average time spent in quarantine D ($D_{_}⁢qs$ or $D_{_}⁢qtr$), we define the utility as

$$
U⁢(s,F,D)=\frac{s⁢F}{D}.
$$

We can then compare the utility of two quarantine strategies by calculating the relative utility, that is, the ratio between the two utilities:

$$
RU(s,F,D,F^{∗},D^{∗})=\frac{sF/D}{sF^{∗}/D^{∗}}=\frac{F/D}{F^{∗}/D^{∗}},
$$

where F and D are the efficacy and duration of quarantine of a new strategy, and $F^{*}$ and $D^{*}$ are the efficacy and duration of the baseline quarantine strategy to which we compare.

The efficacies F and $F^{*}$ in Equation (5) are independent of fraction of individuals in quarantine that are infected s. For the standard quarantine strategy, the durations $D=D_{_}⁢qs$ and $D^{*}=D_{_}⁢qs^{*}$ are also independent of s, and hence the relative utility of the standard quarantine strategy is independent of s. For the test-and-release strategy, however, the duration is a linearly increasing function of s [$D=D_{_}⁢qtr⁢(s)$; Equation (3)]. Hence the relative utility of the test-and-release strategy is dependent on s:

$$
RU⁢[s,F_{_}⁢qtr,D_{_}⁢qtr⁢(s),F_{_}⁢qs^{*},D_{_}⁢qs^{*}]=\frac{F_{_}⁢qtr/D_{_}⁢qtr⁢(s)}{F_{_}⁢qs^{*}/D_{_}⁢qs^{*}}.
$$

In Appendix 1 we show that the relative utility of the test-and-release quarantine strategy is a decreasing function of s.

### Traced contacts versus returning travellers

We consider the scenarios of a traced contact and a returning traveller differently because the values of $t_{_}⁢E$, $t_{_}⁢Q$, and $t_{_}⁢R$ are implemented differently in each case.

#### Traced contacts

Following a positive test result, a confirmed index case has their recent close contacts traced. From contact tracing interviews, we know the date of last exposure between index case and a contact ($t_{_}⁢E$), which we assume is the time of infection of the contact. The contacts begin quarantine at time $t_{_}⁢Q\geqt_{_}⁢E$. The delay between exposure and the start of quarantine represents the sum of the delay to the index case receiving a positive test result and the further delay to tracing the contacts. Under the standard quarantine protocol, the traced contacts are quarantined for a number of days after their last exposure. For example, in Switzerland quarantine lasts until $t_{_}⁢R=t_{_}⁢E+10$ days, but may be longer or shorter depending on individual states’ regulations. Note that the actual time spent in quarantine is $D_{_}⁢qs=t_{_}⁢R-t_{_}⁢Q$ days, which is typically shorter than 10 days due to the delay between exposure and the start of quarantine. For convenience, we set $t_{_}⁢E=0$ for the traced contacts, without loss of generality.

#### Returning travellers

Unlike traced contacts, we generally do not know when travellers were (potentially) exposed. This means that quarantine starts from the date that they return ($t_{_}⁢Q=0$) and lasts until time $t_{_}⁢R$ (Figure 1B). For simplicity, we assume that a traveller was infected with uniform probability at some time over a travel period of duration y days.

For each possible exposure time $-y\leqt_{_}⁢E\leq0$ during the trip, we can compute the fraction of transmission prevented using Equation (1) and then take the average over the possible exposure times. This represents the average fraction of the total transmission potential that is prevented by quarantining this traveller:

$$
F¯_{qs}^{(total)}(y,t_{R})=\frac{1}{y+1}\sumt_{E}=−y0\int_{0}^{t_{R}}dtq(t−t_{E}),
$$

where we have used $t_{_}⁢Q=0$.

For each exposure time $-y\leqt_{_}⁢E\leq0$, we can also compute the local fraction of transmission prevented by quarantine, which is the fraction of transmission prevented by quarantine divided by the maximum amount of transmission that could occur in the local country, that is,

$$
F_{qs}^{(local)}(t_{E},t_{R})=\frac{\int_{0}^{t_{R}}dtq(t−t_{E})}{\int_{0}^{∞}dtq(t−t_{E})},
$$

where we have again used $t_{_}⁢Q=0$. Taking the average over the possible exposure times $-y\leqt_{_}⁢E\leq0$, we have

$$
F¯_{qs}^{(local)}(y,t_{R})=\frac{1}{y+1}\sumt_{E}=−y0F_{qs}^{(local)}(t_{E},t_{R}).
$$

### Interactive app

To complement the results in this paper, and to allow readers to investigate different quarantine scenarios, we have developed an online interactive application. This can be found at https://ibz-shiny.ethz.ch/covidDashboard/quarantine.
