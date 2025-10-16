# Peer review - Round 1

Editors:
- Hugo Merchant, National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71612.sa0](https://doi.org/10.7554/eLife.71612.sa0)

This study investigates the neural underpinnings of the bias property of timing, namely an overestimation for short and underestimation for long intervals, during an interval reproduction task in the medial prefrontal cortex of gerbils. The key novel result is that only neural populations with mixed responses, including ramping activity with linear increasing and slope-changing modulations as a function of reproduced durations, can encode the bias effect. Overall, experiments and data analysis are technically sound, and the conclusions well supported.


---

# Peer review - Round 1

Editors:
- Hugo Merchant, National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71612.sa1](https://doi.org/10.7554/eLife.71612.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Distributed coding of stimulus magnitude in rodent prefrontal cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Hugo Merchant as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The main weakness of the paper is a conceptual problem, which requires clarification. Both the title and the introduction point to magnitude quantification, which in general exhibits the regression effect (Vierordt's law). Interval timing is certainly a form of magnitude quantification and exhibits the regression effect. However, any neural correlate of the regression effect in interval timing does not necessarily generalizes to other forms of magnitude quantification. The way the findings of this paper are framed in the title, abstract, introduction, and discussion seem to make that generalization, and that claim is not supported because the data shown has a narrower scope.

2) It is necessary to clearly demonstrate that the behavioral protocol produces a robust, reliable time interval reproduction. Is also fundamental to provide a valid justification for such low levels of performance. It is especially important to clarify this point before analyzing the potentially associated neuronal activity. It is important to understand how stable the behavior is in a session-by-session base. We suggest including a full description of the learning curve. This point is especially relevant for the population analysis, where the activity of cells collected in different sessions was pooled together. In addition, it's well known that in behavioral protocols like this, behavior tend to stereotype, making it difficult to determine if the neural activity is associated with a particular behavioral variable (such as speed or distance) or elapsed time. Hence, it would be necessary to formally assess how behavioral variables covariate (or not) with time. For this, examples of single sessions are not sufficient. It is necessary to clarify several things. For example, the slopes of the linear regressions for dozens of sessions are presented (Figure 1E) but is not clear if there was a behavioral evolution over the training. For another example, animal 10526 presented high levels of variability in many variables (Figure S2), hence, it would be important to know which sessions were used for the analysis of the neural data.

3) A main conclusion of the paper is that only neural populations with mixed responses, including ramping activity with linear increasing and slope-changing modulations as a function of reproduced durations, can encode the regression effect. How the prior knowledge about the distribution of used intervals in the task is combined with the actual measurement of the passage of time? It is not evident on the last part of the paper how the slope changing cells, associated with a prior signal, are combined with the linearly increasing ramping cells to generate both the regression effect and a sufficiently accurate representation of produced duration. Sessions within the same animal with different slopes in the regression effect show different proportions of the two cell types? How is the mixing accomplished?

4) During reproduction, the percent of neurons categorized with time-dependent PC 1 and stimulus PC 1 responses is < 1%, which is one of the two combinations that gives the best regression effect in the decoding. These linearly increasing ramping cells were very common during measurement and may be encoding elapsed time since the stimulus onset. In contrast, most of the responses in reproduction were slope changing cells, reaching a peak of activation close to the end of the produced interval. This type of responses has been observed when a prediction of time to an event is needed (time-to-contact cells Merchant and Georgopoulos, 2006). A key issue, then, is whether the decoding method used to reconstruct elapsed time is capturing the prediction to an event signal as a regression effect because is aligned to the onset of the time interval, instead of to the end of the produced interval, which is probably the task event that the cells are encoding.

5) The authors say the conventional PCA did not show curved trajectories (line 418, Discussion, Pg. 17) for the measuring phase. However, that is certainly not the case for the reproduction phase, where the decoding analysis was successfully performed, and the regression effect was observed. I don't see the present results as alternative to the hypothesis by Sohn et al., 2019., but as a quite interesting step forward from that. It is possible that what the PFC is encoding in this task is an estimate of when to stop moving. In that case, the neural activity would be equivalent to that observed in Sohn et al., 2019. And perhaps warped and transformed by down-stream reading areas similarly to the "curved manifold projected onto a line". It would be very interesting if slope-changing cells were contributing to a more curved shape of the population trajectory, since they can be encoding a prior as the authors suggest. The results of the decoding analysis which uses a linear (i.e. lower dimensional) decoder indirectly suggest this.

6) Despite the clear differences in neural activity between the two phases presented in figures 2 to 4, authors named the following section "Population activity shares similar components for measurement and reproduction" (page 8 line 58). However, that entire section, that includes figures 5 and 6 and several supplementary figures (e.g. S8 and S9), shows notorious differences between the two phases. From the explained variance (Figures 5, S8, S9) to how single cell activity contributes to the population representations, there are striking differences between the two behavioral phases. Authors must clarify what do they mean by "activity shares similar components" or change the name of the section for something that better represents the data.

7) Elapsed time decoding from populations of cells using classifiers suggest that different ramping cell types can contribute to represent the passages of time and that the decoding error can explain the error in produced interval (Merchant and Averbeck, 2017; Bakhurin et al., 2017). Based on this and the previous comment I am wondering whether a classifier is not a better option for decoding than the linear decoder.
