# Peer review - Round 1

Editors:
- Alicia Izquierdo, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86491.sa0](https://doi.org/10.7554/eLife.86491.sa0)

This work describes a valuable method for indexing trial-by-trial learning and decision making strategies in animal and human behavior. The study provides compelling evidence for the validity of this new method.


---

# Peer review - Round 1

Editors:
- Alicia Izquierdo, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86491.sa1](https://doi.org/10.7554/eLife.86491.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Tracking subjects' strategies in behavioural choice experiments at trial resolution" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The method ignores the precision of the posterior in its selection of the best strategy. This is more of a "winner-take-all" approach rather than a method that exploits the Bayesian framework to take the uncertainty of the posterior into account.

2. The authors do not convincingly demonstrate that their method is robust to the presence or absence of a true strategy. Both reviewers ask for an analysis that shows what happens to the prediction when the true strategy is present or absent.

3. Figures 3 c through f should be clarified.

4. The choice of strategies to test the approach is limited. Strategies are static and are unparametrized for choice stochasticity and trial history dependence. Given that more sophisticated strategies are not explored, it is unclear whether this method can be useful in arbitrating between those.

5. Win-Stay Lose-Shift analysis is confounded and provides limited evidence for what can be learned in real data using the method.

Reviewer #1 (Recommendations for the authors):

1. The approach is presented as Bayesian, however, that is really a stretch, in ways that matter for the interpretation of the tool. First, the evidence at each trial is taken to be all or nothing (l94-95), rather than integrating over any potential uncertainty. This might make sense for deterministic strategies but it is unclear why this approach is taken for non-deterministic policies. I note that for all real data, assuming deterministic policies is very unrealistic. Second, the full posterior computed by the Bayesian method isn't fully used to compare strategies. There should be a better way to incorporate the variance of the posterior into the decision rule (lines 202-204). The variance shouldn't be completely ignored if the MAP probabilities are different. More generally, the full assumptions of the model should be more carefully described when the approach is presented.

2. The strategy space considered is problematic in a few ways, despite the authors' efforts to include probabilistic strategies.

a. First the strategies considered are all static, despite the emphasis on a dynamic environment. In that sense, it should be made extremely clear that this method is purely descriptive, rather than explanatory. It is not a modeling approach, rather a data analysis approach that might allow researchers to answer questions of the type "by when did the animal reliably express a [follow the light] strategy", for example. It cannot offer insights into how the animal arrives at the strategy or learns it.

b. The possibility that the true strategy might be missing is not sufficiently discussed or analyzed. The authors should show comparisons between the case where the true strategy is known and the case where it is not. For example, what would Figure 2b&c look like if the true strategies are not considered?

c. The authors make strong statements that are not adequately supported. For example, "a MAP probability approaching 1 is strong evidence that the tested strategy is, or equivalent to, the true strategy (lines 271-273)." The paper does not include any analysis that supports this statement.

3. The previous two points may limit the usefulness of the new technique. In practice, animals' policies in dynamic environments are unlikely to be stable and unparameterized; most of the literature instead relies on strategies that include noise parameters, and potentially are dependent on trial history in a parameterized way (e.g., multi-choice stickiness, or reward sensitivity). There is no clear way in which such strategies could be considered by the current method; and by contrast, existing model fitting methods would work well for such strategies, which are also more likely to be relevant.

4. Some analyses lack details in descriptions or analysis in a way that makes them hard to evaluate.

a. Figure 3 c/f: the plots are very difficult to read due to scaling, making the comparison difficult.

b. If the strategy is irrelevant in a given trial, the numbers are not updated (i.e., the trial is neither a match nor a non-match). This complicates the win-stay lose shift result interpretation, as it is likely to be a different proportion of win vs. lose trials. This could lead to the apparent slower decay, which would obviate the conclusion that WS-LS is not a single strategy, but two separate strategies.

c. Figures S5-S6 consider the case of probabilistic strategies; however, the task and strategies considered are insufficiently described. In Figure S5, the authors should show p(match) as a function of MAP probability instead of the other way around, because in practice we are more interested in estimating p(match) with MAP probability.

Reviewer #2 (Recommendations for the authors):

I find this approach to be extremely compelling and highly useful. I do have one concern about how robust this approach is to the presence or absence of the real strategy in the candidates that are being tested and updated. This is a slightly different question than what was addressed with the enumeration of possible values of p(match) described on pages 8-9. I would like to see a test that compares the MAP estimates of incorrect strategies A and B when the true strategy C is absent versus present in the strategies being tested.

I congratulate the authors on a well-written and coherent manuscript. I have a few specific suggestions for improving the clarity and readability:

General: check your manuscript for use of the passive voice.

Page 9 line 217: consider re-writing the sentence starting with "We deemed […]".

Figure 2, panels h and i: the caption reads "number of trials after the crossover trial until detection, as a function of how quickly the probabilities […] change per trial". While I understand that the word "quickly" is being used as a substitute for the amount of probability change, it is misleading in that the x-axis of those plots has nothing to do with time.

Figure 3, panels c and f: I found these figures to be especially confusing. It is not clear what each dot represents in each case (in some cases it is trials and in others it is animals). The point the authors are trying to convey is thus not effectively conveyed. For example, the takeaway is that there is a significant difference in the learning trials for each rule between the original and the strategy criterion for the first rule and not the second, aside from the p values, the scatter plots do not serve as effective visualizations of this point.

Page 12 line 366: The section title should read "lose-shift, not win-stay" instead of the current version (it is inverted).
