# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53148.sa1](https://doi.org/10.7554/eLife.53148.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study utilizes electrophysiological, optogenetic and computational modeling approaches to provide comprehensive and quantitative description of the spatiotemporal properties of the dentate gyrus feedback inhibitory microcircuitry. It predicts that these properties selectively enhance the separation of highly similar input patterns during learning- related gamma oscillations. The data were found to be high quality, and the idea that pattern separation is frequency dependent will likely be of interest to many researchers.

Decision letter after peer review:

Thank you for submitting your article "Quantitative properties of a feedback circuit predict frequency-dependent pattern separation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mathew V Jones (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study examines the recruitment of feedback inhibitory interneurons by dentate gyrus (DG) granule cells (GCs) using single whole-cell recordings from GCs during extracellular stimulation of mossy fiber axons in CA3 or optogenetic stimulation of GC populations. The authors very elegantly demonstrate that feedback inhibition in the DG is recruited in a low dynamic range of 0-4% of the active GC population. Moreover, the study demonstrates that inhibition is not uniformly distributed but inhibitory signals show a larger amplitude, low jitter of individually evoked IPSCs and faster time course when induced close to the recorded GC than inhibitory signals evoked at more remote sites in the DG. On the basis of the experimental data and a neuronal network model consisting of the various neuronal components of the DG, the authors demonstrate that such a network is suited to perform pattern separation between two overlapping inputs provided by the modelled perforant path particularly at gamma frequencies. The experimental and computational work is very well performed and the data are of high interest to the currently broadly discussed potential role of the DG in pattern separation. However, addressing the following issues would enhance the strength of the conclusions.

Essential revisions:

1) "Feedback inhibition is recruited steeply with low dynamic range (0-4% of activate GCs)". This central conclusion is very interesting but not fully convincing.

In Figure 1, only 4% of GCs are activated by antidromic stimulation (Figure 1H) which subsequently leads to the 4% ceiling shown in Figure 1K. But the critical parameter may not be how many GCs are stimulated but rather how many MFs are stimulated, since MFs that are unconnected to GCs likely contribute to feedback inhibition (i.e. Figure 1I shows that 30% max of feedback IPSC is recruited by 0 active GCs). Whether the low fraction of GCs responding to antidromic stimulation reflects low connectivity in the slice or inability to recruit MFs is unclear, but either way it raises a question about the robustness of this assay because this limitation dictates the upper limit for% active GCs. Reviewers wondered if Ca2+ imaging of the MFs near the stimulation site would provide a better dynamic range to make a quantitative estimate of% active MFs.

Figure 2. Reviewers appreciated that the authors use a 2nd method to estimate feedback inhibition wherein the full range of MF/GC activation can be assessed. Reviewers found it very surprising that the max IPSC evoked by focal and global Chr2 stimulation was similar (Figure 2I), and that the range of max IPSCs was so variable (<0.1 to >0.8 nA). What is the fraction of hilar interneurons recruited by focal and global ChR2 activation? This might help explain this surprising result and the variability. The authors state (subsection “Quantitative physiological properties of DG feedback inhibition”) that the dynamic range is determined by the cellular connectivity patterns, but it is not clear how connectivity could generate this narrow dynamic range – please explain. In measuring feedback IPSCs, the authors addressed voltage escape for dendritic IPSCs (Figure 2—figure supplement 2), but they did not address whether the ChR2-mediated conductance evoked by global light activation affects the measurement of the global max IPSC. In addition, why do the normalized curves not reach 100% (Figure 2 D and H)? Same question for all other figures where "IPSC [%]" is reported.

2) Figure 3. The slow rise time of IPSCs seem inconsistent with PV interneurons that are thought to be the major source of feedback inhibition. Presumably the IPSCs are slowed by asynchrony/compound events which might be assessed by quantifying individual events rather than averages to infer PV involvement. Were any PV interneurons recruited in Figure 4? It seems important to address the contribution of PVs since they are critical interneuron subtype in the model. Based on reported uIPSC from PVs, can the authors estimate how many PVs might be contributing to feedback inhibition?

3) The small number of active PP afferents used (24 of 400) in the input patterns meant that only about 10% of GCs were active even in the absence of inhibition (Figure 6—figure supplement 2). Just as the authors tested the robustness of their conclusions in the face of stronger feed-forward inhibition, it also seems important to assess the robustness of the conclusions across a range of excitatory drive that might represent EC activity under various conditions.

4) Subsection “Quantitative physiological properties of DG feedback inhibition”. The authors report that the range of active GCs that saturate feedback inhibition is in the range of active GCs reported in vivo. However, Pernia-Andrade and Jonas, 2014, Pilz et al., 2016, and Diamantaki et al., 2016, report higher fractions of active GCs in vivo, although reports using cFos labeling typically support the 1-4% range. The authors should discuss more explicitly the literature about GC activity in vivo and the interpretations of their small dynamic range of feedback inhibition in light of the possibility that GC activity might not be as sparse as suggested by cFos.

5) The nature of the facilitating inhibition remains unclear. Fast-spiking basket cells in the hippocampus usually show paired pulse or multiple pulse depression and for only few interneuron types paired pulse or multiple pulse facilitation has been observed. Whole-cell recordings from GCs during optogenetic stimulation of the different types of DG-interneurons might help to dissect the nature of the facilitating inhibitory inputs (e.g. Somatostatin-expressing cells).

6) GCs also contact Mossy cells (MCs), which in turn recruit DG interneurons and thereby inhibit GCs. It remained unclear why the MC feedback excitation of hilar interneurons was removed from the network model. It is an important functional element of this circuitry, which provides inhibition to GCs.

7) Subsection “Input-output relation of the feedback inhibitory microcircuit”, second paragraph and Figure 1—figure supplement 1 legend – Is it correct that the detection threshold used (0.94%) leads to a "true positive rate of 3%"? That seems very low, and implies that 97% of true responses were not detected. Unless this is a typo, is this not a serious problem that implies that the estimates of the active fraction of GCs are extreme underestimates?

8) Frequency-dependence of facilitation – Please state explicitly whether there was a "frequency tuning" (e.g., a preferred frequency) or whether all frequencies {greater than or equal to} 10 Hz displayed the same facilitation ratio (greater than 1).

9) Spike rates – Here, pattern separation was computed from Pearson's correlation, dot product and pattern overlap of population spike rate vectors, all of which are in general sensitive to absolute spike rates. Therefore, it is not surprising that some of the manipulations in the model (e.g., reducing various sources of inhibition) would enhance correlations by increasing GC spike rates, thus reducing pattern separation. It would be extremely useful to know if the different outcomes in pattern separation are driven mainly by the impact of the various sources of inhibition on GC spike rate alone, or whether there is indeed something else "special" about the different sources of inhibition, such as their differential IPSC latencies following PP or GC spikes, their IPSC timing jitter or failure rate or their input location onto the GCs. Plots of average GC spike rate versus the area under the ∆Rout curve, for the seven model families chosen, would be a first-pass at addressing these questions.

10) "The effect of facilitation on pattern separation is intuitive, since this allows the feedback circuit to integrate GC activity over time, and convert it to inhibition." Reviewers were not sure how intuitive this really is. True, integrating GC activity over time might be useful, but a) depression would allow a mathematical differentiation (or high-pass filtering) of GC activity over time, which arguably could be better than integrating over time for the purpose of separating temporal patterns, and b) the output of the inhibitory circuit is largely depressing anyway, providing the differentiation mentioned above. Thus I think the question remains: what is the purpose of the facilitation of the GC->BC synapse if the ultimate output will be depression at the BC->GC synapse anyway. Indeed, the authors found that the GC->BC facilitation only had a small effect on pattern separation.
