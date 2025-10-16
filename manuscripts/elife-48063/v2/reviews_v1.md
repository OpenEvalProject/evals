# Peer review - Round 1

Editors:
- Michael T Laub, Massachusetts Institute of Technology United States

Reviewers:
- Alan Leonard

## Review text

DOI: [10.7554/eLife.48063.sa1](https://doi.org/10.7554/eLife.48063.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper uses time-lapse microscopy of individual cells to examine the coupling of chromosome replication and cell division. The authors present a new model suggesting a "dual adder" mechanism in which the volume added by cells controls both the subsequent round of replication initiation and cell division. This new model contrasts with recent single "adder" models. Although a dissection of the mechanistic basis remains to be done, this new model represents an important new concept that will guide future studies of the bacterial cell cycle.

Decision letter after peer review:

Thank you for submitting your article "Chromosome replication initiation controls both division and replication cycles in E. coli via a double-adder mechanism" for consideration by eLife. Your article has been reviewed by Gisela Storz as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Alan Leonard (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The regulatory mechanisms that coordinate the bacterial cell cycle remain obscure, but recent technological advances in single cell analysis have resulted in an avalanche of recent manuscripts focused on "adder mechanisms", particularly those related to cell size control where cells add constant length to their birth length and the added length fluctuates independently of either birth size or growth rate. While the "classic" adder model is insightful as a universal cell size maintenance mechanism, its application to other aspect of cell cycle regulation are less satisfying. The studies and model presented here in Witz et al., based on time lapse microscopy of individually growing cells, take the adder concept in an interesting new direction. The authors present an intriguing model that focuses on the initiation of chromosome replication as the critical starting point and incorporates "dual adder" mechanisms whereby cell volume increases from the initiation point controlling the subsequent cell division as well as the next initiation of replication. Importantly, the authors show that their model is compatible with the known parameters for both slow and fast growth conditions (Figure 5), parameters not usually examined or even addressed successfully in prior adder models. The authors also present a compelling comparison of their model with other models in Figure 6 and Figure 6—figure supplement 1. Despite the general enthusiasm for the work, the reviewers have several comments/concerns regarding the analyses presented as well as how the work relates to previous work. These issues will need to be addressed in a revision. Some of the following points are from different reviewers but hit on related points, so some revisions may address multiple points below.

Essential revisions:

1) The results of this study seem to disagree with those of Wallden et al. The latter does not find "adder" correlations in the slower conditions studied. The authors reference Wallden et al., but do not address the discrepancy.

2) The double-adder proposed do not capture the well-established exponential dependence of cell size on growth rate at the bulk level (Donachie, 1968). As such, their statement, in the Discussion section, on how models "fail to capture at least one important observation" may be applicable to the double-adder as well (at least in fast growth conditions).

3) The argument against the previous work of Wallden et al., in Appendix 2 seems incorrect. The authors state that "The histogram of the number of origins at birth shown in Figure 1D shows a clear failure of the model where cells in slow growth conditions are all born with an ongoing round of replication in contradiction with experimental data". But in fact, Figure 1D of this appendix is consistent with initiation occurring shortly after cell birth, which is precisely what the Wallden et al., experimental data shows in the slow growth condition. Moreover, the authors attempt to use (both in the main text Figure 5D and in Appendix 2) the bimodal distribution of the number of origin as a "smoking gun" for one model or another. But such bimodal distributions of origin numbers are mostly model-agnostic, and therefore cannot be used to discriminate between models.

4) In order to discriminate between models, a clearer statement of which models were considered is necessary. In particular, how is noise implemented exactly in the various models considered? e.g. does the noise affect the generation time or the growth rate, and how? What is the biologically dominant source of noise? One reason this might be important is that different implementations might affect the analysis used in Figure 6.

5) In Figure 6, the authors propose a new method for distinguishing between models. The authors should also test the method and validate it on synthetic data, to show that the method can indeed decouple the newly proposed model from previous ones. From the text and Figure 6, it is not obvious that correlation patterns similar to the double-adder cannot be generated by other models (e.g., can this method distinguish between the multiple origins accumulation model and the double-adder?).

6) The results of Figure 5C do not seem compelling. Could the authors perform some statistical analysis to test the data more quantitatively?

7) Regarding the Wallden model test (Appendix 2), it would be useful to show in panel D the data from Figure 3 of the Wallden paper, as to judge the claimed contradiction. Please then also provide a comparison with your model (Figure 5D), so that one can judge how well it predicts their data.

8) This also addresses another general topic: how similar are the data sets from the different studies? Is would be good to do this not only for 5D-style data, but also other quantifications. Are they qualitatively or quantitatively similar? If they are different, what are the causes?

9) In Figure 2 of the appendix, red and blue do not appear to be properly labelled.

10) Regarding the presentation of the modelling, I can guess what the 3x3 and the colouring means, but descriptions are not given in Appendix 3—figure 1, nor what the use of 'estimating independence' is. The former is given in Figure 6A, but no clarification is given about the aim of this exercise – e.g., why are these 4x4 the 'best decompositions' (how can I see that from these 4x4 diagrams)? But also, very basic aspects of their approach, like the notion that different rows in Figure 6A bottom are different models, is highly non-intuitive. In 6B caption, what is the difference between 'blue area', 'shaded blue'. What is the difference between the mathematical 'determinant of the correlation matrix' and the more usual correlation coefficient? Because of its unusual nature, more effort needs to go into explaining such basics. The authors did try to explain some aspects in the main text (subsection “The double-adder model best captures the correlation structure of the data”), but overall these quite crucial parts of the paper are very difficult to follow, even with a quantitative background.

11) The authors did a good job in discussing their results in relation to the possible molecular mechanisms, such as the possibility of replication initiation setting future division sites. This relates to recent work showing rapid min-system-driven repositioning of the FtsA rings in filamentous cells, which appear to be odds with such a notion (Wehrens, 2018), which would be good to discuss. On a different note, that study also found adder behaviour despite already having multiple chromosomes because of the filamented state, and single division events despite many potential division sites and rings, all suggesting some division to division regulation. It would be good to discuss these findings, also to keep open the possibility that such a division to division mechanism may exist, even if it is not required to explain the data presented here.

12) It would similarly be important to discuss surface to volume ratio models, and the extent to which they are consistent or not consistent with the presented data and models.

13) The authors do not discuss at the D period, or its compensations. I was trying to determine whether a birth-division adder has some bearing on this, but could not resolve it. The C period rather fixed in time, while the D period can compensate for (eg small) size at termination (Adicipingrum, 2015). That could be consistent with a birth-division adder, or at least both observations indicate the D period is not a constant time, as suggested in much of the literature, which would be good to discuss.
