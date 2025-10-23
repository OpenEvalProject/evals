# Peer review - Round 1

Editors:
- Karel Svoboda, Janelia Research Campus, Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34700.028](https://doi.org/10.7554/eLife.34700.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Chronic STED imaging reveals high turnover of dendritic spines in the hippocampus in vivo" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Karel Svoboda as the Reviewing Editor, and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal their identity: Anthony Holtmaat (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Imaging and tracking of dendritic spines in vivo poses two distinct challenges: 1. the resolution, contrast and sensitivity need to be sufficiently high to discern spines from the parent dendrite and from one another. 2. dealing with motion artifacts, which can equally degrade the resolution. The first challenge is particularly important in hippocampus, since this is a deep structure with high spine densities. The latter is usually more of an issue in neocortex because it contains a high density of large, pulsating, blood vessels. 2-photon laser scanning microscopy allows imaging dendritic microstructures over time, however its resolution is limited and may not always be sufficient to resolve/detect all spines in the hippocampus. Modeling approaches have been applied to infer dynamics and turnover based on 2P in vivo images (Attardo et al., 2015).

The authors have applied 2P-STED, a super-resolution method, to image spine dynamics in the mouse hippocampus in vivo over 4 days. They dealt with access and motion artifacts by surgically replacing the cortex with a metal cylinder. To showcase the possibilities of the microscope and prep the authors provide paired comparisons between regular 2-photon and 2-photon STED images and measurements of spines. Then they went on to show that, due to the superior resolution, spine densities are closer to the values reported in EM (used as ground truth). The spine turnover rates are higher than what was reported in a previous 2-photon imaging study with a similar preparation (Gu et al. 2014), and similar to the modeling-based measurements derived from microendoscopic images (Attardo et al. 2015).

This paper describes a proof of principle using 2P-STED in vivo and provides a first analysis of structural plasticity data. We have no major concerns as to the validity of the results or their interpretation, but suggest expanding the analysis in order to provide more details about the structure-dynamics relationships.

Major concerns:

1) The spine density reported with STED is still lower than that measured with EM. The authors should produce best-of-class STED images from fixed samples of the same mice and compare the spine densities, this would also control for possible effects of the surgery, loss of resolution in vivo etc.

2) The paper is short, but still a bit flabby. In parts it reads a bit like an infomercial for STED. The resolution advantage over 2p is obvious and should be mentioned once. The effects on measured spine density are also obvious and don't need to be belabored multiple times etc.

3) The data are under-analyzed. One of the main advantages of the current study as compared to the Attardo et al. study, is the information about spine structure (size, length, head size, neck size etc). In cortex, there are clear structure-dynamics relationships, but for hippocampus in vivo this is not known. The authors should expand their analysis into this direction and show whether such relationships between spine dynamics and spine length/size, head size etc exist.

4) The authors argue that the current data set experimentally confirms the modeling data from the Attardo et al. study. Indeed, the first 4 days of imaging suggest that the entire population of spines may be impermanent. However, due to the limited sampling rate, it is not inconceivable that the authors could not detect a more or less stable spine population. To get more insight into this, it would be interesting to analyze the survival rate of new spines, and perhaps model this to estimate the stability and turnover of the entire population. In cortex new spines tend have a half-life in the order of 2 days or so, but in the current data set they could probably live longer. This, together with the finding that about 30% of the entire population disappears over 4 days, may indeed suggest that the whole population of spines is subject to turnover (in contrast to cortex, where the turnover rates to a large extent concerns newly formed spines). The structure-dynamics relationship could also be incorporated into this model.

5) The authors need to discuss or analyze more extensively what were the critical factors in causing the quite different turnover rates between the current study and the Gu et al. paper (one of the co-authors is on both papers!). It is difficult to fathom that the different values (96% stability over 16 days in Gu et al., and 60% stability over 4 days in the current paper) were entirely due to the improved resolution or the hippocampal region. A direct comparison of turnover rates scored in 2P and 2P-STED could have possibly hinted at the underlying factors, or could have identified the type of spines that can be seen turning over in 2P-STED and not in 2P. Furthermore, they should also discuss if long-term 2P-STED could provide better data for cortex or not, given that cortex is usually more prone to movement artefacts?

6) Since this paper focuses heavily on showing the potential of in vivo 2P-STED, we suggest that the authors provide a more substantive comparison between 2P-STED and 2P images in 3D, that is by showing the image stacks that were typically used for scoring, in addition to the projections. This could be done as a figure supplement or as a new figure. This is important since spines are usually scored in 3D (as the authors do too), and resolving them in the axial dimension is most problematic – and probably still difficult in 2P-STED (as the authors comment). This might relate to the remaining difference between the reported spine densities in 2P-STED and EM.

7a) Most of the spine necks measured in 2P-STED are smaller than the PSF in 2P (as measured on beads). For example, there are spines that measure 500-700 nm in 2P, but less than 200 in 2P-STED. Wouldn't one expect the size of the smaller necks in 2P to be limited to the PSF of the microscope? Can the authors explain this phenomenon?

b) Can the authors also explain why the PSF in 2P is highly variable (the FWHM varies from ± 300-450nm)? We assume that the beads were imaged under optimal and standardized conditions. So, what causes the large variability? The PSF in the axial dimension should be presented as well, as this is the dominant factor in the difficulty to discern spines from the parent dendrite in 2P and probably also in 2P-STED.

c) Along similar lines since the PSF, it would be better to measure the PSFs on beads that are embedded in the preparation. This could change the variance and the bounds as seen in Figure 1C, as well as the relationship of the PSF to the measurements in E.

8) The authors should specify the length of dendrite that was analyzed, and provide the number of spines that were counted. For example, subsection “Dendritic spine density of CA1 pyramidal neurons in vivo”, first paragraph and subsection “Dendritic spines undergo high morphological turnover in vivo”, second paragraph.

9) The authors used a parametric test to report differences throughout. Did the authors check for normality of the data? They need to specify this.

10) All dendritic images presented in the manuscript appear saturated, which makes it difficult to judge the accuracy of spine counting and the health of dendrite.

11) The criteria used in counting spines are a bit vague. For example, in Figure 3A, day 1, spine 10 does not seem to be connected to the dendritic shaft; spine 9 seems to be a small bump from the dendritic shaft, whereas similarly-sized bumps (e.g., between spine 18 and 19) are not counted. The methods of counting need to be documented in great and quantitative detail.
