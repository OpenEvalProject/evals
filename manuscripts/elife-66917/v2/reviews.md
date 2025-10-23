# Peer review - Round 1

Editors:
- Caleb Kemere, Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66917.sa1](https://doi.org/10.7554/eLife.66917.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper represents a valuable new tool for detecting and quantifying sequential structure in neural activity. Spontaneously generated sequences (a.k.a. "replay") is thought to be an important way for the brain to make efficient use of experience, facilitating learning and consolidation of information. Replay has been studied in the rodent hippocampus for decades, but it has recently become possible to detect such activity in human MEG (and perhaps even fMRI) data, generating much current excitement and promise in bringing together these fields. The approach of this work enables investigators to assess the overall level of replay present in a dataset (rather than locating individual events). In particular, a strength of the general linear modeling framework is that both the primary hypothesis "is replay prevalent in this data set?" and secondary hypotheses (e.g., "is there more of one type of replay than another?", "does replay strength change over time?") can be assessed.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Measuring Sequences of Representations with Temporally Delayed Linear Modelling" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Matthijs van der Meer (Reviewer #2), and Caleb Kemere (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that we have decided to reject the paper in its current form.

The reviewers all felt that the work is extremely valuable; a domain-general replay detection method would be of wide interest and utility. However, we felt that the paper was lacking context and comparisons to existing methods. Most critically, the paper would be more impactful if comparisons with standard replay methods were included, and the reviewers felt that would be too substantial a change to ask for as a revision. There were also concerns about lack of detail in the description of the methods and data that diminished enthusiasm. The authors would be welcome to make changes along these lines and submit the paper again as a new submission.

Reviewer #1:

This paper describes temporal delayed linear modelling (TDLM), a method for detecting sequential replay during awake rest periods in human neuroimaging data. The method involves first training a classifier to decode states from labeled data, then building linear models that quantify the extent to which one state predicts the next expected state at particular lags, and finally assessing reliability by running the analysis with permuted labels.

This method has already been fruitfully used in prior empirical papers by the authors, and this paper serves to present the details of the method and code such that others may make use of it. Based on existing findings, the method seems extremely promising, with potential for widespread interest and adoption in the human neuroimaging community. The paper would benefit, however, from more discussion of the scope of the applicability of the method and its relationship to methods already available in the rodent and (to a lesser extent) human literature.

1. TDLM is presented as a general tool for detecting replay, with special utility for non-invasive human neuroimaging modalities. The method is tested mainly on MEG data, with one additional demonstration in rodent electrophysiology. Should researchers expect to be able to apply the method directly to EEG or fMRI data? If not, what considerations or modifications would be involved?

2. How does the method relate to the state of the art methods for detecting replay in electrophysiology data? What precludes using those methods in MEG data or other noninvasive modalities? And conversely, do the authors believe animal replay researchers would benefit from adopting the proposed method?

3. It would be useful for the authors to comment on the applicability of the method to sleep data, especially as rodent replay decoding methods are routinely used during both awake rest and sleep.

4. How does the method relate to the Wittkuhn and Schuck fMRI replay detection method? What might be the advantages and disadvantages of each?

5. The authors make the point that spatial correlation as well as anti-correlation between state patterns reduces the ability to detect sequences. The x axis for Figure 3c begins at zero, demonstrating that lower positive correlation is better than higher positive correlation. Given the common practice of building one classifier to decode multiple states (as opposed to a separate classifier for each state), it would be very useful to provide a demonstration that the relationship in Figure 3c flips (more correlation is better for sequenceness) when spatial correlations are in the negative range.

6. In the Results, the authors specify using a single time point for spatial patterns, which would seem to be a potentially very noisy estimate. In the Methods, they explain that the data were downsampled from 600 to 100 Hz to improve SNR. It seems likely that downsampling or some other method of increasing SNR will be important for the use of single time point estimates. It would be useful for the authors to comment on this and provide recommendations in the Results section.

7. While the demonstration that the method works for detecting theta sequences in navigating rodents is very useful, the paper is missing the more basic demonstration that it works for simple replay during awake rest in rodents. This would be important to include to the extent that the authors believe the method will be of use in comparing replay between species.

8. The authors explain that they "had one condition where we measured resting activity before the subjects saw any stimuli. Therefore, by definition these stimuli could not replay, but we can use the classifiers from these stimuli (measured later) to test the false positive performance of statistical tests on replay." My understanding of the rodent preplay literature is that you might indeed expect meaningful "replay" prior to stimulus exposure, as existing sequential dynamics may be co-opted to represent subsequent stimulus sequences. It may therefore be tricky to assume no sequenceness prior to stimulus exposure.

Reviewer #2:

This paper addresses the important overall issue of how to detect and quantify sequential structure in neural activity. Such sequences have been studied in the rodent hippocampus for decades, but it has recently become possible to detect them in human MEG (and perhaps even fMRI) data, generating much current excitement and promise in bringing together these fields.

In this paper, the authors examine and develop in more detail the method previously published in their ground-breaking MEG paper (Liu et al. 2019). The authors demonstrate that by aiming their method at the level of decoded neural data (rather than the sensor-level data) it can be applied to a wide range of data types and settings, such as rodent ephys data, stimulating cross-fertilization. This generality is a strength and distinguishes this work from the typically ad hoc (study-specific) methods that are the norm; this paper could be a first step towards a more domain-general sequence detection method. A further strength is that the general linear modeling framework lends itself well to regressing out potential confounds such as autocorrelations, as the authors show.

However, enthusiasm for the paper is limited by several overall issues:

1. It seems a major claim is that the current method is somehow superior to other methods (e.g. from the abstract: "designed to take care of confounds" implying that other methods do not do this, and "maximize sequence detection ability" implying that other methods are less effective at detection). But there is very little actual comparison with other methods made to substantiate this claim, particularly for sequences of more than two states which have been extensively used in the rodent replay literature (see Tingley and Peyrache, Proc Royal Soc B 2020 for a recent review of the rodent methods; different shuffling procedures are applied to identify sequenceness, see e.g. Farooq et al. Neuron 2019 and Foster, Ann Rev Neurosci 2017). The authors should compare their method to some others in order to support these claims, or at a minimum discuss how their method relates to/improves upon the state of the art.

2. The scope or generality of the proposed method should be made more explicit in a number of ways. First, it seems the major example is from MEG data with a small number of discrete states; how does the method handle continuous variables and larger state spaces? (The rodent ephys example could potentially address this but not enough detail was provided to understand what was done; see specific comments below.) Second, it appears this method describes sequenceness for a large chunk of data, but cannot tell whether an individual event (such as a hippocampal sharp wave-ripple and associated spiking) forms a sequence not. Third, there is some inconsistency in the terminology regarding scope: are the authors aiming to detect any kind of temporal structure in neural activity (first sentence of "Overview of TDLM" section) which would include oscillations, or only sequences? These are not fatal issues but should be clearly delineated.

3. The inference part of the work is potentially very valuable because this is an area that has been well studied in GLM/multiple regression type problems. However, the authors limit themselves to asking "first-order" sequence questions (i.e. whether observed sequenceness is different from random) when key questions – including whether or not there is evidence of replay – are actually "second-order" questions because they require a comparison of sequenceness across two conditions (e.g. pre-task and post-task; I'm borrowing this terminology from van der Meer et al. Proc Royal Soc B 2020). The authors should address how to make this kind of comparison using their method.

Reviewer #3:

The methods used by the authors seem like potentially really useful tools for research on neural activity related to sequences of stimuli. We were excited to see that a new toolbox might be available for these sorts of problems, which are widespread. The authors touch on a number of interesting scenarios and raise relevant issues related to cross-validation and inference of statistical significance. However, given (1) the paucity of code that they've posted, and its specificity to specific exact data and (2) the large literature on latent variable models combined with surrogate data for significance testing, I would hesitate to call TDLM a "framework". Moreover, in trying to present it in this generic way, the authors have muddled the paper, making it difficult to understand exactly what they are doing.

Overall: This paper presents a novel approach for detecting sequential patterns in neural data however it needs more context. What's the contribution overall? How and why is this analysis technique better than say Bayesian template matching? Why is it so difficult to understand the details of the method?

The first and most important problem with this paper is that it is intended (it appears) to be a more detailed and enhanced retelling of the author's 2019 Cell paper. If this is the case, then it's important that it also be clearer and easier to read and understand than that one was. The authors should follow the normal tradition in computational papers:

1. Present a clear and thorough explanation of one use of the method (i.e., MEG observations with discrete stimuli), then present the next approach (i.e., sequences?) with all the details necessary to understand it.

2. The authors should start each section with a mathematical explanation of the X's – the equation(s) that describes how they are derived from specific data. Much of the discussion of cross validation actually refers to this mapping.

3. Equation 5 also needs a clearer explanation – it would be better to write it as a sum of matrices (because that is clearer) than with the strange "vec" notation. And TAUTO, TF and TR should be described properly – TAUTO is "the identity matrix", TF and TR are "shift matrices, with ones on the first upper and lower off diagonals".

4. The cross validation schemes need a clear description. Preferably using something like a LaTeX "algorithm" box so that they are precisely explained.

Recognizing the need to balance readability for a general reader and interest, perhaps the details could be given for the first few problems, and then for subsequent results, the detail could go into a Methods section. Alternatively, the methods section could be done away with (though some things, such as the MEG data acquisition methods are reasonably in the methods).

Usually, we think about latent variable model problems from a generative perspective. The approach taken in this paper seems to be similar to a Kalman filter with a multinomial observation (which would be equivalent to the logistic regression?), but it's unclear. Making the connection to the extensive literature on dynamical latent variable models would be helpful.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Temporally delayed linear modelling (TDLM) measures replay in both animals and humans" for further consideration by eLife. Your revised article has been reviewed by 3 reviewers and the evaluation has been overseen by Laura Colgin as the Senior Editor, and a Reviewing Editor.

While impressed by the novelty and potential utility of the method, the reviewers had a specific critical concern. Namely, do high sequenceness scores truly capture activation of patterns that widely span the specified sequence space (i.e., many complete "ABCDE" sequences) or only a collection of pairwise correlations (i.e., "AB", "DE", "BC")? Presenting more examples from experimental data that demonstrate the former was perceived as critical to demonstrate the utility of TDLM as an approach for "replay detection". Ultimately, the reviewers reached a consensus that in the current presentation, what TLDM actually detects remains opaque, and the impact of the work is diminished. We considered requesting an action plan, but upon reflection, I think that the main issue is one of semantics. However, if you wish to describe TDLM as a method for detecting "replay", it needs to be critically addressed.

In addition to the reviews below, in our discussion, one reviewer noted: "even though they now explain in more detail what they did to analyze theta sequences, the result (~12 Hz) is still seemingly at odds with the ~8-9 Hz repetition one would expect from the literature. I'm actually not sure this adds a whole lot to the paper so I think it would be better to just take this part out."

Reviewer #1:

Overall, I find great value in the effort to provide researchers working with very different animal models and datasets a similar toolkit to apply and analyze reactivation and replay. But I also have significant concerns about the potential for these methods, if poorly understood and applied, to further confound the field. Fully understanding this paper and the described methods and its caveats is not easy for most experimentalists, yours truly included. I am concerned that investigators will misapply these tools and claim significant replay in instances where there is none. These concerns may be addressable by better diagnostics and related guidance for interpretation.

Nevertheless, an important caveat in the work is that it does not detect "replay" per se, but rather temporal biases in decoded activity. Thus I think the title should be amended. In some places, the authors describe this as "sequenceness", or "temporal delays" which are both preferable to "replay". Prior work (e.g. Skaggs and McNaughton) used a similar measure, but referred to it as "temporal bias". While this temporal bias is certainly related to replay and sequences, it is only an indirect measure of these, and more akin to "reactivation", as it's largely pairwise analyses. Clarity on such issues is particularly important in this area given the excessive ambiguity in terminology for the replay and reactivation phenomena.

My other major concern is that the analysis is rather opaque in an area where there is much need for transparency, especially considering the existing debates and controversy surrounding appropriate methodology and conclusions that can be drawn from it. For example, in most of the figures that the authors provide, it's unclear whether the sequenceness score is driven by one particular pair of stimuli, or equally so among most possible pairs. Perhaps a transition graph could be composed from the data, but I did not find this except in cartoon diagrams. I think it would be important for the authors to provide guidance regarding these details. A related question is whether these biased pairs typically appear in isolation, or as part of larger multi-item events? It's not clear if there is a straightforward way to extract this important information. Some sample events could be shown, but examples can also be cherry-picked and non-representative. Probably a histogram of sequence bout lengths would be valuable.

Part of the claimed value in these methods is their possible application to spike trains, e.g. from rodents, particularly for detecting and describing individual events. The authors claim that this is possible. However, while they analyze two rodent datasets in different parts, they do not apply it to any real data, but only on rather contrived (low noise) simulated data. This raises the concern that TDLM is not sufficiently sensitive for detecting individual events. The theta sequence analysis results shown in Supplementary Figure 3d are also concerning to me. They show a very noisy signal that passes threshold in one particular bin. If such a figure were a major result in a new manuscript, and the current eLife manuscript was cited as validation for the methods, would reviewers be obliged to accept it for publication? If not, what additional criterion or diagnostic steps would be recommended?

Comments for the authors:

P2, Line 32: "and" seems misplaced.

P2, Line 34: "periods of activity".

P3, Line 4: perhaps "single neuron" rather than "cellular".

P4, Lines 34-35: it is not clear here what the authors mean by "over and above variance that can be explained by other states at the same time." It gets more clear later in page 11, section "Moving to multiple linear regression". The authors might consider either referring to that section at the end of the sentence or removing the unnecessary details that might confuse the reader at this juncture.

P5, Line 31: This sentence is a bit confusing. It is not clear what "in which" refers to. It might be better to start a new sentence for describing Zf and Zb.

P6, Lines 7-8: The authors might refer to the section "Correcting for multiple comparisons" on page 16, where more details are provided.

P8, Lines 42-46: the description of abstraction may benefit from additional background and exposition.

P9, Line 18-24, I found this entire paragraph very confusing.

P10, Line 7: "that share the same abstract representation" is redundant.

P10, Line 12: "tested" should be corrected to test it.

P10, Lines 23-24: Confusing sentence with multiple "whiches".

P12, Line 24: Is it possible for the auto-correlation structure of Xi(t) to generate false positives for Xj(t+dt), or would this necessarily be entirely accounted for by Xj(t)?

P13, Lines 23-24: How the regularization (penalizing for the norm of W) is supposed to make the model "trained on stimulus-evoked data" generalize better to off-task/rest data? The authors might add a sentence or two at the end of the paragraph to make the aim more clear and motivate the next paragraphs in the section. Based on the descriptions in the first paragraph of Page 14, the regularization seems to add more sparsity to the estimated W that minimizes spatial correlations between the states, etc. Something similar to these descriptions could be used here.

P13, Line 28: It is not exactly clear what authors mean by "the prior term"? Does it refer to the equation before adding any regularization or to some prior probability distribution over W? I think in this context, we should be cautious with using the words like prior, posterior, etc.

P16, Line 30, extra "as".

P17, section "Considerations on second-order inferences". It seems that this section should be placed later in the manuscript, in the section "TDLM FOR RODENT REPLAY".

P23 Line 39, missing "that".

Supplementary Note 5: what shuffle was used?

Reviewer #2:

This paper addresses the important overall issue of how to detect and quantify sequential structure in neural activity. Spontaneously generated sequences (a.k.a. "replay") is thought to be an important way for the brain to make efficient use of experience, facilitating learning and consolidation of information. Replay has been studied in the rodent hippocampus for decades, but it has recently become possible to detect such activity in human MEG (and perhaps even fMRI) data, generating much current excitement and promise in bringing together these fields.

However, comparison and cross-fertilization between different replay studies – even within the same species, let alone across species – has been hampered by a fragmented landscape of different analysis methods, which are often ad-hoc and task-specific. In this study, the authors develop and extend the method previously published in their groundbreaking MEG paper (Liu et al. 2019), notably demonstrating that by aiming their method at the level of decoded neural data (rather than the sensor-level data) it can be applied to a wide range of data types and settings, including human MEG, EEG, and rodent ephys data. A further strength is that the general linear modeling framework lends itself well to regressing out potential confounds and formally testing second-order questions such as whether tthere is more forward vs. reverse replay, or if replay strength changes with time.

In this revised submission, the authors have made several major additions to the manuscript, including a substantive analysis of rodent replay data, and associated multi-scale extension of the method to make it suitable for continuous state spaces. This addition is an important component of the paper, in that it demonstrates the generality of a framework that can be applied to different kinds of data and task state spaces across species. Another much appreciated change is the expanded and much more clear explanations throughout, such as those of the TDLM method itself and of the data analysis pipelines for the various kinds of data. With these additions, I think the paper really makes good on the promise of a domain-general method for the detection of sequences in spontaneous neural activity, and provides a timely impetus to the study of replay across tasks and species.

There is one important area that the paper still falls short on, but that should be straightforward to address with some simple additional analysis and discussion. A distinctive strength of the GLM framework is that it easily accommodates testing important and ubiquitous "second-order" questions, such as whether there is more forward than reverse replay, is replay strength changing over time, and so on. However, the message in the current version that one could simply subtract sequenceness scores doesn't address how one would formally test for a difference, or test for some factor like time being important. For forward vs. reverse, because this is fit to the same data, this is a comparison between different betas in the second-level GLM (Figure 1f). I am not a statistician, but my textbooks say there are a few ways of doing this, for instance z = (βfwd – βrev) / σ_(βfwd – βrev) where the crucial variance term can be estimated as the sqrt(σ(βfwd)2 + σ(βrev)2), matching the intuition that a formal test requires an estimate of variance of the difference between the betas, not just the means.

For early vs. late sleep, things are more complicated because you are not comparing models/betas fit to the same data. I suppose the above approach could also work as long as all the betas are standardized, but wouldn't a better test be to include time as a regressor in the second-level GLM and formally test for an interaction between time and Tfwd (and Tbwd)?

In either case, there are two important points to make to demonstrate the utility of the GLM framework for sequence analysis: (1) these ubiquitous second-order inference questions require a bit more consideration than just saying you can subtract the sequenceness scores; there is another level of statistical inference here, and (2) the TDLM framework, unlike many other approaches, is in fact very well suited to doing just that – it benefits from the existing machinery of linear statistical modeling and associated model comparison tools to make such comparisons.

These points are not currently clear from the "Considerations on second-order inferences" section. If in addition the GLM framework allows for the regressing out of some potential confounds that can come up in rodent data that the authors now reference that's an additional benefit but not the main point I am asking the authors to speak to.

Reviewer #3:

This revised manuscript describes a method for detecting "offline replay" events in human and animal electrophysiology. I have found the TDLM method described in the manuscript to be very valuable for the field. Its detailed description in the present manuscript will be very useful, first because it presents its different components very clearly and in detail – something which is not possible in a manuscript focused on a particular finding obtained using this method. Second, the authors show that this method can be applied not only to human MEG data, but also to rodent electrophysiology data.

I found the manuscript to be well written: it describes clearly and adequately the different analytic steps that have to be applied to avoid confounds arising from known features of electrophysiological signals (autocorrelations, oscillations), and from task features themselves. The fact that they show results obtained using their method from simulated and real data is also a strength of the manuscript. The level of computational detail regarding the equations appears adequate and well balanced for a broad readership, and example code using the method has been posted online.

I have not reviewed the original version of the manuscript, but have first read the revised manuscript before consulting the initial reviews and the responses provided by the authors.

The authors' responses to the initial reviews are extensive and insightful. I wonder how much the presentation of replay detection in EEG data from a single subject is particularly convincing, but nevertheless I agree with the authors that it shows that their method indeed can work using EEG data instead of MEG data.

The authors' extensive response regarding the comparison between their method and other state-of-the-art methods for detecting replay events in electrophysiology data was very clear and useful. The revised manuscript adequately includes a full section on the use of their method for rodent electrophysiology data. The authors also discuss their method in light of other efforts, from Wittkuhn and Schuck using fMRI data for example.

Regarding the more important reservations of Reviewer #2, I found that the authors provided adequate and convincing responses to each of them. Regarding the concerns of Reviewer #3, I found that the revised manuscript allowed understanding the method quite clearly relative to my limited understanding of the details of the method after reading recent empirical papers from the authors (e.g., Liu et al., 2019, Cell). The fact that the authors have posted code online on GitHub is also very useful, and I find that the level of detail regarding the equations is sufficient (and well balanced) for the broad readership of a journal like eLife.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Temporally delayed linear modelling (TDLM) measures replay in both animals and humans" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin as the Senior Editor, and a Reviewing Editor.

We shared the revised manuscript with the reviewers. After some discussion, it was concluded that the manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The reviewers were confused by the data in Figure 7e. We finally concluded that it was an attempt to explain how the regression was formed, but it took lots of back and forth. Given that this is a tools paper, there seems to be no reason why each analysis figure can't be backed with equations that identify the regressions being done, and the variables being regressed.

2. Figure 5 appears to be about analyzing the MEG data when events are detected. (Isn't TDLM an approach for measuring sequenceness over a population of events rather than finding single ones?) Even though this is previously published work, the methods need significant expansion (see Point 1). The text refers to a section that appears to be missing? Here's the text: "We want to identify the time when a given sequence is very likely to unfold. We achieve this, by transforming from the space of states to the space of sequence events. This is the same computation as in the section "States as sequence events". " (Search for "sequence events" yields no results.) Perhaps this refers to Appendix 3, but the text there doesn't really help much.

3. One reviewer had previously asked "in most of the figures that the authors provide, it's unclear whether the sequenceness score is driven by one particular pair of stimuli, or equally so among most possible pairs". To clarify, it seems that the question is: if the model proposed is A→B→C→D, and the data are largely A→B, can that be detected? Or alternatively, can you give a proper way of comparing two models (in this case, A→B→C→D vs A→B)?
