# Peer review - Round 1

Editors:
- Huan Luo, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73651.sa0](https://doi.org/10.7554/eLife.73651.sa0)

How does the brain implement basic logical computations (AND, OR, XOR) regardless of stimulus types? This is one of the most fundamental questions in cognitive neuroscience. This MEG study, by combining interesting experimental paradigms and sophisticated signal analyses, demonstrates four serial neural components in different brain regions that correspond to four system-level computations, respectively.


---

# Peer review - Round 1

Editors:
- Huan Luo, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73651.sa1](https://doi.org/10.7554/eLife.73651.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Different computations over the same inputs produce selective behavior in algorithmic brain networks" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Chris Baker as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Testing the representational generalization across stimulus set. In principle, the logical computation should be independent of the stimuli and would engage similar four-step neural computation in the brain for many types of stimuli. Although the authors demonstrate similar decoding temporal course and patterns for grating and serially presented stimuli (in supplementary materials), it is important to perform a generalization analysis across different stimuli. Specifically, the classifier obtained for face stimuli in the main experiment could be used to decode computations performed over grating stimuli (data in supplementary materials), for example.

2) Clarifying the temporal relationship of the four components and why their alignment over time still supports the four-step conclusion. Moreover, the 3nd component also shows early onset activation. How to reconcile the results with the 4-step computation view? Please see details in the first two comments raised by Reviewer 2.

3) Adding analyses to test alternative computational steps, e.g., 3 system-level, 2 system-level for comparison, and clarifying why the proposed 4-step is the best model to characterize the whole process.

4) The behavioral relevance analysis was only performed on the fourth component. What about the first three components which should in principle be related to behavioral performance as well? More generally, is there any neural signature that is related to behavior for both linear and nonlinear calculations?

5) The authors should collect new data or at least address the possibility of the involvement of eye movement in the four levels of computation.

Reviewer #1:

This work by Jaworska et al. examined the spatiotemporal correlates of logical computations over the same stimuli in the human brain using MEG recordings. They revealed four neural components that occur in different brain regions and at varied latencies, corresponding to four system-level computations respectively.

Overall, it is an important study addressing the most fundamental question in cognitive neuroscience, that is, how, where and when do the basic logic computations (AND, OR, XOR) occur in the brain? The study used advanced analysis approaches to address the thorny question and the results are impressively clean and robust and have been replicated for different stimulus sets and conditions.

My major concern is the representational generalization across different stimuli. Specifically, the logical computation (AND, OR, XOR) in principle should be independent of the employed stimuli (face, gratings, etc.) and would thus engage similar neural computation in the brain for different types of stimuli. Therefore, it is important to confirm that the observed logical computation components could be generalized across different stimulus setting (representational generalization across stimuli).

1) If my understanding is correct, the logical computation (AND, OR, XOR) should be independent of the stimuli and therefore would engage similar four-step neural computation in the brain for other types of stimuli. Although the authors demonstrate similar decoding temporal course and patterns for grating and serially presented stimuli (in supplementary materials), I think it is important to perform a generalization analysis across different stimuli. Specifically, we would expect that the classifier obtained for face stimuli could be used to decode computations performed over grating stimuli, for example.

2) I am curious how could the authors make sure that the logical computation (based on the binary classification on four types of stimuli) are the genuine calculation in the brain, since it is completely defined in terms of the experimenter's terminology and the subjects might use different strategy. Have the authors considered other alternative computation over the same inputs? Or put in another way, how could the current results be incorporated into or account for previous findings?

3) The last component is interesting and shows behavioral correlates, which is important evidence. If my understanding is correct, that component only applies to nonlinear integration in combination with RT. What about the behaviorally related linear computation? Is there a general behaviorally related neural component that is related to both linear and nonlinear computation?

Reviewer #2:

How our brain dynamically represents and transforms the same visual input into integrated features to produce different behavior remains unclear. To study the dynamic algorithms from mass neural signals, the authors recorded the MEG activity of participants who resolved the classic XOR, OR, and AND behavioral tasks. Using linear and nonlinear representations, they found that source-localized MEG activity progresses through four systems-level computations identified within individual participants. The first two computations similarly represent the inputs across the three tasks; the last two differently represent the inputs in a task-dependent manner. The topic is interesting and timely. The study is elegantly designed and the data statistics are highly significant.

To study the dynamic algorithms from mass neural signals, the authors recorded the MEG activity of participants who resolved the classic XOR, OR, and AND behavioral tasks. Using linear and nonlinear representations, they found that source-localized MEG activity progresses through four systems-level computations identified within individual participants. The first two computations similarly represent the inputs across the three tasks; the last two differently represent the inputs in a task-dependent manner. The topic is interesting and timely. The study is elegantly designed and the data statistics are highly significant. I have some comments listed as below.

1. For each task, the authors proposed the 4 systems-level stages of computation link stimulus to behavior (the first two stages represent and linearly discriminate the visual inputs; the third and fourth stages nonlinearly integrate them in a task-specific manner), according to the different onsets from post-stimulus (~60, 100, 260, and 400ms for each stages, respectively). However, the time window of the first stage (Lin) is the same as the second stage (LinBoth), namely, 74-117ms. This was also reflected very well in the results from Figure 1B, the "Lin" and "LinBoth" computations have almost the same onsets and peaks, particularly, the peak of the blue line (first stage, Lin) looks like much latter than the magenta line (second stage, LinBoth). I am confused that how the authors distinguished these two stages when they had the same time window and why the authors proposed they were the two different stages rather than the same stage during their computations. More generally, the authors should offer more evidence for the 4 systems-level stages of computation, for example, whether it explained their results better than the 3 systems-level stages or 2 systems-level stages of computation.

2. Similar to the first point, for the results in Figure 3, there were several significant peak values in the very early time window (0-60ms) for the third stage ("NonLin"). However, the author only focused on the late time window (~260ms) for this stage. How to reconcile these early peaks (early effects) of the third (late) stage?

3. The behavior data and decoding performance lacked in the first three systems-level computations. Functional inferences based on hypothetical computations of MEG data are not convincing.

4. I would like to suggest the authors collect eye movement data to address whether eye movements are a possible confound for the difference between the four systems-level computations.

5. The legend descriptions are too long and confusing, like figure 2. I would like to suggest the authors label small figures in one figure to make the legend easier to understand by readers.
