# Peer review - Round 1

Editors:
- Jeremy Nathans, Johns Hopkins University School of Medicine United States

Reviewers:
- Austin Roorda, University of California, Berkeley United States

## Review text

DOI: [10.7554/eLife.49542.sa1](https://doi.org/10.7554/eLife.49542.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Rod nuclear architecture determines contrast transmission of the retina and behavioral sensitivity in mice" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Austin Roorda (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you will see, all of the reviewers were impressed with the significance and thoroughness of your work. All three reviewers also had specific and useful comments for improving the manuscript. Among them are three general suggestions to which we would like to draw your attention:

1) The Materials and methods section needs substantial editing for clarity and detailed methods of how forward/side scatter measures were performed. A large portion of the manuscript depends on this analysis and it is imperative to include the details.

2) Include a rigorous description of which tests are more or less behaviorally relevant for mouse vision. Showing data for ~1 cycle/deg may exaggerate the biological benefit, as does modelling a ~3 micron point spread function at the retina. The cat face may be marginally relevant based on visual angle on the retina, although it has a certain charm for the non-expert reader.

3) We encourage you to discuss other possible interpretations of the data, including competing hypotheses for the role of nuclear inversion.

Reviewer #1:

The authors have expanded on their previous work to understand the functional significance of the `inversion' of the nuclear architecture in nocturnal mammals, specifically, in this case, the mouse. The conclusion is that the inverted nuclear structure minimizes side scattering, and facilitates forward scattering with a resulting benefit that higher contrast images can reach the photoreceptors, thereby improving contrast sensitivity.

While readers might have inferred this conclusion based on earlier papers by members of this team, the authors do a very nice job of confirming it by comparing contrast transmission and behavioral performance between wild-type mice and mice with a genetic modification (TG-LBR) that prevents the 'inversion' from taking place (these TG-LBR mice appear to be otherwise unaffected visually). The wild-type mice show better contrast sensitivity of a magnitude of 18% and 27% for scotopic (nighttime) light levels compared to the TG-LBR mice. Interestingly, the wild-type and TG-LBR mice behave similarly under photopic (daylight) conditions, which the authors sensibly attribute to a reduction in noise caused by high-photon flux.

The improvement in performance of 18-27% is modest, but not negligible. The authors show that these modest improvements in contrast sensitivity serve to increase detection probabilities many-fold at dim, near-threshold levels. Therefore, the functional advantages of the nuclear inversion are convincing.

The Materials and methods section is very sloppy and needs to be revised. Also, there are some details missing (eg how forward and side-scatter is measured). Otherwise, the paper is well-written, the science is solid, and it sheds new light on the fascinating process of retinal development.

1) Abstract: `…retinal optical quality improves 2-fold…'. The authors overstate the optical benefit by choosing to report on one metric, which was the ratio of the areas of the MTF between the wild type and TG-LBR mice. This is an odd choice, because most of the spatial frequencies used for this metric are seemingly irrelevant for mouse vision. It would be more appropriate for the authors to provide in the abstract numbers for the behavioral improvements (18-27%)

2) Abstract: there should be no hyphen in `contrast-transmission'. (here and throughout the document)

3) Introduction paragraph one: what does less-dense mean? Are the authors referring to refractive index, optical density or actual density?

4) Results paragraph two and three and subsection “Flow cytometry”: Since it is so critical for this paper, it would be helpful if the authors could briefly describe how forward- and side-scattering are measured rather than just providing a citation.

5) Results paragraph three: The definition of side-scatter is vague. Here the authors define it as narrow scattering at 90 deg, but later (eg in subsection “Improved retinal contrast transmission”) they define it as scattering at angles > 30 degrees. Also the authors need to define the axis labels `Forward Scattering Area' and `Side-Scattering Area' in figure 1.

6) Figure 1C (inset). What does Volume-specific scattering mean? This needs to be defined.

7) Figure 1G: What do the rectangles in Figure 1G represent? Are they just sketched in or do the dimensions have an important meaning.

8) Subsection “Improved retinal contrast transmission” –, Figure S5: The authors state that they mimic the mouse eye by using an optical system with a similar f-number. But in the next paragraph, they state that the MTFs '…do not display a strict resolution limit.' These are conflicting statements. The use of limited aperture in the system means that it will have its own MTF. The authors should show the optical system MTF in their plots on Figure 3.

9) In the same subsection: The initials T.V. should be deleted.

10) What range of spatial frequencies were used for these computations?

11) Subsection “Improved retinal contrast transmission”, Figure 3:D2 and D3, subsection “PSF measurements”: The intensity of the PSF in the figure is lower for the TG-LBR mouse across the entire displayed range of -20 to 20 microns. But the authors state that the integrated intensity is the same between the two when the PSF is integrated over an 80 x 80 micron area. I am very skeptical that the integrated intensity under the two curves in Figure 3:D2 will become equal.

12) Results section final paragraph: "This suggest…."

13) Discussion paragraph one: The lack of `nuclear inversion' in diurnal animals is intriguing and the authors make a very sensible suggestion that the ONL is significantly thinner in diurnal animals. However, that statement should be backed up by proper citations or, better yet, a table or a plot comparing ONL between nocturnal and diurnal animals.

14) Materials and methods: In general, this section is sloppily written with numerous typos, combinations of present and past tense – often in the same sentence – and unclear writing. There are numerous typos. The authors flip between the abbreviation SR and strehl ratio.

15) Subsection “Calculation of MTF”. How do the authors propose to use this technique to measure optical impact of outer segments? Note that ex vivo preparations are vulnerable to optical artifacts, especially the delicate optical properties of the retina.

16) Behavioral assessment: What does the temporal frequency mean? Was the stimulus flickering? Or moving, or both? This entire section is very poorly written.

17) Subsection “Image processing and segmentation of ONL model”: Why was this smoothing necessary? Were the final results different when they were not smoothed? Does the smoothing generate refractive index profiles that are more realistic?

18) Subsection “Relative contributions to MTFs from ONL and outer segments”: Replace OS with 'outer segment'

Perhaps the Matlab script mentioned in the text should be shared.

Reviewer #2:

Paper Summary:

The authors build on a body of literature that has identified the interesting phenomenon of "nuclear inversion" in nocturnal mammals. In this report, the authors test the hypothesis that the re-organization of euchromatin and heterochromatin within the nucleus of rod photoreceptor cells could serve to benefit nocturnal mammals by reducing scatter in the outer nuclear layer which is thick in rod-dominant mammals such as mice. An impressive set of data is collected in the report. The authors interpret their findings as supportive of a role of improved contrast sensitivity due to nuclear inversion which purportedly reduces optical scatter, and thereby improves the contrast ratio of images that must project through all retinal layers before striking the outer segments of rods.

The paper is thoughtfully composed and was generally a pleasure to read. The data set is impressive and authors are congratulated on a wholesome battery of tests that span in vitro preparation, phantom simulations, mouse behavioral testing, histology with immunolabeling and transgenic animals that support the general hypothesis. The major criticism for the report, however questions the very raison d'etre of the manuscript; "just how beneficial is this nuclear inversion to mouse visual performance?" While nuclear inversion is indeed a strange behavior of outer retinal cells (especially rods), it is unclear whether this is an epiphenomenon of some other function important to rods, or whether, as the authors would suggest, truly provides visual contrast benefit to the animal. The authors provide some evidence in support of this idea, but there are several misleading conclusions drawn from figures (especially Figure 3) which overstate the contrast benefit to mice by using simulations that are not behaviorally relevant.

Problem 1: Authors show the MTF improvement of contrast transmission when projecting sinusoidal patterns directly onto the retina. The differences in retinal contrast appear impressive in Figure 3AB. When comparing pups or TG-LBR mice (which also do not have nuclear inversion) to the adult WT mice that do have nuclear inversion, contrast transmission appears to increase. However the range of spatial frequencies tested are not generally thought to be behaviorally relevant to mice. Reports by Histed MH, Carvalho LA, Maunsell JH. (J Neurophysiol 2012, and corroborated by a multitude of other studies) suggest that maximum spatial frequency cutoff for the mouse is near 0.5 cyc/deg. This represents the very lowest of the tested spectrum in Figure 3AB. By those measures, roughly 2/3 of the data is behaviorally irrelevant to the normal mouse. When considering data from 0-0.5 cycles/degree, the effect is visually modest in comparison. Reviewer requests revision of the figure to reflect the improvement range to that closer of what is relevant to mouse visual behavior.

Problem 2: Projection of 3 micrometer PSF into the mouse retina (Figure 3D) is behaviorally irrelevant. Based on the literature that the authors cite (and more), Geng et al., Schmucker and Schaeffel, 2004 and others such as Remtulla and Hallett, 1985, a 3 micron PSF is a highly unnatural stimulus for the mouse retina because of spherical aberration, longitudinal chromatic aberration, transverse chromatic aberration, a constantly growing mouse eye and an optically thick retina. Anything less than a single-wavelength stimulus therefore would be impossible to naturally project at a 3 micrometer spot, and thus it is unclear why the authors are using this highly unnatural stimulus to model the PSF spread in Figure 3D.

Problem 3: Authors attempt to simulate the behavioral benefit to the mouse by a friendly example of what the mouse would "see" in an approaching cat by showing a phantom of the cat face. This is a fun example, but again represents a scenario that is unlikely due to the visual acuity of the mouse (adult or otherwise). If assumed that behavioral spatial frequency is limited to ~0.5 cyc/deg, there is little chance the mouse would visualize the cat eyes at any distance represented by Figure 3. The reviewer calculates that interpupillary distance of a typical house cat (which is assumed to be a biotypical natural predator of the mouse? certainly not a tiger!) is 36 mm (following Hughes, 1972 Vision Research). If we are generous and round this to 4cm, the subtended angle on the mouse retina will surely not render the eyes of the cat in such a way that the authors illustrate. At 4 meters, subtended angle is nearly 0.57degrees. At 2 meters, subtended angle is 1.14 degrees. Again, this far exceeds the reported visual acuity of the mouse and therefore the example is inappropriate, behaviorally irrelevant and is misleading to the general scientific audience. There would be no visual benefit to the mouse in these conditions even if nuclear inversion were found to benefit contrast transmission. Request removal of this figure.

Problem 4: Problems 1-3 are further compounded that the generous spatial frequency cutoff for the mouse is 0.5 cycles/deg for photopic conditions (Prusky et al., 2000; Histed et al., 2012). Spatial frequency tuning for the WT mouse is considerably worse under scotopic conditions which is the regime that stands to benefit from rod nuclear inversion (authors report this is a rod-dominated effect and cones generally do not show such behavior). Umino, Solessio and Barlow, 2008, show scotopic contrast sensitivity is even lower than photopic in the mouse. Behaviorally tested cutoff is near 0.2 cyc/. When this is projected back on to the data from Figure 3AB,D1,D2,E and F) the behavioral benefit in Figure 3 seem to be baseless.

Despite these shortcomings, the manuscript has merit. Problems 1-4 are somewhat mitigated by compelling data in Figure 4 which do show a slight benefit in WT mice (with nuclear inversion) vs LBR mice which presumably do not. Scientific audience is left to trust that TG-LBR mice have otherwise normal ocular behavior with the exception of high-chromocenter rod nuclei. Further description of the phenotype would convince skeptics further (including eye size and anterior optical media clarity which could also account for the result in Figure 4).

In the discussion, the authors do not provide enough latitude that other epiphenomenon and bioselection-driven reasons for nuclear inversion are possible. The manuscript would be stronger if such openings for these possibilities are explored further. The reader is left with the feeling that the problem is solved, which it is not. Data is provided to support a hypothesis.

Figure 4F not described in Figure 4 caption.

Supplementary data is appropriate and impressive.

Reviewer #3:

The work by Subramanian et al. demonstrates that the inversion of nuclear architecture in the rod photoreceptors of mice improves visual function in dim light conditions. The paper is very well-written and easy to follow. The work is of the highest quality and the well-thought-out experiments nicely support the conclusions. It was a fun paper to read!

The strength of the paper comes from using a range of approaches, whole animals, tissue histology, dissociated cells, excised retinas, in vitro model systems, and theoretical calculations to demonstrate not only that the inversion improves visual function, but also provide a clear mechanistic explanation. Very convincing!
