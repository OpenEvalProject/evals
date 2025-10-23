# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40986.031](https://doi.org/10.7554/eLife.40986.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Spatial control of neuronal metabolism through glucose-mediated mitochondrial transport regulation" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Timothy A Ryan (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes a general framework for examining the quantitative details of how the feed-forward control of mitochondrial motility by a downstream sensing of glucose metabolism (through OGlcNAc modification) might lead to both changes in the spatial distribution of mitochondria and the potential enhancement of overall metabolic flux that would ensue. The referees agreed that the manuscript was interesting, well-written, and timely.

Essential revisions:

1) The treatments seem to treat the OGT modification as irreversible as no terms describing the reverse reaction that would be driven by an O0GlcNAcase.

2) The authors also only consider two possible fates of Glucose 6P (glycolysis and the hexosamine pathway). The pentose phosphate pathway is another possible shunt that should probably at the very least be discussed or its omission justified.

3) A forward Euler scheme was used to solve the reaction-diffusion Equation 1. Such schemes are known to be generally unstable, so the authors need to justify their use and/or re-do the numerics with a proper scheme (e.g. Crank-Nicholson) to confirm the results.
