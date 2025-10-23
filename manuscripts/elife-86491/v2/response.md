# Author response - Round 1

Authors:
- Silvia Maggi ([ORCID: 0000-0001-6533-3509](https://orcid.org/0000-0001-6533-3509))
- Rebecca M Hock ([ORCID: 0000-0002-0917-570X](https://orcid.org/0000-0002-0917-570X))
- Martin O'Neill
- Mark Buckley ([ORCID: 0000-0001-7455-8486](https://orcid.org/0000-0001-7455-8486))
- Paula M Moran
- Tobias Bast ([ORCID: 0000-0002-6163-3229](https://orcid.org/0000-0002-6163-3229))
- Musa Sami
- Mark D Humphries ([ORCID: 0000-0002-1906-2581](https://orcid.org/0000-0002-1906-2581))

## Response text

DOI: [10.7554/eLife.86491.sa2](https://doi.org/10.7554/eLife.86491.sa2)

Essential revisions:

1. The method ignores the precision of the posterior in its selection of the best strategy. This is more of a "winner-take-all" approach rather than a method that exploits the Bayesian framework to take the uncertainty of the posterior into account.

As we use selection of the best strategy only once, in our view this refers to a minor aspect of analysing a simulation, and not a critique of our main contributions – the algorithm and its insights on learning. But we agree with the underlying sentiment that more could be done to demonstrate the use of having the full posterior, and expand on this below. We note that our aim was to be careful in the paper to separate the method, the estimation of the trial-resolution posterior of p(strategy), from the use of its output by further processing of the posterior, and this comment refers to the latter, not the former.

We use selection of the best strategy only once when quantifying the performance of the algorithm on the example simulation of a synthetic agent. As implied by the phrase “winner-takes-all”, here we use a simple approach of choosing the strategy with the maximum MAP, and breaking ties by choosing the strategy with the highest precision, indicating lower uncertainty. While we suggest in the text this could be a useful approach to apply to data, we readily acknowledged that richer criteria could be derived from the posterior distributions obtained by the algorithm (lines 602-612 in the original submission). To make these points more clearly, we have redrafted the Results text describing the synthetic agent simulation (191-194) and the Discussion section suggesting further development in the use of the algorithm’s output (lines 881-890).

In the paper we outlined two questions we aimed to tackle given the posterior distribution of each strategy: detecting learning and tracking the use of exploratory strategies. Consequently we do not “detect the best strategy” in any data analyses we present (Figure 3-7 and accompanying supplementary figures). We have redrafted the opening paragraphs of the Results (lines 74-79) and the relevant paragraph in the Discussion (lines 875-880) to further clarify the core questions of the paper.

On the issue of making further use of the uncertainty in the posterior we have done three things:

We have added a paragraph to the Results after we introduce the algorithm (lines 155 – 160) to draw the reader’s attention to how we use the posterior and what more could be done with it.

We have given a fuller account of the behaviour of the posterior as a function of the forgetting rate (γ): the Methods now include a clearly marked section and text discussing this around Equations 15 and 16 (lines 947-962); and Figure 2 now includes panels g-i showing the posterior’s behaviour.

We developed and tested two further criteria for learning that considered the uncertainty in the posterior. These are presented in the Results (lines 312-326); outlined in the Methods (lines 802-808); and the outcomes of using these criteria on the Y-maze and lever-press task are summarised in Figure 3 – Supplemental Figure 1. We find all criteria replicate the result that rats learnt the switch from a cued to a spatial rule considerably faster than switching from a spatial to a cued rule.

2. The authors do not convincingly demonstrate that their method is robust to the presence or absence of a true strategy. Both reviewers ask for an analysis that shows what happens to the prediction when the true strategy is present or absent.

As noted above, the determination of which is the “true” strategy was not our goal, and we do not use our algorithm in this way in the paper. Rather, we focused on tracking the probability of user-specified strategies, so that we can capture the evidence for learning or for the features driving exploratory choice (e.g. are agents responding to losses or wins; are they responding to cues or choice etc).

One reason for this focus is that to our minds detecting a single “true” strategy is ambiguous. For the observer, multiple strategies may be logically equivalent – for example, a subject that consistently chooses “go right” and gets rewarded is also consistently choosing “win-stay” to their choice. Subjects may be actively using more than one strategy – for example, when they switch strategies when learning a new rule after a previously-established one, then both are often expressed on different trials (e.g. Figure 1d and f). Thus our algorithm seeks to track the probability of the use of each strategy, and interpret these as the observer’s estimate of the likelihood of their expression.

We have extensively redrafted the section on analysing the algorithm’s performance (Section “Robust tracking of strategies in synthetic data”) to clarify the goals of that analysis and how each set of simulations or analyses addresses them: (1) to provide the rationale for the use of evidence decay; (2) to show how evidence decay affects the algorithm’s output, and thus provide a basis for defining usable values of that parameter; and (3) to provide aid in interpreting the resulting values of P(strategy). In the context of (3), we have considered what values P(strategy) can take when a true exploratory strategy is missing. We redrafted the text on the analysis of the missing “true strategy” (lines 239-246) to clarify its aims and insights.

In redrafting this section we also addressed individual reviewer requests for more information on the limits of the method (the behaviour of the posterior, noted above, lines 209-217) and concerns about the choice of values for the evidence decay parameter (esp. lines 220-230).

3. Figures 3 c through f should be clarified.

We have done the following to clarify the results:

To panel c: added a histogram of the number of identified learning trials per animal

To panel f: shown all individual animals’ data in light, open symbols; reduced the jitter of the symbols to align them better with the x-axis labels; and overplotted the mean and standard error of the mean as solid symbols to provide a clearer summary of the main results (of earlier detection of learning by strategy-based criterion during the first learnt rule; and of slower learning of a cued rule when it followed a spatial rule).

Added ANOVAs to give statistical support to the result that, in the lever-press task, learning the cued rule after a spatial rule is slower than the reverse.

4. The choice of strategies to test the approach is limited. Strategies are static and are unparametrized for choice stochasticity and trial history dependence. Given that more sophisticated strategies are not explored, it is unclear whether this method can be useful in arbitrating between those.

We politely disagree with this statement. We tested 14 different strategies in the paper (Tables 1-3 of the Methods). These include a range of strategies that use trial history dependence (e.g. Figure 7 and Table 3), and the Discussion already touched on ways to extend to other trial history dependence, such as dependence on outcome N trials in the past. We have redrafted the Results text around Figure 7 (lines 459-463) and the Discussion section (lines 602-606) to make this more explicit.

We have clarified that our results already showed the algorithm can track the stochastic use of a strategy (Results lines 223-227, and Figure 2 – Supplemental Figure 3).

5. Win-Stay Lose-Shift analysis is confounded and provides limited evidence for what can be learned in real data using the method.

We agree that we did not explain this well. Indeed in the absence of losses Lose-Shift cannot be updated, and in the absence of wins Win-Shift cannot be updated. However, this analysis focussed on the trials preceding the detected learning trial or the trials following a rule switch. In both cases, there is a mixture of wins and losses, so the probabilities of both Lose-Shift and Win-Stay can be updated. We now show this explicitly by plotting the per-trial rate of correct choices around both learning and rule-shifts in Figure 5. The accompanying text results have been redrafted to acknowledge the need for evidence of losses and wins [lines 371-373 and 385-387]; we have also simplified the text in the Results discussing Figure 5 to further clarify the focus of the analysis on the trials preceding learning and following rule-switches [lines 367 – 389].

Further Revisions

Reviewer 1 suggested we “Define "strategy" and/or give examples in the Introduction because it can be a vague concept to readers from different backgrounds.” The Introduction now gives explicit examples (lines 40-43).

Reviewer 1 commented that “it should be made extremely clear that this method is purely descriptive, rather than explanatory. It is not a modeling approach, rather a data analysis approach”. We are in firm agreement: indeed the Discussion included a dedicated paragraph on this point beginning “The probabilities computed by our algorithm are a description of the observer…”, and throughout the algorithm was described from the perspective of the observer, not the agent. To make this even clearer, we have edited the Results text introducing the method to emphasise that the evidence and computation are from the observer’s point of view (lines 71, 87-91).

We have revised text throughout for clarity.
