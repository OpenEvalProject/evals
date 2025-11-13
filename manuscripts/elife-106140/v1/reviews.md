# Peer review - Round 1

Editors:
- Redmond G O'Connell, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106140.3.sa0](https://doi.org/10.7554/eLife.106140.3.sa0)

This work presents important information on rhythmicity of overlapping target and distractor processing and how this affects behaviour. The methods are, in general, clearly laid out and defensible, with several supplementary analyses leading to a solid base of evidence for their claims.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106140.3.sa1](https://doi.org/10.7554/eLife.106140.3.sa1)

Summary:

Using a combination of EEG and behavioural measurements, the authors investigate the degree to which processing of spatially-overlapping targets (coherent motion) and distractors (affective images) are sampled rhythmically and how this affects behaviour. They found that both target processing (via measurement of amplitude modulations of SSVEP amplitude to target frequency) and distractor processing (via MVPA decoding accuracy of bandpassed EEG relative to distractor SSVEP frequency) displayed a pronounced rhythm at ~1Hz, time-locked to stimulus onset. Furthermore, the relative phase of this target/distractor sampling predicted accuracy of coherent motion detection across participants.

Strengths:

- The authors are addressing a very interesting question with respect to sampling of targets and distractors, using neurophysiological measurements to their advantage in order to parse out target and distractor processing.

- The general EEG analysis pipeline is sensible and well-described.

- The main result of rhythmic sampling of targets and distractors is striking and very clear even on a participant-level.

- The authors have gone to quite a lot of effort to ensure the validity of their analyses, especially in the Supplementary Material.

- It is incredibly striking how the phase of both target and distractor processing are so aligned across trials for a given participant. I would have thought that any endogenous fluctuation in attention or stimulus processing like that would not be so phase aligned. I know there is literature on phase resetting in this context, the results seem very strong here and it is worth noting. The authors have performed many analyses to rule out signal processing artifacts, e.g. the sideband and beating frequency analyses.

Weaknesses:

- In general, the representation of target and distractor processing is a bit of a reach. Target processing is represented by SSVEP amplitude, which is going to most likely be related to the contrast of the dots, as opposed to representing coherent motion energy which is the actual target. These may well be linked (e.g. greater attention to the coherent motion task might increase SSVEP amplitude) but I would call it a limitation of the interpretation. Decoding accuracy of emotional content makes sense as a measure of distractor processing, and the supplementary analysis comparing target SSVEP amplitude to distractor decoding accuracy is duly noted. Overall, this limitation remains and has been noted in the Limitations section.

- Then comparing SSVEP amplitude to emotional category decoding accuracy feels a bit like comparing apples with oranges. They have different units and scales and reflect probably different neural processes. Is the result the authors find not a little surprising in this context? This relationship does predict performance and is thus intriguing, but I think this methodological aspect needs to be discussed further. For example, is the phase relationship with behaviour a result of a complex interaction between different levels of processing (fundamental contrast vs higher order emotional processing)? Again, this has been noted in the Limitations section, but changing the data to z-scores doesn't really take care of the conceptual issue, i.e. that on-screen contrast changes would necessarily be distracting during emotional category decision-making.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106140.3.sa2](https://doi.org/10.7554/eLife.106140.3.sa2)

In this study, Xiong et al. investigate whether rhythmic sampling - a process typically observed in the attended processing of visual stimuli - extends to task-irrelevant distractors. By using EEG with frequency tagging and multivariate pattern analysis (MVPA), they aimed to characterize the temporal dynamics of both target and distractor processing and examine whether these processes oscillate in time. The central hypothesis is that target and distractor processing occur rhythmically, and the phase relationship between these rhythms correlates with behavioral performance.

Major Strengths

(1) The extension of rhythmic attentional sampling to include distractors is a novel and interesting question.

(2) The decoding of emotional distractor content using MVPA from SSVEP signals is an elegant solution to the problem of assessing distractor engagement in the absence of direct behavioral measures.

(3) The finding that relative phase (between 1 Hz target and distractor processes) predicts behavioral performance is compelling.

Major Weaknesses and Limitations

(1) The central claim of 1 Hz rhythmic sampling is insufficiently validated. The windowing procedure (0.5s windows with 0.25s step) inherently restricts frequency resolution, potentially biasing toward low-frequency components like 1 Hz. Testing different window durations or providing controls would significantly strengthen this claim.

(2) The study lacks a baseline or control condition without distractors. This makes it difficult to determine whether the distractor-related decoding signals or the 1 Hz effect reflect genuine distractor processing or more general task dynamics.

(3) The pairwise decoding accuracies for distractor categories hover close to chance (~55%), raising concerns about robustness. While statistically above chance, the small effect sizes need careful interpretation, particularly when linked to behavior.

(4) Neither target nor distractor signal strength (SSVEP amplitude) correlates with behavioral accuracy. The study instead relies heavily on relative phase, which-while interesting-may benefit from additional converging evidence.

(5) Phase analysis is performed between different types of signals hindering their interpretability (time-resolved SSVEP amplitude and time-resolved decoding accuracy).

The authors largely achieved their stated goal of assessing rhythmic sampling of distractors. However, the conclusions drawn - particularly regarding the presence of 1 Hz rhythmicity - rest on analytical choices that should be scrutinized further. While the observed phase-performance relationship is interesting and potentially impactful, the lack of stronger and convergent evidence on the frequency component itself reduces confidence in the broader conclusions.

If validated, the findings will advance our understanding of attentional dynamics and competition in complex visual environments. Demonstrating that ignored distractors can be rhythmically sampled at similar frequencies to targets has implications for models of attention and cognitive control. However, the methodological limitations currently constrain the paper's impact.

Additional Considerations

• The use of EEG-fMRI is mentioned but not leveraged. If BOLD data were collected, even exploratory fMRI analyses (e.g., distractor modulation in visual cortex) could provide valuable converging evidence.

• In turn, removal of fMRI artifacts might introduce biases or alter the data. For instance, the authors might consider investigating potential fMRI artifact harmonics around 1 Hz to address concerns regarding induced spectral components.

Comments on revisions:

The authors have addressed my previous points, and the manuscript is substantially improved. The key methodological clarifications have been incorporated, and the interpretation of findings has been appropriately moderated. I have no further major concerns.
