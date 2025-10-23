# Peer review - Round 1

Editors:
- Supratim Ray, https://ror.org/04dese585 Indian Institute of Science India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72139.sa0](https://doi.org/10.7554/eLife.72139.sa0)

By combining rare EEG and laminar recordings in monkeys, Westerberg and colleagues studied the neural correlates of the well-known attention-related N2pc signal and found that it is due to the activation of extra-granular layers of cortex. Further, this effect was stronger for columns that were more feature selective. These findings are extremely important and a unique contribution to the literature on the neurobiology of attention.


---

# Peer review - Round 1

Editors:
- Supratim Ray, https://ror.org/04dese585 Indian Institute of Science India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72139.sa1](https://doi.org/10.7554/eLife.72139.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Laminar microcircuitry of visual cortex producing attention-associated electric fields" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Chris Baker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Steven J. Luck (Reviewer #2); Anirvan S Nandy (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Effects of attention in V4 generally start earlier (~100 ms). It is unclear why no effect is observed during earlier time periods in these data. To make better comparison with previous studies (such as Nandy et al., 2017), the authors should show the average PSTHs in supragranular, granular and infragranular layers during both target-out versus target-in conditions. Interestingly, Nandy and colleagues found largest changes in firing rates in the granular layer. To better understand the ERP outside the cortex, the authors should also show the average LFPs in the three layers, for target-in and target-out conditions. It is surprising that MI analysis reveals no significant information about the target in granular layer – given that some attentional effects are seen in upstream areas such as V1 and V2.

2. Eye position analysis: my understanding is that the animals could make a saccade as soon as the arrays were displayed. Given that the main effect of attention is observed after ~150-200 ms, the potential effect of saccade preparation could be important. There could also be small eye movements before the saccade. Given that the RFs were quite foveal for one monkey and not too far from the fixation window, and the effect of attention appears to be quite late, detailed analysis of eye position and microsaccades is needed to rule out the possibility of differences in eye movements between target in and target-out conditions influencing the results. A timeline and some analysis of eye movement patterns would be appropriate. The authors should also clearly mention the mean and SD of the saccade onset.

3. Attention studies typically keep the stimulus in the RF the same to tease out the effect of attention from stimulus selectivity. Ideally, the comparison should be between the two green (or red) in RF conditions as shown in Figure 4A. However, these results are shown only after pooling across all color selective columns. This comparison should be shown from Figure 2 itself (i.e., Figure 2C should have green in the RF and red target outside).

4. Information has been well characterized in a large number of previous studies (generally yielding values between a few bits/s, see for example, Reich et. al, 2001, JNP). Here, the absolute value of mutual information seems rather low. This may be due to the way the information is computed. A discussion about these reasons would be useful for scientists interested in information-theoretic measures.

5. Dependence on feature preference: The effect of spatial and feature attention is well studied. (A multiplicative gain model of spatial attention would predict a larger increase in firing rates and perhaps other signals such as CSD) for preferred versus non-preferred signals. Feature similarity gain model would predict the red preferring columns to increase their activity and green preferring columns to reduce their activity when the animal is attending to the feature red, irrespective of which stimulus is in the receptive field. Here, the task is a pop-out task which likely has both a spatial and feature attention component. The authors should discuss their findings in these contexts. Further, the authors should discuss whether their findings could just be a reflection of the magnitude of the change (which could be larger for preferred versus non-preferred stimulus). The information-theoretic measure should ideally not depend on the absolute magnitude, but these quantities often get biased in non-trivial ways based on the magnitude. Does information transmission depend on the magnitudes of firing rates/CSDs?

6. For columns that were not feature selective, is there an effect of attention? Does the magnitude of N2pc change depend on color selectivity? I think that should be the case based on Figure 4H and 4I, but a plot and/or some quantification would be useful.

7. The most challenging aspect of the study is to provide a solid link from the intracortical activity to the voltage on the cortical surface, and then to the monkey scalp ERPs, and finally to human ERPs. Toward that end, the present study relied entirely on correlational evidence, rather than experimental manipulations. That's quite appropriate for a first step, but it must be considered an important limitation on the conclusions that can be drawn. It would be wonderful if future research took the next step of providing experimental evidence.

8. There are also some troubling aspects of the existing evidence. The scalp ERP effect in this study, and the prior work from this group, is a positive voltage over the contralateral hemisphere, whereas in humans the voltage is negative. This may well reflect the orientation of the relevant cortical surface in monkeys versus humans. However, the voltage on the cortical surface in the present study was negative contralateral to the target, not positive. Unless this opposite voltage on the cortical surface relative to the scalp reflects something about the reference site for the cortical surface electrode, then this makes it difficult to link the intracortical effects and cortical surface effects to the scalp ERP effects. Also, the CSD was negative in the upper layers and positive in the lower layers, again suggesting that the voltage should be negative contralateral to the target on the surface. Ironically, this polarity is what would be expected from the human brain, where a contralateral negativity is observed. The oddity seems to be the contralateral positivity in the monkey scalp data. Also, the cortical surface voltage exhibits a polarity reversal at approximately 180 ms, which is not seen in the intracortical CSD. One possible explanation for the discrepancy is that the scalp voltage likely comes from multiple brain areas besides V4. If, for example, areas on the ventral surface of the occipital and temporal lobes produce stronger scalp voltages than V4 under the present conditions, the opposite orientation of these areas relative to the cortical surface would be expected to produce a positive voltage at the scalp electrodes. The manuscript notes that multiple areas probably contribute to the scalp ERPs and argues that the pattern of intracortical CSD results obtained in V4 will likely generalize to those areas. That seems quite plausible. Moreover, the results are interesting independent of their link to scalp ERPs. Thus, the present results are important even if the scalp polarity issue cannot be definitively resolved at this time.

9. There are also some significant concerns about the filters. The high-pass cutoff was high enough that it could have produced artifactual opposite polarity deflections in the data. If causal filters were applied (e.g., in hardware during the recordings), these artifactual deflections would have been after rather than before the initial deflection, possibly explaining the polarity reversal at 180 ms. If noncausal filters were applied in software, this would be a larger problem and could produce artifacts at both the beginning and end of the waveform. Moreover, the filters were different for the CSD data and the extracortical voltages, which is somewhat problematic for the information theoretic comparisons of these two data sources (but is likely to reduce rather than inflate the effects).

The filter for the intracranial recordings was listed as "0.1-12kHz". Was the high pass cutoff really at 0.1 kHz (100 Hz), or was it supposed to be 0.1 Hz to 12 kHz? A cutoff at 100 Hz would make it impossible to see field potentials corresponding to the N2pc. For the extracortical electrode, the 1 Hz cutoff is still quite high. I think you'd need to show how it impacts an N2pc-like artificial waveform (e.g., one half cycle of a 5 Hz sine wave) so that the effects of the filter on the observed data can be estimated. Also, the authors might want to apply offline filters so that the same effective bandpass is used for the extracortical voltage and the intracortical CSD. (This could be shown in a supplemental figure.)

10. The method section states correctly that "current sinks following visual stimulation first appear in the granular input layer of the cortex, then ascend and descend to extra granular compartments". However in the example CSDs shown in Figure 2, Figure 3, Figure S3 there is no visible current sink in the infra-granular layers. Instead, the identified infra-granular layers show a prolonged current source (e.g. Figure S5B,C), which is unexpected. Can the authors comment on this discrepancy?

11. The example RF profile shown in Figure S5A, although aligned, looks a little strange in that the RFs taper off rapidly in the infra-granular layer. Is this the best representative example? It will be important to see other examples of RF alignment.

12. The study used LFP power in the gamma range to compute the response ratio between red and green stimuli. LFPs measured across the cortical depth are highly correlated, and so would gamma power estimated from the LFPs. Given this, how meaningful is the laminar analysis shown in Figure 4B? How confidently can it be established that the LFP derived gamma power estimates have laminar specificity?
