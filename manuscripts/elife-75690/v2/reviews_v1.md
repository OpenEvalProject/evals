# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/04t0gwh46 Institut Curie, CNRS UMR168 Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75690.sa0](https://doi.org/10.7554/eLife.75690.sa0)

This article studies statistical aspects of the role of long-range cellular protrusions called airinemes as means of intracellular communication. The authors use published data showing how airinemes approach a target cell and describe these movements with a mathematical model for an unobstructed persistent random walk. Beyond the specialized readers interested in modeling and airineme biology, this article will also be of interest to cell biologists and biophysicists interested in intracellular communication.


---

# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/04t0gwh46 Institut Curie, CNRS UMR168 Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75690.sa1](https://doi.org/10.7554/eLife.75690.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Zebrafish airineme shape is optimized between ballistic search and diffusive search" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Elena F Koslover (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) (Reviewer#3 and reviewer#2 – point 2) Some aspects of the biological situation under study must be explained better, as early as possible in the main text:

– The authors describe the characteristics of an airineme as it would be a signalling filopodia, e.g. a nanotube or a cytoneme, which sends out to target a cell.

An airineme is fundamentally different from a self-guided cellular protrusion since it is driven by a macrophage. Therefore, it is essential to focus on the "search-and-find" walk of the macrophage and not the passively dragged airineme. In the light of this discussion, it is not clear if statements like "allow the airineme to hit the target cell" are helpful as it would point towards an actively expanding protrusion like a filopodium. Furthermore, since the protrusion tip is directed by a macrophage, contact mean that the driving macrophage must contact the target cell and attached the airineme to it. So the airineme tip has a large spatial extent (the macrophage size), which will certainly affect the contact probability. The consequence of this for the probability of establishing contact must be discussed.

– In the current version of the paper, one must go to the material method section to understand that there is a maximal length for airinemes. For clarity it should be mention in the main text, because it is an important point of the discussion of Section 2.2 and Figure 3A. Indeed it is very well known that a 2D a diffusive walker will always find any target, which makes very surprising the Figure 3A until one understands that there is a maximal length in the model.

2) (Reviewer # 1, Reviewer #3 – point 1, Reviewer #4 ) One possibly surprising results is the fact that the diffusion coefficient is optimised both for finding the target, AND for finding the best compromised between finding the target and providing directional information, while the latter must necessarily require weaker diffusion. This necessitates more explanation. Is this true in general or does this rely on the particular range of parameter explored? Is it applicable to other systems involving a semiflexible structure reaching for a target or a moving agent executing a PRW?

3) Provide a point-by-point response to the reviewers' comments appended below.

Reviewer #1 (Recommendations for the authors):

I found this to be an interesting and well-written manuscript. Most of my recommendations are along the lines of suggestions for clarifications and further discussion placing this work into context.

1) Figure 2A is not very compelling in terms of the long-time scaling. Are there any other metrics that could be shown to bolster the case for approximately diffusive behavior at long times. Velocity correlation functions perhaps? Or step size distributions over long time intervals?

2) I was persistently confused when reading the paper (until I finally found it in the methods) about the definition of contact probability. It should be made clearer in the main text that this is the probability for a fixed length of airineme that somewhere along the length (or is it just at the tip?) it will intersect a circular target.

3) Some background context is provided in the intro and discussion linking the models here to previously explored stochastic processes that are described as persistent random walks. However, as I understand it, the persistent random walk is also mathematically equivalent to a wormlike chain in the polymer physics field. Given the authors are mostly exploring fixed structures of a mechanical object rather than particles moving through time, this is an analogy that could use further highlighting. There is extensive literature available on the distribution properties of wormlike chains. For example, I believe the distribution of angular source positions (used in calculating directional information) could be computed analytically using known wormlike chain distribution functions (such as in Spakowitz and Wang, 2005). In Mogre et al., Biophys J, 2020 very similar problems are discussed in the context of a wormlike chain polymer needing to contact a target with its tip, and the trade-off between a stiff, narrow path and a more meandering one depending on the polymer flexibility. The numerical calculations done in this paper are sufficient and reasonable for the problems addressed, but drawing connections to similar past work in the discussion may be helpful.

4) It would also be helpful to the reader to provide further context on the biological function and regulation of airinemes. In particular, the PRW model here necessarily assumes that the airineme tips grow in an unguided manner (as opposed to following potential signals that indicate target location). Is there any evidence that this is indeed the case? What is the functional role of the airinemes -- what is it they transport and how? Are there diffusing molecules that move through them? Motor-carried particles? Signaling waves? Do they exert mechanical forces on the target? I realize that incorporating transport processes along the airinemes is outside the scope of the calculations in this paper, but further discussion of these issues would be helpful to place the work in context.

5) It would also help to highlight which of the results encountered are generalizable to PRWs in many different systems, not just in airinemes. In particular, the fact that the optimal flexibility both maximizes contact probability and the trade-off between contact and directional information -- is this very specific to the particular length parameter or target size picked? Or is it a general feature of PRWs? If the former, what are the parameter criteria for which this relationship holds? Exploration of this would help future researchers looking to apply these results to biologically unrelated processes that show similar PRW behaviors.

Reviewer #2 (Recommendations for the authors):

The modelling suggests that the shape of the long-range projections can be established by macrophages and thus fits their random walk model. Indeed, such a mechanism would fit very nicely to previously published data describing the chemotaxis movement of macrophages in zebrafish wound healing (Phoebe et al., 2015; Inference of random walk models to describe leukocyte migration). The authors could explore this more in detail and propose a comparative analysis of macrophage movements in different contexts.

Airinemes seem to be protrusions transferring signals to a distant cell. This would be a similar aspect as for nanotubes and cytonemes, defined as signalling filopodia. There is now a good amount of literature on nanotubes from PC12 cells (e.g. structural components) and cytonemes in zebrafish (e.g. dynamics), which deliver the signal directly to a neighbouring cell. I believe the "search-and-find mode" could also be applied to these protrusions? The authors could use their model in the context of these actively extending signalling protrusions.

The authors mention that the "shape of an airineme does not change throughout extension". However, this is an unclear expression because the shape certainly refers also to the length.

Reviewer #3 (Recommendations for the authors):

My recommendation, following the list made in the public review are

1) Discuss the robustness of the conclusion regarding optimisation. hoe can the system be optimised both with respect to optimal contact and to the balance between optimal contact and optimal directionality information.

2) enhance the discussion regarding the biology of the system. What are you really modelling? The motion of a cellular protrusion whose velocity and persistence is related to its molecular constituent (cytoskeleton) or the motion of an entire cell (the macrophage quiding the protrusion).

3) Discuss the data in more detail, in particular how well they really agree with the model.

4) Discuss the assumption of the model more precisely, in particular regarding directional information.

Reviewer #4 (Recommendations for the authors):

I have only a few remarks that could be taken into account to improve clarity of the manuscript.

In the current version of the paper, one must go to the material method section to understand that there is a maximal length for airinemes. For clarity it should probably be better to mention it in the main text, because it is an important point of the discussion of Section 2.2 and Fig 3A. Indeed it is very well known that a 2D a diffusive walker will always find any target, which makes very surprising the Figure 3A until one understands that there is a maximal length in the model.

- Again for clarity it could be useful to present Fig1B also in semi-log scales since this type of curved lines in log-log scales may simply be exponentials. Identifying an exponential law for the step size distribution would certainly lead to a rejection of Levy type walks.

Please also define clearly what is the "best fit exponent" (Section 2.1, first paragraph) : which exponent is it (I guess it is the exponent in the MSD) ? Also what is the step size shown on Fig 2B (is it the distance travelled during a specific time ?)

- To avoid any confusion, it would be useful to draw Fig5A with an airineme that is not perpendicular to the cell surface, so that there is no confusion between the angle that the airineme's tip makes with the cell surface, and the contact angle.
