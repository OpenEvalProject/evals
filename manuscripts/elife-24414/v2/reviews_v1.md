# Peer review - Round 1

Editors:
- Edward G Ruby, University of Hawaii , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24414.040](https://doi.org/10.7554/eLife.24414.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Host-selected mutations converging on a global regulator drive an adaptive leap by bacteria to symbiosis" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and we have drafted this decision to help you prepare a revised submission. The verbatim comments of the reviewers are attached as well.

Summary:

This is an impressive example of bacterial experimental evolution in a host setting, identifying mutational change of a regulator as key for symbiotic association. It is the first description of adaptive significance of particular binK alleles for V. fischeri symbiosis initiation and persistence in E. scolopes, based on work with in vivo squid-host evolution system. The standard is exemplary: multiple lines of evolution, re-sequencing of original and full sequencing of all resulting strains, etc.

Essential revisions:

The major weakness of the work is that it potentially aims to do too much. The transcriptome (and several other) sections appear ancillary and distract from the core findings. These should either be removed or (preferably) moved to supplementary material. Similarly, binK phenotypes that do not connect to the rest of the story should be left out of this paper, and published once there is a clearer understanding of them. Such focusing will also help pare down the 10 pages of Discussion, which contains far too much speculation, mostly about the weakest findings.

Additional points: The reviewers raise many points regarding the presentation and Discussion (see below). Please pay attention to these in your revision, but note that there is no need to enumerate all your responses in the "response to reviewer" letter that will accompany your revision, only those where you disagree with the reviewers and are planning not to follow their advice.

Reviewer #1:

This article is appropriate for publication in eLife. I am in favor of publication because the article is the first description for the adaptive significance of particular binK alleles for V. fischeri symbiosis initiation and persistence in E. scolopes. The authors leverage their experimental, in vivo squid-host evolution system to arrive at this result; this application is a relatively novel and clever use of the system and should be a standard by which these sorts of experiments are performed (multiple lines of evolution, re-sequencing of original and full sequencing of all resulting strains, etc.). Furthermore, the authors have done a thorough job of characterizing multiple effects that a particular binK allele has on symbiosis-associated characteristics in the system – pushing knowledge of the importance of regulation of biofilm-associated phenotypes ahead in this system specifically and host-bacterial symbiosis in general.

The above written, the authors could be much more careful in their writing and editing of this manuscript. This is a long manuscript, and there are many editorial errors (some by omission). Also, although it is nice to have all of the data in one place, the story appears to be a potpourri of findings and overlong. I recommend that the authors streamline and narrow the focus of this story (for example, by leaving out the transcriptomics data, perhaps).

Furthermore, before publication the authors should include a Methods sub-section explicitly describing their statistical tests, the corrections for multiple comparisons, if any, and a more thorough explanation for technical replicates vs. experimental replicates. In the manuscript body, it is sometimes unclear, and always a bit opaque as to, in general, which calls/flags from the coin package were used in R to conduct each test. From the authors' descriptions in the "transparent reporting form" I was unsure if these particular permutation tests, like parametric tests, require corrections when multiple comparisons from the same experiment are completed. I understand why the authors may have chosen to use coin (for example, data non-normality or philosophical opinions about drawing from true, representative subpopulations, perhaps), however, the reader has to infer this and may be a bit confused in general as to these tests (or, for example why the authors choose to use them in all cases except one – see subsection “The large selective advantage conferred by squid-adapted binK improved fitness during both the initiation and maintenance stages of symbiosis, consistent with theoretical predictions”, first paragraph). I urge the authors to clarify their statistical reasoning/philosophy and methodology for the readers before publication. Finally, many experiments appear to contain technical replicates and/or experimental replicates, but few describe what these are and how they were analyzed appropriately via the tests above – for example, many lines (see subsection “Luminescence, homoserine lactone, and cell density determination” for an example) imply that data were all lumped together for technical/experimental replicates.

One final minor note: the authors' use neutral assumptions for their modeling of in-squid dynamics, but the argument is also made that the binK locus is demonstrably not under neutral conditions after initiation – how are these two statements reconciled in the authors' minds?

Reviewer #2:

This is an impressive example of bacterial experimental evolution in a host setting, identifying mutational change of a regulator as key for symbiotic association. A single gene, encoding a sensor kinase, is identified to confer the ability to colonize the host and remain in stable association over several generations, and the downstream effect of the sensor kinase on biofilm (EPS) formation, response of the innate immune system, quorum sensing, and metabolism are elucidated to provide a mechanistic explanation for the genetic result. The authors have conducted a very comprehensive piece of work, including proper controls (strain evolution in culture vs. in symbiosis; knockouts; transcriptomic and metabolism profiling).

I have only a few comments that need to be addressed prior to publication:

Introduction, last paragraph and Figure 2: when describing the experimental setup, the "neutral" /negative control (evolution of MJ11 in pure culture without selection) should be introduced; it is shown in Figure 2 but not mentioned anywhere at this point, so in order to understand the figure and controls, please introduce early in the text.

Figure 2: has the potential to explain the outcome of the experimental evolution in a nutshell but needs serious improvement: symbols are often way too small and the legend does not explain all the information hidden in the figure. Fx the binK "colored dots" in A and C are hard to distinguish (I cannot figure out, which MJ11 mutation occurred twice), even when zooming in, the "host symbols" are hard to recognize, and panel B does not work at all (see also comment below). The structural model (panel C) is poorly explained (I assume the faint grey bar depicts the membrane, so Cache is in the periplasm?), and the scoring matrix is not discussed any further and thus a strange way to suggest that the 4 occurring mutations are not functionally neutral – what is the point to display all other possibilities as well?

One question that arises (and that could have been answered in Figure 2B) is whether the binK evolution results in a convergence of MJ11-evolved BinK to the binK variant of the native strain ES114? Or does it just somewhat lose functionality? Please address.

Figure 4A: is this a conceptual figure or based on actual data? Please make clear.

Figure 9: please define "mean expression per locus": how was that calculated?please use colored labels for compounds that are clearly distinguishable at this size; please indicate whether the 4 replicates are technical or biological; please add gene symbols to the coding loci where possible; I would especially appreciate to add the genes discussed earlier in the study to the heat map, i.e. binA, sypE, sypK, lux, etc.

Subsection “Squid-adapted binK confers metabolic convergence with native symbionts”, last paragraph: Biolog does not measure redox. There's a redox dye that indicates substrate utilization, i.e. it is reduced and results in color precipitation. But saying "greater redox" is not correct.
