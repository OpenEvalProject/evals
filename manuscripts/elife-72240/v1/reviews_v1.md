# Peer review - Round 1

Editors:
- Timothy D Griffiths, University of Newcastle United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72240.sa0](https://doi.org/10.7554/eLife.72240.sa0)

The work demonstrates specific neurophysiological cortical mechanisms for offset responses that are interesting in themselves. Two referees highlighted issues with the behavioural experiments that have been addressed in the revision. Reviewer #2 makes another minor suggestion that he authors might consider before publication of the final version.


---

# Peer review - Round 1

Editors:
- Timothy D Griffiths, University of Newcastle United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72240.sa1](https://doi.org/10.7554/eLife.72240.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Emergence and function of cortical offset responses in sound termination detection" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Timothy D Griffiths as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

We are sorry to say that, after consultation with the reviewers, we have decided that your work will not be considered further for publication by eLife.

The referees found the work very interesting. The neurophysiological data are excellent, but issues are raised with respect to the behavioral data. After discussion the referees all concur that these require further experiments and could not be addressed on the basis of the current data. For this reason, we have recommended rejection of the manuscript. We would be pleased to consider a resubmission that incorporated the additional data suggested.

Reviewer #1:

There has been a great deal of recent interest in the neural basis for offset responses given their hypothesised importance to perception. The possible behavioural relevance to cues like sound duration and gap duration has been taken as a self-evident truth in some work. I found this work attractive in actually testing the relevance of offset responses to duration perception in a mouse model in addition to examining the brain basis. The work is thorough and well executed. The work demonstrates offset responses that occurs for the first time in auditory cortex distinct from A1 where prevention of offsets by activating cells causes worsening of behavioural performance.

1. I think an initial concern in discussion of this manuscript about artefactual effects of spectral splatter due to abrupt sound termination have been addressed in this version of the manuscript.

2. The data appear to support a specialisation for offset response in AAF but have offset responses and their behavioural relevance been examined in A1? The analysis in figure 4 convincingly demonstrates changes in offset responses between MGB and AAF (which is monosynaptic connection) but it would be interesting to know about A1. I appreciate there is s strong prior related to AAF based on previous work but the offset responses being in AAF has been almost taken as a given in manuscript.

Reviewer #2:

In this study, the authors examine: (1) whether offset responses, where neurons respond upon termination of a stimulus, are behaviorally relevant; (2) whether offset responses are merely inherited from subcortical stations or are generated and amplified in cortex; and (3) whether offset responses simply encode sound termination or if they carry stimulus identity information as well. They show, using a combination of optogenetics and behavior, that suppressing offset responses in auditory field AAF results in an impairment of sound termination detection. They then show, using single- and multi-unit recordings, that the behavioral choice of the animal can be decoded on a trial-by-trial basis from the offset and late response phases. Finally, using antidromic stimulation and using multiple stimuli, the authors show that AAF offset responses are not wholly inherited from the auditory thalamus.

The electrophysiological elements of the study seem solid and well-performed. Some weaknesses of the study include the effectiveness of task acquisition by the behavioral subjects, and behavioral analyses that discard trials with potentially useful information. Some statistical tests may not be appropriate and brings into question the results of the decoding analysis. Very recent and highly relevant publications are not discussed in the study. Additional control analyses would strengthen the manuscript.

1. Two very recent studies address questions that are central to this manuscript. First, Li H et al. (Cell Reports, 2021, 35:109003) show using optogenetic manipulations in primary auditory cortex (A1) that A1 OFF activity is required for the perception of sound duration. These results must be discussed in the context of the authors claim that AAF might be specialized for the detection of offset responses.

2. Second, Bondanelli et al. (Elife, 2021, 10:e53151) argue for a role of recurrent A1 connectivity in shaping offset responses in cortex, including the fact that the offset response carries information about stimulus type. These results should be discussed in the context of the authors observations as well.

3. Regarding behavior: the authors discard trials from analyses when the animal licked while the tone was ongoing, and this appears problematic. From the description in the methods, it is unknown what fraction of total trials were discarded from analyses. These trials could be coded as false alarms, and when this information is included in the analysis by using a metric such as the sensitivity index (d’), could provide a complete picture of the behavior.

Considering 30% correct trials as ‘trained’ seems well below traditionally accepted metrics of when a animal is considered trained, especially for a relatively simple detection task. Usually, this number is closer to 70% correct – for example, in the Li et al. 2021 paper mentioned above, mice were considered trained after reaching 90% correct trials on a sound duration discrimination task. Better yet, a d-prime of 1 or 1.5 when false alarms are also considered is a more sensitive metric of behavior (for example, see Caras and Sanes, J. Neurosci 2015).

4. In decoding of performance from activity, given that the reward window opens at offset and is open for only 1 s, the inclusion of the ‘late’ phase is problematic unless it can be shown that licks do not occur within 0.5 s of sound offset. This bump for the hits could result from multiple effects – movement, reward, licking sounds etc. The data supporting the claim of better decoding from offset responses hinges on Figure 3c, where offset responses yield greater accuracy than onset responses. However, pairwise Wilcoxon tests do not seem appropriate for these data where multiple comparisons are being made. The authors should use an ANOVA or Kruskal-Wallis test followed by by multiple-comparisons corrected posthoc tests.

5. From Figure 1E, it appears that the post-inhibitory rebound in other cells in the laser on condition has a similar magnitude to the offset response in the laser off condition. Could the rebound be driving AAF responses that signal an offset, albeit delayed by about 0.2 s, that the animals could be using to detect sound termination? To answer this question, could the authors analyze both the neurophysiological data, as well as determine if the correct responses in the laser ON condition have longer latencies consistent with this 0.2 s delay?

6. If the authors have the data available, it would be great to see a similar control as shown in Figure 2j-m for the longer ramp duration as well in Figure 1. More detail in the methods section as to how the fiber was placed over AAF (in craniotomy but above dura?), whether it was optically shielded to prevent visual cues etc. would be helpful.

7. For the onset-offset neurons that do not have a sustained response profile, it is clear that the highly correlated offset is an important distinguishing cue – it provides a high-SNR signal between the offset response and the previous silent period (when the tone is on). But what if (as for the white noise stimuli, Figure 7b) some amount of sustained activity is present? Is offset-detection behavior worse, and is decoding accuracy using the classifier also worse? If behavioral data is not available, could additional analyses be performed to predict sound termination time for pure tones and white noise, and make a prediction as to what would happen behaviorally?

Reviewer #3:

The goal of this study was to assess the function of cortical offset responses of the anterior auditory field (AAF) in sound perception. The authors used a combination of behavioral, electrophysiological and optogenetic techniques to study the properties of cortical offset responses. Through behavioral experiments combined with optogenetics, the authors first claim to find that inhibiting offset responses in the AAF decrease the mouse’s ability to detect when a sound ends. Furthermore, they report that larger offset responses correlate with an increase in the mouse’s ability to detect sound termination. Functionally, the authors demonstrate via electrophysiological experiments that cortical offset responses have a component that is generated in the AAF and therefore not only inherited from the periphery. The authors also find that offset responses increase with sounds that have longer duration and therefore do not simply encode for silence. The electrophysiological investigation of the properties of cortical offset responses is well designed and the conclusions are justified by the data. However, several questions about the behavioral paradigm arose that warrant further control experiments and re-examining interpretation.

1) The behavioral paradigm suffers from a design in which it is difficult to estimate the false alarm rate. Therefore, it is unclear whether the mouse is trained to lick in response to tone offsets, or rather to reduce licking during the sound presentation. The criterion for “fully trained” is set at 30% hit rate, well below chance (Figure 1b), which seems somewhat low. It is unclear what the mouse licking is reporting.

2) This interpretation of behavioral performance is complicated by the high rate at which mice licked during the trials (Figure S1). (Is the legend for figure S1 correct?) Since the authors report that “Trials with licks at the tone onset were discarded from the analysis (Figure S1)”, question arises whether 60% of the trials were excluded for some mice. In that case, is the lick rate on the trials that were kept simply by chance?

3) The optogenetic manipulation of AAF during behavior drives a relatively small (20%) reduction in performance (Figure 1h and Figure 2i). It is therefore unclear that the conclusion that AAF is necessary for sound offset detection is supported by the data. The behavioral + optogenetic paradigm should be better described in methods, allowing to better assess the presentation of the laser (see point 8).

4) The reduction in performance may be due to general laser presentation and not specific to sound offset. It would be useful to present the laser during the sound or at different points in the stimulus to better understand how its presentation relates to offset responses specifically (Figure 1 and Figure 2).

5) It would be helpful to present more details about how the classifier was trained and tested (Figure 3). The neuronal classifier also does not seem to predict accurately behavior as the accuracy for the offset responses is at ~65 % (Figure 3c). It is furthermore interesting that much of behavior can be explained based on spontaneous neuronal activity, and therefore an alternative interpretation would be that cortical state (or another factor that accounts for differences in spontaneous activity between trials). This also suggests that a control as suggested in point 4 (laser presented at different time points in the stimulus) would be useful, as the classifier would predict significant reduction in performance based on suppression of activity prior to sound, and not at sound offset.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Emergence and function of cortical offset responses in sound termination detection” for further consideration by eLife. Your revised article has been evaluated by Barbara Shinn-Cunningham (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. eLife makes great efforts to avoid multiple cycles of revision but referee #2 and referee #3 raise further important points in their reviews about the behavioural data that need to be addressed.

Reviewer #2:

I appreciate the authors’ detailed responses to the concerns arising from the earlier review of this manuscript. There are no major concerns with the electrophysiology part of the revised manuscript.

Behavior: My concerns with behavioral experiments and what the mice are actually reporting in the task remain.

1) I respectfully disagree with the authors’ statement that false alarm rates cannot be calculated for detection tasks. The term ‘False Alarm’ is derived from signal detection theory, where the subject reports that a signal was present when a signal was not actually present. In this case, the signal is the offset. If a mouse reports an offset by licking during the sound (when an offset, i.e. the signal, was not present), that outcome should be a false alarm. In the authors’ task design, only correct rejections cannot be specified (to do so, one would have to define a trial duration independent of sound termination time. If the mouse withholds licking for the trial duration while the sound has not actually terminated, it would be a correct rejection). I agree with the authors that if the mouse starts licking before even the sound onset, those trials should be discarded.

2) “Likewise, unlike in a discrimination task, a hit rate of 50% is not a chance level in a detection task.”

– It is not a question of what the chance level was, but rather a question of whether the mouse was reliably detecting the offset. P(Hit) + p(FA) + p(Miss) + p(CR) = 1, and a measure of performance would take into account the ratio of desirable (p(Hit)+p(CR)) and undesirable (p(FA)+p(Miss)) outcomes. To illustrate, in Figure S2 panel h, I count 50 trials, with n(Hit) = 23, n(Miss) = 11, nFA = 16, and n(CR) = 0. In this counting, the number of desirable outcomes (23+0=23) is lesser than the number of undesirable outcomes (11+16 = 27) and would result in a d’ = z(Hits) – z(FA) = 0.37. However, if trials in which animals licked during the sound (which I coded as FA) are dropped, then n(Total) = 50-16 = 34, with n(Hits) = 23 (23/34 = 67%). This is why dropping the onset lick trials and considering 30% hits as reaching criterion for training is not convincing.

Other metrics to better capture the behavior might be a discrimination index as used in, for example, Schwartz and David, 2018. Here the cumulative lick probability can be used to calculate ROC curves.

3) Page 5, lines 121 and 125: The authors use a very similar effect size change in hit rate for PV-Cre animals (4.5 +/- 2%) and for wild type animals (4.4 +/- 2.4%) to make the claim that there was a significant change in hit rate (p = 0.0264) for PV-cre animals, but no change (p=0.058) for the wild type animals (Figures 1H and 1L). The appropriate comparison in this case would be between 1H and 1L. (similar analysis must be performed comparing Figure 2I and 2M). It would be instructive if the authors could plot the Laser OFF and ON hit rates separately for the two groups (PV-Cre and wild type animals) so that one can also appreciate if there are overall differences in performance levels.

Additionally, the sizes of the error bars in Figure 1H and 1L are inconsistent with the numbers reported (why does 1H have the larger error bars despite the smaller value of 2% reported in main text)?

Citing recent literature:

I appreciate the authors’ inclusion of two recent studies in the Discussion section. However, these studies also affect the framing of the manuscript in the introduction section.

Page 2, line 39: “De-novo generation or amplification of offset responses in these areas have not been demonstrated yet.” – Please rephrase and appropriately cite the Bondanelli 2021 study here.

Page 2, lines 42 – 52: In this paragraph discussing the perceptual significance of offset responses, please appropriately discuss the Li 2021 study. Please rephrase the last sentence of this paragraph.

Page 4, line 86: Please rephrase “Changing the neuronal activity of sound offset responses without changing any other parameters of the sound response has not been tested” in light of the Li 2021 study.

Decoding analysis:

The classifier accuracy is not significantly different between the offset and onset windows, which suggests that onset responses can be as predictive of the mouse’s offset detection behavior as offset responses. Could the authors please discuss?

Reviewer #3:

The paper represents an innovative and comprehensive body of work aimed to assess the function of cortical offset responses in the anterior auditory field in sound perception. Whereas the majority of work to date in auditory neuroscience has focused on the sound onset responses (largely due to the quick adaptation of cortical responses), the offset responses, which are present in the cortex, and especially, as the authors show, in AAF, have received less attention. The offset responses can play an important role in sound segregation and auditory scene analysis. The authors used a combination of behavioral, electrophysiological and optogenetic techniques to study the properties of cortical offset responses. The authors first test whether and how offset responses correlate and affect behavioral detection of sound offsets. They find that suppressing offset responses in AAF reduces the responses of mice to sound offsets and that there is a significant correlation between cortical responses and behavioral report. The authors next use elegant electrophysiological and manipulation methods to find that cortical offset responses have a component that is generated in the AAF and therefore not only inherited from the periphery. The authors also find that offset responses increase with sounds that have longer duration and therefore do not simply encode for silence. Behaviorally, authors provide evidence for a role of cortical offset responses in sound termination perception. Such an extensive description of these types of responses provides for a substantial advance in our understanding of cortical function.

The authors have conducted additional experiments and analysis and the revised manuscript is much improved. We have only 1 outstanding concern.

Responses to 1+2: We believe that it is important to consider not only the hit rate, but also other signal detection measures in interpreting mouse behavior. In fact, trials on which the mouse licked during sound may be informative, and I am not sure it’s warranted to not include information about them in the analysis. One possible approach would be to compute signal detection theory measures of HR (hit rate), CR (correct rejects), M (misses rate) and FA (false alarm rate), from which one can compute d’ using standard approaches.

– Consider only the trials in which the sound is presented for either 1 s or 2 s.

– To compute hits, compute the percent of 1s-long trials, in which the mouse licked between 1s and 2 s (during the reward window).

– To compute misses, compute the percent of 1s-long trials, in which the mouse did not lick between 1s and 2 s (during the reward window).

– To compute FA, compute the percent of 2s-long trials, in which the mouse licked between 1s and 2s (during the last 1s of sound).

– To compute CR, compute the percent of 2s-long trials, in which the mouse did not lick between 1s and 2s (during the last 1s of sound).

Response to 10. Please use <= 2 significant digits for p values (e.g. p = 0.5655 should be reported as p=0.57 on line 415).
