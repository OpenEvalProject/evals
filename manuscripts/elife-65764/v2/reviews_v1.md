# Peer review - Round 1

Editors:
- Mario Penzo, National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65764.sa1](https://doi.org/10.7554/eLife.65764.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study offers novel insight on neurophysiological mechanisms occurring in the prefrontal cortex (PFC) during the learning of cue-reward associations. The results will be of great interest to scientists in the behavioral and systems neuroscience fields, but also to the broader scientific audience due to the use of challenging in vivo techniques, computational analyses, and statistical methods.

Decision letter after peer review:

Thank you for submitting your article "Specialized coding patterns among dorsomedial prefrontal neuronal ensembles predict conditioned reward seeking" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Maria M Diehl (Reviewer #2); Anthony Burgos-robles (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

The reviewers agree that the authors' identification of dmPFC neuronal ensembles with heterogeneous coding patterns offers important insight about the neurophysiological mechanisms governing cue-reward learning. However, as independently outlined below by each one of the reviewers, there are multiple aspects of the study that must be strengthened before the paper can be considered for publication in eLife. With the exception of the optogenetic behavioral manipulations requested by Reviewer # 3, we consider that all other concerns raised by the reviewers must be addressed in full. Specifically, the authors must address:

1) All technical concerns regarding the imaging technique that were raised by Reviewer # 1.

2) All statistical and data analysis concerns raised by Reviewers #1, 2 and 3.

3) Additional clarifications of methods and analyses, and an improved discussion as suggested by the reviewers.

4) The concerns about the behavioral design raised by Reviewer #1.

5) Due to the lack of causality, revise the text to soften the language a bit in some some of the sentences describing the interpretation.

Please notice that addressing these concerns will require, at a minimum, the incorporation of new data analyses, validation data, and an extensive revision of the manuscript's text.

If you have not already done so, please include a key resource table.

Reviewer #1:

The manuscript addresses a critical question in cortex and neuroscience in general – how do neuronal coding patterns lead to behavioral outputs and learned behaviors? While the manuscript takes a technically innovative approach there are multiple issues with the behavioral design, imaging, and interpretation.

There are issues with the using multiple imaging planes in each animal and with the longitudinal co-registration. Regarding the FOVs, the authors report that each imaging plane was separated by 50uM. However, since GRIN lenses display non-linear ray transformations in both the lateral and axial planes, movement of the external objective in 50uM steps cannot be assumed to produce a 50uM change in imaging plane. Even if we are to accept that no cells were double counted, a more critical issue is that collection efficiency, and therefore SNR of the recording, will be altered as a function of the distance of each neuron from the ideal focal plan of the implanted GRIN endoscope. Additionally, more information is needed on the longitudinal registration including how these data were validated and the percentage of neurons tracked.

With respect to the behavior, it is not clear whether the changes are the result of reward learning or more simply related to non-associative variables like habituation, lick rate, or volume consumed.

The manuscript from Grant et al., explores heterogeneity in coding patterns of mPFC pyramidal neurons during reward learning. The manuscript addresses a critical question in cortex and neuroscience in general – how do neuronal coding patterns lead to behavioral outputs and learned behaviors? While the manuscript takes a technically innovative approach there are multiple issues with the behavioral design, imaging, and interpretation. These issues are addressable, and the manuscript has potential for high impact in the field, but to support the current conclusions would require significant additional analysis and experimentation. Issues are listed below:

1. There are major issues with the imaging methodologies, particularly with the using multiple imaging planes in each animal and with the longitudinal co-registration. Regarding the FOVs, the authors report that each imaging plane was separated by 50uM. However, since GRIN lenses display non-linear ray transformations in both the lateral and axial planes, movement of the external objective in 50uM steps cannot be assumed to produce a 50uM change in imaging plane. Indeed, in the representative images the same vasculature can be seen in multiple planes, and the veins in this area often smaller than 50uM. Though it is difficult to discern, it appears that the same cell constellations appear in multiple planes in the representatives.

2. Even if we are to accept that no cells were double counted, a more critical issue for the current claims of the manuscript is that collection efficiency, and therefore SNR of the recording, will be altered as a function of the distance of each neuron from the ideal focal plan of the implanted GRIN endoscope. This is a potentially critical flaw without significant additional analysis. For example, all of the clustering analysis could be highly biased by the number of neurons that were included from each imaging plane which is likely to vary from animal to animal. While this is always somewhat of a concern with GRIN imaging, because 3-4 imaging planes were used in each animal and that clustering analysis was performed on pooled data it is possible that difference in SNR across imaging planes is driving many of the effects in the manuscript.

3. Regarding longitudinal registration, minimal methodological information is provided which is concerning given that this a notoriously difficult endeavor especially in dense recording such as these data. How were these data validated? Was the data set scored by a second experimenter for cross validation? What percent of neurons were tracked? Was any network analysis of cell location used to verify results?

4. While the issues with the imaging are critical to address, it is likely that in depth analysis could resolve the problems without the need for additional experiments. However, there is also some problems with the behavioral design – these will either require additional experiments or require that the claims of the manuscript be altered. All of the changes in mPFC dynamics that occur across the behavioral task are claimed to be related to reward learning, but there are several processes that are not parsed in the task design. For example, would some of these changes happen with habituation? Would some of these changes happen with lick rate, volume consumed? None of those are dependent on associative learning and could just as strongly predict the changes that are seen in the dataset.

5. What is the justification for using water restriction combined with a sucrose solution in water as a reinforcer? Given that sucrose functions as a reinforcer without water restriction and that water functions as reinforcer under water deprived conditions, it is unclear whether the water or the sucrose is functioning as the primary reinforcer.

Reviewer #2:

Grant et al., used two-photon calcium imaging of dorsomedial prefrontal cortical neurons to examine the neuronal ensemble activity during a sucrose conditioning task in head-fixed mice. Using a spectral clustering algorithm, the authors characterized ensemble activity into 5 distinct clusters whose activity correlated with various aspects of the task: CS+ responding, CS- responding, CS discrimination, reward responding, and licking behavior. Cluster 1 exhibited excitatory responses to both CSs and reward delivery, Cluster 2 exhibited excitatory responses to CS+ only, Cluster 3 exhibited excitatory responses to both CSs, Cluster 4 exhibited excitatory responses to reward delivery only, and Cluster 5 exhibited inhibitory responses to CS+. Next, the authors determined whether each Cluster predicted licking behavior across each conditioning session for each mouse. They found that the proportions of neurons in Cluster 5 positively correlated with successful licking behavior (licking in response to CS+), whereas proportions of neurons in Cluster 3 positively correlated with licking errors (licking in response to CS-). The authors were next interested in whether the neural activity across all dmPFC neurons (regardless of cluster ensembles) predicted task events or animal licking behavior during early vs. late in learning sessions of the task. Overall, CS presentation, CS discrimination, reward delivery, and licking rate were predicted by dmPFC activity during late, but not early, in learning. Taking into account the cluster ensembles, the authors also identified whether the activity of each cluster could predict CS presentation, CS discrimination, reward delivery, and licking rate. Finally, the authors assessed whether the cluster ensembles remain stable after learning; Cluster 1 showed robust responses to both CSs and reward delivery during both early and late in learning sessions of the task, whereas Clusters 2-5 did not, suggesting that these latter Clusters changed their activity patterns as a function of learning. The authors conclude that excitatory neuronal ensembles in dmPFC differentially predict events and behaviors during a sucrose conditioning task and the responses can change across learning. The conclusions of the paper are supported by the data; however, some aspects of the paper need to be clarified, additional analyses performed, and more interpretation of the data is warranted in order to strengthen the importance of this study.

More clarity is needed on how early and late session classification and whether the results would be similar if data were based on trial number instead of auROC across session.

The cluster analysis would benefit from the addition of location information to determine whether the 5 identified clusters are anatomically segregated. The data would also benefit from a cross-correlation analysis to reveal if there are any significant interactions between neurons within the same FOV, determine whether they are from the same cluster, whether cells active early in learning interact with cells that are active late in learning, and whether these cross-correlations remain stable after learning.

1. Behavioral sessions were classified as either "early in learning" or "late in learning" and are defined based on the animal's performance (using auROC) across multiple sessions of the sucrose conditioning task. The authors perform an independent t-test comparing performance in early vs. late in learning sessions; however, these 2 groups of sessions were pre-defined by the animal performance itself. Therefore, it is inappropriate to use a statistical test since the periods of early and late were selected based on the behavioral data (i.e. doing a statistical test on data that was pre-selected). A statistical test is not needed here, but the authors should emphasize that the number of early vs late in learning sessions were unique to each animal and selected based on their performance (this is only mentioned in the methods, but authors should consider reiterating this point in the results). As a reader, it was very difficult to understand how early and late in learning was defined and I had to go back and read the methods multiple times and look through the results for clarification. I initially thought early vs. late in learning referred to early trials vs. late trials within a session. If early and late was defined based on trial number instead of auROC across sessions, are the behavioral results similar to what was reported? On average, how many sessions did it take for each mouse to reach criteria?

2. Because I was confused about early vs late in learning being within session vs. across session, I was also confused about the data analyzed in Figure 4. How many sessions were in early vs late? Was the miniscope lens advanced after each conditioning session? Was there a subset or a different set of neurons that were recorded from across multiple sessions/days? Also, why do the traces in Figure 1I look very identical to the traces in Figure 4B (lower)? Are the cells analyzed in Figure 4 a subset of those shown in Figure 1? Please clarify. I think it would also be helpful to use the same terms consistently throughout the text when referring to the conditioning sessions and clearly state at the beginning of the results that one session was recorded per day and the lens was advanced to a new FOV (if that was the case) – sometimes sessions are referred to as FOVs or different days.

3. PFC-PVT neurons are located in lateral layers of PFC, whereas PFC-NAc are located in more medial layers within PFC. Based on this anatomical distinction, it would be interesting to determine the location of the 5 different cluster ensembles in the layers of PFC, which might suggest cells in particular clusters project to PVT or NAc. For example, are Cluster 5 neurons largely located in lateral layers of dmPFC based on their similarity in neuronal activity to PFC-PVT neurons, whereas neurons from other Clusters are located in medial layers of PFC? This analysis would provide more evidence that Cluster 5 neurons in lateral dmPFC are likely projecting to PVT and show the inhibitory activity profile, whereas neurons from different Clusters in medial dmPFC are likely projecting to Nac and show an excitatory activity profile. This analysis would also provide more concrete interpretation of the data in the Discussion section.

4. In Figure 5, D1 and D2 are denoted to indicate dmPFC activity "across days after learning (lines 621-622). Which conditioning sessions do these refer to – which session/day # relative to all sessions for each mouse? are sessions D1 and D2 the first two days in Late in Learning sessions? Are these neurons a subset of the neurons recorded during the conditioning session and if so, were they in recorded in more ventral regions of dmPFC compared to Early in Learning sessions if the lens was advanced from dorsal to ventral along dmPFC? Could there be differences in neural processing of appetitive cues in dorsal vs. ventral Cg1?

5. One major advantage of 2-photon calcium imaging is the ability to measure calcium dynamics between neurons that are recorded simultaneously (i.e. measured within the same FOV). It would be interesting perform a cross-correlation analysis to reveal if there are any significant interactions between neurons within the same FOV, determine whether they are from the same cluster, whether cells active early in learning interact with cells that are active late in learning, and whether these cross-correlations remain stable after learning.

6. Looking at activity across early vs late in learning, it was found that Cluster 1 was stable but Clusters 2-5 were not on the basis of responding to CSs. How did Clusters 2-5 change as a function of learning? Were they different based on reward delivery or licking behavior? Additional analyses are needed to strengthen this finding.

7. As it reads, the authors discuss their findings in relation to whether they agree with other studies and tools needed to answer questions about the role of specific cell types in prefrontal circuits for appetitive discrimination tasks. To strengthen the importance of this study, further discussion is needed that includes more interpretation of the data. Doing additional analyses will provide more findings to interpret, so the reader has a better grasp of the importance of this study.

8. In figure 3, CDF is undefined. Please define.

Reviewer #3:

In this study, Otis and colleagues evaluated the neural dynamics in the PFC governing reward learning, particularly those occurring during Pavlovian cue-sucrose associations. In particular, the study characterizes five unique neuronal ensembles exhibiting complex response patterns that seem to be relevant for the encoding of reward-predictive cues, the reward itself, and/or reward-related behavioral responses. The study also shows that the activity of these neuronal ensembles decodes behavioral variables better than chance. Interestingly, the study also shows that the activity of these neuronal ensembles during early stages of learning predicts their activity profile during late stages of learning, which remain stable afterwards.

The following list represents other strengths of the study.

1. New insights are revealed on neurophysiological mechanisms in the PFC governing cue-reward learning, using an in-vivo technique that provides great anatomical resolution, 2-photon calcium imaging.

2. This study double downs on the validity and power of head-fixed preparations to evaluate neural dynamics and their relationship to behavioral output.

3. Computational and statistical analyses are used to disentangle neuron-to-neuron variability, and to cluster neurons into distinct categories based on their response patterns.

4. In addition, throughout the study, authors describe complex methods in easy-to-understand language and illustrations to facilitate understanding of otherwise complex neurophysiological datasets and analyses.

Despite these strengths, this study could still be improved in a couple of aspects to better support the main claims and conclusions.

1. The initial analysis to cluster neurons together based on their activity patterns during the task produced somewhat confusing results in which for instance neurons exhibiting either excitatory or inhibitory responses to certain task events (e.g., either CS+, CS-, reward, or licks) were clustered together.

2. In addition, this study can greatly benefit from additional experiments (e.g., optogenetics) to manipulate neural activity during certain task epochs to test the importance of the observed activity patterns.

In general, I feel enthusiastic with the prospect of publication for this article. Though, I have several concerns that require further attention and revision to improve the overall impact of the study. As it stands, I believe this study is not yet ready for publication in eLife. But if my concerns are properly addressed with substantial revisions, I will feel even more enthusiastic to consider this paper for publication in eLife.

In the list below highlights some issues, confusions, or suggestions for additional analyses or experiments with the hopes to improve the overall quality of the study.

1. Results from the initial analysis to separate neurons into distinct neuronal ensembles are confusing. While this analysis (PCA) revealed five "unique" neuronal ensembles that supposedly encode specialized information during cue-reward learning, it is quite confusing that within-cluster responses are still very heterogeneous. For example, as shown in the Figure 1H heatmaps, within-cluster responses varied a lot across and included excitatory responses (in purple), inhibitory responses (in green), and weak responses (colors in between) within each cluster. There is also heterogeneity in the temporal profile of the responses within each cluster. How or why did neurons exhibiting excitatory and inhibitory responses get clustered together? And why did neurons exhibiting very fast responses get clustered together with neurons exhibiting slower responses? What am I missing here? Perhaps the authors could try a different clustering method (e.g., hierarchical analysis) to either confirm their clusters or potentially reveal more homogenous clusters. After all, in theory there could be many more neuronal clusters due to the many experimental variables analyzed (CS+, CS-, sucrose, sucrose omission, licks), all the possible ways neurons could respond (i.e., excitation, inhibition, no response, fast response, delayed response), and all possible response combinations (e.g., excitation to the cue, but inhibition to sucrose, etc).

2. Figure 1J summarizes the average within-cluster response patterns in PSTH form. Keeping in mind my first issue above, these PSTHs then seem misleading. For instance, the average PSTHs for Cluster-2 shows selective excitatory responses to the CS+. Yet, heterogeneity can be appreciated in the heatmaps in Figure 1H, with even some neurons exhibiting inhibitory responses to the CS-. Again, the authors should consider reinforcing or revising these results using a different clustering analysis.

3. In Figure 4, authors attempted to evaluate the evolution of response patterns in the distinct neuronal ensembles across learning. They did so by comparing ensemble activity during early versus late learning sessions. While significant Pearson correlations were detected for most ensembles during CS+ and CS-, I am not convinced that this is the best analysis to explore the evolution of neuronal activity patterns across learning. These results may just indicate that activity patterns may have developed very rapidly early in training, even before significant learning was observed at the behavioral level. To overcome this, authors could instead compare the magnitude of responses across learning sessions, or even at different segments within the early sessions (e.g., first 10 trials, versus 10 subsequent trials, and so on) to better explore whether the magnitude of responses is amplified as training progresses.

4. Caution is recommended for the type of t-test used in some analyses. For example, an independent t-test was used to compare cue discrimination scores between two days in the same subset of animals. Should this rather be a paired sample t-test?

5. Finally, all findings in this study are of correlative nature. Thus, additional experiments are needed to reinforce some of the claims raised in the study. For instance, the last sentence in the abstract says – "Our results characterize the complex dmPFC neuronal ensemble dynamics that relay learning-dependent signals for prediction of reward availability and initiation of conditioned reward seeking". If this is true, then manipulations of neural activity during certain epochs should produce significant changes in behavioral responses. A potential additional experiment could then be optogenetic-mediated inhibition during the CS+ to see whether lick rates are impaired. While this experiment could be performed in a non-ensemble-specific manner (i.e., optogenetic inhibition of all excitatory neurons in the area), it would be even better if the microscope used by the authors has holographic stimulation capabilities to selectively manipulate particular ensembles based on their response pattern. This is consistent with the last suggestion by the authors towards the end of the discussion ("functionally targeting each neuronal ensemble independently…").

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Specialized coding patterns among dorsomedial prefrontal neuronal ensembles predict conditioned reward seeking" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Maria M Diehl (Reviewer #2); Anthony Burgos-robles (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

As you will find from the evaluation summaries provided by each of the reviewers below, the general consensus is that the revised manuscript has addressed most of the critiques raised after the initial submission. However, Reviewer #1 has raised a few remaining points that we feel must be addressed for the manuscript to be considered appropriate for publication in eLife.

Specifically, we deem essential that in addition to authors current graphics on the relative distance of clustered neurons from the GRIN lens, they provide a quantitative analysis of how this distance influences clustering or relation to behavior. For additional details on the requested analyses please refer to the comments from Reviewer #1.

We also ask that when referring to the behavioral procedure the authors adopt terminology that most accurately represent the conditions surrounding behavioral tests (second point from Reviewer #1).

If you have not already done so, please ensure your manuscript complies with the eLife policies for statistical reporting: https://reviewer.elifesciences.org/author-guide/full "Report exact p-values wherever possible alongside the summary statistics and 95% confidence intervals. These should be reported for all key questions and not only when the p-value is less than 0.05."

Please include a key resource table.

Reviewer #1:

The authors were overall responsive to critiques and several of the issues raised in the previous reviews have been addressed. However, some concerns remain, the first of which is still requires additional analysis prior to publication.

1. The most significant remaining issue is the potential effect of differential SNR across imaging planes due to the GRIN lens properties. The fact that clusters show differential patterns and not only differences in amplitude does not negate the potential impact of SNR on the clustering – the ability to detect a differential pattern of responses between neurons is dependent on sufficient SNR, which is evidenced directly in the dataset by the fact that some of the clusters are defined by a lack of response. The authors have made great improvements on dealing with this issue from the original submission but given that essentially all the claims in the manuscript are based on the clustering analyses some quantitative assessment should be provided.

I appreciate the authors caution in using relative measurements to estimate the relative distance of clustered neurons from the GRIN lens – this is the most appropriate way to begin to approach the issue. However, the estimations are only graphically displayed, without quantitative analysis of their influence on clustering or relation to behavior, and the visualization of the data in figure 1 S5 makes it difficult to discern if there are topographical effects due to the number of overlapping points. In Figure 1 Sup 5B, how many neurons are in each line across the D/V axis? Is there a correlation between estimated location and probability of cluster membership? This is critical for determining if there is an influence of imaging plane on the clustering analysis. A complimentary approach would be to subsample and perform the clustering analysis only from a subset of DV planes at a time and determine reproducibility of cluster membership and their relationships with behavior. This is most concerning for the interpretation of Figure 2, where differential number of neurons sampled from each plane across animals could easily produce spurious correlations that reflect sampling bias rather than biological relationships.

2. Regarding the use of concurrent thirst and sucrose to motivate behavior, while it is true that head-fixed procedures often include water deprivation, these procedures were developed to motivate engagement in sensory processing tasks, not to analyze the effects of the reward itself as in the current manuscript. This is highlighted in both of the citations provided by the authors (other than their previous work) – the Goldstein et al., reference also goes on to show that how the deprivation is performed (e.g. water vs food) can dramatically impact the resulting reward-conditioned behaviors. This is not necessarily an inherent flaw in the study, but with the current wording/claims it becomes an issue.

For example, the authors refer to the behavioral procedure as 'Pavlovian sucrose conditioning' throughout – would the conditioned response (anticipatory licking) still occur if only water was delivered? Given that mice typically drink ~4 mL per day and only ~1mL is provided outside of the behavioral task, a strong argument can be made from the literature that the fluid has a much greater reinforcing/conditioning strength than the sucrose itself. I don't see any utility to empirically testing this, but given that the goal of the study is to examine conditioned reward seeking at the very least accurate terminology should be used throughout (e.g. Pavlovian conditioned licking or similar). To facilitate integration with the literature it would also be useful to add a discussion point noting that this protocol is likely to influence sucrose palatability (e.g. PMID: 16248727) as well as magnitude and nature of conditioned responses (e.g. PMID: 26913541 and 16812301).

3. The authors should clarify in the methods when the homecage water was provided in relation to behavioral testing, as well as provide an estimate of the range of total fluid and sucrose consumed in a typical session.
