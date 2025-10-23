# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66169.sa0](https://doi.org/10.7554/eLife.66169.sa0)

The authors present an investigation into the role of threat learning processes in symptoms of anxiety across a broad sample of subjects with and without clinical anxiety, across multiple age groups. Authors demonstrated weaker safety learning in those who were more anxious.


---

# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66169.sa1](https://doi.org/10.7554/eLife.66169.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Computational Modeling of Threat Learning Reveals Links with Anxiety and Neuroanatomy" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Michael Frank (Senior Editor).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

The authors present an investigation into the role of threat learning processes in symptoms of anxiety across a broad sample of subjects with and without clinical anxiety, across multiple age groups. The study uses a simple fear conditioning paradigm in which subjects first undergo an acquisition procedure to learn associations between visual CSs and loud noise USs, before undergoing an extinction procedure where the CS+ is presented without the US. Reinforcement learning models are fit to skin conductance responses, and parameters from these models are used to predict symptoms of anxiety. This demonstrated weaker safety learning (i.e. learning that the CS– did not predict threat) in those who were more anxious, and slower extinction in more anxious individuals, a result that was moderated by gray matter volume in a number of subcortical brain regions.

The reviewers expressed enthusiasm for the manuscript:

– This is an important area, and the results will be of interest to readers across the field of computational psychiatry, and mental health research more widely.

– This work has the potential to be an important study in the field of computational psychiatry. Investigations of threat learning processes in individuals with clinical anxiety are lacking, despite their clear relevance as a mechanism underlying symptoms of these disorders.

– [noted by all reviewers] The sample is large and includes subjects with clinically significant levels of anxiety who were not receiving medication.

– The modelling approach is carefully considered, and the authors have clearly been thorough in testing different model variants.

– The inclusion of brain volume data provides some interesting insights into how gray matter volume relates to these core learning processes.

– The authors explain the added value brought by the computational modelling approach well, and it clearly provides some interesting insights into the role of threat learning that would not be seen in more traditional analyses (e.g. prior work by this team).

– All published work on computational models of threat learning in SCR used comparably smaller samples with more limited age range (Li et al. 2011, Zhang et al. 2016, Tzovara et al. 2018, Homan et al. 2019). Hence, this is an important data set that could offer substantial insights into threat learning.

– This paper is of potential interest to researchers within the fields of clinical psychology, clinical neuroscience and computational psychiatry.

– Over recent years, both the use of dimensional measures of symptoms and adoption of computational modelling has advanced our understanding of psychopathology–related differences in cognitive and brain function. This has encompassed both original empirical studies and application of computational modelling to previously published datasets. Both these approaches have potential value and different advantages and disadvantages. The current study is an example of the latter approach.

– The consideration of nine alternate models in the modelling of SCR responses to the CS+ during acquisition is a strength of the paper.

– The application of computational modelling techniques to such a large differential fear conditioning dataset, with data from both healthy adult and child participants and unmedicated patients seeking treatment for anxiety is highly appealing.

Nevertheless, all 3 reviewers expressed some significant concerns, mostly centered on the analytic framework and other aspects of the approach. There was a consensus among us that the necessary revisions will entail considerable effort on the part of the authors.

– Modeling Approach

Concern: The modelling approach could be validated more robustly. For example, model and parameter recovery analyses are not presented, and so it is unclear how much confidence can be placed in the winning model and the parameter values derived from this model.

Recommendation: Include a more thorough validation of the modelling approach, adding model recovery and parameter recovery analyses. This would provide confidence in the conclusions drawn from the modelling by demonstrating that it is possible to recover the winning model and its parameters accurately.

Recommendation: It would be helpful to also show the BICs for different models to give the reader a clearer idea of how model fit differed across the different models.

Recommendation: It would be helpful if the authors could conduct Bayesian model comparison (see Stephan et al., Neuroimage, 2009) and report the population–level estimate of the proportion of participants best fit by each model. Given the age by anxiety analyses, it would also be helpful if they could report the best–fitting model for high and low anxious children (as assessed using the SCARED) and high and low anxious adults (as assessed using the STAI). Does the same model 'win' for both child and adult participants divided into low and high anxious subgroups?

Concern: Description of model estimation and comparison lacks detail. Model parameters are fit with fminsearch (using which starting values? random? grid search? just one starting value would hardly be sufficient. any parameter constraints?) using OLS minimisation. How is BIC then computed? How are the models compared – the methods mention "per participant and across the sample"; do you assume a fixed or random model structure? What is the purpose of a t–test (p. 13) in the model comparison?

Recommendation: Provide modeling details.

Concern: The model space of the acquisition session does not include any of the "best" threat learning models from previously published work (see below for some specific examples). This precludes a direct comparison; more importantly it may also miss out on the best model in this sample. First, previous work has simultaneously modelled CS– and CS+ responses. This is appropriate (for all sessions), since a priori the agent does not know which is the "safety" cue, and will presumably use the same mechanisms to update value for both cues. The authors state that standard models cannot account for the large increase from first CS– trial (before first reinforced CS+) to next trial; while this is correct, the authors have a model to account for that, and more trivially one may just leave out the first CS– response. Secondly, the observation function (which is only specified in the legend of table 1 – this should appear in the text) maps SCR onto the value terms of all models. All previous SCR modelling work has found SCR is more closely related to associability or uncertainty, or a mixture of these with value.

Concern: The models considered are broadly suitable but comparison of model fit across both SCRs to the CS+ and CS– during acquisition and SCRs to the CS+ and CS– in extinction is missing, which is a limitation.

Recommendation: Include prior models in the model space. Models should simultaneously include CS+ and CS– responses. To this end, they may leave out responses before the first reinforced CS+ trial. Model space should include additional variants of models 9 that account for a mapping onto associability (as in Li et al. 2011, Zhang et al. 2016) or combined associability and value (as in Homan et al. 2019) and a variant of model 3 that accounts for a mixture of uncertainty and value (as in Tzovara et al. 2018).

Related Concern from Another Reviewer: The authors do not consider alternate models for the SCRs to the CS– during acquisition or for the SCRs to the CS+ during extinction and they do not model the SCRs to the CS– during extinction at all.

Recommendations: It would be helpful to know which model best fits all the acquisition data (to both the CS+ and CS–). Does the hybrid model still perform less well than the non–hybrid models? And does model 8 still outperform model 7? (in models 8 and 9, as in model 7, the CS– value could also be modelled as updating after each UCS delivery with model 8 now having 6 free parameters and model 9 4 free parameters.) Similarly, it would be useful to have both CS– and CS+ trials during extinction modelled. Given the raw data indicates the response to both the CS+ and CS– drop off during extinction, understanding if decreased responding to the CS+ during extinction represents active specific updating of the CS+ UCS contingency or a non–specific decreases in expectancy of the UCS after both the CS+ and CS– is clearly important.

– Multiple Comparisons [Multiple Reviewers]

Concern – There are many post–hoc tests on association of model parameters with brain results and participant traits. It is unclear how this was planned and performed – how did the authors correct for multiple comparison across parameters, traits, and experiment phases?

Recommendation: provide appropriate, principled correction for multiple comparisons to mitigate familywise α inflation

Recommendation: Please state how many tests were conducted and what correction was applied for example how many brain regions were investigated, was grey matter volume in each of these related to each of the five learning rate parameters (across acquisition, generalisation and extinction), and were the moderating effects of anxiety, age and anxiety by age considered in each case?

Recommendation: please be clear in defining what "counts" as a family of analyses

– Specificity of key results

Concern: The relationship between anxiety and safety learning (as indexed by the habituation parameter to the CS– during acquisition) is one of the main findings.

Concern: The novelty of this study depends both on the strength of the computational analysis and on the extent to which the results provide new insights into the relationship between child and adult anxiety and differential fear conditioning relative to the non–computational analyses reported in the authors' prior publication on this dataset (Abdend et al., 2020). The relationship between anxiety and safety learning (as indexed by the habituation parameter to the CS– during acquisition) could be one such novel insight – however here a direct comparison of the relationship between anxiety and this parameter versus the habituation parameter to the CS+ is needed to ensure this isn't simply a non–specific habituation effect. The same issue holds for the finding of a relationship between anxiety and rate of extinction to the CS+ – the authors need to show this holds over and above any relationship between anxiety and drop off in responsivity to the CS–.

Recommendation: Here, a comparison of the relative strength of relationship between anxiety and participants' habituation parameter values for the CS– versus that for the CS+ is needed to ensure this isn't simply a non–specific habituation effect. Similarly, the authors need to directly compare the relationship between anxiety and drop off in SCRs to the CS+ during extinction against the relationship between anxiety and drop off in SCRs to the CS– during extinction to be able to make any claim specific to extinction to the CS+. This also applies to the moderating effects of brain structure on this relationship.

– SCR Approach

Concern: SCR data are likely not optimal for model fitting at the subject level; SCR is noisy, and the task involves very few trials. This may result in poorly estimated parameters; however it is not clear from the presented analyses how much of a problem this is.

Recommendation – Given the noisiness of SCR data and the limited number of trials available, parameter estimation could likely be improved substantially by using hierarchical Bayesian parameter estimation methods.

Concern: The quantification of the conditioned response is in line with some previous work, but in fact there is a range of possible analysis choices, summarised in Lonsdorf et al. 2017.

Recommendation: Given this heterogeneity, it would make sense to use the most sensitive method. Bach et al. 2020 Behaviour Research and Therapy and Ojala and Bach 2020 Neurosci Biobeh Rev discuss the most sensitive method to quantify threat conditioning from skin conductance data, and Bach et al. 2020 Nat Hum Behav provide background.

– Missing SCR Data

[Multiple reviewers] Concern: More than 1/3 of the sample are excluded due to "excessive missing data", defined as >50% missing trials.

Recommendations: It is unclear why these data were missing. Please address the explanation and please discuss the potential consequences for inference. Do excluded subjects systematically differ from those included? It would be helpful if the authors could include a table showing a break–down of the characteristics of included and excluded participants by age, gender, diagnostic status and anxiety levels and if they could address in the discussion any associated limitations in particular in relation to the age by anxiety analyses reported.

Concern: It is unclear why missing data are inter/extrapolated?

Recommendation: Use MSE. The model fitting procedure should be happy with missing data points if MSE (rather than SSE) is used as objective function. This would be more appropriate than giving the model a data value that does not exist. Censor, rather than interpolate.

– Disparate Dimensional Measures of Anxiety [Multiple Reviewers]

Concern: The combination of multiple anxiety measures (SCARED, STAI) into a single anxiety measure may not be valid, as it's reasonable to assume these are measuring subtly different constructs (aside from anything else, the SCARED measures recent symptoms while the STAI is a trait measure).

Concern: The main analyses appear to combine measures of anxiety severity across age groups as the primary variable of interest (using the SCARED for youth and the STAI for adults), and in one analysis find an interaction between age and anxiety that is driven by the younger age group. This raises some concerns as these measures are not necessarily measuring the same construct, and may limit the interpretability of these results.

Concern: Children and adults show opposing direction relationships between anxiety and fear generalisation. It is difficult to interpret the anxiety by age results given different measures were used to assess anxiety in children and in adults. This could potentially account for the different relationship between anxiety and fear generalisation in under and over 18s (see Figure 3B). I am not convinced that the authors can simply merge scores from the SCARED (which averages symptom scores based on child and adult reports) and STAI (an adult self–report questionnaire) as if they came from the same measure.

Recommendation: Absent some sort of direct quantitative harmonization (as in the GWAS literature for N/NE) or additional evidence to motivate the Z–score approach, it may not be appropriate to combine or directly compare the younger (SCARED) and older (STAI) samples (i.e. more appropriate to keep them distinct and examine them separately)

– Potential nonlinear effects of age

Concern: Only linear effects of age are modelled.

Recommendation: explore potential nonlinear effects (given that many developmental effects are nonlinear).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised manuscript – "Computational Modeling of Threat Learning Reveals Links with Anxiety and Neuroanatomy in Humans" – for consideration by eLife. Your revised article has been evaluated by Drs. Frank (Senior Editor) and Shackman (Reviewing/Handling Editor) with guidance and consultation from 2 of the 3 original Reviewers.

The manuscript has improved, with one Reviewer emphasizing that "the authors have done a good job of addressing many of the suggestions and the manuscript is definitely substantially improved as a result."

Nevertheless, there was agreement that the paper would benefit from some additional modeling.

One Reviewer wrote that, Abend et al. have addressed some, but not all of my previous concerns. The model space of the acquisition session does not include any of the "best" threat learning models from previous publications. This precludes a direct comparison; more importantly it may also miss out on the best model in this dataset.

The authors now model CS– and CS+ responses simultaneously. Yet they still do not compare their models to any of the those used in previous studies of conditioned SCR (Li et al. 2011, Zhang et al. 2016, Tzovara et al. 2018, Homan et al. 2019). They claim that their model 9 is the hybrid model used in three of these studies, but actually it is not, because the update works differently (presently they update only upon US delivery, and both CS+ and CS– from PE in CS+ trials, where as previous RW and hybrid models used the standard update on every trial, on signed PE, and with no cross–update). They qualitatively argue why the associability term in previous work does not fit their data, but in fact they should just quantitatively compare models that map value and/or associability onto SCR. Finally, they argue that Tzovara's model can only update CS+ or CS– expectation with one parameter, and modelling both CS types within the same model would lead to parameter inflaton, but in fact Tzovara's winning learning model is entirely parameter–free (only has parameters for the observation function), so this is inaccurate.

The authors need to implement these pre–existing models and show quantitatively that they do not fit the data, rather than on rely on qualitative and methodological arguments for why this is unnecessary. Based on their rebuttal, it seems that they had already implemented the models, so it should be relatively straightforward to make the necessary direct ("head–to–head") comparisons.

Along related lines, the other Reviewer noted that, [page 11] The authors argue that to adapt the Tzovara et al. model, a 5th parameter would need to be added, and that this would make it too complex. It would still be worth testing this properly [per the other reviewer's comments], and it is possible (although probably unlikely based on the provided evidence) that the model could fit well enough that it still wins despite the additional complexity–related penalisation.

The Reviewers and Editors also discussed hierarchical Bayesian approaches, with one reviewer noting that, [page 19] Reviewer suggestions related to hierarchical Bayesian parameter estimation do not seem to have been addressed in the revision. For clarity, this refers to the method of estimating reinforcement learning model parameters (see van Geen and Gerraty, 2021), rather than the SCR quantification, and there's a strong possibility it would improve parameter estimation and hence sensitivity. I appreciate that this could be represent a substantial re–analysis.

During the consultation session, the 2 Reviewers agreed that the hierarchical Bayesian approach would be nice, but is not strictly necessary for the revision, with one noting that, "I wouldn't want to force them to redo all the model fitting with a hierarchical Bayesian approach, it would likely provide more accurate estimates, but it would be a fairly big undertaking. Some acknowledgement that other model–fitting procedures exist and could be more appropriate would be nice, however (this probably also applies to their SCR quantification methods)".

And the other writing that, "I agree. This model fitting approach is a major step and may not work for some of the models."

In sum, the Bayesian approach should –– at minimum –– be noted in the Discussion.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Computational Modeling of Threat Learning Reveals Links with Anxiety and Neuroanatomy in Humans" for further consideration by eLife. Your revised article has been evaluated by Drs. Shackman (Reviewing Editor) and Frank (Senior Editor).

We are very pleased to accept your paper for publication pending receipt of a revision that adequately addresses the remaining suggestions from Reviewer #2. Congratulations in advance!

Reviewer #2:

This revision of the paper by Abend et al. is significantly stronger by including a direct comparison of the current model space with previous "best" models. There are two substantive and a few presentation points remaining.

1. The Tzovara et al. model is implemented differently from the original paper. The authors use separate regression parameters for CS+ and CS– trials for the Tzovara et al. model (i.e. 4 parameters) and it is not clear to me why – Tzovara et al. themselves had used only 2 regression parameters across these two trials types. With 2 instead of 4 parameters, the model might fare better (even though the fit/RSS will of course become worse). Could the authors include the original 2–parameter Tzovara et al. model?

2. Perhaps relatedly, I've been wondering about the initial values of the various terms in the update equations. Can they be presented in the tables? I'm wondering, for example, whether they used the same values for α_0 and β_0 in the β distribution of the Tzovara et al. model, but other readers might wonder about other models. Of course, it can make a big difference how a model is "initialised".

3. The authors make an effort to explain the difference between models 1–9, and models 10–14, by using different symbols on the LHS of the equations. Perhaps it could be made more prominent that models 1–9 predict CS–related SCR from US–related SCR and thus need no regression to scale the predictions to the data, whereas models 10–14 predict CS–related SCR from an arbitrary reinforcement variable.

4. I'm still unsure about using t–tests to compare BICs across a group. I have never seen this. What is the statistical foundation for this approach? I would suggest adding the RFX–model comparison by Stephan et al. as had been suggested by two reviewers in the context of the initial manuscript version. It is implemented in a matlab function (spm_BMS), requires only the matrix of BIC values, and takes a few seconds to run.
