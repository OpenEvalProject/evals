# Peer review - Round 1

Editors:
- Morgan Barense, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54519.sa1](https://doi.org/10.7554/eLife.54519.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Memory replay enables humans recall the past in a flexible and temporally-compressed manner. The extent to which this process is shared with nonhuman primates is unknown. Kwok and colleagues demonstrate that, like humans, macaque monkeys temporally compress past experiences with a non-linear forward-replay mechanism. However, replay in macaques was strictly forward; unlike humans, macaque monkeys lacked a global compression mechanism that enabled the flexibility to skip irrelevant information. This work helps to map the evolution the episodic memory.

Decision letter after peer review:

Thank you for submitting your article "Behavioral evidence for memory replay of video episodes in macaque monkeys" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bryan Strange (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All reviewers agreed that this is an interesting and timely paper, and they universally congratulated you on the Herculean effort involved in conducting this research. The reviewers did raise several issues that must be addressed prior to publication. Their reviews are included below.

The manuscript presents a number of very complex analyses, which were at times difficult to digest. In the revision, we encourage the authors to improve the overall clarity of the manuscript by providing more (and clearer) details on the methods. Each reviewer has highlighted specific requests for more information and additional analyses to clarify results. Clearer linkage between the Materials and methods and corresponding Results would also help to improve the manuscript's clarity.

The reviewers raised questions about the behavioural performance measures (e.g., the need to more carefully consider the accuracy data, the inclusion of both correct and incorrect trials, and how stimulus repetition may affect the results). In several instances, the reviewers suggested additional interpretations of the data.

We hope that these comments are helpful as you prepare your revision, and look forward to receiving the revised manuscript.

Reviewer #1:In this manuscript, Zuo and colleagues present novel behavioural data from macaque monkeys with the aim of investigating the presence of replay during temporal order judgments for previously seen video clips. The question and paradigm are interesting and timely. The comparisons between monkey and human strategies and performance are especially intriguing. However, I have some questions about the behavioural performance and measures. The statistical models should also be reported more clearly and the link to predictions should be more explicit.

1) Additional details about the testing paradigm and overall behavioural results are needed. Were the monkeys trained ahead of time (and if so, how long did the training take)? With such a protracted period, it would be interesting to know whether the monkeys' performance improved or changed over the course of the experiment. As their performance is not at ceiling level, it seems possible that they improve overall, or that they start relying on different aspects to make their judgments. Day of testing could therefore also be included as a predictor in the models.

Regarding the monkeys' accuracy: in the subsection “Task performance”, the authors report that the monkeys' overall accuracy was ~68%. Was this the overall accuracy calculated across all 50 testing days? In contrast, the monkeys' accuracy plotted in Figure 2C is barely above chance level – while it's clear that the pattern displayed in the figure will be noisy as the data are split according to target frame location, the lines hover close to chance level and don't seem to average out to 68%. I may be missing something, but unless the data in Figure 2C represent only a subset, for example, this needs to be explained in more detail. Related to the point above, it would generally be helpful if the authors provided a measure of the monkeys' accuracy over the course of testing.

This is also important as the human participants' accuracy was at ceiling after a single testing session (based on the aforementioned subsection) – did the trend of the monkeys' performance remain the same across the 50 testing days (i.e., no global compression), or did this only develop after extensive experience on the task?

2) On a related note, it seems confusing to include both correct and incorrect trials in most of the analyses. In the GLM analyses (subsection “Human-like forward replay in macaques”, Supplementary file 2), the patterns were indeed quite similar for correct and incorrect trials, but it still seems unusual to include trials where the monkeys may not have replayed the content correctly as they reached an incorrect decision. Further, the different amounts of data entered into different models (correct trials only vs. all trials) make it more difficult to compare them. I would recommend that only correct trials are included in all analyses, or additional control analyses are needed to ensure that all findings remain the same when only correct trials are used.

3) The comparison between monkey and human data in Figure 3 is especially interesting. It is intriguing to see that human participants display global compression, but monkeys do not, and this interpretation seems to be well-supported by the data. However, the authors state that monkeys 'reach their memory decision threshold more quickly when probe frames are extracted from the two different contexts' and that these findings 'parallel closely established findings in the humans'. This pattern is in fact the opposite to that observed in humans; when two stimuli are separated by a boundary, humans are slower to reach a decision (e.g. Ezzyat and Davachi, 2014; Heusser et al., 2018, to name just two recent papers). This interpretation should be revised as the data from the present manuscript in fact suggest that boundaries affect human and monkey decision making processes in opposite directions.

4) The manuscript contains a relatively large number of (at times complex) analyses. As the more complex models are such an important aspect of the paper, they should be explained in more detail and the link between Materials and methods and Results should be clear. I found it somewhat difficult to align the description of the analytic approach in the Materials and methods section with the reporting of the results. In general, more detail in the description of the methods is needed. This especially applies to the model and variable descriptions. A few key points below:

– In the subsection “Task and experimental procedure”, the authors state that the experiment comprised four factors: boundary, play order, temporal distance, and exposure. First, I found it unusual that the authors reported temporal distance as a factor with 25 levels, since modeling it as a categorical variable assumes that all 25 levels are independent of one another. If this was not the case, it should be clarified in text, but if this variable was indeed modeled as a categorical factor, this should be changed to continuous or ordinal.

Second, in the subsection “Generalized linear models (GLM)”, the authors then report a set of variables included in the GLM. If I'm not mistaken, these are only regressed out of the very last GLM (subsection “Confirmatory GLMs for the putative patterns”). While the evidence from this analysis is clear and the significance of the key factors of interest does not change, I think including these regressors in each of the analyses and treating them as nuisance regressors would be more convincing/parsimonious.

– The description of the LATER model fitting was somewhat confusing. For example, it wasn't immediately clear that 'both conditions' (subsection “LATER (linear approach to threshold with ergodic rate) modelling”) refers to within vs. across clips. I also found it somewhat confusing that one of the models was called 'unconstrained' in the Materials and methods, but 'two fits' in Supplementary file 5 (if that is indeed the same model). Finally, in the Materials and methods, the authors refer to Figure 4A, which I believe should be Figure 6A. I am not a modeler, but it would nonetheless be important for the model descriptions to be linked back to the experimental predictions to make the connection between model parameters and behaviour clearer.

– How exactly was reciprocal latency calculated? I was not familiar with the term beforehand so I looked it up in the literature, but I would suggest that all key variables are defined in an accessible manner.

5) Related to the above: in the Introduction, the authors say that a 'non-linear' pattern would be predicted, which led me to expect a comparison of linear and non-linear model fits. Similarly, in the Materials and methods, the authors state that they used BIC to 'obtain the best fit among these models' – as this section immediately follows the section on GLMs, I assumed the models would be compared. However, the only BIC value reported is that comparing the 'shift' and 'swivel' models. I believe BIC can be used to compare any model types (i.e. linear and non-linear), but if this is not the case, the approach should be clarified. Unless I'm missing something, it appears that the reciprocal latency was modelled in a linear model (subsection “Human-like forward replay in macaques”), but the 'non-linearity' of the fit was only assessed visually. As the linear analyses all had significant outcomes, it seems important to provide a benchmark of 'goodness of fit' for different models. Reporting the significance of different trends (e.g. linear, quadratic, cubic) could be helpful.

Reviewer #2:In this study, Zuo et al. examined existence of memory replay during the retrieval of video clip material encoded continuously during periods of ~10 seconds. The study combined several computational modeling approaches and complex analytical procedures on reaction time data to test whether monkeys showed forward replay of the encoded material and whether the replayed memory content showed a structured pattern modulated by context changes during encoding, as shown previously in humans. Their results, though similar with humans in many aspects, also revealed striking differences, being the Inability to skip irrelevant Information In their replay a major one.

I found the study very well written and the topic of research of interest among many in the neuroscientific community. The analytical approach is sophisticated and the implementation sounding. I do have however some concerns that would require further attention though, which are listed below:

1) Many of the findings described in human studies related to sequence of images or video clips that are presented only once. Here, animals are shown repeatedly with the video clips. To what extent the repetition is affecting the underlying neural mechanisms and consequently the actual findings? I am aware the study included somehow this in their GLM model (Supplementary Figure 3) but in my view, this should require some more work. The question that one would like to see answered here would be: To what extent differences between humans and macaques are susceptible to be affected by the large amount of repeated material used in monkeys? I am aware many of the analysis included in the study require large number of trials for each individual but maybe authors can explore this issue across participants?

2) Several details concerning the experimental design tested in humans are lacking. Which are the differences between the two species when it comes to the experimental design? This information should be clear in the manuscript so that differences and similarities between species can be fully evaluated.

3) I was expecting that most of the analysis were implemented in monkeys' and in humans' data. Is there any particular reason to skip some of them in humans RTs (for example: effects of context change (within vs. across) and GLM confirmatory analysis)?

4) Correlation results between models should be directly compared and show they differed significantly to be able to attribute a winner one (i.e., Figure 3).

5) I found the results showing that many of the effects were equally robust for correct and incorrect trials a bit confusing. In my understanding, the behavioural manifestation of how memory content is organized and replayed should be specifically evident for when retrieval access has been successful, as otherwise it may be difficult to discard the possibility that the observations are driven by a more general task oriented operation. Can the authors please justify why it would be relevant that many of their central findings were valid for correct and incorrect trials? And if so, wouldn't it be also relevant to show the same results in humans' data?

Reviewer #3:By training 6 macaques on a cinematic video-clip task, Kwok and colleagues have leveraged reaction time (RT) data to make inferences on the ability of non-human primates to make temporal order judgment (TOJ). RT analyses, using LATER and drift-diffusion modelling, enabled to authors to suggest potential mechanistic underpinnings to the behavioural effects they observe. Irrespective of performance, RTs were faster if the still pertained to earlier segments of the video clip. The effect was non-linear, as the correlation was significant for log-transformed RTs. Furthermore, the relationship of still presentation latency to RT was around 10:1, which the authors interpret as time compression in replay. Humans, on the other hand do not show this relationship.

This is an interesting paper, and the cross-species differences are very clearly depicted and highly interesting. I commend the authors on what is a tremendous effort in terms of stimulus preparation and animal training. I have some comments that would need to be addressed before recommending publication.

1) The authors have concentrated mainly on RTs, but when accuracy is considered (plotted in Figure 2C) it is clear that for many target frame locations, the macaques are performing at chance (horizontal blue line). In at least 3 of the macaques, accuracy seems worse for earliest stills from clip 1. Could there be a speed-accuracy trade-off underlying faster RTs for these early stills? I appreciate that, overall, performance was above chance (it is somewhat atypical to report this at the beginning of the Materials and methods section), but the possible confound of monkeys making fast responses with little memory content to these early still probes needs addressing.

2) Furthermore, there is clearly an improvement in accuracy for stills that are at the beginning of clip 2. The authors mention this as "a blip" but provide no statistics. This is an interesting boundary effect that could be reported better and integrated with point 3.

3) Representational similarity analyses were used to demonstrate that "global compression" of individual video clips is not evident in macaques, who appear to show increasing RTs to stills drawn from over the course of the 2 clips (i.e. the strictly forward model). There is a non-significant trend towards global compression effects in humans. It is clear, though, that macaques and humans respond differently. What makes things a bit confusing is that LATER modeling indicated that macaques show an important boundary effect. Memory decision threshold is reached more quickly if probe stills come from different clips. I wonder whether this has something to do with perceptual similarity effects reported later for the GLM analyses, but I did not get a good feel for what this perceptual similarity parameter is measuring.

4) I am undecided as to whether Figure 5 and associated Results section really add to the findings. It is clear from the preceding figures that slope is markedly different in the two species.

5) In view of the indirect nature of the inference, certain statements such as "The monkeys apply a non-linear forward, time-compressed replay mechanism during the temporal-order judgement” (Abstract) need to be toned down.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Behavioral evidence for memory replay of video episodes in the macaque" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor The following individual involved in review of your submission has agreed to reveal their identity: Bryan Strange (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The reviewers were very satisfied with the revisions and we would like to congratulate you on a fine paper. The number of testing days for each animal is testimony to Herculean effort put into this work, and we believe that it will be a very important contribution to understanding cross-species differences in memory replay.

It was noted that with the additional analyses, the paper now shows more robust evidence for a forward scanning strategy in non-human primates. The additional analyses regarding training/testing session over time were also appreciated, in particular including response accuracy as a covariate and the trend analysis.

Only a few relatively minor comments remain:

1) The observation that the findings largely hold up when the data are split by correct and incorrect trials (Table 1) certainly supports the authors' decision to include all trials in their analysis, regardless of correctness. However, since the findings are so similar for correct and incorrect trials, the authors may wish to discuss why this pattern might be observed even on incorrect trials. Is the assumption that the monkeys are replaying the content correctly but then reaching an incorrect decision or that the information was incorrectly encoded? In other words, if the latency data reflects memory processes, an incorrect decision here would suggest that the initially encoded temporal order was incorrect. Either way, this seems like an interesting finding and Discussion point.

2) Regarding the analysis of linear, quadratic, and cubic trends: it is indeed encouraging to see that the non-linear (quadratic and cubic) trends are significant in the monkeys. However, interestingly, only the cubic trend seems to be significant in the human sample (linear and quadratic are not). Since one of the important contributions of this paper is a direct comparison between monkeys and humans, we think it would be helpful if the authors also addressed this difference in the manuscript. We also suggest that the manuscript text more explicitly stated what type of non-linear relationship was observed (i.e., in the subsection “Human-like forward replay in macaques” where these results are reported).

There were two requests for greater clarity:

1) The Introduction sets up the notion of linear vs. non-linear models for RTs and the authors state that they adjudicate between the two aspects of the replay models comparing between human and macaque data. While I appreciate that the non-linear human component refers to the global compression, the fact that monkeys appear to have performed TOJ using a forward search with non-linear compression, might confuse some readers. It was recommended that this be made explicit in the Introduction.

2) The legend of Figure 6—figure supplement 1 needs to include more explanation; please correct. Is the point of this to indicate that there is not a direct mapping of all features between inset and T-shirt images (i.e. the coloured lines don't always go to the same point of the corresponding image)?
