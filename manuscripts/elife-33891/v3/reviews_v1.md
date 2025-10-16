# Peer review - Round 1

Editors:
- Eve Marder, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33891.015](https://doi.org/10.7554/eLife.33891.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Developmental deprivation-induced perceptual and cortical processing deficits in awake-behaving animals" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Eve Marder as the Senior/Reviewing Editor. The reviewers have opted to remain anonymous.

There was extensive discussion among the reviewers about how conclusive they felt these observations to be, and there were a variety of graded opinions about how to deal with these diverse takes on the manuscript, and whether rewriting would be able to deal with them conclusively. Therefore, at odds with the usual eLife practice, we are including all three of the initial reviews in entirety. In your revision, please provide the best and most comprehensive replies to the issues raised in the reviews. Many of the concerns will require more detail, and to some degree our final assessment will depend on how well you are able to deal with the concerns, although all of the reviewers find the work addresses an important set of problems.

Reviewer #1:

This manuscript reports, for normal hearing animals and in animals with a developmental conductive hearing loss, that behavioral performance in an amplitude-modulation (AM) detection task is reflected in auditory cortical but not brainstem population activity. A reduction of the detection ability for high AM frequencies following a moderate, conductive threshold shift is documented.

Overall, this a technically well-executed study with careful controls and sensible analytical approaches. Major assets are that cortical recordings were made while animals performed the task. The observation that behavioral AM performance in Gerbils could be traced to cortical population firing rate changes in normal hearing animals confirms previous reports in this and other species. The fact that this was also true for animals with a substantial conductive hearing loss is certainly novel, even if it only corroborates that a general peripheral threshold shift does not seem to alter how behavior is reflected in sensory cortical activity. The observed reduction of AM-depth detection at high AM frequencies provides behavioral and electrophysiological evidence that parallels observations in humans and supports the hypothesis that chronic conductive loss, likely via reduced inhibition, generates a wider range of temporal response variability, constraining central auditory AM encoding abilities.

A couple of issues, however, diminish the potential interpretations and impact of this approach.

The issue with most attempts to compare psychometric and neurometric thresholds is that there seem to be too many free parameters on the physiology side. What if the decoding model is suboptimal, e.g., missing relevant temporal patterns? What if the assumptions about the decoding model are not biologically realizable? What if there are different subpopulations and the relevant population is undersampled? What if irrelevant neurons are oversampled, corrupting the representation?

The reliance on rate measures is a bit puzzling as work in monkey has shown that primary cortex does utilize temporal response aspects and, in addition, that rate measures may be correlated with performance but not always with a monotonic increase in FR with better performance. How is a population approach, as used here, affected by these different codes and neuronal stimulus dependencies?

Another aspect, previously addressed by the authors and others, is that top-down influences shape learning as well as neuronal properties during performance. Is it conceivable that the observed effects are more a reflection of the recurrent decision process than the encoding/decoding contributions of AC itself?

The claim that the behavioral performance reduction is not reflected in brainstem activity is intriguing but perhaps premature. The main question is what the population activity observed with ABRs and EFRs actually tells us about the local activity of several stations. The summated activity is certainly significantly affected by the degree of synchrony within and across those stations, potentially obscuring subpopulation contributions and firing rate modulations which were the key to the observations in AC. Also, the brainstem responses were not obtained while the animals where performing the task. This may not be necessary to make the point that brainstem activity is seemingly not affected by the hearing loss but further dissociates the two main parts of the study.

Reviewer #2:

This is a great paper, where the authors investigate the effect of a conductive hearing loss on brainstem processing, cortical responses, and perceptual deficits. They focus on two primary results. The first is that conductive hearing loss leads to a reduction in performance on an auditory detection task, with no alteration in brainstem temporal processing. The second is that perceptual deficits were associated with a degraded population code.

Overall, I think it's a lovely paper, and worthy of publication in eLife. I do have some specific comments that I feel will improve the quality of the paper.

1) There are a number of different factors that could alter sound responses in this kind of task. Could you please provide details as to the size of the behavioral apparatus, and comment on the following issues? Specifically since there is only one speaker, the sound path to the animals ear will change as the animal navigates. What is the natural variability in neural responses that you would expect from roaming in such an environment (compared to what you observed in the group differences)? Locomotion effects might also change both firing rate and response variability. Were there systematic differences in the way in which the different groups moved around the arena?

2) "ABR thresholds to clicks, which is a general measure of hearing threshold…". And all other references to ABR's reflecting hearing. There has been work showing that ABRs do not really measure "hearing", they measure brainstem function. Chambers et al. (2016) have shown that lesioning >95% of cochlear afferent synapses can virtually eliminate the ABR but leave tone detection behavior completely normal. It would be nice to make this point clear in the paper.

3) Statistics used should be related to the way the data is presented. As an example, the data in Figure 6D shows median value for the two groups, but the statistical test used does not test for a difference in median. The KS test tests whether the underlying probability distributions differ, and it does this by calculating the KS statistic from the CDF's (so this test is more appropriate when directly comparing CDFs in Figure 6). If the point is to be made that there is a difference in median, then perhaps something like a Wilcoxon Rank Sum test would be a better choice.

4) Population decoding performance normally scales with the number of neurons in the population. Is this the case in your data? And, if so, can you control for this when comparing decoder accuracy between groups of different sizes?

5) You've shown an interesting change in variability between groups, but I wonder whether there may also be differences in co-variability between groups. Have you looked at noise correlations at all (between simultaneously recorded units)? If there was a difference between groups, then the importance of noise correlations could also be studied with the population decoder by shuffling the trial order.

6) With regards to Figure 6A. This figure is showing CDFs of firing rates between groups of animals. I don't think you mention anywhere what the individual animal N is. Could you please provide evidence that this between group difference isn't being driven by a particular (or small group) of animals. This could be achieved (for example) by constructing a bootstrapped statistical test, whereby the same N was drawn repeatedly from each animal. Could you also please show the data that these differences (in FR and CV) holds up for single-units?

Reviewer #3:

In this study, the authors investigate the behavioural and neurophysiological consequences of a permanent developmental conductive hearing loss in gerbils. Unlike previous studies of this topic, the authors are able to record from auditory cortical neurons whilst the animals perform a behavioural task. They find that animals reared with hearing loss are less sensitive to amplitude modulation of sounds, but only for faster modulation rates. A population decoder applied to cortical neurons shows a broadly similar deficit. The authors argue that this is because the responses of cortical neurons are more variable across trials in animals reared with hearing loss. Auditory brainstem responses (specifically the envelope following response) do not show a deficit in animals reared with hearing loss. The authors therefore conclude that the behavioural deficit in temporal processing emerges above the level of the brainstem, perhaps even in the cortex itself.

Overall, the authors should be commended for tackling an important topic using an ambitious and novel methodological approach that produces an interesting set of results. However, there are a couple of areas that could be written more clearly or need additional detail. There are also a number of important differences between the behavioural and neurophysiological data, and it would be helpful to identify these clearly and discuss their implications at greater length.

The methods used for population decoding need to be explained more clearly and in greater detail.

Although the population decoder data share certain features with the behavioural data, there are also a number of important differences. These need to be clarified and discussed at greater length. Estimating thresholds from non-monotonic data, or data that do not cross threshold, also poses a considerable problem that needs to be discussed. Without a consideration of these issues, it is difficult to fully assess the degree of similarity between the behavioural and neurophysiological data.

It would also be helpful to discuss the results in the context of previous anaesthetized work.
