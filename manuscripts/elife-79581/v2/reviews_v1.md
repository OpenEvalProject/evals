# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79581.sa0](https://doi.org/10.7554/eLife.79581.sa0)

This paper describes the development and validation of an automatic approach that leverages machine vision and learning techniques to quantify dynamic facial expressions of emotion. The potential clinical and translational significance of this automated approach is then examined in a "proof-of-concept" follow-on study, which leveraged video recordings of depressed individuals watching humorous and sad video clips.


---

# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79581.sa1](https://doi.org/10.7554/eLife.79581.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Quantifying dynamic facial expressions under naturalistic conditions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Baker (Senior Editor).

The reviewers have discussed their critiques with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers highlighted several strengths of the report, noting that

– This is a well-written, very clear paper that outlines a novel procedure to assess a set of features that is very easy and cheap to collect within a clinical context.

– The methods are relatively straightforward (which is a good thing), and they are applied without flaws as far as I can tell.

Nevertheless, several limitations of the report somewhat dampened enthusiasm.

– A more complete and sober discussion of prior work. The Introduction seems to overstate the accuracy/reliability with which facial expressions can be automatically recognized. This should be addressed. It is also important to highlight differences between posed and spontaneous expressions and the challenge of domain transfer (cf. Cohn et al., 2019).

– Visual overview of pipeline. While (almost) every element of the pipeline is understandable in itself, it would be useful to integrate the different steps into a single figure or table. I see that the code in GitHub is clear in that regard, but it would be nice to give more visibility to the pipeline structure in the paper itself.

– Bootstrap rationale. It is not clear that 100 bootstrap resamples are sufficient. Please provide a rationale for this methodological choice.

– Analytic approach. Please provide a rationale for the decision to drop 1 of the 2 positive stimulus videos from the melancholic depression analysis. Given that the differences between groups appeared smaller in this video (at least what was shown in visualizations, dropping this video may make the difference between groups appear larger or more consistent than we have reason to believe it is given the entire data).

– Machine learning approach. For the SVM described on page 24, please clarify whether the observations were assigned to folds by cluster (participant) or whether observations of the same participant could appear in both the training and testing sets on any given iteration. (The former is more rigorous.) Please also clarify whether the folds were stratified by class (as this has implications for the interpretation of the accuracy metric). The performance of the competing SVM models should be statistically compared using a mixed effects model (cf. Corani et al., 2017).

– More granular performance metrics. Given how much automated methods rely on AU estimates and how much of the interpretation is given in terms of AUs, it will be important to provide direct validity evidence for these estimates. Please report the per-AU accuracy of OpenFace in DISFA (as compared to the human coding). Please make it explicit in the revised report that OpenFace was trained on DISFA, so this reported accuracy is likely an overestimate of how it would do on truly new data, including the melancholic depression dataset featured here.

– A sober and complete accounting of key limitations. The fact that there is not validity evidence in the depression dataset should be indicated as a limitation to be addressed in future studies. Likewise, the modest sample size and related generalizability concerns should be noted as limitations.

– Significance/Path from Bench to Bedside. The manuscript should be revised to clarify the path to clinical translation, if that's the aim. So, how could this pipeline be actually applied in practice? Would a doctor be able to make an effective use of it? Is it intended as a first (cheap and automatised) step in a diagnostic procedure?

References

Cohn, J. F., Ertugrul, I. O., Chu, W.-S., Girard, J. M., & Hammal, Z. (2019). Affective facial computing: Generalizability across domains. In X. Alameda-Pineda, E. Ricci, & N. Sebe (Eds.), Multimodal behavior analysis in the wild: Advances and challenges (pp. 407-441). Academic Press.

Corani, G., Benavoli, A., Demšar, J., Mangili, F., & Zaffalon, M. (2017). Statistical comparison of classifiers through Bayesian hierarchical modelling. Machine Learning, 106(11), 1817-1837. https://doi.org/10/gb4tr9
