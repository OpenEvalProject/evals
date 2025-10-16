# Peer review - Round 1

Editors:
- Joseph F Cheer, https://ror.org/047s2c258 University of Maryland School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95694.sa1](https://doi.org/10.7554/eLife.95694.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Comment on 'Accumbens cholinergic interneurons dynamically promote dopamine release and enable motivation'" for consideration by eLife. Your article has been evaluated by Michael Taffe as Senior Editor, Joseph Cheer as Reviewing Editor, and two reviewers (who have opted to remain anonymous).

Please consider the comments and suggestions made by the two reviewers (please see below) and respond accordingly. Please also address the editorial issues.

Reviewer #1:

The comment by Taniguchi et al. systematically and convincingly demonstrates that the red dopamine sensor RdLight1 is photoactivated in response to blue light in the absence of blue light-activated opsins. Moreover, the dynamics of RdLight1 responses to blue light closely mimic the classic dynamics of dopamine transients and would be difficult to distinguish without proper controls. The magnitude of the artifact scales with blue light duration and intensity, is reproducible across several regions of striatum (and in separate laboratories), is robust to dopamine depletion with reserpine, and shows no evidence of depression with repeated stimulation. Taken together, these data highlight an important caveat for the use of RdLight1 with blue-light-activated opsins. This issue has implications for both the interpretation of the paper by Mohebi, Collins and Berke and for the wider audience of scientists utilizing fluorescent sensors in their work. While the findings of this comment show definitively that Figure 1 of Mohebi et al. is contaminated by an artifact, the remaining figures of the paper add valuable knowledge to our limited understanding of the role of cholinergic interneurons in modulating dopamine activity in the striatum in vivo. It is important to note that this comment is an example of responsible and transparent work that reflects how science should be conducted. Both the authors of the original paper and of this comment showed commendable scientific integrity in producing this comment. The fact that these studies were done across laboratories shows not only open collaboration, which should be applauded but also adds an extra layer of rigor.

1. It is still unclear if dual-color fiber photometry (as is used in some of the remaining Mohebi et al. figures) would be subject to the same artifact, as the light intensities generally used for fiber photometry are much lower than for optogenetics and lower than were tested in this comment. In the future, all authors making use of fluorescent sensors can use the approaches demonstrated in this comment to conduct proper controls for their own experiments.

2. The authors correctly point out that many mApple-based fluorescent sensors have been shown to have similar photoswitching artifacts (Zhuo et al., 2023), but should be careful about singling out mApple as the sole issue. Doing so could lead researchers to falsely assume non-mApple-based sensors are safe from such artifacts. Researchers should be reminded of the need to run appropriate controls for all new sensors.

3. The authors mention that the 405 nm wavelength has not been shown to be an appropriate isosbestic wavelength for RdLight1. This provides an opportunity to highlight the need for those developing new sensors to carefully test and publish the full excitation and emission spectra of their sensors in the future.

Reviewer #2:

In the present Comment Taniguchi et al. address an important methodological issue concerning the primary data collection in Mohebi et al. (2023) that substantially changes the interpretation and impact of the original article. In Mohebi et al., the authors used a red-shifted fluorescent dopamine sensor, RdLight1, to measure dopamine release in behaving rodents. They then simultaneously activated a population of acetylcholine-releasing interneurons (ChIs) using a blue-light gated channel rhodopsin (ChR2). They found that evoking action potentials in the ChIs with blue light led to transient increases in the RdLight1 signal that were interpreted as dopamine release. This result was the key observation for the principal conclusions of their study.

However, the present Comment clearly demonstrates through new data that blue light stimulation also directly 'activates' the RdLight1 sensor to produce a signal that appears as dopamine but is in fact not dopamine. Taniguchi et al. thoroughly tested and verified these findings. These results directly challenge the principal findings from Mohebi et al., including the observation that dopamine release is linearly scaled with intensity and duration of activation of cholinergic interneurons (i.e. no short-term depression).

It should be noted that Mohebi and Berke collaborated on this Comment and acknowledge the methodological error in their original publication. This Comment should be published with no need for additional data. I have no substantive concerns.

There are two changes to the text I would ask the authors to make.

1. The language used in a sentence in the Introduction implies that previous work examining the function of nicotinic receptors on dopaminergic fibers implicated these receptors as the sole drivers of all dopamine release in the dorsal and lateral striatum. This is because it is written that "DA dynamics in the dorsal and lateral striatum were found to persist even after …. interference with ACh signaling". Likely everyone would agree that the majority of "DA dynamics" should persist in these conditions. Please amend this section to use more precise language giving appropriate context to these experiments and results. For example, "previous results were unable to detect a change in DA dynamics…"

2. The authors of this Comment are experts in RdLight1, and similar sensors based on mApple. It would be a tremendous benefit to the field if the authors could leverage that expertise here to identify other sensors that could be impacted by the present results.

a. Are there other red fluorescent sensors that are based on mApple?

b. If the authors had used mApple instead of tdTomato in the experiment discussed in the Results, do they think they would have seen a signal like the one shown by RdLight1? Or is the problem with RdLight1 due to the molecular alterations necessary to make it respond to dopamine?

Please also make the following editorial revisions:

a) Abstract

Reading the article without the cover letter, it is not clear that the author list includes two authors from the paper that is being criticized (Mohebi and Berke): it would be good if this could be made clear by revising the abstract as follows:

It is widely believed that acetylcholine modulates the release of dopamine in the striatum of mammals. Experiments in brain slices clearly show that synchronous activation of striatal cholinergic interneurons is sufficient to drive dopamine release via axo-axonal stimulation of nicotinic acetylcholine receptors, but there is less evidence for this mechanism in vivo. Mohebi, Collins and Berke recently reported that, in awake behaving rats, optogenetic activation of striatal cholinergic interneurons with blue light readily evokes dopamine release, as measured with the red fluorescent sensor RdLight1 (Mohebi et al., 2023). Here, we show that blue light alone alters the fluorescent properties of RdLight1 in a manner that may be misconstrued as phasic dopamine release and that this artefactual photoactivation can account for the effects attributed to cholinergic interneurons. Measurements of dopamine using RdLight1 should, therefore, be interpreted with caution when combined with optogenetics. In light of these results (which were obtained by a multi-laboratory collaboration that included Mohebi and Berke), and the results of other studies that did not observe large acetylcholine-evoked dopamine transients in vivo, the conditions under which such release occurs in behaving animals remain unknown.

b) Results section

The statement "In a separate laboratory..." will confuse readers: please revise the Results section to make clear where the different experiments were performed.
