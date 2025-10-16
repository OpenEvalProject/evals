# Peer review - Round 1

Editors:
- Joseph W Kable, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65661.sa0](https://doi.org/10.7554/eLife.65661.sa0)

This paper will be of interest to neuroscientists studying decision-making and the frontal lobe. On balance, the data provide more support for the view that the dorsolateral prefrontal cortex is involved in reading out the evidence in favor of different choice alternatives than the view that this region implements control processes that bias choices towards normative goals.


---

# Peer review - Round 1

Editors:
- Joseph W Kable, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65661.sa1](https://doi.org/10.7554/eLife.65661.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Evidence accumulation, not "self-control," explains dorsolateral prefrontal activation during normative choice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) One concern is about potential circularity in the analyses of the dlPFC activity. Given that the ROI is identified via a model-based fMRI analysis with the anDDM predicted activity, isn't the current strategy of testing choice-related activity in this region (GLM2 analyses like Figure 4 d-f) a case of circular-analysis /double dipping (Kriegeskorte et al., 2009)? Wouldn't this bias the subsequent tests in this region of whether activity is higher for normative (generous, healthy) versus non-normative (selfish, tasty) choices towards the predictions of the anDDM? In this case, a stronger and more convincing test might be to show that these results hold in a region defined a priori based on previous studies arguing that dlPFC modulates attribute weights (e.g., Hare's work).

2) A second concern is how well the model is recoverable. It would be helpful for the authors to demonstrate parameter recovery, or point the reader to where those results can be found, if they were shown in prior work. (Regarding modeling quality control, the authors may want to consult the guidelines of Wilson and Collins, 2019).

(a) On a specific note, there is skepticism about the need for both input inhibition (v1-v2) as well as inhibition between the accumulators (zeta). How well is this zeta parameter recovered, particularly under minor to major misspecification of the drift rate function v? For instance, if v is in reality non-linear, or has an intercept (see above), might the currently mis-specified drift rate function result in what looks like a non-zero zeta?

(b) There is also a specific question of why the authors constrain zeta and γ in the model fits. By doing so they essentially guarantee concluding that there is self-excitation and mutual inhibition. Constraining parameter values shouldn't be necessary (though constraining the starting values of the search makes sense). All it does, potentially, is to turn a zero mean, high variance distribution into one with less variance but a biased mean.

3) A third question concerns the uniqueness of the neural predictions of the anDDM model. This should be clarified in the revision, specifically with regard to:

(a) Do the predictions of the anDDM differ from those based on a simpler notion of preference strength (e.g. Utility chosen option – utility unchosen option)? What about a conceptualization based in terms of default option/framing (Lopez-Persem et al., 2016)? Or would a model that focuses on conflict/choice difficulty/inverse confidence (Shenhav et al., 2014) make similar predictions? The authors may want to consider a more comprehensive model-comparison/model falsification approach (Palminteri et al., 2017) to validate their computational proposition at both the behavioral and neural activity levels.

(b) Do the predictions depend on specific modeling choices in the anDDM? For example, does a simpler attribute-weighted drift diffusion model (without the self-excitation and mutual inhibition components of the neural model) make similar predictions or not? Do the predictions depend on the specific linking function between model output and neural activity, since alternative formulations could be envisioned here (e.g. sum of the difference -rather than sum- of activity between the 2 neuron pools over time)?

(c) What about a simple account based on reaction time? What would happen, e.g. if RT is added as a parametric regressor (to the boxcar) and competed with the anDDM predictions?

(4) A fourth concern is about the strength of the neural evidence. The evidence on balance favors evidence accumulation, but perhaps not as strongly as one might hope. Where the evidence accumulation and attribute weighting/inhibition hypotheses make different predictions are in the conditions where regulatory focus is on normative goals – attribute weighting would predict greater activity for normative choices while evidence accumulation would predict greater activity for non-normative choices. Only one of the three tests here (health focus in food choice) provides straightforward support in one direction (favoring the evidence accumulation account). The other two tests (ethics and partner focus in altruistic choice) show no difference in activity, which isn't supportive of the attribute weighting account, but seems only weak evidence in favor of the evidence accumulation account. The test of whether regulatory instructions increase or decrease activity in dlPFC is similarly ambiguous, hardly supportive of the attribute weighting account, but only weakly supportive of the predictions of the evidence accumulation account. Furthermore, about half of the ROI critical tests (in Figure 4 e-f) are quite borderline (non-)significant (between P = 0.02 and 0.07). Overall, the strength of the neuroimaging evidence in favor of the proposed theory seems moderate at best.

(a) One response would be the authors to simply acknowledge these issues and temper their claims accordingly.

(b) Alternatively, multiple reviewers wondered if the authors could exploit individual differences to gather further support for their claims. For instance, for Study 3, in the Natural condition, could the authors only analyze subjects who overwhelmingly preferred tasty foods? Or, if the sample is large enough, the authors could look for brain-behavior correlations? Do subjects who show a larger behavioral weight asymmetry also show a larger DLPFC asymmetry?

5) Finally, the authors should address two specific critiques that might be raised regarding their manipulations in Studies 2 and 3. Several possibilities for how to address these were suggested, but beyond these specific suggestions, the essential thing is that authors somehow consider these critiques in the manuscript and rebut them.

(a) One potential critique of Study 2 is that subjects in the instructed conditions (focus on ethics, focus on partner) might take the instructions too literally and essentially be solving math problems rather than truly valuing the outcomes. This would make it less of a value-based decision-making task and more of a perceptual one. Presumably this would disengage the DLPFC, and the other regions. Could the authors comment on whether the standard "reward" regions, e.g. VMPFC, striatum, were active during these conditions? Is there similar evidence that the DLPFC, dorsal ACC, and insula reflect accumulated evidence in perceptual decisions? Are the absolute levels of activity (shown in Figure 4e) meaningful, in terms of saying whether the DLPFC was still engaged in these conditions? Another thing that would make the results from this study more compelling would be if the authors found a significant difference-in-differences between "Natural" and "Partner" conditions in DLPFC or other areas. This would help to alleviate concerns that brain activity is just noisier in the "Ethics" and "Partner" conditions.

(b) A potential critique of Study 3 is that the DLPFC is simply responding to disobeying the experimenters' instructions. Is there any way that the authors can rule this out? Could the authors use a more continuous analysis to show that decisions with a subjective value difference of zero show the most activity in DLPFC, while those with large subjective value differences, in either direction, show less activity? One particular reason for this concern is the lack of correspondence between the behavioral and fMRI data. The naDDM reveals nearly identical behavioral weights in the Natural and Taste conditions, and yet the DLPFC are very different. How can we make sense of this?

Friston, K.J., Penny, W.D., and Glaser, D.E. (2005). Conjunction revisited. NeuroImage 25, 661-667.

Kriegeskorte, N., Simmons, W.K., Bellgowan, P.S.F., and Baker, C.I. (2009). Circular analysis in systems neuroscience: the dangers of double dipping. Nat. Neurosci. 12, 535-540.

Lopez-Persem, A., Domenech, P., and Pessiglione, M. (2016). How prior preferences determine decision-making frames and biases in the human brain (eLife Sciences Publications Limited).

Palminteri, S., Wyart, V., and Koechlin, E. (2017). The Importance of Falsification in Computational Cognitive Modeling. Trends Cogn. Sci. 21, 425-433.

Shenhav, A., Straccia, M.A., Cohen, J.D., and Botvinick, M.M. (2014). Anterior cingulate engagement in a foraging context reflects choice difficulty, not foraging value. Nat. Neurosci. 17, 1249-1254.

Wilson, R.C., and Collins, A.G. (2019). Ten simple rules for the computational modeling of behavioral data. ELife 8, e49547.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Evidence accumulation, not "self-control," explains dorsolateral prefrontal activation during normative choice" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The reviewers appreciated your substantial and responsive revisions, but also identified some remaining issues that should be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors have comprehensively addressed the previous round of concerns and the revised manuscript is stronger and more compelling as a result.

Reviewer #2 (Recommendations for the authors):

The authors have done an admirable job addressing the review team's comments. They looked into parameter recovery and ultimately decided to go with a simpler model that yields similar conclusions. They also added a couple of datasets to Study 3 to help bolster those results.

My overall impression of the paper is fairly positive, though some of my previous reservations remain. To really convincingly make their point, the authors would have ideally shown a dataset where DLPFC activity is significantly higher for the hedonistic choice – an actual reversal of the phenomenon, rather than just elimination of it. This weakness is somewhat mitigated by the individual difference results, though I think that should be expanded on in the paper, since right now they only report it for Dataset 1, and they don't fully report the statistics for Datasets 2 & 3 in their replies.

I also thought that the very last section of the Results section was weak and could, maybe should, be removed. I think the authors have already demonstrated by this point in the paper that the activity in DLPFC is not simply responding to the condition. It's strange to report these main effects but then immediately dismiss them as likely being due to evidence accumulation. For that matter, the lack of effect in Dataset 2 could also be spuriously due to evidence accumulation canceling out an actual main effect. This last section is just messy and I don't see why it's helpful.

I thought that the reference list could be improved, given the focus of the paper. There are multiple mentions of value DDM and fMRI investigations of this, and yet there were no references to the value DDM work by Milosavljevic and Krajbich (2010) or the older work by Busemeyer and colleagues. There were also no references to the fMRI studies on value DDM by Gluth et al. (2012), Rodriguez et al. (2015), Pisauro et al. (2017), etc.

I also had some issues with a couple of the figures.

Figure 2 – I do not understand how the axes are coded. The dependent variable is %healthy choice, so you would think the axes would be the difference in tastiness and healthiness between the healthy and unhealthy options. However, both of those differences go from -3 to +3, indicating that that's not the case – the healthy option can't be less healthy than the unhealthy option. It seems to me that there should only be the top half of each of these figures. It's also unclear why these figures are mostly red, indicating a preference for healthy options, even when the weight on taste is higher. Is this due to the intercept in the model? If so, that would be useful to clarify. Finally, is panel d upside down? The y-axis says H-UH choice, and that should be most positive for the highest percentage of healthy choices, which should be for the light gray bar, not the black one, right?

Figure 4 – panels d and g need labels on the x-axis.

Appendix Figure 5 – to my eye this looks more like insula than IFG, but perhaps I'm mistaken.

Finally, I think it is important to include the Q-P plots in the supplements at least, just to make it clear that the model fits could be improved. I don't think this is critical to the paper, which doesn't really rely on the specific model, but the misfits are noticeable.
