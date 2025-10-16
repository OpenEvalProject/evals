# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- Dan FM Goodman, Imperial College London United Kingdom

## Review text

DOI: [10.7554/eLife.44526.021](https://doi.org/10.7554/eLife.44526.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "State-dependent geometry of population activity in rat auditory cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Dan Goodman (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Kobak et al. study the representation of sounds in primary auditory cortex (A1) as a function of their overall loudness (absolute binaural level or ABL) and of their azimuth (inter-aural level difference or ILD). Using silicon probe recordings of populations of neurons in urethane anesthetized rats, the authors ask how the encoding of ABL and ILD depends on the brain state. They report on two main discoveries. First, they find that the more activated the state, the weaker is the preference of the neurons towards contralateral and/or loud sounds. Second, they consider the geometry of the firing rate vector, and report that in the more active states the representations of ABL and ILD become almost orthogonal to each other and to the axis of overall activity level.

The paper is well written and addresses a major issue of interest to both theorists and experimentalists. The results will help guide the theory of neural coding, and provide a useful framework for future analyses of population activity. What makes the study most interesting is the state dependence reported by the authors, which can be seen in simpler measures and is nicely summarized with their geometric picture. Prior work suggests that neural codes themselves are state dependent, and the current manuscript is a significant new contribution to this line of research.

However, a few issues were identified that need to be addressed before the manuscript can be published.

Essential revisions:

1) On the z-score(Mean firing rate) formula, Equation 1: I think the "subtracting 40" from the ABL values needs some better justification. Why 40? Also, I'd like to see a short explanation, and certainly a reference, justifying why the interaction term (ABL-40)*ILD is the right one for capturing the effects of gain modulation. Most importantly, given that the gain modulation is not working quite as expected, I would really like to know what happens when you remove that interaction term from your formula. This will yield different fits for βILD and βABL. If you re-do the analyses of Figure 3 using those fits, are the results qualitatively the same? Given that many of your insights depend on interpreting these coefficients, I'd like to make sure these results don't depend too much on the precise form you chose for Equation 1.

2) It appears that the geometry analyses were carried out using spike counts over the entire 150ms duration of the stimulus. However the PSTHs (Figure 2 and Figure 2—figure supplement 1) demonstrate that in the active state (or in up states) the late part of the response consists of reduction in firing rate relative to the baseline, which is not the case for the inactive state. It should be clarified whether this suppression of firing is the key to the orthogonality of the representations of ABL or ILD, or if it holds for the onset response as well. Also, is the 1st mode (PC) of the onset response (20-40ms) the same as the 1st mode of the late (70-150ms) portion of the response? Related: is it the case that the values in Figure 3—figure supplement 3A and B are (almost) identical whereas the values in Figure 3—figure supplement 3E and F are not? I believe providing this information is of major importance, e.g. it might suggest that in the active state the response has a second part, which is absent in the inactive state.

3) One of the main shortcomings of the study is that it was performed under anesthesia, hence there is always the question of to what extent the results apply to awake and behaving rodents. This would be even more worrying if it turns out that suppression of firing by the auditory stimulus is key to the presented results (point 3 above), as that would rely on the existence of a highly active state which seems rather unique to urethane. Indeed, McGinley et al. (McGinley et al., 2015) suggest that the best brain state for auditory detection (in awake and behaving rodents) is of moderate rather than high activation. At the very least this point should be included in the Discussion.

4) In the analyses of the signal and noise correlation matrices, you compute (a) mean correlation, (b) fraction of variance by first PCA component, and (c) the dimensionality. This last item is not as self-explanatory as the first two, and it's important to say a bit more in the main text about what exactly you mean by "dimensionality," and how you estimate it. In other words, please don't relegate the entire discussion of this to the Materials and methods, as it is an important point.

5) If I understand correctly the evoked response of every recorded neuron was used. In such studies it is typical to find a substantial percentage of neurons without statistically significant sensory responses. First, it is important to report the percentage of neurons with significant ABL/ILD tuning as a function of brain state. Second, what is the impact of those non-tuned neurons? Some of the analyses (e.g. Figure 3) would benefit if such neurons were excluded. In fact, one probably should only use neurons that show significant tuning to ABL or ILD (or their interaction), otherwise neurons that simply respond to an up-state triggered by the stimulus (Figure 2—figure supplement 1D) would be included as well.
