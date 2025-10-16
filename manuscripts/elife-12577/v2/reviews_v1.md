# Peer review - Round 1

Editors:
- Barbara G Shinn-Cunningham, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12577.017](https://doi.org/10.7554/eLife.12577.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "The Auditory Representation of Speech Sounds in Human Motor Cortex" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Nicholas Hatsopoulos, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Reviewing Editor and David Van Essen as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study examines evoked activity in speech motor cortex due to passive listening of consonant-vowel (CV) syllables to determine the nature of these representations. High-density ECoG grids recorded local field potentials from the surface of motor and auditory cortices of epileptic patients who either produced CVs or passively listened to them. During speaking, evoked neural activity in ventral sensorimotor cortex (vSMC) was somatotopically organized according to place of articulation whereas during listening, the organized seemed to be based on acoustic features. Both reviewers and the reviewing editor believe that the study could shed light on the important question of whether or not speech perception depends upon encoding spoken language in a motor-based neural code. The innovative experimental and analytical techniques add to our enthusiasm for the work. While the data suggest that language perception is encoded in acoustic features rather than speech-motor production features, all of us felt that there were some major issues, especially with the data analysis, that need to be addressed before the full impact of the study can be evaluated.

Essential revisions:

1) The methods state that the data were analyzed using a common-average reference. Following this, to estimate the high-γ power relative to baseline, the power (extracted using the Hilbert transform) in 8 bandpass frequency regions was computed and averaged, and then turned into a z score. Given this processing stream, the number and locations of the electrodes across which the common-average reference was computed might bias the findings, especially since oscillation power was ultimately analyzed (i.e., very strong high-γ power that was synchronous across a small number of nearby sites would end up looking like weak high-γ power across all sites). This issue needs to be discussed; perhaps some bootstrap analysis or other control could demonstrate that such artifacts are not an issue.

2) The authors argue that during listening "the tuning properties of responsive sites in vSMC.… appear to give rise to an acoustic sensory organization of speech sounds (rather than purely motor organization) in motor cortex during listening." The impact of the work rests on this claim, that the responses in vSMC during listening are organized by acoustic rather than motor properties of sound. However, proving this claim requires showing that statistically, the listening response in vSMC is quantitatively better described as "auditory" rather than "motor" (i.e., by a direct statistical comparison of results plotted in Figure 3c and f). Without this proof, the impact of this paper may be less than claimed. This should be addressed by a statistical comparison of the two fits of the vSMClistening results.

3) In the analyses that are provided, the authors select different electrodes when evaluating vSMClistening (98 electrodes) and vSMCspeaking (362 electrodes). The electrodes evaluated in the vSMCspeaking condition are not all active during listening. To allow direct comparison of results for speaking vs. listening, it makes more sense to select identical subsets for both analyses. This in turn means limiting the analysis to those sites that are active for both vSMCspeaking and vSMClistening conditions. It seems problematic to claim that activity patterns are different across conditions when those patterns are being examined in different sets of electrodes. This can best be addressed by a reanalysis that directly compares vSMCspeaking and vSMClistening responses in the more limited set of electrodes that respond in both cases.

4) Related to item 3, the MDS plots for vSMClistening (Figure 3c and f) are less clearly clustered than vSMCspeaking. This may be an artifact of the 3x difference in sample sizes. Depending on how the authors decide to deal with item 2, this may not remain a problem; however, if there is a comparison of clustering results using different sample sizes, the authors need to verify that the results shown in Figure 3d and g are not an artifact of this difference (e.g., by showing that the same effect holds if the vSMCspeaking and STGlistening datasets are subsampled to equalize the sample size).

5) It may be that the evoked responses in motor cortex during passive listening reflect auditory inputs. While high-γ LFPs strongly correlate with multi-unit spiking (as the authors state), high-γ LFPs may also reflect the aggregate synaptic potentials near the electrode. The authors should discuss this possibility.

6) A motor representation in vSMC during listening may be present in a subset of the vSMC sites. The authors show that response in some vSMC sites lead STG sites (Figure 4d-f). If the MDS analysis was restricted to sites that lead STG (i.e., vSMC signals with very short latencies), would these sites reveal a motor representation? Some vSMC may be generating motor-like responses that are triggered by the auditory stimulus, but that reflect motor, not sensory properties. Analysis of the short-latency vSMC responses would address this concern.

7) The authors report that 16 total sites in vSMC have activity that was "strongly" predicted by a linear STRF, with "strong" defined as r>0.10. The authors need to make clear where the subset of 16 electrodes with significant STRFs were located, and also whether or not this fraction of locations (16/X) is significantly above chance (e.g., correcting for false discovery rate). Most likely, X should include all auditory-responsive vSMC sites, but this is not stated clearly. In addition, the authors should explain by what criterion r>0.10 (i.e., a correlation in which 1% of the variance is explained by the strf) is a good criterion for a "strong" prediction. For instance, how does this correlation strength compare to STRF predictions in STG?
