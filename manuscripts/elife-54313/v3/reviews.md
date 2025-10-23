# Peer review - Round 1

Editors:
- Geoffrey Schoenbaum, National Institute on Drug Abuse, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54313.sa1](https://doi.org/10.7554/eLife.54313.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this study, Rich and colleagues recorded neural activity from the orbitofrontal and anterior cingulate cortex of monkeys during a delayed response task in which cues were presented that signaled different value primary or secondary reward. Their goal was to explore the representation of reward value during working memory performance to contrast predictions of proposals regarding whether information is maintained in a stable or dynamic manner. Using a novel approach of constructing ensembles only of neurons tailored to one or the other criteria, they argue persuasively that value information is available to downstream areas from the output of both regions at both timescales. The results are convincing and represent an important new perspective on this important question specifically and more generally on how to think about what information is represented in neural activity.

Decision letter after peer review:

Thank you for submitting your article "Stable and dynamic representations of value in the prefrontal cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Geoffrey Schoenbaum as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Laurence Tudor Hunt (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, Rich and colleagues recorded neural activity from the OFC and ACC of monkeys during a delayed response task in which cues were presented that signaled different value primary or secondary reward. Their goal was to explore the representation of reward value during working memory performance to contrast predictions of proposals regarding whether information is maintained in a stable or dynamic manner. Using a novel approach of constructing ensembles only of neurons tailored to one or the other criteria, they argue persuasively that value information is available to downstream areas from the output of both regions at both timescales. The results are convincing and represent an important new perspective on this important question specifically and more generally on how to think about what information is represented in neural activity.

Essential revisions:

The reviewers were each positive about the research and the paper, in the reviews and in the discussion. In discussion, there were four essential revisions noted below that are most important.

– The first is to clarify why decoding in Figure 5 is high prior to cue onset in some panels. This was commented on by two of the reviewers and must be addressed.

– The second is the issue of how neurons were selected and the issues of cross-validation and circularity raised by these same reviewers.

– Related to this is a third issue, which is whether or not neurons were included as value encoding and in the subsequent ensemble analyses if they had categorical or non-linear value correlates. The authors mention this was true, and on discussion it was felt that it was important to clarify this and ideally to show that the results either do or do not require their inclusion with more traditional linear correlates.

– And finally, fourth, all reviewers agreed that a parallel analysis considering type would be of interest. It is not critical what it shows, but it was felt this analysis could be done and might affect how some interpret these results.

Further details on these points can be found in the full reviews.

Reviewer #1:

This study tests how single and multi-unit recordings from ACC and OFC of non-human primates encode value information across delays. The authors find that both value and reward type information can be decoded from activity in both areas. In addition, subspace analyses for value information show that encoding is both stable and dynamic across time.

The nature of encoding across delays is a timely topic. Here the authors consider both the stability and the dynamics of this encoding over time. This is innovative and I think the results tell us a lot about the nature of neural coding in OFC/ACC. I have a few concerns that should be addressed.

1) I think it is a missed opportunity that the more interesting analyses are only applied to value but not reward type. Encoding of reward type has received considerable attention recently (e.g., Stalnaker et al., 2014; Howard et al., 2015), and here, decoding accuracy for value and type was nominally comparable, so it is unclear why this wasn't done here. I'd strongly encourage the authors to apply the analyses focusing on stability and dynamics of encoding to reward type as well.

2) I do not understand how it is possible that, as shown in Figure 5B (lower panel), the decoder trained on data from 500 ms before cue onset (that is before neurons encode any value) can decode value throughout the rest of the trial.

3) Related to the point above, it appears there are at least two potential sources of non-independence errors in the decoding analyses.

3.1) First, it appears the L2 parameter was selected based on all data and that "the parameter eliciting the best decoding for each condition was used for all decoding results presented here". As described this analysis is circular and will inflate decoding accuracies. Instead the authors should use nested cross-validation, where the parameter is optimized (using cross-validation) within the training data. (That is, the data is split into 3 parts. Different classifiers with different levels of L2 are trained on part 1. These classifiers are then evaluated on part 2 and accuracies are computed. The value of L2 that results in the best accuracy (determined in part 2) is then used to train a classifier based on part 1 and 2, and the final accuracy is computed based on part 3. No parameter decisions are ever based on accuracy that is determined using part 3)

3.2) The second instance of non-independence may occur during the ensembles selection approach. This is not fully explained, but it appears that the ensemble selection was not based on nested cross-validation either. Again, a nested cross validation should be used such that the ensembles are selected within the training data using cross-validation, and the final accuracy matrices should be computed based on data that was never used in the selection procedure.

Reviewer #2:

This study provides further insight into the recent debate around 'stable' versus 'dynamic' representations of value in prefrontal cortex. In short, the authors find evidence supporting both types of value representation. The authors use a range of methods to look at this, but perhaps the most convincing analyses are shown in Figure 5, where different subsamples of the same neural data (different 'ensembles') can be used to create cross-temporal decoding patterns that either appear 'stable' or 'dynamic', with the original data containing a mixture of the two.

Overall I found the paper to provide good support for a hybrid of stable and dynamic coding schemes, and the data to be well analysed. However, there were several points in the paper that I thought could do with a bit more attention.

1) Figure 2A vs. 2C Why are the % of encoding neurons broadly similar between ACC and OFC, but the decoding accuracy different between the two regions shortly after cue onset? This is a bit of an outstanding question that the authors don't really address.

2) In Figure 3, the authors do the right thing of splitting their data into training/test data when sorting by peak latency. (Otherwise, the tiling can easily arise from random noise, e.g. https://twitter.com/steinmetzneuro/status/1150971584812920832). It is, however, equally important that they do this in Figure 4.

3) "We considered value as a categorical variable, as some units activated in a non-linear fashion, for example by responding only to a specific value and could not be modeled with a simple linear regression" – isn't it possible that these neurons are encoding picture identity rather than value? In order to show that there is non-linear coding of value, then presumably the prediction would be that this non-linear value coding would generalise across the primary and secondary reinforcers? This could be easily shown for Supplementary Figure 2 – the lines could be split into primary and secondary reinforcer, with the 'non-linear value' prediction meaning that these two lines should overlap.

4) Figure 5 – it looks like the ACC cross-temporal decoding in the stable subspace goes back in time to before the stimulus onset (i.e. the classifier trained from timepoints -500ms to 0ms pre-cue has above-chance decoding accuracy). Is there a reason for this?

5) I couldn't understand how the 'trajectory speed' in Figure 6A is calculated – is the 'distance' in neural space being computed on raw firing rates, or on classification accuracies? Some further detail on this would be helpful.

6) It would also be interesting to know whether the regression shown in Figure 6B is less successful in the stable ensemble than in the dynamic ensemble?

7) "While value representations have been found in the activity of ACC and OFC e.g. [Rushworth and Behrens, 2008], this is, to our knowledge, the first study of their dynamics during a short delay." – It might be relevant to cite Cavanagh et al., 2016 here? That study used cross-temporal correlation to study how value coding persisted during the delay between the choice and outcome periods, albeit in the context of different subpopulations with different resting autocorrelations (see their Figure 5).

Reviewer #3:

In this study, Rich and colleagues recorded neural activity from the OFC and ACC of monkeys during a delayed response task in which cues were presented that signaled different value primary or secondary reward. Their goal was to explore the representation of reward value during working memory performance – across a delay period in the current task – to contrast predictions of proposals regarding how information regarding expected value would be maintained – whether it would be stable or dynamic. Using a novel approach of hand-picking neurons to compose ensembles tailored to one or the other criteria, they argue persuasively that value information is available to downstream areas at both timescales in both of these two prefrontal areas. The results are convincing I think and represent an important new perspective on this important question specifically and more generally on how to think about what information is represented in neural activity. So I am very positive generally about this paper. That said, I do have some things I would really like to see done.

1) I did not see any behavior. I think it is important to show the behavior in this paper in order to demonstrate that the monkeys do treat the cues as if they have these scalar values and further to show that they treat the cues predicting putatively similar amounts of primary and secondary reward similarly. The latter may be particularly important wrt to my second point below. This should be shown using choice behavior on the probe trials, but I also think it should be evident in reaction time or some other measure during the forced choice trials that comprise the neural data set.

2) I found the classification that something is encoding value to be confusing. The authors say that value was treated as a categorical variable since some neurons had idiosyncratic responses to cues not at the ends of the value ranges. Yet it seems to me that this begs the question of whether these neurons are signaling value. At a minimum, to count as a value neuron, a cell should show the same response across both trial types that have the same putative value. So a value neuron must either have a linear value correlate or it would need to fall into this special category… and even then, I think calling such a cell a "value cell" stretches the conventional definition of value. For instance, if a neuron fired the most to 2 and then significantly less to 1, 3, and 4, I would have trouble seeing this as a value cell by most definitions of value, even if it fired the same to 2 on both trial types. Given this, in my opinion, analyses such as those in Figures 2 and 5 that are the heart of the paper need to be redone without such "non-linear" value neurons as part of the populations. If the results only hold with those neurons included, then I think the interpretation of what is being represented statically and dynamically might be significantly affected for me.

3) Looking at Figure 2C and D, I do not understand the statement at the end of the subsection “Encoding and decoding of value in unit activity”, that because reward type is poorly encoded, the paper focuses on value. I think it is ok to focus on value because that is the question of interest. But this statement misrepresents the reason it seems to me. And really I'd like to see both explored either separately or as part of the same analysis. Both information is relevant to the broader question I think; primary versus secondary is as interesting a part of what is being maintained as simple value. In fact I'd say it is arguably more important, since it is important to me to be paid in dollars and not equivalent piles of marshmallows for example!?!
