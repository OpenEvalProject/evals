# Peer review - Round 1

Editors:
- Baron Chanda, University of Wisconsin-Madison United States

Reviewers:
- Baron Chanda, University of Wisconsin-Madison United States

## Review text

DOI: [10.7554/eLife.47322.sa1](https://doi.org/10.7554/eLife.47322.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Mg2+bala is a critical element that is involved in various physiological processes. CorA is the bacterial ortholog of eukaryotic genes encoding a mitochondrial Mg2+ ion channel found in all eukaryotes. CorA function is negatively regulated by Mg2+. These channels are open when the binding site is unoccupied but they close in the presence of high Mg2+. Previous structural studies primarily using EPR and cryo-EM suggest that the channel undergoes a closed to open conformational switch in absence of Mg2+, which results in loss of five symmetry. Cryo-EM studies show that the open channel exists in at least two conformations which could either represent snapshots of a fluctuating channel or intermediates in the gating pathway. Recent crystallographic studies, however, suggest that the unbound channels may not undergo as much of a conformational change as suggested by the cryo-EM and EPR studies.

In this study, the authors have used high-speed AFM to monitor the time-dependent conformational changes as Mg2+ is removed from the channel. HS-AFM technique allows them to track conformational changes in a single CorA channel over time and correlate these changes with putative gating transitions. Functional experiments show that the gating process of the channel is relatively slow – currents decay over 15-20 minutes in electrophysiology experiments. Thus, the conformational changes are expected to be within the bandwidth of these measurements (500 ms per frame). Mg2+ depletion experiments show that the stable starting structure with five-fold symmetry becomes dynamic with time and ultimately settles to one or more asymmetric structures. One of the most interesting aspects of this study is that unlike most ion channels, the open channel conformation is both asymmetric and dynamic. Overall this is a technically work which advances the field both in terms of providing new information about the gating mechanism of CorA and demonstrating the power of HS-AFM to monitor single molecule structural transitions.

Decision letter after peer review:

Thank you for submitting your article "Real time dynamics of gating-related conformational changes in CorA" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Baron Chanda as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

1) All of the reviewers are concerned about the two-state model assumption for data analysis. The authors themselves state that there are two open states and one closed state. The model fit shown in Figure 3A is clearly inadequate. The open conformation is quite heterogenous, correct? The kymograph shown really looks like 3 states to me (the third being at a lower height, near a Δ Height of 0). And if the Mg2+ bound state is the baseline, lowest-height state, why doesn't the "down" state have a Δ-Height of zero? The choice of 2 states affects the dwell time analysis (everything else in Figure 3), and without a better rationale, I don't see why this choice is valid. There are other possible reasons for poor fit. For instance, some of the conformational transitions in CorA is much faster than the sampling rate and this could result in aliasing. This is difficult to rule out but should be discussed.

Also the height histogram on the right side shows a very disperse distribution, only two not very distinct local maxima that were not taken as level thresholds (so why 2-state?). As this data depiction is crucial for all the analysis done in the rest of Figure 3 it needs to be clearly and convincingly communicated.

STaSI is a model-independent idealization algorithm but it tends to overfit data. Have the authors tried any of the other HHM based algorithms? Given that they are assuming a two-state model, it would make more sense to use HMM.

2) The reviewers are convinced that the CorA molecule becomes highly dynamic in the absence of Mg2+ and find it very interesting that this conformation is conducting. However, we all agree that the assignment of these highly dynamic structures to discrete states is restrictive and perhaps also subjective. It is not clear how the conformational states (closed, open I, open II) taken from EM work were assigned to the conformations recorded with high speed AFM. Was it done manually? What were the objective criteria? How many structures were taken? Figure 5B only gives percentages. Again, this is crucial for all the data analysis done in Figure 5. As the authors have stated, the classification of discrete state in this highly flexible molecule is a challenge. In Figure 5A, it is not clear whether the images shown below are idealized (expected) images or averaged images for each of the states. It should be stated clearly in the legend. The actual averaged image should be shown as an inset. In addition, in some instances, the state assignments are based on changes in the shape rather than height. If both heights and changes in shape are taken into consideration, it appears that the number of possible states will be much more and trying to bin these highly dynamic structures into a few discrete states becomes less meaningful.

3) My other main critique is that it is very difficult to understand how changes in Mg2+ concentration were achieved for each experiment, and why the experiments were designed the way that they were. It seems like two different methods were used to change Mg2+Mg2+ concentrations: either pipetting in EDTA, or slow perfusion with an EDTA-containing solution over 10's of minutes (Figure 2—figure supplement 2). (Subsection “Mg2+-depletion induces large conformational changes 1 of the intracellular face” paragraph two: it's unclear whether perfusion is performed with EDTA solution or not. This could be clarified in the main text so that the reader doesn't have to go to the supplemental figure legend).

I assume that adding EDTA nearly instantaneously removes bulk Mg2+, so that any slow kinetic component is due to channel kinetics. Whereas with perfusion, changes in Mg2+ concentration and the channel's conformational journey from "phase 1" to "phase 3" both occur on over a minutes-long time scale. Because of the slow kinetic component to channel dynamics, it's really important for the logic of the paper to be clear about which method of Mg2+ depletion was used in the data in Figures 2 through 5.

Do I understand correctly that many (all?) of the experiments in Figure 3 involved a ramp from high Mg2+ to low Mg2+ over about 14 minutes with another 12 minutes in Mg2+ free conditions (as shown in Figure 2—figure supplement 2)? In Figure 3, the sharp delineation of the green, blue, and red boxes seem to indicate Mg2+ concentration steps, and the legend refers to images collected at saturating, 2, and 0 mM Mg2+. This is confusing. The text goes back and forth between describing imaging at 2 mM (subsection “Mg2+-depletion induces large conformational changes 1 of the intracellular face” paragraph one and ~2 mM). According to my reading, Figure 5 then uses 3 discrete Mg2+ concentrations, but the use of the color-fade arrows seems to indicate a ramp.

I'm not clear what advantage ramping the Mg2+ concentrations provided. Given the amount of functional data already available for this channel, including a good idea of the Kd for Mg2+, I might have gone straight to imaging at discrete Mg2+ concentrations. Could the rationale be explained?

4) Abstract: "finally equilibrates to an asymmetric structure." Is the final state a single asymmetric structure or it is at least two conformations. Based on the state identification matrix in Figure 5, it would seem that at 0 Mg, there are more than one asymmetric structures, unlike the Mg bound state.

5) Abstract: – "putative open state adopts multiple conformations through hinge-bending motions". This sentence contradicts the previous sentence and it is not clear whether the data provided in this study show hinge-bending motion. The conformational changes are compatible with hinge-bending but there is no direct evidence here.
