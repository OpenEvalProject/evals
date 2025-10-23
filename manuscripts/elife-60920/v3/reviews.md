# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60920.sa1](https://doi.org/10.7554/eLife.60920.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Neuronal morphology is diverse and highly variable across neuron types, within and across species. A principled hypothesis for understanding this diversity is that it reflects differing functional requirements and developmental constraints. This study focuses on the development of the dendritic structure of mechanosensory neurons in Drosophila larvae, providing a detailed quantification of how dendritic branches elaborate and retract. A family of plausible mathematical models for growth reveals that a parsimonious stochastic retraction mechanism can explain the developmental profile of these complex dendritic structures. Both the data and modelling insights will be of interest to a broad section of developmental biologists, anatomists and neuroscientists.

Decision letter after peer review:

Thank you for submitting your article "Achieving functional neuronal dendrite structure through sequential stochastic growth and retraction" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Athanasia Papoutsi (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary

This work gathers and analyses quantitative morphological data of the development of Drosophila sensory neurons during larval development. The manuscript documents growth and retraction of neurites, giving an overall picture of how dendrites on a specific class of proprioceptors develop and how the developmental process may optimise the shape of the dendritic tree to sense bending. The authors propose a parsimonious stochastic optimization model for how neurites might grow, subject to constraints such as wiring cost. This model is found to give a good account of the data.

The reviewers raised several points that the authors should address in a revision of the paper. These are summarised here; the full reviewer comments are included below for reference and need not be addressed point-by-point. The reviewers agreed that no further experiments are necessary.

1) Check/provide evidence that the sampling rate of the time lapse imaging doesn't alias the measurements of dendritic growth and/or present a problem for relating data to the model.

2) Small variations in the model were identified – how are these justified (Figure 6B vs 2D)?

3) The authors should consider balancing their citations toward invertebrate quantitative neuroanatomy and existing quantitative/computational development studies.

4) Additional data for Figure 5A (as a figure supplement) would aid intuition.

Reviewer #1:

This study gathers and analyses quantitative morphological data of the development of Drosophila sensory neurons during larval development. They document growth and retraction of neurites in a very accessible and comprehensive way, giving a nice overall picture of how dendrites on a specific class of proprioceptors develop. The authors propose a parsimonious stochastic optimization model for how neurites might grow, subject to constraints such as wiring cost. This model is found to give a good account of the data.

The manuscript is well presented and methodologically sound. The conclusions are justified. The study should be of broad interest to developmental anatomists, theoretical biologists, neurophysiologists and the connectomics community.

It could be published as-is but would possibly benefit from more balanced and carefully curated scholarship: a lot of the citations in the Introduction concern mouse/rat neurophysiology, neglecting a lot of invertebrate studies. It is nice to connect the findings to dendritic function, but I feel the emphasis on dendritic physiology (e.g. computation in the visual system) is not balanced fairly against the (huge) amount of recent quantitative neuroanatomy work done in this very organism. Similarly, there is an omission of a lot of quantitative developmental work (both modelling and experiment, going back decades). Finally, there are a number of tangential studies that seem to be cited just to bulk up the references. I think the paper will be better received and will benefit the field more if the references could be rebalanced a little, should the authors wish to do so.

Reviewer #2:

The complexity of dendrite development has so far made it difficult to quantitatively describe their growth accurately. This work features in vivo imaging of a Drosophila sensory neuron called vpda, together with a convincing computational model that accurately describes most features of its development. In this aspect, the work is very interesting and poses a significant advance in regard to the quantitative description and understanding of dendritic tree growth and refinement during development. It further considers the functional aspects of vpda, based on curvature analysis and optimization of dendrite orientation for its proprioceptive function. Overall, I believe this is very interesting and thorough work shedding new insight into the little understood rules of dendritic tree development.

1) The embryonic imaging of vpda neurons was performed at 5min intervals, but quantifications were done only at 0.5-1h intervals. This might severely underestimate the growth dynamics during this stage, as dendrites can grow several microns within few minutes. Yet most of the authors' assumptions are based on this analysis. I think in particular growth and retraction rates might be potentially misrepresented, as both can happen to the same branch during the analyzed 30-60 min time intervals. The authors should at least consider this point and make a statement in this regard, or ideally validate their assumptions by analyzing their data at higher temporal resolution.

2) A very complementary preprint (Palavalli et al., 2020) describing and modelling vpda growth arrives at a similar conclusion as the work presented here. However, the computational models differ. Unlike here, the other model considers contact based self-repulsion (mediated by Dscam) as a key feature, resulting in similar simulated dendrite morphologies. I feel it is intriguing that both models basically arrive at the same result, yet the underlying assumptions differ. In my mind, this suggests that different growth mechanisms can result in similar outcomes. Alternatively, self-avoidance is not the only mechanism contributing to 2nd order branch parallelization, but acts in concert with stochastic retraction as described here. As dendrite self-avoidance is nonetheless a major feature of dendrite development from a biological point of view, likely across species and most neurons, the authors should discuss this point more carefully. Can they speculate about a biological correlate for the assumptions they make in their model, which results in stochastic retraction? As most of the parameters of the authors' model are directly derived from experimental data, this might inadvertently include the requirements for self-avoidance.

3) The authors show a very interesting computational analysis of dendrite curvature during larval locomotion, which coincides with neuronal calcium responses. While this result is not entirely novel as stated by the authors (see Vaadia et al., 2019), it still implies that dendrite development is adjusted to optimize its purpose. It is intriguing that the retraction of dorsoventral vpda dendrites coincides with peristaltic activity of the developing animal during the late embryonic stage. For the motor system, a critical period has been postulated around 17-19 h AEL, where rhythmic peristalsis and coordinated activity of motor neurons emerges. Have the authors considered a role for activity in reshaping of the dendritic tree during this phase, particularly during the retraction phase? It would be fairly straight forward to test this by Kir2.1-mediated silencing of vpda, providing a biological correlate shaping the final dendritic morphology.

Reviewer #3:

In the submitted manuscript, Castro and colleagues investigate the development of the dendritic tree of the c1vpda neurons of the Drosophila, by using a combination of in vivo imaging techniques and modelling of synthetic morphologies. The main conclusion of this study is that, during embryonic development, dendritic growth follows the optimal wire principle and that the subsequent stochastic retraction of dendritic branches allows for the maturation of a functional dendritic tree. Overall, the paper describes in detail this developmental process and is of potential wider interest as it showcases how stochastic processes can result in specialized dendritic tree patterns. I also appreciate the authors making their data and code available for the review process. I support this work for publication in eLife, yet I have some comments that would increase the clarity and visibility of the author's results.

1) My main concern has to do with the computational model shown in Figure 6, in combination with the model in Figure 2D/Figure 6B, dashed line. Specifically, I found it confusing why the authors chose to implement two different approaches to model dendritic growth. The results presented Figure 6B seem to better model the experimental data of Figure 2D, for a low number of branch points. The main differences between the two models, as far as I can tell, are in the surface area used to position the random targets and the inclusion of distinct time points. In other words, how are the two approaches different, and do they convey a principle for the developmental growth of the dendrites?

2) The results shown in Figure 5A are interesting and support the author's claim for the random retraction of dendrites. Can the authors provide information regarding the properties of the terminal branches (distributions of length, angle and BLO) that will make these results more intuitive?
