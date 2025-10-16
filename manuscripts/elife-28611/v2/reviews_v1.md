# Peer review - Round 1

Editors:
- Geoffrey Schoenbaum, National Institutes of Health , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28611.018](https://doi.org/10.7554/eLife.28611.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Phasic and tonic neuron ensemble codes for stimulus-environment conjunctions in the lateral entorhinal cortex" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Geoffrey Schoenbaum (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Thomas J. McHugh (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors record in LEC during a trace eyeblink conditioning task in which an auditory and a visual cue led to shock in different contexts. LEC neurons exhibited both phasic and tonic firing, correlated with multiplexed information about the cues, their significance in different contexts and different trial blocks. Particularly remarkable, tonic activity reflected activity about the current block/context between trials, and this activity seemed to reflect a fairly precise internal model of the time or duration of the current block, inasmuch as it seemed to reflect the start of new blocks in the current context, which would otherwise be unsignaled.

Essential revisions:

Reviewers agreed that the work was sound and the results are quite novel and interesting. There were a couple things raised by the two reviewers and in discussions that seemed particularly worthwhile to do. One was to clarify whether firing changes really do precede the first trial of a new block in the same context or whether they are cued by the first shock or shock omission. The other was showing whether or not there is a relationship to behavior would be a good addition.

Reviewer #1:

In this paper, the authors record in LEC during a trace eyeblink conditioning task. In the task, the have an auditory and a visual cue, each of which predicts shock in a different context or box, and they alternate blocks of trials in which shock is given with blocks in which it is not. They report that LEC neurons exhibit both phasic and tonic firing, correlated with multiplexed information about the cues, their significance in different contexts and different trial blocks. Particularly remarkable, tonic activity reflected activity about the current block/context between trials, and this activity seemed to reflect a fairly precise internal model of the time or duration of the current block, inasmuch as it seemed to reflect the start of new blocks in the current context, which would otherwise be unsignaled.

I think the paper is generally sound and the results are quite novel and interesting. I have no major concerns from my reading and generally agree with the comments of the other reviewers. In particular, I think the authors should clarify whether firing changes really do precede the first trial of a new block in the same context or whether they are cued by the first shock or shock omission. I also think showing whether or not there is a relationship to behavior would be a good addition. Clarifying the other analysis issues would be important. In this area, I am particularly interested in the question raised about the decoding and why it is expressed as fractional performance rather than a raw percentage and the question of whether the tonic and phasic description is really a dichotomy.

Reviewer #2:

In this manuscript, Pilkiw and colleagues describe recordings made in the lateral entrorhinal cortex (LEC) as rats experienced a multi-block fear conditioning paradigm previously shown to depend of LEC function. The authors report that during cue presentation, neurons in LEC show complex patterns of mixed selectivity, encoding features of the task blocks (context, current meaning of the CS, modality of the CS) in a combinatorial way. Interestingly, the authors also demonstrate that information about the task's features was represented during the inter-trial interval by a separate population of neurons. The authors further show that the distinct representations of trial blocks they identify are not merely the result of a slow drift in ensemble representations over the course of a session, but rather that at least certain types of block transitions elicit step-like jumps in ensemble representations.

These data are an interesting and potentially valuable contribution to the literature. Attempts to understand entorhinal/hippocampal function in tasks that are not entirely and explicitly spatial are always welcome, and this paradigm is particularly interesting because of the rich temporal structure the blocked design creates; this allows the authors to investigate LEC encoding of both overtly-signaled aspects of the task (e.g. transitions between contexts) and more subtle features that require animals to track simultaneously multiple aspects of the task (e.g. whether the CS predicts shock, which depends on context, CS modality, and the temporal order of blocks). The analyses presented here are sophisticated, detailed, and generally sound, and the authors complement traditional single unit analyses with more modern, decoding-based approaches to identify what information is being represented by the population of neurons they recorded.

I have a few major questions that, if addressed, I think would strengthen the manuscript further.

1) The authors argue that animals learn the temporal structure of the task (i.e. whether the CS will be followed by the US in the particular block of trials). Is there any evidence of this specifically? When the block transition involves a change between the two contexts, rats clearly have overt evidence that there has been a change in block. However, is there specific evidence that they know before the first trial was completed whether or not they'd be shocked after the CS? Certainly once a shock does or does not arrive the identity of the block would be clear. But observing the context change as evidence of a new block and then waiting to see whether or not the CS in the current block is paired with shock is different than learning the temporal sequence of "shock present" and "shock absent" blocks.

This question is particularly interesting for block transitions that did not involve a change in context. In this case, if I understand the design correctly, there is no overt evidence whatsoever that a change in block has occurred. The first observable evidence that they're in a new block would be a change in whether the CS was or was not followed by the US. So, if rats did in fact learn the temporal structure of the task (and weren't using shock presence/absence to determine block identity), for block transitions that did not involve a change in context they would need to somehow time the length of blocks to estimate when transitions had occurred. Over the timescale of blocks on this task, that seems somewhat hard to imagine.

This also relates to the analyses in Figure 6 regarding transitions between neural representations of trial blocks. In the text of the manuscript the authors claim that ensemble transitions occur before the first CS presentation in a new block. Again, this is easy to understand in the case that animals moved to a new context for the block transition in question, but is it also true of transitions that did not involve a change in context? If pre-CS transitions in ensemble representations only occur when block switches involve a change in context, can it really be said that animals "prospectively" anticipated which block would be next?

To be clear, I'm not sure this issue substantially impacts the novelty or importance of the work here. Neural representations clearly differentiate task blocks and show step like changes across at least some block transitions; whether these representations are based on a fully-internal, learned model of how the task works, or whether they are prompted by the confirmatory presence/absence of shocks, I think the result is clear and interesting. But more clarity on precisely what is being claimed here would be appreciated.

2) The decoding results are a bit confusing to me. Why is classification accuracy presented as a fractional value of decoding performance on the shuffled data set rather than the raw percentage of trials correctly classified? I found this somewhat unintuitive. Does classification based on shuffled data not fall to the theoretical chance level? If not, does this suggest some bias has crept into the classifier somewhere?

Similarly, classification accuracy for "relationship" falls substantially below classification accuracy for shuffled data. How can performance on the actual data be worse than data where shuffling has removed all information about the actual trial identity?

3) The authors begin their analyses by dividing neurons into those that had a significant change in firing rate during the CS period and those that did not, and go on to conclude that the two classes of neurons form phasic and tonic codes related to the task. Is it clear, however, whether neurons with phasic responses did not also contribute to task representations during the ITI? Similarly, is it clear that the tonic neurons represented information homogeneously across the entire ITI? Perhaps some of the "tonic" responses were actually phasic and time-locked to the CS or US with a lag, such that their peak firing response occurred during the ITI. For instance, a hypothetical neuron might have reliably fired a burst of spikes 0.5 seconds after the offset of the US; while this response may have been perfectly phasic, it would have fallen during the ITI, and thus been counted as "tonic" activity. Because firing rates for the tonic neurons were computed over the full duration of the ITI (so far as I can tell), phasic responses like this hypothetical example could drive differences in the average ITI firing rate.

I grant that the example neurons the authors present do indeed look pretty "tonic", but it would be interesting to know whether the information the authors can decode during the ITI is truly homogenous across time at a single cell level, or is instead homogeneous across time at a population decoding level, but supported by transient, phasic activations of single neurons.

Reviewer #3:

The manuscript of Pilkiw et al. describes an experiment designed to characterize how neuronal responses in the lateral entorhinal cortex are modulated by sensory and contextual stimuli. The authors build on previous work from their group demonstrating activity in the LEC is required for the acquisition and expression of trace eyeblink conditioning, as well as their characterization of PFC neuronal activity during a very similar behavior. Here they design a clever protocol that interleaves multiple sensory stimuli and contexts to specifically examine how events and environments are associated in the LEC. Overall I find the experiment to be well designed and described and the analyses to support the informative and timely conclusions of the paper. I have a few suggestions and clarifications outlined below:

1) The authors suggest behavioral data establishes a framework in which the observed physiological activity can be interpreted as necessary for the behavior. While I do not disagree, it raises the issue of the correlation of the activity with the rat's behavior on a trial by trial basis. Given the rats only exhibit the CR on roughly 50% of the trials does a comparison of the activity of the various population (phasic/tonic; R/E/M?) of neurons during response/no response trials reveal the relative importance of one type of LEC coding in the rats behavioral output? I realize this is a bit off-topic for the main thrust of this study, it seems like an interesting analyses of these robust data.

2) The authors interpret the tonic activity related to context reflects the animals' experience in the task. Unlike in their PFC recording paper earlier this year, it appears in the current study recording made during both learning and post-learning periods were pooled. Was this indeed the case? If so, how does that impact the interpretation of the data in Figure 6 which is memory-driven predictive code?

3) Given previous LEC recording studies (Tsao et al., Deshmukh et al), albeit in a different task, it was a bit surprising to me that virtually every single recorded neuron here was responsive, either to the CS or tonically. The authors should address this discrepancy in the Discussion.

4) In the Materials and methods the authors describe the "Differential Index" as the absolute value of (FR1-FR2)/(FR1+FR2), thus running on a scale from 0 to 1. However in Figures 3C and 4C they plot the values on a -1 to 1 scale. While I understand the value in this, it should be clarified in the Materials and methods.

5) A simple table describing the number of units recorded per rat and number of sessions per animal would be useful.
