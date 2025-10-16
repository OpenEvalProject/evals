# Peer review - Round 1

Editors:
- Naoshige Uchida, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70263.sa0](https://doi.org/10.7554/eLife.70263.sa0)

Pinto and colleagues used brief optogenetic silencing to study the contributions of different cortical areas in an evidence accumulation task in mice. The authors show that silencing of frontal regions affected evidence accumulation on a longer timescale than that of posterior regions, providing evidence indicating the relation between cortical functions and intrinsic timescales.


---

# Peer review - Round 1

Editors:
- Naoshige Uchida, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70263.sa1](https://doi.org/10.7554/eLife.70263.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Multiple timescales of sensory-evidence accumulation across the dorsal cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gidon Felsen (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Previous studies have indicated that neurons in different cortical areas have different intrinsic timescales. In this study, Pinto and colleagues aimed at establishing the functional significance of intrinsic timescales across cortical regions by performing optogenetic silencing of cortical areas in an evidence accumulation task in mice. The authors observed that optogenetic silencing reduced the weight of sensory evidence primarily during silencing, but also preceding time windows in some cases, suggesting that inactivation of frontal cortical regions had long-lasting effects than that of posterior cortical regions. This study provides important results addressing the relation between cortical functions and intrinsic timescales.

The reviewers agreed that this study addresses an important question, and the authors performed sophisticated experiments, and collected a large amount of data. The results are presented clearly and the manuscript is well-written. All the reviewers thought that the results are potentially of great interest to a wide audience. However, the reviewers found several substantive issues which reduced the confidence on the authors' conclusions. These issues need to be addressed before publication of this study at eLife.

In particular, the following points have been identified as essential issues:

1. The presented analysis does not consider a large variability that exists at the level of individual animals. There is also some variability across conditions (e.g. photoinhibition of different epochs). Furthermore, the statistical analyses presented in the manuscript often rely on a small number of samples, and the sample size is not equal across the conditions (n = 6, 4, 3 for y = 0, 50, 100, respectively). Because of these issues, we felt that the main conclusion needs to be supported by further analysis investigating these variabilities, and careful discussions of these potential caveats.

2. The authors claim that the optogenetic silencing primarily affected the evidence-accumulation computation, but not other decision-related processes. The reviewers found this claim to be not strongly supported by the data. From the presented data, whether silencing specifically affected the evidence-accumulation process, not just passing the evidence to an accumulation process, remains unclear. Furthermore, silencing affects running speed (thus, indicates effects other than accumulation process). Also, the reviewers thought that alternative possibilities have not been fully examined.

3. Optogenetic silencing sometimes increased the running speed. This can potentially reduce the time spent in each location, and may affect the acquisition sensory information. It is important that the reduced regression weight is not the side effect of reduce time spent in each location. Furthermore, some analysis based on time, not just locations, would be very helpful.

More detailed comments and suggestions on the above issues are included in the individual reviewers' comments.

Reviewer #2 (Recommendations for the authors):

1) Overall, the inactivation effect is highly variable across brain regions and conditions. For example, in Figure 1-Supp 2, silencing mV2 and RSC during the 3rd quarter of the cue region reduce weighting 100 cm back, but the effect is not replicated when silencing is extended in time (2nd half of the cue region). The effect is yet different when silencing the posterior cortical regions, which covers mV2 and RSC. There are many cases like this. What is this variability due to? Is this degree of variability expected from behavioral variability? It is difficult to evaluate how robust the behavioral deficits are without an estimate of the expected variability and false positive rate.

2) The conclusion that inactivation primarily affects evidence accumulation is based on weights from the logistic regression. A drop in weights of the sensory evidence presumably means the stimulus information is lost. However, there could be other reasons weights could drop. For example, if mice stop engage in the task after photostimulation, this could presumably lower the weights since mice no longer base their choice on the sensory stimulus. The analysis of weights after photostimulation provides a nice control (Figure 2-Supp2). However, several areas do show prospective deficits in weighting of future evidence, although this is not observed in all areas. Prospective deficits could be consistent with mice stop performing the task. This possibility should be ruled out.

3) Some additional analyses could further corroborate the interpretation that the deficit is specifically in evidence accumulation. For example, if the inactivation selectively abolishes the memory of prior evidence, stimuli presented thereafter should still be integrated and a model based the evidence after the photostimulus should predict choice. If so, this could strengthen the interpretation that the deficits are specific to the accumulated evidence. Otherwise, it could suggest inactivation is degrading performance for other reasons.

4) In general, I could not find information on how well the logistic regression predicts choice.

5) The main result of the paper (Figure 2) is based on effects averaged across different inactivation conditions (different epochs). However, I wonder if it makes sense to combine conditions like this. One, I wonder if this could hide areas that are involved during specific epochs of the task. The text states that "…aligned curves from different epochs were fairly consistent (Figure 2B)", but it is not clear how this is quantified and compared to what reference. Two, I wonder if this pooling would violate assumptions of statistical tests given data now comes from distinct sources, rather than being repeated observations.

6) The analysis of calcium dynamics are based on the autoregressive component of the GLM model. This is counterintuitive because that component is not related to the stimulus or the task. If the claim is that evidence accumulation is related to the timescale of neural dynamics, shouldn't the analysis focus on the coefficients for E_δ (cumulative #R – #L towers), i.e. the component of the dynamics that encodes the stimulus?

7) In a couple of places in the text, I feel the claims should be weakened as they go beyond the data. For example,

a. Intro: "… provide the first casual demonstration that this hierarchy [of timescale] is important for cognitive behavior." A similar statement is in the 2nd paragraph of discussion. I suggest changing the framing. The experiments do not manipulate the timescale of cortical regions. The relationship with the observed behavioral deficit is correlative.

b. Page 11, "This suggests that signals from the different dorsal cortical areas could be combined by downstream regions in a near-linear fashion. Candidate regions include … " The following paragraph is perhaps more suitable for discussion since the experiments do not probe subcortical regions. Also see comment 8 below. The effects of combined-area inactivation in fact appear to be qualitatively different from the average of single area silencing.

c. Page 13, "…the different intrinsic timescales across the cortex support evidence integration over time windows of different durations." For the same reason as in comment (a) above, I suggest rephrasing or removing this framing.

d. Abstract and intro, "inactivation of different areas primarily affected the evidence-accumulation per se, rather than other decision-related process". It seems the results do not examine other decision-related process besides the weighting of sensory evidence.

e. The text claims the spatial resolution of inactivation is 1.5-2mm. This is somewhat misleading. In Figure S2 of Pinto 2019, 60% of neurons are silenced at this light intensity at 2mm from light center. This broad inactivation is also consistent with the characterization from the Svoboda lab (Li et al., eLife 2019), which suggests that the spread of inactivation at 6 mW extends well beyond 2 mm in radius.

8) In Figure 2-Supp 3, the effects of posterior vs frontal cortex inactivation do not appear to be very different from each other. This is somewhat different from the averages of single area effects. In general, the statistical tests in the paper do not directly compare the effects of posterior cortex inactivation vs. frontal cortex inactivation. A more appropriate test for the key conclusion should be an interaction of y-position dependence with cortical regions.

9) The explanation of power analysis is not very clear (page 26-27). How are the control trials subsampled at different number of inactivation trials? What does it mean to bootstrap all the inactivation conditions together? At what effect size is n=250 sufficient to detect the effect?

10) The non-monotonic effect of cluster 3 (V1 and RSC) in Figure 2c is counterintuitive. The effect seems to be present in several individual conditions in Figure 1-Supp 2. However, other conditions don't show this (e.g. delay epoch inactivation). The text states that the effect is potentially compatible with findings that multiple timescales exist in a single region. Please explain this notion more clearly and how it could lead to no deficit for recent stimulus information but deficits for distant stimulus memory.

11) Mice speed up during photostimulation in nearly all conditions (Figure 2-Supp 1). Are mice responding to the light? Ideally, a negative control could be included to show there are no non-specific effects of photostimulation when analyzed in the logistic regression. This could be done by photostimulation in GFP mice or by inactivation a cortical region not involved in the behavior.

Reviewer #3 (Recommendations for the authors):

Related to the above comment on aggregating data across mice, the presentation of the data would be more transparent if mouse-by-mouse results were shown, where possible (like they are in Figure 1B,C; Figure 1-table S1 is also helpful). For example, symbols for individual mice could be shown in Figure 1E instead of (or in addition to) the mean across mice. Presumably change in performance was calculated within mice and then averaged, rather than averaging laser on and laser off performance across mice and then taking the difference between the two. But the description ("inactivation-induced change in overall % correct performance for each inactivation epoch, for data combined across mice", line 119) could apply to either analysis.
