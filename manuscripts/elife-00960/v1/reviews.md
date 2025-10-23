# Peer review - Round 1

Editors:
- Diethard Tautz, Max Planck Institute for Evolutionary Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00960.023](https://doi.org/10.7554/eLife.00960.023)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Spatial Self-organization Favors Heterotypic Cooperation over Cheating” for consideration at eLife. Your article has been evaluated by a Senior editor and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The study is based on a previously developed system of two yeast strains that can enter cooperative interactions. The authors have already published an eLife paper (http://dx.doi.org/10.7554/eLife.00230) describing a spatial patterning model in conjunction with a series of experiments that aimed to study inter-population cooperation. The present paper deals with the question of how cooperating patterns could emerge in the presence of a cheater. They use a similar technological approach as in their first paper and show that self-organization occurs among the cooperators, to the exclusion of the cheater. They validate their findings through modeling.

While the referees consider the topic of potential interest for eLife, there are two major concerns that need to be clarified before a final decision can be taken. One of these requires additional experiments and the conceptual scope of this paper will depend on the outcome of these experiments. Thus it is currently not possible to state that the paper can be accepted once the experiments are done, but the authors are welcome to resubmit the revised version for new assessment.

The first concern relates to the use of the term “heterotypic cooperation” rather than “mutualism”, which is not simply a semantic question, but has direct relevance for the conceptual framing and the experimental approach to be taken. Due to the current interest in social interactions in microbes, this is a crucial issue for the paper. To qualify for cooperation, you need to show that:

(i) In isolation, cooperators grow faster than cheaters. Here, one probably has to show that R outcompetes C in the presence of G. This crucial point does not seem to be addressed, so the system could simply be a case of negative frequency dependent selection. Even in this case, one could have a case of cooperation, but it still remains to be shown that pure cooperator populations maximize fitness (see e.g., MacLean et al, PLoS Biology, http://dx.doi.org/10.1371/journal.pbio.1000486; please check also definitions of ““cooperator” in Nowack, Science 314, 1560 and Doebeli & Hauert, Ecology Letters 8, 748).

(ii) In any mixture, defectors outcompete co-operators. Probably this is what you refer to when you write that “C had a growth advantage over R”, but this crucial point remains unclear. Instead, you turn off the interaction by providing lysine and adenine in the medium, but this is not the same.

With respect to mutualism, referee 2 sees a need to revisit and properly discuss previous concepts. Currently you posit partner choice/recognition as a possible mechanism favouring mutualism and contrast a spatial environment as an alternative explanation. You state however that the “mechanism is unclear” and that there is a “paradox” in terms of the effect of space. In fact this is an example of “partner fidelity feedback”, a mechanism that is well known in the mutualism literature, so there is no paradox. The essence of partner fidelity feedback is that increasing the fitness of a mutualistic partner itself leads to increased fitness for the other partner. The results can thus be easily explained within this framework: cooperators increase the local fitness of their mutualist partners, thus receiving more cooperation themselves. Empty space is required for cooperators and their partners to grow into in order to self-organise.

To clarify these issues, it will be necessary to repeat the experiments (in both supplemented and un-supplemented media) with monocultures of both the cooperator and cheater strains, showing that growth rate is higher for the cheaters when supplemented, but lower when un-supplemented. Ideally you should be able to show that cheaters should also outcompete cooperators. However, it is acknowledged that this relies on an unstructured environment, so you would need to add a non-spatial treatment. If this is feasible it would be great, but other approaches to solve this issue might also be acceptable.

The second concern is about the details of the modeling. The reason for performing simulations are obscure. Do you indeed imply that simulation results “ensure that no biological mechanism beyond cell growth [...] where required for spatial self organisation”? It seems that modeling efforts would only help to arrive at such statements, but would not be sufficient to “ensure” this. Even more problematic is the fact that the model description is far from sufficient to repeat the simulations. In the equation, D is treated as a spatially varying function, but then referred to as a constant. With two different constant values, there are two different equations, but the position of D in a later equation suggests an unnecessary complication. The text suggests that this equation is solved numerically, but no details are given except the boundary conditions. Instead, you give many simulation results as figures, but it is completely unclear how randomness emerges in the deterministic equations. Is this based on some stochastic initial condition (although you speak of densities)? Or do you use a stochastic algorithm to numerically solve a deterministic equation? In the supplement, you list many parameters (enough to fit all kinds of things), but there is no information on how exactly these enter. The only equation in the paper seems to be almost decoration.

The figures combining simulations and experiments are impressive, but it remains unclear how the various parameters of the model where chosen to generate this similarity (which appears to be difficult to quantify). Moreover, a closer inspection of cluster size and form does suggest that there is some qualitative difference between simulations and experiments. Note that it would not be enough to only clarify the source of parameters – so far the model is not described in a way that one could repeat this study. Please describe it in a way that anyone who reads the paper should be able to come up with his or her own numerical code that leads to the same results.

Finally, the current version of the manuscript is unnecessarily condensed, i.e., Results and Discussion are combined and much important information is relegated to the supplementary material. Given that there are no space constraints, an extended version of the manuscript should be envisaged, including all figures that document results and use supplementary files primarily for additional documentation that would in it self not be required for understanding the work.

[Editors’ note: before acceptance, the following revisions were also requested.]

Thank you for resubmitting your work entitled “Spatial Self-organization Favors Heterotypic Cooperation over Cheating” for further consideration at eLife. Your revised article has been favorably evaluated by a Senior editor and a member of the Board of Reviewing Editors. The manuscript has been improved but there are remaining issues that need to be addressed before acceptance, as outlined below.

The comments of referees 2 and 3 are included below. In addition, there was a consultation session with the referees that came to the following conclusion:

The presentation at the places referee 3 has pointed to is a big issue. Taking the perspective of someone reading the paper for the first time, they would quite likely be left confused on many points. A significant improvement in presentation, and addressing the use of non-isogenic lines are the main things the authors need to address.

Reviewer #2:

I have major reservations about the experiments presented in Figure 2 of the revised manuscript, which I feel must be addressed before I can suggest acceptance of the manuscript.

In attempting to demonstrate that a cooperative dilemma occurs the authors pre-adapted both cooperators and cheaters to a lysine-limited environment in order to attempt to remove the confounding effect of adaptation to this environment. While I appreciate that the “adaptive race” could be a large confounding effect, I feel the potential biases introduced are not acceptable. As the strains have been pre-adapted they are likely to no longer be isogenic. As such, all fitness effects observed thereafter could be owing to differing mutations between cooperators and cheaters that have different effects depending on the environment. While much early research on social behaviour in microbes used similarly non-isogenic lines, this has resulted in reduced impact of this work in molecular microbiology. The gold standard now is clearly to use isogenic lines, and I do not feel that I can recommend publication of results using non-isogenic lines in a journal with the aspirations of eLife.

The obvious solution to this problem for me would be to remove the experiments presented in Figure 2 from the paper and simply point to the evidence from Shou et al. 2007 and Waite & Shou 2012 supporting the existence of a cooperative dilemma. Alternatively, if the authors could analyse co-cultures on a short enough timescale so that the adaptive race is not a problem this would be preferable, but I don’t know whether this is possible. Regardless I don’t think inclusion of experiments with non-isogenic lines is acceptable for a journal of eLife’s standing.

Reviewer #3:

After reading the manuscript carefully, I still do have several concerns. Most importantly, the results are presented in a way that is confusing and most probably not beneficial to the community. For example:

- I have checked with several colleagues and the terms “homotypic cooperation” and “heterotypic cooperation” are not at all familiar terms. From the authors reply, I have not understood why they phrase their work in their own terms.

- “Kin selection can achieve positive assortment” makes no sense.

- “Can increase in frequency if it leads to more offspring that are genetically related to the original co-operator” seems to hold for anything that evolves - this statement seems to be empty unless you indicate that the “more offspring” is not produced by the focal individual.

- “Spatial environment, which allows repeated interactions” is a weird formulation. Usually, these two are treated separately, as repeated interactions allow for sophisticated behaviour conditioned on the past, whereas spatial structure per se does not.

- “Can act as a cheater of the system” is a weird formulation. C cheats G by not providing A, but does it cheat R?

- “break of symmetry from the initial symmetric distribution can be due to stochastic effects such as differences in the initial state of cells” - this seems to be self-contradictory.

- “cells attached to the glass rod” - are you sure all cells equally attach? Is this some biased sample?

I am still not convinced that Figure 3 shows a good agreement between experiment and simulations beyond “red-green domains grow, whereas blue regions remain constrained”. Simulations suggest a more complex micro-structure, which is absent ion the experiment. Figure 3 C and F suggests a much stronger association in the Co&Ch treatment than the experiment. I was also wondering why the authors look at frequencies of the two strains throughout – are absolute population sizes not relevant for the interaction? Why?

In the new, slightly improved model section, the notation should be streamlined and made readable. E.g. K always has two indices, but MM is always the same. This is unusual and not necessary. The nabla operator is not defined and nothing is mentioned on its (probably) discrete spatial version. The metabolite model is basically a time discrete version of a stochastic partial differential equation, is there a reason to use a first order algorithm? Why use two separate grid sizes?

All this suggests a high level of sophistication in terms of numerically formulating the model, but it is not clear that the model results are robust. The dynamics of yeast cells is of course individual based, but some formulations suggest that many choices in this model have been made that are not explicitly described in the text. Thus, the model cannot be understood in detail without looking into the source code, which must be commented in a way that it could be read more easily.

While I find the experimental system and the experimental results interesting, it seems that they follow in a straightforward way from the interactions in the system. Partners and co-operators can coexist and grow to high densities, whereas partners and cheaters cannot, which isolates cheaters.

In summary, while this paper has improved in the revision and while I find the basic results of interest, it is not written in a way that makes it easily accessible. I feel that these results could be presented in a much nicer, less confusing way.
