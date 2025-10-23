# Peer review - Round 1

Editors:
- Upinder S Bhalla, National Centre for Biological Sciences , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08105.022](https://doi.org/10.7554/eLife.08105.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Episodic-like memory trace in awake replay of hippocampal place-cell activity sequences” for peer review at eLife. Your submission has been evaluated as potentially interesting by Eve Marder (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission. For your interest, at the very bottom of this letter we have included the initial reviews, so that you can see where the summary conclusions come from.

Summary:

This paper reports that one can predict which actions a rat will take, from replay sequences and firing rates at a decision point. This extends previous work that shows that it is possible to predict goals from sequences of brain activity. The key differences are that the nature of the task is a non-spatial datum, and that this is encoded not in sequences but in firing rates of replays.

Essential revisions:

The reviewers all felt that the paper was potentially interesting. They also agreed that the paper was quite confusing and needs considerable rewriting and clarification of methodology. It especially needs much improved reporting of data and a more thorough statistical analysis. This must include:

1) Direct representation of neuronal recordings.

2) Other forms of analysis of the p-values of the replay sequences.

3) A distinct analysis of encoding beyond the Bayesian decoder.

4) The author must also provide evidence to support the conclusion that “replay in the junction encodes trial-type” is more than just representation of available sensory cues.

The reviewers felt they need to see these clarifications in order to make a final decision on the paper.

Reviewer #1:

This paper reports that one can predict which actions a rat will take, from replay sequences and firing rates at a decision point. There is some similarity in the overall result with David Foster's work on predicting goals. The key differences stated by the author is that task demand information is non-spatial, and that this is encoded not in sequences but in firing rates of replays.

In general I found the findings of the paper potentially quite interesting, but it turned out to be very difficult to track down the source of each of the presented conclusions. The key measurements were under-emphasized. The author seems to have put a layer of analysis all over the direct data, and everything is viewed through the filter of a Bayesian decoder. The paper is confusing in many places.

Major comments:

1) I would like to see direct data showing the results. The figures don't show rates or rasters, instead using a Bayesian decoder for almost all figures. I really think the author needs to use an alternative and more direct method to support each of the conclusions, since much is hidden by the inner workings of the decoder. For example, there is a small sample of a replay in Figure 3-figure supplement 1. I would like to see each of the points about replay events illustrated by a raster, a firing rate histogram, or other forms.

2) The paper lacks clarity in explaining where each of the conclusions comes from. For example, the author states in the Discussion that the task demand is encoded in “temporally compressed firing rates of place cells”. I struggled to find where this result was obtained in the paper, not least because firing rates were hidden from view as mentioned above. This turns out to be mentioned almost in passing in subsection “Replay is enhanced by spatial working memory demand”, and is easy to miss because it refers to the supplemental figure in Materials and Methods, rather than to presented data.

3) The paper builds a case for task demand representation in replay, and asserts that the task demand information is non-spatial. At face value the task demand can also be interpreted as a spatial datum: where to go next? I would ask that the author clarifies why this should be treated as non-spatial.

Reviewer #2:

The author of this study investigates the phenomenon of place cell sequence replay during awake states under several experimental conditions. There are several findings, most of which are confirmatory of previous studies. The main, new finding of the study is that replay is specific to different experimental conditions. While this finding is interesting, there are a number of important aspects that need to be first clarified in a revised version.

First, the author claims that different types of trials result in differential neuronal activity in the hippocampus. However, what is important and should be shown is how different was the neuronal activity across these types of trials and how different was the decoding of this activity. These should be shown at least with average (and standard deviation/error) probability values across conditions in addition to the assessment of overall significance, considering and comparing all experimental possibilities like it was done in Figure 1D.

Second, the reported decoded probabilities are quite small in their average value, which brings into question how did they pass the significance test from control shuffles. Will the main effect still hold if a lower p-value (e.g., 0.01) is chosen as significance for each individual decoded event?

Third, what are some of the mechanisms by which the recruitment of context-specific replay is achieved in this study? Is the medial forebrain bundle stimulation administered as reward playing any role in the context-specific replay?

Finally, what could be the meaning of the replay events presented here, given that a quite large proportion of events significantly representing different and multiple experiences can occur spontaneously even in naive animals, such as in the case of pre-play?

Reviewer #3:

Previous studies have suggested the replay of hippocampal firing sequences that occur during SWR may encode past or future task related behaviors. Here the author uses a nice design to further address this important question. Rats are trained on a task-switching paradigm in which whether they turn left or right at the junction of a Figure 8 maze is determined by visual cues (visual discrimination) or from memory (alternation tasks). Importantly the rats do not know until the juncture which type of task they are performing (but see below). One of the main findings is that by analyzing the spike patterns during replay with a Bayesian decoder it was possible to predict the trial type/condition when the replay occurred at the juncture, but not in the start point or stem.

While the experiments seem well executed, my concern is that it is not seem that the conclusions are supported by the results.

The main finding that replay in the juncture encodes trial-type is difficult to interpret, because at the juncture point trial type is also present in the available sensory cues (that is, the rat can see what the trial type is based on the lights). While the author attempts to address this issue I did not find this conclusion compelling.

I don't think the statements that trial type is predicted during replay in the stem junction are backed by any statistics. While the red bars are above the black in Figure 3F only two trial types are shown (why?). Additionally, I think Figure 3 D-F is mentioned out of order in the text.

It is stated that the rat only knows the correct response at the decision point (see Results section). But in the DA case doesn't it know it will have to alternate (as stated in subsection “Rats' behavior during brief periods of immobility”). Is DA versus NA encoded during the replay in the maze stem?

While trial prediction was well above chance, it was not clear how trial type was encoded. E.g. in Figure 1C conditions VDlr, NAlr, and DAlr look very similar, nevertheless the decoder extracts the trial type. How is this information encoded. Are some place cells only place cells during specific trial types? The relationship between Figure 1D and 1E was not clear. Figure 1D on the VDrr trials most of the predictions were wrong (sum of the black was more than the red). Why does this not show up in the confusion matrix for Rat 1?
