# Peer review - Round 1

Editors:
- Edward H Egelman, University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35383.016](https://doi.org/10.7554/eLife.35383.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "cisTEM: User-friendly software for single-particle image processing" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Ed Egelman) and John Kuriyan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sjors HW Scheres (Reviewer #2); Henning Stahlberg (Reviewer #3); Bridget Carragher (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary

This paper describes a new image processing software solution for cryo-EM single-particle analysis called cisTEM. cisTEM combines many existing and very popular tools from the Grigorieff lab (CTFFIND, UNBLUR, FREALIGN) with several new functionalities, such as auto-picking, 2D classification and ab initio model calculation. The existing tools were all very popular solutions in the field, and their inclusion into cisTEM has motivated a complete re-write in C++. By careful code optimisation, the new programs now run at speeds that are comparable with (or even surpass) implementations by others on GPUs (e.g. RELION or cryoSPARC). In line with their excellent track-record, the authors release the code as open-source, which is laudable in a time where many new software implementations have moved towards licensing solutions for non-academic users. Modifications to existing methods and new methods are described in sufficient detail to be useful for potential users, and in many cases even for those programmers eager to implement their own versions. The GUI described appears to be well thought-through and thereby a good help for less experienced users. This is particularly relevant for access to the 3D classification and refinement approaches, which were less accessible in previous versions of FREALIGN. The results presented for β-gal are impressive: a 2.2A reconstruction is state-of-the-art, and the execution time below 5 hours is extremely fast! Therefore, this tool will undoubtedly be extremely useful for the field. The performance of cisTEM is amazing, in terms of resolution and speed. The authors are to be congratulated for making such a wonderful package available as open-source.

Essential revisions:

1) Eq 15 does not have a CTF_i component. Is that part of the projection operator (with the funny P)? If so, that would be good to spell out. Otherwise, CTF_i should be added to the equation.

2) It was unclear whether the 3D classification approach only marginalises over classes, or whether the marginalisation over the 3 in-plane orientations can also be performed. Perhaps an extra sentence would help.

3) Is cisTEM capable of on-the-fly processing? If so, it might be worth spelling that out, as many EM centres in the world are moving towards automated processing of images while they are being acquired.

4) In subsection “Parallelization”, the authors describe a flexible home-made solution to queueing many little sub-jobs, which could provide additional flexibility on busy clusters. However, it might very well be that many clusters require a given number of free nodes to be specified in their own queueing system in order to use the cluster. Perhaps an additional sentence about this could be added?

5) cisTEM is available under the GNU General Public License. This is not stated in this manuscript but should be.

6) Introduction: Use "direct electron detectors", not "direct detectors".

7) Subsection “Particle picking”: Please define "mode" in this context.

8) Subsection “Particle picking”: It is obvious that the "need" is there now for external users. This statement could be rephrased.

9) Subsection “3D refinement (FrealignX)”: The size threshold of 400kDa, up to which individual particle defocus refinement might be helpful, will depend on various other parameters, such as kV, defocus, ice thickness, electron detector, etc. This statement could be extended to state that this threshold applies to current typical hardware and sample preparation methods.

10) Subsection “3D refinement (FrealignX)”: For the description of applications of particle-wise CTF refinements, it would be helpful to specify, if this was done using the absolute values of the CCterms in Equation (9b), and if so, which Resolution R2 was used as transition from signed to unsigned CC values.

Also, how much does the particle-wise CTF refinement improve the final resolution, if the signed versus the unsigned CC calculation is used?

11) Subsection “3D refinement (FrealignX)”: FSC calculation is done for particles aligned against a single reference, which is resolution limited to a value well below the current resolution estimate minus 2/Dmask. However, here the authors also state that the users can set the resolution limit of the reference to arbitrary values, at their own risk. This sounds like a dangerous option for unexperienced users. Does cisTEM in such cases print out a big fat warning somewhere?

12) Subsection “Ab-initio 3D reconstruction”: "3 direction are chosen". ("s" is missing in "directions").

13) Subsection “Ab-initio 3D reconstruction”: What are the 3 directions that are chosen here? Are those random, linearly independent directions? Or are these related to symmetry axes? Please specify or explain better.

14) Discussion section: GPU hardware doesn't have to be noisier that CPU hardware. Water-cooled housings and water-cooled GPU cards are available, even though at higher costs. Several high-end GPU systems are absolutely silent, even under load. This statement is only valid under very specific settings. I would remove or rephrase it.

15) It would be helpful to know how projects are tracked in a multi user facility. In some facilities there are 100's of different projects, many of which must be well separated for confidentiality reasons. How does cisTEM handle this?

16) Can new programs easily be incorporated into cisTEM? For example, on one of the few features lacking right now is per particle unblurring and I suspect that many people will want to go with motioncorr2. While the authors discuss the intimate link between the GUI and the code as a positive, it would also be good if there were some options to "wrap" other programs as needed. If not, I suspect users will continue to leap in and out of a multitude of packages.

17) Does the package provide a way for sorting particles or images based on confidence values or outputs. E.g. reject all images where the CTF fit is poor etc.

18) While I accept that the DoG algorithm can be modified to select β-gal I would like to know if it really can be optimized on something much more stick like. If not, then I suspect users will have to exit the program to use a template picker until one becomes available. Again, pointing to the value of wrapping one of the many very good available template pickers.

19) It has been discussed by Gabe Lander (and other groups, too) that there is an advantage in packing particles very closely together across holes (e.g. see the Aldolase images in https://www.biorxiv.org/content/early/2017/05/25/141994). How will this affect programs that need to select background regions for determining optimal particle picking parameters or for noise whitening etc.

20) Per particles defocus is also likely to be very useful for images that are tilted relative to the electron beam or that are in two layers (see for example: https://www.biorxiv.org/content/early/2017/12/11/230276). Could the per particle be done in patches? How do the cisTEM results compare to those of gCTF for small particles? Is it possible that the lack of improvement for β-gal compared to the virus is because the method just failed due to the lower signal? How would a user know this? One way might be to plot the defocus values as z-heights which if particles really do all adhere to an air water interface will be in a plane. This might also help smooth out outliers.

21) Should cryoSparc be part of the initial set of software referenced in the Introduction.

22) What FSC is reported, 0.143?

23) Masking instructions are a bit confusing (Subsection “3D refinement (FrealignX)”).

24) Subsection “3D refinement (FrealignX)”: What happened without the mask?

25) BSC scoring (Subsection “3D refinement (FrealignX)”) description is a bit vague.

26) How does the masking affect the FSC exactly – does it come out the same?

27) Subsection “Map sharpening” calculate should be calculated (and this was the only typo I noticed!)

28) Database is interesting, but it is not clear if is it useful to the end user or just the programmers. It might be polite to reference Appion which has been using a very effective database as a tool for delivering results to users and wrapping disparate software packages for over a decade.

29) Can cisTEM be run remotely? Does your computer have to stay awake during a long action?
