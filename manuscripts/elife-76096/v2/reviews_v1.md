# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76096.sa0](https://doi.org/10.7554/eLife.76096.sa0)

One of the key questions in sensory neuroscience is how cortical networks extract invariant percepts from variable sensory inputs. While much of the literature focuses on the role of feedforward hierarchical processing for extracting invariant percepts, this study proposes a novel implementation based on top-down feedback. The article analyses the underlying mechanism based on an invariant subspace and presents instantiations of this mechanism at different levels of biophysical realism.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76096.sa1](https://doi.org/10.7554/eLife.76096.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Invariant neural subspaces maintained by feedback modulation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife at this time.

While all three reviewers appreciated the novelty of the proposed computational role for feedback connections, they estimated that substantial additional work would be needed to establish more firmly the mechanisms underlying context–invariant processing and its biological relevance. Given the extent of the criticisms, we have decided to reject the paper. Should further analyses allow you to fully address these criticisms we would be open to a resubmission.

Reviewer #1:

One of the key questions in sensory neuroscience is how cortical networks extract invariant percepts from variable sensory inputs. Much of the existing literature focuses on the role of feed–forward hierarchical processing for extracting such invariances. The present study proposes an alternative mechanism based on top–down feedback. Focusing on the so–called source–separation, or cocktail–party problem, the manuscript shows how sources mixed in a context–dependent manner can be separated independently of context, using feed–forward networks modulated by top–down context–dependent inputs.

The manuscript starts with a simplified, abstract network, and then progressively moves to more biologically plausible ones. By performing population analyses of network activity, the authors then argue for a mechanism based on context–invariant subspaces.

Strengths of the paper:

– novel proposal for an important class of cortical computations

– very elegant formulation of the problem

– the writing style is very clear and appealing

– network implementations at different levels of biophysical realism.

Weaknesses of the paper:

– the announced mechanism, based on invariant subspaces, is not clearly explained and needs to be supported by additional evidence.

– how the network detects contextual changes does not seem to be explained

– the analyses of network activity, their rationale and the resulting conclusions are difficult to follow.

While I very much appreciated the novelty and the elegance of the approach developed in this paper, ultimately, I was left wondering how the networks perform their task.

– The title and abstract announce a mechanism based on invariant neural subspaces. Clearly, since the readout is fixed, there must be an invariant subspace, but the key question is how it is generated and maintained across contexts. In the Results, this mechanism is explained only briefly at the very end of the results, in connection to Figure 6, which seems to be just an illustration. The authors would need to unpack what precisely the mechanism is (not clear right now) and give more evidence for it.

– An important complementary issue is how the network detects context changes. The manuscript states that "feedback–mediated invariance requires time to establish after contextual changes" (lines 245–246), but how this works does not seem to be explained. What type of error signal does the network use to change the gains?

On a related note, is the network trained on all the contexts it sees during testing, or is it able to deal with totally novel contexts?

– The logic of the sequence of analysis (optogenetic manipulations; correlation; changes in gain…) is a bit difficult to follow and needs more motivation. In particular, why is the non–linear encoding of context important?

– It is a bit surprising that the analyses focus on the most complex version of the network to examine mechanisms. Presumably the simplified networks could be leveraged to identify and explain the mechanisms in a more transparent manner.

Reviewer #2:

The authors aim to explore an understudied potential function of feedback connections: providing context–independent sensory processing. Invariant sensory processing is frequently assumed to be carried out by feedforward processing and much of the study of feedback focuses on how feedback could implement context–dependent processing. This makes this study promising and relatively novel.

The strengths of this paper are that it demonstrates convincingly and using a variety of network architectures and feedback mechanisms that feedback modulations can indeed help a network read out sensory input in a context–independent way.

The weaknesses are in the analysis and comparisons of the various networks. While the basic finding that this invariance does not result from invariant activity on the individual neuron level is interesting and of value, the explanation that it instead leads to invariant population activity is almost tautological given the network architecture. It is also unclear how the simpler models the authors present are meant to provide insight on either the more biologically detailed hierarchical model or on real neural processing, especially given that the mode of modulation in the simplest model (re–weighting of feedforward weights) differs from that of the later models (re–weighting of neural activation). In this way I don't feel that the authors fully achieved their goal of describing the mechanism of feedback modulation.

The methods appear technically sound, but I am confused by some of the choices. For example, the authors start with a single layer network where feedback modulates the weights between the input and output. This is a different mechanism than the normal neuronal gain usually attributed to feedback. The authors then add more details to push the model more in the biological direction, but multiple details are sometimes added at once and the logic behind these choices isn't always clear. I believe the authors switch to using neuronal gain when they want to explore spatially correlated modulation, but they don't talk about neuronal modulation until they introduce their full hierarchical model. The hierarchical model also adds Dale's law and a separate inhibitory population but it is not clear why these details were added or if/how they change the function of the model in a way relevant to understanding feedback modulation. Even the use of a multi–layer model is not very well motivated given that they show that this task can be completed with a very small one layer model. The simplicity of the task has implications for understanding some of these findings as well. For example, to show that modulatory signals can be spatially correlated, the authors create a model with many more neurons than is needed to solve the task and show that the modulatory signal can target nearby cells in this population similarly without sacrificing performance. But the low dimensional nature of the modulatory signal is only really an issue of interest in the context of a higher dimensional task. As a thought experiment: if the 2 neurons in the original model were simply replicated to 50 each and each population of 50 neurons was given the same modulation, this would be essentially equivalent to the original 2 cell model, but under the logic of what the authors have shown here, would supposedly demonstrate that modulatory signals still work if low dimensional. In this way, that analysis fell short.

I think that this work may spur more interest in studying the role of feedback for invariant sensory processing, which would be a very productive outcome. Furthermore, the demonstration that the context signals cannot be linearly readout from the cells performing the modulation is an important lesson for the analysis of neural data. I also think further reflection on the finding that the modulatory network needs direct sensory input (more so even than the input from later processing stages) will be very important for understanding how this modulation works and how it relates to biological structures. As the authors note, this may mean that their model is more akin to inputs from higher order thalamic areas, though even that mapping is imperfect due to the lack of recurrence.

I think it would help the readability of the paper if the authors included a few more brief descriptions of the methods in the Results. For example, a better description of how the signals are generated, the fact that the networks are trained with a single set of signals only, etc. Also, there were points where it wasn't clear if a network was tested under different conditions or actually retrained for them (for example, in figure 2d/e). Also, the fact that the modulation went from being on the weights to on the neurons themselves was not made clear in section "Invariance can be established by spatially diffuse feedback modulation". I also found the schematic in Figure 1a a bit confusing. I don't know why x is represented as a question mark when it is a sum of the two signals. I'd prefer a diagram that makes the dimensionality of x clearer (relatedly, why are there only 3 weights from x to y when I believe it is a 2x2 matrix).

"While we trained the modulatory system using supervised learning, the contextual inference is performed by its dynamics without access to the target sources and thus unsupervised" I feel this could be read as saying that an actual unsupervised objective was used, when in fact only supervised learning took place, so I would suggest re–wording.

I didn't understand the claim about matched EI inputs and how it depends on using gain modulation. This should probably be expanded and related to the main questions of the paper or possibly removed.

Figure 4i seems to be the main demonstration that individual neural activity itself is not invariant to context. I'd like to see a more in–depth exploration of this. Particularly, if the readout only relied on a small handful of neurons then finding that the rest of the neurons are not context–invariant wouldn't prove that individual neural invariance is not a relevant mechanism. Given that the readout from this network is known, it would be particularly easy to determine if the heavily weighted neurons in particular are or are not context invariant.

In general, I don't understand why the authors use a separately trained linear readout when trying to show that the population activity at the final layer is invariant. They eventually acknowledge that "Since this readout is obtained from the data, this procedure does not require knowledge of the readout in the network model. Note that the trained decoder and the network readout are not necessarily identical" but they don't explain why they are using this alternative readout or what new insights its use adds. Particularly, the performance of the network indicates the there is some sort of context invariant read out possible from this population, yet the authors use this other readout in a way that is seemingly supposed to add something to the explanation.

Be sure to say what errorbars are based on in all figures.

"In our model, the mechanism needs to satisfy a few key

requirements: i) the modulation is not uniform across the population, ii) it operates on a timescale similar to that of changes in context, and iii) it is driven by feedback projections." I don't understand claim (iii). If anything, the results show the importance of the modulation being driven by feedforward sensory signals (figure 2d/e).

"In addition, feedback inputs from the sensory to the modulatory system allow a better control of the modulated network state." I don't see how the connections from a sensory system to a modulatory system are "feedback".

Reviewer #3:

I appreciate the didactic way in which the manuscript was written (and beautiful figures!), in particular the progression from a vanilla architecture towards the full fledged model with EI rectified neurons with spatially specific modulation. My main concerns (detailed below) are two–fold:

1. I felt that some extensions were not explicitly justified (e.g. why 2 layers instead of 2, etc)

2. I was expecting more 'reverse–engineering' of the mechanism through which the network accomplishes a context invariant projection. This is the main result of the paper, as reflected in the title, so I think it deserves more unpacking. Below I unpack these concerns, sometimes providing some suggestions to improve the motivation and clarity of the paper (without any particular order)

1. Overall, the architecture choices are a bit unjustified. In the extreme, wouldn't the LSTM alone solve the task? The addition of each feedforward layer should be better motivated (e.g. more biologically realistic? In what sense?). For example, why add an extra layer from extensions 2 and 3? If those are necessary, this should be explained. If they are not necessary, they should be removed.

2. 'Because the task requires a dynamic inference of the context, it cannot be solved by feedforward networks or standard blind source separation algorithms' I think the paper could be better motivated if this was shown explicitly with some examples.

3. A figure explicitly illustrating the training setup would help motivate what is trivially solved and what is actually challenging. For instance, in the main manuscript, it is not clear in which cases the network is trained and tested on the same contexts (ie A(t)) and which cases it is not. In the first case, the context can be easily inferred from x(t) but the latter is more challenging?

4. however I understand that the paper is already too long, Intra / extrapolation results deserve more spotlight and unpacking in my opinion. In general, if there is a lack of space, I would merge Figure 1 and figure 2 – and jump directly to extension 1 – and move most of figure 2 to sup.

5. Most important concern to me: Figure 6, in which the mechanism is revealed, deserves more quantifications to explicitly pinpoint the mechanism. Three suggestions come to mind:

a. Plot the 3 PCs components (instead of just 1) and show the readout in this space. The key result is that the readout is invariant to context and this is not clearly illustrated at the moment. Instead, what is shown is that the representation changes, but that it changes in a way that preserves invariance on the readout is not clearly highlighted.

b. The authors highlight that the network is not just reversing the new mixing coefficients and projecting the activity back into the 2d low manifold. Instead, it is rotating everything out of this manifold. My suggestion would be to show this alternatively explicitly. Is it actually possible? Relatedly, what happens if the context is changed back to context 1?

c. Finally, all the statements made about this figure should be quantified and not just illustrated for 1 trial.
