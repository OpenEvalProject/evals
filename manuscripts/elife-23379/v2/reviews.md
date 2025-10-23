# Peer review - Round 1

Editors:
- Didier YR Stainier, Max Planck Institute for Heart and Lung Research , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23379.028](https://doi.org/10.7554/eLife.23379.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Automated deep-phenotyping of the vertebrate brain" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Allalou et al. describe a platform that they have developed for high throughput characterisation of gene expression patterns and how they are altered in mutant zebrafish embryos and larvae. They have optimised a chromogenic in situ hybridisation protocol for optical projection tomography and developed a pipeline to register mutant and wild-type volumetric datasets to common reference brains, with anatomical annotations. The method is rigorously validated using the fezf mutant, reproducing both previously reported defects, anticipated changes that were previously overlooked (such as the loss of sst1.1 within the otp domain) and novel defects due to a change in telencephalon size. Such changes would be difficult to identify using traditional methods for mutant characterization. Methods are for the most part well described, especially the detailed protocol describing modifications to WISH. This is a powerful new method for quantitative phenotypic characterization.

Essential revisions:

1) Although the statistical technique used for automated correlation analysis (Figure 3A) is robust, the voxel-wise procedure shown in Figure 3C is not very rigorous. This is not a deal-breaker because the procedure is in any case only applied within regions already found positive using the Pearson+Whitney method. Nevertheless, strictly, the voxel-wise method used is really a sort of cluster-based technique, using arbitrary thresholds for voxel-wise significance, and cluster-size threshold. Similar methods are known to be dangerously prone to false positives (see Eklund PNAS 2016). More statistically rigorous voxel-wise analysis should be presented.

2) In several steps of the analysis, a large number of statistical tests are required to compare voxel data for numerous genes and brain regions. What was the basis for setting p value thresholds for so many comparisons?

3) Please provide more detail in support of the statement "The ability to rapidly image and align thousands of WISH-stained embryos in 3D […]". Although timings for some individual steps appears in the Methods, it would be useful to summarise in the results text the rate at which lines can be processed, imaged and registered.

4) The authors state that the registration algorithms used in other studies (e.g. CMTK, used in Randlett, 2016) are unsuitable for their WISH data. It would be informative if they could briefly comment on why this is the case.

Please make sure to submit the code and brain atlases so that they are available for download by the readers.

Also, please consider whether you would like your article to appear as a 'Tools and Resources' article or a regular one.

Suggested revisions:

The authors should offer more detailed rationale for several steps in the registration procedure; additional information in the manuscript will help inform future work by other groups. Two specific questions:

1) For each probe, one embryo (the PRF) is selected via strongest correlation to the probe-specific iterative shape average. This embryo is then registered to the URF using a rigid+affine registration (no elastic step) for the sytox channel, then other embryos registered to the PRF using deformable registration using the green channel. But with this procedure, any inaccuracy in the PRF alignment will be transmitted to all other embryos for that probe. Because initial PRF alignment is rigid+affine and not elastic, accuracy will be limited. So why is elastic registration not used for the PRF? The final registration step (subsection “Image registration”, second paragraph) is not well explained – is this rigid+affine only? How is the average wildtype created (ISA?)

2) Using the WISH pattern to drive registration to a selected wildtype embryo means all the resulting images will have low variability, but actually mask real biological variability in individual WISH patterns. The authors acknowledge this concern at the end of the manuscript – because mutant patterns are elastically aligned to a wildtype WISH pattern differences in the mutant are minimized. My understanding is that the alternate procedure in Figure 1—figure supplement 4, that avoids this problem, is only for the 2D visualization overlays in Figures 4–5, because it is obviously not suitable for statistical comparison. The more obvious procedure would be to independently align each wildtype and mutant embryo to the URF using its sytox channel, apply the transformation to the WISH channel and then perform statistical comparisons. Why was this method not used?
