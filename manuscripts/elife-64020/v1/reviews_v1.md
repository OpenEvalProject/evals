# Peer review - Round 1

Editors:
- Noriaki Emoto, Kobe Pharmaceutical University Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64020.sa1](https://doi.org/10.7554/eLife.64020.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This retrospective clinical study investigated markers of biomechanical stress and plaque rupture in diabetic patients with coronary atherosclerosis. The authors modeled arterial plaque anatomy and characteristics of arterial wall stress in patients with either stable coronary artery disease (stable CAD) or acute coronary syndrome (ACS) using optical coherence tomography (OCT) imaging. The authors identified a cut-off stress value that allows the prediction plaque rupture. The results hold potential to be used for assessment of the plaque rupture risk in patients with CAD using OCT.

Decision letter after peer review:

Thank you for submitting your article "Coronary plaque composition influences biomechanical stress and predicts plaque rupture – a morpho-mechanic OCT analysis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: José Félix Rodriguez Matas (Reviewer #2).

The reviewers have discussed the reviews with one another, and this decision letter is to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This work presents results on the finite element analysis of OCT-reconstructed plaque "3D-models" of 10 ruptured and 10 non-ruptured lesions. The manuscript is well written and structured. The results are found to be of great interest for the assessment of the plaque rupture risk in patients. The study confirms the excellent correlation between the location of the maximum stress in the arterial tissue and the location of the plaque rupture already reported by the authors in a previous study (Reith et al., Cardiovasasc Diabetol 2019; 18(1): 122). In addition, the study finds that in the ruptured lesions, the maximal stress in the fibrous cap and vessel wall were significantly higher than in the non-ruptured plaques. So, the stress concentration excellently predicts plaque rupture, underlying the importance of morpho-mechanic analysis to assess the disrupting effects of plaque stress. However, the ROC curves for the prediction of plaque rupture indicate an Optimal cut-off stress of 150kPa and 169.5kPa for the fiber cap and the plaque respectively. This threshold value is significantly lower than the threshold value of 300kPa reported in literature. The authors explain this difference through the different imaging modalities used to reconstruct the coronary plaque. However, a more plausible explanation can be found in the finite element model itself, in particular in the mechanical properties used for the analysis.

Essential revisions:

1. In the introduction the authors mention among the accepted features of plaque vulnerability: thickness of the fibrous cap, the extent of necrotic lipid core. However, recent studies also indicate the positive remodeling index, low-attenuation plaque, and plaque burden as significant markers of plaque vulnerability. I suggest to extend the literature review in this regard and to also include a recent analysis published in Eur Heart J Cardiovasc Imaging. 2017 Oct 1;18(10):1170-1178. doi: 10.1093/ehjci/jew200. PMID: 27679600.

2. Stress analysis considered an oversimplified model for the tissues. The authors make reference to rather old publications [14] 1992, [15] 1993, [16 ] 2004, [17] 2019 that do not certainly provide adequate information. The stress field, and therefore the peak stress value, will be significantly affected by the adopted mechanical model for the tissue. You are assuming the vessel wall with a Poisson's ratio of ~0.3 when in reality it is a quasi-incompressible material with a Poisson ratio ~0.5. In addition, the authors are using a value for the initial Young modulus for the calcification that is 4 orders of magnitude larger than those reported in literature. A similar observation is made for the arterial tissue, assumed as linear elastic when in reality is non-linear. Using a non-linear hyper-elastic material model for the arterial wall and the plaque will significantly affect the peak wall stress in ruptured and non-ruptured plaques and could modify the ROC curves. In conclusion, the authors should rerun the finite element analysis of all models with adequate material parameters. Please check the work by Yang et al. IEEE Trans Biomed Eng 56(10): 2420-2428 (2009), and references within to update the material parameters used in your analysis and rerun the simulations. Make sure you are using a quasi-incompressible material by imposing a Poisson's ratio of at least 0.48 in the case that a hybrid finite element formulation is not available in the software.

3. Also, the reviewers recommend including a comment regarding the choice of the frame with the minimal lumen area for stable lesions in the Section "Manual segmentation and reconstruction", just for completeness. In the case of ruptured plaques, the reviewers think that the frame immediately preceding the site of the rupture is the best choice. However, in the case of non-ruptured plaques, the choice of the frame with the minimal lumen area is the more intuitive from an engineering point of view, while from a clinical point of view it could be also interesting to assess a section with a positive remodeling, if present.

4. The 3D model was reconstructed by extruding the segmented section for a total length of 10mm. At this point, the results are equivalent to considering a plane-strain model of the plaque i.e., a 2D model. This will significantly reduce the computational cost and significantly simplify the analysis of the results. This fact is demonstrated in Suppl. Figure 3 that show the same results in sections C, D, and E, away from the end caps were boundary effects make the stress field unreliable. Finally, a convergence curve of the mesh size will be appreciated, as well as the average number of nodes and elements used for the analysis

5. Insert a comment in the limitations regarding the sample size. Twenty plaques are not a small number but maybe not sufficiently large as to completely ensure the conclusions of the manuscript. The results are very promising though.

6. Although the authors aptly analyzed the correlation between biomechanical stress and other plaque characteristics, it would be even better and more clinically applicable if the authors could combine the aforementioned factors as a single prediction tool, such as scoring system or a simplified formula to ease its application.

7. Did the authors look at the paper: "Kok AM, Speelman L, Virmani R, van der Steen AF, Gijsen FJ, Wentzel JJ. Peak cap stress calculations in coronary atherosclerotic plaques with an incomplete necrotic core geometry. Biomed Eng Online. 2016 May 4;15(1):48. doi: 10.1186/s12938-016-0162-5. PMID: 27145748; PMCID: PMC4857277."
