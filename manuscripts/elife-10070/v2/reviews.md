# Peer review - Round 1

Editors:
- Oliver Hobert, Columbia University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10070.057](https://doi.org/10.7554/eLife.10070.057)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Untwisting the Caenorhabditis elegans embryo" for peer review at eLife. Your submission has been favorably evaluated by K VijayRaghavan (Senior editor), a Reviewing editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Christensen et al. describes important technical advances in image analysis that will be important in delineating late embryonic developmental events in C. elegans, especially nervous system development. Previous attempts to analyze these stages (in which many key processes of differentiation and circuit formation occur) have been obscured by factors such as muscle movements and the unpredictably folded conformation of the embryo as it elongates. Christensen et al. show that advances in imaging and image analysis can overcome these obstacles, allowing them to generate an 'untwisted' straightened view of the late embryo over time. Although this is laborious (15 h work per embryo) it is an important proof of principle and will open up this phase of development to analysis. The manuscript is thorough and well explained. This work will be of interest to the C. elegans and 'developmental imaging' communities.

Requested revisions (in no order of importance; most of them quite minor):

General points:

1) The manuscript appears quite wordy and disproportionate to the lesson that the reader should extract. Please try to provide more concise descriptions.

2) The untwisted volumetric images of multiple animals need to be compared.

Specific points:

1) Nature of the folding/twisting of the embryo: This may be a minor semantic point but are worm embryos truly twisted (helically, around their axis) or folded/bent, or both? In larval development the body can only flex in the dorsoventral axis, it would be interesting if the embryo does undergo some helical twisting. The authors now have the first accurate dataset on this and it is an omission that ether is not a clearer account of how embryos twist or flex (just a rough statement that it is 'more complex' than in larvae.

2) Seam cell marker is introduced correctly as a marker for seam cell nuclei but later on they are just 'seam cells' which could confuse non-experts. The seam cells are doing a lot that is not captured by the nuclei positions.

3) How many points must be in the lattice for this to work? Can you define a minimum number or does accuracy increase with number of lattice points?

4) Seam cell V5 (Results, sixth paragraph) is presumably Q/V5, which divides in the elongating embryo (Sulston, 1983).

5) Elongation (as displacement of seam cell nuclei) is nicely shown to be biphasic. There have been relevant analyses in some papers on alpha spectrin, e.g. Norman and Moerman, that could be cited.

6) Results, eleventh paragraph: The nose is the anterior terminus of the pharynx (well, buccal cavity) not the intestine.

7) Seam cell displacement is described in the same paragraph of the Results as being 'at variable speeds' but I think the authors mean that different seam cell nuclei separate at a variety of speeds. Although from the data mentioned in the text it is not clear if the speed is different or the duration of movement is different.

8) The authors make a key point that elongation is non uniform along the axis, in that head seam cells separate more than body seam cells. This may not have been explicitly stated before elsewhere but is a natural consequence of the morphology of the comma stage embryo, where the head is thicker than the body so must elongate more. Thus elongation is mostly of the head or H cells, in contrast to postembryonic growth which is mostly in the body. Perhaps more could be made of these data and whether this relates to H vs. V cells seam fates.

9) The authors could discuss whether the approaches developed here could be applied to any other developmental systems.

10) A link to the open-source code, compiled software, and a tutorial to use both, must be present at the start of the paper, perhaps even in the Abstract (as well as other places within the paper). Since websites can go offline for a variety of reasons, it would be best practice to make the code, software, and manuals available as supplements hosted at eLife or perhaps on the Galaxy platform.

11) The authors perform some segmentation of seam cells and the Bao lab has produced software that tracks, in semi-automated fashion, embryonic cell divisions. The authors should address why they did not implement such a method here. In other words, why must every image volume be manually annotated such that a developing embryo requires ~15 hours of manual annotation? Is it not possible to annotate the first volume, then automatically track the seam cells in subsequent volumes thereafter (requiring manual input only when necessary)?

12) Figure 1E–G, left side: The green spline is hard to see above the green fluorescent markers, it would be best to choose another color.

13) Figure 1—figure supplement 2A) refers to a larva, not an "embryo". Also, it would be best practice to identify the larval stage.

14) Results, fifth paragraph: Measurement differences between twisted and untwisted seam cell pairs and the pharyngeal contour need to be quantified as variance or SEM across the 5 profiled embryos as opposed to stating "typical" values. The authors can include mean, max, median, mode… as well if they feel these give an additional perspective on the accuracy of their untwisting method. The same is true for the ninth paragraph and Figure 4—figure supplement 3, wherein we are given a qualitative term "most" instead of a quantifiable statistic. Some of this data is already present in Supplementary files 4 and 5 and should be used in place of the qualitative statements. This is present again in the eleventh paragraph where the tilde symbol is used instead of quantifying the mean and some form of variance (SD or SEM). And, once again, in the Methods, last paragraph.

15) Appendix 1—figure 16 claims that each segmented fluorescent marker pair has a unique color value but that is neither apparent, nor visible in the accompanying picture. Furthermore, algorithm detail #8 states that the short axis of the ellipses comprising the embryonic boundary is half the distance of long axis (between seam cell pairs). As shown in their accompanying EM image (Appendix 1—figure 18), the embryonic cross section is more rounded than this and so the estimated value appears much smaller than necessary. The authors should address this discrepancy. There is a possibility that this choice is affecting the X and Y measurements in the main Figure 3, the authors should address whether the choice of the ellipse's short-axis estimate changes these values.

16) Figure 3 is a phenomenal figure, capturing the power of the authors’ technique. If possible though, it would be helpful to have, in addition to the embryonic stage, the time since the first embryonic division superimposed at the corners of these images (E–H).

17) Results, eighth paragraph: It would be helpful if the authors could discuss potential causes for the time-shifts in elongation course observed between different embryos. Were developmental conditions strictly controlled or is this perhaps a consequence of variables such as maternal effects (starvation, contamination, plate age,…), room temperature, heat from the diSPIM, etc.? This would also help to elucidate what may have caused embryo 5 to have such a radically different migration for the CANs.

18) Results, tenth paragraph: To give proper perspective on these fits, it would be best if the authors could provide the dimensions of the egg. This should be easily recoverable from their image volumes.

19) Figure 5: I believe the axial distance panel annotations are reversed as it appears that panel B represents the least distance and D the greatest.

20) Methods, Strains: The promoters should be identified for the SCM and Coelomocyte markers. Future papers may find that these promoters contribute to deviations from wild-type development. Moreover, for the remaining promoters, the authors should provide forward/reverse primers, genomic locations, and/or paper citations wherein this information can be found.

21) Methods, Data Acquisition: The MIPAV site has been updated and the old link appears to be dead.
