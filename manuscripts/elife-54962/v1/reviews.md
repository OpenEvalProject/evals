# Peer review - Round 1

Editors:
- Samuel J Gershman, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54962.sa1](https://doi.org/10.7554/eLife.54962.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We believe that this paper makes fundamental contributions to our understanding of the perception-decision interface. In particular, it sheds light on how perceptual representation adapts to task demands. We foresee that this paper will stimulate future experimental work to test the mechanistic hypotheses postulated by the theory.

Decision letter after peer review:

Thank you for submitting your article "Efficient sampling and noisy decisions" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Samuel J Gershman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Konstantinos Tsetsos (Reviewer #2); Sebastian Gluth (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In their manuscript, Heng and colleagues derive general optimality principles and predictions of a decision-making system (or agent) that is restricted to encode information in terms of a finite number of binary samples. They find that in case of maximizing accuracy, the principle aligns with mutual information, but this changes if reward maximization is taken into account. Based on this, they conduct three numerosity experiments with different incentive rules ( "perceptual" vs. "preferential"). Surprisingly, they find that participants do not adjust their behavior to the incentive rule. Instead their behavior is best explained by the Decision by Sampling (DbS) framework, which assumes that behavior depends on the distribution of stimuli in the environment (in contrast to a simple log rule), but not in an optimal way. The reviewers agreed that this is an interesting and potentially important contribution to the literature on judgment and decision making, but requires substantive revisions in a number of respects detailed below.

Essential revisions:

1) Technical/conceptual issues.

a) The theoretical results depend on asymptotically taking n to be large. When n is finite, the proposed coding schemes may not necessarily be optimal, which should be recognized. Indeed this forms the basis of the Bhui and Gershman analysis of DbS.

b) The authors write that DbS continues to "explain the shape of ubiquitous psycho-economic functions", but they also provide accuracy maximization results. Do the alternative optimization criteria affect these curves or not?

c) The reward maximizing scheme assumes that agents seek to minimize "regret" (v1-v2). This is a viable hypothesis, but how does optimal encoding change if instead agents care just about the obtained reward (say, v1)? More generally, it is not a given that relative and not absolute reward is the relevant quantity in value based tasks.

2) Experimental/analysis issues.

a) The model recovery results shown in Figure 3D as well as the fits in Figure 4 rely on models in which the shape of the prior distribution is fixed and equal to the shape of the prior distribution used in experiments 1-2. Is the encoding rule still identifiable if the parameter controlling the shape of the prior is free to vary? The authors show recovery of the α parameter within the DbS model (Figure 5) but not when the encoding rule is unknown. Crucially, the conclusion that DbS outperform the other two encoding rules can be undermined if letting the prior free to vary induces model mimicry. Please examine this possibility. If indeed the different encoding schemes are not falsifiable it should be clearly stated that the conclusions (e.g "we found that humans employ a less optima strategy.", "allowed us to test the hypothesis" etc) hold under the specific assumption that the prior distribution is fixed.

b) Modeling of the adaptation to priors in experiments 1-3 assumes by definition that the prior parameter starts from a higher than the nominal value, and adapts across time with a time-scale that is shared across experiments. Is there indeed need/ evidence for adaptation? Observing the data in Figure 4—figure supplement 2 I can see that the accuracy a) is stable across time-rendering any adaptation process counterintuitive and, b) accuracy in Experiments 1-2 is higher than the accuracy in Experiment 3. Thus, the lower asymptotic α appears to serve the role of lowering overall accuracy. Please 1) superimpose the across time accuracy of the DbS model with prior adaptation on the traces shown in Figure 4—figure supplement 2, in order to see if the model systematically misfits the data by starting with α=2.84. 2) Please compare the fits of the adapting prior model with the a) the fits of a DbS model with just a free α parameter and b) a DbS model with α=2 and n as free parameter. Can these alternatives explain the data more parsimoniously?

c) One possible reason why the two conditions did not lead to differences could be that – after doing one condition for two days – it might have been impossible for the participants to adjust their "habit-like" behavior to a new incentive rule. This could be checked by analyzing the first half of the task in a between-subject manner.

3) Expository issues.

a) Provide more intuition for the equivalence between results under different optimization criteria. Do any of these results rely on the asymptotics?

b) The clarity of the Introduction can be improved. In the second paragraph, the authors suddenly jump to a discussion of differences between perceptual and preferential choice, but I think it would be more important to first make clear what the overall goal of the work is. The third paragraph is very confusing. Its first sentence is not even a full sentence (a verb is missing at "where only a finite number.…") and pretty much incomprehensible. Then, the work of Simon Laughlin is discussed, but it is questionable whether this is really the best way to motivate the proposal of a binary encoding system (why not simply saying that neurons provide binary outcomes). The reference to Query Theory in the fourth paragraph remains vague. In a later paragraph, the idea of adaptation to a frequency distribution is introduced without explaining what it actually means (and one reason for this is that DbS is not well explained in the previous paragraph).

c) In the Abstract, the authors should make more clear what the task was about (though we understand that this isn't easy give the word limit). In addition, the word "Here" is used to start two consecutive sentences, and an "a" is missing at "strategy that might be utilized…".

4) Links to related literature.

a) Do the results cast doubt on the argument made in the paper by Rustichini et al., 2017, which argues for a coding scheme based on expected utility maximization rather than mutual information?

b) Clarify that Equation 9 only corresponds to DbS in the asymptotic limit. The finite sample regime was emphasized in Bhui and Gershman, 2018, in order to explain certain phenomena (such as range effects) that do not follow directly from the CDF encoding function. Instead, that paper showed how these results could be obtained from a smoothed encoding function computed on a small set of samples. Relatedly, please clarify the links to the Bhui and Gershman paper. In particular, how does infomax in this paper (like in Supplementary Note 1) related to infomax in their paper? Also their work is described as adding noise after efficient coding, but this is not the case. The "noise" in that model comes purely from the fact that a finite number of samples are drawn, so that the sample-based CDF only approximates the true CDF.

c) The authors should discuss (and scrutinize) their empirical findings a bit more in the context of other studies that have compared perceptual and preferential decisions, in particular Dutilh and Rieskamp, 2015, who studied a quite similar task (choosing based on the number of dots with a perceptual vs. a preferential incentive rule). Here, it was found that decisions were slowest for the most difficult trials in the perceptual condition but not in the preferential condition. The question is whether there are any interesting, related response time differences between the two conditions in the current task (because if the number of dots on the left and right is very similar, one should not think too long about it if the reward depends on the number of dots [preferential], but one would need to think for a long time about it to decipher which side has more dots [perceptual]).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Efficient sampling and noisy decisions" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, including Samuel J Gershman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Konstantinos Tsetsos (Reviewer #2); Sebastian Gluth (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We are optimistic that the next revision will be acceptable for publication.

Summary:

In their revision the authors have successfully addressed most of the points we had raised. In particular the authors now discuss in detail the role of asymptotics and the relationship between their framework and the one proposed by Bhui and Gershman. This development has resulted in the extension of the framework in order to capture finite sampling from the prior distribution. Additionally, the authors have demonstrated that the encoding rule (as well as the shape of the prior and the number of samples) is identifiable when the shape of the prior is free to vary. All these developments have sufficiently improved the manuscript.

Revisions for this paper:

1) Having established the identifiability of the α parameter under the DbS model, it seems imperative to fit Experiment 3 using α as a free parameter and omitting the adaptation mechanism (this has been done in the revision but these results are used to examine whether there is adaptation or not, rather than to actually examine if the fitted prior differs between experiments 1-2 and 3). In other words, Figure 5A can be expanded to include the α fits from Experiment 3. This exercise can address whether there is indeed a change to the shape of the prior across experiments, which is a pivotal component of the proposed framework relative to alternative frameworks that assume complex representational non-linearities without sensitivity to the prior. The results in Figure 5C show that α in Experiment 3 converges to a lower asymptotic value. However, imposing an adaptation process, especially when there is no strong support for such process, can obscure the interpretation of the fits. Furthermore, I remain skeptical about the claim that there is dynamical adaptation within each experiment: i) if anything, the new analyses show that the "free α" model provides a better goodness of fit, and ii) Figures 4—figure supplement 2 and Figure 5—figure supplement 1 show no obvious dynamical trends in behavior. How does the adaptation manifest itself in the data? Figure 5—figure supplement 2 hints toward an early period in which the "free-α" fits worse than the dynamic α model (up to ~150 trials). Perhaps modeling this discrepancy explicitly (e.g. two α parameters for early and late trials, respectively) would suffice.
