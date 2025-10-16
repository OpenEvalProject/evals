# Peer review - Round 1

Editors:
- Vikas Nanda, Rutgers University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40308.027](https://doi.org/10.7554/eLife.40308.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Evolution of Environmentally-Enforced, Repeat Protein Topology in the Outer Membrane" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Vikas Nanda as Guest Editor and Detlef Weigel as Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Vikas Nanda (Reviewer #1).

Our decision has been reached after thorough consultation between the reviewers. The problem of membrane barrel evolution is a very important one that is challenging due to constraints of the membrane environment, repeat structure and low-complexity sequence on evolution; however, there were a number of concerns raised regarding the size of the data set and lack of statistical power to support the conclusions drawn. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Reviewer #1:

The emergence and evolutionary divergence of OMBBs is a fascinating problem due to the highly regular topology (tandem up-down β-hairpins, even number of strands). The authors combine sequence alignments with structural insight to propose a novel, compelling model for how OMBBs evolved. The evolution of repeat proteins is challenging as Elofsson has shown where the evolutionary and structural repeat unit do not necessarily coincide. In Slusky's study – the barrel evolution is more highly constrained than one might expect. A number of new and interesting observations are made in this study, such as the placement of 8-stranded barrels at the root of the OMBB tree, and all other barrels contain evolutionary traces of the original 8-stranded motif. Despite strand amplification being the most compelling mechanism for OMBB diversification, it appears the fixation of duplications was rare. I thought the insight of loop-topology as the primary constraint on the ubiquitous even-strandedness to be quite insightful – this makes a lot of sense.

I found the proposed transitions between 16- to 18- stranded barrels (Figure 5) to be interesting, but difficult to imagine occurring through processive single mutations. A number of concerted mutations would have to occur to convert loops into strands and vice-versa. How would transitions in the 'large rearrangement' mechanism for example be viable? Might such transitions come from multi-residue indels, rather than successive single amino acid changes?

I was hoping for some answer to the mystery of the missing 20-stranded barrel Understandably, it is harder to explain absence evolutionarily. It seems the same processes that lead 16 to 18, could also lead 18 to 20. Likewise, if 8 can go to 14, 14 can go to 20. If 8 can go to 12, 16 can go to 20. >3 amplification steps are not required with the proposed evolutionary model. Perhaps the answer lies in the rarity of amplification events overall and 20 has not been sampled.

Reviewer #2:

The authors study OMBB path of diversification by tracing sequence alignments among their solved structures and finds some intriguing patterns which seems to fit in a story about the evolutionary mechanism of these proteins. Although the story looks plausible, some evidences and statistic tests should have been done to support it.

1) Because the study focuses on structurally resolved proteins, this creates a bias towards sequences/families that have been studied structurally. There is also a bigger issue about the number of structurally resolved OMBBs, 130 structures are too less for an evolutionary study. Most evolutionary studies start with several thousand sequences.

2) The author's claims highly depend on the similarity between proteins/strands, which highly depends on the cut-off E-value of the alignments. This cut-off determines how significant the found patterns are. Since the paper says most β-barrel proteins are homologous (Introduction), I would expect a very low E-value cut-off should have been used in the study. Instead, the paper uses some relatively large values (10-1~10-3). Certain statistic tests or at least some explanations are required to justify the usage of such E-value cut-off.

3) The OMBBs with 22 strands do not seem to be evolutionary related to other OMBBs at lower e-values. Even at e-value of 10-2, a large number of 22 OMBBs do not align with 14-stranded OMBBs. How can the 22 strands BB evolve so fast that they no longer can align with 14 strand OMBBs? Supposedly the 14 to 22 strand evolutionary event is a relatively new one.

4) The paper finds some interesting patterns that connect β-barrel proteins with different sizes together. However, all the results shown look like case study, and few statistics are reported to show how prevalent and significant these patterns are in this protein population.

Here I list only one example to show this issue. In subsection “Internal repeats”: "The 12-, 14-, 18-, and 22-stranded barrels have single hairpin shifts. The 8- and 16- stranded barrels sometimes have double hairpin shifts and sometimes have single hairpin shifts." What are the percentages of the 12-, 14-, 18-, and 22-stranded barrels that have single hairpin shifts and what is the "sometimes" for 8- and 16-stranded barrels are not clear. Concrete numbers should be reported instead of descriptive language.

5) What mechanism was responsible for events that do not involve complete gene duplication? e.g. 14 to 22 strands. The authors should consider mapping the TM strands on to the exons and explore if exon duplication might be one of the mechanisms that achieves this?

6) The authors should comment if an event similar to that of converting an extracellular facing strand to a periplasmic-facing strand has been observed in α-helical membrane proteins.

7) The writing needs a lot of improvement. The English of the paper is neither plain nor scientific. Just one example (subsection “Step 1”) to show this:

This manifests as "at least some" of the 8 strands of the 8-stranded barrels "almost always" (150/151 cases) aligning with "at least some" of last eight strands of the 10-, 12-, and 16-stranded barrels such that strand 1-"when it aligns"-aligns to the 8th to the last strand, and strand 2 to the 7th to last strand, 3 to the 6th to last strand, "etc.".

A sentence in a scientific paper should not spans four rows accompanied with a lot of vague terms (shown in quotes above) but lacking concrete statistic numbers, can make any point clear. And this is not an isolated case.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Evolutionary Pathways of Repeat Protein Topology in Bacterial Outer Membrane Proteins" for consideration by eLife. Your article has been reviewed by Detlef Weigel as the Senior Editor, a Reviewing Editor, and three reviewers.. The following individual involved in review of your submission has agreed to reveal his identity: Vikas Nanda (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

It is appreciated that large, complex proteins likely evolved through duplication or fusion of smaller ancestral domains. In the case of OMP β-barrels, the exclusive repeat of a β-hairpin like structure suggests that modern multi-stranded barrels emerged through a series of hairpin repeats. This work carefully examines that idea using network analysis and state-of-the-art sequence analysis methods based on hidden Markov Models (HMM) of the families represented by known structures, in order to examine sequence relationships and the origins of structural expansion. To date, the understanding of β-barrel fold evolution has been based on the careful work of Remmert et al., (2010), which showed that the β-stranded hairpins represents the primordial evolutionary unit that expanded through duplication events. This work builds on this basic framework and provides evidence for additional, alternative pathways for evolution of hairpins, for example, by insertion of loops.

Central conclusions:

1) Greater similarity is observed between barrels of the same strand number versus those of different size, indicating that hairpin amplification events are rare relative to mutational changes.

2) Alternative mechanisms for strand amplification are identified including loop-hairpin transitions and large-scale strand rearrangements.

3) The progression from ancestral 8-strand barrels to larger barrels proceeded through a set of defined intermediates of increasing strand number.

4) The C-terminal region of OMPs are most conserved across barrels of different strand number, suggesting a conserved folding-nucleation domain that can be traced back to the original family of 8-stranded barrels.

The reviewers find the study to be timely, rigorous, thoughtful, and well written and presented.

Essential revisions:

There was discussion among the reviewers regarding the extent to which including predicted secondary structure information would improve the analysis. Reports of secondary structure prediction as high as 87% have been reported (Ou et al., 2010). It’s unclear to what extent the assignments of evolutionary relationships would be sensitive to precise strand boundary definitions. We would like the authors to consider this question and justify the choice of eliminating sequences where structural data are not available.

Other points to be addressed:

1) "E-values are always lower among barrels of the same strand number than between barrels of a different strand number." Can the authors be sure that this is due purely to similarity, or is there a concern that either the cost of inserting gaps or the greater number of expected alignments adding to noise when using a shorter query to probe a longer target? This may be accounted for in the analysis, but it was not obvious how it was handled. Related to this, is it possible whether the lack of connections from the largest barrels (18- and 22-stranded) to the smallest (8, 10, 12-stranded), might reflect challenges to the scoring schemes when such length differentials are present. How sensitive are the results for these particular connections to lowering of the thresholds? A comment as to the reasons for choosing E <= 10-3 for selection of the cases in the prototypical barrel group (Results section), would be helpful.

2) The conservation of 8 strands throughout the barrel families (depicted in Figure 4) is fascinating, particularly because one would expect that larger barrels would require larger amino acids to enforce the curvature of the barrel circumference. Since the authors know the register of the HMM profiles with respect to structure, can it be said whether this conservation is due to core vs surface residues? Either way – it would inform the discussion regarding the mechanism of folding. A conserved folding nucleus would imply core facing residues are conserved. A conserved surface would imply a different transition state in the presence of the BamA machinery. Of course, both could be true.

3) The authors are using 3D structure of the proteins to gather the strand start and strand register values. It is not clear to how the authors address the artifacts introduced in the X-ray structures. For example, crystals for BamA from Salmonella and Haemophilus ducreyi have been resolved (5ORI and 4K3C respectively). Strands 1 and 16 in both structures have significantly different lengths (3 and 5 in 5ORI and 8 and 10 in 4K3C). How is this resolved?

4) In "Transition from 14- to 22- stranded barrels", the authors claim the 18- stranded barrels do not have plugs. This is incorrect, most barrels > 10 strands have in-plugs.

5) Why are the barrels > 22 strands not included in the study (PapC, 2vqi; FimD, 3rfz; LptD, 4q35)?

6) For the average polarity and hydrophobicity of the loops and strands, it would be useful to have a control in a different region of the protein, as well as standard deviations to get a sense of the variability of these values in context.

7) It would be best if the in-house software Polar Bearal (subsection “Polarity alternation and hydrophobicity calculations”) were made available through GitHub or a similar portal.
