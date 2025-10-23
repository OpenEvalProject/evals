# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65645.sa1](https://doi.org/10.7554/eLife.65645.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper addresses the important question of multidrug resistance evolution, which is of both theoretical and applied interest. The authors' efforts to carefully distinguish population and metapopulation linkage disequilibrium and to develop a framework to rigorously analyze the relationship between the two represent an advance in our understanding of microbial population dynamics.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Understanding the evolution of multiple drug resistance in structured populations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Brian J Arnold (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

We have appended to this message a summary of the two reviewers' comments, including both major and minor concerns. Briefly, there were concerns about the extent of the claims made about the model explaining features of data, the clarity of the model development and notation, and links between the results and previous literature. Please see below for details.

Reviewer 1:

MDR is more common than expected by random chance, especially in particular bacterial species. Understanding how this linkage between resistance elements arises is important for public health but also for generally making sense of genomic data, e.g. classifying genomic patterns as outcomes of specific biological processes. Here, McLeod and Gandon show that spatial heterogeneity across subdivided populations can create LD between resistance elements, even in the absence of epistasis.

The novelty of this manuscript appears to be an extension of Day and Gandon, (2012) to a metapopulation model as well as comparing output of the model to a dataset on pneumococcus, which has sort of served as a model for the ecology and evolution of MDR. One particular result of interest was the observation of simulated transient LD even without epistasis. Though this particular observation is not necessarily new (Martin et al., 2006; Day and Gandon, 2012), casting this metapopulation model in an epidemiological framework appears to be new to my knowledge.

However, the intuition this model provides for Dtot > 0 at equilibrium is intriguing: variability in susceptibility density across populations can create covariance in selection coefficients for the two alleles, in turn creating correlations between subpopulation allele frequencies, driving Dtot > 0. This insight is extremely general and has nothing to do with the biology of a particular species.

While this isn't a major concern, I wanted to point out what I thought was confusing language that made it take longer for me to understand the results.

1) I found the number of ways to quantify LD a little confusing and done with ambiguous language. D is first used in it's standard form D = Pab – Pa*Pb (Equation 1), which made it confusing when I then encountered D within the definition of Dtot (Equation 5), where D is the weighted average of D = Pab – Pa*Pb for each of the subpopulations. I think it would be clearer if D perhaps consistently referred to a subpopulation, the average D across subpopulations were instead indicated with a summation in Equation 5.

Also with Equation 5, it took me a while to figure out what cov(pa, pb) actually referred to, as the definition "spatial covariance between resistance to drugs A and B", along with being primed by historical literature, made me think of this covariance as LD (i.e. how frequently alleles are found within the same genome). However, this is referring to covariance of *allele frequencies across subpopulations* and has nothing to do with whether or not they're found in the same genome. More specific/clear language will help readers distinguish between the different covariances studied here: between alleles across genomes (LD) and between allele frequencies across subpopulations (cov(pa, pb)).

2) Also, I'm left not knowing the ultimate conclusion of applying the model to the pneumococcal data. On line 226 you claim that transient dynamics and epistasis can explain patterns in pneumococcus, whereas on line 301 you claim that variation in SX across subpopulations can generate LD. Some short conclusion regarding these two claims would be useful.

Citations:

Day & Gandon, (2012). The evolutionary epidemiology of multilocus drug resistance. Evolution. https://doi.org/10.1111/j.1558-5646.2011.01533.x

Martin, Otto & Lenormand, (2006). Selection for recombination in structured populations. Genetics, 172(1), 593-609. https://doi.org/10.1534/genetics.104.039982

1) For the case of additive selection, you provide one particular example of parameters that give rise to transient positive LD (Figure 4), but it would seem that many situations would also give rise to negative LD. Is there a symmetry to the model such that if you were to "integrate" across all possible starting conditions, the expectation would be zero? Or is there an asymmetry that makes transient LD more likely to be positive? I assume the latter if you add epistasis, but it's unclear with additive selection. This would help map intuition from your model to results such as Figure 3, in which it seems there's a skew towards positive LD. Is epistasis absolutely needed to explain this skew?

2) One interesting implication of this work is what to expect when bacterial "populations" are either not defined at all or even incorrectly defined. Since Dtot is very positive under many scenarios (even with negative epistasis! Figure 4), you will observe an excess of positive LD between resistance elements (given these starting conditions in Figure 4, that is).

Reviewer 2:

This is an interesting and important topic and the paper promised to be a new take on it, from the point of view of dynamics of linkage disequilibrium.

My major concerns are (1) clarity of the mathematics, notation and model development and (2) with the claims that the model explains data, without a wide range of simulations or a direct comparison of model to data (for example see below re line 239 onwards).

The model in Equation (2) looks linear and the reader has to see figure 1 to note that there is actually a nonlinear term here (the susceptible * infectious term, and a product of two infectious terms) because the sA etc depend on the prevalence.

The model derivation is cumbersome and far from straightforward; I was unable to directly derive (3) from (2). Instead, for the first three terms of (3) I obtained

dpA/dt = (1-pA)(pA sA + pAB (sAB – sA – sB) ) + sB D

instead of the expression in the paper which is

(1-pA) (pA sA + sAB pAB) + sB D

This would seem to carry through to the other equations. However my derivation attempts were simply using sA, sAB, sB as given in the text, and putting in the rate of growth of the AB variant (r + sAB) as in (2) for example, without substituting in the expressions from Figure 1 for sA, sB, and sAB. This may work it out (?) However this left me a bit sceptical.

Bottom of page 4: if doubly-resistant infections are overrepresented in the population, DX > 0. < ----> middle page 5 "since DX > 0" Which is it?

Page 10: "…, drug B resistance is often more likely to occur in an infection with a genetic background resistant to drug A." -- more likely than what?

Line 239++ : This section makes the claim:

"Thus transient dynamics coupled with epistasis can explain the significant within-serotype LD observed in Streptococcus pneumoniae".

This is a big claim, based on a qualitative paragraph with no direct comparison to data, in which there is an underlying assumption of fixation of resistance to drug A in many serotypes. To my knowledge we often do not see fixation of resistance in Streptococcus pneumoniae or in the Maela data in particular, but rather long-term coexistence. I am not convinced that the dynamics of this model explain the significant LD in the data as claimed.

Equation (2) – there is a note above that rholX depends on infection densities; the nature of this dependence should be specified.

Page 12: why, if there is no mechanism maintaining within-population diversity, does this necessarily mean DX = 0 (line 282) ?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Understanding the evolution of multiple drug resistance in structured populations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sonja Lehtinen (Reviewer #1); Stephen M Kissler (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the reviewers of the previous version of your paper were not available to reconsider the revised manuscript, the reviewers of this version of the paper did take the previous comments and your responses into consideration when composing their own reviews.

Collectively we see much potential in your manuscript, but we request the following points to be addressed at minimum (see below reviews for further details and more suggestions):

1. Expanded explanation of the assumptions behind the LD framework. In particular:

a) Is epistasis necessarily defined in terms of an additive expectation on growth rate? (If this is a standard result in population genetics, a reference to an accessible explanation would be enough).

b) The s coefficients are dependent on variable densities – does this matter for the partitioning and interpretation of equations 3 and 4?

2. If the authors disagree with Reviewer 1's questions about the interpretation that variation in susceptible density explains the effect in example 1 and in Lehtinen et al., 2019, more explanation is needed for the following points:

a) Why variation in clearance rate affects selection for resistance when there is a multiplicative cost on clearance rate, but no cost on transmission rate (for the re-interpretation of Lehtinen specifically)?

b) What is happening in example 2, where the effect is currently explained in terms of serotype-specific susceptible density, but the model does not include serotype-specific susceptibles?

3. For examples 2 and 3, please either explain why additive transmission costs are reasonable (given the concerns highlighted below) or change the modeling of cost.

Reviewer #1 (Recommendations for the authors):

My major scientific recommendations are covered by my review. There are some additional less fundamental points that I am happy to share with the authors if they are interested but won't include here as this review is already quite long.

In terms of presentation, I thought everything was mostly very clear, with the exception of the section on serotype dynamics. Here it would be more helpful to make clear the shift from a structured susceptible population to a shared susceptible population.

Reviewer #2 (Recommendations for the authors):

I was asked to review this manuscript after it had already gone through a round of revisions. My comments reflect both my own initial reading of the manuscript and my assessment of the authors' responses to the previous reviews.

While I did not have access the authors' initial submission, it appears that the authors have sufficiently addressed the previous reviewers' comments.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Understanding the evolution of multiple drug resistance in structured populations" for further consideration by eLife. Your revised article has been evaluated by George Perry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed as outlined below in edited comments from Reviewer Sonja Lehtinen, as outlined in points 2-5 below. In addition, I have reviewed the discussion with the eLife editorial office about the article structure and have considered this question myself, ultimately coming to point 1.

1. Please do create a methods section for this paper. There is no need to remove anything from your current main text. Rather, in the new methods section please first overview the methods even if they are already described in more detail elsewhere in the paper (some repetition is ok, and I agree with the level of detail you have provided in the Results section, given the type of paper) in one or more subheadings, and then import all of the sub-headings and the full content of the appendix. Since we don't have page limitations and since this is important to the paper, I think it should be included in the methods section of the main text of the paper, rather than as an appendix.

2. The point the authors are making about density of susceptibles and that this point is not limited to additive costs is understood. However, the section on equilibrium patterns of MDR still should be updated because the difference between additive and multiplicative costs is not explicitly flagged in the main text. (I think the discussion in the Sup Mat is very helpful, but most readers will not read the Supplement). Specifically, when considering equilibrium patterns of MDR, the paragraph starting line 283 is only true for additive costs. Without reading the supplement, this paragraph comes across as a general result. If costs are multiplicative, variation in duration of carriage is both necessary (i.e. variation in transmission rate does not produce LD at equilibrium) and sufficient (explicit transmission costs are not needed). Thus, overall, it is true to say that variation in duration of carriage is not necessary, but not that it is not sufficient. It would be helpful to explicitly make this difference clear somewhere in this section. Please also rephrase the sentence lines 270-273 to avoid implying that the costs in Lehtinen et al., are additive.

3. The main text would benefit from a discussion of additive costs. Specifically:

a. The authors make a good point that cost parameters are subject to constraints however they are modelled. The reviewer's point was that these constraints are qualitatively different for additive transmission costs: reasonable additive costs for single resistance can lead to negative transmission rate for dual resistance (as in the example in my review) in the absence of cost epistasis. This suggests that for cost parameters where this is the case, assuming no epistasis cannot be appropriate. Although the specific parameter values the authors use don't give rise to this problem, the authors also present more general results for a model with additive costs and no epistasis, so it would be helpful to highlight this constraint somewhere.

b. The authors' careful consideration of how the specification of costs affects interpretation is indeed very useful and interesting. In addition to this conceptual point, the authors say that they are aiming to highlight mechanisms – e.g. variation in transmission rate – that could plausibly give rise to patterns of MDR. In the case of equilibrium patterns, variation in transmission rate only gives rise to LD when transmission costs are additive. The plausibility of variation in transmission rate as an explanation for equilibrium patterns of MDR therefore depends on the plausibility of additive transmission costs. Therefore, if the authors want to suggest that variation in transmission rate is a plausible explanation for patterns of MDR, it is necessary to include a discussion of whether/how additive transmission costs might arise.

4. Add "per carriage episode" to the summary of the biological interpretation of the duration of carriage effect in Lehtinen et al., 2017/2019 (lines 244-245), to make it clear that they were not suggesting that (host) populations with longer durations of pathogen carriage have greater antibiotic exposure. (This point was missed in the original review).

5. One final observation, which is not an essential revision and the authors should only address it if they think it will improve the paper. Points 2 and 3 are both related to the result that a model with a multiplicative transmission cost predicts, at equilibrium, LD between duration of carriage and resistance, but not transmission rate and resistance. Would the authors explain this in terms of variation in the density of susceptibles giving rise to the LD with duration of carriage, but this effect being offset by the epistatic interaction between transmission rate and cost of resistance leading to no LD between transmission rate and resistance? This might be interesting to explicitly discuss in the manuscript.
