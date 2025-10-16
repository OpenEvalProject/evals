# Peer review - Round 1

Editors:
- Laura Dugué, Université de Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54497.sa1](https://doi.org/10.7554/eLife.54497.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In their study, Fomenko and colleagues measure the effects of transcranial ultrasound stimulation (TUS) on corticospinal excitability changes as assessed by transcranial magnetic stimulation (TMS) and motor evoked potentials (MEP) in primary motor cortex. This study is very timely as only a few TUS studies have been published in humans so far. Importantly, they systematically investigated the impact of various TUS parameters and TMS pulses on cortical excitability.

Decision letter after peer review:

Thank you for submitting your article "Systematic examination of low-intensity ultrasound parameters on human motor cortex excitability and behaviour" for consideration by eLife. Your article has been reviewed by Richard Ivry as the Senior Editor, Laura Dugué as the Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Wynn Legon (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Fomenko et al., combined transcranial ultrasound stimulation (TUS) and transcranial magnetic stimulation (TMS) of the primary motor cortex (M1) in humans to measure the effects of TUS on corticospinal excitability changes as assessed by TMS and measures of motor evoked potentials (MEP). They systematically investigated the impact of important TUS parameters, such as pulse repetition frequency, duty cycle, and sonication duration on several single- and paired-pulse TMS related indices for GABA-A- (SICI) and -B-receptor mediated inhibition (LICI, cortical silent period) as well as facilitation (SICF, ICF). They found corticospinal excitability to be generally decreased by TUS, and stronger so for longer sonication and shorter duty cycles, as well as a stronger SICI during TUS. They also observed shorter response times during TUS in a visuomotor task. No impact of TUS was found on any of the other parameters.

The reviewers and the editors appreciates the need for such methods paper as TUS is a very promising neurostimulation technique that is at the stage of translating from animal to human research. Despite a few (<10) studies being already published in humans, the impact of the most basic TUS parameters on cortical excitability is still unclear, and systematic studies like this one are very much needed.

That said, there are significant methodological and statistical concerns that need to be addressed before the paper can be published. The following comments highlight the "essential revisions.

Essential revisions:

1) In general, the data lacks apparent robustness. They authors should collect data from more participants (preferably with more trials) to allow for correction for multiple comparisons across all the tested indices and solve the apparent lack of robustness (failed within-study replications) of the data. The following points describe the different results in which robustness issues have been noticed.

1a) Given the relatively low number of subjects and a total of ~16 different measurements being investigated, there is a certain risk of false positive results. Do the results survive correction for multiple comparisons?

1b) Several of the experiments that either vary TUS parameters or investigate paired-pulse effects also contain a single-pulse MEPS with TUS at "basic parameters" for which a clear suppressive effect was found (p = 0.0018) in the beginning. However, in those four experiments, this effect does not seem to replicate: Figure 5C: DC of 30%; Figure 5E: Pulse repetition frequency of 1000 Hz; Figure 7: TS; Figure 7: S1.

1c) Statistical analyses for more than two conditions seem based on one-way rm-ANOVAs (such as 5 different sonication durations normalized to sham), "and conditional on a significant f-value, Dunnett's multiple comparisons was performed to explore groups with significant differences from sham" (subsection “Statistical analysis”). The Dunnett's tests presumably test something very different (namely the differences between each TUS condition against Sham) than the ANOVA, which testes for differences of the sham-normalized conditions with respect to each other, and not of the conditions relative to sham. (a) The Dunnett's test should thus not be conditional on the f-test, as they simply answer very different questions. This would change if the ANOVA would based on raw MEP values and include the sham condition as level. (b) This also means that there is no post-hoc evaluation of the differences between conditions, which would require e.g., post-hoc paried t-tests. (c) Potentially, some legitimate basic comparisons against sham have not been performed, because the f-test was non-significant, even though it tested something very different.

2) The MEP analysis and results need to be reported with more details. The following points should be clarified in the revised version of the manuscript.

2a). It is unclear how many MEPs (for paired-pulse, how many CS+TS and TS alone trials, respectively) were acquired per condition of each of the experiments. It reads like only 10 MEPs were acquired per condition (20 for paired-pulse blocks, so again 10 CS+TS and 10 TS alone). Given the known high variability of the MEP (cf. also subsection “Limitations” "the MEP variability we saw in some subjects") and the low number of participants (N = 12; which is understandable for TUS in humans but still low) these low MEP numbers are problematic. A larger number (20 or more MEPs) per condition would provide a much more stable estimate and allow the detection of small effects. Although there are quite some clinical neurophysiology papers out there with 10 or 15 MEPs, the kind of results presented here may shape the translation of TUS for human application and are thus too important for the community to suffer from low statistical power. Some of the findings (also of the negative ones) are in contrast to a previous study (Legon et al., 2018), and it is unclear whether this has to be attributed to differences in experimental design or simply noise. Many separate measures were obtained for the same subjects, and the effort of the authors is acknowledged, but maybe less measures and more trials would have been the better choice? Please report to point 1.

2b) The authors used the procedure of outlier exclusion. Outlier removal is a controversial method for MEP analyses. MEP amplitudes are not normally distributed but rather follow a power law, and removal of extremes is therefore corrupting the data. Was the pre-activation controlled and excluded together with the outliers? How many MEPs were left for the statistical analysis after exclusion? How do the results change when all trials are kept but the median is used per condition (instead of the mean) or the mean of log-transformed MEP values? Given that robustness is key for these kind of results, transformations should be avoided (or outlier removal at least).

3) Several concerns have been raised regarding M1 targeting and the use of a normalized brain and MNI coordinates. Specifically, in the newly collected data, M1 (or specific parts of it) should be properly targeted by using neuronavigation and individual head models with T1/T2 (instead of a normalized brain and MNI coordinates). Moreover, the following points should be addressed in the revised version of the manuscript.

3a) Why was a normalized brain used? You have a neuronavigation system and each participants' MRI. Why MNI coordinates? Should you not distinguish based on each participants' anatomy and TMS response to determine location?

3b) Why was a mark placed on the head when you have a neuronavigation system? Since BrainSight neuronavigation was used to identify the TUS transducer position on the scalp, why was it not used to ensure and maintain correct transducer placement throughout the many measurements and sessions? Given the small diameter of the sonication beam, tiny changes in tilt or position can have a massive effect on the actually stimulated part of cortex.

3c) Figure 2B: Please also provide sagittal and axial views to allow a better judgement of the targeting of M1. Is it actually targeting M1 or maybe premotor cortex? Which part of the precentral gyrus is actually sonicated?

3d) According to Fox, 2006 and Geyer, 1996 the motor cortex of human is allocated in the sulcus and at best to a small extent at the crown. In Figure 2B the white matter is targeted as well as in Figure 3A where the pyramidal neurons are allocated in the white matter. Thus, the first part of the following sentence might not be accurate: "Similarly, the individual simulations of ultrasound propagation for each participant confirmed acoustic targeting of a portion of M1, as well as underlying white matter tracts. (Figure 2B)." see also "Our finding may suggest that cortical interneurons in layers II/III which are well-encompassed within the acoustic focus (Figure 4)"

3e) Without a CT scan and only T1-weighetd images no really reliable simulations can be obtained for the acoustic waves. Figure 2B only shows one "representative" subject. Have simulations been performed for all subjects or was the transducer only placed on top of the TMS M1 hotspot for each subject without modelling the sonication beam individually? This assumes that the relevant motor neurons of M1 are actually directly beneath the coil center, which is not necessarily the case.

3f) Figure 3A: The location and orientation of corticospinal output neurons in M1 is incorrect and misleading. They are actually located in the anterior bank of the central sulcus and oriented tangentially to the scalp. This should be corrected.

4) The phrasing "… a portion of M1…" is disconcerting. Because the transducer was concentric with the intersection of the TMS coil, wherever you put the coil is where the US was. Is that accurate? How did you confirm this however in your models if you did not use individual MRI but rather normalized MRI. MNI coordinates are mentioned previously but not given anywhere in the manuscript. TUS is highly localized and using generalized MNI coordinates is not appropriate. Please provide an acoustic wave modeling of the sonication for each participant.

5) There is no data on how/if the transducer affected the TMS pulse or vice versa. This needs to be either collected or cited from Legon et al., 2018 and differences in transducer materials/design should be factored in if there are any.

6) Gel pads are notorious for trapping air bubbles between interfaces. This can be easily detected using imaging mode of your transducer. Was this checked for? Was any other coupling media used?

7) TMS was applied in order to measure the cortical excitability changes with MEP. The TMS pulses were locked to the end of FUS or sham stimulation and they had an interstimulus interval of 5 seconds. If there was no jitter for TMS pulses it means that rTMS at 0.2 Hz was applied simultaneously with FUS. Repetitive TMS applied at a very low frequency of 0.2 Hz has been shown to be effective in several studies (Urushihara, 2006; Hosono, 2008). For example, rTMS over PMC led to an increase in somatosensory evoked potentials. Could the possible effect of low frequency rTMS on cortical excitability when applied simultaneously with FUS be discussed?

8a) A further concern is "This sound was triggered every time a FUS or sham condition was delivered to the transducer." This could mean that the effects reflect acoustic TMS pairing, see e.g. doi: 10.3389/fnhum.2014.00398, other papers are around as well. Can the results in Figure 5D be due to longer acoustic stimulation? I expect the sham condition to be performed with the shortest duration, however not sure? Can this explain the lack of an effect in Figure 5E and F?

8b) Also: "and the task was more complex; nevertheless, the sonication parameters and cortical location were similar, and we observed an effect size of about 100 ms, though with higher variability." It may simply be that the start of the sonification sound leads via a kind of pre-triggering to shortened responses. This is discussed by the authors in subsection “Behaviour”. The effect in Figure 8A appears to be implausibly high. Control experiments seem to be reasonable with very light somatosensoric or close to threshold acoustic stimulation. The whole field of TMS-EEG suffers from acoustic and somatosensory contamination.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Systematic examination of low-intensity ultrasound parameters on human motor cortex excitability and behaviour" for consideration by eLife. Your revised article has been reviewed by Richard Ivry as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Til Ole Bergmann (Reviewer #2); Wynn Legon (Reviewer #3).

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Fomenko et al., have thoroughly revised their manuscript. They added four new participants (now N = 16) with more trials (15-20 instead of 10 per condition), as well as more TUS modelling information. While this is not a large increase in sample size, the authors' efforts are appreciated. However, both the reviewers and the editors were concerned by the fact that the effects are robust for the 'block' experiment but not for the 'parameter' (or interleaved) experiment. Consequently, additional data should be collected in a sufficiently large sample (eg. keeping the N = 16 for interleaved and adding N = 16 for a blocked variation of stimulation parameters), targeting specifically the block vs. interleaved question for the duty cycle and pulse repetition frequency parameters.

Essential revisions:

1) Regarding the block vs. interleaved question:

If it makes indeed a difference for single trial MEP modulation whether TUS is applied in a block design with fixed parameters or with trial-by-trial variation of parameters, this would have important implications for TUS application and thus needs additional data collection, as well as detailed discussion. Specifically, for some parameters (sonication duration) the default parameter (0.5s) was effective in the interleaved design. However, for others (duty cycle) it was slightly different (10% instead of 30%), and for yet others (pulse repetition frequency) it was not different from sham anymore at all (but was previously with 1000 Hz). The blocked vs. interleaved interpretation is post-hoc and potentially valid only for duty cycle and pulse repetition frequency.

2) The authors added 4 subjects to the existing data set (N = 12) but the reviewers fail to see the significance of this. First, data from the original 12 is presented in Figure 4 and the data from the new N = 4 is presented on its own. Could the authors explain the added value of this? It looks from the manuscript that N = 16 was inclusive for the parameter testing but not the 'basic parameter' testing. The authors could either remove Figure 4C or include that data in Figure 4A.

3) It is still unclear how many MEPs were left for each participant for the statistical analysis after exclusion. It looks like the new data uses 15 trials but the old 10 and the block experiment 20. Furthermore, it is stated in the Materials and methods that MEPs {plus minus} 2SD of mean were excluded. Please include M+/-SD in the Materials and methods.

4) The following questions still need to be addressed:

- Was the pre-activation controlled and excluded together with the outliers?

- How do the results change when all trials are kept but the median is used per condition (instead of the mean) or the mean of log-transformed MEP values? Also, do the results hold when not removing the outliers?

- Why was the neuronavigation system not used to online maintain coil/transducer position? Coil angle cannot be reliably inferred from a felt pen drawing on the scalp.

5) Could the authors show the sonication beam model for all three slices (coronal, sagittal, axial)? The axial slices do not seem to be the most helpful ones when determining whether M1 was hit and which portion of it.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Systematic examination of low-intensity ultrasound parameters on human motor cortex excitability and behaviour" for consideration by eLife. Your revised article has been reviewed by Richard Ivry as the Senior Editor, a Reviewing Editor, and one reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Til Ole Bergmann.

The Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

We thank the authors for addressing the comments raised in the review process.

The new results demonstrate that the effectiveness of TUS parameters does indeed depend on whether TUS parameters are varied across trials or kept constant within a block. These additional findings are important and will be very useful for others using this approach. These results though also point to one important question that we believe should be in the published study: Are the results in the block design condition due to cumulative effects? That is, is there a systematic change over time, indicative of a cumulative effect? (To quote the reviewer who noted this concern, "Specifically, is there a build-up of suppression across trials within a block? This could be tested e.g. by regressing the MEP amplitude based on within-block trial number or by comparing early and late MEPs within a block. It would be a very important outcome to know whether the observed suppression is instantaneous or accumulating across trials.").
