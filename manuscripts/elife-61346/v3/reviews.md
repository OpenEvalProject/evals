# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61346.sa1](https://doi.org/10.7554/eLife.61346.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper lies out an interesting framework to think about the consequences of immune memory. The central tension is one between memory cells with high affinity for a narrow range of antigens and lower affinity but broader spectrum that can deal with evolving pathogens better. The reviewers appreciated the combination of abstraction, involving thermodynamic and information theoretic frameworks and the grappling with specifics of immune memory.

Decision letter after peer review:

Thank you for submitting your article "Optimal evolutionary decision-making to store immune memory" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kayla Sprenger (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. As promised in the introduction, the authors could comment on how their approach could be applied to memory T cells in future work, even if the dynamics of such memory is different. (Reviewer 1)

2. Improve Figure 1 so it defines the model more comprehensively without the reader having to consult the Methods section. (Reviewer 1)

3. Cross-reactive Abs are observed to take long to evolve. But the authors results seem to suggest that much cross-reactivity is evolved early in the affinity maturation. The authors should clarify. (Reviewer 2)

4. How would the assumed lifetime of memory B cells affect your results? It appears you have assumed that memory B cells persist through the lifespan of the organism. A discussion of how your results would change if memory lasted for less time would be useful. (Reviewer 2)

Reviewer #1:

In this article, Schnaack and Nourmohammad explore the dynamic constraints in triggering optimal immune responses to eradicate infections. The optimization balances the need for higher affinity (higher specificity/efficacy in clearing pathogen) and cross-reactivity (better response to evolving pathogens). The key paradox being addressed here is that, depending on the speed of evolution of pathogens, the immune system can tune the specificity of the lymphocytes' receptor that are selected e.g. by adjusting the size of low-affinity of the memory lymphocyte compartment.

Given that the formalism is quite abstract (e.g. definition of antigenic distance in the shape space), it is hard to assess how experimentally testable the results are. The authors make a good attempt at discussing their main insight and it is certainly thought-provoking: they found that the number of exposures to a pathogen, as it relates to the age span of the organism under consideration, is a critical parameter to decide the amount of cross-reactivity stored in memory leukocytes. This is the strongest insight as it relates to experimental results.

There are theoretical surprises as well: the bimodality of receptor specificities that get selected when pathogens are very diverse at the antigen level is thought-provoking. The authors do point out that this may relate to experimental observations for B cells (mixed populations are selected with or without class switching).

Overall, this is a very well written and insightful manuscript leveraging results from non-equilibrium statistical physics and accounting for varied strategies for the immune system.

Reviewer #2:

This manuscript features a novel mathematical model for investigating how the immune system optimally stores memory of B cell receptor-pathogen interactions in order to maximize protection against future pathogens with diverse evolutionary rates. Results support recent experimental findings that B cell differentiation into memory cells is strongly regulated during the affinity maturation process and that the kinetics and energetics of an immune response are simultaneously optimized to ensure an effective response. Unique insights are also provided into the immunological phenomenon of original antigenic sin, such as the effect on this phenomenon of organismal lifetime, which is also explored in the context of optimal memory storage strategies.

Strengths:

The presented mathematical framework is rigorously constructed such that meaningful insights can be gleaned into the workings of the adaptive immune response to evolving pathogens. The framework combines fundamental concepts from information processing and equilibrium and non-equilibrium thermodynamics with concepts from probability and statistics in a unique and thoughtful way. The conclusions appear to be well-aligned with recent experimental findings, providing validity for the model and for the subsequent predictions that are made on optimal memory storage strategies for organisms with varying lifespans.

The results provide useful insights into longstanding questions in immunology, such as whether cell fate decisions on memory B cell differentiation are regulated during the process of affinity maturation, and into the origins of original antigenic sin from an immune response perspective and potential mitigation strategies. With regards to the former point, the model accurately reproduces recent experimental findings showing differentiation into memory B cells during affinity maturation is indeed highly regulated. This thus sets a bar for future computational models of immunological memory processes and affinity maturation to incorporate this feature, rather than assuming differentiation into memory B cells is stochastic and carried out at a constant rate throughout affinity maturation, which is currently a common assumption.

Broad parameter regimes are explored, rendering the findings potentially relevant for infection scenarios with diverse pathogens.

Weaknesses:

Typically, cross-reactivity or equivalently breadth takes a long time to evolve, as evidenced by the fact that broadly neutralizing antibodies (bnAbs) arise only after many years of infection (or re-infection) by an evolving pathogen. Arguments are made by the authors that memory B cells are preferentially produced early on in the affinity maturation process, and that memory B cells are also preferentially stored with intermediate cross-reactivity, which would seem to imply that a good deal of cross-reactivity can be evolved early on in the maturation process. These arguments would seem to be at odds with the concept of bnAb evolution and thus warrant some clarity.

Two additional points that may warrant some clarity are:

(1) How much the results, especially in the context of organisms of varying life spans, depend on the presumed assumptions that memory B cells have a lifespan that persists throughout the lifetime of the host (seems to still be somewhat of an open question) and that immunological memory does not decay with time, and;

(2) the role of B cell precursor frequencies in the decision-making process of mounting a memory versus naïve B cell response. The authors define an effective deliberation time for the naïve B cell population to reach a level of activity that is similar to the memory B cell population, based on the argument that memory B cells "can respond quicker and in larger numbers" than naïve B cells. However, one could imagine a scenario where the memory B cell response is quickly outcompeted and overshadowed by the naïve B cell response due to the high precursor frequencies of the naïve B cells.

The impact of the paper could potentially be heightened if some discussion of how the principles gleaned on optimal immune memory strategies could be translated to, e.g., vaccine design against fast-evolving pathogens.

General comments:

1. Lines 60-61, It is stated that "as in most molecular interactions, immune pathogen recognization is cross-reactive". I am confused by this statement, as many molecular interactions are indeed not cross-reactive (e.g., lock-and-key binding of enzymes and ligands, etc.). Immune-pathogen recognition would also not typically appear to be cross-reactive unless the pathogen is highly mutable or there have been multiple infections of an evolved pathogen, so this sentence further confuses me. Please note that if the sentence is kept as is, I believe the authors meant to use "recognition" instead of "recognization".

2. Besides the concept of original antigenic sin, could the concept of immune imprinting where immune memory is biased over the lifetime of an organism also be captured by or incorporated into this model somehow?

3. As it appears to be defined, antigenic divergence characterizes two distinct infections by a given pathogen. How relevant is this model and its results for a pathogen like HIV that mutates within its host, where a range of antigenic distances/divergence values quickly become relevant for a single infection?

4. Line 142: in what kinds of scenarios (or against what types of pathogens), might prior preferences be important to consider? To clarify, all of the analyses carried out here assume no prior preferences?

5. In regard to Equation 2, it would seem that the same maximum net utility value could be obtained with either a particularly high expected utility or a particularly low Kdiss. Would the optimal memory protocol look different in these two cases, despite them having the same net utility value? Perhaps this is already addressed, but the answer is not immediately clear to me.

6. Lines 215-218, it is stated that "This optimization [for the case of moderately evolving pathogens] results in a smaller deliberation factor 𝛽 compared to the scenario with slowly evolving pathogens, yet a long enough deliberation to allow the energetically suboptimal memory to react to an infection". This appears to be true for a range of δ about 0.1-0.5. Yet, still within in the defined range of δ for moderately evolving pathogens, δ values between about 0.6 and 0.8 for the lower amplitude cases appear to result in 𝛽 values above those for slowly evolving pathogens. Can the authors please clarify this?

7. Line 104, it is not clear what is meant by the statement that "Physico-chemical constraints in protein structures can introduce a tradeoff between immune receptors' affinity and cross-reactivity". Is this tradeoff not determined by the antigenic divergence that an immune system encounters upon a new infection compared to a past infection?

8. Lines 251-254, the last sentence seems to imply that a moderate amount of cross-reactivity or equivalently breadth is achieved early on in the affinity maturation process. This conflicts with my understanding of the evolution of broadly neutralizing antibodies, which typically arise only after many years of infection/pathogen mutation within a host. Can the authors please comment on this? In addition, I was under the impression that broadly neutralizing antibodies are typically class-switched, i.e., not of the IgM type. Is their evidence that the cross-reactivity of IgM receptors produced early on in affinity maturation is really effective at 'countering evolving pathogens' (lines 279-282)?

9. In the last Results section on the effect of infection frequency, and perhaps in general throughout the manuscript, is the assumption made that memory B cells persist for the entire lifetime of an organism? Some studies have placed the half-life of memory B cells to be only between 8 and 10 weeks, and others up to or possibly beyond 2 years, and still others for the lifetime of the host but requiring constant renewal through antigen-specific stimulation. How might changes in the expected lifetime of memory B cells affect the optimal memory strategies that are presented?
