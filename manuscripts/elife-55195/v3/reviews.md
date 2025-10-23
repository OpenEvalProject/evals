# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55195.sa1](https://doi.org/10.7554/eLife.55195.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article presents a compelling example and analysis of how collective intelligence can lead to the accomplishment of nontrivial tasks. Specifically, the authors show that the method that crazy ants use to move food across complex landscapes involves a sensing range that extends to the group rather than just the individual. As foraging is often described as a random walk, the authors develop several models and show that one that invokes an extended sensing range successfully recapitulates the search paths found in the animals. They also present a theoretical analysis of percolation theory, showing that sensing should extend up to the logarithm of the system size.

Decision letter after peer review:

Thank you for submitting your article "Ant collective cognition allows for efficient navigation through disordered environments" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Gordon J Berman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Adam J Calhoun (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Aviram et al. examine a collective navigation task where longhorn crazy ants are required to transport a large object through a maze-like environment. The task requires cooperation between ants, both to transport the object as well as to find an efficient path out of traps. The authors show that: (1) ants are able to successfully complete the task, even for dense mazes close to the no-solution limit; (2) a simulated biased random walk does not solve the problem as it gets trapped, and argue that the solution requires a non-local sensing component; (3) this non-local sensing is performed by leader ants, which sense an extended area and lead the ants out of traps; (4) a biased random walk with this additional component performs similarly to the ants in simulations; and (5) theoretical arguments which reveal that an extended sensing radius that scales logarithmically with maze size is sufficient to perform this task.

Although the reviewers agreed that the work was of sufficient quality to merit consideration, several major points need to be addressed – enumerated below.

Essential revisions:

1) There was much confusion about the choice of the 10 cm sensing radius. First, Figure 2D shows that "non-local, responsive" algorithms with an extended sensing radius of 20 cm are a factor 10 worse than the ants' performance, which directly contradicts Figure 2C's plot for the extended pinball model, which shows similar performance to the ants. The authors should clarify why this is the case. Moreover, it's unclear what should be taken from Figure 2D, particularly since the simulations discussed in that figure are not discussed until a later section. Second, the simulation results depend strongly on extended sensing radius rsense, which is taken to be 10 cm. The 10 cm is based on the results on ants in traps shown in Figure 3. Importantly, from Figure 3A, it is unclear how rsense is 10 cm, while the scale bar of 5 cm clearly indicates a rsense less than 5 cm. Moreover, the Log(N) label for the heatmap is ill-defined (what is N? what is the base of the Log?)

Is 10 cm supposed to be optimal? Is the prediction that the sensing range has to do with the size of the system found in the natural world, or that it changes with the size of the system that is presented experimentally?

2) The theoretical work is interesting but seems disconnected from the rest of the paper. A connection between the assumptions in the model and the experimental setup is not clearly made. A ballpark estimate from the theory with experimental numbers is also not presented. In general, the reviewers felt that more scaffolding material is needed to tie-in the theory with the experiments/simulations. Specifically, the paper could benefit from having an expanded discussion of the theory in the main text. The general gist comes across, but the reviewers didn't really have a sense of what was going on until they read the supplemental section.

3) On a similar note, it would have been nice to see a slightly longer summary/Discussion section putting the work into context. The reviewers thought that the ideas proposed are strong, but would benefit from a more thorough explanation. In particular, the reviewers felt that more connections to the biological literature were necessary, pointing-out the biological implications of the findings in a more thorough manner.

4) On the whole, many of the figures are difficult to read – the labels are small and in many of the supplementary figures, the legends are impossible to see. The error bars are barely visible. The color schemes are also confusing, for instance, in Appendix 2—figure 2 where both blue and turquoise are used. We ask that the authors extensively modify the figures for clearer presentation.
