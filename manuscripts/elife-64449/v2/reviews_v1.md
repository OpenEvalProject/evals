# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64449.sa1](https://doi.org/10.7554/eLife.64449.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Cortical circuits are subject to ongoing plasticity during an animal's lifetime that has the potential to alter responses to external stimuli over days and weeks. Pérez-Ortega and colleagues examines whether coincident firing of neurons in mouse visual cortex is preserved over a long timescale (one month) in response to repeated stimuli. The authors find that in spite of significant variability in the responsiveness at the population level, subsets of identified neurons maintain coordinated firing. Such cell assemblies may provide a stable substrate for representing visual stimuli.

Decision letter after peer review:

Thank you for submitting your article "Long-term stability of cortical ensembles" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tirin Moore as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Carsen Stringer (Reviewer #1); Laura N Driscoll (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work examines whether coincident firing of neurons in visual cortex is preserved over a long timescale (one month) which is important because it provides insight into the stability and plasticity of neural circuits and visual representations. The authors find that subsets of identified neurons maintain coordinated firing despite some degree of flux in the firin activity across the population.

All reviewers agreed that the question is important but found the analysis lacked depth and there were some technical issues in the experiments that should be addressed with a fuller discussion and potentially additional analysis to eliminate confounds/artefacts. In general, and in light of earlier work (some of which is not cited) the conclusions need to be more circumspect. Specifically:

– There were concerns about movement/loss of cells/calcium indicator artefacts over this long imaging period that should be accounted for more rigorously.

– The analysis applies a somewhat arbitrary criterion for stability (50% of cells remain in responsive in an assembly). This threshold should be systematically explored and justified more carefully.

– The wider literature on this topic should be more thoroughly cited, limitations of the study should be transparently laid out, claims about the overall stability found in this population response and its relevance to memories and behaviour should be moderated in line with the comments below.

Reviewer #1 (Recommendations for the authors):

Perez-Ortega and colleagues performed rigorous experiments to determine if the activity of neurons in visual cortex is similar across days, in particular comparing spontaneous activity in the absence of visual stimuli across days, which was previously not examined to my knowledge. The paper claims that evoked ensembles are more stable than spontaneous ensembles, but more convincing quantitative analyses are required to support these claims.

– There is only one mention of prior work with multi-day imaging in visual cortex (Ranson 2017). Another related study to cite and compare your results to would be Jeon, …, Kuhlman 2018 (and I think a comment about how similar/different your results are from this study + Ranson would be useful for the reader). I would also recommend mentioning that there are studies that have observed differences in evoked activity across learning in V1 (e.g. Poort, Khan et al., 2015; Henschke, Dylda et al., 2020). Do you think there was adaptation across days to the stimulus that you repeated?

– Some GCaMP6f mice have aberrant cortical activity (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5604087/). In the raw data (Figure 1F) it doesn't look present, but it would be useful to show more time and sort the neurons by their first PC weights perhaps to see the activity structure.

– The approach of 3 plane imaging taking the maximum projection seems useful for tracking cells across days. There is a claim that some cells are no longer found / no longer active. Based on Figure 1G it appears there may have been some Z-movement from day 10 to day 46. This Z movement may explain some of the lost active cells. As a sanity check I would recommend plotting the Z-plane on which the cells were maximally active on day 1 vs the Z-plane on which the cells were maximally active on day n.

– There is an emphasis on analyzing the data as ensembles but I think this may be missing other slow, gradual changes. The definition of stable is at least 50% of neurons were preserved across days. However, the fitting procedure of finding ensembles may produce different ensembles even if those neurons are still correlated to each other. I would recommend two possible additional analyses: (1) compare the correlation matrices for common neurons across days (unless there are too few neurons for this); (2) look at changes in single neuron statistics across days. For (2) this may include reliability of neural responses to the visual stimuli, the weights of the neuron onto the first principal component of spontaneous activity, or the correlation of a neuron with running speed. I think these results may solidify your ensemble result (evoked-related statistics change less across time).Reviewer #2 (Recommendations for the authors):

Overall I think the authors collected an interesting dataset. Analyses should be adjusted to include all cells rather than sub-selecting for stability. Additionally, the language needs to be adjusted to better reflect the data. I wish there was any behavioral data included, but if the authors compare their data to publicly available data in V1 for a single recording session during a visually guided task, these concerns could be quelled a bit. Reject, but I would reconsider if the following suggested changes are made.

1. In general the language of this paper and title seem to mismatch the results. The fraction of cells that were 'stable' as the authors say on line 112 was very small, however the authors focus extensively on this small subset for the majority of analyses in the paper. Why ignore the bulk of data (line 119)? What happens if you repeat the same analysis and keep all cells in the dataset? The general language around stability of neural ensembles should be adjusted to better reflect the data (ex: lines 157, 225).

2. There are claims in this paper about how ensembles 'implement long-term memories' in the introduction and conclusion and yet the authors never link the activity of ensembles to any behavioral or stimulus dependent feature. This language reaches far beyond the evidence provided in this paper. The introduction could provide some better framing for expectations of stability vs. drift in neural activity rather than focus on the link between ensembles and memory given that there isn't much focus on the ensembles' contribution to memory throughout. For example, the last sentence of the paper is not supported by data in the paper. Where is the link between ensembles and memory in the data? What is the evidence that transient ensembles are related to new or degraded memories? This reads as though it was the authors' hypothesis before doing the experiments and was not adjusted in light of the results.

3. There is no discussion around the alternative to stability of neuronal ensembles. What are the current theories about representational drift? For example, in Line 34 the authors present an expectation for stability without any reasoning for why there need not be stability. This lack of framing makes their job of explaining results in line 217 more difficult. There is a possibility that the most stable cells aren't more important – what is the evidence that they are? Does an ensemble need a core? Would be interesting to include some discussion on the possibility of a drifting readout (Line 223). [https://doi.org/10.1016/j.conb.2019.08.005]

4. How do activations in V1 in this dataset compare to other data collected from V1 while the animal is performing a task (where for example the angle of the gradings is relevant to how the mouse should respond)? I would be interested to know if the authors compared statistics of their ensembles to publicly available data recorded in V1 during a visually guided behavior. Are the ensembles tuned to anything in particular? Could they be related to movement? [http://repository.cshl.edu/id/eprint/38599/]

5. The authors provide some hypotheses as to why fewer cells are active in the later imaging sessions (dead/dying cells?). This is worrisome in regards to how much it might have affected the imaged area's biology. One alternative hypothesis is that the animal is more familiar with the environment/ not running as much etc. Have the authors collected any behavioral data to compare over time?

6. How much do the results change when you vary the 50% threshold of preserved neurons within an ensemble (Line 146)? Does it make sense to call an ensemble stable when 50% of the cells change? Especially given that the cells analyzed as contributing to an ensemble are already sub-selected to be within the small population of stable cells (Line 119)?

7. Cells are referred to as 'stable' when they're active on 3 different sessions that are separated in time. However, the authors find a smaller number of cells are stable over extended time (43-46 days later). If we extrapolate this over more time, would we expect these cells to continue to be stable? Given these concerns, it might make more sense to qualify the language around stability by the timespan over which these cells were studied.

8. Filtering frames to only coactive neurons for ensemble identification seems strange to me. Authors may be overestimating the extent of coactivation. What happens when you don't do this? How much do the results change when you don't subselect for Jaccard similarity? I would be interested to see how the results vary as you vary this threshold (Line 136).

9. The term 'evoked activity' is misleading because the authors don't link these activations to the visual stimulus. There's no task, so the mice could be paying little attention to the stimulus. Should we really consider this activity to be visually driven? Could the authors provide any evidence of this?

10. A method like seqNMF could reveal ensembles that are offset in time. This looser temporal constraint could potentially reveal more structure. This should be run on the entire dataset (without stability sub-selection). I suggest this as a potential alternative or supplement to the method described by the authors. [https://elifesciences.org/articles/38471]Reviewer #3 (Recommendations for the authors):

Neuronal ensembles have been shown by this lab and others to constitute one basic functional unit for the representation of information in cortical circuits. It is therefore important to determine how stable these blocks of representation might be. If these ensembles were preserved across time and sensory stimuli, this would indicate a significant degree of structure underlying cortical representations. In a first attempt to address these important issues, this manuscript analyzes the long-term stability of ensembles of coactive neurons in the layer 2/3 of mouse visual cortex across several days. Ensembles were recorded during periods of spontaneous activity as well as during visual stimulation (evoked). For this, the authors record spontaneous and evoked activity using two-photon calcium imaging one, ten and 40 days after the first recording session. In order to maximize overlap between successive imaging sessions, the authors record three planes separated by 5 microns almost simultaneously (9ms interval) using an electrically-tunable lens. They show that ensembles extracted during visual stimulation periods are more stable on days 2 and 10 than those computed during spontaneous activity. Stable ensembles display a higher "robustness" (a parameter that quantifies how many times a given ensemble is repeated and how similar these repeats are). Neurons displaying stable membership are more functionally connected than unstable ones. It is concluded that such observed stability of spontaneous and evoked ensembles across weeks could provide a mechanism for memories. Long-term calcium imaging within the same population of neurons is a real challenge that the authors seem to overcome in the study. The conclusions are important, my main concern relates to the number of experiments and analyses supporting these findings as detailed below.

Number of experiments and statistics: According to Table 1, two mice with GCamP6f have been through the complete imaging protocol (days 1,2, 10 and 43) but none with the 6s, since 3 missed the intermediate measure (day 10) and one the last point (day 40+). Therefore five mice have been recorded over weeks with two different indicators, but only two were sampled on day 10. One mouse was only recorded until day 10. Altogether, this is quite a low sampling, but the experiments are certainly difficult. However, the total number of experiments analyzed is higher, due to the repeat of 3 sessions on the same mouse per day. This certainly contributes to reaching significance. However, the three samples from the same mouse are not independent points. Are the FOVs different for each session in the same mouse? If they are the same, then the statistics should be repeated but treating all experiments from the same mouse as single experiments. I would suggest repeating the analysis but using only one data point per mouse per day. Also, given that two different indicators were used (6s and 6f), one would need to see whether the statistics are the same in the two conditions.

Robustness: the authors compute this metric, as the product of ensemble duration and average of the Jaccard similarity and find that stable ensembles display higher robustness: isn't it expected that robustness is higher in stable ensembles given that stable ensembles should be observed more often?

Evoked ensembles: It seems to me that evoked ensembles are ensembles extracted during continuous imaging periods that include stimulation. However, one would expect evoked ensembles to be the cells activated time-locked to the visual stimulation. This notion only appears at the end of the paper with "tuned" neurons in Figure 4. In the discussion, authors conclude lines 205-207 that "sensory stimulus reactivate existing ensembles". I do not think this is supported by the analysis performed here. For this, I believe that one would need to compare, within the same mouse the amount of overlap between spontaneous ensembles and "tuned neurons".

How representative are the illustrated examples in Figures 2 and 3? The authors report that about 20 neurons remain active from day 1 to 46 but their main figures display example rasterplots with more than 60 neurons, which is three times more than the average. Is this example representative? Which indicator was used? Is there a difference in stability between 6f and 6s?

Rasterplot filtering: The authors chose to restrict their ensemble analysis to frames with "significant coactivation". Why not use a statistical threshold to determine the number of cells above which a coactivation is significant instead of arbitrarily setting this number to three coactive neurons? In cases of high activity this number may be below significance.

Demixing neuronal identity: The authors assign a neuron to an ensemble if it displays at least a functional connection with another neuron. They use reshuffling to test significance of functional links but still it seems that highly active neurons are more likely to display a high functional connectivity degree and therefore to be stable members of a given ensemble with that definition of ensemble membership. What is the justification to define membership based on pairwise functional connectivity? The finding that core ensemble members display a high functional degree may be just a property reflecting a property of highly active neurons (as previously described by Mizuseki et al., 2013).

Type of neurons imaged: The authors use Vglut1-Cre mice, therefore they are excluding GABAergic cells from their study, this should be clearly mentioned and even discussed.

Volumetric imaging: I am not sure one can say that "volumetric imaging" was performed here, rather this is multi-plane imaging.

Mouse behavior: there is little detail concerning mouse behavior, are mice allowed to run? What is the correlation between ensemble activation and running?

Abstract: the authors should say that 46 days is the longest period they have been recording, otherwise it gives the wrong impression that after 46 days ensembles are no longer stable. Also "most visually evoked ensembles" should be replaced by "ensembles observed during periods of visual stimulation" (see above). "In stable ensembles most neurons still belonged to the same ensemble after weeks": how could ensembles be stable otherwise?

Discussion: I found the discussion quite succinct. It lacks discussing circuit mechanisms for assembly stability and plasticity (role of interneurons for example?), limitations and possible biases in the analysis and placing results in the perspective of other studies analyzing the long-term stability of neuronal dynamics.
