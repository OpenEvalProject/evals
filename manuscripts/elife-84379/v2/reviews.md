# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84379.sa0](https://doi.org/10.7554/eLife.84379.sa0)

This manuscript presents an important mathematical analysis of metabolic "co-substrates" and how their cycling can affect metabolic fluxes. Through mathematical analysis of simple network motifs, it shows the impact of co-substrate cycling on constraining metabolic fluxes. The combination of mathematical modeling and comparisons with existing data from previous studies offers convincing support for the potential biological relevance of co-substrate cycling. The work will be of interest to researchers who study microbial metabolism and metabolic engineering.


---

# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84379.sa1](https://doi.org/10.7554/eLife.84379.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Dynamics of co-substrate pools can constrain and regulate metabolic fluxes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Babak Momeni as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jonas Cremer (Reviewer #2); Silvio Waschina (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please include the terminology and basic concepts in the introduction to improve the accessibility of the paper.

2) Please revise the manuscript to explicitly include the relevant model assumptions and details of the setups (see individual reviewer comments).

3) Please further address the limitations of the study in the Discussion section (see comments from Reviewer #3).

Reviewer #1 (Recommendations for the authors):

1. Although the definition of cycling is somewhat intuitive, I do not think the formal definition offered in lines 84 and 85 is accurate. I'd suggest revising it (e.g. with A -> B -> C and D -> B -> E, B is produced and consumed via different reactions, but with no cycling).

2. One of the main theses in this manuscript is that limitations by conserved pools in cycles will impact the overall metabolite dynamics. It would be nice to have an estimate of how often cycles will impose a limitation and where they should be expected in the metabolic network. Figure 3 and associated supplementary figures perhaps contain this information, but if possible, a more explicit estimate would be informative.

3. In Figure 3B-D, I do not think that the correct model for the relation between the pool size and the normalized flux is a linear dependency (presumably when the pool size is large enough, the flux will saturate). Should this be taken into account instead of a regression line (and RMSE) for representing whether the model fits the existing data?

4. On lines 245-245, I think the second hypothesis should be phrased more explicitly. It is not immediately clear what "balancing" means.

5. In Figure 5, a simpler configuration can be imagined in which there is no direct reaction between A0 and A1. Presumably such a configuration creates an even stronger dependency between the two pathways through cycling A0 to A1 and vice versa. I am curious why the authors did not choose such a configuration. Alternatively, with the A0 <-> A1 reaction included, what is the impact of the rate of this reaction on the correlation between the two pathways?

Reviewer #2 (Recommendations for the authors):

– Overall, the paper is well written and I was able to follow. However, it also assumes that readers are familiar with a lot of different terminology/examples of metabolic analysis. Below are some remarks that the authors might want to consider. For example, I think the introduction would benefit from a more detailed introduction of terms. For example, a clearer definition of co-substrates in the introduction would be helpful. Similarly, a better introduction of the term flux would help and yield is not introduced such that it remains unclear for readers to see what the tradeoffs are.

– line 46 onwards: What is the evidence? Can a sentence or two be added to clarify?

– line 84 onwards: It seems this paragraph is still part of the introduction.

– Too early reference to Figure 1A (is it Figure S1A). Better to show a summary figure illustrating the different co-substrates mentioned?

– line 101 onwards: paragraph could be better embedded and it is currently hard to follow what the authors want to stress when the following discussion is primarily about steady state.

– line 113 onwards: I think it would be helpful to spell out in the main text what α is.

– line 180 onwards: I am missing background to understand the statement. It was always my impression that it is in general very hard to reliably measure reaction rates in-vivo (kin and Vmax), so how can one establish that kin < Vmax?

– ll 187 onwards: some essential details are missing to understand the type of dataset used (see above).

– It is also important to introduce in more detail the different experimental conditions for which the variation in ATP precursors has been observed. Could it be that ATP levels are merely changing because of the way the conditions change and not because fluxes vary as well?

Reviewer #3 (Recommendations for the authors):

Mathematical equations, transformations, resulting constraints, and conclusions are generally very clearly explained, which allows readers, who might be less-accustomed to kinetic modeling, to follow the line of arguments. One suggestion I have is to provide units of variables that are used in equations also in the text, or perhaps as a (supplementary) table. Specifically, I noticed that this could help readers already at equations (1). Here, the steady-state concentration of m1 is given by the ratio of the two rate parameters k[in] and k[out]. Since in the text, both parameters are only referred to as "flux rates", one could assume that both have the same unit, which would make their ratio (=m1 concentration) unit-less. Only with the units that appear later in figure 2 (k[in] in the figure itself; k[out] in the caption) it becomes clear that the two parameters have different units.

In addition, I understand that the authors claim, that flux-governing and -regulation through means of co-substrate cycling could be a general 'design principle' that is not limited to a specific group of organisms. However, I would suggest to provide more detail on the experimental/FBA data (i.e. fluxes, kinetic parameters obtained from BRENDA) that is used for the comparison with the model predictions. For instance, details on the organisms behind the experimental data that is mentioned e.g. in lines 187-208 and in Figure 3 could be added. This would help readers to put the authors' results in more biological context. Along those lines, the discussion could include a paragraph that addresses current limitations to further evaluate the developed mathematical framework. For instance, from which organisms do we have experimental data to study the potential role of co-substrate cycling using the developed framework? What future experiments/data types will further help to test the mathematical framework?
