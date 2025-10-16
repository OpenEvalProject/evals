# Peer review - Round 1

Editors:
- Michael W Cole, https://ror.org/05vt9qd57 Rutgers, The State University of New Jersey United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81511.sa0](https://doi.org/10.7554/eLife.81511.sa0)

This study presents the valuable finding that the human cerebellum receives highly convergent (rather than sparse) task-related connectivity from the cortex. A compelling case is made that this convergent connectivity supports a wide variety of cognitive functions, though it will be important for future work to fully verify the cortical-to-cerebellar directionality of the results. The work will be of broad interest to cognitive neuroscientists interested in the role of connectivity in cognition.


---

# Peer review - Round 1

Editors:
- Michael W Cole, https://ror.org/05vt9qd57 Rutgers, The State University of New Jersey United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81511.sa1](https://doi.org/10.7554/eLife.81511.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A task-general connectivity model reveals variation in convergence of cortical inputs to functional regions of the cerebellum" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Chris Baker as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Claims of directionality are overstated and should be revised accordingly.

2) The authors should address the differences in model complexity, ideally through an additional analysis (e.g., involving AIC or BIC).

3) More details on the connectivity method used, especially how it handles the task-evoked variance inflation problem.

4) The authors should discuss the possibility that motor tasks are inherently simpler than non-motor tasks, which may have biased their results regarding motor vs. non-motor regions.

Reviewer #2 (Recommendations for the authors):

The authors should compare model performance while accounting for model complexity. One solution is for the Lasso/Ridge models to have the "WTA" weights to be fixed while randomly permuting all other weights. If the Ridge model is truly better, you would expect this random model to perform similarly to the WTA model but worse than the original Ridge/Lasso models. This would suggest that more inputs do not significantly explain more variances in the cerebellum just by chance.

The authors should expand the discussion on the closed-loop anatomical relationship between the cerebellum and the cortex and how its multi-synaptic relationship can allow converging inputs from the cortex to the cerebellum.

For figures 3 and 4, it would be nice to expand and show physically where and how widespread those cortical inputs are. That can help readers contextualize the physical level of "convergence" of the cortex onto cerebellar regions.

Instead of interpreting the results as cortico-cerebellar inputs, discuss how they can be bidirectional interactions.

Reviewer #3 (Recommendations for the authors):

– The authors note that a "convergent architecture would suggest that subregions in the cerebellum integrate information across disparate cortical regions and may coordinate their interactions." It would be interesting to evaluate the degree to which the "disparate" regions that may provide convergent inputs to the cerebellum, as identified in this study, are functionally/anatomically related.

– The authors discuss findings from Pisano et al. 2021 as anatomical evidence for cerebellar outputs from specific regions reaching a variety of cortical targets. However, it is important to note that in most species, and especially in the mouse, it is quite unlikely that any one anatomical tracer injection into the cerebellar cortex can target a functionally distinct region of the cerebellum. See, for example, Fujita et al. 2010 J Comp Neurol where small injections into marmoset cerebellar cortex are difficult to localize to specific longitudinal bands in the cerebellar cortex.

– A map of the cerebellum showing the MDTB regions would be useful to include as a guideline in Figure 3

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A task-general connectivity model reveals variation in convergence of cortical inputs to functional regions of the cerebellum" for further consideration by eLife. Your revised article has been evaluated by Chris Baker (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors did an excellent job improving their manuscript based on previous reviews, except for one major point described below.

R1 point 3 was responded to, but not meaningfully addressed. The authors seemed to misunderstand the issue that regressing out mean task-evoked activity is meant to deal with, resulting in the authors effectively ignoring the issue with regard to their own study. Indicative of misunderstanding the issue, the authors state: "Returning to the papers cited by the reviewer, these are designed to look at connectivity not related to the task-evoked activity." This is a common misunderstanding in the field: Rather than looking at connectivity not related to task-evoked activity, regressing out mean task-evoked activity is meant to deal with a causal confound (common inputs from stimuli), while still allowing estimation of connectivity related to the task-evoked activity. This interest in the impact of the task-related activity on connectivity is clear from the simple logic of most studies utilizing mean task-evoked activity regression, wherein connectivity estimated in the context of condition-specific task-evoked activity is compared. (If all task-evoked activity were removed then there would be no point in comparing task conditions.) What is left over for estimating functional connectivity estimation is trial-by-trial (and moment-to-moment) variation in task-evoked activity (along with spontaneous activity). So, the authors have not dealt with the possibility that common stimulus inputs – such as centrally presented visual stimuli simultaneously activating left and right hemispheres, generating false inter-hemispheric functional connections – are driving some of their connectivity estimates. Ideally, this confound would be dealt with, but at the very least the authors should acknowledge this limitation of their methods.

Beyond this issue (and perhaps more importantly), it is difficult to reconcile the present study's approach with more standard task-related functional connectivity approaches. How can connectivity values estimated via the present study's approach be interpreted? How do these interpretations differ from those of more common task-related functional connectivity approaches? Is there enough advantage to using the present study's unconventional task-related functional connectivity method to make it worth the extra effort for readers to make sense of it and learn to relate it to more standard approaches? The presence of all of these unanswered questions makes it difficult to properly evaluate the manuscript and its results.

Further, in my attempt to answer the above questions myself, I have read and re-read the description of the connectivity approach, and yet I have not been able to make sense of it. I doubt this is my own lack of knowledge or intelligence, but even if that were the case it is likely that many (perhaps most) readers would have the same issue. Therefore, I recommend rewriting the "Connectivity Models" section (within "Methods") to include more details. Some specific details that would be helpful to include:

– The meaning of "fitted time series" is ambiguous. Does this mean the original time series multiplied by the fit β estimate for each condition, resulting in the original time series modulated by the fit to the task regressor for each condition? Or does this mean the regressor time series multiplied by the fit β estimate for each condition? If it is the first option I can imagine interpreting the resulting functional connectivity estimates in a fairly similar way to standard task-related functional connectivity. However, if it is the second option, then I think the interpretation would be quite different from standard task-related functional connectivity. In such a case I think much more details on how to interpret the resulting connectivity values would be warranted. Of course, it could be a third option I haven't considered, in which case it would be helpful to have that option detailed.

– It is unclear what this detail means (pg. 24): "This procedure reweighted the activity estimates in an optimal manner, accounting for the fact that estimates for the instructions were based on 5 s of fMRI data, while estimates for the conditions were based on 10-30 s of data." In what sense is this accounting for the duration of task conditions? This makes me wonder whether the connectivity estimates were based on using cortical β estimates (rather than time series) to predict cerebellar β estimates (rather than time series), which could account for condition duration quite well. But the description is ambiguous with respect to these kind of details, and this possibility doesn't seem to fit well with earlier descriptions of the method.

– It is unclear what this detail means (pg. 24): "This method also mitigates problems that may arise in event-related designs due to correlations between regressors (Mumford et al., 2012)." How exactly? Also, what exactly are the problems that may arise in event-related designs due to correlations between regressors? It sounds like this is related to collinearity, but it is unclear which aspects of the method help with collinearity.

– The details regarding the "crossed" approach need to be fleshed out. It is stated (pg. 25): "we used a "crossed" approach to train the models: The cerebellar fitted time series for the first session was predicted by the cortical time series from the second session, and vice-versa". This procedure is also presented in an ambiguous manner in Figure 1. Right now it is stated in the manuscript that the session 2 cortical time series are used to predict the session 1 cerebellar time series, and yet it is unclear how that would be possible when there are different task conditions across the sessions. Is the connectivity model built using both cortical and cerebellar time series during session 2 (betas from cortex predicting cerebellum), then both cortical and cerebellar time series are used from session 1 to test the session 2 connectivity model (session 2 betas multiplied by session 1 cortical time series to predict session 1 cerebellar time series)? Put more simply: is it the case that the session 2 connectivity model is tested using session 1 data, and that the session 1 connectivity model is tested using session 2 data? If so, the description should change to better describe this. In any case, the description should be clarified with more details.
