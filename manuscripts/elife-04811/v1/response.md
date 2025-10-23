# Author response - Round 1

Authors:
- Mehdi Keramati
- Boris Gutkin

## Response text

DOI: [10.7554/eLife.04811.032](https://doi.org/10.7554/eLife.04811.032)

Animals indulge in many behaviors that violate the premises of physiological homeostasis, like obesity and drug-taking behavior. This appears to be an issue that calls into question some of the fundamental assumptions of this work.

We thank the BREs for prompting us to address this issue. In fact we already performed the simulations showing how irrational behaviors might arise within our theory, yet did not include it in the previous version of the manuscript as we previously felt that a full-blown treatment of irrational behaviors is beyond the scope of this paper and would merit a further publication. To address the BREs’ concern, in the present manuscript we added a subsection titled “Irrational behavior: the case of over-eating.” to illustrate (with simulations) one of the points of vulnerability of our theory that can induce irrational choices. Moreover, in the subsection “Limitations and future works” we discuss on how to approach other pathologies including drug-addiction and anorexia, as results of other mechanisms of our framework going awry. Also, as communicated to the editor previously, modeling drug addiction within our “Homeostatic Reinforcement Learning” framework has been the topic of another entire line of research in our group and we are preparing a further publication on that.

Reviewer 1:

The relation of the theory to the free-energy framework, as well as the allostasis and the good regulator theorem to be explained. Also, the advantage of using optimal control as the optimization techniques to be discussed.

We agree with the reviewer that our theory has significant connections with the free-energy framework. We added a subsection titled “Previous theoretical models” in order to discuss all these and other issues in detail.

Limitations of the theory to be discussed.

We added a subsection titled “Limitations and future works”, and detailed several limitations of the model, as well as constraining assumptions that could be eventually relaxed.

Reviewer 2:

Framing the entire model around rekindling the Hull’s theory is unfortunate. Instead of framing this in a half-century-old debate, why not anchor it in contemporary scientific issues and questions? The results section does not read like a results section but like a discussion section.

We thank the reviewer for this suggestion. While we stand behind our theory’s explanatory power, we do agree that the present manuscript is only a first step in addressing the modern literature on the links between motivation and the internal physiological states. Following the reviewer’s advice, we re-structured the manuscript to make it less polemic and more result-oriented, and tried to clearly de-limit its scope. Rather than framing the whole manuscript around the Hull’s theory, we now only discuss that theory and its relevancy to our model in a subsection of the Discussion titled “Relationship to classical drive-reduction theory”. Also, in that section, we withdrew the claim of “rescuing Hall”, and instead discuss the differences between our formal elaboration and the original theory (Namely, orosensory-based approximation of drive-reduction, and integration with an RL module). Also, for the sake of caution, we only claim that our model addresses “a number of significant criticisms”, rather than “all”, criticisms against the Hull’s theory.

The Results section does not read like a Results section but like a Discussion section. For each of the subsections in the Results I would expect the question/problem to be defined clearly, then the details of how this was addressed in a simulation and then the results of the simulation (for example, one expects results to be substantively organized around/referencing figures). The 'results', as the manuscript stands, are essentially presented in brief in the figure legends. Less argument and 'defending' the model and more illustrating its function.

In response to this concern, we transferred all the other discussion-like issues to the Discussion section (i.e., Neural substrate, predictions, previous models) and greatly expanded the Results section. In the rest of the manuscript, we only focus on the behavioral/neurobiological pattern being addressed, and mechanisms by which our model explains them. We tried to explain the replicated experiments, our simulation results, and the mechanisms of the model with much more details and clarity. Furthermore, we included the full proof of the rationality and the normativity of temporal discounting in the Methods section. In fact we considered including the full proof in the main body of the paper but felt that the paper might become too cumbersome. This is a point we are ready to discuss and if eLife might allow for a “mathbox” to be embedded within the paper, which could be a good solution.

The manuscript ends up with a cavalier quality of 'our model has just solved all these problems' but the solution is superficial. The manuscript is too ambitious, attempting to implement a simple computational model of drive-reduction and then, in effect, wanting to 'put to rest' what comprised decades of (much still unresolved) controversy.

Again, the result reads more like a polemical review, both cavalier and superficial. A more focused, more empirical, less argumentative approach might be more successful.

In general, following the points raised by the reviewer we rewrote the paper in a more empirical and less argumentative way. We further pointed out in the manuscript, which issues are resolved by our model and what are the limitations (new sections added). Furthermore, we tried to clarify in the manuscript that our modeling framework is not only a simple model of drive-reduction, but gives a normative computational theory for the interplay between the former and reinforcement learning theories of motivation. Indeed the present manuscript is only a starting point for a further development of the theory, and we tried to point this out in the manuscript. We sincerely hope that the cavalier quality of our paper has been rectified.

The explanation for extinction bursts is not convincing.

We see the point raised by the reviewer and understand that our suggestion is way too speculative. We decided to remove the “Extinction burst” section from the manuscript and re-consider this issue in the future.

With respect to anticipatory responding, the proposed model is equivalent to the “incentive salience” theory.

We thank the reviewer for pointing out this apparent lack of clarity in our paper. In the new manuscript, we discuss the differences between the two models in detail, in the subsection “Relationship to other theoretical models”.

We would also like to briefly address the specific comment of the reviewer. In our theory the value of a response depends on the internal state at the time of learning and is built from a reward definition that is based on the ability of the response to produces a drive-reducing outcome. We give a precise mathematical formulation of how this should be done (normative reinforcement learning framework). And indeed the response after learning is driven by the value as opposed to by the direct drive reduction. Previously it was controversially argued that “value” in the RL algorithms is equivalent to motivational “incentive salience” (1). However, as we could best understand, the recent computation model of incentive salience separates value learning from influences of the internal state. The value is learned as in the standard RL algorithms (with respect to a reference state and based on externally defined rewards). The internal state at the time of the response then modifies the learned value. As we now argue in the manuscript such a formulation differs from our framework and is unable to account for anticipatory responses.

Just because metabolic information is signaled into the hypothalamus does not necessitate that it is a homeostatic system.

We thank the reviewer for pointing out this issue. Although discussing the neural evidence for the hypothalamus being a homeostatic system is a topic of merit, we feel that in this manuscript, we would better limit the discussion to the neural evidence that is relevant to the novel contributions of our model (i.e. the “integration” of homeostatic and learning systems). We felt that a full discussion of the substrates of the two individual systems is beyond the scope of our manuscript. However, in the new manuscript, we cited further recent review articles that point to the role of hypothalamus in homeostatic regulation.

Furthermore, in the new manuscript, we have explained that from a mathematical point of view, any regulatory system can be formulated either as a dynamical system (interaction of many effectors) or as a homeostatic regulation system. We explain that these formulations can be readily transformed into one another; particularly, the stable equilibrium (settling point) of the dynamical system is equivalent to the setpoint of the homeostatic formulation. Thus, we have tried to make it clear that setpoint vs. settling-point formulation is only a matter of the point of view.

Last but not least, one example where we could have discussed the evidence supporting the homeostatic role of the hypothalamus is in thermoregulation (see the text below). However, we did not see how to include it in the manuscript, without straying too far from issues relevant to the novel contributions of the paper.

A particularly prominent example for the role of the hypothalamus in homeostatic regulation has come over the years in the human and animal thermoregulation literature. Interestingly, the concept of an internally regulated set point appears prominently in that body of literature. The classical review by Benzinger (2) establishes experimental evidence for a thermal set point as a physiological property and points out the role of the “preoptic-spraoptic region of the hypothalamus” in central regulation of the body temperature. The suggestion that hypothalamic circuits play a role in maintenance of thermal homeostasis by translating sensed temperature into neural activity was formalized by Hammel (3) in a model proposing hypothalamic circuitry where integration of thermo-sensitive and thermo-insensitive neuronal activities could lead to dynamic encoding of the thermal setpoint. Populations of heat-sensitive neurons have been identified in the hypothalamus (4, 5): they increase firing rate with increasing body temperature. The heat-sensitive (HS) and heat-insensitive (HI) neurons synaptically innervate two sets of effector neurons. Heat-loss effectors are excited by the heat-sensitive cells and inhibited by the heat-insensitive cells in a manner that balances these inputs at 37C body temperature. Heat-production effector neurons are in turn inhibited by the HS neurons and excited by the HI neurons. Over the years, heat-loss/production effector neurons have been electrophysiologically identified (6–8) and anatomically mapped. The regulatory loop is closed by the thermosensory afferents from the periphery to the HS (but not the HI) neurons (e.g. see (9)). Manipulations of the POA induce body temperature changes (e.g. see (10)) and the effector neurons have been implicated in control of organismal thermoregulatory responses (e.g. as reviewed in Morrison and Nakamura (11) and Boulant (12)) including shivering (13). Furthermore, there is experimental evidence that the regulated thermal temperature point is influenced (or dynamically set) by signals that not in themselves directly related to temperature (e.g. hormonal levels, inputs from joint mechano-receptors receptors) and varies from individual to individual (see (12) for review).

A distinction between tonic and phasic dopamine activity needs to be made.

To make a distinction between tonic and phasic dopamine, we clearly stated in the new manuscript that our model, as in the classical RL model, only addresses the burst (i.e. phasic) activity pattern of dopamine neurons. How changes in the tonic DA levels might be incorporated into our theory is an active topic of current research in our group.

Reviewer 3:

The theory is based on abstracted concepts like homeostatic set point and distances in the homeostatic space that do not directly correspond to any biological properties.

Indeed, our mathematical theory, as any mathematical theory, requires several constructs to be defined. Above, in the response to reviewer 2, we discussed how the concepts used in our framework relate to ideas of dynamically-maintained internal equilibrium and potentials of dynamical systems. The functional equivalency of the two approaches establishes a correspondence between their neurobiological implementation. Thus, we respectfully beg to differ with the opinion of the reviewer, we believe that concepts we use do have connections to biological properties. For example the homeostatic space is simply a coordinate system where the various physiologically regulated quantities are represented: temperature, glucose levels, etc. Also, the setpoint is just equivalent to the stable equilibrium of the underlying dynamical system.

Let us take the example of temperature. Without going into details, as discussed in the text in response to the second reviewer, there are multiple classes of temperature receptors peripherally, and temperature sensitive neurons in the hypothalamus. There have been data-driven suggestions in the literature that activity of such neurons, informed by peripheral afferents, together with temperature insensitive neurons in the hypothalamus, encode the thermal setpoint (approx. 37 degrees) (3–5). There is further evidence that inputs from such neurons, create cold-producing and heat-producing effector neurons (6–8). Modern work on human thermoregulation experimentally suggests an existence of temperature space and “energy functional”, or in our terms, drive function (14).

The model assumes that organisms experience all paths in the homeostatic space, and only then can choose the shortest path. However, once the animal reaches an extreme homeostatic deviation, it can never return (due to death).

Indeed we thank the reviewer for pointing out that we needed to clarify this point. We added a new subsection titled “Stepping back from the brink”, and addressed this issue in detail. In fact our model predicts that animals should learn to act preventively to avoid states with drastic deviations (even without experiencing them directly).

The authors claim to provide a normative explanation for temporal discounting for the first time. However, alternative factors such as the environment being less and less predictable as one moves to the future seem to be a plausible explanation of temporal discounting.

Indeed we agree with the reviewer that temporal discounting intuitive sense for a number of reasons including uncertainty of outcomes in the future, changing environments, etc. However the point we attempted to make was more formal and mathematical: if we were not to include discounting, behavioral policies that maximized rewards did not necessarily minimize the total deviation from the homeostasis and hence could endanger the animal. Hence lack of discounting did not result in equivalence of reward maximization of homeostatic defense. Temporal discounting ensured that such did not happen and ensured the rationality of defending homeostasis. In view of the reviewers comments, we realized that our claim was overreaching and withdrew the claim that our normative explanation for temporal discounting is the only possible explanation. Though, we have not been able to find any alternative formal mathematical explanation.

Quoting form the review: I question whether the theory is falsifiable, as I do not see specific testable predictions.

We thank the reviewer for pointing us toward this point. We added a subsection titled “predictions”, and listed five testable predictions of the model.

Throughout the results I would have preferred either more incorporation of the equations or stronger references to the methods.

We tried to incorporate more formal details in the text, particularly in the development of the theory. At the same time, we felt that including the full mathematical proofs in the main text of the paper would make it too cumbersome. These are now in the Materials and Methods section.

When free parameters in the model are fit to one data set, they should show they can reproduce other data without extra fitting.

We thank the reviewer for this comment. It should be mentioned that the different experimental data we have replicated in the paper come from different species (rat in the anticipatory responding task, and pigeon in the oral/fistula water-seeking task). Thus, it is not surprising that the free parameters have different values for different experimental data sets. For every individual dataset, however, the value of free parameters are chosen to replicate the first part of data, and then the same values have successfully predicted the second part. That is, for the case of anticipatory responding simulations, the free parameters are derived according to the training days (the first 8 days of the experiment), and then are used for predicting the extinction days, as well as the re-acquisition day. Similarly, for the case of oral/fistula water-seeking experiment, the free parameters are chosen to best explain the reinforcement experiment (Figure 7), and are then used for predicting the satiation experiment (Figure 8).

It is also noteworthy that although free parameters are different across different experiments (different species), the essential patterns of simulation results hold for a wide range of free parameters, and the specific values used in every experiment are only to replicate that specific data.

References:

1) McClure SM, Daw ND, Montague PR (2003) A computational substrate for incentive salience. Trends in Neurosciences 26:423–428.

2) Benzinger TH (1961) The diminution of thermoregulatory sweating during cold-reception at the skin. Proceedings of the National Academy of Sciences of the United States of America 47:1683–8.

3) Hammel H (1965) in Physiological Controls and Regulations, eds Yamamoto W, Brobeck J (Saunders, Philadelphia, PA), pp 71–97.

4) Makayama T, Elisenman JS, Hardy JD (1961) Single unit activity of anterior hypothalamus during local heating. Science 134:560–1.

5) Griffin JD, Kaple ML, Chow AR, Boulant JA (1996) Cellular mechanisms for neuronal thermosensitivity in the rat hypothalamus. The Journal of physiology 492 ( Pt 1:231–42.

6) Edinger HM, Eisenman JS (1970) Thermosensitive neurons in tuberal and posterior hypothalamus of cats. The American journal of physiology 219:1098–103.

7) Curras MC, Kelso SR, Boulant JA (1991) Intracellular analysis of inherent and synaptic activity in hypothalamic thermosensitive neurones in the rat. The Journal of physiology 440:257–71.

8) Dean JB, Boulant JA (1989) Effects of synaptic blockade on thermosensitive neurons in rat diencephalon in vitro. The American journal of physiology 257:R65–73.

9) Cliffer KD, Burstein R, Giesler GJ (1991) Distributions of spinothalamic, spinohypothalamic, and spinotelencephalic fibers revealed by anterograde transport of PHA-L in rats. The Journal of neuroscience :theofficial journ al of the Society for Neuroscience 11:852–68.

10) Chen XM, Hosono T, Yoda T, Fukuda Y, Kanosue K (1998) Efferent projection from the preoptic area for the control of non-shivering thermogenesis in rats. The Journal of physiology 512 ( Pt 3:883–92.

11) Morrison SF, Nakamura K (2011) Central neural pathways for thermoregulation. Frontiers in bioscience (Landmark edition) 16:74–104.

12) Boulant JA (2006) Neuronal basis of Hammel’s model for set-point thermoregulation. Journal of applied physiology (Bethesda, Md: 1985).100:1347–54.

13) Zhang YH, Yanase-Fujiwara M, Hosono T, Kanosue K (1995) Warm and cold signals from the preoptic area: which contribute more to the control of shivering in rats? The Journal of physiology 485 ( Pt 1:195–202.

14) Kingma BR, Frijns AJ, Schellen L, Van Marken Lichtenbelt WD (2014) Beyond the classic thermoneutral zone: Including thermal comfort. Temperature 1:142–149.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Reviewer #1:

The authors have embarked on the valuable task of producing a computational framework that combines theories of reinforcement learning with those of homeostasis and drive reduction. This is a worthwhile goal and the authors have several examples of behaviors that arise within their framework as well as predictions. I do think the manuscript reads a bit as though come of the ideas of combining reinforcement learning and homeostasis are novel to the authors, whereas in reality their contribution is to add a mathematical/computational framework which allows for quantitative predictions to be made and suggests what could/should be observed in any neural mechanism.

While overall the writing is very clear, I think the manuscript would be served by the authors being more careful to tone down statements that suggest the idea of combining homeostasis and reinforcement learning is their own. After all, everyone knows that when one is out on a cold winter's day a hot drink is rewarding, whereas in the middle of a hot summer's day a cold drink has greater rewarding value. The authors deserve credit for developing a mathematical scheme (the first I think?) where such results fall out, and I think they now have enough quantitative results and predictions that make the scheme testable.

In response to the reviewer’s suggestion, we added to the paragraph where we first talk about the contributions of the paper (in Introduction):

Given this evident coupling of homeostatic and learning processes, here, we propose a formal hypothesis for what computations, at an algorithmic level, may be performed in this biological integration of the two systems. More precisely, inspired by previous descriptive hypotheses on the interaction between motivation and learning (Hull, 1943; Mowrer, 1960; Spence, 1956), we suggest a principled model for how the rewarding value of outcomes is computed as a function of the animal’s internal state, and of the approximated need-reduction ability of the outcome…

Also, we added the below sentence to the conclusion section:

Being inspired by the classic drive-reduction theory of motivation, our mathematical treatment allows for quantitative results to be obtained, predictions that make the theory testable, and logical coherence.

In a similar vein, some statements to motivate the work are exaggerated, for example in the first line of Discussion the authors’ state:

“Theories of conditioning are founded on the argument that animals seek reward, while reward is defined as what animals seek.”

I think that while these definitions can be found, to state simply “reward is defined” without adding “by some” or “can be defined” or “has been defined by some” is too bold and general. One can find plenty of definitions of reward, in which “primary reward” is “that which aids survival” or “helps propagate the species” or simply in general English, reward is something that is good for you!

In response to the reviewer’s concern, we added the phrase “at least in the behaviorist approach” to the mentioned sentence:

Theories of conditioning are founded on the argument that animals seek reward, while reward is defined, at least in the behaviorist approach, as what animals seek.

In a couple of places (including the Abstract) the authors state that they:

“prove analytically that reward-seeking and physiological stability are two sides of the same coin” and “Our theory mathematically proves that seeking rewards is equivalent to the fundamental objective of physiological stability” whereas in fact through their definition of drive;“we define the “drive” as the distance of the internal state from the setpoint” the authors assume this to be the case and develop a mathematical theory where this result is true. One must be careful in mathematical proofs as to what are the premises. Since the rewards associated with sexual desire are outside the model (as the authors comment) it is clear that it is only within their theory that the mathematical “proof” holds.

In response to the reviewer’s concern, we added the phrase “Within this framework,” in the Abstract:

Within this framework, we mathematically prove that seeking rewards is equivalent to the fundamental objective of physiological stability, defining the notion of physiological rationality of behavior.

Furthermore we added the phrase “On the basis of the proposed computational integration of the two systems” into the sentence below, in the Introduction section:

On the basis of the proposed computational integration of the two systems, we prove analytically that reward-seeking and physiological stability are two sides of the same coin, and also provide a normative explanation for temporal discounting of reward.

Reviewer #2:

1) The authors make a comment early on that equates reward/reinforcer/utility. Given the obvious sophistication of the authors, this is unfortunate. In particular, to make clear the relationship between prior treatments of utility and the authors’ proposal would be helpful. Notably, the authors do describe other approaches to this, but even a sentence or two early on that clarifies rather than lumps together the difference between reinforcer/utility. Specifically because the authors are essentially arguing that homeostatic utility determines reinforcement properties.

We thank the author for pointing out this issue. By “utility”, we mean “economic utility” (as it is defined in Economics) rather than “homeostatic utility”. In economics, the utility of a commodity is a fixed value, without taking the internal state of individuals into account. This is the same problem as with reinforcer/reward value in psychology. In order to resolve this misunderstanding, we now use the term “economic utility” rather than “utility”, in the manuscript.

2) The authors make a comment about 'erroneous estimation of error' and later in the manuscript talk at length about, essentially, taste serving as cues. Three lines of investigation that the authors might find useful in this discussion: (1) Beeler et al Eur J Neuroscience 2012 'taste uncoupled from nutrition fails to sustain the rewarding properties of . . . ' (2) the work of Swithers with artificial sweeteners:

Swithers, S.E. & Davidson, T.L. (2008) A role for sweet taste: calorie predictive relations in energy regulation by rats. Behav. Neurosci., 122, 161- 173.

Swithers, S.E., Baker, C.R. & Davidson, T.L. (2009) General and persistent effects of high-intensity sweeteners on body weight gain and caloric compensation in rats. Behav. Neurosci., 123, 772-780.

Swithers, S.E., Martin, A.A. & Davidson, T.L. (2010) High-intensity sweeteners and energy balance. Physiol. Behav., 100, 55-62.

Finally, the authors cite one paper by de Araujo, but he has significantly developed the notion that the DA cells specifically serve as a metabolic sensor.

We found these references very helpful in supporting some aspects of our theory. In this respect, we added the below paragraph to the end of the subsection “Neural substrates”:

Such orosensory-based approximation of nutritional content, could have been obtained through evolutionary processes (Breslin, 2013), as well as through prior learning (Beeler et al., 2012; Swithers et al., 2009, 2010). In the latter case, approximations based on orosensory or contextual cues can be updated so as to match the true nutritional value, resulting in a rational neural/behavioral response to food stimuli (De Araujo et al., 2008).

The last sentence suggests a probable mechanism for the taste-independent adaptation of dopamine response to the true caloric value of food.

Other than that, I think there are many things that one could nitpick about, especially with regards to the endless details and nuances of the model (eg., I am not sure the authors have fully addressed the question the other reviewer had regarding the 'shortest distance between two points' idea). However, I think the paper is interesting, brings up some very good points, is well done and, as the authors point out, targets the mutual weakness of HR and RL models and brings them together nicely.

Reviewer 3:

1) Scientifically, I think you need to highlight and unpack the major result in the appendix. At an appropriate point in the main text, I would include a paragraph of the following sort:

“In summary, we have established a formal link between the homeostatic imperatives to keep physiological states near some set point and the maximisation of temporally discounted reward (or minimisation of some loss function). This is an important and non-trivial result. The appendix provides a formal proof; however, the underlying idea is fairly simple. Imagine you had to plan a hill walk, during which you wanted to maximise the height (altitude or reward) averaged over the path you take. If someone dropped you at the bottom of the hill, the optimum path would be to ascend the hill and spend as long as possible at the top before returning to your pick up point. Notice that this entails ascending the hill (reward function) before descending. Implicit in this strategy is a maximisation of temporally discounted reward. In other words, going up the hill first and then coming down is better than going down and then coming back up. It is this fundamental (variational) phenomenon that connects homeostasis with classical temporal discounting.

Furthermore, as indicated above, if the homeostatic cost (negative reward) is cast as a log probability then it can be treated as (free) energy.

Thanks to the reviewer’s suggestion, we now explain the importance of temporal discounting more clearly by adding the paragraph below (modified version of the paragraph suggested by the reviewer) in the middle of the section “Normative role of temporal discounting”:

Imagine you had to plan a 1-hr hill walk from a drop-point toward a pickup point, during which you wanted to minimize the height (equivalent to drive) summed over the path you take. In this summation, if you give higher weights to your height in the near future as compared to later times, the optimum path would be to descend the hill and spend as long as possible at the bottom (i.e. homeostatic setpoint) before returning to the pickup point. Equation 5 shows that this optimization is equivalent to optimizing the total discounted rewards along the path, given that descending and ascending steps are defined as being rewarding and punishing, respectively (equation 2).

In contrast, if at all points in time you give equal weights to your height, then the summed height over path only depends on the drop and pickup points, since every ascend can be compensated with a descend at any time.

We chose not to include the second part of the suggested paragraph: with all due gratitude for the reviewers support of our work and appreciation for the efforts of the reviewer to help us improve the clarity of the paper, we felt that launching into a short discussion of the free-energy principle early in our manuscript, before we sowed out the major results of the paper, would be distracting to the reader. We give ample discussion of the relationship between our theory and the free-energy principle in the Discussion where we point out exactly what the reviewer urges us to highlight.

Crucially, the time average or path integral of energy is called action. This means that both the homeostasis and temporally discounted reward are ways of prescribing a principle of least action. From this perspective, one can regard the adaptive behaviours that we are trying to link as necessary and emergent properties of all dynamical systems that comply with (Hamilton's) principle of least action. We will return to this perspective in the Discussion.”

We thank the reviewer for the suggested texts to be added to the manuscript. We used some of the notions mentioned by the reviewer (particularly the principle of least action), and discussed them in the manuscript. For example we added the below text after equation 14:

The equivalency of reward maximization and physiological stability objectives in our model (equation 5) shows that optimizing either homeostasis or sum of discounted rewards corresponds to prescribing a principle of least action applied to the surprise function.

2) The second major point is about the format of your paper. It is still unclear where the reader can find the details of your simulations. I also note that you have included supplementary figures. Can I suggest that you remove all supplementary material and place it in the main text (or discard it and refer to it as results not shown). I think you should prepare the reader for the slightly unusual scientific presentation with a paragraph at the beginning of the paper along the following lines:

“We will develop our theoretical results by appealing to simulations. These simulations are described in figures (and accompanying tables) and are called upon when necessary. All the simulations in this paper followed the same procedure: first we define a model that captures the problem of interest in terms of a Markov decision process. The ensuing behaviour is then optimised using classical reinforcement learning procedures (Q-learning) to define a value function. Actions are then selected using a softmax function of the value of allowable actions or choices. For each simulation we present the graphical model or Markov decision process in the figures, along with the ensuing behaviour. Each figure is accompanied by a table specifying the parameters of the Markovian process, the Q-learning and softmax functions used to simulate behaviour.”

Note that I am suggesting, for every simulation you present, a figure and table. Whenever you refer to results that are not presented in this format I would say so explicitly so the reader does not have to wonder whether they have missed something.

In order to give a better outline of the structure of the paper, we changed the last paragraph of the Introduction section to this:

The paper is structured as follows: After giving a heuristic sketch of the theory, we show several analytical, behavioral, and neurobiological results. On the basis of the proposed computational integration of the two systems, we prove analytically that reward-seeking and physiological stability are two sides of the same coin, and also provide a normative explanation for temporal discounting of reward. Behaviorally, the theory gives a plausible unified account for anticipatory responding and the rise-fall pattern of the response rate. We show that the interaction between the two systems is critical in these behavioral phenomena and thus, neither classical RL nor classical HR theories can account for them. Neurobiologically, we show that our model can shed light on recent findings on the interaction between the hypothalamus and the reward-learning circuitry, namely, the modulation of dopaminergic activity by hypothalamic signals.

Furthermore, we show how orosensory information can be integrated with internal signals in a principled way, resulting in accounting for experimental results on consummatory behaviors, as well as the pathological condition of over-eating induced by hyperpalatability.

Finally, we discuss limitations of the theory, compare it with other theoretical accounts of motivation and internal state regulation, and outline testable predictions and future directions.

Furthermore, we moved “Figure 4–figure supplements 2, 3 and 4” in the previous manuscript into the main text in the current version of the manuscript (merged together in Figure 4).

Also, in order to provide more details of the simulations and to have the same format for all presented results (i.e., problem definition, simulation results, simulated environment (MDP), free parameters of the model), we added four tables (Figure 5–figure supplement 1; Figure 6–figure supplement 2; Figure 10–figure supplement 1; Figure 12–figure supplement 1) and one Markov Decision Process (Figure 12–figure supplement 2) in the figure supplements.
