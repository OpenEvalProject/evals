# Peer review - Round 1

Editors:
- Valentin Wyart, https://ror.org/013cjyk83 École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77220.sa0](https://doi.org/10.7554/eLife.77220.sa0)

This paper provides a new approach, Mixed Neural Likelihood Estimator (MNLE) to build likelihood emulators for simulation-based models where the likelihood is unavailable. The authors show that the MNLE approach is equally accurate but orders of magnitude more efficient than a recent proposal, likelihood approximation networks (LAN), on two variants of the drift-diffusion model (a widely used model in cognitive neuroscience). This work provides a practical approach for fitting more complex models of behavior and neural activity for which likelihoods are unavailable.


---

# Peer review - Round 1

Editors:
- Valentin Wyart, https://ror.org/013cjyk83 École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77220.sa1](https://doi.org/10.7554/eLife.77220.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Flexible and efficient simulation-based inference for models of decision-making" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Valentin Wyart as the Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Luigi Acerbi (Reviewer #1); Jean Daunizeau (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As you will see after reading the two reviews (copied at the bottom of this message), the two reviewers have found that the MNLE approach you describe represents a significant advance over LANs. As summarized by Reviewer #1, instead of estimating the likelihood *independently* for each parameter setting and then training a neural network to interpolate between these density estimates, MNLE uses *conditional* density estimation which trains a density network while sharing information across different parameters settings. This approach, and others built on top of it or inspired by it, may have a large impact in the field, even more so since all code has been made available by the authors.

But while this approach is a priori order of magnitude more efficient than LANs, the reviewers have agreed that the current manuscript does not provide sufficient empirical evidence that it is the case. The reviewers have discussed how in practice the comparison between LANs and MNLEs could be improved to strengthen the manuscript in this respect. Furthermore, the reviewers have also identified limitations of the approach (shared with LANs) that are worth discussing more explicitly in the paper. We hope that you will find the reviews helpful when revising your manuscript. When submitting your revised manuscript, please provide a point-by-point response to the essential revisions that were decided after discussion between the reviewers. The other points made in the separate reviews (provided at the bottom of this message) should also be addressed, but they do not require a point-by-point response.

Essential revisions:

1. While the MNLE approach appears much more sample-efficient than the LAN approach, there is not sufficient empirical evidence that it is indeed the case. The main piece of evidence is described in Section 2.2, where the authors show that MNLE learns likelihood function as accurately as LAN, but with only a fraction of the simulation budget. The authors show that a MNLE estimator trained with 10^5 model simulations is as accurate as a LAN estimator trained with 10^11 model simulations. However, the authors did not show that a LAN estimator trained with only 10^5 model simulations yields less accurate results than a MNLE estimator trained with the same simulation budget, or that a MNLE estimator trained with 10^11 simulations yields much better results than a LAN estimator trained with the same simulation budget. A more interpretable comparison of the two approaches is needed here: claiming that MNLE is more efficient than LAN is important, but requires additional work. We do not require the authors to systematically vary the number of model simulations (spanning the 10^5 to 10^11 range), and quantify each method's efficiency in terms of accuracy profile over this range. The authors could compare their MNLE estimator trained with 10^5 model simulations with a LAN estimator trained on 10^8 samples, which is still 1000 times more than their MNLE estimator, and show that the LAN estimator performs much worse than their MNLE estimator. Note that there is an additional technical caveat here, in that training LANs depends on an additional degree of freedom = how many parameters / how many samples per parameter. The authors should keep a sensible split. The current split appears to be 10^6 parameters and 10^5 samples per parameter. When going down to 10^8, it would make sense to keep a similar ratio.

2. Additional "accuracy" metrics should be considered when comparing MNLE and LAN estimators. These metrics may include likelihood approximation accuracy, parameter estimation accuracy and estimation uncertainty accuracy. The last two are important in practice, because errors in likelihood approximations may have a very small impact on parameter estimation. Regarding parameter estimation accuracy, the metric used in the manuscript (the "absolute difference in posterior sample mean normalized by reference posterior standard deviation") may not be the most informative. Indeed, significant differences between MNLEs and LANs in this metric may have no practical consequence whatsoever in terms of absolute parameter estimation errors. This is what Figure 4A seems to indicate. It could be useful to use metrics that relate to parameter recovery, e.g., parameter estimation error or pairwise parameter confusion. LAN estimators may show more pairwise parameter confusion than MNLE estimators, for example.

3. The following limitations of MNLE estimators (limitations shared with LAN estimators) should be discussed more explicitly in the manuscript:

– The drift-diffusion model used to benchmark the approach has a very low-dimensional observation structure (one binary observation + one continuous observation per trial). This limitation is not necessarily a problem because many models in cognitive neuroscience have a very low-dimensional observation structure, but it is worth mentioning.

– The approach described works for i.i.d. data. Any additional structure/dependence (e.g., adding parameters to characterize the stimulus shown in the trial) effectively increases the dimensionality of the likelihood approximation the network needs to learn.

– The manuscript does not sufficiently discuss nor explore the scalability of the MNLE approach. Given the previous related work by some of the authors, that has shown remarkable results in this respect, it would be useful to discuss the scalability of MNLEs in the discussion.

– Like any neural-network based approach, selecting the hyperparameters and architecture of the network requires either prior knowledge and/or brute force. And it is currently unclear how in practice the MNLE approach can be applied for different models. Importantly, even if training a MNLE estimator *given the hyperparameters* might require a small number of simulations (10^5), we need to account for the additional cost of finding the correct hyperparameters for training the emulator (presumably, requiring an exploration of at least 10-100 hyperparameter settings).

Reviewer #1 (Recommendations for the authors):

I already discussed an earlier version of the manuscript with the authors, so I don't really have much to add to my previous comments and to my public comments (i.e., there are a couple of limitations that the authors could address a bit more explicitly, like dimensionality of the method and the cost of hyperparameter tuning).

Reviewer #2 (Recommendations for the authors):

Let me now explain why I think that authors' main claim (namely: that MNLE is more efficient than LAN) may not be strongly supported by the results reported in the current version of the manuscript.

The main piece of evidence is summarized in Section 2.2, where authors claim that MNLE learns likelihood function as accurately as LAN, but with only a fraction of the simulation budget. In brief, authors showed that a MNLE estimator trained with 10^5 model simulations is as accurate as a pre-trained version of the LAN method for DDMs (which used 10^11 model simulations). The problem here, is that they did not show that a LAN estimator trained with only 10^5 model simulations yields less accurate results. Or that MNLE trained with 10^11 simulations yields much better results. More generally, what is needed here is a quantitative comparison of the efficiency of the method. One would expect that, for both MNLE and LAN, increasing the number of model simulations increases the accuracy of likelihood approximation. However, this probably follows the law of diminishing marginal utility (i.e. using 10^11 simulations may bring little advantage when compared to e.g. 10^10) (:) Hence, efficiency here should be measured in terms of the speed at which the results accuracy increases. In other terms, claiming that MNLE is more efficient than LAN is important, but requires more work than what is done here. Authors should systematically vary the number of model simulations (spanning, e.g. the 10^5 to 10^11 range), and quantify each method's efficiency in terms of the accuracy profile over this range.

Now, this analysis should be performed with different "accuracy" metrics. In particular, authors may measure likelihood approximation accuracy, parameter estimation accuracy and estimation uncertainty accuracy. The latter are critical, because if errors in likelihood approximations may have very small impact on parameter estimation. I note that, w.r.t. parameter estimation accuracy and estimation uncertainty accuracy, I don't think authors chose very informative metrics. For example, the former is defined as the "absolute difference in posterior sample mean normalized by reference posterior standard deviation". If I understood correctly, this metric may show significant differences between MNLE and LAN that would have no practical consequence whatsoever, given that methods would be very similar in terms of their absolute parameter estimation errors. In fact, this is what Figure 4A seems to indicate. I would rather suggest to use accuracy metrics that practically "mean something" for parameter recovery. Measuring parameter estimation error is a possibility (although one may then conclude that MNLE brings no clear advantage when compared to LAN, cf. Figure 4A). But there are other possibilities. For example, likelihood approximation errors may induce pairwise parameter confusions. In turn, for a small simulation budget, LAN estimators may show more pairwise parameter confusion than MNLE. Note: to quantify pairwise parameter confusion in the context of DDM, authors may take inspiration from Feltgen 2021 (or any other metric of their choice).
