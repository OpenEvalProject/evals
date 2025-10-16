# Peer review - Round 1

Editors:
- Mark T Nelson, https://ror.org/0155zta11 University of Vermont United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72802.sa0](https://doi.org/10.7554/eLife.72802.sa0)

This paper will likely be of keen interest to researchers investigating vasculo-neuronal coupling – a proposed signaling mode opposite that of the more widely studied neuro-vascular coupling process. The optogenetics method described, inspired by methodology developed for interrogating ensembles of neurons, effectively enables simultaneous manipulation and monitoring of brain arteriole contractility in three dimensions.


---

# Peer review - Round 1

Editors:
- Mark T Nelson, https://ror.org/0155zta11 University of Vermont United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72802.sa1](https://doi.org/10.7554/eLife.72802.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Precise, 3-D optogenetic control of the diameter of single arterioles in vivo" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mark T Nelson as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Anna Devor (Reviewer #2); Ravi Rungta (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The red-shifted opsin, ReaChR, represents an improvement over opsins used in previously described 3D neuronal activation/monitoring systems. In particular, brief single-photon stimulation (100 ms) of ReaChR led to rapid, robust arteriole constrictions throughout the activation volume, whereas a previous generation ChR2 opsin required stimulation for seconds to achieve slowly appearing constrictions.

2. Single-photon stimulation was capable of completing stopping blood flow in a "first order pre-capillary branch". (Not clear what is meant by the phrase "pre-capillary branch"; anatomically, penetrating arterioles feed capillary branches.) While this speaks to the effectiveness of the method, it also highlights potential supraphysiological effects of stimulation and the importance of titrating stimulus intensity/duration to achieve physiologically meaningful responses.

3. In assessing effects of laser power, the authors assert that "increasing the laser power only slightly expanded the range of constriction". This seems a bit of an overstatement, given that increasing power (30-fold) had a greater effect on the spread (3x) than the magnitude (2x) of the response.

4. The suggestion that penetrating brain arterioles possess a mechanism for upstream conduction of constrictive responses is intriguing (although this intrigue is tempered by the lack of experimental support for the operation of such a mechanism in the brain microvasculature).

5. The authors' premise for comparing contractile kinetics with sensory-evoked kinetics has issues. In attempting to use the kinetics of optogenetic-induced constriction to infer something about the kinetics of sensory-evoked dilation, they are implicitly assuming that the kinetics of contraction and dilation processes intrinsic to mural cells are the same. This is highlighted by their use of the phrase "kinetics of the vasculature", which elides the possibility that dilation and contraction kinetics intrinsic to mural cells are different. Support for this latter possibility is provided by a previous report on renal afferent arterioles showing that the kinetics of myogenic constriction in arterioles are "substantially faster" than those of dilation (PMID: 24173354). Thus, their data do not rule out the possibility that the delay between sensory stimulation and vascular response reflects a slower intrinsic dilatory response rather than the time course of neurovascular coupling mechanisms. Furthermore, arterioles have an internal elastic lamina (IEL), which also determines the rates and degree of constriction and dilation. The IEL ends with the arterioles, and vessels with ensheathing contractile pericytes (and downstream) lack the constraints of the IEL.

6. It's not at all clear how overriding sensory-evoked dilation with optogenetically generated constriction provides a means for distinguishing neural activity from vascular responses. In particular, it is not clear how performing this maneuver while monitoring neuronal activity can provide the suggested insight into "aspects" of functional hyperemia that are essential to neuronal function beyond the relatively trivial observation that there is a point at which blood flow is too low to support continued neuronal activity.

7. Presentation of high vs. low numerical aperture (NA) effects on X-Y and Z resolution is muddled. For high NA, the authors emphasize that the spread of constricting effects is greater in the Z plane than the X-Y plane. For low NA, they note "constrictions over a larger Z-range" (apparently compared to high NA but not clear), without indicating what the spread is in the X-Y plane. This leaves an apples-to-oranges comparison: greater spread in the Z plane compared with X-Y plane for low NA on the one hand versus greater spread in the Z plane with high NA compared with spread in the Z plane with low NA on the other. Need to show the same data for low and high NA (or make the rationale for the comparisons they do show clearer).

8. The authors write in very vague terms about potential applications of their methodology. They should make a greater effort to think through possible experimental applications and clearly present them.

9. Given the chronic nature of the optical window, it is not clear why imaging was done under anesthesia. This point requires explanation. There is a concern that targeting of the vessel wall not possible in awake animals due to brain motion. If yes, that would be a serious limitation of the methodology.

10. A major limitation of the technique is the poor axial point spread function of the SLM ReaChR activation. Although it is to be expected that the axial PSF is worst than the lateral PSF, the results are quite dramatic (with arteriole constriction being triggered when the SLM pattern is focused 150um from the arteriole, and at equivalent magnitude 200um away with the 0.8NA objective Figure 5-1). I think these experiments are important, but it would be helpful to provide some more control experiments to further characterize and help resolve the reason for this effect.

11. The bleach spots from their control experiment with the SLM focused 200um above or below the imaging plane, are not nearly the same size as the large axial PSF of the evoked constriction. One difference between the bleaching experiment and the SLM stimulation is that in the case of the SLM stimulation multiple spots are generated. Would it be possible to perform the bleaching control using the exact multi-spot pattern used for the experiments to ensure the multi spot pattern is not causing the SLM to generate a weird pattern in the z-plane?

12. Is it possible that there is still some 1-photon activation of ReaChR at 1040nm? This may be unlikely, but from the spectrum I found (Lin et al., 2013, PMID: 23995068), it was only tested up to 650 nm and the spectrum is quite broad with significant current evoked at all wavelengths tested.

13. If it is truly due to 2P activation generated within the cone of light, then this suggests that far higher power than necessary is being used (see work by Rickgauer and Tank – PMID: 19706471). In Figure 4 for example, the authors are able to trigger a nice local constriction with 5mW total spot power (>20 times less than is being used in the other experiments). If the same axial precision experiments are done with lower power does the constriction "PSF" decrease in width? Consistent with this idea, what is the result if the authors bypass the SLM and make a point scan 200um above the vessel at 115mW? Do they still trigger a constriction due to excitation with the cone of light? Finally, if the authors perform the experiment in Figure 3D (where they show nice xy precesion) and were then to move the focus of the SLM up in the z-plane, would they maintain this lateral specificity across the z-plane? It is important to properly characterize this axial "PSF" to establish power limitations for future studies.

14. Also as stated in the public review, although the authors state numbers of mice tested in the figure legends, the paper seems to be mostly composed of representative examples without quantification of the results across the other mice on which the method was tested. It is important to provide the average numbers and variability of all the experiments (either directly in the figures, or in the main text). Without this information, it is not possible to get a sense of reproducibility and variability.

15. The authors make comparisons between ReaChR and ChR2, although vascular dynamics are not directly compared between the 2 opsins using the same stimulation paradigm (e.g. line 94, This robust constriction (~20% from baseline level) to such a brief light stimulation is in stark contrast to activation with ChR2, where sustained stimulation over seconds was required for slow constrictions to appear (Hill et al., 2015; Tong et al., 2020a; Hartmann et al., 2021)), Although I appreciate that ReaChR may be preferable, the difference in kinetics of their vascular response is likely predominantly due to the nature of the stimulation (raster scanning vs. flood illumination or SLM) used here, rather than a difference in the opsin (ReaChR vs ChR2) as stated in this sentence. Supporting this thought, previous work has indeed shown rapid dilations and constrictions induced by activation of excitatory and inhibitory opsins with single photon epi-illumination (e.g. Abe et al., 2021, PMID: 34320360; Mateo et al., 2017, PMID: 29107517). The authors should modify the text appropriately. It would also be a nice (although not ultimately necessary) addition to compare their results with the SLM to raster / line scanning 2P activation of ReaChR on arterioles.

16. The mouse line used in this paper results in ReaChR expression in pericytes in addition to SMCs. The study would benefit from a brief description of what happens when they stimulate capillary pericytes with the SLM in comparison to their recently published results (Hartmann et al., 2021 – Nat Neurosci)?
