# Peer review - Round 1

Editors:
- Neil M Ferguson, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34848.029](https://doi.org/10.7554/eLife.34848.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Using paired serology and surveillance data to quantify dengue transmission and control during a large outbreak in Fiji" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Prabhat Jha as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper presents a modelling analysis of an island epidemic of dengue-3 in 2013/4 giving insight into the effect of seasonality and control measures on transmission.

Essential revisions:

- Greater sensitivity analysis and caveats regarding assumptions about vector population dynamics (see both reviews), including modelling larval carrying capacity or at least rainfall-driven recruitment rates.

- On a related topic – both reviewers comment on how seasonality was included for some parameters but not others. The main demonstrated effects of temperature are on EIP and mortality, plus rainfall via carrying capacity. There's not much evidence around temperature affecting biting rates/transmission coefficients. This aspect needs to be approached more systematically, given the effects of seasonality and of the clean-up campaign may be confounded.

- More detail on the MIA data is needed – as was done for the ELISA data, raw data should be shown (for control and DENV3 antigens), and arguably a mixture model fitted. More justification of the use of 2 assays is also needed.

- Excluding data from the key weeks around the peak of the epidemic is problematic. Suggestions as to how this might be avoided are given in the detailed reviewer comments.

- The Materials and methods section needs to include detail of the model comparison exercise undertaken, and tables of parameter estimates included in the Supplementary Information.

- All datasets used need to be made public with the paper.

Reviewer #1:

This paper presents a nicely detailed study of an island epidemic of dengue-3 in 2013/4. The most novel aspect of the study is the model-based estimation of the possible impact of a control program implemented during the epidemic. The authors make a reasonable case that there is evidence that this program had a moderate impact on transmission but to strengthen the robustness of this conclusion, aspects of the analysis require clarification and further sensitivity analysis. Detailed comments follow (but should not be viewed in light of my overall positive view):

- The transmission model assumes a constant mosquito population size (Equation 0.10). Did the authors attempt to fit a model with density dependent regulation of larval populations, perhaps where carrying capacity is driven by rainfall: i.e. K= c + m R, where R is accumulated rainfall over some time interval T (e.g. 1 month)? This might allow a better fit to the epidemiological data – and might eliminate any statistically significant impact of the clean-up campaign, given the sharp drop in rainfall in May and the peak in April.

- Why assume sinusoidal variation in temperature (Equation 0.13), given the actual data is available (albeit I accept it looks reasonably sinusoidal). Then the functional form used in Mordecai et al., 2017 could be used directly, with priors on those parameters. This would seem to be more satisfying…

- It would be better to represent the clean-up campaign (which would have reduced larval habitat, not adult mosquito density) as a (perhaps linearly increasing over time) reduction in the mosquito source term (multiplier on recruitment rate δ in Equation 0.10, or of carrying capacity) than a direct modifier of transmissibility. Doing so will offset the impact on transmission by a generation time – i.e. ~2 weeks. It may then be possible to fit a parametrically simpler model to the exact timing of the clean-up campaign.

- Little mention is made of the discordance of the MIA assay with the ELISA results – how was seroconversion measured with that assay? If with just a ratio, then perhaps a mixture model would fit better? It would also be good to see the raw results for that assay – the authors spend a lot of time modelling the ELISA results, but then use the MIA data in their default (best fit) model with no comment on the relative reliability of one vs the other. Figure 3B should also be updated to show the MIA results as well as the ELISA ones. More generally, why were two serological assays used? The motivation for this is never stated.

- Table 2 should have the MIA results for 'Any dengue' shown to be able to compare properly with ELISA, especially given the MIA model is the one presented in Figure 5.

- I found it difficult to reconcile the data plotted in Figure 1A with the data points plotted on Figure 5A. Which region was being fitted to – I presumed the whole country, but if that's the case, I don't know why the case numbers peak at about 600 in Figure 5A but at over 2000 in the black curve of Figure 1A. Are weekly case number being plotted in some places, and monthly in others? If so, I suggest using weekly numbers throughout (and updating figures to state 'weekly cases'). It would also be good if Figure 1A was a bit bigger.

- It was unfortunate that disease surveillance changed almost coincident with the clean-up campaign. But I was uncomfortable with the authors dropping 2-4 weeks of surveillance data from the fit. The authors refer to a sensitivity analysis for the number of weeks of data dropped, but I couldn't find the results. At the very least, cases of the two types for the missing 2 weeks should be plotted in Figure 5A, shown in a different colors.

- I think the authors could avoid dropping those critical weeks of data, Assuming the transition occurred at different times for different health facilities, on week t let pt denote the proportion of surveillance using lab confirmation, and (1-pt) be the proportion using DLI. Then the expected total number of reported cases (lab plus DLI) is [pt r1 + (1-p) r2]ct. If O1t and O2t are the reported cases in week t from the two surveillance systems, then O1t/O2t gives an estimate of pt/(1-pt). This chain of reasoning can be represented in the likelihood in a number of ways – by using separate likelihoods for the lab and DLI cases, and estimating pt for each of the 2 currently omitted weeks explicitly, or (more crudely) by pre-calculating pt from O1t/O2t for the transition period, and using a single likelihood for total cases (albeit still with r1 and r2 – though a single k would need to be used in that case). Or there may be some cleverer way to do it! As an aside, I wasn't quite clear why different k values were fitted to the different case types – were the estimates different?

- Wouldn't a beta-binomial model (parameterised in terms of a mean p and a overdispersion parameter) be a better representation of the observation process than a negative binomial?

- Any thoughts on why the first DLI point shown in Figure 5A is so high? Though looking at Figure 1A, perhaps this is an artefact of omitting some data points? Otherwise, could it indicate a transiently negative impact of the intervention? How does the model fit change if that point is excluded (see my early ref to the 2-4 week sensitivity analysis mentioned but not presented)?

- Supplementary File 1 – the EIP is a bit long in my opinion – the blood feeding experiments of Simmons etc. might suggest 10 days is a more reasonable value. Some sensitivity analysis to this would be useful, given changing the generation time will change R0 and thus the relationship between infection attack rates and case incidence (perhaps!)

- Regarding Figure S7 and the need for time-varying transmission neglects individual-level heterogeneity in exposure. I get the basic point about the limited serological attack rate, but heterogeneity could in theory explain this. Such heterogeneity is quite extreme for malaria, and likely to be comparable for dengue, given the more limited vector dispersion range. I accept that time-varying transmission is a more likely explanation, but the authors may still want to comment. In addition, while the authors didn't find significant predictors of seroconversion (unsurprising, given the small sample size), the RRs largely agree with intuition.

- The model comparison exercise (Supplementary file 7) should be described in the Materials and methods section.

- Where are all the parameter estimates for the models shown in Table S3? These need to be given. Or at least for the SEIR+climate vs SEIR+climate+control models (ELISA and MIA variants)?

- All data needs to be released with the paper to allow reproducibility of results (i.e. raw data from serosurvey, surveillance data at the resolution used, climate data)

Reviewer #2:

This manuscript combines a mathematical modeling analysis with two empirical data sources pertaining to the 2013-2015 epidemic of dengue in Fiji. One of the most unique aspects of this work is that the authors had the good fortune of having a number of samples collected for other purposes just prior to the epidemic that could be assayed for prior DENV exposure and used to form a longitudinal cohort that was followed up on after the epidemic in 2015. In many cases, epidemic analyses are limited to passive surveillance data, which is also examined here. Thus, this work represents one of a very limited number of opportunities to perform separate and combined analyses with these two different data types, providing insight into the relative strengths and limitations of the two and providing information about the extent of discrepancy between inferences made on one, the other, or both. Moreover, a number of different forms of analysis were conducted, including a mathematical transmission model that was fitted to both data types.

Overall, I view this manuscript as having many strengths and believe that it reflects a nice combination of unique data and thoughtful analysis. My primary criticisms of the paper have to do with where emphasis is placed in terms of results, writing, and take-home messages. My impression from reading this manuscript is that some of the primary results in the authors' view pertain to what factors drove the epidemic and their conclusion that vector control made a perceptible contribution to ending the epidemic. While I concede that these claims are plausible and perhaps even likely, I had reservations about the extent of inference drawn based on the analyses that were performed. The transmission model used here is a standard choice, but the reality is that models of this form were devised for theoretical purposes rather than inferential ones. That is not to say that models of this form cannot be used for inference – indeed, I am engaged in work of that nature myself – but there is a great deal of uncertainty in many structural aspects of these models that must be acknowledged and examined before reliable inferences can be drawn. My concern is that the authors have not done enough in that respect.

To elaborate, in the Abstract, it is stated that "Mathematical modelling showed that temperature-driven variation in transmission and herd immunity could not fully explain observed dynamics." The authors then go on to state that there was an additional reduction in transmission explained by a vector clean-up campaign. While they may be right, a problem with these statements here and elsewhere in the manuscript is that the one relatively simple model chosen was used to make a rather conclusive statement about what did or did not drive the observed dynamics (e.g., "mathematical modeling" rather than "a mathematical model" showed). I can think of numerous ways in which this model could be elaborated on or alternatives proposed (and not necessarily more mechanistic detail but potentially more flexibility from more statistical descriptions in certain places) that would likely better fit the data and could lead to different conclusions. For example, the model did not allow for a dynamic vector population, which could be a major factor in driving seasonal transmission in its own right but also leads to changes in the demographic composition of the vector population that are extremely important epidemiologically and that interact in important ways with control measures. And while there was some allowance for seasonality, it entered the model in a somewhat odd way (effectively influencing biting rate and vector competence but not EIP, mortality, etc.). Given how quickly a list of potentially major concerns about the model's structure can be generated (not to mention the very particular assumption of sinusoidal seasonality, which there is no good reason in principle to expect as opposed to other seasonal forms), it may be overreaching to make strong claims about ruling out or supporting certain factors in driving the epidemic. The results related directly to the model are suggestive, but that's about it.

Inferences based on the serological data are also not completely straightforward. First, there is the difference between what the IgG and MIA assays tell you about: infection with one's first serotype and infection with a particular serotype. Second, the model does not account for multiple serotypes and is thus presumably intended as a DENV-3 model only. The surveillance data are reflective of all DENV serotypes, however, so some discrepancy between models fitted to these data sources is to be expected based on that alone. Whether in fitting the model or performing the age analysis, a lot of care must be taken when dealing with data that speak to non-specific seroconversion. The reason is that there could have been people experiencing their second infection but who did not seroconvert because they were already seroconverted by the time of the period of observation. The MIA data address this issue to a large extent, but that seems to be done in an either/or way using IgG or MIA but not both sources of information. Additionally, I do not have much familiarity with MIA and would have appreciated more exposition about its validity. For example, how do its abilities to infer serotype-specific exposure compare to PRNT? Could some PRNTs be done on samples from this study to demonstrate that? Are results interpretable for individuals with multiple DENV exposures?
