# Peer review - Round 1

Editors:
- Y M Dennis Lo, The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64716.sa1](https://doi.org/10.7554/eLife.64716.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work represents a thought-provoking and timely exploration of the impact of polygenic embryo screening using a liability threshold model. This work is expected to catalyse further debates in this emerging field.

Decision letter after peer review:

Thank you for submitting your article "Utility of polygenic embryo screening for disease depends on the selection strategy" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Mone Zaidi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Qiongshi Lu (Reviewer #3).

Summary:

Polygenic embryo screening is a controversial topic. Due to generally low predictive accuracy of current polygenic risk scores (PRS), the entanglement of genetics's and environment's roles in disease etiology, and a lack of empirical studies, our understanding of potential benefits, and importantly, risks of PRS-based human embryo screening is qualitative at best and far from complete. In this study, Lencz et al. provide a statistical framework to assess the effectiveness of various screening strategies to reduce disease risk. Overall, due to some limitations in the study, the current results do not necessarily endorse practicing human embryo screening using PRS. Instead, the major contribution of this study is to layout the quantitative arguments and metrics which future studies may continue to use. These tools are crucial for researchers to understand the risk/benefit trade-off and to design better strategies. This work is thought-provoking and should open up useful debates in the field.

Major comments:

1. The main conclusions seem to contradict the same group's previous work (Karavani et al., 2019) which argued that screening embryos with PRS has limited utility. The key difference between this paper and the previous study is that here the focus is binary disease outcomes while the previous study focused on quantitative traits. However, the distinction between quantitative traits and their dichotomized counterparts is not always clear (e.g., cholesterol levels and hypercholesterolemia, education years and college attainment), which seems to suggest that the assessment of a screening strategy strongly depends on how the phenotype of interest is defined. Do the conclusions in (Karavani et al., 2019) still hold given the findings of this paper? Would it be fair to say that (i) given all assumptions made in this paper such as a lack of genetic nurture effects and rare variant effects, and (ii) if the interest is to prevent intellectual disability which is a dichotomized version of IQ, a trait extensively studied in Karavani et al. 2019, then polygenic embryo screening may NOT have limited utility as long as the low-risk prioritization approach is used? More extensive discussions are needed to compare the approaches and conclusions between the two closely related papers.

2. It appears to be counter-intuitive that the curves of the "high-risk exclusion" strategy would peak instead of being monotone (e.g. the upper-left panel in figure 2). If the exclusion percentile (i.e., x-axis) keeps increasing, shouldn't this approach behave similarly compared to the "low-risk prioritization" strategy? One would think that a stringent percentile threshold in "high-risk exclusion" (excluding most embryos) would ensure that only embryos with very low risks are planted, which is what the "low-risk prioritization" strategy tries to achieve. So why doesn't the purple curve in that upper-left panel keep going up until reaching ~80% which is suggested by the lower-left panel in Figure 2?

3. The authors should comment on the following points. First, partitioning the PRS "si" into two orthogonal components: polygenic transmission disequilibrium "xi" and parental average score "c" seems intuitive. However, shouldn't parental genotypes predict the distribution of xi? Suppose both parents are homozygous at a SNP and c = (2+2)/2 = 2. Then, si would be 2 without any variability, which means xi is always 0. Even in a polygenic setting, a very high value of c would suggest higher homozygosity which should lead to lower variance of xi. However, the setting in this paper leads to a constant variance of xi which isn't affected by c. Is something missing here?

4. The authors state that they have not explored the age dependence on the number of embryos? How significant would this omission be? What is the age distribution of parents who would typically undertake such polygenic embryo selection?

5. For the high risk exclusion strategy, the authors state that if all embryos are of high risk, then a random embryo would be implanted. Would a decision of not implanting any embryo be a reasonable alternative? If this is indeed a reasonable alternative, would this change the authors' conclusion in any way?

6. The authors should clarify the impact of error in the per-embryo estimation of xs (e.g. from errors in imputation of genotypes if that's used or errors in the β_hat estimates that form the PRS)? I assume in these cases it results in an effective lowering of rps2?7. While the statistical framework in this paper can be used to compare the utility of different strategies, the same analyses can also quantify the potential risks of embryo screening. Although the authors were open about the limitations of the study, no empirical analyses were performed to demonstrate potential risks. This is a missed opportunity. Can the authors expand this somewhat?

8. While it is understandable to make some simplifying assumptions, it is critical to demonstrate the risk which is a main concern of human embryo screening in the field. While it does not appear that the authors have over-stated anything in the original submission, given the sensitivity of this topic, avoiding quantitative discussions on risks may lead to over-optimistic news headlines that only focus on the potential utility and even reckless and potentially harmful practices. With that said, it seems straightforward to generalize the simulation framework in this paper to explore a two-trait setting. Suppose two diseases are genetically correlated (with correlation = -0.1, -0.3, and -0.5, for example). Then, would the "low-risk prioritization approach" on one disease lead to drastically increased risks for the second disease? It wouldn't be fair to ask the authors to find a solution to this problem given the scope of the study. But a quantitative demonstration of risks will improve this paper.

9. What is the current success rate if only one embryo is planted? If multiple embryos (out of 5) are planted to ensure a reasonable success rate in current practices, would it be fair to say that only a "high-risk exclusion"-type strategy that only excludes embryos with higher risk is realistic? Here, the exclusion criterion isn't necessarily based on a population quantile but could be based on PRS ranking among embryos. Some discussions will be helpful.

10. The authors state that one concern about the generalisability of polygenic embryo selection is the extension to non-European populations. Outside of the European populations, is it true that none of the other ethnic groups have high quality polygenic risk score data?

11. The usage of an extended listing of assumptions deep in the Material and Methods was slightly unorthodox to me and I wonder if it would be more transparent and useful for the average reader's consumptions to include these in the discussion itself. While the presented results are helpful, it's important that stakeholders digesting these numbers understand how many unknowns there are to still understand in this area.

12. Beyond the average risk reduction, would it be helpful to understand the variance in outcomes, e.g., which strategies have high variance in outcome? Can the authors speak to that dimension even qualitatively?

13. Perhaps one set of simulations with a finite and varying number of loci would be useful to guide intuition on when the infinitesimal model is appropriate. From experiences in other examples, the infinitesimal can already provide useful predictions for what might at first seem like small numbers of loci and if that holds in this case it might be useful for readers to understand who might otherwise be too quickly dismissive.

14. For clarity, please use a different variable besides in 'e' in sections where 'e' includes environment plus unmeasured genetic effects. Perhaps 'u' for "un-measured" effects?

15. Equation 16, ei* was not explicitly defined, even if it's inferable from context it would be nice to define.
