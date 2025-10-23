# Peer review - Round 1

Editors:
- Friedrich Simmel, Technische Universität München , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09771.034](https://doi.org/10.7554/eLife.09771.034)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Rapid forward engineering of novel genetic ring oscillators" for peer review at eLife. Your submission has been favorably evaluated by Naama Barkai (Senior editor), Friedrich Simmel (guest Reviewing editor), and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The article by Niederholtmeyer et al. demonstrates the realization of 3-node and 5-node genetic ring oscillators in a cell-free transcription/translation system, using a microfluidic nanoreactor with tunable dilution rate. After prototyping the oscillator circuits in vitro, they are implemented in E.coli and shown to function in vivo with similar dynamics, demonstrating a remarkable portability from in vitro to in vivo systems. This is important work, which significantly advances the state-of-the art in terms of circuit design and experimental approach. In particular, the article also contains the first realization of a synthetic 5-node genetic ring oscillator, which functions both in vitro and in vivo.

Essential revisions:

1) Biological significance:

The results themselves do not provide any new biological insight, but raise potentially interesting biological questions that could be addressed in more detail.

For instance, the ability of 3n1 and 3n2 constructs to show population level oscillations is biologically interesting, but unfortunately remains a mere observation with a speculative interpretation. It may also be misleading to term the observation "population level synchronization" (as in the last paragraph of the Main text). For synchronization, one would also expect evolution from an initially unsychronized state towards synchrony. In the present experiments, the bacteria start in a synchronized state and stay approximately synchronized due to slow dephasing (this interpretation is given in the subsection “Transfer of in vitro prototyped 3- and 5-node oscillators to E. coli”). Thus the observation might have a very different cause than the prototypical synchronization of coupled oscillators (as for quorum sensing-coupled bacteria).

In addition, the fact that the 5n networks had to be altered in order to function in vivo due to the system load is another avenue of continuing research that is left open ended by this current manuscript. Is it possible to add more biological insight?

2) Technical issues:

It is quite surprising that the approach taken by the authors actually works so well. Previous work on cell-free circuits did not show oscillatory dynamics (except for two publication cited in the text) because of low enzyme activity and long protein lifetimes, etc. It would be useful for the readers if the authors could point out the decisive technical steps that had to be taken for their work – the specific cell-extract used, the microfluidic dilution system, etc.?

In this context, can the authors comment on what they believe are the most important variables necessary to control for matching in vitro and in vivo environments?

Furthermore, the authors could more closely compare the time to implement designs both in their TX-TL systems and in cells? What is the true cost and time savings when working in vitro versus with E. coli?

3) Presentation:

The manuscript deals with variety of different experimental implementations of the oscillators, which can be slightly confusing at times. For instance, the 3n1 oscillator is implemented on a plasmid, while the 3n2 network is implemented on linear DNA. This is not motivated, however. Is this done for simplicity and faster prototyping?

Furthermore, it is not completely clear why the authors work with two different microfluidic systems for the experiments with bacteria – the "mother machine" (allowing simple single cell experiments?) and the CellASIC system (allowing single layer growth?). Figure 3 contains experiments with both of these two systems – can they be directly compared?

Figure 4 does a great job highlighting the main point of the paper, and this figure or a similar figure could come earlier in the manuscript to guide the reader towards the fact that speed is the true breakthrough. Showing/expanding Figure 4 to include what its in vivo only counterpart would look like, with associated time lines between the two methods, would be helpful to stress that speed is the main advantage here.
