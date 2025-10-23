# Peer review - Round 1

Editors:
- Konstantinos Tsetsos, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63436.sa1](https://doi.org/10.7554/eLife.63436.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Although recent research has described the interplay between attention and decision-making processes, the merits of employing selective attention during choice tasks remain largely underexplored. This paper closes this gap by offering a normative framework that specifies how reward-maximizing agents should employ attention while making value-based decisions. This framework, asides its theoretical importance, makes contact with the existing empirical literature while also providing detailed behavioural predictions that can be tested in future experiments.

Decision letter after peer review:

Thank you for submitting your article "Optimal policy for attention-modulated decisions explains human fixation behavior" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Konstantinos Tsetsos as the Reviewing Editor and Reviewer #, and the evaluation has been overseen by Joshua Gold as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In this paper the authors derive a normative model of attentional switching during binary value-based decisions. The model the authors propose assumes that attentional allocation is under the control of the agent, who on each moment decides among halting deliberation and choosing an alternative, carrying on sampling from the currently attended alternative, switching attention to the other alternative. Under certain assumptions about deliberation and attentional allocation costs, the authors derive the optimal policy, showing also that this policy reproduces key aspects of human behaviour. The approach here stands in contrast with the majority of past research on this topic, which has assumed that attentional allocation is exogenous and that it influences- but is not influenced by- the ongoing choice process. All reviewers agreed that this is an interesting and timely article that takes a normative approach to the important issue of attentional allocation in decision-making tasks. However, the reviewers also agreed that there are several points that will need to be addressed in a revision.

Essential revisions

1. Link between the normative model and human data.

One of the main claims in the paper is that the normative model reproduces key aspects of human behaviour in a value-based binary choice task reported elsewhere (Krajbich et al., 2010). This claim needs to be backed up by additional analyses and clarifications. In particular:

a. In Figure 3A, the model predicts a linear choice curve (as opposed to a sigmoidal in the human data) while, also unlike in the data, the RT curves are concave. Are the shapes of these curves a general feature of the model or do they emerge for a certain parametrisation? Would for example the results look different with fixed bounds?

b. Similarly, in Figure 3D, the model shows that the last fixation influences probability of choice equally across value differences. In the human data this effect diminishes as value difference increases. Is this prediction or a feature of the model?

c. In Figure 3C the authors focus on the number of switches, which however are highly correlated with RTs. Can the authors show in addition the number of switches per unit of time (equivalent to probability of switching) in the human data and in their model?

d. In Figure 4B-C, RTs and "value sum" may covary, with high value sums presumably resulting in shorter RTs. Does the value sum effect persist in the model and in the data once the influence of RTs is accounted for?

2. Comparison between the normative and aDDM models.

The two models differ in the way they conceptualise attentional switching (exogenous vs. endogenous). Does this difference manifest itself in the predictions the two models make? And can the human data distinguish between the two models? The authors comment in the Discussion that their model is more constrained by normative considerations, and may thus fit the data worse than other ad-hoc models. Asides quantitative fitting, which the authors may elect to perform, we would like to see a qualitative comparison between the two models.

a. How does the probability of switching changes as a function of time (within trial) and as a function of absolute value difference and sum (across trials) in the two models and in the data?

b. How does the fixation duration changes as a function of time (within trial) and as a function of absolute value difference and sum (across trials) in the two models and in the data?

c. The model seems to predict a non-negligible number of single fixation trials. How does this align with the data and the aDDM predictions?

d. How do reaction time distributions look like under the normative model? Are these comparable to the RT distributions in the data?

e. Please also show the aDDM predictions together with the novel predictions made by the normative model in Figure 4C.

f. The comparison between the two models is currently done on the basis of mean reward. How do the predictions of the models compare to the mean reward accrued by human participants in Krajbich et al? Please also clarify in the main text that the models are not compared on the basis of goodness of fit. In particular, in the paragraph starting in line 260, terms such as "outperformed", "competitive performance", "comparison" are ambiguous.

g. Please explain why the model shows the pattern that is demonstrated in Figure 3F. Is this pattern also predicted by the aDDM?

3. Comprehensibility of the modelling.

The authors have done an admirable job of boiling down some heavy mathematics (in the SI) into just the key steps in the main text. A lot of this builds on prior work in Tajima et al. Still, the authors could do more to explain the math, which would make this paper more self-contained and really help the reader understand the core ideas/intuitions.

a. Equation 1 – it isn't obvious how the mean will behave over time or where this expressions comes from. It would be helpful to state that the z part is the prior, and that as t->infinity the σ terms become negligible and the expression converges to x/t, namely the true value. The σ-squared terms seem to come out of nowhere. In the methods the authors explain that this has to do with Fisher information, but most readers won't know what that is or why it is the appropriate thing to include here. Also, σx is defined later in the text, but should be defined up front here.

b. Between Equation 1 and 2: In the means for δx, one has a δt multiplying z and one doesn't. Why? Is this a typo? The δt should always be there, but again, it isn't obvious.

c. Equation 2: Why does the mean have a z1| at the beginning of it? Is that a typo?

d. Could the authors elaborate more on why/when the decision maker chooses to switch attention? They say that the decision at each time point only depends on the difference in posterior means but Figure 2c seems to indicate that if the difference in posterior means stays constant over a period of time, then the process enters the "switch" zone and shifts attention.

4. Model assumptions.

a. The model assumes that attention can take one of two discrete states. However, attention is often regarded as operating in a more graded fashion, which would necessitate parameter kappa in the model to be free to change within a trial. This will probably render the model intractable. However, a more viable and less radical assumption, would be to allow for a third "divided attention" mode in which the agent samples equally from both alternatives (divided attention mode). If this extension is technically challenging, one conceptual question that the authors can discuss in the paper, is whether the normative model would ever switch away from this divided attention mode.

b. The authors need to assume a certain prior, namely z_bar = 0, in order to always get a positive effect of attention. This seems like an important controversy in the model; it is a noticeably non-Bayesian feature of a Bayesian model. The authors try to explain this away by noting that the original rating scale included both negative and positive values. However, only positive items were included in the choice task, and there is a consistently positive effect of attention on choice for other tasks (see Cavanagh et al. 2014; Smith and Krajbich 2018; Smith and Krajbich 2019) with only positive outcomes. This needs to be more openly acknowledged and discussed.

c. The last paragraph of Discussion talks about a lack of benefit of focussed attention in the analysed task. Would focussing attention would become beneficial in decision tasks with more than 2 options? Although answering this question would be a separate paper, a few sentences on generalising this work to more than two options could be included in the Discussion.

5. Coverage of literature.

a. In the Introduction, the authors state that the "final choices are biased towards the item that they looked at longer, irrespective of its desirability". This is not quite true. The desirability does matter, as shown in Smith and Krajbich 2019, as well as Westbrook et al. 2020. Moreover, as the authors note in the discussion, Armel et al. 2008 show that attention has a reverse effect when the items are aversive. Please update the introduction accordingly.

b. The authors do not mention that there is some work that has argued for value attracting attention in multi-alternative choice. While that work does not go to the lengths that this paper does, it does make normative arguments for why this should occur, namely to eliminate non-contenders (Krajbich and Rangel 2011; Towal et al. 2013; Gluth et al. 2020). Finally, the authors might also want to mention Ke, Shen, Villas-Boas (2016), which also takes a normative approach to information search in consumer choice.

c. On page 2 the authors state that "no current normative framework incorporates control of attention as an intrinsic aspect of the decision-making process". This does not seem to be accurate given the study by of Cassey et al. (2013). The key difference is that in Cassey et al. the focus was placed on the fixed duration paradigm, while the present manuscript focuses on the free-response paradigm. Please clarify the link of the current study with Cassey et al.

d. In lines 318-321, the authors state that the model of Cassey et al. "could not predict when they [fixation switches] ought to occur". The model of Cassey et al. does predict when the optimal switching times are, but for the case of a fixed duration paradigm with \kappa = 0. In this case the optimal switch policy is much simpler (single or at most double switch at particular times) than in the free-response paradigm nicely analysed in the present manuscript.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Optimal policy for attention-modulated decisions explains human fixation behavior" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

Summary:

The authors have done an excellent and thorough job in addressing most of the comments that were raised during the first review. Please find below a list of remaining issues.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Essential revisions

1. In our previous points 2a-b the request was to show the switch rate and fixation duration as a function of time, value sum and value difference. We apologise if that was not clear previously but with the term "time" we referred to elapsed time within a trial rather than reaction times (RT). Because RT's will be influenced by various properties of the trial (e.g. trial difficulty) the analyses reported in the revision are not very easy to interpret. Additionally, we are puzzled by the fact that the aDDM model predicts non-flat switch rates and fixation durations as a function of the different quantities (Figure 4—figure supplement 1), given that switching in the aDDM version the authors used is random. The aim of these previous points was to (a) highlight the differences between random switching (aDDM) and deliberate switching (optimal model), and (b) understand how switching tendencies change as a function of trial-relevant quantities and time elapsed in the optimal model. We appreciate that such analyses might be difficult to perform given the interrelationship among time, value sum and absolute value difference. Below we offer a few suggestions:

– One possibility is to consider a "stimulus locked" approach, in which the switch rate and fixation duration is plotted as a function of time elapsed from the stimulus onset and up to "x" milliseconds before the response. Inevitably, later time points will more likely include certain trial types, e.g. only difficult trials (or trials with low value sum). The authors can consider using a "stratification" approach, subsampling the trials such that all time-points have comparable trial distributions (in terms of value difference and value sum). The influence of value difference and value sum can be examined using median splits based on these quantities.

– Specifically for the switch rate analysis, the authors could perform a logistic regression trying to predict at each point in time the probability of switching, also considering covariates such as value sum or absolute value difference.

– Since the last fixation can be cut short, we recommend excluding the last fixation from these analyses.

– We recommend that the scaling of the x and y axis in the data and in the models is the same to allow comparison in absolute terms.

2. Krajbich et al. 2010 used an aDDM implementation in which fixations were not random but instead sampled from the empirical switching times distributions (thus fixations depended on fixation number, trial difficulty etc). The authors currently do not acknowledge this previous implementation. The aDDM with random switching is a good baseline for the scope of this paper, but the version used by Krajbich et al. 2010 makes different predictions than the random aDDM; and this should be explicitly acknowledged. For instance, the aDDM where switching matches the empirical distributions, accounts for the fact that the first fixations were shorter than the rest. Discussing this non-random aDDM used by Krajbich et al. 2010, will fit easily in the current discussion, since the optimal model offers a rationale fort the empirical fixation patterns that the older work simply incorporated into the aDDM simulations.

3. The authors slightly mischaracterise Krajbich and Rangel 2011 by saying that "fixation patterns were assumed to be either independent of the decision-making strategy". That paper did condition fixation patterns on the values of the items. Here is a direct quote from the Discussion: "These patterns are interesting for several reasons. First, they show that the fixation process is not fully independent from the valuation process, and contains an element of choice that needs to be explained in further work."

4. When comparing the mean reward of the models, the authors simulate the aDDM not with the parameters from Krajbich et al. 2010, but with different parameters meant to "ensure a fair comparison" between the models. We believe that this approach sets the aDDM to a disadvantage. If the best-fitting parameters of the "optimal model" lead to a lower signal-to-noise ratio than the aDDM best-fitting parameters, that should be acknowledged and accepted as is. We recommend the authors state upfront that the best-fitting optimal model does not outperform the data or the aDDM. However, if you use a non-best-fitting aDDM, then the aDDM underperforms both.
