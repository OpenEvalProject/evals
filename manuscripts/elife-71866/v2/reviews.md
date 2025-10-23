# Peer review - Round 1

Editors:
- Xiang Yu, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71866.sa0](https://doi.org/10.7554/eLife.71866.sa0)

Autism spectrum disorder is characterized by social, communicative and sensory anomalies. This study uses behavioral psychophysics experiments and computational modelling to interrogate how individuals with autism combine sensory cues in multisensory tasks. The results showed that individuals with autism were more likely to integrate cues, but less likely to report doing so, thus raising interesting questions regarding how individuals with autism perceive the world.


---

# Peer review - Round 1

Editors:
- Xiang Yu, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71866.sa1](https://doi.org/10.7554/eLife.71866.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Aberrant causal inference and presence of a compensatory mechanism in Autism Spectrum Disorder" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ulrik Beierholm (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The experiments report interesting results regarding audio-visual integration for spatial discriminations in both typical individuals and individuals with ASD. However, the conceptual framing (including the model) is one of several potential accounts of these data, and should be framed as such. Alternative accounts need to be presented and seriously discussed, and not just as an extension of the Discussion. The abstract and other parts of the manuscript also need to be adjusted accordingly.

2) Related to point 1. Prominent aspects of the data, including higher overall bias in autism in Figure 2, are not captured in the model in Figure 4. The dissociation between explicit and implicit is not convincing, and the stress on group differences puts an emphasis on small effects. Please revise model and/or Discussion to address these concerns.

3) Model fitting is not described sufficiently. How were the sensory parameters fitted? It seems that more than 20 parameters were fitted (Supp. File 1) for the aggregate subject through the slice sampling, is that correct? Was this also done for individual subjects? What was done to ensure convergence? Was any model comparison done? Please include a list or figure showing the different steps of the model fitting.

4) The model may be over-specified with both a lapse rate and a lapse bias. Please test a simpler model without lapse bias or explain why that was not done.

5) In experiments 3 and 4 please detail the specific instructions given. Specifically, were participants asked to press a button if they thought both cues come from the same source, or if they thought that the 2 cues come from 2 sources? Since there was not a default option (an "I don't know option"), it's important to know the default – determined by the way the question was phrased.

6) The participants in each experiment were not clearly described. Please provide more details about the task completion of participants, such as how many completed all four tasks, etc. A table would be helpful. Specifically, what were the performance scores in Experiment 1 – of the sub-group of participants of Experiment 2 – the question of whether the psychometric plots did not differ between ASD and controls participating in this study is crucial for estimating whether they were expected to have different magnitudes of bias (as they actually did). The authors did not address the question of the overall bias magnitude, only the values at the large disparities.

7) Please specify the criteria for the ASD diagnosis, DSM-5 or DSM-4? Are they classic autism or Asperger or PDD-NOS subjects? Were the gold standard ADOS ADIR performed to confirm the diagnosis? If not, the authors should acknowledge this as a limitation in Discussion.

8) More detailed research participant description is required. SCQ and AQ were performed for all participants. Were there ASD individuals below the cut-off of these two scales? or any TD participants above the cut-off? This information should be stated. The authors should consider excluding the ASD individuals below the cut-offs and TD individuals above the cut-offs from data analysis. Please provide more details about how the TD participants were recruited. IQ was available for a subset of the ASD participants: How many of them have IQ scores? IQ was measured using what test? Was the IQ measured for the TD group?

9) Please report effect sizes, e.g. eta2 or Cohen's d.

Reviewer #1:

Using a series of cue combination tasks, the authors studied the causal inference of multisensory stimuli in people with ASD. The authors found the intact ability in optimal cue combination of participants with ASD but impairment in dissociating audio and visual stimuli when presented with wider spatial disparity. It suggested they persisted with a wrong integration model for causal inference. However, the individuals with ASD explicitly report the common cause of stimuli fewer than the controls. Through formal modeling, the authors found increased prior probability for the common cause in ASD. However, reporting the common cause in ASD is reduced in the explicit task, indicative of a compensatory mechanism via a choice bias.

In general, I think this study was well-designed and the results were interesting. The conclusions of this paper are mostly well supported by data. But I have a few questions that I would like to see the author’s address.

1. When comparing the temporal disparity task to the spatial task, the authors concluded that the overall reduced tendency to report common cause at any disparity and across spatial and temporal conflicts seemingly is the defining characteristic of ASD. However, in Figure 3D, it could tell that a higher proportion of common cause reporting in ASD when absolute temporal disparity became greater, which differed from the case of spatial task and from when the temporal disparity was narrower. Could the conclusion be too general? The authors should tone it down or give more discussion about the incongruence.

2. When fitting the model to individual subject data, the authors found comparable pcombined for the explicit task between ASD and control subjects. This seemed to be contrasted to the result of aggregate data and behavioral results. Did the difference come from the fitting procedure? Did the significant decreased in pcombined was because of the lack of consideration of subject heterogeneity? The authors could provide more explanation or discussion of it.

3. A related question is about the intuition behind the two steps of modeling fitting (i.e., to aggregate and individual data). What more could fitting models to aggregate or individual data provide to one another procedure? The authors should elaborate on it.

4. I would like to see the authors discuss more the interesting finding of a potential compensatory mechanism, particularly the meaning of it in terms of the possible relation to ASD symptoms. For example, how would the increased prior probability of common cause report and the compensatory choice bias contribute to the sensory abnormalities in ASD?

5. The participants in each experiment were not clearly introduced. The authors should provide more details about the task completion of participants, such as how many completed all four tasks, etc. And the data of how many participants who participated in both the implicit and explicit spatial task were included in modeling?

6. The authors could also conduct some correlational analyses between estimated model parameters and symptomatology measures, just as what they have done for psychometric features, to further investigate how autistic symptoms would affect the process of causal inference.

7. Since the data of the individuals with poor performance were also fitted (such as 8 of the individuals with ASD in Experiment 3), it is interesting to see if there is anything special or atypical in terms of their model parameters, even though their data were not included in behavioral analyses.

8. I suggest specifying the criteria for the ASD diagnosis, DSM-5? or DSM-4? or ICD-10? Are they classic autism or Asperger or PDD-NOS? Were the gold standard ADOS ADIR performed to confirm the diagnosis? If not, the authors should acknowledge this as the limitation in Discussion.

9. SCQ and AQ were performed to all participants. My question is: is there any ASD individuals below the cut-off of these two scales? or any TD participants above the cut-off. the authors should consider excluding the ASD individuals below the cut-offs and TD individuals above the cut-offs from the data analysis.

10. Please provide more details about how the TD participants were recruited?

11. IQ was available for a subset of the ASD participants: How many of them have IQ scores? Is there any particular reason that the other ASD participants did not have IQ scores? How the IQ was measured? using Wechesler or Raven's test? Was the IQ measured for the TD group?

12. The authors could provide direct comparisons of thresholds and visual weights between two groups in the result section of Experiment 1.

13. Errors bars in Figure 1E and 1H were not very obvious. The authors could consider using simpler markers, such as "+" (i.e., short lines) for simultaneously displaying horizontal and vertical error bars.

14. It should be "As for the case of auditory disparities, …" instead of " As for the case of spatial disparities, …" for the first sentence of the second paragraph after Figure 3.

Reviewer #2:

The paper consists of 4 interesting experiments examining multisensory processing in autism spectrum disorder. The first experiment shows that participants with ASD perform similar to controls in cross-model integration, a conceptual replication of earlier findings from this group. However, the subsequent experiments reveal some intriguing differences between the groups in terms of how they use explicit and implicit information in evaluating if auditory and visual information comes from a common source or distinct sources. The authors propose a model that aims to explain the seeming dissociation between explicit and implicit reports of the two groups. The strength of this work is that the experiments are very interesting and report interesting results regarding audio-visual integration for spatial discriminations in both typical individuals and people with ASD. The comparison between explicit and implicit reports is very interesting. In terms of weaknesses, the dissociation between explicit and implicit is not convincing, and the stress on group differences puts an emphasis on, at best, marginal effects, which the modelling does not explain. For example, an alternative account that is consistent with all the data presented is that there are individuals with ASD who are somewhat poorer auditory discriminators, resulting in the bias effects and broader disparities. These individuals would be less likely to commit to an explicit "single source" statement in line with their reduced auditory localization skills.

The dissociation between explicit and implicit is not convincing, and the stress on group differences puts an emphasis on, at best, marginal effects, which the modelling does not explain (the strongest linearity on ASD's curve in Figure 2 – is not captured in the modelling in Figure 4) For example, an alternative account that is consistent with all the data presented is that there are individuals with ASD who are somewhat poorer auditory discriminators and they impacted overall performance in Experiment 2, resulting in a larger bias effect, and also somewhat broader in disparities. These individuals would be less likely to commit to an explicit "single source" statement, which is quite committing, in line with their reduced auditory localization skills. The authors should at least address this alternative account, and present auditory discrimination curves of Experiment 2's participants.

The model does not account for the data point of individuals with autism being pulled by a reliable visual blob 24 degrees away, which was the main point in Figure 3.

Overall the authors ignore more prominent aspects of the data (e.g. higher overall bias in autism in Figure 2) for points they want to make (non linearity larger in autism than in controls).

Reliability – is a confusing term. The stimuli are reliably presented, but the information the perceivers derive regarding their position is less reliable when stimuli are small.

Figure 1f, g – I had difficulties understanding. I assume that the dashed lines should be to the right of the solid lines, which is the case for "high-reliability" blob, but why is it switched for the low reliability case? In both sample participants (f and g) and I wonder why the bias is larger (larger distance between dashed and matched solid plot, in both participants) for low versus intermediate size (reliability) blobs. If this is the actual result – it needs explanation.

Figure 2 – the main observation is that the bias in autism is larger. Perhaps this group difference stems from this group being somewhat poorer auditory spatial discriminators than their 15 age-matched controls in the experiment. If their auditory discrimination is poorer we would expect an overall larger bias, and perhaps also across a broader range of audio-visual disparities.

Importantly, this is probable account, since this is a smaller population than in Experiment 1 – and their discrimination thresholds are not addressed. Importantly – I could not figure out the overlap in participation across the various experiments. In experiment 1 matched performance was only obtained when 6 participants with ASD were excluded. In Experiment 3 (24 participants originally) – they also excluded a large subgroup, whose behavior was different. Here the group is initially small so variability across participants was not discussed.

The strongest point for the claim of too broad integration is the bottom left point – where high reliability blob has an effect that even increases when the visual blob is presented 24 degrees apart. This point is hard to reconcile (and is not reconciled by the model proposed in Figure 4 either). The authors should show that it is a reliable data point – perhaps by showing single subject data.

In experiments 3 and 4 the specific instructions are crucial – are participants asked to press a specific button if they are perceived as coming from the same source? Or press a button if they are perceived as coming from 2 separate sources. Here phrasing may have affected the decisions of individuals with autism. In order to dissociate between these 2 options it would have been nice to have a third option "don't know". If participants with autism tend to say to be less decisive they would tend to commit to a single source. This account may be explained by being somewhat implicitly poorer localizers.

If you have discrimination functions of the specific subgroups that took part in Experiments 2-3 (since they all participated in Experiment 1 – right?) – please show them or report discrimination skills for these subgroups, since this is the relevant control-ASD matching.

Re modelling and Figure 4 – It is difficult to follow the model – perhaps label the model parameters in the diagram of Figure 4a.

Reviewer #3:

In this paper Noel et al., use a combination of psychophysical experiment and computational modeling to examine the differences in behaviour between participant on the Autism Spectrum Disorder and control participants when dealing with multi-sensory stimuli (e.g. audio-visual). It is well known that ASD subjects tend to differ in how they combine such stimuli, and it has previously been suggested that this may be due to a difference in the tendency to perform causal inference.

The study indeed finds that while ASD participants had similar ability to combine cues when unambiguously from the same source, they differed in the tendency to combine them when unclear if necessary to combine. In contrast when asked to explicitly indicate whether stimuli originated from the same source (and therefore should be combined) they tended to under report.

While the experiments are in themselves very standard, the paper relies on computational modeling to differentiate the possible behavioural effects, using advanced Bayesian statistical methods.

These results confirm existing ideas, and build on our understanding of ASD, while still leaving many questions unanswered. The results should be of interest to anyone studying ASD as well as any other developmental disorders, and perception in general.

I enjoyed reading this paper, although the model fitting procedure especially was not clear to me. How were the sensory parameters fitted? By my count more than 20 parameters were fitted (Supp. File 1) for the aggregate subject through the slice sampling, is that correct? Was this also done for individual subjects? I would be nervous about fitting that many parameters for individual subject data. What was done to ensure convergence?

Was any model comparison done? Might be better to include a list or figure showing the different steps of the model fitting.

I also worry that the model is over specified with both a lapse rate and a lapse bias. From my understanding the lapse rate specifies when subjects (through lack of concentration or otherwise) fail to take trial stimuli into account and therefore go with their prior. In other studies this prior may be identical to the prior over spatial range, or may be a uniform discrete distribution over the bottoms available for response.

Maybe the variables are constrained in ways that I did not understand, but with just a binary response (Left/Right) the model can largely incorporate any bias to a large set of possible parameter values of lapse rate and bias. I.e. that the model is over specified. That would also explain the wide range of values for the fitted parameters in Figure 3.

I think this should really be investigated before the results can be trusted.

Looking at Figure 4E and F makes me hesitant about trusting the results.

Authors also acknowledge that the lapse bias and P combined are too closely entwined to really be well separated in the explicit temporal experiment. Maybe for that reason it would also be useful to test a simpler model without lapse bias?

I find it mildly confusing that D refers to a Left/Right response in the implicit task, and Common/Separate in the explicit task. Maybe better to use separate symbols? D is fine for 'decision' but in places in the text it is instead referred to as 'trial category' which is vague. I also don't really think D is needed in the generative model in Figure 4 as it is not really causing the subsequent variables C or Sa.

Does eLife not require the reporting of effect sizes (e.g. eta2 or Cohen's d)? It would be good to include these.

The plots in Figure 3 mostly look like shifts up for ASD relative to controls. The authors might want to fit a model with a positive bias, i.e.

a*N(mu,sd2)+b

may fit better (could do model comparison) and just show difference in b. This is just a suggestion though, but it may be cleaner for their argument.

In the Discussion, while divisive normalisation is one way to achieve the marginalisation needed for Bayesian causal inference, there are other ways to achieve it (Cuppino et al., 2017, Yamashita 2013, Yu et al., 2016, Zhang et al., 2019). It would be good to acknowledge this.

Eq 5 and 6, 38 are misleading. Likelihood is a function of Sa/Sv, so would be better to write as l(Sa)=N(Xa;Sa,Sv)

Eq 9: is D either 1 or 2? Or 1 or -1?

Detail: maybe use different symbols for lapse rate and lapse bias? I find λ and odell confusing. How about Plapse for the lapse rate to emphasise that it is a probability? Pcommon is already a fitted variable that is also a probability of a Bernoulli distribution.

Page 5 (pages of the pdf):

“ …ASD did not show impairments in integrating perceptually congruent auditory and visual stimuli.”

– “ …ASD did not show impairments in integrating perceptually congruent (and near-congruent) auditory and visual stimuli.”

In experiment 2 there was a six degree discrepancy, so near-congruent seems appropriate.

Typos:

“We perform the integral in Eq. S5 for the implicit task by”: should this be Eq. 35?

References:

Cuppini, C., Shams, L., Magosso, E. and Ursino, M. A biologically inspired neurocomputational model for audiovisual integration and causal inference. Eur. J. Neurosci. 46, 2481-2498 (2017).

Yamashita, I., Katahira, K., Igarashi, Y., Okanoya, K. and Okada, M. Recurrent network for multisensory integration-identification of common sources of audiovisual stimuli. Front. Comput. Neurosci. 7, (2013).

Yu, Z., Chen, F., Dong, J. and Dai, Q. Sampling-based causal inference in cue combination and its neural implementation. Neurocomputing 175, 155-165 (2016).

Zhang, W., Wu, S., Doiron, B. and Lee, T. S. A Normative Theory for Causal Inference and Bayes Factor Computation in Neural Circuits. Adv. Neural Inf. Process. Syst. 32, 3804-3813 (2019).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Aberrant causal inference and presence of a compensatory mechanism in Autism Spectrum Disorder” for further consideration by eLife. Your revised article has been evaluated by Barbara Shinn-Cunningham (Senior Editor) and a Reviewing Editor.

All reviewers agree that the manuscript has improved significantly during revision, but there are some remaining issues to be addressed, as noted below and described in detail in the individual reviews:

1. More detailed description of how statistical analysis was carried out, including clarifications/modifications as suggested by reviewer 1.

2. Rebalancing interpretation of the experimental and odelling results, as suggested by reviewer 2.

Reviewer #1:

The authors have addressed my recommendations and questions in much detail. Their changes have improved the quality of the manuscript as a result, illuminating the perceptual causal inference in ASD across different contexts. However, I believe there still are a couple of points that the authors can address to make the description of the results and the methods even clearer for publication.

1. Figure legends/captions of Figures 3 and 4 in the main texts lack detailed descriptions of the elements in the figures. For example, for Figures 3 and 4, what do those error bars represent? Standard errors or confidence intervals? In Figure 4B, are solid lines the model predictions and hollow points the observations? I believe this essential information would help readers better understand the figures.

2. The data points in Figure 2A-B and Figure 3A-C are slightly different from those in Figure 4B-C. For example, in Figure 2B, the audio bias of 24 deg disparity is weaker than that of 12 deg disparity for the high visual reliability condition (dark brown lines and points); however, in Figure 4B left panel, the audio bias of 24 deg disparity is even larger than that of 12 deg disparity. I assume that the data points depicted in Figure 4B-C are the aggregate data for modelling, in which the data of some participants were not included? I notice that the authors have included which participants were included in the single-subject modelling, but was the aggregate data the same as what was used for plotting Figures 2 and 3? I find it a bit confusing at first sight, perhaps the author could check it again and/or mention the related information in the caption or the main text?

3. From lines 451-453 of merged files (Instead, differences between […] relative to control observers.), did the author imply that the model where pcommon was freely estimated from the data was better, compared with the model where pcommon was fixed (I guess it’s the model in Figure 4 – supplement 2)? In other words, did the authors have two different models and conduct a model comparison here? If so, I think it’s better to provide model comparison results. The question also applies to the texts from lines 460-461. Also, what is DAIC? Is it the difference of AIC between the full model (that allows pcommon) and the restricted model (that fixes pcommon to a constant)? The authors should describe it somewhere in the main text.

4. The authors should be more specific about the tests they used to compare model parameters between groups and those correlational analyses. What type of tests did the authors use, parametric (i.e., Welch t-test, Pearson correlation) or non-parametric (i.e., Mann-Whitney, Spearman correlation, or permutation methods)? Particularly for the comparison of pcombined (Figure 4G), would the result be different when a non-parametric test was used if the test used in the current revision was parametric? I suggest the authors take more robust approaches given that the distributions of the model parameters seemed not quite Gaussian.

5. What is α and ν in Equation 5 and 6, please define them in the text. Also, it would be better if the authors give a short introduction to the meaning of lapse rate, lapse bias, etc., when mentioning them for the first time. Given that many readers are not very familiar with computational modelling, they may not intuitively understand what these parameters represent.

6. The D in DAIC from line 462 is in another font.

7. I apologize in advance if it’s my mistake but I failed to find Supplementary Text 1 mentioned in lines 430, 451, and 459. Where could I find it?

Reviewer #2:

The authors have adequately addressed my comments.

The strong aspects of the results are better clarified, and the overlap between participants across experiments is also clear. Further, the authors do not make claims that are not directly supported experimentally.

The limitation of a somewhat small (<20) number of participants per group in important experiments is still a drawback, given participants’ variability, particularly in the ASD group. Yet, I believe that the main results hold.

The strongest aspects of the study are the direct results, rather than the modelling:

Experiment 1: audio-visual integration is intact in ASD 2. Yet multisensory behavior is atypical (in the current experimental protocol) – ASD participants tend to favor source integration, as manifested by their cross-modal bias in localization even when visual and auditory signal are separable from a sensory perspective. Though both groups tend to over integrate, this is more salient and tend to span a broader distance in ASD. 3. Explicit reports have an opposite tendency – individuals with ASD were less likely to report a common cause for the two stimuli. Given the adequate direct measures of ASD cue integration with a small audio-visual distance (performance in Experiment 1) these results suggest a specific atypicality in cause attribution.

I also find the difference between spatial and temporal integration very interesting. Temporal and spatial groups differences in explicit attribution of a common source merits some additional discussion.

Personally, I think the contribution of the modelling part to the study is overstated in the paper, but I agree that is a personal perspective and need not be imposed on the authors.

Reviewer #3:

The authors have done a very good job including new alternative models, and improving the Description of the modelling (modelling my main points of scepticism). I am happy to recommend the paper for publication.
