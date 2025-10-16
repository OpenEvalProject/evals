# Peer review - Round 1

Editors:
- Mihaela D Iordanova, Concordia University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95802.3.sa0](https://doi.org/10.7554/eLife.95802.3.sa0)

This important study presents a statistical framework for the analysis of photometry signals and provides an open-source implementation. The evidence supporting the benefits of the presented functional mixed-effect modeling analysis as opposed to (1) summary statistics and (2) other pointwise regression models is convincing with a thorough comparison with other methods and datasets. This work will be of great interest to researchers using not only fiber photometry, but other time-series data such as calcium imaging or electrophysiology data, and wanting to implement trial-by-trial temporal analysis, taking also into account variability within the dataset.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95802.3.sa1](https://doi.org/10.7554/eLife.95802.3.sa1)

Summary:

Fiber photometry has become a very popular tool in recording neuronal activity in freely behaving animals. Despite the number of papers published with the method, as the authors rightly note, there are currently no standardized ways to analyze the data produced. Moreover, most of the data analyses confine to simple measurements of averaged activity and by doing so, erase valuable information encoded in the data. The authors offer an approach based on functional linear mixed modeling, where beyond changes in overall activity various functions of the data can also be analyzed. More in depth analysis, more variables taken into account, better statistical power all lead to higher quality science.

Strengths:

The framework the authors present is solid and well explained. By reanalyzing formerly published data, the authors also further increase the significance of the proposed tool opening new avenues for reinterpreting already collected data. They also made a convincing case showing that the proposed algorithm works on data with different preprocessing backgrounds.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95802.3.sa2](https://doi.org/10.7554/eLife.95802.3.sa2)

Summary:

This work describes a statistical framework that combines functional linear mixed modeling with joint 95% confidence intervals, which improves statistical power and provides less conservative and more robust statistical inferences than in previous studies. Pointwise linear regression analysis has been used extensively to analyze time series signals from a wide range of neuroscience recording techniques, with recent studies applying them to photometry data. The novelty of this study lies in (1) the introduction of joint 95% confidence intervals for statistical testing of functional mixed models with nested random-effects, and (2) providing an open-source R package implementing this framework. This study also highlights how summary statistics as opposed to trial-by-trial analysis can obscure or even change the direction of statistical results by reanalyzing two other studies.

Strengths:

The open-source package in R using a similar syntax as lme4 package for the implementation of this framework, the high fitting speed and the low memory footprint, even in complex models, enhance the accessibility and usage by other researchers.

The reanalysis of two studies using summary statistics on photometry data (Jeong et al., 2022; Coddington et al., 2023) highlights how trial-by-trial analysis at each time-point on the trial can reveal information obscured by averaging across trials. Furthermore, this work also exemplifies how session and subject variability can lead to different conclusions when not considered.

This study also showcases the statistical robustness of FLMM by comparing this method to fitting pointwise linear mixed models and performing t-test and Benjamini-Hochberg correction as performed by Lee et al. (2019).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95802.3.sa3](https://doi.org/10.7554/eLife.95802.3.sa3)

Summary:

Loewinger et al. extend a previously described framework (Cui et al., 2021) to provide new methods for statistical analysis of fiber photometry data. The methodology combines functional regression with linear mixed models, allowing inference on complex study designs that are common in photometry studies. To demonstrate its utility, they reanalyze datasets from two recent fiber photometry studies into mesolimbic dopamine. Then, through simulation, they demonstrate the superiority of their approach compared to other common methods.

Strengths:

The statistical framework described provides a powerful way to analyze photometry data and potentially other similar signals. The provided package makes this methodology easy to implement and the extensively worked examples of reanalysis provide a useful guide to others on how to correctly specify models.

Modeling the entire trial (function regression) removes the need to choose appropriate summary statistics, removing the opportunity to introduce bias, for example in searching for optimal windows in which to calculate the AUC. This is demonstrated in the re-analysis of Jeong et al., 2022, in which the AUC measures presented masked important details about how the photometry signal was changing. There is an appropriate level of discussion of the interpretation of the reanalyzed data that highlights the pitfalls of other methods and the usefulness of their methods.

The authors' use of linear mixed methods, allows for the estimation of random effects, which are an important consideration given the repeated-measures design of most photometry studies.

The authors provide a useful guide for how to practically use and implement their methods in an easy-to-use package. These methods should have wide applicability to those who use photometry or similar methods. The development of this excellent open-source software is a great service to the wider neuroscience community.
