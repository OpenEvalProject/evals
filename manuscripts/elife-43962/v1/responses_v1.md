# Author response - Round 1

Authors:
- Javier A Suarez ([ORCID: 0000-0001-5887-4518](https://orcid.org/0000-0001-5887-4518))
- James D Howard ([ORCID: 0000-0002-9309-3773](https://orcid.org/0000-0002-9309-3773))
- Geoffrey Schoenbaum ([ORCID: 0000-0001-8180-0701](https://orcid.org/0000-0001-8180-0701))
- Thorsten Kahnt ([ORCID: 0000-0002-3575-2670](https://orcid.org/0000-0002-3575-2670))

## Response text

DOI: [10.7554/eLife.43962.032](https://doi.org/10.7554/eLife.43962.032)

Essential revisions:

1) This is null result with a rather low number of subjects (n=19). The reviewers require more information why this is a null result rather than a study with too little power.

It would be helpful to provide more quantitative insights here. For instance, a power analysis as described in Mumford and Nichols (2008) or better for a post-hoc case "percent change threshold" estimation could be used

(Nichols, 2002).

The reviewers bring up an important issue. How do we know whether our null result suggests that there is no effect (i.e., the null hypothesis is true) rather than that we did not have enough power to reject the null hypothesis? This is a difficult problem with every null result and there is no satisfying way to fully address it. Our original discussion already touched on this issue, but we agree that additional quantitative information would be helpful.

As a preface, we are fully aware that post-hoc or achieved power analyses are not particularly informative (Mumford, 2012), especially for null results because high p-values always indicate low power (Levine and Ensom, 2001;Hoenig and Heisey, 2001). That said, we attempt to address this concern below in several different ways.

First, we initially powered our study to find an effect for identity PE in the midbrain, as described in our previous paper (Howard and Kahnt, 2018). The size of the identity PE in the midbrain observed here (d=0.84, bootstrapped 90% CI [0.60, 1.36]), indicates that our sample of N=19 provides >90% power for this effect at p<0.05. In other words, our current study was adequately powered to detect responses to identify PE in the midbrain and allowed us to replicate our previous findings. This positive result is important because it shows that trivial explanations (e.g., insufficient fMRI signal in the midbrain, errors in data processing or statistical analysis, etc.) cannot account for the present null result.

Second, the critical test for our main hypothesis was the comparison of PE-related signals evoked by between- and within-category reversals in the midbrain. Given that no previous study (that we are aware of) has compared PE-related responses evoked by between- vs. within-category reversals, we had no empirical basis for computing the a priori power for detecting this effect. Instead, we designed our study such that PE’s evoked by between- and within-category reversals were uncorrelated (i.e., occurred in different trials) and reasoned that if we were sufficiently powered to detect identity PEs in general, then our sample would also provide enough power to detect the category effect, if it exists at all.

Third, the p-value for the comparison of PE-related activity evoked by between- vs. within-category reversals in the a priori midbrain ROI was p=0.937. This is nowhere near our statistical threshold of p<0.05.

Fourth, confidence intervals (CI) have been suggested as a viable alternative to relatively uninformative post-hoc power analyses (Mumford, 2012; Goodman and Berlin, 1994, Ann Intern Med), because they provide an idea of the range of effects that are supported by the data. The estimated effect size of our critical comparison (between- vs. within-category PE) in our a priori midbrain ROI was extremely small (Cohen’s d=0.11; 90% CI [−0.24, 0.67]). Importantly, the 90% CI illustrates that even very extreme (i.e., unlikely) estimates of this effect would still be considered as relatively modest (Cohen, 1988).

Finally, we performed an a priori power analysis to estimate the sample size that would be required if we were to design a new study based on the effect observed here (Mumford, 2012). This analysis shows that we would have to collect data from a very large number of subjects (N=651) to have >80% power to detect this effect at p<0.05. This provides further support for the idea that the effect, even if it were to exist, is probably too small to be meaningful.

Taken together, while we cannot exclude the possibility that the present null result is due to insufficient power, we feel relatively confident that our results indeed indicate the absence of an effect of perceptual distance on identity PE magnitude. We now discuss this issue more thoroughly in the manuscript.

Discussion:

“Reasons for this failure fall into three general categories, the consideration of which are instructive both for understanding the signal and for constructing future experiments to identify its properties. […] Taken together, while we cannot rule out the possibility that the present null result is due to insufficient power, we are relatively confident that this was not the case here, and that if sensory PEs are linearly modulated by perceptual distance, this modulation is presumably very small.”

2) Although orthogonalization can be adequate, in the study presented here it is probably not necessary as detailed in the cited paper by Mumford. The key results should therefore also be presented without orthogonalization to get an unbiased picture of the influence of value and the effects of collinearity.

We appreciate this thoughtful comment and agree that in our case, orthogonalizaton is not necessary. We have therefore reanalyzed all fMRI models with orthogonalization turned off. We now note this in the Materials and methods section.

Materials and methods:

“Serial orthogonalization of parametric regressors was turned off for all analyses reported here (Mumford et al., 2015).”

Accordingly, we have updated all fMRI results, figures, and tables included in the manuscript, as well as the supplementary materials and source data files. Overall, the results are qualitatively similar. The only notable difference is that the difference between unmodulated and MDS distance-modulated PE-responses in piriform cortex is no longer significant (p=0.065). All other effects remain the same.

Results:

“Post-hoc paired t-tests showed that the main effect of modulator was primarily driven by significantly higher parameter estimates for PEs unmodulated by perceptual distance in posterior OFC (t(18)=2.36, p=0.03, Figure 5), but no significant differences were found within the midbrain (t(18)=1.58, p=0.194), PC (t(18)=1.96, p=0.065), and amygdala (t(18)=1.86, p=0.08).”

3) Related to the point above, the correlations between the different quantities (identity prediction errors, perceptual distance, value prediction errors, modulated and unmodulated PEs) should be given.

We thank the reviewers for bringing up this important point. Identity PE and value PE were not correlated (r=-0.0075 ± 0.01), but unmodulated identity PE and identity PE modulated by MDS distance were substantially correlated (r=0.93 ± 0.05). We now report these correlations in the manuscript and discuss that they may explain the modest differences between sensory PEs modulated and unmodulated by perceptual distance.

Results:

“Of note, identity PEs modulated by MDS-based perceptual distance and the unmodulated identity PEs were substantially correlated (r=0.93 ± 0.05), which may explain the lack of strong differences between parameter estimates reported above. […] Overall, these findings further suggest that perceptual distance is unlikely to play a major role for sensory PEs in these regions.”

Materials and methods:

“Although value and identity PE were relatively uncorrelated (r=−0.0075 ± 0.01), this was done to ensure that identity PEs were not confounded by residual value PEs that may have resulted from imperfectly matched odor pleasantness.”

In addition, we would like to emphasize that the critical test of our hypothesis comes from an analysis that compares PE-related responses evoked by two different sets of trials (i.e., PEs evoked by between-category reversals vs. PEs evoked by within-category reversals). Thus, because this test is based on orthogonal repressors per our experimental design, it is not influenced by correlations between the variables reported above.

References:

Goodman SN, Belin JA. The use of predicted confidence intervals when planning experiments and the misuse of power when interpreting results. Ann Intern Med. (1994) 121(3):200-6.

Hoenig JM, Heisey DM. The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis. American Statistical Association (2001) 55(1):1-6.

Levine M, Ensom MH. Post hoc power analysis: an idea whose time has passed? Pharmacotherapy. (2001) 21(4):405-9.
