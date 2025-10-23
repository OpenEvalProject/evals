# Peer review - Round 1

Editors:
- Tobias H Donner, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53664.sa1](https://doi.org/10.7554/eLife.53664.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study uses a combination of neural circuit modeling with pharmacological intervention and behavioral psychophysics in monkeys to dissect the mechanisms of decision-making. It implicates the N-methyl-aspartate (NMDA) receptor in the accumulation of decision evidence, linking NMDA-mediated recurrent excitation of pyramidal neurons to a well-known behavioral phenomenon: a bias to choose options exhibiting larger variations in value. The approach opens up new perspectives for the mechanistic assessment of decision computations in the brain.

Decision letter after peer review:

Thank you for submitting your article "A circuit mechanism for decision making irrationalities and NMDA-R hypofunction: behaviour, modelling and pharmacology" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Tobias Donner as Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Konstantinos Tsetsos (Reviewer #1); Valentin Wyart (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

While editors and reviewers found your work interesting in principle, all reviewers raised some substantial concerns that would need to be addressed before we can reach a final decision on your paper. The essential revisions are listed below. Indeed, it seems possible that the results of these requested analyses will require a substantial toning-down of several of your claims pertaining to E/I balance, in a way that could undermine the specificity of conclusions and the suitability of your paper for eLife. Even so, we agreed to give you the chance to address the concerns, for which two months should be a realistic time frame.

Summary:

This manuscript reports a computational and pharmacological study in monkeys, into a question of interest to a broad research community: The role of the NMDA receptor in evidence accumulation and decision-making. The authors used a protocol developed and tested in humans by Tsetsos and colleagues, in which subjects compare the average length of two sequences of visual bar stimuli. The monkeys exhibit a so-called “pro-variance bias” (PVB) toward choosing the more variable stream, although the monkey behavior differs from humans in other aspects (see below). The authors show that a neural spiking circuit model of bounded evidence accumulation shows a similar PVB, and that a lowered E/I ratio simultaneously decreases accuracy and increases PVB. Finally, they report that intramuscular injection of ketamine transiently decreases accuracy and increases PVB, as predicted by a lowered E/I ratio. The authors interpret their findings in the context of the previous work on PVB as well as pseudo-psychotic effects of ketamine in human subjects.

Essential revisions:

1) Specificity of the pharmacological claim within the circuit model.

You should show that the ketamine behavioural effects are robustly obtained under the lowered E/I hypothesis (e.g. for various magnitudes of E/I reduction ) and, crucially, incompatible with a) sensory deficit, b) elevated E/I, c) concurrent changes in both NMDA receptors. Practically, this means the following.

a) For each hypothesis, model predictions should be shown by varying the relevant model parameter(s) gradually within a range.

b) The similarity between model predictions and behavioural data should always be quantified using a goodness of fit metric (currently this is done by eye balling). Please should focus on perturbations who provide a good quantitative fit to the data.

c) Perturbations appear to be implemented in the same fashion as in Lam et al., 2017. There, the authors also changed other parameters besides the relevant synaptic weights, in order to maintain stability in the model dynamics. It is not clear if and how these extra changes could be pharmacologically induced by ketamine. Please clarify this aspect and derive predictions when stability adjustments are not performed.

2) Effect of drug on lapses.

Please test for a ketamine effect (sedation) on lapse rates. The psychometric functions under ketamine indicate a large change in the lapse rate which is currently not taken into account. All descriptive analyses (logistic regressions) and model simulations should take into account lapse rates. Can an increase in lapse rates explain away the changes in the PVB effect, psychometric curves, and kernels?

3) Validity of circuit model.

Currently, the circuit model is presented as a black box. You devote a couple of sentences in describing how the expansive non-linearities in the F-I curve give rise to the pro-variance effect. This part is not very well developed. One way to test whether indeed the non-linearities are crucial in the pro-variance effect the monkeys show, is to separately analyse trials with "high" (total sum of both streams high) vs. "low" (total sum of both streams low) evidence and see if the PVB effect changes. Or add the total sum as a regressor and compare the regression weights in the model and in the data. In addition to non-linearities in FI curves, the attractor dynamics of the circuit model may (or may not) promote the PVB effect. Are these dynamics even necessary to produce the pro-variance effect in the model? And is there any link between signatures of attractor dynamics (e.g. kernel shapes) and the PVB effect in the data? If dynamics were redundant in the model, would this undermine the claim that the PVB can be diagnostic of E-I balance?

This relates to the question concerning the way the PVB is quantified: in the model, how can the PVB index change even if the F-I non-linearity remains unchanged? It thus seems that the PVB index is sensitive to the overall signal-to-noise associated with the model and it is not a pure marker of the pro-variance propensity.

Please clarify what the PVB index stands for.

4) Results for both task framings.

Please present separate results for the two framings, i.e. "select higher" and "select lower" trials, which is interesting from an empirical viewpoint. Also: Have you mis-labelled the "high-variance correct" and "low-variance correct" trials in the "select the lower" conditions? (If not, then the quantification of the PVB may be wrong.)

5) Generalizability of findings to humans.

Reviewers raised doubts about the suggested analogy of monkey and human performance, and the underlying computations: Showing that both humans and monkeys have a PVB is not sufficient to establish a cross-species link. In the human work by Tsetsos et al. (PNAS, 2012, 2016), the temporal weighting of evidence on choice exhibits recency, in sharp contrast to the primacy found here in monkeys. What does this imply in terms of the relationship at a mechanistic level? This point needs to be discussed.

6) Link to schizophrenia.

Reviewers remarked that the link to schizophrenia is very loose: no patients are tested and overall behavioral signatures are different even from healthy human subjects (see point 3). Reviewers agreed that this point should at least be toned down substantially or dropped altogether. This tentative link could be brought up as speculation in Discussion, but not used as the basis for setting up the study.

7) Discuss limitations of pharmacological protocol.

a) The physiological effects of ketamine on cortical circuits remain speculative. The drug is unlikely to have the single, simple effect, as assumed in the model. This should be acknowledged in Discussion. Also, what happens in the model when NMDA hypofunction is implement in both neuron types?

b) The use of an intramuscular injection of ketamine at 0.5 mg/kg (about an order of magnitude stronger than what would be used in humans) produces a massive transient effect on task behavior, which has potential important drawbacks. First, the effect is massive, with decision accuracy dropping from about 85% correct to less than 60% correct after 5 minutes, followed by a sustained recovery over the next 30 minutes. This effect of ketamine is so strong that it is hard to know whether it is truly NMDA receptor hypofunction that produces the behavioral deficit, or task disengagement due to the substantial decrease in reward delivery (for example). The time window chosen for the analysis is also strongly non-stationary, and it is difficult to assess how much an average taken over this window is truly an accurate depiction of a common behavioral deficit throughout this time period (where accuracy goes from 60% correct to 80% correct). Again, the presence of possible attentional lapses should be accounted for (and reported in the manuscript) in all model fits and analyses, given the strength of ketamine-induced deficits triggered by this pharmacological protocol. We realize that this aspect of the study cannot be changed at this point, but it should be acknowledged as an important limitation.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "A circuit mechanism for decision making biases and NMDA receptor hypofunction" for consideration by eLife. Your revised article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Konstantinos Tsetsos (Reviewer #1); Valentin Wyart (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of new analyses, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting analyses.

Our expectation is that the authors will eventually carry out the additional analyses and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The authors have provided an extensive response to the reviewers' comments based on several additional analyses of their data; they have successfully addressed a large subset of the comments. Specifically, they have performed several additional analyses to (i) test alternative hypotheses as well as the robustness of the favored hypothesis, (ii) examine lapses under ketamine, (iii) unpack the workings of the circuit model, and (iv) examine the frequent-winner effect in the data so they can assess the generalizability of this study to humans. We acknowledge that all these analyses have led to a significant improvement. Nevertheless, we remain uncertain about the validity of the overall conclusion, that ketamine induces NMDA-R hypo-function in excitatory neurons, and that this effect is behaviorally manifested as an increase in a pro-variance bias.

Revisions for this paper:

1) Motivate modeling approach.

Given that you opted not to fit the model (which would be done with the meanfield reduction), or tune its parameters so that it matches the above behavioral patterns, we believe you should unpack the reasoning underlying this particular modeling approach.

2) Plot model predictions along with data.

As we pointed in our first review there seem to be some discrepancies between the data and the model, which we remain concerned about:

i) Ketamine data asymptote at a lower than 100% level. The lapse rates are still not plugged in the circuit model so as to bring the model predictions closer to the data.

ii) The control kernel in Figure 7I and the monkey kernels in Figure 8C look different. In the model, there is a primacy pattern (except for the first item) but in the data we see a flat/ U-shaped pattern. Plotting those together could reveal the degree of discrepancy.

iii) In the control condition, the psychometric functions in Figure 7B and in Figure 8B look different (for example in terms of convergence of the light and dark coloured lines). The elevated E/I plot in Figure 7D appears to be closer to the saline psychometric curve.

Such discrepancies, if true, matter: if the "baseline" model does not capture behavior in the control condition well, we cannot be confident about the validity of the subsequent perturbations performed to emulate the ketamine effect. To allow for better assessing the match, we strongly encourage you to always plot model predictions with the data.

Ideally, you would also assess the goodness of fit using maximum likelihood. (A certain parametrization could exhibit similarity with the data in terms of the logistic regression weights (PVB) but at the same time it can miss largely on capturing the psychometric function.) We believe this would be straightforward, given the simulations you have already performed, but leave the decision to you, whether to not to do this.

We realize that this point was not explicitly raised in the previous round. Then, reviewers had asked for a quantification of the goodness of fit. The approach you chose (logistic regression) is specific to the PVB index (not applied to psychometric functions and kernels) and did not fully convince reviewers.

3) Assess effects of concurrent NMDA-blockade on E and I neurons.

You establish that E/I increase reduces the PVB index while E/I decrease has the opposite effect. However, you have not examined the effect of concurrent changes of NMDA-Rs of both, E and I cells, which we had suggested to do. Please comment on the fact that concurrent changes could mimic the effect of E-E reduction (Figure 7—figure supplement 2: moving up diagonally the purple point would result in equivalent behavior). Unless there is strong support in favor of the selective NMDA change over the concurrent change (assessed via maximum likelihood), the conclusions should be reframed.

4) Add a lapse rate downstream from circuit model.

You have now assessed lapse rates in your analysis, but reviewers remarked that you do not report the best-fitting lapse rates. This makes it impossible to judge just how much lapses contribute to the decrease in task performance in the initial period following ketamine injection (which is included in all analyses). We are concerned that this massive performance drop under ketamine is not only triggered by aPVB, but also (perhaps largely) by an increase in lapses and a decrease in evidence sensitivity.

We would expect a lapse mechanism to be in play in the circuit model when emulating the ketamine effect. You could use the fraction of lapses best fitted to psychometric curves (which clearly do not saturate at p(correct) = 1) for the circuit model simulations. It seems conceivable that allowing the circuit model to lapse will reduce the weight applied on the mean evidence.

5) Different quantification of pro-variance bias.

We do not understand the motivation for compressing sensitivity to mean and to variance into a single PVB index. Our reading is that the pro-variance effect, quantified as a higher probability of choosing a more variable stream (see Tsetsos et al., 2012), can just be directly mapped onto the variance regressor. Combining the weights into a PVB index and framing the general discussion around this index seems unnecessary. The main behavioral result of ketamine can be parsimoniously summarized as a reduced sensitivity to the mean evidence. Relatedly, please discuss if and how the ketamine-induced increase in the PVB effect, the way you quantified it, rides over a strong decrease of the sensitivity to mean evidence under ketamine.

It does seem to be the case that sensitivity to variance remains statistically indistinguishable between saline and ketamine (if anything it is slightly reduced). The E/I increase model consistently predicts that the variance regressor is reduced. This is not the case with the E/I decrease model, which occasionally predicts increases in the sensitivity to the variance (see yellow grids in Figure 7—figure supplement 2). This feature of the E/I decrease model should be discussed, as it seems to undermine the statement that the E/I perturbation produces robust predictions regardless of perturbation magnitude (i.e. depending on the strength of E/I reduction the model can produce a decrease or increase on variance sensitivity, and the relationship is non-monotonic). Overall, we believe that combining sensitivity to mean and variance obscures the interpretation of the data and model predictions.

Again, we realize that this point appears to be new. But reviewers feel they could not really have a strong case regarding this metric without seeing the more detailed model predictions (in a 2-d grid) that you have presented in your revision.
