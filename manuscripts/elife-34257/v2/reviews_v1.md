# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34257.120](https://doi.org/10.7554/eLife.34257.120)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Routine Single Particle CryoEM Sample and Grid Characterization by Tomography" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Kuriyan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christopher J Russo (Reviewer #1); Georgios Skiniotis (Reviewer #2); John AG Briggs (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Noble et al. applied cryo-electron tomography in a large variety of single-particle samples prepared with a range of vitrification devices and grids to characterize the particle distribution in vitreous ice and the ice geometry in vitrified layers. The results demonstrate convincingly that the vast majority of particles in most cases adsorb to the air-water interface, a phenomenon with potential consequences regarding protein denaturation or complex dissociation, non-physiological conformational changes, as well as preferred particle orientation based on the preferential exposure of the most hydrophobic regions. This study, being the first to systematically examine particle localization in vitrified ice, is important given its implications for the rapidly developing cryo-EM field. However, a weakness of the paper is that it does not directly assess whether particle position really correlates with protein denaturation, orientation and reconstruction quality.

Essential revisions:

The authors suggest that the preferred orientation of particles in many cases is due to the exposure at the air-water interface. To this end it would be very helpful if they demonstrate through sub-tomogram averaging, e.g. as they show in Figure 8, that indeed the particles at the interface assume more preferred orientations compared to particles in the middle of the ice layer.

The authors state, e.g. in reference to Figure 5, that it is not clear whether observed protein fragments are from denaturation at the air-water interface, unclean preparation conditions, or protein degradation in solution. This is an important point. Can the authors show that in the majority of these cases there was no degradation in solution, e.g. by SDS PAGE or even negative stain visualization? Could the authors design an experiment showing that particles away from the air water interface are better than those at the air water interface?

It is disappointing that there is no overall analysis of whether sample distribution has an effect on the final 3D reconstruction. Could this be done?

The authors discuss that "protein network films may not be particle friendly", and suggest this might contribute to artefactual reconstructions. This is all rather speculative, but could this be assessed? There must be 3D reconstructions of most of such samples, is an effect seen in the 3D reconstructions where a protein network film is present?

The authors discuss that "particle adsorption implies preferred orientation". There is no explanation as to how preferred orientation was assessed or quantified. Could the authors design an experiment to show whether preferred orientation does correlate with interaction with the air water interface?

The discussion on collection and processing limits (illustrated in Figure 6) could also be followed up in the 3D structures – where the sample is tilted or thick, then changing away from whole-image based CTF estimation toward tilted or per-particle CTF should improve the reconstruction?

Some of the sample properties that the authors suggest should be measured by cryoET can typically also be assessed directly from 2D images. For example, one paragraph is spent on the observation that some areas have overlapping particles. This can be often assessed in 2D for the majority of samples. Concerning the statement "without previously characterizing the sample in the grid holes by cryoET, collection in these areas might severely limit the number of alignable particles due to projection overlap" – many users would see the overlapping particles in 2D images and decide to collect elsewhere. Similarly, people have used CTFtilt in the past to assess whether the field of view is tilted relative to the beam, and estimate the gradient. Tilted exposure areas are not a serious problem for all processing pipelines. Collecting some tomograms can provide a quick and relatively easy sample assessment, and it is a good idea to do this, it is not the case that users who do not do this are doomed to collecting bad images. Please provide a discussion along these lines.

The claims in the subsection “A significant fraction of areas in holes have overlapping particles in the electron beam direction”, about the effects of overlapping particles on cryoEM reconstructions should have citations for each claim or should be left out unless the authors wish to present additional evidence to support the claims.

Technical comments:

In reporting the tilt angles of the specimen in the holes, the authors have provided the magnitude but not the direction of the tilt angles. Even though the tilt direction w.r.t. the grid was unfortunately not tracked, the direction of tilt with respect to the beam axis is important for interpreting the results and statistics so the authors should include the tilt direction for all the tilt angles reported.

If 3D reconstructions of any of the specimen or sub-tomogram particles were performed, plots of the orientation distributions, especially from different regions within the same specimen corresponding to the tomograms presented, should be included. In addition, a more specific reporting of the extent of preferred orientation than "some" "yes" or "unknown" (Table 1) would be helpful.

A detailed description of the measurement of ice thickness, and the determination of the error in this measurement should be reported, i.e. how the value of 10 nm on P14L26 was determined and what are the possible sources of systematic error in these measurements.

For the errors reported in Figure 3, it is not clear if the standard deviation includes the propagated error from the individual measurements or is just the statistical error. This should be described.

For an individual tomogram, the error in the tilt measurement should be determined and included when reporting statistics on multiple tomograms. For example, Figure 3 column 4, the error in an individual tilt angle may be comparable to the value of the angle itself, but one cannot tell currently if this is the case or not.

There is little exploration of the relationships of the parameters that have been measured. For example, is there any correlation between particle size and ice thickness, or between ice thickness and grid type? Given the heterogeneity of the samples, is it appropriate to show average properties (Figure 3), but not explore relationships between parameters?

Comments on presentation:

The manuscript text needs rewriting for readability, at the moment it is very challenging. There are lots of very long sentences and very long paragraphs. The heavy use of "codes" (B2, 2+, M-preferred) is extremely irritating and often unnecessary, forcing the reader to reference figures and tables to understand the text.

The results are all contained within two tables are very difficult to use and understand. Why put three values in one column in brackets running over two lines rather than just three columns or sub-columns? Why use rather cryptic nomenclature like "3+" which requires some thought by the reader to imaging what it might really mean. Entries like "A2, B2 or B3 and B4 and B5‡ (50%), 0°" are hard to interpret, requiring the reader to repeatedly look at legends and other figures to understand anything. The presentation of the data should be rethought.

There are apparent inconsistencies in the manuscript. Some examples: Samples 25 and 46 are said to be ideal, but looking at the schematics in Figure 4, these are not the ideal samples? It seems to me that B1 "Free floating particles (no preferred orientations)" in Table 2 should correlate with + "indicates that there are free-floating proteins" in Table 1 but this does not seem to be the case? How can B3 and B4 be distinguished?

The tables are too small to read when printed – please make fonts larger or put in landscape mode.

The authors often use the term "freely-floating" when they actually mean "randomly oriented" or "randomly positioned." The particles are always under the influence of a variety of forces in solution, some in equilibrium and some not, and are never "freely floating" in liquid water; after vitrification they are stationary.

Throughout the text and tables there is unnecessary complication. Why refer to "ice behaviour (bottom)" as C2, rather than "flat". Why define "N-preferred" and "M-preferred" orientations?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Routine Single Particle CryoEM Sample and Grid Characterization by Tomography" for further consideration at eLife. Your revised article has been favorably evaluated by John Kuriyan (Senior Editor), a Reviewing Editor, and three reviewers.

We thank the authors for addressing many of our concerns. In particular, the new Figure 5 is very informative and a nice addition. However, it is disappointing that there is no further quantification as regards the effect of the surface-air water interface on the particles and the orientation of the particles. Comments expressed by the reviewers are given below, but note that we are not asking for any further work on the manuscript, except for dataset deposition (see below).

Despite the mixed opinions expressed by reviewers, after discussion among the reviewers and the reviewing editor we have concluded that your paper represents a significant contribution that we will be happy to publish in eLife. We are prepared to accept this manuscript as a Tools and Resources article, provided that some of the raw data are publicly deposited. Specifically, we request that both the 2D single particle data and the tilt-series/tomograms be deposited for at least a few specimen, such as, apoferritin, proteasome and maybe another one of the dozens in the tables that are of structures that are already available in the literature. We believe that these deposited datasets will become a resource to the community. When resubmitting the manuscript, please specify which datasets are deposited, and what the accession codes or preliminary processing information is for those datasets.

Detailed comments by the reviewers:

Reviewer #1:

I still feel that the authors have done a significant service to the field of single-particle electron cryomicroscopy by presenting this systematic and comprehensive study of single-particle specimen by tomography. It takes several somewhat abstract concepts, like preferential orientation and the air water interface and makes them strikingly obvious and easy to both quantify, and understand for new-comers to the field. The authors have addressed many of the statistical rigour concerns and certainly improved the paper from its previous version. Still, I am somewhat disappointed that the authors have not made better use of this data to address the questions which are not already clear to experts in the field: namely in what percentage of particles, for a particular specimen, and among different specimen, does adsorption to the air-water interface actually prevent structure determination by either destruction or preferential orientation. By quantifying these two outstanding problems the authors could have set a goal and a benchmark for the field as to the current state of the art as well as point toward the opportunity for improvement by some technological solution. Instead we only have the new Figure 5 which sort of hints that it is a mixture, but with no quantification of either effect.

Ultimately, this paper contains important and useful experiments and analysis that should definitely be published. But to the expert reader, the paper sometimes reads a bit like a straw man argument in that the authors claim that most people believe one thing, which is not universally true historically, given section 6 of Dubochet et al. 1988, so their claims about the "wide-ranging implications" of these observations ring less true. This is what makes the lack of quantification of the both the denaturation and orientation distribution of the particles disappointing as it strikes me as a slightly missed opportunity to push the understanding of the problem, and thus the entire field beyond what Dubochet clearly realised more than 30 years ago.

I think the paper can and should be published in eLife with minor revision if the authors are willing and able to deposit all the raw data (both tomograms and subsequent 2D micrographs/movies) for at least the specimen shown in the figures. In this way others will also be able to perform analyses to help understand the relationship, if there is one, between the location of a particle in a vitrified specimen and its usefulness in structure determination by cryoEM.

Reviewer #2:

I find that the authors have done a good job in addressing most reviewer concerns and comments. The new Figure 5 is very informative and a nice addition. Even though not all comments or suggestions could be addressed with updated experiments, the work is important to the cryo-EM field and the revised manuscript should be published without further delay.

Reviewer #3:

The authors have declined to address most of the essential revisions requested by the reviewers, reasonably arguing that the work required is substantial and it would be better to get the paper out there.

Here is the background to my opinion:

There are already some examples of particles clustering at the air water interface from tomograms – the ribosomes in Bharat and Scheres, Nature Protocols 2016, Figure 6 are a good example. It has been assumed since Dubochet, though has not been demonstrated, that particles at the air-water interface may be subjected to denaturation. It has also been broadly accepted in the field that particles showing preferred orientations often due so due to interactions at the air water interface:

"Occasionally particles adopt preferred orientations, presumably due to interactions with the air/water interface.": A primer to single particle cryo-electron microscopy, Cheng et al., 2015.

"In situations where the target adopts a preferred orientation due to interactions with the air-water interface or substrate, there may be a problem similar to the missing wedge problem": Single particle analysis at high-resolution, Cong and Ludtke., 2010.

This manuscript describes an interesting study, showing that the majority of particles in large number samples are located at the air water interface, but it doesn't tell us how detrimental this is for reconstruction, or why it does/doesn't happen. Many of the structures solved from these samples presumably went to high resolution, so this is an interesting question. I think that a descriptive study of the distribution of particles in ice is informative and interesting for the cryo-EM field, but in the first round of reviews we asked to go beyond this and ask how particle position influences the results of the single particle experiment. Without this, I feel that the manuscript is still of interest to the cryo-EM field, but does not have the importance that is typical of papers in eLife.
