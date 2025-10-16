# Peer review - Round 1

Editors:
- Markus Meister, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52949.sa1](https://doi.org/10.7554/eLife.52949.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

How the retina extracts the direction of motion of a visual object ranks as a cardinal problem of computation in neural circuits. Much has been revealed about this over the past half century, but the present paper offers an exquisitely detailed window on the underlying mechanisms in the fine neuronal dendrites of the retinal ganglion cell.

Decision letter after peer review:

Thank you for submitting your article "The functional organization of E/I in the dendritic arbors of retinal direction-selective ganglion cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Markus Meister as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: William Grimes (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please aim to submit the revised version within two months.

Summary

Jain et al. explore the functional organization of excitation and inhibition (E/I) on dendrites of ON-OFF DS RGCs in mouse retina. This is an extremely well studied circuit, but several details of the computation remain to be understood. The key question in this study is whether imprecise directional tuning in the dendrites averages out at the soma or whether, instead, directional tuning is already precise in small dendritic segments. The authors argue for the latter, showing very precise tuning and suggesting independent synaptic input down to the scale of ~5-10 μm. The results are consistent with a biophysical picture in which (1) Ca transients in the DSGC are spatially confined on a scale <10 µm, and (2) synapses separated by ~10 μm receive input from different SAC dendrites, and (3) those SAC dendrites are tuned to within 30° (SD) of the same null direction.

Essential revisions

1) Framing of the study.

These observations about the spatial structure of SAC inputs to the DSGC are interesting and mostly consistent with expectation from the known anatomy. However, the authors frame the report in a very different light: as a study of spatially and temporally precise excitation-inhibition interactions within dendrites, for example: "which allowed us for the first time to directly infer the degree to which the presynaptic excitatory and inhibitory inputs to DSGCs are functionally organized at a subcellular level"; "suggest that presynaptic excitatory and inhibitory inputs are precisely organized"; "patterns of presynaptic activity are coordinated with enough precision to support computations based on fine scale E/I integration"; "suggests that the underlying excitatory and inhibitory inputs are highly coordinated throughout the DSGC's dendritic tree"; "underlie the high fidelity of excitation and inhibition"; "tight spatial and temporal E/I coordination".

These claims are only half-supported. In the conventional wisdom, the excitatory input is almost entirely untuned and direction selectivity results from the inhibitory inputs. All the interesting dynamics of integration that produce direction-selectivity have been accomplished by the SAC already. Consistent with this conventional picture, the present experiments primarily report on inhibitory inputs to the DSGC, rather than any precise interaction of excitation and inhibition. There are multiple indications in this work that the details of excitation matter little, other than offering a baseline signal that can be inhibited: First, the overall excitatory input to the DSGC is untuned (Figure 1A). Second, when the authors perturb the excitation by blocking NMDA receptors the dendritic tuning remains the same (Figure 4). Third, the experiments do not manipulate the relative timing of excitation. In fact, one suspects that the dendritic tuning would be identical if they supplied the excitatory input entirely through the recording electrode. By contrast, when the inhibition gets removed, by knockout of vGAT (Figures 5C,D, Figure 6G) or with SAC ablation (Figure 8), the fluctuations and the DS in the Ca response mostly disappear. So the report is primarily about inhibition, not any detailed functional organization between excitation and inhibition.

We recommend that the authors reframe the study to emphasize what has been learned about the spatial distribution of inhibitory inputs. In general the observations seem to accord remarkably well with prior expectations from the anatomy of SAC-DSGC connections and the literature on presynaptic direction tuning at that same synapse (e.g. Poleg-Polsky et al., 2018). This itself may be a satisfying conclusion, but any deviations from those expectations could be highlighted as well.

As an alternative the authors might actually test whether there is any high-fidelity coordination of excitation and inhibition on a small scale, but that will require different experiments: separate manipulation of excitation and inhibition, and releasing the block on the dendritic sodium channels to observe any threshold nonlinearities that process the summed signal. A conventional picture of dendritic integration would suggest that E and I signals get summed over distances much greater than 10 μm before a spike is initiated.

2) The study seems to focus entirely on directional encoding in the ON arbors of the ON-OFF RGC without a clear justiﬁcation or explanation as to why. The spike recordings show responses to the leading and trailing edges of to the moving spots, are the resultant calcium signals conﬁned to their respective arbors? Do OFF dendrites show motion signals on a similar spatial scale?

3) The manuscript often refers to "active conductances" being blocked when in fact only NaV channels are blocked. Voltage-gated Ca2+ channels are essential for the measurement, and there is no discussion at all about possible roles of voltage-gated K+ channels, or other active channels in the dendrites, if they exist. Some explanation would be helpful.

4) Subsection “Independent synaptic processing within small dendritic segments”, Figure 6: This analysis is about noise correlations, namely the fluctuations trial-to-trial that occur under the identical visual stimulus. Those fluctuations may well have a different origin from the systematic signal that produces directional tuning. The difference between noise and signal correlations and their interpretations and possible origins should be brought out better.

5) Subsection “Dendritic nonlinearities promote dendritic independence”: The model in Figure 7 seems poorly constrained. It is not clear how many free parameters there are, how they were chosen, and how robust the main ﬁnding is over parameter space.

6) Discussion section: Expand the section that relates known circuit anatomy to function. For example from the SAC coverage factor one can estimate how many null-side SACs connect to each OODS, providing additional context for the ablation experiments. Dramatic change in DSI in some spots and not others suggests that each hotspot might correspond to output from a single SAC. Similarly, the length scale of noise correlations may be related to the axonal arbor of a single bipolar cell. Non-specialists might not fully appreciate the size difference between an OODS RGC and the bipolar cells that are providing its excitatory input.

7) Subsection “Functional versus anatomical characterization of the circuit”: "The directional tuning of dendritic sites was relatively homogeneous; 95% of the dendritic sites fell within 63° of the DSGC's true PD (two standard deviations). This is a much tighter distribution than can be estimated from the anatomical connectivity, which shows SAC dendrite orientations roughly equally represented across a 90° spread." Actually, the opposite seems to be the case and the anatomical connectivity sounds slightly tighter: a uniform distribution ranging over 90° has a standard deviation of 26°, less than the 31° reported here for dendritic tuning. Actually though, the close correspondence is another indication how well the observations in the present report accord with prior understanding from physiology and anatomy in this circuit.
