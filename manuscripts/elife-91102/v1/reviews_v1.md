# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91102.3.sa0](https://doi.org/10.7554/eLife.91102.3.sa0)

This manuscript provides a valuable demonstration that distractor effects in multi-attribute decision-making correlate with the form of attribute integration (additive vs. multiplicative). The evidence supporting the conclusions is convincing, but there are questions about how to interpret the findings. The manuscript will be interesting to decision-making researchers in neuroscience, psychology, and related fields.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91102.3.sa1](https://doi.org/10.7554/eLife.91102.3.sa1)

Summary:

The current study provided a follow-up analysis using published datasets focused on the individual variability of both the distraction effect (size and direction) and the attribute integration style, as well as the association between the two. The authors tried to answer the question of whether the multiplicative attribute integration style concurs with a more pronounced and positively oriented distraction effect.

Strengths:

The analysis extensively examined the impacts of various factors on decision accuracy, with particular focus on using two-option trials as control trials, following the approach established by Cao & Tsetsos (2022). The statistical significance results were clearly reported.

The authors meticulously conducted supplementary examinations, incorporating the additional term HV+LV into GLM3. Furthermore, they replaced the utility function from the expected value model with values from the composite model.

Weaknesses:

The authors did a great job addressing the weaknesses I raised in the previous round of review, except on the generalizability of the current result in the larger context of multi-attribute decision-making. It is not really a weakness of the manuscript but more of a limitation of the studied topic, so I want to keep this comment for public readers.

The reward magnitude and probability information are displayed using rectangular bars of different colors and orientations. Would that bias subjects to choose an additive rule instead of the multiplicative rule? Also, could the conclusion be extended to other decision contexts such as quality and price, where a multiplicative rule is hard to formulate?

Overall, the authors have achieved their aims after clarifying that the study was trying to establish a correlation between the integration style and attraction effect. This result may be useful to inspire neuroimaging or neuromodulation studies that investigate multi-attribute decision making.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91102.3.sa2](https://doi.org/10.7554/eLife.91102.3.sa2)

This paper addresses the empirical demonstration of "distractor effects" in multi-attribute decision-making. It continues a debate in the literature on the presence (or not) of these effects, which domains they arise in, and their heterogeneity across subjects. The domain of the study is in a particular type of multi-attribute decision-making: choices over risky lotteries. The paper reports a re-analysis of lottery data from multiple experiments run previously by the authors and other labs involved in the debate.

Methodologically, the analysis assumes a number of simple forms for how attributes are aggregated (adaptively, or multiplicatively, or both) and then applies a "reduced form" logistic regression to the choices with a number of interaction terms intended to control for various features of the choice set. One of these interactions, modulated by ternary/binary treatment, is interpreted as a "distractor effect."

The claimed contribution of the re-analysis is to demonstrate correlation in the strength/sign of this treatment effect with another estimated parameter: the relative mixture of additive/multiplicative preferences.

Major Issues

(1) How to Interpret GLM 1 and 2

This paper, and others before it, have used a binary logistic regression with a number of interaction terms to attempt to control for various features of the choice set and how they influence choice. It is important to recognize that this modelling approach is not derived from a theoretical claim about the form of the computational model that guides decision-making in this task, nor an explicit test for a distractor effect. This can be seen most clearly in the equations after line 321 and its corresponding log-likelihood after 354, which contain no parameter or test for "distractor effects". Rather the computational model assumes a binary choice probability, and then shoehorns the test for distractor effects via a binary/ternary treatment interaction in a separate regression (GLM 1 and 2). This approach has already led to multiple misinterpretations in the literature (see Cao & Tsetsos, 2022; Webb et al., 2020). One of these misinterpretations occurred in the datasets the authors study, in which the lottery stimuli contained a confound with the interaction that Chau et al., (2014) were interpreting as a distractor effect (GLM 1). Cao & Tsetsos (2022) demonstrated that the interaction was significant in binary choice data from the study, therefore it can not be caused by a third alternative. This paper attempts to address this issue with a further interaction with the binary/ternary treatment (GLM 2). Therefore the difference in the interaction across the two conditions is claimed to now be the distractor effect. The validity of this claim brings us to what exactly is meant by a "distractor effect."

The paper begins by noting that "Rationally, choices ought to be unaffected by distractors" (line 33). This is not true. There are many normative models which allow for the value of alternatives (even low-valued "distractors") to influence choices, including a simple random utility model. Since Luce (1959), it has been known that the axiom of "Independence of Irrelevant Alternatives" (that the probability ratio between any two alternatives not depend on a third) is an extremely strong axiom, and only a sufficiency axiom for a random utility representation (Block and Marschak, 1959). It is not a necessary condition of a utility representation, and if this is our definition of rational (which is highly debatable), not necessary for it either. Countless empirical studies have demonstrated that IIA is falsified, and a large number of models can address it, including a simple random utility model with independent normal errors (i.e. a multivariate Probit model). In fact, it is only the multinomial Logit model that imposes IIA. It is also why so much attention is paid to the asymmetric dominance effect, which is a violation of a necessary condition for random utility (the Regularity axiom).

So what do the authors even mean by a "distractor effect." It is true that the form of IIA violations (i.e. their path through the probability simplex as the low-option varies) tells us something about the computational model underlying choice (after all, different models will predict different patterns). But we do not know how the interaction terms in the binary logit regression relate to the pattern of the violations because there is no formal theory that relates them. Any test for relative value coding is a joint test of the computational model and the form of the stochastic component (Webb et al,. 2020). These interaction terms may simply be picking up substitution patterns that can be easily reconciled with some form of random utility. While we can not check all forms of random utility in these datasets (because the class of such models is large), this paper doesn't even rule any of these models out.

(2) How to Interpret the Composite (Mixture) model?

On the other side of the correlation is the results from the mixture model for how decision-makers aggregate attributes. The authors report that most subjects are best represented by a mixture between additive and multiplicative aggregation models. The authors justify this with the proposal that these values are computed in different brain regions and then aggregated (which is reasonable, though raises the question of "where" if not the mPFC). But an equally reasonable interpretation is that the improved fit of the mixture model simply reflects a misspecification of two extreme aggregation process (additive and EV), so the log-likelihood is maximized at some point in between them.

One possibility is a model with utility curvature. How much of this result is just due to curvature in valuation? There are many reasonable theories for why we should expect curvature in utility for human subjects (for example, limited perception: Robson, 2001, Khaw, Li Woodford, 2019; Netzer et al., 2022) and of course many empirical demonstrations of risk aversion for small stakes lotteries. The mixture model, on the other hand, has parametric flexibility.

There is also a large literature on testing expected utility jointly with stochastic choice, and the impact of these assumptions on parameter interpretation (Loomes & Sugden, 1998; Apesteguia & Ballester, 2018; Webb, 2019). This relates back to the point above: the mixture may reflect the joint assumption of how choice departs from deterministic EV.

(3) So then how should we interpret the correlation that the authors report?

On one side we have the impact of the binary/ternary treatment which demonstrates some impact of the low value alternative on a binary choice probability. This may reflect some deep flaw in existing theories of choice, or it may simply reflect some departure from purely deterministic expected value maximization that existing theories can address. We have no theory to connect it to, so we cannot tell. On the other side of the correlation with have the mixture between additive and multiplicative preferences over risk. This result may reflect two distinct neural processes at work, or it may simply reflect a misspecification of the manner in which humans perceive and aggregate attributes of a lottery (or even just the stimuli in this experiment) by these two extreme candidates (additive vs. EV). Again, this would entail some departure from purely deterministic expected value maximization that existing theories can address.

It is entirely possible that the authors are reporting a result that points to the more exciting of these two possibilities. But it is also possible (and perhaps more likely) that the correlation is more mundane. The paper does not guide us to theories that predict such a correlation, nor reject any existing ones. In my opinion, we should be striving for theoretically-driven analyses of datasets, where the interpretation of results is clearer.

(4) Finally, the results from these experiments might not have external validity for two reasons. First, the normative criterion for multi-attribute decision-making differs depending on whether the attributes are lotteries or nor (i.e. multiplicative vs additive). Whether it does so for humans is a matter of debate. Therefore if the result is unique to lotteries, it might not be robust for multi-attribute choice more generally. The paper largely glosses over this difference and mixes literature from both domains. Second, the lottery information was presented visually and there is literature suggesting this form of presentation might differ from numerical attributes. Which is more ecologically valid is also a matter of debate.

Minor Issues:

The definition of EV as a normative choice baseline is problematic. The analysis requires that EV is the normative choice model (this is why the HV-LV gap is analyzed and the distractor effect defined in relation to it). But if the binary/ternary interaction effect can be accounted for by curvature of a value function, this should also change the definition of which lottery is HV or LV for that subject!

Comments on latest version: the authors did respond to some of my comments with discussion points in the paper.

References

Apesteguia, J. & Ballester, M. Monotone stochastic choice models: The case of risk and time preferences. Journal of Political Economy (2018).

Block, H. D. & Marschak, J. Random Orderings and Stochastic Theories of Responses. Cowles Foundation Discussion Papers (1959).

Khaw, M. W., Li, Z. & Woodford, M. Cognitive Imprecision and Small-Stakes Risk Aversion. Rev. Econ. Stud. 88, 1979-2013 (2020).

Loomes, G. & Sugden, R. Testing Different Stochastic Specifications of Risky Choice. Economica 65, 581-598 (1998).

Luce, R. D. Indvidual Choice Behaviour. (John Wiley and Sons, Inc, 1959).

Netzer, N., Robson, A. J., Steiner, J. & Kocourek, P. Endogenous Risk Attitudes. SSRN Electron. J. (2022) doi:10.2139/ssrn.4024773.

Robson, A. J. Why would nature give individuals utility functions? Journal of Political Economy 109, 900-914 (2001).

Webb, R. The (Neural) Dynamics of Stochastic Choice. Manage Sci 65, 230-255 (2019).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91102.3.sa3](https://doi.org/10.7554/eLife.91102.3.sa3)

Summary:

The way an unavailable (distractor) alternative impacts decision quality is of great theoretical importance. Previous work, led by some of the authors of this study, had converged on a nuanced conclusion wherein the distractor can both improve (positive distractor effect) and reduce (negative distractor effect) decision quality, contingent upon the difficulty of the decision problem. In very recent work, Cao and Tsetsos (2022) reanalyzed all relevant previous datasets and showed that once distractor trials are referenced to binary trials (in which the distractor alternative is not shown to participants), distractor effects are absent. Cao and Tsetsos further showed that human participants heavily relied on additive (and not multiplicative) integration of rewards and probabilities.

The present study by Wong et al. puts forward a novel thesis according to which interindividual differences in the way of combining reward attributes underlie the absence of detectable distractor effect at the group level. They re-analysed the 144 human participants and classified participants into a "multiplicative integration" group and an "additive integration" group based on a model parameter, the "integration coefficient", that interpolates between the multiplicative utility and the additive utility in a mixture model. They report that participants in the "multiplicative" group show a negative distractor effect while participants in the "additive" group show a positive distractor effect. These findings are extensively discussed in relation to the potential underlying neural mechanisms.

Strengths:

- The study is forward looking, integrating previous findings well, and offering a novel proposal on how different integration strategies can lead to different choice biases.

- The authors did an excellent job in connecting their thesis with previous neural findings. This is a very encompassing perspective that is likely to motivate new studies towards better understanding of how humans and other animals integrate information in decisions under risk and uncertainty.

- Despite that some aspects of the paper are very technical, methodological details are well explained and the paper is very well written.

Weaknesses:

- The authors quantify the distractor variable as "DV - HV", i.e., the relative distractor variable. Conclusions mostly hold when the distractor is quantified in absolute terms (as "DV", see also Cao & Tsetsos, 2023). However, it is not entirely clear why the impact of the distractor alternative is not identical when the distractor variable is quantified in absolute vs. relative terms. Although understanding this nuanced point seems to extend beyond the scope of the paper, it could provide valuable decision-theoretic (and mechanistic) insights.

- The central finding of this study is that participants who integrate reward attributes multiplicatively show a positive distractor effect while participants who integrate additively show a negative distractor effect. This is a very interesting and intriguing observation. However, it does not explain why the integration strategy covaries with the direction of the distractor effect. As the authors acknowledge, the composite model is not explanatory. Although beyond the scope of this paper, it would be valuable to provide a mechanistic explanation of this covariation pattern.
