# Peer review - Round 1

Editors:
- Christian Rosenmund, Charité-Universitätsmedizin Berlin , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03658.011](https://doi.org/10.7554/eLife.03658.011)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Fast retrieval and autonomous regulation of single spontaneously recycling synaptic vesicles” for consideration at eLife. Your article has been favorably evaluated by Eve Marder (Senior editor) and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and all felt that this work is interesting, providing novel approaches and insights in vesicle exocytosis.

The reviewers felt that the following major points of analysis and interpretation are however needed to be adequately addressed to publish at eLife.

1) Quantification. How tightly linked are simultaneously occurring pre- (single vesicle release) and post-synaptic (Ca imaging) spontaneous events? Only postsynaptic events that follow immediately after presynaptic events are of relevance.

2) How well can different release sites (or nearby boutons) be separated? Are multiple vesicles being released from one bouton within 120 ms (if so, please do not call this multiquantal release, which is more in the time scale of one's and tens of millisec: that is confusing)?

3) Are events from spontaneous and evoked release really different? One potential test: Do the evoked release events also correlate with a Ca signal that is driven by NMDARs?

4) There were also significant concerns about the histogram analysis and multiquantal release conclusion. It was unclear why a fixed delay between two sequential release events was used while alternative hypothesis (that these events are just a bit larger and the distribution is not exactly normal) was not considered simpler? At least the alternative interpretation should be discussed. Also, it is essential that the fusion frequencies (Figure 5) are recalculated using the actual number of detected events (regardless of amplitude), so that the frequencies are not dependent on a specific interpretation such as multivesicular release.

Please find below the initial reviewer comments that led to the consensus view above. There are additional issues in these reviews that should also be addressed.

Reviewer #1:

This is an excellent and very interesting paper that reveals several striking differences between spontaneous and evoked vesicle retrieval and reacidification rates. The data analysis is convincing and carefully performed. A surprisingly fast rate of vesicle endocytosis and reacidification is shown after spontaneous fusion events. The results are of fundamental importance for an understanding of CNS synaptic transmission. Together, these results present a strong case for major differences between spontaneous and evoked vesicle recycling and acidification rates.

Major:

1) Results section: For the average decay time constant (e.g. 3.7s) and median decay time (e.g. 0.28) please add an error bar to these numbers as you have done elsewhere in the Results section.

2) Results section: For how long are the neurons bathed in the 50 mM TRIS solution before experiments are performed?

3) In Figure 5C what was the average frequency of the spontaneous fusion events in 2 mM Ca and in 8 mM Ca? Please give the average number with error bar. It seems like a 3-fold increase in frequency. Also, what is the average increase in spontaneous mEPSC frequency from 2 mM external Ca to 8 mM external Ca? This seems like an easy experiment for the authors to conduct and it would be very interesting to compare the numbers of this change to the numbers from the imaging data.

4) Change the first paragraph of the Discussion into three paragraphs.

5) Why not try the experiment in Figure 1 with an external solution that is based on 25 mM bicarbonate (a more physiological pH buffer)? Is there a problem with exchanging the HEPES-based solution of the cultures with a bicarbonate-based solution and then performing the experiment of Figure 1? A vesicle that recycles with 10 mM HEPES in its lumen may have a different pH buffering than one with 25 mM bicarbonate. If an experiment cannot be performed with bicarbonate then some discussion of this issue should be given in the text.

6) What is the CV of the distributions in Figures 1C, 1H and 1K? Seems like a CV of about 0.4-0.5, which is close to that of mEPSCs. It would be interesting to know how well these match each other.

Reviewer #2:

The authors use Phluorin imaging to detect spontaneously fusing vesicles and determine their reacidification kinetics, as well as their calcium-dependence. The study is well performed, the detection of spontaneous release using pHluorin constructs is impressive and overall believable, and the authors reach conclusions, which are important and interesting for the field. However, there are some points that require clarification, which will include more analysis, and the interpretation regarding multivesicular release appears not sufficiently supported (details below).

Major points:

1) A major point is that it is not clear that the optically detected 'spontaneous events' really represent fusion of synaptic vesicles, and not for instance fusion of endosomes. The authors in principle address this point elegantly by co-expressing a fluorescence calcium-indicator (GCaMP5K) fused to PSD-95 and doing dual-color imaging. This is a nice approach, but from the text and analysis presented it does not become clear whether there was a tight correlation between pre- and post-synaptic events, and therefore there is not enough evidence for the conclusion: “...spontaneous fusing vesicles elicit postsynaptic Ca2+ signals”. For instance in Figure 2B: are those events (red and green channel) detected simultaneously? How often did spontaneous increases in the red channel correlate with increases in the green channel? How many events in the red channel did not coincide with events in the green channel? The authors could calculate and plot the waiting times between sequential red and green events at identified synapses. If the authors are right, such a plot should have a peak at very short intervals. Finally, the authors write “Spontaneous increases in fluorescence that were correlated (within {plus minus} 1 s) with Ca2+ signals..” I do not understand the {plus minus} here: presumably the relevant events would be those were the red event would precede (or coincide with) the green event, not the other way around. Overall, the authors need to present additional analysis of these data.

2) I am skeptical about the conclusion that the larger amplitudes of events at higher calcium concentrations are due to multivesicular release (Figure 3, text in the Results section). The larger events in the presence of higher calcium concentration could be because of the preferential fusion of slightly larger vesicles under these circumstances (or even due to a change in the photophysical properties of pHluorin). The author's argument doesn't make sense to me: “It is unlikely that this increase in fluorescence is due to variation in the number of pHluorin molecules, as the increase in amplitude is observed when extracellular Ca2+ concentrations are increased.” Why not? The histogram of event sizes could not be fitted with a single Gaussian, but who is to say whether spontaneously fusing vesicles exactly follow a Gaussian distribution? The three distributions at 1q, 1.3q and 2q are not visible as peaks in the histogram at all; especially the fit of a distribution at 2q appears unreasonable. Finally, the suggestion that events with normalized amplitude at 1.3 q would result from multivesicular release of two vesicles with a fixed delay (118 ms) appears unreasonable; what mechanism would ensure that multivesicular release would happen always with this delay, especially as this is spontaneous release? I think the authors should remove this interpretation, which has consequences also for the interpretation of Figure 4 and for the rates reported in Figure 5 and possibly in Figure 6.

3) The authors use the lack of a correlation between decay time and amplitude as an argument that “there is a fundamental difference in the kinetics of endocytosis and reacidification between vesicles that fuse spontaneously and those that fuse in response to stimulation.” But I would argue that this finding, together with the previous work of the authors, Leitz and Kavalali, 2001 is an argument against the interpretation of multivesicular release.

4) To follow up on the last statement above in point 2, to estimate the fusion frequencies (reported in Figure 5) the authors “counted all events with amplitudes within the first quantal mean as a single event, and events with larger amplitudes as two events”. This is not appropriate, first because it is not clear whether larger events represent multiple events, and second because the distributions at 1q and 1.3q overlap. The authors should only use the number of events that they can detect as such, independently of amplitude. The same goes for Figure 6, if the rates were calculated in the same way.

5) The correlation analysis in Figure 6B-D has not been described in the statistics section of the Materials and Methods. Was this Pearson's correlation coefficient? The R^2 is quite small, but nevertheless the slope is positive under all circumstances. The authors should add a statistical test of the hypothesis R=0, and report whether there is a significant (but small) correlation. Finally, the authors should explain why all evoked fusion probabilities are integer multiples of 0.1 (panel C, D), or 0.05 (panel B). Why this difference between the conditions? Finally, given that fusion probabilities can be measured in only 10 (C, D), or 20 (B) discrete categories, would non-parametric correlation analysis be more appropriate?

Reviewer #3:

In the current manuscript, “Fast retrieval and autonomous regulation of single spontaneously recycling synaptic vesicles,” Leitz and Kavalali investigate the retrieval and re-acidification of vesicles spontaneously released, and find that these events have a faster decay than single vesicles released with AP stimulation. Using dual color imaging, they also show that spontaneous events can elicit NMDAR-mediated calcium responses. Additionally, they show that multiple vesicles can be release spontaneously at a single release site, and that this occurs more frequently with increasing calcium concentrations, without showing a change in the pHluorin decay kinetics. They argue that the different release modes, spontaneous and evoked, may use distinct methods of endocytosis. Furthermore, as they show there is no correlation between the release probability of evoked events and the frequency of spontaneously released events at single release sites, they conclude that these are two functionally distinct vesicle pools.

Overall, this is a well-written and clear paper with many appropriate controls. The dual color imaging of the spontaneous release events and postsynaptic response are important and interesting, while some concerns exist and are discussed below.

1) Detection of single, spontaneous release events is a crucial technique for this paper. Though the amplitude distribution of the detected events looks convincing, it would also be useful to show how the distribution shifts when spontaneous release is blocked (i.e. with tetanus toxin incubation). Additionally, it is not clear how the noise events were detected. It would also be necessary to show how what the detection criteria discover when run with a negative amplitude (i.e. -2X the SD of the 17 points prior to the event).

2) For Figure 2, the correlation between the spontaneous pHluorin events and spontaneous Ca2+ events was stated to be {plus minus} 1 s. While the limitations for time resolution in the dual color imaging are expected, since the vesicle release should directly cause the Ca2+ influx, these events should really only be considered if the Ca2+ influx occurs in a time range after the detected pHluorin event.

3) Figure 2. What do the corresponding Ca2+ signals look like for the evoked SypHTomato events? Can they be more closely time-locked?

4) Figure 3. Multivesicular release events recorded by electrophysiology are thought to occur essentially simultaneously. The 1.3q events seem likely to be events happening with a 118 ms delay. Also to this point, how well resolved are the single release sites? Could the multiple vesicle release events be closely neighboring synapses, which happen to release vesicles in close temporal proximity? Also, are the multivesicular spontaneous events Ca2+ dependent? How do they look in the presence of Cd2+?

5) Figure 5. The frequency of spontaneous release events clearly increases in 8 mM Ca2+ in the presence of folimycin. The authors explain this as recruitment of very rapidly retrieved vesicles. However, does the frequency of spontaneous events also increase in folimycin with 2 mM Ca2+? From the Figure, it doesn't appear to, but it would be interesting to see.

6) Figure 6. This is an important figure for the authors' interpretation of the separate pools of vesicles (spontaneous and evoked) released with distinct properties at single synapses. However, a few issues could cloud the interpretation from the lack of correlation between evoked fusion probability and spontaneous release frequency. First, for an event to be considered evoked with a 1 s lag time from the stimulus seems too long even for asynchronous release with a single action potential. Second, there is again the issue of spatial resolution. Are these actually single release sites? Finally, the release probability (the calculation of which should be clearly stated in the text) seems very high for these synapses in 4 mM Ca2+. This could argue for the multiple release site measurement.

7) Figure S1. The increase in signal for the PSD-95-GCaMP5K is difficult to interpret, because it could be due to either the increased extracellular Ca2+ or due to the increased multivesicular release events. This could also be interesting to see in the presence of Cd2+.

[Editors’ note: further revisions were requested before acceptance, as shown below.]

Thank you for resubmitting your work entitled “Fast retrieval and autonomous regulation of single spontaneously recycling synaptic vesicles” for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor) and the original three reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

All three reviewers would like to see that all (new) analysis is properly implemented in the manuscript. Specifically, there are arguments that you made in your rebuttal letter that do not appear in the manuscript, but should. Moreover the reviewers generally all agree that support for multivesicular release is not that strong, and feel that this claim should be better balanced by dealing with caveats and alternative explanations.

Additional comments that surfaced in response to your revision are provided below:

1) Regarding detection of events, the authors added improved analysis. One reviewer would like to see addition of “false positive” events either from negative implement the detection (inversed) or from 0 Ca2+ to the histograms for amplitude and decay times. In addition, it would be helpful to subtract weighted average decay of false positives from weighted average decay of spontaneous events to obtain “net events”.

2) Coincidence of pre- and postsynaptic events: The detection of postsynaptic responses at the -1 frame will still be confusing to the reader, and additional clarification in the text is required. Given that the distribution of events puts most of them between 0 to 5 frames after stimulation, this is the time window that the authors should use for analysis. They will lose very few events and it will be more straightforward as it makes little sense that the postsynaptic signal should occur prior to the presynaptic signal. If the -1 frame events are to be included, the explanation for why these events would appear to occur before the stimulation, as included in the rebuttal letter must also be in the text.

Unfortunately, the postsynaptic signals coupled to the evoked Syp-Tomato signals are missing, and this is still an obvious gap in the paper. As the authors explain in the rebuttal letter, this is due to an understandable technical issues with field stimulation and network activity, although that the field stimulation itself causes a signal is strange when NMDARs are not blocked by Mg2+. Again, the authors should address this issue in the text. Pointing out to the reader that the recording the postsynaptic events with stimulation is technically difficult does not take anything away from the findings, and will also preempt questions from a reader who sees the comparison of the postsynaptic signals generated by evoked or spontaneous release as the obvious next step.

3) Release probability vs spontaneous release: There is only a 50% increase in the average spontaneous fusion rate with Ca2+ increase to 8 mM, while average release probability increases 3-fold. This figure could simply suggest that the release frequency of minis is much, much less sensitive to calcium than evoked release probability. This should be discussed by the authors.

4) Sensitivity to detect individual events/multiquantal release: Overall, the single site, multiquantal spontaneous release claim is still not convincing (or at least multiple release site cannot be ruled out convincingly). I do not understand how the Murthy et al., 1997 citation excludes the possibility that the authors are not detecting coincident release from neighboring synapses and not the multi-quantal events they report-particularly as the release probability they claim will result in individual sites in 2mM Ca2+ and this will be less likely occur as Ca2+ increases. Additionally, aside from the increase in release probability with increased calcium, other factors that contribute to ability to differentiate individual synapses include the density of synapse and the amount of binning.

The discrepancy between mEPSC frequency increase in electrophysiological recordings and optical recordings of spontaneous events (though small) could suggest the events reported as multiquantal are, in fact, neighboring synapses. It would be worth testing when the portion of the population of events with 1.3 q and 2 q amplitudes are treated as individual events from neighboring synapses, does the frequency increase of the optical recordings better match the electrophysiological ones.
