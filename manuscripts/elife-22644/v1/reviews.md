# Peer review - Round 1

Editors:
- Carl T Bergstrom, University of Washington , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22644.022](https://doi.org/10.7554/eLife.22644.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Bacterial cartels at steady supply" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Eric D Kelsic (Reviewer #1).

Our decision has been reached after consultation between the reviewers. As you will see, one of the reviewers raised a number of significant concerns, many of which the other reviewer acknowledged to be important during subsequent discussion. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Reviewer #1:

The manuscript by Taillefumier et al. is well written and comprehensive, and I found the theory of bacterial cartels to be quite elegant and thought-provoking. The authors set out to understand microbial diversity by modeling communities of organisms that require a number of essential building blocks for growth. If the building blocks are present in the environment they may be imported into cells, or cells may choose to obtain the building block by enzymatically converting from one type to another. The authors model the growth potential of different strategies under the constraint of a fixed enzyme budget. Through a number of simplifying assumptions and linearizations the authors identify optimal metabolic classes and finally show that sets of organisms, termed "cartels", can optimally consume resources and prevent other species from invading. While such communities only coexist at fixed points within the space of external resource concentrations, the authors beautifully show that these points are attractors for regions within the space of supply rates, and thus cartels will frequently emerge when communities are continually challenged with organisms exhibiting various metabolic strategies.

The cartel theory makes significant progress toward understanding the diversity of microbial communities. Importantly, the work shifts the emphasis away from the number of (rather abstract) environmental resources and focuses instead on the building blocks that are essential for growth and the various strategies by which to obtain these building blocks. I find this setup more conceptually appealing. I believe that the manuscript will be of broad general interest and it would be great to see it published in eLife.

I have no major concerns. The manuscript is already highly polished and could be published without significant revisions.

Reviewer #2:

The manuscript by Wingreen and co-workers examines the structure of bacterial communities that consist of different metabolic types, under a non-trivial model that involves feedbacks from external metabolite concentrations and internal metabolic conversions and fluxes, subject to specific enzyme availability, onto the growth rates. Overall, this is an important subject for which general theoretical results could be useful for guiding experiments as well as introducing new ideas for analysis of bacterial communities.

Unfortunately, the text does an extremely poor job of explaining the main conclusions. One can follow the main assumptions of the model, but once the notions of consortia and cartels are introduced, it requires a good deal of work to follow which features of the model have been preserved and which ones have been conveniently thrown out the window under some new assumption that enables analysis. Over the course of the manuscript, several such assumptions are made, which effectively change the underlying model, while the key notions of consortia and cartels are defined non-rigorously and in a model-dependent manner.

The section entitled Model is the clearest section of the paper. The authors make many modeling assumptions here, some of which are questionable (see below), but these are all explained clearly.

The Results section begins with Numerical Simulations, which motivates the rest of the manuscript. The authors give too few details on how extensive their simulations are. How reproducible are they? How long have they run them? How complex a space of strategies was explored?

A) A key point at this stage of the manuscript (i.e. Results) and at the end of the Model Section is the statement that the authors are interested only in the structure of the equilibrium attained, not in the dynamics. They state: "Eventually, at long times, the surviving population will consist entirely of optimal cell types and will no longer change. It is this final population that concerns us; we only simulate metabolic competition to gain insight into the final optimized population, which is independent of the specific dynamics of the simulation."

This statement appears to be some kind of hope since it is neither (a) proven nor (b) demonstrated by extensive numerical simulations. The simulations assume that new types are only added once other types have gone extinct (subsection “Competitive population dynamics”, last paragraph), which is a pretty big assumption regarding "specific dynamics of the simulation" and which, in fact, guarantees that once a community consists of types that are not going extinct it won't have to worry about new types coming in. Indeed, the structures that are later called "cartels" in this manuscript are automatically stable under the given dynamics, due to the fact that avoidance of extinction necessarily excludes competition by new types; such dynamics are intrinsically 'cartel-friendly'. Under different dynamics, for example where new types appear at random times, or are formed by mutation from existing types, there would be no such guarantee, and it is therefore not at all clear that the final population structure (if such a stable structure even exists; see B) would not depend on the specific dynamics.

In fact, Figure 2D seems to contradict the basic assertion that a surviving population consists only of optimal types and no longer changes. In Figure 2D, blue and yellow curves seem to exchange at regular intervals, and the population composition is dynamic in time. In this case, the caption states that the "external building-block concentrations fluctuate due to the invasion by and extinction of metabolic variants." Which leads to my next major point.

B) The entire analytical treatment of the manuscript is predicated on the assumption that the external concentrations Ciext are fixed. From the second paragraph of the subsection “Optimal metabolic classes” to the end of the first paragraph of the subsection “Structure of consortia”, the authors develop the basic framework in which external concentrations are self-consistently derived such that they obtain an optimal metabolic strategy under the assumption that Ciext do not fluctuate. However, they have already shown in Figure 2D that even in the simplest cases the dynamics may converge to a fluctuating solution under even their cartel-friendly dynamics (see A above).

Thus, at this point in the text, the authors have subtly shifted our attention away from the dynamics they initially presented, to some new scenario, in which they search for a certain type of optimum (i.e. one with fixed Ciext). They carry out a careful analysis of such optima (with some additional caveats) throughout the rest of the text. However, they provide no information as to whether such optima are dynamically stable at all. But if these optima are not dynamically stable, then what use is all of their analysis?

Overall, it appears that the authors have performed a nice characterization of a well-defined graph-theoretic optimization problem (stated in the aforementioned subsections). They motivated this problem in the context of a dynamical system, but they have failed to demonstrate that the dynamics converge to their optimum; or more precisely, to give a characterization of conditions (i.e. the choice of constant supply rates, initial conditions, and the exact simulation dynamics) under which their optimum is achieved. Therefore, I recommend that they submit this paper elsewhere, e.g. to a graph theory or combinatorial optimization journal, where their more rigorous results will be properly assessed by mathematicians. Biologists who read eLife will not understand the range of applicability, or lack thereof, of these results. I certainly do not.

Other concerns:

C) The assumption to study the "minimum model" in the last paragraph of the subsection “Structure of consortia” is quite strong. For example, the growth rate no longer depends on the bi variables that were introduced initially. This is another example of the authors presenting a much more general model than the one they ultimately analyze. For the poor reader who has made it through the Model section, but is not technically proficient to follow the derivations where the extra assumptions are buried (such as in the last paragraph of the subsection “Structure of consortia”), this can end up being misleading.

D) On the technical level, the question of the bi is important, since different bacteria may have different composition, at least with regard to a subset of key building blocks, and one would like to know if this impacts the metabolic specialization across the community to any extent. Another place where this seems to be relevant is in Equation (3), where the term -gbi at the end of the equation corresponds to the assumption, stated earlier, that building blocks are consumed at a rate proportional to their concentration in biomass, i.e. bi. This is necessary for the steady-state growth, and will be achieved automatically at the level of the bulk population, but at the level of enzymatic activity inside cells, one expects something like -gci. This point should be discussed, and the relevant extra assumptions that are being made here need to be pointed out.

E) In the Discussion, the authors state "In particular, cartels maintain fixed external resource concentrations by adjusting their populations to compensate for changes in supply." This is a question of dynamics, again, but dynamics have not been addressed in the analysis. Critically, the statement here is that if the external resource changes (over some unspecified timescale), the subpopulation sizes that contribute to the cartel will adjust such that the external resource concentrations will be maintained. Since the change of subpopulation size is what appears to be controlling the resource concentrations in such cases, the authors appear to be violating their own "separation of timescales" assumption which they made: "since the lifetime of a cell is much larger than the timescales associated with metabolic processes… separation of timescales justifies steady-state approximation for the fast variables: (ddt)ciσ=0∧(ddt)ciext=0

F) Consortia and Cartels are never rigorously defined before they are used. The terms are typically used first and defined later. For example, Cartels are actually defined only in Figure 4 caption, and later in the Discussion. The term consortia is used in the first sentence of the subsection “Structure of consortia” in a loose sense, i.e. interchangeably with "community composition", but that is inconsistent with the use of the term in the definition of cartels as "consortia with at least p distinct metabolic classes" (Caption, Figure 4), since it lacks the important notion of optimal types, which appears in the definition in the Discussion (first paragraph).

Even after reading these sections multiple times, it seems that the authors are missing something in their verbal definitions. There is no mention of "co-optimality" in their final definition: "Cartels are defined as consortia of at least as many distinct optimal cell types – each with a fixed metabolic strategy – as there are shared resources". The definition really should include the fact that all of these types contribute to the same optimum.

It is striking that the authors neglected to give a rigorous mathematical definition of either Cartel or Consortia, for example in terms of a big set C = {σ: condition is true}.

Additional points:

G) The derivation of the growth rate function, Equation (1), assumes an assembly line for biomass in which reactions do not occur in parallel, at least for the most part. This might be fine for building up a protein in a sequential manner from amino-acids, but many other reactions that build biomass involve building blocks that can themselves be formed from other constituents along different parallel pathways.

H) Interconversion reactions, represented by Κij, could in reality involve multiple reactants, for example any metabolic reaction of the form A + B <-> C, and these would introduce non-linearities that are not captured by the equations.

I) Taking the death rate to be independent of the phenotype and the external conditions seems to be a very strong assumption Equation (6).

J) One could not tell in the last paragraph of the subsection “Competitive population dynamics” whether the simulation captures finite population size effects or not, i.e. demographic fluctuations of size 1 / N.

K) The numerical simulations do not involve mutation, in that new types are introduced randomly rather than as mutated version of existing types. One expects that mutational dynamics could have different stability criteria. Also, if a random type is introduced, presumably it arrives from outside the community, and therefore why should it be introduced in small numbers? Is that a reasonable assumption for bacteria? It doesn't seem intuitive.

L) What happens to a cartel if one member is removed? Does it matter which member is removed?

M) The word cartel has strong negative associations (i.e. drug cartels), and even at a more basic level the use of this word in the manuscript is fundamentally inaccurate, since the economic definition of a cartel is based on an agreement to control prices, instead of an optimization principle. I am not sure why the authors want to go in this direction.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Microbial consortia at steady supply" for further consideration at eLife. Your revised article has been favorably evaluated by Arup Chakraborty as the Senior Editor, Carl Bergstrom as the Reviewing Editor (Carl Bergstrom) and two reviewers.

The manuscript has been greatly improved and both referees enthusiastically recommend publication.

Reviewer #1:

In "Microbial consortia at steady supply", the authors consider a population model in which microorganisms exposed to a flux of metabolites follow different strategies concerning which metabolites to import and which to produce through conversion. They show that populations evolve to form cartels, which prevent invasion from other strategies and keep external resources fixed. Overall, I think the authors do a good and extensive job of demonstrating their results. I recommend this paper for publication.

Reviewer #2:

Taillefumier et al. present an elegant and compelling theory of microbial coexistence driven by diverse strategies for import and synthesis of essential metabolic building blocks. I found the revised manuscript to be improved over the original submission, making several changes that facilitated communication of the main results. In particular, the elaborated explanation of the dynamics of the simulation better clarifies that communities are converging toward optimal consortia (rather than being mistaken for oscillatory dynamics). Additionally, I found it reassuring that the new results using gradient-based optimization of communities arrived at similar results as the simulations that were continuously challenged with randomly sampled species types. This resolves one of my main concerns from the original manuscript, and shows that the authors' theory of optimal cartels captures essential aspects of the simulations despite extensive simplifications. Finally, the earlier definition of cartels in the Introduction aided understanding, and multiple revisions in the Discussion helped for putting the theory in context.

This is a high-quality work in theoretical ecology that makes significant progress toward the major problem of understanding microbial diversity, and I support its publication in eLife where it can reach a broad biological audience.
