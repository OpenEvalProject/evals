# Peer review - Round 1

Editors:
- Christian Rutz, University of St Andrews United Kingdom

Reviewers:
- Christian Rutz, University of St Andrews United Kingdom
- Kyle Elliot, McGill University Canada
- Yuuki Watanabe, National Institute of Polar Research Japan
- Gil Bohrer

## Review text

DOI: [10.7554/eLife.43842.016](https://doi.org/10.7554/eLife.43842.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Wind prevents cliff-breeding birds from accessing nests through loss of flight control" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Christian Rutz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ian Baldwin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kyle Elliot (Reviewer #2); Yuuki Watanabe (Reviewer #3); Gil Bohrer (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study is one of the first to examine the dynamic component of flight in wild birds, and as such represents a notable advance. It brings an exciting topic into focus, through effective combination of field observations and airflow modelling, and will likely inspire future work on a wide range of taxa.

Essential revisions:

1) Presentation: While the reviewers enjoyed the lucid writing style, there was broad agreement that the presentation of the material could be improved. Please use separate Materials and methods, Results and Discussion sections (in that order) to structure the narrative better, and: (a) include sample sizes for all datasets and analyses (number of colonies, birds/landing attempts observed etc.); (b) provide more comprehensive summaries of the underlying data (including landing success/failure data for each species); (c) report results separately throughout for the two study species (guillemots and razorbills); and (d) clarify which analyses, and inferences, are based on observational data and which ones refer to your modelling work.

2) Sampling: Your work is based on two samples of colonies from a single island (Skomer): a set of 19 colonies for assessing orientation patterns, and a subsample of five colonies for observing birds' landing attempts. Please provide more information on how these samples were selected. You say that the 19 colonies were the "main" (subsection “Data collection”) or "largest" colonies (Figure 3 legend). How were these terms defined here (spatial extend or number of nests), what was your size criterion, and why did you not sample across the full range of colony sizes (from small to large), or include all local colonies? This is important, as you use this sample to conduct formal statistical analyses (Figure 3). In fact, given the good availability of suitable data for auks, the reviewers felt it would be important to replicate distribution analyses across different islands, to rule out the possibility that patterns are driven by factors other than wind conditions (such as access to preferred foraging sites). Finally, does your subsample of five colonies (subsection “Data collection”, first paragraph; Supplementary file 1) adequately capture the full variation of environmental conditions experienced by birds on Skomer? It would also be useful to know sample sizes – in terms of sites rather than individuals – for each wind speed measurement (e.g., did all the data on the windiest day come from a single site?). Finally, if different colonies are at different locations with different ledge sizes, statistical analyses would need to account for this.

3) Modelling: For your wind speed distribution, you use a normally distributed variable. Wind speed is only positive. Wind velocity at each of the 3 spatial components can be negative, but the bird does not care if the wind goes left or right – that makes it just as hard to land. You assume, correctly, that the birds are affected by the speed of the wind vector, and the speed [sqrt(sum(ui^2)) |i=1:3] is a positive property. Please use log normal distribution for W, which presumably will affect Equation 5.
