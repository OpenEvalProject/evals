# Peer review - Round 1

Editors:
- Markus Meister, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71132.sa0](https://doi.org/10.7554/eLife.71132.sa0)

This rigorous computational study simulates the sampling of the visual image by cone photoreceptors in the human eye, and explains how the image content can be reconstructed from those cone signals. The authors show that a number of properties of the human retina and of human perception are predicted from these simulations. Their modeling framework also serves to unify previous treatments and invites extension to subsequent stages of visual processing.


---

# Peer review - Round 1

Editors:
- Markus Meister, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71132.sa1](https://doi.org/10.7554/eLife.71132.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "An Image Reconstruction Framework for Characterizing Early Vision" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Markus Meister as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tirin Moore as the Senior Editor.

The reviewers have discussed their comments, and the Reviewing Editor has drafted this consensus review to help you prepare a revised submission.

Essential revisions:

Main recommendations

1. Sensor model: The cone mosaic is assumed to be totally regular (a triangular array) with irregularity in cone type. What happens to reconstruction when the array is not a perfect triangular array?

2. Image statistics model: Please comment on the role of fixational eye movements during human vision. Under normal viewing conditions the retinal image doesn't hold still for the 50 ms integration time used here (line 357). In reality the image drifts so fast that any given cone looks at different image pixels every 5 ms (e.g. doi.org/10.1073/pnas.1006076107). Please discuss how this might affect the conclusions derived from an assumption of static images.

3. The natural scenes prior: This is a prominent component of the algorithm. Please elaborate how important the inclusion that prior term is for producing the results. For example:

3.1. Figures6, 7, and 8: Some supplemental comparison images with no-prior or weak-prior estimates would be helpful to visualize the effect that including the prior term has on the results presented here.

3.2. Figure 9: How important is the natural scenes prior for replicating the gratings psychophysics results? If you used just an MLE estimate, or reduced the weight on the prior term, would the results change dramatically?

4. Extrafoveal vision: At the eccentricities considered in Figure 8 the circuitry of the retina already pools over many cones. Why is a reconstruction based on differentiable cones still relevant here? Generally some more discussion of post-receptor vision would be helpful, or at least a justification for not considering it.

5. Please offer some interpretation for the visualizations produced by the Bayesian model, for example:

5.1. In Figure 6, the protanopia images have a reddish hue, and the images generated using reference methods do not.

5.2. In Figure 7, the images tend to get more speckled as light intensity decreases, which doesn't seem to match up with perception during natural vision.

5.3. In Figure 8, we might expect from human vision that chromatic saturation would increase as we move to the periphery, but the example images don't show that.

6. Relation to prior work:

6.1. Discuss how the current assumptions differ from Garrigan et al., (2010).

6.2. Discuss relation to the Plug and Play Bayesian image reconstruction and image restoration methods (e.g. doi: 10.1109/TCI.2016.2629286, doi: 10.1109/TPAMI.2021.3088914). These methods are also optimization-based MAP estimation algorithms, and are conceptually quite similar to the approach taken in the paper.

6.3. Repeatedly the results of this new approach end up consistent with earlier work that operated with simpler analysis (lines 318, 435, 522). In the discussion, please give a crisp summary of what new insights came from the more complex approach.

6.4. When introducing ideas that are part of conventional wisdom, a broader list of citations would help the reader, for example: the notion that multi-chromatic receptors are less useful in dim light (line 347); the optimal allocation of spectral types given the spectra of natural scenes (line 235 ff); the importance of prior distributions in evaluating visual system design (line 277).

Other suggestions

7. Title and elsewhere: “Early vision” is often interpreted as “everything up to V1” (see textbooks and e.g. doi.org/10.1523/JNEUROSCI.3726-05.2005). Here the signal hasn’t even emerged from the receptors. None of the post-receptoral circuitry is included, which ultimately comes to dominate visual perception. Please consider a title that is more specific to the article.

8. Figure 5:

8.1. Maybe plot all curves on the same y-scale. Could be easier to see the systematic variation.

8.2. Maybe color the symbol nearest the minimum of each function.

9. Figure7:

9.1. Please include the original images, since in those panels the reader is trying to compare image degradation (also in S5).

9.2. What if at twilight the goal is to reconstruct the gray scale image and not the RBG image? Would the reconstruction be more spatially accurate and less noisy?

10. Lines 525-533. Other species like zebrafish have a much more limited range of tasks to perform than humans. Is image reconstruction still the appropriate cost function in those cases?
