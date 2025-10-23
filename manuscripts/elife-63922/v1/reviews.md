# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63922.sa1](https://doi.org/10.7554/eLife.63922.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript will be of interest for social psychologists and neuroscientists as it presents a first step toward understanding the neural correlates of decisions that involve corruption and harm third parties. The behavioral and neuroimaging data support the conclusion that different moral costs associated with such choices are correlated with activity in different brain areas (anterior insula and temporo-parietal junction), but integrated into a value signal in the ventromedial prefrontal cortex.

Decision letter after peer review:

Thank you for submitting your article "Neural basis of corruption in power-holders" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This human fMRI study focuses on the behavioral and neural correlates of decisions involving fraud and corruption. In a novel behavioral task, subjects could either accept or reject offers from a proposer who divided a monetary payoff in a recommended or fraudulent way. The latter involves a bribe to the participant as well as harm to a third party. The key finding is that the two types of moral costs at stake here (norm violation and harming a third-party) correlate with activation in different brain regions (insula and TPJ).

All reviewers agreed that this study addresses an important question and that it is well executed, with an impressive set of analytical tools. They also agreed that the manuscript will be of interest to a broad readership. However, there was consensus on several important issues that need to be addressed in a revised version of the manuscript.

Revisions:

Reviewers identified several essential issues that need to be addressed before the manuscript can be accepted for publication in eLife:

1) There is a concern about selective reporting and cherry-picking. Findings should be reported more comprehensively in the main text and SI. And clarification is needed regarding how correction for multiple comparisons was applied (ROIs, models, etc.).

2) There were concerns about the lack of random effects in the mixed linear models for the analysis of behavioral data.

3) It would be important to present data to confirm that subjects believed the cover story as a basic manipulation check of the experiment.

4) Please include a more detailed plan for data and code sharing.

5) Please revise the framing of the manuscript.

6) The individual differences analysis is likely underpowered and the results should clearly be described as exploratory.

Reviewer #1:

This manuscript assesses the behavioral and neural correlates of decisions to accept an offer from a proposer who either follows a monetary payoff recommended by the computer (control condition) or lies by choosing the option not recommended by the computer (bribe condition). In addition, in a solo scenario, the proposer's offer to the participant does not harm anyone, while in a dyad condition it harms a third party whose payoff will be decreased as a consequence of the proposer behaving dishonestly by not following the computer choice. The authors report that these two moral costs (the proposer "lying" and the third party being harmed) both reduce the participants' propensity to accept the proposer's offer, and can be captured by two parameters in a computational model. Finally, a combination of univariate and multivariate analyses of the neuroimaging data is reported to identify how some of the model-predicted signals are encoded in the brain, and particularly in the anterior insula, TPJ, vlPFC and dlPFC.

This study is impressively executed, the manuscript is clearly written, and the topic of moral transgression and integration between dishonest behavior and third-party harm is novel and very relevant. However, I still have concerns that I would like to see addressed before I can recommend this manuscript for publication.

1) Study framing and ecological validity

a) Given the current climate in the world of misinformation spreading and the media tendency to misinterpret scientific results and jump to conclusions, I would recommend the authors to use a title and a framing that reflects more precisely the findings of their study. As they acknowledge, corruption is a very complex process, and what their task assesses is a small part of what can lead to corruption, namely the role of two forms of moral transgressions (fraud and third-party harm) in the decision to accept a bribe, and their representation and integration in the brain. Generally, I would refrain from using such a strong term as corruption, except maybe in the Discussion where the implications of the findings in light of understanding corruption can be brought up.

b) This concern mostly stems from the overall lack of ecological validity of the task used. Specifically, the proposer's behavior was fully controlled by the experimenter (and a cover story was used to pretend otherwise) and it is unclear whether participants fully believed the cover story or not. Was participants' belief that proposers and third parties were attendants of a previous study actually tested? If participants don't believe this cover story and instead suspect that everything is fictitious, their behavior would not constitute a moral transgression. In the dyad situation, it also seems like the third party will never know that they actually would have gotten a better outcome if the proposer hadn't lied. If that's indeed the case, that would make the current task less likely to mimic real-life situations where third parties are aware they were harmed (e.g. competitors for a project who do not get selected).

c) If I understand the design correctly, there was never a situation where the computer picked the low payoff option and the proposer also honestly reported this offer. This appears to me as a major drawback of the task as the participant could interpret the proposer's behavior as being simply value maximizing rather than fraudulent or dishonest. Also, while helpful for the analysis, the fact that essentially every single trial contained a bribe is concerning. If proposers' choices had been obtained in a previous online study, they would have likely looked very different than what is being displayed to the participants in the current task. Presumably, many proposers would have followed the computer choice even for the low payoff option, and/or would not have offered to split their offer by the indicated proportions. Additionally, it is likely that the share offered by the proposer would be higher in the bribe than in the control condition. I believe all these concerns should be acknowledged in the Discussion.

2) fMRI analysis and interpretation of results

Generally, I find that the fMRI results lack cohesion and a clear interpretation that tie them together, mostly due to the combination of many methods/GLMs used and not always justified, to the unclear process of selecting and using multiple regions of interest, and to potential confounds in the contrasts and regressors examined.

a) How many regions of interests were included? The authors state in the Materials and methods that they used a whole-brain cluster-level FWE correction at P<0.05, but most the key results are in fact small-volume corrected. It seems very unlikely that the authors had only one a priori region of interest in mind for each analysis they report. In the Introduction for example, they seem to focus on four key regions (vAI, TPJ, vmPFC, dlPFC), but other studies on dishonesty have reported potential roles of the amygdala (Garrett et al., 2016, Nature Neuroscience), or nucleus accumbens (Speer et al., 2020, PNAS) in dishonest behavior. Were other ROIs considered initially? If so, correction for the number of ROIs may be needed.

b) Given the design of the task, any activation contrasting the bribe vs control condition cannot distinguish between representing the proposer lying vs being honest and the computer recommending the low vs high payoff offer, as the proposer always lies when the computer chooses the low payoff. Because of this, I find the results in Figure 3A difficult to interpret. Why would we expect vAI to track expected personal profits positively in the DB condition but negatively in the SC condition, and not at all in the other two conditions? There also seems to be a main effect of scenario (dyad vs solo) on vAI tracking on expected profits, which is not discussed.

c) Why wasn't the expected loss to the third party added as a parametric modulator of the DB condition in GLM1a, thus allowing to control for the expected gains of the participant and the proposer? Is this because the loss to the third party is highly correlated with the gain of the proposer? If so, then those two signals can't be separated, and this should be addressed.

d) The rationale for examining vmPFC-dlPFC functional connectivity analyses is unclear to me. Was connectivity with other regions of interest, like TPJ or vAI, tested but not significant? If so, the authors should be clear about this and correct for the number of regions tested. Similarly, the Materials and methods section about the inter-subjects RSA suggests that several "hypothesized regions including bilateral dlPFC" were tested, but then the results focus exclusively on the dlPFC. If other regions were indeed tested, this should be clarified and accounted for.

e) The interpretation of the IS-RSA results in the Discussion is unclear, especially in what those results mean in and of themselves, and how they can be reconciled with the univariate dlPFC result and the vmPFC-dlPFC functional connectivity analysis.

Reviewer #2:

The reported study investigates the neural basis of corruption in social interactions. The main finding is that two types of moral costs in bribery (norm violation versus harming a third-party) correlate with activation in dissociable brain regions (insula versus TPJ). There is much to like about this well-written manuscript: it addresses an important question, and the experimental manipulations appear sound. The manuscript will certainly be of interest to a broad readership working on social interactions or on the neural basis of decision making. Nevertheless, I have a couple of concerns, particularly regarding data analysis, which the authors need to address in a revision.

1) The GLMs used for the fMRI analyses should be specified in more detail already in the Results section, not only in the Materials and methods. This would make it easier to understand which contrasts show significant activation in insula or TPJ. In general, I find the presentation of the imaging results rather confusing, mainly because a large number of analyses was computed (nine in total: GLM1a-c, GLM2a-b, GLM3, PPI, multivariate analysis, IS-RSA), and the authors often just selectively report one contrast of each GLM, while the results of other contrasts are not even reported in supplementary tables. This analysis approach raises questions regarding the robustness of the imaging results. For example, when testing the hypothesis that the TPJ shows enhanced activation in dyad versus solo scenarios, no significant results are observed in two contrasts for GLM1c, but only in an additional multivariate analysis. However, these non-significant results are ignored in the Discussion section, and the significant TPJ finding in the multivariate analysis is taken as evidence for the authors' hypothesis. It also remains unclear why the authors specified separate models with parametric modulators for personal benefits (GLM1a) and third-party loss (GLM1b), as in principle these variables could be modelled within one model. All this leaves the impression of cherry-picking and makes the imaging results appear less robust and convincing than as they are presented.

2) Regarding the mixed linear models for the analysis of behavioral data, the authors state that "factors allowing varying intercept across participants" were entered as random-effect predictors. Please be more precise regarding which random effects were specified in the model. It is generally recommended to maximize the random effects structure in order to minimize the risk of type I errors (Barr et al., 2013). As the current study seems to follow a strict within-subject design, I think that all fixed-effect predictors should be modelled as random slopes in addition to random intercepts

3) The task did not involve real social interactions, but the offers were computer-generated. I might have missed it, but it seems nowhere stated whether participants believed the cover story or not (was this assessed at all). In any case, the authors should add a caveat in the Discussion section clarifying that the social interactions in the study were only hypothetical.

Reviewer #3:

Dr. Hu et al. report a neuroimaging study of corruption in which (computer agent) proposers provide participants the opportunity to personally benefit from turning a blind eye to deception that in some cases has monetary costs for a third party. Through a series of computational models, the authors confirm that participants incur a moral cost, beyond inequity models, for engaging in the corrupt act, that is at its worst when a third party is injured. Each component of the model is then tied to a specific aspect of brain function that aligns with prior findings. The authors conclude that an inhibition mechanism is associated with reduced participation in corrupt acts.

I enjoyed the paper. It covers an interesting topic, is methodical, and shows a great deal of expertise in a wide range of methods.

1) Tests for the involvement of a particular brain region in a given step of the corruption decision are mixed without justification. GLM and MVPA analyses seem to be deployed as tests with increasing sensitivity rather than to test for computational differences. Not making a distinction is understandable since there is not a consensus on how each should be interpreted. However, this sort of variation on testing until a finding is reached can lead to overestimation of effect sizes and confirmation bias of previously proposed roles. Is there a reason beyond sensitivity for using multivariate models in some cases rather than others?

2) A number of GLMs are used to reach different conclusions presumably because of covariance issues between regressors. This, in and of itself, is not a problem if the covariance tables are shown and the repartitioning of common variance is acknowledged/interpreted.

3) Individual difference model – individual difference studies of forty participants assume a large effect size to be considered reliable. Most psychological (and biological indices) do not fall in this range. The result is fine as an exploratory analysis but that means it should be described as such.

4) Deception success measures. Was any data collected to confirm the believability of the proposer and third-party deception? Were participants debriefed afterwards?

5) The brain data is largely used to lend construct validity to the corruption task and confirm psychological interpretations of the processes involved in the decision. Ideally, the neural data would be used to adjudicate between two competing behavioral models (and/or behavioral data used to adjudicate between competing neural models). This somewhat lessens the utility of a promising neuroimaging dataset.

6) Complete analysis scripts (Main and SI, behavioral and neuroimaging) and minimally processed imaging data should be posted and referenced for the article. It is not clear that these fit in the 'source data' option for eLife without an accession number noted in the article.
