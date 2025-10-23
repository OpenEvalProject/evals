# Peer review - Round 1

Editors:
- Howard Eichenbaum, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07886.018](https://doi.org/10.7554/eLife.07886.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Phase-amplitude coupling supports phase coding in human ECoG” for peer review at eLife. Your submission has been favorably evaluated by Timothy Behrens (Senior Editor), a Reviewing Editor, and three reviewers.

The reviewers have discussed their reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All of the reviewers felt the paper was strong, but there were several concerns that need to be addressed:

Reviewer #1:

Watrous et al. tackle the important question of whether phase coding is a mechanism for information encoding in the human brain. They test whether cross-frequency coupling (CFC) subserves phase dependent coding of distinct visual categories. The study is highly relevant for the field of systems neuroscience.

1) The authors may be unintentionally inflating their findings by defining PAC by power increases in HFA through the oscillation triggered coupling (OTC) procedure. PAC does not require a change in power, but a change in the distribution of power relative to the phase of the low-frequency oscillation. Evoked activity might distort CFC results. Did the authors attempt to study evoked and non-stimulus locked activity separately?

2) OTC needs more explanation in this paper. Given the major claims of the paper, the authors should compare the OTC to more established PAC methods, so that the reader can better assess the results. The findings may be inflated by the chosen metric.

3) There are reports (Mathewson, 2009; Schyns, 2011) that indicate that phase coding only becomes evident in stages of high power. It is necessary to test the phase vs. power coding and then assess phase coding separately for high and low power trials. This is important, since the decoding results imply that HFA alone might explain some of the findings. FMAX and FMIN values per subject should be reported. In order to establish PAC as a putative mechanism, one needs to rule out that neither HFA nor low frequency phase/power alone can explain the findings.

4) Could the distribution of phase angles at stimulus onset exhibit a systematic bias with respect to the visual stream? To rule out entrainment to the rhythmic stream the authors could employ ITC or phase-locking to the sensory stream (e.g. Thut et al., 2011).

5) A major concern is the use of wavelets for extracting oscillatory phase. Wavelets constitute an acausal approach to determine the phase of a signal, since an underlying oscillation is assumed. This leads to frequency, but also phase smoothing, e.g. that a transient ERP contaminates the pre-stimulus phase estimates by backward ‘smearing’. The paper would benefit from a causal approach. Please consult Zoefel and Heil (2013, FIPSY).

6) The difference score is introduced in the second paragraph of the subsection “HFA occurs at different phases for different categories” and requires earlier explanation. A schematic for OTC and DS would be preferable.

7) Were the phase and power extracted from the same electrode? Was PAC calculated on epoched data? Both things could possibly lead to spurious findings.

8) Why did the authors only analyze the frequency spectrum up to 120 Hz? Often findings in HG in ECoG only start at 100 Hz and then extend up to 250 Hz.

9) Were eye movements recorded in any of the subjects? The authors argue that this is an unlikely source of artifactual data but eye-tracking data would be more assuring.

Reviewer #2:

A growing literature in systems neuroscience has observed a consistent relationship between the timing of spikes in local ensembles, relative to the phase position of local oscillatory field potentials. This putative phase-coding mechanism provides an interesting means of coordinating population coding, and makes clear predictions about temporal constraints on computation. To date, phase-coding has been studied in rodent models and non-human primates. In their submission, Watrous et al. seek to quantify a correlate of phase-coding in human cortex using direct intracranial recordings. As a means of quantifying phase-coding, the authors focus on phase-amplitude coupling (PAC) in the cortical surface potential, specifically low frequency phase modulation of high-frequency amplitude (HFA). This approach is supported by the correlation between HFA and local population spiking, and previous evidence of phase modulation of HFA. In this regard, HFA PAC reflects a macro-scale measure of population phase-coding.

The role of PAC in cognition is an active area of investigation and the author's attempts to link this phenomenon to phase-coding using human intracranial recordings is of great interest. At a general level, the relationship between phase-coding and local field potential PAC is unclear given the population level readout of spiking in the HFA. In their study, Watrous et al. attempt to identify unique PAC based phase-coding for different visual categories. The authors provide a clear motivation, and employ sophisticated analysis methods towards this endeavor.

1) Anatomy: While the authors provide evidence for PAC, and phase based coding of visual categories, their conclusions make no reference to functional neuroanatomy. Recording sites across subjects come from a wide variety of regions; this strikes me as a challenge when interpreting the specific coding of visual categories. The supplemental movie suggests a range of distant regions, not typically associated with higher-level vision, display some degree of phase-coding/representation of visual categories. This seems inconsistent with previous electrophysiology and functional imaging work (which is not cited or discussed in any detail). On a related note, the diversity of recording sites also makes the use of count statistics as somewhat arbitrary. Percentage of electrodes displaying an effect of interest can be equally meaningful for large or small percentages (e.g. low % for anatomically specific effect or high % for a trivial global effect). The authors should clarify why macro-scale phase-coding exists for visual categories across many cortical regions, rather than focused to the more classical regions of categorical selectivity.

2) Task/decoding: In their task, the authors present only four exemplars for each category, repeating each 33 times (if I understand correctly). While this may serve to aid mnemonic encoding, it does limit the claim of categorical decoding. Specifically, in developing a category decoder, the large number of stimulus repetitions limits insight, given the similarity between any training and test set. On a related note, I found the reporting of the basic decoding results unclear (is the decoder working above expected chance levels? >25%). Given the authors’ aims, it seems that a better use of the data would be quantifying the consistency of phase-coding metrics across repetitions of stimuli, as well as within/between class comparison. This approach would focus more on extracting single trial features and testing similarity across repeated trials (I note issues of repetition suppression come into play here). This approach of displaying consistency of stimulus phase-coding would provide more robust evidence for the authors’ claims.

Reviewer #3:

The manuscript by Watrous and colleagues is an interesting look at phase coding in the human cortex and medial temporal lobe. While the authors have a great deal of experience with ECoG analyses, including phase coding and PAC, and their manuscript is generally of interest, I have a number of questions and concerns.

Technical comments:

1) In Figure 2H, Figure 2–figure supplement 1, the authors show “low gamma” PAC and “high gamma” PAC. This 32 Hz coupling mode seems striking, because it's likely that coupling extends even further below this range into the beta range. This low gamma has been argued to be distinct from more “broadband” high gamma (Kai Miller and Dora Hermes' work), which is correlated with population spiking (Mukamel, Science; Manning, J. Neurosci.), in contrast to low gamma, which is more oscillatory. Thus, the low gamma effect may be more a form of “nested” coupling as has been argued by Nancy Kopell.

2) There appears to be a disproportionate PAC effect at 0.5Hz and 1.0Hz, but with surprising specificity, and not between those two frequencies as seen in Figure 4–figure supplement 1. Why do the authors believe this occurs, and why do they believe their PAC effects are so restricted to this delta range, in contrast to what others have observed in ECoG?

3) How sensitive is detection of HFA event times to the filtering method?

4) With regards to electrode choice, the rationale for only using electrodes in the contralateral hemisphere is unclear. Why systematically reject an entire hemisphere (except for 1 subject, oddly) when you visually inspect channels for epileptic activity anyway? Additionally, what is the medical justification for implanting patients with electrodes in what is putatively a healthy hemisphere?

Statistics comments:

1) Watson-Williams test assumes a von Mises distribution. Is this true for the distributions studied here? If not, use the Wheeler-Watson test.

2) For the resampling statistics: the images were shown in groups of four, but the resampling seems to use random permutation. Resampling should be performed such that the labels for the “chunks” should be shuffled, but within these 4-trial chunks, the labels should be kept the same. This would control for any effect of this chunking.

3) Are there still significant differences between categories? How many electrodes have a category with DS=3?

4) It would be nice to also be given an estimate of effect size wherever a p-value is given.

5) For the SVM bootstrapping estimates, are the two bootstrapping experiments actually independent in order to support the expected false alarm rate of 0.42 electrodes?

General comments:

1) Are there spatial clusters among the electrodes that have phase coding for each of the different categories (c.f. Vidal et al, 2010)?

2) Please make all rose phase plots opaque as in Figure 3C so that we can see the phase distributions for each category.

3) For these phase plots, it would be nice to see the true number of high frequency activity events within each phase bin.

4) It is unclear how Figure 3–figure supplement 1 should be interpreted. For example, the primary effect in the paper is in the delta range, but this figure seems to show poor delta phase clustering. Why?
