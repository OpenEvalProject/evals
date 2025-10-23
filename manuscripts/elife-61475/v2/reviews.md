# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61475.sa0](https://doi.org/10.7554/eLife.61475.sa0)

Clemens et al. present a computational model of the cricket song recognition network, which they show is capable of reasonably reproducing neural activity and song selectivity in G. bimaculatus. They then explore the parameter space of this network and find that varying parameters of model cells enable it to produce a range of selectivities for the period, pulse duration, duty cycle, or pause duration of input song. They then identify the network parameters that most affect song selectivity and investigate the relationship between several subsets of parameters and song preference. This is a fascinating exploration of the computational flexibility of a small neural circuit; it is well researched and written and was enjoyable to read.


---

# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61475.sa1](https://doi.org/10.7554/eLife.61475.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "A small, computationally flexible network produces the phenotypic diversity of song recognition in crickets" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ann Kennedy (Reviewer #1); Barbara Webb (Reviewer #2); Martin Paul Nawrot (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Clemens et al., present a computational model of the cricket song recognition network, which they show is capable of reasonably reproducing neural activity and song selectivity in G. bimaculatus. They then explore the parameter space of this network and find that varying parameters of model cells enable it to produce a range of selectivities for the period, pulse duration, duty cycle, or pause duration of input song. They then identify the network parameters that most affect song selectivity and investigate the relationship between several subsets of parameters and song preference. This is a fascinating exploration of the computational flexibility of a small neural circuit; it is well researched and written and was enjoyable to read.

Essential Revisions:

There were several concerns that must be addressed before the paper can be accepted.; including justification/discussion of the generality (beyond crickets) of the insights gained.

1. Explanation of the core principle of function is not clear, particularly as it relates to whether the filter properties in the model have some plausible biophysical counterpart. The authors must present a knowledgeable discussion of the biophysical mechanisms that could generate the described filter functions particularly the seemingly long delays in the linear filter shapes.

2. The use of LN2 output instead of AN1 output for neurons downstream of AN1 seems like an unnecessary kluge and could have affected the results. "For simplicity and since AN1 and LN2 produce similar responses, we used the output of LN2_M in lieu of AN1_M responses for all neurons postsynaptic to AN1_M". How is it simpler? It sounds like a mistake in constructing the model. It could strongly affect the results, e.g. by making the excitatory and inhibitory inputs to LN4 more similar, as both are derived from LN2, instead of excitation from AN1 and inhibition from LN2.This should be fixed and the model reassessed.

Along the same lines the authors should discuss how they would translate the network output into behavioral output. Currently they seemingly compare behavioral response fields with their network output response field – there was considerable confusion about Figure 1B – but this has not been fully explained.

3. Several of the results in this paper, such as the anti-diagonal bands in Figure 3 and Figure 4b, seem to be a consequence of the fact that all simulated pulse trains had a fixed duration of 140ms. Is it reasonable to assume that pulse trains would have such a precisely fixed duration? Is LN4 also selective for pulse trains of a specific duration? If there isn't data on this, it would be an interesting thing to test with the model: if the input pulse train has one extra pulse or one fewer pulse, how are model LN4 responses affected? Does the model predict a preferred pulse train duration, or could it be the case that (for instance) longer pulse trains always lead to stronger LN4 activation?

Along the same lines, a cricket song consists of pulse-pause patterns, which are grouped within chirps that are separated by chirp pauses. The present paper ignores this and refers to the pulse-pause pattern filtering as 'song recognition'. This concern relates how the model would perform for an extra pulse.

4. One of the biggest discrepancies between data and model is the LN5 response at longer periods/pause durations (Figure 2b). Is it possible for the authors to comment on how this discrepancy might impact their other findings in the paper?

5. The distribution of model tolerances in Figure 4d seems surprising. It seems to suggest that the four categories of tolerances (period/duration/duty cycle/pause) do not correspond to distinct categories of models, but rather that the tolerance axis can take essentially any orientation. Is this true of other cricket species as well? If so, might it be that dividing tolerant axes into these four categories is misleading, in that it imposes discrete categories onto what is really a continuously varying signal?

6. We wonder how reasonable it is to describe all models as having a narrow "selective" axis and a broad "tolerant" axis as depicted in 4A. Among generated models where LN4m was responsive, was the LN4m response field always reasonably fit by a single ellipse, or did any models have more complex response fields?

7. The authors should discuss the previously described behavioral inter-individual variability within the species bimacultus in relation to the inter-species variability, which they cover with their parameter distributions.

These major points are further explained in the individual reviewsReviewer #1:

Clemens et al., present a computational model of the cricket song recognition network, which they show is capable of reasonably reproducing neural activity and song selectivity in G. bimaculatus. They then explore the parameter space of this network, and find that varying parameters of model cells enable it to produce a tremendous range of selectivities for the period, pulse duration, duty cycle, or pause duration of input song. They then identify the network parameters that most affect song selectivity, and investigate the relationship between several subsets of parameters and song preference. This is a fantastic exploration of the computational flexibility of a small neural circuit; it is very well researched and written, and was enjoyable to read. Although I had a few questions about the paper contents (see below), I believe that all of these can be addressed by the authors, upon which I would warmly recommend this paper for publication in eLife.

1) Several of the results in this paper, such as the anti-diagonal bands in Figure 3 and Figure 4b, seem to be a consequence of the fact that all simulated pulse trains had a fixed duration of 140ms. Is it reasonable to assume that pulse trains would have such a precisely fixed duration? Is LN4 also selective for pulse trains of a specific duration? If there isn't data on this, it would be an interesting thing to test with the model: if the input pulse train has one extra pulse or one fewer pulse, how are model LN4 responses affected? Does the model predict a preferred pulse train duration, or could it be the case that (for instance) longer pulse trains always lead to stronger LN4 activation?

2) Because of the number of layers and nonlinearities in this model, it is hard to picture what is happening under the hood to give rise to preferences for a particular period, duration, duty cycle, or pause in Figure 4. I found Figure 3 to be very helpful for the example of G. bimaculatus- would it be possible to generate similar plots for some of the models from Figure 4e, for comparison?

3) I was a bit surprised by the distribution of model tolerances in Figure 4d. This seems to suggest that the four categories of tolerances (period/duration/duty cycle/pause) do not correspond to distinct categories of models, but rather that the tolerance axis can take essentially any orientation. Is this true of cricket species as well? If so, might it be that dividing tolerant axes into these four categories is misleading, in that it imposes discrete categories onto what is really a continuously varying value?

4) On a related note, I found myself wondering how reasonable it is to describe all models as having a narrow "selective" axis and a broad "tolerant" axis as depicted in 4A. Among generated models where LN4m was responsive, was the LN4m response field always reasonably fit by a single ellipse, or did any models have more complex response fields? In addition to the orientation and preference of the selective axis, is there anything to be learned from looking at the width of the tolerant/selective axes, or the preference range of the tolerant axis?

5) One of the biggest discrepancies between data and model is the LN5 response at longer periods/pause durations (Figure 2b). Is it possible for the authors to comment on how this discrepancy might impact their other findings in the paper?Reviewer #2:

This paper contributes an interesting study of how parameter variation in a five-neuron network, closely based on identified neurons in the cricket, can establish different temporal tuning properties. The main application is to cricket song recognition; although the paper argues for more general insight into temporal recognition circuits, this is somewhat limited. Similarly, the argument for evolutionary relevance, as explaining how the diversity of cricket song might arise, would be more strongly supported either by showing potential 'pathways' of divergence (ideally through co-evolution models of production and recognition) or a clearer link from the model components to plausible biophysical mechanisms that could produce the relevant properties (e.g. specific filter shapes, especially where these are assumed to be comprised of multiple components within one neuron). As such, though the work is sound, it is of somewhat narrow interest.

Main contributions: the context of the work is that evolution of sensory preferences has been well explored at receptor level, but not yet for more complex stimulus properties, for which more sophisticated neural processing is needed to identify the preferred property in the signal. The main result of the paper is that different song preferences, as found across cricket species, can be obtained for different parameter settings within the same circuit, with biases in the frequency of preference types that match phenotypic diversity. The specific parameters/neural properties that produce qualitative differences in tuning (preference for period, duration or duty-cycle) are examined in more detail to provide some mechanistic insight into the circuit. This is approached in a very thorough manner, e.g., looking at each neuron's contribution and carrying out a full exploration followed by a sensitivity analysis to focus on the most important properties, and as such is of also of interest from a purely methodological point of view in neural modelling.

Substantive concerns:

1) As someone familiar both with cricket song recognition research and neural modelling, I had to work very hard to understand the circuit function from the presented description. The paper seems to assume the reader has very close familiarity with the papers by Kostarakos and Hedwig, 2012 and Schöneich et al., 2015 rather than giving a sufficiently clear account. E.g. in the introduction, the key concept is described as coincidence detection of delayed original input (AN1) and a "post-inhibitory rebound driven by the end of each sound pulse (LN5)". On the face of it, this seems to be a mechanism for pulse duration tuning, not period tuning, and it is unclear why "feature detector neuron LN4 integrates excitatory input from LN3 and inhibitory input from LN2, …sharpens its selectivity." From close inspection Figure 2, the mechanism for period selectivity appears to be 1) the timing of the rebound from LN5 from one syllable coincides with the onset of the next syllable 2) the response per syllable without this input decays for repeated syllables, and is further reduced in LN4 by inhibition with the same pattern as AN1. To some extent these phenomena are discussed later in the paper with reference to the effects of specific parameters, e.g. to increase the duration of the rebound from LN5; but it is difficult for the reader to follow without having the initial conceptual understanding of the original model.

2) The model seems relatively complex (multiple, somewhat arbitrarily chosen filters for each neuron, many parameters) and there is no discussion of whether it could be simplified while retaining the flexibility to be tuned to different song properties. Nor does the reader gain much insight into whether the parameters causing particular effects are plausible, or what might be the biophysical basis (this is discussed only for time delay variables) that could be subject to genetic modification.

3) The argument for insight into evolution from close examination of this network is not very convincing. Why would the existing network in one species be the "mother network" for other species? In the introduction, it is argued that "song recognition networks must be selective and modifiable to adapt to changing signal patterns" but the evolutionary drive seems more likely to be the opposite – the song should adapt to the recognition. Discussion of the co-evolution of production and recognition is very limited.Reviewer #3:

This model study nicely and exemplarily describes how, in a sensory system with highly limited neuronal resources, a small generic network with 5 neuron types can flexibly generate a variety of tuning properties, allowing for species-specific auditory mate-recognition. Building on their previous body of works, the authors here employ a phenomenological (i.e. non-mechanistic) rate-based feed-forward circuit model, fitted to accommodate known single-neuron input/output features. The model faithfully predicts the animals' (average) response behavior to parametrically controlled sensory stimuli. Targeted parameter modifications can tune the network for different auditory pulse patterns. The authors argue that such a flexible generic network motive could allow for evolutionary fast species separation.

1) The authors state "The neuronal circuit … has been revealed p.4 …". However, is there clear anatomic evidence for the explicit network wiring of 5 neurons and 6 connections? Does each of these neurons exist only once per hemisphere of any individual or are the authors referring to neuron types? Clear evidence should be referenced or missing evidence should be critically discussed.

2) The authors present a purely phenomenological model. How are these computations implemented biophysically? Which synaptic, cellular and network mechanisms are involved? Discussion of possible mechanisms and references to relevant works seems mandatory, in particular with respect to the (long) delays / rebound delay in the causal filters and the divisive normalization. Discussing adaptation for type AN1 and LN1 by means of either SFA (Nagel and Wilson, 2011, Nat Neurosci 14(2); Farkhooi et al., 2013, PLoS CB 9(10); Benda et al., 2003,2008) or short-term depressing synapses is straightforward. The phenomenological rate model has its own value. However, the argument that the authors did not aim at a biophysical implementation because ion channels and conductances are not known is not a good argument, this would have prevented 95% of published model studies.

3) The authors repeatedly refer to "song-recognition". However, the authors only investigate pulse sequences (Figure 1B) neglecting the impact of chirp tuning (e.g. Grobe et al., 2012, JEB 2015; Meckenhäuser et al., 2013, PloS one, 8; Clemens and Hennig, 2013). This needs to be discussed.

4) The authors argue their model "has the capacity to reproduce the behavioral preferences" (p.8) with reference to behavioral tuning in Figure 1B. They should make explicit that this refers to the congruence of the LN4 response field (Figure 3) and behavioral response field (Figure 1B) for G. bimaculatus; no attempt was made to explicitly model behavioral output. How could behavior be generated? What is the typical delay between song onset and behavioral response? What is known about the behavioral decision circuit? Please discuss possible mechanisms of behavioral decision making such as the previously suggested drift diffusion models (Hennig et al., 2014, Front. Physiol 5; Clemens et al., 2014, PNAS 11; Meckenhäuser et al., 2014, Front. Sys. Neurosci 8) and possible others?

5) Inter vs. intra-species variability. To my knowledge there is large inter-individual variability in female G.bimaculatus behavior (Grobe et al., 2012, Meckenhäuser et al., 2013) and the authors sate tenfold neuron parameter variation within species. However, they model only an average animal and do not mention behavioral variability at all. How could parameter variation for inter-individual variability in their network differ from inter-species variability? This should be discussed.

6) What is the critical test for the existence of a 'multi-purpose' circuit across species? Do the authors expect the same basic network topology across species and did they attempt to identify it (anatomically) in any species other than G. bimaculatus? Can they think of other methods of validation? This should be addressed in the Discussion.

7) Authors briefly mention various song preference patterns across species. It would be great to see specific examples of song patterns for a few species along with matching model tuning, e.g. in a supplemental figure, possibly together behavioral date / response diagrams.

8) The core result on multi-species covered in Figure 4 and text indicates all four "principal types" of response fields can be achieved by the model with reference to Figure 1B. Where does Figure 1B come from? Are we looking at sketches? Or behavioral response fields measured in crickets? Please make this clear and give references to the underlying data. Clemens and Hennig 2013 and Hennig et al., 2014 do not show these graphs. Ideally, the authors can reproduce exemplary experimental data from diverse cricket species for illustration.
