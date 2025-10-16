# Peer review - Round 1

Editors:
- Jonas Obleser, University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70907.sa0](https://doi.org/10.7554/eLife.70907.sa0)

Kluger and colleagues investigated the influence of respiration on visual sensory perception in a near-threshold task and argue that the detected correlation between respiration phase and detection precision is liked to α power, which in turn is modulated by the phase of respiration. The main finding is that the moment-to-moment relationship between excitability and perception in turn is coupled to the body's slower respiratory oscillation. This advances our understanding of how the brain-body system works as a whole.


---

# Peer review - Round 1

Editors:
- Jonas Obleser, University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70907.sa1](https://doi.org/10.7554/eLife.70907.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Respiration aligns perception with neural excitability" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andreas Draguhn (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Above and beyond the major points of revision raised in the individual reviews, we have agreed on the following queries to be addressed by new analyses (and/or new data, although we are not asking for new data as a hard criterion, obviously, given the current situation):

i) the paper needs more evidence for causality, rather than correlation, including data supporting the specificity of effects for α (compared to other frequencies).

See detailed comments by the Reviewers regarding these issue below.

As an editorial hint, here the authors might want to look into state-of-the-art statistical approaches to inferring causality from observational/correlational data (for review see e.g. https://doi.org/10.1038/s41562-018-0466-5).

At the very least, the question of causality should at least be discussed more explicitly and all causal or causality-insinuating language should be avoided where not warranted.

ii) While we will not ask for new data as a hard requirement in the face of the curren pandemic, the authors should take note of our general concern about the lack of insights in underlying mechanisms; the reviewers feel the authors should at least consider interventions like mouth versus nasal breathing. This would also contribute substantially to the causality-related questions.

iii) better acknowledgement of earlier efforts and findings re. α and breathing and breathing and visual perception is in order. See comments esp. by Reviewer 2 below.

Reviewer #1 (Recommendations for the authors):

1. As described above in the public review, it seemed to me to be assumed that respiration causes fluctuations in α power, and fluctuations in α power in turn cause fluctuations in behavior (or we can speak of excitability, and maybe α power is a reflection of that, I'm not hung up on this). Could it be that respiration and α are both fluctuating on their own, and both influence behavior, but the two signals are not connected? I realize that the phase-amplitude coupling analysis is supposed to answer this question. However, this analysis seems problematic in that activity in frequency bands spanning 5-40 Hz (theta to low γ) is coupled to respiration. So there's nothing specific about α/excitability that is related to respiration. Is it possibly the case that "measurability" (signal-to-noise ratio) is rather respiration coupled, as opposed to neural excitability? So, brain activity for whatever reason is easier to measure at certain phases of the respiration cycle? And therefore the brain-behavior relationship is clearer or stronger? That would be boring, but I think important to discuss / rule out. One possibility for the α-causality issue would be some kind of causal or moderator analysis. I'm not an expert, but I think there are some exciting new statistical techniques that could be useful here. I'm less sure about how to better assess the α-specificity of the effect, or to conceptually deal with an unspecific effect.

2. I was not able to understand the analysis that involved shifting the α time course. Unfortunately, I'm not sure what to recommend here, because I really didn't understand well enough to advise on how to make it clearer. I wonder whether a didactic analysis figure panel as part of Figure 4 might help?

3. I think there are a few ways to update the analyses of the psychometric thresholds to make the results more interpretable and also to be more parallel across sections.

– First, the authors use the sine and cosine of a circular predictor in their regression. They then interpret the β values and statistics separately for the two predictors. I think the more common and meaningful approach is to recombine the betas into a single value that reflects the predictive power of the phase predictor, and then calculate corresponding statistics for the combined value. To do so, take the root-mean-square of the b1 and b2 values, sqrt(b12 + b22). Since this value will always be positive, it is often tested for significance using a permutation-based approach, which the authors are already comfortable with. I recently learned that this approach is called "harmonic regression" (for googleableness).

– The approach I described above to recombine betas for the phase predictor will not work in the first analysis the authors present based on mutual information. Actually, I was wondering why the authors chose this approach, when a logistic regression would have worked equally well, would have been more cohesive with the other analyses in the paper, and would afford the same model-comparison approach as they used for the other analysis, instead of the Wilcoxon test on MI values. I would suggest that the results would be more streamlined with a regression approach here that algins with the other sections.

– It might also be nice to substitute the hits > misses contrast on α power with a regression approach examining how α power changes psychometric thresholds so that the analyses start to align better across sections.

4. I think I didn't fully follow the logic in the Intro/Discussion regarding the one of the paths by which respiration might affect excitability. In particular, for the route via the olfactory bulb, it wasn't clear to me how phase-amplitude coupling between slow olfactory, respiration-coupled phase and amplitude of "faster oscillations" would structurally or functionally lead to fluctuations in amplitude of parieto-occipital α oscillations. Is this known, or is this rather for future work?

5. The conversion of the normalized respiration time course to phase involved using Matlab's findpeaks function, assigning peaks and troughs values of 0 and {plus minus} π, respectively, and then linearly interpolating the phase values between them. This seems odd, especially as the later analysis (p. 25) accomplished the same thing via the Hilbert transform (more what I was expecting). I also would ask how, given that values between peak and trough were interpolated, it would be possible to see phase slips and nonlinear phase transitions, as in Figure 1d.

Reviewer #2 (Recommendations for the authors):

The study should include a comparison between nasal and oral breathing with reliable monitoring. Video alone might not suffice.

The analysis of the MEG signal should be extended to the entire frequency spectrum captured by the method.

If blood CO2 is the suspected mediator between breathing cycle and excitability the authors should consider manipulations that alter this parameter, using for example, controlled shallow vs. deep breathing.

Reviewer #3 (Recommendations for the authors):

Specific recommendations (not sorted by priority):

i) Introduction, lines 75-77: The sentence is a bit puzzling. It starts with "The bidirectionality…", but this bidirectionality had not been introduced previously to the reader. Rather, the connections mentioned in the second part of the sentence may lead to / explain such bidirectional relations.

ii) The raincloud plot in Figure 1c is not easily understandable to unfamiliar readers. Please explain in some detail and, if possible, label x-dimension.

iii) Figure 2c: Can you please provide an additional panel with extended contrast resolution (x-axis) to illustrate the dispersion of the curves more clearly? At present, density of curves and lacking contrast make it almost impossible to see the details.

iv) Figure 3b shows an apparent strong performance-dependent difference in α power AFTER stimulus presentation. This should be made explicit and discussed. Could it be that the difference in this phase of the experiment does also affect the behavioral decision which, obviously, comes after presentation?

v) Figure 4c does also need a more thorough explanation to be understandable.
