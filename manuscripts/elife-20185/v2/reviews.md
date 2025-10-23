# Peer review - Round 1

Reviewers:
- Russ Fernald, Stanford University , United States

## Review text

DOI: [10.7554/eLife.20185.022](https://doi.org/10.7554/eLife.20185.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Locally-Blazed Ant Trail Achieves Efficient Collective Navigation Despite Limited Information" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors describe navigational decisions of Paratrechina longicornis ants cooperatively transporting a large food item. In contrast to other species and this species in other circumstances, these animals use a locally-blazed trail, marking short segments beginning at the site of the load. Subsequently, animals may lose the guiding trail but successfully regain their direction using partially available information. In doing this experiment, the authors' used side view cameras allowing detection of putative scent marking activity over a large two-dimensional surface.

The reviewers had some concerns that need to be addressed in the text:

1) There is some concern that the authors did not experimentally test or validate a prediction from the model. And that in the Discussion, other examples of animal cooperation (e.g., birds, bats wolves, etc.) could be compared and contrasted.

2) Each ant makes its own decision, independently of other ants, so the problem seems to require additional mechanisms to keep the individual's cohesive with the group. How is this accomplished? How does it affect the PF algorithm, and its performance? Does the algorithm require a leader?

3) Are there any biological predictions that can be made from the model? For example, values of model parameters, or their relationships? Theorems suggest a very precise relationship between some of these parameters (λ, mu, q, etc.) in order for the algorithm to work. Does this relationship also hold true for ants? While it is always difficult to relate complex biological parameters to abstract model parameters, this would at least provide some feedback from the model back to learning new biology. Moreover, the model assumes parameters values are fixed, but the data seem to suggests that ants likely change their behavior when an obstacle is reached, preferring to explore more. Isn't this an important biological factor to consider?

4) Third, it's not clear what the role of pheromone is in this model when an ant decides its next move. For real ants, it seems like pheromone may be important and is what contributes to the fact that the classical trail is stable over a long time, whereas the locally-blazed trails are less stable. How does this interface with advice (which seems like a distance-dependent marker, and not a typical pheromone marker indicating previous activity)? Are there possibly different pheromones?

5) Fourth, the analysis of MANETs demonstrates a real-world application, but is this necessary? If this is to be included, the authors need to compare their algorithm with state-of-the-art MANET routing algorithms (e.g. gossip algorithms). Figure 4D–E shows a stretch of 10-50x, which seems quite bad to me, but maybe it isn't. Without a comparison, it is difficult to appreciate Figure 4D–E, and it doesn't provide any evidence that the probabilistic algorithm the authors suggest is valuable to this well-established community.
