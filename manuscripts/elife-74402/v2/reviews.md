# Peer review - Round 1

Editors:
- Claire M Gillan, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74402.sa1](https://doi.org/10.7554/eLife.74402.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Humans perseverate on punishment avoidance goals in multigoal reinforcement learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Claire M Gillan as Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Christian Büchel as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers were overall favourably disposed to this manuscript – it was felt that the paper extends previous work on how humans use a mix of learning strategies to make decisions in cognitively demanding environments to show that humans flexibly adjust goal-directed learning based on statistics of the environment but inflexibly engage in punishment avoidance regardless of current goals. The task design and model are novel and interesting. However, all 3 reviewers had substantial concerns (i) aspects of the behavioural analysis (modelling), (ii) the interpretations of behavioural effects, and perhaps most substantially, (iii) the extension to psychopathology. I have outlined these essential revisions below by way of summary. Individual reviewers made further suggestions that can be considered optional, though we encourage that they also be addressed as they will strengthen the paper.

Essential revisions:

1) All three reviewers felt that the clinical analyses, albeit interesting, were not approached with the same rigour and clarity as the analyses of behaviour preceding them (which were excellent). A revision must address this comprehensively, including (i) how non-independence of parameter estimates influence clinical analyses, (ii) the inclusion of clinical covariates without first reporting bivariate effects, (iii) correction for multiple comparisons should be more extensive, (iv) visualisation of all clinical effects not just select ones, (v) more complete reporting with respect to all clinical measures gathered (including analysis of somatic anxiety). Related to this, the authors may wish to consider in the discussion that there are potential difference between non-clinical and clinical cohorts in terms of correlation of clinical measures, though the data are still a bit mixed:

Imperiale, M. N., Lieb, R., Calkins, M. E., and Meinlschmidt, G. (2021). Multimorbidity networks of mental disorder symptom domains across psychopathology severity levels in community youth. Journal of psychiatric research, 141, 267-275.

Groen, R. N., Wichers, M., Wigman, J. T., and Hartman, C. A. (2019). Specificity of psychopathology across levels of severity: a transdiagnostic network analysis. Scientific reports, 9(1), 1-10.

2) With respect to the modelling of behaviour, (i) more information about parameter recovery is requested, and (ii) concerns were raised about parameter estimation more generally given the skew evident in the inverse temperatures, coupled with the multicollinearity. More information should be provided here, including proportion of recovered parameters that can capture the main parameter-based results of the paper.

3) The interpretation of the key behavioural effects: could the authors defend the interpretation that GP is not an actual strategy, but rather a noisy or distracted attempt at MB learning. It was felt that it is rather a big claim to say that the GP approach is a reasonable third strategy on top of MF/MB learning and if this interpretation is to be maintained, the authors need to back this up by showing it is something more than just an imprecise MB approach. This ties in with additional concerns about the exclusion of participants that did not obey certain rules of the task. It was not clear how their exclusion was justified given a valid interpretation of some of these key effects may be that (i) people find it hard to keep instructions in mind in complex tasks, (ii) people may be utilising strategies that you have not defined and are not well understood but are nonetheless real – e.g. belief that reward probabilities / 'luck' switches from trial to trial. Other concerns regarding exclusion were that they appear to be asymmetric with respect to reward/punishment conditions, suggesting these data are meaningful.

Reviewer #1 (Recommendations for the authors):

1. Psychopathology analyses.

a. If the authors wish to make a connection to psychopathology, reporting the relationship between worry alone – rather than controlling for other overlapping symptom measures and model parameters – would be more appropriate. The recommendations for testing multiple, partially overlapping psychopathology measures in this paper may be helpful: DOI: 10.1177/21677026211017834

b. An alternate approach would be to focus this paper on the main findings about learning strategies and to save relationships to psychopathology for a future paper with a more appropriate sample.

2. Parameter-based analyses.

a. Providing more information on parameter recovery is needed. In particular, showing the proportion of recovered parameters that can capture the main parameter-based results of the paper (Figure 2C/D) would show that these findings reflect true underlying parameter differences rather than artifacts of model estimation.

b. If the authors retain the psychopathology analyses, they should be conducted in a way that does not assume independence of parameter estimates.

c. Alternatively, the analyses using relative model fits and trialwise regressions provide most of the information needed for the conclusions of the paper. The parameter-based analyses could be omitted with the focus instead on these other kinds of analyses.

Reviewer #2 (Recommendations for the authors):

The authors used the term "predicted" quite a bit to describe associations. I don't think this is justified (they haven't really done any predictive analyses).

If I understand correctly, the same 4 random walks were used for all participants (randomised between the 4 associations). Of the two shown, one looks much more stable than the other. It would be useful to see all 4 walks to see how comparable they are (if I am correct that the same 4 are used for all participants). If the walks are very different, should their allocation to the associations be controlled for in the analysis?

It would be useful to report the relationship between worry and the block effect (i.e. you suggest high worry is associated with higher GP/lower MB for losses-do worried people adapt to changes in the base rates of the outcomes?).

Reviewer #3 (Recommendations for the authors):

Well done on an interesting read and a contribution that will be informative for a lot of researchers. I have some suggestions to improve the paper.

All analyses with the 3 clinical factors should be presented in full; including supplementary figures if possible. Simple associations should be carried out before adding covariates to assist the reader in interpreting these findings and in generating hypotheses based on them. OCD is said to be not related to parameters at p=.08, while worry is at p=0.04 (uncorrected i guess more like p=0.02 for the latter), these are not likely to be different from one-another. And they may depend on the inclusion of these variables in the same model. Reader needs more transparency around these effects and any claims of specificity need more support. The data presented actually suggests the opposite.

Relatedly, the result in relation to worry, the effect is marginal at p=.04. While 2 multiple comparisons are controlled for, this is a fairly liberal decision given several tests were conducted and reported (i.e. GP MB and MF for punishment/reward = 6 at least; plus the 3 clinical scales = 18 etc). I'd encourage the authors to report all of the associations in a table, correct for multiple comparisons. This will serve the same purpose of suggesting the most interesting avenue for future research but also give the reader a fuller view on specificity of this to worry. This exploratory framing for the clinical effects does not detract from the main contribution of the paper or the potential for this to be especially interesting for 'worry' – it would just make them clearer and let the reader decide that for themselves a bit more.

There needs to be a bit more done with respect to relating the clinical variables to the model parameters. I would have thought this would be best placed within the hierarchical model itself. Alternatively, I wonder if these is a point-estimate that could be generated that is more flexible and less dependent on the overall group effects and other parameter values.

The authors describe issues with collinearity of the parameter values. Can a correlation matrix in the supplement be included that reports these (I think currently you can sort of see it based on simulated vs real data, but this is not the same as correlating real vs real across params).

I strongly encourage all subjects are retained (though i feel less strongly about excluding those not completing enough trials, 90% even seems a bit harsh/wasteful of data). If not, then a clear justification for why the strategy or approach of these subjects is not an accurate reflection of potentially the decision making preferences of 22% of the population. More standard indicators of inattentive responding focus on RTs, overly rigid responding that renders modelling choice impossible. Not clear why these were not used here as they seem better justified indicators of inattentive subjects. At the risk of belabouring the point(!), defining these subjects as 'not understanding instructions' could be applied to many of the key findings of this paper (i.e. avoidance perseveration suggests they don't pay attention to the current goals etc). So I think this practice is not ideal.
