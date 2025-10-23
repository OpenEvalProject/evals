# Peer review - Round 1

Editors:
- Samuel L Díaz-Muñoz, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58410.sa1](https://doi.org/10.7554/eLife.58410.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The recent discovery of phage communication allowing collective decision making (Erez et al., 2017), raised many questions about the social lives of viruses. This paper uses a mathematical modeling approach to determine the conditions under which a small molecule communication system among phages governing the lysis-lysogen decision would evolve. The paper, the first to employ theory on the topic, demonstrates the evolutionary advantages of phage communication over a bet-hedging strategy, which was previously believed to govern life cycle decisions in viruses.

Decision letter after peer review:

Thank you for submitting your article "Repeated outbreaks drive the evolution of bacteriophage communication" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Samuel L Díaz-Muñoz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This paper uses a modeling approach to determine the conditions under which a small peptide-mediated communication as a strategy informing lysis-lysogeny decision would arise in viruses. This topic arises from the recent discovery of phage communication by Erez et al., 2017. It starts using traditional differential equation system to investigate the lysis-lysogeny decision in a bet hedging context. However, most of the manuscript goes on to describe a modeling strategy mimicking serial passaging to examine the bet hedging strategy and the communication strategies, including examining how they work in a head to head competition (when does the communication strategy invade). Finally, the paper examines the threshold of proportion of cells infected at which phages are predicted to switch to lysogeny, coming up with 0.5 as a consistent number across a wide parameter swath. The manuscript demonstrates how such a communication mechanism can be fitter than a bet-hedging strategy where some fixed fraction of infections result in lysogeny.

In sum, this manuscript is very clear, well-argued, well-written, and it was a pleasure to read it. This paper is a brilliant contribution not only for being (surprisingly) the first to address this topic from a theoretical perspective, but for its thoughtfulness, rigor, completeness, and the connection of the theoretical and the biological. There are a few areas for improvement, but this manuscript should be an outstanding contribution, certainly to the emergent sociovirology literature, but also to a wide audience including microbiologists, virologists, ecologists, evolutionary biologists, and behaviorists.

Please pay very special attention to the “Revisions expected in follow-up work” section below in revising your manuscript, the other revisions are there for our consideration and are given with the intention of improving the manuscript.

Revisions for this paper:

1) Some assumptions of the model should be better justified and/or discussed, for the reader to assess the generality of the conclusions obtained in the manuscript. In particular:

a) Subsection “Model” paragraph three: It would be good to comment on how realistic the stepwise assumption is for phi(A).

b) Results third paragraph: This discussion strongly relies on the fact that cells stop dividing as carrying capacity is reached. In reality, cells may die at a certain rate, or some cells may leave the system or be lost, implying that some rate of division could be sustained at equilibrium. It would be really good to discuss this possibility and the impact it may have on results. The serial passaging scenario considered afterwards is a special way of including such an effect, but at discrete and periodic times.

Fourth paragraph: It would be important to further motivate the serial passaging scenario that is chosen. Is it related to actual or potentially realistic experiments? Are the conclusions obtained robust to modifications of this scenario?

2) Results second paragraph: I completely agree with the statements and rationale outlined in this paragraph. However, the scenario described in paragraph four should then be part of the Materials and methods. I still think it can be included in the Results as is, but needs to be included in the Materials and methods.

3) Some elements of Discussion should be specified:

(3a) Paragraph four: Two mutations occurring in a very short lapse of time seems rather unlikely a priori. Could the authors comment on whether scenarios where one happens and then the other would be favorable? Related to mutations: In the passaging is there selection with regard to the phage mutations or are they likewise proportionally represented in the next passage? If they are rare in the system, they could be lost in the dilution. How would this affect the potential evolution and impact the model outcomes?

b) Could there be other scenarios under which the production of arbitrium by lysogens is more useful?

c) Final paragraph: It would be great if the authors could give some indications about how the current model could be adapted to these other cases and what insight it may bring. This would add value to the manuscript by potentially making its scope broader.

4) The readability of Figure 1A, which I think needs revision. I can see the authors likely spent considerable effort on it, but it remains very difficult to parse. Is it really necessary to have four different kinds of arrows? As the eye wanders around the diagram, it's not clear where to start or where to end. Perhaps it would help to organizing cycles more neatly into circles? The many virus pictograms add visual clutter without aiding clarity. I don't have a clear recipe, but I'd encourage the authors to solicit input from colleagues outside their field so as to make this figure maximally accessible, especially for a broad-audience-journal like eLife. Elsewhere the authors do a truly admirable job, reminding the reader what their parameters are etc., so it would be a shame for the reader to stumble at Figure 1A.

5) The discussion is brief, but excellent. It really covers a lot of the questions that I wanted to know before reading the paper and does an amazing job of connecting model results to biology and making predictions to test empirically.

Revisions expected in follow-up work:

1) My major "science concern" was spurred right from the start by the sentence in the Abstract, "our model predicts the selection of phages that switch infection strategy when half of the available susceptible cells have been infected". Seeing as it is notoriously difficult for a virus to estimate what fraction of cells were infected, this raised a worry that persisted through reading the entire paper – until the very last paragraph, where it was finally discussed. My suggestions would be to do this (a) sooner, and (b) better.

a) Sooner: I'd recommend explicitly commenting on the issue already in the Introduction and at least promise that it will be discussed.

b) Better: “The arbitrium concentration during the early epidemic then is a direct reflection of the fraction of susceptible cells that have so far been infected”

The readout is a direct reflection only of how many cells were lysed. In the model, yes, this is the same as fraction. But as the authors acknowledge at the very end this requires the assumption that bacterial cells were at carrying capacity K. In natural conditions, the carrying capacity can differ due to environmental factors – "unknown" to the virus.

Far from being a minor worry, the issue is directly relevant for the authors' comparison between the communicating and the bet-hedging strategy. Under the communicating strategy, if the carrying capacity were modulated to e.g. half of its usual value, it seems that the virus would never switch to the lysogenic phase – a crippling blow to fitness. In contrast, the bet-hedging strategy seems vastly more robust to such a modulation. This suggests that the conclusions could be changed quite strongly if the carrying capacity were picked randomly (within some range) between passaging trials.

It sounds like there is a prediction here.

I do not intend this comment as negative / undermining authors' findings. Quite the opposite, I think by adding this analysis the authors could strengthen their argument, demonstrating the utility of a quantitative framework like theirs, and perhaps even make additional predictions. Beyond what level of (passage-to-passage) variability of K the bet-hedging strategy becomes favored? Addressing this comprehensively would be a project in itself; but generating a figure panel illustrating this in simulations would strengthen the authors' case for the benefits of modeling work.

An optional point:

Since the cell-mediated uptake and degradation of arbitrium is also mediated by bacterial cells, and is thus also dependent on bacterial cell density, it's possible that this might mitigate the problem (making the arbitrium concentration less strongly dependent on K than naïve linearity). I don't know if it's true, but if it is, it would be cool, and worth highlighting. Unless I'm mistaken, this is not currently discussed. I think that could strengthen the story.

2) Figure 3: In the competition between bet-hedging and communicating variants, what is the impact of initial conditions? Moreover, here, only the 2 top variants of each type are competed against each other. Is this sufficient to conclude that communicating variants will always be selected by competition? If binary comparisons are sufficient, this should be stated and explained. If not, then it would be important to show explicitly what happens when various phages of both types compete together.

3) Scripts really should be openly available unless there is a compelling reason not to do so, especially in this case where the results depend so closely on the code. I would strongly urge the authors to instead publish all simulation scripts alongside the manuscript, both for archiving purposes but also to facilitate access.

4) The parameters tested should be in the main text. Note that, other than the construction of the equations according to life history parameters, this is the only connection to "biology" that non-theoretical researchers will have to the manuscript. Table A1 should be in the main text. The table should list the conventional units of the parameters. For instance does burst size of 2 refer to 2 virions? This value would normally be in the 10's-100's for most phages. Some of these parameters don't seem reasonable at first glance. For instance, the adsorption rate is usually something on the order of 10-10 to 10-12. I suspect this could be because these are "scaled" values. If the scaled values are made for model convenience they should also be listed separately. This way the connection between the model and the biology will be more evident to readers.

5) The idea of having to go away from a steady state for this to work is very appealing. It is also likely much closer to biological reality in this case. Other than models that specifically address serial passaging, is the approach of disturbing ESS's regularly a new concept? Is there a generalizable framework for this?

6) Some conclusions should be specified or clarified:

a) Figure 2 B-C: Some diversity seems to survive at steady state for T>5h. I believe this is what the authors refer to as "quasi-species" in the manuscript. It would be important to discuss and interpret this surviving diversity, and to explain whether it is going to survive forever or to slowly decay, and why.

b) Figure 4: Please explain the difference between the analytical prediction and the simulation results at small values of bB in Figure 4B. In particular, does any of the simplifying assumptions result in this discrepancy?
