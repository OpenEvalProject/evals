# Peer review - Round 1

Editors:
- Gary L Westbrook, Oregon Health and Science University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51675.sa1](https://doi.org/10.7554/eLife.51675.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The study by Huang, Knoblich et al. represents an important contribution to the field, providing critical examination of in vivo 2-photon calcium imaging for the detection of underlying spike events. Overall, the work is very high quality. The demonstration that spike detection is ~15% under normal "low zoom" imaging conditions is a stunning observation that should be a wake-up call to large parts of the community. The results are somewhat sobering for investigators in the sense that no once-size-fits all strategy accurately extracted spiking in commonly-used conditions from fluorescence data.

Decision letter after peer review:

Thank you for submitting your article "Relationship between spiking activity and simultaneous fluorescence signals in transgenic mice expressing GCaMP6" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Karel Svoboda (Reviewer #1); Michael Higley (Reviewer #2); Bernardo L Sabatini (Reviewer #3).

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary

This manuscript explores an important topic with data that is difficult to obtain. All reviewers thought the manuscript was worth publishing in eLife after appropriate revisions. However all reviewers had concerns (some overlapping) that are important to address. Many of comments can be addressed with clarifications, rewording and better explanation/analysis of some aspects of the work. However, the manuscript contains some statements and conclusions that indicate incomplete understanding of sources of noise in the imaging experiments. This is important because the paper is really focused on detection. The full comments of the reviewers are below.

Reviewer #1:

Calcium imaging is widely used to track activity in large populations of neurons. Calcium-dependent fluorescence is often thought of as “activity”, but it is unclear what this means because the spike to fluorescence transform is not well understood. As a result the interpretation of calcium imaging data is often superficial and misleading. This is in part because ground truth data (i.e. simultaneous imaging and recording) is scarce. The major contribution of this paper is the report of a substantial bolus of additional ground truth data in several widely used transgenic mouse lines. This is hard-won data and I support publication. But some work is required first.

The take-home messages in this paper are: There are differences in spike detection across mouse lines, with 6s-expressing mice outperforming 6f-expressing mice. This is expected.

There are differences in detection across mice expressing the same indicator:

These differences across mice expressing the same indicator are not explained. My suspicion is that differences in neuropil (i.e. background) is likely the culprit (emx1 expresses in L4 – with lots of axons in L2/3; CamK2 does not). Explain this and the strange claim that the noise level is different in the emx1-s vs the tetO-s mice.

There is variability in the response to single spikes:

No attempt is made to distinguish interesting biological sources of noise (e.g. spike calcium coupling) to non-interesting biology (movement) and non-biological explanations (instrumentation). The paper would be stronger if the sources of noise were analyzed better. In particular, are the measurements done in a shot-noise limited regime? Does movement contribute? How about other instrumentation noise (shouldn't but still)?

Lower zoom imaging produces lower snr than higher zoom imaging

The section “Comparing spike-to-calcium fluorescence response curves imaged at high and low spatiotemporal resolutions” is also strange. It's not clear to me what exactly the point is here.

Obviously, everything else being equal, increasing the fov from 20 – 400 μm reduces the light dose per neuron by a factor of 400 and thus the SNR by a factor of 20 (see Peron et al., CONB 2015) just based on shot-noise alone! No one would image a 20 μm FOV with the same power as a 400 μm FOV.

Reviewer #2:

The study by Huang, Knoblich et al. represents a very important contribution to the field, providing critical examination of in vivo 2-photon calcium imaging for the detection of underlying spike events. Overall, the work is very high quality, and I have no concerns or suggestions with regard to data collection. I do have several major points on analyses that need to be addressed, detailed below. Overall, the work reads as if the major focus is the comparison of different transgenic GCaMP6 lines. While this topic is interesting, the far more important issue is the ability to estimate spiking from imaging data under "real world" conditions. Thus, far more emphasis needs to be placed on the "low zoom" data. The difference between the mouse lines is modest at best. However, the demonstration that spike detection is ~15% under normal imaging conditions is a stunning observation that should be a wake-up call to large parts of the community.

1) As noted, the high impact value of the study is on the "low zoom" data, as this represents the situation for the vast majority of experimental labs using GCaMP6. All analyses in the manuscript, including the examples comparing ΔF/F and spiking (Figures 1-6) need to be repeated for the low-zoom data. The analysis of neuropil correction is absolutely critical, as this may play a much larger role in the reduced spatiotemporal sampling regime. I would actually suggest making these analyses the major focus, rather than limited to Figure 7.

2) The paired statistical comparisons of single spike signals with a random period (e.g., Figures 4—figure supplement 1 and Figure 7—figure supplement 1) are not very informative. The fact that there is an average difference is far less important than the discriminability of true spikes from noise.

3) It is unclear how the 91 selected cells were chosen for "high quality recording and imaging". It would be useful to know how the results change for "lower quality" imaging, as this may better inform experimentalists on data collection.

4) The authors should make some attempt to explain why the spike detection is so much poorer at low zoom. Is it the fewer pixels per cell (factor of 16) or the lower sampling rate (factor of 4-5). Disambiguating these contributors would better help the field. For example, how does spatially or temporally down-sampling the high-zoom data affect spike detection?

5) The sensitivity and ROC analyses assume that the only way to extract spike information from a fluorescence trace is to do a linear thresholding on ΔF/F amplitude, but many spike extraction methods take into account multiple properties of the shape of fluorescence transients. It would be beneficial if the authors could apply some of the most commonly used spike extraction algorithms to their data in order to benchmark/validate them (particularly under the low-zoom conditions).

6) Please address the accuracy of spike detection under low-zoom for all locations across the FOV. At low zoom, most commercial two-photon microscopes have increased PSF and reduced photon collection efficiency at the edges of a large field.

7) Please explain why the imaging data were temporally smoothed. This is non-standard, and it is important to know how the analyses apply to conventional approaches.

8) It is unclear why the tetO-GCaMP6s have a higher noise floor. Are there any systematic differences in the way these data were collected (different anesthetic, different depth, different amounts of brain motion, different age of mice) that could explain this?

9) Please state the ages of each individual animal used in this study. Is age a confound? Are the distribution of ages for each mouse line matched? For viral expression of GCaMP, time of expression is an important variable. What role does it play in transgenic mice?

Reviewer #3:

This is a well done and systematic comparison of the relationship between electrophysiologically recorded action potentials and GECI-reported fluorescence transients in a variety of transgenic mouse lines used for such recordings. The authors carefully compare the ability of detect single and 5 spike events. Many people will read this study and find its results useful in designing their own experiments and in analyzing their data.

A few points need consideration

1) The authors only use 91 out of the of the 237 cells collected. If there was selection made based on the quality of the imaging data, this may strongly impact the results. How were the cells chosen for inclusion? What happens if the other cells are analyzed?

2) Only peri-cell annular neuropil fluorescence correction is attempted. What if CNMF-type algorithms are used? Does this yield substantially different results? It is not clear that the fixed r-value subtractive approach is necessarily the best when trying to detect single spikes. (I am happy to be convinced otherwise if I am wrong).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Relationship between simultaneously recorded spiking activity and fluorescence signal in GCaMP6 transgenic mice" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, and the evaluation has been overseen by Gary Westbrook as the Senior Editor and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Karel Svoboda (Reviewer #1); Michael Higley (Reviewer #2); Bernardo L Sabatini (Reviewer #3). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option.

Summary

The reviewers all agreed that this data is an important resource. This manuscript reports a valuable simultaneous ephys-ophys dataset with a great number of cells recorded (N = 237) and selected (N = 91). This data set will support the development of more refined spike-to-fluorescence or fluorescence-to-spike inference models. However, inclusion of data collected under more "real world" conditions – meaning low zoom and typical laser power – would substantially increase the impact. As presented, the results remain somewhat limited without such data for comparison. The authors were requested to examine how different spike detection and neuropil subtraction algorithms would change their conclusions. Instead of including that analysis here, they have instead posted another manuscript to BioRxiv. Although this makes the analysis public, it fails to improve this manuscript.

A number of specific comments below require your attention before we can make a final decision regarding publication in eLife.

Essential revisions

1) There is really only minimal analysis of the data. It would be greatly improve the impact of this work to compare detailed spike to fluorescence model parameters to other measurements using the models in Wei et al., 2019.

2) From this and previous studies it is clear that viral expression of GCamp provides better SNR than transgenic expression. This remains a mystery and would be worthy of comment in the manuscript

3) Of course, it is expected that SNR will decrease with zoom at constant power because of shot noise. But it is highly unlikely that investigators would use the same laser power for imaging over changes in zoom by a factor of 20. Please comment.

4) Critical references are missing. Dana et al., 2014 and Wei et al., 2019 have shown that “GCaMP6s cells have spike-triggered fluorescence responses of larger amplitude, lower variability and greater single-spike detectability than GCaMP6f” in transgenic mice.

5) Important spike-to-calcium parameters (e.g. rise- and decay- time constants) are missing. These parameters should be reported as part of the basic analyses; please incorporate the analyses e.g. Figures 2D,E,F and 3F in Chen et al., 2013. One can also use existing spike-to-fluorescence models to estimate the parameters (Wei et al., 2019).

6) Spike-event snippet creation. First, the authors should demonstrate how they chose the parameters for the snippets in each imaging condition. It is not clear that the choice of snippet parameters were optimal; for example, Emx1-s and tetO-s ΔF/F at 4APs in Figure 2 seem not to reach the maximum within 200 ms window. Ideally, these parameters could be determined by the estimates of rise- and decay- time constants. For example, if the half-rise time is 100 ms and the spike-event snippet is 200 ms, one should use a time window at least 400 ms to capture the peak dF/F.

7) Neuropil removal. This is a confusing part throughout the manuscript. At the beginning, the authors preferred not performing neuropil correction because it might increase peak ΔF/F variability (Figure 2—figure supplement 1D), then in the later part, the authors claimed that the importance of the neuropil correction to the spike detection. The authors could offer a systematic study to address if neuropil should be removed and how. It seems like the optimal r for each cell should be used throughout the manuscript. One study from Kerlin et al., 2010 (this paper should be cited) provided some answers to this.

8) ΔF/F computation. In general one would take a long time-window to compute F0 with the background subtraction in the denominator, where F0 aims to reflect 0AP fluorescence. Computing locally as the mean within 50 or 20 ms before the first spike event is risky, because F0 in a short window can be contaminated by the previous calcium decay after a many-AP event e.g. F0 around 5-AP in Figure 1B.

9) Peak ΔF/F variability. First, it is not clear how the mean coefficient of variation of ΔF/F peak (a main measure of peak ΔF/F variability throughout the manuscript) was defined and computed. Is the coefficient in the term of the number of spikes? How was it computed in a given nAP case, e.g. Figure 4A right or Figure 4B? Second, although shot noise is dominant on single pixels, or at high sample rates or in low brightness conditions, variability would be reduced when computing F by averaging over N pixels. The analysis on single pixels is somewhat misleading. Third, trial-by-trial variability is important but the measurement is not clear. In general, the peak ΔF/F should depend on the time series of the spikes. It roughly depends on the number of the spikes in a brief time window. One would thus expect two sources of trial-by-trial variance, one depends on the number of spikes; the other depends on the spike pattern as the number of spikes is fixed. Authors should be able to decompose the variability into these terms.

10) The finding that variance in response amplitude is no larger than expected from shot-noise is surprising and unlikely to be true. There are many reasons why the coupling between AP and Ca might be variable (modulation, baseline potential, state of channels, channel fluctuations). Make sure this analysis is correct.

11) Lastly, as demonstrated above, the peak ΔF/F does not directly depend on behavioral condition when the spike pattern is given. Yet the difference in spon vs visstim in Cux2-f mice is striking. Can this difference be explained by the spike pattern difference in spon vs visstim conditions? If not, what causes this difference?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Relationship between simultaneously recorded spiking activity and fluorescence signal in GCaMP6 transgenic mice" for further consideration by eLife. Your revised article has been evaluated by Gary Westbrook (Senior Editor) and Reviewers 2 and 3 from the original submission.

We are satisfied with the data in the revised manuscript, but ask that you revise the text in accord with the comments below as we believe that these changes with substantially improve the impact of your important work.

Reviewer #2:

Far more emphasis needs to be placed on the "low zoom" data. The difference between the mouse lines is modest at best. However, the demonstration that spike detection is ~15% under normal imaging conditions is a stunning observation that should be a wake-up call to large parts of the community.

Reviewer #3:

The authors have done a great deal to improve the study. There are some remaining points can be easily addressed to improve the study even further.

1) There is no description of what cells the Cux2 and Emx1 cre lines target. It would help make the study more approachable and useful to include this information here.

2) The authors report that there is no epileptiform activity in the mice they use. Do they not see such activity in these mice in their hands or do they select individual mice without seizures? How to they judge the presence of epileptiform activity?

3) In light of point 2, the fraction of spikes that are in groups of 1-5 spike bursts is very different for GCAMP6s and GCAMP6f mice. This is a metric measured by the cell-attached recording. Doesn't this indicate that the transgene has a large effect on cellular or circuit activity patterns?

4) The authors use QC metrics to reduce the number of cells analyzed from >200 to 48. Can they report what factors result in 75% of the cells being rejected? Do they know which rejection factors actually impact the ability to accurately infer spiking from fluorescence? Such insight would be very useful for others who don't have cell-attached recordings but want to be able to understand what cells to include in their final analyses.

5) Lastly, the Discussion leaves something to be desired. It is a synopsis of the conclusions and iterates some rather obvious points but also making some claims without backing. It is not clear that the statements about GFP quantum yield being the limiting factor to further improvement of single-spike detection is correct. The Ca-sensitive fluorophores may not get brighter, but their linearity, DF/F, stability etc may improve. Given the assumption that photon-budget is limiting, the statement that voltage-sensors may provide the solution seems wrong as these will provide many fewer photons per AP. The authors could use the discussion instead of provide some helpful hints to imagers to make the best use of their data based on the analyses presented.
