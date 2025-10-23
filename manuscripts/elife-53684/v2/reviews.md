# Peer review - Round 1

Editors:
- Claire Wyart, Institut du Cerveau et la Moelle épinière, Hôpital Pitié-Salpêtrière, Sorbonne Universités, UPMC Univ Paris 06, Inserm, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53684.sa1](https://doi.org/10.7554/eLife.53684.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Correcting for physical distortions in visual stimuli improves reproducibility in zebrafish neuroscience." for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andre Maia Chagas (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The three reviewers agree that the study is of general interest and will help future studies on visual integration in zebrafish properly design their setups. Precisions and corrections are listed below. Please address all points raised and improve clarity of figures, check legends of supplementary videos.

Reviewer #1:

In this manuscript, the authors describe how to correct for distortions of the light path in vision experiments in aquatic animals. They first discuss and illustrate relevant physical laws and then showcase how distortions associated with suboptimal stimulus configurations could have affected two recent studies on looming stimuli in zebrafish. The impact of their manuscript can be subdivided into the following four points.

1) They raise awareness about stimulus stretching, compression and attenuation occurring in aquatic stimulus setups, which have oftentimes been ignored in zebrafish vision research. This will certainly be of high interest for the growing community of scientists working with aquatic animals, especially zebrafish.

2) The authors show that a critical parameter (da/dw) determines how the physical laws (Fresnel equations, Snell's law) will affect the stimulus appearance in one of the frequently used recording configurations: the apparent position of a stimulus is shown to depend on the ratio of the water column length and the free-air distance between display and water container (da/dw). While the physical laws are no news, the provided equation can be useful for scientists working with such a recording configuration.

3) They calculate, how stimuli have likely been distorted in two recent publications. This is a very helpful type of analysis that can potentially correct/explain observed differences in studies. The authors state that in the original publications the critical stimulus sizes were reported as 21.7° and 72.0° (difference: factor 3.3), and after their correction, the stimulus sizes were 0.6% and 1.9% (of 4π steradians, difference: factor 3.2). If I understand the authors correctly, the authors take the small absolute difference of 1.9% and 0.6% ( = 1.3%) as evidence for a better match after optical correction, because the absolute difference (14%) in the original studies before correction (72° – 21.7°=50.3° ~ = 14% of 360 degrees) had been much bigger. However, I don't agree that this is the best way to compare the results. The relative difference is about a factor of 3 in both cases, so not much different after correction. That being said, it is of course nonetheless very useful to perform these distortion calculations as they can be used to report the stimulus characteristics from the animal's perspective, which is what matters.

4) A programming tool is provided to help scientists calculate the distortions in their setups. It would be helpful if the functionality (inputs, outputs, available configurations) were described in more detail in the manuscript. The tool can be used for the experimental setup in Figure 1A, but for other configurations, users likely need to adapt it or use other software for ray tracing.

In summary, I think that the topic of the manuscript will be of interest to the community of aquatic vision researchers. The presented results and discussion present a rather incremental scientific advance, but are timely for zebrafish vision researchers.

Reviewer #2:

In this study, Dunn and Fitzgerald evaluate the effects of refractive index mismatches and consequent visual distortions upon zebrafish visual neuroscience experiments. They show that refraction at water-air interfaces causes distortions and translations to visual stimuli that, if ignored, will lead to erroneous conclusions about receptive field properties of visual neurons and visuomotor relationships. They show that accounting for Snell's law explains a large part of the apparent discrepancy between the critical angular sizes reported in two studies of looming-evoked escape behavior. The authors also provide a software tool to simulate the effects of refraction on visual stimuli.

Overall, this paper and the associated software will be of considerable value to the growing community of researchers investigating the larval zebrafish visual system. By highlighting an issue that has hitherto largely been ignored and providing means to improve experimental design and interpretation, the paper should enhance the quality and reproducibility of experiments in this important neuroscience model.

I have two main comments:

1) The authors do not appear to have considered the angular intensity profiles of the screens used to present visual cues. However, this will influence the most eccentric location at which an image feature (pixel) is visible to the fish as well as the observed intensity distribution. Moreover, the types of screens used in different studies vary. For example, Dunn et al. used a diffusive screen (for back projection) which will have some scattering characteristic – how was this modeled? Temizer et al. used an OLED screen where individual pixels have a (likely more limited) angular emission profile. This will determine the maximal theta' from which a ray can be emitted that will reach the fish, causing clipping at eccentric locations an affecting the size and amplitude profile of receptive fields. Can the authors incorporate the angular intensity profile of the presentation screen into their modeling (tool)?

2) It was not clear to me why the maximum image size is assumed to be 360° or 4π steradians. In the Dunn and Temizer papers, I assume angular size is computed according to a simple 2D model where one eye views a directly approaching orthogonal object.

In this case, the largest angular size subtended at the eye is 180° (at impact). However, the largest image size cast on the retina of a real eye will be limited by the visual field of that eye (and thus occur prior to impact). Similarly, for the analysis of solid angle, the authors compute percentages assuming a maximal size of 4π, which is clearly not biologically plausible. I would find it more useful if image sizes were given as a proportion of the (monocular) visual field. What is this estimated to be?

Reviewer #3:

I would like to start by thanking the authors for putting this paper together, as it is well written and definitely an asset for experimenters working with aquatic species, or in general for any other researchers that have visual stimuli that need to go through different media before reaching the animal/subject. I'm surprised that this issue hasn't been raised before, but glad to see that this is done here. I also enjoy the fact that they made a repository with more details on the tool they are proposing as a solution to the issue reported here, also that you can reproduce the paper's figures using this repository.

Here are some comments I hope will make the paper even more enjoyable:

1) Would it be possible for the authors to setup their repository to work with "My Binder" (https://mybinder.org/), so that readers who are not using/familiar with python could still use their notebook?

2) In the second paragraph of the main text the authors state that in traditional experimental setups for zebrafish, due to Snell's law, stimuli that are distant appear to the fish at the asymptotic value of ~48.6°, and that this would lead to a "Snell window" of 97.2°. I think this leads to some interesting questions:

2.1) In this setup configuration, the Snell window is covering what area of the bottom of the Petri dish? It would be nice to see visually represented what is the projection size of the window as size of the dish, since:

2.1.1) If the window is only covering part of the dish, the animals are freely moving, and the correction algorithm is used, this would mean that as the animals move, they could go past the edge of the window and be in a region where the stimulus is not present?

2.1.2) It would be nice to know how big the window projection is in relation to the animal's visual space, and how the distance between the petri dish and the projection window change this

3) The authors also mention that having water instead of air in the space between the petri-dish and the projection could be used as an alternative solution to the problem (main text, last paragraph), with the shortcoming of having a reduced transmission of stimuli in large angles. I wonder what these large angles would be? Would this be something easy to calculate? I wonder about this, since Franke et al. (https://elifesciences.org/articles/48779), show a "fish cinema" system where a lot of the fish's field of view is covered (while projecting directly at a screen which was the water container wall – so no air or water interface before the projected image)

4) One thing that I didn't see mentioned in the paper is chromatic aberration. Given the fact that stimuli are travelling through 3 different media at least, one could expect that different wavelengths will be projected slightly misaligned when compared to one another, especially considering the wide chromatic range present in Zebrafish vision? I wonder if it would be easy to incorporate these calculations in the tools they are describing, and most importantly, how could this affect the calculation of receptive fields, considering the misaligned patches of different wavelengths could directly influence some of these receptive fields?

I'm happy to clarify any points that might be unclear, or provide further arguments for the above mentioned points.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Correcting for physical distortions in visual stimuli improves reproducibility in zebrafish neuroscience." for further consideration by eLife. Your revised article has been evaluated by Didier Stainier as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers have addressed most of the comments from the three reviewers satisfactorily. The authors now include a description of the relative differences of solid angles between the two studies, which is good. However, the presentation is still somewhat confusing for readers, because the comparison of fractional apex angles and fractional solid angles introduces a huge difference simply due to the fact of switching from a one-dimensional to a two-dimensional/squared parameter (the solid angle is proportional to the surface area of the sphere). Thus, the effect of the optical correction is partially masked by the effect of this parameter conversion, and the current text fails to make this transparent and resolve it for the reader.

1) Without optical correction, the absolute difference of 70.3° and 21.7° corresponds to solid angles of 1.15 sr and 0.112 sr, which is a 10-fold relative difference [according to the equation Ω=2π1-cosθ; Ω corresponds to the solid angle, 2θ to the apex, see https://en.wikipedia.org/wiki/Solid_angle]. After optical correction, the relative difference is reduced to 3-fold (0.24 sr vs. 0.08 sr).

Our suggestion is to present results in the main text and in Figure 2C in relative steradian terms. The authors could state that the initial 10-fold difference in covered stimulus area (between the two studies) was surprising, but that after optical correction, this difference is reduced markedly (by a factor of 3).

The remaining 3-fold difference could potentially be explained by a dependence of behavior on the spatial stimulus location (as the authors already write). If the authors structure the paragraph like this, they could then also delete the following sentence, which they need in their current version to present results accurately, but which can be confusing and anticlimactic for readers and the story: "These corrections did not eliminate the discrepancy in relative terms, as Dunn et al. still found a critical size that was approximately three times as large as Temizer et al.".

2) We are not convinced that a 50.3° difference is "far more striking" than a similar relative difference at small stimulus sizes (as the authors state in their point-by-point response). Sensory systems typically encode stimulus magnitudes in logarithmic terms (Weber-Fechner law).

According to the logic used by the authors, a difference of 50.3° is striking irrespective of the base stimulus size. I think they would agree though, that two stimuli, 360° and 310.7° in size, are not very different. This is why the description of differences in relative terms is important, which the authors have now included in their revision.
