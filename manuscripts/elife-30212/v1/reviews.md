# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30212.019](https://doi.org/10.7554/eLife.30212.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Evolutionary dynamics of incubation periods" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. One of the reviewers, Martin A Nowak, has agreed to share his name.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

1) All the reviewers found the calculations extremely interesting and considered the results to be novel and important. However, there was a shared concern that the connection of these results with the biological phenomenon of the incubation period was not on firm ground. In particular, the assumption that 100% – or close to 100% – of the host cells are infected when symptomatic infection starts was not well-motivated, and the biological plausibility of this assumption was unclear.

2) We would like to encourage the authors to reconsider the interpretation of their findings. Ideally they should provide a broader a list of biological phenomena (not only incubation periods) that could be described by their model.

3) If they want to strengthen their interpretation of incubation periods, a mechanistic description how the model describes specific diseases is needed along with a discussion of possible caveats.

4) It would also be of interest to discuss the question of time-varying N (either growing N, or declining N as a result of the pathogen killing host cells). However, following consultation, it was felt that anything more than discussion of this question is beyond the scope of the current work.

Reviewer #1:

Strogatz et al. present a model for why the length of disease incubation periods tend to have a right-skewed probability distribution. The core idea is marvelously simple: even in the absence of complications such as host or pathogen heterogeneity, a simple stochastic model for within-host disease spread predicts a right-skewed distribution for the time between inoculation and the pathogen reaching a threshold value (corresponding to the threshold of immune activation that marks the end of the incubation period). The main text is unusually clearly written for a pure theory paper.

My primary concerns surround the relatively limited connection back to the biology. The authors consider multiple different possibilities for within-host network connectivity and provide some biological justification for the different topologies (e.g., structured tissue = 3d lattice, epithelium = 2d lattice, etc.); however:

1) The analysis of the Moran model focuses on the time to fixation of the invading allele (i.e. 100% infection of the modeled network); however, immune activation does not wait until 100% of the population is infected but rather activates at a much lower threshold (admittedly again in a stochastic fashion). One of the key findings of this work is that a right-skewed distribution arises due to the "coupon collector problem" where the last few uninfected nodes in the graph can take a long time to be infected, particularly for high-dimensional topologies. However, if the incubation period were to end when, say, any 1% of cells were infected rather than 100%, then the coupon collector problem seems less (or perhaps not at all) relevant.

2) Infection / reproduction in a spatial situation will often happen in parallel rather than serially. The argument that high-dimensional topology may lead to a slow down of the final infections appears predicated on the idea that the rate of infection is constant due to the serial nature of the Moran model – but the overall infection rate presumably increases as a function of the surface area of the infected volume (and analogously for other topologies). Does this really not matter for the distribution of time to fixation? This area is not my specialty, but the theory surrounding Fisher's wave of advance may be relevant.

3) Many pathogens cause infections in a bursting fashion (e.g., lytic viruses) for which it is not obvious if the Moran model assumption of one random birth / one random death at a time is relevant.

Reviewer #2:

Ottino-Loeffler et al. propose a simple and elegant solution, based on invasion dynamics in structured population, to the interesting observation that incubation periods for a variety of diseases are right-skewed. I found the idea to be very elegant, the text well-written, and overall the arguments to be compelling and easy to follow. I especially liked the interpretation for the dispersal coefficients naturally ranging between certain limits. However, I have a few concerns/questions that I would like to see addressed:

1) In order to apply the ideas of evolutionary graph theory the authors assume that the populations are finite (all graphs have only N nodes); however, this is not always true (certainly not for all the diseases that the authors mention in the abstract and introduction) and I would have liked to have seen from the authors at the very least an acknowledgement of this strong assumption and a discussion of how relaxing this assumption might affect the conclusions. It would be even better (and really interesting) if the authors could pick one example of dynamically-growing network (this should be doable at least for the complete graph) and see how that affects their predictions.

2) The Death-birth (DB) dynamic that the authors employ is actually different from the DB dynamic proposed by Ohtsuki et al. 2006 (unlike the BD dynamic which is the same). Ohtsuki et al. consider death to be random (all nodes have probability 1/N) and birth competition to be among the neighbors, proportional to their fitness. Of course, it's no problem proposing a new variant; I'm just curious whether the authors had a biological reason for choosing this variant of the DB update rule. Especially since they find in their Materials and methods (section on truncation) that the update rule actually matters a lot, a fact that has been observed in evolutionary graph theory more broadly. On that note, I thought this result was sufficiently important that it deserved at least a couple of sentences in the Discussion (rather than just being mentioned in the Materials and methods); I had the same reaction to all the results in that section ("Testing robustness to update rule, fitness, and truncation"), which I thought deserved some mention in the main Discussion.

3) My final point is more a question than a concern: the authors apply this method to in-host dynamics and incubation periods; however, it seems like it could apply to epidemiological questions as well (e.g. spread of flu in a population). Have the authors considered the parallels? Are there any data analogous to incubation periods that could be employed to show the applicability of this model to epidemiological questions as well?

Reviewer #3:

In Evolutionary Dynamics of Incubation Periods, Ottino-Loffler et al. investigate the distribution of times to fixation and to near fixation of mutants on an evolutionary graph as a model for incubation periods. Using this conceptual framework, they endeavor to explain features of the observed distribution of incubation times, including approximate log-normality with dispersion in the range of 1.1-1.5, without invoking heterogeneity in invader fitness, disease burden at which symptoms manifest, or initial dosage.

Ottino-Loffler et al. provide analytical calculations for the distribution of fixation times on complete, star, and cycle graphs in the infinite-fitness mutant limit, as well as numerical simulation results on a variety of other graphs. The distribution of times to fixation for a mutant in a structured population is an extremely important and interesting theoretical question. The authors provide novel and fascinating mathematical results.

I am very much in favor of publication of these findings. I do have some questions or concerns regarding the biological interpretation of the paper.

What is the relationship between the model, specifically time to fixation in a Moran process on a graph, and the biological phenomenon of an incubation period. Clarification about the biological motivation for this theoretical framework and for the different update rules could strengthen the paper. In particular, which of the several diseases mentioned in the paper does the model apply to, and why? Also, clarification regarding the choice of fixation time to quantify the length of the incubation period would strengthen the paper. Lowering the threshold to below 100 percent appears to remove the skew in some instances.

Second, might the distribution of clock times differ from the distribution of step times in the process.

Third, certain model choices produce symmetric, rather than skewed, distributions of times to a threshold. I am curious if a more complete investigation of this observation could shed light on the appearance of skewness in different evolutionary scenarios.

A final small, technical clarification would help to understand the derivation of skewness when r = 1 at the end of the paper. How is the number of steps which do not change the number of mutants being counted? Further, at the end of the fourth paragraph of the subsection “Asymptotic skew of conditioned random walk”, should An(1) be Mn(1)?

Again I wish to emphasize the great interest and novelty of this work. While some issues associated with the interpretation of the paper remain unclear, I think that the authors will be able to address them by pointing to biological scenarios, perhaps even outside of infection, in which their calculations provide valuable insight.
