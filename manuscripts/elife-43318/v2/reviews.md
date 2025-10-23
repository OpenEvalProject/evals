# Peer review - Round 1

Editors:
- Tâm Mignot, CNRS-Aix Marseille University France

Reviewers:
- Jonathan Hodgkin
- Oleg A Igoshin, Rice University United States

## Review text

DOI: [10.7554/eLife.43318.033](https://doi.org/10.7554/eLife.43318.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Shared behavioral mechanisms underlie C. elegans aggregation and swarming" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jonathan Hodgkin and Oleg A Igoshin.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript of Ding et al. investigates collective feeding in the roundworm C. elegans with combination of time-lapse imaging, image analysis and mathematical modeling. It's a very well-written paper that presents broadly interesting and intriguing set of observation. Combination of experimental, quantitative analysis and modeling is the major strength of the paper. The authors study a prey-induced worm collective motility behavior called "swarming" and propose a mechanistic basis for this phenomenon. Both individual and population-level behaviors are quantified. Subsequent modeling is used to identify three key behaviors that drive aggregation: edge reversals, a density-dependent switches in speeds, and taxis towards neighboring worms. The same models can account for swarming when local food depletion is taken into account.

Major points:

1) Importantly, the modeling approach could be improved given the wealth of the experimental data. Specifically, it is surprising that the authors chose a fully phenomenological approach to construct their agent-based models that uses very little of the quantified data. Furthermore, authors do little to quantitatively compare resulting behaviors of agents in the model to those of tracked worms. Therefore, the reviewers are not fully convinced that identified behaviors in the model are either necessary or sufficient (given considerable noise in individual behaviors) for the observed population behaviors.

To circumvent this issue, measured individual worm behaviors should be used in constructing and/or constraining their model (see for example References PMID: 30514635, PMID: 28533367). Importantly, the noise and variability of the movement of agent match those of worms. It is not clear if this is the case in the current model. Furthermore, comparison of the resulting behaviors of agents and worms would allow testing the model. For example, is there correlation (e.g. between the agent velocity and the vector to nearby worm) that can quantify the degree of taxis? Can this correlation be compared between the model and experiments? Similar quantitative characteristics of other proposed 'key behaviors" need to be compared. Can changes in worm behaviors in nutrient-rich vs depleted regions be quantified and fit into the model? Either of the two approaches or some combination of them is needed to show convincingly that the postulated behaviors are indeed observed and responsible for the observed population self-organization.

2) The authors discuss possible neuronal mechanisms underlying their behavioural rules. Ideally, it would be good to apply or at least suggest possible experimental tests of these mechanisms, in particular of the proposed important medium-range taxis between neighbouring worms. It is suggested that this might be O2 tension mediated: how might this be tested? They do provide convincing experiments that exclude any significant contribution of ascaroside pheromones to swarming.

Other comments:

- The work also mainly compares behaviour in the standard lab strain N2, which is 'hypo-social', to behaviour in a 'hyper-social' npr-1 mutant of N2. Neither of these exactly corresponds to the natural state of almost all wild C. elegans, so the analysis is somewhat artificial; this might be more explicitly admitted.

- The authors state that to their knowledge "this swarming phenotype has not been reported in C. elegans previously", which betrays ignorance. For example, the following observation in Hodgkin and Barnes (2002, PMID: 1684664): "When a population has consumed almost all the bacteria, the worms… form a swarming mass that moves as a wave across the remaining bacterial lawn, and then disperses when all the bacteria have been consumed." This indicates that N2 swarms under appropriate conditions, perhaps of higher bacterial food density. The authors' experiments were performed only on "thin, even bacterial lawns".

- They also state that "it is still unclear whether aggregation and swarming have a function in the wild". Swarming is almost certainly naturally advantageous in predation on pathogenic or repellent bacteria, as a result of the 'wolfpack' effect that has been studied in myxobacterial swarms, to which some reference should be made. This reviewer, and others working on interactions between C. elegans and soil bacteria, have often observed N2 swarming at the edge of unpalatable bacterial lawns. These swarms appear to allow the worms to overcome bacterial defences by collective action of digestive enzymes or other secretions.

- Do worms in the experiments move in purely 2D, i.e. never crawl on top of one another and never overlap? Is this true for the agents in the simulations?

- Better justification of the level of complexity chosen to model worms with agent-based approach is necessary. Why would simple "vector particle" models fail? How important is that each worm is multi-segmented? How important are the elastic properties of the worm? Does the assumption of the propulsive force generation at the head vs throughout the body affects the motion?

- By comparison with the bacterial literature, the term swarming used by the authors could be somewhat confusing (e.g. by comparison with the widespread phenomenon referred to as bacterial swarming, e.g. PMID: 20694026). It is also probably acceptable to use the term "swarming" in the worm field, but a clear definition should be added in the Introduction.
