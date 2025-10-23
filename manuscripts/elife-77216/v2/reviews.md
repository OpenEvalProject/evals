# Peer review - Round 1

Editors:
- Juan Álvaro Gallego, https://ror.org/041kmwe10 Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77216.sa0](https://doi.org/10.7554/eLife.77216.sa0)

This solid modelling study presents a valuable contribution toward understanding the neural control of movement. The authors show that a minimal model comprising key sensorimotor cortical areas as well as a spinal circuits controlling a limb readily replicates landmark observations from behavioural and electrophysiological studies. This work will be of broad interest to motor control researchers, as well as to neurophysiologists interested in testing the predictions derived from this model.


---

# Peer review - Round 1

Editors:
- Juan Álvaro Gallego, https://ror.org/041kmwe10 Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77216.sa1](https://doi.org/10.7554/eLife.77216.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Adaptive plasticity in the spinal cord can produce reaching from scratch and reproduces motor cortex directional tuning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tamar Makin as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Marco Capogrosso (Reviewer #2); Rune W Berg (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The general consensus was that this is an interesting model, which will be a valuable contribution to the literature provided that additional controls and clarifications are provided.

Below you will find the individual reviewers comments. In addition to these, the editor prepared for the authors a summary of the essential revisions required. This is based on both the individual comments and the extensive following discussion between the reviewers and editor.

Essential revisions:

1. The paper focuses on an intriguing new hypothesis: that the spinal cord minimizes an error signal generated in motor cortex. Given the novelty of this hypothesis and its implications for the present manuscript, it is critical that the authors provide additional controls/analyses that specifically address it. These include:

a) What happens if error minimisation happened in the motor cortex rather than in the spinal cord; would the model still produce reaching movements? Do the cortical neurons look like actual neurons (distribution of directional tuning, rotational dynamics)? Do "synergies" still emerge in the spinal cord?

b) Does a model with the same hierarchical structure that doesn't perform error minimisation and is still capable of reaching exhibit the properties that the current model does (in terms of motor cortical activity, synergies, etc)?

2. The authors posit that motor cortex reports and error that is being minimised during learning. Under this assumption, the motor cortical signals should be reduced to zero, which is what indeed seems to happen, e.g., in Figure 2E. Nevertheless, it is known that the activity of motor cortical neurons is not zero during the execution of a correct movement, even in highly trained individuals: e.g., trained monkeys have rotation dynamics when reaching (Churchland Cunningham et al. Nature 2012) or hand cycling (Russo et al. Neuron 2018). How can these observations be reconciled with the current model?

3. The cerebellum is mentioned a couple of times but not included in the model. Based on the known fact that the cerebellum receives and integrates both massive corticopontine input and spinocerebellar proprioceptive input, its role is hence often assumed to be exactly what the motor cortex does in this model. The rationale behind not letting Cerebellum assume this role, but instead making the motor cortex assume this role, is not clear.

4. The authors claim that previously known phenomena (convergent force fields and rotational dynamics) "emerge" with their learning model. However, this is not supported by the results. Firstly, when they tested the convergent force field, the spinal cord was separated from the descending and ascending connections with cortex. This means that this observed property is independent of having learned the cortico-spinal connections. In addition, rotational dynamics were almost exclusively observed in the one-to-one cortical coupling, which the authors call a "less-plausible model. Therefore, these phenomena are not an emergent property that results from their learning model. It is necessary to specify what are the essential factors for each observed phenomenon.

5. This model has attributed all of the learning effects to the synaptic connection between the cortex and spinal cord (descending and ascending connections). However, it has been repeatedly demonstrated that plastic changes within the cortex occur during motor learning (Roth et al. Neuron 2020). How is the physiological relevance of attributing all the learning to descending and ascending pathways justified?

6. In relation to the previous comment: an equivalent circuit could be achieved by changing the intracortical synaptic connections. Why is the corticospinal connection the sole target of learning, and how do the results change (or remain unchanged) if learning happens in other parts of the circuit?

7. No model can reproduce the whole CNS. However, the reviewers think that a few key features should be added to the model:

a) The authors have not included any form of feedback in the spinal cord. Indeed, short-latency stretch reflexes are critical for movement: coupled with motoneurons, they are the basic units to generate movement (Xu, Tianqui et al. PNAS 2018); models of human walking show that gait can emerge only considering sensory inputs to the cord (Song and Geyer J Physiol 2015); and their absence prevents recovery from spinal cord injury (Takeoka, Aya et al. Cell 2014). Ia afferents have perhaps the strongest monosynaptic glutamatergic synaptic input to spinal motoneurons and constitute a primary driver of spinal motoneuron excitability which this model is currently missing. Does adding short-latency feedback change the conclusion of the paper?

b) As the authors discussed in the manuscript, the model omits many components that are known to be involved in learning and, as a result, the model reproduces the impaired motor control rather than the intact state. However, this prevents us from verifying whether the model properly reproduced the biological motor control. Specifically, they claim that the model reproduced ataxic reaching which resemble to the cerebellum patients. However, it is not surprising that a poorly tuned feedback controller (i.e. PID controller) shows an oscillation. Therefore, it is necessary for the authors to show that their model significantly resembles the biological motor control by comparing to the model which share the hierarchical structures but the error is corrected within the cortex and only motor commands descend to the spinal cord.

c) 20 % of corticospinal projections to motoneurons innervating the arm and particularly the hand are thought to be monosynaptic. Does their addition change the present results?

d) The proportions and the connectivity of the network make the model seem less biologically plausible, which should at least be addressed in the text. First, the number of neurons in the populations at various levels seems rather small compared to the immense size of these structures. Why not have more neurons in the networks? This applies to all parts of the model, also to the spinal network. In many species, the ratio of motor neurons to interneurons is about 1:10, yet in this model, it is more like 1:2 (the trio). Also, the connectivity has a bias towards the feedforward network, yet local recurrent connectivity seems to be widely present in the nervous system. The proportions in the connectivity from M to C could also be problematic. All the spinal units (c = [c1, …. ,cN]) receive commands/error signal from M (e = [e1, …. ,eM]). Is M>N? Presuming M is > N this would represent a converging input from M to C, and that is problematic since the corticospinal projections are rather sparse. More likely there is diverging connectivity from M to C. It is unclear to me if this is an important problem, it may not be, but it would be appropriate to address such proportions in the text.

e) The model does not include any form of "pattern generator", a limitation the authors are aware of, and denote as the "supraspinal pattern formation" problem. They seem to export this to another area of the brain while the motor cortex-spinal cord loop takes care of an appropriate execution. This needs to be clarified and/or addressed with the model.

f) It is well-known that the spinal cord autonomously can produce motor behaviors. It is unclear whether C in the model is capable of this.

g) Regarding the synergistic model, their model has spinal interneurons recruiting two motoneuron pools, which is very different from the muscle synergies observed in animals (d'Avella et al., J Neurosci 2006). It is necessary to justify why this type of synergies should be used here.

Reviewer #1 (Recommendations for the authors):

The authors aimed to study corticospinal control of reach movements. More specifically they aim to understand how an unsupervised system could learn to reach and whether that system would then show properties observed in experiments. For this, the authors conceived a neural network model with defined hierarchy and architecture coupled to a simple biomechanical arm model in a closed-loop that is capable of learning a reach-out task. Interestingly, the model shows several properties found in experimental data such as directional tuning of motor cortical units as well as discrete force fields in the spinal cord.

Strengths

The paper has many strengths. It is rigorous and well written, and while not well articulated in the introduction I completely agree with the authors that computational models are necessary if we want to aim at any variation of the concept of "understanding" in relation to the central nervous system. Therefore their goal is absolutely significant and relevant.

I also particularly liked the approach to start from specific hypotheses on the structure and function of the different modeled layers while leaving completely free the organization and strength of synapses in the system. This approach is elegant because starting from clear hypotheses it allows to observe what properties emerge "spontaneously" and compare these properties with experimental data.

The results obtained are reasonable in terms of kinematics and it's interesting to observe the emergence of these properties from an error minimization rule imposed within the spinal cord.

Weaknesses

The conclusions that the authors make in the paper are very strong. Given the emergence of certain interesting properties within the nervous system, it is implicit the implication that this model can have some sort of general meaning, and most importantly, that it validates from the theoretical point of view the homeostatic control idea. More specifically, the paper starts with a very strong hypothesis, which is that the spinal cord is minimizing an error signal generated in motor cortex. For an experimental neuroscientist (as myself) this is intriguing but also strikes as a very strong interpretation of the role of what we call motor cortex that for decades has been imagined as an actuator of movements. Because of the importance of the implication I don't think that the properties shown in the paper are sufficient to make such a claim, even if implicit. Therefore I think that some form of control is required. I understand completely that models are hard to build, but I can't escape wondering what would happen if the motor cortex would not be producing an error signal. What if that error minimization happened instead in the motor cortex and not in the spinal cord? Would your model still produce reach movements? Would those cortical neurons show directionality? Would "synergies" still emerge in the cord? I think this is an important point if we're claiming that those properties emerge as a consequence of the fact that the motor cortex is calculating an error and the spinal cord is minimizing that error. Therefore, to validate the main hypothesis of the paper, which is that the motor cortex is calculating an error and the spinal cord is minimizing that error, then I would like to see that a model that does not do that, but it's still capable of reaching while maintaining the same hierarchical architecture would not show the properties that the authors found in their model.

The second weakness is somehow related to the first. There are certain assumptions on the structure that are not true experimentally and it would be important to incorporate these because they may change the observed properties and could thus be used as further validation.

The first missing property is direct cortico-spinal control of spinal motoneurons. The authors say in the introduction that the motor cortex does not activate spinal motoneurons directly and only connects to interneurons. Instead, the major difference between primates (including humans) and all the other animals is precisely the existence of direct monosynaptic connections between the motor cortex and muscles of the upper limb (particularly the hand). These monosynaptic components are thought to represent about 20% of the cortico-spinal tract. It would be important to see whether their presence changes the results that they obtained.

The second more important functional inaccuracy concerns the spinal cord. The authors send their sensory signals to the "thalamus" which then relays them to the "sensory cortex" and "motor cortex". In the supplementary material they described the fact that they decided not to include what they call "short reflex" that would connect "the thalamus" to the spinal cord, or provide a feedback in some way. Therefore in their model, the spinal cord is not receiving a feedback at all. Unfortunately, this is in stark contrast with the actual structure of the spinal cord. Proprioceptive afferents are pivotal members of the spinal motor infrastructure. They are so important than in simple animals, coupled with motoneurons, they constitute the units that generate movement (Xu, Tianqi, et al. "Descending pathway facilitates undulatory wave propagation in Caenorhabditis elegans through gap junctions." Proceedings of the National Academy of Sciences 115.19 (2018): E4493-E4502.); models of human locomotion show that it is possible to build walking models without pattern generators that only consider sensory inputs int he spinal cord (Song, S., and Geyer, H. (2015). A neural circuitry that emphasizes spinal feedback generates diverse behaviours of human locomotion. J. Physiol. 593, 3493-3511.) and they seem to be critical to direct motor learning and recovery after spinal cord injury (Takeoka, Aya, et al. "Muscle spindle feedback directs locomotor recovery and circuit reorganization after spinal cord injury." Cell 159.7 (2014): 1626-1639.) Most importantly Ia afferents have perhaps the strongest monosynaptic glutamatergic synaptic input to the spinal motoneurons and constitute a primary driver of spinal motoneuron excitability which this model is currently missing. Additionally, some of the agonist-antagonist relationship that the authors find could be significantly changed by the presence of these afferents because Ia afferents connect not only to homologous motoneurons but up to 60% of motoneurons of synergistic muscles and they inhibit antagonists via Ia inhibitory interneurons (See Moraud E. (2016) Mechanisms Underlying the Neuromodulation of Spinal Circuits for Correcting Gait and Balance Deficits after Spinal Cord Injury, Neuron).

In consequence, the presence of this "short-feedback" seems paramount to me to have an accurate representation of the spinal cord, and it's important to verify that this structure would not change the main conclusions of the paper.

Indeed, as the authors have correctly implied, the main difference between the nervous system and an artificial neural network is the underlying defined architecture and hierarchy that must be represented at least for the most important elements. And spinal sensory feedback is a building block of movement and learning. Indeed, completely paralyzed rats are capable of learning different walking patterns when totally disconnected from the brain if excitation is provided by means of electrical stimulation and likely sensory afferents are the driver of this learning (Courtine, Grégoire, et al., "Transformation of nonfunctional spinal circuits into functional states after the loss of brain input." Nature neuroscience 12.10 (2009): 1333-1342.).

Reviewer #2 (Recommendations for the authors):

In this study, the authors investigate how the motor cortex and spinal cord interact in a long-loop reflex organization, from a computational modeling perspective. The motor cortex represents kinematic aspects, i.e. the actual movement of the hand and arm, as opposed to dynamics, which would involve the forces exerted by the muscles or higher-level parameters of the movement. Nevertheless, to achieve the end goal of a certain movement of the hand, a transformation from actuator (muscle) coordinates has to take place, and this is a challenging process. The authors propose that the motor cortex report an error between the desired and the actual movement, use computational modeling to explain how a flexible error reduction mechanism can be achieved and explained by computational modeling of the interplay between cortex and the spinal cord.

Strengths: A theoretical analysis of the interplay between the spinal cord and motor cortex has rarely been studied previously especially using the long-loop reflex, dynamics, pattern formation, and plasticity. This theoretical contribution is important, especially in the light of the vast new experimental data that is being generated by e.g. calcium imaging and electrophysiology and the new observations of rotational cortical dynamics. It is also rare that the role of the spinal cord is being incorporated into the executing of movement in parallel with the motor cortex.

Weaknesses: Some of the assumptions hinges on a flexible error reduction mechanism, which is described in a previous (unpublished) study, which seems somewhat fragile. The model does not really get to the root of the problem of how the nervous system generates the desired movement, which the authors are aware of and call the "supra spinal pattern formation" problem. They seem to export this problem to another area of the brain and describe how the motor cortex-spinal cord loop takes care of an appropriate execution.

The study evaluates multiple aspects of the model in comparison with experimental observation such as direction tuning curve, rotational dynamics, and learning.

Overall, this is an interesting and well-executed study.

Specific comments:

There are a couple of issues regarding the model that is not so clear (or perhaps well-hidden somewhere in the supplement). It is stated that the role of the motor cortex is to report the "error signal" of the movement, i.e. the signal coming from SPA, which is the difference between the desired movement (SP) and the actual movement (SA). First, if the motor cortex is reporting the error, and this error is being minimized while learning, then the signal in the motor cortex should ideally be reduced to zero, which is also what seems to happen in e.g. Figure 2E. Nevertheless, it is known that activity in the motor cortex is not zero during the execution of correct movement, especially in highly trained individuals, e.g. trained monkeys have rotational dynamics when hand-cycling (Churchland 2012). This also seems to be the case in the current study with directional tuning (Figure 5) and rotation, which appear contradictory to me. This is a bit unclear how this is possible. Second, the cerebellum is mentioned a couple of times but not included in the model. It is known that the cerebellum receives and integrates both massive corticopontine input and spinocerebellar proprioceptive input and the role of the cerebellum is hence often assumed to do exactly what the motor cortex does in this model. The rationale behind not letting Cerebellum assume this role, but instead making the motor cortex assume this role, is not clear to me.

The current model does not explain what the authors call the "supra spinal pattern formation" problem, i.e. how the motor commands arise in the neuronal networks in the cortex and elsewhere. The problem of motor commands is conveniently exported to the external parameter "SP" module that is generating the intended movement. This is for a good reason since it is indeed a hard problem to explain how motor programs arise. I do not see a solution to this issue, only that it is a limitation to be aware of, which the authors seem to be. Nevertheless, the model proposed by the authors makes an effort to explain some of the dynamics of the different regions involved in properly learning and executing the motor commands.

I have some concerns regarding the network, the proportions, and the connectivity that make the model seem less biologically plausible, which should at least be addressed in the text. First, the number of neurons in the populations at various levels seems rather small compared to the immense size of these structures. Why not have more neurons in the networks? This applies to all parts of the model, also to the spinal network. In many species, the ratio of motor neurons to interneurons is about 1:10, yet in this model, it is more like 1:2 (the trio). Also, the connectivity has a bias towards the feedforward network, yet local recurrent connectivity seems to be widely present in the nervous system. The proportions in the connectivity from M to C could also be problematic. All the spinal units (c = [c1, …. ,cN]) receive commands/error signal from M (e = [e1, …. ,eM]). Is M>N? Presuming M is > N this would represent a converging input from M to C, and that is problematic since the corticospinal projections are rather sparse. More likely there is diverging connectivity from M to C. It is unclear to me if this is an important problem, it may not be, but it would be appropriate to address such proportions in the text.Reviewer #3 (Recommendations for the authors):

This study proposes a new computational model for learning upper limb reaching control. In particular, this study develops a model that satisfies biological plausibility, which has not always been satisfied by previous models: (1) a network of the whole sensorimotor loop, (2) a model using neural elements, (3) learning using local information, and (4) continuous online learning. Specifically, their model showed that learning in the synaptic weights of descending and ascending projections between the cortex and spinal cord can reproduce ataxic reaching often observed in cerebellar patients. Furthermore, various phenomena that have been demonstrated in the motor control field emerge with this model. Based on these results, the authors argue that this is a biologically plausible learning model for animals' reaching control.

Strength:

1) This study examines a number of previous motor learning models and defines the constraints to develop a biologically plausible model. Given that there are too many parameters to be considered to build the motor control model, I truly appreciate the authors defining the constraints for a biological motor learning model and clarifying the research goal.

Weakness:

1) As the authors discussed in the manuscript, the model omits many components that are known to be involved in learning and, as a result, the model reproduces the impaired motor control rather than the intact state. However, this prevents us from verifying whether the model properly reproduced the biological motor control. Specifically, they claim that the model reproduced ataxic reaching which resemble to the cerebellum patients. However, it is not surprising that a poorly tuned feedback controller (i.e. PID controller) shows an oscillation. Therefore, it is necessary for the authors to show that their model significantly resembles the biological motor control by comparing to the model which shares the hierarchical structures but the error is corrected within the cortex and only motor commands descend to the spinal cord.

2) This model has attributed all of the learning effects to the synaptic connection between the cortex and spinal cord (descending and ascending connections). However, it has been repeatedly demonstrated that plastic changes within the cortex occur during motor learning [1 and others]. Therefore, the physiological relevance of attributing everything to descending and ascending pathways is questionable.

[1] Roth, R. H. et al. Cortical Synaptic AMPA Receptor Plasticity during Motor Learning. Neuron 105, 895-908.e5 (2020).

3) Relating to the previous comment, this model only changed the connection with the spinal cord, but the equivalent circuit can be achieved by changing the intracortical synaptic connection. It is necessary to justify why the connection with the spinal cord should be the sole target of learning.

4) The authors claim that previously known phenomena (convergent force field and rotational dynamics) "emerge" with this learning model. However, this is not supported by the results. Firstly, when they tested the convergent force field, the spinal cord is separated from the descending and ascending connections with cortex. This means that this observed property is independent of the learning of the cortico-spinal connections. In addition, rotational dynamics is almost exclusively observed in the one-to-one cortical coupling, which the authors call a "less-plausible model. Therefore, these phenomena are not emergent properties as a result of their learning model. It is necessary to specify what are the essential factors for each observed phenomenon.

5) Regarding the synergistic model, their model has spinal interneurons recruiting two motoneuron pools, which is very different from the muscle synergies observed in animals

[2]. It is necessary to justify why this type of synergies should be used here.

[2] d'Avella A, Portone A, Fernandez L, Lacquaniti F (2006) Control of fast-reaching movements by muscle synergy combinations. The Journal of neuroscience: the official journal of the Society for Neuroscience 26:7791-7810

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Self-configuring feedback loops for sensorimotor control" for further consideration by eLife. Your revised article has been evaluated by Tamar Makin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Although the reviewers were satisfied by the new analyses, they were also unanimous in thinking that the manuscript is hard to follow and that this complexity could make it less broadly appealing. Our recommendation is thus for the authors to try to simplify the text, minimising the mental burden to the reader. The main concerns were:

1) The five different "configurations" are not well explained/motivated throughout the paper.

2) Figure captions are too short, which makes it hard to understand the results (e.g., what is Figure 8 about?).

3) There are too many abbreviations, which again does not help comprehend the text.

4) The Discussion is hard to follow, foremost because it requires that the readers remember all five configurations, which were presented in the much earlier -and very long- Results section.

5) The overall logic could be potentially streamlined so the study becomes easier to understand.

In addition, you may want to consider addressing the comment by Reviewer #4, although it is not mandatory.

Reviewer #4 (Recommendations for the authors):

I really appreciate the authors revising the manuscript. The argument is now much clearer. I found that the authors are very open about what neural implementation this motor learning is occurring in, and it seems too early to suggest the neural implementation since the same learning can occur either in the spinal cord or in the cerebral cortex, or perhaps in other structures such as the cerebellum which is omitted by this model.

As a neurophysiologist, I am curious about what insights this computational model will provide into our understanding of the neural mechanism of motor learning. I understand that the key assumptions of this model are that (1) errors vary monotonically with motor command and (2) differential Hebbian learning at the output connections reduces the errors. The second assumption has already been discussed for possible implementation in the spinal cord. However, the validity of the first assumption is not yet clear. I would like to suggest the authors elaborate on what neural mechanism could transform errors in the multiple sensory systems (e.g visual systems) into the monotonic error such as muscle length. It is also important to mention where the desired somatosensory activity (Sp) comes from.
