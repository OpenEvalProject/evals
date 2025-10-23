# Author response - Round 1

Authors:
- Andrei Khilkevich ([ORCID: 0000-0002-1876-4928](https://orcid.org/0000-0002-1876-4928))
- Juan Zambrano
- Molly-Marie Richards
- Michael Dean Mauk

## Response text

DOI: [10.7554/eLife.37443.026](https://doi.org/10.7554/eLife.37443.026)

Essential revisions:

The reviewers all found the work to be interesting and convincing. The "General Assessments" from the reviewers are all included below for the authors' information and satisfaction. Since they are so favorable, we thought the authors would like to read them in their raw form.

Major points:

1) Data presentation/statistical analysis:

A) During Control 2 experiments, CS1 as well as CS2 were associated with US1. Then during sequence training only CS1 was used. Occasionally, a probe trial was inserted where a CS2 would be presented. This elicited a CR1, but the question was whether presence of CR1 would be sufficient to be followed by CR2. You find that if and only if CS2 produced a CR1, then it was followed by a CR2 (occasionally CS2 did not produce a CR1, and in those cases there was also no CR2). This is a critical result, but the presentation of the data is inadequate. Your results should be shown as a conditional probability relationship, not correlation of likelihoods (Figure 5D).

We apologize for the confusion. In eyelid conditioning literature the terms “likelihood” and “probability” are often used interchangeably, referring to the fraction of trials where CRs were observed. We agree that “likelihood” has a quite distinct meaning in statistics and thus can be confusing to the reader. We therefore clarified the definition of CR probability in the text (subsection “Training an ipsilateral sequence of CRs”) and updated our terminology throughout the text and figures.

With that said, we believe that Figure 5C and G show the data exactly in the format the reviewer is asking. There, the probability of CR2 is shown for four conditions (CS1 trials with CR1, CS2 trials with CR1, CS2 nonCR1 trials and a control for spontaneous eyelid movement).

Results in Figure 5D and H are less critical and show an existence of correlation between first two conditions on different sessions (probability of CR2 on CR1 trials, elicited by CS2 (Y axis) or CS1 (X axis)). We updated and color-coded axis labels to make this transition clearer.

Figure 6 data are confusing and should be replaced with data that test for existence of a conditional probability (if CR1, then CR2). The control condition is the null hypothesis of independence of two events.

Similarly to the previous point, Figure 6E and F already show the probability of CR2 conditioned of CR1 amplitude. We again apologize for the confusion.

B) Similar to my comment above, correlation coefficients are inappropriate for quantifying temporal dependence of one event on another. You are asking the following question: given that CR1 and CR2 occurred, was the timing of CR2 conditioned on timing of CR1? The null hypothesis is that given that CR1 and CR2 occurred, the timing of CR2 was not conditioned on timing of CR1.

We thank the reviewer for this suggestion. We calculated distribution of time intervals between corresponding timing measures of CR1 and CR2 and, for comparison, the same distribution with permuted trials for CR1 data. If the timing of CR2 was conditioned on timing of CR1, the distribution with real inter-CR intervals should differ from the distribution after permutation. We show the real (appropriately colored) and shuffled (grey) distributions on the right of corresponding panels in Figure 7. We found a significant difference between distributions in all cases where the number of trials was sufficient (see Figure 7—source data 1).

We added the description of this new analysis in subsection “Prediction 4: Timing of CRs in a sequence should co-vary on a trial-by-trial basis”. We believe though that the correlation analysis is also informative and did not remove its results.

2) Complex spikes: Like all good papers, the work demonstrates a novel finding that naturally raises follow-up questions. The presentation of the simple spikes is critical for providing evidence that learning of CR2 appears to be similar to CR1. The data in Figure 8 for this question is convincing. However, because complex spikes have also been recorded, presentation of the simple spikes begs the question of what happened to the complex spikes. I request that another figure be added to show data on the complex spikes.

We appreciate the reviewer’s interest. We would like to explain though why we did not put complex spike data in the first place. While we put effort into separating complex spikes from simple spikes of PCs, our goal was simply to assess whether PC responded to US with complex spikes (qualifying for definition of eyelid PC) or not. For this purpose we did not necessary need to reliably recognize every complex spike. Accordingly, we utilized a previously described cluster-cutting procedure (Halverson et al., 2015), which relies on the consistency of complex spike waveform. This is true only to a degree and it is likely that in some cases we are not counting some complex spikes or over-counting in others, if late spikelets are recognized as separate events.

For these reasons we do not feel comfortable to perform a fine level of analysis on the complex spikes data that we have.

3) Data Clarification: In 36% of late acquisition sessions if there was a CR2, there was also a CR3, with appropriate relative timing. The problem is that unlike the condition for learning of CR2 where a US2 is present, there is no error to the cerebellum to encourage learning of CR3. Without an error signal, even when CR3 occurs, it should undergo extinction. Therefore, CR3 should be a transient part of the learning process that might develop as CR2 is learned, but then disappear without a US3. Is there data on this?

We improved the explanation in subsection “Training an ipsilateral sequence of CRs” why CR3 do not extinguish (as long as CR2 do not). We also put into notation “FSL” and “FSR” to better distinguish between FS from left and right eyelid CRs in contralateral sequence.

We see the fact that CR3 remains without a direct reinforcement as evidence that the effective “CS” is the same for both CR2 and CR3 in ipsilateral sequence. Because of this, reinforcement of CR2 on a portion of trials is sufficient to prevent both CR2 and CR3 from extinguishing.

4) Placing work in context: The current paper does not attempt to relate the proposed sequence learning mechanism to theories of cerebellar contributions to movement that posit internal models. How does the proposed mechanism relate to theories of cerebellar control that posit an inverse model, forward model, or a combination within the cerebellum? Because the current sequence learning mechanism requires reinforcement of each component of the sequences, this type of learning mechanism is not obviously consistent with previous theories positing internal models. Thus, the authors need to clarify whether or not their view is consistent with the inverse and forward models of cerebellar control. The end of the discussion seems to imply an internal model, but what type of model and how it relates to other theories was not clear.

We agree that the internal model framework is one of the prominent theories of motor control and cerebellar contribution to it. We think though that eyelid conditioning in general is ill-suited for studying the specifics of internal model involved. In our case, the cerebellum does not only learn a prediction but also serves as a controller that sends a motor signal to the eyelid plant.

We thus chose to place our sequence learning mechanism in context of general dynamical interaction between the cerebellum and cortical areas, being agnostic to the model that describes the cerebellar function.

5) The Purkinje cell recordings demonstrate nice correlates of the two CRs generated with the ipsilateral paradigm, but these findings simply reinforce the previously established causal relationship between decreases in simple spike activity and CR dynamics. The key for making this project highly significant would be to identify the feedback signal and how it relates to the development of precisely timed changes in Purkinje cell activity.

We agree about the importance of identifying the feedback signal route and hope that future studies will address this exciting question. Since multiple possible routes exist, the answer might not be singular and can depend on relative laterality and timing of responses in the sequence.

We expanded the section in Discussion that addressed the above question and added a possible feedback route from red nucleus.
