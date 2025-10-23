# Peer review - Round 1

Editors:
- Edward H Egelman, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83724.sa0](https://doi.org/10.7554/eLife.83724.sa0)

Single-particle tomography (SPT) is a useful method to determine the structure of proteins imaged in situ. This important work presents an easy-to-use tool for SPT that approximates the use of 2D tomographic projections using a ‘pseudo-subtomogram’ data structure, chosen to facilitate implementation within the existing RELION codebase. The examples shown provide solid support for the claims about the efficacy of the approach.


---

# Peer review - Round 1

Editors:
- Edward H Egelman, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83724.sa1](https://doi.org/10.7554/eLife.83724.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A Bayesian approach to single-particle electron cryo-tomography in RELION-4.0" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of Our Board of Reviewing Editors, and the evaluation has been overseen by Volker Dötsch as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Alberto Bartesaghi (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) Half the citations in the manuscript are self-references (16 out of 32!), and important/relevant work on SPT was left out and should be referenced: Himes et al., 2018 (https://doi.org/10.1038/s41592-018-0167-z), Chen et al., 2019 (https://doi.org/10.1038/s41592-019-0591-8), and Sanchez et al., 2019 (https://doi.org/10.23919/EUSIPCO.2019.8903041). Also, with the exception of their own sub-volume averaging approach [4], the vast body of work on missing-wedge compensation was not referenced in the introduction.

(2) In the section on "Orientation priors", they state that one advantage of the proposed approach is that "the coordinate system of the pseudo subtomograms themselves can be chosen arbitrarily" and that "this not only accelerates the refinement" but also "makes it possible to solve more challenging structures because fewer solutions are allowed". This advantage, however, is certainly not specific to the "pseudo-subtomogram" data representation proposed here. Indeed, this strategy was originally proposed in the context of single-particle cryo-EM by Jinag et al., 2001 (https://doi.org/10.1006/jsbi.2001.4376) and was first used for processing cryo-ET data by Forster et al., 2005 (https://doi.org/10.1073/pnas.040917810), followed by many others. This point should be contextualized and the appropriate references included.

(3) Results on the HIV-1 Gag benchmark dataset (EMPIAR-10164) have two components: (1) processing of a "standard" subset consisting of 5 tilt-series, and (2) processing of the entire dataset (43 tilt-series). As far as I know, the best reconstruction obtained using the five tilt-series is a 3.3 A map obtained using emClarity (https://www.ebi.ac.uk/emdb/EMD-13354). Since only lower resolution results obtained with NovaCTF (3.9A) and Warp (3.8A) are cited in the text, my guess is that the authors were not aware of this newer result. Given that the resolution of the emClarity map (3.3A) is similar to the one presented here (3.2A), it would be useful to compare their reconstruction against emClarity's EMD-13354 (both in terms of map features and FSC).

(4) When processing the entire dataset, a 3.0A resolution map was obtained which matches the resolution obtained by Warp/M [24]. This result, however, is "not shown" (page 5). Since this is the only benchmark dataset analyzed in this study and given that many other packages have analyzed the same data, this map should be presented together with the corresponding FSC curve, data processing details, and comparisons made against M's 3.0A EMD-11655 map.

(5) No experiments are presented to validate the ability of the approach to correct for higher-order aberrations. Since "higher-order aberration correction will probably be most useful for reconstructions that extend beyond 3A resolution", why didn't they validate their approach using one of the sub-3A cryo-ET datasets available on EMPIAR (e.g., EMPIAR-10491)?

(6) It would be useful to include a table with a summary of all the relevant data collection/data processing parameters (e.g., pixel size, detector, number of tilt-series and sub-volumes, symmetry, resolution, number of refinement rounds, etc.) for all datasets analyzed in this study.

(7) Ony the 3.8A map for the COPII inner coat has been deposited in the EMDB. All other maps and related metadata need to be deposited as well.

(8) Computational complexity is a very important topic in the context of SPT, but no details are included in the text other than the following statement: "Compared to M, RELION-4.0 uses computationally more efficient algorithms that do not require the computational power of a GPU". Does this imply that computationally inefficient algorithms require the use of GPUs? If the authors want to comment on computational complexity (which I think would be very important to do), actual numbers need to be presented, such as running times, compute resources used, storage, etc.

9) Regarding the use of a "true 2D approach" vs. "pseudo-volumes" (page 6), the following claim is made: "For example, the current implementation could be used to process pairs of tilted images, but a 2D implementation would be more efficient", does this refer to efficiency in computing terms, storage, or both? Also, the authors should comment on the storage requirements of their 3D approach. Since the pseudo-tomograms have three components (Eqs. 8-10), does this mean that they require 3x more storage compared to traditional subtomogram averaging? This would be an important practical consideration for prospective users of this tool and should be adequately discussed.

10) In general, the use of the term "particle polishing" could lead to misinterpretations since it means different things in SPA and tomography. In SPA, "polishing" refers to the analysis of intermediate vidoe frames (which also exist in tomography), but the present study doesn't consider them at all. Also, I noticed that the term "frames" is used interchangeably to refer to SPA "vidoe frames" and "particle tilts" in tomography, which adds to the confusion. For example, the term "frame alignment" is mentioned twice on page 6, but I believe the authors are really referring to "tilt image alignment" instead. This should be clarified and the terms "frame" and "tilts" should be used consistently throughout the manuscript.

(11) For the Caulobacter crescentus S-layer reconstruction, the new cryo-ET map corresponding to the inner domain of the S-layer seems to have even better resolution than the SPA reconstruction reported in the original work [26] (3.5A vs. 3.7A for EMD-10389). Since the authors say these maps are in "excellent agreement", a quantitative comparison should be included. Was the second LPS binding site visible in the 3.7A SPA map? In Figure 2d, the fit between LPS and the cryo-ET density (right-hand side) seems to be of lower quality (i.e., no density for parts of the LPS model is seen). Without having access to the maps, it is not possible to properly evaluate these results.

(12) The paper is well-written and clear, but the description of the new concepts and evaluation of the method is somewhat minimalistic. While these may not be absolutely necessary, they will facilitate better understanding by a broader user community.

(i) A graph describing the workflow as implemented in RELION, e.g., as a flow chart, would increase the readability of the paper.

(ii) A figure visually describing the pseudosubtomograms would make the concept clearer to the reader.

(iii) A more in-depth description of the input files (alignment files from imod, particle lists, and orientation from Dynamo/elsewhere) needed to perform alignments and averaging in RELION using pseudosubtomograms would be beneficial to the community. This could be incorporated into a flowchart as suggested in (i).

13) Along the same lines, the authors do not include any description of the particle-picking procedures or the software requirements. This seems to be important as the authors state "(particles) relative defoci are known from the geometry of the tilt series and the known 3D positions of the particles in the tomogram".

14) In section 2.2 it is shortly discussed that rotational priors can be used to constrain orientational searches. As this is often very useful for particle alignment in cryo-ET, this and the implementation should be described in more detail.

15) The progress in map quality is only shown by improvements to resolution in the FSC for the test datasets. It would be beneficial to also show the initial and intermediary maps for at least one of the test cases so that the reader can better assess the improvement in map quality. Overall maps should be shown to evaluate performance on the "whole particle" level, given considerations of flexibility (especially in cases where focused refinement was used). Corresponding local resolution maps would be informative in such cases.

(16) For the immature HIV capsid data, the FSC curves are only shown for the small subset of data. As it is an important point that the RELION pseudosubtomogram approach can reach the same resolution as previous software such as M, the data should also be shown for the full dataset (authors write "data not shown").

(17) In general, a proper comparison to the previous approaches/results, maybe by providing the maps for comparison in the figures, would be helpful for the reader to evaluate which approach to choose, and based on what expectations/biological system.

18) In section 4 it is briefly discussed that particle rotation is not modeled in the per-particle motion correction. They draw parallels to single particles and conclude that this might be an issue at resolutions better than 2 Å. However, could the authors comment on whether the difference in dose and time frame of data collection as well as the thickness of sample, may affect the assumption that this is only an issue at a higher resolution?

(19) Many subtomogram averages are resolved at a more moderate resolution (e.g. 8-20 Å) than the maps presented in this study due to different reasons. It would be beneficial for the reader if the authors could comment on/discuss which optical and geometrical parameters can be confidently modeled at a lower resolution and if they improve resolution.

(20) Could the authors comment on whether it is possible to extract the refined optical and geometrical parameters for a set of particles from a tilt series, and apply them to a different set of particles from the same tilt series (or to the full tilt series to obtain a better quality tomogram for new particle picking).

(21) Along the same line: would it be possible to refine two distinct species (e.g. two distinct conformations of the same protein or two completely unrelated proteins) together in a multi-species refinement of optical and geometrical parameters? As the overall tilt series alignment and imaging parameters are the same, this might aid in refinement for lower abundance.

(22) On a more conceptual level, the reasoning to separate the SPA/Cryo-ET workflows completely in the software package remains unclear to me and it would be valuable if the authors could briefly discuss this.

(23) Can the authors comment on the "The data model assumes independent Gaussian noise on the Fourier components of the cryo-EM images of individual particles" with respect to the more complex in situ data, where noise is expected to be more structured?
