# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14022.054](https://doi.org/10.7554/eLife.14022.054)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "High-throughput mathematical analysis identifies signaling networks for robust reaction-diffusion patterning" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Naama Barkai as the Reviewing Editor and Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The following individuals involved in review of your submission have agreed to reveal their identity: Hans Othmar.

Summary:

Determining the existence/non-existence of Turing instabilities is difficult for anything but the simplest network topologies. Consequently, a tool/resource/method to perform this calculation for more complex networks would be a significant and novel contribution to the field.

This paper outlines such a method. The method is clearly described (including a well-written supplemental), and rigorous. The use of examples to illustrate the approach is useful and convincing (particularly the synthetic biology example in which the method seems very useful).

The main finding of the paper is that Turing instabilities can readily form for a large range of parameters in realistic biological circuits including with different diffusivities of the components than commonly believed- this is a novel conclusion and is different from expectations from simpler networks.

Essential revisions:

1) The previous results and references mentioned by reviewer #2 should be incorporated into the analysis. This would probably require quite a substantial effort, but it probably necessary;

2). Several mis-interpretations are discussed by Reviewer #1. (in particular presence of LALI in type II/III networks but also the other points). Please correct and explain.

Reviewer #1:

1) I do not agree that the type II/type III networks do not show local activation, long range inhibition (LALI)

The authors find new networks that generate Turing instabilities without differential diffusivities (but see #2 below for a minor point). In several places, they state as a key result that these networks are "fundamentally different from the concepts of short-range activation and long-rage inhibition". We disagree. We think that LALI is present, but differential diffusivity is no longer required for LALI.

Type II network:

Viewed from the perspective of the variable u, then u inhibits itself over a long range via w, and activates itself over a short range via v.

Mathematically, the condition for instability (rewritten) is:

D_w / D_v > c3 / c4

(with c3, c4 defined to be positive)

Reinterpreting the parameters c3,c4 by the more traditional molecular half-lives, c3 = 1/ tW, c4 = 1/ tV

Then the instability condition is:

D_w t_w > D_v t_v

Now, if we write the lengthscale of a linearly degraded and diffusing molecule as

L_w = sqrt(D_w t_w)

Then we get:

L_w > L_vi.e. LALI.

Type III network

Viewed from the perspective of the variable u, u activates itself over a short range by v, and over a long range by the combined action of w and v. The effective range of w and v together is expected to be larger than v alone (if w diffuses); thus we expect LALI for any (positive) diffusivities.

To make this a little more concrete, assuming that v and w reach pseudosteady state relative to u (i.e. move to some region of parameter space).

Then the fourier transform of u, u(q), should obey (the linear terms only):

\partial u(q) / \partial t =

=u (q).[A / (D_v q^2+c_v) – B / ((D_v q^2+c_v) (D_w q^2+c_w))]

If we look at the second term, expanding to lowest order in q^2, we get a term like:

-u(q). B / (const + (D_v + D_w)q^2)

In this case the A-term is the local activation by v; the B-term is the long range inhibition via w and v – which by definition has an effective diffusivity larger than D_v.

Now these arguments won't work for all regions of parameter space – but we expect the same qualitative logic to hold true – LALI (albeit with no direct differential diffusivity).

2) Turing instabilities require differential diffusivity

This has been proved in the general case, see the Satnoianu 2005 reference. I think the point to make is that by having an immobile component and a diffusing component automatically satisfies differential diffusivity. This is more of a mathematical, rather than a biological point.

Satnoianu 2005:

Satnoianu, R. A., and P. van den Driessche. "Some remarks on matrix stability with application to Turing instability." Linear algebra and its applications 398 (2005): 69-74.

3) The graph theory is interesting, but its main point is obscure in the writing

I found the graph theory section very interesting. The main conclusion as I see it: it provides an elegant/pictorial way to calculate the a_k (Routh-Hurwitz) coefficients. These can then be used to derive the instability conditions.

However, from the writing it wasn't clear that this was the main result from the graph theory – when reading the main text and the supplemental, I thought that the graph theory was used to derive instability conditions directly without recourse to the Routh parameters. I would recommend more plainly/directly saying what the graph theory does.

Relatedly, the requirement for a cycle with positive weight ("the instability cycle") is perhaps related to the condition for Turing instability outlined in Satnoianu 2000 (referred to in the main text). In this case, you might be able to make a graph-theory-only condition: necessary conditions for instability are the existence of a positive weight cycle.

4) Clarify some 'robustness' terms in the main text

The term 'robust' was used in various places, some of which it was clear, and some of which it wasn't ("more robust" should be something like "more robust to parameter changes").

5) There are examples of a 3 node network with only 1 diffusing component that has a Turing instability. See example 3.1 in Satnoianu 2000. Only one diffusive species is required!

(What is really nice, however, is that I could get other examples using RDNets.com)

Reviewer #2:

This paper describes a computational approach and associated software aimed at automating the process of finding kinetic networks that support Turing instabilities. While this is a worthwhile effort, there are several issues concerning this paper.

First and foremost is that the authors are apparently unaware of a result proved long ago that gives necessary conditions on the kinetic network alone for the absence of Turing instabilities. Thus the violation of any of these conditions can give rise to a Turing instability. The result appears in a paper by Othmer in 1980, entitled 'Synchronized and differentiated modes of cellular dynamics', which appeared in Dynamics of Synergetic Systems, H. Haken ed. The theorem goes as follows (σ(A) is the spectrum of A.

Let D be diagonal with Dj {greater than or equal to} 0. In order that σ(K − μD) ⊂ LHP for all such D and all μ ∈ [0, ∞),it is necessary that

• σ(K) ⊂ LHP

• σ(K[i1, i2, · · ·, ip]) ⊂ LHP for all pth

-order submatrices of K, where 1 {less than or equal to} p {less than or equal to} n − 1.

The result could alter the search for Turing instabilities described in Appendix 1 quite dramatically, since one could first categorize the networks that have a sub-network that is unstable when severed from the full network at the steady state of the full system, and only then determine the pattern of diffusion coefficients that produce different types of instabilities. This eliminates the need to examine all RH determinants over the entire range of wave numbers. Notice that the theorem does not require that the fully-isolated sub-network be unstable on its own, though this is allowable, but rather that the Jacobian of the terms affecting the sub-network have one or more eigenvalues in the RHP.

A second remark is that much of Appendix 1 and most of Appendix 2 contains material readily available in the literature, and could be eliminated. It would be better to replace this material with a precise formulation of the problem the authors are addressing. For example, they implicitly assume that all diffusible species must satisfy homogeneous Neumann boundary conditions, but this means that the results don't apply to common situations in pattern formation, such as the production of a morphogen at the boundary of the domain.
