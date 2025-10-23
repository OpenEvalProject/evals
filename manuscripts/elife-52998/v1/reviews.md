# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52998.sa1](https://doi.org/10.7554/eLife.52998.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper constructs and analyses a detailed computational model of zebrafish pigment stripe formation. It highlights the role of iridophores in organizing the melanophores and xanthophores, a facet that has largely been unaccounted for in computational modeling of zebrafish stripe patterns. Of particular interest is the analysis of the schachbrett mutant, which points to the role of tight junctions in the transition of S-iridophore packing.

Decision letter after peer review:

Thank you for submitting your article "A quantitative model for zebrafish pattern formation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sreelaja Nair (Reviewer #1); Raj K Ladher (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript describes a computational model that attempts to capture the complexities of xanthophore and iridophore interactions to explain zebrafish pigment stripe pattern formation. While the reviewers appreciate that the model is sufficient to reproduce known stripe patterns, it has not been demonstrated that the interactions included are necessary, and all reviewers were of the opinion that the model has not been used to make sufficiently interesting predictions. In order for a revision to be publishable, it must distinguish the work sufficiently from the work of Volkening and Sandstede by including several more predictions (see points 1,2,3 of reviewer 1, and point 3 of reviewer 3). In addition, as pointed out by reviewer 2, it is essential that the existing and added predictions be shown to be robust to changing parameter values within biologically reasonable ranges – tuning parameters one by one, keeping all others fixed, only between low and high values, is not a sufficient exploration of the parameter space to prove such robustness. A more comprehensive exploration of parameter space is also essential to satisfy reviewer 2 that the interactions included in the model are indeed necessary as claimed in the manuscript, and that despite the very large number of parameters the behaviour of the model is constrained enough to make robust predictions. The manuscript should also tone down claims of the novelty of the methods and the superiority of this approach compared to reaction-diffusion approaches – in particular, as reviewer 2 points out, stochasticity is easily included in reaction-diffusion approaches so that cannot count as a reason to favour a lattice-based model.

Reviewer #1:

In the manuscript entitled "A quantitative modeling approach to zebrafish pigment pattern formation", Owen et al. describe in silico modeling strategies to explain zebrafish pigment stripe formation. The authors use on-lattice modeling, in which five pigment cell types that are necessary to form the adult zebrafish pigment stripe pattern are treated as fixed to a mutually exclusive space within the domain in which the pattern will emerge. Onto this basic framework, the authors model known behaviors of the pigment cell types and intercellular interactions to simulate emergence of stripe pattern. Their modeling approach incorporates the role of iridophores in organizing the melanophores and xanthophores, a facet that has largely been unaccounted for in computational modeling of zebrafish pigment stripe pattern formation. The authors validate their model by recapitulating the wild type stripe pattern and test the model by simulating stripe pattern formation in the absence of one or more of the cell types/interactions. These additional simulations very nicely recreate stripe patterns observed in known zebrafish mutants. Overall the study is well carried out and the authors comprehensively validate their modeling strategy, making a strong case for on-lattice agent based modeling rather than a Reaction Diffusion modeling for pigment stripe pattern in zebrafish.

It is not surprising that the model recapitulates known pigment patterns, since the model was built based on biological evidences. On the basis of this the authors state that the current experimental evidences together with their model’s assumptions of S-iridophore behavior is sufficient to explain pigment pattern formation. For a set of biological interactions to be termed as sufficient for formation of a pattern, the model could perhaps be challenged by stating predictions that are currently not easy to test experimentally.

1) For example: As the authors point out, zebrafish do not incorporate additional pigment stripes as they grow. The biological basis for this is not known. In their wild type simulation starting at stage PB, how would a pattern evolve if initially the melanophores were in 3 or 5 stripes instead of the normal 4 stripes?

2) At the start of the simulations at stage PB, the dense iridophores appear along the horizontal myoseptum. Is this spatial location of iridophores relevant to formation of the pattern? Would the pattern that emerges be different if the original metamorphic pattern of dense iridophores at the horizontal myoseptum was displaced dorsally or ventrally?

3) The authors very nicely factor in the layered arrangement of the different cell types along the z-axis, to mirror the biological scenario. It is experimentally tough to switch the order of the layers, but should be possible to do in the simulations? This would be interesting because developmentally the three pigment cell types take distinct dorsal or ventral migratory routes along the horizontal myoseptum to reach their eventual z-layer. The route of migration has been thought to be critical in determining the fate of the pigment cell type (or of the stem cells that resides in the adult) and in establishing the stripe pattern. Could this assumption be partially tested to determine the relevance of the spatial order of the layers in eventual stripe formation?

Overall, I enjoyed the manuscript and the insights mathematical modeling can provide to understand complex phenomena such as pattern formation. My comments stem from limitations that mutants etc pose for understanding what information is sufficient to generate a pattern. The model is based on a finite set of proven interactions, several untested permutations and combinations of these and additional novel interactions are always possible. A major advantage of mathematical modeling is in the predictive zone, some of which experimentalists may find hard/impossible to venture into. The current study falls short of taking that leap, which would have been an interesting and informative exercise.

Reviewer #2:

This manuscript reports the study of pigment patterns in zebrafish embryos claiming a novel bottom-up stochastic model. My understanding is that this is an extensively employed standard approach using the chemical master equation for interacting (and diffusing) species to simulate emergent stochastic patterns. The authors incorporate many detailed and complex interactions between five different cell types and claim that all the interactions are essential to explain the observed patterns. My feeling is that such a study with a large number of control parameters is overkill and does not enhance our understanding of stripe patterns. As such, I do not recommend publishing this study in eLife.

1) In this manuscript, the authors present a quantitative model for simulating the stripe patterns seen in wt and mutant embryos of zebrafish. They develop a stochastic description based on the purported interactions between xanthophores, xanthoblasts, melanocytes and (two kinds of) iridophores while also incorporating motility that is biased by short- and long-ranged interactions between the cell types. These are augmented by cell division, death, differentiation and tissue growth. The resulting detailed numerical simulations are shown to qualitatively reproduce pigment patterns in wt and mutant conditions. Further, the authors quantitatively compare cell density, straightness of stripes and interstripe widths with experimental results. Several other results, such as the pair-correlation-function of cell densities, provide further justifications to the model developed.

2) The main point of this study seems to be the development of a bottom-up stochastic model incorporating as many complex and varied interactions between the cells to simulate pigment patterns. The authors contrast their approach with reaction-diffusion modelling approaches (such as Turing patterns) by saying that such approaches lack the stochasticity observed inherently in pigment patterns.

I would disagree with this viewpoint. The point of reaction-diffusion approaches is minimalistic coarse-grained descriptions of the complex effective interactions between cells (or any other constituents of the patterns) that can capture the essence of the emergent patterns. It is easy to incorporate stochasticity even in approaches that use partial-differential equations.

A complementary approach is to simulate the underlying master equation that governs the chemical interactions, supplemented by a compartment-based approach to diffusion. There are several such studies done in the past using the standard Gillespie algorithm for simulating the chemical master equation. Such studies incorporate the essential chemistry (e.g., activator-inhibitor dynamics) and coupled with diffusion can lead to emergent stripe patterns with inherent stochasticity built-in.

3) The authors, instead, develop a detailed lattice-based model with sufficiently complex interactions between 5 species of cells along with short-ranged local interactions and long-ranged non-local interactions. These interactions bias the hopping rates of the cells along the lattice. The authors speculate on the possible physical origins of these interactions. However, it is not clear if there aren't other possible interactions that could also lead to the same emergent dynamics. And hence the questions arises as to what are the essential features required at this level of modeling and what details are incidental. It should be noted that even though the authors claim that their approach is bottom-up, they are not modelling interactions between molecules. Rather, the interactions incorporated in their modeling are also effective cell-level interactions. In essence, this study has considered a master-equation like approach to simulate zebrafish stripe patterns.

4) The authors claim that all the interactions included in their model are essential for stripe patterns. This is demonstrated by turning off each interaction in-turn and showing that some feature of the pattern is lost. This is an 'all or none' switch. For the set of other parameters chosen, this might indeed lead to the conclusion that all interactions are absolutely needed. One could vary the interaction strengths in a continuous manner and then it is not clear if all the said interactions are absolutely needed for all parameter values.

5) Looking at the appendix and the supplementary material, I feel that the model is sufficiently complicated, and has so many turning parameters, that any range of behaviors is possible. It is not unreasonable to see that the large-scale emergent dynamics of such a complex model is essentially that of Turing systems which could have been simulated with much less complexity.

For the above reasons, I cannot recommend publishing in eLife.

Reviewer #3:

Owen et al. describe the formulation of a model to understand the formation of stripes in zebrafish. They revisit the Turing model that previous studies have described and refine the interaction parameters that were simplified in those models. The model presented recapitulates many of the patterns found in WT and in mutants, and models the formation of these stripes.

The study does capture the complexities of xanthophore and iridophore interactions well. Furthermore, the ability to place weights on the strength of interactions also gives the model flexibility.

The paper is well-written. However, I would like to make some suggestions, listed below.

1) The assumptions and the way the model works could be made more explicit. For this I would suggest that the authors consider incorporating Figure 1, 2 and 3 from Appendix 1 into the main manuscript.

2) I would suggest that the authors emphasise the differences of their model from the Volkening paper published in Aug 2018. I do take issue with the authors characterisation of this paper as very recent, and would suggest that they make greater reference to it in the Introduction.

3) One very interesting piece of data from this study, and the one that does differentiates this study from that of Volkening and Sandstede, is the analysis of the schachbrett mutant. This mutant points to the role of tight junctions in the transition of S-iridophore packing. It would be worth extending this analysis to the compunctiond sbr/leo and sbr/luc mutants described in Fadeev et al. Additionally, there is a suggestion of an interaction between sbr and seurat – I wonder if the model were able to predict what a double sbr/seurat would look like?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for re-submitting your article "A quantitative model for zebrafish pattern formation" for consideration by eLife. Your article has been re-reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sreelaja Nair (Reviewer #1); Raj K Ladher (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) In the revised manuscript, you write:

"The most commonly used mathematical paradigm for stripe formation takes the form of a Turing reaction diffusion model. In these representations, melanocytes and xanthophores diffuse and interact via a few long and short range 'reactions'. This class of model typically rely on a small number of parameters which, upon being altered, can generate a diverse range of patterns. Simplified models such as these have the benefit that they are often analytically tractable, allowing a deep understanding of the model. However, their main limitation is that, due to the simplicity of the approach, there is often no consistent way to link the parameters with measurable data, making it difficult to relate the model results back to the biology."

This gives the impression that (i) Turing pattern models are always simplified, and analytically tractable, and (ii) Turing models face a difficulty in relating their parameters to measurable data. Both are untenable statements and should be removed – there are several examples of both highly nonlinear Turing-type or reaction-diffusion models for pattern formation that are neither simple nor analytically tractable, and in several cases now people have shown how to relate their parameters to measurable data.

2) The authors write:

"Turing reaction-diffusion type models posit that combinations of short and long range dynamics between melanocytes and xanthophores generate stripe patterns. Indeed, much of the excitement around such models is the ease with which small parameter value changes result in diverse patterns, many readily recognisable from nature. […] A major difference between our model and Turing reaction diffusion models is that small parameter changes in our model do not typically generate qualitatively different patterns, whereas Turing reaction diffusion models can show substantial pattern changes in response to small changes (Budi, Patterson and Parichy, 2011; Yamaguchi, Yoshimoto and Kondo, 2007)."

This gives the impression that large changes in behaviour due to small changes in parameters is a generic feature of Turing models, as opposed to the model in this manuscript. This is not true, and the statements implying this should be removed – it is quite possible for Turing and reaction-diffusion models to produce small changes upon small changes in parameters, and equally it is possible for stochastic lattice models to exhibit large changes in behaviour upon small changes in parameters – it depends on the interactions and nonlinearities included in the model.

3) Finally:

"From an analytical perspective, a significant advantage of our on-lattice model in contrast to off-lattice models is their amenability to the derivation of a continuum model. Our model therefore opens up the opportunity for future exploratory work using a continuum model for mutants pfe and nac in order to explore whether pattern formation in these cases individually can be described as Turing patterns and to determine parameter ranges for successful pattern formation."

Here you argue, and we agree, that the model in the manuscript is in fact simply a discretized version of a reaction-diffusion model (albeit a quite complex one with many dynamical variables and many interactions). Thus, there is no great difference in approach between the discretized stochastic model you analyze and reaction-diffusion models, so please remove all statements that imply a large difference in your approach vs. reaction-diffusion or Turing type models. Further, a continuum limit can easily be constructed for off-lattice models as well, so this is not an advantage of your approach over that of Volkening et al. Please remove this statement, and present the opportunity for building continuum models as one that applies to both your model as well Volkening et al.'s model.
