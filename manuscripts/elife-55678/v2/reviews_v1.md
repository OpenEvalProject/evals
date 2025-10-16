# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55678.sa1](https://doi.org/10.7554/eLife.55678.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents a mathematical model of affinity maturation, which quantitatively fits single cell measurements of B-cell affinities during maturation. The main experimental finding is that maturation speed has an optimum at intermediate antigen dosage. This phenomenon is elegantly explained in the model by a trade-off between selection strength, which is stronger at small antigen dosage, and length of maturation, which is prolonged at high dosage. Overall, this work introduces a novel theoretical framework for B-cell maturation and brings an intuitive insight into the underlying forces that drive the affinity maturation of B-cells.

Decision letter after peer review:

Thank you for submitting your article "Quantitative modeling of the effect of antigen dosage on B-cell affinity distributions in maturating germinal centers" for consideration by eLife. Your article has been reviewed by Naama Barkai as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Andreas Mayer (Reviewer #1); William S DeWitt III (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This manuscript presents a mathematical model of affinity maturation, which quantitatively fits single cell measurements of B cell affinity dynamics. The main experimental finding is that maturation speed has an optimum at intermediate antigen dosage. This phenomenon is elegantly explained in the model by a trade-off between selection strength, which is stronger at small antigen dosage, and length of maturation, which is prolonged at high dosage. More broadly, a notable contribution of the work is to introduce a novel theoretical framework, which provides intuitive insight into what drives maturation dynamics and allows more rigorous parameter inference than in prior work.

The reviewers agree that the manuscript presents an interesting approach to address B-cell maturation, but they raise major concerns that we would like to see addressed.

Essential revisions:

1) One major concern is about the compatibility of the proposed dynamics with a number of recent experiments that show a rapid emergence of clonal dominance in a significant fraction of germinal centers (e.g. Tas et al., 2016, Abbott et al., 2018). This incompatibility is certainly concerning. However, we also agree that the data presented in the paper is not a product of a single germinal center (GC) but rather are cells harvested from spleens, which can contain tens of GCs at a given time point. In other words, despite the current claim, which needs to be revised, the manuscript is presenting an effective model for multiple GCs in one spleen. Each of these GCs may contain homogenized populations of cells (consistent with Tas et al.,), but the spleen data may show maintenance of diversity arising from distinct clonal populations established in different GCs.

Given this discrepancy, there are multiple issues that need to be addressed:

1.1) Simulation and modeling extension should be added to systematically include heterogeneous GC structures within a spleen.

1.2) The picture presented in the current work in which the stochastic dynamics within a germinal center is well-described by a deterministic traveling wave dynamics in affinity space seems to be in contradiction with the earlier findings (Tas et al., 2016). Importantly, as evolutionary trajectories approach affinity fitness peaks, it will become increasingly difficult for affinity-increasing mutations to occur. Subsection 'Model limitations and discussion' states "we believe this saturation effect is not relevant to model the limited maturation observed in experiments". This needs more justification, considering the convergent outcomes found in some studies (e.g. Tas et al.,). It's not obvious that the traveling wave asymptote is obtained in GC dynamics.

We propose that the authors explicitly demonstrate a specific scenario (e.g. through simulations) that their model provides at least a correct effective description for evolution of cells harvested from a spleen. Traveling wave approach might be a more realistic effective model for multiple GCs than for affinity maturation in a single GC, as currently presented.

2) The lack of any validation for ML inference procedure is a serious limitation. The manuscript describes a rugged likelihood surface for which convex optimization would be inadequate for arriving at the maximum likelihood estimation (MLE). The authors use parallel tempering to cope with this, which allows sampling across multiple local minima. However, there is no attempt to validate that model parameters can be accurately recovered by this procedure. It is not enough to say that the data are fit well as many points in the high dimensional parameter space may fit the data well. Therefore, the authors should demonstrate that model parameters can reliably be recovered from simulated data for a range of parameter values. It would be more convincing if the authors can further show that recovery is not severely impacted by model assumptions that were adopted for analytical tractability but can be violated in simulations (i.e. model misspecification). Without such validation on simulated data, it is difficult to reliably trust the parameter inference from experimental data.

3) The manuscript describes a computational method for simulation and for inferring parameters from affinity data, but the computational implementation is not made available. Access to the implementation is needed for several reasons: (1) more complete peer review will be possible if reviewers are able to assess the implementation details and even run the code, (2) reproducibility of the results, (3) upon publication, it will be more feasible for other researchers to use or build on this work. We ask the authors to make their code available to the reviewers for the next revision.
