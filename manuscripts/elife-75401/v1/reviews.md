# Peer review - Round 1

Editors:
- Helen Zhou, https://ror.org/01tgyzw49 National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75401.sa0](https://doi.org/10.7554/eLife.75401.sa0)

The study presents a useful fine-grained functional parcellation map of the infant cerebral cortex. The data and methodology presented are solid. It will facilitate future research in neuroanatomy and neurodevelopment disorders.


---

# Peer review - Round 1

Editors:
- Helen Zhou, https://ror.org/01tgyzw49 National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75401.sa1](https://doi.org/10.7554/eLife.75401.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Generation of Infant-dedicated Fine-grained Functional Parcellation Maps of Cerebral Cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tamar Makin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Emma C. Robinson, PhD (Reviewer #1); Kilian M. Pohl (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Include quantitative comparisons to the HCP parcellation.

2. More data on the robustness of network clustering (e.g. binarization/averaging step and random repeat/generation step).

3. Improve discussion (e.g. accessibility to a broader audience, number of parcels, the impact of gender) and references.

4. Improve clarity and readability (methods and Figures).

Reviewer #1 (Recommendations for the authors):

As stated this is a very good paper. I think if the comparisons to the HCP and the evaluation of the robustness of the network clustering could be improved it would make a very strong eLife paper.

The biggest area for improvement is the clarity of the methods. For example, for aligning the HCP 32k_LR space via fsaverage space, which specific part of reference 53 are they referring to? Assumedly, the authors didn't use landmark registration; therefore, do they mean that they use part of the HCP pipeline to map from fsaverage to FS_LR? If so this doesn't use (53).

For the computation of the individual functional gradient density map more details need to be provided for the motivation behind using the 2nd order correlation matrix and then subsequently correlating to that. Even if it is discussed in previous adult papers this manuscript should stand alone. Some more figures of what these stages look on a cortical surface would help. Unfortunately, I can't clearly follow the process through Figure 1. The resolution of this figure could also be improved.

I also don't fully understand the methods section on 'variability between functional gradient density maps.' What are p1 and p2 here? Are they vectors generated from an image patch surrounding some location?

For section 5.7 'parcel-wise development' I don't follow the description of the efficiency calculation. What is meant be 'the AUC is calculated to represent the local efficiency to avoid the influence of local densities.' What is efficiency here? Is there a calculation for it? I don't have a clear intuition for what it means. What do you mean by 'to have an intuitive and spatiotemporally detailed view of their development'

The method for clustering should be explained. And as stated in the public response the stability of the clustering should be tested and the comparison with the HCP should be quantitatively evaluated.

Some additional points on the results: The analysis of the clustering is quite difficult to follow. Firstly, the colours of the central and peripheral visual clusters are too close. Secondly, I don't understand what is meant by 'the auditory network is distinguished at 3 months and merges into the hand sensorimotor at 6 months' perhaps some arrows would help. I'm also not clear why we have labels for 'hand' sensorimotor' and 'mouth' sensorimotor – is there a reference for this?

Figure resolution needs fixing throughout and Figure 7 needs absolute scale.

References – the paper would benefit from a more thorough citing of the international literature. Pg 19 references only a few papers that estimate resting state networks for babies and ignores:

Doria, Valentina, et al. "Emergence of resting state networks in the preterm human brain." Proceedings of the National Academy of Sciences 107.46 (2010): 20015-20020.

Fitzgibbon, Sean P., et al. “The developing Human Connectome Project (dHCP) automated resting-state functional processing framework for newborn infants.” NeuroImage 223 (2020): 117303.

The references for FLIRT are:

M. Jenkinson and S.M. Smith. A global optimisation method for robust affine registration of brain images. Medical Image Analysis, 5(2):143-156, 2001.

M. Jenkinson, P.R. Bannister, J.M. Brady, and S.M. Smith. Improved optimisation for the robust and accurate linear registration and motion correction of brain images. NeuroImage, 17(2):825-841, 2002.

Reference 48 is clearly heavily inspired by FSL's FIX and therefore FIX should be referenced.

G. Salimi-Khorshidi, G. Douaud, C.F. Beckmann, M.F. Glasser, L. Griffanti S.M. Smith.

Automatic denoising of functional MRI data: Combining independent component analysis and hierarchical fusion of classifiers. NeuroImage, 90:449-68, 2014

L. Griffanti, G. Salimi-Khorshidi, C.F. Beckmann, E.J. Auerbach, G. Douaud, C.E. Sexton, E. Zsoldos, K. Ebmeier, N. Filippini, C.E. Mackay, S. Moeller, J.G. Xu, E. Yacoub, G. Baselli, K. Ugurbil, K.L. Miller, and S.M. Smith. ICA-based artefact removal and accelerated fMRI acquisition for improved resting state network imaging. NeuroImage, 95:232-47, 2014

The citation for Melodic is also missing.

Beckmann, Christian F., and Stephen M. Smith. "Probabilistic independent component analysis for functional magnetic resonance imaging." IEEE transactions on medical imaging 23.2 (2004): 137-152.

For functionally driven cortical surface registration (pg 26) the authors should also reference MSM and other papers that have previously used spherical demons to drive functional alignment.

Robinson, E. C., K. Garcia, M. F. Glasser, Z. Chen, T. S. Coalson, A. Makropoulos, J. Bozek, R. Wright, A. Schuh, M. Webster, J. Hutter, A. Price, L. Cordero Grande, E. Hughes, N. Tusor, P. V. Bayly, D. C. Van Essen, S. M. Smith, A. D. Edwards, J. Hajnal, M. Jenkinson, B. Glocker, and D. Rueckert. 2018. "Multimodal Surface Matching with Higher-Order Smoothness Constraints." NeuroImage 167. doi:10.1016/j.neuroimage.2017.10.037.

Robinson, Emma C., Saad Jbabdi, Matthew F. Glasser, Jesper Andersson, Gregory C. Burgess, Michael P. Harms, Stephen M. Smith, David C. Van Essen, and Mark Jenkinson. 2014. "MSM: A New Flexible Framework for Multimodal Surface Matching." NeuroImage 100: 414-26. doi:10.1016/j.neuroimage.2014.05.069.

Nenning, Karl-Heinz, Hesheng Liu, Satrajit S. Ghosh, Mert R. Sabuncu, Ernst Schwartz, and Georg Langs. 2017. "Diffeomorphic Functional Brain Surface Alignment: Functional Demons." NeuroImage. Elsevier.

When discussing parcellation validation and homogeneity Arslan et al. 2018 should be cited.

Arslan, Salim, et al. "Human brain mapping: A systematic comparison of parcellation methods for the human cerebral cortex." NeuroImage 170 (2018): 5-30.

Reviewer #2 (Recommendations for the authors):

Figures: overall the figures are difficult to interpret and the caption fail to explain nomenclature and provide a take home message for the corresponding figure, i.e., figures cannot be understood without carefully reading the text. In the detail comments below – comments for one figure also apply to proceeding ones.

– Figure 1: Given the amount of detail provided, it should be moved to the supplement or method section where the individual components are then described.

– Figure 2: Instead of a)-d) it would be fantastic if one provides short heading (such as Proposed Atlas). Also, at a first glance they do not seem to have anything to do with each other (other than c and d – but then it is not clear why there are three images in d). d) might be better for the supplement as the message of Figure 2 is unclear.

– Figure 3: what is L and R, why are both hemispheres shown even though the result section does not discuss differences in hemispheres? Why are roughly 450 parcellations chosen for each hemisphere – why is that better than e.g. 600 or 300 parcellations? What is 3M … 24M referring to and which brains belong to which group? I know it is somewhere described in the text but each figure should be self-explanatory.

Figure 4 - b) is never explained in the text.

Figure 5: why are hemisphere not oriented as in other pictures?

Figure 6: chosen stability criteria seems arbitrary – why not chose max?

Point of Figure 8 is entirely unclear.

The result section lacks focus. For example, it jumps back and forth between "common" and age-related atlas. The reason for the common atlas is not made clear until the method section and Section 2.3 seems to indicate that the age-related atlas are not needed at all.

It would be helpful if the regions and networks mentioned in the text would also be pointed out in (one) figure so that the manuscript can actually be used as a self-contained reference.

Frequent use of jargon/uncommon terms: group-average functional gradient, functional gradient density maps, Temporal variabilities, the functional architecture development, "Keeping this spatial distribution".

Certain statements are not supported:

– "dice ratio reaches 0.9295 {plus minus} 0.0021 indicating the high reproducibility" – what is high and low scores for this application?

– "demonstrates that our method can well capture these important and detailed functional gradient patterns, which are usually missed by the compared methods" Output of compared method is not shown.

– how are visual areas V1, MT, MST, sensorimotor areas 2, 3, 4, auditory areas A1, LBelt, and language areas 44, 45 are defined (in infants)?

Regarding method section:

– alignment to HCP template (generated from adults) needs to be justified – is that a potential source of error/how do they relate to infant brains.

– Table 1 should be presented at beginning of the method section – can you provide % of sex in each age bracket. Also the % seems to be significantly different between age groups – how does that impact the atlas?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Infant-dedicated Fine-grained Functional Parcellation Maps of Cerebral Cortex" for further consideration by eLife. Your revised article has been evaluated by Tamar Makin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #3 (Recommendations for the authors):

I still believe that the proposed atlas could be of great importance to the field. However, the rather sloppy responses to my concerns lowers my overall enthusiasm (many issues were not responded to or they were responded to but the manuscript was not altered).

I originally stated that "Diminishing enthusiasm is the lack of focus in the result section, the frequent use of jargon, and figures that are often difficult to interpret." which still holds true.

For example, the abstract and intro was hardly edited (only expanded – see blue highlights) so that these sections (like the rest of the manuscript) are difficult to read. For example, the term "functional gradient density" is not a common term in the community (and was not even addressed in the response) and the meaning behind "age-common fine-grained parcellation maps" or "infant brain functional developmental maps" is difficult to grasp. While many of the figures improved, the take home message of Figure 2 -6 is unclear as is the reason for showing Figure 7 at all.

Parts added to the article bring up additional concerns. Table 1 clearly shows that the greater the imbalance between sexes, the greater the impact on reproducibility (up to 8% changes). The criteria for reproducibility (based on thresholding) does not seem to relate to how the functional parcellations maps are generated.

The added sentence:

"the across-age variability shows a multi-peak fluctuation, … again for 18-24 months."

might again be related to sex differences as it seems to correlate with those and are biologically not well supported.

The intuition behind null parcellations (which are not explained until much later) is missing as I assume that the measured deviations partly depend on how much the vertices are perturb (what does the x-axis in the plot of Figure 4 refer to).

The selected number of networks based on the plots in Figure 5a still seems arbitrary.

Something I missed in the initial review (I apologize) is the use of PA and AP scans. Why are they not combined before performing functional analysis to correct for spatial distortion? Why include scan sessions that do not contain both scans? How are differences across acquisition sites modeled?

Given that this is an atlas hopefully used by many other studies, a more detailed description of the demographics of each age group would be helpful. While mentioned several times, what is the web address of the atlas and are there any restrictions for downloading it?
