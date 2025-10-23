# Peer review - Round 1

Editors:
- Sriram Subramaniam, University of British Columbia Canada

Reviewers:
- Jürgen M Plitzko, Max Planck Institute of Biochemistry Germany

## Review text

DOI: [10.7554/eLife.45919.015](https://doi.org/10.7554/eLife.45919.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "PIE-scope: integrated cryo-correlative light and FIB/SEM microscopy" for consideration by eLife. Your article has been reviewed John Kuriyan as the Senior Editor, Sriram Subramaniam as Reviewing Editor, and three reviewers. The following individual involved in review of your submission have agreed to reveal their identity: Jürgen M Plitzko (Reviewer #1).

The reviewers have discussed the reviews with one another. You will see that all three reviewers find your work interesting but raise a number of concerns. Since each reviewer's concerns have a somewhat different flavor, we have chosen to send the individual reviews to you below without merging them. Your revised submission must satisfactorily address the major comments and concerns of the reviewers in order for the manuscript to be considered for publication in eLife.

Reviewer #1:

The manuscript "PIE-scope: integrated cryo-correlative light and FIB/SEM microscopy" corresponded by Alex de Marco describes a "triple-beam" instrument that includes photons, ions and electrons, referred to as a "PIE-scope" for the correlation and fabrication of cryo-FIB lamellae from frozen hydrated and high-pressure frozen samples for subsequent analysis by cryo-electron tomography (cryo-ET). The integration eliminates the multiple sample transfers that typically take place in the current cryo-ET workflow, which greatly simplifies its application. As a result, and through its retrofittable design, it can provide a way to make this workflow more accessible to other laboratories while increasing the overall throughput. The authors plausibly document their developments and achievements, and I regard this as important advance in this field. However, while the manuscript is direct and to the point, its writing appears somewhat rushed and misses details. In some places the writing is too technical (or jargon) and therefore it could be definitely improved to make it more accessible.

It is somewhat disappointing that there is no final TEM analysis showing that after correlation and sample preparation, cryo-ET can be successfully performed on the produced lamella from either of the two samples. The question is: Could this still be performed?

The paper by Gorelick et al., presents a new design for an integrated fluorescent and dual-beam microscope. This technological advance is a great addition to the correlative tools available for cellular cryo-electron tomography. The implementation described is simple and elegant and seems to work very well. In particular, the ability to target with a precision of ~500 nm is very encouraging.

I find the technology worthy of publishing, but I think that the manuscript requires significant revisions in order to target a wide readership, but more importantly more results need to be included to make sure it will be a useful tool for people interested in this technology. Besides needing many more details in the text, a manuscript like this should contain detailed supplementary data for the expert reader.

Reviewer #2:

1) Information necessary to reproduce the setup.a) The authors state that the software is constantly changing and can be made available from the authors. In order for anyone to implement this technology, they have to be sure that the work described here can be implemented outside of the authors' set up. Thus, a stable release of the software, with a detailed description of all the requirements, should be a necessary condition for publication.b) Along these lines, the drawings and all needed equipment for reproducing the set up should be available (can be upon request but needs to be explicitly stated).

2) The imaging is only done in 2D. The authors describe three positions in software: LM imaging, FIB imaging, and lamella preparation.a) How are the transformation of coordinates done for 2-D images between these imaging modes? Specifically, how is the fluorescence signal superimposed onto the tilted (FIB milling) position? Is the rotation simply done by a compression in the direction of the tilt?b) What is the SEM imaging position with respect to the others? A table, figure, or paragraph describing the relative distances and angles should be provided.c) When checking for the fluorescent signal at different stages of milling, is the sample tilted back so that it is orthogonal to the FIB beam, or is the tilted image used? Do the authors routinely use FIB imaging during milling, or is only the SEM used for this task?

3) In describing the sample preparation, the authors are not very explicit. A notable example is the lack of details in the brain sample. Was it high-pressure frozen? If it was plunge frozen, there is no chance that this sample will be vitrified. While the authors may argue that for the purposes of this manuscript this is not relevant, it should then be clearly stated.

4) The biggest gap in the manuscript is the characterization of the quality of the lamellae for cryo-ET. Each of the points are essential for the work to be useful:a) While the authors did not alter the cryo-stage, the authors should test and report on whether there are any alterations to the stability of the system in any way. Are there any new vibration or other issues that were introduced?b) Are there any added contamination rates from the introduction of the fluorescence set up? Without subsequent cryo-TEM images, it is hard to gauge the quality of the finished lamella.c) In fact, the finished lamella seems thick and cracked, and the thickness is not reported. Even if one would consider this work not to be about lamellae production, the detectability of the fluorescent signal for very thin lamellae should be demonstrated.d) A major issue with fluorescence imaging at cryogenic temperatures is the potential for devitrification. If the authors do not think this is a concern due to the low power of the illumination used, they should provide clear arguments. otherwise, they should show the vitrification of the lamella in the TEM after preparation in the PIE scope.

5) In their letter, the authors claim that this is a non-expensive set up ($50K). I think that as part of supplementary data they should provide a list of materials required and their approximate cost, which is customary when describing a new set up. For instance, what is the cost of ThermoFishder Autoscirpt?

Reviewer #3:

General assessment:

Very well written. Clearly described what has been reached and how the system provides a significant addition to the set of tools available for cell biological studies that require morphological/structural information of molecular structures in their cellular context.

The capability to perform the preparation of cryo-lamella using a focused ion beam SEM with an integrated light microscopy is very exciting as it can be used to ensure that the feature of interest is present in the lamella. This approach will improve possibilities to perform cell biological experiments in which targeted cryo electron tomography of fluorescently tagged structures are an essential ingredient.

It is very exciting that a proof-of-principle is provided on larvae of C. elegans on which the technological solution is evaluated. It is also exciting that the instrumentation is principle retrofittable and the software to make all this work for CLEM operation is open source.

Major concerns:

A major concern I have with the manuscript is that though it describes overall features and possibilities of the instrumentation with sufficient detail to illustrate the potential of its capabilities with the proof-of-principle, but that it lacks a discussion on some of the remaining technological bottlenecks of 3D CLEM on frozen hydrated specimen. In my view the steps that still need to be taken to meet the requirements to make the system applicable for a more wider audience are not mentioned with sufficient detail.

Subsection “Characterizing the system” summarizes the specifications of the system very nicely. Bottlenecks are the accurate 2D positioning of the lamella around a target (~200-400 nm, though is claimed that it could be ~~100 nm), the reduction in imaging quality due to drift (optical astigmatism due to drift, how large is the drift and can limitation be solved?) as well as the outlook for 3 D correlation to achieve an accuracy that would be sufficient for targeted FIB-milling (~500 nm, the need for deconvolution to improve the z-resolution can this indeed be improved, and to what accuracy?)

It would strengthen the paper considerably, if additional discussion/argumentation was giving detailing the possibility of a more accurate performance on next-generation systems.
