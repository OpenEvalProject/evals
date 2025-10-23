# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.102475.4.sa0](https://doi.org/10.7554/eLife.102475.4.sa0)

This valuable study asks how the neural representation of individual finger movements changes during the early periods of sequence learning. By combining a new method for extracting features from human magnetoencephalography data and decoding analyses, the authors provide solid evidence of an early, swift change in the brain regions correlated with sequence learning, including a set of previously unreported frontal cortical regions. The authors also show that offline contextualization during short rest periods is the basis for improved performance. Further confirmation of these results on multiple movement sequences would further strengthen the key claims.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102475.4.sa1](https://doi.org/10.7554/eLife.102475.4.sa1)

Summary:

This study addresses the issue of rapid skill learning and whether individual sequence elements (here: finger presses) are differentially represented in human MEG data. The authors use a decoding approach to classify individual finger elements, and accomplish an accuracy of around 94%. A relevant finding is that the neural representations of individual finger elements dynamically change over the course of learning. This would be highly relevant for any attempts to develop better brain machine interfaces - one now can decode individual elements within a sequence with high precision, but these representations are not static but develop over the course of learning.

Strengths:

The work follows from a large body of work from the same group on the behavioural and neural foundations of sequence learning. The behavioural task is well established a neatly designed to allow for tracking learning and how individual sequence elements contribute. The inclusion of short offline rest periods between learning epochs has been influential because it has revealed that a lot, if not most of the gains in behaviour (ie speed of finger movements) occur in these so-called micro-offline rest periods.

The authors use a range of new decoding techniques, and exhaustively interrogate their data in different ways, using different decoding approaches. Regardless of the approach, impressively high decoding accuracies are observed, but when using a hybrid approach that combines the MEG data in different ways, the authors observe decoding accuracies of individual sequence elements from the MEG data of up to 94%.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102475.4.sa2](https://doi.org/10.7554/eLife.102475.4.sa2)

Summary:

The current paper consists of two parts. The first part is the rigorous feature optimization of the MEG signal to decode individual finger identity performed in a sequence (4-1-3-2-4; 1~4 corresponds to little~index fingers of the left hand). By optimizing various parameters for the MEG signal, in terms of (i) reconstructed source activity in voxel- and parcel-level resolution and their combination, (ii) frequency bands, and (iii) time window relative to press onset for each finger movement, as well as the choice of decoders, the resultant "hybrid decoder" achieved extremely high decoding accuracy (~95%).

In the second part of the paper, armed with the successful 'hybrid decoder,' the authors asked how neural representation of individual finger movement that is embedded in a sequence, changes during a very early period of skill learning and whether and how such representational change can predict skill learning. They assessed the difference in MEG feature patterns between the first and the last press 4 in sequence 41324 at each training trial and found that the pattern differentiation progressively increased over the course of early learning trials. Additionally, they found that this pattern differentiation specifically occurred during the rest period rather than during the practice trial. With a significant correlation between the trial-by-trial profile of this pattern differentiation and that for accumulation of offline learning, the authors argue that such "contextualization" of finger movement in a sequence (e.g., what-where association) underlies the early improvement of sequential skill. This is an important and timely topic for the field of motor learning and beyond.

Strengths:

The use of temporally rich neural information (MEG signal) has a significant advantage over previous studies testing sequential representations using fMRI. This allowed the authors to examine the earliest period (= the first few minutes of training) of skill learning with finer temporal resolution. Through the optimization of MEG feature extraction, the current study achieved extremely high decoding accuracy (approx. 94%) compared to previous works. The finding of the early "contextualization" of the finger movement in a sequence and its correlation to early (offline) skill improvement is interesting and important. The comparison between "online" and "offline" pattern distance is a neat idea.

Weaknesses:

One potential weakness, in terms of the generality, is that the study assessed the single sequence, the "41324" across all participants. Future confirmation test of using different sequences would be important.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102475.4.sa3](https://doi.org/10.7554/eLife.102475.4.sa3)

Summary:

One goal of this paper is to introduce a new approach for highly accurate decoding of finger movements from human magnetoencephalography data via dimension reduction of a "multi-scale, hybrid" feature space. Following this decoding approach, the authors aim to show that early skill learning involves "contextualization" of the neural coding of individual movements, relative to their position in a sequence of consecutive movements. Furthermore, they aim to show that this "contextualization" develops primarily during short rest periods interspersed with skill training, and correlates with a performance metric which the authors interpret as an indicator of offline learning.

Strengths:

A strength of the paper is the innovative decoding approach, which achieves impressive decoding accuracies via dimension reduction of a "multi-scale, hybrid space". This hybrid-space approach follows the neurobiologically plausible idea of concurrent distribution of neural coding across local circuits as well as large-scale networks.

Weaknesses:

A clear weakness of the paper lies in the authors' conclusions regarding "contextualization". Several potential confounds, which partly arise from the experimental design, and which are described below, question the neurobiological implications proposed by the authors, and offer a simpler explanation of the results. Furthermore, the paper follows the assumption that short breaks result in offline skill learning, while recent evidence casts doubt on this assumption.

Specifically:

The authors interpret the ordinal position information captured by their decoding approach as a reflection of neural coding dedicated to the local context of a movement (Figure 4). One way to dissociate ordinal position information from information about the moving effectors is to train a classifier on one sequence, and test the classifier on other sequences that require the same movements, but in different positions (Kornysheva et al., Neuron 2019). In the present study, however, participants trained to repeat a single sequence (4-1-3-2-4). As a result, ordinal position information is potentially confounded by the fixed finger transitions around each of the two critical positions (first and fifth press). Across consecutive correct sequences, the first keypress in a given sequence was always preceded by a movement of the index finger (=last movement of the preceding sequence), and followed by a little finger movement. The last keypress, on the other hand, was always preceded by a ring finger movement, and followed by an index finger movement (=first movement of the next sequence). Figure 3 - supplement 5 shows that finger identity can be decoded with high accuracy (>70%) across a large time window around the time of the keypress, up to at least {plus minus}100 ms (and likely beyond, given that decoding accuracy is still high at the boundaries of the window depicted in that figure). This time window approaches the keypress transition times in this study. Given that distinct finger transitions characterized the first and fifth keypress, the classifier could thus rely on persistent (or "lingering") information from the preceding finger movement, and/or "preparatory" information about the subsequent finger movement, in order to dissociate the first and fifth keypress. Currently, the manuscript provides little evidence that the context information captured by the decoding approach is more than a by-product of temporally extended, and therefore overlapping, but independent neural representations of consecutive keypresses that are executed in close temporal proximity - rather than a neural representation dedicated to context.

During the review process, the authors pointed out that a "mixing" of temporally overlapping information from consecutive keypresses, as described above, should result in systematic misclassifications and therefore be detectable in the confusion matrices in Figures 3C and 4B, which indeed do not provide any evidence that consecutive keypresses are systematically confused. However, such absence of evidence (of systematic misclassification) should be interpreted with caution. The authors also reported that there was only a weak relation between inter-press intervals and "online contextualization" (Figure 5 - figure supplement 6), however, their analysis suprisingly includes a keypress transition that is shared between OP1 and OP5 ("4-4"), rather than focusing solely on the two distinctive transitions ("2-4" and "4-1").

Such temporal overlap of consecutive, independent finger representations may also account for the dynamics of "ordinal coding"/"contextualization", i.e., the increase in 2-class decoding accuracy, across Day 1 (Figure 4C). As learning progresses, both tapping speed and the consistency of keypress transition times increase (Figure 1), i.e., consecutive keypresses are closer in time, and more consistently so. As a result, information related to a given keypress is increasingly overlapping in time with information related to the preceding and subsequent keypresses. Furthermore, learning should increase the number of (consecutively) correct sequences, and, thus, the consistency of finger transitions. Therefore, the increase in 2-class decoding accuracy may simply reflect an increasing overlap in time of increasingly consistent information from consecutive keypresses, which allows the classifier to dissociate the first and fifth keypress more reliably as learning progresses, simply based on the characteristic finger transitions associated with each. In other words, given that the physical context of a given keypress changes as learning progresses - keypresses move closer together in time, and are more consistently correct - it seems problematic to conclude that the mental representation of that context changes. During the review process, authors pointed at absence of evidence of a relation between tapping speed and "ordinal coding" (Figure 5 - figure supplement 7). However, a rigorous test of the idea that the mental representation of context changes would require a task design in which the physical context remains constant.

A similar difference in physical context may explain why neural representation distances ("differentiation") differ between rest and practice (Figure 5). The authors define "offline differentiation" by comparing the hybrid space features of the last index finger movement of a trial (ordinal position 5) and the first index finger movement of the next trial (ordinal position 1). However, the latter is not only the first movement in the sequence, but also the very first movement in that trial (at least in trials that started with a correct sequence), i.e., not preceded by any recent movement. In contrast, the last index finger of the last correct sequence in the preceding trial includes the characteristic finger transition from the fourth to the fifth movement. Thus, there is more overlapping information arising from the consistent, neighbouring keypresses for the last index finger movement, compared to the first index finger movement of the next trial. A strong difference (larger neural representation distance) between these two movements is, therefore, not surprising, given the task design, and this difference is also expected to increase with learning, given the increase in tapping speed, and the consequent stronger overlap in representations for consecutive keypresses.

A further complication in interpreting the results stems from the visual feedback that participants received during the task. Each keypress generated an asterisk shown above the string on the screen. It is not clear why the authors introduced this complicating visual feedback in their task, besides consistency with their previous studies. The resulting systematic link between the pattern of visual stimulation (the number of asterisks on the screen) and the ordinal position of a keypress makes the interpretation of "contextual information" that differentiates between ordinal positions difficult. While the authors report the surprising finding that their eye-tracking data could not predict asterisk position on the task display above chance level, the mean gaze position seemed to vary systematically as a function of ordinal position of a movement - see Figure 4 - figure supplement 3.

The authors report a significant correlation between "offline differentiation" and cumulative micro-offline gains. However, to reach the conclusion that "the degree of representational differentiation -particularly prominent over rest intervals - correlated with skill gains.", the critical question is rather whether "offline differentiation" correlates with micro-offline gains (not with cumulative micro-offline gains). That is, does the degree to which representations differentiate "during" a given rest period correlate with the degree to which performance improves from before to after the same rest period (not: does "offline differentiation" in a given rest period correlate with the degree to which performance has improved "during" all rest periods up to the current rest period - but this is what Figure 5 - figure supplements 1 and 4 show).

The authors follow the assumption that micro-offline gains reflect offline learning. However, there is no compelling evidence in the literature, and no evidence in the present manuscript, that micro-offline gains (during any training phase) reflect offline learning. Instead, emerging evidence in the literature indicates that they do not (Das et al., bioRxiv 2024), and instead reflect transient performance benefits when participants train with breaks, compared to participants who train without breaks, however, these benefits vanish within seconds after training if both groups of participants perform under comparable conditions (Das et al., bioRxiv 2024). During the review process, the authors argued that differences in the design between Das et al. (2024) on the one hand (Experiments 1 and 2), and the study by Bönstrup et al. (2019) on the other hand, may have prevented Das et al. (2024) from finding the assumed (lasting) learning benefit by micro-offline consolidation. However, the Supplementary Material of Das et al. (2024) includes an experiment (Experiment S1) whose design closely follows the early learning phase of Bönstrup et al. (2019), and which, nevertheless, demonstrates that there is no lasting benefit of taking breaks for the acquired skill level, despite the presence of micro-offline gains.

Along these lines, the authors argue that their practice schedule "minimizes reactive inhibition effects", in particular their short practice periods of 10 seconds each. However, 10 seconds are sufficient to result in motor slowing, as report in Bächinger et al., elife 2019, or Rodrigues et al., Exp Brain Res 2009.

An important conceptual problem with the current study is that the authors conclude that performance improves, and representation manifolds differentiate, "during" rest periods. However, micro-offline gains (as well as offline contextualization) are computed from data obtained during practice, not rest, and may, thus, just as well reflect a change that occurs "online", e.g., at the very onset of practice (like pre-planning) or throughout practice (like fatigue, or reactive inhibition).

The authors' conclusion that "low-frequency oscillations (LFOs) result in higher decoding accuracy compared to other narrow-band activity" should be taken with caution, given that the critical decoding analysis for this conclusion was based on data averaged across a time window of 200 ms (Figure 2), essentially smoothing out higher frequency components.
