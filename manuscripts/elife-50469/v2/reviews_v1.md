# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50469.sa1](https://doi.org/10.7554/eLife.50469.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper combines a computational model with analysis of human data to explain how humans learn to use temporal proximity to learn task sets and switch between the task sets.

Decision letter after peer review:

Thank you for submitting your article "Temporal chunking as a mechanism for unsupervised learning of task-sets" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper develops a model of task switching that uses synaptic plasticity that includes temporal contiguity to chunk the tasks, and compares the model to human behaviour and fMRI findings. The combination of all these 3 ingredients is interesting and allows for a precise comparison between model and data.

Essential revisions:

1) In the model the weights in the Association Network are gradually updated. One would imagine that once participants have been exposed to a limited number task sets in the recurrent task, they can switch very rapidly (and perhaps without invoking synaptic plasticity). I.e. an alternative to the model is that the connections in the Association Network are directly gated by the task network. I would like to see the predictions of the model regarding this, namely I would like to know how the data plotted in Figure 6B evolve as learning progresses, and compare data to model.

2) In the Task Network starting from small weights there is a sudden emergence of a cluster when weights cross g_I (as the Discussion section mentions it should actually be modelled as an attractor in a Hopfield network). Is there evidence for such a switch in the data?

3) Related to that, it would be interesting to see the model prediction for the case that a new task-set partly overlaps with a learned one and one needs to un-learn the previous task-set.

4) While the full model fits better than the non-chunking model in terms of AIC, I would really like to see the actual fit of both models.

5) Clarification of model. I found the description of the model to be unclear and more can be done to explain why certain modeling choices were made. Specifically, was this an attractor network with internal dynamics and did the activity in the network persist from trial-to-trial? Equations 5 and 7 suggest that learning occurs in the difference between trial-to-trial activity in the task-set network and that the activity in the task-set network on one trial influence the weights of the associative network in the subsequent trial. I found this surprising – based on the Introduction, I was expecting to see a recurrent model in which activity was sustained across trials.

6) It appears the model was fit separately for the "recurrent" and "open-ended" session – why was this done? I find it implausible that subjects would have two sets of parameters that best describe their behavior in this task (as this analysis implies, especially Figure 5B), especially as the two sessions were un-signaled. It makes more sense to me to fit a single model to all of the data and examine the trial-by-trial log-loss. Does the model have the expressiveness to capture both sessions under the same parameter set? How does this change the analysis?

7) The comparison to previous computational models is lacking. There is an existing neuro-biological model of task-set learning with physiological constraints (Collins and Frank, 2013) that warrants comparison, especially as the first author of that paper was the first author of the paper re-analyzed here. The paper itself was cited but described as "without any physiological constraint" which is not a fair description of the work. More broadly, the comparison to basal ganglia/PFC gating models is worth making (e.g. Frank and Badre, 2012; Rougier et al., 2005), as it is not obvious to me how the author's model makes different predictions from prior biological models. I would also note that there are algorithmic similarities between this model, the successor representation (Russek et al., 2017) and the Temporal context model (Gershman et al., 2012 explains this most clearly).

8) Were there any findings in the hippocampus related to the task-set network? There is a long literature of sequential dependencies being represented in the hippocampus (see Davachi and Dubrow, 2015 for review), and it would not be surprising if the model accounted for hippocampal activity as well.

9) Conceptually, the model is a minor extension of the existing model of Rigotti et al., (2010a,b) from the Fusi group with application to the human behavioral task at hand. It combines standard reinforcement learning of stimulus-response associations with a context-network that encodes the current task (called task-set network). To generalize across the three different possible stimuli in a given task the context network uses a Hebbian unsupervised learning rule. The most problematic part, from a biological perspective, is the fact that the feedback from the context network to the stimulus-response association network acts directly on the connections inside the stimulus-response association network (as opposed to input to neurons which would be the standard way of doing it). Unless this is justified by additional information (could be text, links to biological literature of biological synapses, or simulations of a more complex, but neuron-based model) I consider this as a potential flaw of the model. The link to the Fusi paper is not sufficient in my opinion.

10) Motivation of model. Even though the authors imply that they have put together a biologically plausible model, it actually looks more like a very high-level abstract model where a whole population of neurons is replaced by a single binary switch; where there are exactly as many binary switches as there are potential combinations of stimuli and responses; and where learning rules are written as algorithmic updates rather than as weight changes driven by pre-and postsynaptic activity.

Thus, I was not convinced about the approach until I understood in Figure 6 and the associated text that the authors actually use this abstract model (which only has a few free parameters, number to be clarified, see below) to fit behavioral data on a subject-by-subject basis. For me this is the strongest point of the paper which eventually makes me support publication after some modifications.

Nevertheless, it is unclear to me whether the same learning rules would also work if the neural network model included a large number of randomly connected neurons, heterogeneity, and continuous-values rate units. I understand that the competitive dynamics would make the continuous-values units near-binary after learning, but the dynamics during learning might still be different, and hence convergence times as well (which could influence the results of the paper). Alternatively, reformulate the text to make it clear that the modeling work uses a rather abstract model with abstract learning rules.
