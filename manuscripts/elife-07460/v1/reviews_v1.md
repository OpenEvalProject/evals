# Peer review - Round 1

Editors:
- Peter Rodgers, eLife , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07460.017](https://doi.org/10.7554/eLife.07460.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Fraxinus: a citizen science DNA alignment game where players beat software & reveal a winning strategy for crowdsourcing” for consideration at eLife. Your article has been favourably evaluated by three reviewers, but needs to be revised in response to the following comments from the referees before we can reach a final decision on publication.

Summary:

The paper, through the analysis of data arising from the platform game Fraxinus, proposes a linear model that predicts the likely outcomes of crowdsourcing projects. The authors, by means of a descriptive analysis, show a case in which the crowd shows higher performances than the machine. Predicting the outcomes of a crowdsourcing project is certainly an interesting topic whose implications are relevant not only for scientists themselves, but also for R&D managers, administrators of granting agencies, and policy makers. The article describes a novel crowdsourcing project and provides relevant insights for crowdsourcing in bioscience. Nonetheless, there is considerable scope for the manuscript to be improved.

Essential revisions:

1) The title of this paper describes Fraxinus as “a citizen science DNA alignment game where players beat machines” and the Abstract states that Fraxinus players “matched or improved computational alignments in 94% of cases”. However, it turns out that only 15% of the time players gained a higher percent identity (and in 78% of alignments the percent identity was equal). Therefore, the claims in the title and Abstract need to be toned down.

The authors should also slightly shorten the paragraph containing the comparison of performances between the crowd and the machine. This topic, despite its relevance, has been already addressed by literature (e.g. Cooper at al. 2010).

2) In the Abstract the authors claim that their model will provide a framework for the design and implementation of future citizen-science initiatives. However, the paper just provides limited hints of such a framework. The authors should consider extending this section. The authors should also consider adding a paragraph about the generalizability of the model, possibly containing evidences of its goodness (e.g. through the prediction of the outcomes of other crowdsourcing project).

3) Many key concepts necessary to describe multiple sequence alignments and genetic variant predictions are explained only brief. Please supply more detailed descriptions for the benefit of readers who are not familiar with these concepts.

4) The authors should explain their model more fully. In particular, they should better explain the model assumptions (e.g. why press releases only influence the behavior of new players?) and the implications of these assumptions. Crowston and Fagnot (2008), Panciera, Halfaker and Terveen (2009), and Jackson and colleagues (2015WP) develop dynamic models of virtual collaboration that may be useful in thinking about this issue.

5) The authors should consider a refinement of their model to address the following points:

Results and Discussion, first paragraph: The authors claim that 49 players (0.7%) contributed to half of the total answers. However, the authors do not consider this information when they developed their model.

Similarly, they write (Results and Discussion, fifth paragraph) that not all time contributed by players is equally productive. However, they make this assumption in their model. The authors should explain the reasons of these choices.

A number of recent studies (e.g. Sauermann and Franzoni 2015) describes user's contribution pattern and highlights that the idea of a homogenous group of participants is far from reality. The authors should consider these contributions to refine their model.

Using Google Analytics persistent cookies may generate a bias in assessing both the number of new players (overestimation) and the number of returning players (underestimation). The authors should describe how they took into account this bias in their computation.

6) Concerning the results, it would be good to have a justification for the parameters used. Why do you choose a 21 nt game window? Do you try the game with a longer window? Could you expect better results if a longer window is used? In the same sense, the alignments are compared in two ways; by calculating the percent identity and by computing an alignment score. With respect to the measure of identity, why the authors did not use ‘standard’ measures such as Sum of Pairs, and Total Column metrics? What about comparing the score of the alignments using the score functions reported by state of the art MSA algorithms?

7) It is not clear to the reader what software/computational method the players are being compared to, especially in the figures and tables. Please explicitly the software/computational method in the captions of the relevant figures and tables.

8) The section ‘Human contribution estimation’ needs some revision. If the formulae given in this section are standard formulae taken from the literature, please supply references. And if these formulae are not standard formulae, please supply more information about how they were derived.

9) Please consider adding the following references and discussing them in the text at the appropriate place:

Open-Phylo: a customizable crowd-computing platform for multiple sequence alignment Genome Biology 14, R116 (2013). This paper seems to have a lot of common features with the study presented here, and it can be used for comparison purposes.

Algorithm discovery by protein folding game players PNAS 108, 18949-18953 (2011). This paper could be used to develop the idea that the alignment strategies used by players could be implemented in algorithms for potential improvements.

It would be useful to be explicit about the relationship between the present work and previous publications (MacLean et al., GigaScience, 2013; MacLean et al., eLife, 2013).
