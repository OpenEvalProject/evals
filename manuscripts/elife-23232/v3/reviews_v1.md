# Peer review - Round 1

Editors:
- Klaas Enno Stephan, University of Zurich and ETH Zurich , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23232.035](https://doi.org/10.7554/eLife.23232.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dynamic Modulation of Cortical and Behavioral Decision Biases by Brainstem Arousal Systems" for consideration by eLife. Your article has been favorably evaluated by Sabine Kastner (Senior Editor) and three reviewers, one of whom, Klaas Enno Stephan (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Micah Allen (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary of manuscript:

This study examines biases in human perceptual decision-making processes, testing the hypothesis that they may arise from fluctuations in the activity of neuromodulatory brainstem nuclei, such as the locus coeruleus, which may correspond to variations in arousal. Participants performed a simple forced choice perceptual detection task in the MRI scanner while their pupil responses were tracked. The authors report that larger peri-response pupil sizes were associated with reduced bias, and that pupil size variation was reflected by activity in prefrontal and parietal cortex, the basal forebrain, and noradrenergic and dopaminergic brainstem nuclei. They conclude that phasic arousal signals explain a significant portion of choice variability. While the authors have reported the behavioral effects previously (de Gee et al., 2014, PNAS), the current paper goes an important step further in examining potential neurobiological mechanisms.

Summary of reviews:

Overall, all reviewers agreed that the paper represents an important step forward in understanding possible neurobiological determinants of choice variability. However, they also thought that the paper was densely written and not easy to read, and they identified a number of issues that would need to be addressed in a revision of the paper.

The policy of the journal is to provide you with a single set of comments which reflect the consensus view amongst reviewers. These comments can be found below and must be addressed convincingly. We hope that you will find these comments helpful to further improve the paper.

1) The paper is densely written and not easy to read. Given that the eLife does not impose length restrictions, you would have the liberty to explain your rationale, analyses and findings in a less condensed way. We think it would be very helpful for most readers and would enhance the reception of your paper if you could consider this and reformulate the text where you think it is appropriate.

2) The fMRI analysis of effects of phasic arousal (as indexed by TPR) on sensory responses in visual cortex (subsection “Phasic arousal predicts a reduction of accumulation bias”) appears to be unnecessarily complicated. Would it not be much simpler (and arguably more direct) to test for TPR x stimulus interactions, using a standard GLM?

3) A similar concern applies to the next section, the fMRI analysis of phasic arousal on decision-making (subsection “Phasic arousal predicts selective changes in frontal and parietal decision signals”). The analysis presented does not refer to computational variables (from the drift diffusion model) but tests for an effect of TPR on decision-making in an indirect way (differences in lateralisation of activity between low and high TPR trials). Against this background, the conclusion that "[…] the selective effect of phasic arousal on behavioural bias is mediated by a selective modulation of cortical decision signals" (our emphasis) seems a little overstated; testing for interactions between TPR x drift rate interactions would have been more convincing. Furthermore, it would help if you clarified what exactly you mean by "selective" (this word occurs frequently throughout the paper) and how in this analysis you operationalise "lateralisation".

4) The analysis of association between TPR and activity in brainstem nuclei is compelling as it does not restrict itself to the locus coerulus. Having said this, it is not clear how/whether you corrected for multiple comparisons – could you please clarify?

5) Several aspects of the mediation (structural equation modeling) analysis are not clear. First, it is not clear why the structural model presented is the most obvious choice, and it would be helpful to see a model comparison (e.g., based on BIC) against at least two alternative models: (i) a model that does not allow for the indirect path (i.e. a model lacking the path from TPR to Ctx); (ii) a model without stimulus input into Choice. Second, what exactly is the "cortical response" in Ctx? Third, where does the "predicted probability that the subject made a yes-choice" (subsection “Mediation analysis of TPR effect on cortical signals and behavior”) come from?

6) Psychologically it is unclear whether there might be alternative interpretations of what the variations in pupil size reflect. Given that activity fluctuations in multiple neuromodulatory nuclei show a relation to TPR, is a strong conclusion/interpretation in terms of a "phasic arousal signal" warranted? This may be an obvious interpretation for noradrenaline, but is this an appropriate interpretation for dopamine and acetylcholine? For example, could something like motor confidence, (violations in the) expectation of being correct, or simply fluctuations in attention represent alternative interpretations?

7) It would be helpful if the relation of pupil responses to response times could be illustrated. Relatedly, could you verify that you did not decode differences in response times in the multivariate choice analysis?

8) Although it used to be standard practice for the authors of psychophysics papers to be subjects too, one wonders whether in this case, the inclusion of authors as subjects may have biased the findings, given that they knew the results of the previous paper. Do the results quantitatively remain the same when excluding the two authors? Relatedly, one subject performed significantly more trials than the other subjects (640 instead of 400-480 trials). Please specify whether this was one of the authors and demonstrate that this subject did not bias the findings.

9) A sense factor of 3 is relatively high, and one might be concerned that residual aliasing or noise enhancement affected the data. Could you please address this?

10) Model comparison (subsection “Phasic arousal predicts a reduction of accumulation bias”): do the DIC values reported reflect an overall group result, i.e., was the model treated as a fixed effect in the population? If so, did you verify that this result was not driven by a single or few outliers (a random effects analysis would protect against this)? Do AIC or BIC provide for converging conclusions?
