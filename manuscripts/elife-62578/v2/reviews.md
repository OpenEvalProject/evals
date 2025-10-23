# Peer review - Round 1

Editors:
- Timothy Verstynen, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62578.sa1](https://doi.org/10.7554/eLife.62578.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

All three reviewers (including the Reviewing Editor) were impressed with the changes to the manuscript. They felt that the revised work strongly justifies the conclusion that humans can rapidly and flexibly shift control policies in response to environmental perturbations.

Decision letter after peer review:

Thank you for submitting your article "De novo learning and adaptation of continuous control in a manual tracking task" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tamar Makin as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This work looks at "de novo learning" in the context of fast continuous tasks, i.e., shifts of control policies (or controllers), rather than parameter changes in existing policies, with visuomotor adaptation. In a set of 2 experiments, using a mixture of discrete point-to-point movement trials and continuous tracking of moving target trials, the authors set out to determine whether the structure of shifts between visual and proprioceptive information determines whether learning relies on adaptation or shifts in control policies. Using both the presence of post-shift aftereffects and trailwise model fitting, the authors find that, simple rotations of visual inputs of the hand lead primarily to changes in control parameters while mirror reversals lead to changes in the control policy itself. Although there was evidence for a mixture of adaptation and de novo learning in both conditions. The authors infer from this evidence that humans can rapidly and flexibly shift control policies in response to environmental perturbations.

In general, this was a very cleverly designed and executed set of studies. The theoretical framing and experimental design are clean and clear. The data is compelling on the existence of condition differences. However, all three reviewers identified significant concerns that should be addressed.

Essential revisions:

1. Inferential logic

Reviewer #1 pointed out that there are two key parts to the analyses used to infer that mirror-rotations lead to de novo policy shifts while rotations lead to adaptation. The first is the presence of post-perturbation aftereffects. While we clearly see stronger aftereffects in the rotation condition than in the mirror reversal condition, suggesting a difference in fundamental control mechanisms, it is not clear why control policy shifts are the only alternative explanation for attenuated aftereffects. I'm pretty sure that this is just a confusion based on how the problem is posed in the paper.

The second are the alignment matrices (in both immediate hand position and movement frequency spaces), that are estimated based on model fits to the data. I'll consider both in turn. Perhaps more problematically, the alignment matrices (Figure 3A) and vectors (Figure 3A, 5B, 6B), based on the model fits, show a very high degree of variability across conditions and do not perfectly align to the simple predictions shown in Figure 3A. While the reviewer agrees that if you squint on the mean vector direction, they look qualitatively consistent with the models, but only qualitatively. In fact, the fits to the "ideal" shifts or rotations (Figure 5C, 6C) suggest only partial alignment to the pure models. How are we sure that this isn't reflecting an alternative mechanism, instead of partial de novo learning?

In both the aftereffect and alignment fit analyses, the inference for de novo learning seems to be based on either a null (i.e., no aftereffect in mirror-rotation) or partial fits to a specific model. This leaves the main conclusions on somewhat shaky ground.

Reviewer #2 raised similar concerns, pointing out that the authors introduce the concept of de novo learning in contrast to both error-driven adaptation and re-aiming: 'a motor task could be learned by forming a de novo controller, rather than through adaptation or re-aiming.' However, the discussion reframes de novo learning as purely in contrast with implicit adaptation: '[…] de novo learning refers to any mechanism, aside from implicit adaptation, that leads to the creation of a new controller'. While this apparent shift in perspective is likely due to their results and realistically represents the scientific process, this shift should be more explicitly communicated.

As explicitly raised in the discussion and suggested in the introduction, the authors have categorized any learning process that is not implicit adaptation as a de novo learning process. To substantiate this conceptual decision, the authors should further explain why motor learning unaccounted for by established learning processes should be accounted for by a de novo learning process.

This same reviewer also pointed out that, participants could not learn mirror-reversal under continuous tracking without the point-to-point task, which the authors interpret to mean that re-aiming is important for the ‘acquisition’ of a de novo controller. This suggests that re-aiming may not be important for the ‘execution’ of a de novo controller.

However, the frequency-based performance analysis presented in the main experiment would seem to suggest otherwise. As mentioned in the introduction, low stimulus frequencies allow a catch-up strategy. Both rotation and mirror groups were successful at compensating at low frequencies, but the mirror-reversal group was largely unsuccessful at high frequencies. Assuming that higher frequencies inhibit cognitive strategy, this suggests to me that catch-up strategies might be essential to mirror-reversal, possibly not only during learning but also during execution.

Further, the authors note that, in the rotation group, aftereffects only accounted for a fraction of total compensation, then suggest that residual learning not accounted for by adaptation was attributable to the same de novo learning process driving mirror reversal. This framing makes it unclear to me how the authors think re-aiming fits into the concept of a de novo learning process (e.g. Is all learning not driven by implicit adaptation de novo learning? What about the role of re-aiming?)

Reviewer #3 points out that in the abstract, the last line says, 'Our results demonstrate that people can rapidly build a new continuous controller de novo and can flexibly integrate this process with adaptation of an existing controller'. It's not clear if the authors have shown the latter definitively. What is the reasoning for this statement, "flexibly integrate this process with adaptation of an existing controller"? It would seem you would need the same subjects to perform both experimental tasks (mirror reversal and VMR) concurrently to make this claim.

Reviewer #3 also points out that, on lines 339-342, the results show that mirror-reversal learning is low at high frequencies (Figure 5B). The authors interpret this as reason to believe that this is actually de-novo learning and not adaptation of an existing controller. This seems somewhat unfounded. Could it be that de novo learning performs well at low frequency, through 'catch-up' movements, but not at high frequencies? Do the authors have a counter argument for this explanation?

On lines 343 – 350, Reviewer #3 points out that the authors ascribe the difference between after-effects and end of learning to be due to de-novo learning even in the rotation group. However, that difference would likely be due to the use of explicit strategy during learning and its disengagement afterwards, or perhaps a temporally labile learning. Can the authors rule these possibilities out? What were the instructions given at the end of the block and how much time elapsed?

2. Linearity analysis

Reviewer #1 reported having a hard time understanding the analysis leading to the conclusion that there is a linear relationship between target motion and hand motion. The logic of the spectral analysis was not clear to me, and the results shown in Figure 4 were not intuitive. In addition, there was no actual quantification used to make a conclusion about linearity. Thus, it was difficult to determine whether this aspect of the authors' conclusion (a critical inference for them to justify their main conclusion) was correct.

Reviewer #2 raised similar concerns, pointing out that using linearity as a metric for mechanistic inference has limitations.

– The absence of learning (errors) would present as nonlinearity.

– The use of cognitive strategy could present as nonlinearity.

– It doesn't seem possible to parse the two mechanisms, especially as you might expect both an increase in error at the beginning of learning and possibly an intervening cognitive strategy at the beginning of learning.

Given these issues, a more grounded interpretation is that linearity simply represents real-time updating. If the relationship between the cursor and the hand is nonlinear, then updating is not in real time.

The data shown in Figure 4B do not appear to provide clear evidence that the relationship between the cursor and the hand was approximately linear. Currently, it seems equally plausible to say that the data are approximately non-linear. Establishing a criterion for nonlinearity would be useful (e.g. shuffling a linear response for comparison). This was also pointed out by Reviewer #3 who pointed out that details about frequency analysis are buried deep in the methods (around line 711), especially how the hand-target coherence (shown in 4B) is calculated. It would be helpful to include some of these details in the main text. For example, it is currently very difficult to understand the relationship when from moving from Figure 4A to 4B.

Reviewer #3 raises a similar concern. The authors show the tracking strategies participants applied by investigating the relationship between hand and target movement. The linear relationship would suggest that participants tracked the target using continuous movements. In contrast, a nonlinear relationship would suggest that participants used an alternative tracking strategy. The authors only state this relationship is based on figure 4 but it seems do not provide any proof of the linearity. It would be more convincing to provide an analysis to show that the relationship is indeed linear or nonlinear.

3. Statistical results

Reviewer #1 points out that any of the key statistical results were buried in the main text and some were incompletely reported. Can the authors provide a table (or set of tables) of the key statistics, including at least the value of the statistical test itself and the p-value, if not also estimates of confidence on the estimates?

Reviewer #3 also points out that outlier rejection based on some subjects who had greatly magnified, or attenuated data seems like it might be biasing the data. Also, the outlier rejection criteria used (>1.5 IQR) seems very stringent. Furthermore, it appears there was no outlier rejection on the main experiment. It would be good to be consistent across experiments.

4. Experiment 2

The intention for experiment 2 is to see how much training on the point-to-point task influenced adaptation mechanisms during the tracking task. Yet, this experiment still included extensive exposure to the point-to-point task. Just not as much as in experiment 1. Given this, how can an inference be cleanly made about the influence of one task on the other? Wouldn't the clean way to ask this question be to just not run the point-to-point tracking task at all?

5. Frequency analysis

The authors state that "The failure to compensate at high frequencies.… is consistent with the observation that people who have learned to make point-to-point movements under mirror-reversed feedback are unable to generate appropriate rapid corrections to unexpected perturbations." This logic is not clear. How is this inferred based on which movement frequencies show an effect, and which do not, leading to this conclusion?

6. Clarity of logic

Reviewer #3 states that would be helpful if the authors could provide more background/context on their view of de novo learning and explanations on relationship between de novo learning and the adapted controller model. For example, why does the lack of aftereffects under the mirror-reversal imply that the participants did not counter this perturbation via adaptation and instead engaged the learning by forming a de novo controller (Line 199)? Is the reasoning purely behavioral observations, or is there a physiological basis for this assertion?

In addition, this same reviewer points out that on lines 197-199: The reason for the lack of after-effects in the mean-squared error analysis is a little vague. It took a few tries to understand the reasoning. It would be good to spell this out a little more clearly. In lines 223-225: The logic behind why coupling across axes is not nonlinear behavior seems to be missing. It's quite unclear and currently difficult to understand. It would be very helpful to spell this out too.

7. Learning in the visuomotor rotation (VMR) condition.

Reviewer #3 also shows that surprisingly, there is no measurement of aiming in the learning to VMR. Several motor learning studies (several the authors cite) show that learning in VMR is a combination of implicit and explicit. It is understood that this is not possible in the continuous tracking task, but can certainly be done in the point to point task. Is there a reason this was not done? Wouldn't this have further supported the author's claim of an existing controller?
