# Peer review - Round 1

Editors:
- Jonas Obleser, University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.102823.3.sa0](https://doi.org/10.7554/eLife.102823.3.sa0)

This study aims to clarify the effects of cochlear neural degeneration on auditory processing in listeners with normal audiograms (sometimes referred to as 'hidden hearing loss'). The authors provide important new data demonstrating associations between cochlear neural degeneration, non-invasive assays of auditory processing, and speech perception. Based on a cross-species comparison, the findings pose compelling evidence that cochlear synaptopathy is associated with a significant part of hearing difficulties in complex environments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102823.3.sa1](https://doi.org/10.7554/eLife.102823.3.sa1)

This study is part of an ongoing effort to clarify the effects of cochlear neural degeneration (CND) on auditory processing in listeners with normal audiograms. This effort is important because ~10% of people who seek help for hearing difficulties have normal audiograms and current hearing healthcare has nothing to offer them.

The authors identify two shortcomings in previous work that they intend to fix. The first is a lack of cross-species studies that make direct comparisons between animal models in which CND can be confirmed and humans for which CND must be inferred indirectly. The second is the low sensitivity of purely perceptual measures to subtle changes in auditory processing. To fix these shortcomings, the authors measure envelope following responses (EFRs) in gerbils and humans using the same sounds, while also performing histological analysis of the gerbil cochleae, and testing speech perception while measuring pupil size in the humans.

The study begins with a comprehensive assessment of the hearing status of the human listeners. The only differences found between the young adult (YA) and middle aged (MA) groups are in thresholds at frequencies > 10 kHz and DPOAE amplitudes at frequencies > 5 kHz. The authors then present the EFR results, first for the humans and then for the gerbils, showing that amplitudes decrease more rapidly with increasing envelope frequency for MA than for YA in both species. The histological analysis of the gerbil cochleae shows that there were, on average, 20% fewer IHC-AN synapses at the 3 kHz place in MA relative to YA, and the number of synapses per IHC was correlated with the EFR amplitude at 1024 Hz.

The study then returns to the humans to report the results of the speech perception tests and pupillometry. The correct understanding of keywords decreased more rapidly with decreasing SNR in MA than in YA, with a noticeable difference at 0 dB, while pupillary slope (a proxy for listening effort) increased more rapidly with decreasing SNR for MA than for YA, with the largest differences at SNRs between 5 and 15 dB. Finally, the authors report that a linear combination of audiometric threshold, EFR amplitude at 1024 Hz, and a few measures of pupillary slope is predictive of speech perception at 0 dB SNR.

I only have two questions/concerns about the specific methodologies used:

(1) Synapse counts were made only at the 3 kHz place on the cochlea. But the EFR sounds were presented at 85 dB SPL, which means that a rather large section of the cochlea will actually be excited. Do we know how much of the EFR actually reflects AN fibers coming from the 3 kHz place? And are we sure that this is the same for gerbils and humans given the differences in cochlear geometry, head size, etc.?

[Note added after revision: the authors have added new data, references, and discussion that have answered my initial questions].

(2) Unless I misunderstood, the predictive power of the final model was not tested on held out data. The standard way to fit and test such model would be to split the data into two segments, one for training and hyperparameter optimization, and one for testing. But it seems that the only spilt was for training and hyperparameter optimization.

[Note added after revision: the authors now make it clear in their response that the modeling tells us how much of the current data can be explained but not necessary about generalization to other datasets.]

While I find the study to be generally well executed, I am left wondering what to make of it all. The purpose of the study with respect to fixing previous methodological shortcomings was clear, but exactly how fixings these shortcomings has allowed us to advance is not. I think we can be more confident than before that EFR amplitude is sensitive to CND, and we now know that measures of listening effort may also be sensitive to CND. But where is this leading us?

I think what this line of work is eventually aiming for is to develop a clinical tool that can be used to infer someone's CND profile. That seems like a worthwhile goal but getting there will require going beyond exploratory association studies. I think we're ready to start being explicit about what properties a CND inference tool would need to be practically useful. I have no idea whether the associations reported in this study are encouraging or not because I have no idea what level of inferential power is ultimately required.

[Note added after revision: the authors have added to the Discussion to put their work into a broader perspective.]

That brings me to my final comment: there is an inappropriate emphasis on statistical significance. The sample size was chosen arbitrarily. What if the sample had been half the size? Then few, if any, of the observed effects would have been significant. What if the sample had been twice the size? Then many more of the observed effects would have been significant (particularly for the pupillometry). I hope that future studies will follow a more principled approach in which relevant effect sizes are pre-specified (ideally as the strength of association that would be practically useful) and sample sizes are determined accordingly.

[Note added after revision: my intention with this comment was not to make a philosophical or nitty-gritty point about statistics. It was more of a follow on to the previous point. Because I don't know what sort of effect size is big enough to matter (for whatever purpose), I don't find the statistical significance (or lack thereof) of the effect size observed to be informative. But I don't think there is anything more that the authors can or should do in this regard.]

So, in summary, I think this study is a valuable but limited advance. The results increase my confidence that non-invasive measures can be used to infer underlying CND, but I am unsure how much closer we are to anything that is practically useful.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102823.3.sa2](https://doi.org/10.7554/eLife.102823.3.sa2)

Summary:

This paper addresses the bottom-up and top-down causes of hearing difficulties in middle-aged adults with clinically-normal audiograms using a cross-species approach (humans vs. gerbils, each with two age groups) mixing behavioral tests and electrophysiology.. The study is not only a follow-up of Parthasarathy et al (eLife 2020), since there are several important differences. Parthasarathy et al. (2020) only considered a group of young normal-hearing individuals with normal audiograms yet with high complaints for hearing in noisy situations. Here, this issue is considered specifically regarding aging, using a between-subject design comparing young NH and older NH individuals recruited from the general population, without additional criterion (i.e. no specifically high problems of hearing in noise). In addition, this is a cross-species approach, with the same physiological EFR measurements with the same stimuli deployed on gerbils.

This article is of very high quality. It is extremely clear, and the results show clearly a decrease of neural phase-locking to high modulation frequencies in both middle-aged humans and gerbils, compared to younger groups/cohorts. In addition, pupillometry measurements conducted during the QuickSIN task suggest increased listening efforts in middle-aged participants, and a statistical model including both EFRs and pupillometry features suggest that both factors contribute to reduced speech-in-noise intelligibility evidenced in middle-aged individuals, beyond their slight differences in audiometric thresholds (although they were clinically normal in both groups).

These provide strong support to the view that normal aging in humans leads to auditory nerve synaptic loss (cochlear neural degeneration - CND- or, put differently, cochlear synaptopathy) as well as increased listening effort, before any clearly visible audiometric deficits as defined in current clinical standards. This result is very important for the community, since we are still missing direct evidence that cochlear synaptopathy might likely underly a significant part of hearing difficulties in complex environments for listeners with normal thresholds, such as middle-aged and senior listeners. This paper shows that these difficulties can be reasonably well accounted for by this sensory disorder (CND), but also that listening effort, i.e. a top-down factor, further contributes to this problem. The methods are sound, well described and I would like to emphasize that they are presented concisely yet in a very precise manner, so that they can be understood very easily - even for a reader that is not familiar with the employed techniques. I believe this study will be of interest to a broad readership.I have some comments and questions which I think would make the paper even stronger once addressed.

Main comments:

(1) Presentation of EFR analyses / Interpretation of EFR differences found in both gerbils and humans

(a) Could you comment further on why you think you found a significant difference only at the highest mod. frequency of 1024 Hz in your study? Indeed, previous studies employing SAM or RAM tones very similar to the ones employed here were able to show age effects already at lower modulation freqs. of ~100H; e.g. there are clear age effects reported in human studies of Vasilikov et al. (2021) or Mepani et al. (2021), and also in animals (see Garrett et al. bioRxiv : https://www.biorxiv.org/content/biorxiv/early/2024/04/30/2020.06.09.142950.full.pdf)

Furthermore, some previous EEG experiments in humans that SAM tones with modulation freqs. of ~100Hz showed that EFRs do not exhibit a single peak, i.e. there are peaks not only at fm but also for the first harmonics (e.g. 2fm or 3fm) see e.g. Garrett et al. bioRxiv https://www.biorxiv.org/content/biorxiv/early/2024/04/30/2020.06.09.142950.full.pdf

Did you try to extract EFR strength by looking at the summed amplitude of multiple peaks (Vasilikov Hear Res. 2021), in particular for the lower modulation frequencies? (Indeed, there will be no harmonics for the higher mod. freqs).

b) How the present EFR results relate to FFR results, where effects of age are already at low carrier freqs? (e.g. Märcher-Rørsted et al., Hear. Res., 2022 for pure tones with freq < 500 Hz)Do you think it could be explained by the fact that this is not the same cochlear region, and that synapses die earlier in higher compared to lower CFs. This should be discussed.Beyond the main group effect of age, there were no negative correlations of EFRs with age in your data?

(2) Size of the effects / comparing age effects between two species:Although the size of the age effect on EFRs cannot be directly compared between humans and gerbils - the comparison remains qualitative - could you a least provide references regarding the rate of synaptic loss with aging in both humans and gerbils, so that we understand that the yNH/MA difference can be compared between the two age groups used for gerbils; it would have been critical in case of a non-significant age effect in one species.

Equalization / control of stimuli differences across the two species: For measuring EFRs, SAM stimuli were presented at 85 dB SPL for humans vs. 30 dB above detection threshold (inferred from ABRs) for gerbils - I do not think the results strongly depend on this choice, but it would be good to comment on why you did not choose also to present stimuli 30 dB above thresholds in humans.

Simulations of EFRs using functional models could have been used to understand (at least in humans) how the differences in EFRs obtained between the two groups are quantitatively compatible with the differences in % of remaining synaptic connections known from histopathological studies for their age range (see the approach in Märcher-Rørsted et al., Hear. Res., 2022)

(3) Synergetic effects of CND and listening effortCould you test whether there is an interaction between CNR and listening effort? (e.g. one could hypothesize that MA subjects with largest CND have also the higher listening effort)

Comments on revised version:

The authors did well to address all the points raised in my review. This paper will make an important contribution to our assessment of the sources of age-related auditory processing deficits beyond the cochlea that impair speech intelligibility.
