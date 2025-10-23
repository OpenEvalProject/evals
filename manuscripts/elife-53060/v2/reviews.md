# Peer review - Round 1

Editors:
- Thomas Yeo, National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53060.sa1](https://doi.org/10.7554/eLife.53060.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this study, Cui and colleagues utilized linear control theory to compute the amount of "energy" necessary for a brain to transition from a baseline state to a frontoparietal control state. They showed that minimum control energy necessary for the transition is lower for older participants and is maximal in the frontoparietal regions. The patterns of control energy can be used to predict participants' age. Furthermore, control energy of cingulate cortex is negatively correlated with executive function performance even after controlling for age. This works highlights a potential mechanism by which executive function develops. The work is technically excellent and the findings are likely to be of broad interest to the community. Moreover, the authors demonstrate the effect from multiple angles. We are also very impressed by the authors' response to the reviewers' comments.

Decision letter after peer review:

Thank you for submitting your article "Optimization of energy state transition trajectory supports the development of executive function during youth" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, Cui and colleagues utilized linear control theory to compute the amount of "energy" necessary for a brain to transition from a baseline state (zero activity everywhere) to a frontoparietal control state (activity of ones in frontoparietal regions and zeros everywhere else). They showed that minimum control energy necessary for the transition is lower for older participants and is maximal in the frontoparietal regions. The patterns of control energy can be used to predict participants' age. Furthermore, control energy of cingulate cortex is negatively correlated with executive function performance even after controlling for age. This works highlights a potential mechanism by which executive function develops. The manuscript follows logically from the authors' previous work and convincingly demonstrates that network-mediated control of executive areas is correlated with age. The work is technically excellent and the findings are likely to be of broad interest to the community. Moreover, the authors demonstrate the effect from multiple angles.

Essential revisions:

1) For a life sciences journal, the manuscript is quite technical and uses a lot of jargon such as modal controllability that is not well defined and might not be understandable to a life science readership. It would be useful to better explain the biological basis of terms such as the control trajectory distance.

2) We suggest toning down language throughout the paper. Associations of r=0.17 can hardly be called strong, particularly given that this is cross-sectional sample. The extended discussion of electrical stimulation and neurofeedback is peripheral to the current results, given that these modalities were not investigated. I suggest keeping the discussion specific to the current results and providing some basic discussion of biological or network mechanisms that could potentially underpin the relation between control energy and age.

3) While network control theory is a novel way to capture the relation between brain network development, it would be useful to understand the basic network properties that change over age and therefore underpin the relation between age and control energy. As they currently stand, the control theory results are quite abstract and do not appear to provide insight into specific network-related or biological mechanisms that enable lower-cost transitions.

a) The computation of control energy is fully characterized by the network connectivity matrix. Therefore, any relation between age and control energy should be able to be traced back to relations between age and other simpler network properties of the connectivity matrix. It would be informative to evaluate whether the modular structure or connectivity strength relates to age, which could provide a simpler characterization of the control energy result that is closer to the underlying biology.

b) One possibility is that the FP network may show greater modularization with age, together with an overall increase in network integration. Indeed, the authors have previously suggested increased segregation of the FPN in this dataset (Baum et al. 2017). The fact that control energy is greater in the randomized null might be consistent with this notion. This kind of insight would be useful to link the control energy results and underlying network-level mechanisms.

c) A related possibility is that the results might simply be re-capitulating the fact that younger participants have weaker long range connections. First, it seems obvious that the best way to "activate" the frontoparietal regions would be to inject energy into the target (frontoparietal) regions, so it's not surprising that frontoparietal regions required the most control energy (Figure 1C). For older participants, this energy might be lower because frontoparietal regions are now more strongly connected to other regions, so the overall control energy (and frontoparietal control energy) can be reduced by "distributing" the control energy budget to other regions.

4) The authors should explicitly mention the definition of the final state and initial states in the Results section. While this is explained in the Materials and methods section, this should really be in the Results section because this is quite important.

5) The authors justified their choice of initial and final state as follows "We set the baseline state to zero, because we sought to model the contrast in activation between an executive task and the resting state. This comparison is motivated by a long history of task fMRI experiments that explicitly contrast executive tasks to the resting state, resulting in robust activation of the fronto-parietal cortex (Cohen et al., 1997; Forsyth et al., 2014; Nagel et al., 2009; Ragland et al., 2002; Rowe et al., 2000). We set the values of regions in the fronto-parietal system to 1 to represent the fact that these regions were activated." We agree with the rationale, but based on the rationale, it seems that a better initial state should be the fMRI activity pattern averaged across all time points during a resting-fMRI scan and the final state should be the fMRI activity pattern averaged across all time points during an executive function task.

6) Equation 2: "S is 0-1 diagonal matrix of size N x N that selects only the nodes that we wish to control. Here, we only constrain the activity of the fronto-parietal system." – Can the authors clarify this statement? Is S the identity matrix? We thought that all nodes are targeted since the target state comprises 1 for the frontoparietal nodes and 0 for other nodes. But the authors now seem to imply they only constrain the activity of the frontoparietal nodes.

7) "When model weights were examined at the level of individual network nodes, the regions that most contributed to the prediction of brain maturity aligned with univariate analyses, and included the dorsolateral and ventrolateral prefrontal cortex, the cingulate cortex, superior parietal cortex, and lateral temporal cortex" – It is well-known that model weights should not be interpreted without filtering (Haufe et al., 2014). Given the authors are using ridge regression, Haufe's approach is perfect for this situation.

8) The authors need to provide more details about how they controlled for linear and nonlinear effects of age in their analysis (e.g., correlation between control energy and executive performance). The authors mentioned generalized additive models and penalized splines, but the details were nowhere close to being sufficient.

9) The authors need to provide more details about the mediation analysis (e.g., assumptions). How do we interpret the betas in Figure 4C and D? Total effect is 0.67, while mediation effect is 0.03 and direct effect is 0.64. Doesn't this mean that the analysis is suggesting that the indirect effect is quite small relative to the direct effect? If so, this should be discussed.

10) The age prediction analysis requires motivation and better integration with the rest of the paper. It is likely that simpler features such as the tractography connectivity strengths or basic network properties would also yield good predictive models of age. Therefore, the reason for using a more complex feature space is unclear, unless it can be demonstrated that control energy can outperform the accuracy of more basic features, or reveals a specific mechanism that characterizes network development.

11) The relation identified between control energy and age appears to be linear based on Figure 2 and thus the reasons for fitting penalized splines to characterize nonlinear associations could be better described. Are the lines shown in Figure 2 representative of the splines? The claims regarding the specificity of the FP network require clarification. The null model corresponding to the rewired graph does not appear to have been evaluated for the other canonical networks. To establish specificity of the FP, the null model should also be considered for the other networks. Based on this global null model alone, we would suggest that it is hard to claim that the brain is explicitly wired to optimize transition cost to the FP activation state. Wiring organization is also likely to contribute to other cognitive functions as well.

12) In addition, it would be interesting to know whether the node-level measures are related to degree and/or strength. The authors use the two statistics as covariates in the predictive model, but do not show whether they are related to control energy directly.
