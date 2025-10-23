# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51005.sa1](https://doi.org/10.7554/eLife.51005.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

That sleep can protect and improve memories is well known, but many details remain unclear. This paper builds a detailed biological computational model to explore and demonstrate such effects.

Decision letter after peer review:

Thank you for submitting your article "Can sleep protect memories from catastrophic forgetting?" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Francesco P Battaglia (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Gonzalez and colleagues study a computational network model of sequence memory encoding and replay, in a thalamocortical network and find that sleep can untangle stored sequences.

Essential revisions:

As you will see there is a rather extensive list of comments and amendments requested. This is not typical for eLife, which aims to either reject or have small revisions. But we felt that if the issues are addressable, it would make a very interesting paper.

Reviewer #1:

Gonzalez and colleagues study a network model of memory encoding and replay, in a thalamocortical network.

The model, based on previous work from the same group, is a quite detailed rendition of neural dynamics (including Hodgkin-Huxley spike generation, and a host of other important conductances and neuromodulatory influences). This enables a fairly realistic depiction of the wake-sleep transition and of Up-Down states dynamics during NREM sleep.

The authors use several different protocols to implement training and replay of overlapping or non-overlapping sequences. Sleep appears to effective at stabilizing and orthogonalizing sequences, preventing catastrophic interference, as much, or in some cases more, than awake training.

The results are interesting in two ways. First, because they show, for the first time to my knowledge, that memory replay can happen and effectively supports consolidation in a realistic model of neural dynamics, and second because it shows some detail about how replay may support memory reorganization, orthogonalization, and protection from interference. Especially this second aspect could be improved in my view by expanding on some analyses, as detailed below:

– The Up/Down states are simulated in the network based on thalamocortical interactions. They are used in the analysis to "segment" neural activity. However, electrophysiological evidence (e.g. Johnson and McNaughton) shows that memory replay is strongest/most likely at the Down to Up state transition. Is this the case in these simulations as well?

– While many of the parameters have different values during wake and sleep, the values of the A+ constant in the STDP rule seem to be the same. If I understand correctly, A- is different in training with respect to sleep (what happens at retrieval?). I was wondering how this affects the higher amount of orthogonalization seen with sleep replay with respect to interleaved awake training.

– Related to the previous point: is total synaptic strength decreasing, or increasing during NREM sleep? This would parallel ideas from e.g. Tononi and Cirelli or Grosmark and Buzsaki. Is greater synaptic depression during sleep a key ingredient for catastrophic interference protection?

– The effect of sleep seems to increase the amount of structure in each of the network blocks, with distinct groups of neurons forming for the sequences in the two directions (for example). This is studied mostly by looking at the synaptic level (asymmetry measure), and there, only by looking at an increase in the variability in the measure. That analysis could easily be extended in my view, by looking at neural activity measures (e.g. population vector correlation), more directly comparable with experimental results from neural ensemble recording. Is there evidence for the emergence of new within and across block structures? For example, to make the parallel with place cells (as done throughout the paper), is there evidence for the emergence, with training, of directional place cells from non-directional ones?

– The retrieval protocol used, in which all neurons in a "block" are strongly activated, may actually downplay the orthogonalizing power of the wake/sleep learning dynamics, because neurons that are assigned to, say, both the S1 and S1* sequences are primed. Is that the case? Wouldn't things look even "better" with a more gentle activation protocol?

– Figure 7B: after S1 training (second panel) the bulk of the neuron pairs shift, as expected, their asymmetry in the direction of S1, however, a smaller subset of neuron pairs go in the opposite direction, towards the K01 corner. Why is that?

Reviewer #2:

Here Gonzalez et al. implement a thalamocortical model to investigate how sleep rescues forgetting in a group of neurons competing for different memories. The study investigates sleep's role in protecting memories encoded in overlapping groups of neurons and provides important insights about the underlying mechanisms. The manuscript is well-written and easy to follow. They show that training a new sequence in a subpopulation that overlaps with a previous sequence leads to interference with the old sequence. Replay during Up states of sleep following this training however is able to reverse the damage caused by competing memories. This replay of competing memories during sleep creates subsets of strongly unidirectional synaptic connections for each learned sequence and some bidirectional connections that may act like network hubs. The approach is interesting and provides general insights into how spiking networks can create distinct but overlapping memories, and also makes some testable predictions.

The main issue, however, is that a key test of the effects of sleep replay on catastrophic interference was not performed: under realistic scenarios, sleep takes place after each sequence learning session separately and new memories are formed on top of pre-existing ones. E.g. the order in typical day-to-day experience is S1, sleep, S2, sleep, S1*, sleep, etc. This important scenario should be examined to test whether the results still hold. In the current models, the sequences seem to saturate specific synapses, which may create issues for future learning.

A second concern is that "replays" are inferred but not explicitly shown. The replay sequence was measured in terms of pairs of neurons active in a given Up state instead of how well the trained sequence is represented. The authors explain that Figure 6C is "suggesting" that two sequences replay simultaneously, but this should be more explicitly shown or better illustrated, as it is an interesting and important prediction of the model. There should also be discussion of how this observation is to be reconciled with the body of literature indicating distinct replay of isolated sequences. Perhaps previous methods based on template matching would fail to detect such overlapping replays? In particular, Wikenheiser and Redish (Hippocampus, 2013) indicate bidirectional replay during sleep, which appears inconsistent with the current results, at least in the hippocampus.

A third issue concerns how memories are selected for replay. In the model it seems that stronger synapses lead to increased replay. This would suggest that replay begets more replay, until synapses are fully saturated. The effects of multiple sleep sequences and/or longer sleep durations should be simulated to examine this scenario, and (as noted above) whether new learning can take place in synapses saturated by sleep. It is also important to note that studies investigating hippocampal replay (e.g. O'Neill et al., 2007; Giri et al., 2019) show decreasing replay of familiar sequences. Do the authors predict different patterns in the cortex? Please discuss.

The authors present and discuss an asymmetric expansion of place fields following sleep. However, this result is not consistent with Mehta et al., 1997 as the authors claim. Mehta in fact found that the backwards expansion of place fields was reset at the beginning of each track session (presumably as a result of overnight sleep), but that the place-fields expanded again over the course of a behavioral session. The findings of Mehta et al. are therefore more consistent with net downscaling of memory during sleep, rather than the model presented here. This discrepancy should be addressed.

Reviewer #3:

This paper examines the formation of sequence memories in a computational model of hippocampus equipped with STDP, and in particular in the role of sleep.

Sleep, as well as interleaved training, is shown to separate storage of forward and backward sequences.

How this relates to catastrophic forgetting is a bit tentative. For instance, I don't think the setup will allow storage of both ABCDE and ABCFG, but it would be nice to be proven wrong.

I wonder whether the story has a simple interpretation: Balanced STDP (A+ = A-, τ+ = τ-) by itself breaks symmetry and will not allow bidirectional connections between neurons. Therefore during sleep recurrent connections are cleared up. During learning however the symmetry is explicitly broken by hand by reducing the LTD term (subsection “Synaptic currents and spike-timing dependent plasticity (STDP)”).

I wonder if the mechanism thus requires an extraordinary amount of fine-tuning that could not expected in biology. On the other hand, during interleaved training, during which the symmetry is presumably also broken by hand, bi-directional connections are also removed. As a result I am not fully convinced my explanation is correct. In any case, I think it would be important to show that the mechanism does not require fine-tuning of the A+/A- ratio.

The paper could have been presented better. The Materials and methods are particularly poor, as it mentions for instance histamine modulation and minis, however, they are mentioned just once and it remains completely unclear whether these ingredients matter. Now it might well be that this was extensively discussed in previous papers, but that is no excuse.

Similarly the dynamics of the synaptic input (subsection “Synaptic currents and spike-timing dependent plasticity (STDP)” is not discussed.
