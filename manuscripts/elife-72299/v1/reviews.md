# Peer review - Round 1

Editors:
- Armita Nourmohammad, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72299.sa0](https://doi.org/10.7554/eLife.72299.sa0)

This manuscript presents a general statistical framework to infer selection on a quantitative trait, based on measurements of the values of this trait along related cell lineages. The manuscript provides both a detailed explanation of the mathematical underpinnings of the method and an illustration of its application to existing and new cell lineage datasets. This is a general framework and is not tailored to particular growth models or environmental conditions, making it applicable to broad examples of exponentially growing populations.


---

# Peer review - Round 1

Editors:
- Armita Nourmohammad, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72299.sa1](https://doi.org/10.7554/eLife.72299.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A unified framework for measuring selection on cellular lineages and traits" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Srividya Iyer-Biswas (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors should restructure the paper so it is accessible to the broad audience of eLife. The main issues to keep in mind:

i. Better clarify of the biological questions that the approach can address and the biological insights that it can provide. Tangible connections to specific biological systems would strength the work.

ii. Better structure the results and present the main points in an accessible language to those not interested in the mathematical intricacies.

2. Better clarify the definitions and measures used for fitness, selection, evolutionary advantages, etc in the paper and contrast them with the common notion of fitness as the instantaneous growth. See the comments regarding the definitions of selection strength by reviewers #1 and #2.

3. Discuss the impact of inherent stochasticity in division events on the results and the outcome of lineage evolution.

4. Discuss how the mathematical formalism and results acquired for the stationary state can be applied (or modified) to address non-stationary conditions that are more relevant for the processes discussed in the manuscript. See comment 3 by reviewer #3.

The reviews below contain a number of other suggestions that we encourage you to consider.

Reviewer #1 (Recommendations for the authors):

– In the Introduction it is mentioned that « cell population's growth rate becomes greater than the mean division rate ». Can the formalism presented here describe this in a simple way?

– It could be useful for a broader audience to explicitly explain how skewness and cumulants are related.

– It could be good to define W1 and W2 in the theoretical background section.

– Figure 7: I recommend to explicitly tell what x is.

– How do definitions depend on the discrete or continuous nature of x? Practically, do we need to, say in Figure 7, bin x to compute different functions? How is this done?

Reviewer #2 (Recommendations for the authors):

The main concepts were previously proposed and published by the same authors (ref 13). The new clarification and applications are welcome but the scope of their novelty and impact is not totally obvious. Currently, the paper tends to read as a technical paper with new observations that are intriguing but not totally understood (e.g. the difference between stationary and non-stationary growth). It would benefit from a clarification of the biological questions that the approach can address and the biological insights that it can provide.

Selection is most commonly thought to act on traits and, in constant environments, quantified by the instantaneous growth. This quantity is often identified to fitness with a straightforward relation to adaptation at the population level. The reduction of fitness variance that the authors mention (in the abstract and line 260) is derived in this context. The paper takes a different perspective and it would be helpful to contrast it more clearly to this more usual approach: Why and when is it justified to define selection at the level of lineage trait? Why should we be interested in multiple definitions of selection strength in this context? What can we expect to learn?

Further explaining the questions that the formalism intend to address is needed or the paper may appear as a formal exercise to solve a problem that the authors artificially created, i.e. introducing multiple measures of selection strength on an unusual quantity. Further explaining the biological insights that the framework can provide is also needed if the intent is to reach readers interested in applications and not only mathematical technicalities.

Some questions along those lines:

Why multiple definitions of selection strength? Is it just a matter of quantifying the difference between Q_{rs}(x) and Q_{cl}(x) which cannot be reduced to a scalar quantity? What information is in principle contained in the difference? What is the biological interpretation of the observation that it can be reduced to 2 numbers in many cases (when higher order cumulant are negligible)?

In applications, it appears that interpretable conclusions are mainly drawn from two quantities: S_KL(D) for global selection and S_rel(X) for selection of a specific trait. In the current understanding of the approach, are these the quantities that one should compute to reach biological insights in practical applications?

Can we use the approach to rule out that a trait is under selection? If so, what would be the statistical evidence?

How critical is the formalism: can the authors derive a biological conclusion that would not be accessible without it?

The application of the method to non time-invariant conditions (regrowth, changing environments) is not completely clear. The results should depend on the time-window and important information pertaining to selection should be contained in the time evolution. The observation that empirical observation that S_KL2 differs from S_KL1 in this context is intriguing but its origins and implications unclear.

The authors stress that their model is independent from mechanisms, which makes it broadly applicable. But only correlations can be assessed which may limit the identification what drives selection.

What is the relationship to adaptation and evolution? The abstract raises the question but no further mention of adaptation is made in the rest of the paper.

Heredity is generally as important as selection: is it within or beyond the scope of the framework?

Reviewer #3 (Recommendations for the authors):

I recommend addressing the specific concerns raised through appropriate discussions and clarifications in the manuscript text.
