# Peer review - Round 1

Editors:
- Joshua Johansen, RIKEN Center for Brain Science Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56491.sa1](https://doi.org/10.7554/eLife.56491.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The hippocampus is important for associative learning and memory underlying adaptive behavior. These memories can be altered by new experiences, but it is not clear if or how hippocampal neuronal ensembles dynamically encode these changes. This paper addresses this question using in-vivo calcium imaging to record the activity of hippocampal neurons during recall and subsequent extinction of an associative behavioral memory. Strikingly, the transition from stable memory expression to extinction engages a new population of neurons and reorganizes functional connectivity within neuronal assemblies in the hippocampus.

Decision letter after peer review:

Thank you for submitting your article "Distinct Neuronal Populations Contribute to Trace Conditioning and Extinction Learning in the Hippocampal CA1" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joshua Johansen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kaori Takehara-Nishiuchi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Hansen et al. describe experiments designed to characterize how neuronal responses in the dorsal hippocampus are modulated by trace conditioning and subsequent extinction using single cell calcium imaging in mice. The authors build on previous findings that both of these behavioral tasks depend on the integrity of the dorsal hippocampus. They report that distinct CA1 cells and ensembles are recruited during conditioning and extinction, which is consistent with expectations from previous literature (eg, Lacagnina et al., 2019, Nat Neuro; Tronson et al. J Neurosci 2009; Mehrab et al. eLife 2014; Zhang et al. PLOS 2019). However, this is the first instance where distinct learning and extinction cells have been characterized and where identification of different neuronal ensembles have been measured in concert with learning in CA1 during trace eyeblink conditioning. This represents an advance over these previous studies.

While the results are potentially interesting, critically important controls are missing, making it difficult to draw firm conclusions from the results about whether distinct populations and networks of cells are present during eyeblink training and extinction. Furthermore, there are a number of experimental and analytical issues which need to be addressed. We therefore would like to invite the authors to respond to these concerns before a decision can be made on whether this work could be published in eLife.

Essential revisions:

1. The authors claim that the CS excited two largely disjoint groups of neurons during 40 CS-US paired trials (trace conditioning) and subsequent 40 CS-only trials (extinction). However, it is possible these changes are simply dependent on time (or non-associative effects), and not learning per se. To further strengthen this argument, they must demonstrate that comparable groups of neurons respond to the CS if CS-US contingency was kept the same throughout the entire session. One possibility could be that the authors use the data collected on the day before last training/extinction and the final day and examine how CS-evoked activity differed between the first 40 CS-US pairings and the last 40 CS-US pairings. If their argument is correct, the percentage of neurons with similar CS-evoked responses (Figure 2Dii) and the co-activity patterns (Figure 4E) should be comparable between the first and last 40 CS-US trials. And, these measures in the session with the contingency change should be greater than those in the control session without the contingency change. Alternatively, the authors could break up the last training session into two epochs, and run the exact same single cell and co-occurrence/network map analysis comparing these two epochs. If learning is the driving factor behind the emergence of distinct ensembles over time, the percentage of overlapping cells and percentage of cells with shared edges should be larger when comparing epochs that both occurred during the last session vs comparing either of these to extinction. A final possibility would be to run another control group in which the final extinction session is replaced with further overtraining to examine whether the extinction induced changes are produced by extinction or some other non-associative process. In this case cell and ensemble (co-active cells) could be examined across the last session of training and the subsequent overtraining. The prediction would be that there would not be as much change in the cell/ensemble representation with overtraining compared with extinction. Something like this is required to make any claims regarding differences in cell populations during training and extinction.

2. On a similar note, the comparison between correct and incorrect trials needs controls. We would recommend that the authors run the same analysis (Figure 5) after shuffling the trial labels (i.e., correct or incorrect trials) assigned to each co-activity pattern. This analysis allows for testing whether the percentage of the shared edge (Figure 5c) between correct and incorrect trials is significantly lower than the chance level.

3. The method of cell registration across sessions is poorly described. As the quality of cross-registration is crucial for some aspects of this study (within session cross registration is less of a worry), evidence for correct registration is key. The stated method of registering cells within 50 pixels (~50um) of one another and having at least 50% of pixel overlap seems like it has the potential for many false positives, particularly with 1-photon imaging where the authors are effectively sampling cells across tens of μm in the z-dimension. How was registration validated? Also, it is unclear as to whether registration was performed across the last session and extinction session.

4. There is considerable variability among mice for the number of cells examined, yet each mouse's contribution is not weighted in the analysis to reflect this. Can the authors show that the results of their analyses are not sensitive to differing numbers of cells across animals? Otherwise, can they provide alternative analyses that are not subject to this influence (e.g., pool all neurons from all mice for a session type and run a fisher's exact test (or equivalent) to test for significance when assessing changes in the proportion of neural responses across session types (e.g., first vs last training session)). Alternatively using subsampling procedures using numbers from the mouse with the least number of cells could address this issue.

5. Similarly, there is considerable variability among mice for behavioral performance (Figure 2B). Is there a correlation between overall task performance and neural responses? All individual data points should be color coded for mouse identity so the reader can track how behavioral performance corresponds to neural data.

6. Although the absolute value of CR% varies depending on the criteria used to detect CRs, CR% of ~40% in the first session seems very high. Please include the frequency of spontaneous eyeblinks in Figure 2B for comparison.

7. For the data shown in Figure 2, a more detailed neuronal analysis of the response properties of CA1 cells is necessary. One important point is that extinction is not a static process, while, in theory, the last training session occurring before it is. One might imagine that during early extinction the network would be more similar to the last training session and that over the course of extinction the extinction defined cells would emerge. As it stands, the extinction session is lumped into one category. The authors should analyze this in more detail by determining the change in response properties over the course of extinction and comparing different portions of the extinction dataset to the last training data. Furthermore, it says that the data in Figure 2C comes from one example animal. The authors should show a heat plot for all cells from all animals to give a more comprehensive view. In addition, in Figure 2C most of the responsive cells have a high activity level prior to stimulus onset. This is confusing as it says in the methods that the cells were classified as having a larger response during the stimulus period compared with the pre-stimulus period. Furthermore, it is unclear why only cells with higher baseline/pre-stimulus activity would be the 'responsive' cells. Additionally, it would be helpful to show a population averaged peri-event time histogram of the responses in the different trial-periods shown in Figure 2C to give a better idea of the dynamics. Finally, for Figure 2D, the authors should say what the data is normalized to.

8. Is there a reason why the trial sample size is not matched across comparisons? For example, incorrect trials constitute, on average, only ~1/4 the amount of correct trials. Given the large variability in trial-to-trial neural activity, the number of edges identified via co-occurence analysis would likely increase with trial number, which could be driving the false impression of greater connectivity (albeit short of significance) during correct vs incorrect trials. Since for most animals the number of correct trials will be >2x the number of incorrect trials, the authors could also take subsets of correct trials and compare these against each other to test for consistency across correct trials.

9. There are several instances of 1-tailed tests throughout the manuscript (e.g., when comparing the proportion of tone-trace active cells during training vs extinction). A rationale for these 1-tailed tests should be provided or, ideally, 2-tailed tests should be used.

10. The authors should address why the specific value of 2% deviation from average eye size was chosen as the threshold for a conditioned response? Is this an arbitrary value? Empirically based?

11. Regarding the co-occurence network map, the authors should address whether the threshold for edge creation between two nodes just a single trial where the 2 nodes were coactive. If they increase this threshold so only more robust ensembles are counted, does the proportion of shared edges change appreciably?

12. The method of fluorescence trace normalization in which they fit a normal distribution to the lowest 50th percentile of the data, used the mean of this distribution as the baseline , subtracted this baseline from each trace and then scaled data by 5% of the maximum range of the full calcium trace seems somewhat convoluted and suggests that they cannot isolate single cells/ROIs. This should be explained and/or corrected.

13. The method of classifying a cell as responsive during the tone-puff window (described in lines 526-538) is not ideal. The classification threshold of a larger calcium response during the stimulus compared with the baseline period of 0.15 (several 5% or one 30% increase) seems somewhat arbitrary. It would be better to use a statistical comparison.

References:

Lacagnina et al. Distinct hippocampal engrams control extinction and relapse of fear memory. Nature Neuroscience 22, 2019

Mehrab et al. CA1 cell activity sequences emerge after reorganization of network correlation structure during associative learning. eLife 2014

Tronson et al. Segregated Populations of Hippocampal Principal CA1 Neurons Mediating Conditioning and Extinction of Contextual Fear. J. Neurosci. 29, 2009

Zhang et al. Dynamics of a hippocampal neuronal ensemble encoding trace fear memory revealed by in vivo Ca2+ imaging. PLOS One 2019

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Distinct Neuronal Populations Contribute to Trace Conditioning and Extinction Learning in the Hippocampal CA1" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joshua Johansen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kaori Takehara-Nishiuchi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The authors have added new data and analyses which provide stronger support for the claims made in the paper. However, there are some remaining concerns which should be addressed before a final decision can be made.

Essential revisions:

1. The greatest concern with the initial submission was, that the authors show that distinct populations are engaged during late training vs extinction periods, but it is possible these changes are simply dependent on time (or non-associative effects, and not learning per se). The reviewers suggested two potential solutions to this: "One possibility could be that the authors use the data collected on the day before last training/extinction and the final day and examine how CS-evoked activity differed between the first 40 CS-US pairings and the last 40 CS-US pairings… Alternatively, the authors could break up the last training session into two epochs, and run the exact same co-occurrence/network map analysis comparing these two epochs." This additional analysis of splitting up the prior days session was run. However, the analysis of this is unclear and it could still benefit from modification to clarify and/or optimally address the concern it was in response to. Specifically, in Figure 2, the authors compare neural activity in the 'First Half' and 'Second Half' of Late Training, but it is unclear what trials these represent. Relatedly, when comparing Last Training to Extinction it is not clear what trials were used. This is confusing because they use either 60 or 80 trials on the Late Training day, 20 or 40 trials for the Last Training session and 40 Extinction trials. The ideal analysis would be to use 60 trials for late training, 20 last training trials and 40 extinction trials so that the late training (20 early, 40 late) comparison could be matched to the last day (20 last training, 40 extinction). The authors need to explain how this was done and clearly state this in the text/figure legend. If possible, they should also try to avoid gaps in trials in, for example, the Late Training or Last Training session to match trial numbers as this could present a confound.

2. Related to point 1, the authors state that 3 mice had an approx. 20 minute wait between the end of the CS-US session and the CS-only extinction session, where the animals remained headfixed. It introduces an additional 20-minute gap that is not present in the late session control data. Should these animals be excluded from analysis? Alternatively, they could analyze the data both ways and if there aren't major differences then combine them.

3. The authors have modified their criteria for task-responsive cells, but it still leaves much to be desired. The criteria of being active on 10%+ of trials was selected as a threshold because it is 3x the average background firing rate of ALL cells. However, cells with a higher baseline firing rate would be more likely to be labeled as responsive, just by virtue of their increased firing probability (and not due to any specific responsivity to the CS or trace). Why not tailor the cutoff on a cell by cell basis? Eg, run statistical analysis comparing CS/trace activity to background activity on a cell-by-cell basis? Or compare a cell's CS/trace activity to a shuffled distribution of that cell's background activity?

4. In the initial version of the manuscript there was a significant behavioral extinction detected, but in the current version there is no significant behavioral extinction (Figure 2B in previous and current versions and explained in lines 285-293). This change should be explained to the reviewers. Also, this is a bit of a problem for the interpretation of their data which relies on trial summed neural responses. They may be able to resolve this by statistically comparing the last training session CR to the later extinction session (similar to the first half to last half extinction analysis reported in lines 211-217). Furthermore, they could/should also show the trial-by-trial CRs during the entire extinction session (single trial or 2/3 trial bins). This may provide support for their contention that "…learning is dynamic during the extinction session" and give the reader more insight into the behavioral changes occurring during extinction.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Distinct Neuronal Populations Contribute to Trace Conditioning and Extinction Learning in the Hippocampal CA1" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Joshua Johansen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

The authors have addressed most of the reviewer concerns, but there is one outstanding reviewer comment which we advise you to consider and incorporate into the final version of your manuscript (see below).

Essential revisions:

We thank the authors for the clarification regarding point number 1 of the essential revisions. The only remaining suggestion is that the authors incorporate the gap between the late session trial blocks used for the control Jaccard index comparison or discuss this issue in the conclusion of the paper. That is, instead of comparing trials 1-20 and 21-40, compare trials 1-20 and 61-80 (or 41-60 in animals that did not undergo 80 trials). The idea is for this control analysis to better reflect the gap between last and extinction session blocks (which appears to be either 40 trials, or presumably ~ 20 mins + 20 trials for the animals that were subject to the technical memory limitation), and thus more precisely control for any potential changes due to elapsed time or task engagement.

Reviewer #1:

The authors have addressed my previous concerns. I support publication.

Reviewer #3:

The authors have addressed the majority of previous concerns. The only remaining concern is the analysis of the late session, where the authors should incorporate the gap between the late session trial blocks used for the control Jaccard index comparison. That is, instead of comparing trials 1-20 and 21-40, compare trials 1-20 and 61-80 (or 41-60 in animals that did not undergo 80 trials). The idea is for this control analysis to better reflect the gap between last and extinction session blocks (which appears to be either 40 trials, or presumably ~ 20 mins + 20 trials for the animals that were subject to the technical memory limitation), and thus more precisely control for any potential changes due to elapsed time or task engagement.
