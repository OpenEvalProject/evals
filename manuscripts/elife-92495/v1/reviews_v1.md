# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92495.3.sa0](https://doi.org/10.7554/eLife.92495.3.sa0)

This important study proposes a new method for tracking neurons recorded with Neuropixel electrodes across days. The methods and the strength of the evidence are convincing, but the authors do not address whether their approach can be generalized to other brain areas, species, behaviors, or tools. Overall, this method will be potentially of interest to many neuroscientists who want to study long-term activity changes of individual neurons in the brain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92495.3.sa1](https://doi.org/10.7554/eLife.92495.3.sa1)

Neurons are not static-their activity patterns change as the result of learning, aging, and disease. Reliable tracking of activity from individual neurons across long time periods would enable studies of these important dynamics. For this reason, the authors' efforts to track electrophysiological activity across days without relying on matching neural receptive fields (which can change due to learning, aging, and disease) is very important.

By utilizing the tightly-spaced electrodes on Neuropixels probes, they are able to measure the physical distance and the waveform shape 'distance' between sorted units recorded on different days. To tune the matching algorithm and to validate the results, they used the visual receptive fields of neurons in the mouse visual cortex (which tend to change little over time) as ground truth. Their approach performs quite well, with a high proportion of neurons accurately matched across multiple weeks.

This suggests that the method may be useable in other cases where the receptive fields can't be used as ground truth to validate the tracking. This potential extendibility to tougher applications is where this approach holds the most promise. However, the study only looks at one brain area (visual cortex), in one species (mouse), using one type of spike sorter (Kilosort), and one type of behavioral prep (head-fixed). While the authors suggest methods to generalize their technique to other experimental conditions, no validation of those generalizations was done using data from different experimental conditions. Anyone using this method under different conditions would therefore need to perform such validation themselves.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92495.3.sa2](https://doi.org/10.7554/eLife.92495.3.sa2)

The manuscript presents a method for tracking neurons recorded with neuropixels across days, based on the matching of cells' spatial layouts and spike waveforms at the population level. The method is tested on neuropixel recordings of the visual cortex carried over 47 days, with the similarity in visual receptive fields used to verify the matches in cell identity.

This is an important tool as electrophysiological recordings have been notoriously limited in terms of tracking individual neuron's fate over time, unlike imaging approaches. The method is generally sound and properly tested but I think some clarifications would be helpful regarding the implementation of the method and some of the results.

(1) Page 6: I am not sure I understand the point of the imposed drift and how the value of 12µm is chosen.

Is it that various values of imposed drift are tried, the EMDs computed to produce histograms as in Fig2c, values of rigid drifts estimated based on the histogram modes, and then the value associated with minimum cost selected? The corresponding manuscript section would need some clarification regarding this aspect.

(2) The EMD is based on the linear sum, with identical weight, of cell distance and waveform similarity measures. How performance is affected from using a different weighting of the 2 measures (for instance, using only cell distance and no waveform similarity)? It is common that spike waveforms associated to a given neuron appear different on different channels of silicon probes (i.e. the spike waveform changes depending the position of recording sites relative to the neuron), so I wonder if that feature is helping or potentially impeding the tracking.

(3) Fig.5: I assume the dots are representing time gaps for which cell tracking is estimated. The 3 different groups of colors correspond to the 3 mice used. For a given mouse, I would expect to always see 3 dots (for ref, putative and mixed) for a given tracking gap. However, for mouse AL036 for instance, at tracking duration of 8 days, a dot is visible for mixed but not for ref and putative. How come this is happening?

(4) Matched visual responses are measured by the sum of correlation of visual fingerprints, which are vectors of cells' average firing rate across visual stimuli, and correlation of PSTHs, which are implemented over all visual stimuli combined. I believe that some information is lost from combining all stimuli in the implementation of PSTHs (assuming that PSTHs show specificity to individual visual stimuli). The authors might consider, as alternative measure of matched visual responses, a correlation of the vector concatenations of all stimulus PSTHs. Such simpler measure would contain both visual fingerprint and PSTH information, and would not lose the information of PSTH specificity across visual stimuli.

2nd revision

(1) From reading the authors' response, I could understand several of the points I had previously missed. I still think that some part of the results are not straightforward to understand, the way it is written. Adding a few introductory sentences to the paragraphs (for instance the one related to my previous point #1) would really help the reader comprehend this important work.

(2) Following on my point #2, the w value used is 1500 and the recovery rate doesn't seems to reach a peak but rather a plateau for larger w values. From such large w value and the absence of a downward trend for increasing values, it would seem that only the 'waveform distance' matter and that the 'location distance' doesn't contribute much to the EMD distance. Is this correct?
