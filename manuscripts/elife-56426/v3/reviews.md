# Peer review - Round 1

Editors:
- Jonathan Ewbank, Aix Marseille Université, INSERM, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56426.sa1](https://doi.org/10.7554/eLife.56426.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The clarifications that you have made now allow readers to judge for themselves the utility of this novel imaging modality. While the current system falls short of providing truly continuous high-speed (i.e. > 10 fps) imaging of 80-96 wells, it clearly has great potential for multiple applications.

Decision letter after peer review:

Thank you for submitting your article "Solid state high throughput screening microscopy" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Didier Marguet (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is “in revision at eLifeeLife”. Please let us know if you would like to pursue this option.

The reviewers all recognised the originality of your solution to perform high throughput imaging without moving parts. They do have some serious reservations, primarily regarding the evaluation of the quality and utility of the technique and in addition to the other points raised, consider it essential that you address the following:

– The standard topics for any new microscope paper: "objective" numerical aperture, image resolution, optical aberration, and camera sensor size, together with the specific aspects related to this technique, including dependence on homogeneous illumination, and sensitivity to maintenance of F2 distance.

– A substantial expansion of the scope of the data presented, to provide readers with sufficient evidence with which to evaluate the quality of the technique, including proof of principal with a 96-well plate assay.

– A direct quantitative comparison with existing HTS imaging solutions.

Reviewer #1:

Ashraf and colleagues describe an approach to perform high throughput screening imaging without moving parts. The setup is original and offers to experimentalists the flexibility to record quasi-simultaneously stacks of images of multiple samples at the full field of resolution of the camera. The optical aberration inherent to the use of a parabolic mirror are mostly overcome by collimating light from the objective lens. The images require a post-processing in two steps for taking into account the image stretching on the detector and the variation in magnification due to the variation of the distance between the mirror and the image. Two applications illustrate the potential of the solid-state HTS.

To my opinion, the following points need to be clarified:

– How homogeneous is the field of illumination with a single LED? Especially for a large field of illumination, a non-homogeneous illumination would compromise the quantifications.

– The accuracy of this ssHTS is related to the robustness at keeping the distance F2 constant between samples. In other words, how sensitive is the image acquisition to the potential variation in the F2 distance between samples as well as within a single large field of view?

– The magnification Mc must be explained.

– Is the post-processing compensation applied only in the y-direction?

Assuming that such publication aims to disseminate the use of an ssHTS setup to a wide scientific community, I find the description of the setup as well as the applied image post-processing rather succinct, even with the 3D printing and source codes information.

Reviewer #2:

Astronomers have spent centuries learning how to image the night sky with limited sensor hardware. Ashraf et al. present an ingenious adaptation of a technology developed for telescopes-parabolic reflectors-for imaging biological samples. In principle, the approach seems like it could be incredibly useful across a wide range of applications where multiple samples must be imaged in tandem. By placing multiple samples under a single parabolic reflector, multiplexing of samples and imaging hardware can be accomplished without sample-handling robots or moving cameras. The authors highlight two applications: cardiac cells in culture and free-moving nematodes.

The authors explain the theory behind their technique in a clear and convincing way. However, the biggest challenge in most imaging projects is making the theory work in practice. In its current form, the manuscript falls far short of demonstrating the practical usefulness of parabolic mirrors for imaging biological samples. The authors include only a small amount of image data-for the nematode work, this consists of eight images collected from two plate regions. Data of this scope cannot provide readers or reviewers with sufficient evidence with which to evaluate the quality of the technique.

1) The images shown-are they typical or are they the best possible images that can be collected from the device? The authors do not provide any quantitative evaluation of the quality of their images, in absolute terms or relative to existing methods, with which to understand the practical performance of parabolic mirrors. The authors should estimate the spatial resolution and dynamic range that can be obtained in practice with the devices, and evaluate how such image quality metrics vary across the entire field of view. Does performance degrade towards the edge of the mirror? Does performance degrade over time, as devices become de-calibrated with use?

2) The manuscript is additionally weakened by the absence of a non-trivial measurement made with the device. Pilot experiments are included, demonstrating that images can be collected. However, no evidence is provided to show that these images can be used to compare samples and draw biological conclusions from them. A more convincing proof-of-principle would involve the measurement of some non-trivial biological difference between samples measured with the device, either confirming previous work or discovering something new.

3) The authors highlight the comparative simplicity of their method: it eliminates the need for motorized samples or cameras. However, this simplicity must come at some: for example a substantially increased use of space or perhaps an increase in delicate calibration required, or equipment price. If a 0.25 meter mirror is required to measure four C. elegans plates, how large a mirror would be required to measure 16 plates-the number that can typically be measured using a flatbed scanner? The authors could also expand greatly on other practical issues: for example, is a dedicated imaging table required to align mirrors and samples? Readers would benefit from a clearer evaluation of the practical trade-offs in deploying parabolic mirrors in a laboratory setting relative to other imaging approaches.

Reviewer #3:

The authors present a cool new idea: using a large parabolic reflector in combination with a macroscopic lens array and rapidly modulated LED array to enable fast image multiplexing between spatially separated samples. I believe that there may be interesting applications that would benefit from this capability, although the authors have not clearly demonstrated one. The paper is short, and light on discussion, details, and data.

1) The manuscript does not discuss several standard, key topics for any new microscope paper: "objective" numerical aperture, image resolution, optical aberration (other than distortion, which is discussed), and camera sensor size.

2) Why was an array of low-performance singlet lenses used? With that selection, the image quality cannot be good. Can the system not be paired with an array of objectives or higher performance multielement lenses?

3) Fluorescence imaging is not discussed or demonstrated but would obviously increase the impact of the microscope. At least some discussion would be helpful.

4) Actual HTS applications are almost always implemented in microtiter plates (e.g. a 96-well plate) to reduce reagent costs and enable automated pipetting, etc. I do not believe anyone would implement HTS in thousands of petri dishes. The paper would be strengthened substantially by a demonstration of simultaneous recording from all (or a large subset) of the wells in a 96-well plate. It's not clear whether this is possible due to the blind spot in the center of the parabolic mirror's field of view that is blocked by the camera.

5) One of the primary motivations for this approach is given in the first paragraph as: "wide-field imaging systems [which capture multiple samples in one frame] have poor light collection efficiency and resolution compared to systems that image a single sample at a given time point." With a f = 100 mm singlet lens, the light collection efficiency of the demonstrated microscope is also low (estimated NA = 0.12) and the resolution is unimpressive with the high-aberration lens and 1x magnification. They demonstrated only trans-illumination applications (e.g. phase contrast), where light collection efficiency is not important. I believe a fancy photography lens mounted directly on a many-megapixel camera set to image all or part of a microtiter plate could likely outperform their system in throughput and simplicity, at least for the demonstrated applications of cardiomyocytes and C. elegans.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Solid state high throughput screening microscopy" for further consideration by eLife. Your revised article has been evaluated by Didier Stainier (Senior Editor) and a Reviewing Editor following review and discussion by the three original reviewers.

Overall, the reviewers recognised that this setup could be useful for readers looking for an inexpensive bright-field imaging setup for multi-well imaging without fluorescence. They agree that you have provided substantial additional data and analysis that support your claim that parabolic reflectors can be useful for studying many samples in a parallel. The new images and videos of a 96-well plate were judged compelling. In particular, the prospect of focusing samples simply by adjusting the wavelength of illumination was thought an important step towards the goal of designing a "solid-state" imaging apparatus with no moving parts.

Nevertheless, although the reviewers were satisfied that you had addressed most or all of the material points, they had considerable reservations about the way in which these improvements were presented and could not support publication of the manuscript in its present form. Indeed, there are numerous lacunae and parts where the writing is not at all clear and leads to confusion about how the system functions and what its limits are. Please find below a summary of their most important comments and a series of points made by individual reviewers, all of which would need to be addressed in a revised manuscript. If this would require a further round of experimental work, then I am afraid that we will not be able to consider your work for publication.

The description of the 96-well plate data was considered both terse and vague, leaving unclear several aspects of experimental design and interpretation.

– If no samples were loaded into columns 6 and 7 of the 96 well plate because of the use of 40 LED arrays, this should be stated explicitly.

– What was the exact reason for not imaging in column 4 of row E or row 1F.

These discrepancies between the theoretically predicted function of the device and its practical performance must be clarified.

If these issues do not reflect technical limitation of the device, you would need to demonstrate that these columns/wells can be imaged just like the others (i.e. this is a criterion for rejection).

The details about acquisition are so poorly described that one reviewer wrote, "why not leverage those capabilities to scan 33 wells in parallel at 15 Hz rather than one well at a time at 15 Hz?". This illustrates how you have failed to convey clearly that the system captures data from multiple wells in parallel at 120-500 fps. One video does show how 120 fps can be divided up across 80 wells, and it is illustrated in Figure 1, but these details need to be explicitly stated in the text. In Figure 2, a faster (500 fps) camera of lower resolution is used. As well as making all acquisition details clearer, you will need to provide an explicit discussion of camera choice, and any trade-off between image resolution and speed. Additionally, you need to address another technical limitation and trade-off, namely rates of acquisition and data transfer so that the possibility (and cost) of implementation in a HTS setting (see below) is clear.

The center of the optical system is intrinsically blind since space is required to position the detector. This point is implicit and must be documented as a function of the magnification.

The microscope resolution in the 15 – 20 µm range is poor relative to the sub-micron resolution of a traditional microscope. It is probably not good enough, for example, to tell individual mammalian cells apart in a confluent monolayer. This will limit the range of potential applications. Thus the spatial resolution needs to be stated in the Abstract or Introduction, not buried deep in the Materials and methods. Further, you will need to include a detailed comparison with a standard commercial widefield microscope with a scanning stage (resolution, imaging modalities, scan time, defocusing over time, cost, integration into robotic workflows). If you wish to claim HTS capacity, the comparison should also include a dedicated commercial HCS/HTS system, and the many other features needed for HTS (e.g. see https://www.ncbi.nlm.nih.gov/books/NBK558077/).

Alternatively, in the absence of easy incorporation of the system in an automated setting, at a time when HTS can mean >50,000 tests/day, "High Throughput" should be removed from the title ("multi-sample" or "multi-well" would be better), and any suggestion in the text that your system is HTS-compatible seriously toned down. Equally, given the very different uses in optics or electronics of the term "solid-state", you should avoid it in the title, replacing it, for example by, "with no moving parts".

There was also a general consensus that your design is not a Newtonian telescope, which has two mirrors instead of a single mirror as in this design. The reviewers recommend changing "novel Newtonian telescope design" to "large on-axis parabolic mirror design", "parabolic reflector", or something similar that is clearer and more accurate. Including a phrase like "inspired by a Newtonian telescope" would be acceptable.

Further points made by individual reviewers:

1) The authors compare wild-type C. elegans to nuo-6 mutants. The authors are vague and qualitative in their descriptions of movement. Nuo-6 mutants are predicted to "move less frequently" than wildtype. This is confusing, as C. elegans generally exhibit some degree of continuous movement as long as they remain alive, involving body postural changes, head movements, or pharyngeal pumping. Are the authors referring to the frequency of a particular type of movement? For the purposes of this paper, the authors probably do not need to alter their imaging pipeline, but they should be substantially more specific about which behavior their method is measuring.

2) Many nematode behaviors change in response to stimulation with light, physical stimulus, or immersion in liquid. Other behaviors are suppressed by long periods spent immersed in un-mixed liquids. It remains difficult to interpret the authors' results without additional information describing how the light and culturing conditions they are use influences nematode behavior and how this influences their results. In particular, the behavioral difference observed between day 1, 2 and 3 could be expected as a technical artifact (i.e., in the absence of any underlying aging process) if nematodes remained in the same wells for multiple days.

3) The authors observe a difference in activity between nuo-6 and wild-type animals, and also between young animals and old animals. However, discussion of this is surprisingly qualitative given the quantitative thinking found elsewhere in the paper. Are the observed differences in movement approximately the same magnitude as what would be expected given previous results? Why is a significant difference between the two strains observed only on day one and three, but not day two?

4) The Figure 1 caption uses fM and fL while Figure 1 uses F1 and F2. Please make consistent.

5) Equation 2 is not fully displayed.

6) Introduction: Please give some concrete examples of experiments that require continuous long-term recording where low-resolution brightfield imaging would be the appropriate readout modality.

7) Introduction: The phrase "high resolution" is misleading, as the 15-22 µm resolution of this microscope would be considered very low resolution by most microscopists. Please insert the actual resolution here.

8) Results: I would not call this a high light collection efficiency design, as most standard microscopes have higher efficiency. Light collection efficiency is not very important here, so please change the language to be less contentious.

9) Results: Calling an LED source spatially coherent is really straining the definition. Please use different language.

10) Materials and methods: Something is wrong or confusing about the depth of focus discussion. Please cite a source for the equations and clearly define all variables. If u = f as you indicate in the text, then DOF=2c≠0.9 mm, which was stated in the text. The f-number does not appear in the equation you have, but the discussion seems to indicate that it is important (as would be expected).

11) Figure 2 legend: should be "(blue trace in B)"

12) Figure 3 legend: duplicated text "C) Focal plane…."

13) The authors limit their discussion of statistical analysis of animal movement to the legend of Figure three. This analysis would seem more natural to include either in the main text or in a dedicated statistical methods section

14) Provide more precise references to allow others to set up an ssHTS system; see for example the references for LEDs.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Random Access Parallel Microscopy" for further consideration by eLife. Your revised article has been evaluated by Didier Stainier (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors stress that one of the principal interests of the system is the capacity for rapid and continuous imaging. They write, "captures data 15 fps/well by measuring groups of eight wells in parallel". Then they write, "As the system captures data from multiple wells in quick succession at a rate of 120 fps, the time needed to acquire 100 frames for each of the 76 wells for this assay is just over one minute". They need to be more explicit. When they are capturing data from 76 wells, then are they imaging each well at ca. 1.5 fps? As it stands, a reader might understand that they are switching between groups of eight wells, imaging one group at 15 fps/well, then moving to the next group after capturing 100 frames (6.7 seconds). If this were the case, then they would return to image the first group after a minute, so their system would not be continuous. This clearly requires clarification.
