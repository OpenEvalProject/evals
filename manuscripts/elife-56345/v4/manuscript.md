# Paranoia as a deficit in non-social belief updating

## Authors

- Erin J Reed<sup>1</sup> ([ORCID: 0000-0003-1669-1929](https://orcid.org/0000-0003-1669-1929))
- Stefan Uddenberg<sup>3</sup>
- Praveen Suthaharan<sup>4</sup>
- Christoph D Mathys<sup>5</sup>
- Jane R Taylor<sup>4</sup>
- Stephanie Mary Groman<sup>4</sup> ([ORCID: 0000-0002-5231-0612](https://orcid.org/0000-0002-5231-0612))
- Philip R Corlett<sup>4</sup> ([ORCID: 0000-0002-5368-1992](https://orcid.org/0000-0002-5368-1992)) †

### Affiliations

1. Interdepartmental Neuroscience Program, Yale School of Medicine New Haven United States
2. Yale MD-PhD Program, Yale School of Medicine New Haven United States
3. Princeton Neuroscience Institute, Princeton University Princeton United States
4. Department of Psychiatry, Connecticut Mental Health Center, Yale University New Have United States
5. Scuola Internazionale Superiore di Studi Avanzati (SISSA) Trieste Italy
6. Translational Neuromodeling Unit (TNU), Institute for Biomedical Engineering, University of Zurich and ETH Zurich Zurich Switzerland

† Corresponding author

## Abstract

Paranoia is the belief that harm is intended by others. It may arise from selective pressures to infer and avoid social threats, particularly in ambiguous or changing circumstances. We propose that uncertainty may be sufficient to elicit learning differences in paranoid individuals, without social threat. We used reversal learning behavior and computational modeling to estimate belief updating across individuals with and without mental illness, online participants, and rats chronically exposed to methamphetamine, an elicitor of paranoia in humans. Paranoia is associated with a stronger prior on volatility, accompanied by elevated sensitivity to perceived changes in the task environment. Methamphetamine exposure in rats recapitulates this impaired uncertainty-driven belief updating and rigid anticipation of a volatile environment. Our work provides evidence of fundamental, domain-general learning differences in paranoid individuals. This paradigm enables further assessment of the interplay between uncertainty and belief-updating across individuals and species.

## Introduction

Paranoia is excessive concern that harm will occur due to deliberate actions of others (Freeman and Garety, 2000). It manifests along a continuum of increasing severity (Freeman et al., 2005; Freeman et al., 2010; Freeman et al., 2011; Bebbington et al., 2013). Fleeting paranoid thoughts prevail in the general population (Freeman, 2006). A survey of over 7000 individuals found that nearly 20% believed people were against them at times in the past year; approximately 8% felt people had intentionally acted to harm them (Freeman et al., 2011). At a national level, paranoia may fuel divisive ideological intolerance. Historian Richard Hofstadter famously described catastrophizing, context insensitive political discourse as the ‘paranoid style’:

“The paranoid spokesman sees the fate of conspiracy in apocalyptic terms—he traffics in the birth and death of whole worlds, whole political orders, whole systems of human values. He is always manning the barricades of civilization. He constantly lives at a turning point [emphasis added].” (Hofstadter, 1964).

At its most severe, paranoia manifests as rigid beliefs known as delusions of persecution. These delusions occur in nearly 90% of first episode psychosis patients (Freeman, 2007). Psychostimulants also elicit severe paranoid states. Methamphetamine evokes new paranoid ideation particularly after repeated exposure or escalating doses (86% and 68%, respectively, in a survey of methamphetamine users) (Leamon et al., 2010).

Paranoia has thus far defied explanation in mechanistic terms. Sophisticated Game Theory driven approaches (such as the Dictator Game [Raihani and Bell, 2018; Raihani and Bell, 2017]) have largely re-described the phenomenon — people who are paranoid have difficulties in laboratory tasks that require trust (Raihani and Bell, 2019). However, this is not driven by personal threat per se, but by negative representations of others (Raihani and Bell, 2018; Raihani and Bell, 2017). We posit that such representations are learned (Fineberg et al., 2014; Behrens et al., 2008), via the same fundamental learning mechanisms (Cramer et al., 2002) that underwrite non-social learning in non-human species (Heyes and Pearce, 2015). We hypothesize that aberrations to these domain-general learning mechanisms underlie paranoia. One such mechanism involves the judicious use of uncertainty to update beliefs: Expectations about the noisiness of the environment constrain whether we update beliefs or dismiss surprises as probabilistic anomalies. The higher the expected uncertainty (i.e., ‘I expect variable outcomes’), the less surprising an atypical outcome may be, and the less it drives belief updates (‘this variation is normal’). Unexpected uncertainty, in contrast, describes perceived change in the underlying statistics of the environment (Yu and Dayan, 2005; Payzan-LeNestour and Bossaerts, 2011; Payzan-LeNestour et al., 2013) (i.e. ‘the world is changing’), which may call for belief revision.

Since excessive unexpected uncertainty is a signal of change, it might drive the recategorization of allies as enemies, which is a tenet of evolutionary theories of paranoia (Raihani and Bell, 2019). We tested the hypothesis that this drive to flexibly recategorize associations extends to non-social, domain-general inferences. We dissected learning mechanisms under expected and unexpected uncertainty – probabilistic variation and changes in underlying task structure (volatility). Here, volatility is a property of the task. Unexpected uncertainty is the perception of that volatility. Participants completed a non-social, three-option learning task which challenged them to form and revise associations between stimuli (colored card decks) and outcomes (points rewarded and lost), in addition to their beliefs about the volatility of the task environment. They encountered expected uncertainty as probabilistic win or loss feedback (‘each option yields positive and negative outcomes, but in different amounts’), and unexpected uncertainty as reassignment of reward probabilities between options (‘sometimes the best option may change,’ reversal events). Although reversal events elicit unexpected uncertainty by driving re-evaluation of the options, participants increasingly anticipate reversals and develop expectations about the stability of the task environment. We implemented an additional task manipulation: a shift in the underlying probabilities themselves (contingency transition, unsignaled to the participants), that effectively changes task volatility. Armed with the task structure and participants’ choices, we applied a Hierarchical Gaussian Filter (HGF) model (Mathys et al., 2011; Mathys et al., 2014) which allowed us to infer participants’ initial beliefs (i.e., priors) about task volatility, their readiness to learn about changes in the task volatility itself (meta-volatility learning rate) and learning rates that captured their expected and unexpected uncertainty regarding the task.

We examined the behavioral and computational correlates of paranoia both in-person and in a large online sample, spanning patients and healthy controls with varying degrees of paranoia. We also undertook a pre-clinical replication in rodents exposed chronically to saline or methamphetamine to determine whether a drug known to elicit paranoia in humans might induce similar perceptions of unexpected uncertainty, without contingency transition (Groman et al., 2018). We predicted that people with paranoia and rats administered methamphetamine would exhibit stronger priors on volatility, facilitating aberrant learning through unexpected uncertainty. We further hypothesized that this learning style would manifest as frequent and unnecessary choice switching (increased choice stochasticity and ‘win-switch’ behavior) rather than increased sensitivity to negative feedback (increased ‘lose-switch’ behavior/decreased ‘lose-stay’ behavior).

## Results

We analyzed belief updating across three reversal-learning experiments (Figure 1): an in laboratory pilot of patients and healthy controls, stratified by stable, paranoid personality trait (Experiment 1); four online task variants administered to participants via the Amazon Mechanical Turk (MTurk) marketplace (Experiment 2); and a re-analysis of data from rats on chronic, escalating doses of methamphetamine, a translational model of paranoia (Experiment 3) (Groman et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig1-v4.jpg)

**Figure 1.:** (a) Human paradigm: participants choose between three decks of cards with different colored backs (Blue, Red, and Green) with different, unknown probabilities of reward and loss. (b) Reward contingency schedule for in laboratory experiment (Reward probabilities associated with the different colored decks, Blue, Red, Green, across trials and blocks). On trial 81, the probability context shifted from 90%, 50%, and 10% (dark grey) to 80%, 40%, and 20% without warning (light grey). (c), Reward contingency schedules for online experiment. (d) Rat paradigm: subjects choose between three noseports (Blue, Red, Green, for illustrative puposes) with different probabilities of sucrose pellet reward. (e) Reward contingency schedule for rat experiment (Groman et al., 2018). Performance dependent reversals occur after a certain number of choices of the high reward deck. Performance independent reversals occur regardless of participant behavior.

### Experiment 1

First, we explored trans-diagnostic associations between paranoia and reversal-learning in-person. Participants with and without psychiatric diagnoses (mood disorders: anxiety, depression, bipolar disorder, n = 8; schizophrenia spectrum: schizophrenia or schizoaffective disorder, n = 8; and healthy controls, n = 16), completed questionnaire versions of the Structured Clinical Interview for DSM-IV Axis II Personality Disorders (SCID-II) screening assessment (Ryder et al., 2007), Beck’s Anxiety Inventory (BAI) (Beck et al., 1988), Beck’s Depression Inventory (BDI) (Beck et al., 1961), and demographic assessments (Table 1). Approximately two-thirds of participants endorsed three or fewer items on the SCID-II paranoid personality subscale (median = 1 item). Participants who endorsed four or more items were classified as high paranoia (n = 11), consistent with the diagnostic threshold for paranoid personality disorder. Low paranoia (n = 21) and high paranoia groups did not differ significantly by age, nor were there significant group associations with gender, educational attainment, ethnicity, or race, although a larger percentage of paranoid participants identified as racial minorities or ‘not specified’ (Table 1). Diagnostic category (i.e., healthy control, mood disorder, or schizophrenia spectrum) was significantly associated with paranoia group membership, χ2 (2, n = 32)=12.329, p=0.002, Cramer’s V = 0.621, as was psychiatric medication usage, χ2 (1, n = 32)=9.871, p=0.003, Cramer’s V = 0.555. These differences were due to the higher proportion of healthy controls in the low paranoia group. As expected, paranoia, BAI, and BDI scores were significantly elevated in the high paranoia group relative to low paranoia controls (Table 1; paranoia: mean difference (MD) = 0.536, CI=[0.455,0.618], t(30)=13.476, p=2.92E-14, Hedges’ g = 5.016; BAI: MD = 0.585, CI=[0.239, 0.931], t(30)=3.453, p=0.002, Hedges’ g = 1.285, MD = −0.585; BDI: MD = 0.427, CI=[0.078, 0.775], t(11.854) = 2.67, p=0.021, Hedges’ g = 1.255).

**Table 1.**
 In Lab vs. Online Version 3.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">In Lab</th>
      <th colspan="4">Online Version 3</th>
    </tr>
    <tr>
      <th></th>
      <th>Low Paranoia (n=21)</th>
      <th>High Paranoia (n=11)</th>
      <th>Statistic</th>
      <th>p-value</th>
      <th>Low Paranoia (n=56)</th>
      <th>High Paranoia (n=16)</th>
      <th>Statistic</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4"></td>
      <td colspan="4"></td>
      <td>Demographics</td>
    </tr>
    <tr>
      <td>Age (years)</td>
      <td>36.0 [3.2]</td>
      <td>38.9 [3.9]</td>
      <td>-0.531 (27)†</td>
      <td>0.6</td>
      <td>38.6 [1.6]</td>
      <td>32.9 [1.7]</td>
      <td>2.441 (41.8)†</td>
      <td>0.019¶</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td></td>
      <td></td>
      <td>0.006 (1)‡</td>
      <td>1§</td>
      <td></td>
      <td></td>
      <td>.780 (1)‡</td>
      <td>0.410</td>
    </tr>
    <tr>
      <td>% Female</td>
      <td>71.4%</td>
      <td>72.7%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>50.0%</td>
      <td>62.5%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Male</td>
      <td>28.6%</td>
      <td>27.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>50.0%</td>
      <td>37.5%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Other or not specified</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Education</td>
      <td></td>
      <td></td>
      <td>4.972 (6)‡</td>
      <td>0.638§</td>
      <td></td>
      <td></td>
      <td>5.351 (6)‡</td>
      <td>0.549§</td>
    </tr>
    <tr>
      <td>% High school degree or equivalent</td>
      <td>19.0%</td>
      <td>45.5%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>16.1%</td>
      <td>6.3%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Some college or university, no degree</td>
      <td>14.3%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>17.9%</td>
      <td>25.0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Associate degree</td>
      <td>9.5%</td>
      <td>9.1%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>12.5%</td>
      <td>12.5%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Bachelor's degree</td>
      <td>23.8%</td>
      <td>27.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>35.7%</td>
      <td>56.3%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Master's degree</td>
      <td>9.5%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>14.3%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Doctorate or professional degree</td>
      <td>4.8%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>1.8%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Completed some postgraduate</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>1.8%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Other / not specified</td>
      <td>19.0%</td>
      <td>18.2%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Ethnicity</td>
      <td></td>
      <td></td>
      <td>.134 (1)‡</td>
      <td>1§</td>
      <td></td>
      <td></td>
      <td>.117 (1)‡</td>
      <td>1§</td>
    </tr>
    <tr>
      <td>% Hispanic, Latino, or Spanish origin</td>
      <td>23.8%</td>
      <td>18.2%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>8.9%</td>
      <td>6.3%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Not of Hispanic, Latino, or Spanish origin</td>
      <td>76.2%</td>
      <td>81.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>91.1%</td>
      <td>93.8%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Race</td>
      <td></td>
      <td></td>
      <td>6.250 (4)‡</td>
      <td>0.186§</td>
      <td></td>
      <td></td>
      <td>5.368 (4)‡</td>
      <td>0.229§</td>
    </tr>
    <tr>
      <td>% White</td>
      <td>61.9%</td>
      <td>36.4%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>85.7%</td>
      <td>75.0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Black or African American</td>
      <td>19.0%</td>
      <td>36.4%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0%</td>
      <td>12.5%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Asian</td>
      <td>14.3%</td>
      <td>9.1%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>3.6%</td>
      <td>6.3%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% American Indian or Alaska Native</td>
      <td>4.8%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>1.8%</td>
      <td>6.3%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Multiracial</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>3.6%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Other / not specified</td>
      <td>0%</td>
      <td>18.2%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>5.4%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td colspan="4"></td>
      <td colspan="4"></td>
      <td>Mental Health</td>
    </tr>
    <tr>
      <td>Psychiatric diagnosis</td>
      <td></td>
      <td></td>
      <td>12.329 (2)‡</td>
      <td>0.002§</td>
      <td></td>
      <td></td>
      <td>7.850 (3)‡</td>
      <td>0.039§</td>
    </tr>
    <tr>
      <td>% No psychiatric diagnosis</td>
      <td>71.4%</td>
      <td>9.1%</td>
      <td>adj. residuals</td>
      <td>0.004</td>
      <td>71.4%</td>
      <td>50.0%</td>
      <td>adj. residuals</td>
      <td>0.465</td>
    </tr>
    <tr>
      <td>% Schizophrenia spectrum</td>
      <td>19.0%</td>
      <td>36.4%</td>
      <td>adj. residuals</td>
      <td>0.546</td>
      <td>0%</td>
      <td>6.3%</td>
      <td>adj. residuals</td>
      <td>0.307</td>
    </tr>
    <tr>
      <td>% Mood disorder</td>
      <td>9.5%</td>
      <td>54.5%</td>
      <td>adj. residuals</td>
      <td>0.020#</td>
      <td>21.4%</td>
      <td>43.8%</td>
      <td>adj. residuals</td>
      <td>0.356</td>
    </tr>
    <tr>
      <td>% Not specified</td>
      <td>0%</td>
      <td>0%</td>
      <td>adj. residuals</td>
      <td>n/a</td>
      <td>7.1%</td>
      <td>0%</td>
      <td>adj. residuals</td>
      <td>0.751</td>
    </tr>
    <tr>
      <td>% Medicated</td>
      <td>23.8%</td>
      <td>81.8%</td>
      <td>9.871 (1)‡</td>
      <td>0.003§</td>
      <td>7.1%</td>
      <td>31.3%</td>
      <td>8.730 (2)‡</td>
      <td>0.023§</td>
    </tr>
    <tr>
      <td>Beck's Anxiety Inventory</td>
      <td>0.27 [0.08]</td>
      <td>0.85 [0.17]</td>
      <td>-3.453 (30)†</td>
      <td>0.002</td>
      <td>0.24 [0.04]</td>
      <td>0.90 [0.20]</td>
      <td>-3.303 (16.179)†</td>
      <td>0.004¶</td>
    </tr>
    <tr>
      <td>Beck's Depression Inventory</td>
      <td>0.23 [0.05]</td>
      <td>0.66 [0.15]</td>
      <td>-2.67 (11.854)†</td>
      <td>0.021¶</td>
      <td>0.25 [0.04]</td>
      <td>1.03 [0.19]</td>
      <td>-3.951 (16.659)†</td>
      <td>0.001¶</td>
    </tr>
    <tr>
      <td>SCID Paranoia Personality Score</td>
      <td>0.09 [0.02]</td>
      <td>0.63 [0.04]</td>
      <td>-13.476 (30)†</td>
      <td>2.92E-14</td>
      <td>0.1 [0.02]</td>
      <td>0.72 [0.04]</td>
      <td>-16.551 (70)†</td>
      <td>6.712E-26</td>
    </tr>
    <tr>
      <td colspan="4"></td>
      <td colspan="4"></td>
      <td>Reversal Learning Performance</td>
    </tr>
    <tr>
      <td>Total points earned</td>
      <td>7061.9 [286.9]</td>
      <td>6290.9 [372.2]</td>
      <td>1.608 (30)†</td>
      <td>0.118</td>
      <td>7533.0 [143.8]</td>
      <td>6503.1 [340.6]</td>
      <td>3.177 (70)†</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>Total reversals achieved</td>
      <td>4.8 [0.7]</td>
      <td>2.5 [0.8]</td>
      <td>2.145 (30)†</td>
      <td>0.04</td>
      <td>6.3 [0.3]</td>
      <td>4.9 [0.8]</td>
      <td>1.758 (20.14)†</td>
      <td>0.094¶</td>
    </tr>
    <tr>
      <td>% Achieving reversals</td>
      <td>90.5%</td>
      <td>72.7%</td>
      <td>1.407 (1)‡</td>
      <td>0.327§</td>
      <td>100%</td>
      <td>87.5%</td>
      <td>7.200 (1)‡</td>
      <td>0.047§</td>
    </tr>
    <tr>
      <td>Trials to first reversal</td>
      <td>29.2 [4.5]</td>
      <td>27.9 [11]</td>
      <td>0.136 (25)†</td>
      <td>0.893</td>
      <td>20.0 [1.7]</td>
      <td>13.7 [1.8]</td>
      <td>1.774 (68)†</td>
      <td>0.081</td>
    </tr>
    <tr>
      <td>% Recovering post-reversal</td>
      <td>81.0%</td>
      <td>54.5%</td>
      <td>2.490 (1)‡</td>
      <td>0.213§</td>
      <td>91.1%</td>
      <td>69.0%</td>
      <td>3.482 (1)‡</td>
      <td>0.097§</td>
    </tr>
    <tr>
      <td>Trials to switch</td>
      <td>1.68 [0.22]</td>
      <td>1.43 [0.20]</td>
      <td>0.671 (24)†</td>
      <td>0.509</td>
      <td>2.1 [0.2]</td>
      <td>2.6 [0.6]</td>
      <td>-1.088 (64)†</td>
      <td>0.280</td>
    </tr>
    <tr>
      <td>Trials to recovery</td>
      <td>3.75 [0.51]</td>
      <td>4 [0.93]</td>
      <td>-0.285 (21)†</td>
      <td>0.779</td>
      <td>2.9 [0.3]</td>
      <td>4.9 [0.8]</td>
      <td>-2.694 (60)†</td>
      <td>0.009</td>
    </tr>
    <tr>
      <td>Win-switch rate, block 1 (90-50-10)</td>
      <td>0.08 [0.03]</td>
      <td>0.24 [0.09]</td>
      <td>-1.742 (12.379)†</td>
      <td>0.106¶</td>
      <td>0.04 [0.01]</td>
      <td>0.13 [0.05]</td>
      <td>-1.906 (15.762)†</td>
      <td>0.075¶</td>
    </tr>
    <tr>
      <td>Win-switch rate, block 2 (80-40-20)</td>
      <td>0.07 [0.04]</td>
      <td>0.21 [0.1]</td>
      <td>-1.601 (30)†</td>
      <td>0.12</td>
      <td>0.02 [0.01]</td>
      <td>0.12 [0.05]</td>
      <td>-2.02 (15.915)†</td>
      <td>0.061¶</td>
    </tr>
    <tr>
      <td>Lose-stay rate, block 1 (90-50-10)</td>
      <td>0.19 [0.03]</td>
      <td>0.13 [0.06]</td>
      <td>0.919 (30)†</td>
      <td>0.365</td>
      <td>0.30 [0.03]</td>
      <td>0.39 [0.06]</td>
      <td>-1.425 (70)†</td>
      <td>0.158</td>
    </tr>
    <tr>
      <td>Lose-stay rate, block 2 (80-40-20)</td>
      <td>0.26 [0.05]</td>
      <td>0.12 [0.05]</td>
      <td>1.817 (30)†</td>
      <td>0.079</td>
      <td>0.33 [0.03]</td>
      <td>0.37 [0.06]</td>
      <td>-0.554 (70)†</td>
      <td>0.581</td>
    </tr>
    <tr>
      <td>Null trials</td>
      <td>8.5 [2.8]</td>
      <td>10.4 [3.7]</td>
      <td>-0.391 (30)†</td>
      <td>0.699</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
  </tbody>
</table>

_† Independent samples t-test: t-value (df). Two-tailed p-values reported ‡ Exact test, chi-square coefficient (df)§ Exact significance (2-sided)¶ Equal variances not assumed # Not significant (bonferonni correction)._

Participants completed a three-option reversal-learning task in which they chose between three decks of cards with hidden reward probabilities (Figure 1a and b). They selected a deck on each turn and received positive or negative feedback (+100 or −50 points, respectively). They were instructed to find the best deck with the caveat that the best deck may change. Undisclosed to participants, reward probabilities switched among decks after selection of the highest probability option in nine out of ten consecutive trials (‘reversal events’). Thus, the task was designed to elicit expected uncertainty (probabilistic reward associations) and unexpected uncertainty (reversal events), requiring participants to distinguish probabilistic losses from change in the underlying deck values. In addition, reward contingencies changed from 90%, 50%, and 10% chance of reward to 80%, 40%, and 20% between the first and second halves of the task (‘contingency transition’; block 1 = 80 trials, 90-50–10%; block 2 = 80 trials, 80-40–20%, unsignaled to the participants). This transition altered the volatility of the task environment, thereby making it more difficult to achieve reversals and often delaying their occurrence. Successful achievement of reversals was contingent upon adapting stay-vs-switch strategies, thereby testing subjects’ abilities to update beliefs about the overall task volatility (‘metavolatility learning’). High paranoia subjects achieved fewer reversals (MD = −2.31, CI=[−4.504,–0.111,], t(30)=-2.145, p=0.04, Hedges’ g = 0.798), but total points earned did not significantly differ, suggesting that there was no penalty for the different behaviors expressed by the more paranoid subjects (Table 1). We predicted that paranoia would be associated with unexpected uncertainty-driven belief updating.

### Experiment 2

We aimed to replicate and extend our investigation of paranoia and reversal-learning in a larger online sample. We administered three alternative task versions to control for the contingency transition (Figure 1c). Version 1 (n = 45 low paranoia, 20 high paranoia) provided a constant contingency of 90-50–10% reward probabilities (Easy-Easy); version 2 (n = 69 low paranoia, 18 high paranoia) provided a constant contingency of 80-40–20% (Hard-Hard); version 3 (n = 56 low paranoia, 16 high paranoia) served to replicate Experiment 1 with a contingency transition from 90-50–10% to 80-40–20% (Easy-Hard); version 4 (n = 64 low paranoia, 19 high paranoia) provided the reverse contingency transition, 80-40–20% to 90-50–10% (Hard-Easy). The stable contingencies (versions 1 and 2) lacked contingency transitions. Versions 3 and 4 manipulated task volatility mid-way, although the contingency transition was not signalled to participants. We predicted that high paranoia participants would find versions 3 and 4 particularly challenging. Given that version 3 is easier to learn initially, we expected participants to develop stronger priors and thus be more confounded by the contingency transition, compared to version four participants.

Participants’ demographic and mental health questionnaire responses did not differ significantly across task version experiments (Table 2). Total points and reversals achieved suggest variations in task difficulty (Table 2, version effects: points earned, F(3, 299)=32.288, p=4.16E-18, ηp2=0.245; reversals achieved, F(3, 299)=4.329, p=0.005, ηp2=0.042), but there was no significant association between task version and attrition rate (52.7%, 52.9%, 54.6%, and 53.1% attrition, respectively; χ2 (3, n = 752)=0.167, p=0.983, Cramer’s V = 0.015).

**Table 2.**
 Online experiment.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Version 1</th>
      <th colspan="2">Version 2</th>
      <th colspan="2">Version 3</th>
      <th colspan="2">Version 4</th>
      <th colspan="2">Version Effect</th>
      <th colspan="2">Paranoia Effect</th>
      <th colspan="2">Interaction</th>
    </tr>
    <tr>
      <th></th>
      <th>Low Paranoia (n=45)</th>
      <th>High Paranoia (n=20)</th>
      <th>Low Paranoia (n=69)</th>
      <th>High Paranoia (n=18)</th>
      <th>Low Paranoia (n=56)</th>
      <th>High Paranoia (n=16)</th>
      <th>Low Paranoia (n=64)</th>
      <th>High Paranoia (n=19)</th>
      <th>Statistic</th>
      <th>p-value</th>
      <th>Statistic</th>
      <th>p-value</th>
      <th>Statistic</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Demographics</td>
      <td colspan="14"></td>
    </tr>
    <tr>
      <td>Age (years)</td>
      <td>36.5 [1.5]</td>
      <td>35.4 [2.4]</td>
      <td>36.2 [1.4]</td>
      <td>39.5 [2.8]</td>
      <td>38.6 [1.6]</td>
      <td>32.9 [1.7]</td>
      <td>37.6 [1.3]</td>
      <td>30.7 [1.6]</td>
      <td>1.12 (3)††</td>
      <td>0.342</td>
      <td>3.202 (1)††</td>
      <td>0.075</td>
      <td>2.619 (3)††</td>
      <td>0.051</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>7.29 (6)‡</td>
      <td>0.238§</td>
      <td>1.373 (2)‡</td>
      <td>0.503§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Female</td>
      <td>44.4%</td>
      <td>45.0%</td>
      <td>47.8%</td>
      <td>50.0%</td>
      <td>50.0%</td>
      <td>62.5%</td>
      <td>57.8%</td>
      <td>73.7%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Male</td>
      <td>55.6%</td>
      <td>55.0%</td>
      <td>50.7%</td>
      <td>50.0%</td>
      <td>50.0%</td>
      <td>37.5%</td>
      <td>42.2%</td>
      <td>26.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Other or not specified</td>
      <td>0%</td>
      <td>0%</td>
      <td>1.4%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Education</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>15.9 (21)‡</td>
      <td>0.812||</td>
      <td>7.326 (7)‡</td>
      <td>0.4§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% High school degree or equivalent</td>
      <td>17.8%</td>
      <td>20.0%</td>
      <td>13.0%</td>
      <td>16.7%</td>
      <td>16.1%</td>
      <td>6.3%</td>
      <td>25.0%</td>
      <td>10.5%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Some college or university, no degree</td>
      <td>22.2%</td>
      <td>30.0%</td>
      <td>24.6%</td>
      <td>22.2%</td>
      <td>17.9%</td>
      <td>25.0%</td>
      <td>25.0%</td>
      <td>26.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Associate degree</td>
      <td>13.3%</td>
      <td>15.0%</td>
      <td>17.4%</td>
      <td>22.2%</td>
      <td>12.5%</td>
      <td>12.5%</td>
      <td>9.4%</td>
      <td>21.1%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Bachelor's degree</td>
      <td>33.3%</td>
      <td>35.0%</td>
      <td>40.6%</td>
      <td>22.2%</td>
      <td>35.7%</td>
      <td>56.3%</td>
      <td>28.1%</td>
      <td>31.6%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Master's degree</td>
      <td>8.9%</td>
      <td>0%</td>
      <td>2.9%</td>
      <td>0%</td>
      <td>14.3%</td>
      <td>0%</td>
      <td>7.8%</td>
      <td>10.5%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Doctorate or professional degree</td>
      <td>4.4%</td>
      <td>0%</td>
      <td>0%</td>
      <td>5.6%</td>
      <td>1.8%</td>
      <td>0%</td>
      <td>1.6%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Completed some postgraduate</td>
      <td>0%</td>
      <td>0%</td>
      <td>1.4%</td>
      <td>5.6%</td>
      <td>1.8%</td>
      <td>0%</td>
      <td>3.1%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Other / not specified</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>5.6%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Income</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>14.961 (18)‡</td>
      <td>.671||</td>
      <td>1.177 (6)‡</td>
      <td>0.981§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Less than $20,000</td>
      <td>24.4%</td>
      <td>25.0%</td>
      <td>24.6%</td>
      <td>33.3%</td>
      <td>17.9%</td>
      <td>37.5%</td>
      <td>23.4%</td>
      <td>15.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>$20,000 to $34,999</td>
      <td>40.0%</td>
      <td>25.0%</td>
      <td>20.3%</td>
      <td>22.2%</td>
      <td>33.9%</td>
      <td>31.3%</td>
      <td>28.1%</td>
      <td>31.6%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>$35,000 to $49,999</td>
      <td>15.6%</td>
      <td>15.0%</td>
      <td>18.8%</td>
      <td>16.7%</td>
      <td>12.5%</td>
      <td>6.3%</td>
      <td>18.8%</td>
      <td>15.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>$50,000 to $74,999</td>
      <td>13.3%</td>
      <td>35.0%</td>
      <td>20.3%</td>
      <td>5.6%</td>
      <td>21.4%</td>
      <td>12.5%</td>
      <td>18.8%</td>
      <td>21.1%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>$75,000 to $99,999</td>
      <td>4.4%</td>
      <td>0%</td>
      <td>7.2%</td>
      <td>11.1%</td>
      <td>8.9%</td>
      <td>6.3%</td>
      <td>7.8%</td>
      <td>15.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Over $100,000</td>
      <td>0%</td>
      <td>0%</td>
      <td>5.8%</td>
      <td>5.6%</td>
      <td>3.6%</td>
      <td>6.3%</td>
      <td>1.6%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Not specified</td>
      <td>2.2%</td>
      <td>0%</td>
      <td>2.9%</td>
      <td>5.6%</td>
      <td>1.8%</td>
      <td>0%</td>
      <td>1.6%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Cognitive Reflection</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>11.922 (9)‡</td>
      <td>0.223||</td>
      <td>7.002 (3)‡</td>
      <td>0.071§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Answering 0/3 correctly</td>
      <td>11.1%</td>
      <td>25.0%</td>
      <td>10.1%</td>
      <td>11.1%</td>
      <td>17.9%</td>
      <td>25.0%</td>
      <td>15.6%</td>
      <td>26.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Answering 1/3 correctly</td>
      <td>4.4%</td>
      <td>5.0%</td>
      <td>15.9%</td>
      <td>11.1%</td>
      <td>8.9%</td>
      <td>25.0%</td>
      <td>14.1%</td>
      <td>15.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Answering 2/3 correctly</td>
      <td>13.3%</td>
      <td>25.0%</td>
      <td>15.9%</td>
      <td>16.7%</td>
      <td>19.6%</td>
      <td>25.0%</td>
      <td>21.9%</td>
      <td>31.6%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Answering 3/3 correctly</td>
      <td>71.1%</td>
      <td>45.0%</td>
      <td>58.0%</td>
      <td>61.1%</td>
      <td>53.6%</td>
      <td>25.0%</td>
      <td>48.4%</td>
      <td>26.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Ethnicity</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>5.162 (3)‡</td>
      <td>0.157§</td>
      <td>3.715 (1)‡</td>
      <td>0.069§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Hispanic, Latino, or Spanish origin</td>
      <td>4.4%</td>
      <td>15.0%</td>
      <td>1.4%</td>
      <td>0%</td>
      <td>8.9%</td>
      <td>6.3%</td>
      <td>1.6%</td>
      <td>15.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Not of Hispanic, Latino, or Spanish origin</td>
      <td>95.6%</td>
      <td>85.0%</td>
      <td>98.6%</td>
      <td>100.0%</td>
      <td>91.1%</td>
      <td>93.8%</td>
      <td>98.4%</td>
      <td>84.2%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Race</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>19.559 (15)‡</td>
      <td>.173||</td>
      <td>9.626 (5)‡</td>
      <td>0.084§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% White</td>
      <td>82.2%</td>
      <td>75.0%</td>
      <td>84.1%</td>
      <td>88.9%</td>
      <td>85.7%</td>
      <td>75.0%</td>
      <td>85.9%</td>
      <td>73.7%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Black or African American</td>
      <td>6.7%</td>
      <td>15.0%</td>
      <td>5.8%</td>
      <td>11.1%</td>
      <td>0%</td>
      <td>12.5%</td>
      <td>4.7%</td>
      <td>10.5%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Asian</td>
      <td>8.9%</td>
      <td>10.0%</td>
      <td>7.2%</td>
      <td>0%</td>
      <td>3.6%</td>
      <td>6.3%</td>
      <td>7.8%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% American Indian or Alaska Native</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>1.8%</td>
      <td>6.3%</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Multiracial</td>
      <td>2.2%</td>
      <td>0%</td>
      <td>1.4%</td>
      <td>0%</td>
      <td>3.6%</td>
      <td>0%</td>
      <td>1.6%</td>
      <td>15.8%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Other / not specified</td>
      <td>0%</td>
      <td>0%</td>
      <td>1.4%</td>
      <td>0%</td>
      <td>5.4%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Mental Health</td>
      <td colspan="14"></td>
    </tr>
    <tr>
      <td>Psychiatric diagnosis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>10.783 (9)‡</td>
      <td>0.292||</td>
      <td>2.960 (3)‡</td>
      <td>0.361§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% No psychiatric diagnosis</td>
      <td>73.3%</td>
      <td>80.0%</td>
      <td>60.9%</td>
      <td>55.6%</td>
      <td>71.4%</td>
      <td>50.0%</td>
      <td>65.6%</td>
      <td>42.1%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Schizophrenia spectrum</td>
      <td>2.2%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>6.3%</td>
      <td>0%</td>
      <td>0%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Mood disorder</td>
      <td>13.3%</td>
      <td>15.0%</td>
      <td>27.5%</td>
      <td>22.2%</td>
      <td>21.4%</td>
      <td>43.8%</td>
      <td>26.6%</td>
      <td>31.6%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Not specified</td>
      <td>11.1%</td>
      <td>5.0%</td>
      <td>11.6%</td>
      <td>22.2%</td>
      <td>7.1%</td>
      <td>0%</td>
      <td>7.8%</td>
      <td>26.3%</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>% Medicated</td>
      <td>8.9%</td>
      <td>10.0%</td>
      <td>13.0%</td>
      <td>22.2%</td>
      <td>7.1%</td>
      <td>31.3%</td>
      <td>14.1%</td>
      <td>10.5%</td>
      <td>3.575 (6)‡</td>
      <td>0.744§</td>
      <td>4.164 (2)‡</td>
      <td>0.121§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Beck's Anxiety Inventory</td>
      <td>0.34 [0.06]</td>
      <td>0.52 [0.14]</td>
      <td>0.31 [0.04]</td>
      <td>0.6 [0.13]</td>
      <td>0.24 [0.04]</td>
      <td>0.90 [0.20]</td>
      <td>0.33 [0.06]</td>
      <td>0.79 [0.18]</td>
      <td>1.244 (3)†</td>
      <td>0.2941</td>
      <td>38.752 (1)††</td>
      <td>1.63E-09</td>
      <td>2.577 (3)††</td>
      <td>0.0539</td>
    </tr>
    <tr>
      <td>Beck's Depression Inventory</td>
      <td>0.36 [0.07]</td>
      <td>0.86 [0.15]</td>
      <td>0.32 [0.05]</td>
      <td>0.79 [0.13]</td>
      <td>0.25 [0.04]</td>
      <td>1.03 [0.19]</td>
      <td>0.38 [0.07]</td>
      <td>1.06 [0.20]</td>
      <td>1.023 (3)†</td>
      <td>0.3827</td>
      <td>74.528 (1)††</td>
      <td>3.62E-16</td>
      <td>1.089 (3)††</td>
      <td>0.3542</td>
    </tr>
    <tr>
      <td>SCID Paranoia Personality Score</td>
      <td>0.11 [0.02]</td>
      <td>0.67 [0.04]</td>
      <td>0.11 [0.02]</td>
      <td>0.61 [0.03]</td>
      <td>0.1 [0.02]</td>
      <td>0.72 [0.04]</td>
      <td>0.11 [0.02]</td>
      <td>0.65 [0.03]</td>
      <td>1.297 (3)†</td>
      <td>0.2756</td>
      <td>879.379 (1)††</td>
      <td>4.81E-91</td>
      <td>2.018 (3)††</td>
      <td>0.1114</td>
    </tr>
    <tr>
      <td>Reversal Learning Performance</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total points earned</td>
      <td>8656.7 [182.9]</td>
      <td>8372.5 [405.2]</td>
      <td>6045.7 [135.7]</td>
      <td>6266.7 [288.0]</td>
      <td>7533.0 [143.8]</td>
      <td>6503.1 [340.6]</td>
      <td>7171.1 [175.6]</td>
      <td>6510.5 [403.6]</td>
      <td>32.288 (3)†</td>
      <td>4.16E-18</td>
      <td>6.175 (1)††</td>
      <td>0.0135</td>
      <td>2.258 (3)††</td>
      <td>0.0818</td>
    </tr>
    <tr>
      <td>Total reversals achieved</td>
      <td>7.2 [0.3]</td>
      <td>6.5 [0.5]</td>
      <td>5.5 [0.3]</td>
      <td>5.7 [0.5]</td>
      <td>6.3 [0.3]</td>
      <td>4.9 [0.8]</td>
      <td>5.9 [0.3]</td>
      <td>4.8 [0.6]</td>
      <td>4.329 (3)†</td>
      <td>0.005</td>
      <td>5.762 (1)††</td>
      <td>0.017</td>
      <td>1.101 (3)††</td>
      <td>0.349</td>
    </tr>
    <tr>
      <td>% Achieving reversals</td>
      <td>100%</td>
      <td>100%</td>
      <td>98.6%</td>
      <td>94.4%</td>
      <td>100%</td>
      <td>87.5%</td>
      <td>96.9%</td>
      <td>94.7%</td>
      <td>2.26 (3)‡</td>
      <td>0.598§</td>
      <td>4.4 (1)‡</td>
      <td>0.058§</td>
      <td>n/a</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>Win-switch rate, block 1 (90-50-10)</td>
      <td>0.09 [0.03]</td>
      <td>0.09 [0.04]</td>
      <td>0.07 [0.01]</td>
      <td>0.11 [0.05]</td>
      <td>0.04 [0.01]</td>
      <td>0.13 [0.05]</td>
      <td>0.1 [0.03]</td>
      <td>0.21 [0.06]</td>
      <td>2.284 (3)†</td>
      <td>0.079</td>
      <td>7.117 (1)††</td>
      <td>0.008</td>
      <td>1.15 (3)††</td>
      <td>0.329</td>
    </tr>
    <tr>
      <td>Win-switch rate, block 2 (80-40-20)</td>
      <td>0.05 [0.02]</td>
      <td>0.08 [0.03]</td>
      <td>0.04 [0.01]</td>
      <td>0.05 [0.04]</td>
      <td>0.02 [0.01]</td>
      <td>0.12 [0.05]</td>
      <td>0.06 [0.02]</td>
      <td>0.15 [0.05]</td>
      <td>2.067 (3)†</td>
      <td>0.105</td>
      <td>9.918 (1)††</td>
      <td>0.002</td>
      <td>1.174 (3)††</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>Lose-stay rate, block 1 (90-50-10)</td>
      <td>0.27 [0.03]</td>
      <td>0.34 [0.05]</td>
      <td>0.37 [0.03]</td>
      <td>0.34 [0.04]</td>
      <td>0.3 [0.03]</td>
      <td>0.39 [0.06]</td>
      <td>0.32 [0.03]</td>
      <td>0.34 [0.04]</td>
      <td>0.561 (3)†</td>
      <td>0.641</td>
      <td>1.834 (1)††</td>
      <td>0.177</td>
      <td>0.754 (3)††</td>
      <td>0.521</td>
    </tr>
    <tr>
      <td>Lose-stay rate, block 2 (80-40-20)</td>
      <td>0.28 [0.03]</td>
      <td>0.23 [0.05]</td>
      <td>0.4 [0.03]</td>
      <td>0.32 [0.05]</td>
      <td>0.33 [0.03]</td>
      <td>0.37 [0.06]</td>
      <td>0.29 [0.03]</td>
      <td>0.33 [0.06]</td>
      <td>2.47 (3)†</td>
      <td>0.062</td>
      <td>0.177 (1)††</td>
      <td>0.674</td>
      <td>0.834 (3)††</td>
      <td>0.476</td>
    </tr>
    <tr>
      <td>Reaction time, block 1</td>
      <td>433.6 [28.8]</td>
      <td>789.3 [282.7]</td>
      <td>548.1 [77.8]</td>
      <td>365.6 [26.4]</td>
      <td>448 [60.1]</td>
      <td>442.1 [59.5]</td>
      <td>557.2 [108.2]</td>
      <td>530 [130.2]</td>
      <td>0.793 (3)†</td>
      <td>0.499</td>
      <td>0.161 (1)††</td>
      <td>0.689</td>
      <td>1.727 (3)††</td>
      <td>0.161</td>
    </tr>
    <tr>
      <td>Reaction time, block 2</td>
      <td>370.7 [23.3]</td>
      <td>494.3 [88.6]</td>
      <td>465.3 [61.6]</td>
      <td>331.4 [22.9]</td>
      <td>391.7 [52.3]</td>
      <td>555.9 [121.2]</td>
      <td>385.4 [29.2]</td>
      <td>504.1 [82.7]</td>
      <td>0.394 (3)†</td>
      <td>0.757</td>
      <td>1.92 (1)††</td>
      <td>0.167</td>
      <td>1.949 (3)††</td>
      <td>0.122</td>
    </tr>
  </tbody>
</table>

_† Univariate analysis, F(df) with df error = 306 Exact test, ‡chi-square coefficient (df), § Exact significance (2-sided), || Monte Carlo significance (2-sided)._

Across task versions, high paranoia participants endorsed higher BAI and BDI scores (n = 73 high paranoia, 234 low paranoia; BAI: F(1, 299)=38.752, p=1.63E-09, ηp2=0.115; BDI: F(1, 299)=74.528, p=3.62E-16, ηp2=0.20; Table 2). Both correlated with paranoia (BAI: Pearson’s r = 0.450, p=1.09E-16, CI=[0.348, 0.55]; BDI: Pearson’s r = 0.543, p=6.26E-25, CI=[0.448, 0.638]). Trial-by-trial reaction time did not differ significantly between low and high paranoia (Table 2), but high paranoia participants earned fewer total points (F(1, 299)=6.175, p=0.014, ηp2=0.020) and achieved fewer reversals (F(1, 299)=5.762, p=0.017, ηp2=0.019; Table 2). Deck choice perseveration after negative feedback (lose-stay behavior) did not significantly differ by paranoia group, but choice switching after positive feedback (win-switch behavior) was elevated in high paranoia (block 1: F(1, 299)=7.117, p=0.008, ηp2=0.023; block 2: F(1, 299)=9.918, p=0.002, ηp2=0.032; Table 2).

### Experiment 3

To translate across species, we performed a new analysis of published data from rats exposed to chronic methamphetamine (Groman et al., 2018). Rats chose between three operant chamber noseports with differing probabilities of sucrose reward (70%, 30%, and 10%; Figure 1d and e). Contingencies switched between the 70% and 10% noseports after selection of the highest reinforced option in 21 out of 30 consecutive trials (Figure 1e). This task was most similar in structure to the first blocks of online versions 2 and 4. There was no increase in unexpected volatility mid-way through the task. Rats were tested for 26 within-session reversal blocks (Pre-Rx, n = 10 per group), administered saline or methamphetamine according to a 23 day schedule mimicking the escalating doses and frequencies of chronic human methamphetamine users (Groman et al., 2018), and tested once per week for four weeks following completion of the drug regimen (Post-Rx; n = 10 saline, seven methamphetamine) (Groman et al., 2018). Relative to rats exposed to saline, those rats exposed to methamphetamine exhibited increased win-switch behavior, similar to what we has observed in the high paranoia human participants, and additionally, unlike humans, they perseverated after negative feedback (Groman et al., 2018).

### Computational modeling

We employed hierarchical Gaussian filter (HGF) modeling to compare belief updating across individuals with low and high paranoia, as well as across human participants and rats exposed to methamphetamine (Table 3). We paired a three-level perceptual model with a softmax decision model dependent upon third level volatility (Figure 2a). We inverted the model from subject data (trial-by-trial choices and feedback) to estimate parameters for each individual (Figure 2b). Level 1 (x1) characterizes trial-by-trial perception of task feedback (win or loss in humans, reward or no reward in rats), Level 2 (x2) distinguishes stimulus-outcome associations (deck or noseport values), and Level 3 (x3) renders perception of the overall task volatility (i.e., frequency of reversal events, changes in the stimulus-outcome associations).

**Table 3.**
 ANOVA results for HGF parameters.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Block effect †</th>
      <th colspan="2">Group effect‡</th>
      <th colspan="2">Interaction effect</th>
    </tr>
    <tr>
      <th></th>
      <th>Statistic§</th>
      <th>p-value</th>
      <th>Statistic§</th>
      <th>p-value</th>
      <th>Statistic§</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">Experiment 1</td>
    </tr>
    <tr>
      <td>ω3</td>
      <td>11.672 (1)</td>
      <td>0.002</td>
      <td>1.294 (1)</td>
      <td>0.264</td>
      <td>6.948 (1)</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>25.904 (1)</td>
      <td>1.809E-5</td>
      <td>7.063 (1)</td>
      <td>0.012</td>
      <td>5.344 (1)</td>
      <td>0.028</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>7.768 (1)</td>
      <td>0.009</td>
      <td>7.599 (1)</td>
      <td>0.010</td>
      <td>0.003 (1)</td>
      <td>0.960</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>2.182 (1)</td>
      <td>0.150</td>
      <td>4.186 (1)</td>
      <td>0.050</td>
      <td>0.058 (1)</td>
      <td>0.811</td>
    </tr>
    <tr>
      <td>µ20</td>
      <td>4.831 (1)</td>
      <td>0.036</td>
      <td>1.261 (1)</td>
      <td>0.270</td>
      <td>0.370 (1)</td>
      <td>0.547</td>
    </tr>
    <tr>
      <td>BIC</td>
      <td>0.061 (1)</td>
      <td>0.807</td>
      <td>8.801 (1)</td>
      <td>0.006</td>
      <td>1.7 (1)</td>
      <td>0.202</td>
    </tr>
    <tr>
      <td colspan="7">Experiment 2, Version 3</td>
    </tr>
    <tr>
      <td>ω3</td>
      <td>14.932 (1)</td>
      <td>0.0002</td>
      <td>1.128 (1)</td>
      <td>0.292</td>
      <td>1.406 (1)</td>
      <td>0.240</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>64.651 (1)</td>
      <td>1.54E-11</td>
      <td>6.366 (1)</td>
      <td>0.014</td>
      <td>0.003 (1)</td>
      <td>0.959</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>15.53 (1)</td>
      <td>0.0002</td>
      <td>13.521 (1)</td>
      <td>0.0005</td>
      <td>0.011 (1)</td>
      <td>0.916</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>0.027 (1)</td>
      <td>0.869</td>
      <td>8.70 (1)</td>
      <td>0.004</td>
      <td>0.090 (1)</td>
      <td>0.765</td>
    </tr>
    <tr>
      <td>µ20</td>
      <td>11.432 (1)</td>
      <td>0.001</td>
      <td>0.030 (1)</td>
      <td>0.864</td>
      <td>0.203 (1)</td>
      <td>0.653</td>
    </tr>
    <tr>
      <td>BIC</td>
      <td>1.110E-5 (1)</td>
      <td>0.997</td>
      <td>16.336 (1)</td>
      <td>0.0001</td>
      <td>1.678 (1)</td>
      <td>0.199</td>
    </tr>
    <tr>
      <td colspan="7">Experiment 3: Rats</td>
    </tr>
    <tr>
      <td>ω3</td>
      <td>30.086 (1)</td>
      <td>6.2785E-5</td>
      <td>4.579 (1)</td>
      <td>0.049</td>
      <td>9.058 (1)</td>
      <td>0.009</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>31.416 (1)</td>
      <td>5.0188E-5</td>
      <td>8.454 (1)</td>
      <td>0.011</td>
      <td>5.159 (1)</td>
      <td>0.038</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>9.132 (1)</td>
      <td>0.009</td>
      <td>13.356 (1)</td>
      <td>0.002</td>
      <td>2.644 (1)</td>
      <td>0.125</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>32.192 (1)</td>
      <td>4.4173E-5</td>
      <td>22.344 (1)</td>
      <td>0.0003</td>
      <td>18.454 (1)</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>µ20</td>
      <td>5.226 (1)</td>
      <td>0.037</td>
      <td>0.368 (1)</td>
      <td>0.553</td>
      <td>2.087 (1)</td>
      <td>0.169</td>
    </tr>
    <tr>
      <td>BIC</td>
      <td>5.052 (1)</td>
      <td>0.040</td>
      <td>1.890 (1)</td>
      <td>0.189</td>
      <td>0.331 (1)</td>
      <td>0.573</td>
    </tr>
  </tbody>
</table>

_Block refers to first versus second half in human studies, Pre-Rx vs Post-Rx in rat studies.‡ Group refers to low versus high paranoia in humans, saline versus methamphetamine in rats §F-statistic (degrees of freedom); df error = 30 in Experiment 1, 70 in Experiment 2, Version 3, and 50 in Experiment 3: Rats; split-plot ANOVA (i.e., repeated measures with between-subjects factor)._

![Figure 2.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig2-v4.jpg)

**Figure 2.:** (a) 3-level HGF perceptual model (blue) with a softmax decision model (green). Level 1 (x1): trial-by-trial perception of win or loss feedback. Level 2 (x2): stimulus-outcome associations (i.e., deck values). Level 3 (x3): perception of the overall reward contingency context. The impact of phasic volatility upon x2 is captured by κ (i.e., coupling). Tonic volatility modulates x3 and x2 via ω3 and ω2, respectively. μ30 is the initial value of the third level volatility belief. (b) HGF model parameter estimates from each of our three studies (in laboratory, online, rat - columns), ω3, μ30, κ, and ω2, displayed hierarchically, in rows, in parallel with the position of the particular parameter in the model depiction in a). Parameters replicate across high paranoia groups in the in-laboratory experiment (n = 21 low paranoia [gray], 11 high paranoia [orange]; dark bars are initial task blocks, lighter bars follow the contingency transition); the analogous online task (version 3, n = 56 low paranoia [gray], 16 high paranoia [orange]; dark bars are initial task blocks, lighter bars follow the contingency transition); and rats exposed to chronic, escalating saline or methamphetamine (n = 10 per group, Pre-Rx [dark gray]; Post-Rx, n = 10 saline [light gray], seven methamphetamine [orange]). Center lines depict medians; box limits indicate the 25th and 75th percentiles; whiskers extend 1.5 times the interquartile range from the 25th and 75th percentiles, outliers are represented by dots; crosses represent sample means; data points are plotted as open circles. *p≤0.05, **p≤0.01, ***p≤0.001.

Belief trajectories were unique to each subject due to the probabilistic, performance-dependent nature of the task, so we estimated initial beliefs (priors) for x2 and x3 (μ20 and μ30, respectively). We also estimated ω2, the tonic volatility of stimulus-outcome associations. Lower ω2 indicates that subjects are slower to adjust beliefs about the value of each option; they maintain rigid beliefs about the underlying probabilities. The κ parameter captures the impact of phasic volatility on updating stimulus-outcome associations. In the setting of our experiments, κ approximates the influence of unexpected uncertainty. Higher κ implies faster updating of stimulus-outcome associations – that is, participants are more likely perceive volatility as reversal events. Our final parameter of interest, ω3, characterizes perception of ‘meta-volatility,’ such as changes in the frequency of reversal events (Lawson et al., 2017). The lower ω3, the slower a subject is to adjust their volatility belief; they adhere more rigidly to their volatility prior (μ30).

Priors did not differ between groups at x2 (Table 3) but paranoid individuals and rats exposed to methamphetamine exhibited elevated μ30, they expected greater task volatility (Figure 2b, blue). In Experiment 1, we observed an interaction between task block and paranoia group (F(1, 30)=5.344, p=0.028, ηp2=0.151; Table 1): μ30 differed between high and low paranoia in both blocks (block 1, F(1, 30)=4.232, p=0.048, ηp2=0.124, MD = 0.658, CI=[0.005,1.312]; block 2, F(1, 30)=7.497, p=0.010, ηp2=0.20, MD = 1.598, CI=[0.406, 2.789]), but only low paranoia subjects significantly updated their priors between block 1 and block 2 (F(1, 30)=39.841, p=5.85E-07, ηp2=0.570, MD = 1.504, CI=[1.017, 1.99]). In Experiment 2, the analogous task design (version 3) demonstrated significant effects of block (F(1, 70)=64.652, p=1.54E-11, ηp2=0.480, MD = 1.303, CI=[0.980,1.627]) and paranoia (F(1, 70)=6.366, p=0.014, ηp2=0.083, MD = 0.909, CI=[0.191, 1.628]; Table 1). Rats showed a similar effect following methamphetamine exposure with a significant time (Pre-Rx, Post-Rx) by treatment (methamphetamine, saline) interaction (F(1, 15)=5.159, p=0.038, ηp2=0.256; pre versus post methamphetamine effect: F(1, 15)=12.186, p=0.003, MD = 1.265, CI=[−0.493, 2.037]; Pre-Rx mean [standard error]=−1.25 [0.56] saline, −0.77 [0.80] methamphetamine; Post-Rx: m = −0.69 [0.74] saline, 0.58 [0.73] methamphetamine). Random effects meta-analyses confirmed significant cross-experiment replication of elevated μ30 in human participants with paranoia (in laboratory and online version 3; MDMETA = 1.110, CI=[0.927, 1.292], zMETA = 11.929, p=8.356E-33) and across humans with paranoia and rats exposed to methamphetamine (MDMETA = 2.090, CI=[0.123, 4.056], zMETA = 2.083, p=0.037). Both paranoid humans and rats administered chronic methamphetamine had strong beliefs that the task contingencies would change rapidly and unpredictably – in other words, they expected frequent reversal events. Methamphetamine exposure made rats behave like humans with high paranoia (Figure 2b, Post-Rx condition, orange). This is particularly striking when compared to human data from the first task block (before contingency transition), when task designs are most similar across experiments.

Paranoid participants and methamphetamine exposed rats updated stimulus-outcome associations more strongly in response to perceived volatility (e.g., correctly or incorrectly inferred reversals; Figure 2b). κ showed significant paranoia group and block effects across the in laboratory experiment and online version 3 (Table 1; paranoia effects, in laboratory: F(1, 30)=7.599, p=0.010, ηp2=0.202, MD = 0.081, CI=[0.021, 0.140]; online version 3: F(1, 70)=13.521, p=0.0005, ηp2=0.162, MD = 0.068, CI=[0.031–0.104]; MDMETA = 0.079, CI=[0.063, 0.095], zMETA = 9.502 p=2.067E-21); see Table 3 for block effects). κ increased from baseline in rats on methamphetamine, yielding significant effects of treatment (F(1, 15)=13.356, p=0.002, ηp2=0.471, MD = 0.045, CI=[0.019, 0.072]) and time (F(1, 15)=9.132, p=0.009, ηp2=0.378, MD = 0.041, CI=[0.012, 0.069]); however, the interaction between time and treatment did not reach statistical significance (Table 3; Pre-Rx m = 0.499 [0.015] saline, 0.523 [0.040] methamphetamine; Post-Rx: m = 0.518 [0.053] saline, 0.585 [0.029] methamphetamine). Replication of group effects was significant across all three experiments (MDMETA = 2.063, CI=[0.341, 3.785], zMETA = 2.348, p=0.019). Thus, learning was more strongly driven by unexpected uncertainty in high paranoia participants and rats chronically administered methamphetamine; they were faster to interpret volatility as reversal events than their low paranoia and saline exposed counterparts.

Expected uncertainty (ω2) was decreased in paranoid participants and rats exposed to methamphetamine (Figure 2b). In laboratory and online (version 3), paranoid individuals were slower to update stimulus-outcome associations in response to expected uncertainty (Table 1; ω2 paranoia effect, in laboratory: F(1, 30)=4.186, p=0.050, ηp2=0.122, MD = −1.188, CI=[−2.375,–0.002]; online version 3: F(1, 70)=8.7, p=0.004, ηp2=0.111, MD = −0.993, CI=[−1.665,–0.322]; MDMETA = −1.154, CI=[−1.455,–0.853], zMETA = −7.521, p=5.450E-14). The effects of methamphetamine exposure in rats were consistent (MDMETA = −1.992, CI=[−3.318,–0.665], zMETA = −2.943, p=0.003) yet more striking, with a strongly negative ω2 accounting for the more pronounced lose-stay behavior or perseveration in rats (time by treatment interaction, F(1, 15)=18.454, p=0.001, ηp2=0.552; pre versus post methamphetamine: F(1, 15)=42.242, p=1.0E-522, ηp2=0.738, MD = −1.604, CI=[−2.130,–1.078]; Pre-Rx m = 0.198 [0.33] saline, −0.036 [0.42] methamphetamine; Post-Rx: m = −0.023 [0.56] saline, −1.640 [0.71] methamphetamine). High paranoia humans and rats exposed to methamphetamine maintained rigid beliefs about the underlying option probabilities relative to low paranoia and saline controls. This was associated with perseverative behavior in the rats but not in humans.

Meta-volatility learning (ω3) was similarly decreased across paranoia and methamphetamine exposed groups (in laboratory, online version 3, and rats: MDMETA = −1.155, CI=[−2.139,–0.171], zMETA = −2.3, p=0.021), suggesting more reliance on expected task volatility (i.e., anticipated frequency of reversal events) than on actual task feedback. In laboratory, we observed a block by paranoia group interaction (Table 1, F(1, 30)=6.948, p=0.010, ηp2=0.188). Post-hoc tests differentiated first and second blocks for the low paranoia group only (F(1, 30)=26.640, p=1.5E-5, ηp2=0.470, MD = −0.876, CI=[−1.222,–0.529]). The paranoia effect did not reach statistical significance for online version 3 (block effect only, F(1, 70)=14.932, p=0.0002, ηp2=0.176, MD = −0.692, CI=[−1.050,–0.335]; Table 3), but meta-analytic random effects analysis confirms a significant paranoia group difference (in laboratory and online version 3: MDMETA = −0.341, CI=[−0.522,–0.159], zMETA = −3.68, p=0.0002). Methamphetamine exposure rendered ω3 more negative in rats (time by treatment interaction, (F(1, 15)=9.058, p=0.009, ηp2=0.376; pre versus post methamphetamine: F(1, 15)=30.668, p=5.7E-5, ηp2=0.672, MD = −1.210, CI=[−1.676,–0.745]; Pre-Rx m = −0.692 [0.44] saline, −0.607 [0.51] methamphetamine; Post-Rx: m = −1.044 [0.44] saline, −1.817 [0.32] methamphetamine). These data indicate that paranoia and methamphetamine are associated with slower learning about changes in task volatility, suggesting greater reliance on volatility priors than task feedback.

In summary, our modeling analyses suggest the following about paranoia in humans and methamphetamine exposed animals: they expect the task to be volatile (high μ30), their expectations about task volatility are more rigid (low ω3), and they confuse probabilistic errors and task volatility as a signal that the task has fundamentally changed (high κ, low ω2).

We applied False Discovery Rate (FDR) correction for multiple comparisons of each model parameter (Hochberg and Benjamini, 1990). κ group effects survived corrections within each experiment (Table 4). In addition to κ, μ30 survived for experiment 1; μ30 and ω2 survived in online version 3; and μ30, ω2, and ω3 survived in experiment three as group effects. Such correction is not yet standard practice with this modeling approach (Lawson et al., 2017; Powers et al., 2017; Sevgi et al., 2016) but we believe it should be, and when effects survive correction we should increase our confidence in them.

**Table 4.**
 Corrections for multiple comparisons.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">Group effect †</th>
      <th colspan="4">Interaction effect‡</th>
    </tr>
    <tr>
      <th></th>
      <th>Survives bonferroni?§</th>
      <th>Survives FDR?</th>
      <th>Critical value</th>
      <th>Benjamini-Hochberg p-value</th>
      <th>Survives bonferroni?§</th>
      <th>Survives FDR?</th>
      <th>Critical value</th>
      <th>Benjamini-Hochberg p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Experiment 1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ω3</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.05</td>
      <td>0.264</td>
      <td>No</td>
      <td>No</td>
      <td>0.0125</td>
      <td>0.052</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.025</td>
      <td>0.024</td>
      <td>No</td>
      <td>No</td>
      <td>0.025</td>
      <td>0.056</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.0125</td>
      <td>0.04</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.05</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>No</td>
      <td>No</td>
      <td>0.0375</td>
      <td>0.0667</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.0375</td>
      <td>1.081</td>
    </tr>
    <tr>
      <td>Experiment 2, Version 3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ω3</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.05</td>
      <td>0.292</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.0125</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>No</td>
      <td>Yes</td>
      <td>3.75E-02</td>
      <td>0.0187</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.05</td>
      <td>0.959</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.0125</td>
      <td>0.002</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.0375</td>
      <td>1.221</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.025</td>
      <td>0.008</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.025</td>
      <td>1.53</td>
    </tr>
    <tr>
      <td>Experiment 3: Rats</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ω3</td>
      <td>No</td>
      <td>Yes</td>
      <td>5.00E-02</td>
      <td>0.049</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.025</td>
      <td>0.018</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>3.75E-02</td>
      <td>0.0147</td>
      <td>No</td>
      <td>No</td>
      <td>0.0375</td>
      <td>0.0507</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.025</td>
      <td>0.004</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.05</td>
      <td>0.125</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.0125</td>
      <td>0.0012</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.0125</td>
      <td>0.004</td>
    </tr>
  </tbody>
</table>

_N/A denotes to p-values that were not significant before corrections. † Low versus high paranoia in humans, saline versus methamphetamine in rats. ‡ Group by time (i.e., first versus second half in human studies, Pre-Rx vs Post-Rx in rat studies). § p-value < 0.0125._

### Paranoia effects across task versions

To examine the relationship between beliefs about contingency transition and paranoia within our HGF parameters, we performed split-plot, repeated measures ANOVAs across all four task versions. Paranoia group effects were specific to versions of the task in which we explicitly manipulated uncertainty via contingency transition which increased volatility (Figure 3, Table 5, versions 3 and 4). Specifically, we observed paranoia by version interactions for κ (F(3, 299)=4.178, p=0.006, ηp2=0.040) and ω2 (F(3, 299)=2.809, p=0.040, ηp2=0.027; Table 2). Post-hoc tests confirmed that significant paranoia group effects were restricted to version 3 (κ: F(1, 299)=12.230, p=0.001, ηp2=0.039, MD = 0.068, CI=[0.03,0.106]; ω2: F(1, 299)=8.734, p=0.003, ηp2=0.028, MD = −0.993, CI=[−1.655,–0.332]) and a trend for version 4 (ω2: F(1, 299)=2.909, p=0.089, ηp2=0.010, MD = −0.528, CI=[−1.138, 0.081], Figure 3a). μ30 also exhibited a paranoia by version trend (Table 2, F(3, 299)=2.329, p=0.075, ηp2=0.023), largely driven by version 3 (F(1, 299)=6.206, p=0.013, ηp2=0.020, MD = 0.909, CI=[0.191, 1.628]; Figure 3a). There were no significant paranoia effects or interactions for ω3 (Table 5). In sum, our contingency shift manipulation – from easily discerned options to underlying probabilities that are closer together – increased unexpected uncertainty the most, particularly in highly paranoid participants, compared to the other task versions.

**Table 5.**
 Experiment 2 effects across block, paranoia group, and task version.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Block</th>
      <th colspan="2">Group</th>
      <th colspan="2">Version</th>
      <th colspan="2">Block*group* Version</th>
      <th colspan="2">Group*version</th>
      <th colspan="2">Block*group</th>
      <th colspan="2">Block*version</th>
    </tr>
    <tr>
      <th></th>
      <th>F (df)†</th>
      <th>P</th>
      <th>F (df)†</th>
      <th>P</th>
      <th>F (df)†</th>
      <th>P</th>
      <th>F (df)†</th>
      <th>P</th>
      <th>F (df)†</th>
      <th>P</th>
      <th>F (df)†</th>
      <th>P</th>
      <th>F (df)†</th>
      <th>P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ω3</td>
      <td>3.722 (1)</td>
      <td>0.055</td>
      <td>0.499 (1)</td>
      <td>0.481</td>
      <td>2.061 (3)</td>
      <td>0.105</td>
      <td>0.415 (3)</td>
      <td>0.742</td>
      <td>1.005 (3)</td>
      <td>0.391</td>
      <td>0.145 (1)</td>
      <td>0.704</td>
      <td>7.0155 (3)</td>
      <td>1.42E-4</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>288.1 (1)</td>
      <td>1.01E-45</td>
      <td>2.604 (1)</td>
      <td>0.108</td>
      <td>2.321 (3)</td>
      <td>0.075</td>
      <td>0.261 (3)</td>
      <td>0.853</td>
      <td>2.329 (3)</td>
      <td>0.075</td>
      <td>0.281 (1)</td>
      <td>0.597</td>
      <td>0.061 (3)</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>120.9 (1)</td>
      <td>7.65E-24</td>
      <td>3.602 (1)</td>
      <td>0.059</td>
      <td>5.06 (3)</td>
      <td>0.002</td>
      <td>0.08 (3)</td>
      <td>0.971</td>
      <td>4.178 (3)</td>
      <td>0.006</td>
      <td>1.028 (1)</td>
      <td>0.312</td>
      <td>2.559 (3)</td>
      <td>0.055</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>35.3 (1)</td>
      <td>7.92E-9</td>
      <td>4.435 (1)</td>
      <td>0.036</td>
      <td>4.155 (3)</td>
      <td>0.007</td>
      <td>0.166 (3)</td>
      <td>0.919</td>
      <td>2.809 (3)</td>
      <td>0.04</td>
      <td>2.387 (1)</td>
      <td>0.123</td>
      <td>8.697 (3)</td>
      <td>1.5E-5</td>
    </tr>
    <tr>
      <td>µ20</td>
      <td>71.3 (1)</td>
      <td>1.33E-15</td>
      <td>0.242 (1)</td>
      <td>0.623</td>
      <td>0.616 (3)</td>
      <td>0.605</td>
      <td>1.081 (3)</td>
      <td>0.358</td>
      <td>0.412 (3)</td>
      <td>0.744</td>
      <td>0.057 (1)</td>
      <td>0.812</td>
      <td>1.505 (3)</td>
      <td>0.213</td>
    </tr>
    <tr>
      <td>BIC</td>
      <td>56.6 (1)</td>
      <td>6.23E-13</td>
      <td>8.073 (1)</td>
      <td>0.005</td>
      <td>5.385 (3)</td>
      <td>0.001</td>
      <td>0.262 (3)</td>
      <td>0.853</td>
      <td>4.927 (3)</td>
      <td>0.002</td>
      <td>0.451 (1)</td>
      <td>0.502</td>
      <td>11.905 (3)</td>
      <td>2.19E-07</td>
    </tr>
  </tbody>
</table>

_† F-statistic (degrees of freedom); df error = 299; split-plot ANOVA (i.e., repeated measures with two between-subjects factors).N/A denotes to p-values that were not significant before corrections. † Low versus high paranoia in humans, saline versus methamphetamine in rats. ‡ Group by time (i.e., first versus second half in human studies, Pre-Rx vs Post-Rx in rat studies). § p-value < 0.0125._

![Figure 3.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig3-v4.jpg)

**Figure 3.:** (a) Estimated model parameters derived from participant choices in response to the tasks. Low paranoia is shown in gray, high paranoia is shown in orange. μ30, κ, and ω2 are shown in separate panels (top, middle, and bottom panels, respectively; y-axes). X-axes depict each separate online task version from Experiment 2 (version 1: Easy-Easy, version 2: Hard-Hard, version 3: Easy-Hard, version 4: Hard-Easy). (b) Behavior. Win-switch rate (top): paranoid participants switched between decks more frequently after positive feedback. Rates are collapsed across all task versions and blocks (paranoia group effect; n = 234 low paranoia [gray], 73 high paranoia [orange]). U-value (bottom): a measure of choice stochasticity, calculated for low (gray) and high (orange) paranoia participants and collapsed across task blocks. U-values are shown separately for each online task version (1 through 4, as in part a). In versions 3 and 4 only (the versions containing unsignaled contingency transitions), paranoid participants showed higher U-values, suggesting increasingly stochastic switching rather than perseverative returns to a previously rewarding option. Center lines show the medians; box limits indicate the 25th and 75th percentiles; whiskers extend 1.5 times the interquartile range from the 25th and 75th percentiles, outliers are represented by dots; crosses represent sample means; data points are plotted as open circles. P-values correspond to estimated marginal means post-hoc comparisons: *p≤0.05, **p≤0.01, ***p≤0.001.

### Covariate analyses

We completed three ANCOVAs for each HGF parameter derived from Experiment 2: demographics (age, gender, ethnicity, and race); mental health factors (medication usage, diagnostic category, BAI score, and BDI score); and metrics and correlates of global cognitive ability (educational attainment, income, and cognitive reflection; Tables 6 and 7). For κ, our metric of unexpected uncertainty, the paranoia by version interaction remained robust across all three ANCOVAs (demographics: F(3, 294)=3.753, p=0.011, ηp2=0.037; mental health: F(3, 257)=4.417, p=0.005, ηp2=0.049; cognitive: F(3, 290)=4.304, p=0.005 ηp2=0.043). The paranoia by version trend of μ30 diminished with inclusion of demographic, mental health, and cognitive covariates (demographic: F(3, 294)=1.997, p=0.119, ηp2=0.020; mental health: F(3, 257)=1.942, p=0.123, ηp2=0.022; cognitive: F(3, 290)=2.193, p=0.089, ηp2=0.022). The paranoia by version interaction for ω2 was robust to mental health and cognitive factors (F(3, 257)=3.617, p=0.014, ηp2=0.041; F(3, 290)=3.017, p=0.030, ηp2=0.030). A paranoia group effect and paranoia by version trend remained with inclusion of demographics (ω2, paranoia effect: F(1, 294)=4.275, p=0.040, ηp2=0.014; interaction: F(3, 294)=2.507, p=0.059, ηp2=0.025). Thus κ – participants’ perception of unexpected uncertainty – was the only parameter whose main effect of paranoia (higher κ in high paranoia participants) and paranoia-by-version interaction (higher κ in high paranoia participants as a function of increasing unexpected volatility in version 3) survived covariation for demographic, mental health and cognitive covariates. We are most confident that high paranoia participants have higher unexpected uncertainty which drives their excessive updating of stimulus-outcome associations.

**Table 6.**
 Experiment 2 ANCOVAs.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">ω3</th>
      <th colspan="2">µ30</th>
      <th colspan="2">κ</th>
      <th colspan="2">ω2</th>
    </tr>
    <tr>
      <th>Effect</th>
      <th>Df</th>
      <th>F</th>
      <th>p-value</th>
      <th>F</th>
      <th>p-value</th>
      <th>F</th>
      <th>p-value</th>
      <th>F</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="10">Demographics (age, gender, ethnicity, and race)</td>
    </tr>
    <tr>
      <td>Block</td>
      <td>1, 294</td>
      <td>0.328</td>
      <td>0.568</td>
      <td>10.835</td>
      <td>0.001</td>
      <td>3.425</td>
      <td>0.066</td>
      <td>2.711</td>
      <td>0.101</td>
    </tr>
    <tr>
      <td>Block * Age</td>
      <td>1, 294</td>
      <td>0.659</td>
      <td>0.418</td>
      <td>2.035</td>
      <td>0.155</td>
      <td>2.195</td>
      <td>0.14</td>
      <td>0.212</td>
      <td>0.646</td>
    </tr>
    <tr>
      <td>Block * Gender</td>
      <td>1, 294</td>
      <td>0.363</td>
      <td>0.547</td>
      <td>0.105</td>
      <td>0.746</td>
      <td>4.042</td>
      <td>0.046</td>
      <td>0.096</td>
      <td>0.757</td>
    </tr>
    <tr>
      <td>Block * Ethnicity</td>
      <td>1, 294</td>
      <td>0.016</td>
      <td>0.901</td>
      <td>0.042</td>
      <td>0.837</td>
      <td>0.268</td>
      <td>0.605</td>
      <td>0.024</td>
      <td>0.876</td>
    </tr>
    <tr>
      <td>Block * Race</td>
      <td>1, 294</td>
      <td>3.244</td>
      <td>0.073</td>
      <td>0.279</td>
      <td>0.598</td>
      <td>0.082</td>
      <td>0.775</td>
      <td>1.386</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>Block * Paranoia Group</td>
      <td>1, 294</td>
      <td>0.001</td>
      <td>0.969</td>
      <td>0.162</td>
      <td>0.687</td>
      <td>0.738</td>
      <td>0.391</td>
      <td>1.189</td>
      <td>0.277</td>
    </tr>
    <tr>
      <td>Block * Version</td>
      <td>3, 294</td>
      <td>7.61</td>
      <td>7.25E-05</td>
      <td>0.561</td>
      <td>0.641</td>
      <td>2.568</td>
      <td>0.055</td>
      <td>8.613</td>
      <td>1.97E-05</td>
    </tr>
    <tr>
      <td>Block * Paranoia Group * Version</td>
      <td>3, 294</td>
      <td>0.451</td>
      <td>0.717</td>
      <td>0.135</td>
      <td>0.939</td>
      <td>0.119</td>
      <td>0.949</td>
      <td>0.1</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>Age</td>
      <td>1, 294</td>
      <td>3.054</td>
      <td>0.082</td>
      <td>2.974</td>
      <td>0.086</td>
      <td>2.101</td>
      <td>0.149</td>
      <td>2.339</td>
      <td>0.128</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>1, 294</td>
      <td>0.438</td>
      <td>0.509</td>
      <td>0.02</td>
      <td>0.886</td>
      <td>0.005</td>
      <td>0.941</td>
      <td>0.014</td>
      <td>0.905</td>
    </tr>
    <tr>
      <td>Ethnicity</td>
      <td>1, 294</td>
      <td>0.029</td>
      <td>0.865</td>
      <td>0.059</td>
      <td>0.808</td>
      <td>0.087</td>
      <td>0.768</td>
      <td>0.221</td>
      <td>0.639</td>
    </tr>
    <tr>
      <td>Race</td>
      <td>1, 294</td>
      <td>0.072</td>
      <td>0.789</td>
      <td>2.218</td>
      <td>0.138</td>
      <td>0.373</td>
      <td>0.542</td>
      <td>0.333</td>
      <td>0.564</td>
    </tr>
    <tr>
      <td>Paranoia Group</td>
      <td>1, 294</td>
      <td>4.71E-04</td>
      <td>0.983</td>
      <td>0.741</td>
      <td>0.39</td>
      <td>1.795</td>
      <td>0.182</td>
      <td>3.302</td>
      <td>0.071</td>
    </tr>
    <tr>
      <td>Version</td>
      <td>3, 294</td>
      <td>1.845</td>
      <td>0.14</td>
      <td>1.914</td>
      <td>0.128</td>
      <td>4.975</td>
      <td>0.002</td>
      <td>3.786</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>Paranoia Group * Version</td>
      <td>3, 294</td>
      <td>0.935</td>
      <td>0.424</td>
      <td>1.911</td>
      <td>0.129</td>
      <td>3.599</td>
      <td>0.014</td>
      <td>1.919</td>
      <td>0.127</td>
    </tr>
    <tr>
      <td colspan="10">Mental health factors (medication usage, diagnostic category, BAI score, and BDI score)</td>
    </tr>
    <tr>
      <td>Block</td>
      <td>1, 257</td>
      <td>3.333</td>
      <td>0.069</td>
      <td>95.753</td>
      <td>3.12E-19</td>
      <td>25.498</td>
      <td>8.78E-07</td>
      <td>8.341</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>Block * BAI</td>
      <td>1, 257</td>
      <td>0.26</td>
      <td>0.611</td>
      <td>1.532</td>
      <td>0.217</td>
      <td>2.852</td>
      <td>0.093</td>
      <td>0.394</td>
      <td>0.531</td>
    </tr>
    <tr>
      <td>Block * BDI</td>
      <td>1, 257</td>
      <td>0.009</td>
      <td>0.926</td>
      <td>0.208</td>
      <td>0.649</td>
      <td>6.55</td>
      <td>0.011</td>
      <td>0.597</td>
      <td>0.441</td>
    </tr>
    <tr>
      <td>Block * Medication Usage</td>
      <td>1, 257</td>
      <td>0.027</td>
      <td>0.87</td>
      <td>1.288</td>
      <td>0.258</td>
      <td>0.691</td>
      <td>0.407</td>
      <td>0.871</td>
      <td>0.352</td>
    </tr>
    <tr>
      <td>Block * Diagnostic Category</td>
      <td>1, 257</td>
      <td>1.366</td>
      <td>0.244</td>
      <td>1.785</td>
      <td>0.183</td>
      <td>0.063</td>
      <td>0.803</td>
      <td>0.208</td>
      <td>0.649</td>
    </tr>
    <tr>
      <td>Block * Paranoia Group</td>
      <td>1, 257</td>
      <td>0.068</td>
      <td>0.795</td>
      <td>0.298</td>
      <td>0.586</td>
      <td>0.298</td>
      <td>0.586</td>
      <td>0.007</td>
      <td>0.935</td>
    </tr>
    <tr>
      <td>Block * Version</td>
      <td>3, 257</td>
      <td>5.872</td>
      <td>0.001</td>
      <td>0.531</td>
      <td>0.662</td>
      <td>0.906</td>
      <td>0.439</td>
      <td>6.16</td>
      <td>0.0005</td>
    </tr>
    <tr>
      <td>Block * Paranoia Group * Version</td>
      <td>3, 257</td>
      <td>1.024</td>
      <td>0.383</td>
      <td>0.869</td>
      <td>0.458</td>
      <td>0.266</td>
      <td>0.85</td>
      <td>0.095</td>
      <td>0.963</td>
    </tr>
    <tr>
      <td>BAI</td>
      <td>1, 257</td>
      <td>1.108</td>
      <td>0.294</td>
      <td>0.012</td>
      <td>0.913</td>
      <td>0.954</td>
      <td>0.33</td>
      <td>0.921</td>
      <td>0.338</td>
    </tr>
    <tr>
      <td>BDI</td>
      <td>1, 257</td>
      <td>0.037</td>
      <td>0.848</td>
      <td>0.574</td>
      <td>0.449</td>
      <td>1.343</td>
      <td>0.248</td>
      <td>2.372</td>
      <td>0.125</td>
    </tr>
    <tr>
      <td>Medication Usage</td>
      <td>1, 257</td>
      <td>0.327</td>
      <td>0.568</td>
      <td>0.058</td>
      <td>0.81</td>
      <td>0.002</td>
      <td>0.966</td>
      <td>0.467</td>
      <td>0.495</td>
    </tr>
    <tr>
      <td>Diagnostic Category</td>
      <td>1, 257</td>
      <td>4.252</td>
      <td>0.04</td>
      <td>0.004</td>
      <td>0.949</td>
      <td>1.443</td>
      <td>0.231</td>
      <td>1.743</td>
      <td>0.188</td>
    </tr>
    <tr>
      <td>Paranoia Group</td>
      <td>1, 257</td>
      <td>0.057</td>
      <td>0.811</td>
      <td>0.233</td>
      <td>0.63</td>
      <td>1.032</td>
      <td>0.311</td>
      <td>1.695</td>
      <td>0.194</td>
    </tr>
    <tr>
      <td>Version</td>
      <td>3, 257</td>
      <td>3.183</td>
      <td>0.025</td>
      <td>2.73</td>
      <td>0.045</td>
      <td>5.274</td>
      <td>0.002</td>
      <td>4.468</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>Paranoia Group * Version</td>
      <td>3, 257</td>
      <td>0.311</td>
      <td>0.818</td>
      <td>2.307</td>
      <td>0.077</td>
      <td>4.556</td>
      <td>0.004</td>
      <td>3.397</td>
      <td>0.019</td>
    </tr>
    <tr>
      <td colspan="10">Global cognitive ability (educational attainment, income, and cognitive reflection)</td>
    </tr>
    <tr>
      <td>Block</td>
      <td>1, 290</td>
      <td>1.19E-04</td>
      <td>0.991</td>
      <td>51.264</td>
      <td>7.60E-12</td>
      <td>28.675</td>
      <td>1.83E-07</td>
      <td>18.388</td>
      <td>2.51E-05</td>
    </tr>
    <tr>
      <td>Block * Education</td>
      <td>1, 290</td>
      <td>0.603</td>
      <td>0.438</td>
      <td>0.001</td>
      <td>0.975</td>
      <td>0.033</td>
      <td>0.856</td>
      <td>0.258</td>
      <td>0.612</td>
    </tr>
    <tr>
      <td>Block * Income</td>
      <td>1, 290</td>
      <td>1.211</td>
      <td>0.272</td>
      <td>2.874</td>
      <td>0.091</td>
      <td>3.483</td>
      <td>0.063</td>
      <td>2.421</td>
      <td>0.121</td>
    </tr>
    <tr>
      <td>Block * Cognitive Reflection</td>
      <td>1, 290</td>
      <td>1.83</td>
      <td>0.177</td>
      <td>0.709</td>
      <td>0.401</td>
      <td>1.221</td>
      <td>0.27</td>
      <td>4.667</td>
      <td>0.032</td>
    </tr>
    <tr>
      <td>Block * Paranoia Group</td>
      <td>1, 290</td>
      <td>0.005</td>
      <td>0.946</td>
      <td>0.359</td>
      <td>0.55</td>
      <td>0.263</td>
      <td>0.608</td>
      <td>0.885</td>
      <td>0.348</td>
    </tr>
    <tr>
      <td>Block * Version</td>
      <td>3, 290</td>
      <td>8.861</td>
      <td>1.27E-05</td>
      <td>0.182</td>
      <td>0.909</td>
      <td>2.325</td>
      <td>0.075</td>
      <td>8.815</td>
      <td>1.35E-05</td>
    </tr>
    <tr>
      <td>Block * Paranoia Group * Version</td>
      <td>3, 290</td>
      <td>0.826</td>
      <td>0.48</td>
      <td>0.478</td>
      <td>0.698</td>
      <td>0.15</td>
      <td>0.929</td>
      <td>0.3</td>
      <td>0.825</td>
    </tr>
    <tr>
      <td>Education</td>
      <td>1, 290</td>
      <td>0.111</td>
      <td>0.739</td>
      <td>0.578</td>
      <td>0.448</td>
      <td>1.395</td>
      <td>0.239</td>
      <td>0.608</td>
      <td>0.436</td>
    </tr>
    <tr>
      <td>Income</td>
      <td>1, 290</td>
      <td>2.763</td>
      <td>0.098</td>
      <td>1.382</td>
      <td>0.241</td>
      <td>0.055</td>
      <td>0.814</td>
      <td>1.035</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>Cognitive Reflection</td>
      <td>1, 290</td>
      <td>0.164</td>
      <td>0.686</td>
      <td>12.807</td>
      <td>0.0004</td>
      <td>0.224</td>
      <td>0.636</td>
      <td>0.807</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>Paranoia Group</td>
      <td>1, 290</td>
      <td>0.069</td>
      <td>0.793</td>
      <td>0.555</td>
      <td>0.457</td>
      <td>2.477</td>
      <td>0.117</td>
      <td>4.715</td>
      <td>0.031</td>
    </tr>
    <tr>
      <td>Version</td>
      <td>3, 290</td>
      <td>2.104</td>
      <td>0.1</td>
      <td>2.55</td>
      <td>0.056</td>
      <td>5.53</td>
      <td>0.001</td>
      <td>3.799</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>Paranoia Group * Version</td>
      <td>3, 290</td>
      <td>1.288</td>
      <td>0.279</td>
      <td>2.568</td>
      <td>0.055</td>
      <td>4.469</td>
      <td>0.004</td>
      <td>2.793</td>
      <td>0.041</td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Modified Cognitive Reflection Questionnaire Items.


<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Prompt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>A folder and a paper clip cost $1.10 in total. The folder costs $1.00 more than the paper clip. How much does the paper clip cost?</td>
    </tr>
    <tr>
      <td>2</td>
      <td>If it takes 5 clerks 5 min to review five applications, how long would it take 100 clerks to review 100 applications?</td>
    </tr>
    <tr>
      <td>3</td>
      <td>In a garden, there is a cluster of weeds. Every day, the cluster doubles in size. If it takes 48 days for the cluster to cover the entire garden, how long would it take for the cluster to cover half of the garden?</td>
    </tr>
  </tbody>
</table>

### Relationships between parameters and paranoia

We found a significant correlation between κ and paranoia scores (Figure 4). However, depression and anxiety were also related to κ, and indeed, paranoia and depression correlate with one another, in our data and in other studies (Na et al., 2019). In order to explore commonalities among the rating scales in the present data, we performed a principle components analysis (Figure 5), identifying three principle components. The first principle component (PC 1) explained 82.3% of the variance in the scales and loaded similarly on anxiety, depression, and paranoia. It correlated significantly with kappa (r = 0.272, p=0.021). Depression, anxiety and paranoia all contribute to PC1. We suggest that this finding is consistent with the idea that depression and anxiety represent contexts in which paranoia can flourish and likewise, harboring a paranoid stance toward the world can induce depression and anxiety.

![Figure 4.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig4-v4.jpg)

**Figure 4.:** Paranoia (SCID-II, top), depression (BDI, middle), and anxiety (BAI, bottom). (a) Among all 72 subjects from online version 3, κ correlates with paranoia (r = 0.30, p=0.011, top) and depression (r = 0.250, p=0.034, middle), but not anxiety (r = 0.210, p=0.077, bottom). (b) Among participants who endorse at least one paranoia item (SCID-II paranoia >0, n = 39), κ correlates with paranoia (r = 0.588, p=8.1E-5, top), depression (r = 0.427, p=0.007, middle), and anxiety (r = 0.367, p=0.021, bottom). All correlations are two-tailed.

![Figure 5.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig5-v4.jpg)

**Figure 5.:** Principal component analysis (PCA) was performed on behavioral data to explain the relationship between κ and the rating scales - paranoia (SCID), depression (BDI) and anxiety (BAI). (a) Scree plot of PCA illustrates percent of variance for each component explained by SCID, BDI and BAI. (b) Principal component 1 (PC1) plotted against κ values. κ correlates with PC1 (r = 0.272, p=0.021).

### Multiple regression

In order to make the case that our observations were most relevant to paranoia, we examined the effects of paranoia, anxiety, and depression on κ within the online version three dataset with multiple regression. A significant regression equation was found (F(3,68)=3.681, p=0.016), with an R (Freeman et al., 2005) of 0.140. Participants’ predicted κ equaled 0.486 + 0.062 (PARANOIA)+0.012 (BDI) −0.006 (BAI). Paranoia was a significant predictor of κ (β = 0.343, t = 2.470, p=0.016, CI=[0.012, 0.113]) but depression and anxiety were not (BDI: β = 0.086, t = 0.423, p=0.674, CI=[−0.043, 0.066]; BAI: β = −0.043, t = −0.218, p=0.828, CI=[−0.063, 0.050]). Examination of correlation plots for κ (Figure 4) revealed a much stronger relationship when analyses were restricted to individuals with paranoia scores greater than 0 (i.e., endorsement of at least one item); among participants who denied all questionnaire items, a minority (seven out of 32) exhibited elevated κ. To account for the possibility that some individuals with severe paranoia may avoid disclosing sensitive information, we performed additional analyses of participants who endorsed one or more paranoia item. The correlation between paranoia and κ in the first block of the task increases from r = 0.3, p=0.011, CI=[0.074, 0.497] (all participants, n = 72) to r = 0.588, p=8.0E-5, CI=[0.335, 0.762] (participants with paranoia >0, n = 39). In this subset, a significant regression equation was also found (F(3,35)=6.322, p=0.002), with an R2of 0.351 (Figure 4). Participants’ predicted κ was equal to 0.432 + 0.150 (PARANOIA)+0.013 (BDI) −0.004 (BAI). Paranoia was a significant predictor of κ (β = 0.538, t = 2.983, p=0.005, CI=[0.048, 0.252]) but depression and anxiety were not (BDI: β = 0.111, t = 0.494, p=0.624, CI=[−0.041, 0.067]; BAI: β = −0.035, t = −0.163, p=0.872, CI=[−0.057, 0.049]). Thus, paranoia predicts kappa across participants. Anxiety and depression do not predict kappa.

### Behavior and simulations

Win-switching was the prominent behavioral feature of both paranoid participants and rats exposed to methamphetamine (Table 1, Table 2; Groman et al., 2018). Collapsed across blocks and task versions, our Experiment 2 data demonstrated a main effect of paranoia group (Figure 3b; F(1, 299)=9.207, p=0.003, ηp2=0.030, MD = 0.059, CI=[0.021, 0.097]; version trend: F(3299)=2.263 p=0.081, ηp2=0.022; low paranoia: m = 0.06 [0.01], high paranoia: m = 0.12 [0.02]). To elucidate whether this behavior was stochastic or predictable (e.g., switching back to a previously rewarding option), we calculated U-values (Kong et al., 2017), a metric of behavioral variability employed by behavioral ecologists (increasingly an inspiration for human behavioral analysis [Fung et al., 2019]), particularly with regards to predator-prey relationships (Humphries and Driver, 1970). When a predator is approaching a prey animal, the prey’s best course of action is to behave randomly, or in a protean fashion, in order to evade capture (Humphries and Driver, 1970). The more protean or stochastic the behavior, the closer to the U-value is to 1. Across task blocks, paranoid participants exhibited elevated choice stochasticity (paranoia by version interaction, F(3, 298)=3.438, p=0.017, ηp2=0.033; Table 2). Post-hoc tests indicate that this stochasticity was specific to versions with contingency transition, suggesting a relationship to unexpected uncertainty (Figure 3b; version 3, F(1, 298)=17.585, p=3.6E-5, ηp2=0.056, MD = 0.071, CI=[0.038, 0.104]; version 4, F(1, 298)=6.397, p=0.012, ηp2=0.021, MD = 0.039, CI=[0.009, 0.07]). Our task manipulation, increasing unexpected volatility, increases win-switching behavior and stochastic choice more in more paranoid participants.

To test the propriety of our model, we simulated data for each subject in online version 3 and determined whether or not key behavioral effects (Figure 7a, Table 1, Table 8) were present. Using individually estimated HGF parameters to generate ten simulations per participant, we recapitulated both elevated win-switch behavior (paranoia effect, F(1, 70)=15.394, p=2.01E-4, ηp2=0.180, MD = 0.186, CI=[0.091, 0.28]) and choice stochasticity (U-value; paranoia effect, F(1, 70)=13.362, p=0.0005, ηp2=0.160, MD = 0.065, CI=[0.030, 0.101]) in simulated paranoid participants (Figure 7b; simulated win-switch rate, low paranoia: m = 0.24 [0.02], high paranoia: m = 0.43 [0.04]; simulated U-value, low paranoia: m = 0.851 [0.008], high paranoia: m = 0.916 [0.016]). Neither real nor simulated data showed any significant relationship between lose-stay behavior and paranoia (Table 1, Table 2, Table 8). To demonstrate the effects of parameters on task performance, we performed additional simulations in which we doubled or halved a single parameter at a time from the baseline average of low paranoia participants. These results confirmed the impact of κ, ω2, and ω3 on win-shift behavior (Figure 4). Parameter recovery revealed significant correlations for κ and ω2 between original subject parameters and those estimated from simulations (Figure 6; ω: r = 0.702, p=2.52E-11, CI=[0.557, 0.805]; κ: r = 0.305, p=0.011, CI=[0.072, 0.506]). Higher level parameters (ω3, μ30) were less consistently recovered, as noted in previous publications (Bröker et al., 2018). Thus, the model we chose, with meta-volatility and three coupled layers of belief, successfully simulates the key features of paranoid behavior: higher win-switching and stochastic choice.

![Figure 6.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig6-v4.jpg)

**Figure 6.:** We simulated behavior from low paranoia participants (online Version 3, n = 54) to evaluate the effects of κ,μ30, ω2, and ω3 on win-shift and lose-stay rates. Estimated perceptual parameters were averaged across subjects to create a single set of baseline parameters. Additional parameter sets were created by doubling or halving one parameter at a time (e.g., 2 κ or 0.5 κ), while the others were held constant (n.b., 2 ω2 violated model assumptions and was excluded from analysis). We also included the average parameter values of rats exposed to methamphetamine (Meth). Ten simulations were run per subject for each condition (i.e., parameter set). Win-shift and lose-stay rates were calculated, then averaged across simulations and subjects. Rates from each condition were divided by the baseline condition rate to generate relative win-shift and lose-stay rates. We compared relative rates for each condition to the baseline (relative rate of 1, depicted as the dotted line; paired t-tests, Bonferroni-corrected p-values). Of note, baseline parameters were positive for κ and ω2, and negative for μ30 and ω3. Consequently, the doubled (2x) condition makes μ30 and ω3 more negative (lower). (n = 54). Box-plots: center lines show the medians; box limits indicate the 25th and 75th percentiles; whiskers extend 1.5 times the interquartile range from the 25th and 75th percentiles, outliers are represented by dots; crosses represent sample means; data points are plotted as open circles; *p≤0.05, **p≤0.01, ***p≤0.001.

![Figure 7.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig7-v4.jpg)

**Figure 7.:** (a) Actual subject trajectory: this is an example choice trajectory from one participant (top). The layers correspond to the three layers of belief in the HGF model (depicted in Figure 2a). Focusing on the low-level beliefs (yellow box): The purple line represents the subject’s estimated first-level belief about the value of choosing deck 1; blue, their belief about the value of choosing deck 2; and red, their belief about the value of choosing deck 3. Simulated subject trajectory represents the estimated beliefs from choices simulated from estimated perceptual parameters from that participant (middle), and Recovered subject trajectory represents what happens when we re-estimate beliefs from the simulated choices (bottom). Crucially, Simulated trajectories closely align with real trajectories (the increases and decreased in estimated beliefs about the values of each deck [purple, blue, red lines] align with each other across actual, simulated and recovered trajectories), although trial-by-trial choices (colored dots and arrow) occasionally differ. Outcomes (1 or 0; black dots and arrows) remain the same. (b) Actual versus Recovered: these data represent the belief parameters estimated from the participant’s responses (Actual) compared to those estimated from the choices simulated with the participant’s perceptual parameters (Recovered). Actual and Recovered values significantly correlate for ω2 (r = 0.702, p=2.52E-11) and κ (r = 0.305, p=0.011) but not ω3 (r = 0.172, p=0.16) or µ30 (r = 0.186, p=0.13). Box plots: gray indicates low paranoia, orange designates high paranoia; center lines depict medians; box limits indicate the 25th and 75th percentiles; whiskers extend 1.5 times the interquartile range from the 25th and 75th percentiles, outliers are represented by dots; crosses represent sample means; data points are plotted as open circles. Online version three dataset.

**Table 8.**
 Simulations and behavior.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Win-switch rate</th>
      <th colspan="2">U-value</th>
      <th colspan="2">Lose-stay rate</th>
    </tr>
    <tr>
      <th>Effect</th>
      <th>Df</th>
      <th>F</th>
      <th>p-value</th>
      <th>F</th>
      <th>p-value</th>
      <th>F</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="8">Experiment 1</td>
    </tr>
    <tr>
      <td>Block</td>
      <td>1, 30</td>
      <td>1.465</td>
      <td>0.236</td>
      <td>16.999</td>
      <td>0.0003</td>
      <td>1.334</td>
      <td>0.257</td>
    </tr>
    <tr>
      <td>Block*Paranoia Group</td>
      <td>1, 30</td>
      <td>0.602</td>
      <td>0.444</td>
      <td>2.393</td>
      <td>0.132</td>
      <td>2.575</td>
      <td>0.119</td>
    </tr>
    <tr>
      <td>Paranoia Group</td>
      <td>1, 30</td>
      <td>3.579</td>
      <td>0.068</td>
      <td>3.312</td>
      <td>0.079</td>
      <td>2.283</td>
      <td>0.141</td>
    </tr>
    <tr>
      <td colspan="8">Experiment 2, Version 3</td>
    </tr>
    <tr>
      <td>Block</td>
      <td>1, 70</td>
      <td>0.935</td>
      <td>0.337</td>
      <td>10.153</td>
      <td>0.002</td>
      <td>0.122</td>
      <td>0.728</td>
    </tr>
    <tr>
      <td>Block*Paranoia Group</td>
      <td>1, 70</td>
      <td>0.001</td>
      <td>0.982</td>
      <td>0.003</td>
      <td>0.958</td>
      <td>1.93</td>
      <td>0.169</td>
    </tr>
    <tr>
      <td>Paranoia Group</td>
      <td>1, 70</td>
      <td>12.698</td>
      <td>0.001</td>
      <td>19.209</td>
      <td>4.03E-05</td>
      <td>1.095</td>
      <td>0.299</td>
    </tr>
    <tr>
      <td colspan="8">Simulations†</td>
    </tr>
    <tr>
      <td>Block</td>
      <td>1, 70</td>
      <td>0.176</td>
      <td>0.676</td>
      <td>3.335</td>
      <td>0.072</td>
      <td>5.073</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>Block*Paranoia Group</td>
      <td>1, 70</td>
      <td>2.039</td>
      <td>0.158</td>
      <td>2.624</td>
      <td>0.11</td>
      <td>0.036</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>Paranoia Group</td>
      <td>1, 70</td>
      <td>15.394</td>
      <td>0.0002</td>
      <td>13.362</td>
      <td>0.0005</td>
      <td>0.042</td>
      <td>0.839</td>
    </tr>
  </tbody>
</table>

_†Simulated data from experiment 2, Version 3._

### Alternate models

Our model is complex and other simpler reinforcement learning models might explain behavior on this task. Given the win-switching behavior we sought to understand, we fit a model from Lefebvre and colleagues that instantiated biased belief updating via differential weighting of positive and negative prediction errors (Lefebvre et al., 2018). Fitting this model to online version 3, we saw no significant paranoia group differences in learning rates for positive or negative prediction errors in parameters derived from all 180 trials (independent samples t-test: α+, t(70)=-0.532, p=0.597; α-, t(70)=0.963, p=0.339), nor did we see any significant block*paranoia or paranoia group effects by repeated measures ANOVA (block*paranoia: α+, F(1, 70)=0.188, p=0.732, α-, F(1, 70)=0.378, p=0.540; paranoia group: α+, F(1, 70)=0.243, p=0.623, α-, F(1, 70)=1.292, p=0.260). See Table 9.

**Table 9.**
 Alternative models fail to capture paranoia group differences.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Low Paranoia (n=56)†</th>
      <th colspan="3">High Paranoia (n=16)†</th>
      <th colspan="2">Paranoia Group Effect‡</th>
      <th colspan="2">Paranoia x Block Effect‡</th>
    </tr>
    <tr>
      <th></th>
      <th>Mean</th>
      <th>SEM</th>
      <th>95% CI</th>
      <th>Mean</th>
      <th>SEM</th>
      <th>95% CI</th>
      <th>F(df)</th>
      <th>P</th>
      <th>F(df)</th>
      <th>P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="11">Q-learning with learning rates for positive and negative prediction errors</td>
    </tr>
    <tr>
      <td colspan="11">Positive prediction error (α+)</td>
    </tr>
    <tr>
      <td>1st half</td>
      <td>0.463</td>
      <td>0.038</td>
      <td>[0.388, 0.538]</td>
      <td>0.475</td>
      <td>0.071</td>
      <td>[0.335, 0.616]</td>
      <td>0.243 (1, 70)</td>
      <td>0.623</td>
      <td>0.118 (1, 70)</td>
      <td>0.732</td>
    </tr>
    <tr>
      <td>2nd half</td>
      <td>0.476</td>
      <td>0.039</td>
      <td>[0.398, 0.555]</td>
      <td>0.535</td>
      <td>0.074</td>
      <td>[0.379, 0.672]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="12">Negative prediction error (α-)</td>
    </tr>
    <tr>
      <td>1st half</td>
      <td>0.421</td>
      <td>0.022</td>
      <td>[0.377, 0.464]</td>
      <td>0.365</td>
      <td>0.041</td>
      <td>[0.284, 0.446]</td>
      <td>1.292 (1, 70)</td>
      <td>0.260</td>
      <td>0.320 (1, 70)</td>
      <td>0.573</td>
    </tr>
    <tr>
      <td>2nd half</td>
      <td>0.386</td>
      <td>0.021</td>
      <td>[0.344, 0.427]</td>
      <td>0.364</td>
      <td>0.039</td>
      <td>[0.285,0.442]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="11">Inverse temperature (β )</td>
    </tr>
    <tr>
      <td>1st half</td>
      <td>271</td>
      <td>74.0</td>
      <td>[126, 416]</td>
      <td>147</td>
      <td>133</td>
      <td>[-114, 408]</td>
      <td>1.626 (1, 70)</td>
      <td>0.207</td>
      <td>0.043 (1, 70)</td>
      <td>0.837</td>
    </tr>
    <tr>
      <td>2nd half</td>
      <td>316</td>
      <td>82.3</td>
      <td>[155, 477]</td>
      <td>145</td>
      <td>132</td>
      <td>[-114, 403]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="11">2-level HGF with softmax decision model</td>
    </tr>
    <tr>
      <td colspan="11">µ2</td>
    </tr>
    <tr>
      <td>1st half</td>
      <td>-0.059</td>
      <td>0.081</td>
      <td>[-0.218, 0.100]</td>
      <td>-0.303</td>
      <td>0.157</td>
      <td>[-0.611, 0.005]</td>
      <td>3.039 (1, 70)</td>
      <td>0.086</td>
      <td>0.385 (1, 70)</td>
      <td>0.537</td>
    </tr>
    <tr>
      <td>2nd half</td>
      <td>-0.244</td>
      <td>0.082</td>
      <td>[-0.405, -0.082]</td>
      <td>-0.566</td>
      <td>0.155</td>
      <td>[-0.869, -0.262]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="11">Inverse temperature (β)</td>
    </tr>
    <tr>
      <td>1st half</td>
      <td>131</td>
      <td>30.6</td>
      <td>[71.3, 191]</td>
      <td>35.3</td>
      <td>6.20</td>
      <td>[23.2, 47.5]</td>
      <td>2.665 (1, 70)</td>
      <td>0.107</td>
      <td>0.250 (1, 70)</td>
      <td>0.619</td>
    </tr>
    <tr>
      <td>2nd half</td>
      <td>119</td>
      <td>30.6</td>
      <td>[58.7, 179]</td>
      <td>52.1</td>
      <td>12.1</td>
      <td>[28.3, 75.9]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_† Online version 3 data ‡ Repeated measures ANOVA._

We can also simplify within our hierarchical Gaussian Filter framework. The model we chose had three layers of beliefs and the highest level seemed to capture most of the task and paranoia effects of interest (Figure 8). To confirm this suspicion, we removed the third layer, fitting an HGF model that had beliefs about outcomes and deck values but no beliefs about volatility, no unexpected volatility learning rate, nor meta-volatility. This model failed to capture the task effects or group differences in its parameters (see Table 9).

![Figure 8.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig8-v4.jpg)

**Figure 8.:** (a) Plots of in laboratory and online behavioral metrics. Win-switch rate (switching after positive feedback), U-value (behavioral stochasticity) and Lose-stay rate (perseverating after a loss). Low paranoia participants are shown in gray, High paranoia in orange. Win-switch rates and U-values are collapsed across blocks. For Lose-stay rates, darker colors are block one data and lighter colors are block two data. Behavioral switching patterns replicate across in laboratory and online version three experiments. Perseveration after negative feedback (lose-stay behavior) did not significantly differ between paranoia groups or task block. (b) Simulated data generated from HGF perceptual parameters (version 3). Win-switch rate, U-value and Lose-stay rate of the simulated data are depicted. The model simulated data replicate the win-switch and U-value behavioral differences between high and low paranoia participants presented in panel a. Like the real participants, there was no difference in lose-stay rates in the simulated data. Center lines show the medians; box limits indicate the 25th and 75th percentiles; whiskers extend 1.5 times the interquartile range from the 25th and 75th percentiles, outliers are represented by dots; crosses represent sample means; data points are plotted as open circles.*p≤0.05, **p≤0.01, ***p≤0.001. Plots of participant behavioral metrics (a) are presented side by side with simulated data (b).

Therefore, a more complicated model, one that captures higher-level beliefs about contingency transitions or learning when to learn, seems most appropriate, and indeed, that type of model was able to simulate the key features of our data (Palminteri et al., 2017). Future work will compare and contrast different potential computational models included, but not limited to Bayesian Hidden State Markov Models (Hampton et al., 2006), as well as switching (Gershman et al., 2014) and volatile Kalman Filters (Piray and Daw, 2020).

### Clustering analysis

Given the apparent similarity in effects of paranoia and methamphetamine in humans and rats, respectively (Figure 2b), we searched for latent structure in our data using two-step cluster analysis (Tkaczynski, 2017). This approach sorts subjects into groups (clusters) on the basis of some experimenter-selected variables such as estimated model parameters. The goal is to find distinct subsets in the data such that each cluster exhibits a cohesive pattern of relationships between the variables. Whereas some clustering approaches require the experimenter to predefine the expected number of clusters, two step-clustering determines both the optimal number of clusters and the composition of each cluster. The greater the similarity (or homogeneity) within a group and the greater the difference between groups, the better the clustering.

Considering that paranoia and methamphetamine exposure share a pattern of elevated μ30 and κ accompanied by decreased ω2 and ω3 (Table 10), we hypothesized that these four variables would yield a distinct cluster: a ‘paranoid style’ across species. We analyzed μ30, κ, ω2, and ω3 estimates derived from the first block of experiment one and online version 3 (pre-context change data, because rats do not experience a context shift) with post-chronic exposure rat data (methamphetamine and saline). We identified two clusters with good cohesion and separation, meaning that subjects sorted into two groups (each containing rodents and humans) whose parameters travelled in such a way that their values were close to the centroid or mean of the cluster they were in and as far as possible from the centroid of the other cluster (average silhouette coefficient = 0.7; cluster size ratio = 2.46; Figure 9a). All parameters contributed to clustering; κ contributed most strongly (Figure 9b). Importantly, the cluster solution did not separate rats from humans (despite the differences in task structure, incentives, manipulanda, and phylogeny). Relative to the overall distribution, Cluster one was characterized by high κ and μ30, and decreased ω2 and ω3. Cluster one membership was significantly associated with high paranoia and methamphetamine exposure, χ2(1, n = 121)=29.447, p=5.75E-8, Cramer’s V = 0.493 (Figure 9c). Notably, no participants in the low paranoia group with paranoia scores above zero were ascribed Cluster one membership. The cluster solution was robust to validation by split-half analysis (removing half of the participants and repeating the clustering), removal of the rat subjects, and removal of human participants. In each case, we identified two clusters with good cohesion and separation (Split-half 1, n = 19 cluster 1, 42 cluster 2: silhouette coefficient = 0.6; Split-half 2, n = 17 cluster 1, 43 cluster 2: silhouette coefficient = 0.7; No Rat, n = 26 cluster 1, 78 cluster 2: silhouette coefficient = 0.7; Rat Only, n = 6 cluster 1, 11 cluster 2: silhouette coefficient = 0.7). In summary, paranoid participants and methamphetamine-exposed rats cluster together (high μ30, high κ, low ω2, and low ω3), suggesting that these parameters share an underlying generative process and that paranoia and methamphetamine have similar effects on reversal-learning.

**Table 10.**
 Summary of paranoia/methamphetamine effects on belief-updating.


<table>
  <thead>
    <tr>
      <th></th>
      <th>In lab</th>
      <th>Online</th>
      <th>Rats</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ω3</td>
      <td>↓†</td>
      <td>⇣</td>
      <td>⬇</td>
    </tr>
    <tr>
      <td>µ30</td>
      <td>⬆</td>
      <td>⬆‡§</td>
      <td>⬆</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>⬆</td>
      <td>⬆‡</td>
      <td>⬆</td>
    </tr>
    <tr>
      <td>ω2</td>
      <td>⬇</td>
      <td>⬇‡¶</td>
      <td>⬇</td>
    </tr>
    <tr>
      <td>µ02</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

_⇡ ⇣ Non-significant increase/decrease in high paranoia or meth, relative to low paranoia or saline ↑ ↓ Trend-level increase/decrease in high paranoia or meth, relative to low paranoia or saline ⬆⬇ Significantly higher/lower in high paranoia or meth, relative to low paranoia or saline - - No significant findings or trends † Baseline trend; parameter decreases in second block for low but not high paranoia ‡ Version 3 only § Trend-level significance disappears with inclusion of demographic covariates ¶ Significance reduced to trend with inclusion of demographic covariates._

![Figure 9.](https://cdn.elifesciences.org/articles/56345/elife-56345-fig9-v4.jpg)

**Figure 9.:** Two-step cluster analysis of model parameters (ω3, μ30, κ , ω2) across rat and human data sets (rat, post-Rx; in laboratory and online version 3, block 1). Automated clustering yielded an optimal two clusters with good cohesion and separation (average silhouette coefficient = 0.7; cluster size ratio = 2.46). (a) Density plots for μ30, κ, ω2, and ω3 (light pink) depict cluster-specific distributions for each parameter (red). Unlike frequency histograms (that depict the number of data points in bins), density plots employ smoothing to prioritize distribution shape and are not restricted by bin size. Beneath each density plot, box-plots of overall median, 25th quartile, and 75th quartile for each parameter are aligned (pink), with cluster medians and quartiles superimposed (red). Relative to the overall distribution, Cluster 1 (n = 35) medians are elevated for μ30 and κ, decreased for ω2 and ω3. Cluster 2 (n = 86) falls within each overall distribution. (b) Predictor importance of included parameters. Consistent with the color scheme in Figure 2a, Uncertainty weighting parameters (κ, ω2, ω3 ) are depicted in purple and μ30 the prior is in blue. (c) Distribution of cluster identities within groups. Black bars signify the proportion of group members assigned to Cluster one and gray bars represent the proportion of group members assigned to Cluster 2. Cluster one membership is significantly associated with paranoia and methamphetamine groups (χ2(1, n = 121)=29.447, p=5.75E-8). Columns display means [standard error] or percentage of participants within the described category, test-statistics, and p-values. †Independent samples t-test: t-value (df). Two-tailed P-values reported. ‡Chi square coefficient (df). §Fisher’s exact test, exact significance (2-sided). ¶Equal variances not assumed. #Not significant (Bonferonni correction). ††Data presented in Figure 8; repeated measures ANOVA, paranoia group trend or effect: F(df), P; estimated marginal means and standard error. ‡‡Data presented in Figure 2; repeated measures ANOVA, F(df), P. In laboratory: paranoia x block interactions for ω3, μ30; paranoia group effects for κ, ω2. Version 3: paranoia group effects reported. See Table 3 for complete ANOVA. results. Version columns display means [standard error] or percentage of participants within the described category. ††Univariate analysis, F(df). ‡Exact test, chi-square coefficient (df). § Exact significance (2-sided). ||Monte Carlo significance (2-sided). ‡‡Data presented in Figure 3; repeated measures ANOVA, F(df), P. Mean values collapsed across blocks.

## Discussion

During non-social probabilistic reversal-learning, paranoid individuals and rats chronically exposed to methamphetamine have higher initial expectations of task volatility (μ30). In other words, they start the task anticipating more changes in stimulus-outcome associations, and they switch choices readily and excessively in anticipation of reversal events. By relying more on their expectations of volatility than on actual experience (exemplified by switching even after positive feedback), they are slower to learn about changes in task volatility. This manifests as decreased meta-volatility learning (ω3) and failure to significantly adjust μ30 after contingency transitions. More paranoid individuals are similarly slower to adjust expected deck values (lower ω2) but faster to attribute volatility to reversal events (elevated κ), perceiving change (unexpected uncertainty) instead of normal statistical variation (expected uncertainty). They sit at Hofstadter’s ‘turning point’, constantly expecting change but never learning appropriately from it.

In the reversal learning literature, choice switching after positive feedback has garnered less attention than perseverative behavior and sensitivity to negative feedback (Izquierdo et al., 2017; Waltz, 2017). Individuals with depression and schizophrenia seemingly perseverate less than healthy controls, but this has formerly been attributed to increased sensitivity to negative feedback (Waltz, 2017; Robinson et al., 2012). However, elevated win-switch tendencies have been reported in youths with bipolar disorder, major depressive disorder, and anxiety disorder (Dickstein et al., 2010). A prior study in people with schizophrenia described excessive win-switch behavior that correlated with the severity of delusional beliefs and hallucinations (Waltz, 2017). Likewise, an elevated prior on environmental volatility (μ30) and higher sensitivity to this volatility (κ) have been observed in HGF analyses of 2-choice probabilistic reversal-learning in medicated and unmedicated patients with schizophrenia (Deserno, 2018). These authors did not explore paranoia specifically.

We assessed paranoia across the continuum of health and mental illness, provided three choice options, and explicitly manipulated unexpected volatility across task versions. The version that shifted from an easier to a more difficult contingency context (version 3) was associated with paranoia group effects on μ30, κ, and ω2, and a meta-analytic effect on ω3. Furthermore, this contingency transition – an exposure to truly unexpected volatility – rendered low paranoia controls more similar to their paranoid counterparts by decreasing their meta-volatility learning (ω3). Paranoid participants responded to contingency transitions in version 3 and version four by switching stochastically. These findings suggest a continuum of behavioral responses to volatility, moving from optimal learning to diminished feedback sensitivity (i.e, decreased ω3 in low paranoia participants) and from diminished feedback sensitivity (lower ω3 and increased win-switching in high paranoia participants) toward complete dissociation from experienced feedback (stochastic switching).

Unexpected uncertainty, the perception of change in the probabilities of the environment — particularly ‘unsignaled context switches” (Yu and Dayan, 2005) which increase unexpected volatility — is thought to promote abandonment of old associations and new learning. However, our results suggest that this response might vary according to a hierarchy of belief. Paranoid participants were quick to abandon ‘best deck’ associations and explore alternative options (i.e., x2 beliefs), but in turn they relied more on their higher-level beliefs about the task volatility (x3 beliefs) and less on sensory feedback (lower metavolatility learning). Our analysis of covariates warrants specific focus on κ, the sensitivity to unexpected volatility. Other parameter-paranoia associations did not endure after controlling for demographic factors (age, gender, ethnicity, and race), although we see their derangement in our rodent study as well as in the significant meta-analytic effects across our experiments. Furthermore, these demographic factors are themselves strong predictors of paranoia (Holt and Albert, 2006; Iacovino et al., 2014; Mahoney et al., 2010). It is notable too that κ was the most powerful discriminator of the two clusters of human and animal participants. We conclude that elevated κ - belief updating tethered to unexpected volatility - is the parameter change most robustly associated with paranoia. Doubling κ in our simulations induced significantly more win-switching.

Multiple neurobiological manipulations may induce such win-switching behavior. Lesions of the mediodorsal thalamus in non-human primates (Chakraborty et al., 2016) or neurons projecting from the amygdala to orbitofrontal cortex in rats (Groman et al., 2019) engender win-switching. Unexpected uncertainty, and the κ parameter of the HGF in particular (Marshall et al., 2016), are thought to be signaled via the locus coeruleus and noradrenaline (Yu and Dayan, 2005; Payzan-LeNestour and Bossaerts, 2011; Payzan-LeNestour et al., 2013; Tervo et al., 2014). This mechanism is thought to modulate switching versus staying behaviors (Kane et al., 2017; Aston-Jones and Cohen, 2005; Aston-Jones et al., 1999; Eldar et al., 2013), as well as responses to stress (Borodovitsyna et al., 2018; McCall et al., 2015; Atzori et al., 2016) and subliminal fear cues (Liddell et al., 2005) to coordinate fight-or-flight responses (Atzori et al., 2016). The dual role of the locus coeruleus in recognizing and responding to threats as well as unexpected uncertainty suggests that dysfunction could produce both paranoia and the inferential abnormalities we observed. Methamphetamine may induce similar dysfunction (Ferrucci et al., 2019; Ferrucci et al., 2013; Ferrucci et al., 2008). Acute moderate doses increase pre-synaptic catecholamine release, particularly noradrenaline (Rothman et al., 2001), and induce exploratory locomotive effects modulated through adrenoceptors on dopamine neurons (Ferrucci et al., 2013).

Excessive release of noradrenaline from the locus coeruleus into the anterior cingulate cortex drives feedback insensitivity and stochastic switching behavior in rats completing a three-option counter prediction task (Tervo et al., 2014). Evolutionarily, departure from predictable, rational actions might offer an adaptive mechanism for escape from intractable threat. As a protean defense mechanism, behavioral stochasticity impedes predators’ abilities to create accurate, actionable countermeasures (Humphries and Driver, 1970; Richardson et al., 2018; Humphries and Driver, 1967). If driven by excessive unexpected uncertainty, underwritten by noradrenaline, protean defense may represent a heavily conserved, continuous common mechanism underlying vigilance and false alarms (Aston-Jones et al., 1994; Rajkowski et al., 1994; Usher et al., 1999), arousal-linked attentional biases (Eldar et al., 2013) and selective processing of social threats. However, protean behaviors are not necessarily adaptive. Pathological insensitivity to feedback and reliance on internal beliefs over evidence constitute a ‘break from reality’ – in other words, psychosis.

Efference copy models of motor control Wolpert and Ghahramani, 2000 have been evoked to explain psychotic symptoms (Blakemore et al., 2000; Blakemore et al., 1998; Blakemore et al., 1999; Blakemore et al., 2002; Frith et al., 2000a; Frith et al., 2000b; Shergill et al., 2005; Shergill et al., 2014). Aberrant mismatches between expected and experienced sensory consequences of actions, weighted by their uncertainty (Wolpert and Ghahramani, 2000), can lead to the misattribution of one’s movements to an external agent (Blakemore et al., 2000; Blakemore et al., 1998; Blakemore et al., 1999; Blakemore et al., 2002; Frith et al., 2000a; Frith et al., 2000b; Shergill et al., 2005; Shergill et al., 2014). Since we model others’ intentions with reference to our model of ourselves (Friston and Frith, 2015), volatile experiences of ones’ body and actions will lead to uncertain and ultimately more threatening inferences about others (Friston and Frith, 2015). This would be entirely consistent with the present observations.

When confronted with intractable unexpected uncertainty our participants rely on higher-level beliefs about the task environment. When humans experience non-social volatility, (For example through threats to their sense of control [Whitson and Galinsky, 2008] or exposure to surprising non-social stimuli [Proulx et al., 2012; Heine et al., 2006]), they appeal to the influence of powerful enemies, even when those enemies’ influence is not obviously linked to the volatility (Sullivan et al., 2010). Our account places the locus of paranoia at the level of the individual. Here, our account departs from evolutionary accounts of paranoia grounded in coalitional threat (Raihani and Bell, 2019; persecutors are not scapegoats that increase group cohesion. Rather, when paranoid, we have a ready explanation for hazards. With a well-defined persecutor in mind, a volatile world may be perceived to have less randomly distributed risk (Sullivan et al., 2010). However, paranoia might become a self-fulfilling prophecy, engendering more volatility and negative social interactions. This aspect may be captured in our task through win-switch behavior. By failing to incorporate positive feedback from the best option, paranoid individuals sample sub-optimal options which delivers misleading positive feedback.

There are some important limitations to our conclusions. Compared with humans, rats are relatively asocial. But they are not completely asocial. In our experiment they were housed in pairs, and, more broadly, they evince social affiliative interactions with other rats (Donaldson et al., 2018; Kondrakiewicz et al., 2019; Urbach et al., 2010). A further limitation centers on the comparability of our experimental designs. In humans our comparisons were both within (contingency transition) and between groups (low versus high paranoia). In rats, the model was also mixed with some between (saline versus methamphetamine) and some within-subject (pre versus post chronic treatment) comparisons. We should be clear that there was no contingency context transition in the rat study. However, just as that transition made low paranoia humans behave like high paranoia, chronic methamphetamine exposure made rats behave on a stable contingency much like high paranoia humans - even in the absence of contingency transition. The comparable results across species, despite these differences, warrant the inference that our basic, relatively asocial, approach provides a robust tool for computational dissection of learning mechanisms.

Social interactions play a rich and undeniable role in paranoia, but translational, domain-general approaches may ultimately facilitate biological insights into paranoia, psychosis and delusions (Corlett and Fletcher, 2014; Feeney et al., 2017). Whilst we contend that our task is relatively free of social features (certainly compared to others [Raihani and Bell, 2017]), the possibility remains that the elevated U-values in our participants are reflective of attempts (and perhaps failures) to predict our intentions as experimenters. Indeed, this is a possibility raised previously with regards to simple conditioned behaviors in experimental animals. Even during Pavlovian conditioning, animals may attempt to infer a generative model of the task environment, which might, ultimately, include the experimenter arranging the contingencies (Gershman and Niv, 2012; Gershman and Niv, 2010). It is possible that all instances of human cognitive testing involve an element of inference by the participant with regards to the intentions of the experimenter, whether or not the task at hand is explicitly social, and indeed, all cognitive functions may be aimed at or modulated by such inferences (Turner et al., 1994).

In summary, a strong belief in the volatility of the world necessitates hypervigilance and a facility with change. However, in paranoia, that belief in the volatility of the world is itself resistant to change, making it difficult to reassure, teach, or change the minds of people who are paranoid. They remain ‘on guard,’ adhering to expectations over evidence. By using a non-social task, we have shown that this paranoid style is not restricted to the social domain, and that it can be modeled in relatively asocial animals. Additionally, our domain-general approach reaffirms the merit of establishing expectations of a stable, predictable environment to promote recovery from paranoia-associated illness (Powers et al., 2018). We note with interest the apparent relationship between conspiratorial ideation and societal crisis situations (terrorist attacks, plane crashes, natural disasters or war) throughout history, with peaks around the great fire of Rome (AD 64), the industrial revolution, the beginning of the cold war, 9/11, and contemporary financial crises (van Prooijen and Douglas, 2017). In today’s world of escalating uncertainty and volatilty – particularly environmental climate change and viral pandemics – our findings suggest that the paranoid style of inference may prove particularly maladaptive for coordinating collaborative solutions.

## Materials and methods

Experiments were conducted at Yale University and the Connecticut Mental Health Center (New Haven, CT) in strict accordance with Yale University’s Human Investigation Committee and Institutional Animal Care and Use Committee. Informed consent was provided by all research participants.

### Experiment 1

English-speaking participants aged 18 to 65 (n = 34) were recruited from the greater New Haven area through public fliers and mental health provider referrals. Exclusion criteria included history of cognitive or neurologic disorder (e.g., dementia), intellectual impairment, or epilepsy; current substance dependence or intoxication; cognition-impairing medications or doses (e.g. opiates, high dose benzodiazepines); history of special education; and color blindness. Participants were classified as healthy controls (n = 18), schizophrenia spectrum patients (schizophrenia or schizoaffective disorder; n = 8), and mood disorder patients (depression, bipolar disorder, generalized anxiety disorder, post-traumatic stress disorder; n = 8) on the basis of clinician referrals and/or self-report. Participants were compensated $10 for enrolment with an additional $10 upon completion. Two healthy controls were excluded from analyses due to failure to complete the questionnaires and suspected substance use, respectively.

### Experiment 2

332 participants were recruited online via Amazon Mechanical Turk (MTurk). The study advertisement was accessible to MTurk workers with a 90% or higher HIT approval rate located within the United States. To discourage bot submissions and verify human participation, we required participants to answer open-ended free response questions; submit unique, separate completion codes for the behavioral task and questionnaires; and enter MTurk IDs into specific boxes within the questionnaires. All submissions were reviewed for completion code accuracy, completeness of responses (i.e., declining no more than 30% of questionnaire items), quality of free response items (e.g., length, appropriate grammar and content), and use of virtual private servers (VPS) to submit multiple responses and/or conceal non-US locations (Dennis VPS paper, 2018). Upon approval, workers were compensated $6. Those who scored in the top 25% on the card game (reversal-learning task) earned a $2 bonus. We rejected or excluded 19 submissions that geolocation services (https://www.iplocation.net/) identified as originating outside of the United States or from suspected server farms, four submissions for failure to manually enter MTurk ID codes, and two submissions for insufficient questionnaire completion. Submissions with grossly incorrect completion codes were rejected without further review.

### Experiment 3

Subject information, behavioral data acquisition, and behavioral analyses were described previously (Groman et al., 2018). Long Evans rats (Charles River; n = 20) ranged from 7 to 9 weeks of age. Rats were exposed to escalating doses and frequency of saline (n = 10) or methamphetamine (n = 10, three withdrawn during dosing), imitating patterns of human methamphetamine users (Segal et al., 2003; Han et al., 2011). Prior to dosing (Pre-Rx), rats completed 26 within-session reversal sessions, including up to eight reversals per session. Post-dosing (Post-Rx), rats completed one test session per week for four weeks. Computational model parameters were estimated from each session and averaged across treatment conditions to yield one Pre-Rx and Post-Rx set of parameters per rat.

### Behavioral task

Participants completed a 3-option probabilistic reversal-learning paradigm. Three decks of cards were displayed on a computer monitor for 160 trials. Participants selected a deck on each trial by pressing the predesignated key. We advised participants that each deck contained winning and losing cards (+100 and −50 points), but in different amounts. We also stated that the best deck may change. Participants were instructed to find the best deck and earn as many points as possible. Probabilities switched between decks when the highest probability deck was selected in 9 out of 10 consecutive trials (performance-dependent reversal). Every 40 trials the participant was provided a break, following which probabilities automatically reassigned (performance-independent reversal).

In Experiment 1, the task was presented via Eprime 2.0 software (Psychology Software Tools, Sharpsburg, PA). Participants were limited to a 3 s response window, after which the trial would time out and record a null response. A fixation cross appeared during variable inter-trial intervals (jittering). Task pacing remained independent of response time. In block 1 (trials 1–80) the reward probabilities (contingency) of the three decks were 90%, 50%, and 10% (90-50–10%). Without cue or warning (i.e. unsignaled to the participants) the contingency transitioned to 80%, 40%, and 20% (80-40–20%) upon initiation of block 2 (trials 81–160).

In Experiment 2, the task was administered via web browser link from the MTurk marketplace. We changed the task timing to self-paced and eliminated null trials and inter-trial jittering. A progress tracker was provided every 40 trials. Workers were randomly assigned to one of four task versions, using restricted block randomization to ensure comparable numbers of high paranoia participants across task versions. Version one had a constant contingency of 90-50–10%. Version 4 maintained a constant contingency of 80-40–20%. Version 3 replicated the 90-50–10% (block 1) to 80-40–20% (block 2) context transition of Experiment 1. Version 4 presented the reversed contingency transition, 80-40–20% (block 1) to 90-50–10% (block 2). We analyzed attrition rates across the four versions.

### Questionnaires

Following task completion, questionnaires were administered via the Qualtrics survey platform (Qualtrics Labs, Inc, Provo, UT). Items included demographic information (age, gender, educational attainment, ethnicity, and race) and mental health questions (past or present diagnosis, medication use, Structured Clinical Interview for DSM-IV Axis II Personality Disorders (SCID-II) (Ryder et al., 2007), Beck’s Anxiety Inventory (BAI) (Beck et al., 1988), Beck’s Depression Inventory (BDI) (Beck et al., 1961). We removed the single suicidality question from the BDI for Experiment 2. Experiment 2 included additional items: income, three cognitive reflection questions (Table 7), and three free response items (‘What do you think the card game was testing?’, ‘Did you use any particular strategy or strategies? If yes, please describe’, and ‘Did you find yourself switching strategies over the course of the game?’). We quantified trait-level paranoia using the paranoid personality subscale of the SCID-II, and we included an ideas of reference item from the schizotypy subscale (‘When you are out in public and see people talking, do you often feel that they are talking about you?’) This item, along with other SCID-II items, has previously been included as a metric of paranoia in the general population (Bebbington et al., 2013; Bell and O'Driscoll, 2018). Participants who endorsed four or more paranoid personality items (i.e., the cut-off for the top third identified in Experiment 1) were classified as ‘high paranoia.’ Each participant’s SCID-II, BAI, and BDI scores were normalized by total scale items answered. Response rates were higher than 90% for all questionnaire items and scales (Table 11).

**Table 11.**
 Questionnaire item completion (% responses).


<table>
  <thead>
    <tr>
      <th>Questionnaire/subscale</th>
      <th>Experiment 1</th>
      <th>Experiment 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age</td>
      <td>90.6%</td>
      <td>99.7%</td>
    </tr>
    <tr>
      <td>Gender</td>
      <td>100.0%</td>
      <td>100.0%</td>
    </tr>
    <tr>
      <td>Ethnicity</td>
      <td>100.0%</td>
      <td>100.0%</td>
    </tr>
    <tr>
      <td>Race</td>
      <td>100.0%</td>
      <td>100.0%</td>
    </tr>
    <tr>
      <td>Education</td>
      <td>100.0%</td>
      <td>99.7%</td>
    </tr>
    <tr>
      <td>Meds</td>
      <td>100.0%</td>
      <td>90.6%</td>
    </tr>
    <tr>
      <td>Dx</td>
      <td>100.0%</td>
      <td>94.1%</td>
    </tr>
    <tr>
      <td>Income</td>
      <td>N/A</td>
      <td>98.0%</td>
    </tr>
    <tr>
      <td>SCID-II Paranoia - all items</td>
      <td>96.9%</td>
      <td>94.1%</td>
    </tr>
    <tr>
      <td>SCID-II Paranoia - one item missing</td>
      <td>3.1%</td>
      <td>5.5%</td>
    </tr>
    <tr>
      <td>SCID-II Paranoia - three items missing</td>
      <td>0.0%</td>
      <td>0.3%</td>
    </tr>
    <tr>
      <td>Cognitive reflection - all items</td>
      <td>N/A</td>
      <td>97.7%</td>
    </tr>
    <tr>
      <td>Beck's Anxiety Inventory (BAI) - all items</td>
      <td>90.6%</td>
      <td>96.7%</td>
    </tr>
    <tr>
      <td>BAI - one item missing</td>
      <td>3.1%</td>
      <td>2.9%</td>
    </tr>
    <tr>
      <td>BAI - two items missing</td>
      <td>6.3%</td>
      <td>0.3%</td>
    </tr>
    <tr>
      <td>Beck's Depression Inventory (BDI) - all items</td>
      <td>100.0%</td>
      <td>99.0%</td>
    </tr>
    <tr>
      <td>BDI - one item missing</td>
      <td>0.0%</td>
      <td>1.0%</td>
    </tr>
  </tbody>
</table>

### Behavioral analysis

We analyzed tendencies to choose alternative decks after positive feedback (win-switch) and select the same deck after negative feedback (lose-stay). Win-switch rates were calculated as the number of trials in which the participant switched after positive feedback divided by the number of trials in which they received positive feedback. Lose-stay rates were calculated as number of trials in which a participant persisted after negative feedback divided by total negative feedback trials. In Experiment 1, we excluded post-null trials from these analyses. To further characterize switching behavior, we calculated U-values, a measure of choice stochasticity:

$$
U−value=−Σ_{i=1}^{\beta}\frac{log⁡(\alpha_{i}) x \alpha_{i}}{log⁡(\beta)}
$$

where β is the number of possible choice options (i.e., card decks or noseports) and α equals the relative frequency of choice option $i$ (Kong et al., 2017). To avoid any choice counterbalancing effects across reversals, choice frequencies were determined by the underlying probabilities of the decks rather than their physical attributes (e.g., deck position or color). Additional behavioral analyses included trials to first reversal, trials to post-reversal recovery, and trials to post-reversal switch. The latter two were restricted to the first reversal in the first block. Trials post-reversal were counted from the first-negative feedback trial following the true reversal event. Recovery was defined as switching to the best deck and staying for at least one additional trial.

### Computational modeling

#### Materials

The Hierarchical Gaussian Filter (HGF) toolbox v5.3.1 is freely available for download in the TAPAS package at https://translationalneuromodeling.github.io/tapas (Mathys et al., 2011; Mathys et al., 2014). We installed and ran the package in MATLAB and Statistics Toolbox Release 2016a (MathWorks, Natick, MA).

#### Perceptual parameter estimation

In the human reversal-learning experiments, we estimated perceptual parameters individually for the first and second halves of the task (i.e., blocks 1 and 2). Each participant’s choices (i.e., deck 1, 2, or 3) and outcomes (win or loss) were entered as separate column vectors with rows corresponding to trials. Wins were encoded as ‘1’, losses as ‘0’, and choices as ‘1’, ‘2’, or ‘3’. We selected the autoregressive 3-level HGF multi-arm bandit configuration for our perceptual model and paired it with the softmax-mu03 decision model.

Rat reversal-learning data was entered similarly, with choices designated as ‘1’, ‘2’, or ‘3’ and reward presence or absence noted as ‘1’ and ‘0’, respectively. Perceptual parameters were estimated as a single block per session and averaged across Pre-Rx or Post-Rx sessions for each subject. Since the contingency remained 70-30–10%, we used the default start point values of µ2 and µ3, as in block one estimations for the human reversal-learning experiments).

#### Simulations

We performed ten simulations per participant (online version 3) to determine whether our parameter estimates and model successfully captured behavioral differences between groups (e.g., win-switch rates). Each simulation required the participant’s actual data (i.e., the column vectors ‘outcomes’ and ‘choices’) and the corresponding set of derived perceptual parameters. On each trial, a new choice was simulated conditional on the actual inputs in previous trials.

To illustrate the effects of each parameter on task behavior we doubled or halved one parameter at a time, by establishing a baseline set of perceptual parameters containing the average values from the low paranoia participants (online version 3). We then ran 10 simulations per subject for each of the following conditions: baseline, 2κ, 0.5κ, 2µ30, 0.5µ30, 2ω3, 0.5ω3, 2ω2, 0.5ω2, and the average perceptual parameters (κ, µ30, ω3, and ω2) from Post-Rx methamphetamine rats. The 2ω2 condition yielded parameters in a region where model assumptions were violated (negative posterior precision error message) and was excluded from further analysis. Win-shift and lose-stay rates were calculated from each simulation as follows, and then averaged for each condition:

$$
Win-switchrate=\frac{Numberoftrialsinwhichchoiceswitchedafterpositivefeedback}{Totalpositivefeedbacktrials}
$$



$$
Lose-stayrate=\frac{Numberoftrialsinwhichchoicerepeatedafternegativefeedback}{Totalnegativefeedbacktrials}
$$

For each participant, we divided rates derived from each condition by the baseline rates to determine relative win-switch and lose-stay rates. We compared each relative rate to the baseline condition (i.e., 1.0) with paired-samples t-tests using Bonferroni-corrected p-values.

#### Parameter recovery

We performed perceptual parameter estimation (see above) on 10 simulations per subject using first block data from online version 3. These simulations were generated from each subject’s corresponding perceptual parameters. We averaged recovered parameters across simulations and low versus high paranoia (Figure 7).

#### Alternative models

We employed a Q-learning model with separate parameter weights for positive and negative prediction errors to determine whether differential weighting might contribute to paranoia group effects. This model has been described previously (Lefebvre et al., 2018). We also evaluated whether a simpler two-level HGF model might suffice to capture paranoia group differences. To sever the third level from the model, we fixed the log- κ parameter at negative infinity (i.e., by additionally setting the variance to zero), and similarly fixed the values of µ3, ω3, ω2, Φ3 at the values previously assigned in the configuration file. Parameter estimation was performed as described above, with a softmax decision model.

#### Statistics

Unless otherwise specified, statistical analyses and effect size calculations were performed in IBM SPSS Statistics, Version 25 (IBM Corp., Armonk, NY), with an alpha of 0.05. Box-plots were created with the web tool BoxPlotR (Spitzer et al., 2014). Model parameters were corrected for multiple comparisons using the Benjamini Hochberg (False Discovery Rate) method. Bonferroni corrected results were largely consistent (Table 4).

To compare questionnaire item means between two groups (Table 1, low versus high paranoia), we conducted independent samples t-tests. To compare questionnaire item means across paranoia groups and task versions (Table 2), we employed univariate analyses. Associations between characteristic frequencies and subject group or task version were evaluated by Chi-Square Exact tests (two groups) or Monte Carlo tests (more than two groups). Pearson correlations established the associations between paranoia and BDI scores, BAI scores, win-switch rates, and κ. We selected two-tailed p-values where applicable and assumed normality. Multiple regressions were conducted with κ estimates from the first task block (dependent variable) and paranoia, BAI, and BDI scores from online version 3.

To compare HGF parameter estimates and behavioral patterns (win-switch, U-value, lose-stay) across block, paranoia group (Experiment 1, Experiment 2 version 3), and/or task version (Experiment 2), we employed repeated measures and split-plot ANOVAs (i.e., block designated within-subject factor, paranoia group and task version as between subject). We similarly evaluated Experiment three parameter estimates for treatment by time interactions. For Experiment 2, we performed ANCOVAs for μ30, κ, ω2, and ω3 to evaluate three sets of covariates: (1) demographics (age, gender, ethnicity, and race); (2) mental health factors (medication usage, diagnostic category, BAI score, and BDI score); (3) and metrics and correlates of global cognitive function (educational attainment, income, and cognitive reflection). Unless otherwise stated, post-hoc tests were conducted as least significant difference (LSD)-corrected estimated marginal means.

Meta-analyses were conducted using random effects models with the R Metafor package (Viechtbauer, 2010). Mean differences were assessed for low versus high paranoia groups in the in-laboratory experiment and online version 3. Standardized mean differences (methamphetamine or high paranoia versus saline or low paranoia) were employed to account for the differences in task design between animal and human studies.

The 2-step clustering analysis approach was selected to automatically determine optimal cluster count and cluster group assignment. Clustering variables included paranoia-relevant parameter estimates (μ30, κ, ω2, and ω3) from Experiment 1 (block 1); online, version 3 (block 1), and rats (Post-Rx) as continuous variables with a Log-likelihood distance measure, maximum cluster count of 15, and Schwarz’s Bayesian Criterion (BIC) clustering criterion. We validated our clustering solution by sorting the data into two halves and running separate cluster analyses. We also compared cluster solutions derived exclusively from rat data versus human data. A Chi-Square test determined the significance of the association between cluster membership and group (methamphetamine/high paranoia versus saline/low paranoia).

### Data availability

Data are available on ModelDB (McDougal et al., 2017; http://modeldb.yale.edu/258631) with accession code p2c8q74m.
