# Peer review - Round 1

Editors:
- Talía Malagón, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70970.sa0](https://doi.org/10.7554/eLife.70970.sa0)

This large multicenter study tracked the clinical journeys of COVID-19 hospitalized patients over 2020, and found variations in clinical outcomes over time. This paper will be of interest to the large class of clinicians, public health workers and health policy makers who want to know the variation in the nature and duration of the care provided to hospitalised patients during an infectious disease epidemic. The study highlights the importance of maintaining the capacity of registration of infectious disease like COVID-19, during a pandemic and after. While the cohort recruited patients from multiple countries, the vast majority of patients came from the UK, so the results are most applicable to this country.


---

# Peer review - Round 1

Editors:
- Talía Malagón, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70970.sa1](https://doi.org/10.7554/eLife.70970.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Ten months of temporal variation in the clinical journey of hospitalised patients with COVID-19: an observational cohort" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Provide further rationale for the separation of gastrointestinal and common symptoms for analyses.

2. There are several indications that the cohort may not be entirely representative of all hospitalised patients with COVID-19 in the study settings, including a surprisingly high case fatality rate and few participants recruited at some study sites. Please provide more discussion regarding the representativeness of the cohort, eligibility criteria, and study participation rates.

3. Please provide date of end of follow-up and an estimate of the average/total follow-up time.

4. Indicate whether all participants were followed-up over equivalent periods of time to assess study outcomes, in order to justify the use of logistic regression rather than survival analysis.

5. Provide more information regarding what variables are being included in the model, and whether Table 4 represents results from a model including all variables or multiple separate models. This influences how readers interpret the variable coefficients, as it is important to know what variables have been adjusted for and whether the ratios should be interpreted as crude or adjusted associations, and whether interactions are being accounted for in the estimated effects.

6. While less essential, the reviewers made several other suggestions/queries that should be considered by the authors in their revision.

Reviewer #1:

In this study, COVID-19 hospitalized patient trajectories were tracked over 2020 in order to assess whether patient outcomes changed over time. The study of these time trends can be useful for assessing how health systems respond to pandemics, and may help in better planning for future outbreaks and pandemics.

Some of the major strengths of this study include its very large sample size, which allowed a detailed examination of clinical pathways of patients, and the ability to demonstrate clear time trends by age group, as well as interesting interactions between age and ICU admission on the risk of death. The study was able to look at multiple outcomes of interest, including death, discharge, ICU admission, and time to these events. Detailed analyses are provided in either the main text or the appendix.

As the authors point out, it is likely that temporal changes in patient outcomes were influenced not only by changes in clinical management and treatments over the course of the pandemic, but potentially by surges in the numbers of admissions which may have taxed the system capacity and quality of care at specific points in time. The authors rightly point out that system capacity should be adequately controlled for when assessing the effects of interventions against COVID-19. However, in their own analysis they do not control for any variable that would be an indicator of system capacity, and do not provide any suggestions for how other studies could control for this. Therefore, the analysis in this study by itself does not demonstrate that system capacity had an impact on patient outcomes. The reasons underlying the time trends they observe therefore remain unclear.

While the cohort recruited patients from multiple countries, the vast majority (83%) of patients came from the UK. It is therefore likely that most time trends reflect the evolution of the pandemic and health-seeking patterns in the UK. It is not clear to what extent the time trends are generalizable to other countries who may have had epidemic peaks at different times and that may have different holidays (which are deeply influential on infection patterns and health-seeking behaviors).

It is unclear to what extent selection bias may have influenced the results and observed time trends. In terms of selection into the cohort, there is not much information on how study sites were selected, when they started contributing cases to the cohort, if there were any additional selection criteria applied to participants beyond being a confirmed or suspected COVID-19 case, and what proportion of theoretically eligible participants were recruited into the study. The low number of participants recruited at some study sites suggests that the recruited participants only represent a fraction of all potentially eligible COVID-19 patients at each study site. This may have led to a selection bias if those who were not recruited differed in some systematic way from those included. If recruitment probability varied over time, then this might have also influenced the time trends observed. In terms of selection out of the cohort, there is little information on how many patients were lost to follow-up, had missing outcome data, or were transferred to other facilities. It is possible these patients may have systematic differences from those with complete data, which may lead to selection bias.

Comments for the authors:

1. Please provide date of end of follow-up and an estimate of the average/total follow-up time (STROBE item 14C).

2. Please provide more information regarding participant recruitment, such as numbers potentially eligible and recruited into the study (STROBE item 5,6,13). Were all eligible COVID-19 cases included, or were only some included? Are there more eligibility criteria than those mentioned? The discussion suggests it is the latter (which the authors refer to as "enrolment bias", would recommend rephrasing this as selection bias). If site case loads influenced recruitment then this could potentially lead to selection bias if certain types of patients are favored for study inclusion and this varies over time.

3. Please report in the main text the number (%) of patients lost to follow-up or with missing data for each analysis (STROBE item 13,14).

4. It is unusual to have an outcome of odds or probability of an event where the time frame over which the patient can experience the outcome is not specified. Presumably the outcomes for question 2 and 4 are ICU admission or death over the entire study period. This is not a fair comparison, because patients recruited in later months may not have been followed-up as long as patients recruited earlier, and the follow-up of patients may have varied over the duration of the study. It is generally more rigorous to specify a time frame over which the outcome is assessed and only analyze patients with that follow-up time (ex. death within 3 months of admission) or to use analysis methods which account for differential follow-up time of participants, such as Kaplan-Meier or survival analyses. I would suggest modifying the logistic regressions to have the outcome over a specified time frame or to use survival analyses instead (or to explain why these methods were not used).

5. P39: "Patients lost to follow-up before any of these outcomes were included unless the time to that event was the outcome of interest" It is unclear to me what this means. Does this mean that patients lost to follow-up are included as non-events in the denominator?? It seems to me a better way to treat these patients would be to exclude them or better yet to include them as right-censored observations in survival analyses, as suggested above.

6. Table 4:

– There is an excessive number of decimal places in this table (pseudo-precision) that are not clinically meaningful. I would suggest rounding all values to the nearest decimal (odds ratios) or to the nearest percentage point (percentages). Reducing the number of decimal points will make this table much simpler to read and understandable.

– Please consider dropping the p-values for each individual value. The confidence intervals are much more informative as they indicate the precision around each estimate, convey the same information, and put the emphasis on the estimation of the parameter rather than its statistical significance. The small p-values in most cases are a reflection of the large sample size.

– Conversely, the addition of p-values for the Wald type III test for the overall effect of each variable to the table would be informative.

– The above suggestions (decreasing decimal places and dropping p-values) should create more space in the table. Please consider using this space to add descriptive data on the probability of experiencing death and the number days to death or discharge for each category. This descriptive information helps to contextualize the odds ratios and relative time increases, and may be more clinically useful for some readers than the ratio measures.

– It is not clear whether the results from this table present univariate or multivariable regression model results (presumably the latter). If the analyses are multivariable, then all the variables that were included in the model should be described in a footnote, as this influences the interpretation of the results. For example, it is important to know whether the monthly estimates are adjusted for sex and age, as the age and sex of patients varied over time.

– The pregnancy variable is conflated with the effect of sex because presumably all the men where categorized as 0 for this variable. This variable should be treated as an interaction variable with sex (sex + sex*pregnancy) in order to separate the effect of sex from the effect of pregnancy.

7. There is no Table 3.

8. The authors mention system capacity during epidemic surges as a potential contributor to time trends, but did not include any indicator of system capacity in their analysis, so this interpretation remains speculative. Have the authors considered included such indicators as a variable in their multivariable model (ex. number of COVID-19 infections or hospitalizations reported during the day/week of admission in each country)?

Reviewer #2:

This paper reports here the multi-national collaborative effort on establishment of cohort of 142,540 patients hospitalised with COVID-19. The authors confirmed the previous findings of the trend of hospitalization, ICU admission and case fatality ratio. The author not only shared the large cohort data, including UK and other countries, they also did Multivariable logistic or linear regression to investigate factors associated with the main outcomes, including time from symptom onset to hospital admission, probability of ICU/HDU admission, time from hospital admission to ICU/HDU admission, case fatality ratio (CFR) and total length of hospital stay.

Strengths:

This is a large database from ISARIC Clinical Characterisation Group. Based on the large data, the author answered six important questions, especially time to hospital admission, ICU admission, length of stay and case fatality ratio. The findings are valuable, such as health systems may at times be overwhelmed; system capacity may be an important predictor of patient outcome and may supersede other factors such as increasing case management skills and the influence of new therapies.

Weaknesses:

Although the paper does have strengths in principle, the weaknesses of the paper are that these strengths are not directly demonstrated. In particular:

1. In this study, why gastrointestinal symptoms (abdominal pain, diarrhoea, and vomiting) are emphasized?

2. In this study, patients with a recorded hospital admission date before their symptom onset date, were taken to be a nosocomial infection. But patients who had got infection after exposure to virus may present symptoms later after admission. That is ,on the day of admission, the patient may be in the incubation period.

3. Similarly, "patients with nosocomial infections had lower odds of being admitted to ICU/HDU (OR 0.68, 95% CI 0.62-255 0.74)". The underlying reason may be not nosocomial infection, but that these patients had been admitted earlier than those with adverse outcomes.

4. Line 205: "times" should be "time". Similarly, in the lines 209 and 218.

5. For admission to ICU as an example, the comparison between different months means little, as there are many confounding factors for admission to ICU. One and half years have passed, it is time to look forward to improve treatment.

6. Why less elderly patients were admitted to ICU?

7. Why a wide variety of serious or chronic medical conditions were associated with lower odds of ICU admission. Is it because of lower admission of elderly patients?

8. The raw case fatality rate (CFR) was extremely high in this paper. The readers would be interested in the representativeness of this cohort.

9. In this study, the authors confirmed what is known that Age, male and comorbidities are risk for higher mortality. The readers would like to understand why asthma was associated with lower mortality.

10. Discussion: "patients admitted after experiencing symptoms for longer than 1 week were less likely to die." I am afraid that the explanation lacks scientific evidence.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Ten months of temporal variation in the clinical journey of hospitalised patients with COVID-19: an observational cohort" for further consideration by eLife. Your revised article has been evaluated by Miles Davenport as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The authors mention that the time periods over which the probability of ICU admission and death/discharge were measured are implicit in the cutoff times for time to event analyses (13 days and 45 days). This should be made explicit in the manuscript by indicating that the outcomes were ICU admission within 13 days for question 2 and death/discharge within 45 days for question 4.

2. While the authors specify that all analyses are multivariable in the text, this should also be mentioned in the table legends and/or footnotes in order for tables to be self-sufficient.

3. Table 1: because 'nosocomial infection' is no longer defined in the methods, this row should be relabeled as post-admission symptom onset infections

4. There is an error in Table 2, the rows for symptoms at admission are mistakenly labeled as comorbidities and vice-versa.

5. The authors refer to an non-existent supplementary figure 2 in the results. Presumably they mean Figure 2. This should be fixed.

6. Figure 4 is missing a C inset.

7. On line 446 the authors refer to Figure 3 when they should be referring to Figure 4.

8. Table 3 appears to be lacking the standard deviation for time from symptom onset to hospital admission.
