# Peer review - Round 1

Editors:
- Jörn Diedrichsen, Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89131.4.sa0](https://doi.org/10.7554/eLife.89131.4.sa0)

This important study provides a new perspective on why preparatory activity occurs before the onset of movement. The authors report that when there is a cost on the inputs, the optimal inputs should start before the desired network output for a wide variety of recurrent networks. The authors present compelling evidence by combining mathematically tractable analyses in linear networks and numerical simulation in nonlinear networks.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89131.4.sa1](https://doi.org/10.7554/eLife.89131.4.sa1)

In this work, the authors investigate an important question - under what circumstances should a recurrent neural network optimised to produce motor control signals receive preparatory input before the initiation of a movement, even though it is possible to use inputs to drive activity just-in-time for movement?

This question is important because many studies across animal models have shown that preparatory activity is widespread in neural populations close to motor output (e.g. motor cortex / M1), but it isn't clear under what circumstances this preparation is advantageous for performance, especially since preparation could cause unwanted motor output during a delay.

They show that networks optimised under reasonable constraints (speed, accuracy, lack of pre-movement) will use the input to seed the state of the network before movement and that these inputs reduce the need for ongoing input during the movement. By examining many different parameters in simplified models they identify a strong connection between the structure of the network and the amount of preparation that is optimal for control - namely, that preparation has the most value when nullspaces are highly observable relative to the readout dimension and when the controllability of readout dimensions is low. They conclude by showing that their model predictions are consistent with the observation in monkey motor cortex that even when a sequence of two movements is known in advance, preparatory activity only arises shortly before movement initiation.

Overall, this study provides valuable theoretical insight into the role of preparation in neural populations that generate motor output, and by treating input to motor cortex as a signal that is optimised directly this work is able to sidestep many of the problematic questions relating to estimating the potential inputs to motor cortex.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89131.4.sa2](https://doi.org/10.7554/eLife.89131.4.sa2)

This work clarifies neural mechanisms that can lead to a phenomenology consistent with motor preparation in its broader sense. In this context, motor preparation refers to activity that occurs before the corresponding movement. Another property often associated with preparatory activity is a correlation with global movement characteristics such as reach speed (Churchland et al., Neuron 2006), reach angle (Sun et al., Nature 2022), or grasp type (Meirhaeghe et al., Cell Reports 2023). Such activity has notably been observed in premotor and primary motor cortices, and it has been hypothesized to serve as an input to a motor execution circuit. The timing and mechanisms by which such 'preparatory' inputs are made available to motor execution circuits remain however unclear in general, especially in light of the presence of a 'trigger-like' signal that appears to relate to the transition from preparatory dynamics to execution activity (Kaufman et al. eNeuron 2016, Iganaki et al., Cell 2022, Zimnik and Churchland, Nature Neuroscience 2021).

The preparatory inputs have been hypothesized to fulfill one or several (non-mutually-exclusive) possible objectives. Two notable hypotheses are that these inputs could be shaped to maximize output accuracy under regularization of the input magnitude; or that they may help the flexible re-use of the neural machinery involved in the control of movements in different contexts.

Here, the authors investigate in detail how the former hypothesis may be compatible with the presence of early inputs in recurrent network models driving arm movements, and compare models to data.

Strengths:

The authors are able to deploy an in-depth evaluation of inputs that are optimized for producing an accurate output at a pre-defined time while using a regularization term on the input magnitude, in the case of movements that are thought to be controlled in a quasi-open loop fashion such as reaches.

First, the authors have identified that optimal control theory is a great framework to study this question as it provides methods to find and analyze exact solutions to this cost function in the case of models with linear dynamics. The authors not only use this framework to get an exact assessment of how much pre-movement input arises in large recurrent networks, but also give insight into the mechanisms by which it happens by dissecting in detail low-dimensional networks. The authors find that two key network properties - observability of the readout's nullspace and limited controllability - give rise to optimal inputs that are large before the start of the movement (while the corresponding network activity lies in the nullspace of the readout). Further, the authors numerically investigate the timing of optimized inputs in models with nonlinear dynamics, and find that pre-movement inputs can also arise in these more general networks. The authors also explore how some variations on their model's constraints - such as penalizing the input roughness or changing task contingencies about the go cue timing - affect their results. Finally, the authors point out some coarse-grained similarities between the pre-movement activity driven by the optimized inputs in some of the models they studied, and the phenomenology of preparation observed in the brain during single reaches and reach sequences. Overall, the authors deploy an impressive arsenal of tools and a very in-depth analysis of their models.

Oustanding questions that could lead to interesting follow-up work:

Like all great pieces of research, this article makes it clear where current limitations lie and therefore opens up opportunities for future work.

(1) Though the optimal control theory framework is ideal for determining inputs that minimize output error while regularizing the input norm or other simple input features, it cannot easily account for some other varied types of objectives - especially those that may lead to a complex optimization landscape. For instance, the reusability of parts of the circuit, sparse use of additional neurons when learning many movements, and ease of planning (especially under uncertainty about when to start the movement), may be alternative or additional reasons that could help explain the preparatory activity observed in the brain. It is interesting to note that inputs that optimize the objective chosen by the authors arguably lead to a trade-off in terms of other desirable objectives. Specifically, the inputs the authors derive are time-dependent, so a recurrent network would be needed to produce them and it may not be easy to interpolate between them to drive new movement variants. In addition, these inputs depend on the desired time of output and therefore make it difficult to plan, e.g. in circumstances when timing should be decided depending on sensory signals. Finally, these inputs are specific to the full movement chain that will unfold, so they do not permit reuse of the inputs e.g. in movement sequences of different orders. Of note, the authors have pointed out in the discussion how their framework may be extended in future work to account for some additional objectives, such as inputs' temporal smoothness or some strategies for dealing with go cue timing uncertainty.

(2) Relatedly, if the motor circuits were to balance different types of objectives, the activity and inputs occurring before each movement may be broken down into different categories that may each specialize into their own objective. For instance, previous work (Kaufman et al. eNeuron 2016, Iganaki et al., Cell 2022, Zimnik and Churchland, Nature Neuroscience 2021) has suggested that inputs occurring before the movement could be broken down into preparatory inputs 'stricto sensu' - relating to the planned characteristics of the movement - and a trigger signal, relating to the transition from planning to execution - irrespective of whether the movement is internally timed or triggered by an external event. The current work does not address which type(s) of early input may be labeled as 'preparatory' or may be thought of as a part of 'planning' computations, or whether these inputs may come from several different source circuits. Future research could investigate these questions using a different approach, for instance, by including structural constraints from brain architecture into a neural network model.

(3) While the authors rightly point out some similarities between the inputs that they derive and observed preparatory activity in the brain, notably during motor sequences, there are also some differences. For instance, while both the derived inputs and the data show two peaks during sequences, the data reproduced from Zimnik and Churchland show preparatory inputs that have a very asymmetric shape that really plummets before the start of the next movement, whereas the derived inputs have larger amplitude during the movement period - especially for the second movement of the sequence. In addition, the data show trigger-like signals before each of the two reaches. Finally, while the data show a very high correlation between the pattern of preparatory activity of the second reach in the double reach and compound reach conditions, the derived inputs appear to be more different between the two conditions. Note that the data would be consistent with separate planning of the two reaches even in the compound reach condition, as well as the re-use of the preparatory input between the compound and double reach conditions. Therefore, different motor sequence datasets - notably, those that would show even more coarticulation between submovements - may be more promising for finding a tight match between the data and the author's inputs. In the future, further analyses in these datasets could help determine whether the coarticulation could be due to simple filtering by the circuits and muscles downstream of M1, planning of movements with adjusted curvature to mitigate the work performed by the muscles while permitting some amount of re-use across different sequences, or - as suggested by the authors - inputs fully tailored to one specific movement sequence that maximize accuracy and minimize the M1 input magnitude.

(4) Though iLQR is a powerful optimization method to find inputs optimizing the author's cost function, it also has some limitations. First, given that it relies on a linearization of the dynamics at each timestep, it has a limited ability to leverage potential advantages of nonlinearities in the dynamics. Second, the iLQR algorithm is not a biologically plausible learning rule and does not account for biological constraints affecting the circuits that produce and process these inputs. Therefore, it might be difficult for the brain to learn to produce the inputs that it finds. Consequently, when observing differences between model and data, this can confound the question of whether it comes from a difference of assumed objective or a difference of optimization procedure or circuit implementation. It remains unclear whether using alternative algorithms with different limitations - for instance, using variants of BPTT to train a separate RNN to produce the inputs in question - could impact some of the results.

(5) Under the objective considered by the authors, the amount of input occurring before the movement might be impacted by the presence of online sensory signals for closed-loop control. Even if the inputs include some sensory activity and/or the RNN activity could represent all general variables (e.g. sensory) whose states can be decoded from M1, the model does not currently include mechanisms that process imperfect (delayed, noisy) sensory feedback to adapt the output in a trial-specific manner. The information related to such sensory feedback cannot be anticipated, and therefore the related input would have to reach the motor cortex after preparation. Thus, it is an open question whether the objective and network characteristics suggested by the authors could also explain the presence of large preparatory activity before e.g. grasping movements that are thought to be more sensory-feedback-driven (Meirhaeghe et al., Cell Reports 2023).

(6) More broadly, with the type of objectives that the authors assume the inputs fulfill, some M1 properties that lead to strong preparation - notably, limited readout controllability - may not be favorable for control in general, so it would be interesting if other objectives and assumptions could robustly lead to strong preparation under more general M1 properties.'


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89131.4.sa3](https://doi.org/10.7554/eLife.89131.4.sa3)

I remain enthusiastic about this study. The manuscript is well-written, logical, and conceptually clear. To my knowledge, no prior modeling study has tackled the question of 'why prepare before executing, why not just execute?' Prior studies have simply assumed, to emulate empirical findings, that preparatory inputs precede execution. They never asked why. The authors show that, when there are constraints on inputs, preparation becomes a natural strategy. In contrast, with no constraint on inputs, there is no need for preparation as one could get anything one liked just via the inputs during movement. For the sake of tractability, the authors use a simple magnitude constraint: the cost function punishes the integral of the squared inputs. Thus, if small inputs before movement can reduce the size of the inputs needed during movement, preparation is a good strategy. This occurs if (and only if) the network has strong dynamics (otherwise feeding it preparatory activity would not produce anything interesting). All of this is sensible and clarifying.

As discussed in the prior round of reviews, the central constraint that the authors use is a mathematically tractable stand-in for a range of plausible (but often trickier to define and evaluate) constraints, such as simplicity of inputs (or inputs being things that other areas could provide). The manuscript now embraces this fact more explicitly and also gives some results showing that other constraints (such as on the derivative of activity, which is one component of complexity) can have the same effect. The manuscript also now discusses and addresses a modest weakness of the previous manuscript: the preparatory activity in their simulations is often overly complex temporally, lacking the (rough) plateau typically seen for data. Depending on your point of view, this is simply 'window dressing', but from my perspective it was important to know that their approach could yield more realistic-looking preparatory activity.

The most recent version of the manuscript also has a useful section in the Discussion on the topic of preparation when there is no external delay, which I found helpful given prior behavioral and physiological studies arguing that preparation can (1) be very brief, but (2) is always present. These findings mesh nicely with the authors' central result that preparation is a good network strategy, and that it would thus be normative for there to be at least a brief interval of preparation even when not imposed externally.
