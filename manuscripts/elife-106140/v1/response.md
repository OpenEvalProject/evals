# Author response - Round 1

Authors:
- Changhao Xiong ([ORCID: 0009-0008-2766-8373](https://orcid.org/0009-0008-2766-8373))
- Nathan M Petro ([ORCID: 0000-0002-7553-4459](https://orcid.org/0000-0002-7553-4459))
- Ke Bo ([ORCID: 0000-0003-3286-7891](https://orcid.org/0000-0003-3286-7891))
- Lihan Cui ([ORCID: 0000-0001-7722-3550](https://orcid.org/0000-0001-7722-3550))
- Andreas Keil ([ORCID: 0000-0002-4064-1924](https://orcid.org/0000-0002-4064-1924))
- Mingzhou Ding ([ORCID: 0000-0002-1024-3503](https://orcid.org/0000-0002-1024-3503))

## Response text

DOI: [10.7554/eLife.106140.3.sa3](https://doi.org/10.7554/eLife.106140.3.sa3)

The following is the authors’ response to the original reviews

Reviewer 1:

(1) In general, the representation of target and distractor processing is a bit of a reach. Target processing is represented by SSVEP amplitude, which is most likely going to be related to the contrast of the dots, as opposed to representing coherent motion energy, which is the actual target. These may well be linked (e.g., greater attention to the coherent motion task might increase SSVEP amplitude), but I would call it a limitation of the interpretation. Decoding accuracy of emotional content makes sense as a measure of distractor processing, and the supplementary analysis comparing target SSVEP amplitude to distractor decoding accuracy is duly noted.

We agree with the reviewer. The SSVEP amplitude of the target at the whole trial level indeed reflected the combined effect of the stimulus parameters (e.g., contrast of the moving dots) as well as attention. However, the time course of the target SSVEP amplitude within a trial, derived from the moving window analysis, reflected the temporal fluctuations of target processing, since the stimulus parameters remained the same during the trial. We now make this clearer in the revised manuscript.

(2) Comparing SSVEP amplitude to emotional category decoding accuracy feels a bit like comparing apples with oranges. They have different units and scales and probably reflect different neural processes. Is the result the authors find not a little surprising in this context? This relationship does predict performance and is thus intriguing, but I think this methodological aspect needs to be discussed further. For example, is the phase relationship with behaviour a result of a complex interaction between different levels of processing (fundamental contrast vs higher order emotional processing)?

Traditionally, the SSVEP amplitude at the distractor frequency is used to quantify distractor processing. Given that the target SSVEP amplitude is stronger than that of the distractor, it is possible that the distractor SSVEP amplitude is contaminated by the target SSVEP amplitude due to spectral power leakage; see Figure S4 for a demonstration of this. Because of this issue we therefore introduced the use of decoding accuracy as an index of distractor processing. The lack of correlation between the distractor SSVEP amplitude and the distractor decoding accuracy, although it is kind of like comparing apples with oranges as pointed out by the reviewer, serves the purpose of showing that these two measures are not co-varying, and the use of decoding accuracy is free from the influence of the distractor SSVEP amplitude which is influenced by the target SSVEP amplitude. Also, to address the apples-vs-oranges issue, the correlation was computed on normalized time series, in which a z-score time series replaced the original time series so that the correlated variables are dimensionless. Regarding the question of assessing the relation between behavior and different levels of processing, we do not have means to address it, given that we are not able to empirically separate the effects of stimulus parameters versus attention.

Reviewer 2:

(1) Incomplete Evidence for Rhythmicity at 1 Hz: The central claim of 1 Hz rhythmic sampling is insufficiently validated. The windowing procedure (0.5s windows with 0.25s step) inherently restricts frequency resolution, potentially biasing toward low-frequency components like 1 Hz. Testing different window durations or providing controls would significantly strengthen this claim.

We appreciate the reviewer’s insightful suggestion. In response, we tested different windowing parameters, e.g., 0.1s sliding window with a 0.05s step size. Figure S5 demonstrates that the strength of both target and distractor processing fluctuates around ~1 Hz, both at the individual and group levels. Additionally, Figures S6(A) and S6(B) show that the relative phase between target and distractor processing time series exhibits a uniform distribution across subjects. In terms of the relation between relative phase and behavior, Figure S6(C) illustrates two representative cases: a high-performing subject with 84.34% task accuracy exhibited a relative phase of 0.9483π (closer to π), while a low-performing subject with 30.95% accuracy showed a phase of 0.29π close to 0. At the group level, a significant positive correlation between relative phase and task performance was found (r = 0.6343, p = 0.0004), as shown in Figure S6(D). All these results, aligning closely with our original findings (0.5s window length and 0.25s step size), suggest that the conclusions are not dependent on windowing parameters. We discuss these results in the revised manuscript.

To further validate our findings, we also employed the Hilbert transform to extract amplitude envelopes of the target and distractor signals on a time-point-by-time-point basis, providing a window-free estimate of signal strength (Figures R3 and R4). The results remain consistent with both the original findings and the new sliding window analyses (Figure S6). Specifically, Figure S7 reveals ~1 Hz fluctuations in target and distractor processing at both individual and group levels. Figures S8(A) and S8(B) confirm a uniform distribution of the relative phase across subjects. In Figure S8(C), the relative phase was 0.9567π for a high-performing subject (84.34% accuracy) and 0.2247π for a low-performing subject (28.57% accuracy). At the group level, a significant positive correlation was again observed between relative phase and task performance (r = 0.4020, p = 0.0376), as shown in Figure S8(D).

(2) No-Distractor Control Condition: The study lacks a baseline or control condition without distractors. This makes it difficult to determine whether the distractor-related decoding signals or the 1 Hz effect reflect genuine distractor processing or more general task dynamics.

The lack of a no-distractor control condition is certainly a limitation and will be acknowledged as such in the revised manuscript. However, given that our decoding results are between two different classes of distractors, we are confident that they reflect distractor processing.

(3) Decoding Near Chance Levels: The pairwise decoding accuracies for distractor categories hover close to chance (~55%), raising concerns about robustness. While statistically above chance, the small effect sizes need careful interpretation, particularly when linked to behavior.

This is an important point. To test robustness, we have implemented a random permutation procedure in which trial labels were randomly shuffled to construct a nullhypothesis distribution for decoding accuracy. We then compared the decoding accuracy from the actual data to this distribution. Figure S9 shows the results based on 1,000 permutations. For each of the three pairwise classifications—pleasant vs. neutral, unpleasant vs. neutral, and pleasant vs. unpleasant—as well as the three-way classification, the actual decoding accuracies fall far outside the null-hypothesis distribution (p < 0.001), and the effect size in all four cases is extremely large. These findings indicate that the observed decoding accuracies are statistically significant and robust in terms of both statistical inference and effect size.

(4) No Clear Correlation Between SSVEP and Behavior: Neither target nor distractor signal strength (SSVEP amplitude) correlates with behavioral accuracy. The study instead relies heavily on relative phase, which - while interesting - may benefit from additional converging evidence.

We felt that what the reviewer pointed out is actually the main point of our study, namely, it is not the target or distractor strength over the whole trial that matters for behavior, it is their temporal relationship within the trial that matters for behavior. This reveals a novel neuroscience principle that has not been reported in the past. We have stressed this point further in the revised manuscript.

(5) Phase-analysis: phase analysis is performed between different types of signals hindering their interpretability (time-resolved SSVEP amplitude and time-resolved decoding accuracy).

The time-resolved SSVEP amplitude is used to index the temporal dynamics of target processing whereas the time-resolved decoding accuracy is used to index the temporal dynamics of distractor processing. As such, they can be compared, using relative phase for example, to examine how temporal relations between the two types of processes impact behavior. This said, we do recognize the reviewer’s concern that these two processes are indexed by two different types of signals. We thus normalized each time course using zscoring, making them dimensionless, and then computed the temporal relations between them.

Appraisal of Aims and Conclusions:

The authors largely achieved their stated goal of assessing rhythmic sampling of distractors. However, the conclusions drawn - particularly regarding the presence of 1 Hz rhythmicity - rest on analytical choices that should be scrutinized further. While the observed phaseperformance relationship is interesting and potentially impactful, the lack of stronger and convergent evidence on the frequency component itself reduces confidence in the broader conclusions.

Impact and Utility to the Field:

If validated, the findings will advance our understanding of attentional dynamics and competition in complex visual environments. Demonstrating that ignored distractors can be rhythmically sampled at similar frequencies to targets has implications for models of attention and cognitive control. However, the methodological limitations currently constrain the paper's impact.

Thanks for these comments and positive assessment of our work’s potential implications and impact. As indicated above, in the revision process, we have carried out a number of additional analyses, some suggested by the reviewers, and the results of the additional analyses, now included in the Supplementary Materials, served to further validate the main findings and strengthen our conclusions.

Additional Context and Considerations:

(1) The use of EEG-fMRI is mentioned but not leveraged. If BOLD data were collected, even exploratory fMRI analyses (e.g., distractor modulation in visual cortex) could provide valuable converging evidence.

Indeed, leveraging fMRI data in EEG studies would be very beneficial, as has been demonstrated in our previous work. However, given that this study concerns the temporal relationship between target and distractor processing, it is felt that fMRI data, which is known to possess low temporal resolution, has limited potential to contribute. We will be exploring this rich dataset in other ways in the future, where we will be integrating the two modalities for more insights that are not possible with either modality used alone.

(A) The amplitude time series of the 4.29 Hz component and the Fourier spectrum. (B) The group level Fourier spectrum. At both individual and group level, no 1 Hz modulation is observed, suggesting that the 1 Hz modulation observed in our data is not introduced by the artifact removal procedure.

(2) In turn, removal of fMRI artifacts might introduce biases or alter the data. For instance, the authors might consider investigating potential fMRI artifact harmonics around 1 Hz to address concerns regarding induced spectral components.

We have done extensive work in the area of simultaneous EEG-fMRI and have not encountered artifacts with a 1Hz rhythmicity. Our scanner artifact removal procedure is very standardized. As such, it stands to reason that if the 1Hz rhythmicity observed here results from the artifact removal process, it should also be present in other datasets where the same preprocessing steps were implemented. We tested this using another EEG-fMRI dataset (Rajan et al., 2019) . Author response image 1 shows that the EEG power time series of the new dataset doesn't have 1 Hz rhythmicity, whether at the individual level or at the group level, suggesting that the 1 Hz rhythmicity reported in the manuscript is not coming from the removal of the scanner artifacts, but instead reflects true rhythmic sampling of stimulus information. Also, the fact that the temporal relations between target processing and distractor processing at 1Hz impact behavior is another indication that the 1Hz rhythmicity is a neuroscientific effect, not an artifact.

References

Rajan, A., Siegel, S. N., Liu, Y., Bengson, J., Mangun, G. R., & Ding, M. (2019). Theta Oscillations Index Frontal Decision-Making and Mediate Reciprocal Frontal–Parietal Interactions in Willed Attention. Cerebral Cortex, 29(7), 2832–2843. https://doi.org/10.1093/cercor/bhy149
