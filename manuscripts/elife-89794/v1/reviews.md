# Peer review - Round 1

Editors:
- Pierre Sens, Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89794.3.sa0](https://doi.org/10.7554/eLife.89794.3.sa0)

The authors discuss an effect, "diffusive lensing", by which particles would accumulate in high-viscosity regions – for instance in the intracellular medium. To obtain these results, the authors rely on agent-based simulations using custom rules performed with the Ito stochastic calculus convention. The "lensing effect" discussed is a direct consequence of the choice of the Ito convention without spurious drift which has been discussed before and its adequacy for the intracellular medium is insufficiently discussed and relatively doubtful. Consequently, the relevance of the presented results for biology remain unclear and based on incomplete evidence.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89794.3.sa1](https://doi.org/10.7554/eLife.89794.3.sa1)

The revised manuscript "Diffusive lensing as a mechanism of intracellular transport and compartmentalization" is very similar to the original manuscript. The main difference between the revised and the original manuscript is that the authors have removed the reference to viscosity gradient and instead talk of diffusivity gradient. With this change the manuscript the analysis and claims in the manuscript are much more aligned. The manuscript, as the original version, explores the role of spatially varying diffusion constant in three scenarios:

(i) Spatial localization of non-particles

(ii) Clustering in presence of inter-particle interactions

(iii) Moment analysis for non-interacting particles in space with discrete patches of inhomogeneous diffusivity.

Since the manuscript has not changed much the strengths and weaknesses, in my opinion, remain similar to that of the original manuscript.

Strengths: The implications of a heterogeneous environment on phase separation and reaction kinetics in cells are under-explored. This makes the general theme of this manuscript relevant and interesting.

Weaknesses: The central part of the paper "diffusive lensing", i.e., particles localizing in the region of low diffusion constant is not new. Some of the papers authors cite already show that. The parts on phase separation and frap analysis that could provide new results are not rigorous enough for a theory paper.

I reiterate some of my comments from the original version that are valid for the revised version as well.

My main criticism was not to say that some convention should be used or some not. But instead, the main point was to say that just because there is spatial diffusion constant that does not mean there will be a spatial gradient of particles. From the authors response to my comments, it is clear that they understand the subtilties around it and are aware of the relevant papers. However, a reader not familiar with this discussion may work under the impression that if there if there is a spatialy varying diffusion constant in cell there will be an accumulation of particles in the region of low diffusivity but that may not always be the case. Moreover, localisation of particles in the region of low diffusivity has been reported in many different context. Some of the papers that the author cite already show that. For example, in Rupprecht et al. 2018 non-isothermal interpretation is applied to the dynamics of objects inside cells.

Given that the central result is not new. The paper could still be of general interest to the biophysics community if the follow up sections (ii) Clustering in presence of inter-particle interactions and (iii) Moment analysis for non-interacting particles in space with discrete patches of inhomogeneous diffusivity were analysed rigorously.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89794.3.sa2](https://doi.org/10.7554/eLife.89794.3.sa2)

Summary:

The authors study through theory and simulations the diffusion of microscopic particles, and aim to account for the effects of inhomogeneous viscosity and diffusion - in particular regarding the intracellular environment. They propose a mechanism, termed "Diffusive lensing", by which particles are attracted towards low-diffusivity regions where they remain trapped. To obtain these results, the authors rely on agent-based simulations using custom rules performed within the Ito stochastic calculus convention, without drift. They acknowledge the fact that this convention does not describe equilibrium systems, and that their results would not hold at equilibrium - and discard these facts by invoking the facts that cells are out-of-equilibrium. Finally, they show some applications of their findings, in particular enhanced clustering in the low-diffusivity regions. The authors conclude that as inhomogeneous diffusion is ubiquitous in life, so must their mechanism be, and hence it must be important.

Strengths:

The article is well-written, clearly intelligible, its hypotheses are stated relatively clearly and the models and mathematical derivations are compatible with these hypotheses. In the appendices, the authors connect their findings to known results for classic stochastic differential equation formalisms.

Weaknesses:

This study is, in my opinion, deeply flawed. The main problem lies in the hypotheses, in particular the choice of considering drift-less dynamics in the Ito convention. It is regrettable that the authors choose to use agent-based custom simulations with little physical motivation, rather than a well-established stochastic differential equations framework.

Indeed, stochastic conventions are a notoriously tricky business, but they are both mathematically and physically well-understood and do not result in any "dilemma" [some citations in the article, such as (Lau and Lubensky) and (Volpe and Wehr), make an unambiguous resolution of these]. In the continuous-time limit, conventions are not an intrinsic, fixed property of a system, but a choice of writing; however, whenever going from one to another, one must include a corresponding "spurious drift" that compensates the effect of this change - a mathematical subtlety that is omitted in the article (except in a quick note in the appendix): in the presence of diffusive gradients, if the drift is zero in one convention, it will thus be non-zero in another. It is well established that for equilibrium systems obeying fluctuation-dissipation, the spurious drift vanishes in the anti-Ito stochastic convention; more precisely one can write in the anti-Ito convention

dx/dt = - D(x)/kT grad U(x) + sqrt(2D(x)) dW

with D(x) the diffusion, kT the thermal energy (which is space-independent at equilibrium), and dW a d-dimensional Wiener process. Equivalently one can write in the Ito convention:

dx/dt = - D(x)/kT grad U(x) + sqrt(2D(x)) dW + div D(x) (*)

where the latter term is the spurious drift arising from convention change. This ensures that the diffusion gradients do not induce currents and probability gradients, and thus that the steady-state PDF is the Gibbs measure (this form has been confirmed experimentally, for instance, for colloidal particles near walls, that have strong diffusivity gradients despite not having significant forces). It generalizes to near-equilibrium systems with non-conservative forces and/or temperature gradient in the form:

dx/dt = F(x) + sqrt(2D(x)) dW + div D(x) (**)

where the drift field F(x) encodes these forces. In some cases, it has been shown through careful microscopic analysis that one can have effectively a different form for the last term, namely

dx/dt = F(x) + sqrt(2D(x)) dW + alpha div D(x)

where alpha is a "convention parameter" that would be = 1 at equilibrium. For instance, in the Volpe and Wehr review this can occur through memory effects in robotic dynamics, or through strong fluctuation-dissipation breakdown. In a near-equilibrium system, this should be strongly justified, as the continuous-time dynamics with alpha \neq 1 and drift F would be indistinguishable from one with alpha = 1 and drift F + (1-alpha) div D: the authors would have the burden of proving that the observed (absence of) drift is indeed due to alpha\neq 1, rather than to much more common force fields F(x).

Here, without further motivation than the statement that cells are out-of-equilibrium, drifts are arbitrarily set to zero in the Ito convention, which is in (**) the equivalent to adding a force with drift $-div D$ exactly compensating the spurious drift. It is the effects of this arbitrary force that are studied in the article. The fact that it results in probability gradients is trivial once formulated this way (and in no way is this new - many of the references, for instance Volpe and Wehr, mention this). Enhanced clustering is also a trivial effect of this probability gradient (the local concentration is increased by this force field, so phase separation can occur). As a side note the "neighbor sensing" scheme to describe interactions is itself very peculiar and not physically motivated - it violates stochastic thermodynamics laws too, as detailed balance is apparently not respected. There again, the authors have chosen to disregard a century of stochastic thermodynamics in favor of a non-justified unphysical custom rule.

The authors make no further justification of their choice of driftless Ito simulations than the fact that cells are out-of-equilibrium, leaving the feeling that this is a detail. They make mentions of systems (eg glycogen, prebiotic environment) for which (near-)equilibrium physics should mostly prevail, and of fluctuation dissipation ("Diffusivity varies inversely with viscosity", in the introduction). Yet the "phenomenon" they discuss is entirely reliant on an undiscussed mechanism by which these assumptions would be completely violated (the citations they make for this - Gnesotto '18 and Phillips '12 - are simply discussions of the fact that cells are out-of-equilibrium, not on any consequences on the convention).

Finally, while inhomogeneous diffusion is ubiquitous, the strength of this effect in realistic conditions is not discussed. Even in the most "optimistic" case where alpha=0 would make sense (knowing that in the cellular context we are discussing thermal systems immersed in water and if energy consumption and metabolism were stopped alpha would relax back to 1), the equation (*) above shows that having zero ito drift is equivalent to having a potential countering the spurious drift, with value

U(x) = kT log(D(x) / D0 )

[I have assumed isotropic diffusion for simplicity here, so the div is replaced by a grad]. This means that the diffusion contrasts logarithmically compare to the chemical potential ones -- for instance a major diffusion difference of 100x is equivalent to 4.6kT in potential energy, a relatively modest effect. To prove that the authors' effect of "diffusive lensing" is involved in such a system, one would thus have to

1. observe strong spatial variations of the diffusion coefficient (this is doable, and was done before), AND

2. show that there is an enrichment of the diffusing species in the low-diffusion region inversely proportional to the diffusion, AND

3. show that this enrichment cannot be attributed to mild differences in potential energy, for instance by showing that if nonequilibrium energy consumption stops, the concentration fully homogenizes while the diffusion gradients remain.

If the authors were to successfully show all that in an experimental system, or design a theoretical framework where these effects convincingly emerge from physically realistic microscopic dynamical rules, they would have indeed discovered a new phenomenon. In contrast, the current article only demonstrates the well-known fact that when using arbitrary dynamical rules in heterogeneous diffusion simulations, one can get concentration gradients.
