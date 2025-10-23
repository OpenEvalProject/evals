# Peer review - Round 1

Editors:
- Matteo Carandini, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04677.025](https://doi.org/10.7554/eLife.04677.025)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Moment by moment: Vacillation, indecision and hesitation in monkey motor cortex” for consideration at eLife. Your article has been evaluated by Eve Marder (Senior editor) and three reviewers, plus a member of our Board of Reviewing Editors. Their opinion is favorable provided that you can address two main concerns described below, which entail additional analysis of behavioral data.

This manuscript describes population activity in premotor and motor cortex during single trials to study internal events occurring during free choice, such as changes of mind and vacillations. The results suggest that initial motor plans, even those that stem from free choices, are sometimes corrected or changed on the fly. Previous studies have reported evidence for such ‘vacillations’ before, but here the aim is to describe them in single trials. The results are likely to be of interest to a wide range of neuroscientists studying decision making and motor control. However, there are two main concerns.

First, the data are not very abundant, particularly for one of the monkeys. Only 5 datasets (∼3 days of recordings) had sufficient statistical power for single trial analysis. This leads to multiple questions. Five out of how many? What happens in the rest of the datasets? Does the decoder not work for them? How many neurons are in each data set? What is the sensitivity of the decoder to the number of neurons? How homogeneous is the weight of each neuron in the decoder?

The paucity of data in turn reflects on the other main concern, namely whether both monkeys indeed engaged in “decisions” and occasional “free choices”. In one monkey, indeed, the supposed free choice conditions led to lopsided behavior (dataset J2, Table 1): for the T-maze, the animal moved left 92% of the time when that choice was easy, and 0% when it was hard (“diff”). Similarly lopsided percentages were seen for the S-maze, where the animal moved to the left nearly 100% of the time when the rightward choice was hard, and 6-23% of the time when it was easy.

Though these data may reflect truly free choices, a more prosaic explanation is that they reflect a learned, arbitrary sensorimotor association between a screen configuration and a reach movement. In the rare cases when the animal makes a movement to the other target (e.g. 8% of the time to the right in the easy|easy condition for J2T), it may simply mean that he hasn't learned the association well enough and is making an “error” with regard to the association. An incomplete learning of the association may also help explain the activity of the other monkey, where the percentages are less lopsided.

If the monkey has learned to make a movement to the left when it sees a particular stimulus configuration, then it is hard to argue that it is making a free choice. For example, drivers learn to stop at a red light. But is that a decision in any interesting sense, i.e. does it involve weighing the outcomes of different alternatives and choosing one based on one's values or preferences, or after accumulating enough evidence about the correct answer? It is thus possible that the data here reflect arbitrary sensorimotor associations, which have been studied for years, particularly in PMd. In such learned associations between a stimulus and response, activity during the delay period is simply preparation for translating a sensory stimulus to a particular upcoming movement.

These two concerns are related: perhaps by analyzing more behavioral data (concern 1) it is possible to help the case for free choices (concern 2). Indeed, the current Figure 2G-I lumps together all the conditions, giving the potentially misleading impression that the animal is “freely” choosing to go either to the left or the right with nearly equal frequency. It would be useful to analyze more behavioral data, and to provide additional analyses. One could be a summary bar plot comparing the percentage of vacillations across all conditions for a given data set, i.e., forced choices, free choices, taken/untaken switches and likely/unlikely changes, indicating whether those percentages differed significantly across conditions (say, based simply on their overall occurrence and binomial statistics).

Other issues:

Why do all the decoded values start with a leftward (negative) bias (for instance, Figure 2D-I, x axis)? Because crossing the zero value is a criterion for determining a vacillation, it seems important to ensure that decoded values computed before the maze onset are not artificially biased, as this could potentially affect the labeling of trajectories as vacillations.

The monkeys show highly uneven preferences for each target (Table 1). Is there a neural correlate of this bias?

The present analysis makes no effort to separate neurons recorded from M1 and PMd. Yet, this group has recently documented a difference in preparatory activity between these two areas. Why is such a pooling acceptable? It would be more interesting to see a comparison between the two areas. What happens if the analysis is done for each area separately?

The vacillations in the decoder in the free choice condition (Figure 2G-H) look extremely stereotyped further supporting the idea that this condition is not reflecting a free choice but rather the temporal dynamics of planning of an arbitrary sensorimotor association. In both panels, the leftward movements almost always shift to the right first before shifting to the left.

It seems odd that vacillations are not associated with longer reaction times (RT). There was an effort to see if long RTs were associated with vacillations, but the reverse selection criterion might be more fruitful: having identified single trials as vacillations, are their RTs longer?

The manuscript states (in the Results section) that neuronal responses encoded forced and free choices similarly, and emphasizes that this result was not necessarily expected. It should be quantified more rigorously. How was the similarity between neuronal responses assessed? What were the reaction times for the respective choices? Using tuning preference as the only measure to make this point is rather weak.

The manuscript argues that because the time course of the neural response is nearly identical for forced and free trials, the monkey made up his mind quickly when presented with a free choice. This claim is unsubstantiated. An alternative explanation may be that the monkey rapidly integrated sensory information and associated a particular stimulus configuration with a particular movement.

Also in the Results, the authors state: “more traces cross the midline for free choices than forced choices.” This should be quantified.

Still in the same section: “on roughly half of such trials, the monkey should have already fortuitously chosen the ‘lucky’ side.” Given that choice probabilities were not 50/50, what proportion of the time did the monkey actually choose the “lucky” side?

The following sentence, in the Results: “in both monkeys, a modest number of trials exhibited spontaneous vacillations.” Since decoded choices are ultimately a reflection of population firing rates, is there some feature of the population firing rate that was different on vacillated trials? Namely, were firing rates lower? If overall population firing rates were similar between vacillated trials and regular trials, is there a subset of neurons that changes firing rate? It would be good to understand if/how neural firing rates in both single cells and the population give rise to vacillations.

In the Results, the authors state: “to our knowledge, observations of such spontaneous vacillations when presented with a free choice—without changing external evidence—have not previously been described”. This claim appears unsubstantiated. Vacillations could simply be measurement error in the neural trajectory. Indeed, in 40% of the datasets, there was no significant difference in the number of vacillated trials between free and forced choice conditions.

Discussion, first paragraph: Consider comparing these results with the work of Stanford and colleagues on saccades (Nat Neurosci 13:379, 2010; J Neurosci 33:16394, 2013), which also demonstrates competition between motor plans within the same task, from quick choices to slower trials in which the initially dominant motor plan is suppressed and overtaken by the alternative one (’changes of mind'). Although that work is based on trial-averaged data, it tightly relates those motor planning patterns to behavior, and to RT in particular.

Discussion, second paragraph: “our data seem at odds with standard integrate-to-bound models.” In what way are they incompatible? Most of the neurons in Figure 2–figure supplement 1 differentiate one choice from the other in less than 200 ms relative to the onset of the maze, showing an initial rise and differentiation that resemble the data from saccade-based tasks. (Responses are much more variable when aligned on movement onset, but that is understandable given the dependencies of PMd and M1 neurons on kinematic parameters). Second, such rise-to-threshold models have been used successfully in a variety of choice tasks, not just in random-dots tasks ’when information is delivered slowly.‘ But if ‘ramping’ is understood simply as an increase in motor planning activity, then the classic ramping associated with saccades is indeed very quick, on the order of 200 ms (Science 274:427, 1996; Neuron 76:616, 2012). Again, the work of Stanford and colleagues illustrates that a scheme in which alternative motor plans compete to reach a threshold works well even when decisions are urgent and choices quick. The work of Cisek and colleagues is consistent with such competition too, but over much longer time scales (Neuron 45:801, 2005; J Neurosci 29:11560, 2009; Neuron 81:1401, 2014). Thus, the rate at which sensory information is delivered or perceived is orthogonal to this issue of how to characterize motor-planning activity.

The following statement in the Results: “the slow RTs on these trials were not due to re-planning, but instead involved a hesitation to execute.” The high RTs on untaken switch trials (Figure 4A) is reminiscent of a phenomenon known as saccadic inhibition, in which a the appearance of an irrelevant distracter slows down a planned saccade to an unambiguous, unique, predictable target (J Cogn Neurosci 14:371, 2002; J Neurosci 31:12501, 2011; Vision Res 69:32, 2012). This is as if a sensory event (a change in a barrier, in this case) transiently interrupted and delayed an ongoing motor plan.

Figure 2: what are the dots on the decoder trajectories in this case?

Free-to-forced trials: it may be nice to show the decoder in these trials before and after the change in the maze.

Forced-to-free trials: how do we explain trials without a detectable change of mind?

What happens during unsuccessful trials?

The title is compelling, but the three phenomena it lists—vacillation, indecision and hesitation—are not clearly distinguished in the manuscript. It would be helpful if the manuscript described them better.

For instance, the definition of a vacillation (or change of mind, but better stick to one word) is clearly explained in the Methods, but it would be useful if the main text mentioned that they were identified as big swings in the decoded choice.

Results, tenth paragraph: consider adding some clarification when mentioning “…on free-choice trials…”. Rather, the lower performance may reflect somewhat higher variability or complexity during free choices or something similar.
