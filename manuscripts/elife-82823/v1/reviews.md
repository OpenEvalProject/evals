# Peer review - Round 1

Editors:
- Redmond G O'Connell, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82823.sa0](https://doi.org/10.7554/eLife.82823.sa0)

This important study by Ruesseler, Weber and colleagues employs psychophysical kernels and EEG reverse correlation methods to identify the decision process adjustments used to account for variations in target frequency and duration in a task in which targets emerge periodically within a continuous stimulus stream. The paper provides solid evidence for the role of leak and threshold adjustments. The paper will be of interest to researchers studying mathematical models and neurophysiological correlates of decision making and more broadly authors with an interest in the application of reverse correlation techniques for neural signal analysis.


---

# Peer review - Round 1

Editors:
- Redmond G O'Connell, https://ror.org/02tyrky19 Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82823.sa1](https://doi.org/10.7554/eLife.82823.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Decision-making in dynamic, continuously evolving environments: quantifying the flexibility of human choice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Redmond G O'Connell as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Charline Tessereau (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The conclusions drawn from the integration kernel analyses appear difficult to reconcile with key features of the behavioural data. For example, the authors argue that the kernel analyses point to a difference in leak between the frequent and rare conditions but no corresponding change in false alarm rate is observed. Similarly, where the authors conclude from kernel analyses that participants did not alter their decision bounds between frequent and rare conditions the motor preparation ERP signal suggests that there is a bound adjustment. A key issue here is that it is not clear that integration kernels can be used to conclusively discriminate between a leak, bound or drift rate adjustment as each of these could conceivably impact the kernel. In order to make sense of the dataset, the authors should consider fitting alternative model variants to the data or, at minimum, simulating the impact of different decision process parameter adjustments on the integration kernel in order to determine whether their conclusions are warranted.

2) The reviewers raise questions regarding the nature of the decision required by the particular task implemented by the authors. The authors' approach relies on the assumption that participants are simply integrating coherent motion as they might for a standard variant of the random dot motion task. However on this task, targets were actually defined not by the presence of coherent motion but by a criterion duration of coherent motion, during which time the frame-to-frame coherent motion variance diminished. Can the authors rule out the possibility that decisions were partly or entirely based on detecting changes in stimulus variance and or coherent motion duration? If not, can it still be assumed that the rare and frequent targets were matched in terms of the ease with which they could be distinguished from the intervening noise intervals?

Reviewer #1 (Recommendations for the authors):

My principle suggestion would be that the authors consider running simulations of alternative models to see if they can reproduce the current behavioural trends. Drift rate adjustment to Rare vs Frequent target conditions is an obvious candidate.

In general, I found it hard to marry up all the different behavioural/kernel/EEG findings. I recommend the authors examine whether leak adjustment really provides a comprehensive account of their data or if additional/alternative parameter adjustments must be invoked to reconcile their data.

Reviewer #2 (Recommendations for the authors):

1) While I don't think it is problematic, the authors should acknowledge (even if just in methods) that subjects might be able to use the stimulus variance to identify response periods. Also, strictly speaking, the description of the noise as following a normal distribution cannot be correct because it is limited to the range of [-1,1]. I presume this also explains why the authors reduced the standard deviation in the response periods – to avoid hitting those edges too often.

2) Figure 1d is very challenging to interpret. I appreciate that the authors fully acknowledge that it involves signal and noise. However, I think this introduces so many confounds to that analysis that I'm not sure you can say much with confidence from it. Most obviously, the dynamics will reflect the RT differences and the associated shift in the onset of the signal contribution. Also, because it seems to be based on all coherences together, the signal contribution will critically depend on the relative proportion of each coherence in each condition. I'm not sure there is any way to disentangle all of that.

3) I wasn't quite sure how false alarm rate was calculated in Figure 3. Conditions differ in the total time for every run that subjects were in the baseline state where they could have a false alarm. Is the denominator of this rate calculation total task time or total time where subjects could possibly have a false alarm. I think the latter is the most useful comparison. I would guess the authors did that, but I couldn't find the description.

4) It would be useful to have a figure showing individual subject CPP effects shown in aggregate in Figure 5? A scatter plot comparing effect size for FREQUENT and RARE would be a good way to illustrate that.

5) In the discussion, the authors state that initial simulations suggest that a range of decay time constants could be optimal. This may provide another explanation for the lack of change in time constant in different conditions. If a range are possibly optimal for any given condition, perhaps the subjects can remain close to optimal in this task without changing their decay time constant between conditions.

6) I noticed two typos/formatting errors in the methods. In the subscripts for the regression, a "D" was shown for the "δ" symbol. Also, the words "regressed out" are duplicated in EEG pre-processing section.

Reviewer #3 (Recommendations for the authors):

General notes:

– Figure captions should describe what is being shown, with a link to the method and/or supplementary material for lengthy computations.

– Throughout the text, the authors sometimes refer to 'net motion', 'coherence', and 'evidence'. I would make sure to use the same terminology.

– Some analyses are missing, e.g. the proportion of long answers that have been ignored (that could indicate a level of engagement in the task).

Detailed comments/suggestions:

Task design:

– Methods: are subjects instructed about what the dots mean in advance? How long do the dots stay colored for during feedback?

– How much do participants get in total? The total bar is 30 points and they get only 50 cts to have 15 points which are after 5 good responses without error on average. Are the feedback distracting the participants? Do the authors think that the money aspect here provides a substantial motivation for participants?

– Figure 1c:" The resulting evidence integration kernel is well described by an exponential decay function, whose decay time constant in seconds is controlled by the free parameter tau ": As formulated, the caption hints that the figure analyses how well described is the kernel. As I understand, the exponential kernel is a choice that is imposed by the authors, and how well it fits the coherence level before a decision is not addressed in the paper. I would reformulate and clearly state that the authors define an exponential kernel from the past coherence levels. More details on the definition of this kernel are required, and statistics about how well it fits the data would enable stronger claims of its use throughout the text. In particular, the average coherence can take 3 values (30, 40, or 50), are the authors averaging for all coherence levels together? Should A be correlated with those values? What is the effect of the mean coherence level during response periods?

P7, Figure 2:

– b and c: is that the mean or median (for b) and the error bar the std/95expectiles (for c) of participants' detection rate/RT? Is the RT tau? I know both variables are defined in the methods section but they should also be explained here or a link should be made to the method section so that the reader can know what they are looking at.

– d: is the integration kernel here referring to the exponential, or simply the average signal before the decision, averaged across all participants?

– d again: why is the maximum coherence 0.5 here? is that only for switches from 0 to 0.5 coherence? What happens for switches from 0 to 30 coherence?

– d again: the authors observe no effect on the response window duration on the response kernel, but have applied a threshold on the duration of the response on the long response period in order to make this plot. What happens if the authors include all response lengths? (also applies to the discussion p17 and 18).

P 8:

– "This provides further evidence that participants were overall more conservative in their responses in LONG conditions than SHORT" can the authors define what conservative means?

– It is not surprising that the integration kernels are not affected by the length of the response period if the long responses are not considered.

– I think the kernel analysis during baseline is necessary to show that participants are not randomly making motor movements, however, the authors could describe in a bit more detail the difference between a correct response and a false alarm: how are the integration kernels different in the baseline vs response period? (the kernels for false alarms seem a bit shorter?)

– When do false alarms occur compared to the response periods? Are they regularly after the end of a response period? What is the pattern of the coherence that causes those false alarms? Are they always when the frame update is 1s, for example?

Figure 3:

a) the authors mention significance but do not provide p values. Why is it consistent with having a more cautious response threshold? I'd favor the reverse interpretation that short response periods induce more confusion between signal and noise.

b) is that the averaged signal before false alarms? Do they always occur when the mean average coherence reaches 0.5? Why is the maximum value 0.5?

c) explain what the points show and how these are computed.

P.11

(ii) To me, it is not clear that the behavioral evidence from 'false alarms' indicate that participants are still integrating sensory evidence – a stricter definition and existence of the kernel (how well it fits for every response) could help support this statement

– Is 'net motion' coherence here?

– On the same page – the regressor 'absoluted sensory evidence' has not been named like this before.

P. 12:

– Why is it consistent with the behavioral finding of lower detection rate and slower RT in rare conditions?

– I understand the analysis is done regardless of the response. What about missed response periods/responses during the baseline?

Figure 4:

– The caption is incomplete, what does the right-hand side show? Is it one weight for one regressor across time for one example electrode?

– What is the goodness of fit of the regression?

P13 – Figure 5:

– What are the lines showing? What is the black thick line on top?

– P.14 To test whether these signals are decision-related, the authors could also compare the results of the regression when false alarms are made and when the response period is missed.

– Figure 6: has the effect of previous exposure been controlled for the vertical motion? Could the authors discuss whether this would have an impact on the CPP.

– P 15: could the authors give more details on the behavioral correlate and how is it computed.

– "this negative-going component was larger in amplitude (i.e. more negative) in participants who would integrate sensory evidence over longer durations (i.e. had a higher value of τ).": could the authors elaborate on how to interpret this finding with regard to existing literature?

– Figure 7 P 16 spearman correlation: can the authors describe the top plot? what are the lines showing? if that's the mean it should be mentioned and the standard deviation should be shown. Can the authors describe the bottom plots? why are the authors using log(tau) for the x-axis?

Discussion:

- p 17: 'The behavior is well described by a leaky evidence accumulator' the exponential kernel is a reverse correlation that the authors have done themselves, but they have not shown causality nor statistical analysis on what those kernels mean in relationship with the behavior.

Methods:

– In the regressor table, what is 'prediction error' regressor?
