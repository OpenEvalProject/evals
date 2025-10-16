# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- William S Ryu, University of Toronto Canada
- Adam J Calhoun, Princeton University United States

## Review text

DOI: [10.7554/eLife.50316.sa1](https://doi.org/10.7554/eLife.50316.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

One of the most important open problems in theoretical ecology and movement ecology in particular is whether or not observed Lévy walk movement patterns (and similar behavior) are caused by intrinsic pattern generators implemented as neuronal networks. The alternative possibility is that such movement patterns are an emergent side-effect of how animals interact with the environment. The former explanation suggests that Lévy walks etc. are adaptive, whereas the latter explanation suggests that the behavior is not evolved. This experimental paper gives what is close to a definitive answer to this longstanding question.

The experiment has been custom designed, the data carefully processed, and the analysis has been undertaken with the required high standards (for example, the authors have taken care to distinguish power laws from truncated power laws). There are several technical results that, together, paint a picture that is as surprising as it is significant. When the experimenters artificially impair brain processing of sensory information, the resulting movement paths resemble Lévy walks, supporting the idea that there is an evolved neurophysiological mechanism that generates paths resembling Lévy walks.

Decision letter after peer review:

Thank you for submitting your article "Optimal searching behaviour generated intrinsically by the central pattern generator for locomotion" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: William S Ryu (Reviewer #1); Adam J Calhoun (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

There are some concerns and needs for clarifications requiring revision. The full reviewer comments are provided and should be fully addressed, but as a guide to the revision, we emphasize a few points brought out in these reviews.

1) Both reviewer #1 (main concerns – request to check if the statistics change over time (e.g. dependent on satiety?)) and #2 (point 4 – is there any adaptation to the turn rate?) overlap and indicate the need for serious consideration by the authors of stationarity in the data.

2) The additional concerns of reviewer #2 can be characterized as two question each requiring a careful response:

a) Is a random walk model (RWM) appropriate for fly larva foraging?

For RWM, the assumption is that reorientation events are independent and that the "steps" do not have some non-trivial correlations (e.g. curvature with direction of turn, etc.). We ask the authors to show additional statistics about turns and steps in support of a RWM. In addition, inspection of the tracks in the figures makes it look like sometimes larvae are either on a curvy track or turning a lot. Our guess is that this is real, and we think some small figure emphasizing that would be not too difficult to produce. For instance, if the authors simply show that slightly different thresholds in the tracking still results in truncated power laws we would be fine with the analysis. Our main concern would simply be that all these power laws are simply a result of the particular tracking.

b) How sensitive are the results to the segmentation parameters?

The authors are looking at 1D of the 2D data set so they aren't identifying "turns" directly and so can't directly do a sensitivity test for "turn angle." Essentially, they are identifying step lengths which statistically reproduce the same exponent of the power law distribution. We ask for a better description of the segmentation pipeline for step lengths in the main text, to help clarify to readers that the analysis does not identify turns directly, since we feel this might be overlooked by some readers. Moreover, we require some comment on how sensitive these results are regarding any parameters used in this pipeline, including image processing, filtering, data exclusion (xmin), and fitting.

Reviewer #1:

This is nice work.

Stochasticity is a fundamental element of animal behavior and in the context of search is universal across a wide range of species. Recent measurements of animal movements has shown that these probabilistic movement patterns approach a Lévy distribution. Leveraging the neurogenetic power of the fly model, this work addresses important questions. How do animals generate these non-trivial distribution? How are these random number generators implemented biologically? Are they generated through sensory information, sensory processing, higher order computation (extrinsically) or through a mechanism at a lower level (intrinsically)?

I believe technically the experiments are sound and that the data analysis uses appropriate and modern statistical tests required for determining the distribution parameters. I especially appreciate the inclusion of the order of magnitude of the data range, and the transparency of the testing details shown in the supplementary files.

The authors are careful to show important controls and experimentally the tracking experiment looks also to be carefully controlled for environmental inhomogeneities. However there are two parameters that I would like the authors to comment on. In C. elegans it has been shown that searching behavior changes scale over time, slowly increasing with a tau measured in tens of minutes. Are the fly search patterns constant in time over the 1 hour experiment? Does this differ between the BL/SOG blocked conditions? Also, it is assumed in C. elegans that the change in time is due to a change in satiety levels. At the beginning of the experiment the worm is well fed and so when searching on an agar surface with no food, it looks local with a short time/length scale, but as it gets hungry it extends the searching scale. While the blocked BL/SOG condition was shown to be within a range of normal feeding (Figure 2), I wonder if there might be still be a systematic nutritional or a satiety difference that is occurring. These comments are directed at a better understanding of mechanism, and does not affect the author's primary argument for an intrinsic vs. extrinsic characterization. But I think might at the very least deserve some comment in a response or perhaps even a comment in the text.

One part of the MLE analysis I did not fully understand. The authors describe a procedure to reduce the data range (xmin, xmax) for the fitting. Why was this necessary? I would like to better understand the differences in fitting if this data pruning was not done. Perhaps one could gleam this information from the supplementary files, but looking it over it is not clear to me.

Reviewer #2:

In the foraging literature, Lévy walks (or truncated power laws) are of fundamental importance and are seen across the animal kingdom. Where do they come from? In this manuscript, Sims et al. propose that power law movement is generated intrinsically by the motion generating circuitry of Drosophila larvae. The fits certainly look like power laws and the authors provide evidence that larvae generate this even in the absence of a synaptic activity in the brain. Still, I have some concerns about the way the data is quantified and interpreted.

1) I would like to see some further quantification of how the analysis pipeline identifies turns. This is fundamental to the entirety of the manuscript but when I look at the examples of turns in Figure 4A I am not convinced that there are not large numbers of spurious turns. Are there thresholds that they can vary to ensure that this result isn't the effect of some spurious parameter?

2) I would also like some more insight into how path curvature relates to power law scaling of random walk step length. Many of these paths certainly look curved, and I know other worms such as C. elegans do have curved paths. Do Drosophila larvae? Is a curved path equivalent to a sequence of frequent turns?

3) Some quantification of turning angle seems like it would be useful as well. Can the authors clarify whether optimal search relies on uncorrelated turn angle? If you have a sequence of anticorrelated turns, you may get a power law alpha ~ 2.0 (for the sake of argument) but the animal would move outward in a ballistic fashion which is very different behaviorally. I am especially wondering about turns between short steps which are (I assume) very small and would look very different than the random walks you get in Viswanathan et al., 1999, or the authors' own Figure 1A, for instance.

4) Is there any adaptation to the turn rate, e.g. if you quantify exponent early vs. late is it the same? Many animals perform an area-restricted search when placed in a new environment, which might affect the overall measured exponent.

5) The authors perform a lot of manipulations to see if the animal will continue to produce Lévy flights and indeed they do (I am impressed they do anything with some of these manipulations). In fact, it seems impossible for them to do anything except Lévy flights. Have the authors considered a manipulation (puffing on odorants, for instance) that would induce a Brownian random walk and see if they revert to a Lévy flight or if they indeed continue on in a Lévy flight? Some of the manipulations, such as apoptosis experiment in the brain lobes in Figure 7D, suggest that the VNC (not CPGs per se) are what are driving the power law – but there could still be local sensory processing here. My concern here is that the authors may not be truly getting rid of the sensory processing that could drive the power law.

Reviewer #3:

This study is an excellent paper that should be published as soon as possible.

One of the most important open problems in theoretical ecology and movement ecology in particular is whether or not observed Lévy walk movement patterns (and similar behavior) are caused by intrinsic pattern generators implemented neurophysiologically. The other possibility is that such movement patterns are an emergent side-effect of how animals interact with the environment. The former explanation suggests that Lévy walks etc. are adaptive, whereas the latter explanation suggests that the behavior is not evolved. In this context, this paper gives what is close to a definitive answer to this longstanding question.

This is an experimental study that answers an important theoretical problem. The experiment has been custom designed, the data carefully processed and the analysis has been undertaken with the required high standards (for example, the authors have taken care to distinguish power laws from truncated power laws).

There are a number of technical results that, together, paint a picture that is as surprising as it is significant: when the experimenters artificially impair brain processing of sensory information, the resulting movement paths resemble Lévy walks, strongly supporting the idea that there is an evolved neurophysiological mechanism that generates paths resembling Lévy walks.
