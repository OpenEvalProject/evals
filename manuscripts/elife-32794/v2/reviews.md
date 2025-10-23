# Peer review - Round 1

Editors:
- Sheila McCormick, University of California-Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32794.034](https://doi.org/10.7554/eLife.32794.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Why plants make puzzle-shaped cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Hardtke as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Epidermal cells on many plant leaves have complex, interdigitating shapes. The mechanism by which these complex yet robust shapes are formed, and their functional significance has been the subject of much investigation, with various interpretations proposed, all with their own merits and problems. Here they propose that the need to contain or distribute mechanical stress in cells to prevent potential catastrophic breakdown has been a primary driver in the generation of this cellular pattern, and they provide a relatively simple mechanical stress-based model by which such catastrophic stress could be automatically avoided. A major challenge in this field is to provide conclusive experimental proof, and the paper does struggle on this point. However, the large amount of data/observations provided are consistent with their model, the simplicity and robustness of the model itself (compared to alternatives which invoke local cell/cell signaling, in which the nature of the mobile signal is very unclear/contentious) makes a strong case that their model captures an important element of the patterning system, both in terms of how lobed cells are generated and the underlying reason. The quality of the Supplemental videos really brings this work to life and make their key points in a very convincing manner.

Essential revisions:

1) Incorporate discussion of "Mechanochemical polarization of contiguous cell walls shapes plant pavement cells", by Majda et al., 2017 which provides some idea about how altered cytoskeletal/cellulose patterns might feed into differential ROP2/cell wall structure, allowing lobing to occur i.e., it addresses some of the mechanistic points raised below. There may be questions about cause and effect between the two papers, but this is a discussion point.

2) Modeling results are described in a highly non-quantitative or comparative manner making it impossible to judge the robustness of outcomes against parameter variations, or which parameters are most critical. In subsection “A mechanistic model of puzzle shape emergence” it says that the main parameters are cell wall stiffness, angle at which additional connections can be made and the convexity criteria for attaching to the opposing wall and that's it. The authors state that growth needs to be isotropic for puzzle-shapes to emerge. However, it is nowhere made clear how stringent this demand is, i.e. is an anisotropy ratio of 1:1 sufficient to prevent puzzle-shapes or does it need to be 10? More quantitative data and comparisons are called for, and not phrases like "somewhat isotropically" (subsection “Isotropic tissue growth is correlated with puzzle-shaped cell formation”). At the very least the authors should:

- Give a table listing all parameters and their default values.

- Indicate for results whether these parameter values or others have been used.

- Vary for all (major) parameters the used values over a range.

- Determine how modeling outcomes depend on these parameter values.

- Analyse which parameters are hence most critical.

- Argue why the used parameter values are valid.

It might be useful to present accessible simulation runs, like those shown in their movies, with a slider for their key parameters. This would allow users to readily validate (or not) how robust their models are.

3) A key part of the model is how opposite sides of a cell (with appropriate curvature) "know" what is happening. The role of ROP2/ROP6 is reasonable, but there are still obvious holes in our molecular/structural understanding of this process. Authors might want to highlight that this is an important mechanistic "unknown" in their model. They propose that additional springs are removed if they are connecting to concave sides and added if they are connecting to convex sides. Yes, ROP2 and ROP6 are mutually exclusive, and ROP2 links to actin and expansion and ROP6 to microtubules and constriction. However, this indicates that ROP type influences local curvature, but not the other way around, i.e. that curvature determines ROP species. It will eventually boil down to this as an end result, but how is it justified to use it as a causal agent unless there is a causal link between curvature and the type of ROP species accumulating?

4) In the analysis of the spike1 mutant, the epidermal cell area seems much larger than in WT – is this true? Even if WT puzzle cells attained this size they would not be expected to show the cell separation phenotype observed in spike1. Is this true? What is the modeled stress distribution in the spike1 epidermal cells, particularly around the circumference? Could it in anyway account for the cell separation phenotype? The link between spike1 cell shape and cell separation was unclear. Can the authors clarify? In subsection “A strategy for when lobes cannot be formed” the authors imply that they mimicked the spike1 phenotype by removing ROP2 only from their model. I think SPIKE1 is meant to modulate both ROP2 and ROP6, which are proposed to act in mutual inhibition. In the model, is loss of ROP2 alone functionally equivalent to the loss of both ROP2 and ROP6? Needs clarification.

5) Another key proposition of their model is that mechanical stress is focused on particular regions of the cell circumference. Is there any evidence of localized change in cell wall composition/architecture that might allow these regions to withstand/cope with these stress points? As the authors mention (subsection “Cell shape and size across species”), one way around the potential issue of excessive mechanical stress in the outer paradermal cell wall of the epidermis is to have a thicker/stronger cell wall, and, indeed, this wall is generally significantly thicker than other cell walls. In their model, is it possible to explore how much relatively thicker this cell wall would have to be to contain the relative increase in stress predicted to occur in this wall, i.e., to prevent bursting? Linked to this point, the authors state (Introduction) that the puzzle-shape cell shape benefits the plant by "lowering the amount of cellulose necessary to keep the integrity of the cell wall". Do the authors really provide any evidence for this conjecture? They don't need to invoke this reasoning. If the models hold true, then preventing cell bursting would appear to be the key feature (unless a very minor change in paradermal cell wall thickness would solve the problem). Also linked to this, their model starts with the assumption of the wall being homogenous (Introduction). This is a reasonable place to start but, obviously, is a major simplification (cell walls are not homogenous) and there are ample possibilities for local anisotropy/structure within a cell wall. This should be made explicit. Subsection “A mechanistic model of puzzle shape emergence” and following: New springs are envisioned as cellulose, yet pure cellulose is definitely not elastic! Maybe better to say that the preferred orientation of cellulose µFs is set by this parameter? Authors should avoid suggesting that cellulose can act as an an elastic spring. At some places they say that the additional across cell springs resist elongation, whereas also in subsection “A mechanistic model of puzzle shape emergence” it seems to say they do not grow at all. So, what exactly is done with the length of these additional springs, e.g. in the updating where new ones can be added and old ones removed based on curvature, are lengths adjusted or not?

They propose that microtubules (aka additional springs) only form across the cell and not from one indentation to the next on the same side. Why is this a reasonable assumption? Because microtubules and actin do not cross? Because this would imply odd bending for microtubules? Subsection “Experimental evidence that stress needs to be managed”: Something that depolymerizes cortical microtubules interferes with cellulose deposition and thus strongly impacts wall stiffness and is not some minor thing that can be excluded.

6) In a number of the figures (e.g., Figure 3H) the authors refer to maximal stress. Do they mean maximal stress values in the outer paradermal cell wall or are these actually mean stress values calculated for all surfaces of the cell? The key point from the images is the localization of the max stress value and how this is dissipated/decreased by the change of cell shape. It needs to be clear from the figures and associated legends which "stress" values the graphs are referring to.

7) Subsection “Cell shape predicts mechanical stress magnitude” and in the Discussion section – note that in some leaves (grasses) growth is clearly anisotropic. Consistent with their hypothesis, longitudinal division maintains a similar anisotropy in the un-lobed long epidermal cells. However, in some regions of the grass epidermis (often adjacent to veins) cells do occur which have some lobing. This may reflect special topography or growth vector in this region. Main point is that not all leaves grow isotropically.
