# Peer review - Round 1

Editors:
- Martin Vinck, Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67171.sa1](https://doi.org/10.7554/eLife.67171.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

One of the major challenges of cortical circuits is to learn associations between events that are separated by long time periods, given that spike-timing-dependent plasticity operates on short time scales. In the Hippocampus, a structure critical for memory formation, phase precession is known to compress the sequential activation of place fields to the theta-cycle (~8Hz) time period. Reifenstein et al., describe a simple yet elegant mathematical principle through which theta phase precession contributes to learning the sequential order by which place fields are activated.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Synaptic learning rules for sequence learning" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Martin Vinck as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Francesco P Battaglia (Reviewer #2); Frances Chance (Reviewer #4).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. However, eLife would welcome a substantially improved manuscript that addresses concerns raised; this would be treated as a new submission, but likely go to the same reviewers.

The reviewers acknowledged that the study addresses an important topic. They also applauded the rigor and elegance of the analytical approach. However, reviewers individually, and in subsequent discussion, expressed the concern that the physiological relevance of the findings is far from clear; this point would require a substantial amount of new simulations and models. They furthermore commented that the generation and storage of sequences remains unclear, again requiring substantial additions to the manuscript. Reviewers therefore recommended that, at present, the manuscript appears to be more suited for a more specialized journal.

Reviewer #1:

This paper develops a model of the way in which phase precession modulates synaptic plasticity. The idea and derivations are simple and easy to follow. The results, while not surprising, are overall interesting and important for researchers on phase precession and sequence learning. There are some useful analytical approximations in the paper. I have several comments:

1. The paper is all based on pairwise STDP.

How robust are these results when we consider perhaps more realistic STDP rules like triplet STDP? Perhaps this is something to discuss or explore, because it is not a priori obvious to me.

2. What are the widths reported in the literature for hippocampus? With all the recent literature on the dependence of STDP in vitro on Ca2+ levels, one has to take this with a grain of salt of course. I would think it's around 100ms which would make the benefit small?

3. The approximation of theta as an oscillator that shows no dampening is of course not realistic; in reality autocorrelation functions will show decreasing sidelobes. It's maybe not a problem, but could actually benefit your model.

4. To say that phase precession benefits sequence learning is maybe not the whole story. It seems that in general long STDP kernels benefit sequence learning for place fields, and they do this equally well for phase or no phase precession. If the STDP kernels are short, sequence learning is more difficult (and requires huge place field overlap), and phase precession is beneficial for that.

How does benefit interact with place field overlap? If the place fields are highly overlapping, then how does STDP kernel size regulate the sequence learning? Are longer STDP kernels invariantly better for sequence learning in the hippocampus? Or does this depend on place field separation. In other words are there are some scenarios where short STDP kernels have a clear benefit and where phase precession then gives a huge boost?

Reviewer #2:

Reifenstein and Kempter propose an analytical formulation for synaptic plasticity dynamics with STDP and phase precession as observed in hippocampal place cells.

The main result is that phase precession increases the slope of the 2-cell cross-correlation around the origin, which is the key driver of plasticity under asymmetric STDP, therefore improving the encoding of sequences in the synaptic matrix.

While the overall concept of phase precession favoring time compression of sequences and plasticity (when combined with STDP) has been present in the literature since the seminal Skaggs and McNaughton, 1996 paper, the novel contribution of this study is the elegant analytical formulation of the effect, which can be very useful to embed this effect into a network model. As a suggestion of a further direction, one could look at models (e.g. Tsodyks et al., Hippocampus, 1996) where asymmetries in synaptic connections are driver for phase precession. One could use this formulation for e.g. seeing how experience may induce phase precessing place field by shaping synaptic connections (maybe starting from a small symmetry breaking term in the initial condition).

The analytical calculation seems crystal clear to me (and quite simple, once one finds the right framework)

Reviewer #3:

The study uses analytical and numerical approaches to quantify conditions in which spike timing-dependent plasticity (STDP) and theta phase precession may promote sequence learning. The strengths of the study are that the question is of general interest and the analytical approach, in so far as it can be applied, is quite rigorous. The weaknesses are that the extent to which the conclusions would hold in more physiological scenarios is not considered, and that the study does not investigate sequences but rather the strength of synaptic connections between sequentially activated neurons.

1. While the stated focus in on sequences, the key results are based on measures of synaptic weight between sequentially activated neurons. Given the claims of the study, a more relevant readout might be generation of sequences by the trained network.

2. The target network appears very simple. Assuming it can generate sequences, it's unclear whether the training rule would function under physiologically relevant conditions. For example, can the network trained in this way store multiple sequences? To what extent do sequences interfere with one another?

3. In a behaving animal movement speed varies considerably, with the consequence that the time taken to cross a place field may vary by an order of magnitude. I think it's important to consider the implications that this might have for the results.

4. Phase precession, STDP and sequence learning have been considered in previous work (e.g. Sato and Yamaguchi, Neural Computation, 2003; Shen et al., Advances in Cognitive Neurodynamics ICCN, 2007; Masquelier et al., J. Neurosci. 2009; Chadwick et al., eLife 2016). These previous approaches differ to various degrees from the present work, but each offers alternative suggestions for how STDP and phase precession could interact during memory. It's not clear what the advantages are of the framework proposed here.

5. While theta sequences are the focus of the introduction, many of the same arguments could be applied to compressed representations during sharp wave ripple events. This may be worth considering. Also, given the model involves excitatory connections between neurons that represent sequences, the relevance here may be more to CA3 were such connectivity is more common, rather than CA1 which is the focus of many of the studies cited in the introduction.

Reviewer #4:

This manuscript argues that phase precession enhances the learning of sequence learning by compressing a slower behavioral sequence, for example movement of an animal through a sequence of place fields, into a faster time scales associated with synaptic plasticity. The authors examine the synaptic weight change between pairs of neurons encoding different events in the behavioral sequence and find that phase precession enhances sequence learning when the learning rule is asymmetric over a relatively narrow time window (assuming the behavioral events encoded by the two neurons overlap, ie the place fields of the neurons overlap). For wider time windows, however, phase precession does not appear to convey any advantage.

I thought the study was interesting – the idea that phase precession "compresses" sequences into theta cycles has been around for a bit, but this is the first study that I've seen that does analysis at this level. I think many researchers who are interested in temporal coding would find the work very interesting.

I did, however, have a little trouble understanding what conclusions the study draws about the brain (if we are supposed to draw any). The authors conclude that phase precession facilitates if the learning window is shorter than a theta cycle – that seems in line with published STDPs rules from slice studies. However, Figure 4 seems to imply that the authors have recovered a 1 second learning window from Bittner's data – are they suggesting that phase precession is not an asset for the learning in that study (or did I miss something)? Are there predictions to be made about how place fields must be spaced for optimal sequence learning?

Also, I'd be curious to know how the authors analysis fits in with replay – is the assumption that neuromodulation is changing the time window or other learning dynamics?
