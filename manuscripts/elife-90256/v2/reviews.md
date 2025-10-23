# Peer review - Round 1

Editors:
- Mackenzie W Mathis, https://ror.org/02s376052 École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90256.sa0](https://doi.org/10.7554/eLife.90256.sa0)

This computational study is a valuable empirical investigation into the common trait of neurons in brains and artificial neural networks: responding effectively to both objects and their mirror images and it focuses on uncovering conditions that lead to mirror symmetry in visual networks and the evidence convincingly demonstrates that learning contributes to expanding mirror symmetry tuning, given its presence in the data. Additionally, the paper delves into the transformation of face patches in primate visual hierarchy, shifting from view specificity to mirror symmetry to view invariance. It empirically analyzes factors behind similar effects in many network architectures, and key claims highlight the emergence of invariances in architectures with spatial pooling, driven by learning bilateral symmetry discrimination and importantly, these effects extend beyond faces, suggesting broader relevance.


---

# Peer review - Round 1

Editors:
- Mackenzie W Mathis, https://ror.org/02s376052 École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90256.sa1](https://doi.org/10.7554/eLife.90256.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Emergence of brain-like mirror-symmetric viewpoint tuning in convolutional neural networks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Mackenzie Mathis as Reviewing Editor and Yanchao Bi as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

Overall we collectively found the study valuable, but requires two major revisions to significantly strengthen the work. The concerns, and thus recommendations for major revision, largely revolve around the combination of choosing two weaker architectures and not establishing any correspondence to brain data. Thus, we agree to the two following essential revisions:

1. Please broaden the architectures that are being analyzed, including at least one state-of-the-art model for the effect you are studying. We think EIG is the most natural choice. To really strengthen the paper, recommend to include ResNets (strong computer vision models and good alignment to brain data), Transformers (strong computer vision models with different building blocks which would "stress-test" their learning and max-pooling claims), and HMAX (Leibo et al. claim this explains mirror-symmetric tuning, but not sure how well it aligns to data relative to EIG and other models).

2. Please defend your current choice of architectures by testing the brain alignment of VGG/AlexNet versus the current state-of-the-art EIG. we suggest performing comparisons of model activations to brain data for recordings where the subjects viewed mirror-symmetric stimuli (e.g., neural predictivity and/or CKA), or metrics that focus more explicitly on the mirror-symmetry effects, similar to Figure 3 in the Yildirim et al. paper. The most relevant result for connecting the models under study in this paper to neural recordings is this the paper by Yildirim et al. where VGG is found to be a poorer model than their proposed EIG. Depending on the choice of metric I think it is well possible that VGG is comparable to EIG, but it's up to the authors of this manuscript to defend their choice, and to make the comparison.

Reviewer #1 (Recommendations for the authors):

1. The potential mechanisms underlying mirror-symmetric tuning have been investigated in the past as has been acknowledged and intensively discussed in the paper. However, some of the conclusions made in this paper were already made in previous work, although not explicitly tested. As stated by Leibo et al. "the Hebb-type learning rule generates mirror-symmetric tuning for bilaterally symmetric objects, like faces", suggesting that it will also allow for mirror-symmetric tuning for other object categories. It would be important to acknowledge this. Moreover, while Yildirim et al. reports mirror-symmetric viewpoint tuning in VGGFace, they find that this tuning is less present than the view-invariant identity tuning, thereby contradicting neural findings in area AL. It would be beneficial to compare mirror-symmetry with view-invariant coding (as introduced in Figure 1A) in the fully-connected layers of the CNNs in this work, or at least to discuss and acknowledge this potential mismatch of CNNs with neural data.

2. The authors propose a mirror-symmetric viewpoint tuning index, which, although innovative, complicates comparison with previous work. This index is based on correlating representational dissimilarity matrices (RDMs) with their flipped versions, a method differing from previous approaches that correlated RDMs with idealized model RDMs corresponding to mirror symmetry. The mirror-symmetric tuning reported by Yildirim et al. for VGG-raw (corresponding to VGGFace in this study; Figure S2) appears significantly lower than the current study (Figure S1). To clarify these differences, an analysis using an idealized model, as in prior studies, or to better motivate the index used in this study would be valuable.

3. The analysis of reflection equivariance vs. invariance in both trained and untrained CNNs' convolutional layers is informative. However, an illustrative figure would enhance clarity and underscore the distinction between equivariance and invariance.

4. Faces seem to behave quite differently from all other object categories tested in this study. The mirror-symmetric viewpoint tuning for faces starts very low but then achieves similar values as other categories in the fully-connected layers. Moreover, the difference between task training and between trained and untrained AlexNet is maximal for faces (Figure 4 and S2). None of these differences are discussed in the paper. Given the critical role of faces for this study, the authors should provide speculations or potential explanations for these observations.

5. The study's analysis of training task and dataset raises some questions. Some categories, such as faces, seem to depend strongly on the task/dataset compared to others (e.g. boats). Acknowledging this finding and discussing potential reasons could enhance the manuscript.

6. It is surprising that the face-trained VGGFace shows lower mirror-symmetric viewpoint tuning as VGG16 (Figure S1). What could be possible explanations for this result? Could it be due to an overfitting to natural images of faces (compared to the Basel Face model faces used in this study) of the VGGFace network? A discussion of this finding would be beneficial to the paper.

7. The authors suggest that mirror-symmetric viewpoint tuning is a stepping stone towards view invariance. However, the study lacks explicit testing that this tuning is necessary for viewpoint invariance to emerge. For instance, if one prohibits a network to learn mirror-symmetric viewpoint tuning, would it still achieve viewpoint invariance for bilaterally symmetric objects? While such an analysis might be beyond the scope of this study, it could be beneficial to discuss this as a future direction.

Reviewer #2 (Recommendations for the authors):

I believe you have all the tools available to address the major weakness with respect to model architectures: https://github.com/CNCLgithub/EIG-faces provides code for the EIG model from Yildirim et al. 2020, and this model also includes pooling and versions of it have been trained for other datasets. As far as I am aware, the EIG model is state-of-the-art for the neural data of mirror-symmetric viewpoint tuning, so applying your analyses to this model would make them a lot more relevant and general.

You could also see if more recent "standard" convents such as ResNet-50 explain the neural data at least as well as EIG and then generalize your analyses to this (and other) model(s). To make this case you would have to quantitatively compare the two models on their neural alignment (I believe the data from Yildirim's paper should be public). You might also say that AlexNet and VGG are in the same ballpark for explaining the neural data, but then you should include that analysis in the paper and in the Yildirim paper, VGG seems to fall behind EIG's neural similarity by 10-20 percent points (Figure 3 D iv and E iv).

Reviewer #3 (Recommendations for the authors):

– It would be reassuring to know that the object classes have independent measures of symmetry *on which the networks operate*. If the statements about object-class-specific symmetry came after performing the experiments, then I recommend re-writing so that those statements are interpretations.

– It would be a great contribution to the field if the authors could clarify the relationship between this work and Baek et al.'s. Can they confirm that untrained networks have mirror-tuned units? If that is not replicable, then the "emergence" framing is accurate, and one can exercise appropriate weighing of that other study. This would help the field. If learning just amplifies this symmetry (by strengthening connections of view-dependent units, for example), that is also helpful to learn.
