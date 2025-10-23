# Peer review - Round 1

Editors:
- Vaughn S Cooper, University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97216.3.sa0](https://doi.org/10.7554/eLife.97216.3.sa0)

This fundamental study uses a creative experimental system to directly test Ohno's hypothesis, which describes how and why new genes might evolve by duplication of existing ones. In agreement with existing criticism of Ohno's original idea, the authors present compelling evidence that having two gene copies does not speed up the evolution of a new function as posited by Ohno, but instead leads to the rapid inactivation of one of the copies through the accumulation of mostly deleterious mutations. These findings will be of broad interest to evolutionary biologists and geneticists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97216.3.sa1](https://doi.org/10.7554/eLife.97216.3.sa1)

The authors construct a pair of E. coli populations that differ by a single gene duplication in a selectable fluorescent protein. They then evolve the two populations under differing selective regimes to assess whether the end result of the selective process is a "better" phenotype when starting with duplicated copies. Importantly, their starting duplicated population is structured to avoid the duplication-amplification process often seen in bacterial artificial evolution experiments. They find that while duplication increases robustness and speed of adaptation, it does not result in more highly adapted final states, in contrast to Ohno's hypothesis.

Comments on revised version:

The authors have addressed my prior concerns, and I have no further comments on the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97216.3.sa2](https://doi.org/10.7554/eLife.97216.3.sa2)

Summary:

Drawing from tools of synthetic biology, Mihajlovic et al. use a cleverly designed experimental system to dissect Ohno's hypothesis, which describes the evolution of functional novelty on the gene-level through the process of duplication & divergence.

Ohno's original idea posits that the redundancy gained from having two copies of the same gene allows one of them to freely evolve a new function. To directly test this, the authors make use of a fluorescent protein with two emission maxima, which allows to apply different selection regimes (e.g. selection for green AND blue, or, for green NOT blue). To achieve this feat without being distracted by more complex evolutionary dynamics caused by the frequent recombination between duplicates, the authors employ a well-controlled synthetic system to prevent recombination: Duplicates are placed on a plasmid as indirect repeats in a recombination-deficient strain of E. coli. The authors implement their directed evolution approach through in vitro mutagenesis and selection using fluorescent-activated cell sorting. Their in-depth analysis of evolved mutants in single-copy versus double-copy genotypes provides clear evidence for Ohno's postulate that redundant copies experience relaxed purifying selection. In contrast to Ohno's original postulate, however, the authors go on to show that this does not in fact lead to more rapid phenotypic evolution, but rather, the rapid inactivation of one of the copies.

Strengths:

This paper contributes with great experimental detail to an area where the literature predominantly leans on genomics data. Through the use of a carefully-designed, well-controlled synthetic system the authors are able to directly determine the phenotype & genotype of all individuals in their evolving populations and compare differences between genotypes with a single or double copy of coGFP. With it they find clear evidence for what critics of Ohno's original model have termed "Ohno's dilemma", the rapid non-functionalization by predominantly deleterious mutations.

Including an expressed but non-functional coGFP in (phenotypically) single copy genotypes provides an especially thoughtful control that allows determining a baseline dN/dS ratio in the absence of selection. All in all the study is an exciting example of how the clever use of synthetic biology can lead to new insights.

Weaknesses:

In the revised version of the paper, the authors now discuss one potential weakness of their study, which is tied to its biggest strength (as often in experimental biology there is a trade-off between 'resolution' and 'realism').

The experimental set-up leaves out an important component of the evolutionary process in order to disentangle dosage effects from other effects that carrying two copies might have on their evolution. Specifically, by employing a recombination-deficient strain and constructing their duplicates as inverted repeats their experimental design completely abolishes recombination between the two copies. This was pointed out in my first review to be problematic for two reasons:

(i) In nature, new duplicates do not arise as inverted, but rather as direct (tandem) repeats and - as the authors correctly point out - these are very unstable, due to the fact that repeated DNA is prone to recA-dependent homologous recombination (which arise orders of magnitude more frequently than point mutations).

(ii) This instability often leads to further amplification of the duplicates under dosage selection both in the lab and in the wild (e.g. Andersson & Hughes, Annu. Rev. Genet. 2009), and would presumably also be an outcome under the current experimental set-up if it was not prevented from happening?

In their revised version, the authors now address this point and with much clarity explain why their experimental system is so powerful to study the fate of a gene duplicate, not despite lacking recombination, but *because* it lacks recombination.
