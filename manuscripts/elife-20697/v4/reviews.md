# Peer review - Round 1

Editors:
- Howard Eichenbaum, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20697.013](https://doi.org/10.7554/eLife.20697.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Synchronized excitability in a network enables generation of internal neuronal sequences" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Overall the reviewers found the study quite interesting and potentially important. However, there were also major concerns, especially about the method for detecting replay events and that ripple associated replay under MS inactivation alone is a rather expected result. Detailed comments are provided below.

Reviewer #1:

Yingxue, Roth, and Pastakova recorded spiking and local field potential data from CA1 in rats as they traversed an alternation task. The task required the animal to run on a 'running wheel' during the delay period. The authors have several main findings. First, they report that episode field sequences are replayed during sharp wave ripples with a similar consistency as place field sequences. Second, they show that muscimol inactivation of the medial septum (which reduces theta oscillations) did not block the occurrence of sharp wave ripples – in fact, the number of ripples increased. Third, they show that replay of place field sequences and episode field sequences were preserved during ripples in the muscimol condition (despite the disruption of episode field sequences during muscimol inactivation). Finally, the authors show that replay events of place field and episode field sequences are generally restricted to sharp wave ripple events.

In general I find the paper will be interesting to many, but I feel that the conclusions drawn by the authors about the role of sharp wave ripples in memory is grandiose. The authors point to prior reports that selective elimination of sharp wave ripples disrupt memory performance and consolidation. They then frame muscimol inactivation as a method to test memory while preserving sharp wave ripples to test whether sharp wave ripples are sufficient to support memory. The authors state that since muscimol inactivation disrupts memory performance, then sharp-wave ripple activity is not sufficient to support memory. I cannot understand why this is an interesting conclusion – and I feel that the authors have reached too far here. Muscimol inactivation of the septum does many things to hippocampal and entorhinal physiology including the reduction or elimination of 1) theta oscillations, 2) cholinergic input, 3) speed modulated input, 4) theta sequences, 5) episode/time fields, 6) spatial selectivity of grid cell input, 7) theta cycle skipping of HD cells. With so much disrupted it’s almost meaningless to say that the one or two things that remain intact are not sufficient for memory performance. An analogy would be to remove 90% of a car engine and conclude that the transmission alone isn't enough for the car to operate. At a minimum I would suggest the authors discuss this point in detail.

The authors also conclude that sharp wave ripples might then be needed for learning. Using their own logic, do the authors predict that learning will be intact during septal inactivation? This seems incredibly unlikely. While I agree that sharp wave ripples may be needed for learning (didn't Wilson et al. 1994 say this?) I don't think the data presented here addresses this point at all.

The most interesting parts of this paper are that 1) there is replay of episode fields, 2) replay in conserved during septal inactivation, 3) replay of episode fields is conserved even though episode fields are disrupted during septal inactivation. I think the authors need to focus on these points and probably forget about their discussion of memory. On a positive note, I did appreciate the discussion on how a "wave of excitability" could generate a sequence.

Reviewer #2:

This manuscript observed place cell sequences during sharp wave ripples (SPW-Rs) under the suppression of the medial septum during a delayed alternation task. Septal inhibition increased the incidence of SPW-Rs and increased the error rates of the animal (as reported in their previous paper). Therefore, the authors suggest that sequence reactivation during SPW-Rs is not sufficient for the animal to perform the delayed alternation task. The work is potentially significant, however, they need to address several technical questions.

1) According to their previous paper, septal inhibition increased the error rate but the animal still showed a bias to choose the correct arm. Therefore, it is important to show that, during error trials, sequences reactivation can still be seen.

2) Is there a correlation between the error rate observed in a session and quality of sequence reactivation?

3) Although SPW-R may not be needed for memory recall, it is possible that they may reflect the arm choice of the animal. Therefore, it is needed to be quantified whether reactivated sequences reflect preferentially the past or future choice of the animal under septal inhibition. They report these for the before inactivation case but their description is confusing. This data needs to be described better and I think it would also deserve a separate figure considering that it may not agree with previous work.

4) SPW-Rs were not detected the 'usual way', in fact they detected high synchrony periods and the Methods section does explain how it was verified whether indeed ripples were present during these periods. According to Figure 4E no sequences were detected outside SPW-Rs. Does it mean that high synchrony periods with low ripple power did not contain sequences? Again, if this was the case, it is surprising and it does not agree with past work that usually shows a 10-20% correspondence between SPW-Rs and high synchrony periods.

Reviewer #3:

In this study, the authors examine the effect of inactivation of the medial septum (MS) on the generation of sequential patterns of activity across ensembles of hippocampal CA1 neurons in the context of a dual arm alternation memory task, modified to include a running wheel. This work builds on prior work by the same group (Wang et al., 2015) and it represents new analyses performed on this same data set. The main findings reported by the authors include 1) the observation that episode field sequences are "replayed" during sharp wave ripple LFP events at rate that is higher than would be expected by chance and similar to the rate of place field sequence replay. 2) Inactivation of MS using muscimol does not abolish SPW replay of event/place field sequences, in fact it increases the occurrence of these replay events. However, I believe that the statistics employed to detect replay events are flawed, and thus I do not believe that the data supports the main claims of the paper. I outline the nature of my concerns below.

Though one has to dig through the previous paper to understand the methods for detecting sequences of firing on small time scales that are similar to sequences of firing on longer timescales, I believe I understand the analysis steps taken by the authors, and I believe they are problematic. The authors first detect episode/place field sequences as described in Wang 2015. They derive from these sequences an ordered sequence of firing peaks across cells. To detect replay events, they then compute a sequence similarity score by comparing each pair of spikes recorded in different cells within a time window, adding 1 to a sequence score if the order of those two spikes is the same as the order of the peak firing rates in the episode/place field sequence, and adding -1 otherwise. To assess significance, the authors shuffle the cell identity of each spike, maintaining spike timing, across the active cells within the epoch. They do this 10,000 times to build a null distribution of sequence scores. If the observed sequence score falls outside of 95% of the shuffle-computed sequence scores, the authors identify the sequence as being significantly similar to the episode/place field sequence.

However, it appears from the examples shown that there is often structure in the autocorrelation function of neurons' spiking, for example, neurons seem to burst in many identified sequences. By shuffling the cell identity of each spike independently, the authors break this feature of spiking statistics, inflating the significance of patterns they identify as sequences. For an extreme example, imagine two cells fire three spikes each in non-overlapping bursts, in the order found in the original episode/place field sequence. Shuffling spikes independently makes the particular observed sequence score unlikely by chance. However, if the autocorrelation function of the cells were to be preserved, that particular sequence score becomes very likely by chance, essentially those bursts of spikes would need to travel together in the reshuffling process. I think this is a huge problem for their data and conclusions.

Unfortunately, for me, since much of the claims of the paper rely on accurately identifying replay events, these issues are a non-starter for considering the validity of the authors' conclusions. The authors would need to convince me that performing their shuffling procedure in a way that maintains the structure of the autocorrelation within neurons does not change their results for me to consider the paper further.
