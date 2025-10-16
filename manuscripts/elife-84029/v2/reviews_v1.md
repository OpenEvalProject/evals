# Peer review - Round 1

Editors:
- Gary L Westbrook, https://ror.org/009avj582 Oregon Health & Science University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84029.sa0](https://doi.org/10.7554/eLife.84029.sa0)

This manuscript addresses the potential value of a "tagged" version of iGluSnFRs with the idea that this approach provides a more localized measure of glutamate release at synapses. Although the new sensor does not have an increase in signal-to-noise ratio, the authors nicely address the potential advantages and limitations of their sensor and the experiments provide an important test of the localized expression of such a sensor.


---

# Peer review - Round 1

Editors:
- Gary L Westbrook, https://ror.org/009avj582 Oregon Health & Science University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84029.sa1](https://doi.org/10.7554/eLife.84029.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Targeted sensors for glutamatergic neurotransmission" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a myself as Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kevin J Bender (Reviewer #3).

Comments to the Authors:

We are sorry to report that, after a joint discussion with the reviewers, we have decided that your work will not be considered further for publication by eLife. The reviewers understood the potential value of the approach to develop a synaptically targeted version of iGluSnFR, but raised a number of technical and conceptual issues that we think would require more than modest revisions to support the conclusions.

Reviewer #1 (Recommendations for the authors):

Hao et al. targeted the genetically encoded glutamate sensor iGluSnFR to synapses by fusion with auxiliary subunits of the AMPA receptor, y2 (stargazin) and y8. They report decreased affinity and increased response stability compared to non-anchored iGluSnFR. Early infection with SnFR-γ2 (or just stargazin) blocked EPSCs, suggesting that AMPARs were displaced from their postsynaptic sites. This effect was less extreme when cultures were transfected late (DIV6), but currents were still down by 50% compared to iGluSnFR-transfected neurons, while presynaptic function appeared to be normal.

To analyze the imaging data, the authors developed a strategy to use the signal (stimulation-evoked increase in fluorescence) to select their regions of interest. This allowed them to identify sites of glutamate release, but is not an unbiased sampling of the synaptic population. The authors show only one example of colocalization with homer (Figure 3a), leaving some doubt as to what fraction of indicator molecules was successfully targeted. For a well-targeted indicator, it should be possible to use resting fluorescence spots to select ROIs.

During repeated stimulation at 5 Hz in 2 ca2+, SnFR-y2 produced stable responses while iGluSnFR responses decreased. EPSCs in SnFR-y2 neurons were smaller (Figure 4C, note split axis) but displayed similar short-term plasticity (Figure 7C). Comparing neurons, SnFR-y2 was highly correlated with short term facilitation / depression while iGluSnFR signals were not. The authors speculate that the poor correlation of iGluSnFR is due to run-down, but this would manifest as exaggerated depression, not spurious facilitation as the data suggest. So the reason for the improved performance of SnFR-y2 is not entirely clear. The authors then use the SnFR signals to analyze single synapses in autaptic culture. They show very nicely that the glutamate output is a function of extracelluar ca2+, providing direct proof for multivesicular release at individual synapses. Full optical quantal analysis requires measurable responses to the release of a single quantum, which SnFR-γ2 and SnFR-γ8 do not seem to provide (Note that the spontaneous fluorescence transients recorded without TTX (Figure 2) are potentially multivesicular events).

In summary, the improvement of the new variants compared to iGluSnFR could be due to their decreased affinity for glutamate, resulting in selection of the strongest synapses and very focal signals, but lack of sensitivity to the fusion of a single vesicle. The price to pay for synaptic targeting, strong alteration of postsynaptic receptor composition, seems relatively high and may prevent widespread adoption of the new variants.

Concerns:

1) Synaptic targeting: The appearance of the targeted indicator is punctate, but the ROIs that were selected by their signal often have no higher resting fluorescence than their surroundings (Figure 2) while the brightest spots apparently produce no signal. By co-expressing homer, the authors tried to quantify colocalization, but show only one single SnFR-y2 spot (n=1) that is colocalized with homer. (As a side remark, iGluSnFR SIGNALS should also be colocalized with homer, but the example is not). In the text, they state that the complexity of expression (?) precluded colocalization analysis. Thus, in spite of the author's efforts, evidence for successful synaptic tagging is lacking, and the schema presented in Figure 9 (88% of SnFR-y2 inside PSD) seems optimistic. All differences in y2-sensor responses compared to iGluSnFR (e.g. spatially restricted responses) could be due to its reduced affinity for glutamate and in consequence, selection bias towards the most powerful synapses.

2) Run-down of iGluSnFR vs. stability of SnFR-y8 (Figure 6): As SnFR-y8 has a lower affinity for glutamate than iGluSnFR, the ROI detection algorithm finds fewer active pixels on SnFR-y8 neurons. I would expect these to correspond to the strongest and most reliable sources of glutamate. iGluSnFR with its higher affinity will also pick up synapses with a small pool of release-ready vesicles. Small synapses are likely to display pronounced depression during a train. So, the stability of SnFR-y8 responses might reflect a selection bias for the strongest synapses. Figure 6g does little to rule out this possibility, since the size of the compound ROI does not reflect the strength of the synapse (but may pool the response of several synapses). The interpretation of the authors, that synaptic targeting somehow stabilized the fluorescence of the SnFR, I find much less likely. Another scenario that cannot be ruled out is stronger illumination of the iGluSnFR cells (perhaps due to low expression levels), resulting in increased photobleaching during the stimulation train. To monitor indicator bleaching, the resting fluorescence (F0) during the train should be reported for both indicators. In figure 6e, fluctuations in the time course are highly correlated across ROIs, which points to an artifact (non-stationary stimulation or illumination). To solve the mystery of run-down, it would be very helpful to see the EPSCs generated by this stimulation in iGluSnFR and in SnFR-y8 neurons.

3) Quantal analysis: As the biological meaning of the quantal parameters is best defined in single synapses, I will first comment on the single synapse experiments (Figure 8, Figure S6, Figure S8). The authors analyze single ROIs at three different calcium concentrations, resulting in increasing response amplitudes. This is interpreted as multi-vesicular release from a single synapse. While I follow this general interpretation, it seems the sensitivity of sensor/imaging system is not sufficient to detect the release of individual vesicles. In 0.5 mM ca2+, the recorded SnFR-y8 traces show no difference between simulated and non-stimulated epochs, strongly suggesting that the fluctuations in fluorescence intensity are noise. Consequently, the histograms of 0.5 mM ca2+ responses show no separation between failures and sucesses, just a single peak. To assume that this peak corresponds to the release of a single vesicle, the quantal response (q), is wrong. The example traces from iGluSnFR at 0.5 mM ca2+ look slightly more promising (Figure S6), but again, the histogram does not show a separation between failures and successes, and the compound histogram treats the entire first peak as the quantal response (i.e., assumes there were no failures in 0.5 mM ca2+). A method that lacks the sensitivity to detect single vesicle fusion is not useful for quantal analysis: Due to increasing variance and indicator saturation, the separation between multi-vesicular events will be less clear, not better, than the separation between uni-vesicular events and failures.

4) Quantal analysis of autaptic connections (Figure 7): The authors use the CV method developed for paired recordings, which seems appropriate for an autaptic neuron. Compared to the analysis of single synapses, the meaning of N is less well defined here. Early studies assumed that one synapse can only release one vesicle at a time, which makes N the number of connecting synapses and Pr the synaptic release probability. For autaptic cultures, multi-vesicular release is established, so N is the number of "release sites", several of which can be located in a single synapse. Thus, N must be larger than the number of recorded synapses, which in this case is the number of ROIs.

It is very difficult to understand Figure 7. Trains of 5 AP are evoked at 5 Hz ten times in 3 different Ca concentrations and recorded in an unspecified number of ROIs (synapses). In panel c, facilitation/depression during the train is compared for electrical and optical recordings. I assume these points (n=6) correspond to different cells, not different ROIs (please indicate the point corresponding to the cell analyzed in panels a and b). SnFR-y2 responses are better correlated with the electrical responses in 2 and 4 Ca, but SnFR-y2 synapses tend towards depression compared to iGluSnFR synapses. This population difference in EPSC dynamics raises the nasty possibility of presynaptic effects caused by SnFR-y2 expression (but due to low sample size, may just be a fluke).

In Figure 7D, mean and standard deviations are calculated, but the basis is not clear. I am assuming each ROI produces 5 points in panel D, each averaged over the 10 repeats. It would be helpful to explain this more clearly. The CVs (slopes in panel D) are related to N and Pr. As the authors state, they end up with 3 numbers for an equation system with 4 variables. It is not clear to me how fitting can help in this situation (as there should be no error, regardless which number is chosen for N). So perhaps panel F shows the numbers they chose for N, perhaps based on the number of ROIs? (The legend of F is cryptic. Please indicate in E and F which points correspond to the cell shown in D.) This would be based on the assumption of univesicular synapses, though, which they refute in Figure 8. In any case, they point out that this N is similar to the N reported by Bekkers and Stevens, who were interested in the number of release sites connecting two neurons. The numbers (N = 4-7) seem very low for a connection producing 2 nA EPSCs (400 pA per uniquantal synapse?). It could of course be argued that the autaptic connection is made of many more synapses than the few that are sampled optically. The N determined by optical quantal analysis, however, has to be higher than the number of ROIs (active synapses), it cannot be lower. If the N is assumed to be equal to the number of ROIs (uniquantal synapses), it makes no sense to call the process quantal analysis (as in this case, the distribution of N values (Figure 7F) is not the result of any fitting procedure). Without understanding the basis of N, I cannot interpret the meaning of Pr (synaptic? vesicular?).

Suggested improvements:

Provide conclusive evidence for successful synaptic targeting, e.g. by homer/y2 co-transfection of individual neurons and high-resolution imaging. Targeting is expected to be most specific at low expression levels.

I am not sure how to improve the quantal analysis (more excitation light?). A symmetrical failure peak should appear exactly at df/f = 0 which is absent from all histograms. Perhaps the problem is background subtraction (leading to division by zero) or the handling of negative df/f values. If there is no way to separate failures from low probability release events in individual trials, I will remain skeptical about multi-peaked compound histograms apparently separating 4 from 3 simultaneously released vesicles.

Please commit to a clear definition / interpretation of the extracted parameters from the coefficient of variance method, specifically in relation to the number of ROIs. At present, the biological interpretation of N and Pr with respect to autaptic synapses is unclear, at least to me.

Reviewer #2 (Recommendations for the authors):

1. According to the authors, one principal advantage of their approach is that SnFR-y2/8 provides a more 'spatially precise' signal compared with iGluSnFR. Clearly, an optical sensor that is proposed as expressed within a nanoscopic membrane domain will yield a more spatially constrained signal compared with the sensor expressed evenly over cell membranes. However, this simply reflects the sensor distribution properties rather than anything else. In words, SnFR-y2/8 will tend to report the brightest glutamate signal where SnFR-y2/8 is accumulated, rather than where the glutamate concentration is highest (e.g., release site proximity). In contrast, the sensor homogenously distributed in space, such as the original iGluSnFR variants, should provide unbiased readout of glutamate hotspots. It appears therefore that the authors strategy is somewhat self-defeating.

2. The authors use TIRF imaging, and single-line diode lasers as an excitation source. This type of imaging is only suitable for monolayer cultures: whether their sensor will be efficient when imaged in organized brain tissue using two-photon excitation is not clear. The claim on a methodological advance appears therefore premature.

3. The other key statement is that iGluSnFR is prone to photobleaching (rundown) more than is SnFR-y2/8. First, fluorophore's photobleaching properties in 1P as opposed to 2P mode could be very different, which has not been addressed or explored. Second, this observation is surprising because several recent studies have documented a fairly stable iGluSnFR signal over multiple cycles of glutamate release imaged at 'quantal' resolution, both in 1P and 2P excitation regimes, both in cultures and in acute slices (e.g., Tagliatti et al., 2020 PNAS 117: 3819; Jensen et al. 2019 Nat Commun 10: 1414). The authors do not seem familiar with these studies. Dye photobleaching depends on multiple imaging parameters starting with laser power: this has not been investigated consistently in the present work.

4. Stargazin overexpression has been used as a principal tool for the iGluSnFR targeting to synapses, but the authors report that this renders a proportion of synapses nonresponsive to glutamate (Figure 4). That the method interferes with the physiological integrity of synaptic circuits, or at least requires some additional experiment-specific manipulations to minimize it, does not speak in its favor.

5. The signal-to-noise ratio of the SnFR-y2 signal does not appear improved compared with that of iGluSnFR (Figure 8A).

6. The quantal-analysis histograms presented here (Figure 8C-D) appear noisier hence less reliable than similar or related analyses in the aforementioned publications that employed iGluSnFR.

Reviewer #3 (Recommendations for the authors):

Hao and colleagues developed new variants of the glutamate sensor iGluSnFR, termed SnFR-γ2 and SnFR-γ8, that are fusion proteins with postsynaptic density (PSD) proteins Stargazin and γ-8. This chimeric protein thus localizes specifically at the PSD. These new variants are characterized, using heterologous expression systems and hippocampal neuron microisland cultures, allowing one to monitor autapses with simultaneous electrical and optical access. Overall, SnFR-γ2 outperforms traditional iGluSnFR in terms of signal localization; presumed single synapses are observed with limited "spillover" of signal to neighboring regions, and imaged transients are amenable to traditional noise analysis. Some concern regarding competition for PSD membrane is raised due to overexpression of these variants, but it appears that such overexpression artifacts can be avoided by ensuring that SnFR-γ2 is delivered after synapses are largely formed. This could be an important tool for the field, as it improves one's ability to resolve the activity of single glutamatergic synapses with sufficient signal to noise. Work here has shown feasibility in cultures systems. Future work will need to show similar performance levels in acute slice and in vivo, though based on past observations with iGluSnFR, this performance is likely within reach.

The main question I have is one of extensibility: can this approach work in more intact systems, or even in vivo? I recognize that asking such a question involves an entirely new dataset, and am not proposing that the authors engage in such an effort after already doing an excellent job characterizing these GluSnFR variants. Rather, I'd hope that the authors would expand on their discussions, which is largely focused on questions of release dynamics observed with their sensors, to also include potential technical advantages or limitations of these variants in other preparations.

Comments below are aimed at improving interpretation of data reported herein:

1) A control for infection is needed for autapse data. Please make parallel recordings in cells infected with control viruses that lack any glutamate sensor to determine if these currents are in the normal range at these ages.

2) Data in Figure 5C and F should be analyzed quantitatively by calculating correlation coefficients for each pair of data. If there are differences in the relative separation of each region (I understand that these were chosen by hand) then a potential comparison could be made by plotting correlation coefficients vs. centroid distance of paired ROIs.

3) Data in Figure 7C, 0.5 mM. There is an obvious outlier near 7 P5/P1 for the SnFR-gamma2. This is likely due to a very low P1 value for this one cell, indicative of excess failures. I'd be curious to know if any correlation holds if this one datapoint is held out of the dataset. If so, perhaps the authors could explain this observation in the main text.

4) Figure 7, data related to optical quantal analysis. Considering that these are autaptic recordings, with superb electrical access, one should be able to perform traditional electrophysiological quantal analysis and determine whether SnFR is allowing for identification of all synapses. This is a critical analysis that should be made on a cell-by-cell basis, paired with optical analyses; however, if this is not feasible at this time, some information could be gleaned from separate recordings, given that you observed fairly consistent numbers of sites optically (4 to 7). This would address your concern that the detection methods bias towards high Pr synapses. Though, if there are more synapses made a significant distance from the coverslip, then they would never be imaged under TIRF microscopy, obviating this request.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Targeted sensors for glutamatergic neurotransmission" for further consideration by eLife. Your revised article has been evaluated by Gary Westbrook (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

This manuscript is an attempt towards synapse specificity for glutamate probes. The current probe's utility is limited to specific cases, and it has what could be considered advantages and drawbacks, even in that specific case (CMOS imaging of cultured cells). It is commendable how carefully the authors characterized side effects of this sensor on synaptic function. The reviewers agreed that several issues require clarifications in the text.

1. Please explain that any glutamate rises or waves in the tissue, any significant glutamate spillover signaling, or even fluctuations in tissue optical conditions, could be falsely perceived as local synaptic signals by an PSD-constrained sensor rather than by an evenly distributed sensor. This is a key limitation of the current method.

2. The authors seem to insist that the use of iGluSnFR or any sensor labeling is generally disadvantageous. It is advantageous in most cases. In terms of this sensor's fluorescence properties, there is no evidence for improved performance in the manuscript.

3. Please consider the specific points raised by the reviewers and address them in the text to the extent possible.

Reviewer #1 (Recommendations for the authors):

The authors have provided their explanations and rebuttal regarding the previous comments, albeit without new experimental evidence.

1. It appears that the authors did not fully understand the main objection. Or perhaps it was not explained clearly enough. To reiterate: SnFR-y2/8 expressed locally at the synapse may in fact sense and report glutamate that is released elsewhere in the vicinity, thus giving a false impression of its local synaptic release. In other words, SnFR-y2/8 may report the spillover signal as well as the actual synaptic signal.

It is true that, in 2PE mode, in organized brain tissue, iGluSnFR will report optical signal integrated, due to diffraction of light, within the PSF depth of ~800 nm, etc., and thus may include glutamate release events, if any, from nearest synaptic neighbors. However, the same will happen if such neighbors express SnFR-y2/8: their optical signal will still be integrated within the diffraction-limited PSF in 2PE imaging mode.

In the case when no glutamate spillover ever occurs in the preparation of interest, both iGluSnFR and SnFr-y2/8 will report true synaptic signals when such happen. In this case, however, glutamate rises or waves arising from other sources, such as astroglia, will still be reported by SnFr-y2/8 very locally, giving an impression of local synaptic events – whereas iGluSnFR will report the entire glutamate 'landscape'. Thus, SnFr-y2/8 does not seem to have any principal spatial-resolution advantage over iGluSnFR.

2. Authors' attention is drawn to yet another recent publication (Mendonca et al. 2022 Nat Commun 3497) showing an excellent stability, S/N ratio, etc. for highly localized glutamate release events detected with iGluSnFR. That this sensor is performing not as satisfactory in the present authors' hands cannot be a basis for their extrapolated claim.

3. The authors concede that the S/N ratio of their probe readout is probably no better than that of iGluSnFR.

4. The authors have made no attempt to check their probe performance in 2PE mode and/ or in organized brain tissue.

5. The amplitude histograms shown in Figure 9C-D do not match satisfactorily the best-fit quantal analysis curves. While the authors acknowledge the difficulty, the reasons for displaying unsatisfactory quantal analysis data are not clear.

6. The entire concept would have made a much greater impact if the authors aimed to express the sensor at a specific, functionally or genetically distinct, sub-population of synapses.

Reviewer #2 (Recommendations for the authors):

The authors have addressed concerns raised by all three reviewers to the best of their ability. Their commentary that untagged SnFR is likely detecting large hotspots of both synaptic and spillover is taken well. Though the concern regarding how well the tagged variant works remains in question. If one can only resolve a few synapses (less than 10 per cell were analyzed) of what the authors suggest are ~100 potential autapses, are these few ROIs representative of the whole? This may be a good point of discussion.

Given the way in which eLife is modifying its review process and overall publishing criteria, this work should be accepted. It represents a new tool that is well characterized. Advantages and flaws are discussed well.

Reviewer #3 (Recommendations for the authors):

In their revised version, the authors address questions about synaptic localization of their GEGI by demonstrating good overlap with the PSD95 signal (new Figure 3). The explanation of Figure 8 has been much improved, quantal parameters are now well defined. The correlation between electrical and optically measured depression during a train (Figure 8c) is indeed much better for their targeted indicator compared to iGluSnFR, which is a strong argument that synaptic (and not extrasynaptic) glutamate is reliably measured by their sensor. In this context, it is an advantage of the autaptic model that all synapses on a given neuron have the identical history of activity and therefore express similar (but cell-specific) short-term plasticity. I do not like the analysis of rundown in Figure 7F: Splitting a continuous distribution into 2 groups, using an arbitrary threshold, then counting the number of cases (ROIs) on either side of the threshold, is not good statistical practice. The analysis in Figure S5 I like much better, it shows no significant difference between the two indicators. As the authors cannot offer a convincing mechanistic explanation why a difference in rundown would be expected, I suggest downplaying this point (getting rid of Figure 7E-G, sticking with the message of S5).

Apart from this quibble, the science is sound and well presented. The separation of quantal histogram peaks is impressive and certainly aided by localizing the indicator to the places of highest glutamate concentration. Extrasynaptic indicator molecules, exposed to a near-continuous range of glutamate concentrations, would be expected to widen the peaks considerably (as shown in the iGluSnFR example in Figure 9c). For future tool development and targeting efforts, the technical information and precise measurements are very useful, even as a somewhat cautionary tale with regard to potentially severe side effects of tool expression.
