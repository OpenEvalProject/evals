# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99767.3.sa0](https://doi.org/10.7554/eLife.99767.3.sa0)

This manuscript presents a valuable minimal model of habituation which is quantified by information theoretic measures. The results here could be of use in interpreting habituation behavior in a range of biological systems. The evidence presented is solid, and uses simulations of the minimal model to recapitulate several hallmarks of habituation from a simple model.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99767.3.sa1](https://doi.org/10.7554/eLife.99767.3.sa1)

In this study, the authors aim to investigate habituation, the phenomenon of increasing reduction in activity following repeated stimuli, in the context of its information theoretic advantage. To this end, they consider a highly simplified three-species reaction network where habituation is encoded by a slow memory variable that suppresses the receptor and therefore the readout activity. Using analytical and numerical methods, they show that in their model the information gain, the difference between the mutual information between the signal and readout after and before habituation, is maximal for intermediate habituation strength. Furthermore, they demonstrate that the Pareto front corresponding to an optimization strategy that maximizes the mutual information between signal and readout in the steady-state and minimizes dissipation in the system also exhibits similar intermediate habituation strength. Finally, they briefly compare predictions of their model to whole-brain recordings of zebrafish larvae under visual stimulation.

The author's simplified model serves as a good starting point for understanding habituation in different biological contexts as the model is simple enough to allow for some analytic understanding but at the same time exhibits most basic properties of habituation in sensory systems. Furthermore, the author's finding of maximal information gain for intermediate habituation strength via an optimization principle is, in general, interesting. However, the following points remain unclear:

(1) How general is their finding that the optimal Pareto front coincides with the region of maximal information gain? For instance, what happens if the signal H_st (H_max) isn't very strong? Does it matter that in this case, H_st only has a minor influence on delta Q_R? In the binary switching case, what happens if H_max is rather different from H_st (and not just 20% off)? Or in a case where the adapted value corresponds to the average of H_max and H_min?

(2) The comparison to experimental data isn't very convincing. For instance, is PCA performed simultaneously on both the experimental data set and on the model or separately? What are the units of the PCs in Fig. 6(b,c)? Given that the model parameters are chosen so that the activity decrease in the model is similar to the one in the data (i.e., that they show similar habituation in terms of the readout), isn't it expected that the dynamics in the PC1/2 space look very similar?


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99767.3.sa2](https://doi.org/10.7554/eLife.99767.3.sa2)

The authors use a generic model framework to study the emergence of habituation and its functional role from information-theoretic and energetic perspectives. Their model features a receptor, readout molecules, and a storage unit, and as such, can be applied to a wide range of biological systems. Through theoretical studies, the authors find that habituation (reduction in average activity) upon exposure to repeated stimuli should occur at intermediate degrees to achieve maximal information gain. Parameter regimes that enable these properties also result in low dissipation, suggesting that intermediate habituation is advantageous both energetically and for the purpose of retaining information about the environment.

A major strength of the work is the generality of the studied model. The presence of three units (receptor, readout, storage) operating at different time scales and executing negative feedback can be found in many domains of biology, with representative examples well discussed by the authors (e.g. Figure 1b). A key takeaway demonstrated by the authors that has wide relevance is that large information gain and large habituation cannot be attained simultaneously. When energetic considerations are accounted for, large information gain and intermediate habituation appear to be the favorable combination.

Comments on the revision:

The authors have adequately addressed the points I raised during the initial review. The text has been clarified at multiple instances, and the treatment of energy expenditure is now more rigorous. The manuscript is much improved both in terms of readability and scientific content.
