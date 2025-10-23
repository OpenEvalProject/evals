# Peer review - Round 1

Editors:
- Yaroslav Ispolatov, University of Santiago Chile Chile

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94056.3.sa0](https://doi.org/10.7554/eLife.94056.3.sa0)

This study presents a cellular automaton model to study the dynamics of virus-induced signalling and innate host defense against viruses such as SARS-CoV-2 in epithelial tissue. The simulations and data analysis are convincing and represent a valuable contribution that would be of interest to researchers studying the dynamics of viral propagation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94056.3.sa1](https://doi.org/10.7554/eLife.94056.3.sa1)

Summary:

The manuscript describes a model based on 5-state cellular automata of development of an infection. The model is motivated and qualitatively justified by time-resolved measurements of expression levels of viral, interferon-producing, and antiviral genes. The model is set up in such a way that the crucial difference in outcomes (infection spreading vs. confinement) depends on the initial fraction of special virus-sensing cells. Those cells (denoted as 'type a') cannot be infected and do not support the propagation of infection, but rather inhibit it in a somewhat autocatalytic way. Presumably, such feedback makes the transition between two outcomes very sharp: a minor variation in concentration of 'a' cells results in qualitative change from one outcome to another. As in any percolation-like system, the transition between propagation and inhibition of infection goes through a critical state with all its attributes, including a power-law distribution of the cluster size (corresponding to the fraction of infected cells) with a fairly universal exponent and a cutoff at the upper limit of this distribution.

Strengths:

The proposed model suggests a well-justified explanation for the frequently observed yet puzzling diversity of outcomes of viral infections such as COVID.

Weaknesses:

None.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94056.3.sa2](https://doi.org/10.7554/eLife.94056.3.sa2)

Xu et al. introduce a cellular automaton model to investigate the spatiotemporal spreading of viral infection. In this study, the author first analyzes the single-cell RNA sequencing data from experiments and identifies four clusters of cells at 48 hours post-viral infection, including susceptible cells (O), infected cells (V), IFN-secreting cells (N), and antiviral cells (A). Next, a cellular automaton model (NOVAa model) is introduced by assuming the existence of a transient pre-antiviral state (a). The model consists of an LxL lattice; each site represents one cell. The cells change their state following the rules depending on the interaction of neighboring cells. The model introduces a key parameter, p_a, representing the fraction of pre-antiviral state cells. Cell apoptosis is omitted in the model. Model simulations show a threshold-like behavior of the final attack rate of the virus when p_a changes continuously. There is a critical value p_c, so that when p_a < p_c, infections typically spread to the entire system, while at a higher p_a > p_c, the propagation of the infected state is inhibited. Moreover, the radius R that quantifies the diffusion range of N cells may affect the critical value p_c; a larger R yields a smaller value of the critical value p_c. The authors further examine the result with stochastic version dynamics, and the main findings are unchanged upon stochastic dynamics. The structure of clusters is different for different values of R; greater R leads to a different microscopic structure with fewer A and N cells in the final state. Compared with the single-cell RNA seq data, which implies a low fraction of IFN-positive cells of around 1.7%, the model simulation suggests R=5. The authors also explored a simplified version of the model, the OVA model, with only three states. The OVA model also has an outbreak size. The OVA model shows dynamics similar to the NOVAa model. However, the change in microstructure as a function of the IFN range R observed in the NOVAa model is not observed in the OVA model.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94056.3.sa3](https://doi.org/10.7554/eLife.94056.3.sa3)

Summary:

This study considers how to model distinct host cell states that correspond to different stages of a viral infection: from naïve and susceptible cells to infected cells and a minority of important interferon-secreting cells that are the first line of defense against viral spread. The study first considers the distinct host cell states by analyzing previously published single-cell RNAseq data. Then an agent-based model on a square lattice is used to probe the dependence of the system on various parameters. Finally, a simplified version of the model is explored, and shown to have some similarity with the more complex model, yet lacks the dependence on the interferon range. By exploring these models one gains an intuitive understanding of the system, and the model may be used to generate hypotheses that could be tested experimentally, telling us "when to be surprised" if the biological system deviates from the model predictions.

Strengths:

- Clear presentation of the experimental findings and a clear logical progression from these experimental findings to the modeling.

- The modeling results are easy to understand, revealing interesting behavior and percolation-like features.

- The scaling results presented span several decades and are therefore compelling.

- The results presented suggest several interesting directions for theoretical follow-up work, as well as possible experiments to probe the system (e.g. by stimulating or blocking IFN secretion).

Weaknesses:

- The fixed time-step of the agent-based modeling may introduce biases. I would consider simulating the system with Gillespie dynamics where the reaction rates depend on the ambient system parameters.

- Single-cell RNAseq data requires careful handling or it may generate false leads. The strength of the RNAseq evidence presented is not clear.

Two places where the manuscript could be extended:

- Since the "range" of IFN is an important parameter, it makes sense to consider other lattice geometries other than the square lattice, which is somewhat pathological. Perhaps a hexagonal lattice would generalize better.

- Tissues are typically three-dimensional, not two-dimensional. (Epithelium is an exception). It would be interesting to see how the modeling translates to the three-dimensional case. Percolations transitions are known to be very sensitive to the dimensionality of the system.

Justification of claims and conclusions:

The claims and conclusions are well justified.
