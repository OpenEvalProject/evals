# Peer review - Round 1

Editors:
- Hongbo Jia, https://ror.org/034t30j35 Suzhou Institute of Biomedical Engineering and Technology, Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74988.sa0](https://doi.org/10.7554/eLife.74988.sa0)

This paper presents a valuable method of mesoscopic imaging for behavioral neuroscience, particularly of high potential in applications such as tracking behaving subjects in 3D arena simultaneously with a neural population activity readout. The technical and conceptual advances are based on solid presentations of the engineering and the pilot experiments. Readers of this paper are advised to first gain a deeper insight of its working principle as well as the consequent advantages and caveats of this method before applying it in their own labs.


---

# Peer review - Round 1

Editors:
- Hongbo Jia, https://ror.org/034t30j35 Suzhou Institute of Biomedical Engineering and Technology, Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74988.sa1](https://doi.org/10.7554/eLife.74988.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "Gigapixel behavioral and neural activity imaging with a novel multi-camera array microscope" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, and the evaluation is being overseen by a guest Reviewing Editor and Didier Stainier as the Senior Editor.

The current reviewer consensus is that you are invited for a revision in which, the fluorescence imaging data shall be removed from the main text and the behavior imaging data shall be further improved primarily by addressing reviewer 1's comments. By doing so, the data quality and scientific value will meet the expectations of the journal. Other reviewer comments shall also be adequately addressed. If you accept these suggestions, please reply with a confirmation and proceed with revising your manuscript and resubmission. We will then advise further as soon as possible. Thank you very much.

Reviewer #1 (Recommendations for the authors):

There are really two applications here, one on large-scale behavioral imaging of multiple animals in parallel, and another on fluorescence imaging. The behavior story is clearly viable – it (nearly) achieves the titular gigapixel claim, makes effective use of stereo imaging to localize animals in 3D, and has already provided much of the characterization necessary to merit publication. The same cannot be said for the unconvincing attempt at fluorescence imaging, especially quantitative neural imaging, in behaving animals.

If this is just about behavior, with some added clarification and characterization, the manuscript would be fine. For fluorescent imaging, it's unconvincing that this can produce credible neural data. There are some serious conceptual issues with the fluorescence imaging experiments (discussed in the fluorescent imaging section below).

It might be advisable for the authors to split this into two, so that the behavioral side is not held up by serious design flaws on the fluorescence side.

Behavior

1. The manuscript contains repeated claims to be "inexpensive", but doesn't state how much it costs. The lenses alone appear to be >$7,000. 16 FPGAs and large custom circuit boards aren't cheap either. For fluorescence, filters alone would apparently add another $8,000 per MCAM or >$31,000 at gigapixel scale. Since the hardware and firmware are not open source, the company will presumably add significant additional costs on top of the basic material costs, which are already considerable.

2. "…comprehensive high-resolution recording from multiple spatial scales simultaneously, ranging from cellular structures to large-group behavioral dynamics." With 18 μm resolution (or worse, discussed below), the present invention does not record cellular structures except under extreme sparsity conditions. Even then, the measurements may not be sound (see fluorescent imaging discussion). It's unclear if "high-resolution" refers to behavioral imaging or fluorescence imaging, a conflation that occurs throughout the manuscript (see point #3 below).

3. The introduction conflates systems designed for neural imaging and systems designed for behavioral imaging. Throughout, it's unclear whether the authors are attempting to claim an advance in behavioral imaging or neural imaging. Existing fluorescent microscopy methods attempt to address real issues such as axial resolution, dynamic range, photobleaching etc. These are all problems that the current MCAM system does not attempt to address. For example, consider this statement: "Alternatively, closed-loop mechanical tracking microscopes have recently been developed in an attempt to address this challenge, but can only follow single organisms and thus miss inter-organism interactions." This statement is inaccurate in numerous ways: The citations jumble together systems for behavioral imaging only and systems for neural and behavioral imaging, which have fundamentally distinct requirements. It also misses recent work (Susoy et al., 2020) that used closed loop tracking to simultaneously image behavior and neural activity during worm mating, a form of inter-organism interaction. Susoy et al. were able to achieve both cellular resolution brain-wide imaging with sound microscopy techniques and observe sustained inter-organism interactions. Similarly, Grover et al. 2020 simultaneously imaged neural activity and behavior in copulating flies. The authors should take a more scholarly approach here, and make a clearer case for the merits and limitations of their system.

4. Regarding inter-organism interactions, this is overstated and confusing. In tracking microscopes, the field of view restriction is typically only on the microscopy side – the associated behavioral field of view is usually far less restricted. It is not difficult to simultaneously observe the behavior of multiple animals. Numerous existing methods using off-the-shelf parts and open source software already do so (Buchanan et al. 2015 as one of many examples).

5. The authors' claim of 147 lp/mm resolution appears to neglect depth of field / defocus issues as animals move axially. According to the lens datasheet, even a 20 lp/mm sample loses substantial contrast as it moves axially over a range of a couple millimeters. This degradation in resolution will be even more severe at 147 lp/mm.

6. "We performed standard flat-field correction to compensate for vignetting and other brightness variations within and between cameras (Methods)". This needs more detail. What are "other brightness variations"? Give numbers for the amount of brightness variation within and between cameras. This is especially important because inexpensive smartphone sensors assume a tilted chief ray angle (CRA) as a function of image height, which the authors do not discuss. How mismatched is the CRA with respect to the sensor's design assumption, and how much does this impact vignetting?

7. "Using this stereoscopic depth measurement approach yields approximately 100 μm accuracy in depth localization over a >5 mm depth range". How was this 100 μm accuracy number determined?

8. There is a troubling disregard to axial extent. In one instance, there is a reference to 5 mm height. In the case of zebrafish fluorescence imaging, the height is stated as 1-2 mm. Axial defocus should be characterized, and some statement of the practical usable axial imaging extent should be provided.

9. With regard to the siamese network / melanophore patterns, are the embeddings stable over recording time, animal pose, etc? There is insufficient detail to evaluate this. With regard to "250 augmented images per fish", how many real images of the animal were used, before augmentation? Is Figure 2c based on training or test? The number of real images used for training and test appears much too low to address questions of stability over time and animal pose, for example. Why is there no quantitative comparison of performance of training vs test?

Fluorescence imaging

There are some deeply concerning issues with the design that are not discussed in the manuscript. The manuscript seems to neglect the fact that existing microscopes have axial resolution, in addition to lateral resolution. Setting aside the necessity for more accurate characterization, there are some fundamental issues that are inherent to the imaging approach.

Fundamental problems with the design:

1. Without any axial sectioning capability, the fluorescent signal can be corrupted by the position and orientation of the animal. As the animal moves across the field of view of each microcamera, the detection PSF (point spread function) tilts in a position-dependent way, such that a different set of signals across the axial extent of the thick tissue are projected onto the same sensor pixel. Similarly, each time the pose of the animal changes, each pixel now is the summation of signals from a fundamentally different set of cells and even regions across the brain.

2. Ratiometric imaging cannot be done when the green and red fluorescence comes from different cells! This combined with point #1 above, means that every time the animal changes its pose, a given red fluorescent pixel is potentially summing photons from a different set of cells and brain regions than the "matching" green fluorescent pixel. This is fundamentally not sound. (The dual-color images in Figure 3h show obvious labelling differences, as expected from the use of different promoters and cell types in the two color channels.)

3. Related to #2, the red and green fluorescent light is collected from different cameras. This means that due to point #1, even if the same promoter was used for the green and red channels (as it should), each sensor pixel of the green image is sampling a different projection through the thick tissue compared to the corresponding sensor pixel of the red image. Applying cross-channel normalization of thick fluorescent tissue using this imaging geometry is fundamentally unsound.

4. Both lateral and axial resolution are depth dependent. Without axial sectioning capability, as the animals moves up and down in z, each point in the sample (e.g. a cell) contributes a different angular distributions of photons to a given pixel on the camera. To put this simply, a pixel on the camera is sampling a different distribution of signals depending on the axial position of the animal. This cannot be solved by ratiometric imaging. The information contained within each pixel is fundamentally changing as a function of depth. There is a reason that standard microscopy techniques go to great length to adjust focus as a function of depth.

5. The authors do not provide standard lateral and axial point spread functions (PSF) (i.e. using a submicron fluorescent bead), or demonstrate how both lateral and axial PSF change across x, y, and z. This is a standard optical characterization for a fluorescent imaging system.

6. Illumination brightness is not expected to be homogenous across x y and z. There is no discussion of brightness correction for either excitation or collection light across 3 dimensions. For characterization, the authors would need to show the results of a thin (submicron) fluorescent sample across the entire field of view, and across z.

7. Need a detailed analysis of signals from the red fluorescent protein as control. In the ideal case, the measurement from the red channel should of course be flat, but reporting the reality is important to establish the effective noise floor of the technique. The most problematic is systematic noise – intensity changes related to movement, lateral or axial position, animal pose or brain angle, all of which can lead to spurious correlations that complicate the use and interpretation of the fluorescence data in quantitative studies of animal behavior. Claiming detection of movement-related GCaMP activity is not that meaningful, as numerous studies have recently demonstrated that movement causes widespread activation throughout the brain.

8. The system is designed for visualizing inter-animal interactions, but there is no fluorescent data obtained during inter-animal interactions. When animals come into contact with one another, or overlap on z, a given pixel on the camera may become the summation of photons from both animals, further corrupting the neural signal.

9. If the system is to be evaluated as a microscope, the authors should provide a bleaching curve. Is the blue light on all the time, or is it strobed? How long can a user realistically image with this system?

10. There is no discussion on how a user is supposed to calibrate this system in 3D for fluorescent imaging. Though it's unclear to what extent calibration can alleviate the core conceptual issues embedded in the design.

11. The 2x2 Bayer filter is problematic, particularly for the fluorescence imaging case, where the effective number of imaging pixels isn't a gigapixel, or even a quarter of that, but in fact an 1/8th (green) or a 1/16th (red) of that. In the red channel, the effective pixel pitch appears to be around 18 um, which means the claimed 18 μm two-point separation is demonstrably false. For example, consider two (red fluorescent) point sources located at the midpoints of the 18 μm effective pixel pitch, spaced apart by 18 um. These will be detected as one bright red pixel flanked by two half-intensity red pixels, with no separation whatsoever. In the green channel, the effective pitch on one diagonal axis is twice the effective pitch of the other diagonal axis, and the same resolution argument holds.

12. The system that has been presented collects only 8 bit image data. Typical bit depths in microscopy systems range from 12 bit to 16 bit. The restriction to 8 bit is particularly problematic because due to inhomogeneities in fluorescence intensity of the sample and intensity of the illumination, combined with the desire to avoid saturated pixels which prevent extraction of quantitative signals, with 8 bit data one ends up with a severely limited dynamic range and severe quantization noise. The authors make no mention of the unconventional use of 8 bit data for fluorescence imaging, nor the associated caveats.

Claims that are not sufficiently substantiated or slightly misleading:

"To reduce motion artifacts, we started by embedding zebrafish in low melting point agarose and recorded spontaneous neural activity for 5 min". This should be removed from the paper, as it avoids all of the problems introduced by the MCAM imaging approach, most importantly brightness and focus changes over the FOV of each microcamera and over the 1-2 mm bath depth, as well as animal position-dependent and pose-dependent axial projection of thick brain tissue onto the 2D image sensor. The legend text greatly overstates: "Average ∆F/F traces of these ROIs show that differences in neural activity are easily resolved by the MCAM." To even partially address the many challenges posed by a freely behaving MCAM calcium imaging experiment, the authors should suspend the embedded animal from a motorized stage (e.g. a glass slide overhanging a typical lab XYZ translation stage) and then capture images of the brain over the ~ 38 mm x 19 mm field of view (including the corners of the rectangular field of view, which represent the most aberrated condition of the imaging lens), as well as the 1-2 mm depth axis that freely behaving animals move in. Note, I estimated the field of view of each microcamera to be 38 mm x 19 mm based on the sensor pitch of 19 mm and the 2:1 overlap strategy, but the authors should clearly state the actual numbers in the methods.

" While the MCAM in the current configuration cannot detect single-neuron fluorescence activity in the zebrafish brain, the data do show that our multi-sensor architecture can measure regionally localized functional brain activity data in freely moving fish". The data do not demonstrate sound optical principles and analysis. It's not just a matter of sensor resolution – the complete lack of axial sectioning/resolution is a fundamental problem. The wording appears to imply that MCAM eventually could, but this is impossible to evaluate.

Calibrated videos of freely swimming transgenic zebrafish with pan-neuronal GCaMP6s expression verify that our system can non-invasively measure neural activity in >10 organisms simultaneously during natural interactions. The word "calibrated" is unclear. What precisely was done? If the authors simply mean "flat-field corrected", then say that, or else add a description of this "calibration" in the methods and refer to it here.

"…the latter can increase both the information content and accuracy of quantitative fluorescence measurement in moving specimens". Due to the differences in view angle dependent axial projection of thick tissue onto a 2D sensor, angle-dependent sample occlusion (e.g. overlying pigment or blood cells), and other above-mentioned uncorrected differences in imaging performance across a large 3D imaging area, the current approach is fundamentally unsound. Claiming that it suitable for accurate quantitation is indefensible.

"…there are likely a wide variety of alternative exciting functionalities that MCAM overlapped sampling can facilitate". As an existence proof, please give one or more examples.

"i.e., the ability to resolve two 9 μm bars spaced 9 μm apart": This is misleading as stated. This should be described as "a center to center spacing of 18 um".

"…we used custom Python code to produce gigapixel videos from the image data streamed directly to four separate hard drives". A solid state drive is not a "hard drive". Just say "solid state drives" or "rapid storage drives".

Reviewer #2 (Recommendations for the authors):

This manuscript provides a useful tool for mesoscale imaging in complex biological systems. Simultaneous imaging at a large field-of-view and high resolution has been a challenge for biological studies, resulting from the optical aberration and data throughput of sensors. In this work, Thomson et al. proposed a flexible framework that enables multi-channel parallel imaging of 96 cameras from a field of view up to 20 cm*20cm and at a resolution of 18 μm. They have demonstrated various interesting experiments, which only be achieved with these mesoscale imaging and may arouse great interest.

Strengths:

This paper remains a great engineering effort. In order to achieve a large field view and high resolution, the authors build the 0.96 gigapixel camera array with 8*12 camera sensors, with 16 FPGA routing the image data to the computer. Two different imaging modes are developed: a full-frame mode with 96 cameras at 1 HZ and a single sensor mode with 4 cameras at 12 Hz, corresponding to fast and slow applications.

Also, I like the idea of stereo-imaging. Spatial overlapping is inevitable in image stitching, and most previous works tried to reduce the overlapping area to increase the data throughput and to reduce the inhomogeneous image. In this manuscript, all the imaging area is imaged simultaneously by at least two cameras, so the whole image is homogenous and the extra multi-view information is utilized for axial localization.

The authors have verified their system parameters in a series of biological experiments, such as zebrafish, C. elegans, and Black carpenter ants, which indicates its wide scope of applications. I believe all these experiments are quite interesting to a broad audience, e.g. social behavior for sociologists. Overall, I think the MCAM configuration is a promising initial scaffold for parallel image acquisition.

Weaknesses:

1. Although the paper does have strengths in principle, the weakness of the paper is that the strength of this system is not well demonstrated. The fundamental limitation of this system is the imaging rate is far too slow for the dynamic recording of various demonstrated applications, such as zebrafish's collective behaviors. The authors have realized this drawback and discussed it in the manuscript, but they do not give a practical estimation of how fast it could be, with up-to-date technologies. Is it possible to improve the speed by using different computers simultaneously for distributed data acquisition, as in Fan et al. Nature Photonics 13:809-816, 2019.?

2. Another concern is the asynchronized trigger mode for different cameras. When the exposure time of each image is short to avoid image blur, it is likely that all images are taken at different time points. Is it possible to use an external trigger to synchronize all cameras, or is it possible to output timestamp for each image, so that the error of time difference could be estimated?

3. In abstract and supplementary figure 2, the authors claim their system has 5 μm sensitivity, but this is confusing. The fact that this system can capture light from 5 μm beads, but not from 3 μm beads, is that the signal from 3 μm beads is not strong enough to distinguish itself from background noise. For example, if the illumination is strong enough, it is possible for microscopic systems to image small nanoparticles, but this does not indicate those systems have nanometer sensitivity. I understand that light collection efficiency is a serious concern for such low NA microscopic systems, but they should compare the light efficiency in a more persuasive way.

4. Another concern is the dual-color imaging. The fact that this system enables stereo-imaging seems to contradict dual-color imaging for 3d objects. Imagine there are two light sources at different depths, they could overlap on one camera but separate on another. I think more proper demonstrations are 2D samples, such as a disk of dual-color cells or worms.

Reviewer #3 (Recommendations for the authors):

The authors aimed at a low-cost technical solution for large-array gigapixel live imaging for biological applications. The endeavor is highly appreciated by the community as existing devices that are capable of such high volume of biological imaging are unaffordable or inaccessible by ordinary biological research labs. However, their current manuscript presented with design and engineering caveats that causally resulted in poor biological signal acquisition performance, as follows:

1) The low numerical aperture (NA, = 0.03) is inacceptable for imaging applications that require cellular resolution. The statement of the authors that their device can acquire cellular-level neuronal activities is unsupported by both optical principle and their demonstrated imaging data (Figure 3). This is due to the authors' optical design using simple lens per each sensor chip. Correct design strategy should be combinatorial, i.e., one set of lens per a subarray of sensor chips, that the optical NA can be sufficiently high to satisfy realistic cellular resolution in living organisms.

2) The image data streaming rate as 1Hz for full-frame Gigapixel image is too low for most biological applications that require temporal resolution to study behavior or cellular dynamics. However, this is an engineering bottleneck, not methodological. As a single sensor chip used in this study, the OMNIVISION's OV10823, does indeed support full-frame streaming at 30 Hz – which is nowadays commonly accepted in biological imaging community as video-rate imaging. The bottleneck is caused by the choice of low-cost USB3.0 transfer protocol and a single PC workstation. Solution to this issue is simple: parallelize the data transfer by using multiple PCs with either timestamp markers (e.g., synchronized indicator LEDs through the optical system per each sensor) or synchronized triggered acquisition. There is of course, a new concern to balance the cost/performance ratio.

3) the claim of 'cellular-level' signal or resolution has to be removed throughout the manuscript as the authors did not provide any evidence that what they claim as cellular objects or signals are indeed from individual cells. Proper wording for this type of low-resolution, low-sensitivity signal can be: cell population activity.

4) The authors made major efforts in applying machine learning algorithms for identifying and tracking objects in the stitched Gigapixel image, however, the authors did not consider the cost for implementing such working pipelines to handle such high volume of raw imaging data for obtaining biologically meaningful signals and analysis results. In particular, for tracking just a few animals as the authors presented in data, how much gain in performance is enabled by their device as compared to existing well-established methods using a single or few imaging sensors?

These concerns together suggest that the authors' design and engineering did not enable their claim of expected performance. Low-cost device is good for advancing science, however, only in condition when scientific criteria can be met.
