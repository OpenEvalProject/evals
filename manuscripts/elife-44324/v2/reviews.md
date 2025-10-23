# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- Emilio Salinas, Wake Forest School of Medicine United States

## Review text

DOI: [10.7554/eLife.44324.011](https://doi.org/10.7554/eLife.44324.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Fast and flexible sequence induction in spiking neural networks via rapid excitability changes" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Emilio Salinas as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript investigates, via computer simulations, the functional consequences of a physiological phenomenon known as long-term potentiation of intrinsic excitability (LTP-IE), whereby neurons that fire intensely (due to input S) for a short period of time then respond more strongly to subsequent input (from a different source G). This mechanism is important for several reasons: 1) reports of LTP-IE show a two-fold magnitude increase in EPSPs, substantially higher than what is reported for STDP, and 2) as the authors demonstrate, it can quickly generate highly effective, transient communication channels that may mediate cognitive flexibility. The computer simulations show that this mechanism can explain the replay of place cell responses observed in the hippocampus; specifically, the fact that such activation sequences can replay in forward or reverse order, and over a compressed time scale. More generally, this mechanism is also shown to allow the reactivation of arbitrary response sequences for cells embedded within a recurrent network.

The introduction of intrinsic plasticity concepts to the analysis of population sequences is highly innovative and quite interesting. Although the model has limitations, it represents a feasible and simple mechanism that could underlie hippocampal replay events, and it has other, more general implications. The manuscript is interesting, even provocative, and will certainly enrich the field.

Essential revisions:

The paper requires some updates with regard to the discussion of previous findings by other labs, and some clarification to maximize its impact.

1) Is LTP-IE-time-restricted in the model, or is it assumed to be long-lasting? This is an important question for two reasons. First, because of intersecting trajectories, which could substantially limit the proposed model. The model proficiently generates simple trajectories, such as ABCDE…, but in naturalistic environments (such as open field) there is replay of complex sequences, such as ABCDAEFG. Second, a similar issue arises when the trajectory inducing LTP-IE is very long, as this model would facilitate replays of any length.

The authors should consider some evidence showing that LTP-IE might be time-limited, see e.g. Pignatelli et al., 2019, which would reduce the impact of both of these concerns.

2) Explaining the replay of complex sequences, as mentioned above, would be a major contribution to the field, but it is not clear whether the model can generate those or not. There are many proposed models of reactivation of simple sequences, but none (as far as I know) for reactivation of complex/realistic sequences. While the authors are commended for proposing a new biophysical mechanism for explaining replay, this a moderate contribution to the field. What would be really exciting would be a model such as the one they propose that goes beyond the kind of simple sequences typically found in hippocampus studies with rodents running on linear tracks.

3) Discussion, last paragraph and elsewhere: the authors clearly state that their model works in the absence of synaptic modification, in fact this is one of the major points. This idea (that intrinsic plasticity can act based on existing, but not changing synaptic connectivity) has been presented by other groups before and this prior work should be cited and discussed in appropriate detail.

For instance, previous modeling work (Salinas, 2004; Salinas, 2004) showed that changes in excitability very similar to those proposed here, in which one input modulates the response to another, are ideal for switching a network from one functional configuration (say, sensory-motor map 1) to another (say, sensory-motor map 2). Although the changes in excitability in that earlier work went by a different name, "gain modulation", the underlying mathematics would still apply, so discussing those earlier findings would bolster the argument that LTP-IE could indeed be computationally effective for the sorts of remapping proposed in this manuscript.

The work also needs to be discussed in the context of Moshe Abeles' neuronal avalanche concept (despite its stronger focus on the neocortex).

In the context of LTP-IE, it might be interesting to discuss a recent finding that spike firing can be independent of dendritic EPSP amplitudes, and is instead intrinsically controlled, see Ohtsuki and Hansel, 2018.

4) The authors state that 'this mechanism….is observed in hippocampus only'. If this statement refers to LTP-IE, it is not correct, see e.g. Daoudal, Hanada and Debanne, 2002. Debanne's work should also be cited with regard to STDP. If the statement does not refer to LTP-IE, this needs to be stated more precisely.

5) Given the co-occurrence of replay and sharp-wave ripples, the lack of inhibition in the current model may be a substantial limitation. Replay was triggered using depolarizing current, however the physiological relevance of the model would be bolstered if replay could be triggered by a sharp-wave ripple event in an inhibitory population. More broadly, how does the model behave if one were to add inhibition in addition to excitation?

6) Related to the above point, it was difficult to evaluate the robustness of the model. There are many parameters, but which ones are more critical for the results, and what is the 'operating range' of the model? Is the model robust to small perturbations in parameters?

7) Regarding Figure 4, it is unclear where in the brain a recurrent sensorimotor network with LTP-IE might exist to support the generation of transient associations using the proposed mechanism. What do the authors suggest is the biophysical substrate for non-spatial transient associations?

8) Some parts of the manuscript were found to be somewhat technical and difficult to follow. Specifically, throughout the Results: second paragraph; subsection “LTPIE increases membrane voltages and spike rates under random gating inputs”, first and last paragraphs; subsection “Spike sequences propagate along LTP-IE-defined paths through a network”, second paragraph; subsection “Dependence of LTP-IE-based sequence propagation on network parameters”, first paragraph and subsection “LTP-IE-based sequences can encode temporary stimulus response mappings”, last paragraph. The Results should be more accessible to a broader readership not specialized in computational neuroscience.

For instance, it is not easy to understand how the results in Figure 2 relate to, and emerge from, those in Figure 1. In general, it would be useful if the authors could better explain the relationship between their neuronal mechanism and the results.

In addition, while the model works well for encoding spatial trajectories in which the closeness of individual locations is pre-encoded in the recurrent connectivity weights, it is difficult to see how this would extend to the given example of cognitive flexibility (i.e., raising our right hand when a particular word is heard, and the left hand when a different word is heard), particularly if no a priori spatial relationship exists. Are spatial relationships necessary? There is no evidence provided to suggest that the neocortical network has the necessary architecture to support LTP-IE based replay.
