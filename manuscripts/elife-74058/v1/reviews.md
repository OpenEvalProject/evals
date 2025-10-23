# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74058.sa0](https://doi.org/10.7554/eLife.74058.sa0)

This paper will be of interest to neuroscientists interested in predictive coding and planning. It presents a novel analysis of hippocampal place cells during exploration of an open arena. It performs a comprehensive comparison of real and synthetic data to determine which encoding model best explains population activity in the hippocampus.


---

# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74058.sa1](https://doi.org/10.7554/eLife.74058.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Sampling motion trajectories during hippocampal theta sequences" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The demonstration that place cell firing samples potential future trajectories from the current location has so far only been shown in narrow armed mazes. This study, based on hippocampal recording in rats exploring 2D environments, is thus an interesting new contribution. However, there are several aspects of the analyses that should be clarified. Most importantly, it was recently shown that future sweeps of place cells alternate left/right on a T-maze (Kay et al., 2020). Grid cells may do the same in open environments (Gardner R. J., Vollan A. Z., Moser M.-B., Moser E. I. (2019) Soc. Neurosci. Abstr. 604.13/AA9). This study would thus benefit from bringing its original framing more up to date and from analyzing whether consecutive sweeps are anticorrelated.

2) Then, it is possible that the sampling of future trajectories corresponds to the representation of multiple coexisting "maps" (e.g. Jackson and Redish Hippocampus 2007, Kelemen and Fenton PLoS Biol 2010), especially since the animals alternated between two different behavioural strategies, namely the search of the "away" location and going back to the "home" location. This "flickering" between maps could potentially explain the over-dispersion of the data, resulting in variance that could be interpreted as sampling of possible future trajectories. Additional analyses could clarify this potential bias.

3) The generative model seems to be a key aspect of the study. A lot of work has clearly been done to model as accurately as possible an animal's movement. However, it also raises the question of how critical this is for the whole analysis. Are the predictions somehow different with a simpler model, for example one that would be generated as a successor representation? It is possible that generating naturally looking trajectories this way is not possible, but it would be interesting to at least discuss why all components of the generative model are strictly necessary. In other words, to discuss why the same predictions cannot be done with a simpler model.

4) It is unclear how the diversity prediction of the DDC model was tested. Specifically, how the variance in panel 5b was computed?

5) Not all "signatures" were shown for all models. The study would benefit from a summary figure or table showing how each model's prediction compared to the data for each of the signatures.

Reviewer #1 (Recommendations for the authors):

I think this paper should be presented from the point of view that theta sweeps are already thought to represent specific potential trajectories extending from the current location, from extensive work on mazes. However, in open field data (where trajectories are not constrained to specific routes), although there are similar reports concerning replay in open fields and theta sweeps in entorhinal cortex, it is still possible that place cells actually represent the distribution of possible future trajectories, and you show that this is not the case, providing some of the first evidence that theta sweeps in open fields encode specific trajectories.

I did not find it helpful that the paper is framed as evaluating different possible neural representations of uncertainty, and I don't think the rejection of the product or DDC schemes for doing this necessarily tells us much about whether or not they are used in situations where the brain might in fact represent a probability distribution.

Reviewer #3 (Recommendations for the authors):

Please provide more details how the increased diversity prediction of the DDC was tested. How is the diversity decoded from the population? What do the cumulative probabilities on Figure 5 subplot b show exactly and why and how can they show the increased diversity? The authors may want to provide some intuition/more explanation about what the decoded SD reflects in Figure 5 b, d and why it reflects the diversity and not the uncertainty which would increase in the late cycles for the rest of the models too.

We assume all analyses ("signatures") were applied to all models but not all of the results are shown. We appreciate that the step-by-step approach eliminating one model at a time makes for a simpler story but a figure with all results would seem to be very informative: e.g. are the other signatures that contradict the product scheme?

Presentation: we did not understand the cumulative probability panels and how they are related to the text. E.g. lines 249-252 and Figure 5b, same for Figure 6. Maybe it would be more intuitive to show the pdf instead of the cdf? But even then, the x-axis and general interpretation remains unclear to us.

Line 333: How do the results suggest efficient planning in the hippocampus? It suggests probabilistic, i.e. close to statistically optimal computations, but the authors should provide more details why they think it is also efficient.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sampling motion trajectories during hippocampal theta sequences" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but reviewer #2 has one remaining issue that needs to be addressed, as outlined below.

Reviewer #1 (Recommendations for the authors):

The authors have answered my main concerns

Reviewer #2 (Recommendations for the authors):

In this revision, the authors have made a number of improvements to what was already a systematic, rigorous examination of an important issue. The control analysis ruling out excess variance is due to different place maps across navigation-to-goal and random foraging further enhances confidence in the results, and is additionally supported by a similar analysis in Brad Pfeiffer's paper that just came out (PMID: 35396328).

My one remaining hesitation with this paper is the one I brought up in my previous review but perhaps didn't explain clearly, so I will try again. My understanding of the core logic of the paper is that the authors first establish what the signatures are of the coding schemes they wish to distinguish, by implementing these schemes in a series of models that generate synthetic spiking data. Then, they test to what extent those signatures exist in real data, and draw inferences from comparison with the simulated results.

I think this is a powerful approach and am completely on board with it. However, it does raise an overall question of how robust the simulation results are: what components of the simulation are necessary and sufficient for the results? How sensitive are the results to specific parameter choices? I appreciate and agree with the authors' argument that the Kalman filter is an appropriate and relatively minimal way to model the animal's uncertainty about its own location. But it is not obvious to me what modeling the animal's uncertainty about its position contributes to the results in the first place. Would you get the same simulated signatures if all you had was a probability distribution of expected future trajectories given true current location, and then applied the various coding schemes (encoding MAP trajectory, sampling, etc)?

Hence, my suggestion of using the SR to obtain such trajectory distributions from the animal's behavioral data, but really any approach that estimates these distributions from the data would help address my concern. This feels important, because comparison between these different generative models would give a sense of what data sets/behavioral tasks/task conditions should show the predicted signatures. Ultimately we don't want to just understand what happens in the Pfeiffer and Foster 2013 data set the authors analyze, but have some idea of what to expect say, in the dark with high uncertainty about current location, or on armed mazes where possible futures are highly constrained.

I realize that the paper is already extensive and thorough, but unless I'm off base with this intuition or misunderstand the authors' argument, it could actually simplify their paper if the same results obtain with a simpler way of generating probability distributions over trajectories. If they don't obtain, then this is important to point out, because of the resulting prediction that theta sequences ought to have different spiking statistics in high vs low uncertainty-about-current-position conditions.

Reviewer #3 (Recommendations for the authors):

The authors have addressed all my concerns. They have added an interesting new analysis as the result of the reviewer suggestions. Congratulations to the authors for an impressive piece of work.

In the final version, I'd like to encourage the authors to better explain the cause of the bias towards similar directions described in line 404. I didn't understand it. Please elaborate.
