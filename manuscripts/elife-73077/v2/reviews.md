# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73077.sa0](https://doi.org/10.7554/eLife.73077.sa0)

This eLife Advance by Sun et al. expands on a previous publication in 2020 which developed and outlined a model for biologically inspired visual navigation circuit. Here they include odour and wind input and successfully recreate complex multimodal behavioural observations in ants, illustrating that the model is suited to generate viable hypotheses about circuit-level implementation of navigational control networks in insects in response to varied sensory inputs.


---

# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73077.sa1](https://doi.org/10.7554/eLife.73077.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "How the insect central complex could coordinate multimodal navigation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Mani Ramaswami as Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stanley Heinze (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the work is significant, valuable and of general interest, several key issues that need to be addressed prior to publication are enumerated below.

1) The authors integrate odor based and visual navigation behavior in the same model by simply swapping out the sensory apparatus and early stage processing pathways. While the principal approach is not unreasonable, it is possible that this is an over-simplification. Odor information reaches the antenna in discrete packages (pulses resulting from pockets/filaments of odor molecules suspended in an air stream), while visual information is sampled continuously. Yet the model appears to treat both equivalently and updates each sensory input with every step of the model? Would the model still perform well, if the olfactory input were present intermittently? Could odor concentrations be varied such that odor packages are received only occasionally? How would that affect optimal cue integration? Note that the these are is the likely precise nature of odor stimuli in air rather the "pure" odor gradients used in Matthieu Louis's fly larval experiments. If the authors agree that this is a relevant point, potential consequences in the paper should be discussed, ideally, by includung modeling data showing the impact of different temporal structure of stimuli.

2) The authors postulate a ring attractor circuit in the FB of the CX and refer to the fly connectome (Hulse et al.,) for support. However, that paper explicitly states (while referring to path integration memory): "… Solutions like these seem unlikely to be implemented by the FB, since they require FB-centered attractors with circuit motifs for shifting the bump, similar to those found in the EB-PB attractor, which we see no evidence for in the FB network. (Hulse et al., 2021)" There is clearly the possibility that the fly connectome has missed footprints of such a circuit, or that ants and bees contain circuits that flies are lacking. This should be made explicit in the paper, to not give the impression that FB ring attractors have been found.

3) In line with comment 2, the model might be better called biologically inspired or plausible rather than realistic, simply to avoid that readers take the model as biological reality.

4) The authors introduce the odor input to the model by stating that odors reach the CX via known pathways, which can be swapped out for the visual inputs. This implies that processing is similar in these pathways and that it is indeed sensory information that reaches the CX. However, for olfactory information, the downstream targets of the lateral horn are not well described and, to my knowledge, do not include any CX neurons. Secondly, the output neurons of the MB are no longer sensory, but encode stimulus valence. The equivalence suggested by the text and implied in the model, is thus not biologically realistic. These simplifications should be more explicit in the text.

5) The pathway described for wind processing seems not fully correct (line 112). The AMMC is the target region of the antennal sensory neurons. Their targets then project to the wedge, from where neurons connect to the LAL and CX. In the text, the order is wedge first, then AMMC, LAL and CX. Please re-check and rephrase.

6) As the authors mention in Discussion, there are known to be direct connections from the MB to the LAL that likely mediate learned odor attraction/avoidance. This is in addition to connections to motor centers from pathways originating in the lateral horn that likely help with navigation behaviors triggered by innate odor preference. Is it the authors belief that all chemotaxis would go through the CX, as they appear to be suggesting in this integrated model (e.g., in lines 101-102)? Why? This needs to be much better motivated and discussed, particularly because Drosophila larvae, which are mentioned frequently in this study, do not even have what we would think of as a CX, and yet seem to perform pure chemotaxis much like the model agent does.

7) It's true that the WPN neurons do feed into the NO and then the FB, as the authors assume. However, the WPN neuron is also an input to the ER (ring) neurons that innervate the ellipsoid body and connect to the compass/HD system (Hulse et al., 2020). That is, wind direction is not just a self-motion cue, but is something that the HD system can directly tether to and that can help the compass integrate multiple sensory cues through plasticity in the EB. This merits some discussion, if not being added to the model, because it may affect how exactly the copy-and-shift mechanism should work with and without wind. This is also related to the switch between the first and current paper when it comes to model implementations: assuming a single "global" compass here versus assuming two different compass references in the previous model.

8) It would help if the figures, figure legends and Results are made to be more self-explanatory rather than requiring the reader to repeatedly refer to the earlier paper.
