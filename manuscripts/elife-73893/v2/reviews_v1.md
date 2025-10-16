# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73893.sa0](https://doi.org/10.7554/eLife.73893.sa0)

In this important work, the authors develop compelling new open source methods to study compound eye vision, with particular emphasis and examples in insects and appropriately supporting arbitrarily diverse spatial distributions, types and mixtures of types of ommatidia. The manuscript introduces example experiments to illustrate the use of the new methodology. This work supports future studies of invertebrate brains, a timely addition to the newly mapped connectomes of insect brains.


---

# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73893.sa1](https://doi.org/10.7554/eLife.73893.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "CompoundRay: An open-source tool for high-speed and high-fidelity rendering of compound eyes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by myself Albert Cardona as a Reviewing Editor and Tirin Moore as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Stephan Saalfeld (Reviewer #1); Andrew D Straw (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All reviewers agree that the raw ommatidial view buffer aspect of the work is the strongest piece and with the most potential to support neuroscience experiments. Expanding on this and discussing the possible applications in simulating insect vision and e.g., interpreting the neural connectomes of insect visual systems is most appropriate. Discussion of the modeling of e.g., insect compound eyes with asymmetric ommatidia is a must; one such example could be robber flies.

2) The motivation for the visualization for human observers is weak, and it is unclear of what use it can be for insect vision or vision research more generally. On surface, it seems a contradiction that the software goes to great lengths to model ommaditia with independent focal points, as necessary for the accurate modeling of each ommatidium, only to then project to a single nodal point to create a camera eye image, contrary to the main point of the work. A stronger motivation with explicit applications that aren't possible otherwise with this camera image are necessary. Otherwise, this aspect of the work ought to be downsized relative to the clearly innovative and useful raw ommaditial view buffer approach for compound eye vision research.

Reviewer #1 (Recommendations for the authors):

More details as they emerged, comments overlap:

98 Do you really mean that each ray has a maximum recursion depth of 0? Did you implement illumination by a light source? If rays do not recurse or trace to light sources, all surfaces are 100% diffuse and ambient and ray casting is equivalent to polygon projection with local illumination. If no illumination by an independent light source is implemented, all surfaces are 100% ambient and ray casting is equivalent to polygon projection. Please clarify.

64 – 67 The first two criteria both cover "arbitrary ommatidia geometry" which I think is one criterion.

65 Spectral sensitivity, which could be criterion 2 is not addressed as far as I understand. The renderer is purely RGB in 8-bit depth, correct? This is not discussed in section "Criterion 2" and could be a big obstacle for real applications. Is it hard to fix?

78 shadow maps are not more resource hungry than ray tracing with direct illumination, can you please explain better or remove?

84 interreflection of light can be implemented by e.g. calculating radiosity maps or doing sampling of rays cast from light sources. I do not see that CompoundRay is doing either, so it is not clear what the relationship to this work is? Can you please clarify?

Overall, I find the paragraph about ray-casting ray-tracing and the concrete relationship with CompoundRay unnecessarily confusing. As said before, I believe it would be better to explain the relevant differences of rendering methods only in how they relate to this project. I.e. how they produce an image (projection rendering by projecting polygons using painters algorithm, texture mapping and/ or colorize with local illumination model; ray-casting by identifying first intersection, texture mapping and/ or colorize with local illumination model, averaging over rays). Mention illumination, shadows (maps for each light in projection, testing for object intersection by tracing to light in ray-tracing) and global models (radiosity or photon sampling) only as possible extensions, not used in this work.

124 – 128 state the above but the language and reasoning are unclear.

227 – 229 eventually clarify that CompoundRay does not currently implement any illumination model or first order ray recursion to cast shadows, so the output would be equivalent to per ommatidium camera rendering and integration, this is way too late in the text as illumination and shading capabilities were used earlier to root for ray-casting for no practical reason.

Reviewer #2 (Recommendations for the authors):

Abstract:

L12-13: I think some expectation of why this might be relevant or interesting would be useful.

L19: Was there any insight that arose from doing this? Especially in regards to the idea raised above – that the shape and overall structure have been ignored?

Intro:

Figure 2: It would be helpful to explicitly indicate which approach is used in the present paper.

Figure 7, top panel and caption for top panel: If I understand it correctly, this top panel is a composite of 100s of individual images but I am confused that I do not see many, if any, vertical edges where one set of samples gives way to another. Also, the jagged effect is not particularly obvious.

Reviewer #3 (Recommendations for the authors):

Below I list a number of small details in need of attention.

Figure 2c could improve, at least by making it larger, or by magnifying a few adjacent ommatidia to better appreciate the effect of not sharing a focal point.

Line 124: Figure 1b is not adequate to illustrate that insect eyes "contain many hundreds or even thousands of lenses".

Line 183: "an image can be generated that captures the full compound eye view." But isn't the point that an image cannot be generated because of the lack of a shared focal point, assuming then that the brain's internal representation of the field of view will be the product of a neural network parsing the output of the many ommatidia? The "cone of influence" of each ommatidium on the final image seems … premature. Neural circuits will combine inputs from ommatidia in ways that have not been worked out in the insect literature, as far as I know. The motivation for wanting to generate an image is unclear: is this for ease of the researchers, which are human, or what is the goal?

The "raw ommatidial view buffer" seems most useful to neuroscientists. The design of a neural network that composes your "Display buffer" from the "raw ommatidial view buffer" would be a most interesting research project, particularly for the opportunity to compare it with the existing, mapped circuit wiring diagram, or connectome, of the Drosophila optic lobes. You could discuss this. In other words, Line 240, "These values are then re-projected into a human-interpretable view" is the potential start of a fascinating research project in its own right, if one redefines this as "fruit-fly interpretable view", as in, the brain of the fruit fly needs to make effective use of this information to successfully navigate the world.

Line 227: "Currently CompoundRay implements only a simple texture lookup, interpolating the nearest pixels of the texture associated with the geometry intersected." What would be gained by, or what is lost now relative to, implementing the full ray tracing approach?

Line 247: "Both pipelines share a common geometry acceleration structure and material shaders so as to save device memory." How is this possible? Can you hand-hold the reader a bit more to clarify how can both pipelines share the same GPU shaders? I may have missed a critical point.

Line 253: "rendering using a traditional camera skips steps 1", you mean, your software can alternatively use traditional cameras in place of modeled ommatidia? I am not sure I get it.

Line 293: "inhomogeneous ommatidial properties". An example you could cite is the eyes of the robber flies, Wardill et al., 2017 Curr Biol., where a frontal fovea with enlarged facets is reported.

Figure 6: seems to imply that overlap is not desirable? Overlap could allow for all kinds of spatial computations, from supraresolution to contrast enhancement to motion detection.

Line 309: the statements would apply only in the absence of a nervous system that would make full use of the ommatidial signals.

And, in general: aren't insect compound eyes known to present significant overlap in the field of view of each ommatidium relative to its neighbors? Figure 6c would then be the most realistic, if ignoring post-processing by the optic lobes?

Figure 7: qualitatively, the top rendered scene looks quite similar throughout. I am not able to notice much difference between the left and right ends. Figure 7 needs work to better convey your message, and to better establish or highlight the vertical relationship between the images in the top and middle and the plot at the bottom.

Line 357: "using a genetic algorithm to ﬁnd the location", where are the technical details of this approach? Parameters? Framework used, or code? Is it your own code?

Line 440: "On top of the potential biological insights CompoundRay may be able to offer", indeed, your paper would be so much stronger if you showed one such biological insight. It would then become a reference software for compound eye vision.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "CompoundRay, an open-source tool for high-speed and high-fidelity rendering of compound eyes" for further consideration by eLife. Your revised article has been evaluated by Tirin Moore (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Line 234: the sentence starting with "This will aid…" makes claims that, first, aren't entirely clear, and second, seem speculative and belong to the discussion.

Figure 10: the legend is far too short. Needs more detail on what each panel is, particularly for the lower panels. Also, where in the methods is the neural network described? Could be referenced here. Also, "network" is not quite the right shorthand to describe a neural network. Was it a CNN? Or generically an ANN? Or a perceptron?

Line 504: where is the Materials and methods description for the "4-layer fully-connected neural network"?

Line 532: "neural network was trained across 100 epochs three times", why? Why not 200 epochs, or 50, and 2 times, or 10? Why a batch size of 64? Also, these details are hardly worthy of opening the "Experimental results" section. Rather, they belong to the methods, alongside explanations and figures demonstrating why the set of parameters chosen are sensible and appropriate for the problem at hand.

Line 538, isn't the fact that a simple "single eye" design achieved a similar utility score concerning? Perhaps this reveals a disconnect between the test, which runs for 100 epochs (as plotted in Figure 10), and the real world, where an insect needs to take split-second decisions from the let go.

Line 565 reference to "Figure 10 bottom left" could really use the lettering of panels. In addition to a far lengthier and detailed explanation on what, exactly, is in that panel and how it was generated. And if these panels are as critical as they seem to be to evaluate the performance of the 3 eye models, then they ought to be bigger and far more richly annotated, to assist the reader in understanding what is being plotted.

Line 603: if you see opportunities for modeling the "recently reported" (2017) microsaccadic sampling in fruit flies, then why didn't you? Or is this the subject of a paper in preparation or under review elsewhere?

A question for the discussion: with its intrinsically distributed light sampling, compound eyes surely work not with frame-processing downstream circuits but rather event-based circuits, such as those of the dynamic vision sensor or silicon retina (Tobi Delbruck et al., various papers). Could you discuss the implications of asynchronous compound eye-based sensors, particularly when considering uneven ommatidial size which is not available in camera-based eyes such as in mammals or cephalopods? In a fast-moving animal such as a flying honeybee, asynchronous processing surely has advantages for motion detection and obstacle detection and avoidance, and scene recognition (i.e., flowers to land on), or better, to decode the waggle dance language of conspecifics.

Considering event-based computing could make for a much nicer discussion than the caveats of anthropomorphised, frame-based visual computing, or at least complement it well, outlining the intrinsic advantages of compound eyes.
