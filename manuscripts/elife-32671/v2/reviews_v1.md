# Peer review - Round 1

Editors:
- Karel Svoboda, Janelia Research Campus, Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32671.018](https://doi.org/10.7554/eLife.32671.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Three-dimensional Two-photon Optogenetics and Imaging of Cortical Circuits in vivo" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom, Karel Svoboda is a member of our Board of Reviewing Editors and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers appreciated the great potential of the photostimulation method. But the paper fell short in documenting the technical advances. The central claim of the paper is that the use of scanning galvos coupled with scanless SLM system for optogenetic stimulation greatly reduces the power required to photostimulate neurons relative to other 3D holography techniques. This was not directly shown. Moreover, optical and electrical crosstalk has not been characterized sufficiently.

Reviewer #1:

Previous work demonstrated the ability to manipulate specific cells with single-neuron precision within a given optical plane (2-dimensional stimulation). The aim of this work was to expand the number of addressable neurons by enabling stimulation in 3-dimensions using modest laser powers. The method (ability to stimulate 27 neurons in 3D) represents an advance in this field.

Major point:

The method portion that is novel is not thoroughly characterized.

Figure 1: Schematic of microscope and quantification of z-psf on photostimulation path. Important, z-psf is relatively broad due to the small size of the galvo, they could have made it tighter (at the expense of the size of the field-of-view). They also characterize targeting error and excitation efficiency relative to position in field of view. Overall, characterization of photostimulation path is thorough.

Spike count vs stimulation power and spiral duration. Spike latency, jitter and spatial resolution are all comparable to those reported from previous work that employed the same photostimulation technique (Packer, 2015). They need to provide more detail about how this measurement was done. How many different off-target spots were stimulated and where were they? What power and duration?

Why is there no quantification of excitation caused by the imaging laser? They do not mention the power used for imaging; in the discussion they state that they kept the imaging power "as low as possible".

Why are such long duration spirals used (up to 400 ms)? Excitation is maximized when the duration of the spiral is much less than the off time constant of the channel (40ms for C1V1).

Figure 2: They illustrate, as has been shown in previous work, that neurons that are targeted are reliably excited. The map highlights the effects of a broad z-psf. It would be nice to see if they could efficiently excite their targeted neurons with lower powers or durations while improving the spatial resolution.

Figure 3: The novelty is the ability to stimulate a 'large' number of neurons simultaneously. This capability is only demonstrated anecdotally in an experiment in which they simultaneously stimulate 27 neurons. The efficiency doesn't seem to drop off much going from 15 targeted neurons up to 27 targeted neurons. Would it have been possible to stimulate more? Can they move from 70% activation for the 27 neuron group up to 100% by changing stimulation parameters (i.e. power, duration, # of spirals)? Better characterization of the limits of the method is absolutely necessary.

Figure 4: To make this experiment more interesting it would be nice to demonstrate a result that could not be achieved by less sophisticated methods such as 1-photon stimulation. One such example would be to show how the change in selectivity in the population depends on the particular SOM neurons that were stimulated. What happens if another group of SOM neurons is stimulated?

Reviewer #2:

As stated by the authors in the Discussion section: "it has become the norm to use holographic approaches" for 2P stimulation of single or multiple opsin-expressing neurons. The central advance of this paper is the use of scanning galvos coupled with beamlets produced by a scanless SLM system for optogenetic stimulation. The authors claim this greatly reduces the power required to photostimulate neurons relative to other 3D holography techniques, which allows for further multiplexing of the beam and stimulation of more neurons. Unfortunately, this claim is not experimentally validated by the authors anywhere in the submitted manuscript. The manuscript suffers from a lack of rigor that is necessary to push the field forward and is poorly written.

1) Test the central claim of the paper: The microscope setup should be able to switch between scanless 3D holography, and the hybrid holographic-galvo spiral stimulation approach which the authors' claim greatly lowers the light powers required for stimulation. Both stimulation techniques could be used on the same animal with the same low-repetition laser. This would elegantly control for hardware and animal-to-animal variability (particularly opsin expression level). Please demonstrate that the light dosage required to stimulate neurons, either by GCaMP readout or cell-attached electrophysiology recordings (the latter would be better), is much smaller for the hybrid approach relative to scanless holography. I notice that the stimulation time is quite long for the spiral stimulation (the Materials and methods section has large range 10-2800 ms), so be sure to match time of stimulation as well as power to compare light dosage vs. excitability. In my opinion, this set of experiments is essential for the manuscript to be considered for publication.

2) It has now been several years that people have been publishing simultaneous 2P imaging and stimulation with GCaMP and C1V1. The authors report in the Results section "minimal cross-talk between the imaging and photostimulation beams" without characterization. If this is going to become a mainstream technique, it is vital that optical and electrical cross-talk be well characterized using these reagents. This is vital for progress in the field:

a) The authors' use cell attached recordings to measure latency and jitter of their stimulation paradigm, so they are proficient with in vivo electrophysiology. Please measure perturbations to cell activity (cell-attached) and membrane potential (whole cell) of C1V1 expressing cells when 2P scanning with typical conditions for GCaMP imaging. Please verify that the C1V1 cells that are recorded from also respond to the stimulation paradigm to confirm suitable expression levels.

b) The authors show an example for optical cross talk of the opsin-stimulation beam during GCaMP imaging (Figure 1—figure supplement 3), and their software solution. Please provide quantification for how large the artifacts tend to be, and how well the data processing removes it. One experiment to include would be to stimulate cells in a mouse with only GCaMP (no C1V1), and measure what percentage of cells, after implementing the data processing pipeline, are still characterized as stimulated by the activation criteria written in the methods. This will give a sense for false positives.

3) The authors report in the Results section "response rate of individual targeted cell remained high and stable (Figure 3F, 82% +- 9%). Within a group of cells that were simultaneously photostimulated, the percentage of responsive cells was also stable (Figure 3G, 82% +- 9%)."

a) I do not understand Figure 3F. The stimulus conditions presented conditions go from 1-27 targets. The y-axis reports individual targeted cell response rate. What I imagine this graph is showing is the number of cells that were responsive during each of these conditions, yet that appears to be what Figure 3G is presenting. Is this graph showing excitation of each cell one at a time in all conditions (e.g. marching through each of 27 neurons in condition 7)? If so, what is the value of this graph? Figure 3G makes much more sense to me.

b) Figure 3F and 3G have very different distributions as a function of stimulation condition, so I find it hard to believe that the quoted percentage (82% +- 9%) is identical for both graphs.

c) I disagree with the assessment that the percentage of responsive cells is stable. The histogram peaks appear to generally decline with further multiplexing of the beam. I would eliminate this statement.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Three-dimensional Two-photon Optogenetics and Imaging of Cortical Circuits in vivo" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Bernardo L Sabatini (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript has improved. The presentation is much clearer, and the benefits over and comparisons to previous techniques are better stated. The data is now better quantified. The techniques are more thoroughly explained and many previously missing details have been added.

Given that adding scan mirrors is a straightforward modification to most SLM based stimulation systems, this method could be readily adopted by many labs.

Essential revisions:

The comparison between scanning and scan-less approaches (Figure 1—figure supplement 2) is still scant. Given that many cells can be targeted at once, why is this analysis done for only 9 cells across 2 mice?

If the main goal of this paper is to maximize the number of neurons activated in some fixed time window, it is important to know how much faster cells can be activated using scanless techniques than scanning techniques. If scanless stimulation can activate cells significantly faster then, it might be a more efficient way to excite many cells in a fixed time window than the scanning techniques presented here.

It is nice to see a larger population activated than in the previous version. But what is the reason why so many cells fail to respond? Is it simply that they weren't expressing enough C1V1? This is worth checking via fluorescence of mCherry and discussing in the text.

Add some information about the depth of the cells in this analysis.

Regarding Figure 1—figure supplement 4. There appears to be some activation from scanning at 90mw relative to 0mw. A t-test should give a p-value around 0.05. The text should address this.

There are several relatively straightforward analysis steps that the authors should take to address the concerns regarding why cells that fail to respond during ensemble stimulation. Can the cells that fail to respond during ensemble stimulation be stimulated by themselves or are they just not excitable?
