# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90327.3.sa0](https://doi.org/10.7554/eLife.90327.3.sa0)

This study develops useful tools for distinct optogenetic control of neuronal activity by red or blue light. The basic characterization of the activation of a red-shifted channelrhodopsin paired with a blue-light sensitive anion channel engineered to obtain desired inhibitory current kinetics is solid. However, evidence for their practical use under simultaneous multi-color or high frequency stimulation in cells are missing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90327.3.sa1](https://doi.org/10.7554/eLife.90327.3.sa1)

Summary

In this manuscript, the authors generate an AAV-deliverable tool that generates action potentials in response to red light, but not blue light, when expressed in neurons. To do this, they screen some red light-excitatory/blue light-inhibitory opsin pairs to find ones that are spectrally and temporally matched. They first show that this works with Chrimson and GtACR2, however, they expand their search after finding that the tau-off (inactivation after light cessation) kinetics of these two opsins are not well-matched. They directly examine a small set of options based on a literature search and settle on a variant of red light-excitatory Chrimson and blue light-inhibitory ZipACR. To even more closely match the kinetics of this pair, the authors create a structure homology model of the ZipACR retinal binding pocket and use this to guide generation of a small mutant panel, leading to a more optimized ZipACR mutant. They then show that a bicistronically expressed fusion arrangement of these opsins, plus some functional peptides, can drive action potentials up to 20hz with red light and does not do so with blue light, in hippocampal cells transduced by AAV. They also show function in vivo, in a mouse, using a physiological readout. They conclude that their new tool may be useful for complex experimental designs requiring multiple optical channels for write-in/read-out.

The major advantage claimed by the authors over existing tools is the temporal time-locking of their inhibitory opsin - this is driven by the contrast between tau-off kinetics of their ZipACR variant compared to gtACR2, which is used by the leading competitor tool (BiPOLES).

Big thoughts

While the authors were carefully thoughtful about the potential influence of temporal kinetics on the efficiency of a tool such as this one, there were no experiments conducted that make use of the unique properties of this molecular strategy (although the authors state that these experiments are now underway in their lab). They share some examples of how the tool could be useful in the discussion. Where do I think this could be useful?

First, experimental designs that require multiple optical channels of control. This appears to be aligned with the author's thoughts, as they state, correctly, that opsins utilizing retinal as a light-sensing chromophore are universally activated by blue light (the so-called 'blue shoulder'). Therefore, their tool may be useful for stimulating multiple populations using a blue excitatory opsin in neuron A and their tool for red excitation of neuron B - or, in the author's own words, "A potential solution to the problem of cross-talk...". In this manuscript, the authors provide state that there this is possible in theory and that there are no obvious reasons that it would not work, but do not present data that showcases their new tool for this purpose (e.g. Vierock, Johannes, et al. "BiPOLES is an optogenetic tool developed for bidirectional dual-color control of neurons." Nature communications 12.1 (2021): 4527. Figure 4f-I; 6). The same set-up could be imagined for green GECI (or equivalent) imaging of cells in the same volume that their tool is being used in - for instance, interleaving red stimulation light and blue imaging light, (perhaps) without the typical concern of imaging light bleed-through activating the opsin itself. I agree that it will likely work for multi-channel control, but only time will tell, at this point.

Second, for high-frequency temporal control over both excitation and inhibition in the same neuron. Red light turns the cell on, and blue light turns the cell off (see, for instance, Zhang, Feng, et al. "Multimodal fast optical interrogation of neural circuitry." Nature 446.7136 (2007): 633-639. Figure 2; Vierock as above, Figure 4a,b). Again, here the authors are long on theory ("The new system...can drive time-locked high-frequency action potentials in response to red pulses") and short on explicit data. While they do show that red light = excitation and blue light = inhibition, they neither show (1) all-optical on/off modulation of the same cell; nor (2) high-frequency inhibition or excitation (max stim rate of 20hz, which is the same as the BiPOLES paper used for their LC stimulation paradigm; Vierock, as above, Figure 7a-d). They did provide a response to this critique that data showing excitation and inhibition spread across multiple panels were largely collected from the same cells.

Despite these major shortcomings, the further development and characterization of tandem opsins, such as this one, is of interest to the community. There is on-going work by the BiPOLES team to create new iterations (e.g. Wahid, J., et al. "P-15 BiPOLES2 is a bidirectional optogenetic tool with a narrow activation spectrum and low red-light excitability." Clinical Neurophysiology 148 (2023): e16.). The authors have collected a substantial amount of additional data along the course of review and, even aside from the final tool, the overall data and approaches shown are useful.
