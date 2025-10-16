# Peer review - Round 1

Editors:
- Kate M Wassum, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49315.009](https://doi.org/10.7554/eLife.49315.009)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Acceptance summary:

In this study, the authors demonstrate that dopamine neuron ensembles encode the specific identity of surprising outcomes. This work is an extension, and more in depth analysis, of two previously published studies by these research groups who previously demonstrated that (putative) dopamine neurons or midbrain BOLD signals do not only signal surprising changes in value (as generally assumed), but also signal sensory prediction errors (i.e. value-neutral violations in expected outcome identity). Here, the authors take this a step further, using a decoding analysis to show that the firing pattern in putative dopamine ensembles or midbrain fMRI signals also encode the specific identity of the surprising outcome. This has potentially far-reaching implications for our understanding of the role of dopamine in learning.

Decision letter after peer review:

Thank you for submitting your article "Dopamine neuron ensembles signal the content of sensory prediction errors" for consideration by eLife. Your article has been reviewed by three peer reviewers and the evaluation has been overseen by Kate Wassum as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

You will see that the reviewers were very enthusiastic about the paper, but raised a number of overlapping concerns. We expect you will make good faith effort to address each of the concerns noted in the appended reviews. We especially direct your attention to the following:

1) Discuss the problem of dimensionality (i.e., the vastness of potential sensory prediction errors relative to the number of dopamine neurons; reviewer 2 point 2) and of the limitations of using 2 outcomes in this task.

2) Discuss of the limitations of the decoding analysis approach (reviewer 3 point 1) including whether or how this information might be read out in the brain (reviewer 2 point 1).

3) Apply the decoding analysis to the value prediction error phase of the task to ask whether DA/midbrain ensembles encode outcome identity when the presence of the outcome altogether, not only its identity, is surprising (reviewer 1 point 1).

4) Discuss how these data are compatible (or not) with evidence that optogenetic activation, which activates DA neurons, but disrupts the precise firing pattern of DA ensembles, can promote learning about the sensory features of an event (reviewer 1 point 3).

Reviewer #1:

In this study, Stalnaker et al. make the original and thought-provoking argument that dopamine neuron ensembles encode the specific identity of surprising outcomes. This work is an extension, and more in depth analysis, of two previously published studies by these two research groups (Schoenbaum and Kahnt) who independently demonstrated that (putative) dopamine neurons do not only signal surprising changes in value (as generally assumed), but also signal sensory prediction errors (i.e. value-neutral violations in expected outcome identity). Here, the authors take it a step further. Using a decoding analysis, they present converging evidence from single cells recording in rats (experiment 1) and fMRI in humans (experiment 2) showing that the firing pattern in dopamine ensembles also encode the specific identity of the surprising outcome. This has potentially far-reaching implications for our understanding of the role of dopamine in learning.

The results are compelling, data are presented in a manner that is easy to understand, interpretations are logical, and the manuscript is very well written. The inclusion of rodent and human work in the same paper is commendable. Although some results from these datasets have already been published, the type of analyses and the conclusions derived from these analyses are clearly novel, and well beyond what was previously published, and justifies a separate publication.

- Encoding of sensory information in "classic" reward prediction errors?

It seems that the decoding analysis was applied strictly to the portion of the task that features identity prediction errors (value-neutral switch from O1 to O2). But what about the portion of the task that features "classic" reward prediction errors? Is there also evidence that DA ensembles encode outcome identity when the presence of the outcome altogether, not only its identity, is surprising (arguably the most common scenario when organisms learn about outcomes)?

- Functional role for sensory information in DA prediction errors?

Authors propose that the information about the identity of a surprising outcome contained in the firing pattern of DA ensembles, instructs downstream areas what to learn. The authors should highlight how this hypothesis is a significant shift from the way prediction errors (even sensory PE) are generally conceived (i.e. as permissive signals for learning, with the content of learning being determined by activity in downstream regions, e.g. Glimcher, 2011). The authors should also consider discussing how this new hypothesis fits with the highly divergent and overlapping nature of DA projections (Arbuthnott and Wickens, 2007; Matsunda et al., 2009; Bolam and Pissadaki, 2012).

- The authors cite studies showing that DA firing promote learning about sensory features of an event. Some of these studies (Sharpe et al., 2017; Keiflin et al., 2019) used optogenetic activation, which activates DA neurons as a whole but most likely disrupts the precise firing pattern of DA ensembles. How is that compatible with the idea the precise pattern of firing in DA ensembles instruct the content of learning?

Reviewer #2:

This paper studies the population activity of dopamine neurons in rodents and midbrain BOLD in humans and shows that it is possible to decode more sophisticated aspects of predictive failures than would be implied just by changes in scalar value. In particular, a change from an outcome of one flavor (rodents) or sweet vs. savory (humans) is decodeable from this population activity.

In short, this is a very well conducted pair of studies, and the results and the analyses are convincing. The paper relates well to previous studies looking at less scalar aspects of the dopamine signal, adding an interesting new perspective.

My main concern is that the underlying implications are not so clear:

- Many dopamine cells have exuberant axonal arbors (although for sure, more in the SNc than the VTA) – thus the experimenter's ability to decode this signal from individual cells may vastly outweigh the ability of downstream neurons or tissue to do this decoding. It would be good to be convinced that this signal had a way of actually mattering. The fMRI results don't constitute such a proof.

- Related to this – what my computational colleagues refer to as the dimensionality of the problem seems unfavorable. The number of possible juices, let alone things of equivalent value, that could be substituted, is vast. They have elaborated representations in various regions of the cortex which is sized to match. However, there aren't many dopamine neurons. Thus, the fact that there is a reliably decodable signal – coming, for instance, from the upstream sampling properties of individual dopamine neurons (e.g., if they get somewhat random collections of inputs) – when there are only two choices, and the chance to build a sophisticated decoder bears little on the real problem of making state- rather than value-based prediction errors be useful.

Reviewer #3:

This study examines the role of dopamine neurons in sensory prediction errors, which are signals that indicate an event that violates expectancies, independent of the value of the event. The authors show that the response of single dopamine neurons detects sensory violations, but they don't necessarily discriminate between different kinds of violations. However, at the population level it is possible to decode the nature of the violation. In addition, they show that a similar pattern of results can be obtained in humans using fMRI. The study is a solid contribution to the literature and its interpretation is relatively straightforward. The task is well-designed, the analyses are appropriate, and the results are clear.

1) The Discussion should do more to couch the interpretation of the results. A danger with decoding analyses is that just because something can be decoded, it doesn't necessarily mean that the brain is using that information. For example, it would be relatively straightforward to decode line orientation from retinal ganglion cells, even though we know that these cells are not encoding this information.

2) Figure 3A: The mountain plot obscures the data. I'd suggest just plotting the top-down view and allowing the color to represent decoding accuracy.

3) Figure 3C: I don't know why this data has been spatially smoothed. Confusion matrices are not continuous.

4) Figure 4D: The description in the figure legend is confusing. The first sentence states that decoding accuracy was above chance on the error trial, but then the next sentence states that it was not above chance on this trial.

5) Figure 4E: Unlike Figure 3C there are no stats to support the claims as to what data is or is not significant.
