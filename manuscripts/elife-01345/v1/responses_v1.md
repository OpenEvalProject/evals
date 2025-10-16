# Author response - Round 1

Authors:
- Dan Shi
- Brent L Nannenga
- Matthew G Iadanza
- Tamir Gonen

## Response text

DOI: [10.7554/eLife.01345.019](https://doi.org/10.7554/eLife.01345.019)

The following substantive points should be addressed in a revision.

1) Specify the significance of the MR solution (TFZ and LLG). A 2Fo-Fc map should be shown after MR in order to assess the quality of the MR phases. Moreover, a “omit” refinement should be performed with a small fragment of the protein omitted (< ∼10%) and a difference map of that omitted region calculated in order to assess the potential model bias of the maps.

The significance of the MR solution is indicated in the methods section and a new figure was added showing the 2Fo-Fc map after MR and a composite omit map (5% omit) (Figure 6). These maps are also discussed in the revised text.

2) Plot a quantity related to radiation damage (for example, the average diffraction intensity) as a function of dose for each subsequent shot for the three crystals used for the final data set.

For each crystal that was used, we planned to plot average intensity versus dose at the resolution shell of 3-4Å. However, once we began the analysis we found that the large number of partial intensities made it difficult to accurately track any individual spot over a complete data set of up to 90 frames. We therefore performed an additional experiment to quantify the effect of dose on spot intensities. Diffraction data was collected from a single lysozyme microcrystal using a dose of 0.1e-/Å2 per frame. 120 frames were collected without tilting the crystal for a total accumulated dose of ∼12e-/Å2. In this way we could follow individual reflections throughout all frames and plotted the intensity values versus accumulated dose. This new data is presented as Figure 3 and discussed in the revised text. We found that the diffraction intensity is not adversely affected until the accumulated dose reaches a “critical” value of ∼9e-/Å2.

3) Figure 2A: Is the diffraction limit of the crystals related to size? In other words, is the useful limit related to the number of electrons per Bragg peak?

We do not believe this is the case as even crystals significantly smaller than those used here contain more than enough unit cells to get strong Bragg peaks. We updated the text to reflect this point more clearly.

A major limitation that we observed is likely because of inelastic scattering in thick crystals. We believe that we are not limited by the number of electrons per Bragg peak but instead inelastic scattering from crystals that are too thick is severely limiting the data. In this revised version of our manuscript we added data demonstrating that the achievable resolution is affected by crystal thickness. These are presented in Figure 2A and 2D and described in the revised text.

4) There is an XFEL lysozyme structure available to higher resolution (to dmin = 1.9) (Boutet et al., Science 2012) with comparable crystal size (less than 1 micrometer by 1 micrometer by 3 micrometers). This perhaps suggests that low-dose electron diffraction data collection is ultimately limited by radiation damage or the number of electrons per Bragg peak, in contrast to XFELs where radiation damage is circumvented, even at high-photon flux. The authors should comment on this.

We note that data in our study was collected to 1.7Å resolution but that the structure was determined to 2.9Å resolution. This resolution cut off is self imposed based on our current software limitations. As such we note that the resolution collected here is comparable to the study by Boutet et al. Science 2013. We updated the manuscript at various places (including the Abstract) to make this clearer. We apologize for the confusion and for not making this point clearer in the original version of our manuscript.

5) Did the authors try a standard indexing programs used in X-ray crystallography? It is curious why a new indexing program was developed.

We did initially attempt to use MOSFLM to process our data but were met with several roadblocks that, although not insurmountable, made it more practical to develop some basic programs of our own for this initial proof of principal. We still believe that one of the future improvements of this work will be its integration into current data processing software used in X-ray crystallography. Text was added to the Discussion and Methods sections highlighting this point.

6) Taking the maximum intensity among the set of equivalent reflection in order to approximate the fully recorded refection is a very crude approximation that depends on the chance of recording approximately fully recorded reflections. This chance in turn is related to the energy bandwidth of the electron beam, the crystal mosacity, crystal and detector parameters, and crystal size (for very small crystals). A discussion of these factors and parameters for this particular experiment would be useful.

We added additional text to the Discussion to highlight these points and suggested how some future improvements to data collection may improve the accuracy of the measured intensities.

7) The “blind” test cases either did not lead to a MR solution or they would not allow refinement. Please specify details: did some of the blind tests produce an MR solution, but refinement was stuck at high Rfree?

Table 2 was added to provide this information.

8) The observation of non-zero intensities for systematic extinctions is interesting. The explanation by dynamic scattering is possible, although could there be other possibilities, e.g., due to small crystal size?

We do not believe that the crystal size played a role here. Extensive studies from material science describe systematic absences appearing in diffraction patters dominated by dynamic scattering. When precession data was collected these spots were averaged out (For example see references Gemmi and Nicolopoulous, (2007) Ultramicroscopy 107:483-494; Gjonnes et al., (1998) Acta Cryst A 54: 306-319).

9) In the Introduction the authors commented on XFELs: the large sample requirement is a limitation of current delivery methods and data analysis (i.e., without post-refinement), not due to XFELs per se. However, the comment on the limited availability of beam time is well taken. In this respect, the low-dose method presented by the authors could be an important staging method for XFEL experiments, and the combination of both experiments could be very powerful.

We added the phrase “the current implementation of this technology” to differentiate that this is, as stated, a limitation of the current delivery methods, and not of the technique itself.
