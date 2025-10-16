# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92683.4.sa0](https://doi.org/10.7554/eLife.92683.4.sa0)

This important study develops a machine learning method to reveal hidden unknown functions and behaviors in gene regulatory networks by searching parameter space in an efficient way. Solid evidence is presented for the method, which should be of broad interest to anyone working in biology, as the ideas put forward by the authors extend beyond gene regulatory networks to reveal hidden functions in any complex system with many interacting parts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92683.4.sa1](https://doi.org/10.7554/eLife.92683.4.sa1)

Summary:

This paper suggests to apply intrinsically-motivated exploration for the discovery of robust goal states in gene regulatory networks.

Strengths:

The paper is well written. The biological motivation and the need for such methods are formulated extraordinarily well. The battery of experimental models is impressive.

Weaknesses:

(1) The proposed method is compared to the random search. That says little about the performance with regard to the true steady-state goal sets. The latter could be calculated at least for a few simple ODE (e.g., BIOMD0000000454, `Metabolic Control Analysis: Rereading Reder'). The experiment with 'oscillator circuits' may not be directly interpolated to the other models.

The lack of comparison to the ground truth goal set (attractors of ODE) from arbitrary initial conditions makes it hard to evaluate the true performance/contribution of the method. A part of the used models can be analyzed numerically using JAX, while there are models that can be analyzed analytically.

"...The true versatility of the GRN is unknown and can only be inferred through empirical exploration and proxy metrics....": one could perform a sensitivity analysis of the ODEs, identifying stable equilibria. That could provide a proxy for the ground truth 'versatility'.

(2) The proposed method is based on `Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning', which assumes state action trajectories [s_{t_0:t}, a_{t_0:t}], (2.1 Notations and Assumptions' in the IMGEP paper). However, the models used in the current work do not include external control actions, but rather only the initial conditions can be set. It is not clear from the methods whether IMGEP was adapted to this setting, and how the exploration policy was designed w/o actual time-dependent actions. What does "...generates candidate intervention parameters to achieve the current goal...."

mean considering that interventions 'Sets the initial state...' as explained in Table 2?

(3) Fig 2 shows the phase space for (ERK, RKIPP_RP) without mentioning the typical full scale of ERK, RKIPP_RP. It is unclear whether the path from (0, 0) to (~0.575, ~3.75) at t=1000 is significant on the typical scale of this phase space. is it significant on the typical scale of this phase space?

(4) Table 2:

(a) Where is 'effective intervention' used in the method?

(b) In my opinion 'controllability', 'trainability', and 'versatility' are different terms. If there correspondence is important I would suggest to extend/enhance the column "Proposed Isomorphism". otherwise, it may be confusing. I don't see how this table generalizes generalizes "concepts from dynamical complex systems and behavioral sciences under a common navigation task perspective".


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92683.4.sa2](https://doi.org/10.7554/eLife.92683.4.sa2)

Summary:

Etcheverry et al. present two computational frameworks for exploring the functional capabilities of gene regulatory networks (GRNs). The first is a framework based on intrinsically motivated exploration, here used to reveal the set of steady states achievable by a given gene regulatory network as a function of initial conditions. The second is a behaviorist framework, here used to assess the robustness of steady states to dynamical perturbations experienced along typical trajectories to those steady states. In Figs. 1-5, the authors convincingly show how these frameworks can explore and quantify the diversity of behaviors that can be displayed by GRNs. In Figs. 6-9, the authors present applications of their framework to the analysis and control of GRNs, but the support presented for their case studies is often incomplete.

Following revision, my overall perspective of the paper remains unchanged. The first half of the paper provides solid evidence to support an important conceptual framework. The evidence presented for the use cases in the latter half is incomplete; as the authors note, they are preliminary and meant to be built on in future work. I have included my first round comments below.

Strengths:

Overall, the paper presents an important development for exploring and understanding GRNs/dynamical systems broadly, with solid evidence supporting the first half of their paper in a narratively clear way.

The behaviorist point of view for robustness is potentially of interest to a broad community, and to my knowledge introduces novel considerations for defining robustness in the GRN context.

Some specific weaknesses, mostly concerning incomplete analyses in the second half of the paper:

(1) The analysis presented in Fig. 6 is exciting but preliminary. Are there other appropriate methods for constructing energy landscapes from dynamical trajectories in gene regulatory networks? How do the results in this particular case study compare to other GRNs studied in the paper?

Additionally, it is unclear whether the analysis presented in Fig. 6C is appropriate. In particular, if the pseudopotential landscapes are constructed from statistics of visited states along trajectories to the steady state, then the trajectories derived from dynamical perturbations do not only reflect the underlying pseudo-landscape of the GRN. Instead, they also include contributions from the perturbations themselves.

(2) In Fig. 7, I'm not sure how much is possible to take away from the results as given here, as they depend sensitively on the cohort of 432 (GRN, Z) pairs used. The comparison against random networks is well-motivated. However, as the authors note, comparison between organismal categories is more difficult due to low sample size; for instance, the "plant" and "slime mold" categories each only has 1 associated GRN. Additionally, the "n/a" category is difficult to interpret.

(3) In Fig. 8, it is unclear whether the behavioral catalog generated is important to the intervention design problem of moving a system in one attractor basin to another. The authors note that evolutionary searches or SGD could also be used to solve the problem. Is the analysis somehow enabled by the behavioral catalog in a way that is complementary to those methods? If not, comparison against those methods (or others e.g. optimal control) would strengthen the paper.

(4) The analysis presented in Fig. 9 also is preliminary. The authors note that there exist many algorithms for choosing/identifying the parameter values of a dynamical system that give rise to a desired time series. It would be a stronger result to compare their approach to more sophisticated methods, as opposed to random search and SGD. Other options from the recent literature include Bayesian techniques, sparse nonlinear regression techniques (e.g. SINDy), and evolutionary searches. The authors note that some methods require fine-tuning in order to be successful, but even so, it would be good to know the degree of fine-tuning which is necessary compared to their method. [second round: the authors have included a comparison against CMA-ES, an evolutionary algorithm]
