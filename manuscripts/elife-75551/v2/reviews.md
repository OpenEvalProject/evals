# Peer review - Round 1

Editors:
- Alexander Young, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75551.sa0](https://doi.org/10.7554/eLife.75551.sa0)

Lu et al. provide a powerful statistical method that measures excess sharing of de novo mutations between pairs of disorders. This method extends the concept of 'genetic correlation' to disorders caused by de-novo mutations, measuring the correlation in excess de-novo mutations in genome-wide genes for different classes of mutations. The authors apply the method to nine disorders including a developmental disorder, autism spectrum disorder, congenital heart disease, schizophrenia, and intellectual disability, finding a statistically significant overlap between 12 pairs of disorders in de novo mutations that cause a loss of gene function. This method will be of interest to researchers working on disorders caused by de-novo mutations.


---

# Peer review - Round 1

Editors:
- Alexander Young, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75551.sa1](https://doi.org/10.7554/eLife.75551.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Quantifying concordant genetic effects of de novo mutations on multiple disorders" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The manuscript needs to explain better the different approaches taken by encoreDNM and mTADA, and the corresponding strengths and weaknesses. The authors focus on power in frequentist hypothesis testing for non-zero genetic overlap between disorders, but mTADA takes a Bayesian approach. Clarification is needed here on whether the statistical basis of the comparison is fair.

2) Greater clarification of the model fitting procedure is needed: how the de-novo mutability parameter is used and the computational complexity of optimizing the likelihood function.

3) The heatmaps that present the results of the empirical analysis show only statistical significance levels. Since the authors' method's primary parameter is the correlation parameter, it would be helpful to display estimates of this parameter in the main text and to focus discussion on that parameter more and on statistical significance less.

Reviewer #1 (Recommendations for the authors):

Here, I have the following comments.

1. Authors proposed a mixed-effect Poisson model with overdispersion. I have a few questions regarding this model. First, it is not clear whether the de novo mutability m_i is a parameter or a given estimation in the model. Authors mentioned on line 110 that the background component is a gene-specific fixed effect but in the Methods they do not treat it as a parameter in the section of parameter estimation. Second, to treat overdispersion in Poisson model, negative binomial distribution is usually applied. Here, authors added an overdispersion variable \phi_i in the model. It will be helpful to discuss on this point. Third, a MCMC algorithm was used to solve the EncoreDNM model. How is the computational efficiency? On line 431, authors used the inversion of Fisher information matrix to obtain the covariance for parameters. Is there any non-invertibility problem here?

2. In the data analysis, authors used Figure 4c-f to suggest better fit of mixed-effect model. It is better to use a table to summarize the goodness of fit test instead of using bar plots in Supplementary Figure 3. On line 197, before reading the whole paragraph, it is not clear at the beginning whether single-trait analysis refers to mixed-effect or fixed-effect. Next, authors discovered that no significant correlation as identified between any disorders and control groups. Discussions about this should be helpful.

3. In Figure 5, panel b and c can be simplified with upper triangle for LoF and lower triangle for synoymous. Moreover, the heatmaps here only reflect the significance of correlations but no information regarding the correlation magnitude itself. It would be helpful to include this in the same figure. This point could be applied to other heatmaps in the supplement. In addition, Figure 5b shows more significant correlations for diseases with larger sample sizes. This is consistent with common sense. So including correlation magnitudes in this figure would be more informative.

Reviewer #2 (Recommendations for the authors):

1. I felt the introduction and discussion lacked a more in-depth comparison between EncoreDNM and other similar methods (specifically mTADA). In particular, what are the differences in parameters between these two methods and why do you see such an increase in false positives (Figure 3) for mTADA over EncoreDNM?

2. L66: The technical wording of this statement could be improved. The paper cited was commenting on remaining haplo-insufficient genes yet to be discovered. I also do not believe "undetected" to be the correct word here as this refers to a statistical test for enrichment rather than a clinical association. There are several genes (e.g. in Kaplanis et al. Supp Table 2) that are known to cause developmental disorders clinically but do not pass p. value thresholds suggesting a statistical enrichment in studies like DDD.

3. In Figure 1, is there a vertical line missing? On the left, there are squares representing genes, but there is also one rectangle.

4. L103-117: Could the derivation of the dispersion parameter Φ be explained in better lay-terms somewhere? I understand that it is attempting to quantify the random nature of DNM counts one expects when sequencing a subset of individuals with a given disorder, but the maths in the methods section is a bit impenetrable for somebody who is not well-versed in calculus. This is especially crucial considering the major role it plays in interpreting the various results presented, and in comparison, to mTADA. It will be difficult for some readers of a journal with a broad range of topics such as eLife to understand how this parameter, particularly σ, was estimated.

5. L108: Further to point 4, what are reasonable values of the parameters used to fit your model? Additionally, the authors state that β "tends to be larger… and smaller…" under various conditions, but based on Figure 3, it appears that it shifts between positive and negative?

6. L151: The word "could estimate" is loaded and represents an opinion and should be removed in favour of "estimates".

7. L184-187: The excessive use of acronyms for various disorders makes for difficult reading. While I am familiar with acronyms for developmental disorders, autism spectrum, and schizophrenia because these are my field, I constantly had to refer back to the definitions is it possible to just use the actual disorder names throughout the manuscript where possible?

8. Figure 3: I think it is relevant to put the various simulated parameters that constitute Φ (e.g. σ, ρ) into context with actual data as presented in Figure 4. i.e. do the simulated parameters used here represent reasonable assumptions of these values and are they within the expectations of mTADA? Could the range of parameters have an outsized effect on the differences between mTADA and EncoreDNM? Or does it have to do with p. value thresholding (see below). Furthermore, I would appreciate it if x-axis labels included the actual parameter setting rather than the less descriptive "small" and plots A and C had labels which described which parameters were fixed in those respective analyses.

9. L246: "i.e." should be removed. There are five genes and you listed all five.

10. L267-272: Are the authors certain the thresholding on the mTADA results is reasonable? Whilst the FDR cutoff the authors have applied may suggest "significance", the p. values for the mTADA synonymous variant analysis seem very similar across all disorder combinations. Furthermore, the general pattern of p. values for LoFs seems similar to that shown for EncoreDNM. I suspect that the correlation between p. values of EncoreDNM and mTADA will be high and one could generate similar results by adjusting significance thresholds independently for each tool.

Additionally, as mTADA is based on a Bayesian approach, shouldn't the authors threshold based on posterior probabilities rather than p. values? I am unsure if comparing the π values from the different mTADA results is a valid approach as described in the methods? How do the authors conclusions change when using thresholds based on those the authors of mTADA suggest (e.g. PP > 0.8)?

11. Figure 6: Could a visual cue/text be added to differentiate between the analyses in the upper and lower triangles?

12. What is the overall rank of genes identified between different disorders when comparing between mTADA and EncoreDNM? Could the authors plot relative p/PP values for genes identified to be significantly enriched between disorders?

13. L228-229: Do not use the terms "hints at correlation" or "correlate strongly". It either does or does not meet your p. value threshold and/or correlate.

14. L257-260: Are the recurrent LoF mutations found in developmental disorders any different than those already identified by Kaplanis et al.? If so, how do your results increase understanding of the mechanisms underlying developmental disorders? I would perhaps shift the focus of this section to identifying recurrent mutations across disorders (and perhaps cite/refer to Rees et al. in Nature Communications; PMID: 34504065).

15. L274-280: I do not feel the LD score analysis constitutes a new analysis and should be moved to the discussion. A similar result was recently published in by Abdellaoui and Verweij in Nature Human Behaviour (PMID: 33986517) that covers many of these traits.

16. Throughout: Could the term "Type I Error" be avoided? I would prefer false-discovery/false-positive be used as it is a much clearer term and immediately recognisable by the majority of readers.

17. L365-366: I do not think identifying gene-disease associations is a goal of EncoreDNM so I do not consider it a limitation of the study.

18. L584: I think the hyperlink is broken? I was able to find the repository for EncoreDNM in ghm17's github account, so this was not a major issue.
