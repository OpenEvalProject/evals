# Peer review - Round 1

Editors:
- Laura L Colgin, University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55252.sa1](https://doi.org/10.7554/eLife.55252.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

There are still so few studies about the lateral septum, disproportional to its potential significance. This is solid work with a novel finding that increases our understanding of mechanisms underlying motivated behaviors and neural representations of space.

Decision letter after peer review:

Thank you for submitting your article "Differences in reward biased spatial representations in the lateral septum and hippocampus" for consideration by eLife. Your article has been reviewed by Laura Colgin as the Senior Editor and Reviewing Editor and three reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Alexey Ponomarenko (Reviewer #1).

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Wirtshafter and Wilson investigated spatial firing of lateral septal (LS) and CA1 neurons using parallel recordings from the two regions during a rewarded navigation task. They show that a large number of LS cells display place-selective firing, a finding the authors have previously reported. Here, they perform more detailed analysis of place field characteristics of LS neurons, showing that LS place fields are similar in many ways to HPC fields and that LS place fields are more likely to occur near reward/choice locations. They found that one-dimensional place fields of LS neurons are in many respects similar to CA1 place fields, yet they display different skewness in relation to reward location. Further, firing of LS and CA1 cells is more correlated for those cells with place fields close to the reward location. Because neural representations in LS are poorly understood, studies of circuits including LS can provide new insights into functions of hippocampus and other interconnected regions. The present high-quality data contribute to the understanding of information processing in LS and substantially extend earlier reports (Takamura et al., 2016) showing the influence of reward location on spatial firing of LS neurons. The LS has been given somewhat short shrift by the broader hippocampal community, and although the work is somewhat exploratory, this was viewed as appropriate for the relatively early days of investigating the LS.

However, the study was viewed as having some shortcomings in its quantifications that leave open important questions. The paper needs to show a more transparent presentation of the results. The results should also be better situated in the existing literature.

Essential revisions:

1) There was a considerable variability of firing in individual runs, and LS place fields maxima did not converge to a single location. Reviewers had questions about the variability in LS firing patterns:

a) Was this variability in the different arms of the maze, and other features of spatial representations in general, related to behavioral performance or behavioral variations in the task?

b) Related to the above point, an underlying assumption is that LS neurons are selectively encoding information about reward proximity or recent reward receipt (supported by the data in Figure 6). The authors observe a higher probability of LS place fields on the Choice Side when the rat is leaving vs. approaching a reward well. An open question which is important to interpret these results is whether LS neurons care only about location relative to *possible* reward, or rather care about location relative to *actual* reward. Given that rat performance is ~75% correct according to the methods, do the authors observe an effect of success or failure on the task? Do LS neurons differentiate between runs toward or away from the same location when that location is actually rewarded vs. when it was not? On a similar note, given the increase in LS place fields upon leaving the reward site, do the authors observe larger LS place fields after correct vs. incorrect trials? Alternatively do the authors observe LS place fields which do not distinguish between the two arms, but instead only represent correct vs. incorrect trials?

c) There was confusion about the results described in Figure 4E-F. The fact that the curve for hippocampal neurons eventually reaches zero indicates that spatial representation stabilizes over time. However, while the curve is downward for LS cells (indicating some level of stabilization), the reason why it never reaches zero was unclear. Do these data simply mean that each lap is highly variable for LS cells even after a small amount of initial stabilization? If so, and if the final distance of lap place field center to average place field center is 20 cm, this indicates that the 'place field' on each lap moves up to 40 cm (+/- 20 cm from average center). Considering that the track center is ~120 cm long and each arm is ~70 cm long, movement of 40 cm from lap-to-lap seems quite substantial. Is it possible that LS place fields shift slowly across time, making it near-impossible for any given lap to align with the average across all laps? Given the bias for LS place fields to be located near the reward well, are near-reward place fields more or less likely to stabilize than reward-distant fields?

d) LS cells are quite heterogeneous in their firing rate and the regularity of discharge. Was there any systematic relationship between spatial firing properties and firing rate, coefficient of variation and the recording location? This information may also help explain apparent discordances with other studies of spatial firing in LS (Tingley and Buzsaki, 2018).

2) Regarding the data in Figure 2, the distribution of HPC unit bits/spike appears to be comprised of at least two (possibly three) clusters: one with very low bits/spike (near zero), one with moderate bits/spike (centered around 1.25), and possibly a third with very high bits/spike (centered around 2.9). This is what would be expected in a population of neurons in which most, but not all, encode spatial information in any given environment. Appropriately, the division between cells that encode spatial information and those that do not (bits/spike = 0.8) does seem to correctly divide those populations. However, for the LS neurons, the distribution appears to be composed of a single population, and the separation that the authors make between cells that encode spatial information and those that do not seems rather arbitrary for LS cells. In other words, if you only looked at the distribution of bits/spike for LS cells, where would you draw the red dashed line? Reviewers raised a concern that the distribution of bits/spike for LS cells is not reflective of a true spatial encoding, but rather, what one might expect from random firing patterns. If the authors shuffle cell IDs for each spike, do they still observe a similar distribution of bits/spike across the shuffled units? If the authors create 452 artificial units using Poisson firing, do they observe a similar distribution of bits/spike for the artificial units? In other words, is the place representation of some neurons really different than one would expect from chance, given that the authors are sampling 452 neurons and at least some of those neurons are likely to fire in spatially restricted locations by chance?

3) Could increased cross-correlations computed for a broad range of lags of 100 ms in the choice arm be due to higher firing rates proximal to rewards? Information about firing rates (peak rates, average rates in field) in different arms is difficult to find in the manuscript.

4) Given the importance of LS place fields to this study, reviewers would like to see more than four examples. Reviewers suggested a Supplemental Figure that presents a large number of LS place fields, selected in an unbiased way.

5) Reviewers would also like to see examples of spike cross-correlations supporting the data in Figure 7.

6) The authors note in the introduction that the hippocampal encoding of goal locations has been characterized, but they do not cite a highly-relevant study: Dupret et al., 2010. These experiments showed that the hippocampal over-representation of goal is not universal, but instead depends on the cognitive demands of the task. It is important to know, therefore, whether goal locations are over-represented in the present study. One straightforward way to address this would be to re-analyze the data from panels 6E-F. If the probability of a field were *per unit distance*, results from the different track segments would be directly comparable. This would reveal whether hippocampal place cells themselves are clustered near reward in this task, and to what degree LS neurons might amplify that clustering.

7) The plot in Figure 7B shows an intriguing correlation. This quantification only shows the effect is present when averaging across all neurons, however. Does every neuron show such a correlation, or just a subpopulation? This information could help to corroborate or reject the authors' models. Related to the previous point, it would also provide an estimate of what fraction of hippocampal neurons might be specialized for encoding reward.

8) The recording location in the caudodorsal LS is very close to the septohippocampal nucleus (SHN) based on Paxinos and Watson's stereotaxic atlas, and indeed, at least one of the recording sites in Figure 1A appears to be in the SHN. I am unaware of any literature quantifying place representation in the SHN, but given the controversy regarding whether LS neurons have place fields, it is important to determine whether the place-selective units in the current study are more likely to be LS or SHN neurons. Do the authors observe a correlation between medial/lateral (or other stereotaxic orientation) recording location and likelihood of observing place-specific firing? Perhaps in a supplemental analysis, the authors could replicate several of their core findings using only units recorded on the lateral-most tetrodes, which would be the least likely to be in the SHN.

9) In Figure 5, the authors quantify skewness and compare runs to reward vs. runs away from reward, reporting a significant difference for hippocampal fields, but not for LS fields. To facilitate interpretation of these results, reviewers would like to know if the skewness of HPC or LS neurons during runs to reward were different from zero (or different from a shuffle distribution). The same point was raised for runs away from reward.

10) Do LS cells have direction-specific place fields, and how does direction-selective firing (in HPC and LS neurons) impact skewness? Is the skewness driven entirely by uni-directional fields, or is it observed for both uni- and bi-directional fields?

11) The datapoints in Figure 5 and Figure 5—figure supplement 2 don't seem to line up, and there was confusion about these figures. Is it correct that each dot represents a cell with its average place field peak at that location (relative to reward) and with that skewness? If that is correct, shouldn't the data in Figure 5F-G be a subset of the data in Figure 5—figure supplement 2? However, those points aren't the same. The difference should be made clear in the text or in the figure legend.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Differences in reward biased spatial representations in the lateral septum and hippocampus" for consideration by eLife. Your article has been reviewed by Laura Colgin as the Senior Editor and Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Alexey Ponomarenko (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Reviewers agree that authors have satisfactorily addressed most concerns. Reviewers are grateful that the authors identified the coding error that led to many of the reviewer questions and also appreciate the additional work the authors have performed on analyses and reworking the text of the manuscript. Reviewers agree that this is a considerably stronger manuscript after the revisions. There are only a few comments remaining:

Essential revisions:

1) It is still possible that the higher cross-correlations over many tens of milliseconds between HPC and LS cells with place fields in the choice side (Figure 7) can be secondary to a higher number of place fields in both regions in this part of the maze (Figure 6). This might be addressed, for instance, by comparing cross-correlations for forced, middle and choice sides for subsampled spike trains selected to ensure a matched degree of overlap of place fields in HPC and LS. However, the paper would still be interesting and worthy of publication even if it turns out that cross-correlations are due to concentration of Hip and LS place fields on the choice side close to rewards.

2) Figure 5 seems to be consistent with the lack of influence of hippocampal inputs on the skewness of LS place fields. The latter are similarly skewed at different locations. However, HPC place fields change their directional skewness depending on the proximity of the reward. It would be helpful to integrate this finding in the models proposed.
