# Peer review - Round 1

Editors:
- Joseph F Cheer, University of Maryland School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62390.sa1](https://doi.org/10.7554/eLife.62390.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this paper, fiber photometry and a perceptual choice task are utilized to provide a very interesting and important window onto the activity of dopamine axons in three different regions of the striatum. Unexpectedly, activity in all three regions was found to be quite similar, in contrast to accepted function of dopamine actions in different striatal. In addition, a model is provided that captures some features of the behavior and may explain this homogeneity.

Decision letter after peer review:

Thank you for submitting your article "Distinct temporal difference error signals in dopamine axons in three regions of the striatum in a decision-making task" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Melissa J Sharpe (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses and major text revisions are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this paper, the authors use fiber photometry coupled to a perceptual choice task to provide a functional window onto the activity of dopamine axons in three different regions of the striatum (VS: the ventral striatum; DMS: the dorso-medial striatum; and DLS: the dorso-lateral striatum). Unexpectedly, fluorescence signals in all regions are exhibit only relatively subtle differences of baseline (DLS has an elevated baseline) and movement sensitivity (largely in the DMS). The authors lay out a picture of the various signals, and also provide a model that captures some aspects of the behavior.

Essential revisions:

1) While the models used to explain the data are quite elegant, the overall results remain correlative. There are no experimental manipulations to test the primary conclusions. Most notably, the lack of "dopamine dip" in the DLS following a smaller than expected reward may support a role for this region in habitual behaviors. However, this remains speculative, as there is no operationally defined metric that animals are unambiguously showing habits.

2) The homogenous pattern of dopamine neuronal signaling across striatal regions during reward-directed behavior in the current study contrasts starkly with extensive heterogeneity observed in prior studies using Ca2+ imaging (Howe et al., 2016; Parker et al., 2016) or voltammetry (Brown et al., 2011; Willuhn et al., 2012 PNAS). For example, Oyama et al., 2010, record single-unit activity in DLS and find that these neurons do not show negative errors in response to unexpected omission of reward in a similar task used here. Please provide a potential and detailed explanation for why such dramatic differences are observed in the current work, that cannot be solely related to differences in the technique used.

3) The idea that the DLS might be engaged in something like the actor learning part of the actor-critic learning rule (rather than Q learning, say) has been relatively widely suggested – the authors might comment on the observation in REINFORCE rules (that the paper cites) that it is possible to add an "arbitrary" action-independent baseline to the equivalent of the prediction error and derive the same expected change in the weights (only the variance is affected). Does this not imply that the baseline shift in the DLS is unlikely to be associated with a different functional property?

4) It would be expected that the model would make a much larger distinction between the medium reward in the BIG than the SMALL condition than was apparent in the data. Indeed, one of the puzzles for me about the paper was the tiny effect of the BIG vs SMALL side (as in Figure 4C, for instance) – why might that be? Would the authors' previous results not predict a larger difference?

5) The FP data shows three peaks in DA in correct trials, whereas the model only really shows two. The second peak, associated with leaving the sampling well is important – particularly for the DMS – could the authors comment on its absence in the model?

6) Further analysis is required from the transition between block 1 and block 2 and the speed of adaptation could provide useful cues about the employment of goal-directed or habitual values, and distinguish DMS and DLS.

7) It is unclear why the data is combined across regions in showing responses to the odor or choice. Is the only time these signal diverge during reward delivery? I think it would significantly increase the novelty and impact of the findings if the authors could focus on representing the differences between these regions in their figures (e.g. Figure 2 and 3), and conduct the analyses in relation to the different regions (rather than clumping all regions in the modeling). What are the parameters that change when data is sorted out this way? The claim that these data all line up a TD error simply cannot be the case, because DLS does not show the hallmark dip in activity to an unexpected reward that would be expected of a TD error.

8) The claim is made that DLS activity is consistent with the "law of exercise" proposed by Thorndike, encoding how to perform motor sequences. However, these data are also consistent with this region encoding the reward outcome as a stimulus (i.e. the smallest reward is encoded as a small reward, instead of a reduction in value). Alternatively, it could be encoding the "long run history" of rewards (and impervious to single reductions in reward magnitude), which is consistent with current theories of habitual learning. Therefore, suggesting changes to existing theories on the basis of a single characteristic of neural activity in a limited data set, without a behavioral test that would facilitate such an understanding is not advisable. In fact, this can be removed with no detrimental effect to the paper.

9) The fact that these data can be modeled in a TD framework does not mean dopamine terminals are acting as a model-free TD error. This is because there is no test outside this hypothesis. There is nothing other than reward "value" that is manipulated. And dopamine neurons are capable of acting outside a model-free TD error. This has been demonstrated many times by many different labs in the past 3-5 years; all of this should be noted and discussed. Indeed, dopamine neurons in VTA respond to unexpected changes in reward identity (Takahashi et al., 2017), and stimulation of dopamine neurons drives learning between neutral cues without endowing them with "model-free" value (e.g. Sharpe et al., 2020, Nature Communications). This is not predicted by a model-free TD signal. Indeed, similar "model-based" findings have been found in ventral striatum (e.g. Corbit and Balleine, 2011, Journal of Neuroscience; Cerri et al., 2014, Behavioral Neuroscience).

10) Please rephrase your interpretation as follows: " our modeling approach is consistent with activity at DA terminals functioning within the lines of a TD error framework in this particular reward-learning task, while we acknowledge that it is likely these signals are also acting outside of this framework in other tasks".

11) It is crucial to report whether animals engage in licking in the water (or sample) port before the reward is provided? Does this covary with model 'value' and confidence? Does it covary with FP signals?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Distinct temporal difference error signals in dopamine axons in three regions of the striatum in a decision-making task" for further consideration by eLife. Your revised article has been evaluated by Kate Wassum (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below.

In subsection “Similarity of dopamine axon signals across the striatum” paragraph three, optimism in Q learning should not be described without qualification. The fact that Q learning uses max_b Q(s(t+1),b) at the next state (s(t+1)) is not thought of being borne of optimism – this in fact reflects what the subject thinks it could do at that state (although it would indeed be optimistic to think that it would always do that). Confusion may arise in that optimistic Q values are associated with the motivation to explore. If the authors wish to include the assertion about Q learning, they should expand on their exact point.

The" dip" in the signal is important for the TD error. And if the proxy for the DLS signals is "more excitation" represented in Figure 8, this should still predict a dip in the DLS (albeit a smaller one). However, signals in DLS still show an increase in activity from baseline during water omission. This should be clarified.

The authors propose that the observed signals look like the scalar difference between the expected an observed value (with the exception of the DLS), but are not necessarily used to attach this scalar value product to the antecedent cue or action. This should be specifically and explicitly stated in the text as it is not necessarily scalar value that attaches to antecedent events, which is alluded to by referencing and modeling using the model-free TD algorithm.

Please include summary statistics in additional to P values where appropriate (e.g., for ANOVA and t-tests).
