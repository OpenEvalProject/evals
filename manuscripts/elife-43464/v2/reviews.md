# Peer review - Round 1

Editors:
- Thomas E Nichols, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43464.015](https://doi.org/10.7554/eLife.43464.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Empirical examination of the replicability of associations between brain structure and psychological variables" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The work considers the reliability of behavioural correlations with brain structure, within a mass univariate linear modelling approach using Voxel Based Morphometry data. Using 446 healthy subjects and 371 patients, repeated subsamples are drawn and analysed to create maps of consistency of detected clusters in a whole-brain approach, and then a ROI approach is also used on matched "discovery" and matched "test" samples. 30 behavioural variables were evaluated, in addition to age and BMI used as high-power benchmark measures. The reproducibility of the brain-behavioural correlations was found to be very poor, with little overlap between discovery and test clusters. Reproducibility based solely on the sign of the correlation and (to a lesser extent) Bayes Factors showed better consistency, suggesting the presence of true effect but with very low detection power.

Although some other work on this topic has been carried out, the current study takes a rigorous approach, by assessing various aspects of replicability of SBB studies in different ways. Highlights of the study include:

- the use of two large, independent, samples (one with clinical subjects)

- assessing both the replicability of whole brain exploratory SBB associations, and that of an ROI-based confirmatory approach

- the use of two reference phenotypical measures (age and BMI) that serve as benchmark for replicability

- investigation of the effect of (discovery/test) sample size on replicability

Essential revisions:

There needs to be greater motivation for the particular analytic strategy taken in the paper. While the Introduction nicely covers the history of replicability in imaging and SSBs, and then describes all the analysis that is going to be done, there is a need for more motivation: Why all these analysis are done. What is the benefit in doing 30-70, 50-50 and 70-30 setups? Analysing spatial overlap? Why should we have direction testing, sign testing, and Bayes' testing? What are the scientific questions that will be answered by these questions? How has previous literature lead us to answer these questions. These concerns can be highlighted with a bit of reorganizing the Introduction. Ideally, each analysis decision in the Results should be set up by a few sentences in the Introduction as to why it is necessary to see the results of such step. While carefully described, the motivation of the very lenient replicability measure "by sign" should be amplified (at first glance, one wonders what could be the added value is since one may expect an enormous amount of correlation coefficients of about zero, carrying hardly any information regarding replicability).

The Discussion is missing a well-identified limitations section. For example, while sample sizes of the current study are relatively large (and maybe large as compared to most published works in this area), the conclusions about poor replicability are limited to these sample sizes; e.g. if you had used the Human Connectome Project or larger samples, you would have potentially discovered the N where reliability 'kicks in' for more of the behavioral measures. Another limitation might be the fact that only one implementation is used: cluster-based analysis, whereas not all studies employ this approach. Moreover, the results (and conclusions) are also limited with respect to parameter settings, such as smoothing kernel width and the use of modulated gray matter segments (instead of, e.g. surface based analyses).

The role of multivariate statistical methods, which are growing in use, was mentioned only in passing in the Discussion. Please make a note already in the Introduction about multivariate side-by-side with the mass-univariate approach and how they have different replicability properties, emphasising that this work focusses on the mass-univariate approach. In the Discussion, the recommendation comes off as a gap in the paper. While the reviewers agree that enough analysis has been done, the phrasing of the multivariate discussion (subsection “Poor spatial overlap of SBB across resampling: possible causes and recommendations”, last paragraph) could be reorganized so that the reader is not left with the question "Why weren't these extra interesting ideas tried out?" Perhaps suggestions can be given as to how those hypotheses/recommendations could be tested in the future.

In the Discussion a clear discussion on sample size and power vis-à-vis correlation is needed. For example, at first blush the sample sizes in this study and in the discipline are simply too small. For example, note that in the UK Biobank the strongest correlation between cognition and T1 was found to be r=0.10 https://www.nature.com/articles/nn.4393/figures/6, Figure 6B), indicating a need for about N=800 subjects to attain 80% power at 0.05 uncorrected. Does your analysis indicate a minimum r that is needed for the sample sizes considered?
