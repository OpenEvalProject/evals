# Peer review - Round 1

Editors:
- Timothy Verstynen, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53232.sa1](https://doi.org/10.7554/eLife.53232.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Cross-species cortical alignment identifies different types of anatomical reorganization in the primate temporal lobe." for consideration by eLife. Your article has been reviewed by three peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Katja Heuer (Reviewer #2).

Summary:

This manuscript describes a cross species analysis of temporal lobe organization between three primate species (macaque, chimpanzee, and humans). Using cortical myelin mapping to define regional organization and diffusion weighted imaging (DWI) tractography to define connectivity profiles, the authors tested the hypothesis that species differences in temporal lobe organization do not just reflect expansion/movement of specific modular regions, but also a fundamental reorganization of connection topology as well. The simple null hypothesis is that species-differences in the location of white matter fascicle terminations will be completely explained by migration of cortical regions. The authors found that, for a subset of temporal lobe regions, including the arcuate, ILF, and SLF, the shift in connection topology from macaque-to-chimp-to-humans is not completely explained by migration of cortical areas. The authors conclude that regions undergo different evolutionary modifications beyond the location and extent of distinct functional regions in the cortex.

All three reviewers found this to be a very clear, compelling, and contributes a valuable insight into the anatomy and possible evolutionary scenarios of several major temporo-parietal fiber tracts across 3 primate species, as well as with a refined method for a cross-species registration. The hypothesis is rational and clear, both in what it predicts and how it links to the methods used to evaluate it. The story that emerges is interesting both from an evolutionary neuroscience perspective and for understanding the specialization of the temporal lobe in humans.

Over the course of the review and consultation, a few critical concerns were brought up that fall under common themes. These concerns are consolidated here.

Essential revisions:

1) Hypothesis evaluation.

Reviewer 1 found that the logic of the hypotheses as laid out in Figure 1 are quite clear and follow a rational logic: if differences in white matter topology are simply following the movement of functionally specialized regions across evolution, then accounting for the migration of cortical areas should full explain endpoint locations in the major white matter fascicles that are preserved across species. However, this all relies on the assumption that the measures used to both map cortical regions and map connectivity are veridical and without noise or bias. Unfortunately we know that this is not the case, especially with the DWI tractography. The authors should see these papers for a review of these problems:

– Thomas, C., Frank, Q. Y., Irfanoglu, M. O., Modi, P., Saleem, K. S., Leopold, D. A., and Pierpaoli, C. (2014). Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. Proceedings of the National Academy of Sciences, 111(46), 16574-16579.

– Maier-Hein et al., 2017.

Not only are DWI tractography results sensitive to biases with respect to resolving individual fascicles depending on their geometry, but differences in DWI sequences can lead to different tractography results. Both are problems for comparing across species: i.e., the same pathway may have different geometries that make it easier or harder to track reliably and each species was imaged using different DWI sequence parameters (e.g., TR, number of directions, diffusion gradient strength).

This leaves an alternative explanation for the results shown in Figures 3-5: perhaps noise in the tractography process leads to different cortical endpoint fields in the different species. Right now, it is impossible to distinguish between this and a reorganized connectivity profile hypothesis. You should find a way to vet the connectivity reorganization hypothesis against the "noisy measures" hypothesis.

Reviewer 3 raised a similar concern, pointing out that if some tracts have extremely low overlap between predicted vs. actual – can this be attributed to real evolutionary/phylogenetic differences or an artefact of worse accuracy in transformation? Reviewer 3 shared one proposal for how this could be quantifiable using existing data and techniques used in the paper. The authors should feel free to improve this suggestion.

If we can create a distribution of how extent of errors in registration map to errors in tractography predictions (dice overlap, predicted tract extension), it would provide an upper bound of the largest possible discrepancies in tractography predictions. Then if the observed non-overlap in AF tracts exceed what one might expect due to registration errors alone, then indeed this provides more definitive evidence that such non-overlap can truly be attributed to phylogenetic distance between species. One way to do this is as follows:

– Step 1: In order to align macaque to human brains the paper suggests that a composition of transforms from macaque to chimp then chimp to human provides more accurate registration than a direct macaque to human mapping. One option to investigate the consequence of registration errors is then to compare the superior but indirect macaque to human transforms with the less accurate direct transform. Ultimately any macaque to human comparison has the same phylogenetic difference, so the discrepancy between the direct and indirectly transformed myelin maps offer a distribution of registration errors.

– Step 2: Analogous to analyses already performed in the paper, one can also perform tractography predictions using the direct macaque to human transform, in addition to the indirect transform already performed. Any discrepancies between the direct and indirect predictions are now attributable to registration errors.

– Step 3: For each of the investigated tracts it would be useful to create a 2D joint distribution of registration discrepancy and tractography discrepancy. This would provide an overall picture of how worse registration might lead to worse tractography predictions and thus provide a useful guideline for follow-up studies.

– Step 4: The bar plots in Figure 5 can be augmented with an additional bar corresponding to the less accurate macaque-human transform, to act as a "secondary control" for the current macaque to human comparison. Unfortunately, I cannot think of a way to provide a similar control for the chimp to human comparison.

2) Concerns with spatial alignment.

Reviewer 2 noted that some cortical regions are very compressed when mapped into a sphere, in particular, the frontal pole or the temporal pole. Have you evaluated the impact that this may have on a cross-species registration? And with larger geometric differences between 2 of the species as compared to the third?

Reviewer 3 asked what factors prevent the macaque/chimp to human projection from being an unbiased one? Suppose that one has an oracle that could learn the theoretically best possible cross-species registration by perfectly mapping all changes due to expansion/relocation all over the brain. Where might we expect myelin based registrations to differ from such an oracle?

a) Accuracy of spatial registration maybe unevenly distributed. The authors allude to this in the Discussion. Appendix 2—figure 1, also provides evidence of mesh distortion. I take these maps to be evidence of potentially uneven accuracy of spatial registration. There certainly seems to be some evidence that frontal areas and temporal areas have non-trivial mesh distortion. These overlap with the areas where the tractography of arcuate fasciculus fail to overlap across species.

b) The authors also demonstrate how surface coverage affects the overlap between predicted and actual tractography in Figure 5. It is certainly evident from this figure that low surface overlap exaggerates the human/non-human discrepancy.

c) While these investigations are extremely useful but only serve to highlight that thoroughly accounting for the effect of registration errors are important. They don't cover the possibility that the areas where species actually differ and likely more prone to registration errors and thus might exaggerate or compound the changes in tract length attributable to evolution.

2) Myelin mapping. The primary measure of distinct cortical regions is the T1w/T2w ratio maps thought to reflect differences in cortical myelin. As is shown in Figure 1C (and Figure 2), these maps are largely biased towards primary cortical regions (both sensory and motor). Yet a vast majority of the temporal lobe is association cortex. How do we know that there is enough reliable myelin signal in the temporal association areas to know that the across-species alignment is accurate? How similar does the mapping look when using another measure? Could this bias towards primary regions (e.g., A1) explain why some tracts are better aligned than others?

3) Connectivity fingerprints.

Reviewer 1 was confused as to what the connectivity fingerprints are showing. Even after digging into the Materials and methods, they are still not entirely sure what they are or how the interpretations being made map to the data presented. For example, what would a null finding really look like in these results (Figure 5)? A lot more detail needs to be provided, both in the Results and Materials and methods to clarify what these are and how they can be interpreted within the context of the paper.

Reviewer 2 had a similar concern, pointing out that connectivity data and myelin maps are not fully independent features, though, but could be considered rather the one conditioning the other. In particular, from a developmental point of view, connections need to be formed before they can be myelinated. What gives pre-eminence to one modality over another?

Reviewer 3 was concerned about the nature of the alignment used to evaluate the fingerprints, pointing out that, in the subsection “Predicted Tract Maps”, the authors explain that myelin based spatial transforms are applied to the derivative tract maps after doing DWI tractography in the species-native space. Why not apply registration directly to the DWI images first and then conduct tractography itself in the human-aligned space rather than applying to derived maps? Given the novelty of this paper, it would be useful to make clear if this is a potential avenue for methodological interest. On the other hand, if there is a serious flaw with the approach I propose, it would be also useful to clarify this. I don't see any discussion of this choice.

4) Data sharing.

Reviewer 2 raised an issue of data availability as a means of expanding the impact of the current study. If it were possible, the authors may consider sharing their data more openly (not only upon request), and also sharing raw data to improve the replicability of their findings and impact on the community. The code instructions inside their shared script folder ensure reusability of the method by the community.

Furthermore, the authors may consider adding a note on the sharing status of the original data they use to their manuscript. For example, the data from the National Chimpanzee Resource, is made available upon request to W. Hopkins. Including such information would help the community and encourage re-use of valuable data resources (or to not lose their time trying to track data sources for possible re-use).

In-vivo structural and DWI Chimp data obtained from W. Hopkins, NCBR – available upon request with W. Hopkins.

Myelin maps of 29 chimps (Donahue and Glasser data) – available?

DWI data for the 5 chimps (Mars) – available?

Macaque ex-vivo structural MRI data (Mars) – available?

1 ex-vivo macaque (de Crespigny) – available?

T1w/T2w myelin maps macaque (Mars?) – available?
