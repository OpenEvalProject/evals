# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75517.sa0](https://doi.org/10.7554/eLife.75517.sa0)

The manuscript introduces a new enhancement to the dynamic clamp technique, CapClamp that, analogous to the artificial conductances of standard Dynamic Clamp, allows the experimenter to adjust the somatic time constant by setting a new membrane artificial capacitance independent of any change in input resistance. The technique is shown to have application for studying temporal integration, energetic costs of spiking and bifurcations. The technique is rigorously tested in model and physiological application and is robust when sampling frequency of the feedback (clamp) loop is fast compared to the fastest electrical event in a neuron (usually action potentials), and for vertebrate neurons it should be 20KHz or faster and yet faster for fast spiking neurons.


---

# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75517.sa1](https://doi.org/10.7554/eLife.75517.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A dynamic clamp protocol to artificially modify cell capacitance" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Ronald L Calabrese as the Senior and Reviewing Editor and Reviewer #3. The following individual involved in review of your submission has agreed to reveal their identity: Jorge Golowasch (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) As discussed by Reviewer #2 in their public review, the changes in capacitance have a weak effect on excitability in real neurons. The authors should definitely apply the same comparison already performed for action potential, i.e., expected changes vs. real changes in FI curve following capacitance clamp. Maybe in DGGCs, not much effect is expected on gain, but this has to be clearly demonstrated. Otherwise, it raises concerns about the efficiency of capacitance clamp beyond the soma.

2) Please address all the concerns expressed in the Recommendations for the authors.

Reviewer #1 (Recommendations for the authors):

This is an excellent paper. The new dynamic clamp method described here to control membrane capacitance is based on sound theory, it is well described and tested. I have no major concerns. In fact, I appreciate the authors for developing this in such a timely manner for me, as I was planning to do something similar myself.

Reviewer #2 (Recommendations for the authors):

1) The authors demonstrate in the neuron model that manipulating capacitance not only affects action potential waveform but also significantly alters the excitability profile of the cell, modifying in particular the gain of the fI curve of the neuron. However, when tested on DGGCs, the effect of capacitance on action potential shape is very strong but the effect on excitability is very mild. The overall change in gain is close to 20% for a 5-fold change in capacitance, while a similar change in capacitance induced a ~2-fold in gain in the neuron model. While the authors say that the results in real neurons are similar to the ones obtained in the simulated neuron, the quantitative difference is large enough to contradict that statement. Moreover, this discrepancy questions the ability of the capacitance clamp to efficiently modify capacitance in real neurons. In fact, concerning action potential shape, the authors compare the effect of capacitance manipulation in real neurons with the expected effect (Figure 4B), but do not present this comparison for excitability measurements. It would have been very interesting to see whether the actual results significantly depart from the expected results.

2) Concerning the potential impact of capacitance clamp, and since most changes in capacitance in physiological contexts seem to be related to neuronal growth, it would have been really interesting to compare the impact of manipulating capacitance with the impact of manipulating concomitantly input resistance and capacitance, which is expected when neuronal size is changing, for instance during development. This type of comparison would also help underlining the significant contribution of changes in capacitance, which have been so far undermined. Testing these two manipulations in parallel would greatly help to disentangle the specific contributions of changes in membrane resistance and capacitance during neuronal growth, and would emphasize the value of the capacitance clamp tool.

Reviewer #3 (Recommendations for the authors):

The manuscript is very clearly written and well-focused.

Lines 93-94: "…change with respect to the original capacitance (e.g. Ct=67.4 pF: C=67.5 pF; Ct=336.9 pF: C=338.1 pF), whereas the… Why are these examples chosen and not a more uniform range?

Section 2.5.1: I found this very confusing. In an RC circuit the response sizes to a sequence of current pulses as measured by baseline to peak are identical. It is very confusing to say "…the cell's response to the second one should be higher than to the first one." Or to say "…as apparent by the larger step sizes in the stair-like voltage response and the finally higher ratio of last to first pulse response." Please rewrite.

Section 2.5.3: This section was the only part of the paper I found unconvincing. It is a foregone conclusion that the CapClamp can find the critical capacitance in the Wang-Buzsáki neuron, given Section 2.3. The failure of the technique to find the critical capacitance in a dentate gyrus granule cell is thus an ambiguous result. Is this a technical failure or a real result? I suggest deleting this section.
