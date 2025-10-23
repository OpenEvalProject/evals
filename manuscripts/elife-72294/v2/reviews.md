# Peer review - Round 1

Editors:
- Joshua T Schiffer, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72294.sa1](https://doi.org/10.7554/eLife.72294.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "External Validation of a Mobile Clinical Decision Support System for Diarrhea Etiology Prediction in Children: A Multicenter Study in Bangladesh and Mali" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Serwadda as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sanjat Kanjilal (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please address the relative lack of seasonality in the data used for model validation in both cohorts.

2) Please discuss how operational components may impact the performance characteristics of the decision making tools.

3) Please discuss how frequently which the mode missed bacterial or protozoal infections.

4) Please limit jargon and provide definitions for all terms listed by Reviewer 2. The mechanistic and statistical explanations for α and β in the methods are also insufficient to interpret the results, particularly for the generalist reader. Please provide a lengthier and clearer explanation of the calibration procedure.

5) Please discuss the potential impact of the rotavirus vaccine on observed study outcomes.

Reviewer #1:

Garbern and Nelson et al., performed an external validation of clinical decision support system (CDSS) for prediction of a viral etiology for kids presenting with diarrhea in low and middle income countries, that is deployable on a mobile app. The prediction model is derived from data accrued in the Global Enteric Multicenter Study (GEMS), which completed in 2011 and defined etiologies and factors associated with pediatric diarrhea across 7 countries. The original GEMS samples were re-analyzed by a different group of investigators using a multiplex gastroenteritis syndromic panel to establish the 'ground truth' data upon which a random forest model was trained (Liu, Lancet, 2016). A simpler 5 feature logistic regression model was chosen using the variable weights assigned by the random forest and included only factors that would be obtainable by practitioners in real time. The final model utilized patient-intrinsic features as well as a viral seasonality model that they combined into a single prediction using a pre-determined cutoff (attributable fraction > 0.5) validated in previous work and by expert opinion. The study had a 'lead in' period where adjustments were made to the CDSS to adjust for real-world deployment and then they collected data from 2 referral centers, the first in Dhaka, Bangladesh and the second in Bamako, Mali.

The results of this external validation study show that model performance dropped relative to the internal validation (AUC 0.83) at both sites and were just at the arbitrary AUC cutoff of 0.75 for acceptable model accuracy, though with suboptimal calibration.

Strengths

Most antibiotic use in the setting of pediatric gastroenteritis is unnecessary. The impact of the CDSS for management of pediatric diarrhea in the literature appears mixed, with some studies showing increased antibiotic use and others showing decreased. This highlights the critical need for a rigorous prospective multicenter RCT to evaluate the utility of a point of care CDSS for optimal decision making around pediatric gastroenteritis. The results of the current study are an important stepping stone to that objective. The establishment of ground truth using a multiplex PCR assay provides for a more sensitive and (possibly) more specific reference by which to compare model outputs relative to traditional culture, EIA and uniplex PCR methods used in GEMS. Additionally, the use of a mobile app with a simple UI maximizes the number of staff members that will be able to utilize the CDSS. Finally, the use of an interpretable model that incorporates local data is an excellent design choice for improving trust and uptake.

Weaknesses

It is not entirely clear that the data support the claim that the model passed external validation. While the point estimate for the overall model was just above the AUC cutoff of 0.75, the 95% CIs were (0.67 – 0.84). Furthermore, most of the site specific models has an AUC estimate below 0.75 and this was consistent across various model sets. It is important to note that being below an arbitrary AUC cutoff of 0.75 does not necessarily indicate the model will not perform well in practice.

The operational component is important when interpreting results of CDSS validation studies. In this study the key personnel were general practice nurses / study nurses who enrolled no more than 8 children per day and had no other responsibilities. In actual deployment, one could imagine staff members would likely have other duties in addition to managing kids presenting with acute diarrhea and would need to triage more than 8 per day, depending on the season. This may lead to over-estimation of the CDSS's utility in higher volume / higher acuity settings, perhaps due to entry error or time constraints. The results of the ongoing RCT evaluating this platform will be critical for assessing real-world utility.

From what I could tell, models features are parameterized on a cloud based server and variable weights are then downloaded on to the mobile phone app. I understand the CDSS recommendations were not reported to treating clinicians but were they generated in real time (ie as soon as the staff entered the data)?. How long did it take for results to appear? Would consider describing this a little more clearly. I'm also curious to know how often the model was re-trained on the server (if at all)? Not critical to overall hypothesis but important to think about when trying to develop the infrastructure to deploy this approach in other settings.

Were the study nurses who entered data into the app the same ones who entered the data into the CRF? If so, may be hard to differentiate the App's ease of use and accuracy since there will be correlation in symptom documentation.

The change in the design of the application halfway through the first phase in Bangladesh means that data accrued prior to the change are not relevant to the evaluation of the CDSS' external validity or generalizability. I would consider dropping the '(no date restriction)' analyses from the results.

Unclear what is being referred to with regards to "these independent models" (line 337 – 338). Also, from what I could tell, the prediction model combines 3 separate prediction models in a Bayesian analysis. Why could all features not be included in a single Bayesian model? This is not my area of expertise, but I did not understand the rationale here.

There was significant heterogeneity between the sites in terms of the percentage without a viral etiology and the distribution of organisms. As noted in the limitations section, this may be partially explained by differences in rotavirus seasonality. However, model accuracy seemed paradoxically better in Mali where almost 50% of children did not have an etiology determined. Is this presumably due to better discrimination in cases where bacterial infection is more likely? On a more general note, a deeper (or more explicit) discussion of the factors that could explain the drop in AUC between the internal and external validation studies would be helpful.

Different model sets performed best at the different sites. Might this suggest utility in incorporating a trial period to establish which model has the best performance for a given locale? Might be a better approach than using a single model architecture globally.

Table 4: Should the first row be called 'Patient-Intrinsic Only' to be consistent with Table 3? Also as noted above, would consider dropping the 'no date restriction' results.

Line 490: Probably semantics but the actual model being deployed is a 5 feature logistic regression which was derived from a random forest built on a small but highly curated dataset. This isn't typically what most people think of as machine learning, though technically both fit under the definition.

The time frame for the study is 2 months at each site, ie within one season. It would be helpful to see how well the validation performs across multiple seasons but understand completely the disruptions brought on by the COVID-19 pandemic.

Reviewer #2:

A potentially interesting study of 199/302 children <5yo with etiologically defined acute (ie 1-7d) diarrhea in November-December 2019 in Bangladesh and in January-February,2020 in Mali, of whom 22% in Mali and 63% in Bangladesh had only viral etiologies identified, and who could reasonably accurately be predicted to have viral-only diarrhea, using a mobile App. The vast majority of viral etiologies were rotaviral (90/94 in Bangladesh; 24/33 in Mali). However, several concerns and comments include:

1. The ill-explained jargon throughout makes the paper difficult to follow. For example, clearer explanations are especially needed for the "patient intrinsic,"historical patient," recent patient and even viral seasonality and climate models used. Another example is "pre-test odds model" and "viral seasonality model" mentioned in the abstract as their major conclusion without any explanation. So what, then is the take-away message or importance of that (especially given several major limitations noted below)?

2. A glaring gap is the lack of any comment about rotavirus vaccine impact in these populations and for any relevant generalizations made.

3. Were the 73 patients with 'overcalling' of vomiting excluded from all analyses, as this certainly skews any prediction models?

4. It is difficult to believe that there were no norovirus infections in this season in Bangladesh, can this be at least commented upon?

5. The major limitation of only 2 month study periods at each site for highly seasonal pathogen incidences needs comment and explanation.

6. What were the frequencies of antimicrobial use in these study children?

7. The converse hypothesis of potentially treatable bacterial infections (with a single dose of azithromycin for example) or even protozoa such as Giardia, should be examined and mentioned. For example, how many patients were misidentified as 'viral' when they had bacterial or protozoal infections?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "External Validation of a Mobile Clinical Decision Support System for Diarrhea Etiology Prediction in Children: A Multicenter Study in Bangladesh and Mali" for further consideration by eLife. Your revised article has been evaluated by David Serwadda (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) The new Figure 3 could be more clearly presented with a) larger font, b) better labeling (unclear if viral seasonality is seasonality alone or present patient + viral seasonality as in the legend as in the table: I would suggest including all 3), c) inclusion of proportions rather than absolute numbers in the table

2) I am not sure that the App accurately identified viral-only etiology for diarrhea as stated in the abstract. It misclassifies a decent number of cases. To this end, a paragraph is needed in the discussion to impart whether the tool is in fact sufficient for clinical use. I would argue that it is not, based on a relatively low AUC (reasonably high numbers of false negatives and positives). I would suggest that the authors speculate on what additional features could raise the AUC to a level sufficient for use by the bedside.
