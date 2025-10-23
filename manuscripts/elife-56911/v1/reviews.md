# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56911.sa1](https://doi.org/10.7554/eLife.56911.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The findings presented in this paper describe the relationship between cognitive flexibility and replay in humans. A major strength of this study is that it shows a direct relationship between replay and individual differences in behavior. This is a major step toward a better understanding of how replay contributes to reinforcement learning and planning.

Decision letter after peer review:

Thank you for submitting your article "The roles of online and offline replay in planning" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Samuel J Gershman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments or analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper presents evidence for the relationship between cognitive flexibility and replay decoded from MEG signals. The work significantly extends prior results, by connecting replay with individual differences in behavior. All reviewers agreed that this work is technically solid and the experimental results compelling, distinguishing between forward and backward replay as well as online vs. offline replay. Reviewers also found the paper clearly written but somewhat dense. Reviewers also noted some issues that should be addressed with additional analyses and/or data before the manuscript can be accepted for publication.

Essential revisions:

1) Evidence for replay is based on decoding of the previous state at the time of outcome. How much of this decoding can be explained by sensory input or sensory processing of the previous image, rather than replay as a separate neural event? Figure 2A shows that decoding might still be above chance after image offset. And Figure 2—figure supplement 2B suggests that decoding of the previous state is already above chance at and likely before outcome onset. Can the authors show that decoding is indeed driven by a replay-like mechanisms rather than sensory/perceptual processing of the previous state? For instance, how does decoding evolve in the second(s) before outcome onset? If decoding is driven by replay at outcome onset, should we not expect decoding to peak after outcome onset? Also decoding at outcome onset should not depend on the length of the ISI between the offset of the previous image and outcome onset. (Alternatively, if decoding is driven by sensory processing, decodability should be higher for shorter compared to longer ISIs.) Finally, the authors could use data from a more passive viewing task to get an idea of how long decoding should be expected to remain above chance after image offset in the absence of replay. To support the main conclusions about replay, it would be important to show that decoding is not simply driven by residual processing of the previous image.

2) Where in the brain does replay occur? It would be interesting to see which of the 273 MEG channels contribute to successful decoding. If the authors could show that putative replays is localized near hippocampal sensors rather than, e.g., visual ones, this may also help to convince that decoding of the previous state is not simply based on visual processing (see essential revision point 1).

3) Some reviewers found the manuscript very hard to read. Results are consistently stated in terms of technical constructs and/or methods that require substantial acquaintance with the authors' previous work. For example, the Introduction cites a copious literature on rodent replay and preplay in hippocampus without justifying the premise that this can be successfully decoded from MEG in humans. Another example: subsection “Bayesian hierarchical Gaussian Process time series analysis”, second paragraph. This was considered far too dense, particularly since several critical modeling choices were not well justified. The concern is that this style forces non-specialist readers (and even some specialists) to do a lot of work that might be avoided with more motivation and explication. A better description of some of the key analysis methods (the sequenceness analysis) in the main text would be helpful. In this regard, it might also help to have some kind of conceptual figure relating individual flexibility, model-free vs. model-based learners, preplay/replay, on-task/off-task, and other relevant constructs so readers can see their relationships. The authors present a number of different results in different epochs pertaining to different claims, but it is hard to see the coherent whole, particularly for those not already heavily invested in these debates.

4) The authors invoke the recent Mattar and Daw theory of hippocampal replay, arguing that it predicts that "subjects should be more disposed to replay trajectories that they might not want to choose again, rather than trajectories whose choice reflects a firm policy". We gather that this is related to Figure 5 in Mattar and Daw. But aren't the theory's predictions more complicated? Mattar and Daw also point out that enhanced replay should occur when an agent is likely to repeat an action, for example when receiving a larger than expected reward. Another issue is that Mattar and Daw's theory specifically predicts an effect on reverse replay ("backward sequenceness" here) not forward replay ("forward sequenceness"), but the authors report an effect for forward sequenceness.

5) "off-task sequenceness negatively correlated with IF (Figure 3). This association of sequenceness during rest with low flexibility is consistent with a proposed role of offline replay in establishing model-free policies." The logic of these predictions is understandable based on algorithms like Dyna, but couldn't this also go in the opposite direction? For example, if one thinks about the Gershman, Markman and Otto, 2014 studies, their revaluation index is conceptually similar to the IF measure used here. But in that case large revaluation (i.e., greater flexibility) was used to argue in favor of more replay in a Dyna-like manner, and this hypothesis received more direct confirmation from the Momennejad eLife paper. How can we reconcile these two interpretations of flexibility (as reflecting more vs. less replay)?
