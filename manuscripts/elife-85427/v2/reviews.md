# Peer review - Round 1

Editors:
- Peter Rodgers, https://ror.org/04rjz5883 eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85427.sa1](https://doi.org/10.7554/eLife.85427.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Meta-research: The effect of the COVID-19 pandemic on the gender gap in research productivity within academia" to eLife for consideration as a Feature Article. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a member of the eLife Features Team (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Emil Bargmann Madsen.

The reviewers and editors have discussed the reviews and we have drafted this decision letter to help you prepare a revised submission. The points that need to be addressed in a revised version are listed below. As you will see, there are quite a few points that need to be addressed.

Summary

This study provides fundamental evidence substantially advancing our understanding of the gender-specific impacts of the Covid-19 pandemic on academic research productivity. However, there are a number of concerns that need to be addressed.

Essential revisions

1) I am concerned about the use of the included studies for a formal meta-analysis. Firstly, it is clear from the authors well-structured description in the methods section that many studies are not measuring the same outcome.

Many studies use number of submitted or published articles, which may be a fairly comparable metric, but many of the survey studies use very different measures of productivity:

a. Research time (N = 4), job-loss (N = 1), burnout (N = 1), and number of projects (N = 1).

b. These are highly different outcomes, and should not be analysed as comparable.

2) Secondly, it is not clear how the studies differ in their use of the pandemic as an "intervention".

a. Some studies will ask respondents to compare their productivity before and after, while some studies will provide actual comparisons of productivity before and after. Both methods will have their share of drawbacks, but I do not think they are comparable.

b. The different survey studies will also have been fielded at different times, making the "intervention" (the pandemic) very different. Perhaps the loss of research time is most acute in the beginning, before academics have had time to adapt? Or later, because of burn-out?

3) Thirdly, the diversity of research design and modelling techniques makes it hard to conduct formal comparisons of effect estimates.

None of the included studies are randomised controlled experiments. In fact, the research design (and modelling techniques) differs immensely across included studies. Therefore:

a. We do not know to what degree individual, and thus by extension, individual gender gap estimates can be causally interpreted. This should be more explicitly acknowledged in the article.

b. Different estimates may be relatively closer to a causal effect, depending on the research design. By treating all designs equally, the authors gloss over these crucial differences in what we can gleam from each study.

c. It is not clear what "estimand" we get from the meta-analytical model. Some studies are cross-sectional, and will give us the average between-subject difference in productivity. Other studies, longitudinal ones, may give us the "difference in differences", i.e. the average difference in within-subject publication productivity trend. These are fundamentally two different answers to the question: Has the pandemic exacerbated the gender gap in research?

d. The guidance from e.g. Cochrane is to use a random effects model to account for variation in what effect is estimated. The authors seem to use a random effects model to account for dependency between effects extracted, but I think they should also be more explicit in leveraging this for accounting for variation in what effect is estimated.

e. Each included paper will have different modelling strategies. E.g. the Myers et al. 2020 paper uses regularised regression (Lasso), while the Andersen et al. (2020) used a hierarchical logit model. These differences may contribute to differences in estimated gender gaps in ways we don't know or lead to overfitting.

When 49 % of variation is explained, simply, by the data employed (survey, publication, or submission, see p. 5 of manuscript), it makes me wonder how much is simply explained by differences in research design or modeling strategy.

4) Another concern is the conclusions drawn from the differences in meta-analytic effect drawn from figure 2. To me, the arguments of survey estimates being more "true" to the actual effect, because they are closer to the real-time events (p. 17) could easily be turned on its head.

Those estimates are also self-reported, and only a snapshot at one point.

a. People are bad at judging changes.

b. Productivity may have been severely hampered early on, when surveys were fielded, and then normalised over time.

c. Survey estimates are around 4.2 and 4.9 times larger than estimates from publication data (0.193/0.046) and submission data (0.193/0.039) (p. 7), but also has the smallest sample sizes (I think from looking at 1/SE in figure 2). Couldn't this easily be an effect of higher degrees of noise and lower power in this data?

d. Often, large-scale international surveys of researcher suffer from very low response rates and often mostly cover few countries (North American and Western Europe). At best, it makes it hard to generalise beyond these areas, and at worst this bias the results.

I appreciate a discussion of why survey estimates differ so much from publication- or submission-based studies, but this discussion is currently one-sided. The authors should consider if perhaps survey data suffers from other problems that could inflate estimates.

5) The authors seem to conflate gender inequality with gender bias throughout the paper (e.g. on line 55 or 281). In science studies, one would often denote a difference in outcome as a bias only if there is a provable mechanism of discrimination or differential treatment of women in e.g. journal accept rates, grant funding, etc. Instead, an indirect or structural difference could be a disparity or inequality brought on by other factors (e.g. women being disproportionally allotted more teaching load, domestic work, not being promoted to equal degree, etc.).

a. There is a great working paper by Traag and Waltman with a discussion of these, and I suggest the authors use some of their clarification (doi.org/10.48550/arXiv.2207.13665).

b. I think this is important, not because I want to downplay potential bias, but because it matters for possible interventions. What we should do to ameliorate unfair differential productivity differs according to the causal mechanism at work.

6) How was "before " and "during" pandemic defined? – this is not specified in the inclusion criteria, nor in how the data was extracted.

Lines 456-457: unclear how you define "before the pandemic" and form where you get the data on the numbers. E.g., my first impression was that you analysed yourself all publications for a given discipline as your baseline. Please clarify.

7) Screening

– Study screening section: the inclusion criteria are too vague to be reproducible. It is also incomplete. Was publication status used to exclude evidence? How about publication language and full text availability? Was there a limitation on the geographical scope or targeted career stages for the included studies and was this information coded in any way?

– Line 360: why not all articles were double-screened to avoid errors? It would not add much work.

– Line 368 and 382: no details provided how full-text articles were screened, e.g., in terms of the used software, also it is not specified if they were double-screened.

– Table 1 header: first and only mention that articles were screened from 2020 only – this is a first mention on having such a limit on publication searches – this should be in the search strategy description.

– The authors should describe whether some quality weighting was used or quality assessment played a part in the inclusion criteria.

8) Data and meta-data

– Extracting variables section: please refer the reader to a proper meta-data SI file describing in detail all extracted variables, at a level that enables replication of the data extraction and fully informed data reuse (the "meta-data" file archived on Zenodo does not provide such information in sufficient detail and some of the variables in the provided raw data file are quite cryptic).

– A data file is needed including a list of articles at the full-text screening stage, with individual reasons for exclusion.

– A meta-data file is needed describing in detail all extracted variables, at a level that enables replication of the data extraction and fully informed data reuse (the "meta-data" file archived on Zenodo does not provide such information in sufficient detail and some of the variables in the provided raw data file are quite cryptic).

9) Lines 324-327: Only 17 out of 21 eligible articles were included in the extracted data set – what happened with the remaining 4? Why were they not included in the dataset? From the data files available on Zenodo I can see these were not published as journals articles, however inclusion criteria do not state that only grey literature should be excluded.

10) Line 339-352: The search string used had only 14/17 sensitivity (82%). However, the next step of search strategy refined did not improve the sensitivity and just removed some of the irrelevant studies to reduce the screening effort.

Given the limited sample size, and limited scope of the searches, it is of concern that a significant proportion of potentially available evidence has been missed (at least 20%). The main reason for using "test set" (benchmarking) articles is to improve search sensitivity, with search precision being less important. Since it is hard to get 100% sensitivity in database searches, additional search strategies should be used to locate potentially missed articles, for example by collecting and screening articles that were cited by or cited already included articles (after the main database searching and screening is completed). Also, grey literature should have been searched.

11) Lines 350-251: the recommended 10% hit rate should be calculated from pilot screening round not from how many "test set" articles have been captured by the search string.

12) Lines 411-413: regression models per se are not effect sizes, please specify which estimates from these models were used as effect sizes and how they were combined with other effect sizes.

13) Analyses section: no description of any sensitivity analyses (e.g., doing analyses leaving out outliers or leaving-one-study-out approach).

14) Limitations section: there are many potential limitations of this study that are not mentioned here. For example, limitations of the search conducted to find the evidence – not searching grey literature, no other additional searches, not searching in languages other than English. This potentially resulted in biased evidence as well as limited the sample size. Also, some statistical analyses are less reliable due to small numbers of effect sizes within some of the levels of categorical variables tested.

15) Table S4 item 20d: Figures 2, 3, 5 show meta-regression results testing secondary hypotheses. Those are not sensitivity analyses.
