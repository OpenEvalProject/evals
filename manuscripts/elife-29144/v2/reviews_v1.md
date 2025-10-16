# Peer review - Round 1

Editors:
- Lee Niswander, University of Colorado Anschutz Medical Campus United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29144.024](https://doi.org/10.7554/eLife.29144.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for submitting your article "A minimally sufficient model for rib proximal-distal patterning based on genetic analysis and agent-based simulations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Lee Niswander) and Marianne Bronner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Linus Schumacher (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. However, as you will see, the work necessary to address the concerns of the reviewers may take more than the two months we normally allow for return of a revised manuscript. If you feel you can address these issues in a reasonable length of time, please draft a response letter to the editor and reviewers in which you outline the work you are prepared to undertake and a time table for its completion. The editor and reviewers will consider your response and follow with recommendations.

Summary:

This manuscript from the Mariani lab focuses on an understudied aspect of development, rib formation, using mouse genetic mutants and simulation modeling to address how proximal-distal patterning of the ribs is specified during embryogenesis. The phenotype being studied and the agent-based model to generate hypotheses to be tested in vivo are interesting and informative. A model of early Hh-mediated specification followed by expansion is invoked. Although this specification-expansion mechanism has been shown in the limb and neural tube, the current results lay an excellent framework in which to conceptualize, and model with a few simple rules, various processes from graded morphogen signals to cell death and proliferation rate in conjunction with bi-phasic specification and expansion in the formation of complex structures

Despite the enthusiasm of the reviewers for the biological question and the modeling, a number of concerns were raised and it is felt that the results and modeling only address a subset of the complex phenotype and hence the manuscript remains incomplete and only a partial explanation.

Essential revisions:

The major difference between the Shh and the Shh/Apaf1 KO mouse is the absence of distal rib cartilages after e12.5. The agent-based model ends at eE12.5, so does not take this into account. While the modeling may show decreased "distal cell" number in the Shh/Apaf1 mutant condition (it is hard to actually appreciate this outcome), the observable Sox9-expressing condensations in the distal region suggest the initial stages of chondrogenesis are "ok." Combined histological, molecular (ISH), cellular (cell death by an apoptosis-independent mechanism?) analyses may help elucidate the problems within the distal cartilage anlagen. It seems that the authors favor an idea that the pool of chondroprogenitors is so reduced that differentiation does not take place. The authors speculate the proliferation drops due to over–compensation but this is not a very satisfying hypothesis.

An unexplained aspect is that the Apaf1 somite is reduced in size by 25% around the time that Shh-mediated specification by Shh from the notochord and floor plate should be occurring. This would seem to predict that Shh could act on a greater portion of the somite and hence could specify a greater number of cells to a rib fate or lead to an increase in proximal rib fate as in Figure 6B, yet this is not observed.

Another aspect that is not explained by the model is the spatial patterning of the two segments in a Shh KO or Shh;Apaf1 dKO wherein distal chondroprogenitor are seen distally but not proximally and in the Shh KO the distal cartilage is formed next to the sternum in the absence of proximal rib cells (or proximal chondroprogenitors).

If a preprint cannot be cited, the authors should provide arguments as to why the parameters and the structure of the model are biologically plausible. Methodological details of the model are insufficiently stated, and while the code is provided, this hinders reproducibility and assessment of model justification.

Furthermore, it is not always clear in which way model outcomes and experiments were compared. For example, what constitutes "replicating the Apaf1 KO" given that this is a very small or no effect? If the point is simply that no change is observed when cell death and proliferation are lowered in concert, that is to be expected. It's fine to illustrate that with a simulation, but the point needs to made more clearly.

Was the choice of parameter perturbations to replicate gene KO an informed one, or was the parameter space systematically searched to find "best matches?

The manuscript could be strengthened by emphasizing the interplay between simulations and experiments more strongly and sooner. As it stands, there is a lot of "classic" experimental work to get through before getting to the simulations, and even then, the prediction of the simulations (about somite size and proliferation rate in the DKO) is not very clear in the figure.

Quantification of the Sox9 domain at E12.5 in whole mount was performed, but the data are not shown and the method is not described.

What is the positive control for Apaf1 KO working, given the effect is hardly seen here?

The method for quantifying the cross–sectional area is not described. How were the sections selected for analysis, what is the sample size for each genotype?

pHH3 does not appear to label many cells in Figure 7, so the biological meaning of the changes are not clear. How many sections/embryo were analyzed? How many embryos were analyzed for each genotype?

The manuscript could be shortened overall (especially the Introduction and Discussion section).

[Editors’ note: formal revisions were requested, following approval of the authors’ plan of action.]

Thank you for choosing to send your work entitled "A minimally sufficient model for rib proximal-distal patterning based on genetic analysis and agent-based simulations" for consideration at eLife. Your plan has been considered by a Senior Editor and a Reviewing editor, and we are prepared to consider a revised submission with no guarantees of acceptance.
