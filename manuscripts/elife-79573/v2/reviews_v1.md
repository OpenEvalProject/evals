# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79573.sa0](https://doi.org/10.7554/eLife.79573.sa0)

This valuable article describes a fragility index based on the geometry of chi-square tests. The result is linked to the concept of measurement error in outcomes, such that one can directly quantify how less-than-perfect sensitivity or specificity will call into question the statistical significance of a particular finding. The methodology rests upon solid mathematical exposition and several real-world examples of both interventional and observational studies. Noteworthy extensions for future considerations would be the application of this approach to censored outcomes.


---

# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79573.sa1](https://doi.org/10.7554/eLife.79573.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "The Ellipse of Insignificance: a refined fragility index for ascertaining robustness of results in dichotomous outcome trials" for consideration by eLife. My apologies for the delay in getting these reviews returned to you. Your article has been reviewed by 2 peer reviewers, including Philip Boonstra as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Fei Jiang (Reviewer #2).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Specifically, as the reviewers note, the proposed approach does not adequately address the limitations of the existing family of fragility indices and therefore seems to suffer from the same limitations as the methods it is intended to improve upon, and the improvement over the fragility index is neither characterized or quantified.

Reviewer #1 (Recommendations for the authors):

This article extends the concept of the fragility index for clinical trials using geometric arguments. The proposed approach is a two-step calculation. First, the two-dimensional ellipsis that contains the insignificance region is calculated, where each dimension represents one of the two arms in the trial. Then, the shortest vector between the trial's actual result and this ellipsis is identified. Shorter-length vectors point to greater fragility in the findings.

The idea of the fragility index is to measure how many subjects' outcomes would need to be changed in order to change the qualitative conclusion of a trial. The author raises several challenges to the fragility index: a lack of feasibility for time-to-event outcomes, a lack of clear distinction between 'robust' versus 'fragile', the need to calculate Fisher's exact test multiple times, and, in some cases, an inability to deal with fragility in both treatment arms at the same time.

Unfortunately, the proposed idea, although mathematically very intriguing, does not ultimately address these stated deficiencies, which limits its utility. Specifically, there is no solution proposed for the issue of time-to-event outcomes; there is no resolution to the issue of distinguishing between robust and fragile; and the perceived computational burden of calculating multiple Fisher's exact tests is actually not particularly great given the computational power of today's personal computers. Thus, the primary contribution of this article – from this reviewer's perspective – is with regard to the ability to generalize the fragility index to considering changes in both arms simultaneously.

Separately – I wonder if it would be more appropriate to define an irregular polygon of insignificance, defined as the largest polygon that is encompassed by the EOI and is comprised of connected segments of integer valued (x,y) coordinates. My thinking here is that since it is impossible to have continuously valued counts of responses, one should only consider integer-valued (x,y) coordinates as possibilities.

It may also be worthwhile to compare and contrast the difference in assumptions and approximations between Fisher's exact test and a chi-squared analysis.

1. The chosen acronym (FECKUP) is very similar-sounding and similar-looking to an English-language vulgarity. I wonder if the author might consider a different choice of acronym for their index.

2. The definitions of Qe, Qc, and Qa in Inequalities (11), (12), and (13), respectively, are somewhat unclear. Since these are inequalities, the mathematical implication is that Qe, Qc, and Qa can be any values less than their upper bounds, as in rows 4 and 5 of Table, whereas they are presented as single values in Table 3. I think the intent is to define Qe, Qc, and Qa as being equal to these upper bounds and to then claim that these are 'best case' scenarios for these different error types. Can the author please clarify/change how precisely to interpret Qe, Qc, and Qa and potentially consider changing these expressions in the manuscript?

Reviewer #2 (Recommendations for the authors):

This paper provides a potentially useful tool for conducting reproducible research with binary endpoints. The work provides steps to construct evaluation criteria of how sensitive a scientific conclusion regarding the changes of the observations. Overall, the study problem is important, but the proposed methods are not fully evaluated against the existing approach to justify the superiority of the method.

Strengths:

The derivation of the measurement is comprehensive.

Two case studies are interesting

Weaknesses:

No comparison with the existing method.

The author claim that the method is computationally inexpensive, but did not report the computational time for the proposed method and the existing method.

It is not clear what the improvement the proposed method made upon the existing method.

Impact:

The new tool can be useful for conducting reproducible research if the methods have been validated more rigorously.

Suggestions:

1, The paper will benefit from adding some simulation studies to justify the superiority of the method.

2, The author should be more precise about their terminologies. For example, what does "minimal error", "maximal proportion error" refer to? Also (11), (12), and (13) only provide upper bound of Qe, Qc, Qa, not their exact values. It is not clear why Qa reported in Table 2 has an exact solution. Please clarify.

3, The authors must compare with existing methods in real data examples.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The Ellipse of Insignificance, a refined fragility index for ascertaining robustness of results in dichotomous outcome trials" for further consideration by eLife. Your revised article has been evaluated by Mone Zaidi (Senior Editor) and a Reviewing Editor. Thanks also for your patience in getting this review back to you.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

Reviewer #1 (Recommendations for the authors):

Thanks to the author for their revised submission. Now that I have a better understanding of the approach, I do unfortunately have some additional questions, not all of which were raised in my initial review.

1. I am confused by the difference in definition between x_i vs x_m and y_i vs y_m. The legend in Figure 2 states that the green line depicts x_i, whereas the caption in Figure 2 caption states that the green line depicts x_m. Similarly, Table 1 also implies that x_m is the green line by virtue of stating that it is equal to 6.9. In fact, x_i is not explicitly defined in the manuscript as far as I can tell, but based upon the paragraph before equation (11), I believe it is interpreted as 'the number of subjects in the experimental group with a recorded positive endpoint who would need to be reclassified to negative in order for the study to lose statistical significance at the given significance threshold, holding fixed all measurements in the control group'. And y_i would be defined analogously. I think these are more or less the classic FI metrics. And therefore, I believe that the green line in Figure 2 is x_i, not x_m. In contrast, x_m and y_m must take into account some external knowledge/assumptions about the sensitivity and specificity of the measurement process; these values cannot be learned from the data itself. The sentence just before equations (14) and (15) states that x_m and y_m are the 'minimum miscoded cases', but I believe they are more appropriately defined as an 'anticipated number of miscoded cases given presumed values of specificity and sensitivity' (in particular, I would argue that they should be written as functions of se and sp: xm(se, sp)). If my understanding about this is all correct, I do not believe these definitions are adequately communicated in the manuscript and sometimes contradictorily used (e.g. in the caption of Figure 2). I would suggest, for example, that in the illustrative example on the bottom of page 4, it is clearly stated what x_i and y_i are, what the presumed values of se and sp are, and therefore what the presumed values of x_m and y_m are (as a related aside: how is the reader supposed to know that it is demonstrable fact that at least 9 patients had been miscoded? Is this discussed in the reference?).

2. Thanks to the author for clarifying the definitions of Qe, Qc, and Qa (now defined as epsilon_E, etc). I especially appreciate the added sentence between equations (11) and (12) that interpret it for a non-statistical audience. However, I see that the Methods section has been moved after the Results and Discussion section. I am not strictly opposed to this decision; however, the result is that readers who read through the manuscript as it is written will see these novel technical terms used prior to their definitions. I suggest that the author either return to the ordering of sections that is more traditionally used for statistical articles and which was used in the original submission (Introduction, Methods, Results, Discussion) or add references to defining equations for any novel technical terms used at their first use and a simple, non-statistical interpretation.

3. If the definitions /distinctions between x_i and x_m can be cleared up as per my first comment above, are the epsilons really necessary at all? Put differently, can the author please clarify why these statistics offer distinct information? Epsilon_A would seem to be just a rescaling of x_i by the sample size.

4. Figure 4: I suggest to add a parenthetical that the FECKUP vector is in red. A legend such as what is used in Figure 2 would be helpful.

5. Also, in the spirit of creating Figures that 'stand alone', can the caption of Figure 4 be modified to make clear which illustrative example it refers to? The only evidence that Figure 4 refers to the hypothetical liquid biopsy data is the use of the term 'city A' in the second sentence of the caption.

6. Figure 2 is not referenced anywhere in the text of the manuscript (as far as I can tell).

7. Can the author please add some sort of enumerative label or title to each of the illustrative examples and ensure that tables and figures make clear in their captions which illustrative example they refer to?

8. The third paragraph of the discussion says the method is 'only currently applicable to dichotomous outcome trials' but, assuming that the word 'trial' refers to an active intervention, I believe the author intends that this approach is more widely applicable to any study (that is, both interventional and observational) with a non-censored dichotomous endpoint.

9. I am still unclear on the need for the inequality in (13): does this inequality give a definition of epsilon_a, i.e. is epsilon_a really the entire set of numbers less than the RHS of this inequality? If so, why is epsilon_a only ever given as a single number and not an interval?

10. Figure 4: presuming this Figure refers to the cancer screening example, the units of analysis here are more appropriately referred to as 'subjects' not 'patients'. This comment applies more broadly, i.e. the second paragraph of the discussion.

11. The statement immediately following (15): "If xm >= xi or ym >= yi or both conditions are met…". Should there be absolute values around these expressions? For example, if xi < 0 and xm=0, then the sentence as currently written suggests that the results are not robust, which seems misleading. I believe the intended meaning here is "If |xm| >= |xi| or |ym| >= |yi| or both conditions are met…".
