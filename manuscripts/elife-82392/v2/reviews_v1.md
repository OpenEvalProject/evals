# Peer review - Round 1

Editors:
- Richard A Neher, https://ror.org/02s6k3f65 University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82392.sa0](https://doi.org/10.7554/eLife.82392.sa0)

Sanderson developed novel interactive software for visualizing phylogenetic trees representing millions of sequences. This is a fundamental advance over previous software that is typically limited to trees with a few thousand tips. Taxonium has been used intensively by the virus evolution community over the past months and has thus already proven its utility and performance.


---

# Peer review - Round 1

Editors:
- Richard A Neher, https://ror.org/02s6k3f65 University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82392.sa1](https://doi.org/10.7554/eLife.82392.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Exploration of million-sequence viral phylogenies with Taxonium" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Richard A Neher as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Neil Ferguson as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Art FY Poon (Reviewer #2); James Hadfield (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers agreed that Taxonium enables the interactive exploration of phylogenies orders of magnitude larger than what was possible before and represents an urgently needed technological advance given the large volume of SARS-CoV-2 data that was generated over the last 3 years. The reviewer comments mostly represent clarifications and suggestions for a more precise description of the tool, its scientific context, or prior work. The most essential revision is the following:

We would like to see a more detailed description of the "sparsification" algorithm. How are the tips selected that is being rendered? how does this interact with the search? Could this (possibly as in future development) be made dependent on metadata (hosts, geography)?

In addition to improvements to the manuscript, the reviewers have identified a number of points that might be useful to consider during the future development of Taxonium.

Reviewer #3 (Recommendations for the authors):

Terminology: the term "nodes" is used in the manuscript to represent tips (as far as I can tell), whereas this typically refers to both internal nodes and terminal nodes (tips).

Examples: "Taxonium scales to trees with millions of nodes' and "NextStrain analyses are typically limited to ~4,000 nodes". I suggest changing to "tips" or "terminal nodes".

The introduction talks about 11 million sequences, but Cov2Tree only uses the NCBI set (~6 million). I presume this is due to GISAID data-sharing conditions and not a technical limitation of Taxonium. This is a delicate situation however it was strange to introduce the former but then present the latter.

The following points should be thought of as suggestions to improve Taxonium rather than requirements for publication:

– A legend to explain the colours is needed – you essentially add this in Figure 3 but it should be part of the software.

– Panning of trees (x + y direction) is intuitive but it's easy to get lost and pan the tree off the screen! It should be possible to prevent panning outside the bounds of the tree.
