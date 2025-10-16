# Peer review - Round 1

Editors:
- Wenying Shou, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70694.sa0](https://doi.org/10.7554/eLife.70694.sa0)

In this article, authors propose a novel hypothesis that can help explain why microbes release metabolites. In their NAC (noise-averaging cooperation) hypothesis, within-population cross-feeding can arise due to noisy metabolism in microbes. The authors predict substantial noise-driven growth inefficiencies from single-cell protein abundance data, review evidence for NAC, and propose how to detect NAC in microbial populations.


---

# Peer review - Round 1

Editors:
- Wenying Shou, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70694.sa1](https://doi.org/10.7554/eLife.70694.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Noisy metabolism can drive the evolution of microbial cross-feeding" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Naama Barkai as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewers overall liked this article. Reviewers want to see the evolution of noise-averaging cooperation (NAC), and the evolutionary stability of NAC against cheaters. To help revision, all reviews are attached.

Reviewer #2 (Recommendations for the authors):

1. As authors already have discussed, they have shown the optimality of metabolite sharing, not the evolution of cross-feeding. I agree that the authors nicely discussed what scenario could be feasible to evolve cross-feeding from the metabolite sharing. But still, two steps are not explicitly shown: (1) evolutionary stability of sharing metabolites (2) evolution from metabolic sharing to cross-feeding by gene deletion. I do not insist that the authors should examine them, but the current title "Noisy metabolism can drive the evolution of microbial cross-feeding" is misleading. So, it should be revised.

Because of the mismatch between the title and the model, I was confused about what cross-feeding really means. I admit that cross-feeding can happen within a single species, but the model considers identical individuals. It makes me confused that the authors consider metabolite sharing between identical individuals as cross-feeding.

2. Also, the model strongly depends on the bursty behavior of enzyme production, which makes me difficult to find which noise (or stochasticity) is necessary for NAC (or what is a fundamental mechanism of it). It seems that deterministic dynamics with bursty behavior starting from different enzyme concentrations give similar results. If the enzyme production feedback is less frequent, the gap between metabolite concentrations will increase. That induces a lower growth rate. In this case, metabolite sharing will also be optimal.

In the end, I realized that the noise in metabolite concentrations should play a fundamental role not one in the dynamics. But still, I am not sure about the fundamental mechanism, "noise" or "imbalance" of metabolite concentrations. I think the imbalance induces a lower growth rate with a smaller population size leading to a larger CV. Hence, to me, imbalance seems to be the more fundamental reason why metabolite sharing becomes optimal.

3. As I am not an expert in the Black Queen Hypothesis (BQH), it was unclear which question the authors aim to answer in the introduction either the generalization of BQH or the origin of the leakage. At the end of the reading, I found that the authors have asked the latter one. I think this confusion arises because I have no enough background in BQH. Thus, adding an explanation of BQH would help the audience to understand what the main question is.

4. I found that the initial enzyme concentrations are missing in the main text. I guess that the same initial concentrations of all enzymes are used for Figure 1C and 1D, but the authors should mention the initial conditions in the main text. Also, I wonder whether the results are robust under different initial conditions such that the different enzymes have different concentrations.

5. In lines 237~238, the term "curse of dimensionality" is often used in computer science. When the volume of the space increases so fast as the dimensionality increases, the available data becomes sparse. Thus one cannot find the statistical significance. However, in the main text, the authors have used this terminology to emphasize the situation where a large number of metabolites suppress the growth rate. I think the "curse of dimensionality" is inappropriate to be used in this situation.

6. The authors said that the correlated enzyme levels suggest the correlated metabolite levels (lines 248-251). However, in Appendix7 -Figure1, only the correlation between enzyme concentrations is shown without the correlation for the metabolites. It would be nice to verify this assumption by showing the correlation between metabolite concentrations in simulations.

7. As authors explained in lines 253-256, the correlation between metabolites could make their concentrations even but it is not always so. When each concentration has different average values, one can have an outlying low metabolite level even with a positive correlation. It is because the correlation does not tell the metabolite level itself. I think the results in Figure 3D are obtained at the same fixed average metabolite concentrations. If so, please clarify this.

8. In Equation (3) and (4), noise strength is not given in the main text.

9. Typo in line 53: that -> that

Reviewer #3 (Recommendations for the authors):

I enjoyed reading the manuscript: the NAC framework is an interesting new take on the evolution of cross-feeding and the manuscript is well written and organized. However, I have some suggestions for improving the presentation of the model.

1. The relation between NAC and BQH should be rephrased in more neutral terms (see public review).

2. It would be important to also mention the economies of scale hypothesis on cross-feeding evolution (see public review). I suggest briefly mentioning it in the intro and discussing how it relates to NAC in more detail in the discussion. Much of this work has been done in the context of amino-acid cross-feeding (see work by Christian Kost) and this would, e.g., be an appropriate place to discuss this.

3. In the absence of an evolutionary model, I think it is essential to phrase any statements about evolutionary dynamics more carefully and make clear to the reader that additional work is needed to confirm these hypotheses (see public review).

4. As mentioned in the public review I think some of the model assumptions have debatable biological rationale. It would be important to justify why these assumptions were made and to discuss how they affect the main conclusions. Additional simulations to explore the sensitivity of the model to these assumptions could be helpful, but are not necessary, provided that the authors can give an intuitive understanding of how these assumptions affect their conclusions.

5. In lines 142-144 and 185-186 the authors talk about the role of extracellular volume/cell density; however, no explanation is given of how these results were derived. I think these statements need to be supported by either a SI figure or by an intuitive explanation of how rv impacts model predictions.

6. In the analytical analysis presented in lines 187-205 the authors make use of various additional simplifying assumptions. Without additional details it is very hard to judge to what extend they affect the presented results. I think some additional discussion on the rational/effect of these assumptions would be highly beneficial to the reader (alternatively one could add a SI figure to e.g. compare the predictions of Equation 5 with data from simulations).
