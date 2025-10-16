# Peer review - Round 1

Editors:
- Floris P de Lange, Radboud University Netherlands

Reviewers:
- Floris P de Lange, Radboud University Netherlands
- Laurentius Huber, United States
- David G Norris, Radboud University Nijmegen Netherlands

## Review text

DOI: [10.7554/eLife.46856.sa1](https://doi.org/10.7554/eLife.46856.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work uses high-field imaging and innovative analytical approaches to examine the laminar profile of two distinct modulatory influences on sensory processing: multisensory interactions and attentional modulation. Interestingly, multisensory and attentional mechanisms modulated the laminar activity profile in distinct ways. This strongly suggests that these two forms of modulatory responses modulate sensory processing via different neural pathways.

Decision letter after peer review:

Thank you for submitting your article "Resolving multisensory and attentional influences across cortical depth in sensory cortices" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Floris P Lange as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Christian Büchel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Laurentius Huber (Reviewer #2); David G Norris (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript entitled "Resolving multisensory and attentional influences across cortical depth in sensory cortices" describes a layer-fMRI study with audio and visual stimuli and it investigates layer dependent signal changes across different attention and modality conditions. The main conclusion of the study is that cross-modal activity modulates the deeper layers, whereas attentional differences modulate the superficial layers. The fact that this can be measured noninvasively in humans, will be of great interest to a large research field.

Essential revisions:

Some of the most significant concerns raised are:

1) Risk of false positive significance scores. Possibly exacerbated by a low sample size (N=11)?

2) None of the effects in the main conclusion are reproduced in control task conditions: The attention effect in visual areas is not reproduced by attention effects in auditory areas. The cross-modal modulation in auditory areas is not reproduced in visual areas (neither in size, direction, nor shape of layer signals).

3) Similarly, none of the effects in the main conclusion are reproduced across the alternative control analysis approaches (shape parameters vs. decodability): Crossmodal layer-profiles in A1 and V1 (Figure 3A) look very different for B-parameters compared to the respective decodability values (zero, constant, decreasing, zero).

These and other points are elaborated in the individual reviews below.

Reviewer #1:

The authors present an elegant study of visual, auditory and multimodal processing of looming stimuli. In addition, they employ an attention modulation, effectively generating a 3x2 design. They record high resolution (0.75mm isotropic) gradient-echo BOLD of 11 subjects and analyze it using the GLM framework. They use equivolume layering and the median activation over four ROIs (two auditory and two visual) to extract 4x6 laminar profiles. Summarizing their findings, they generally find the expected increase in visual areas for visual and auditory areas for auditory stimuli. They in addition find deactivations across modalities. They find cross-modal modulations only in auditory cortex, interestingly in Heschel's gyrus only in multi-voxel decoding, not in amplitude. Attentional modulations were mostly constrained to auditory regions as well.

The study is complex, but with a solid design. The analyses are described in detail, the code is freely available (the data not yet, so I didn't test their pipeline), and the methods used are appropriate. The paper is also well written, clear and consistent. The figures are detailed, give single subject estimates and are mostly clear. I especially enjoyed that the authors provide all results, not only the significant tests. This is even more important, given that they test quite a lot (which should probably be discussed a bit more, especially in light of a small n=11), and thus there is no hard significance-filter for the results.

Reviewer #2:

The manuscript entitled "Resolving multisensory and attentional influences across cortical depth in sensory cortices" describes a layer-fMRI study with audio and visual stimuli and it investigates layer dependent signal changes across different attention and modality conditions. The main conclusion of the study is that cross-modal activity modulates the deeper layers, whereas attentional differences modulate the superficial layers. The fact that this can be measured noninvasively in humans, will be of great interest to a large research field. And upon some revisions, I ultimately recommend its publication with great enthusiasm.

The novelty and strengths:

– While some other groups are also currently working on it, I believe this is the first manuscript of layer-dependent analyses of multi-modal integration.

– I believe I have not seen any layer-fMRI manuscript that combines so many different brain areas (including PT, which is new for layer-fMRI) and so many different task conditions in one study.

– The authors developed a novel analysis methodology of interpreting the layer-profiles as a combination of linear 'slopes' and 'constant' offsets that allow straightforward summary statistical tests across task conditions.

– The data-acquisition methodology is technically sound and appropriate to address the research questions. Like in previous studies of that group, they use the most advanced imaging hardware, sequences and imaging protocols. Without being too advanced that it would require additional method-validation-studies.

– The statistical results are shown very honestly in violin diagrams for all conditions in and all participants. And data will be shared.

The weaknesses:

– I feel the task design might have been pushed it a bit too much. There are as many as 6 task conditions with subtle differences. Thus, either one of the condition differentiations does not have so many trials to average across compared to comparable layer-fMRI studies. As a result, multiple different tasks conditions needed to be averaged together and the main conclusions are based on effects that (almost) disappear in the noise level.

– I believe the clarity of the manuscript can be improved. Each figure has up to 20 sub panels, whereas most of them show insignificant effects that cannot be used to support the main conclusion. It took me quite a while to filter out the relevant information.

– I believe the way the analysis is conducted and the data are presented could benefit from more discussions on the limits of their interpretability. I am hesitant whether I can interpret the shape parameters and decodability profiles as measures of neural activity in a way that the main conclusion is the most plausible explanation for all the depicted results.

Reviewer #3:

In this paper, the authors examine the responses of early sensory cortices to auditory, visual, and combined auditory-visual stimuli, in conjunction with an attentional modulation, using laminar resolution fMRI. The results presented are of interest, and convincing. Nevertheless, I feel that the paper could be improved by consideration of the following:

1) In the Abstract the claim is made that these findings are crucial for understanding "how the brain regulates information flow across senses". A sceptic could claim that the article only succeeds in reproducing animal literature, and I would suggest that the authors expand their Discussion so as to better substantiate this claim.

2) The figures are organised to present the results of auditory and visual stimulation separately, whereas the text is organised to first deal with auditory and then visual stimulation. It may be more logical to deal with both modalities in parallel. Beyond the criticism at the organisational level, the current structure rather masks obvious asymmetries between the responses in primary auditory and visual cortices. The narrative that emerges would seem to be of a dominance visual modality. The Discussion rather misses the opportunity to compare and contrast across the modalities. For example, there are obvious differences shown in Figures 2A, and 3A which could benefit from some in-depth discussion.

3) Cross modal modulation is assessed by examining the contrast AV-A in auditory cortex and correspondingly AV-V in visual cortex. To me it would seem more logical to construct a contrast AV-(A + V). For example, if AV-A would produce no significant activation, but a visual stimulus in isolation would deactivate auditory cortex, then there would be a clear cross-modal effect that would be missed by your chosen contrast parameter. I would suggest re-analysing the data.

4) Please justify the inclusion of, and discuss the interpretation of the results from, the planum temporale. In this context please also explain in the Results why the left hemisphere was imaged.

5) It could be easier to follow some of the text if the authors would deal with areas of early visual cortex that activate upon visual stimulus separately from those that deactivate upon visual stimulus.

6) I had some concerns about the stimulus design, which I could not find addressed in the text. First, the baseline condition of visual fixation is itself some form of visual task. Second, the auditory target apparently has a fixed amplitude but is presented at a variable time against a looming auditory stimulus: doesn't this affect the detectability?

7) The English is generally good, but the authors persistently introduce comparative statements with no clear object. This is particularly confusing when paragraphs start with: "by contrast"; "in contrast"; "hence". Most of these can be deleted without any effect on the meaning. The authors also tend to introduce a chronology ("next we…") which is not really necessary.
