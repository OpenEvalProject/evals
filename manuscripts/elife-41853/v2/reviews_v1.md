# Peer review - Round 1

Editors:
- Ofer Tchernichovski, Hunter College United States

Reviewers:
- Franz Goller, University Utah United States

## Review text

DOI: [10.7554/eLife.41853.015](https://doi.org/10.7554/eLife.41853.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Energetic costs and locomotor constraints on vocal development" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom as a guest Reviewing Editor, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Franz Goller (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Gustison and colleagues recorded and analyzed the development of coordination between vocal and locomotor behaviors in the marmoset monkey. Results show that mature vocalizations develop earlier than locomotion. Further, coordination between vocalization and locomotion develop gradually. Younger infants produce mature-sounding vocalizations only while not moving. Older infants, on the other hand, coordinated their vocalization with movements. Recording heart rate suggest that energetics constraints could potentially explain the late development of coordinated behavior across modalities. However, the reviewers found some substantive concerns, as elaborated below.

Essential revisions:

There are two very major concerns that should be fully addressed before resubmission can be considered:

First, all reviewers concluded (during discussion) that data do not support the major claims authors make about energetic constraints on the development of vocal-locomotor coordination. Therefore, authors should drop out heart rate as a measure of metabolic cost of vocalization. Instead, the revised manuscript should be focused on describing the developmental trajectories with more details, and compare them to relevant literature in other species (which should be presented in Introduction).

Second, authors used sessions (and sometimes even calls) as independent measurements to make statistical inferences. In the revised version, statistics should be redone using each animal as a statistic (i.e., with df = number of monkeys -1). It is essential to test if the phenomenon of different maturation rate can hold using simple paired comparisons. Further, performing the statistics on the fitted spline curves makes it hard to assess if conclusions are sufficiently supported. The dynamic analysis of calls/locomotion coordination should also be supported with similar statistics.

Reviewer #1:

This is an important longitudinal study that compare maturation rate of vocalization to movement and postures. Authors discoveries, if correct, are of general theoretical and practical interest. Of particular interest is the dynamic analysis of movements and calls coordination, showing reversal of patterns over development. Before this manuscript can be published, several concerns about the statistical approach and about conclusions should be addressed:

A) Statistical approach:

1) Using each call as independent statistic is problematic, and (to my knowledge) not an acceptable practice in acoustic analysis. At least for the most critical tests, the n must be the number of monkeys studied, namely 7.

2) Authors should be more careful with their statistical modeling, and take a simple, direct approach whenever possible. In particular, when comparing time courses of calls and movement maturity indexes, author should simply test if those time courses are different. That is, the null hypothesis should be that those are the same. Here all we need is a pairwise comparison within each subject: is the zero crossing the same or not? Such pairwise comparison with n=7 using paired Wilcoxon, or even paired t or just binomial test would be (one can safely reject the null hypothesis (with p=1/2^7) and conclude that the maturation time course of vocalization is indeed faster.

3) The way authors did the test is inappropriate in several ways. First, raising 3 distinct hypotheses (H1= more, H2=same, H3=less) is not necessary, it suffice to look for a significant difference from null. Second, and most critical – where do 124 degrees of freedom comes from? This looks like an obvious pseudo-replication, which resulted with illegitimate power of W = 3936 (!) and an erroneously huge significance (p < 0.0001). Such p values are rarely correct in biology, certainly not with the sample size of the current study.

4) Similarly, the analysis of movement vs. Wiener entropy should be done with each monkey as a statistic, and again, paired comparisons should be done within each animal.

5) The only place where I find it reasonable to use calls as statistics is in the dynamic analysis shown in Figures 4 and 5. In such a fine grain developmental analysis, and after the major effects where established, it makes sense to look at time courses of call movements interactions, considering each event as statistically independent.

B) Conclusions:

This is an important, but still a correlational study – we don't know cause and effect. For example, the statement "infants must overcome the energetic costs of coordinating their vocalizations with body movement" is not fully supported by the data. For example, the marmoset is likely to vocalize while already agitated and this effect might be age related. Further, one might suspect that vocalization might be used to communicate high energy/agitation state.

Reviewer #2:

In this very interesting and well-written manuscript Gustison et al. address the maturation of two motor systems (vocal and locomotor) in marmosets and test a string of clearly defined hypotheses. The authors quantify vocal, postural and locomotory behaviors over complete postnatal development and the resulting datasets are impressive. They use these observations to compute maturity indices for the three behavioral classes, allowing comparison of maturity onsets for the systems separately. The authors convincingly show that young infants only produce adult like calls when not moving and older ones can move while calling. The paper includes several novelties: i) concurrent analyses of both the developmental timescale as well as the real-time (seconds) timescale to investigate energetic tradeoffs during vocalizations. ii) which allows to them study coupling for the first time. The authors show that this coupling exists at the second scale suggesting higher energy investment in calling behavior is required for producing mature calls. The data is well presented with clear figures.

Major comments:

1) The data is used to support the hypothesis that mature contact call production requires an energy investment that increases with age. In the light of energy expenditure during vocalizations this can be explained if the calls get louder. Increasing respiratory effort and thus lung pressure increases predominantly sound amplitude in laryngeally produced sounds. Fundamental frequency only changes slightly with pressure. Wiener entropy as a measure for noisiness is not regularly used outside of the birdsong field, but will increase most likely in chaotic regimes when pressures are very high.

It would be rather straightforward for the authors to quantify the source levels of the vocalizations. The low-frequency cry is not directional but the wave-number can be used to coarsely estimate the directionality of the phee call. (ka = 2pi/λ * a (, where λ is wavelength (v/f) and a is emitter size radius – guessing 2 cm for a marmoset. with k=2pi/(340/7000) and a = 0.02) ka=2.5, which is above 1. Thus the phee call is directional, which makes it more complicated to compute source levels without microphone array. However luckily the microphone was located in the far-field 90 cm above the cage directing down, making vocalization's aimed in the horizontal plane directly comparable.

2) The authors list four empirical data papers in the last paragraph of the discussion that investigated human infant vocal-locomotor coordination. At least Berger et al. and Abney et al. present similar datasets of concurrent posture and vocalization (not at the second timescale). These papers should be acknowledged and placed in perspective up front in the Introduction.

3) The locomotor behavior was basically scored as difference images. Did the authors observe any structural changes in locomotory patterns, such as certain accompanying displays (vocal postures) that matured over development?

Reviewer #3:

General comments:

This manuscript describes a research effort, in which development of locomotor and vocal skills as well as, importantly, their coordination have been studied quantitatively and have been related to energetic aspects. This is a very interesting study that tries to fill a gap in our understanding of the ontogeny of motor system coordination and its energetic background. The presented data partly meet the goals set out in the Introduction (questions 1-3), but especially for questions 2 and 3 fall somewhat short and require clarification.

1) The various sets of hypotheses listed in the results present sets that leave out potential alternatives. Specific suggestions are mentioned below.

2) The assessment of the energetic cost of call production is problematic at multiple levels, from the premises to the estimate and the interpretation. Specifically, the following general points should be considered:

2.1) Several assumptions had to be made to convert heart rate to metabolic activity. We know from critical assessments of the technique that careful calibrations are needed to achieve reliable estimates. That means that the applied conversion factors may not be valid across development within an individual and certainly are problematic when applied across individuals. Whereas this is a general difficulty with the technique that cannot be solved in this study, it should be acknowledged and should lead to more careful conclusions.

2.2) It is not clear to me how baseline levels of heart rate have been determined for call production episodes with and without locomotor activity. Because heart rate changes are very dynamic, this is one of the critical methodological issues, which we face. Are observed changes due to actual changes or differences in baseline levels?

2.3) Rapid changes in heart rate can be caused by motivational and other modulatory factors that have no direct link to energy expenditure of a behavior. This is a major shortcoming of using heart rate to assess the metabolic cost for short-duration behaviors.

2.4) It is not clear to me how the cost of locomotion, which is expected to be several-fold greater than that for vocalization has been disentangled to conclude that production of phee calls imposes a high metabolic cost.

3) The presentation of the results is interwoven by methods (somewhat necessitated by the fact that the method section is at the end) and lots of introductory material and posing of hypotheses. The actual results are then described very briefly, and statistical as well as descriptive presentation is quickly reduced to very derived spline curves. At least to me this generates the feeling that I do not know the results sufficiently to assess whether or not the later conclusions are supported sufficiently.

Specific comments:

Abstract: Is the intended meaning that locomotion uses resources that would otherwise be available for call production? I cannot see that such an energetic bottleneck exists. If a constraint exists, it is more likely that locomotion and call production require either muscle efforts that are difficult to generate simultaneously or some other coordination-related trade-off. The absolute energy level is very unlikely to be the bottle neck here.

Introduction paragraph one: Of course, there are always energetic costs to vocal production. How much energy is required may vary, but as discussed above it is hardly so high that energy levels prohibit vocalization.

Subsection “The vocal system matures before postural and locomotor systems” paragraph two: This description of hypotheses is almost "trivial" and thus does not need to be so elaborate.

Subsection “Mature contact call production and locomotor activity become increasingly coordinated during development”: These hypotheses are based on the same notion that absolute energy levels at the time of vocalization could dictate whether or not calls can be produced. I do not see that such an energy shortage could exist. It is more likely (as alluded to above) that other factors dictate whether or not a call can be produced (e.g., can a particular respiratory muscle generate sufficient force if it also is engaged in locomotion, etc.). Another matter is whether or not an animal engages in a particular behavior because of general energetic condition. These conceptual issues are at the heart of this paper, and, in my opinion, the current reasoning is not realistic in regard to the physiological understanding of metabolic cost and movement.

Subsection “Mature contact call production and locomotor activity become increasingly coordinated during development”: This discussion would read very differently if the constraint were seen more like discussed above.

Final sentence of subsection “Mature contact call production and locomotor activity become increasingly coordinated during development”: This statement may have to be revised if calibrations at different ages were available.

Materials and methods: It is not clear how baseline heart rate was determined. Because metabolic cost of locomotion is not restricted in time to the actual duration of movement, but elevated metabolism continues after the movement, the timing of call production relative to locomotion is very important. This issue is very critical, if the costs of locomotion and vocalization are to be disentangled. It is also not clear how z-scores were calculated to make data comparable over developmental time.

[Editors' note: comments from the first round of re-review follow.]

Thank you for resubmitting your work entitled "Coordination of vocal and locomotor behavior emerges in development as a function of arousal state" for further consideration at eLife. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below.

In particular:

1) Statistics need improvement. Please provide cross validation by doing shuffle statistics (shuffling subjects across groups). Also, if you choose to continue with the GLM please provide detailed statistical results including within and between subjects results.

2) As reviewer 3 noted, the problem of disentangling metabolism related to locomotion from emotional influences is not fully resolved by using the term 'arousal'. A weaker interpretation of the results could help (in addition to clarifying terminology as suggested).

Reviewer #1:

Authors addressed my comments and the manuscript is much improved but I am still worried about the statistics. Authors now use GLM throughout but they did not specify how dependent repeated observations are treated in the model. judged by the p values, which are all lower than 0.0001, I suspect that p values are based on the dependent call events and movement events as the statistics, rather than the animal. This is a problem. I will need to see the breakdown of within and between subject results, and how p values were computed to confirm, but looking at the raw data, I am almost sure that p values are wrong. Authors should keep in mind that as opposed to R, Matlab is not a statistical software, and it is very easy to get the model wrong. One should use Matlab statistical packages carefully, particularly when extracting p values from complex models, to make sure all assumptions are correct. I still believe it would be much safer to shuffle statistics here: simply shuffle subjects across groups and extract direct p values. Simple is better than sophisticated.

Reviewer #2:

After carefully reviewing the response to reviewers and the new manuscript, I do not have any substantial concerns and recommend the paper for publication.

Reviewer #3:

The manuscript has been improved following the suggestions. The metabolic data and associated argumentation have been taken out. In its place, the heart rate data were used to assess "arousal". "Arousal" is a vague concept and is not defined very well in this manuscript. Whereas I do not see the issues as critical as in the case of metabolism, I am not clear on whether or not the problem of disentangling metabolism related to locomotion from emotional influences has been solved any better here. Perhaps I still do not understand it correctly, but the issue of baseline data has in my opinion also not been resolved satisfactorily. Namely, the interpretation of whether or not and how much heart rate increased depends on the period of baseline measurement. I am not sure I understand what a session is (letter) for which the normalized data are taken. Is it the period before and after as outlined in the manuscript? Certainly, different locomotor activity during these periods will make comparisons very difficult. Because locomotor behavior increases with maturity level, so will the associated heart rates. To what degree it is a change in arousal, can therefore only be said with confidence if the two influences on heart rate can be disentangled.

[Editors' note: comments from the second round of re-review follow.]

Thank you for resubmitting your work entitled "Coordination of vocalization and locomotion emerges in development in association with arousal state" for further consideration at eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor), a Reviewing Editor, and a statistician expert. Unfortunately, there are still very serious issues with statistics that preclude publication of your manuscript in eLife at its present form.

Following your disagreement with the reviewers’ criticism about statistics, we sent your manuscript to a statistician expert. The expert concerns are similar to those raised earlier, but are even more substantial. We are worried about the p-values you reported, which seem inconsistent with your sample size and with the raw measures. Therefore, we cannot accept your manuscript, unless we can validate and replicate your results, according to the guidelines provided by the statistician expert.

We would like to clarify that as much as we find your study interesting and potentially valuable, unless the revised version can fully convince the expert that the stats and p-values are correct and easily replicated, we will have no choice but to reject your manuscript.

Reviewer #4:

Major concerns:

1) Authors use LMM which is fine. They say they have infants as random effect and that is fine too, but I wonder how could authors get with 7 monkeys p<0.0001? I looked at the tables with per-animal results. The variability is high in the coefficients per monkey, sometimes with results of opposite directions. Treating them as a sample does not yield the precision near to that claimed.

2) I cannot exclude the possibility that authors may be right, BUT when submitting such an analysis reproducible computing is a must. The statistical model itself should be specified and the entire code made available. I think that giving this information is minimal requirement, but making the code and the data available at this stage so that reproducibility could be checked is already a requirement made by leading journals and here it is crucial.

3) In particular in this case, it is important to know whether the model considered sessions as nested within monkeys or not. It will have great impact, and you cannot tell it from the information authors provided.

4) In the correlation analysis authors use all observations as if they are independent and that is wrong, but since it is used only for creation of scale it does not matter much.

5) Authors also present too many figures only with no data, only summaries: all of 4 and 5B.

6) eLife requires treatment of multiplicity issues; none of that was done.

[Editors' note: comments from the third round of re-review follow.]

Thank you for submitting your article "Vocal and locomotor coordination develops in association with arousal state" for consideration by eLife. Your article has been reviewed by one peer reviewer, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

We appreciate authors efforts to correct the statistical issues. However, there are still major problems with statistics that authors need to address before the manuscript can be accepted. Please carefully follow the statistician guidance, and in particular correct the models to include individual slopes, and properly adjust p values for multiplicity. Please send us correspondence if statistical significance of the major finding is no longer valid.

Reviewer #4:

Reviewer notes on "Vocal and Locomotor coordination…" by Gustison et al.

I thank the authors for their response to my previous questions. Their effort to make their analysis transparent and reproducible are evident in this version. I hope this version can serve as a model for reproducible research for others.

These compliments do not mean that there are no problems with their analyses,

I shall list three of them:

1) The model they used allows only random intercepts, and not random slopes.

hence the variability from one monkey to the other is not reflected in the calculations of the slope's standard deviation and p-value, which are far too small. In order to enhance replicability of their results, when the experiment will be conducted on another set of monkeys the random slopes inference is important (Then the models should be ~Day + Day/Subject)

The analyses for individuals is appropriate so it lets assess how serious this flaw is.

Sometimes it is very inappropriate: HeartRatePercentileMean~CallType_Cry0Phee1

The estimated same slope is is 3.6 and StanError.96

The individual ones are 1.09, -4.9, 6.4, 3.4, -0.9, 10.8, 7.7 and from these 7 values the standard errors about 2.

Sometimes it will be more reasonable and the conclusion will probably remain unchanged.

The estimated same slope is is.25 and StanError.06

The individual ones are.25,.39,.11,.25,.2,.11,.11, and from these 7 values the standard errors about.04

2) When modelling individual events within the day (from Analysis 1.5 on) all observations within a day (up to 50) are assumed independent.

In such longitudinal data within the day correlations from observation to the next one are expected to be high.

This hampers analyses of individuals as well producing to optimistic standard errors and small p-values.

A simple way out is to construct a daily summary.

3) Adjusting for multiplicity is needed also when trying different models for heart rate, namely its dependency on different variables and in different subsets (1 month 2nd month etc)

With the current p-values not much will change in the conclusion, with new ones I do not know.
