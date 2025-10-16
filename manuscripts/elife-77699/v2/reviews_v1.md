# Peer review - Round 1

Editors:
- Christian Rutz, https://ror.org/02wn5qz54 University of St Andrews United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77699.sa0](https://doi.org/10.7554/eLife.77699.sa0)

This article will be of interest to researchers working on predator-prey interactions in the fields of biomechanics and neurosensory biology. It presents a valuable mathematical model that outputs possible escape trajectories given parameters relevant to the predator-prey system of interest. The premise of the modeling is attractive, as it includes the time required for prey to turn.


---

# Peer review - Round 1

Editors:
- Christian Rutz, https://ror.org/02wn5qz54 University of St Andrews United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77699.sa1](https://doi.org/10.7554/eLife.77699.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Geometric model incorporating prey's turn and predator attack endpoint explains multiple preferred escape trajectories" for consideration by eLife.

Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Andrew D Bolton (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Senior Editor has drafted this decision letter to help you prepare a revised submission.

Essential revisions:

Both reviewers were supportive of publication as long as a carefully revised submission clearly explains the rationale for how the speed of the predator was estimated and addresses the use of experimental parameters to model the escape response in other species. The measured values of predator speed should be reported. The additional points raised in the reviewers' full reports, which are appended below, also need to be addressed. Finally, please note that eLife has recently adopted the STRANGE framework, to help improve reporting standards and reproducibility in animal behaviour research – these recommendations are relevant to the empirical component of your study. In your revised submission, please consider the scope for sampling biases and potential limitations to the generalisability of your findings:

https://reviewer.elifesciences.org/author-guide/journal-policies

https://doi.org/10.1038/d41586-020-01751-5

Reviewer #1 (Recommendations for the authors):

Outside of my general public comments, a few thoughts. If you remove the predator adjustment model from Figure 1, Table 1 can be incorporated with the bottom left panel drawing. The bottom left of Figure 1 isn't as clear as it could be – the radius of the predator's mouth is certainly very subtle. Getting rid of the top right and bottom right panels (put them with the model's description in the Appendix) will free up explanatory space for the variables in the bottom left panel. The drawing could also use color to make each variable clear.

Figure 3 would benefit from 95% confidence intervals on the regression fit using bootstrap. Figure 4 needs a bit of work: 5 circles with a 3 ms aren't the right interval choice if the Tdiffs all max out at 10 -- it leaves the outer two circles with basically no information, and the max value is not on a div line. Figure 4A requires explanatory labeling for the concentric circles and axes; in fact, all circular plots in Figures 2 and 4 should have labels.

Reviewer #2 (Recommendations for the authors):

The predator's speed used to predict the optimal ET should be calculated from the empirical data for each interaction. Selecting a single predator speed for all interactions does not reflect the fact that the prey fish were responding to a stimulus that was approaching them at a particular speed.

Figure 1 is difficult to comprehend in its current format. The features of Figure 1C are the most important for understanding the model, but the formatting could be improved. For example, different colors could be used to define the different parameters and their labels. There also appears to be a mix of bitmap and vector elements here, the bitmap elements are low quality and upon magnification this becomes apparent. The caption refers readers to a table and an appendix in order to understand the different elements, which places a large burden on the reader. The figure and its caption should include all the information necessary for understanding.

It is unclear why the number of recordings of an individual prey fish was not standardized. This should be addressed along with more details of the experimental protocol that addresses the time between trials of an individual prey fish.

What was the procedure for selecting the particular kernel bandwidth value used to produce the results in Figure 2?

The data in Figure 2A are escape trajectories, what is the range of values that this variable can take? Is it 0-360, or -180 to 180? As described in the Methods section, it is unclear.

On away/toward responses: If Β = 180, then what is considered an away (toward) response? That is, what would the value of α be if the turn is CCW versus CW?

Figure 4: Since time difference is not a circular variable, rose plots are not appropriate for displaying these results.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your revised article entitled "Multiple preferred escape trajectories are explained by a geometric model incorporating prey's turn and predator attack endpoint" for further consideration by eLife. Your article has been evaluated by two reviewers and a Senior Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed:

Reviewer #1 (Recommendations for the authors):

The authors have addressed nearly all of my comments. Figure 2 is much improved and no longer requires Table 1 to be in close proximity in order to understand the variables in the model. All requested fixes to plots have been accomplished and I remain in strong support of publication in eLife. However, I do believe that the authors misconstrued my argument about the stochastic nature of behavior in their paper, and how it fits into the bigger picture of stochastic behavior in animals generally. This may be due to my use of technical words during my review. To be clear, stochastic does not mean "completely random". A priori, this is a poor strategy to use when the location of a predator is accurately detected because it would inevitably result in unnecessary death a large percentage of the time. I also did not mean that the behavior should be noisy around the optimal choice; both of these strategies are presented in the new Figure 1. When I used the word "Bernoulli draw" in my review, what I meant is this. Drawing from a Bernoulli distribution is a stochastic binary choice. The prey fish is doing this during the behavior. They are drawing a "toward" versus "away" choice that the authors convincingly argue is parameterized by the probability mass dictated by their model-generated TDiff. In other words, if the "advantage" shown from the optimal to suboptimal peak is high, the probability of drawing an "away" swim becomes higher, while if the advantage is low, the choice of swimming toward or away becomes closer to equally likely. This is stochastic behavior, and it is probability matched to the topology of TDiff, which is an amazing finding, and likely leads to balanced unpredictability when playing the zero-sum game of escaping a predator who can predict trajectories if they are too stereotyped. If one were to directly translate the TDiff space into a continuous multimodal distribution, the fish could be thought of as drawing from this distribution stochastically and making the optimal choice when accounting for predator learning. This is what I meant in my review, and therefore the changes to Figure 1 don't really fit what I was trying to convey. My guess is that the Mauthner neurons of the fish are biased according to the Bernoulli probabilities dictated by the authors' model. It is fine with me if the authors want to leave Figure 1 as is to generally convey that the fish can use random strategies to circumvent predictability, and it is also fine if they choose to publish as is without my suggested reasoning. I just think that the idea of a Matching Law in ethological fish behavior is really interesting considering that most Matching Law results are in the context of unnatural reinforcement learning paradigms.

Reviewer #2 (Recommendations for the authors):

The authors addressed all concerns and suggestions in the revised manuscript. In particular, the new figure 1 and revised figure 2 convey the escape behavior and the geometric model much more clearly. The additional text describing predator speed optimization and the subsequent discussion add valuable context. Finally, the authors' revised text regarding their model's potential application to other species is more clear and better justified.

But I find that the authors are misinterpreting the findings of reference 42, Nair et al. In that paper, the stochastic strategy observed in zebrafish for initial orientations <30 (deg) and >150 (deg) was attributed to the distance advantage between an away and toward response. That is, when the advantage was small, either direction was equally likely. This is analogous to the authors' finding regarding the TDiff advantage. I think the authors should highlight the similarities in these findings and discuss how they relate to sensing the approaching predator.
