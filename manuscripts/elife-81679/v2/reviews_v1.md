# Peer review - Round 1

Editors:
- Michael J Frank, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81679.sa0](https://doi.org/10.7554/eLife.81679.sa0)

This paper posits that higher uncertainty environments should lead to more reliance on episodic memory, finding compelling evidence for this idea across several analysis approaches and across two independent samples. This is an important paper that will be of interest to a broad group of learning, memory, and decision-making researchers.


---

# Peer review - Round 1

Editors:
- Michael J Frank, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81679.sa1](https://doi.org/10.7554/eLife.81679.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Uncertainty alters the balance between incremental learning and episodic memory" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

All of the reviewers felt that this was a promising paper with compelling results, but they also raised a number of questions about the methodology and interpretation of the results that should be addressed in a revision, as detailed below.

Reviewer #1 (Recommendations for the authors):

The wide vs. skinny error bars are very difficult to visually differentiate. I recommend a more obvious difference.

Reviewer #2 (Recommendations for the authors):

1. 40-45% of the participants are excluded from the analysis in the main and replication samples. The authors should clarify how many were excluded for each criterion. Was the main culprit whether people responded to the volatility manipulation in the original deck learning task? If so, what does this mean about the generality of the effects of uncertainty in incremental learning? I suspect this may be due to the relative attentiveness of online participants, but the authors should address the caveat in the text. Some aspects of these excluded data may still be relevant. For example, if these participants do not register any differences in uncertainty between the two environments, wouldn't the prediction be that their use of episodic memory also does not differ?

2. Some aspects of the methods were not clear.

a. Was the order of the high and low volatility blocks counterbalanced across participants? Was the order the same in the first deck learning and second deck learning + card memory tasks? Were participants told explicitly that the environments would carry over between the two tasks? (The last point would further support using estimates fit to the first task out of the sample in the second.)

b. How individual objects were re-sampled was described in the overview (lines 435-439), but I imagine the details will matter a lot to people interested in replicating and extending this work. It would help to point the interested reader to where these could be found (eg, is the code provided, or is it based on a previous study described in detail, etc.).

3. Given that the results precede the methods, there are some aspects of the task that would be helpful to explain at the outset (around Figure 1). I was initially confused because the outcome in Figure 1 is $1 but the value memory was on a scale of 0-100, but this could be cleared up with a sentence about the possible outcomes. It would also be helpful to mention the mean outcome on the lucky versus unlucky deck, how frequently the lucky deck changes, and what participants are told explicitly about the volatility manipulation. This could be done in the text or with a revision to Figure 1. I was also confused about how the two samples were used until the end of the Results section (are they being analyzed together or separately? What am I looking at in Figures 2-5?). Again, a well-placed sentence at the top of the Results section would clear this up.

4. In Figure 3, I think a slightly different comparison would be useful, in addition to or instead of the two Rescorla-Wagner models. One difference between the reduced Bayesian and RW models is that the learning rate is dynamic in the RB model but not the RW model. But another difference between the way the two models are implemented is that the RB model assumes the value of the two decks are perfectly anti-correlated (ie, it is learning only one value estimate), while the RW model does not (ie, it is learning about the two decks independently). Thus, the RB model assumes a critical aspect of the structure of the task that the RW model does not. I doubt this difference completely accounts for its better performance, but this should be tested. A δ-rule model with a fixed learning rate that learns a single value estimate (like the RB model) would be the needed comparison. This comparison would also isolate the effect of including the dynamic learning rate (according to RU and CPP) in the model.

5. The discussion goes into the different effects of novelty, surprise, and uncertainty on subsequent memory (lines 349-364), in the context of the lack of effect of uncertainty (RU from the reduced Bayesian model) at encoding. But have the authors looked at the effect of surprise (changepoint probability in the reduced Bayesian model) at encoding? The previous studies discussed here would predict that surprise at encoding should enhance subsequent memory (and perhaps the use of episodic memory in choice). This point is not central to the manuscript, of course, but the authors have additional data relevant to the distinctions they are raising here.

Reviewer #3 (Recommendations for the authors):

As mentioned in the public review, I thought this was a very interesting study and the results were clearly communicated. However, I have a number of questions/recommendations for the authors to strengthen the results and interpretation.

Regarding the points made in the public review about uncertainty v volatility and context, I'd make the following recommendations:

(1) Uncertainty vs. volatility (described in public review): it would make sense to reframe results around volatility rather than uncertainty, or strengthen the trial-wise RU analyses to look at trial-wise RU only at trials far away from reversals. At least there should be some discussion of where uncertainty arises besides volatility.

(2) Context: I think the analyses would be strengthened with an additional model using context inference rather than incremental learning. A natural choice might be Gershman and Niv 2012, although you could possibly get away with something simpler if you assume 2 contexts.

(3) The focus on incongruent trials seems potentially thorny. It is intuitive why the authors do this: trials in which episodic and incremental values disagree are informative about which normative strategy the subjects are using. However, in the high volatility condition, if subjects are using incremental value, they may be more likely to have an outdated incremental value which would look consistent with the episodic choice. I would propose the authors look at congruent trials as well to confirm that they are indeed less likely to make errors on these trials in the high volatility condition than they are in the low volatility condition.

(4) Another question relates to the interpretation of competing for episodic v. incremental strategies, as opposed to just learning about independent features. One could argue that the subjects are doing instrumental learning over objects and colors separately, and when the reliability of one feature (color) is decremented, the other feature is relatively up-weighted. This also seems consistent with the fact that episodic and incremental learning tradeoff -- attending more to the object feature would perhaps compete with color.

(5) The authors show that uncertainty at encoding time does not have a discernible effect on the episodic index. This is evidence that volatility is modulating episodic contribution to decision-making, rather than encoding strength, which is a pretty fundamental part of the results (and in contrast to eg Sun et al. 2021, where unpredictability modulates episodic consolidation). One key thing to look at is if subjects show any difference in their ability to recall familiarity/value of objects from the different conditions. This would also speak to the question of if volatility is affecting encoding rather than just recall during decision-making. It would also make sense to look at the role of other variables at encoding time (eg prediction error) to see if these predict future use. It would also be interesting to see if subjects are storing the object value or the incremental value at the time the object was first shown -- this would be easy to check (when subjects rate the value in the last block, are they more likely to err in the direction of the incremental value at the time of encoding (eg like Figure 2A but with x-axis = incremental value at the time estimated with RW)). This would shed insight into exactly what kind of episodic strategy the subjects are deploying.

(6) The analysis showing that subjects that were better at recall in block 3 also had higher episodic index was a useful sanity check. It seems it would also be possible to perform this analysis within-subject (eg does episodic choice correlate with accurate value memory) and that would bear more on the question of whether it was uncertainty or simply a subjective preference for one strategy or another.
