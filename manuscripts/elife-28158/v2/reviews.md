# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28158.034](https://doi.org/10.7554/eLife.28158.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Rapid whole brain imaging of neural activities in freely behaving larval zebrafish" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Ronald L Calabrese (Reviewer #1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an exciting manuscript, which reports a new development in Light Field Microscopy (LFM). The authors developed a Light Field Microscope: eXtended (XLFM) field of view seamlessly integrated with an X-Y tracking system and an auto focus. XLFM can simultaneously image intact brain neural activities (over a volume of 800 µm X 800 µm X 200 µm) at ~ 3.4 µm X 3.4 µm X 5 µm spatial resolution and at 77 Hz volume rate, with the aid of genetically encoded calcium indicator GCamp6f in a freely moving larval zebrafish during visual stimulation and prey capture. They provide stunning videos and enough processed data to show the value of the new development for imaging activity across the brain during real behavior.

The work is nicely illustrated with exemplar data. This is not a full report on the science behind the experiments illustrated but rather a proof of principle. Exciting science is in the offing but a new technology is showcased, as is appropriate for a Tools and Resources paper.

Essential revisions:

1) We find this technology to be a significant advance. There are several technical issues, however, that must be resolved. Further clarifications to the text are needed about precisely what was done and how it was done. Some claims need to be more carefully worded to recognize the limitations of the technique and recognize other contributions. The writing should be improved. The expert reviews provide a detailed list of all the points that should be considered in revision. Rather than paraphrasing those reports, they are included in full to ensure that the detailed technological issues are well-stated.

2) As stated explicitly in the expert reviews, software and design features must be made fully available to the scientific community with publication.

Reviewer #1:

1) The chamber in which the freely moving larva swims is ONLY 0.8 mm deep. Thus the animal is sandwiched between glass plates with no real ability to move in the z-direction. Essentially, it moves in two dimensions. The authors should address this limitation in their approach.

Reviewer #2:

In Cong et al., two advances are reported. First, a tracking system is introduced capable of keeping a freely swimming larval zebrafish in one location most of the time. Second, a new form of light field microscopy is reported capable of fast 3D imaging. Putting these together constitutes a system for whole-brain imaging in freely swimming zebrafish larvae, with a resolution slightly below single-cell.

In my opinion this is a major advance and I am supportive of publication in eLife with a few improvements.

For background, previous efforts to perform whole-brain imaging in behaving animals consisted of light-sheet (slower than light-field) in head-restrained animals, or light-field (a variant with, I believe, lower spatial resolution) in head-restrained animals. Imaging in freely behaving animals has been done in C. elegans, which move more slowly than zebrafish. Thus, compared to previous work, the advances of this manuscript are considerable. Furthermore, imaging most of the brain in freely swimming animals in really impressive.

Points that should be addressed:

1) The authors claim that the point spread function (PSF) is spatially invariant. This appears to be true if one considers the microscope an ideal optical system, but with non-ideal optics, it's unlikely. Even with a good objective, the entire system contributes to the PSF, and it's unlikely that all microlenses are diffraction limited over the entire field of view. Moreover, differential distortion between the sub-images would cause the full camera PSF to warp as the point source moves in the sample. So if Richardson-Lucy deconvolution only works with a spatially invariant PSF, and the true PSF is not fully spatially invariant, the question arises, What image artifacts do you get?

There may be multiple ways to answer this question. One path might be to (a) move a bead around a few x-y locations, including the extreme ones, and check how spatially invariant the PSF really is (and include the raw PSF volumes in the manuscript, e.g. by measuring them at two extreme points, shifting one by the predicted amount, and overlaying the two in different colors). (b) Next, assuming a spatially invariant PSF derived from one of the bead locations (e.g. the center), reconstruct a bead positioned at various points, including the edges of the volume, and quantify the spread of the point source in the reconstructed volume (this should have high brightness at the original bead position, plus dimmer pixel values spread at other locations, which should be quantified).

2) A follow-up: if the PSF is not fully spatially invariant, what does this mean for the statement that overlapping sub-images are permitted (subsection “Image reconstruction of XLFM”)? My understanding is that the overlap is fine so long as the PSF is fully x-y invariant, and if not, then some artifacts will be introduced. The reasons and assumptions underlying this statement should be clarified in the text.

For clarity, points (1) and (2) are not criticisms of the system, only a call for characterization of the artifacts that the reconstruction algorithm introduces when using simplifying assumptions.

3) The reconstruction algorithm (subsection “Image reconstruction of XLFM”) contains confusing notation (if I understand it correctly). The coordinates (x,y) on the left hand side of Equation 5, refer to image coordinates. But (x,y,z_k) on the right hand side refers to coordinates in the 3D volume. That's confusing, x and y should not be used for both. Moreover, I believe that PSF_A,B(x,y,z_k) are each 2 dimensional objects. So in reality, spelled out with all the indices, using ^superscript for volume coordinates and _subscript for image coordinates, I believe the equation is

ImgEst_(x',y') = sum {ObjA^(x,y,z_k) conv^(x,y,z_k) PSFA^(x,y,z_k)_(x',y') +.…}

Explaining this equation better, e.g. by writing it out as above or stating that Img_est is a 2D object in image coordinates, and PSF_A,B(x,y,z_k) is 2D in image space contingent on x,y,z_k in volume space, will make this section more understandable.

4) Can the lateral resolution be measured instead of estimated?

5) The manuscript says the reconstruction algorithm is based on optical wave theory. What do the authors mean by this? The algorithm is based on the assumption of a spatially invariant PSF and observations of how to apply Richardon-Lucy to sets of microlenses of different focal lengths. Where does this rely on optical wave theory instead of just classical optics?

6) I assume CAD models of the microlens holder and the autofocus system exists, can these files be made available?

7) Most of the code is said to be available (e.g. real-time behavioral analysis and 3D reconstruction), but in some cases it is not mentioned. Can the code for the tracking and autofocus system be made available?

Reviewer #3:

My overall opinion of the manuscript is positive. I think being able to image neuronal activity in a freely moving larval zebrafish is an advance and the current paper serves as a satisfactory proof of principle.

I have some issues regarding the term "whole-brain" and the resolution claimed by the authors. The authors claim, or at least imply, that they can simultaneously (within 1 Orca camera frame which has a 2048 x 2048 pixel sensor) image 800 x 800 x 200 microns at 3.4 x 3.4 x 5 micron resolution. I find this very difficult to believe. Imaging with this resolution requires imaging 800/(3.4/2) = 470 pixels in both x and y for 200/(5/2) = 80 planes (the factor of 2 arise from Nyquist sampling). Given the sensor dimensions one can fit at most 25 planes into it (5 x 5). The authors show that they are able to use their microlens distribution to image 27. I do not believe there is enough information on the chip to have the claimed resolution. The authors may be able to distinguish 2 fluorescent particles 6 microns apart as in Figure 1—figure supplement 7, but these are still sparse particles appearing in the center of their CMOS chip, not a densely fluorescent tissue as a pan-neuronally fluorescent larval zebrafish. I think my argument is corroborated by the data shown in Figure 4: this data does not have the resolution claimed and does not show the whole brain of the larva.

The above argument assumes that the fish's head is also perfectly in focus. The z extent of a larval zebrafish head at this age is ~ 250 microns, which will already be larger than the z field of view. The axial shift shown in Figure 3, typically 20 microns but up to 80 will greatly affect this. The authors mention they use a 500 fps camera for the lateral tracking, but do not (or I missed) the speed of their auto-focus camera for axial tracking: how fast is this?

I do not think that these are "deal-breakers", but I think it is important for the authors to rewrite their claims and be explicit about what their system can't and can do (which is a lot). In the Discussion the authors claim to have developed a whole brain imaging setup: I am not sure what this means.

Figure 1 looks at an agarose restrained larval zebrafish. The authors should be explicit about this in the text and the Figure caption (for example the name of the figure). I do not think that panel d presents maximum intensity projections – they are far too clean for this (the bottom panel looks more like a snapshot of a 3d rendering of the stack). Can the authors correct this in the caption or be explicit about what they are showing?

Closed-loop systems have also been implemented in restrained fish with their tail free to move (e.g. Portugues and Engert 2011) which can remove the issue the authors mention relating to proprioception (Introduction paragraph two). The authors also mention improper vestibular feedback when fish are restrained, but in their setup, due to the closed look, the fish would also experience a reduced vestibular feedback: if the closed-loop was perfect the head would not move at all and the same vestibular deficits would be observed. If this is correct then the authors should comment on this.

The authors talk about "visual stimulation. What does this visual stimulation consist of? This should be explained in the Materials and methods clearly.

The claim in Results paragraph seven is a strong one and I am not sure it is fully warranted. Given the resolution and the data shown I would omit the phrase "for the first time" and again, explain carefully what is meant (here and in other places) by the term "whole brain".

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rapid whole brain imaging of neural activity in freely behaving larval zebrafish (Danio rerio)" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

This is an exciting manuscript, which reports a new development in Light Field Microscopy (LFM). The authors have made a strong effort at revising the manuscript in response to the last review. They have answered forthrightly almost every point raised and the manuscript is much stronger. There is still one major concern that must be addressed, and there some more minor concerns. The reviews are reproduced in their entirety to aid revision.

Major Concern

1) As brought up by reviewer #3 the definition and technical details of the claimed resolution are not adequately documented and explained. The detailed comments of the reviewer should be fully addressed.

Reviewer #2:

The manuscript has improved and I think that most of our comments have been addressed.

The changes include a new piece of useful information: the non-idealness of the point spread function (PSF) has been measured, and attributed, in part, to small differences in focal lengths of the microlenses.

I think this is great work and the revised version is even better. There are a few final comments I'd like to make,

In the subsection “Image reconstruction of XLFM”: "Furthermore, our system took practical conditions, such as imaging system and light properties, into consideration." What does this mean; can this be explained better?

About the reconstruction algorithm: The authors opt for sticking with the conventions and use the same indices x,y on both sides of the equation. This is ok, but in that case, some explanation should be added. For example,

"The 2D convolution is over x and y" and "Per convention in optics, x,y on both sides represent object space, even though in practice, x,y at the left will refer to image space on the camera chip and x,y on the right to the sample coordinates."

In the same section the authors seem to agree that the statement that the algorithm can deal with overlapping fish images depends on the invariance of the PSF, this information should be explicitly stated, i.e. include a statement like "under the condition that the PSF is spatially invariant, which is satisfied apart from small aberrations, the algorithm can handle overlapping fish images".

Results paragraph one: "Therefore, a spatially invariant point spread function (PSF) of the entire optical imaging system could be defined and measured (Figure 1—figure supplement 2)". Here also it would be good to mention that it's an approximately spatially invariant PSF.

A reference to a recept paper from the Vaziri lab, Nobauer et al., 2017, should be included. (This is also about light field microscopy, but I want to emphasize that this does in no way diminish the impact of the current manuscript.)

Reviewer #3:

As I mentioned previously, I like the paper, and the authors have addressed most of the minor issues appropriately. There are two points which I am still not sure have been resolved.

1) I do not believe the authors have fully addressed my previous point relating to resolution, which I reproduce below. This argument may be wrong, and I would be very happy if the authors could explain to me where my logic fails.

"I have some issues regarding the term "whole-brain" and the resolution claimed by the authors. The authors claim, or at least imply, that they can simultaneously (within 1 Orca camera frame which has a 2048 x 2048 pixel sensor) image 800 x 800 x 200 microns at 3.4 x 3.4 x 5 micron resolution. I find this very difficult to believe. Imaging with this resolution requires imaging 800/(3.4/2) = 470 pixels in both x and y for 200/(5/2) = 80 planes (the factor of 2 arise from Nyquist sampling). Given the sensor dimensions one can fit at most 25 planes into it (5 x 5). The authors show that they are able to use their microlens distribution to image 27.”

I am not worried about reconstructing the volume; that is not the point here. The issue is that of resolution and discriminability of points. This involves two aspects: the "optical resolution" of the imaging system and the sampling. The Rayleigh resolution criterion states the minimal distance resolvable is half the width of the first diffraction order. This depends on the wavelength of the light and the NA of the system. Ideal sampling is then obtained by using the Nyquist criterion: the inverse image of a pixel should be half the optical resolution of the system, so that there is a "negative dip" in between the two bright pixels.

Using this last sampling definition, the number of resolvable points can be estimated as follows:

- every bright pixel has to be surrounded (in the chip) by a dark set of pixels.

- the number of bright pixels you can have on the chip in this configuration is the number of resolvable points. This is a quarter of the number of pixels on the chip.

- ideally, the inverse image of a pixel should be a quarter of the first diffraction order peak width, for sampling and optical resolution to be perfectly matched.

With a 2048 by 2048 chip, there are at most ~ 1 million resolvable points.

The authors claim they can resolve ~ 2.2 million (800 x 800 x 200 microns at 3.4 x 3.4 x 5 micron resolution).

Deconvolution is a linear process, so XLFM may "shuffle or combine" the intensities of different pixels, but must do so in a linear way.

In addition, as the authors state, the NA of the objective (nominally 1.05) is greatly decreased (to an effective 0.4) because a lot of light is blocked by the array casing. The optical resolution of the system is bound to be significantly affected.

Figure 1—figure supplement 7 does try to address this issue, but I remain unconvinced because column 3 of panel b shows no dip whatsoever in between the two particles. This indicates to me that the authors are not using the Rayleigh criterion. It is definitely possible to separate two identical Gaussians whose positions differ by less than two SDs (situation which approximates to the Rayleigh criterion), but this is not what is usually called resolution.

2) I am not sure I understand the authors' claims of a spatially invariant PSF. In Figure 1—figure supplement 9 they in fact show it is not spatially invariant even within the focal plane (which they attribute to variation in the magnification across microlenses).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rapid whole brain imaging of neural activity in freely behaving larval zebrafish (Danio rerio)" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and one reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. Given that this would be a third round, we must now bring this process to a close with no possibility of further revisions.

Reviewer #3 concerns must be addressed more fully.

I appreciate the authors' comments to the points I raised, but unfortunately I do not feel they have been addressed. I still believe there are two points which need to be addressed: the resolution and the PSF. I think both these points could be addressed by rewriting the manuscript and making claims that are both theoretically sound and supported by the data presented. Given that the manuscript is a proof of concept about an exciting and promising new imaging technique I think it is fundamental to be precise, as this paper will set the baseline for all future work involving this technique and other freely swimming whole brain imaging approaches.

1) Resolution.

The authors have not addressed my argument or provided a counterargument. I still believe my argument is correct. I think the authors are under a misconception. As I mentioned in my previous report, the resolution of an optical system depends on only two things:

a) The optical resolution of the system that results in the Rayleigh criterion.b) The sampling resolution that results in the Nyquist criterion.

Specifically, the resolution does not depend on either the reconstruction (as suggested by the authors in answer to my first review) or the sparseness (as the authors argue in the answer to my second and third review).

I repeat the basis of my argument. Given the dimensions of the chip, the number of resolvable points cannot be more than ~ (2000/2)^2 which is about 1 million. This assumes that a diffraction-limited point in the sample is images onto 1 pixel in the camera chip and that the whole chip is used. The first point is not true for the current system (see Figure 1—figure supplement 9 in which a 0.5um bead results in at least 6 reconstructed pixels in the image). In fact, a one such diffraction limited spot will automatically be imaged onto 27 points just by construction). The second point is also not true for this system (see Figure 1—figure supplement 5 in which only about half the chip is used). My estimate is that at most one fifth of this upper limit of the number of points can be resolved, about 200,000, and probably much closer to 100,000.

Paragraph two of the Results is now very confusing. In the second sentence, the authors state that they can image a field of view of ~ 800 x 800 x 200 μm with 3.4 x 3.4 x 5 μm resolution. This corresponds to 2 million resolvable points. This is probably a factor of 20 out. Then later in the paragraph it is claimed that it is 500 x 500 x 100 μm at this resolution. This corresponds to 400,000 points. First of all I think this is still way too high. And secondly I do not understand the contradictory statements in this paragraph. The resolution does not depend on the sparseness. In addition, one can interpolate and reconstruct at whatever desired resolution to make pretty images, so this does not play a role either.

2) PSF.

The authors have developed a deconvolution algorithm that to my understanding calculates an effective PSF which they assume to be spatially invariant (in 3 dimensions) and which they then use to deconvolve their data. If this is true I think this is a statement that I am very happy with and support. In traditional lightfield microscopy it can be shown theoretically that the PSF is not spatially invariant. I cannot see why the setup presented by the authors would result in a spatially invariant PSF. If they claim this it should be shown theoretically (this is a methods paper). I agree that inhomogeneities arising from unequal microlens magnifications will contribute to worsen the spatial invariance of the PSF, as argued in Figure 1—figure supplement 8. But I do not believe this is the only source for them, so I do not agree with the statement in the figure legend. In Figure 1—figure supplement 9 the authors show that the PSF is not spatially invariant. And the data here relates to the "focal plane z=0" How does the PSF look at x=400um and z =100um? It will most likely look "worse" than that in the last panel of this figure. The authors seem to propose that the PSF of their imaging system is spatially invariant until it is not, away from the center of the field of view and the focal plane. This is not a rigorous scientific statement and not one which can be made in a methods paper that proposes a new imaging technique in a highly regarded journal such as eLife. I can definitely stand and support the argument put forward in the first sentence of this paragraph but if the authors claim spatial invariance they will have to either theoretically prove it or measure the PSF throughout the field of view and show it (and Figure 1—figure supplement 9 contradicts this).
