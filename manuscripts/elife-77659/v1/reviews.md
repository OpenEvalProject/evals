# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77659.sa0](https://doi.org/10.7554/eLife.77659.sa0)

This valuable study is of relevance to the field of collective animal behaviour. The proposed crop-cue-based motion-switching rules provide a welcome alternative to other models that assume far more deliberative abilities of ants. The authors present solid evidence to back up their claims.


---

# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77659.sa1](https://doi.org/10.7554/eLife.77659.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Emergent regulation of ant foraging frequency through a computationally inexpensive forager movement rule" for consideration by eLife.

Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Theodore P. Pavlic (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this decision letter to help you prepare a revised submission.

Essential revisions:

1) It was confusing to the reviewers how exactly the inward/outward directions were defined. Is it simply away, or towards the entrance? It is not clear from the text, and since this system is not symmetric (cubic with entrance at one of the corners) the authors should clarify this point.

2) For the biased random walk analysis of the ants, the authors "coarse-grained" the steps as being "inwards", "outwards" and "stay". It is not clear how this level of granulation is justified. Since the authors have access to the actual trajectories and all trophallaxis events, why not just calculate the actual turning angles between consecutive steps the ants take? This would give an actual assessment of both the bias and the noise imposed on the random walks, which the authors could then use directly in their models. Some discussion of this point is important.

3) It would be important to better connect the authors' previous mechanism (relating the colony's response to individual ants sensing their own food levels and its temporal dynamics) to the new mechanism (spatial-temporal dynamics). Are they mutually exclusive? It would be useful to elaborate on this in the Discussion.

4) The addition of a few supplementary movies from the experiments, showing ants moving toward the entrance with low food loads, and moving away from the entrance with high food loads, would be extremely helpful.

5) Much of the authors' argument rests on trajectories and statistics generated from a two-dimensional computational simulation that may be overly simplistic. The computational model simulates a single forager (as opposed to multiple foragers) arriving to a nest that is partitioned into a grid of squares with an immobile ant in the center of every square. Foragers move in discrete steps from square to square, with the guarantee of an interaction in each step. This "grid world" model of ant nest movements is significantly different from the experience of real foraging ants returning to the nest, and the authors even admit that deviations between the empirical data and the computational model may be due to nest-ant clumping and interaction sparsity in the paths of real ants. Continuous-motion agent-based models are commonly used to investigate collective-motion hypotheses, and so the choice of a grid world model instead seems surprising and weakens the authors' arguments. Furthermore, while the deterministic mathematical model of grid-world forager trajectories seems overly simplistic, the stochastic model in the Appendix that attempts to validate the deterministic model's results seems to have some potential flaws and is itself not validated experimentally against replicated simulation data. Instead of perfecting these models, the authors could bolster their arguments using more familiar approaches from statistical mechanics that might help explain the likely depth an ant "diffuses" into such a nest. In the current form of the manuscript, the mathematical models do not add much beyond the simulation models (and the lack of replication of the simulated data may make some readers wonder if the example trajectories were representative). Further discussion of continuum models would help to bolster the authors' claims, and the reviewers agreed that direct comparison of the authors' results from grid-based simulations to simulations from continuum models likely would be the most effective way to strengthen the manuscript and support its conclusions (see comments from Reviewer #2 for more details).

6) There are a few questionable parameters that the authors have chosen in their model, likely for analytical tractability. For example, the authors assume that at each interaction between a forager and a nest ant, the forager offloads enough food to fill 15% of the crop space remaining in the receiving ant. One can assume that this parameter is something like the 63.21% associated with an exponential time constant or may be based on empirical measurements of transfer in real ants, but the actual justification is not completely clear from the manuscript. Because the mathematical models make predictions that depend on these parameters, their existence (and plausible values) is itself an important assumption that needs to be defended for the argument to be compelling.

7) The behavioral model described by the authors assumes that ants are able to choose a direction toward their nest's entrance at any time. This within-nest path-integration ability does not seem cognitively inexpensive, which narrows the cognitive distance between the behavioral model they propose here and the one they had proposed in their prior work, and weakens the argument for the relevance of this new model. The authors failed to place their work within the context of other simple cue-based motion-switching behaviors discussed in the literature for other taxa -- such as "running" and "tumbling" in E. coli bacteria -- but if they had, they might have envisioned an alternative crop-based motion rule that would have the same effect as their current rule (i.e., movement toward the entrance on low crop state) without having to assert that the ant moves directly back towards the entrance. Bridging the work to these other studies would be important here.

8) Focusing on the explanatory power of this model specifically for (some) ants, the authors do not address how to empirically reconcile the ambiguity between the more cognitive mechanisms proposed in their previous work (where ants "decide" to exit a nest) and the current proposal (where the nest cavity "decides" when the ant will exit). For this new hypothesis to be useful, it must be empirically discriminable from the previous hypothesis. At first glance, it is difficult to imagine an experiment that would lead to different predicted behavior from the two different hypotheses. In other words, at the moment, it seems impossible to tell whether the "ant decide" or the "nest decide" model is a better predictor of real ant behavior/cognitive architectures. The lack of discriminability becomes even more problematic when considering that the current version of the model actually increases some cognitive demands by assuming (as described above) that ants keep track of the position of the entrance over the trajectory within the nest.

9) In the stochastic model in the Appendix (an integral is used when instead of a sum, perhaps?), it seems like the average values s(Bin) and s(Bout) should depend on F. However, they are treated as constants in Equations (S3) - (S5). If the authors tried to empirically validate the stochastic model by generating many simulated replications and then plotting averages against this prediction, they would likely have a hard time calculating s(Bin) and s(Bout) to generate their numerical predictions. The authors should clarify this point.

10) "It has recently been suggested that physical space can be utilised to offload computation from individuals' cognition to their environment in the context of collective quorum sensing ([5])." It seems surprising to say that this is the first time this has been suggested. For example, the literature on the effects of nest architecture cited by Reviewer #3 is based on this idea (see below). More generally, the idea that movement patterns determine encounter rates and thus communication was suggested for ants decades ago. This study seems to sidestep many spatially explicit models on information exchange through encounters (e.g., see review in Gordon 2020 Ann Ent Soc 2020doi: 10.1093/aesa/saaa03). The models use assumptions that ignore the effects of space. The impact of these assumptions should at least be considered.

11) The manuscript says nothing about the empirical data which were obtained in another study. This manuscript should say how "average crop load" was measured, including some measure of variation. The manuscript should also say how "foraging frequency" was measured and under what conditions. How often are these conditions likely to occur for colonies of this species?

12) What is the "linearity of foraging frequency"? Line 49: "Progress has also been made toward revealing the local mechanism underlying the linearity of foraging frequency, though to a lesser extent. " Again, on lines 105-106: "emergent linear relationship between foraging frequency and total colony hunger." Better definition of this term is important.

13) Figure 5D – empirical results: Why does the forager have a higher crop load at the end of its time inside the nest than at the beginning?

14) If "hunger" is defined as below as the amount of food in the colony, then it is circular (not "intriguing") to say that the rate at which food comes in matches the total level of "hunger" or level of food.

15) It seems strange to cite Oster and Wilson to say that ants collecting food are called foragers. There is at least 100 years of work on ants before Oster and Wilson that referred to "foragers".

16) Lines 36-38: "Trophallaxis is the main food-sharing method in many ant species 36 ([12]). Each time a laden forager returns to the nest, she unloads the food from her crop to several receivers via 37 trophallaxis. The food further circulates through a complex trophallactic network among all colony members38 ([9], [13]-[17])." This is a misleading way of framing this study, because it equates the distribution of food sources among ants within the nest with the unloading of nectar by foragers. There are many species that use trophallaxis but not directly from foragers.

17) The results suggest that unloading is associated with whether a forager moves toward or away from the nest entrance. This is called the "deeper nest", but it seems the previous empirical study was performed in a flat arena, and the simulations do not include anything about depth. Thus it gives the impression that an ant associates unloading with going up or down, but in this study, unloading was associated with toward or away from the entrance from an arena. It would be better not to use "deeper" to mean "away from the entrance" as this evokes an image of depth in an ant nest, which is misleading. Since "deep" has an ambiguous meaning here, it is difficult for the reader to know what "deepening" and "lengthening" mean in line 140: "The simulation qualitatively reproduced the lengthening and deepening of foragers' trips."

18) It was unclear what was meant by: "Note that contrary to the assumptions used in our previous paper ([1]), here a forager never decides to exit the nest. Rather, an exit occurs if the forager's motion brings her to the nest exit." What is the difference between 1) a decision to go to the nest exit and leave the nest, and 2) going to the nest exit and leaving? In the literature on behaviour, decision-making, and cognition, 1) and 2) are the same.

Reviewer #2 (Recommendations for the authors):

This very clever manuscript was a joy to read, and I look forward to when it is finally published. These crop-cue-based motion-switching rules provide a welcome alternative to other models that assume far more deliberative abilities on ants, and it will be valuable to add this example to the collective motion and collective decision-making literature. That said, I think there are three major issues that I feel warrant addressing in a revised version: overly simplistic models, no connections to similar phenomena in motion ecology as well as statistical mechanics, and potential flaws in the stochastic modeling approach. I will address each of these below.

Issue 1: Overly simplistic models

The manuscript's arguments are currently tailored to overly simplistic models. Choosing models for natural systems necessarily means leaving out some realism, but the grid-world models used by the current manuscript do not achieve the appropriate benefit-cost balance of analytical tractability to organismal fidelity. A good, illustrative simulation model need not have all of the details of the real system but it should have plausible relative scaling. A grid-world model of an ant nest, where there is an ant on every square and the single incoming forager moves from every ant to every other ant at each step is a significantly distorted proxy for a real ant colony. Agent-based modeling tools (and/or API's) allow for quickly building models of mobile agents that move in an approximation of continuous space, where an incoming forager could be moving around a nest that itself had nestmates that were moving. Putting both types of agents into motion will create natural gaps and clumps that help to create a more realistic temporal scales of events – possibly allowing for Figures 4B and 4C to have the same units as Figure 4A. Furthermore, simulating multiple foragers simultaneously might be important as the foragers will effectively compete for off-loading opportunities. Although using a continuous-time model may seem to complicate building mathematical models, the more realistic motion rules may actually simplify some of the analysis as they can lead to justifying well-mixedness assumptions that allow for using mean-field ODE models. In summary, although the grid-world simulations provide interesting visual evidence that such a model can generate hunger-dependent penetration depths inside a colony, such grid-world models are not convincing when discussing the actual temporal duration of those trajectories. Demonstrating these results in continuous-time agent-based models with potentially multiple returning foragers as well as mobile nest ants will be convincing and will able to be scrutinized in terms of temporal fidelity as well.

Issue 2: Connections to motion ecology and statistical mechanics

The manuscript in its current form describes what would happen if an ant had the ability to decide whether to move deeper within the nest or turn around and move directly toward the exit. From a mechanistic perspective, it would make more sense to suggest a mechanism (or family of mechanisms) that tend to have those two effects without assuming that the ant can achieve both of those subtasks. For example, following the flocking literature, it seems much more likely that ants would be able to move "toward center" or "away from center" (or even "toward darkness" (skototactic) and "toward light" (phototactic)). If the cue-based switching proposed lead to these two outcomes and then ants could follow walls when unable to move further away from center, then it seems likely that the same tendencies identified by the authors would be met without actually having to assert that ants can path integrate an "entrance vector" continuously. So I would recommend re-running simulations with more generic "inward" and "outward" motions. It is my guess that a wide variety of switching behaviors will lead to similar outcomes (albeit with a lengthening of the duration an ant spends in a nest, which might actually bring the simulations closer to the real traces anyway).

Event-based switching from one searching behavior to another is not unprecedented in the motion literature. Fish schooling literature (from Iain Couzin et al.) has shown that switching from one velocity to another based on whether you're in a dark or light area can lead to aggregations of fish, for example. A wide variety of animals (and even ants, such as Temnothorax albipennis when searching for its lost leader in a tandem run) incorporate switches from straight runs to circular searching and back again based on cues. Plume tracking in many flying insects is thought to involve simple switching rules that help ensure movement "upstream" despite the ugly turbulent flows in the odor plumes that are far from a smooth gradient. And that brings me to the example I mentioned in the public review -- E. coli "running" and "tumbling," which has been associated with chemotactic gradient climbing. Interestingly, E. coli are too small to sense a spatial gradient, and so some sequential sampling is apparently incorporated to estimate when it is ready to switch from rotating flagella in one direction ("running" straight) to the other direction ("tumbling" randomly). That implies that even bacteria can sense rate, which is possibly an argument for ants being able to sense the rate that their crop is being depleted. That said, if we forget about using the bacteria as a minimal model of cognition, we can focus on "running" and "tumbling" as a motion framework that ants could be using too. If the hypothesized ants can be conceptualized as "running" at high crop state and "tumbling" at low crop state, then could they be interpreted as climbing a nutrient gradient (i.e., in toward the nest when the nest is full of food but out of the nest when the nest is not full of food)? Not only would generic "tumbling" (as opposed to "moving toward the entrance") be less cognitively demanding for ants, but making the connection between ant and bacterial motion rules would help extend the scope and scale of the potential impact of this manuscript. So I would encourage: (a) seeing if simply increasing the probability of making random turns when the crop is low leads to a similar result as the current approach, and (b) considering whether "run" and "tumble" provides a gradient-climbing interpretation of what the foraging ants might be doing (i.e., they either climb into a "full" nest or they climb out of an "empty" nest toward a full environment).

Along those lines, there seem to be significant missed opportunities to interpret the trajectory density from a statistical mechanics perspective. Stating that trajectories tend to penetrate deeper into a test when colonies are "full" and is shallower when colonies are "empty" suggests that colony state might be viewed as a kind of "temperature", and the depth of penetration could reflect a corresponding Boltzmann distribution setup by the motion of foraging ants diffusing into the colony -- where those foraging ants would be excited by the "temperature" of the colony. If this interpretation is correct, then this statistical-mechanics perspective suggests other mathematical models that would be more general and more convincing than the simplistic mathematical models within the current manuscript (see more comments about these below). Alternatively, it might be possible to think of a sort of "contact potential" between the foragers (from outside) and the nest ants. When the colony is full, foragers can diffuse very far into the nest before the "charge imbalance" stops them from going further. However, when the colony is hungry, the "charge imbalance" balances at a much shorter distance (and so there is very little diffusion). At this moment, these are just descriptive models which may fit the data well. However, these descriptive models have specific physical phenomena associated with them which may inspire other ways to think about the motion of the individual ants. In general, diffusion is a very fundamental process which certainly applies to ants moving randomly from place to place, and so it seems like the clear modulation of penetration depth by hunger state is very likely to represent a kind of temperature. In this interpretation, the fuller the ant colony, the "more energetic" the forager, which is a happy coincidence.

Issue 3: Possible flaws in stochastic modelling approach

In the stochastic model in the appendix (where an integral is used when I think a sum was intended), it seems like the average values s(Bin) and s(Bout) should depend on F. However, they are treated as constants in Equations (S3) – (S5). Consequently, the stochastic model doesn't make sense to me. If the authors tried to empirically validate the stochastic model by generating many simulated replications and then plotting averages against this prediction, I think they would have a hard time calculating s(Bin) and s(Bout) to generate their numerical predictions. If I were building this model, I would have probably started with Markov renewal-reward theory. The individual forager encounters ants randomly and exchanges a random amount of food with them. The renewal process counts up the number of encountered ants, and the reward is the accumulated amount of food transferred to other ants. Framed this way, a wide range of results on Markov renewal-reward processes can be used to characterize the experience of the forager.

An alternative approach to the stochastic modeling would be to consider the hitting time of a drift-diffusion process. The manuscript already discusses how the "hunger" of the colony tunes the drift of such a process, with a "full" colony creating significant drift away from the absorbing barrier and an "empty" colony creating significant drift toward the absorbing barrier. Why not actually try to model the ant formally this way and import all of the mathematics already developed for such a system?

Reviewer #3 (Recommendations for the authors):

Methodological questions:

1). Space

"It has recently been suggested that physical space can be utilised to offload computation from individuals' cognition to their environment in the context of collective quorum sensing ([5])." It seems strange to say that this is the first time this has been suggested. For example, the literature on the effects of nest architecture cited here is based on this idea.

More generally, the idea that movement patterns determine encounter rates and thus communication was suggested for ants decades ago. This study sidesteps many spatially explicit models on information exchange through encounters (e.g. review in Gordon 2020 Ann Ent Soc 2020doi: 10.1093/aesa/saaa03).

The models use assumptions that ignore the effects of space. The impact of these assumptions should at least be considered.

a. How does the crop load of a recipient influence its location inside the nest? Social insect colonies are spatially organized; e.g.:

Franks NR, Tofts C. Anim. Behav. doi:10.1006/anbe.1994.1261;

Mersch DP et al. 2013 doi:10.1126/science.1234316;

Crall et al. Nat. Comm. 9:1-13.

b. How does a forager's movement influence the probability of meeting another individual with a particular crop load?

Davidson 2017 J. R. Soc. Interface.http://doi.org/10.1098/rsif.2017.0413

The model considers only one meeting. How would a 2nd, 3rd, … encounter influence the results?

c. Setting the bias to go toward the entrance equal to the bias to move away also has a strong effect on the results. What is the effect of removing this assumption?

d. Variation among ants met in crop load determines the probability that a forager will encounter a particular set of crop loads for a particular movement pattern. E.g. O'Shea-Wheller et al. 2017. Proc. R. Soc. B Biol. Sci. 284: 20162237.

Assuming there is no variation probably has a strong effect on this result, lines 216-18: "Nevertheless, it turns out that the average amount of food given to each nest-ant is still proportional to (1 − F), and that since both the inward and outward biases are constant, the number of steps spent with each nest ant is, on average, also constant (neglecting boundary effects)."

2). Data

The manuscript says nothing about the empirical data which were obtained in another study. This manuscript should say how 'average crop load' was measured, including some measure of variation. The manuscript should also say how 'foraging frequency' was measured and under what conditions. How often are these conditions likely to occur for colonies of this species?

3). Linearity

What is the 'linearity of foraging frequency'?

Line 49: "Progress has also been made toward revealing the local mechanism underlying the linearity of foraging frequency, though to a lesser extent."

Again, lines 105-106: “emergent linear relationship between foraging frequency and total colony hunger.”

I think this is the relation of rate of foragers exiting the nest vs estimate of total amount of food in the crops of workers in the nest? Why is it important that this relationship be linear? It seems more likely that it would be nonlinear, e.g. that foragers would be more likely to exit when levels are very low and not as much when levels are high.

4). Unloading

Figure 5D – empirical results: Why does the forager have a higher crop load at the end of its time inside the nest than at the beginning?

Conceptual issues and presentation:

The manuscript refers to 'ant colonies', in the abstract, introduction and discussion, as if these results apply to all ant colonies. However, the species studied here is one that feeds on nectar. While there are many other such species, they are not the majority of ant species. What is unusual is that they ingest their food, instead of just carrying it back to the nest, and they must unload it before they can collect more. The manuscript should make it clear that the process described here has evolved in relation to this particular, unusual type of feeding. In fact a similar process has evolved independently in honey bees, which also collect nectar. While Seeley's work on this in honeybees (reference 44) is mentioned in passing, the manuscript does not discuss this resemblance between this aspect of foraging behavior in honey bees and a similar and relatively unusual one in ants.

1). If 'hunger' is defined as below as the amount of food in the colony, then it is circular (not 'intriguing') to say that the rate at which food comes in matches the total level of 'hunger' or level of food.

Line 31: "Intriguingly, the rate at which food enters the colony matches the total level of hunger in the colony 31 ([1], [8], [9]).

Line 43-44: "Specifically, each forager's unloading rate was proportional to the 4total "empty crop space" in the colony (hereinafter, 'colony hunger')."

2). Strange to cite Oster and Wilson to say that ants collecting food are called foragers. There is at least 100 years of work on ants before Oster and Wilson that referred to 'foragers'.

3). Line 31 – what is a distributed nature?

4). Trophallaxis

Lines 36-38y: "Trophallaxis is the main food-sharing method in many ant species 36 ([12]). Each time a laden forager returns to the nest, she unloads the food from her crop to several receivers via 37 trophallaxis. The food further circulates through a complex trophallactic network among all colony members38 ([9], [13]-[17])." This is a misleading way of framing this study because it equates the distribution of food sources among ants within the nest with the unloading of nectar by foragers. There are many species that use trophallaxis but not directly from foragers.

5). The results suggest that unloading is associated with whether a forager moves toward or away from the nest entrance. This is called the 'deeper nest', but it seems the previous empirical study was performed in a flat arena and the simulations do not have anything about depth. Thus it gives the impression that an ant associates unloading with going up or down, but in this study, unloading was associated with toward or away from the entrance from an arena. It would be better not to use 'deeper' to mean 'away from the entrance' as this evokes an image of depth in an ant nest, which is misleading. Since 'deep' has an ambiguous meaning here, it's difficult for the reader to know what 'deepening' and 'lengthening' mean in Line 140: "The simulation qualitatively reproduced the lengthening and deepening of foragers' trips."

6). This is puzzling: "Note that contrary to the assumptions used in our previous paper ([1]), here a forager never decides to exit the nest. Rather, an exit occurs if the forager's motion brings her to the nest exit." What is the difference between 1) a decision to go to the nest exit and leave the nest, and 2) going to the nest exit and leaving? In the literature on behavior, decision-making, and cognition, 1) and 2) are the same.

7) line 122: It will be confusing to readers to call the forager's moving around inside the nest a 'trip', since it is very common to call its journey outside the nest a 'trip'.
