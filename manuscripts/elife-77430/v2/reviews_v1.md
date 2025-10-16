# Peer review - Round 1

Editors:
- David Badre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77430.sa0](https://doi.org/10.7554/eLife.77430.sa0)

This article addresses the question of how the brain segments naturalistic events and the relationship between perceived event boundaries and neural pattern shifts. By applying an innovative analysis to a large, publicly available dataset, they observe evidence of different timescales of neural state shifts that correspond with perceived event bounds. These results will be of interest to cognitive neuroscientists investigating the relationship between neural states and event segmentation.


---

# Peer review - Round 1

Editors:
- David Badre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77430.sa1](https://doi.org/10.7554/eLife.77430.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Timescales and functional organization of event segmentation in the human brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Charan Ranganath (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that this submission will not be considered further for publication in eLife.

The reviewers were in agreement that this is an important topic and that this research is both interesting and promising. However, the reviewers raised a number of significant concerns that centered around two themes. First, there were a number of points raised about the methodology itself and its validity. After some discussion, it was decided that these methodological points could be addressable through additional analysis and/or simulation, but likely require considerably more work than would be usual for an eLife revision. The second set of concerns were with regard to the clear scientific advance over prior work; there was not consensus that these findings move the field forward in a clear way. Reviewer 1 suggested that the generalizability and impact might be improved by drawing direct links to the existing literature, including analysis of a secondary dataset as in the Baldasano et al. (2017) paper. Though, there might be other ways to clarify the impact, as well. Regardless, this is a challenging concern to address in a straightforward way through revision.

As addressing these concerns would likely require more than is typically expected for an eLife revision, it was decided to reject this submission. This being said, if you were to undertake the work required to conclusively address these issues, there was sufficient enthusiasm among reviewers that they would be willing to consider this paper again, as a new submission.

I have appended the detailed reviews to this decision letter. I hope you find them constructive with this work.

Reviewer #1:

In this paper, Geerligs et al. focus on the alignment of event boundaries across brain regions. They examine the transitions between brain states using the method introduced by Baldassano et al. (2017), and how these state transitions are shared across nodes of large-scale brain networks. They introduce a method that enables them to map event-timescales in a broader set of regions than previously possible, and they use this method to reveal how functional networks of regions share time-aligned "event transitions".

This is a well-written manuscript on a timely and important question.

My main concerns relate to the validity (and potential sources of bias) in the methodology for identifying the event-rate of each region, and I also outline a number of other areas where the conceptual and methodological framing could be improved.

p.3 "This dataset, in combination with the application of hyperalignment to optimize functional alignment (Guntupalli et al., 2016), allowed us to study event segmentation across the entire cortex for the first time, because this dataset shows reliable stimulus-driven activity (i.e., significant inter-subject correlations) over nearly all cortical brain regions (Geerligs et al., 2018). "

A central methodological question, which affects almost every claim in this manuscript, is whether the inference of event boundaries from the HMM model (the methods in Figure 1) is valid, and in what ways it might be biased. The validity question is simple: does it measure what it is supposed to measure? In particular, I would like the authors to justify the final step, in which they compute the difference between the correlation for real boundaries and the correlation for random boundaries. Surely, this difference computation will be affected by the noise ceiling of the individual ROI being examined? I understand why using the random condition as a "reference" makes some sense, but I do not understand why the final decision is made based on the simple arithmetic difference of the mean value for the random boundaries and real boundaries? I suggest that the authors justify this procedure using a simulation procedure where the ground truth about event transitions is known, and the procedure should be compared against the method applied in the original Baldassano et al. (2017) paper.

The bias question is also fairly simple: which factors influence the "k" that is inferred? In particular, if a region has high reliability or low reliability of its response across subjects, does this affect the number of events that will be inferred for that region using the HMM procedure? As noted above, this simulation could additionally investigate how the "k" value varies as function of the noise level (i.e. response reliability) of the ROI.

Additionally, although hyperalignment render a larger swathe of cortex available to analysis, but there will still be variability in the reliability of the signal across regions, and this might interact with the hyperalignment performance. In particular, the accuracy of the hyper alignment procedure (for each subject) will presumably also increase for regions whose reliability of response is higher; it is therefore very to consider whether noise (in "space") introduced by the hyperalignment procedure (and varying across regions as a function of their reliability) could further bias the measurement of the event-timescale via the HMM procedure.

Finally, to better understand this method, the authors could also apply their approach to the freely available data from the Baldassano et al. (2017) paper. Does this method produce results that are at least qualitatively similar? This could help to resolve the question of why the event timescales in this paper are shorter than those observed in the Baldassano et al. paper.

p.7: Event networks: "We found that event boundaries are shared within long-range networks that resemble the functional networks that are typically identified based on (resting state) timeseries correlations (see figure 3A)".

This is one of the most intriguing aspects of this paper. However, it would be much more convincing if the authors would replace their qualitative language (e.g. "resemble") with quantitative metrics of overlap. The overlap could be measure between (a) networks defined based on event-timing and (b) networks defined based on functional connectivity. All of the major functional networks should be available in atlases (e.g. the Yeo lab atlases) or via data sharing repositories. Thus, the authors should be able to substantiate their broad claims of "resemblance" with quantitative demonstrations of how well the event-networks match the functional-connectivity-networks. All of the visual networks as well as the FPN and DMN should be quantitatively compared against standard networks defined elsewhere in the literature.

On the same point: p.13 "The fractionation of the DMN into a fast and slow subnetwork closely aligns with the previously observed posterior and anterior DMN subnetworks (Andrews-Hanna et al., 2010; Campbell et al., 2013; Lei et al., 2014)."

Again, please quantify the alignment when claiming spatial alignment with prior findings.

p.13 "Our results show for the first time that neural events are shared across brain regions in distinct functional networks. "

The authors should consider re-wording this sentence to distinguish their findings from what was already shown in Figure 4B of Baldassano et al. (2017). In particular, note the commonality of event boundaries across early visual and late visual areas (part of the visual network), as well as the commonality of events across angular gyrus and posterior medial cortex (parts of the DMN).

On a related note, in the Abstract we read: "This work extends the definition of functional networks to the temporal domain" – I am unclear on how novel this extension is. To the best of my understanding, the concept of dynamic functional connectivity is not new (e.g. Hutchison et al., 2013), and even second-order pattern-transition methods have been employed to study functional networks (e.g. Anzellotti and Coutanche, 2018). I would like the authors to sharpen their argument for why this result is not entirely expected in light of prior work. Shouldn't members of the same functional networks be expected to exhibit state-transitions at rates higher than chance?

p.11. I struggled to follow the logic of the analysis employed in Figure 6. Why is event duration being predicted from individual frequency bands of the PSD? There is voluminous evidence for band-specific and region-specific artifact (e.g. Birn et al., 2013; Shmueli et al., 2007). Furthermore, distinct functional networks have distinct frequency profiles and coherence patterns (e.g. Salvador et al., 2008; Baria et al., 2011; Stephens et al., 2013). Finally, the frequency bands in the PSD are non-independent (because of the temporal smoothing in the BOLD signal). Therefore, the relationship between frequency band and event duration is confounded by (i) non-independence of frequencies and (ii) frequency covariation across brain regions which arises for a multitude of reasons. The results in Figure 6A seem rather noisy to me, and I imagine that this is because the regression procedure on the PSD is influenced by many interacting and confounding variables.

Another region why this analysis produces (in my opinion) curious results is that it spans distinct sensory modalities which are already known to have opposite PSD-event relationships: along the auditory pathway, PSDs get flatter as event time-scales get longer, while in the visual pathway, PSDs in V1 are already very steep, even while the event timescales are short. It is not clear what is gained by fitting a single model to regions with obviously different relationships of PSD and event structure.

p.12. "These results suggest that visual and auditory stimulation are a prerequisite for observing the temporal hierarchy we describe in this paper and that this hierarchy only partly reflects an intrinsic property of brain function that is also present in the resting state."

I do not follow the logic supporting this claim. How can we know whether the (event-based) temporal hierarchy is preserved in the resting state unless we can measure the event transitions in the resting state data? Isn't this analysis just another way of saying that the PSDs have different shapes during rest and during movie viewing?

References

Anzellotti, S., and Coutanche, M. N. (2018). Beyond functional connectivity: investigating networks of multivariate representations. Trends in cognitive sciences, 22(3), 258-269.

Baria, A. T., Baliki, M. N., Parrish, T., and Apkarian, A. V. (2011). Anatomical and Functional Assemblies of Brain BOLD Oscillations. Journal of Neuroscience, 31(21), 7910-7919. https://doi.org/10.1523/JNEUROSCI.1296-11.2011

Birn, R. M., Diamond, J. B., Smith, M. A., and Bandettini, P. A. (2006). Separating respiratory-variation-related fluctuations from neuronal-activity-related fluctuations in fMRI. Neuroimage, 31, 1536-1548. https://doi.org/10.1016/j.neuroimage.2006.02.048

Coutanche, M. N., and Thompson-Schill, S. L. (2013). Informational connectivity: identifying synchronized discriminability of multi-voxel patterns across the brain. Frontiers in human neuroscience, 7, 15.

Hutchison, R. M., Womelsdorf, T., Allen, E. A., Bandettini, P. A., Calhoun, V. D., Corbetta, M.,.… Chang, C. (2013). Dynamic functional connectivity: Promise, issues, and interpretations. NeuroImage, 80, 360-378. https://doi.org/10.1016/j.neuroimage.2013.05.079

Salvador, R., Martínez, A., Pomarol-Clotet, E., Gomar, J., Vila, F., Sarró, S.,.… Bullmore, E. (2008). A simple view of the brain through a frequency-specific functional connectivity measure. NeuroImage, 39(1), 279-289. https://doi.org/10.1016/j.neuroimage.2007.08.018

Shmueli, K., van Gelderen, P., de Zwart, J. A., Horovitz, S. G., Fukunaga, M., Jansma, J. M., and Duyn, J. H. (2007). Low-frequency fluctuations in the cardiac rate as a source of variance in the resting-state fMRI BOLD signal. Neuroimage, 38(2), 306-320.

Stephens, G. J., Honey, C. J., and Hasson, U. (2013). A place for time: The spatiotemporal structure of neural dynamics during natural audition. Journal of Neurophysiology, 110(9), 2019-2026. https://doi.org/10.1152/jn.00268.2013

Reviewer #2:

In this paper, Geerlings and colleagues leverage a large, publicly-available dataset in order to assess shared and distinct timescales of neural pattern shifts at event boundaries across different areas of the brain. In line with prior work, the authors report a gradient of timescales in neural event segmentation, with sensory regions comprising the fastest-shifting areas and 'default mode' nodes such as precuneus and medial prefrontal cortex comprising the slowest-shifiting areas. Importantly, the authors build on this previous research and demonstrate that canonical functional networks – such as the frontoparietal network, and the 'default mode' network – feature distinct subnetworks with corresponding faster and slower timescales of pattern shifts. Finally, a fairly novel analysis applied to these types of data examined power spectral density across regions, which could be used to predict event duration across regions (consistent with observed pattern shifts), and could partly, but not entirely, characterize resting-state fMRI data (suggesting that the audiovisual stimulus drove additional functional properties in brain networks not observed during rest).

Overall, this is an interesting and timely study. The question of how the brain segments naturalistic events is one of increasing popularity, and this manuscript approaches the question with a large sample size and fairly thorough analyses. That said, there are a number of questions and concerns, primarily regarding the analyses.

• Procedures such as hyperalignment, or the related shared response model used by Baldassano and colleagues, are typically implemented by training on one set of the data, and applying the alignment procedure to a separate, held-out dataset (i.e., training and testing sets). It is unclear whether this approach was taken in the current study, or whether the hyperalignment algorithm was trained and tested on same dataset. In the latter case, there is a degree of circularity in the way across-participant alignment was conducted, potentially leading to biased correlation measures. The movie used in the CamCAN dataset is only 8 minutes long, which is probably not enough data for obtaining separate training and test datasets. However, this is still potentially a serious issue for this manuscript, and I am not sure if the use of hyperalignment is appropriate. If I have misunderstood the methodology, it perhaps warrants some clarification in how the training and application of the hyperalignment algorithm proceeded. (I will note that I am aware you used cross-validation for deriving the number of events, but that is unfortunately a separate issue from a train-test split in the hyperalignment routine itself.)

• A key finding from the study is that the FPN and DMN fractionate into different subnetworks that have fast and slow timescales. As noted above, the present results are based on an analysis of data from a relatively short period of time. Although the sample size is very large, one wonders whether this distinction would remain solid with a longer movie. With a very short movie, one can only sample a small number of real events, and this could lead to some instability in estimates of the timescale of representations in relation to the events. This might be an issue in relation to the differentiation of fast and slow subnetworks within the FPN and DMN. For instance, Figure 3B, suggests that the fit values for the slow FPN remain more or less stable across a range of event durations (which presumably reflect k values?). The slow FPN shows an interesting bimodal distribution (as do many of the networks) with the second peak coinciding with the peak for the fast FPN. The differentiation is a bit more convincing for the fast and slow DMN, but it is still not clear whether there are enough events and enough fMRI data from each subject to ensure reliable estimates of the timescales. Just to provide some context for this point, some estimates suggest that reliable identification of resting state networks requires at least 20 minutes of fMRI data.

• Throughout the paper, fMRI results are described in reference to event processing, but the relationship is underdeveloped. Much of the paper relies on the Hidden Markov Model, which assumes that there is a pattern that remains stationary throughout an event. Baldassano's data shows a surprisingly strong correspondence in posterior medial cortex, but it is less clear whether this assumption is valid for other areas. In relation to this point, one can think of event processing as an accumulation of evidence. At the onset of an event, one might have a decent idea of what is about to happen, but as information comes in, the event model can be refined to make stronger predictions. These kinds of within-event dynamics would be lost in the Hidden Markov model. A related point is that the paper conflates timescales of neural states with psychologically meaningful conceptions of events. EST suggests that event segmentation is driven by prediction error-by one interpretation of the model, sensory information can change considerably without leading one to infer an event boundary. However, change in incoming sensory information would almost certainly lead to the detection of "event boundaries" across short timescales in sensory cortical areas. Figure 5 makes it fairly clear that there is a pretty strong distinction to be made between data-driven event identification based on the fMRI data and psychologically meaningful events inferred by the subjects. It would be helpful for the authors to be more clear about what the data do and do not show in relation to putative event cognition processes.

• Why were voxels with an intersubject correlation of less than r=0.35 excluded from analyses? Is this based on prior studies or preliminary analyses? It is not necessarily a bad thing if this choice was made arbitrarily, but I imagine this threshold could have important impacts on the data as presented, so it is worth clarifying.

• Was ME-ICA the only step taken to account for head motion artifacts? If so, there is some concern about whether this step was sufficient to deal with the potential confound. This is especially critical given the fairly brief time series being analyzed here. It would be more compelling to see a quantitative demonstration that head motion is not correlated with the measures of interest.

• A related issue is that of eye movements. Eye movements are related to event processing (e.g., Eisenberg et a., 2018), so one can expect neural activity related to event prediction/prediction error to be confounded with lower-level effects related to eye movements. For instance, we might expect signal artifacts in the EPI data, as well as neural activity related to the generation of eye movements, and changes in visual cortex activity resulting from eye movements. It is unlikely that this issue can be conclusively addressed with the current dataset, and it's not a deal-breaker in the sense that eye movements are intrinsically related to naturalistic event processing. However, it would be useful for the authors to discuss whether this issue is a potential limitation.

• The power spectral analyses were a bit difficult to follow, but more importantly, the motivation for the analysis was not clearly described. The main take home points from this analyses are nicely summarized at the end of p. 14, but it would be helpful to clarify the motivation for this analysis (and the need for doing it) on p.11 in the Results section. Relatedly, is Figure 6A an example spectrum from a particular voxel or region, or an average across regions?

• The take-home message appears to be that different brain networks have different timescales at which they seem to maintain event representations. Moreover, certain networks (e.g., the posterior medial/'default mode' network) do not have uniformly fast or slow timescales. The network-based analysis used here is indeed novel, but the impact of the work could be enhanced by clarifying the significance of the results in relation to what we know about event processing. The explicit demarcation of 'fast' and 'slow' subnetworks may be the key conceptual advance, as was the power spectral analysis, but it isn't clear whether these conclusions could also be ascertained from the maps shown in Baldassano et al., 2017 or other papers from the Hasson group.

This review was completed by Zach Reagh, Ph.D. in collaboration with Charan Ranganath, Ph.D. (I sign all reviews)

Reviewer #3:

Geerligs and colleagues conduct a thorough set of analyses aimed at identifying event segmentation timescales across the cortex in a large cohort of participants. They extend previous work by Baldassano et al. by covering the entire cortex, and nicely control for the power spectrum of different regions. In addition, they examine which regions share the same event boundaries, not just the same timescale, and relate these to functional connectivity networks. Overall, their work is impressive and rigorous, but there are a few points that make it somewhat difficult to assess the how strong the contribution is to our understanding of processing timescales:

1. The authors divide the brain into functional networks based on boundary similarity and find that this division is very similar to functional networks defined using resting-state timeseries correlations. They further find increased similarity between regions of different networks that are that are interconnected. Wouldn't the similarity between boundary vectors be strongly linked to the timeseries correlations (both between regions in the same network and across networks)? While the similarity-based functional networks aren't completely identical to those identified in rest, perhaps the same results would be obtained by correlating timeseries in this specific dataset, using the movie data (altering the interpretation of the results).

2. It seems that the power spectrum analysis is run both on the resting-state data and on the movie data, whereas the timescale segmentation is run only on the movie data. I expect this is because hyperalignment is possible only when using a shared stimulus, and the HMM is run only on the hyperaligned data. However, this may bias the correlations presented in figure 6 – the movie PSD-based timescale estimation would be expected to be more similar to the HMM timescales than the rest, simply because the same data is used. A more convincing analysis would be to run the HMM on the rest data as well, and test for correlations between the two estimations of event timescales in the rest data, although this would entail substantial additional analyses (as HMM would also have to be run on non-hyperaligned movie data for comparability). It would also help with point 1, testing whether similarity in boundary vectors arises directly from timeseries correlations. I realize this adds quite a bit of analysis, and the authors may prefer to avoid doing so, but the conclusions arising from the power spectrum analysis should be softened in the Results and Discussion, clearly mentioning this caveat.

3. It would aid clarity to better separate the current contributions from previous findings, in the Results, and mainly in the Discussion. The authors do describe what has previously been found, citing all relevant literature, but it would be helpful to have a clear division of previous findings and novel ones. For example in the first paragraph of the Discussion, and in general when discussing the interpretation of activity the different regions (currently regions that have already been found are somewhat intermixed with the new regions found).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A partially nested cortical hierarchy of neural states underlies event segmentation in the human brain" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers were positive about the revisions you made to this submission and felt that extensive work had been done to improve the paper. There were a few remaining points raised by this review that could be addressed the further strengthen the paper. The Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Reviewer 1 has raised some additional points for clarification in their review, as noted below. These should be clarified in a revision. Please refer to the comments below for these notes.

2. Some of the conclusions do not completely reflect the results. If additional analyses are not added, perhaps these conclusions could be rephrased, such as "some of the neural boundaries are represented throughout the hierarchy.… until eventually reflected in conscious experience" (p. 14) and "boundaries that were represented in more brain regions at the same time were also more likely to be associated with the experience of an event boundary" (p. 15).

3. Since the GSBS algorithm was fine-tuned based on the data that was later used for analysis, it would be helpful to include additional information demonstrating the choices in the optimization procedure are independent of the eventual results. For example, it isn't clear what 'important boundaries being detected late' means, whether that indicates event boundaries were being missed by the original algorithm. Combined with the fact part of the optimization was based on fixing the number of state boundaries to the number of event boundaries – could these choices have increased the chance of finding overlap between state boundaries and event boundaries?

4. Two small notes: the network defined as posterior DMN includes anterior regions, which is slightly confusing; were the regional differences in HRF assessed on the resting state data or the movie watching data?

Additional Suggestions for Revision (for the authors):

One of the reviewers had some suggestions for additional analyses that might strengthen the results. We pass them along to you here, but you should view these as optional. Only include them if you agree that they will strengthen the conclusions.

there are a few analyses that may help strengthen the conclusions - these are suggested as optional additional analyses, but the authors should feel free not to include them:

• To verify the overlap between searchlights is not due to various artifacts, it may be preferable to compare the searchlight in one region with the searchlights of other groups in the second region (following the rationale of intersubject functional connectivity vs. functional connectivity). It would also be interesting to further explore the nature of the overlap - to see whether there are specific state boundaries that drive most of the overlap or whether different pairs of regions have different overlapping boundaries. This could be used to explore the nature of the hierarchy between regions, beyond just finding that higher regions share boundaries with lower regions. For example, it could enable testing whether state shifts shared by multiple lower level regions are the ones that traverse the hierarchy.

• Further to this, it would be interesting to test whether event boundaries and non-event neural state boundaries form a similar hierarchy (though this may not be feasible with such a low number of event boundaries).

• To assess the effects of noise reduction on the overlap between neural state boundaries and event boundaries, it may be worth testing whether neural state boundaries shared across groups of participants are also more likely to be event boundaries (and specifically whether this effect is stronger in the same regions arising from the co-occurrence analysis). This analysis wouldn't provide an answer, but could help shed some light on the role of noise reduction.

Reviewer #1:

This work investigates timescales of neural pattern states (periods of time with a relatively stable activity pattern in a region) across the brain and identify links between state shifts and perceived boundaries events. In multiple regions, they find significant overlap between state shifts and event boundaries, and an even stronger overlap for state shifts that occur simultaneously in more than one region. The results are interesting and timely and extend previous work by Baldassano et al. that found a similar hierarchy in a specific set of brain regions (here extended to the entire cortex).

Strengths

The question of whether neural state shifts form a hierarchy such that state shifts in higher regions coincide with state shifts in sensory regions, and the question of whether event boundaries occur at conjunctions of shifts in different regions are both very interesting.

The optimized GSBS method nicely overcomes limitations of previous methods, as well as a previous version of GSBS. In general, justification is provided for the different analysis choices in the manuscript.

The current work goes beyond previous work by extending the analysis to the entire cortex, revealing that state shifts in higher regions of the cortex overlap with state shifts in lower regions of the hierarchy.

Weaknesses

One of the important conclusions of the paper is that simultaneous neural state shifts in multiple brain regions are more likely to be experienced as boundaries. This finding fits in nicely with existing literature, but the analysis supporting it is not as compelling as the rest of the analyses in the paper:

1. The methods section describing the analysis is not entirely clear. Do Oi, Oj refer to the number of neural state boundaries in searchlights I,j? Or the number of neural state boundaries in each that overlap with an event boundary? If the former (which was my initial interpretation), then how is the reference searchlight chosen – max {Oi,Oj}, as indicated by the formula, or the searchlight with the larger overlap of its unique boundaries (and is the overlap calculated in numerical value or the proportion of overlap)? Given the unclarity, it is difficult to assess whether the degree of overlap between neural state boundaries and event boundaries in each of the searchlights (and/or the number of boundaries in each) could affect the results. It would be helpful to provide verification (either mathematically or with simulations) that higher overlap in one/both searchlights does not lead to a larger difference in overlap between shared and non-shared boundaries.

2. The analysis focuses on pairs of searchlights/regions, demonstrating that in a subset of regions there is a higher chance of an overlap with event boundaries for neural state boundaries that are shared between two regions. Yet the interpretation goes beyond this, suggesting that "boundaries that were represented in more brain regions at the same time were also more likely to be associated with the experience of an event boundary". Additional analyses would be needed to back this claim, demonstrating that overlap between a larger number of regions increases the chance of perceiving a boundary.

3. Could the effect be due to reduction of noise rather than event boundaries arising at neural state boundaries shared between regions? Identifying boundaries shared by two regions has a similar effect to averaging, which the authors have indeed found reduces noise and provides a better estimation of boundaries within each searchlight. This possibility should be discussed.

Recommendations for the authors:

1. As this is a revision of a previous version of the manuscript, and the authors have already conducted a great deal of work to address previous concerns, I am hesitant to suggest additional analyses. However, there are a few analyses that may help strengthen the conclusions – these are suggested as optional additional analyses, but the authors should feel free not to include them:

• To verify the overlap between searchlights is not due to various artifacts, it may be preferable to compare the searchlight in one region with the searchlights of other groups in the second region (following the rationale of intersubject functional connectivity vs. functional connectivity). It would also be interesting to further explore the nature of the overlap – to see whether there are specific state boundaries that drive most of the overlap or whether different pairs of regions have different overlapping boundaries. This could be used to explore the nature of the hierarchy between regions, beyond just finding that higher regions share boundaries with lower regions. For example, it could enable testing whether state shifts shared by multiple lower level regions are the ones that traverse the hierarchy.

• Further to this, it would be interesting to test whether event boundaries and non-event neural state boundaries form a similar hierarchy (though this may not be feasible with such a low number of event boundaries).

• To assess the effects of noise reduction on the overlap between neural state boundaries and event boundaries, it may be worth testing whether neural state boundaries shared across groups of participants are also more likely to be event boundaries (and specifically whether this effect is stronger in the same regions arising from the co-occurrence analysis). This analysis wouldn't provide an answer, but could help shed some light on the role of noise reduction

2. Some of the conclusions do not completely reflect the results. If additional analyses are not added, perhaps these conclusions could be rephrased, such as "some of the neural boundaries are represented throughout the hierarchy.… until eventually reflected in conscious experience" (p. 14) and "boundaries that were represented in more brain regions at the same time were also more likely to be associated with the experience of an event boundary" (p. 15).

3. Since the GSBS algorithm was fine-tuned based on the data that was later used for analysis, it would be helpful to include additional information demonstrating the choices in the optimization procedure are independent of the eventual results. For example, it isn't clear what 'important boundaries being detected late' means, whether that indicates event boundaries were being missed by the original algorithm. Combined with the fact part of the optimization was based on fixing the number of state boundaries to the number of event boundaries – could these choices have increased the chance of finding overlap between state boundaries and event boundaries?

4. Two small notes: the network defined as posterior DMN includes anterior regions, which is slightly confusing; were the regional differences in HRF assessed on the resting state data or the movie watching data?
