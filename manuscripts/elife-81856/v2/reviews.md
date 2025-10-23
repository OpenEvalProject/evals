# Peer review - Round 1

Editors:
- Jan E Carette, https://ror.org/00f54p054 Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81856.sa0](https://doi.org/10.7554/eLife.81856.sa0)

Replogle et al. present their design of a compact and functionally validated dual sgRNA library and dCas9-effector protein that will enable new forms of CRISPRi-based screening in mammalian cells. Quantitative comparisons to previously published standards demonstrate strengths and weaknesses that along with the protocols and design strategies outlined, should enable end-users to rapidly adopt their approach.


---

# Peer review - Round 1

Editors:
- Jan E Carette, https://ror.org/00f54p054 Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81856.sa1](https://doi.org/10.7554/eLife.81856.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Maximizing CRISPRi efficacy and accessibility with dual-sgRNA libraries and optimal effectors" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mauro Calabrese (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The consensus is that it is a strong manuscript and a very useful resource for the community. The necessary revisions are mainly clarifications and should involve only minimal new experiments.

Reviewer #1 (Public Review):

The manuscript is written clearly and places appropriate emphasis on the strengths and weaknesses of the new approach. In Figure 1, the authors aggregate a large body of data from 126 previously performed CRISPRi screens as well as previously vetted computational predictions to create dual sgRNA libraries that can be used for succinct CRISPRi screens in human cells. They validate the functionality of their dual sgRNA library using Perturb-seq. They also note that one particular weakness of the dual sgRNA system is sgRNA recombination between lentiviruses, resulting in chimeric delivery of sgRNAs to cells. Quantitative analyses estimate that in K562 cells, recombination frequency in their new system is ~30%. In Figure 2, the authors use RNA-seq to demonstrate that in K562 cells, certain dCas9-repressors have greater off target effects than others; this was particularly striking for the SID-dCas9-Kox1 construct, which previously had been used for a handful of CRISPRi screens. In Figure 3 the authors compare the ability of different dCas9-repressors to reduce expression of several target genes, and from these experiments, identify Zim3-dCas9 as the most effective in K562 cells. In Figure 4 the authors show that Zim3-dCas9 is effective in additional human cell lines that have been used for CRISPRi screens. By my evaluation, all conclusions are well supported and justified by the data. CRISPR screens are labor and cost intensive endeavors. With this work, Replogle et al. present a validated set of novel reagents that will enable more effective and efficient CRISPR screens. The manuscript also highlights certain limitations and caveats of different forms of CRISPR screens whose clear explanation here will also benefit the community.

Reviewer #1 (Recommendations for the authors):

1) I appreciated the author's quantitation of recombination frequency in dual sgRNA libraries, and agree that essentially all users of the dual sgRNA approach will similarly want to discard reads that contain recombined sgRNAs. The main utility of this manuscript is the protocol it outlines and the reagents developed. In that spirit, I would request that authors provide readers with a link to a well-commented python script that enables users to repeat the author's exact protocol for detecting and discarding recombined reads.

2) Also related to protocol development and deployment: can the authors provide ranked sets of dual sgRNA libraries targeting the mouse transcriptome as well? If necessary, they could work exclusively from the predictions made in Horlbeck 2016a, but if any reasonable CRISPRi screens in mouse could serve as a validated reference, users would greatly benefit from their analysis here. CRISPR users in the mouse community would benefit, particularly for in vivo screens.

Reviewer #2 (Public Review):

The authors performed a series of impressive experiments to systematically establish each part of their CRISPRi method. They provided one of the most compact design of CRISPRi dual-guideRNA library, with a genome-wide coverage; they confirmed prior finding on the optimal repressor domain to generate a set of useful vectors for expressing the repressor; they showcased the usage of the system in multiple common cancer cell lines. The authors also took an important step towards providing a detailed and well-annotated protocol (in the supplementary materials) to help users of their methods. The items listed below would be helpful to further improve this work

First, while the dual guideRNA design is a useful development, the author also noted the significant rate (~30%) recombination between the two sgRNAs. This should be further discussed and evaluated in the manuscript to help readers understand the implication of this high recombination rate. For example, across replicate experiments or across cell types tested, would the recombination be stochastic, or there may be some bias of which guide would be recombined? Are there any cell-type dependencies here in terms of the recombination rate? This would also help future users to decide if they would need to check for this effect during functional screening.

Second, on the repressor development and evaluation. As the author mentioned in the text, the expression level of the repressor can confound their conclusion on fitness/efficiency comparisons of CRISPR repressor. Thus, it would be helpful to perform protein level validation using the cell lines they generated, such as a WesternBlot comparison to rule out this potential issue.

This work would also benefit from including cell proliferation/viability measurement using the selected Zim3-dCas9 repressor in multiple cell lines, as it seems this was only done initially in K562 cells. As authors noted, the fitness effects of the CRISPR repressor would be a major concern when performing functional genomics screening, so such validation of fitness-neutrality of the repressor can be very helpful for potential users of their method and approach.

Third, a major resource from this work, as the authors noted, is a suite of useful Zim3-dCas9 cell lines. The authors have performed a set of experiments to demonstrate the knockdown efficiency with dozens of guideRNAs. While this is a good initial validation, to really ensure the cell lines are performing as expected, a small scale screening in pooled fashion will be more convincing. This would be a setting more relevant for potential readers, given that pooled screening would likely be the most powerful application of these cell lines.

Reviewer #2 (Recommendations for the authors):

It's very helpful to have multiple constructs generated based on the Zim3-dCas9 design the author selected. It would be helpful to make a list of these constructs available in supplementary materials, and also note their design consideration or reasons to choose a particular construct, this could help readers to understand the author's perspective on how to choose the best construct for experiments.

There are some minor confusing issues, such as in Figure 3D, some of the plots don't seem to match the number/percentage given, such as the strong targeting guideRNA group where plots seem to show less repression compared with the numbers labeled, or does the number represent something different? In general, the figure labels can be improved, in particular for Figure 2A (UCOE etc. should be described in legend), Figure 3C/E, it may be better to consistently use percentage, or fraction. Figure 4C is now placed between panel A and B, it could be moved to the end.
