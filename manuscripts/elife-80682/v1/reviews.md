# Peer review - Round 1

Editors:
- Steffen Rulands, https://ror.org/01bf9rw71 Max Planck Institute for the Physics of Complex Systems Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80682.sa0](https://doi.org/10.7554/eLife.80682.sa0)

This paper is a fundamental work in developmental biology that supports its findings with compelling evidence drawn from both theoretical and experiment insights. It provides a potentially general mechanism for the control of a proliferative cell population. This work will be of interest to researchers in the fields of developmental and stem cell biology.


---

# Peer review - Round 1

Editors:
- Steffen Rulands, https://ror.org/01bf9rw71 Max Planck Institute for the Physics of Complex Systems Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80682.sa1](https://doi.org/10.7554/eLife.80682.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mother cells control daughter cell proliferation in intestinal organoids to minimize proliferation fluctuations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Didier Stainier as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Philip Greulich (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please clarify the model definition such that there is no ambiguity regarding whether the compartments pertain to fate or proliferation (Reviewer 2).

2) Please clearly line out in the text how this model is to be interpreted by a readership that might not be familiar with mathematical modelling and in particular the way "simple" models as the one presented here relate to potentially more complex biology. Specifically, as Reviewers 1 and 3 point out, it needs to be discussed whether the compartment model should be interpreted at face value or whether it is a simplified mathematical description for potentially diverse biological scenarios.

Reviewer #1 (Recommendations for the authors):

The manuscript would benefit from a discussion of the scope of the findings, in particular the modelling results. The authors propose a compartmentalized model, which is to be understood as a coarse-grained mathematical description of a potentially diverse set of biological realities. The authors should be clearer in the discussion about what is the precise biological scope of the mathematical model.

L53: The final sentence of this paragraph is not clear. Presumably, the authors mean "fluctuations in the number of proliferating cells".

L97: The definition of proliferating cells of course strongly depends on the ratio of the typical cell cycle time and the time of duration of the experiment. Can the authors give a statistical estimate on the percentage of cells being misclassified as "non-proliferating" due to the finite length of the observation interval?

L104: It would help the readers if the authors briefly stated the basic assumptions underlying the "simple model of cell proliferation" in the main text.

L108: I was at first very confused about the naming of the variable D describing the number of proliferating cells. I would usually associate "D" with a diffusion coefficient with units m2/s while the number of cells is dimensionless. The authors might consider renaming this variable to "N".

Figure 2A, B: To my eyes, there are oscillations in the number of cells and partially the number of proliferating cells. Is this evidence for temporal synchronization of cell divisions?

Figure 2B: This figure would benefit from a statistical analysis of the slopes as it is not evident to me whether the majority of lines have a vanishing slope or positive slope.

Figure 2B, D: Could the enrichment of even clone sizes have arisen by chance (p-value)?

Reviewer #2 (Recommendations for the authors):

I have a few comments though on a few additional analyses/theoretical controls that might help the paper even more readable – especially as model-data comparisons are sometimes not the most straightforward in presentation, making me unsure I fully follow the reasoning in places.

Point A/ Figure 4: the text is in general well-written, although I had to re-read this a few times this part to make sure I fully understood the model. I feel like calling the two domains "proliferative compartments" vs "non-proliferative compartments" is a bit confusing, because in fact the compartments are not implemented through changing proliferation, but instead changing fate.

On the first read, I thought the model would be that the authors would simply turn on proliferation in the bottom compartment, and turn it off in the other. In fact, I wonder – given the fact that Figure 2 identifies each compartment by proliferation rate, whether it would be pedagogical for the reader to go through this model first (it can be in SI obviously). I guess the point of the author is that this model would fail vs data. But it would be interesting to see exactly how, to set the stage for their model (because as the best-fit requires anyways \α_p close to 1, this might give rise to similar predictions?). Plotting the model output in the same way as the previous data from Figure 2C-D might also be nice for comparison.

The last thing where I got confused by the model is that it implements compartments in a spatial way – if I understand correctly (line 637 of the SI). But the point of the authors, based on data, is that fate of daughters is dependent on lineage rather than position (although they say in lines 646-647 that the two are highly correlated in the model for the rT they choose – see also point below). It would be good to clarify this.

Point B: Also in Figure 4, it is not very clear how the authors pick their rearrangement rate rT (lines 188-191). They say that they pick rT=1 to reproduce well the correlation between cousins, but that they find similar findings for larger rT. Would this mean then that this parameter is not necessary for the model, and that this leads to over-fitting? (But then I got a bit confused as in the Supp part, they say large rT do no work? (Line 644-646). As the authors have done high-quality tracking, I would have thought that maybe they could "just" infer this parameter from the x,y,z, and t coordinates of neighboring cells. This would help distinguish model fitting and model prediction in a better way in the manuscript. In general, maybe the authors could use the modelling section on the SI to summarise a bit the fitting and prediction strategy (and maybe provide in Figure S5 a more systematic fitting/sensitivity analysis rather than showing two extreme values only of rT?).

Point C: Figure 6: Maybe the authors could define an "asymmetry index" (eg. the cumulative probability "missing" from the odd clones assuming some smooth gaussian from neutral drift without lineage correlations). I also wonder whether the authors could recapitulate their findings in a toy model of stochastic fate choices with correlation time T in outcome (to connect it more directly to previous models of neutral drift on a 1D ring). This type of model making correlation time in fates an explicit variable would go well with the discussion on the number of generations at which correlations in fate are lost (line 360-370). It would also be nice to mention the consequence that this would have on longer-term clonal conversion dynamics that have been extensively studied in the past.

Reviewer #3 (Recommendations for the authors):

As said in the public review, my concern is to take the two-compartment model too literally. I do agree that the presented analysis is fine, and the two-compartment model works as a valid simplification to capture the qualitative features of the mechanism, but I am worried that the reader takes this at face value. Instead, given the measurements in Figure 5E, it is more likely that the proliferative potential decreases continuously with distance from Paneth cells. So while the two-compartment model works as a simplification of the numerical analysis (being a representative of a larger class of models where proliferative potential decreases with distance), it does not work well as a description of reality.

Further suggestions, questions, and corrections:

– When saying that fractions of asymmetric divisions are "low" (e.g. line 135), then this should be compared with the case to be expected when sister cell fate is unrelated: namely in that case, asymmetric divisions would be at 50%.

– For α=0 one wouldn't expect uncontrolled exponential growth as stated in line 170. Stochastic fluctuations can be very large for α=0, even exceeding the set threshold of 5-fold, but this is still not exponential growth. It should also be mentioned that this may depend strongly on the arbitrarily set threshold.

– In line 195 it is said that "stochastic depletion occurred when α_p <~ 0.5". However, the scale in the referred figure is set arbitrarily. Since there the depletion rate is always non-zero, depletion will always occur after sufficiently large times. So when saying "stochastic depletion occurred when α_p <~ 0.5", then it should be said over which time scale of observation this is meant.

– In the caption of Figure 1 the part for panel G should refer to panel F instead.

– Figure 5: the colours are difficult to distinguish for a red-green colour impaired reader (roughly 10% of the male population): orange vs. green is difficult to distinguish and the thin black font colour vs. thin red font colour of vertical axis labels in Figure 5E are difficult to distinguish.

– The value of phi reported in Figure 5E (phi=0.98) is significantly higher than that reported in Figure 3A (adding the symmetric events when both sisters go on dividing, never dividing, or dying, gives phi = 0.81). Where does this discrepancy come from?

– Figure 6D: It would be helpful to have an interpolation curve to see the enrichment at n=6 (currently this is not visible). Alternatively, plotting on a logarithmic scale could make this more visible.
