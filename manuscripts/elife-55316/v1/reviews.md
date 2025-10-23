# Peer review - Round 1

Editors:
- Marc Tittgemeyer, Max-Planck-Institute for Metabolism Research Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55316.sa1](https://doi.org/10.7554/eLife.55316.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers and I are convinced that this study will help to progress our understanding of human cardiovascular control. We compliment the authors on the novel and innovative task and the carefully carried out analyses thereof.

Decision letter after peer review:

Thank you for submitting your article "Deciphering the neural signature of human cardiovascular regulation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Marc Tittgemeyer as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Christian Büchel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ivan De Araujo (Reviewer #2); Olivia K Faull (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All reviewers agree that the paper describes a very interesting study to explore brain centers of cardiovascular regulation in humans.

The regulatory pathways underlying neural responses to bodily signals are currently intensively researched particularly regarding the capacity of the organism to shape its ongoing activity. Relating to interoception (sensing of internal bodily states) brain-heart interaction came recently into focus to better understand the influence of internal sensory information on perception, memory, cognition, and gating of our fear responses. To that end, the topic of the paper is very timely, and the study may offer important insights into human neural pathways within cardiovascular control that may also lead to potentially beneficial clinical applications.

To carry out their study the authors have undertaken a clever experimental paradigm that makes use of functional MRI to characterize human subcortical brain regions involved in cardiovascular tone. The authors stimulated orthostatic stress via footward blood volume displacement (-30 mmHg), which induced sympathetic excitation and vagal inhibition in response to the challenge. The authors describe three hypothalamo-medullary subsystems potentially involved in cardiovascular control, preserving some parallel to activation patterns observed in animal studies.

A further interesting aspect of the paper is an elaborate processing pipeline for the notoriously difficult task to analyze brainstem and hypothalamus fMRI data.

Essential revisions:

While the study may thus advance our knowledge and all reviewers are in general enthusiastic about this work, some concerns must be adequately addressed before the paper can be accepted.

1) Relating to confounds associated with the involvement of control systems that only indirectly link to cardiovascular regulation per se: Specifically, the cardiovascular challenge employed induces responses in motor systems associated with respiration such as the craniofacial and thoracic motor systems. Several of those nuclei (parvocellular, intermediate, and medullary reticular nuclei, PCRt, IRt, MdRt) are known to be primarily involved in motor control of head and upper body muscles. It is unclear how exactly the authors did dissociate cardiovascular from other motor control systems in their analyses.

2) Various pathways implicate in the central regulation of cardiocvascular reactivity. The output of these pathways is coordinated by a number of central nervous system regions based on afferent information, but the central nervous system does not only involve the brain but also e.g. spinal cord. The authors mention for instance the melanocortine system which is not only involved in vagus nerve signaling but likely also regulated by somatosensory afferent from the spine via PBN. That said, it is sensible for the authors to emphasise primary regulators, such as hypothalamic regions and the lower brain stem. However, to then interpret the results as direct connections between hypothalamus and brainstem is a simplification, especially also as their connectivity measure is a very indirect one. This aspect needs to be discussed.

3) The authors argue that the "canonical" frequency of the BOLD signal lies outside the frequency bands of blood pressure and heart rate and that analysis is not affected by this. This argument needs more evidence.

4) Some consideration regarding susceptibility to noise in the image analyses is warranted. It is noticeable that many activated areas overlap with neighbouring ventricles, and in fact, some images suggest the peak activation voxel is centered at the ventricular area proper (e.g. Figures 2E, Figure 2—figure supplement 5D, E). Further assurance that no artefacts (e.g. movement given no spatial filtering etc.) influenced the determination of the areas described.

5) Furthermore, the use/non-use of physiological noise correction in this analysis needs more elaboration. While removing all signal associated with physiological recordings may drastically reduce the power to detect neural changes associated with the changes in physiology that are of interest, simply ignoring this step may dramatically influence the results. There would be two possible approaches that could ameliorate concerns that the results are driven by physiological artefacts (preferably both):

– A wider/whole-brain unmasked GLM analysis of the time-course associated with the 5 “cardiovascular” regions identified within the current analysis. The brain areas that correspond to these signals within a wider field of view would allow us to more accurately identify whether this signal is significantly associated with common physiological artefacts, as outlined here: https://doi.org/10.1016/j.jneumeth.2016.10.019

– A supplementary repeat of the analysis with the inclusion of physiological noise regressors, to understand which of the results can be robustly identified independently of the physiological artefacts.

6) The current method employed of only including ICA components that sit primarily within the grey matter does not fully prevent the influence of physiological artefacts, in particular second-order effects such as changes in relatively global signal primarily associated with cerebral vasculature, resulting from fluctuations in ventilation and/or metabolism (the former of which would occur with LBNP). The Discussion could also benefit from a short discussion of the limitations of disentangling physiological artefacts from neural underpinnings for the readers who are less familiar with the difficulties of this topic. This issue is particularly important if the authors are going to claim that their frequency analyses challenge the notion of the canonical HRF, as this claim can only be true if what they are reporting is in fact of neural origin, and not simply a non-neuronal artefact. Furthermore, the induction of LBNP is also regularly associated with a hyperventilatory response, and the high-frequency band sits right within the respiratory range and thus it is not surprising this sees differences with LBNP. Lastly, the HRF in the brainstem and hypothalamus are not clearly mapped nor understood, and as the vasculature in these smaller brain areas is vastly different from the original cortical locations where the HRF was identified, it might be advisable to proceed with caution when using strong statements in this regard.

7) The continuous blood pressure measurement seems to reside on peripheral arterial pressure pulse. Given that these are healthy participants, is there written consent and permission from the ERB explicitly to acquire arterial blood pressure, given that this is of course super invasive?
