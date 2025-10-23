# Peer review - Round 1

Editors:
- Sam McDougle

Reviewers:
- Torgeir Moberget, University of Oslo Norway
- Maedbh King, University of California, Berkeley United States

## Review text

DOI: [10.7554/eLife.46831.023](https://doi.org/10.7554/eLife.46831.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The cerebellum is involved in processing of predictions and prediction errors in a fear conditioning paradigm" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Sam McDougle as the Reviewing Editor and Richard Ivry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Torgeir Moberget and Maedbh King.

Your submission has been favorably evaluated though several major concerns must be addressed for re-submission of the manuscript. We have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revision.

Summary:

The authors present an fMRI fear conditioning paradigm, and test the prediction that acquired responses to visual conditioning stimuli (i.e., shape images) and a paired aversive tactile unconditioned stimulus (i.e., a brief electric shock) will be observed in the cerebellum during the conditioning process, and will change predictably over the course of learning and extinction. The fMRI results appear to support these predictions, showing reliable activity in lateral regions of the cerebellum in response to the conditioning stimulus (CS+) versus a non-paired stimulus (CS-), and also in response to an omitted US following a CS+, subsequent to the acquisition of the fear association. Moreover, PPI analyses reveal learning-related connectivity patterns between the cerebellum and striate visual cortex, as well as the insula, implicating the cerebellum in a wider network of regions contributing to the conditioning process. These results in the affective domain support the broader idea that the cerebellum is a generalized predictive substrate, one that is involved in various learning domains outside of the traditionally highlighted role in motor learning.

While we see considerable value in this work in terms of expanding our conceptualization of the functional domain of the cerebellum, there are some methodological details that need to be clarified, as well as additional control analyses to support the interpretations of the imaging results, as well as further efforts in linking the current results to the literature.

Essential revisions:

1) Did the authors make a priori predictions about ROI activation? Given the work that has been done to map the cognitive cerebellum, the authors could have theorized that the activation would be elicited in "emotional" (Guell et al., 2018) or "prediction" (Moberget et al., 2014) regions of the cerebellum. Instead, their interpretations of the specific regional activations found seemed to be done a posteriori. This important distinction should be discussed. Moreover, several of the cerebellar foci reported in the current paper (Crus I, lobule VI) appear to overlap with cerebellar regions typically associated with higher cognitive function (e.g., working memory). Since the subjects quickly grasped the association between CS+ and US, and could in most cases explicitly report this afterwards, could representations of the learned associations in working memory explain the engagement of more "cognitive" cerebellar regions? In other words, if the association had been harder to detect explicitly by the subjects (e.g., by including many more conditioned stimuli with varying association levels with the US), would the authors expect the same results/regions?

2) Re: heart rate and respiration. Particularly with a fear conditioning paradigm, it could be argued that the results are vulnerable to task-related changes in heart rate, which can confound functional data. Importantly, both of these variables were measured and accounted for in the GLM. However, it would be useful to know if either one changed predictably during the acquisition and extinction phases (e.g., ramped up in anticipation of the US), so the potential for collinearity would be clearer.

3) One concern is that the PPI results (specifically the observed FC between cerebellum and occipital regions) could be driven by "bleed over" from visual cortex. The authors mention that they manually corrected the cerebellar mask but they did not provide any specific details. Given the importance of this analysis, extra care should be taken here to ensure that there is no mixture of signals. The mask could be recomputed (e.g., perhaps by regressing out signal from visual cortex like in Buckner et al. (2011) or a "buffer mask" could be created by removing voxels from both the occipital lobe + anterior cerebellum so that there is no abutting regions). One or both of these analyses used to recompute would provide assurance that the PPI results are not contaminated by bleed over.

4) One reviewer expressed concern that smoothing was done, given the high-resolution 7T data. While smoothing is common, it would be nice to know how different the (cerebellar) results come out if the data are unsmoothed.

5) Co-registration appeared to be done between the mean EPI and structural images. The EPIs were then corrected for slice timing and realigned to the first volume of the habituation phase. Were the EPIs first realigned to the "corrected" mean EPI image (the one coregistered with the anatomical image)? If not, it seems that the functional and anatomical images were not in the same space, which would be problematic. Moreover, the functional volumes were normalized to SUIT space, though it's not clear whether the mask used to do this was based only on the voxels from the corrected anatomical mask (cerebellum only) or whether it was a "functional" mask. This should be made clear in the manuscript.

6) The 8 second interval between the CS and US is much longer than what is thought to be the "effective" time scale of cerebellar learning (e.g., around 500ms in eyeblink conditioning paradigms; Schneiderman and Gormezano, 1964). The authors should discuss the choice of this particular interval, and address the discrepancy between the length of their chosen interval and the conventional understanding that there is only a small temporal window for cerebellar-driven learning to occur.

7) For the CS+>CS- contrast, was this analysis collapsed over the habituation, acquisition, and extinction phases? It would seem odd to include the habituation phase. Moreover, the acquisition and extinction phases should theoretically produce different results as well. The authors should perform this contrast over each phase separately. Moreover, it would be useful to have the CS+/CS- β results for the habituation phase (subsection “Mean β values related to each event (presentation of US, CS+, CS-, omission of US) compared to rest”) included, and those should also be included in Figure 5.
