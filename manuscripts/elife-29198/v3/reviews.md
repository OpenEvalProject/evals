# Peer review - Round 1

Editors:
- Mark Jit, London School of Hygiene & Tropical Medicine, and Public Health England United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29198.019](https://doi.org/10.7554/eLife.29198.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Quantifying the contribution of malaria versus other causes to febrile illness amongst African children" for consideration by eLife. Your article has been favorably evaluated by Prabhat Jha (Senior Editor) and three reviewers, one of whom, Mark Jit, is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Thomas Eisele.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We agree that while the manuscript is not acceptable in its current state, we believe that it has potential and would like to see a version with major revisions.

In particular, the reviewers and I agreed that you took an interesting approach to an important public health question, using a large, rich dataset. However we felt that there were methodological shortcomings in the model (or at least in the current description of it) that needed to be addressed. The main issues that need to be addressed are listed below.

1) Model validation

Although it is mentioned that the fever model has been validated (subsection “Model overview”), it is not clear how this was actually done. Part of the problem is that you have not presented any of the original data on fevers and malaria prevalence. This makes it impossible to tell the goodness of fit.

Given that eLife has no space or figure restrictions, the following data plots would ideally be shown:

- The raw 2x2 table showing all fevers versus RDT positivity (data and predictions), which is really interesting and is key to the message of the paper. This should also be plotted by country and transmission intensity.

- Model-predicted vs. observed all cause fever by pixel or by country. A fairly small subset of the available DHS and MICS surveys are used, presumably because the rest do not have any data on RDT positivity (and/or GPS?). However these other surveys do contain data on all-cause fever and therefore would be an excellent source of validation data for this aspect of the model.

- A plot of the final fitted relationship between fever prevalence, parasite prevalence and the malaria-attributable fraction (and data on the 1st two variables)

- Comparison with observed vs. predicted fever prevalence. These data are not presented, and one of the reviewers who checked could not reconcile some of their predictions with the available data online. E.g. Results subsection “Prevalence of all-cause fever”: fever prevalence in Liberia is quoted as 51.7% in 2014, but on the DHS survey website only a Liberia survey in 2013, which gave fever prevalence as 28.6%. Similarly the most recent data from Niger (DHS 2012) shows a fever prevalence of 14.2%, but the quoted value by the authors is 57.2%. Please could you check and explain the reasons for any discrepancies.

- Related to those countries with the highest and lowest prevalence of fever (subsection “Prevalence of all-cause fever”): predicted values are given for Eritrea, Niger, Botswana and Zimbabwe. But in the supplementary data table (Supplementary file 2), the list of surveys does not include any data from any of these countries. Is this correct, or is the data list incomplete? If correct it seems concerning that the least certain estimates produce the outlying predictions. This should warrant some reinvestigation of the model fit. We suggest at least comparing the predictions against available fever prevalence estimates, even if not coupled with RDT data (as mentioned above).

More generally, external validation should be performed by comparing model results to datasets not used to parameterise it. For instance you mention that case-control studies, transmission models etc. have been used to estimate the attributable fraction of malaria in fever – it would be useful to compare the model results with these studies.

For transparency and to comply with eLife policy for mathematical models, you should provide the initial and final set of model equations (including coefficients) and the code used to select the final model, either in Supplementary Materials or in a suitable online repository such as github. Major data sets used that are not already in the public domain should also be provided unless there are compelling scientific or ethical reasons not to.

2) Extending the model beyond environmental variables

Although in the fifth paragraph of the subsection “Covariates” it mentions that socio-demographic predictors of fever were considered, all the examples in the paragraph and in Supplementary file 3 are environmental. This seems like quite a large omission, especially given that fever is self-reported. As well as many varied causes of fever, cultural perceptions of fever are important here (and language, e.g. some languages do not have a specific word for fever). We were not clear how well environmental variables could be expected to predict this, especially given that you are extending fever predictions into countries for which there are no data.

Besides cultural factors, a list of suitable covariates may include socioeconomic factors such as nutrition, crowding, mother's education, access to clean water etc. Many of these are available in DHS/MICS data but it is difficult to see how they were used. Indeed, given that the final model contained 167 predictor variables, it is difficult to see why there was any human selection at all. The authors have not tried to justify any of their chosen variables based on causality arguments, so would it not make more sense to use the entire DHS dataset as predictors, and then let variable selection algorithms winnow this down?

We are also concerned about the apparent lack of variables at the household or even individual level. This may be a problem if being malaria-positive is (positively or negatively) associated with having a fever beyond what can be explained by the spatial covariates examined. For instance, within a particular town or village (with homogeneous environmental variables) there will be poorer households who are more likely to be both malaria-positive and to have non-malaria fevers. Within the household there will be further associations in distribution due to the age, gender, birth order, genetic makeup etc. of individuals. Perhaps this has been taken into account, but it is not clear how this happened.

In general, we get the impression that the ecology of the pathogen, its environment and insect host is well-described, but the epidemiological, immunological, cultural and socioeconomic determinants of disease within the human host are either less well captured or at least less well explained. Perhaps you should include someone with clinical or at least public health training in your authorship list.

3) Scope

There are a number of areas where we believe that the scope and implications of the results may be overstated.

- You need to clarify that this study aims at improving burden estimates of uncomplicated malaria, and not case management policy. WHO clearly recommends, as do all national policies in African countries with endemic malaria, that all fevers/suspected malaria presenting at facilitates in malaria endemic areas should receive a laboratory diagnosis for malaria, and if positive treated with the first-line antimalarial. This doesn't mean the attending health professional cannot go on to treat other presenting illnesses and symptoms. But even if the fever is not directly attributable to the Pf infection at that time, it should be treated. This needs to be made clear in the paper. You should stick to how these findings impact the overall epidemiology of fever illness among children in Africa, and not make recommendations or draw conclusions from this study in the discussion for malaria case management (or IMCI) policy.

- You argue that the results of their work will improve burden estimates. We find this to be somewhat of a 'straw man' attack, as to our knowledge no burden estimates have been based on an RDT positive child with a history of fever in the past 2 weeks. Neither WHO GMP, MAP nor GBD uses such a method.

- You present cross-sectional household survey data that measures a 2-week (or there about) RDT period prevalence based on persisting HRP2 antigenemia from a Pf infection, plus an overlapping fever history based on the recall by the mother/caregiver. Their primary results suggest a large proportion of these fevers are not directly attributed to the underlying Pf infection. While this seems an appropriate interpretation of the results and in line with malaria epidemiology, the cross-sectional nature of the study is a major limitation. You need to make note that the underlying Pf infection likely would have resulted in at least 1 parasite-attributable fever, likely in the first month of the infection, and additional parasite-related fevers will likely occur, especially if a new infection occurs on top of the existing infection (just based on the malaria therapy data). So the timing of the observed RDT+ and fever is important in understanding the true relationship between the underlying Pf infection, the observed fever recall, and the relationship between the underlying infection and fever at that time. Results and Discussion should take this into consideration when interpreting results throughout the paper.
