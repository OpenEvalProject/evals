# Peer review - Round 1

Editors:
- Alexander Borst, Max Planck Institute of Neurobiology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23496.030](https://doi.org/10.7554/eLife.23496.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Angular velocity integration in a fly heading circuit" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Alexander Borst (Reviewer #1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andreas V M Herz (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary

This is a magnificent paper! Based on a clear-cut hypothesis for the neural mechanism underlying head-direction coding in the ellipsoid body of the fly, Turner-Evans et al. continue their discovery story about the neural network underlying spatial navigation in Drosophila. Previously, they reported on a neural population termed 'compass neurons' that tracks the fly's heading orientation in visual surrounds and in darkness. Here, they show a novel cell population that is both pre- (in one neuropil) and postsynaptic (in another neuropil) to the compass neurons and moves the activity bump of the compass neurons in darkness, an elegant mechanism to update the fly's heading representation during turns. The study addresses a timely question and has been carried out with great care. It is technically at the highest level, comprising state-of-the-art genetics, voltage recording, calcium imaging and modeling. Given the unresolved neural mechanisms underlying head-direction signaling in vertebrates, this paper provides an important advance toward resolving that question by focusing on the simpler insect organism. In summary, Turner-Evans et al. present an excellent piece of modern systems neuroscience and provide a very interesting solution to a key problem in spatial navigation.

Major Comments

There is an overwhelming amount of supplementary figures. Some supplementary figures could be merged with the respective main figures. Other supplementary figures do not seem to be entirely necessary. Figure 2—figure supplement 1 could be moved to . Figure 3—figure supplement 1, Figure 3—figure supplement 4, Figure 3—figure supplement 5, Figure 3—figure supplement 6, , Figure 7—figure supplement 4 could be removed and, if not already the case, some of the information from these figures could be mentioned in the main text or Materials and methods section.

A lot of text is used to interpret the anatomy of both E-PG and P-EN neurons in terms of their polarity. Why haven't the authors used a presynaptic marker to show that directly?

As the authors mention, it is counterintuitive that the activity bump of E-PNs lags the E-PG bump in the PCB, but leads it in the EB. Based on the conceptual model and the anatomy it would be expected that both bumps overlap in the PCB. Do the data indicate that the peak of the E-PN bump in the PCB is formed by different E-PN cells than the E-PN bump in the EB, and thus that the location of the bump is different for E-PN dendrites versus axons? This was not entirely clear to me.

Subsection “P-EN spiking activity and membrane potential dynamics encode changes in angular velocity”: It is an interesting finding that the coding bandwidth of P-ENs corresponds with the behavioral bandwidth. Was this expected? Does the bandwidth of heading angles in E-PGs in darkness also correlate with behavioral bandwidth? Is every single glomerulus of the PCB only innervated by one P-EN and one E-PG neuron, or by multiple neurons of the same type? If so, different neurons innervating the same glomerulus could have different bandwidths. This point should be discussed more extensively.

Figure 1B: Please show a single E-PG neuron. Also, a connectivity map of the bridge and the ellipsoid body like Figure 6 in Hanesch et al., 1989, or Figure 3 of the authors in their Current Biology article 2016 would be helpful. Along these lines, some words about the intriguing bilateral asymmetry of this structure could be included in the discussion.

For Figure 2 the behavioral trace was convolved with the GCamP6f filter before correlation with the calcium signals in the noduli. In my understanding this was not done for the dual color calcium experiments in Figure 7 and Figure 8. Why not? Maybe this would account for the quantitative differences in the PVA offsets for the different indicator combinations.

Figures 1, 2, and 8 provide partial sketches about the system's connectivity but I missed a comprehensive wiring diagram: Which P glomerulus projects via P-ENs to which of the 8 tile-shaped sectors of the ellipsoid body, and which of the 16 wedge-shaped sectors of the ellipsoid body projects via E-PGs to which glomerulus? In particular, one would like to know how successive tile-shaped sectors overlap – I assume by one wedge, but these important details do not seem to be addressed in the manuscript (the movie touches a bit on these issues but can't provide a good solution).

The authors use the population vector to decode the heading direction from the E-PG activity. It would be great if they could elaborate on that concept and discuss whether the PV is also calculated by the fly (and if so: where) or whether the PV is simply a method for the experimentalist to study E-PG activity (if so: does the animal estimate its heading direction, and if so: how?)

Definition of the model system: the notation, e.g., ω(Θi,t) or the ∂t ω, suggests a system of partial differential equations, in contrast to the finite number of neurons (54) in each cell population. This approach also suggests that each cell population is continuous, i.e. without the notion of wedges or tiles with (more or less) homogeneous populations within each sector. In addition, the model does not distinguish between the larger tiles and smaller wedges – in fact, 54 is not divisible by 8 so this choice remains a bit mysterious. On the other hand, the authors' compact model is appealing. But one would like to see a detailed discussion on how the model relates to the experimental (in particular: anatomical) facts.

Predictions of the model system: it would be nice if the authors could run a simulation with time-dependent velocity input, similar to the experimental situation shown in Figure 1E. This would greatly help to appreciate the model's predictive power and could be included as a separate new panel in Figure 8.

Figure 2—figure supplement 1: Why are there negative correlation coefficients for CCW in the left nodulus (and for CW in the right nodulus)? Could this phenomenon hint at a pull-push mechanism, with pull (excitation) in front of the E-PG bump and push (inhibition) behind it?

Interestingly, several features of the P-EN neurons do not fit well with the hypothetic wiring scheme, while other, yet unknown neural elements, still need to be identified in order to fully explain the neural network involved in head direction coding. I suggest addressing these issues more clearly and openly in the discussion, in particular the apparent lack of visual responses in P-EN neurons and the unexpected one-glomerulus shift of P-EN activity following the E-PG activity as these will guide future efforts to unravel the missing elements in the mechanisms of head-direction coding.

Why do the authors use the term "glomerulus" for substructures in the protocerebral bridge that Ito et al., 2014, in a widely accepted intention for a uniform nomenclature of insect brain structures have termed "slice" instead? The term "glomerulus" has originally been used to denote substructures in the antennal lobe/olfactory bulb that are reminiscent in organization to a kidney glomerulus (shell and core). Nothing like this is apparent in the slices of the protocerebral bridge and using the term "glomerulus" instead might cause confusion about its internal organization. By the way, the term has only been used in flies and not in other insect species, which is again highly unfortunate. Therefore, I suggest changing the term "glomerulus" to the widely accepted term "slice".

Subsection “An excitatory loop between P-ENs and E-PGs”. It is highly surprising to see that the P-EN neurons apparently do not respond to visual cues. Unfortunately, only two experiments are provided to support this (Figure 3—figure supplement 2). If this is correct, however, the P-EN neurons cannot receive synaptic input (directly or indirectly) from E-PG neurons in the ellipsoid body, because their signaling as shown by Seelig and Jayaraman (2013, 2015) is dominated by visual over proprioceptive feedback cues. This may be the reason why activation of the E-PG neurons resulted in inconclusive responses in P-EN neurons. I think this discrepancy in the results should be more clearly addressed in the discussion. In other insect species there are multiple sets of P-EN and E-PG neurons (e.g. in locust 3 sets of EPG neurons termed CL1 and 2 sets of PEN neurons termed CL2, partly with opposite polarity). How is it in flies? If the situation is similar, these second or third set, not studied here, will likewise contribute to compass coding, and might be in part responsible for the discrepancies between hypotheses and results.
