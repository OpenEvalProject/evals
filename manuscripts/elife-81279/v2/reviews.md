# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81279.sa0](https://doi.org/10.7554/eLife.81279.sa0)

This important paper provides an in-depth analysis of the advantages and potential pitfalls of the application of Granger Causality (GC) to calcium imaging data, especially regarding various types of pre-processing. The authors' approach uses compelling rigor in arguing their points, and it is very clear how one would go about replicating their work. These results should be of interest to any researcher attempting to analyze calcium imaging data.


---

# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81279.sa1](https://doi.org/10.7554/eLife.81279.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Granger causality analysis for calcium transients in neuronal networks: challenges and improvements" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) It was not clear to the reviewers what lessons are specific to the system they are studying and which ones are to be taken as more general lessons. Certainly, dealing with slow calcium dynamics, motion artifacts, and smoothing, are general problems in calcium imaging, but the reviewers were puzzled a bit about how to decide which neurons are "strange" without a lot of system-specific knowledge. This seems to be a rather important effect, and having a bit more guidance as to this point in the discussion would be useful.

2) It was not entirely sure what results one should take home from the hindbrain analysis. It is clear that there is a more-or-less global signal modulating all neural activity, but this is a common occurrence in population recordings (often, one subtracts this off via PCA or another means before proceeding). Is the general lack of causal links (via the MVGC at least) a generic phenomenon in recurrent networks, or is there something more system-specific here? Accordingly, it might be interesting to run a recurrent neural network simulation with similar properties to the hindbrain (and perhaps with correlated driving) to see what GC/MVGC would predict. Is there any hope of these methods finding information flow in recurrent networks, or should we restrict the method to networks where we expect the primary mode of information transmission to be feedforward? Either performing simulations or limiting the stated results to feedforward networks would be important.

3) The reviewers pointed out several studies that adapt the classical GC for both electrophysiology data and calcium imaging data (e.g., [1] A. Sheikhattar et al., "Extracting Neuronal Functional Network Dynamics via Adaptive Granger Causality Analysis", PNAS, Vol. 115, No. 17, E3869-E3878, 2018. [2] N. A. Francis et al., "Small Networks Encode Decision-Making in Primary Auditory Cortex", Neuron, Vol. 97, No. 4, 2018. [3] N. A. Francis et al., "Sequential Transmission of Task-Relevant Information in Cortical Neuronal Networks", Cell Reports, Vol. 39, No. 9, 110878, 2022.). In reference [1], a variation of GC based on GLM log-likelihoods is proposed that addresses the issues of non-linearity, non-stationarity, and non-Gaussianity of electrophysiology data. In [2] and [3], a variation of GC using sparse multi-variate models is introduced with application to calcium imaging data. In particular, all three references use the sparse estimation of the MVAR parameters in order to mitigate overfitting and also use corrections for multiple comparisons that also reduce the number of spurious links. We suggest discussing these relevant references in the introduction (paragraphs 2 and 3) and discussion.

4) A major issue of GC applied to calcium imaging data is that the trials are typically limited in duration, which results in overfitting of the MVAR parameters when using least squares (See references [2] and [3] above, for example). The authors mention on page 4 that they use least squares to estimate the parameters. However, for the networks of ~10 neurons considered in this work, stationary trials of a long enough duration are required to estimate the parameters correctly. We suggest that the authors discuss this point and explicitly mention the trial durations and test whether the trial durations suffice for stable estimation of the MVAR parameters (this can be done by repeating some of the results on the synthetic data and using different trial lengths and then assessing the consistency of the detected GC links).

5) The definition of the "knee" of the average GC values as a function of the lag L needs to be a bit more formalized. In Figure 2H using the synthetic data, the "knee" effect is more clear, but in the real data shown in Figure 2I, the knee is not obvious, given that the confidence intervals are quite wide. Is there a way to quantify the "knee" by comparing the average GC values as well as their confidence bounds along the lag axis?

6) Another key element of existing GC methods applied to large-scale networks is dealing with the issue of multiple comparisons: for instance, in Figures 2, 3, 4, 6, 7, and 8, it seems like all arrows corresponding to all possible links are shown, where the colormap indicates the GC value. However, when performing multiple statistical tests, many of these links can be removed by a correction such as the Benjamini-Hochberg procedure. It seems that the authors did not consider any correction of multiple comparisons; we suggest doing so and adding this to your pipeline.

7) In Figure 5C, the values of W_IC for the MV cases seem to be more than 1, whereas by definition they should be less than or equal to 1. Please clarify.

8) Is there evidence that the lateralized and rostrocaudal connectivity of the motoneurons occurs at the time-scale of ~750 ms? Given that this time scale is long enough for multiple synapses, it could be the case that some contralateral and non-rostrocaudal connections could be "real", as they reflect multi-hop synaptic connections. Please clarify.

9) Redundant signals: throughout the brain, it's expected that a population of neurons can encode the same information. It's unclear how GC (both the original and the modified versions) can handle this redundancy. Given how pervasive redundant signals are in the brain, this should be addressed in both simulation and experimental data. For example, in one of the manuscript's simulated networks, replace one neuron with 10 copies of it, each with identical inputs and outputs but with the weights scaled by 1/10. Such a network is functionally equivalent to the original but may pose some challenges for the various versions of GC. This issue may also account for the MVGC results in the hindbrain dataset. It might be more appropriate to apply GC to groups of neurons (as indeed the authors cited), instead of applying it at the single-cell level with redundant signals.

10) Both BVGC and MVGC appear to be extremely sensitive to any outlier signals. The most worrying aspect is that the authors developed their corrections and pipelines with the benefit of knowing the structure of the underlying system, whereas in the case where GC would be most useful, the user would be unable to rely on prior knowledge of the underlying structure. For instance, the motion artifact in Figure 3a-c was a helpful example of a vulnerability of naive GC, but one could easily imagine scenarios involving an unmeasured disturbance (e.g. the table is bumped) causing a similar artifact, but if the experimenter is unaware of such unmeasured disturbances then they will not be included in Z, and hence can result in the detection of widespread spurious links. There is a circularity here that's concerning. It seems that one already needs to have the answer (e.g. circuit connectivity) in order to clean up the data sufficiently for BVGC or MVGC to work effectively. Perhaps the authors would be interested in incorporating ideas from the systems identification literature, which can include the estimation of unmeasured disturbances, perhaps in conjunction with L1 regularization on the GC links. This is certainly out of scope for the present work, but it would be worth acknowledging the difficulties of unmeasured disturbances and deferring a general solution to future work. Similar considerations apply to a common unmeasured neuronal input (e.g. from a brain region not included in the field of view of the imaging).

11) Interpretation – would it be correct to state that BVGC identifies plausible causal links, while MVGC identifies a plausible system-level model? We think these interpretations, carefully stated, might provide a helpful way of thinking about the two GC approaches. Taking the results of the paper together, neither BVGC nor MVGC is definitive – BVGC may overestimate the true number of causal links but MVGC is prone to a winner-take-all phenomenon that may represent just one of many plausible system-level models that can account for the observed data. This should be more clearly stated in the manuscript.

Reviewer #3 (Recommendations for the authors):

There are numerous typos in the manuscript and some odd choices in the citations in the introduction. Given that there are still some major conceptual issues to address, I'll defer these to the future.
