# Peer review - Round 1

Editors:
- Nils Brose, Max Planck Institute of Experimental Medicine Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66709.sa1](https://doi.org/10.7554/eLife.66709.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Your paper describes an interesting new role of the ion channel TRPM7 in the regulated release of neurotransmitters. The corresponding data provide important new insights into the mechanisms by which synaptic transmitter release is fine-tuned.

Decision letter after peer review:

Thank you for submitting your article "TRPM7 is critical for short-term synaptic depression by regulating synaptic vesicle endocytosis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Lu Chen as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Essential – Not Requiring Additional Experimental Work

1. The TRPM7 KO strategy is based on the deletion of exon 17. The initial description of the KO (Jin et al., 2008) does not clearly show whether there is a possibility of the generation of a truncated variant of the channel or one with a deletion within the sequence upstream of the TMDs. Can this been excluded?

2. For all data in the manuscript, the authors need to show data points, not just bar graphs with mean and SE.

3. The data in Figure 1E showing longer fission pore durations in the KO are interesting (and similarly, the data in Figure 4H on the rescue), but in the legend it becomes clear that only 42 events in each group were considered, which yielded p<0.05. Strikingly, though, the authors measured from no less than 83 and 110 cells with approximately 6 events per cell (Figure 1B), so overall, <10% of the events were included in panel E. Based on the Methods, the authors only considered events with step sizes >0.2 fF and durations >15 ms, citing a low-pass filter set at 1 ms (24 dB). The reviewers understand that the method has limitations (and the authors are clearly competent in the field), but it is a concern to be concluding based on such a small selection of events. With a filter setting at 1 ms, could the authors attempt to visualize the entire distribution of events down to 5 ms, to inspect if the difference between WT and KO is found only for the longest events, or independently of the event duration?

4. In the example of the current flowing through the patch of a WT but not KO cell in Figure 1F, the capacitance change appears to be >10 times in size compared to the example shown in Figure 1A. If this is not a simple typo, an explanation is required as to whether this finding even applies to the smaller events.

5. The authors aimed to study the physiological function of presynaptic TRPM7, and they conclude that TRPM7 might act as a Ca2+-influx pathway. However, the pipette-solutions for whole-cell experiments (in chromaffin cells and HEK-cells, where TRPM7-related currents were apparently detected directly, in Figure 1F and Figure 4A) did not contain Mg2+ (in chromaffin cells Na-ATP and Na-GTP were used; in HEK-cells no nucleotides or magnesium were included), and TRPM7 is described as a ion channel that is fully inhibited by 2 mM intracellular Mg-ATP (Nadler et al., 2001). Therefore, it is not straight forward to see how Ca2+ would permeate the channel under physiological conditions. The authors have data (e.g. CGaMP6) consistent with Ca2+-influx, and they show that a mutation (LCF) blocking permeation also blocks function in chromaffin cells, but this is not conclusive evidence that permeation is involved. The authors need to discuss the negative regulation of TRPM7 by Mg-ATP carefully (it seems to not even be mentioned), and whether physiologically relevant conditions are likely to arise where this block would be relieved. They should also discuss their choice of pipette solutions. Finally they should discuss whether their data might be consistent with other scenarios than Ca2+-influx through TRPM7.

6. It is unclear why the KO-induced changes in vesicle fusion do not show-up as a slower rise in the SypHy measurements shown in Figure 3. This should be briefly discussed.

7. The explanatory connection that the authors make between the TRPM7-KO effects on calcium signals, endocytosis, and short-term plasticity seems forced. The KO reduces presynaptic calcium signals (likely also with endocytosis during stimulation trains) and increases synaptic depression already very early in the train. There are more parsimonious explanations for the short-term plasticity change: Reduced bulk calcium levels could cause reduced calcium-dependent activation of the vesicle priming machinery or even reduced activation of calcium sensors in fusion (Synaptotagmins). This aspect should be considered in the discussion part of the paper. It may well be that the short-term plasticity defect in the TRPM7 KO neurons is not directly related to the endocytosis defect. Further, it seems hard to imagine that a selective slow-down of endocytosis would become manifest as an appreciable change in exocytosis already after only 10 APs – unless one considers 'site clearing' as proposed by Neher and Sakaba.

8. It is unclear why the 'endocytosis-associated conductance' the authors describe was missed in the many studies employing whole-cell recordings in chromaffin cells. Do the authors assume that detection failed in these cases due to the outward-rectifying character and/or the fact that typical measurements are done at -80 mV? This issue should be discussed.

9. The time scale of changes in endocytosis kinetics in TRPM7 KO chromaffin granules is of no known physiological impact. This should be discussed.

Essential – Requiring Additional Experiments

1. A basic analysis of the morphology of TRPM7 KO chromaffin cells and neurons is needed to complement the present data. Further, it should be tested if the TRPM7 KO affects the expression or localization of proteins that are critically involved in presynapse function, especially in endocytosis and endocytotic fission (e.g. Dynamins).

2. It should be properly verified that WT and mutant versions of TRPM7 are expressed and targeted in the same fashion. Figure S5 does not support the case that the mutant protein is correctly trafficked. It is unclear what the anti-FLAG staining corresponds to in the KO cells infected with a virus with an empty vector. This staining appears to be vesicular, which is also present in the TRPM7-WT infected cells, but not in the LCF infection. A higher resolution approach is required to localize the FLAG staining (confocal might be sufficient). If TRPM7 is no longer targeted correctly when it has the conduction mutation, one cannot conclude that the current through the channel is what is important.

3. Given the ability of the authors to perform very high-end electrophysiological analyses of transmitter secretion from chromaffin cells, the use of KCl-depolarization to assess TRPM7-KO-induced changes in exocytosis from chromaffin cells appears 'crude'. This type of stimulation is massive and somewhat unphysiological. The key question that remains open is whether exocytosis triggered by more physiological stimuli is affected by the KO (e.g. as assessed by short depolarisation stimuli combined with capacitance measurements). This should be tested in a small KO-vs.WT analysis.

4. Figure 3E-F show reacidification in WT and KO neurons. The description of this experiment is insufficient. The rationale of the experiment is a bit diffuse and it is unclear how the quantification (i.e. on what part of the trace). Moreover, the trace in panel E seems to be inconsistent with the quantification in panel F. In panel E, the reduction in DeltaF in the presence of the second low-pH pulse is steeper in the WT than in the KO. Can this be explained? In essence, these data in their present state are not sufficient to draw unequivocal conclusions regarding reacidification. The authors should include controls with bafilomycin, to understand whether the slopes they measure are actually reporting reacidification.

5. Reacidification kinetics are not resolved, yet are reported as a single parameter of an exponential fit. Furthermore, when the acid was removed, the KO cells should have had higher fluorescence, since it is decaying more slowly (e.g. difference WT vs. KO at the 80 s time point). The acid quenching experiment showed no difference. Given that the authors are not resolving an exponential decay of the acid-quenched surface signal, it would be more appropriate to simply report what fraction of the signal early on after the end of the stimulus – where there is a real difference in the amount of the signal that has decayed (e.g. at the 60 s time point) – can be quenched by acid perfusion. If it is the same fraction for WT and KO, the differences are not explained by the build-up of an alkaline pool, which is really what the authors want to assess here.

6. It is important to know if the phenomena described in the present study occur under physiological conditions (i.e. 37{degree sign}C, ~1.25 mM Ca). The temperature in particular is important as cooling can substantially distort the relevance of different molecular processes. The reviewers do not expect a repetition of all experiments at 37{degree sign}C. The easiest might be an experiment on pHluorin assessment of vesicle recycling in neurons, showing that at 37{degree sign}C there is a measurable impact on the pHluorin recovery kinetics due to the absence or presence of external Ca2+.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "TRPM7 is critical for short-term synaptic depression by regulating synaptic vesicle endocytosis" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Lu Chen as the Senior Editor.

Your manuscript has been very substantially improved. However, the reviewers have identified three issues that need to be resolved before the paper can be published in eLife:

1. The new confocal images added to Figure 3 (supplement 3, panels A-D; supplement 4, panels A, C, E, G) and to Figure 4 (supplement 2, panel C) are of very poor quality (very low resolution, blurred, pixelated) and do not look like confocal images (rather like ones that have been improperly digitally compressed). In fact, the new panel C in Figure 4, supplement 2 appears to be of even less resolution than the original images in panel A. In essence, the problematic panels indicated above are not of publication quality and need to be redone.

2. The description of confocal microscopy in the methods part is insufficient and requires more detail (i.e. numerical aperture and type of objective, light source, pinhole setting, etc.).

3. Regarding Figure 5, supplement 1, it seems that the 340 nm images in panel A are saturated. If so, it would be impossible to do a ratio analysis as shown in panel B. This issue needs to be explained and resolved.
