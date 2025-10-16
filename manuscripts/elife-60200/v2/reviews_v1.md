# Peer review - Round 1

Editors:
- Alvaro Sanchez, Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60200.sa1](https://doi.org/10.7554/eLife.60200.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In our opinion, the work presented here will have a broad influence in the field, by presenting an analytical model linking epistasis to mechanistic processes. This is important as such models are scarce. The paper is conceptually innovative, by studying epistasis in the context of a chemical reaction network, and showing how the underlying biochemical reactions constrain epistasis. This adds to ongoing efforts to more precisely understand, at the mechanistic level, how epistasis arises from microscopic processes, and as such will be of interest to a wide range of researchers in evolutionary cell biology, evolutionary genetics, and biophysics.

Decision letter after peer review:

Thank you for submitting your article "Emergence and Propagation of Epistasis in Metabolic Networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Benjamin H Good (Reviewer #1); Arvind Murugan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This manuscript investigates the emergence and propagation of epistasis in metabolic networks. To that end, the author provides a mathematical analysis of the relationship between epistasis for steady-state flux and network toplogy in linear metabolic networks. The approach is a mathematical study of the combined effect of pairwise perturbations of parameters in the set of linear ODEs that describes the system. The author considers these perturbations of microscopic reaction rates as "mutations", and the interaction between the effects is interpreted as epistasis between the mutations.

Reviewers were positive overall about the paper, but noted three important areas where it must be improved prior to being acceptable for publication. I proceed to summarize these areas where revisions are needed.

With the goal of making these criticisms as useful and constructive as possible, I also include potential solutions to the issues raised by the reviewers. Note that these are offered as suggestions.

1) Clarity: The reviewers found that the paper was hard to read and that it would benefit from a clearer presentation. Below I summarize some of the main concerns regarding this issue and provide potential solutions:

Revision #1: The manuscript uses a complicated notation and terminology to derive results that are in the end (mathematically) rather simple. This makes the manuscript hard to read, and it will limit the readership. Just remembering the notation and the exact meaning of the terms is a challenge, and this level of complexity is not necessary to derive these results.

Possible solutions: Attempt to simplify notation. State the two theorems in the main text rather than in the appendix. Simplify the notation in the main text. Consider moving Proposition 6 to the main text.

Revision #2: The Materials and methods were hard to navigate even for specialists who are familiar with the math. A better organization should help. For instance, what the reviewers looked for in the Materials and methods was – (a) how to compute the expansion in Equation 3 for a simple network and in general, (b) details to understand the results on series and parallel pathways. These ideas are not easily found in Materials and methods.

Possible solutions: Re-organize the Materials and methods section in a more modular way, with clear headings and an introduction describing what is going to be accomplished in each subsection, linking each section with the main results in the text (e.g. "Derivation of Equation X"). Organizing by such themes, working out a specific example, and following it up with the general proofs would make it more easily readable. Clearly separating proofs/propositions that get at zero-th order ideas from mathematical technicalities would help.

Revision #3: The results in Figure 1D and e.g., why negative epistasis is maintained across coarse-graining. (see text below Equation 4) were not immediately intuitive.

Possible solutions: Present explicit expressions for H, F, epsilon in Equations 3,4 for a particular simple network and then state that these results in fact hold for any topology as shown in Materials and methods.

2) Generalizability and scope: All results are derived for linear ODEs near equilibrium. The linear steady-state assumption needs to be contextualized. The scope of the study and its practical applications could be understood more clearly if the validity of this approximation were more explicitly discussed (e.g. its validity for mutations of small effect, or as a null model)

Revision #4: The linear steady-state assumptions would be appropriate for mutations of small effect. This issue should be addressed, i.e. whether aspects of network toplogy can be inferred from system-level epistasis may simply depend on the effect size of the "mutations".

Possible solutions: In addition to explicitly address the linear quasi-steady state assumption head on in the Abstract, Introduction and Discussion, the author should also evaluate the conditions where this assumption would be valid, e.g. how small do the changes need to be for the system to behave according to the theory?

3) Context: All reviewers found that the connection to previous work could be strengthened significantly, including references to key previous work.

Revision #5: The revised manuscript should include a more structured discussion of the relevant literature on gene interactions in metabolic networks and in gene-regulatory networks where the assumption of linear reactions is common. A brief discussion of Fisher's geometric model would be useful (e.g. the study by Martin (2014) Genetics should be referenced). The paper should also include a discussion of other systems where a similar “emergent” epistasis has been reported. For protein epistasis, Otwinoswki et al., 2018 made a phenomenological observation of emergence – e.g., epistasis between mutations in β-lactamase can be explained as a global non-linearity applied to non-epistatic linear trait. Sailer et al., 2017, Husain et al., 2020 give mechanistic explanations for how simple global epistasis can emerge from complex underlying interactions, closely tied to the discussion in “Inter-gene epistasis is generic”. Similarly, epistasis due to steady states, central to this paper, is similar to the arguments of Bender, Case and Gilpin, Ecology, 1984 (and later reviews by Case, Billick) in the context of (mistakenly) inferring ecological interactions from correlated variations of species abundances at steady state.

Possible fix: See the references suggested above, as well as:

Clark, A. G. 1991. Mutation-Selection Balance and Metabolic Control theory. Genetics 129: 909-923.

Fievet, J. B., C. Dillmann, and D. de Vienne. 2010. Systemic properties of metabolic networks lead to an epistasis-based model for heterosis. Theor. Appl. Genet. 120: 463-473.

Gjuvsland, A. B., B. J. Hayes, S. W. Omholt, and O. Carlborg. 2007. Statistical epistasis is a generic feature of gene regulatory networks. Genetics 175: 411-420.

Hansen, T. F., and G. P. Wagner. 2001. Modeling genetic architecture: A multilinear model of gene interaction. Theor. Pop. Biol. 59: 61-86.

Keightley, P. D. 1989. Models of quantitative variation of flux in metabolic pathways. Genetics 121: 869-876.

Keightley, P. D. 1996. Metabolic models in selection response. J. theor. biol. 182: 311-316.

Omholt, S., E. Plahte, L. Øyehaug, and K. F. Xiang. 2000. Gene regulatory networks generating the phenomena of additivity, dominance and epistasis. Genetics 155, 969-980.

Peccoud, J., K. Vander Velden, D. Podlich, C. Winkler, L. Arthur and M. Cooper. 2004. The selective values of alleles in a molecular network model are context dependent. Genetics 166: 1715-1725.

Plathe, E., A. B. Gjuvsland, and S. W. Omholt. 2013. Propagation of genetic variation in gene regulatory networks. PhysicaD 256: 7-20.

Wagner, G. P., M. D. Laubichler, and H. Bagheri-Chaichian. 1998. Genetic measurement theory of epistatic effects. Genetica 102/103: 569-580.

Jayawardhana et al. (Handling Biological complexity using Kron reduction, Mathematical Control Theory I, Lecture Notes in Control and Information Sciences, 2015)

Martin (2014), Fisher's Geometrical Model Emerges as a Property of Complex Integrated Phenotypic Networks, Genetics 197(1): 237-255.

Revision#6: Finally, reviewers also identified an issue that needs clarification. The main results appear to be derived for closed chemical reaction networks at steady state, rather than the driven metabolic networks (e.g. those with fixed input flux) that are more commonly considered in other works. This may complicate the interpretation of the results, since we do not know which findings are specific to the equilibrium assumption.

Possible solutions: The author may either (i) explicitly extend the results to allow for networks with a fixed input flux or (ii) simply rephrase key parts of the Abstract, Introduction, and Discussion to make this distinction more explicit. The author should discuss how commonly used approaches such as Flux Balance Analysis would relate to this work, and in particular whether the assumptions of FBA are covered by his model. Can the author comment on how the results would change if one used dynamic flux balance where the environment changes over time as cells grow on it?
