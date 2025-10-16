# Peer review - Round 1

Editors:
- Jonathan Roiser, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62051.sa1](https://doi.org/10.7554/eLife.62051.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is a very interesting study whose goal is to determine what drives subjective mood over time during a reward-based decision making task. The authors report data from a series of online behavioural studies and one performed during neuroimaging. Participants played a well-established gambling task during which they had to select between a sure outcome and a 50:50 gamble, reporting momentary mood assessments throughout the game. The authors compared the performance of a number of computational models of how the mood ratings were generated.

The authors identify as their "baseline" model that proposed by Rutledge and colleagues, in which an important determinant of mood seems to be the reward prediction error - this is called the Recency model. They contrast it with a Primacy model, in which earlier events (in this case, aggregated and weighted experienced outcomes) play a more important role. They validate the model across different behavioural conditions, involving healthy participants and depressed patients. The conclusion is that the data are more consistent with their Primacy model, in other words a stronger weight of earlier events on reported mood. In the fMRI experiment they found that the weights of the Primacy model correlated with prefrontal activation across participants, while this was not the case for the Recency model.

The paper is clearly written and easy to understand. The question of how humans combine experienced events into reported mood is topical and the conclusions are striking, given the dominance of recency-based models in the literature (e.g. Kahneman's peak-end heuristic). The paper takes an interesting approach and presents an impressive amount of data, and the reviewers and editor felt that it makes a substantial contribution to the literature.

Decision letter after peer review:

Thank you for submitting your article "The temporal representation of experience in subjective mood" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that substantial additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This is a very interesting study whose goal is to determine what drives subjective mood over time during a reward-based decision making task. The authors report data from a series of online studies and one performed with fMRI. Participants played a well-established gambling task during which they had to select between a sure outcome and a 50:50 gamble, reporting momentary mood assessments throughout the game. The authors compared the performance of a number of models of how the mood ratings were generated.

The authors identify as their "baseline" model that proposed by Rutledge and colleagues, in which an important determinant of mood seems to be the reward prediction error - the authors call this Recency model. They contrast it with a Primacy model, where earlier events (in this case, average experienced outcomes) play a more important role. They validate the model across different behavioural conditions, involving healthy subjects, teenagers and depressive patients. The conclusion is that the data are more consistent with their Primacy model, in other words a higher weight of earlier events on reported mood. In the fMRI experiment they found that the weights of the Primacy model correlated with prefrontal activation across subjects, while this was not the case for the Recency model.

The paper is clearly written and easy to understand. The question of how humans combine experienced events into reported mood is topical and the conclusions are striking, given the dominance of recency-based models in the literature (e.g. Kahneman's peak-end heuristic). The paper takes an interesting approach and presents an impressive amount of data.

However, at some points the arguments seemed a considerable stretch, in part because important experimental and methodological detail is missing, and in part because the analyses do not currently consider a number of potential confounds in both the models and the task design. It is not clear whether these concerns can be addressed or not, but we would like to give you the opportunity to do so. Ultimately, these concerns come down to whether we can be certain that the results reflect a true primacy effect, as opposed to some other process that simply appears at face value to be a primacy effect.

To this end, some important checks need to be made concerning both the computational and the fMRI analyses, as detailed below. These do require substantial extra modelling work, and it is quite possible that the conclusions will not survive these control analyses.

Essential revisions:

1. In relation to model comparison, the authors need to show us whether or not their model selection criteria allow them to correctly recover the true generative model in simulated datasets. Are we sure that the model selection criteria are unbiased toward the two models?

2. Related to point (1), can the authors provide a qualitative signature of mood data that falsifies the Recency model at the group level (see Palminteri, Wyart and Koechlin. 2017). They do so in Figure S2 for one participant, but it would be important to show the same (or similar) result at the group level (this should be easier in the structured or in the structured-adaptive conditions).

3. It is not clear where the weights on the primacy graph (Figure 1B) come from. The recency weights make sense - there is a discount factor in the model that is less than 1, so there is a an exponential discount of more distant past events. However, for the primacy model the expectation is apparently calculated as the arithmetic mean of previous outcomes (which suggests a flat weight across previous trials) and the discount factor remains. So how can this generate the decreasing pattern of weights? It would be really useful if the authors could spell this out as it is currently quite confusing.

4. The models differ in terms of whether they learn about the expected value of the gamble outcomes, or whether they assume a 50:50 gamble (the Recency model assumes this, the Primacy model generates an average of all experienced outcomes). This leaves open the possibility that the benefit of the Primacy model is simply that people do in fact largely use experienced outcomes to generate their expectations, rather than believing the outcome probabilities displayed in the experiment. Can the authors exclude this possibility?

5. Related to the above point, the structured and adaptive environments seem to have something to learn about (blocks with positive vs. negative RPEs), so it is perhaps not surprising that humans show evidence of learning here, and a model with some learning outperforms one with none.

The description of these environments is insufficient at present - can the authors explain how RPEs were manipulated? Was it by changing the probability of win/loss outcomes, and if so how? Or was it by changing the magnitudes of the options? For the adaptive design was the change deterministic? And was the outcome (and thus the RPE) therefore always positive if mood was low; or was this probabilistic, and if so with what probability? Finally, did the Recency model still estimate its expectations here as 50:50, even when this was not the case? If so, this requires justification.

6a. In addition to changing the expectation term of the Recency model, the Primacy model also drops the term for the certain outcomes (because this improves model performance). Can this account for the relative advantage of the Primacy over the Recency model? In other words, if the certain outcome term is dropped from the Recency model as well, does the Primacy model still win? If the authors want to establish conclusively that Primacy is a better model than Recency, then surely more models ought to be compared, at the very least using a 2x2 design with primacy/recency of expectations/outcomes.

6b. On a related point, the standard Recency model was originally designed such that the certain option C was NOT the average of the two gambles, so C was required in the model (at least in the 2014 PNAS paper). Here, C is the average of the gambles, so presumably it would be identical to E in the Recency model, and therefore be extraneous in the Recency model as well as the Primacy model. Did the authors perform model comparison to see if C could be eliminated from the Recency model? If so, this is not another difference between the models after all.

7. The structured and structured-adaptive tasks seem to have some potential problems when it comes to assessing their impact on mood ratings:

i. the valence of the blocks was not randomised, meaning that the results could be confounded. E.g. what if negative RPE effects are longer-lasting than positive RPE effects? This seems plausible given the downward trend in mood in the random environment despite average RPE of zero. Could this also explain the pattern of mood in the other two tasks, rather than primacy?

ii. scaling: if there is a marginally decreasing relationship between cumulative RPE and mood (such that greater and greater RPEs are required to lift/decrease mood by the same amount), then this will resemble a primacy effect? This is unlikely to be an issue in the random task but could be a problem in the structured and certainly in the structured-adaptive tasks.

iii. individual differences in responsiveness to RPE: in the structured-adaptive task, some subjects' mood ratings may be very sensitive to RPE, and others very insensitive. One might expect that given the control algorithm has a target mood, the former group would reach this target fairly soon and then have trials without any RPEs, while the latter group would not reach the target despite ever increasing RPEs. In both cases the Primacy model would presumably win, due to sensitivity to outcomes in the first half or insensitivity to bigger outcomes in the second half respectively? Can the authors exclude these possibilities?

8. In relation to the fMRI analyses, the results in the main text seem to result from a second-level ANCOVA, where the individual weights of the Primacy model are shown to correlate with activation in the prefrontal cortex. Similar analyses using the weights of Recency model do not produce significant results at the chosen threshold. This analysis is problematic for two reasons. First, absence of evidence does not imply evidence of absence - was a formal comparison of the regression coefficients conducted? Second, to really validate the model the authors should show that the trial-by-trial correlates of expectations and prediction errors are more consistent with the Primacy than the Recency model, using a parametric analysis at the participant level.

9. Similar to point 6, it is hard to conclude much about the models from the fact that the Primacy model E beta (but not the Recency model E beta) correlates with BOLD responses in a prefrontal cluster, when the Recency model E term is based on previous expectations, not previous outcomes. Likewise with the direct comparison of the models' voxel-wise correlation images.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "The temporal representation of experience in subjective mood" for consideration by eLife. Your article has been reviewed by the same 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted the below summary to help you prepare a revised submission. The reviewers felt that you had been very receptive to their comments, making extensive changes and performing the requested additional analyses. Consequently, the manuscript is nearly ready for publication, subject to a few final clarifications that are listed below.

Essential Revisions:

1. The new Figure S1 is helpful, but caused some confusion as the description in the legend could be clearer. The reviewers assume that the blue bars are the weights attached to all outcomes (not expectations) from trial 1-8, all contributing to the expectation on trial 8; the orange bars are the weights attached to all outcomes from trial 1-7, all contributing to the expectation on trial 7; and so on. Assuming this understanding is correct, please amend the text in the legend to clarify this better, and also provide a colour key for the figure to make it clear that the bars refer to outcomes from specific trials.

2. The Primacy vs Recency model comparison is of critical importance, so it would help the paper to be as clear as possible about it. The key comparison here is between the variant of the Recency model that is identical to the Primacy model in terms of having both a learned outcome as the expectation and without the certainty term. Your model comparison seems to test these changes separately rather than together (apologies if we have misunderstood this).

Can you explain what it is, specifically, about the Primacy model that causes it to perform better than the best Recency one (e.g. is it the nature of the way the expectation is learned, or something else)? As we understand it, the central claim of your paper is that people learn the expectation term in a way that effectively puts more weight on the initial outcomes encountered, so it would be really useful to understand what it is about the learning process that causes this effect, and whether it is this that improves the fit of the model.

3. Relating to the above point, the key comparisons between Primacy and Recency models in the main manuscript (e.g. the comparative fMRI analyses) should be between these similar models, not the Primacy and original Recency model.
