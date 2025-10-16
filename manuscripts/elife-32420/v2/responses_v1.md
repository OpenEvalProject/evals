# Author response - Round 1

Authors:
- Peng Zhong
- Casey R Vickstrom ([ORCID: 0000-0003-0536-1211](https://orcid.org/0000-0003-0536-1211))
- Xiaojie Liu
- Ying Hu
- Laikang Yu
- Han-Gang Yu ([ORCID: 0000-0001-6838-8310](https://orcid.org/0000-0001-6838-8310))
- Qing-song Liu ([ORCID: 0000-0003-1858-1504](https://orcid.org/0000-0003-1858-1504))

## Response text

DOI: [10.7554/eLife.32420.025](https://doi.org/10.7554/eLife.32420.025)

Essential revisions:

1) In their current state, the experiments studying synaptic parameters (i.e. minis, AMPA/NMDA ratio…) are: (1) per se not sufficient to provide mechanistic insights (2) rather confusing (see reviewers' comments) (3) not sufficiently discussed. Thus, we advise that you remove this data set (and the corresponding discussion) from your revision. Alternatively, although it is not the reviewer's preferred option, the authors may choose performing all additional experiments suggested by the reviewers in their detailed reviews.

Also, for the sake of clarity, the Results section measuring the sag of membrane potential are really not necessary and should be removed.

We have removed the experiments studying synaptic parameters (original Figure 3B-E), membrane potential sag (original Figure 4H,I), and the corresponding discussions.

2) The VTA contains a heterogeneous population of DA neurons with respect to their projection targets and HCN channel expression. Specifically, neurons that project to the nucleus accumbens exhibit large HCN currents, whereas those that project to the prefrontal cortex do not.

It is imperative that the authors analyze (Results section) and interpret (Discussion section) their results in light of the different target populations and different cell types that were identified in the VTA. Notably, the paper by Friedman et al., 2014 where Ih and VTA neuronal excitability were studied in another stress paradigm and the article by Moreines et al., (2017) where reduced activity was observed in a subpopulation of VTA DA cells in a CMS model, must be discussed. Additionally, because of the "laterality" issue raised by Moreines et al., the authors are requested to document and discuss the location of the recorded DA cells (both ex vivo and in vivo).

The reviewer is correct that the VTA contains a heterogeneous population of dopamine neurons in regard to many aspects, including projection targets and HCN expression. Given that HCN current is the focus of our present study, our in vivo and ex vivo recordings targeted the lateral parabrachial pigmented area (PBP) of the VTA, where dopamine neurons exhibit large HCN currents, predominantly project to the lateral shell of the NAc and play a primary role in reward and motivated behavior. Our ex vivo recordings were made from NAc lateral shell-projecting DA neurons labelled with retrobeads, which were predominantly located in the lateral PBP of the VTA, consistent with Lammel et al., (2008, 2011). We also made efforts to target DA neurons in the lateral PBP in our in vivo recordings. The coordinates used for in vivo recordings (AP -2.9 to -3.3 mm, ML 0.6 to 1.1 mm, DV -3.9 to -4.5 mm) correspond to the PBP (mainly lateral PBP) but not in midline nuclei such as the interfascicular nucleus and the rostral linear nucleus, nor A10 DA neurons in the supramammillary nucleus. The location of some neurons was confirmed by juxtacellular labeling with neurobiotin and TH staining, with one neuron labeled in each mouse. To clarify the location of recorded DA neurons, we have revised the manuscript to more explicitly state that recordings were targeted to the lateral PBP.

Additionally, we provide a clearer rationale for targeting the lateral PBP and NAc lateral shell-projecting DA neurons, and better discuss our results in the context of VTA DA neuron heterogeneity. We specifically addressed the “laterality” issue raised in the Moreines et al. study. We suspect that differences in CMS paradigms and animal species might explain why Moreines et al. did not observe alterations in lateral VTA dopamine neuron firing. In addition, we have further discussed our results in the context of Friedman et al., 2014. In particular, we discuss effects on Ih current in DA neurons that project to different targets, and discuss the circuit-specific effects on HCN overexpression on depressive-like behavior. Further, we make clear the limitations of our viral knockdown and overexpression approaches, and discuss opportunities for future investigation into cell- and circuit-specific contributions of HCN2 channels in depressive- and anxiety-like behavior.

3) The revised version must include the following technical details:

-The resting conductance of the neurons must be provided in a table. The conductance of the cells illustrated in Figure 4 and Figure 6 are very different.

We analyzed the instantaneous current (Iins) in traces of Ih current in Figure 4 and Figure 6, and plotted this current against the hyperpolarizing voltage steps. The slope of these I-V curves provides an approximation of the resting membrane conductance (Gresting) (the measurement of Gresting has been shown in Figure 4—figure supplement 1). We find that there was not a significant effect of CMS on resting membrane conductance compared to control (Figure 4G). However, HCN2 knockdown with shRNA reduced resting membrane conductance compared to scramble-shRNA (Figure 6—figure supplement 1). We have replaced traces for Ih current in Figures 4 and 6 that better represent the averaged data. We have described the design and interpretation of the resting membrane conductance in the Materials and methods, Results and Discussion sections.

-The capacitance of the dopamine cells (50 pS) is about twice that which is often reported. How was the capacitance of the cells measured? What were the setting for the acquisition and filtering frequencies?

VTA dopamine neurons have a relatively large cell body compared with many other cell types. We performed a literature search to determine what previous studies have measured for the capacitance of VTA dopamine neurons in mice. We find that the capacitance we recorded (control, ~51 pF; CMS, ~45 pF) is consistent with published studies (Chung et al., 2017, PMID: 28894175; Baimel et al., 2017, PMID: 28178514; Zhang et al., 2010, PMID: 20600174). Chung et al., (2017) reported the capacitance for VTA dopamine neurons to be ~50-60 pF. Baimel et al., (2017) reported differences in VTA dopamine neuron capacitance for different projection-defined dopamine neurons. Consistent with our result, the average capacitance for NAc lateral shell-projecting DA neurons was 57 pF. Although other populations had lower capacitances (24 pF for NAc medial shell-projecting; 38 pF for BLA-projecting), our recordings focused on NAc lateral shell-projecting neurons. In a third study, Zhang et al., (2010) report a capacitance of 79 pF for VTA DA neurons in the lateral VTA and 54 pF in the medial VTA. Thus, our result does not differ substantially from published studies. Membrane capacitance was measured by Clampex software using small amplitude hyperpolarizing and depolarizing steps ( ± 5 mV). As mentioned in the Materials and methods section, signals were sampled at 10 kHz and filtered at 2 kHz.

-In the figure legends, the statements of the number of n per group are not clear. For example, in Figure 2E, it states "n=10-13 neurons from 4-5 mice". Does this mean 4-5 mice per group (control vs CMS), or combined between both groups?

In each relevant figure legend, we have clarified the numbers of neurons and mice in each group to avoid confusion.

-The authors state that the C57BL/6 mice and the DAT-tdTomato mice did not show significant differences in their behavioral tests, so the results were pooled. The authors should show supplementary data to demonstrate this claim.

We now provide Figure 1—figure supplement 1 presenting this data and Figure 1—source data 1 for statistical analysis of this data.
