# Peer review - Round 1

Editors:
- Jonas Obleser, University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68265.sa1](https://doi.org/10.7554/eLife.68265.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study takes a comprehensive look at the relationship between pupil-indexed arousal and cortical MEG activity and performance on a demanding sensory behaviour in humans subjects. Understanding how pupil activity, widely interpreted as a proxy of arousal, ties in with the dynamics of neural activity and behaviour is a key challenge in systems and cognitive neuroscience. The authors identified a widespread component of cortical activity that can be explained by changes in pupil dilation and which in turn predicts performance in participants' decision-making. This work will help build an important bridge between animal models of arousal and human cognition and behaviour.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Spectral signature and behavioral consequence of spontaneous shifts of pupil-linked arousal in human" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jan Willem de Gee (Reviewer #3).

Our decision has been reached after consultation between the reviewers.

The reviewers and editors felt that this manuscript aims at offering important insights. First, brain-wide relationships across a wide range of spectra have only rarely been tested in humans. Second, testing direct and indirect links between baseline pupil size, spectral power and behaviour, separately, has not been done before in humans, to the best of our knowledge. Finally, the authors try to combine and compare the behavioural relevance of slow as well as fast pupil size fluctuations, linking to previous research in non-human animals.

Our enthusiasm was tempered, however, as the methodical issues raised by all reviewers are substantial. The editors were not convinced that these are outweighed by the potential advance in the results. The main concerns tie into issues raised by all reviewers about what appear to us as somewhat arbitrary decisions in how the models were formulated. The individual reviews, attached below, will delineate these concerns in greater detail.

Reviewer #3:

I think this is an important paper. The characterization of the relationship between baseline pupil size and large-scale cortical spectral power across a wide range of frequencies (localized using Dynamic Imaging of Coherent Sources) is state of the art and novel. However, I do have a number of serious issues with the methods. I expect at least some of the results will change when the authors address these.

I have a number of issues about the mixed effects modeling.

– The authors write that they only considered random intercepts, and not random slopes. Why? See for example Barr et al., Journal of Memory and Language, 2013. I believe two common approaches to keep the random structure maximal (random intercepts and random slopes) are: (i) fit the model with the maximal random structure, and stick to that model if it converges, (ii) start with the maximal random structure, and formally compare that model (with AIC/BIC) to models in which you drop one random factor at a time and choose the model with the lowest AIC/BIC.

– Since the authors compare models, I think they were not fitted through restricted maximum likelihood estimation (REML); what method did they use?

– I think it's commendable that the authors considered quadratic models. However, I think they should formally test whether adding a quadratic component significantly improves the fit (via AIC/BIC), and present result accordingly.

– I'm confused about the way "residual pupil size" is calculated. Why is it necessary to first fit a group level model, and then a subject-level? Why not do subject-level directly? Furthermore, it seems very award to not regress out the quadratic relationships here, as we have learned that they are important. I understand the multicollinearity problem, but there may be a more elegant way to deal with this?

I think that the question whether "the effect of baseline pupil state (a peripheral marker of arousal) on perceptual behavior is mediated by the shift in cortical spectral power (a central marker of arousal)" is important. However, I think that the partial correlation approach they use is not ideal to answer this question. Have the authors instead considered to perform an actual mediation analysis? If they want to stick to partial correlation, I think they should do proper partial correlation, and not only regress out cortical spectral power from baseline pupil size, but also from their behavioral metrics, and only then compute the residual relationship between pupil and behavior.

Eyelink records pupil data in arbitrary units. How did the authors meaningfully pool "slow states" across different experimental runs? Z-scoring does not do the trick here. For example, a pupil that is consistently large all the time will result in slow states close to Z=0. Also, strong slow drift results in a large standard deviation, and will push the z-scores down, which is precisely not what you want in that case. Related, why are the units in Figure 3B (z-score) different than in Figure 4C,D (%). In the latter case, % of what?

Are results the same after excluding slow states including blinks? I understand that the authors used ICA to remove blink-related artifacts from the MEG data. However, blinks also cause relatively large transient pupil constrictions (Knapen et al., PLOS ONE, 2016), which will work into the 2-s averages. Related, how often did subjects blink? From Figure 1D it seems about 10 times per minute, which means that 33% of "slow states" might be affected. Finally, why did the authors not use the blink onset and offset timestamps provided by Eyelink? I'm asking because using a constant threshold will miss partial blinks. If the authors want to detect blinks themselves, they should do so based on outliers in the first derivative of the pupil time series.

I think the authors should better integrate their findings with the existing literature, and be more precise with their citations:

– Line 42: "and animals" -> ref. 7 should be cited here as well.

– Line 54: "across a wide range of frequencies" -> ref. 14 did, albeit only in auditory cortex.

– Line 96: "play a functional role in behavior" -> ref. 15, 41 should be cited, and see also de Gee et al., PNAS, 2014; de Gee et al., eLife, 2020; Krishnamurthy et al., NHB, 2017; Urai et al., Nat Comm, 2017.

– Line 322: "limited data is available in humans" -> ref. 41 should be cited.

– Line 326: "deserved further investigation" -> ref. 41 should be cited.

Reviewer #4:

Podvalny and colleagues investigate the links between spontaneous variations in arousal, as indexed by varying pupil size, and spectral power as well as perceptual decision performance. The study represents extends previous work in non-human animals, initial findings in humans, and improves our understanding of behaviourally relevant changes in arousal and their effects on mesoscopic measures of brain activity (M/EEG). Despite these valuable contributions to the field, central results hinge on methodical approaches that are potentially problematic. In addition to these methodical issues, the transparency and clarity with which results are presented should be improved.

1) Linear mixed effect models:

Although I applaud the general approach of fitting linear mixed effect models to neural and behavioural data, the exact implementation in the current manuscript could be improved and is potentially problematic. First of all, it remains unclear why the authors do not use the potential of LMMs and also fit random slopes to test effects on the single subject level. This is only carried out to partialize pupil size and spectral power, respectively, but not in any models that concern behaviour or the link between spectral power and pupil size. Is there a reason the authors did not fit random slopes? I advocate for the inclusion of random slopes (depending on the model fit) for variables of interest and the inclusion of single subject estimates in all figures. If random slopes for all predictors within the same model lead to convergence issues or problematic model fit, the use of multiple models that only differ in their random slopes (e.g., pupil or spectral power) is acceptable. In this context, it seems to me as if the authors never model behaviour as a joint function of pupil size and spectral power. I strongly suggest to include both spectral power and pupil size in models of behaviour to account for shared variance in the dependent variable of interest (e.g. hit rate or false alarm rate). Furthermore, although the comparison of purely linear and quadratic (including a linear term) models represents an aptly chosen approach, the authors should handle their inferences regarding these model terms with great care and report them more cautiously. Figure 4C for example features visualized quadratic trends that do not represent significant model terms (e.g., sensitivity, response times, etc.). It should be made very clear to the reader that these quadratic effects do not explain additional variance in behaviour and do not fit the data well. In addition, in models where quadratic trends explain significant portions of variance, linear and quadratic effects should be compared directly (e.g., Wald-z statistic) and the results of these comparisons should be reported. Only this way, readers can be able to judge whether linear or quadratic trends are pervasive in a certain relationship. On another note, it is unclear to me if the model coefficients that are presented (e.g., Figure 5) represent standardized betas. If this is the case, they can also work as effect size estimates and an intuitive interpretation should be offered (e.g., "one unit change in pupil size coincides with x…").

2) Stats reporting:

Although the authors have included tables in their manuscript, essential test statistics should be reported within the main text (estimates, confidence intervals, p-values). Despite some p-values, this is missing entirely and should be added. Additionally, I suggest to report standardized effect size estimates to allow for an intuitive interpretation of results. Furthermore, it would be important to note how much variance in brain, behavioural, or pupil data were explained by the winning models. Maybe I have missed this information, if not, it should be added.

3) Stimulus category decoding:

While this is an elegant approach to study the representation of sensory stimuli within neural data and compare them across conditions, the employed chance level is problematic. While it is true that 25% represents the theoretical chance level in a case where four alternatives are discriminated, this is only true for infinite numbers of trials – or at least large datasets (Combrisson et al., 2015, JNeuroMeth). If I understood the approach of bin-wise leave-one out classification correctly, each bin contained about 70 trials. In this case, the empirical chance rate can be calculated as Emp_chance = binoinv(1-α,n_trials,1/n_classes)/n_trials; Where α corresponds to the desired significance level (.05), n_trials to the number of trials and n_classes (4) to the number of possible outcomes. Using this approach, an empirical chance level of 34.2 % is calculated which clearly differs from the theoretical level 0f 25 %. I suggest to either test against the empirical chance level or establish a noise distribution of prediction accuracies using permutations, against which to test.

Reviewer #5:

The study by Podvalny et al. measured the relationship between pupil diameter and cortical spectral power, assessing how they provide overlapping versus complementary indices of brain state. The authors used regression analysis to identify relationships between spontaneous, pre-stimulus fluctuations in pupil and MEG spectral power and performance on a visual discrimination task. The analysis revealed correlations between pupil and cortical spectral power but also unique variance between each of these signals and task performance. The experiments and data are novel and are nicely designed and executed. While the results are interesting, they appear in many cases to replicate previous findings. It would help if the authors could more clearly explain the gaps the new results fill in the existing literature.

1. The authors cite work several previous studies in human (Washke et al., Van Kempen et al., de Gee et al) and animal (McGinley et al., Joshi et al., Reimer et al) that explored similar questions and appear to be largely consistent with the current data. This study does appear make a few new comparisons and identifies some differences with the previous work, but the new results appear as a scattered list of observations throughout the discussion. The main observation of explanatory overlap between pupil and cortical spectral power appears to be a replication. It would help if the authors could clarify the novelty of their main results.

2. The modeling results could be presented more clearly. While the general methodology appears sound, it is difficult to discern what aspects of the cortical spectral power are shared with pupil versus not. For example, would it be possible to contrast coefficients for the pupil-independent spectral power model (Figure 5) with coefficients for a model without removing pupil? This information is available in some form in Figures 3 and 4, but it is unclear if and how the units of these different models can be compared. It seems like there should be a unified way to present the joint versus unique contributions of the pupil and MEG signals in terms of variance explained, which would make the results much easier to digest. Without a more comprehensive summary, the results appear as mostly disparate observations.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Spectral signature and behavioral consequence of spontaneous shifts of pupil-linked arousal in human" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor), a Reviewing Editor, the original reviewers, and a new reviewer.

This study takes a comprehensive look at the relationship between pupil-indexed arousal and cortical MEG activity and performance on a demanding sensory behavior in humans subjects. Understanding how pupil activity, widely interpreted as a marker of arousal, relates to cortical activity, is a key challenge in systems and cognitive neuroscience. The authors identified a widespread component of cortical activity that can be explained by changes in pupil and that predict performance on a behavioral task. This work helps build an important bridge between animal models of arousal and human cognitive behavior.

Essential revisions:

Presentation of single subject data (as per Rev #1).

1) Presentation of effect sizes and explained variance (as per Rev #1).

2) Are pupil-related effects really essentially uniform across the cortex? Or are the differences really the important thing? It would be nice if this could be addressed even briefly in the Discussion. (as per Rev #3)

3) Since the present analysis is focused on quantifying pupil size it is important to account for other factors which might affect measured pupil size, notably, fixation and saccades. The section devoted to detailing the analysis of the pupil data omits any discussion of these factors. Did the authors check that fixation is maintained at all times? Were periods associated with saccades away from fixation (which will result in apparent changes to pupil size) removed from the analysis? (as per Rev #4)

4) The analysis of "fast events" was not very clear to us (as per Rev #4, please follow the details for an additional/re-analysis there):

a) we are worried about the low-pass filter and a potential acausal smearing it might have contributed.

b) The statement (line 492) "to be considered a peak/through, the data point should have highest/lowest amplitude within 500 ms vicinity" was also not clear. It would be helpful if you plotted (or reported) the duration distribution of the events you ended up analyzing (as per Rev #4, see details also below).

Reviewer #1:

The authors have revised large parts of their manuscript and addressed most comments.

However, two of my previous concerns have not been resolved entirely.

1) Presentation of single subject data.

The authors argue that this is not feasible as it would require to plot more than 8000 data points. This likely is a misunderstanding. While it is true that plotting single subject points for all power / frequency / ROI bins is not feasible, this is not what I asked for. Take figure 3B as an example. In every panel, the authors plot spectral power (in bins) as a function of pupil size (in bins). They plot one data point per bin (with an error bar around it). If I am not entirely mistaken, this data point represents the group average. It is essential, however, to show single subject data at this point. What speaks against plotting a cloud of N=24 dots around their mean instead of each dot? I realize that this might take up a bit more space but I am convinced that this is an essential service to every reader. Importantly, the same comment applies to figure panels 4C, 4D, and 4E.

2) Effect sizes and explained variance

While it is true that the concept of variance is explained is not easily transferred to the world of linear mixed models, it is entirely possible to offer such an estimate, both for linear mixed models as well as generalized mixed models. Even if imperfect, such an approximation represents an important piece of information since it puts the models in perspective to the space they were trying to capture. I allow myself to recommend the excellent R-package lme4 which allows the fitting of such models and in combination with functions from the sj_plot package (e.g., tab_model) offers all relevant information. I am sure transferring their models from python to R should be a simple task for the authors.

Furthermore, I suggest to offer an explicit discussion of model fits and effect sizes which is missing in the current version of the manuscript. The supplementary tables illustrate that effects rather are small and likely don't account for large parts of variance in the data. This does not have to be an issue but it should be acknowledged prominently and discussed.

Reviewer #2:

The authors have performed a thorough revision and addressed my concerns. I have no remaining issues.

Reviewer #3:The authors were responsive to all the concerns raised in the initial review. The revised manuscript clarifies the significance of the work and more rigorously identifies the link between pupil size, cortical activity and task performance.Overall, the manuscript looks great. Just a small lingering question. The effects in Figure 3 appear strikingly consistent across brain networks, and any differences appear to be quantitative more than qualitative (ie, even where a quadratic effect may not be significant, one can still see a trend that is consistent with networks showing a quadratic effect). Does this mean that pupil-related effects are more or less uniform across the cortex? Or are the differences really the important thing? It would be nice if this could be addressed even briefly in the Discussion.

Reviewer #4:

I joined the review process at the revision stage. I did not read the previous version of the manuscript or the rebuttal later in order to form an unbiased view of the work.

1) The experiment is quite long (over an hour and a half). In addition to task related effort, experimental length can have consequences for pupil dynamics due to effort related to maintain fixation and accommodation. It is critical that the authors demonstrate that pre-stimulus pupil size is not correlated with time within the experiment.

2) Similarly, since the present analysis is focused on quantifying pupil size it is important to account for other factors which might affect measured pupil size, notably, fixation and saccades. The section devoted to detailing the analysis of the pupil data omits any discussion of these factors. Did the authors check that fixation is maintained at all times? Were periods associated with saccades away from fixation (which will result in apparent changes to pupil size) removed from the analysis?

3) The analysis of "fast events" was not very clear to me.

a) Why was a low pass filter applied to the data before identifying the phasic events? Wouldn't a low pass filter smear the timing of these events? Depending on the filter (no details are provided) this could result in latency shifts on the order of 200ms, making the "fast event" analysis (Figure 6) difficult to interpret.

b) The statement (line 492) "to be considered a peak/through, the data point should have highest/lowest amplitude within 500 ms vicinity" was also not clear. It would be helpful if you plotted (or reported) the duration distribution of the events you ended up analyzing and maybe follow the analysis approach as used in e.g. Joshi et al. (2016; Neuron) where phasic events are defined as zero-crossings of the pupil slope separated by {greater than or equal to}75 ms. This will make it easier to relate your findings to the literature on phasic pupil responses.

4) Analysis in Figure 6 (and page 12).

a) Why was a Pearson and not spearman correlation used? The latter is less sensitive to outliers and would provide stronger evidence for the claims the authors wish to make.

b) Panel C: I am a bit confused by the example of identified pupil events provided. In the methods you state that you defined dilation/constriction events as having a duration of at most 500 ms. But from eye balling the figure the first dilation event (left most blue dot) appears to last more than a second? (Similarly the right most blue dot in the plot).

c) I would like to see more discussion of the shape of the patter of MEG activity triggered by the pupil events. I found the pattern extremely surprising. e.g. that the sharp peak/trough exactly coincides with 0; is it possible that the preceding peak at ~-400 relates to a previous dilation/constriction event? I would appreciate more detailed discussion of what this all means. Similarly the pattern of correlation across channels looks quite systematic. Did the authors try to source localize this pattern?

Other points

1) It is stated that sensitivity (d') is related to prestimulus size in an inverted U-shaped relationship. This is not obvious at all from looking at the data points in the figure. Instead the behavioral performance appears to not differ much for pupil bins 2-5.

2) I understand it is difficult to control in the present experiment, but doesn't a larger pupil also imply stronger visual input? Would this be able to explain the largely linear link between pupil size and brain activity in the β and γ ranges?
