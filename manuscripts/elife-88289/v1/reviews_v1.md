# Peer review - Round 1

Editors:
- Marla B Feller, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88289.3.sa0](https://doi.org/10.7554/eLife.88289.3.sa0)

This valuable study contributes to understanding how retinal activity shapes the response properties of excitatory and inhibitory neurons in a major visual target, the superior colliculus. The evidence supporting the claim is convincing: the work is technically excellent yet the interpretation of these results assumes an unbiased sampling and integration of the RGC axon in the SC, a caveat pointed out by the authors. Overall, this study provides insights into the integration of visual information from the eye to the brain, and this work will be of interest to visual neuroscientists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88289.3.sa1](https://doi.org/10.7554/eLife.88289.3.sa1)

Gehr and colleagues used an elegant method, using neuropixels probes, to study retinal input integration by mouse superior collicular cells in vivo. Compared to a previous report of the same group, they opto-tagged inhibitory neurons and defined the differential integration onto each group. Through these experiments, the author concluded that overall, there is no clear difference between the retina connectivity to excitatory and inhibitory superior colliculus neurons. The exception to that rule is that excitatory neurons might be driven slightly stronger than inhibitory ones. Technically, this work is performed at a high level, and the plots are beautifully conceived, but I have doubts if the interpretation given by the authors is solid. I will elaborate below.

Some thoughts about the interpretation of the results.

My main concern is the "survivor bias" of this work, which can lead to skewed conclusions. From the data set acquired, 305 connections were measured, 1/3 inhibitory and 2/3 excitatory. These connections arise from 83 RGC onto 124 RGC (I'm interpreting the axis of Fig.2 C). Here it is worth mentioning that different RGC types have different axonal diameters (Perge et al., 2009). Here the diameter is also related to the way cells relay information (max frequencies, for example). It is possible that thicker axons are easier to measure, given the larger potential changes would likely occur, and thus, selectively being picked up by the neuropixels probe. If this is the case, we would have a clear case of "survival bias", which should be tested and discussed. One way to determine if the response properties of axonal termini are from an unbiased sample is to make a rough functional characterization as generally performed (see Baden et al. 2006). This is fundamental since all other conclusions are based on unbiased sampling.

One aspect that is not clear to me is to measure of connectivity strength in Figure 2. Here it seems that connectivity strength is directly correlated with the baseline firing rate of the SC neuron (see example plots). If this is a general case, the synaptic strength can be assumed but would only differ in strength due to the excitability of the postsynaptic cell. This should be tested by plotting the correlation coefficient analysis against the baseline firing rate.

My third concern is the assessment of functional similarity in Fig. 3. It is not clear to me why the similarity value was taken by the arithmetic mean. For example, even if the responses are identical for one connected pair that exclusively responds either to the ON or OFF sparse noise, the maximal value can only be 0.67. Perhaps I misunderstood something. Secondly, correlations in natural(istic) movies can differ dramatically depending on the frame rate that the movie was acquired and the way it is displayed to the animal. What looks natural to us will elicit several artifacts at a retinal level, e.g., due to big jumps between frames (no direction-selective response) or overall little modulation (large spatial correlations). I would rather opt for uniform stimuli, as suggested previously. Of course, these are also approximations but can be easily reproduced by different labs and are not subjected to the intricacies of the detailed naturalistic stimulus used.

Fourth. It is important to control the proportion of inhibitory cells activated optogenetically across the recording probe. Currently, it is not possible to assess if there are false negatives. One way of controlling for this would be to show that the number of inhibitory interneurons doesn't vary across the probe.

Fifth. In Fig. 4, the ISI had a minimal bound of 5 ms. Why? This would cap the firing rate at 200Hz, but we know that RGC in explants can fire at higher frequencies for evoked responses. I would set a lower bound since it should come naturally from the after-depolarization block. Another aspect that remains unclear is to what extent the paired-spike ratio depends on the baseline firing rate. This would change the interpretation from the particular synaptic connection to the intrinsic properties of the cell and is plausible since the bassline firing rate varies tremendously. One related analysis would be to plot the change of PSR depending on the ISI. It would be intuitive to make a scatter plot for all paired spikes of all recorded neurons (separated into inhibitory and excitatory) of ISI vs. PSR.

Panel 4E is confusing to me. Here what is plotted is efficacy 1st against PSR (which is efficacy 2nd/efficacy 1st). Given that you have a linear relation between efficacy 1st and efficacy 2nd (panel 4C), you are essentially re-plotting the same information, which should necessarily have a hyperbolic relationship: [ f(x) = y/x ]. Thus, fitting this with a linear function makes no sense and it has to be decaying if efficacy 2nd > efficacy1st as shown in 4C.

Finally, in Figure 5, the perspective is inverted, and the spike correlations are seen from the perspective of SC neurons. Here it would also be good to plot the cumulative histograms and not look at the averages. Regarding the similarity index and use of natural stats, please see my previous comments. Also, would it be possible to plot the contribution v/s the firing rate with the baseline firing rate with no stimulation or full-field stimulation? This is important since naturalistic movies have too many correlations and dependencies that make this plot difficult to interpret.

Overall, the paper only speaks from excitatory and inhibitory differences in the introduction and results. However, it is known that there are three clear morphologically distinct classes of excitatory neurons (wide-field, narrow-field, and stellate). This topic is touched in the discussion but not directly in the context of these results. Smaller cells might likely be driven much stronger. Wide-field cells would likely not be driven by one RGC input only and will probably integrate from many more cells than 6.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88289.3.sa2](https://doi.org/10.7554/eLife.88289.3.sa2)

This study follows up on a previous study by the group (Sibille et al Nature Communications 2022) in which high density Neuropixel probes were inserted tangentially through the superficial layers of the superior colliculus (SC) to record the activity of retinocollicular axons and postsynaptic collicular neurons in anesthetized mice. By correlating spike patterns, connected pairs could be identified which allowed the authors to demonstrate that functionally similar retinal axon-SC neuron pairs were strongly connected.

In the current study, the authors use similar techniques in vGAT-ChR2 mice and add a fiber optic to identify light-activated GABAergic and non-light-activated nonGABAergic neurons. Using their previously verified techniques to identify connected pairs, within regions of optogenetic activation they identified 214 connected pairs of retinal axons and nonGABAergic neurons and 91 pairs of connected retinal axons and GABAergic neurons. The main conclusion is that retinal activity contributed more to the activity of postsynaptic nonGABAergic SC neurons than to the activity of postsynaptic GABAergic SC neurons.

The study is very well done. The figures are well laid out and clearly establish the conclusions. My main comments are related to the comparison to other circuits and further questions that might be addressed in the SC.

It is stated several times that the superior colliculus and the visual cortex are the two major brain areas for visual processing and these areas are compared throughout the manuscript. However, since both the dorsal lateral geniculate nucleus (dLGN) and SC include similar synaptic motifs, including triadic arrangements of retinal boutons with GABAergic and nonGABAergic neurons, it might be more relevant to compare and contrast retinal convergence and other features in these structures.

The GABAergic and nonGABAergic neurons showed a wide range of firing rates. It might be interesting to sort the cells by firing rates to see if they exhibit different properties. For example, since the SC contains both GABAergic interneurons and projection neurons it would be interesting to examine whether GABAergic neurons with higher firing rates exhibit narrower spikes, similar to cortical fast spiking interneurons. Similarly, it might be of interest to sort the neurons by their receptive field sizes since this is associated with different SC neuron types.

The recording techniques allowed for the identification of the distance between connected retinocollicular fibers and postsynaptic neurons. It might also be interesting to compare the properties of connected pairs recorded at dorsal versus ventral locations since neurons with different genetic identities and response properties are located in different dorsal/ventral locations (e.g. Liu et al. Neuron 2023). Also, regarding the strength of connections, previous electron microscopy studies have shown that the retinocollicular terminals differ in density and size in the dorsal/ventral dimension (e.g Carter et al JCN 1991).

Was optogenetic activation of GABAergic neurons ever paired with visual activation? It would be interesting to examine the receptive fields of the nonGABAergic neurons before and after activation of the GABAergic neurons (as in Gale and Murphy J Neurosci 2016).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88289.3.sa3](https://doi.org/10.7554/eLife.88289.3.sa3)

This study performs in vivo recordings of neurons in the mouse superior colliculus and their afferents from the retina, retinal ganglion cells (RGCs). Building on a preparation they previously published, this study adds the use of optogenetic identification of inhibitory neurons (aka optotagging) to compare RGC connectivity to excitatory and inhibitory neurons in SC. Using this approach, the authors characterize connection probability, strength, and response correlation between RGCs and their target neurons in SC, finding several differences from what is observed in the retina-thalamus-visual cortex pathway. As such, this may be a useful dataset for efforts to understand retinocollicular connectivity and computations.
