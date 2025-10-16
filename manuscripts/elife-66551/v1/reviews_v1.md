# Peer review - Round 1

Editors:
- Sachin Deshmukh, Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66551.sa1](https://doi.org/10.7554/eLife.66551.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Frey et al. describe a convolutional neural network capable of extracting behavioral correlates from wide-band LFP recordings or even lower-frequency imaging data. The analysis program described by the authors provides a rapid "first pass" analysis using raw, unprocessed data to generate hypotheses that can be tested later with conventional in-depth analyses. This approach is of real value to the community, particularly as it becomes more commonplace for labs to acquire multi-site in vivo recordings.

Decision letter after peer review:

Thank you for submitting your article "Interpreting wide-band neural activity using convolutional neural networks" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers agree that the tools and resources described in the manuscript are a substantial contribution to the field, but have raised a number of concerns which need to be addressed. The requested changes do not require any new data, but do require new analyses to be performed. Complete reviewer recommendations are appended at the end of this message, and a summary of essential revisions follows.

Essential revisions:

1) The CNN described in the manuscript needs to be better characterized in terms of its history dependence, comparison to Bayesian decoding, and ability to decode non-local representations. Head direction decoding using CNN needs to be compared with that using a Bayesian decoder.

2) The ability of the CNN to discover underlying truth needs to be characterized using simulations.

3) Contributions of low frequency activity need to be better distinguished from the low frequency components of excitatory spikes.

4) The amount of data required for accurately recovering the frequency bands contributing to decoding needs to be characterized using simulations as well as sub-sampled data. Relative contributions of using the Wavelet coefficients as inputs and the CNN to improved accuracy also need to be characterized.

Reviewer #1 (Recommendations for the authors):

In the current manuscript, Frey et al. describe a convolutional neural network capable of extracting behavioral correlates from wide-band LFP recordings or even lower-frequency imaging data. Other publications (referenced by the authors) have employed similar ideas previously, but to my knowledge, the current implementation is novel. In my opinion, the real value of this method, as the authors state in their final paragraph, is that it represents a rapid, "first-pass" analysis of large-scale electrophysiological recordings to quickly identify relevant neural features which can then become the focus of more in-depth analyses. As such, I think the analysis program described by the authors is of real value to the community, particularly as it becomes more commonplace for labs to acquire multi-site in vivo recordings.

However, to maximize its utility to the community, I have several questions/concerns that I believe need to be addressed.

(1) It is obviously important to quantify the relative accuracy of the authors' method to existing methods which correlate neural activity to behavior or sensory input. The authors attempt to do this by comparing CNN decoding to Bayesian decoding with clustered cells (Figure 1). However, I think there are several points where that comparison may be flawed.

(1a) First, while some manuscripts (including Zhang et al., 1998, referenced by the authors) do use a continuity prior in their decoding algorithms, most do not (see the vast array of papers from Matt Wilson, David Redish, Loren Frank, David Foster, and others in the field). Indeed, even Olafsdottir et al., 2015 that the authors reference in apparent support of the use of a continuity prior (Line 111 of the manuscript) explicitly state that they do not use a continuity prior in their methods. It is unclear to me in reading through the methods whether the CNN-based decoding also utilizes a continuity prior to restrict the decoded location.

To truly be a useful tool to the community, the algorithm should be capable of correlating neural activity to behaviors/sensory input in a manner that is history-independent, as it seems that a fundamental advantage of this system is for unbiased probing of such correlations. If such history-independent decoding is not possible with the CNN, this should be explicitly stated to clarify the parameters for which this method is appropriate.

Thus, I would like clarification of whether the CNN uses the animal's history to constrain its decoding output. If so, is the use of the animal's history a necessary component of the CNN-based decoding? If the CNN can be used in a history-independent manner, I would like to see it compared to history-independent Bayesian decoding.

(1b) The authors report that part of the advantage of the CNN over Bayesian decoding was that the CNN made fewer large errors, and that the median error was more similar across the two methods (Line 120). When performing the Bayesian decoding, it appears as though spikes throughout the entire experiment were used. However, it is known that during periods of immobility, population bursts during sharp-wave/ripples can encode virtual trajectories across the environment, producing non-local spatial representations. If such remote trajectories were included in the Bayesian decoding, this may account for large "errors" between the decoded location and the animal's actual location (even though this may not be an error at all!). Thus, I would like to see this comparison repeated using only periods of active movement, when the literature suggests that place cells are more likely to encode local spatial information.

In addition, it appears that the authors use a 500 ms window to quantify Bayesian decoding accuracy, but, from what I can tell, they use a ~33 ms window (within 2 second 'chunks') to quantify CNN decoding accuracy. This doesn't seem like a fair apples-to-apples comparison as the animal can move quite a bit over 500 ms. I would thus like to see a comparison between these two methods using similar timescales that are appropriate for both methods, perhaps a ~100-200 ms window.

(1c) Related to the previous point, a fundamental advantage of using single unit activity to examine behavioral information is that it allows the experimenter to identify when the neural population is representing information other than the immediate sensory input or behavioral output. For example, in the place cell field, one can correlate activity of single units to position during active behavior, and then study when virtual paths are encoded during hippocampal sharp-wave/ripples (a.k.a. replay) or theta sequences.

Thus, a basic question is whether such non-local representation is accessible in the authors' CNN. Can the authors train the network on behavioral data (using only periods of active movement) and then faithfully decode virtual trajectories during immobility-based ripples? Alternatively, can the authors identify the shorter theta sequences observed during active movement if the CNN operates on a finer timescale? If the position decoding is largely based on high-frequencies in the LFP representing action potentials, it seems that such finer-scale, non-local representations should also be available. Importantly, if such non-local or fine-time-scale representations cannot be identified using this method, it is important to clarify this to avoid incorrect future use.

(2) Although the majority of self-location information was present in high-frequency bands, the data in Figure 1E show that LFP frequencies below 250 Hz were also informative above chance (and very near Bayesian decoding accuracy). However, given that Figure 3B shows excitatory spikes spread well into low 200 Hz frequency ranges, it seems that using LFP below 250 Hz is likely also including some spike information. For clarification of how accurately low-frequency bands can reflect position information, I would like to see the analysis in Figure 1E performed with LFP frequencies less than 150 Hz (fast gamma and slower).

If position information can still be faithfully extracted using <150 Hz frequencies, it is important to further rule out non-spatial correlates. For example, are there spatial locations where the rat is more likely to run at predictable velocities, allowing theta-band frequencies to effectively decode the animal's location? Is the LFP-based decoding more/less accurate at specific locations of the environment (near walls, near a rewarded location, etc.)? A heat-map of average decoding error per spatial bin (per animal) would be useful to visualize this analysis.

(3) When quantifying the accuracy of head direction decoding, they compare the CNN to chance levels. Although this is a valuable measure, given that head direction seems heavily driven by LFP frequencies associated with excitatory and inhibitory spiking, can the authors also compare head direction decoding between the CNN and Bayesian decoding from clustered spikes (including both exc. and inh. cells)? Is head direction information available in the clustered data or are there other elements in the high-frequency LFP that correlate to head direction? If head direction can be decoded via clustered spikes, why do the authors think this has not been observed in prior studies?

(4) In the Methods (line 356), I'm not sure what the authors mean by "16 eight tetrodes". Do they mean 16 tetrodes?

(5) The x-axis of Figure 4D and 4H should be labeled, especially since the scale seems to be log rather than linear.

Reviewer #3 (Recommendations for the authors):

– I think this method could be very useful for the EEG/ECoG communities, which care about frequency representations, and appealing to those communities would significantly expand the utility of your method for the broader neuroscience community. In my opinion, if there is no example of this type of use in the paper, it is much less likely for EEG/ECoG researchers to actually use your method in practice. I think that having an EEG or ECoG example would be much more beneficial than the calcium imaging example, since researchers are not trying to determine what frequency contents are important within a calcium imaging signal. This has a list of many open datasets for EEG: https://github.com/meagmohit/EEG-Datasets

– I think providing a general overview of your approach/method at the beginning of Results would be helpful for many readers.

– Please clarify when you are reporting test-set vs. training set predictions in your results.

– In the final paragraph of the introduction, you write "Our model differs markedly from conventional decoding methods which typically use Bayesian estimators…" This is overly specific to hippocampal decoding – in movement decoding Bayesian methods are not frequently used, although linear methods still commonly are.
