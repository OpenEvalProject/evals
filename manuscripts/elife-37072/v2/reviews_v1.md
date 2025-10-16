# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37072.031](https://doi.org/10.7554/eLife.37072.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Changes in the genetic requirements for microbial interactions with increasing community complexity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Alvaro Sanchez (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In "Changes in the genetic requirements for microbial interaction with increasing community complexity" the authors show that bacteria require a different set of genes to grow alone, in pairwise competition, or in communities. Moreover, they also show that the gene expression profile in the bacteria changes upon the bacterial interaction partner. The addressed question and the conclusion that genetic requirements of bacteria are interaction dependent are very, very interesting.

Please note we are aware of the messaging exchange that clarified a key methodological concern of the reviewers and enabled this request for resubmission. Please make sure that the clarification of these concerns is clearly addressed in the revised submission.

Major concerns:

The mutant library consists of 150,000+ strains. Were all of these strains grown as 150,000 separate colonies on the CCA agar plates? Or were they a complex mixture? If they were grown as a mixture, then different mutants can interact within the mix (e.g. cross-feeding) obscuring the findings of genes relevant for growth on CCA medium. Please clarify the growth conditions and discuss the limitations of the chosen condition.

Spatial aspects:

The experiments were done in a spatial setting, by plating the bacteria on agar. However, this will lead to strong spatial heterogeneity, with areas where only specific mutants grow, whereas interaction may happen only at the borders of those patches. This may obscure a lot of interaction. Moreover, the population expands in a spatial environment, which is known to cause genetic drift that can obscure the fitness outcomes of those bacteria.

Single species cultures were done on 100mm (?) petri dishes but pairwise and community experiments were done in 96-well plates and thus different spatial settings. Why was the experimental design changed between the different experiments? Moreover the number of bacteria per area was much higher in the petri dishes than in the 96-well plates. Since the size of the inoculum will change the spatial organization (fewer cells lead to bigger, homogeneous patches) and the interaction depends on the spatial organization, the change of experimental design from one experiment to the other may alter the outcome and makes me wonder how comparable the experiments are.

Terminology:

All reviewers had trouble with the terminology: "essential" vs. "important" genes. An "essential gene" is one essential for growth. That is not the usage by the authors. Instead, here, "essential genes" are just genes with reliably negative fitness effects upon knock-out. However, this may be true for many (likely even the majority of) genes?

The authors state that the fitness was calculated for 3289 genes. 40 were removed by showing positive fitness effects upon knock out, but in the end only 160 genes were identified as having negative fitness effects. Does it mean that the majority of genes (around 3000) were excluded because they showed non-reliable data (small t-score)? Are the obtained 160 genes not so much 'essential genes' but simply genes that lead to reproducible data? In other words, the majority of gene-knockout could lead to decreased fitness but just some show reliable results and those are called 'essential genes'. How strong is variation for different insertion localizations within the same gene? How sensitively are fitness measures depending on the parameters chosen for the pipeline? How strong is variation between triplicates? Does this explain the many unreliable fitness values?

Timing:

This issue is related to the library pool method that the authors use to determine fitness. Is it that they are pooling together the entire transposon deletion library, throwing it together into their CCA medium, and measuring the fitness at three different time points? What they are putting together is already a community of E. coli strains which, collectively, strongly modify their environment as they grow. Thus, this E. coli community already contains multiple interactions among mutant strains, which are probably less strong early on during the growth period (say at day 1) when the environmental effects of the community's growth (i.e. through the collective depletion and secretion of resources) would be expected to still be weak-ish. However, on days 2, 3 there should be significant environmental construction by the community, and indeed this is apparent, not only by the fact that the population is not growing anymore after ~40hr (Figure 1A), but by the fact that the genes that show a negative fitness effect on days 2-3 are not the same as those that have an effect on day 1 (Figure 1B).

The authors do have a control for this, by looking at individual mutants that had been scored as having a negative effect within the community and directly competing them against the wild-type after one day of co-culture. In most cases this works well (See Figure 1—figure supplement 5), but they did not do the same for days 2-3, when interactions among deletion mutants that are pooled together may be stronger. A different but related complication to interpret deleterious mutations during days 2-3 (when the multi-strain population is not growing anymore) is the possibility of cell death. The authors measure population size by CFUs, and the population size does barely change after 40hrs. While the obvious explanation is that cells are just not dividing anymore but is it possible that some cell death is occurring but it is balanced by cell divisions? A breakdown of which genes are deleterious on days 1, 2, 3 in each of the conditions (monoculture, pairwise, community) would be helpful to disentangle which genes are deleterious in the unperturbed CCD environment that the authors provide (and whose composition is well understood) versus in the environment constructed by the E. coli community, which is much less well understood in this case. This is important in order to adequately rationalize and interpret interactions with other species either in pairwise or multi-species communities; The data presented in Figure 2-3 is also, evidently, pooling together genes that are deleterious in days 1, 2, 3.

An analysis where the genes found to be essential on days 1, 2, 3 are separated (which to some extent they do in Figure 1B, but then they do not incorporate into their analysis any further, as far as I could see) would be worthwhile, and a discussion of the limitations of the method particularly in the context of environmental/niche construction would significantly strengthen the paper.

Discussion points:

Either in the Introduction, or in the Discussion sections, the authors should relate their findings of suggested mechanisms for interactions in communities to related findings from other microbial communities, beyond cheese. In addition, E. coli (which the work mainly focuses on, i.e. Figures1-5) does not normally live on cheese rinds and is therefore not a natural interaction partner for the other species. The authors address this issue in the Introduction only very briefly, by pointing out that their transposon screen allows them to identify the genetic requirements for E. coli interacting with the other species. This is correct of course, but identifying the relevant interactions for E. coli to live with species it never encounters in the real world may be irrelevant. The authors can use the same data and analysis to identify how the 3 cheese-native species interact with other species using E. coli as a readout. This kind of analysis is already present in the results description, but a clearer distinction between which side of the interaction is being investigated throughout the manuscript would conceptually strengthen the manuscript. In addition, a clearer and longer description (beyond technological justification) in the Introduction for why using E. coli is relevant is needed.

higher-order interactions, subsection “Identification of E. coli genes essential for growth within the community and comparison with genes essential for growth in pairwise conditions”, last paragraph: The authors mention that their findings from the TnSeq screen "underline the presence of higher-order interactions". An explanatory paragraph on the relevant genes is necessary. There is currently only one paragraph (see seventh paragraph of the aforementioned subsection), which does not describe anything about these genes except that there are 14+3 relevant genes. Also: this small number of relevant genes seems to be at odds with the rather broad statement of the relevance of higher-order interactions given at the end of the Introduction.

The function of every gene doesn't need to be discussed in the main text (e.g. subsection “Identification of genes essential for E. coli growth in pairwise conditions”, fifth paragraph). The P. psychrophila story might just be put to the supplement, since it does not really add new things. Either in the Introduction, or in the Discussion sections, the authors should relate their findings of suggested mechanisms for interactions in communities to related findings from other microbial communities, beyond cheese.

Many of the figures show number of genes that are essential for this or that condition. These numbers are hard to interpret. They are not really put into context (e.g. what does the 26 in Figure 2B top really convey? How would it change the overall message if this number were 10 or 50?). In most cases they confuse more than they transport real information. More of a summary of the meaning of the numbers would perhaps be helpful.

Specific questions:

Subsection “Identification of the basic genetic requirements for growth of the E. coli sensor species in isolation”, first paragraph: This equation for the fitness cannot be correct, as it will always be positive. Or should the normalization be included in the fitness equation? But which strain has no growth rate defect on CCA medium? The WT? Please clarify and reword. It seems like some mutants had a growth-increase on CCA medium (but were excluded from the analysis).

Subsection “Identification of the basic genetic requirements for growth of the E. coli sensor species in isolation”, second paragraph: Why is the number of genes for which the fitness was calculated smaller than the number of genes covered in the transposon library?

Subsection “Identification of the basic genetic requirements for growth of the E. coli sensor species in isolation”, last paragraph: Why were only 25 defined mutants tested and not all (since the Keio collection is comprehensive)? How were these 25 mutants chosen?

How many genes did the authors remove based on the criteria of T0? Was there any bias in the genes you removed?

How was fitness value estimated and t-score? assume it is described in Wetmore at al., 2015, but it would be helpful to shortly explain here as well.

How was number of generations measured in Figure 1A? Could the authors show the fitness 'raw data' of the pairwise and community conditions like they showed them for E. coli alone in Figure 1B?
