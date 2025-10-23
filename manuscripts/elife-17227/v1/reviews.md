# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17227.019](https://doi.org/10.7554/eLife.17227.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Resolving coiled shapes reveals new reorientation behaviors in C. elegans" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Roland Calabrese, is a member of our Board of Reviewing Editors, and another is Gordon Berman (Reviewer #2), and the evaluation has been overseen by Naama Barkai as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this innovative short report, the authors use a computational approach in combination with video recording of movement to study turning in C. elegans, both escape turns and stochastic foraging turns. They develop an automated method for disambiguating coiled postures that builds on their previously published postural analyses that has given rise to the postural eigenmodes by PCA; there are 4 principal eigenmodes. They use this technique to describe turns and the locomotion proceeding and following as movement through the eigenmode space, showing how turns involve the third and fourth eigenmodes and basic crawling the first two eigenmodes. They then apply this techniques to show that escape turns are very stereotyped, while foraging turns have two basic forms; the conventionally recognized omega-turn (similar to the escape turn) and the newly described delta-turn corresponding to the serpentine analog of a left-right step. Moreover in foraging these turns are independent at about the same frequency and show parallel declines with foraging duration. All in all this was an enjoyable paper to read. It introduces a new technique that should be of great interest to the worm community and can serve as an inspiration for automated tracking and dimensionality reduction in other systems. Moreover, it makes a significant discovery the delta-turn that makes unbiased foraging possible.

Essential revisions:

1) The authors should emphasize more clearly in the Abstract and Discussion that the laser stimulus only elicits omega-turns.

2) There is concern that foraging in a copper ring where a nearly equal frequency of omega-turns and delta-turns were observed may not be indicative of foraging in an open petri plate, because copper serves as an aversive stimulus. Are the worms actively avoiding the copper boundary and is this influencing the performance of delta-turns?

3) The authors should clarify the developmental stage of the worms tracked in the copper ring experiments. Larval worms are more flexible than adults and this may influence the presence of delta-turns.

4.)The authors should more clearly acknowledge the early work of Croll (1976) and mention that that work reported that worms reorient randomly to dorsal or ventral side when bumping into a bead, and that their new observation may explain how.

5) The authors might do well to mention in their Discussion the neuronal basis for omega bend initiation and execution by the Bargmann lab (Gray et al., 2004, PNAS). They reported that the SMD and RIV motorneurons appear to stimulate omega bends, and that omega bend amplitude is encoded by SMD, and RIV underlies the ventral bias of omega bends. Indeed, dorsal reorienting turns were shown to occur with equal frequency as ventrally oriented omega bends (Figure 5 H) when the RIV motorneurons were ablated. These dorsal omega bends made by ablated worms in Gray et al. may relate to delta turns in intact worms in the present work.

6) We would particularly like to know how the observed eigenmodes change when including the new data as mentioned explicitly in the minor comments. It also would be interesting to determine if the fourth eigenmode shows similar dynamics to the third, as it temporally leads the 3rd (at least in the example shown in Figure 3C). Is this earlier signal (likely a head deflection) predictive of whether the worm goes into an omega or a delta turn?

7) We would like the authors to provide code for their analysis in some form (even just sample code, not necessarily beautifully-written software) so that others can more easily evaluate and use their novel methods for tracking, as mentioned in the minor comments).
