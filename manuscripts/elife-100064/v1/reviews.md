# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100064.3.sa0](https://doi.org/10.7554/eLife.100064.3.sa0)

This useful study examines the neural activity in the motor cortex as a monkey reaches to intercept moving targets, focusing on how tuned single neurons contribute to an interesting overall population geometry. The presented results and analyses are solid, though the investigation of this novel task could be strengthened by clarifying the assumptions behind the single neuron analyses, and further analyses of the neural population activity and its relation to different features of behaviour.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100064.3.sa1](https://doi.org/10.7554/eLife.100064.3.sa1)

Summary:

This study addresses the question of how task-relevant sensory information affects activity in motor cortex. The authors use various approaches to address this question, looking at single units and population activity. They find that there are three subtypes of modulation by sensory information at the single unit level. Population analyses reveal that sensory information affects the neural activity orthogonally to motor output. The authors then compare both single unit and population activity to computational models to investigate how encoding of sensory information at the single-unit level is coordinated in a network. They find that an RNN that displays similar orbital dynamics and sensory modulation to motor cortex also contains nodes that are modulated similarly to the three subtypes identified by the single unit analysis.

Strengths:

The strengths of this study lie in the population analyses and the approach of comparing single-unit encoding to population dynamics. In particular, the analysis in Figure 3 is very elegant and informative about the effect of sensory information on motor cortical activity. The task is also well designed to suit the questions being asked and well controlled.

It is commendable that the authors compare single-unit to population modulation. The addition of the RNN model and perturbations strengthen the conclusion that the subtypes of individual units all contribute to the population dynamics.

Weaknesses:

The main weaknesses of the study lie in the categorization of the single units into PD shift, gain and addition types. The single units exhibit clear mixed selectivity, as the authors highlight. Therefore, the subsequent analyses looking only at the individual classes in the RNN are a little limited. Another weakness of the paper is that the choice of windows for analyses is not properly justified and the dependence of the results on the time windows chosen for single unit analyses is not assessed. This is particularly pertinent because tuning curves are known to rotate during movements (Sergio et al. 2005 Journal of Neurophysiology).

This study uses insights from single-unit analysis to inform mechanistic models of these population dynamics, which is a powerful approach, but is dependent on the validity of the single-cell analysis, which I have expanded on below.

I have clarified some of the areas that would benefit from further analysis below:

Task:

The task is well designed, although it would have benefited from perhaps one more target speed (for each direction). One monkey appears to have experienced one more target speed than the others (seen in Figure 3C). It would have been nice to have this data for all monkeys, although, of course, unfeasible given that the study has been concluded.

Single unit analyses:

The choice of the three categories (PD shift, gain addition) is not completely justified in a satisfactory way. It would be nice to see whether these three main categories are confirmed by unsupervised methods.

The decoder analyses in Figure 2 provide evidence that target speed modulation may change over the trial. Therefore, it is important to see how the window considered for the firing rate in Figure 1 (currently 100ms pre - 100ms post movement onset) affects the results. Whilst it is of course understandable that a window must be chosen and will always be slightly arbitrary, using different windows and comparing the results of two or three different sizes or timed windows would be more convincing that the results are not dependent on this particular window.

RNN:

Mixed selectivity is not analysed in the RNN, which would help to compare the model to the real data where mixed selectivity is common. The CCA and Procrustes analysis are a good start to validate the claim of similarity between RNN and neural dynamics, rather than allowing comparisons to be dominated by geometric similarities that may be features of the task. However, some of the disparity values for the Procrustes analysis are quite high, albeit below that of the shuffle. Maybe a comment about this in the text should be included. There is also an absence of alternate models to compare the perturbation model results to.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100064.3.sa2](https://doi.org/10.7554/eLife.100064.3.sa2)

Summary:

In this manuscript, Zhang et al. examine neural activity in motor cortex as monkeys make reaches in a novel target interception task. Zhang et al. begin by examining the single neuron tuning properties across different moving target conditions, finding several classes of neurons: those that shift their preferred direction, those that change their modulation gain, and those that shift their baseline firing rates. The authors go on to find an interesting, tilted ring structure of the neural population activity, depending on the target speed, and find that (1) the reach direction has consistent positioning around the ring, and (2) the tilt of the ring is highly predictive of the target movement speed. The authors then model the neural activity with a single neuron representational model and a recurrent neural network model, concluding that this population structure requires a mixture of the three types of single neurons described at the beginning of the manuscript.

Strengths:

I find the task the authors present here to be novel and exciting. It slots nicely into an overall trend to break away from a simple reach-to-static-target tasks to better characterize the breadth of how motor cortex generates movements. I also appreciate the movement from single neuron characterization to population activity exploration, which generally serves to anchor the results and make them concrete. Further, the orbital ring structure of population activity is fascinating, and the modeling work at the end serves as a useful baseline control to see how it might arise.

Weaknesses:

While I find the behavioral task presented here to be excitingly novel, I find the presented analyses and results to be far less interesting than they could be. Key to this, I think, is that the authors are examining this task and related neural activity primarily with a single-neuron representational lens. This would be fine as an initial analysis, since the population activity is of course composed of individual neurons, but the field seems to have largely moved towards a more abstract "computation through dynamics" framework that has, in the last several years, provided much more understanding of motor control than the representational framework has. As the manuscript stands now, I'm not entirely sure what interpretation to take away from the representational conclusions the authors made (i.e. the fact that the orbital population geometry arises from a mixture of different tuning types). As such, by the end of the manuscript, I'm not sure I understand any better how motor cortex or its neural geometry might be contributing to the execution of this novel task.

Main Comments:

My main suggestions to the authors revolve around bringing in the computation through a dynamics framework to strengthen their population results. The authors cite the Vyas et al. review paper on the subject, so I believe they are aware of this framework. I have three suggestions for improving or adding to the population results:

(1) Examination of delay period activity: one of the most interesting aspects of the task was the fact that the monkey had a random-length delay period before he could move to intercept the target. Presumably, the monkey had to prepare to intercept at any time between 400 and 800 ms, which means that there may be some interesting preparatory activity dynamics during this period. For example, after 400ms, does the preparatory activity rotate with the target such that once the go cue happens, the correct interception can be executed? There is some analysis of the delay period population activity in the supplement, but it doesn't quite get at the question of how the interception movement is prepared. This is perhaps the most interesting question that can be asked with this experiment, and it's one that I think may be quite novel for the field--it is a shame that it isn't discussed.

(2) Supervised examination of population structure via potent and null spaces: simply examining the first three principal components revealed an orbital structure, with a seemingly conserved motor output space and a dimension orthogonal to it that relates to the visual input. However, the authors don't push this insight any further. One way to do that would be to find the "potent space" of motor cortical activity by regression to the arm movement and examine how the tilted rings look in that space. Presumably, then, the null space should contain information about the target movement. The ring tilt will likely be evident if the authors look at the highest variance neural dimension orthogonal to the potent space (the "null space")--this is akin to PC3 in the current figures, but it would be nice to see what comes out when you look in the data for it.

The authors attempt this sort of analysis in the supplement, alongside their dPCA results, but the results seem misinterpreted. The authors do identify one kind of output-potent space using the reach direction components of dPCA, and the reach directions are indeed aligned here. However, they then go on to interpret the target-velocity space as the output-null space, orthogonal to the potent space. There are two problems with this. (1) The target-velocity space is not necessarily orthogonal to the reach-direction space. This is a key aspect of dPCA--while the individual components within a particular marginalization space are orthogonal, the marginalization spaces themselves are not necessarily orthogonal unless they are forced to be (which the authors don't mention doing). (2) Even if the target-velocity space were orthogonal to the reach-direction space, it would not comprise the whole output-null space--such a null space would also include dimensions of neural population activity that have target-velocity/reach-direction interaction, which the authors show is a major component of neural population variance. Incidentally, the dPCA analysis the authors present shows what I would expect from their unsupervised results, but as it is written, the dPCA results are interpreted in a strange or potentially misleading way.

(3) RNN perturbations: as it's currently written, the RNN modeling has promise, but the perturbations performed don't provide me with much insight. I think this is because the authors are trying to use the RNN to interpret the single neuron tuning, but it's unclear to me what was learned from perturbing the connectivity between what seems to me almost arbitrary groups of neurons. It seems to me that a better perturbation might be to move the neural state before the movement onset to see how it changes the output. For example, the authors could move the neural state from one tilted ring to another to see if the virtual hand then reaches a completely different (yet predictable) target. Moreover, if the authors can more clearly characterize the preparatory movement, perhaps perturbations in the delay period would provide even more insight into how the interception might be prepared.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100064.3.sa3](https://doi.org/10.7554/eLife.100064.3.sa3)

Summary:

This experimental study investigates the influence of sensory information on neural population activity in M1 during a delayed reaching task. In the experiment, monkeys are trained to perform a delayed interception reach task, in which the goal is to intercept a potentially moving target.

This paradigm allows the authors to investigate how, given a fixed reach end point (which is assumed to correspond to a fixed motor output), the sensory information regarding the target motion is encoded in neural activity.

At the level of single neurons, the authors find that target motion modulates the activity is three main ways: gain modulation (scaling of the neural activity depending on the target direction), shift (shift of the preferred direction of neurons tuned to reach direction), or addition (offset to the neural activity).

At the level of the neural population, target motion information was largely encoded along the 3rd PC of the neural activity, leading to a tilt of the manifold along which reach direction was encoded that was proportional to target speed. The tilt of the neural manifold was found to be largely driven by the variation of activity of the population of gain modulated neurons.

Finally, the authors study the behaviour of an RNN trained to generate the correct hand velocity given the sensory input and reach direction. The RNN units are found to similarly exhibit mixed selectivity to the sensory information, and the geometry of the « neural population » resembles that observed in the monkeys.

Overall, the experiment is well set up to address the question of how sensory information that is directly relevant to the behaviour but does not lead to a direct change in behavioural output modulates motor cortical activity.

The finding that sensory information modulates the neural activity in M1 during motor preparation and execution is non trivial, given that this modulation of the activity must occur in the nullspace of the movement.

The authors provide analyses at both the single neuron and the population level, leading to a relatively complete characterization of the effect of the target motion on neural activity.

Additionally, they start exploring the link between the population geometry and the mixed selectivity of the single neurons in their RNN model. While they could be extended in future work, the analyses of the RNN provide a good starting point to address how exactly the task setup and constraints on the network shape the single neuron selectivity and the population geometry.
