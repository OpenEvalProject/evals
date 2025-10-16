# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86190.sa0](https://doi.org/10.7554/eLife.86190.sa0)

This study presents a valuable finding on the causal contribution of the inferior frontal gyrus (IFG) in behavioral control. State-of-the-art transcranial ultrasonic stimulation in combination with EEG is used to stimulate the IFG and find changes in speed and accuracy in a stop-signal task. This convincing work will be of interest to a wide range of basic neuroscientists.


---

# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86190.sa1](https://doi.org/10.7554/eLife.86190.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Transcranial focused ultrasound to rIFG improves response inhibition through modulation of the P300 onset latency" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Lennart Verhagen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The use of silicone (without doping) is not recommended as a coupling medium. While its sound velocity and attenuation are appropriate, the density of undoped silicone is significantly different from human tissue Z 0.97 vs. 1.55. As such, the reported pressure/intensity in the head is unlikely to be accurate and significantly lower than reported. I would suggest you empirically test this medium in a tank or include it in your models.

2. Are the W/cm^ values reported Isppa or Ispta?

3. There are multiple missing references. Matzke, Wagner, Lacoutoure … this is sloppy and seriously detracts from the manuscript.

4. The EEG pre-processing is insufficient. There is mention of interpolation several times but no details. Data is said to be re-referenced 3 separate times … is this correct? If so, why?

5. Citations are needed for many of the methods for example the use of artifact subspace reconstruction, k-medoids, dynamic time warping, etc. You may know who and why these methods are used but many others will not. There is a line in the methods that this is a "standard approach in inhibitory control electrophysiology" – cite something.

There is mention of the approach of Mattia. What is it?

6. The data in figure 3 does not appear to be the data of the main logistic regression analysis but is the crux of the paper. The ANOVA before the figure refers to Figure 3 but so also does the ANOVA after Figure 3. Which is it?

7. The data in Figure 3A are from the ANOVA from the logistic regression? I don't think so as these are probabilities and not log odds but are referred to as such. Please confirm. Also, there is another ANOVA done separately for the different SSDs? It is also not clear what data, and how many trials went into the analysis (especially the regression). There is mention of estimating data points. Why was this done? What happened to the actual data?

8. A table outlining the data; means etc. plus the results of all tests would be very helpful in sorting through all the data.

9. Finally, the interpretation of the ERP data in Figure 4 looks to be all descriptive. What tests were done to determine latency or peak differences? How were these quantified if at all? Be sure to cite for the use of permutation statistics and were these done only in sensor space but not temporally across the waveforms? How was latency/onset determined and statistically tested?

10. I think adding the direct comparison between rIFG-tFUS and S1-tFUS and between rIFG-tFUS and sham-tFUS to figures 3 and 4 would strengthen the study.

11. It would be wonderful to learn more about the sham condition. From the methods I couldn't work out how this was performed, how the transducer was placed, whether stimulation was applied or only a sound, or how exactly this condition controlled for possible auditory effects.

12. A figure with the exact trial timing would be very helpful to understand the timing of the go cue, SSD, the exact timing of the tFUS relative to the go and/or stop signal, the temporal overlap between tFUS and SSRT and ERP, etc.

13. Was the tFUS at stop delivered 100 ms before the stop signal (as in Legon 2014, t=-100ms), or at the time of the stop signal (t=0ms)?

14. Did the stop signal (red square) appear at random times (as suggested in the caption of figure 1), or at one of four discrete SSDs (as suggested by the methods section)?

15. The description of the tFUS methods would benefit from 1) a clearer specification of the intensity together with the other stimulation parameters, and 2) an estimation of indices relevant for safety, such as the MI and estimated thermal rise in the skull and brain or TIC.

16. You report that tFUS improved stopping behaviour. This was only the case for the SSD at 95% of baseline RT, right? It seems that with SSD at 65% of baseRT the performance was impaired (Figure 3A). Although in the text on page 21, the opposing effects at 65% and 95% are together described as '[…] inhibitory performance appear greater at longer SSDs'.

17. On page 17, I didn't quite understand how the ERPs corresponded to the 85% and 105% of mean go RT, while the SSDs corresponded to the 65% and 95% of the baseline go RT. Is this because there was a difference between baseline go RT and task go RT?

18. The EEG analyses might benefit from quantified statistical analyses. Cluster-based permutation tests are described in the methods, and three contrasts are mentioned, but it seems none are reported in the Results section.

19. In general, the methods section, especially the description of the statistical inference, could benefit from more clarity and more rigorous and consistent descriptions of conditions and parameters.

20. I would recommend using the same y-axis range across the panels of figure 4B. This will allow a direct comparison of the ERPs between no-tFUS and stop-tFUS conditions.

21. The discussion might benefit from considering the tFUS timing in relation to the SSRT. How much tFUS was delivered before the SSRT was reached? Especially considering that the effect was only present at SSD = 95%. How does this relate to the known delay between tFUS onset and modulation of spiking activity (e.g. 50-100ms delay)?

22. The discussion mentions that TMS has a resolution in the order of a few millimeters and TUS of about 1-2mm. This seems similar, and both are somewhat optimistic. The lateral FWHM of the TUS beam was already 5mm, and the axial/longitudinal FWHM is probably in the order of centimeters.

23. Do you have any ideas on the neurophysiological mechanism through which tFUS led to improved stopping behaviour (or impaired at 65% SSD)?

24. Some conclusions from the discussion do not seem to be strongly supported by evidence. For example, I did not fully understand how you conclude that rIFG tFUS is not involved in P300 amplitude modulation. Also, the conclusion on N200 amplitude relation to response inhibition outcome seems to be based on a visual comparison. Did I miss something? And the same for the conclusion that N100 was modulated in the no-tFUS, but not in other tFUS conditions? Was this also a visual comparison?

Reviewer #1 (Recommendations for the authors):

I found this manuscript a real challenge to read and interpret. The background and premise were solid and the use of online tFUS to modulate the rIFG to see what this does to stop-signal behavior and ERPs was solid. Once I hit the methods/results however I got lost. Below are a few issues that I feel need to be addressed before publication.

Methods

The use of silicone (without doping) is not recommended as a coupling medium. While its sound velocity and attenuation are appropriate, the density of undoped silicone is significantly different from human tissue Z 0.97 vs. 1.55. As such, the reported pressure/intensity in the head is unlikely to be accurate and significantly lower than reported. I would suggest you empirically test this medium in a tank or include it in your models.

Are the W/cm^ values reported Isppa or Ispta?

There are multiple missing references. Matzke, Wagner, Lacoutoure … this is sloppy and seriously detracts from the manuscript.

The EEG pre-processing is insufficient. There is mention of interpolation several times but no details. Data is said to be re-referenced 3 separate times … is this correct? If so, why? Citations are needed for many of the methods for example the use of artifact subspace reconstruction, k-medoids, dynamic time warping, etc. You may know who and why these methods are used but many others will not. There is a line in the methods that this is a "standard approach in inhibitory control electrophysiology" – cite something.

There is mention of the approach of Mattia. What is it?

– The data in figure 3 does not appear to be the data of the main logistic regression analysis but is the crux of the paper. The ANOVA before the figure refers to Figure 3 but so also does the ANOVA after Figure 3. Which is it?

– The data in Figure 3A is from the ANOVA from the logistic regression. I don't think so as these are probabilities and not log odds but are referred to as such. Please confirm. Also, there is another ANOVA done separately for the different SSDs? It is also not clear what data, and how many trials went into the analysis (especially the regression). There is mention of estimating data points. Why was this done? What happened to the actual data?

– A table outlining the data; means etc. plus the results of all tests would be very helpful in sorting through all the data.

– Finally, the interpretation of the ERP data in Figure 4 looks to be all descriptive. What tests were done to determine latency or peak differences? How were these quantified if at all? Be sure to cite for the use of permutation statistics and were these done only in sensor space but not temporally across the waveforms? How was latency/onset determined and statistically tested?

Reviewer #2 (Recommendations for the authors):

Fab work. I have been hoping to see this published for a while.

I think adding the direct comparison between rIFG-tFUS and S1-tFUS and between rIFG-tFUS and sham-tFUS to figures 3 and 4 would strengthen the study.

It would be wonderful to learn more about the sham condition. From the methods I couldn't work out how this was performed, how the transducer was placed, whether stimulation was applied or only a sound, or how exactly this condition controlled for possible auditory effects.

A figure with the exact trial timing would be very helpful to understand the timing of the go cue, SSD, exact timing of the tFUS relative to the go and/or stop signal, temporal overlap between tFUS and SSRT and ERP, etc.

Was the tFUS at stop delivered 100 ms before the stop signal (as in Legon 2014, t=-100ms), or at the time of the stop signal (t=0ms)?

Did the stop signal (red square) appear at random times (as suggested in the caption of figure 1), or at one of four discrete SSDs (as suggested by the methods section)?

The description of the tFUS methods would benefit from 1) a clearer specification of the intensity together with the other stimulation parameters, and 2) an estimation of indices relevant for safety, such as the MI and estimated thermal rise in the skull and brain or TIC.

You report that tFUS improved stopping behaviour. This was only the case for the SSD at 95% of baseline RT, right? It seems that with SSD at 65% of baseRT the performance was impaired (Figure 3A). Although in the text on page 21, the opposing effects at 65% and 95% are together described as '[…] inhibitory performance appear greater at longer SSDs'.

On page 17, I didn't quite understand how the ERPs corresponded to the 85% and 105% of mean go RT, while the SSDs corresponded to the 65% and 95% of the baseline go RT. Is this because there was a difference between baseline go RT and task go RT?

The EEG analyses might benefit from quantified statistical analyses. Cluster-based permutation tests are described in the methods, and three contrasts are mentioned, but it seems none are reported in the Results section.

In general, the methods section, especially the description of the statistical inference, could benefit from more clarity and more rigorous and consistent descriptions of conditions and parameters.

I would recommend using the same y-axis range across the panels of figure 4B. This will allow a direct comparison of the ERPs between no-tFUS and stop-tFUS conditions.

The discussion might benefit from considering the tFUS timing in relation to the SSRT. How much tFUS was delivered before the SSRT was reached? Especially considering that the effect was only present at SSD = 95%. How does this relate to the known delay between tFUS onset and modulation of spiking activity (e.g. 50-100ms delay)?

The discussion mentions that TMS has a resolution in the order of a few millimeters and TUS about 1-2mm. This seems similar, and both are somewhat optimistic. The lateral FWHM of the TUS beam was already 5mm, and the axial/longitudinal FWHM is probably in the order of centimeters.

Do you have any ideas on the neurophysiological mechanism through which tFUS led to improved stopping behaviour (or impaired at 65% SSD)?

Some conclusions from the discussion do not seem to be strongly supported by evidence. For example, I did not fully understand how you conclude that rIFG tFUS is not involved in P300 amplitude modulation. Also, the conclusion on N200 amplitude relation to response inhibition outcome seems to be based on a visual comparison. Did I miss something? And the same for the conclusion that N100 was modulated in the no-tFUS, but not in other tFUS conditions? Was this also a visual comparison?
