# Peer review - Round 1

Editors:
- Lisa M Giocomo, Stanford School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80671.sa0](https://doi.org/10.7554/eLife.80671.sa0)

This is an important article that leverages a spiking network model of the hippocampal circuit to show how spike-time-dependent plasticity can implement predictive reinforcement learning and form a predictive map of the environment. The authors provide a convincing and solid framework for understanding the prediction based learning rules that may be employed by the hippocampus to optimize an animal's behavior. This paper will be of interest to theoretical and experimental neuroscientists working on learning and memory as it provides new ways to connect computational models to experimental data that has yet to be fully explored from a reinforcement learning perspective.


---

# Peer review - Round 1

Editors:
- Lisa M Giocomo, Stanford School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80671.sa1](https://doi.org/10.7554/eLife.80671.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Learning predictive cognitive maps with spiking neurons during behaviour and replays" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael E. Hasselmo (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Based on the comments from all reviewers, I'd recommend focusing your revisions on the primary topic of improving the link between their model and experimental data. Specifically, this would include: Consideration (or modeling) of how the model would extend to 2D, discussion on how the neural activity would be used to perform computations, the limitations of RL as it relates to interpreting experimental data, and to more appropriately frame the work in the context of experimental studies (all reviewers had detailed suggestions for how to do this with text changes). I've provided highlights from the three reviewers below that apply to these concerns but note that reviewer 2 also provided a number of specific suggestions related to text/reference changes. All reviewer comments are also included at the bottom of this message.

Reviewer 1:

– The successor representation is learned at the level of synaptic weights between the two layers. It is not clear how it is read out into neural activity and exploited to perform actual computations, as both layers are assumed to be strongly driven by external inputs. This is a major limitation of this work.

– One of the results is that STDP at the timescale of milliseconds can lead to learning over behavioral timescales of seconds. This result seems related to Drew and Abbott PNAS 2006. In that work, the mapping between learning on micro and macro timescales in fact relied on precise tuning of plasticity parameters. It is not clear to which extent similar limitations apply here, and what is the precise relation with Drew and Abbott.

– Most of the results are presented at a formal, descriptive level relating plasticity to reinforcement learning algorithms. The provided examples are quite limited and focus on a simplified setting, a linear track. It would be important to see that the results extend to two-dimensional environments, and to show how the successor representation is actually used (see first comment).

– The main text does not explain clearly how replays are implemented.

Reviewer 2:

I think the authors of this article need to be clear about the shortcomings of RL. They should devote some space in the discussion to noting neuroscience data that has not been addressed yet. They could note that most components of their RL framework are still implemented as algorithms rather than neural models. They could note that most RL models usually don't have neurons of any kind in them and that their own model only uses neurons to represent state and successor representations, without representing actions or action selection processes. They could note that the agents in most RL models commonly learn about barriers by needing to bang into the barrier in every location, rather than learning to look at it from a distance. The ultimate goal of research such as this should be to link cellular level neurophysiological data to experimental data on behavior. To the extent possible, they should focus on how they link neurophysiological data at the cellular level to spatial behavior and the unit responses of place cells in behaving animals, rather than basing the validity of their work on the assumption that the successor representation is correct.

Reviewer 3:

1. Could the authors elaborate more on the connection between the biological replays that are observed in a different context in the brain and the replays implemented in their model? Within the modeling context, when are replays induced upon learning in a novel environment, and what is the influence of replays when/if they are generated upon revisiting the previously seen/navigated environment?

2. The model is composed of CA1 and CA3, what are the roles of the other hippocampal subregions in learning predictive maps? From the reported results, it looks like it may be possible that prediction-based learning can be successfully achieved simply via the CA1-CA3 circuit. Are there studies (e.g., lesioned) that show this causal relationship to behavior? Along this line, what are the potential limitations of the proposed framework in understanding the circuit computation adopted by the hippocampus?

3. Do the authors believe that the plasticity rules/computational principles observed within the 2-layer model are specific to the CA1-CA3 circuit? Can these rules be potentially employed elsewhere within the medial temporal lobe or sensory areas? What are the model parameters used that could suggest that the observed results are specific to hippocampus-based predictive learning?

4. The analytical illustration linking the proposed model with reinforcement learning is well executed. However, in practice, the actual implementation of reinforcement learning within the model is unclear. Given the sample task provided where animals are navigating a simple environment, how can one make use of value-based learning to enhance behavior? Explicit discussion on the extent to which reinforcement learning is related to the actual computation potentially needed to navigate sensory environments (both learned and novel) would be really helpful in understanding the link between the model to reinforcement learning.

5. Subplots both within and across figures seem to be of very different text formatting and sizing (such as panel F in Figure 4 and Figure 5). Please reformat them accordingly.

Reviewer #2 (Recommendations for the authors):

Important: Note that the page numbers refer to the page in the PDF, which is their own page number-1 (due to eLife adding a header page).

Page 3 – "smoothly… and anything in between" – this is overstated and should be removed.

Page 3 – "don't need to discretize time…". Here and elsewhere there should be citations to the work of Doya, NeurIPS 1995, Neural Comp 2000 on the modeling of continuous time in RL.

Page 3 – "using replays" – It is very narrowminded to assume that all replay do is set up successor representations. They could also be involved in model-based planning of behavior as suggested in the work of Johnson and Redish, 2012; Pfeiffer and Foster, 2018; Kay et al. 2021 and modeled in Hasselmo and Eichenbaum, 2005; Erdem and Hasselmo, 2012 and Fenton and Kubie, 2012.

Page 3 – They assume that STDP can occur during replay, but evidence for STDP during replay is unclear. McNaughton's lab showed that LTP is less likely to be induced during the modulatory states during which sharp-wave ripple replay events occur. They should look for citations that have actually shown LTP induction during the replay state.

Page 4 – Marr's three levels – They should remove this discussion about Marr's three levels as I think the implementation level is relatively sparse and the behavioral level is also relatively sparse.

Page 4 – "The hippocampus has long been thought" – It's astounding that the introduction only cites two experimental papers (O'Keefe and Dostrovsky, 1971; Mehta et al. 2000) and then the start of the Results section makes a statement like this and only cites Stachenfeld et al. 2017 as if it were an experimental paper. There are numerous original research papers that should be cited for the role of hippocampus in behavior. They should cite at least five or six so that the reader doesn't get the impression all o this work started with the holy paper by Stachenfeld et al. 2017. For example, they could again cite O'Keefe and Nadel, 1978 for the very comprehensive review of the literature up to that time, plus the seminal work of Morris et al. 1982 in Morris water maze and Olton, 1979 in 8-arm radial maze and perhaps some of the work by Aggleton and by Eichenbaum on spatial alternation.

Page 5 – The description of successor representations is very one dimensional. They should mention how it can be expanded to two dimensions.

Page 5 – "Usually attributed to model based…". They cannot just talk about SR being model free. Since this section was supposed to be for neuroscientists, they need to clearly explain the distinction between model free and model-based RL, and describe why successor representations are not just model-based RL, but instead provide a look-up table of predictive state that does NOT involve model-based planning of behavior. The blog of Vitay gives a much better overview that compares model-free, model-based and successor representations:

https://julien-vitay.net/post/successor_representations/ – This needs more than just a citation – there should be a clear description of model-based and model-free RL in contrast to SR, and Vitay is an example of that.

Page 5 – Related to this issue – they need to repeatedly address the fact that Successor representations are just an hypothesis contrast with model-based behavior, and repeatedly throughout the paper discuss that model-based behavior could still be the correct accounting for all of the data that they address.

Page 5 – "similar to (Mehta et al. 2000)" – Learning in the CA3-CA1 network has been modeled like this in many previous models that should be cited here including McNaughton and Morris, 1987; Hasselmo and Schnell, 1994; Treves and Rolls, 1994; Mehta et al. 2000; Hasselmo, Bodelon and Wyble, 2002.

Page 6 – Figure 1d looks like the net outcome of the learning rule in this example is long-term depression. Is that intended? Given the time interval between pre and post, it looks like it ought to be potentiation in the example.

Page 7 – They should address the problem of previously existing weights in the CA3 to CA1 connections. For example, what if there are pre-existing weights that are strong enough to cause post-synaptic spiking in CA1 independent of any entorhinal input? How do they avoid the strengthening of such connections? (i.e. the problem of prior weights driving undesired learning on CA3-CA1 synapses is addressed in Hasselmo and Schnell, 1994; Hasselmo, Bodelon and Wyble, 2002, which should be cited).

Page 7 – "Elegantly combines rate and temporal" – This is overstated. The possible temporal codes in the hippocampus include many possible representations beyond just one step prediction. They need to specify that this combines one type of possible temporal code. I also recommend removing the term "elegant" from the paper. Let someone else call your work elegant.

Page 7 – "replays for learning" – as noted above in experiments LTP has not been shown to be induced during the time periods of replay – sharp-wave ripple replay events seem to be associated with lower cholinergic tone (Buzsaki et al. 1983; VandeCasteele et al. 2014) whereas LTP is stronger when Ach levels are higher (Patil et al. J. Neurophysiol. 1998). This is not an all-or-none difference, but it should be addressed.

Page 7 – "equivalent to TD…". Should this say "equivalent to TD(0)"?

Page 8 – "Bootstrapping means that a function is updated using current estimates of the same function…". This is a confusing and vague description of bootstrapping. They should try to give a clearer definition for neuroscientists (or reduce their reference to this).

Page 9 – Figure 2 – Do TD λ and TD zero really give equivalent weight outputs?

Page 8 – "that are behaviorally far apart" – I don't understand how this occurs.

page 10 – "dependency of synaptic weights on each other as discussed above." This was not made sufficiently clear either here or above.

Page 10 – "dependency of synaptic weights on each other" This also suggests a problem of stability if the weights can start to drive their own learning and cause instability – how is this prevented?

Page 10 – "average of the discounted state occupancies" – this would be uniform without discounting but what is the biological mechanism for the discounting that is used here?

Page 10 – "due to the bootstrapping" – again this is unclear – can be improved by giving a better definition of bootstrapping and possibly by referring to specific equation numbers.

Page 11 – "exponential dependence" what is the neural mechanism for this?

Page 11 – "Ainsley" is not a real citation in the bibliography. Should fix and also provide a clearer definition (or equation) for hyperbolic.

Page 11 – "elegantly combines two types of discounting" – how is useful? Also, let other people call your work elegant.

Page 11 – how does discounting depend on both firing rate and STDP -- should provide some explanation or at least refer to where this is shown in the equations.

page 13 – "Cheng and Frank" – this is a good citation, but they could add more here on timing of replay events.

Page 15 – This whole section on the shock experiment starts with the assumption of a successor representation. As noted above, they need to explicitly discuss the important alternate hypothesis that the neural activity reflects model-based planning that guides the behavior in the task (and could perhaps better account for the peak of occupancy at the border of light and dark).

Page 16 – "mental imagination" – rather than using it for modifying SR, why couldn't mental imagination just be used for model-based behavior?

Page 17 – "spiking" – again, if they are going to refer to their model as a "spiking" model, they need to add some plots showing spiking activity.

Reviewer #3 (Recommendations for the authors):

I found the proposed modeling framework to be very exciting and of potential interest to not only computational neuroscientists but also to readers who are interested in neural mechanisms underlying learning in general. The manuscript is well-written and includes a detailed description and rationale of the model setups as well as the findings and their relevance to biological findings. That said, I have a few comments that I hope the authors could help address:

1. Could the authors elaborate more on the connection between the biological replays that are observed in a different context in the brain and the replays implemented in their model? Within the modeling context, when are replays induced upon learning in a novel environment, and what is the influence of replays when/if they are generated upon revisiting the previously seen/navigated environment?

2. The model is composed of CA1 and CA3, what are the roles of the other hippocampal subregions in learning predictive maps? From the reported results, it looks like it may be possible that prediction-based learning can be successfully achieved simply via the CA1-CA3 circuit. Are there studies (e.g., lesioned) that show this causal relationship to behavior? Along this line, what are the potential limitations of the proposed framework in understanding the circuit computation adopted by the hippocampus?

3. Do the authors believe that the plasticity rules/computational principles observed within the 2-layer model are specific to the CA1-CA3 circuit? Can these rules be potentially employed elsewhere within the medial temporal lobe or sensory areas? What are the model parameters used that could suggest that the observed results are specific to hippocampus-based predictive learning?

4. The analytical illustration linking the proposed model with reinforcement learning is well executed. However, in practice, the actual implementation of reinforcement learning within the model is unclear. Given the sample task provided where animals are navigating a simple environment, how can one make use of value-based learning to enhance behavior? Explicit discussion on the extent to which reinforcement learning is related to the actual computation potentially needed to navigate sensory environments (both learned and novel) would be really helpful in understanding the link between the model to reinforcement learning.

5. Subplots both within and across figures seem to be of very different text formatting and sizing (such as panel F in Figure 4 and Figure 5). Please reformat them accordingly.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Learning predictive cognitive maps with spiking neurons during behaviour and replays" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer 1 makes two text suggestions that I believe would clarify the findings. There remains some lack of clarification around (1) how the second layer of the model mixes the successor representation with a representation of the current state itself and (2) justification for the difference in duration of the external inputs to the two layers. Reviewer 1 also suggests an additional figure, but I leave the decision to add (or not) this to the authors. Details regarding the requested clarifications are below.

Reviewer #1 (Recommendations for the authors):

The revised article has only partly resolved my confusion.

My main issue was the following: in the proposed feed-forward model, the synaptic weights between the two layers learn the entries of the successor matrix. If external inputs were fed only to the first layer, the second layer would directly read out the successor representation (this is suggested in Figure 1 E-F, but not explicitly mentioned in the text as far as I can tell). Instead, in the model, both layers are driven by external inputs representing the current state. This is crucial for learning, but it implies that the activity of the second layer mixes the successor representation with a representation of the current state itself. Learning and readout, therefore, seem antagonistic. It would be worth explaining this fact in the main text.

In their reply, the authors clarify that the external inputs drive the activity of the second layer only for a limited time (20%). As far as I can tell, in the text, this is mentioned explicitly only in the legend of Figure 5-S2. That seems to imply that there is a large difference in the duration of the external inputs to the two layers. How can that be justified?

More importantly, it seems that varying the value of the delay should lead to a tradeoff between the accuracy of learning and the accuracy of the subsequent readout in the second layer. Is that the case? It would be useful to have a figure where the delay is varied.
