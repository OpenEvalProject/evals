# Peer review - Round 1

Editors:
- Xiang Yu, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74998.sa0](https://doi.org/10.7554/eLife.74998.sa0)

This study by Kim et al. is of interest to neuroscientists studying neocortical neural activity, as related to social behavior and in mouse models of neuropsychiatric disorders. These results provide new data on how the loss of the postsynaptic scaffolding and adaptor protein IRSp53 impacts prefrontal cortex activity and social interaction in mice. The authors propose the interesting idea that suppressed neuronal activity dynamics and burst firing may contribute to the impaired cortical encoding of social information and social behaviors in IRSp53-mutant mice.


---

# Peer review - Round 1

Editors:
- Xiang Yu, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74998.sa1](https://doi.org/10.7554/eLife.74998.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Suppressed prefrontal neuronal firing variability and impaired social representation in IRSp53-mutant mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Catherine Dulac as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. More evidence of social impairments in IRSp53 KO mice. Based on the results of Figure 1, the authors stated that KO animals 'display social impairments', but this may not be the only interpretation of their data. In Figure 1E, time spent sniffing the objects during the first S-O session is not significantly different between wild-types and KOs, although variability is higher in KOs; similarly, social sniff times are also variable. Perhaps the KO animals have somewhat stronger sniffs, or are faster at processing the olfactory information, requiring them to spend less time sniffing and remaining in the in-zone. Please address this comment by providing further data demonstrating social impairments in KO mice.

2. Stronger evidence that the observed changes in firing rate really reflect differences in response to social and non-social targets in WT and IRSp53 KO mice. In the identified single-units in the mPFC of either WT or IRSp53 KO, only 10% were responsive to social and/or object targets, while 90% of the recorded units are not responsive to either target (Figure 7E). Consistently, the mean firing rate in E-E, fS-O and sS-O are similar in both WT and KO mice (Figure 3-supplement 1E), indicating that the presence of social targets had little effect in regulating most of the recorded mPFC neurons. Therefore, it is not convincing that the recorded mPFC neurons play an essential role in discriminating social targets. Please examine whether the FR range and burst firing proportion are different between WT and KO in resting and non-social conditions.

3. Suggestions for further data analysis. Perhaps moving the classification in Figure 7 to earlier in the manuscript, and analyzing firing rate statistics separately for 'social' vs 'non-social' neurons. Does unit classification (i.e., of 'social' or not) hold up across sessions or episodes of engagement within a session? If these really are 'social' units, presumably that aspect should be reliable across interactions with different mice.

4. Further analysis of firing rate data. To what extent are changes in the max firing rate during social task / the discrimination index explained by changes in bursting explain all of this? If one takes out the bursts, e.g., eliminate bursts in the spike trains – do changes in the discrimination index, etc. go away? Please also assess the proportion of social and object neurons in shuffled data to rule out the possibility that changes in the proportions of these neurons is due to nonspecific changes in activity. Other suggestions for further analysis include looking at single cell metrics, e.g., area under the receiver operator curve, mutual information, etc.

5. Cleaner analysis relating the unit spike trains to moment-to-moment features of social interaction or other behaviors occurring during the S-O sessions. The authors use machine learning to classify mouse part position, but only seem to mark where the mouse is in the track. The unit activity over time might be much more interesting if correlated with DeepLabCut-based analysis of what the animal was doing (or perhaps what the social interaction partner was doing) during the sessions. Please correlate behavior to activity, both of individual units and of simultaneously-recorded populations.

6. The authors found that the average resting firing rates of excitatory mPFC neurons in awake IRSp53-KO mice are larger than that in WT mice (Figure 1C and 1D). These results are opposite to their previous findings obtained from anaesthetized mice (Chung et al., 2015, Figure 8b and 8c). However, no such difference was observed between awake and anaesthetized WT animals. Please discuss.

7. Additional data on the contribution of NMDA receptors to observed changes in firing, Additional data on the effects of NMDAR antagonists could significantly strengthen the manuscript by potentially providing some mechanistic information and strengthening the correlation between changes in these physiological measures and changes in behavior. Please also provide some discussion about how increased NMDAR function or other neurobiological mechanisms cause decreased bursting.

8. Further discussion on social behavior deficits in IRSp53 KO mice and how components of excitatory synapses contribute to autism. While there may be few autism patients with IRSp53 mutations, IRSp53 is an important component of excitatory synapses. If IRSp53 KO mice have social deficits similar to autism-related genes with similar physiological functions, the findings of this study may have more general significance.

9. Further discussion on how changes in activity related to abnormal social behavior, or whether abnormal social behavior cause decreased release e.g., of a neuromodulator, that cause these changes in neural activity.

Reviewer #2 (Recommendations for the authors):

The broader significance of these findings is questionable because the relevance of this model to autism is unclear, the actual magnitudes of differences between genotypes are very small, and the relationship of changes in neural activity to either underlying mechanisms or behavior is unclear. When you put all of these things together, it's unclear how these findings lead to a general insight into how the brain works or autism. These issues could be addressed if a) the link between this gene and autism was much stronger, b) there was some exploration of the effects of NMDAR antagonists which reverse behavioral deficits such as memantine, and/or c) there was substantially greater exploration of how bursting contributes to encoding social information that lead to new insights into fundamental biology. As it stands, while I find the results interesting, it's hard to see what is the big insight that would justify publication in eLife vs. a more specialized neuroscience journal.

Additional comments:

1. There is a lot of discussion about 'decoding' but the authors do not actually examine this, e.g., by building a decoder, or even looking at single cell metrics, e.g., area under the receiver operator curve, mutual information, etc. This is critical because the dynamic range of a neuron is not the only determinant of how much information is transmitted about a stimulus. In particular, it is possible that decreased variability, either at the single cell or population level, compensates for changes in dynamic range (which are not accounted for in the discrimination index).

2. To what extent are changes in the max firing rate during social task / the discrimination index explained by changes in bursting explain all of this? What if you get rid of bursts, e.g., eliminate bursts in the spike trains – then do changes in the discrimination index, etc. go away?

3. Some intuition for / discussion about how increased NMDAR function or other neurobiological mechanisms cause decreased bursting is warranted.

4. As the authors allude to, it can be difficult to disentangle cause and effect in studies like this. E.g., are changes in activity a cause of abnormal social behavior, or does abnormal social behavior cause decreased release e.g., of a neuromodulator, that cause these changes in neural activity. This is very difficult to work out, and I don't think it is a fatal issue but some additional discussion / acknowledgement of this is warranted.

5. The authors might want to assess the proportion of social and object neurons in shuffled data to rule out the possibility that changes in the proportions of these neurons simply reflect nonspecific changes in activity. This does not seem to be the case because the proportion goes up for the empty chamber but it is easy enough to do this.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Suppressed prefrontal neuronal firing variability and impaired social representation in IRSp53-mutant mice" for further consideration by eLife. Your revised article has been evaluated by Catherine Dulac (Senior Editor) and a Reviewing Editor.

The manuscript has now been seen by all three previous reviewers. Reviewers 2 and 3 are satisfied with the revisions, while reviewer 1 suggested some additional analyses and text revisions.

Reviewer #1 (Recommendations for the authors):

I appreciate the significant effort the authors have put into addressing and analyzing the original concerns with this study. While the manuscript has been improved, some of my original concerns have not been fully addressed.

My original comment related to a decreased proportion of social neurons in the mPFC of IRSp53 KO mice (original Figure 7, now Figure 3) has not been appropriately addressed. I think using different z-score cut-offs to define social and object neurons is artificial. In Figures 3C and 3D, target shuffled data compared between WT and KO mice were significantly different, suggesting the comparison between non-linear fits could be oversensitive in revealing statistical significance that is unreal. Based on the data, I would suggest the authors perform an auROC analysis to define neurons responsive to either social or object cues (see Li et al., 2017 Cell from Catherine Dulac's lab).

The manuscript remains difficult to read and the rationale behind different analyses could be more clear. Some main figures describing similar changes could be combined while some non-essential results could be moved to supplementary.

Reviewer #2 (Recommendations for the authors):

The authors have responded to my comments in several ways including:

- Finding that social, but not nonsocial decoding is impaired in KO mice

- Showing how bursts vs. tonic firing contribute to altered firing and encoding related to social exploration

- Showing that the NMDA receptor antagonist memantine has opposing effects on burst firing in WT vs. KO mice

- Identifying social and object neurons based on shuffled data

Together, these additions address the major issues/suggestions I raised in my previous review.

Reviewer #3 (Recommendations for the authors):

I think the authors have done a good job responding to the earlier round of critiques. The new analyses are nice and directly address my concerns, especially on social behavior, with DLC, and on neural activity similarity across first and second S-O sessions.
